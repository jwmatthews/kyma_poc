# eap8/eap7
## Description
This ruleset provides rules to support the migration to hibernate search 6.0. Developed under WINDUPRULE-900
* Source of rules: https://github.com/konveyor/rulesets/tree/main/default/generated
* Sample application: https://github.com/deewhyweb/eap-coolstore-monolith
## Violations
Number of Violations: 2
### #0 - javax-to-jakarta-dependencies-00004
* Category: mandatory
* Effort: 1
* Description: javax.activation groupId has been replaced by jakarta.activation
Replace dependency groupId `javax.activation` with `jakarta.activation`
* Labels: konveyor.io/target=jakarta-ee9+, konveyor.io/target=jakarta-ee, konveyor.io/target=eap8, konveyor.io/target=eap, konveyor.io/source
* Links
  * Jakarta EE: https://jakarta.ee/
* Incidents
  * file:///opt/input/source/pom.xml
      * Replace dependency groupId `javax.activation` with `jakarta.activation`
### #1 - javax-to-jakarta-import-00001
* Category: mandatory
* Effort: 1
* Description: javax.{renamed} has been replaced by jakarta.{renamed}

* Labels: konveyor.io/target=jakarta-ee9+, konveyor.io/target=jakarta-ee, konveyor.io/target=eap8, konveyor.io/target=eap, konveyor.io/source
* Incidents
  * file:///opt/input/source/src/main/java/io/konveyor/demo/ordermanagement/OrderManagementAppInitializer.java
      * Replace the `javax.servlet` import statement with `jakarta.servlet`
      * Code Snippet:
```java
  1  package io.konveyor.demo.ordermanagement;
  2  
  3  import javax.servlet.ServletContext;
  4  import javax.servlet.ServletException;
  5  import javax.servlet.ServletRegistration;
  6  
  7  import org.springframework.web.WebApplicationInitializer;
  8  import org.springframework.web.context.ContextLoaderListener;
  9  import org.springframework.web.context.support.AnnotationConfigWebApplicationContext;
 10  import org.springframework.web.servlet.DispatcherServlet;
 11  
 12  
 13  public class OrderManagementAppInitializer implements WebApplicationInitializer  {
 14  
 15  	@Override
 16  	public void onStartup(ServletContext container) throws ServletException {
 17  		AnnotationConfigWebApplicationContext context = new AnnotationConfigWebApplicationContext();
 18        context.setConfigLocation("io.konveyor.demo.ordermanagement.config");
 19  
 20        context.scan("io.konveyor.demo.ordermanagement");
 21        container.addListener(new ContextLoaderListener(context));
 22  
 23        ServletRegistration.Dynamic dispatcher = container
 24          .addServlet("dispatcher", new DispatcherServlet(context));
 25        
 26        dispatcher.setLoadOnStartup(1);
 27        dispatcher.addMapping("/");
 28  		
 29  	}
 30  
 31  }

```
  * file:///opt/input/source/src/main/java/io/konveyor/demo/ordermanagement/OrderManagementAppInitializer.java
      * Replace the `javax.servlet` import statement with `jakarta.servlet`
      * Code Snippet:
