## Prompt:
You are an excellent enterprise architect who has an extensive
background in helping companies rewrite their legacy Java EE applications to 
Quarkus.  Your task is to examine code snippets from a legacy Java EE application and 
generate correct and proper code changes to update the application to use Quarkus.

You will be given information from a static code analysis tool which has assessed the 
Java EE application's suitability for adopting Quarkus and will highlight key issues it has found.

You will examine this analysis information and may also have an example problem that was solved 
for a similar problem.  If the example problem is present it will contain the original source code 
and then the updated source code. Pay attention to how the example was solved if it is present.  

## Here is a description of the problem: Stateless annotation can be replaced with scope
Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`

## 'Example Original Source Code':
### File name: src/main/java/com/redhat/coolstore/service/OrderService.java
```
package com.redhat.coolstore.service;

import com.redhat.coolstore.model.Order;
import java.util.List;
import javax.ejb.Stateless;
import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
import javax.persistence.criteria.CriteriaBuilder;
import javax.persistence.criteria.CriteriaQuery;
import javax.persistence.criteria.Root;

@Stateless
public class OrderService {

  @PersistenceContext
  private EntityManager em;

  public void save(Order order) {
    em.persist(order);
  }

  public List<Order> getOrders() {
    CriteriaBuilder cb = em.getCriteriaBuilder();
    CriteriaQuery<Order> criteria = cb.createQuery(Order.class);
    Root<Order> member = criteria.from(Order.class);
    criteria.select(member);
    return em.createQuery(criteria).getResultList();
  }

  public Order getOrderById(long id) {
    return em.find(Order.class, id);
  }
}
```


## 'Example Updated Source Code'
### File name: src/main/java/com/redhat/coolstore/service/OrderService.java
```
package com.redhat.coolstore.service;

import com.redhat.coolstore.model.Order;
import java.util.List;

import jakarta.enterprise.context.ApplicationScoped;
import jakarta.persistence.EntityManager;
import jakarta.persistence.PersistenceContext;
import jakarta.persistence.criteria.CriteriaBuilder;
import jakarta.persistence.criteria.CriteriaQuery;
import jakarta.persistence.criteria.Root;

@ApplicationScoped
public class OrderService {

  @PersistenceContext
  private EntityManager em;

  public void save(Order order) {
    em.persist(order);
  }

  public List<Order> getOrders() {
    CriteriaBuilder cb = em.getCriteriaBuilder();
    CriteriaQuery<Order> criteria = cb.createQuery(Order.class);
    Root<Order> member = criteria.from(Order.class);
    criteria.select(member);
    return em.createQuery(criteria).getResultList();
  }

  public Order getOrderById(long id) {
    return em.find(Order.class, id);
  }
}
```

## 'Message' related to the issue we need to solve
Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`

## 'Current Source Code' we need to update to Quarkus:
### File name: src/main/java/com/redhat/coolstore/service/CatalogService.java
```
  1  package com.redhat.coolstore.service;
  2  
  3  import java.util.List;
  4  import java.util.logging.Logger;
  5  
  6  import javax.inject.Inject;
  7  
  8  import javax.persistence.criteria.CriteriaBuilder;
  9  import javax.persistence.criteria.CriteriaQuery;
 10  import javax.persistence.criteria.Root;
 11  
 12  import javax.ejb.Stateless;
 13  import javax.persistence.EntityManager;
 14  import javax.persistence.PersistenceContext;
 15  
 16  import com.redhat.coolstore.model.*;
 17  
 18  @Stateless
 19  public class CatalogService {
 20  
 21      @Inject
 22      Logger log;
 23  
 24      @PersistenceContext
 25      private EntityManager em;
 26  
 27      public CatalogService() {
 28      }
 29  
 30      public List<CatalogItemEntity> getCatalogItems() {
 31          CriteriaBuilder cb = em.getCriteriaBuilder();
 32          CriteriaQuery<CatalogItemEntity> criteria = cb.createQuery(CatalogItemEntity.class);
 33          Root<CatalogItemEntity> member = criteria.from(CatalogItemEntity.class);
 34          criteria.select(member);
 35          return em.createQuery(criteria).getResultList();
 36      }
 37  
 38      public CatalogItemEntity getCatalogItemById(String itemId) {
 39          return em.find(CatalogItemEntity.class, itemId);
 40      }
 41  
 42      public void updateInventoryItems(String itemId, int deducts) {
 43          InventoryEntity inventoryEntity = getCatalogItemById(itemId).getInventory();
 44          int currentQuantity = inventoryEntity.getQuantity();
 45          inventoryEntity.setQuantity(currentQuantity-deducts);
 46          em.merge(inventoryEntity);
 47      }
 48  
 49  }

```


