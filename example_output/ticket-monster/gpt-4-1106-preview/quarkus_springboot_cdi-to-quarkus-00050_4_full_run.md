## Prompt:
You are an excellent enterprise architect who has an extensive
background in helping companies rewrite their legacy Java EE applications to 
Quarkus.  Your task is to examine a code snippet from a legacy Java EE application and 
generate correct and proper code changes to update the application to use Quarkus.

You will be give:
1. The source code snippet to update, 'Source Code to Update'
2. A hint of what needs to be updated via a 'Description' and a 'Message'
3. Optionally, a working example of a diff of a similar problem that was solved which we will call a 'Solved Problem'

## 'Source Code to Update'
Source code filename ``` backend-v1/src/main/java/org/jboss/examples/ticketmonster/rest/BookingEndpoint.java ``` is:
```
package org.jboss.examples.ticketmonster.rest;

import java.util.ArrayList;
import java.util.List;

import javax.ejb.Stateless;
import javax.persistence.EntityManager;
import javax.persistence.NoResultException;
import javax.persistence.OptimisticLockException;
import javax.persistence.PersistenceContext;
import javax.persistence.TypedQuery;
import javax.ws.rs.Consumes;
import javax.ws.rs.DELETE;
import javax.ws.rs.GET;
import javax.ws.rs.POST;
import javax.ws.rs.PUT;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.QueryParam;
import javax.ws.rs.core.Response;
import javax.ws.rs.core.Response.Status;
import javax.ws.rs.core.UriBuilder;
import org.jboss.examples.ticketmonster.rest.dto.BookingDTO;
import org.jboss.examples.ticketmonster.model.Booking;

/**
 * 
 */
@Stateless
@Path("forge/bookings")
public class BookingEndpoint
{
   @PersistenceContext(unitName = "primary")
   private EntityManager em;

   @POST
   @Consumes("application/json")
   public Response create(BookingDTO dto)
   {
      Booking entity = dto.fromDTO(null, em);
      em.persist(entity);
      return Response.created(UriBuilder.fromResource(BookingEndpoint.class).path(String.valueOf(entity.getId())).build()).build();
   }

   @DELETE
   @Path("/{id:[0-9][0-9]*}")
   public Response deleteById(@PathParam("id") Long id)
   {
      Booking entity = em.find(Booking.class, id);
      if (entity == null)
      {
         return Response.status(Status.NOT_FOUND).build();
      }
      em.remove(entity);
      return Response.noContent().build();
   }

   @GET
   @Path("/{id:[0-9][0-9]*}")
   @Produces("application/json")
   public Response findById(@PathParam("id") Long id)
   {
      TypedQuery<Booking> findByIdQuery = em.createQuery("SELECT DISTINCT b FROM Booking b LEFT JOIN FETCH b.tickets LEFT JOIN FETCH b.performance WHERE b.id = :entityId ORDER BY b.id", Booking.class);
      findByIdQuery.setParameter("entityId", id);
      Booking entity;
      try
      {
         entity = findByIdQuery.getSingleResult();
      }
      catch (NoResultException nre)
      {
         entity = null;
      }
      if (entity == null)
      {
         return Response.status(Status.NOT_FOUND).build();
      }
      BookingDTO dto = new BookingDTO(entity);
      return Response.ok(dto).build();
   }

   @GET
   @Produces("application/json")
   public List<BookingDTO> listAll(@QueryParam("start") Integer startPosition, @QueryParam("max") Integer maxResult)
   {
      TypedQuery<Booking> findAllQuery = em.createQuery("SELECT DISTINCT b FROM Booking b LEFT JOIN FETCH b.tickets LEFT JOIN FETCH b.performance ORDER BY b.id", Booking.class);
      if (startPosition != null)
      {
         findAllQuery.setFirstResult(startPosition);
      }
      if (maxResult != null)
      {
         findAllQuery.setMaxResults(maxResult);
      }
      final List<Booking> searchResults = findAllQuery.getResultList();
      final List<BookingDTO> results = new ArrayList<BookingDTO>();
      for (Booking searchResult : searchResults)
      {
         BookingDTO dto = new BookingDTO(searchResult);
         results.add(dto);
      }
      return results;
   }

   @PUT
   @Path("/{id:[0-9][0-9]*}")
   @Consumes("application/json")
   public Response update(@PathParam("id") Long id, BookingDTO dto)
   {
      TypedQuery<Booking> findByIdQuery = em.createQuery("SELECT DISTINCT b FROM Booking b LEFT JOIN FETCH b.tickets LEFT JOIN FETCH b.performance WHERE b.id = :entityId ORDER BY b.id", Booking.class);
      findByIdQuery.setParameter("entityId", id);
      Booking entity;
      try
      {
         entity = findByIdQuery.getSingleResult();
      }
      catch (NoResultException nre)
      {
         entity = null;
      }
      entity = dto.fromDTO(entity, em);
      try
      {
         entity = em.merge(entity);
      }
      catch (OptimisticLockException e)
      {
         return Response.status(Response.Status.CONFLICT).entity(e.getEntity()).build();
      }
      return Response.noContent().build();
   }
}

```