```java
  1  package io.konveyor.demo.ordermanagement;
  2  
  3  import javax.servlet.ServletContext;
  4  import javax.servlet.ServletException;
  5  import javax.servlet.ServletRegistration;
  6  
  7  import org.springframework.web.WebApplicationInitializer;
  8  import org.springframework.web.context.ContextLoaderListener;
  9  import org.springframework.web.context.support.AnnotationConfigWebApplicationContext;
 10  import org.springframework.web.servlet.DispatcherServlet;
 11  
 12  
 13  public class OrderManagementAppInitializer implements WebApplicationInitializer  {
 14  
 15  	@Override
 16  	public void onStartup(ServletContext container) throws ServletException {
 17  		AnnotationConfigWebApplicationContext context = new AnnotationConfigWebApplicationContext();
 18        context.setConfigLocation("io.konveyor.demo.ordermanagement.config");
 19  
 20        context.scan("io.konveyor.demo.ordermanagement");
 21        container.addListener(new ContextLoaderListener(context));
 22  
 23        ServletRegistration.Dynamic dispatcher = container
 24          .addServlet("dispatcher", new DispatcherServlet(context));
 25        
 26        dispatcher.setLoadOnStartup(1);
 27        dispatcher.addMapping("/");
 28  		
 29  	}
 30  
 31  }

```
  * file:///opt/input/source/src/main/java/io/konveyor/demo/ordermanagement/OrderManagementAppInitializer.java
      * Replace the `javax.servlet` import statement with `jakarta.servlet`
      * Code Snippet:
```java
  1  package io.konveyor.demo.ordermanagement;
  2  
  3  import javax.servlet.ServletContext;
  4  import javax.servlet.ServletException;
  5  import javax.servlet.ServletRegistration;
  6  
  7  import org.springframework.web.WebApplicationInitializer;
  8  import org.springframework.web.context.ContextLoaderListener;
  9  import org.springframework.web.context.support.AnnotationConfigWebApplicationContext;
 10  import org.springframework.web.servlet.DispatcherServlet;
 11  
 12  
 13  public class OrderManagementAppInitializer implements WebApplicationInitializer  {
 14  
 15  	@Override
 16  	public void onStartup(ServletContext container) throws ServletException {
 17  		AnnotationConfigWebApplicationContext context = new AnnotationConfigWebApplicationContext();
 18        context.setConfigLocation("io.konveyor.demo.ordermanagement.config");
 19  
 20        context.scan("io.konveyor.demo.ordermanagement");
 21        container.addListener(new ContextLoaderListener(context));
 22  
 23        ServletRegistration.Dynamic dispatcher = container
 24          .addServlet("dispatcher", new DispatcherServlet(context));
 25        
 26        dispatcher.setLoadOnStartup(1);
 27        dispatcher.addMapping("/");
 28  		
 29  	}
 30  
 31  }

```
  * file:///opt/input/source/src/main/java/io/konveyor/demo/ordermanagement/model/Customer.java
      * Replace the `javax.persistence` import statement with `jakarta.persistence`
      * Code Snippet:
```java
  1  package io.konveyor.demo.ordermanagement.model;
  2  
  3  import javax.persistence.Column;
  4  import javax.persistence.Entity;
  5  import javax.persistence.GeneratedValue;
  6  import javax.persistence.GenerationType;
  7  import javax.persistence.Id;
  8  import javax.persistence.SequenceGenerator;
  9  import javax.persistence.Table;
 10  
 11  @Entity
 12  @Table(name = "customers")
 13  public class Customer {
 14  	@Id
 15      @SequenceGenerator(
 16              name = "customersSequence",
 17              sequenceName = "customers_id_seq",
 18              allocationSize = 1,
 19              initialValue = 6)
 20      @GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "customersSequence")
 21  	private Long id;
 22  	
 23  	@Column(length = 20)
 24  	private String username;
 25  	
 26  	@Column(length = 20)
 27  	private String name;
 28  	
 29  	@Column(length = 40)
 30  	private String surname;
 31  	
 32  	@Column(length = 250)
 33  	private String address;
 34  	
 35  	@Column(name = "zipcode", length = 10)
 36  	private String zipCode;
 37  	
 38  	@Column(length = 40)
 39  	private String city;
 40  	
 41  	@Column(length = 40)
 42  	private String country;
 43  	
 44  	public Long getId() {
 45  		return id;
 46  	}
 47  	public void setId(Long id) {
 48  		this.id = id;
 49  	}
 50  	public String getUsername() {
 51  		return username;
 52  	}
 53  	public void setUsername(String username) {
 54  		this.username = username;
 55  	}
 56  	public String getName() {
 57  		return name;
 58  	}
 59  	public void setName(String name) {
 60  		this.name = name;
 61  	}
 62  	public String getSurname() {
 63  		return surname;
 64  	}
 65  	public void setSurname(String surname) {
 66  		this.surname = surname;
 67  	}
 68  	public String getAddress() {
 69  		return address;
 70  	}
 71  	public void setAddress(String address) {
 72  		this.address = address;
 73  	}
 74  	public String getZipCode() {
 75  		return zipCode;
 76  	}
 77  	public void setZipCode(String zipCode) {
 78  		this.zipCode = zipCode;
 79  	}
 80  	public String getCity() {
 81  		return city;
 82  	}
 83  	public void setCity(String city) {
 84  		this.city = city;
 85  	}
 86  	public String getCountry() {
 87  		return country;
 88  	}
 89  	public void setCountry(String country) {
 90  		this.country = country;
 91  	}
 92  	
 93  	@Override
 94  	public String toString() {
 95  		return "Customer [id=" + id + ", username=" + username + ", name=" + name + ", surname=" + surname
 96  				+ ", address=" + address + ", zipCode=" + zipCode + ", city=" + city + ", country=" + country + "]";
 97  	}
 98  }

```
  * file:///opt/input/source/src/main/java/io/konveyor/demo/ordermanagement/model/Customer.java
      * Replace the `javax.persistence` import statement with `jakarta.persistence`
      * Code Snippet:
```java
  1  package io.konveyor.demo.ordermanagement.model;
  2  
  3  import javax.persistence.Column;
  4  import javax.persistence.Entity;
  5  import javax.persistence.GeneratedValue;
  6  import javax.persistence.GenerationType;
  7  import javax.persistence.Id;
  8  import javax.persistence.SequenceGenerator;
  9  import javax.persistence.Table;
 10  
 11  @Entity
 12  @Table(name = "customers")
 13  public class Customer {
 14  	@Id
 15      @SequenceGenerator(
 16              name = "customersSequence",
 17              sequenceName = "customers_id_seq",
 18              allocationSize = 1,
 19              initialValue = 6)
 20      @GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "customersSequence")
 21  	private Long id;
 22  	
 23  	@Column(length = 20)
 24  	private String username;
 25  	
 26  	@Column(length = 20)
 27  	private String name;
 28  	
 29  	@Column(length = 40)
 30  	private String surname;
 31  	
 32  	@Column(length = 250)
 33  	private String address;
 34  	
 35  	@Column(name = "zipcode", length = 10)
 36  	private String zipCode;
 37  	
 38  	@Column(length = 40)
 39  	private String city;
 40  	
 41  	@Column(length = 40)
 42  	private String country;
 43  	
 44  	public Long getId() {
 45  		return id;
 46  	}
 47  	public void setId(Long id) {
 48  		this.id = id;
 49  	}
 50  	public String getUsername() {
 51  		return username;
 52  	}
 53  	public void setUsername(String username) {
 54  		this.username = username;
 55  	}
 56  	public String getName() {
 57  		return name;
 58  	}
 59  	public void setName(String name) {
 60  		this.name = name;
 61  	}
 62  	public String getSurname() {
 63  		return surname;
 64  	}
 65  	public void setSurname(String surname) {
 66  		this.surname = surname;
 67  	}
 68  	public String getAddress() {
 69  		return address;
 70  	}
 71  	public void setAddress(String address) {
 72  		this.address = address;
 73  	}
 74  	public String getZipCode() {
 75  		return zipCode;
 76  	}
 77  	public void setZipCode(String zipCode) {
 78  		this.zipCode = zipCode;
 79  	}
 80  	public String getCity() {
 81  		return city;
 82  	}
 83  	public void setCity(String city) {
 84  		this.city = city;
 85  	}
 86  	public String getCountry() {
 87  		return country;
 88  	}
 89  	public void setCountry(String country) {
 90  		this.country = country;
 91  	}
 92  	
 93  	@Override
 94  	public String toString() {
 95  		return "Customer [id=" + id + ", username=" + username + ", name=" + name + ", surname=" + surname
 96  				+ ", address=" + address + ", zipCode=" + zipCode + ", city=" + city + ", country=" + country + "]";
 97  	}
 98  }

```
  * file:///opt/input/source/src/main/java/io/konveyor/demo/ordermanagement/model/Customer.java
      * Replace the `javax.persistence` import statement with `jakarta.persistence`
      * Code Snippet:
```java
  1  package io.konveyor.demo.ordermanagement.model;
  2  
  3  import javax.persistence.Column;
  4  import javax.persistence.Entity;
  5  import javax.persistence.GeneratedValue;
  6  import javax.persistence.GenerationType;
  7  import javax.persistence.Id;
  8  import javax.persistence.SequenceGenerator;
  9  import javax.persistence.Table;
 10  
 11  @Entity
 12  @Table(name = "customers")
 13  public class Customer {
 14  	@Id
 15      @SequenceGenerator(
 16              name = "customersSequence",
 17              sequenceName = "customers_id_seq",
 18              allocationSize = 1,
 19              initialValue = 6)
 20      @GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "customersSequence")
 21  	private Long id;
 22  	
 23  	@Column(length = 20)
 24  	private String username;
 25  	
 26  	@Column(length = 20)
 27  	private String name;
 28  	
 29  	@Column(length = 40)
 30  	private String surname;
 31  	
 32  	@Column(length = 250)
 33  	private String address;
 34  	
 35  	@Column(name = "zipcode", length = 10)
 36  	private String zipCode;
 37  	
 38  	@Column(length = 40)
 39  	private String city;
 40  	
 41  	@Column(length = 40)
 42  	private String country;
 43  	
 44  	public Long getId() {
 45  		return id;
 46  	}
 47  	public void setId(Long id) {
 48  		this.id = id;
 49  	}
 50  	public String getUsername() {
 51  		return username;
 52  	}
 53  	public void setUsername(String username) {
 54  		this.username = username;
 55  	}
 56  	public String getName() {
 57  		return name;
 58  	}
 59  	public void setName(String name) {
 60  		this.name = name;
 61  	}
 62  	public String getSurname() {
 63  		return surname;
 64  	}
 65  	public void setSurname(String surname) {
 66  		this.surname = surname;
 67  	}
 68  	public String getAddress() {
 69  		return address;
 70  	}
 71  	public void setAddress(String address) {
 72  		this.address = address;
 73  	}
 74  	public String getZipCode() {
 75  		return zipCode;
 76  	}
 77  	public void setZipCode(String zipCode) {
 78  		this.zipCode = zipCode;
 79  	}
 80  	public String getCity() {
 81  		return city;
 82  	}
 83  	public void setCity(String city) {
 84  		this.city = city;
 85  	}
 86  	public String getCountry() {
 87  		return country;
 88  	}
 89  	public void setCountry(String country) {
 90  		this.country = country;
 91  	}
 92  	
 93  	@Override
 94  	public String toString() {
 95  		return "Customer [id=" + id + ", username=" + username + ", name=" + name + ", surname=" + surname
 96  				+ ", address=" + address + ", zipCode=" + zipCode + ", city=" + city + ", country=" + country + "]";
 97  	}
 98  }

```
  * file:///opt/input/source/src/main/java/io/konveyor/demo/ordermanagement/model/Customer.java
      * Replace the `javax.persistence` import statement with `jakarta.persistence`
      * Code Snippet:
```java
  1  package io.konveyor.demo.ordermanagement.model;
  2  
  3  import javax.persistence.Column;
  4  import javax.persistence.Entity;
  5  import javax.persistence.GeneratedValue;
  6  import javax.persistence.GenerationType;
  7  import javax.persistence.Id;
  8  import javax.persistence.SequenceGenerator;
  9  import javax.persistence.Table;
 10  
 11  @Entity
 12  @Table(name = "customers")
 13  public class Customer {
 14  	@Id
 15      @SequenceGenerator(
 16              name = "customersSequence",
 17              sequenceName = "customers_id_seq",
 18              allocationSize = 1,
 19              initialValue = 6)
 20      @GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "customersSequence")
 21  	private Long id;
 22  	
 23  	@Column(length = 20)
 24  	private String username;
 25  	
 26  	@Column(length = 20)
 27  	private String name;
 28  	
 29  	@Column(length = 40)
 30  	private String surname;
 31  	
 32  	@Column(length = 250)
 33  	private String address;
 34  	
 35  	@Column(name = "zipcode", length = 10)
 36  	private String zipCode;
 37  	
 38  	@Column(length = 40)
 39  	private String city;
 40  	
 41  	@Column(length = 40)
 42  	private String country;
 43  	
 44  	public Long getId() {
 45  		return id;
 46  	}
 47  	public void setId(Long id) {
 48  		this.id = id;
 49  	}
 50  	public String getUsername() {
 51  		return username;
 52  	}
 53  	public void setUsername(String username) {
 54  		this.username = username;
 55  	}
 56  	public String getName() {
 57  		return name;
 58  	}
 59  	public void setName(String name) {
 60  		this.name = name;
 61  	}
 62  	public String getSurname() {
 63  		return surname;
 64  	}
 65  	public void setSurname(String surname) {
 66  		this.surname = surname;
 67  	}
 68  	public String getAddress() {
 69  		return address;
 70  	}
 71  	public void setAddress(String address) {
 72  		this.address = address;
 73  	}
 74  	public String getZipCode() {
 75  		return zipCode;
 76  	}
 77  	public void setZipCode(String zipCode) {
 78  		this.zipCode = zipCode;
 79  	}
 80  	public String getCity() {
 81  		return city;
 82  	}
 83  	public void setCity(String city) {
 84  		this.city = city;
 85  	}
 86  	public String getCountry() {
 87  		return country;
 88  	}
 89  	public void setCountry(String country) {
 90  		this.country = country;
 91  	}
 92  	
 93  	@Override
 94  	public String toString() {
 95  		return "Customer [id=" + id + ", username=" + username + ", name=" + name + ", surname=" + surname
 96  				+ ", address=" + address + ", zipCode=" + zipCode + ", city=" + city + ", country=" + country + "]";
 97  	}
 98  }

```
  * file:///opt/input/source/src/main/java/io/konveyor/demo/ordermanagement/model/Customer.java
      * Replace the `javax.persistence` import statement with `jakarta.persistence`
      * Code Snippet:
