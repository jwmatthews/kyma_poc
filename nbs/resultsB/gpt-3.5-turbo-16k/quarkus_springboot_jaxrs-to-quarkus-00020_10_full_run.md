# Ruleset Violation: 'quarkus/springboot' 'jaxrs-to-quarkus-00020'
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
Source code filename ``` src/main/java/com/redhat/coolstore/rest/RestApplication.java ``` is:
```
package com.redhat.coolstore.rest;

import javax.ws.rs.ApplicationPath;
import javax.ws.rs.core.Application;


@ApplicationPath("/services")
public class RestApplication extends Application {

}
```

## Static Code Analysis Information:

You will be given information from a static code analysis tool which has assessed the 
Java EE application's suitability for adopting Quarkus and will highlight key issues it has found.

You will examine this analysis information and strongly consider it as an important 
issue we need to address when we rewrite the source code to Quarkus

### 'Description' of the problem: 
```
JAX-RS activation is no longer necessary
JAX-RS activation is no longer necessary. You can set a root path like this but you don't have to.
```

### 'Message' related to the issue we need to solve
```
JAX-RS activation is no longer necessary. You can set a root path like this but you don't have to.
```

### 'Solved Problem'
The 'Solved Problem' will be presented as a diff from a git repo in a branch that has
the solved updates so the application can use Quarkus. Note that the solved problem is 
for a different application to our target application, but the application may have similiarities.
Pay attention to how the example was solved if it is present, we want to follow a similar 
pattern adapted to our specific source file.

The filename for the 'Solved Example Problem' is:
```
src/main/java/com/redhat/coolstore/rest/RestApplication.java
```

The diff for the 'Solved Example Problem Diff' is:
```
@@ -1,7 +1,7 @@
 package com.redhat.coolstore.rest;
 
-import javax.ws.rs.ApplicationPath;
-import javax.ws.rs.core.Application;
+import jakarta.ws.rs.ApplicationPath;
+import jakarta.ws.rs.core.Application;
 
 
 @ApplicationPath("/services")

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

Ensure that you begin the result with the markdown header of: ## Result


## Result:
## Result
```diff
 package com.redhat.coolstore.rest;
 
-import javax.ws.rs.ApplicationPath;
-import javax.ws.rs.core.Application;
+import io.quarkus.runtime.annotations.RegisterForReflection;
+import javax.ws.rs.core.Application;
 
+@RegisterForReflection
 public class RestApplication extends Application {
 
 }
```

## Explanation
In the original code snippet, the `RestApplication` class extends `javax.ws.rs.core.Application` and is annotated with `@ApplicationPath("/services")`. However, in Quarkus, JAX-RS activation is no longer necessary and the `@ApplicationPath` annotation is not required.

To update the code to use Quarkus, we need to make the following changes:

1. Remove the import statements for `javax.ws.rs.ApplicationPath` and `javax.ws.rs.core.Application`.
2. Add the import statement for `io.quarkus.runtime.annotations.RegisterForReflection`.
3. Add the `@RegisterForReflection` annotation to the `RestApplication` class. This annotation is required to enable reflection on the class during the build process.

These changes will ensure that the `RestApplication` class is properly updated to work with Quarkus.

