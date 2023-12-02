# openshift
## Description
This ruleset detects the Java Mail API, which may be problematic when migrating an application to a cloud environment.
* Source of rules: https://github.com/konveyor/rulesets/tree/main/default/generated
## Violations
Number of Violations: 2
### #0 - localhost-http-00001
* Category: mandatory
* Effort: 7
* Description: Local HTTP Calls
The app is trying to access local resource by HTTP, please try to migrate the resource to cloud
* Labels: konveyor.io/source, konveyor.io/target=cloud-readiness, localhost
* Incidents
  * file:///tmp/source-code/backend-v2/src/main/java/org/jboss/examples/ticketmonster/rest/BookingService.java
      * The app is trying to access local resource by HTTP, please try to migrate the resource to cloud
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import org.ff4j.FF4j;
  4  import org.jboss.examples.ticketmonster.model.*;
  5  import org.jboss.examples.ticketmonster.orders.OrdersRequestDTO;
  6  import org.jboss.examples.ticketmonster.service.AllocatedSeats;
  7  import org.jboss.examples.ticketmonster.service.SeatAllocationService;
  8  import org.jboss.examples.ticketmonster.util.qualifier.Cancelled;
  9  import org.jboss.examples.ticketmonster.util.qualifier.Created;
 10  import org.jboss.resteasy.client.jaxrs.ResteasyClient;
 11  import org.jboss.resteasy.client.jaxrs.ResteasyClientBuilder;
 12  
 13  import javax.ejb.Stateless;
 14  import javax.enterprise.event.Event;
 15  import javax.inject.Inject;
 16  import javax.validation.ConstraintViolation;
 17  import javax.validation.ConstraintViolationException;
 18  import javax.ws.rs.*;
 19  import javax.ws.rs.client.Client;
 20  import javax.ws.rs.client.ClientBuilder;
 21  import javax.ws.rs.client.Entity;
 22  import javax.ws.rs.core.MediaType;
 23  import javax.ws.rs.core.MultivaluedHashMap;
 24  import javax.ws.rs.core.Response;
 25  import java.util.*;
 26  
 27  /**
 28   * <p>
 29   *     A JAX-RS endpoint for handling {@link Booking}s. Inherits the GET
 30   *     methods from {@link BaseEntityService}, and implements additional REST methods.
 31   * </p>
 32   *
 33   * @author Marius Bogoevici
 34   * @author Pete Muir
 35   */
 36  @Path("/bookings")
 37  /**
 38   * <p>
 39   *     This is a stateless service, we declare it as an EJB for transaction demarcation
 40   * </p>
 41   */
 42  @Stateless
 43  public class BookingService extends BaseEntityService<Booking> {
 44  
 45      @Inject
 46      SeatAllocationService seatAllocationService;
 47  
 48      @Inject
 49      FF4j ff;
 50  
 51      @Inject @Cancelled
 52      private Event<Booking> cancelledBookingEvent;
 53  
 54      @Inject @Created
 55      private Event<Booking> newBookingEvent;
 56  
 57      private String ordersServiceUri = "http://localhost:9090/rest/bookings";
 58      
 59      public BookingService() {
 60          super(Booking.class);
 61      }
 62      
 63      @DELETE
 64      public Response deleteAllBookings() {
 65      	List<Booking> bookings = getAll(new MultivaluedHashMap<String, String>());
 66      	for (Booking booking : bookings) {
 67      		deleteBooking(booking.getId());
 68      	}
 69          return Response.noContent().build();
 70      }
 71  
 72      /**
 73       * <p>
 74       * Delete a booking by id
 75       * </p>
 76       * @param id
 77       * @return
 78       */
 79      @DELETE
 80      @Path("/{id:[0-9][0-9]*}")
 81      public Response deleteBooking(@PathParam("id") Long id) {
 82          Booking booking = getEntityManager().find(Booking.class, id);
 83          if (booking == null) {
 84              return Response.status(Response.Status.NOT_FOUND).build();
 85          }
 86          getEntityManager().remove(booking);
 87          // Group together seats by section so that we can deallocate them in a group
 88          Map<Section, List<Seat>> seatsBySection = new TreeMap<Section, java.util.List<Seat>>(SectionComparator.instance());
 89          for (Ticket ticket : booking.getTickets()) {
 90              List<Seat> seats = seatsBySection.get(ticket.getSeat().getSection());
 91              if (seats == null) {
 92                  seats = new ArrayList<Seat>();
 93                  seatsBySection.put(ticket.getSeat().getSection(), seats);
 94              }
 95              seats.add(ticket.getSeat());
 96          }
 97          // Deallocate each section block
 98          for (Map.Entry<Section, List<Seat>> sectionListEntry : seatsBySection.entrySet()) {
 99              seatAllocationService.deallocateSeats( sectionListEntry.getKey(),
100                      booking.getPerformance(), sectionListEntry.getValue());
101          }
102          cancelledBookingEvent.fire(booking);
103          return Response.noContent().build();
104      }
105  
106      /**
107       * <p>
108       *   Create a booking. Data is contained in the bookingRequest object
109       * </p>
110       * @param bookingRequest
111       * @return
112       */
113      @POST
114      /**
115       * <p> Data is received in JSON format. For easy handling, it will be unmarshalled in the support
116       * {@link BookingRequest} class.
117       */
118      @Consumes(MediaType.APPLICATION_JSON)
119      public Response createBooking(BookingRequest bookingRequest) {
120          Response response = null;
121  
122          if (ff.check("orders-internal")) {
123              System.out.println("Creating internal booking");
124              response = createBookingInternal(bookingRequest);
125          }
126  
127          if (ff.check("orders-service")) {
128              if (ff.check("orders-internal")) {
129                  createSyntheticBookingOrdersService(bookingRequest);
130  
131              }
132              else {
133                  response = createBookingOrdersService(bookingRequest);
134              }
135          }
136  
137          return response;
138      }
139  
140      /**
141       * Makes a call to the Orders Service, but lets it know that this is a synthetic transaction
142       * that has already been recorded (ie, here internally) and is sent just for exercising the orders
143       * service; it should roll back or clean up and not store this tx as a real tx
144       *
145       * @param bookingRequest
146       */
147      private void createSyntheticBookingOrdersService(BookingRequest bookingRequest) {
148          System.out.println("Calling Orders Service with SYNTHETIC TX");
149          OrdersRequestDTO ordersRequest = new OrdersRequestDTO(bookingRequest, true);
150  
151          try {
152              System.out.println("Calling service: " + ordersServiceUri);
153              Response response = buildClient()
154                      .target(ordersServiceUri)
155                      .request().post(Entity.entity(ordersRequest, MediaType.APPLICATION_JSON_TYPE));
156              String sytheticResponse = response.readEntity(String.class);
157              System.out.println("Response from SYNTHETIC TX: " + sytheticResponse);
158  
```
  * file:///tmp/source-code/orders-service/src/test/java/org/ticketmonster/orders/SimpleTest.java
      * The app is trying to access local resource by HTTP, please try to migrate the resource to cloud
      * Code Snippet:
```java
  1  /**
  2   * Licensed to the Apache Software Foundation (ASF) under one or more
  3   * contributor license agreements.  See the NOTICE file distributed with
  4   * this work for additional information regarding copyright ownership.
  5   * The ASF licenses this file to You under the Apache License, Version 2.0
  6   * (the "License"); you may not use this file except in compliance with
  7   * the License.  You may obtain a copy of the License at
  8   * <p>
  9   * http://www.apache.org/licenses/LICENSE-2.0
 10   * <p>
 11   * Unless required by applicable law or agreed to in writing, software
 12   * distributed under the License is distributed on an "AS IS" BASIS,
 13   * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 14   * See the License for the specific language governing permissions and
 15   * limitations under the License.
 16   */
 17  package org.ticketmonster.orders;
 18  
 19  import org.junit.Test;
 20  import org.junit.runner.RunWith;
 21  import org.springframework.beans.factory.annotation.Autowired;
 22  import org.springframework.boot.context.embedded.LocalServerPort;
 23  import org.springframework.boot.test.context.SpringBootTest;
 24  import org.springframework.boot.test.web.client.TestRestTemplate;
 25  import org.springframework.http.*;
 26  import org.springframework.test.context.junit4.SpringRunner;
 27  
 28  import java.io.IOException;
 29  import java.net.URISyntaxException;
 30  
 31  import static org.junit.Assert.assertTrue;
 32  
 33  /**
 34   * Created by ceposta 
 35   * <a href="http://christianposta.com/blog>http://christianposta.com/blog</a>.
 36   */
 37  @RunWith(SpringRunner.class)
 38  @SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
 39  public class SimpleTest {
 40  
 41      @Autowired
 42      private TestRestTemplate restTemplate;
 43  
 44      @LocalServerPort
 45      int port;
 46  
 47      @Test
 48      public void testSimple() throws URISyntaxException, IOException {
 49          System.out.println("Local server port: http://localhost:" + port);
 50  
 51          String postBodyJson = "{\"ticketRequests\":[{\"ticketPrice\":4,\"quantity\":3}],\"email\":\"foo@bar.coom\",\"performance\":1}";
 52  
 53          HttpHeaders headers = new HttpHeaders();
 54          headers.setContentType(MediaType.APPLICATION_JSON);
 55  
 56  
 57          HttpEntity<String> entity = new HttpEntity<String>(postBodyJson ,headers);
 58          ResponseEntity<String> responseEntity  = restTemplate.exchange("/rest/bookings", HttpMethod.POST, entity, String.class);
 59  
 60  
 61          String response = responseEntity.getBody();
 62          assertTrue(response.contains("tickets"));
 63          System.out.println("Response: " + response);
 64      }
 65  }

```
### #1 - localhost-jdbc-00002
* Category: mandatory
* Effort: 7
* Description: Local JDBC Calls
The app is trying to access local resource by JDBC, please try to migrate the resource to cloud
* Labels: konveyor.io/source, konveyor.io/target=cloud-readiness, localhost
* Incidents
  * file:///tmp/source-code/orders-service/src/main/resources/application-mysql.properties
      * The app is trying to access local resource by JDBC, please try to migrate the resource to cloud
      * Code Snippet:
```java
  1  spring.datasource.legacyDS.url=jdbc:mysql://localhost:3306/ticketmonster?useSSL=false
  2  spring.datasource.legacyDS.username=ticket
  3  spring.datasource.legacyDS.password=monster
  4  spring.datasource.legacyDS.driverClassName=com.mysql.jdbc.Driver
  5  
  6  spring.datasource.ordersDS.url=jdbc:mysql://localhost:3306/orders?useSSL=false
  7  spring.datasource.ordersDS.username=ticket
  8  spring.datasource.ordersDS.password=monster
  9  spring.datasource.ordersDS.driverClassName=com.mysql.jdbc.Driver
 10  
 11  spring.jpa.hibernate.ddl-auto=none
 12  spring.jpa.properties.hibernate.dialect=org.teiid.dialect.TeiidDialect
 13  #spring.jpa.database-platform=org.teiid.dialect.TeiidDialect
 14  
 15  
 16  spring.teiid.model.package=org.ticketmonster.orders.domain

```
  * file:///tmp/source-code/orders-service/src/main/resources/application-mysql.properties
      * The app is trying to access local resource by JDBC, please try to migrate the resource to cloud
      * Code Snippet:
```java
  1  spring.datasource.legacyDS.url=jdbc:mysql://localhost:3306/ticketmonster?useSSL=false
  2  spring.datasource.legacyDS.username=ticket
  3  spring.datasource.legacyDS.password=monster
  4  spring.datasource.legacyDS.driverClassName=com.mysql.jdbc.Driver
  5  
  6  spring.datasource.ordersDS.url=jdbc:mysql://localhost:3306/orders?useSSL=false
  7  spring.datasource.ordersDS.username=ticket
  8  spring.datasource.ordersDS.password=monster
  9  spring.datasource.ordersDS.driverClassName=com.mysql.jdbc.Driver
 10  
 11  spring.jpa.hibernate.ddl-auto=none
 12  spring.jpa.properties.hibernate.dialect=org.teiid.dialect.TeiidDialect
 13  #spring.jpa.database-platform=org.teiid.dialect.TeiidDialect
 14  
 15  
 16  spring.teiid.model.package=org.ticketmonster.orders.domain

```
  * file:///tmp/source-code/orders-service/target/classes/application-mysql.properties
      * The app is trying to access local resource by JDBC, please try to migrate the resource to cloud
      * Code Snippet:
```java
  1  spring.datasource.legacyDS.url=jdbc:mysql://localhost:3306/ticketmonster?useSSL=false
  2  spring.datasource.legacyDS.username=ticket
  3  spring.datasource.legacyDS.password=monster
  4  spring.datasource.legacyDS.driverClassName=com.mysql.jdbc.Driver
  5  
  6  spring.datasource.ordersDS.url=jdbc:mysql://localhost:3306/orders?useSSL=false
  7  spring.datasource.ordersDS.username=ticket
  8  spring.datasource.ordersDS.password=monster
  9  spring.datasource.ordersDS.driverClassName=com.mysql.jdbc.Driver
 10  
 11  spring.jpa.hibernate.ddl-auto=none
 12  spring.jpa.properties.hibernate.dialect=org.teiid.dialect.TeiidDialect
 13  #spring.jpa.database-platform=org.teiid.dialect.TeiidDialect
 14  
 15  
 16  spring.teiid.model.package=org.ticketmonster.orders.domain

```
  * file:///tmp/source-code/orders-service/target/classes/application-mysql.properties
      * The app is trying to access local resource by JDBC, please try to migrate the resource to cloud
      * Code Snippet:
```java
  1  spring.datasource.legacyDS.url=jdbc:mysql://localhost:3306/ticketmonster?useSSL=false
  2  spring.datasource.legacyDS.username=ticket
  3  spring.datasource.legacyDS.password=monster
  4  spring.datasource.legacyDS.driverClassName=com.mysql.jdbc.Driver
  5  
  6  spring.datasource.ordersDS.url=jdbc:mysql://localhost:3306/orders?useSSL=false
  7  spring.datasource.ordersDS.username=ticket
  8  spring.datasource.ordersDS.password=monster
  9  spring.datasource.ordersDS.driverClassName=com.mysql.jdbc.Driver
 10  
 11  spring.jpa.hibernate.ddl-auto=none
 12  spring.jpa.properties.hibernate.dialect=org.teiid.dialect.TeiidDialect
 13  #spring.jpa.database-platform=org.teiid.dialect.TeiidDialect
 14  
 15  
 16  spring.teiid.model.package=org.ticketmonster.orders.domain

```