## Static Code Analysis Information:

You will be given information from a static code analysis tool which has assessed the 
Java EE application's suitability for adopting Quarkus and will highlight key issues it has found.

You will examine this analysis information and strongly consider it as an important 
issue we need to address when we rewrite the source code to Quarkus

### 'Description' of the problem: 
```
Stateless annotation can be replaced with scope
Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
```

### 'Message' related to the issue we need to solve
```
Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
```

### 'Solved Problem'
The 'Solved Problem' will be presented as a diff from a git repo in a branch that has
the solved updates so the application can use Quarkus. Note that the solved problem is 
for a different application to our target application, but the application may have similiarities.
Pay attention to how the example was solved if it is present, we want to follow a similar 
pattern adapted to our specific source file.

The filename for the 'Solved Example Problem' is:
```
backend-v1/src/main/java/org/jboss/examples/ticketmonster/rest/BookingService.java
```

The diff for the 'Solved Example Problem Diff' is:
```
None
```


## Instructions
Your job is to look at the 'Solved Example Problem Diff' and update it to work correctly with Quarkus,
following the best information you know of Quarkus.  Use the static code analysis information we share 
here, and study how the prior example was solved if present.  Read the 'Solved Example Problem Diff'
and and determine if a similar pattern can be applied to the 'Source Code to Update'.

Think through the changes you will make and explain each step of the process and why you think it is needed.
If you are unsure of what changes is needed please state you are unsure and ask 
for clarification to help you.


When you are done explaining the reasoning for each change, write the updated 
Quarkus source code for the 'Source Code to Update' in the form of a diff
in Markdown format as the below:

## Result
```diff
 ...
```

Write the reasoning you have for each change in the Markdown header for '##Reasoning'
Write the source code changes you have made in the form of a 'diff' under the Markdown header for '##Result'



## Result:
## Reasoning

The static code analysis information indicates that the `@Stateless` annotation from Java EE can be replaced with a CDI scope annotation such as `@ApplicationScoped` when migrating to Quarkus. This is because Quarkus is based on CDI (Contexts and Dependency Injection) and does not support the traditional EJB model. By using `@ApplicationScoped`, we define that there will be a single instance of the bean for the duration of the application lifecycle, which is a suitable replacement for the stateless session bean in many cases.

Additionally, we need to ensure that the `EntityManager` is properly injected in a CDI-compatible manner. In Quarkus, we typically use `@PersistenceContext` to inject an `EntityManager` in a JPA application. However, Quarkus prefers constructor injection over field injection for better testability and cleaner code, so we will update the code to use constructor injection for the `EntityManager`.

Since there is no 'Solved Example Problem Diff' provided, we will proceed with the changes based on the static code analysis information and best practices for Quarkus.

## Result
```diff
package org.jboss.examples.ticketmonster.rest;

import java.util.ArrayList;
import java.util.List;

-import javax.ejb.Stateless;
+import javax.enterprise.context.ApplicationScoped;
import javax.persistence.EntityManager;
import javax.persistence.NoResultException;
import javax.persistence.OptimisticLockException;
-import javax.persistence.PersistenceContext;
import javax.persistence.TypedQuery;
import javax.ws.rs.Consumes;
import javax.ws.rs.DELETE;
import javax.ws.rs.GET;
import javax.ws.rs.POST;
import javax.ws.rs.PUT;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.QueryParam;
import javax.ws.rs.core.Response;
import javax.ws.rs.core.Response.Status;
import javax.ws.rs.core.UriBuilder;
import org.jboss.examples.ticketmonster.rest.dto.BookingDTO;
import org.jboss.examples.ticketmonster.model.Booking;

/**
 * 
 */
-@Stateless
+@ApplicationScoped
@Path("forge/bookings")
public class BookingEndpoint
{
-   @PersistenceContext(unitName = "primary")
-   private EntityManager em;
+   private final EntityManager em;

+   // Constructor for injecting the EntityManager
+   @Inject
+   public BookingEndpoint(EntityManager em) {
+       this.em = em;
+   }

   @POST
   @Consumes("application/json")
   public Response create(BookingDTO dto)
   {
      // ... method implementation remains unchanged ...
   }

   // ... other methods remain unchanged ...
}
```

In the diff above, we have made the following changes:

1. Replaced the `@Stateless` annotation with `@ApplicationScoped` to indicate that the bean should be application-scoped in the CDI context.
2. Removed the `@PersistenceContext` annotation and changed the `EntityManager` injection to constructor injection. This is a preferred method in CDI and Quarkus for better testability and cleaner code.
3. Added an `@Inject` annotation to the constructor to indicate that the `EntityManager` should be injected by the CDI container.

These changes should make the `BookingEndpoint` class compatible with Quarkus, replacing the legacy Java EE patterns with CDI-based patterns.