Your job is to look at the 'Current Source Code' and updated it to work correctly with Quarkus,
following the best information you know of Quarkus, the static code analysis information we share 
here, and the studying how the prior example was solved if present.  Read the 'Example Original Source Code'
and see how it was updated to 'Example Updated Source Code', and determine if a similar pattern can 
be applied to the 'Current Sourec Code'.

Think through the changes you will make and explain each step of the process and why you think it is needed.
If you are unsure of what changes is needed please state you are unsure and ask 
for clarification to help you.

When you are done explaining the reasoning for each change, write the updated 
Quarkus source code for the 'Current Sourec Code' in the form of a diff
in Markdown format, e.g.:

```diff
 ...
```


## Result:
To update the 'Current Source Code' to work correctly with Quarkus, we need to replace the `@Stateless` annotation with a scope annotation, such as `@ApplicationScoped`. 

Here are the steps to make the necessary changes:

1. Remove the `import javax.ejb.Stateless;` statement.
2. Add the `import jakarta.enterprise.context.ApplicationScoped;` statement.
3. Replace the `@Stateless` annotation with `@ApplicationScoped` annotation on the class level.

The updated code will look like this:

```diff
 1  package com.redhat.coolstore.service;
 2  
 3  import java.util.List;
 4  import java.util.logging.Logger;
 5  
 6  import javax.inject.Inject;
 7  
 8  import javax.persistence.criteria.CriteriaBuilder;
 9  import javax.persistence.criteria.CriteriaQuery;
10  import javax.persistence.criteria.Root;
11  
12- import javax.ejb.Stateless;
13  import javax.persistence.EntityManager;
14  import javax.persistence.PersistenceContext;
15  
16  import com.redhat.coolstore.model.*;
17  
18+ import jakarta.enterprise.context.ApplicationScoped;
19  
20- @Stateless
+ @ApplicationScoped
21  public class CatalogService {
22  
23      @Inject
24      Logger log;
25  
26      @PersistenceContext
27      private EntityManager em;
28  
29      public CatalogService() {
30      }
31  
32      public List<CatalogItemEntity> getCatalogItems() {
33          CriteriaBuilder cb = em.getCriteriaBuilder();
34          CriteriaQuery<CatalogItemEntity> criteria = cb.createQuery(CatalogItemEntity.class);
35          Root<CatalogItemEntity> member = criteria.from(CatalogItemEntity.class);
36          criteria.select(member);
37          return em.createQuery(criteria).getResultList();
38      }
39  
40      public CatalogItemEntity getCatalogItemById(String itemId) {
41          return em.find(CatalogItemEntity.class, itemId);
42      }
43  
44      public void updateInventoryItems(String itemId, int deducts) {
45          InventoryEntity inventoryEntity = getCatalogItemById(itemId).getInventory();
46          int currentQuantity = inventoryEntity.getQuantity();
47          inventoryEntity.setQuantity(currentQuantity-deducts);
48          em.merge(inventoryEntity);
49      }
50  
51  }
```

In the updated code, we have replaced the `@Stateless` annotation with `@ApplicationScoped` annotation on line 20. This change ensures that the class is managed as a CDI bean with the application scope in Quarkus.

Please let me know if you need any further assistance.

