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
Source code filename ``` backend-v1/src/main/java/org/jboss/examples/ticketmonster/util/Resources.java ``` is:
```
package org.jboss.examples.ticketmonster.util;

import java.util.logging.Logger;

import javax.enterprise.inject.Produces;
import javax.enterprise.inject.spi.InjectionPoint;
import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;

/**
 * This class uses CDI to alias Java EE resources, such as the persistence context, to CDI beans
 * 
 * <p>
 * Example injection on a managed bean field:
 * </p>
 * 
 * <pre>
 * &#064;Inject
 * private EntityManager em;
 * </pre>
 */
public class Resources {

    /**
     * Alias the persistence context
     */
    // use @SuppressWarnings to tell IDE to ignore warnings about field not being referenced directly
   @SuppressWarnings("unused")
   @Produces
   @PersistenceContext
   private EntityManager em;
   
   /**
    * Provider injectable loggers based around Java Util Logging.
    * @param injectionPoint
    * @return
    */
   @Produces
   public Logger produceLog(InjectionPoint injectionPoint) {
      return Logger.getLogger(injectionPoint.getMember().getDeclaringClass().getName());
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
Producer annotation no longer required
In Quarkus, you can skip the @Produces annotation completely if the producer method is annotated with a scope annotation, a stereotype or a qualifier... This field could be accessed using a `@Named` getter method instead.
```

### 'Message' related to the issue we need to solve
```
In Quarkus, you can skip the @Produces annotation completely if the producer method is annotated with a scope annotation, a stereotype or a qualifier... This field could be accessed using a `@Named` getter method instead.
```

### 'Solved Problem'
The 'Solved Problem' will be presented as a diff from a git repo in a branch that has
the solved updates so the application can use Quarkus. Note that the solved problem is 
for a different application to our target application, but the application may have similiarities.
Pay attention to how the example was solved if it is present, we want to follow a similar 
pattern adapted to our specific source file.

The filename for the 'Solved Example Problem' is:
```
backend-v1/src/main/java/org/jboss/examples/ticketmonster/util/Resources.java
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
The static code analysis tool has identified that the `@Produces` annotation is no longer required in Quarkus if the producer method is annotated with a scope annotation, a stereotype, or a qualifier. In our case, the `@Produces` annotation is used on the `EntityManager` field in the `Resources` class. Since the field is not directly referenced, we can remove the `@Produces` annotation and use a `@Named` getter method to access the field instead.

## Result
```diff
 package org.jboss.examples.ticketmonster.util;
 
 import java.util.logging.Logger;
 
-import javax.enterprise.inject.Produces;
 import javax.enterprise.inject.spi.InjectionPoint;
 import javax.inject.Inject;
 import javax.inject.Named;
 import javax.persistence.EntityManager;
 import javax.persistence.PersistenceContext;
 
 /**
  * This class uses CDI to alias Java EE resources, such as the persistence context, to CDI beans
  * 
  * <p>
  * Example injection on a managed bean field:
  * </p>
  * 
  * <pre>
  * &#064;Inject
  * private EntityManager em;
  * </pre>
  */
 public class Resources {
 
     /**
      * Alias the persistence context
      */
-    // use @SuppressWarnings to tell IDE to ignore warnings about field not being referenced directly
-   @SuppressWarnings("unused")
-   @Produces
     @PersistenceContext
-   private EntityManager em;
+    private EntityManager em;
+    
+    @Named("entityManager")
+    @Produces
+    public EntityManager getEntityManager() {
+        return em;
+    }
    
    /**
     * Provider injectable loggers based around Java Util Logging.
     * @param injectionPoint
     * @return
     */
    @Produces
    public Logger produceLog(InjectionPoint injectionPoint) {
       return Logger.getLogger(injectionPoint.getMember().getDeclaringClass().getName());
    }
  
 }
```