```java
  1  package io.konveyor.demo.ordermanagement.model;
  2  
  3  import javax.persistence.Column;
  4  import javax.persistence.Entity;
  5  import javax.persistence.GeneratedValue;
  6  import javax.persistence.GenerationType;
  7  import javax.persistence.Id;
  8  import javax.persistence.SequenceGenerator;
  9  import javax.persistence.Table;
 10  
 11  @Entity
 12  @Table(name = "customers")
 13  public class Customer {
 14  	@Id
 15      @SequenceGenerator(
 16              name = "customersSequence",
 17              sequenceName = "customers_id_seq",
 18              allocationSize = 1,
 19              initialValue = 6)
 20      @GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "customersSequence")
 21  	private Long id;
 22  	
 23  	@Column(length = 20)
 24  	private String username;
 25  	
 26  	@Column(length = 20)
 27  	private String name;
 28  	
 29  	@Column(length = 40)
 30  	private String surname;
 31  	
 32  	@Column(length = 250)
 33  	private String address;
 34  	
 35  	@Column(name = "zipcode", length = 10)
 36  	private String zipCode;
 37  	
 38  	@Column(length = 40)
 39  	private String city;
 40  	
 41  	@Column(length = 40)
 42  	private String country;
 43  	
 44  	public Long getId() {
 45  		return id;
 46  	}
 47  	public void setId(Long id) {
 48  		this.id = id;
 49  	}
 50  	public String getUsername() {
 51  		return username;
 52  	}
 53  	public void setUsername(String username) {
 54  		this.username = username;
 55  	}
 56  	public String getName() {
 57  		return name;
 58  	}
 59  	public void setName(String name) {
 60  		this.name = name;
 61  	}
 62  	public String getSurname() {
 63  		return surname;
 64  	}
 65  	public void setSurname(String surname) {
 66  		this.surname = surname;
 67  	}
 68  	public String getAddress() {
 69  		return address;
 70  	}
 71  	public void setAddress(String address) {
 72  		this.address = address;
 73  	}
 74  	public String getZipCode() {
 75  		return zipCode;
 76  	}
 77  	public void setZipCode(String zipCode) {
 78  		this.zipCode = zipCode;
 79  	}
 80  	public String getCity() {
 81  		return city;
 82  	}
 83  	public void setCity(String city) {
 84  		this.city = city;
 85  	}
 86  	public String getCountry() {
 87  		return country;
 88  	}
 89  	public void setCountry(String country) {
 90  		this.country = country;
 91  	}
 92  	
 93  	@Override
 94  	public String toString() {
 95  		return "Customer [id=" + id + ", username=" + username + ", name=" + name + ", surname=" + surname
 96  				+ ", address=" + address + ", zipCode=" + zipCode + ", city=" + city + ", country=" + country + "]";
 97  	}
 98  }

```
  * file:///opt/input/source/src/main/java/io/konveyor/demo/ordermanagement/model/Customer.java
      * Replace the `javax.persistence` import statement with `jakarta.persistence`
      * Code Snippet:
```java
  1  package io.konveyor.demo.ordermanagement.model;
  2  
  3  import javax.persistence.Column;
  4  import javax.persistence.Entity;
  5  import javax.persistence.GeneratedValue;
  6  import javax.persistence.GenerationType;
  7  import javax.persistence.Id;
  8  import javax.persistence.SequenceGenerator;
  9  import javax.persistence.Table;
 10  
 11  @Entity
 12  @Table(name = "customers")
 13  public class Customer {
 14  	@Id
 15      @SequenceGenerator(
 16              name = "customersSequence",
 17              sequenceName = "customers_id_seq",
 18              allocationSize = 1,
 19              initialValue = 6)
 20      @GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "customersSequence")
 21  	private Long id;
 22  	
 23  	@Column(length = 20)
 24  	private String username;
 25  	
 26  	@Column(length = 20)
 27  	private String name;
 28  	
 29  	@Column(length = 40)
 30  	private String surname;
 31  	
 32  	@Column(length = 250)
 33  	private String address;
 34  	
 35  	@Column(name = "zipcode", length = 10)
 36  	private String zipCode;
 37  	
 38  	@Column(length = 40)
 39  	private String city;
 40  	
 41  	@Column(length = 40)
 42  	private String country;
 43  	
 44  	public Long getId() {
 45  		return id;
 46  	}
 47  	public void setId(Long id) {
 48  		this.id = id;
 49  	}
 50  	public String getUsername() {
 51  		return username;
 52  	}
 53  	public void setUsername(String username) {
 54  		this.username = username;
 55  	}
 56  	public String getName() {
 57  		return name;
 58  	}
 59  	public void setName(String name) {
 60  		this.name = name;
 61  	}
 62  	public String getSurname() {
 63  		return surname;
 64  	}
 65  	public void setSurname(String surname) {
 66  		this.surname = surname;
 67  	}
 68  	public String getAddress() {
 69  		return address;
 70  	}
 71  	public void setAddress(String address) {
 72  		this.address = address;
 73  	}
 74  	public String getZipCode() {
 75  		return zipCode;
 76  	}
 77  	public void setZipCode(String zipCode) {
 78  		this.zipCode = zipCode;
 79  	}
 80  	public String getCity() {
 81  		return city;
 82  	}
 83  	public void setCity(String city) {
 84  		this.city = city;
 85  	}
 86  	public String getCountry() {
 87  		return country;
 88  	}
 89  	public void setCountry(String country) {
 90  		this.country = country;
 91  	}
 92  	
 93  	@Override
 94  	public String toString() {
 95  		return "Customer [id=" + id + ", username=" + username + ", name=" + name + ", surname=" + surname
 96  				+ ", address=" + address + ", zipCode=" + zipCode + ", city=" + city + ", country=" + country + "]";
 97  	}
 98  }

```
  * file:///opt/input/source/src/main/java/io/konveyor/demo/ordermanagement/model/Customer.java
      * Replace the `javax.persistence` import statement with `jakarta.persistence`
      * Code Snippet:
