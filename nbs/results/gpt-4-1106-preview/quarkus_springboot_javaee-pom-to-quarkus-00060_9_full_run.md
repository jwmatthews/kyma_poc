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

## Here is a description of the problem: Add Maven profile to run the Quarkus native build
Leverage a Maven profile to run the Quarkus native build adding the following section to the `pom.xml` file:. ```xml. <profiles>. <profile>. <id>native</id>. <activation>. <property>. <name>native</name>. </property>. </activation>. <properties>. <skipITs>false</skipITs>. <quarkus.package.type>native</quarkus.package.type>. </properties>. </profile>. </profiles>. ```

## 'Example Original Source Code':
### File name: 
```

```


## 'Example Updated Source Code'
### File name: 
```

```

## 'Message' related to the issue we need to solve
Leverage a Maven profile to run the Quarkus native build adding the following section to the `pom.xml` file:. ```xml. <profiles>. <profile>. <id>native</id>. <activation>. <property>. <name>native</name>. </property>. </activation>. <properties>. <skipITs>false</skipITs>. <quarkus.package.type>native</quarkus.package.type>. </properties>. </profile>. </profiles>. ```

## 'Current Source Code' we need to update to Quarkus:
### File name: pom.xml
```
None
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
Since there is no 'Current Source Code' provided for the `pom.xml` file, I will assume that we are starting with a basic Maven `pom.xml` file from a legacy Java EE application that does not yet have any Quarkus configuration.

To update the `pom.xml` file to support Quarkus native builds, we need to add a Maven profile specifically for building the native executable. This profile will be activated by the presence of a system property named `native`. When this profile is active, it will set the `quarkus.package.type` property to `native`, which tells Quarkus to produce a native executable instead of a JVM-based JAR.

Here are the steps to update the `pom.xml`:

1. Add a `<profiles>` section if it does not exist.
2. Inside the `<profiles>` section, add a new `<profile>` with the `<id>` of `native`.
3. Within the `<profile>`, add an `<activation>` section that activates the profile when the `native` property is present.
4. Inside the `<profile>`, add a `<properties>` section that sets `skipITs` to `false` (to ensure integration tests are not skipped) and `quarkus.package.type` to `native`.

The reason for setting `skipITs` to `false` is to ensure that integration tests are run during the build process, which is important for verifying the application's functionality before producing the native executable.

Here is the updated `pom.xml` in the form of a diff:

```diff
+ <profiles>
+   <profile>
+     <id>native</id>
+     <activation>
+       <property>
+         <name>native</name>
+       </property>
+     </activation>
+     <properties>
+       <skipITs>false</skipITs>
+       <quarkus.package.type>native</quarkus.package.type>
+     </properties>
+   </profile>
+ </profiles>
```

Please note that this is a generic update and the actual `pom.xml` file may contain other profiles or properties that need to be considered. If there are other specific configurations or dependencies in the legacy Java EE application's `pom.xml` that need to be updated for Quarkus, those would need to be addressed as well. Without the actual `pom.xml` content, I can only provide the changes related to the native build profile as requested.

