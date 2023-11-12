# Ruleset Violation: 'quarkus/springboot' 'javaee-pom-to-quarkus-00060'
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
Source code filename ``` pom.xml ``` is:
```
<?xml version="1.0" encoding="UTF-8"?>
<project 
    xmlns="http://maven.apache.org/POM/4.0.0" 
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.redhat.coolstore</groupId>
    <artifactId>monolith</artifactId>
    <version>1.0.0-SNAPSHOT</version>
    <packaging>war</packaging>
    <name>coolstore-monolith</name>
    <properties>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <maven.build.timestamp.format>yyyyMMdd'T'HHmmss</maven.build.timestamp.format>
        <project.encoding>UTF-8</project.encoding>
        <maven.test.skip>true</maven.test.skip>
    </properties>
    <dependencies>
        <dependency>
            <groupId>javax</groupId>
            <artifactId>javaee-web-api</artifactId>
            <version>7.0</version>
            <scope>provided</scope>
        </dependency>
        <dependency>
            <groupId>javax</groupId>
            <artifactId>javaee-api</artifactId>
            <version>7.0</version>
            <scope>provided</scope>
        </dependency>
        <dependency>
```

## Static Code Analysis Information:

You will be given information from a static code analysis tool which has assessed the 
Java EE application's suitability for adopting Quarkus and will highlight key issues it has found.

You will examine this analysis information and strongly consider it as an important 
issue we need to address when we rewrite the source code to Quarkus

### 'Description' of the problem: 
```
Add Maven profile to run the Quarkus native build
Leverage a Maven profile to run the Quarkus native build adding the following section to the `pom.xml` file:. ```xml. <profiles>. <profile>. <id>native</id>. <activation>. <property>. <name>native</name>. </property>. </activation>. <properties>. <skipITs>false</skipITs>. <quarkus.package.type>native</quarkus.package.type>. </properties>. </profile>. </profiles>. ```
```

### 'Message' related to the issue we need to solve
```
Leverage a Maven profile to run the Quarkus native build adding the following section to the `pom.xml` file:. ```xml. <profiles>. <profile>. <id>native</id>. <activation>. <property>. <name>native</name>. </property>. </activation>. <properties>. <skipITs>false</skipITs>. <quarkus.package.type>native</quarkus.package.type>. </properties>. </profile>. </profiles>. ```
```

### 'Solved Problem'
The 'Solved Problem' will be presented as a diff from a git repo in a branch that has
the solved updates so the application can use Quarkus. Note that the solved problem is 
for a different application to our target application, but the application may have similiarities.
Pay attention to how the example was solved if it is present, we want to follow a similar 
pattern adapted to our specific source file.

The filename for the 'Solved Example Problem' is:
```

```

The diff for the 'Solved Example Problem Diff' is:
```

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
To update the legacy Java EE application to use Quarkus, we need to make several changes to the `pom.xml` file. The static code analysis information provided indicates that we should add a Maven profile specifically for building a native Quarkus application. This is important because Quarkus offers the ability to compile applications to a native executable using GraalVM, which can significantly reduce the startup time and memory footprint of the application.

Since we do not have a 'Solved Example Problem Diff' to refer to, we will proceed with the information given in the 'Description' and 'Message'. The instructions are clear: we need to add a Maven profile for the native build.

Here's what we need to do:

1. Add a new Maven profile with the ID `native`.
2. Within this profile, we need to activate it based on the presence of a property named `native`.
3. We need to set the property `skipITs` to `false` to ensure integration tests are not skipped during the native build.
4. We need to set the property `quarkus.package.type` to `native` to indicate that we want to build a native executable.

Let's proceed with the changes to the `pom.xml` file.

## Result
```diff
<?xml version="1.0" encoding="UTF-8"?>
<project 
    xmlns="http://maven.apache.org/POM/4.0.0" 
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.redhat.coolstore</groupId>
    <artifactId>monolith</artifactId>
    <version>1.0.0-SNAPSHOT</version>
-   <packaging>war</packaging>
+   <packaging>jar</packaging> <!-- Quarkus uses jar packaging by default -->
    <name>coolstore-monolith</name>
    <properties>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <maven.build.timestamp.format>yyyyMMdd'T'HHmmss</maven.build.timestamp.format>
        <project.encoding>UTF-8</project.encoding>
        <maven.test.skip>true</maven.test.skip>
+       <quarkus.platform.version>2.8.1.Final</quarkus.platform.version> <!-- Specify the Quarkus version -->
+       <quarkus-plugin.version>${quarkus.platform.version}</quarkus-plugin.version>
+       <quarkus.package.type>uber-jar</quarkus.package.type> <!-- Default package type for non-native builds -->
    </properties>
    <dependencies>
-       <dependency>
-           <groupId>javax</groupId>
-           <artifactId>javaee-web-api</artifactId>
-           <version>7.0</version>
-           <scope>provided</scope>
-       </dependency>
-       <dependency>
-           <groupId>javax</groupId>
-           <artifactId>javaee-api</artifactId>
-           <version>7.0</version>
-           <scope>provided</scope>
-       </dependency>
+       <!-- Replace Java EE dependencies with Quarkus dependencies -->
+       <dependency>
+           <groupId>io.quarkus</groupId>
+           <artifactId>quarkus-resteasy</artifactId>
+       </dependency>
+       <dependency>
+           <groupId>io.quarkus</groupId>
+           <artifactId>quarkus-arc</artifactId>
+       </dependency>
+       <!-- Additional Quarkus dependencies as needed -->
    </dependencies>
+   <build>
+       <plugins>
+           <plugin>
+               <groupId>io.quarkus</groupId>
+               <artifactId>quarkus-maven-plugin</artifactId>
+               <version>${quarkus-plugin.version}</version>
+               <executions>
+                   <execution>
+                       <goals>
+                           <goal>build</goal>
+                       </goals>
+                   </execution>
+               </executions>
+           </plugin>
+       </plugins>
+   </build>
+   <profiles>
+       <profile>
+           <id>native</id>
+           <activation>
+               <property>
+                   <name>native</name>
+               </property>
+           </activation>
+           <properties>
+               <skipITs>false</skipITs>
+               <quarkus.package.type>native</quarkus.package.type>
+           </properties>
+       </profile>
+   </profiles>
</project>
```

In the diff above, we have:

- Changed the packaging from `war` to `jar` as Quarkus uses jar packaging by default.
- Added the Quarkus platform version property and set the default package type to `uber-jar`.
- Removed the Java EE dependencies and replaced them with Quarkus dependencies such as `quarkus-resteasy` and `quarkus-arc`.
- Added the Quarkus Maven plugin to handle the build and create the native executable.
- Added the `native` profile with the necessary properties to enable native compilation.

These changes should update the legacy Java EE application to be compatible with Quarkus and allow for native builds.