```java
  1  package io.konveyor.demo.ordermanagement.model;
  2  
  3  import javax.persistence.Column;
  4  import javax.persistence.Entity;
  5  import javax.persistence.GeneratedValue;
  6  import javax.persistence.GenerationType;
  7  import javax.persistence.Id;
  8  import javax.persistence.SequenceGenerator;
  9  import javax.persistence.Table;
 10  
 11  @Entity
 12  @Table(name = "customers")
 13  public class Customer {
 14  	@Id
 15      @SequenceGenerator(
 16              name = "customersSequence",
 17              sequenceName = "customers_id_seq",
 18              allocationSize = 1,
 19              initialValue = 6)
 20      @GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "customersSequence")
 21  	private Long id;
 22  	
 23  	@Column(length = 20)
 24  	private String username;
 25  	
 26  	@Column(length = 20)
 27  	private String name;
 28  	
 29  	@Column(length = 40)
 30  	private String surname;
 31  	
 32  	@Column(length = 250)
 33  	private String address;
 34  	
 35  	@Column(name = "zipcode", length = 10)
 36  	private String zipCode;
 37  	
 38  	@Column(length = 40)
 39  	private String city;
 40  	
 41  	@Column(length = 40)
 42  	private String country;
 43  	
 44  	public Long getId() {
 45  		return id;
 46  	}
 47  	public void setId(Long id) {
 48  		this.id = id;
 49  	}
 50  	public String getUsername() {
 51  		return username;
 52  	}
 53  	public void setUsername(String username) {
 54  		this.username = username;
 55  	}
 56  	public String getName() {
 57  		return name;
 58  	}
 59  	public void setName(String name) {
 60  		this.name = name;
 61  	}
 62  	public String getSurname() {
 63  		return surname;
 64  	}
 65  	public void setSurname(String surname) {
 66  		this.surname = surname;
 67  	}
 68  	public String getAddress() {
 69  		return address;
 70  	}
 71  	public void setAddress(String address) {
 72  		this.address = address;
 73  	}
 74  	public String getZipCode() {
 75  		return zipCode;
 76  	}
 77  	public void setZipCode(String zipCode) {
 78  		this.zipCode = zipCode;
 79  	}
 80  	public String getCity() {
 81  		return city;
 82  	}
 83  	public void setCity(String city) {
 84  		this.city = city;
 85  	}
 86  	public String getCountry() {
 87  		return country;
 88  	}
 89  	public void setCountry(String country) {
 90  		this.country = country;
 91  	}
 92  	
 93  	@Override
 94  	public String toString() {
 95  		return "Customer [id=" + id + ", username=" + username + ", name=" + name + ", surname=" + surname
 96  				+ ", address=" + address + ", zipCode=" + zipCode + ", city=" + city + ", country=" + country + "]";
 97  	}
 98  }

```
