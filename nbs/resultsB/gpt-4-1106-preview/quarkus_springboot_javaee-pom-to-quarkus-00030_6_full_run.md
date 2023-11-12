# Ruleset Violation: 'quarkus/springboot' 'javaee-pom-to-quarkus-00030'
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
Adopt Maven Compiler plugin

```

### 'Message' related to the issue we need to solve
```
Use the Maven Compiler plugin adding the following sections to the `pom.xml` file:. ```xml. <properties>. <compiler-plugin.version>3.10.1</compiler-plugin.version>. <maven.compiler.release>11</maven.compiler.release>. </properties>. <build>. <plugins>. <plugin>. <artifactId>maven-compiler-plugin</artifactId>. <version>$</version>. <configuration>. <compilerArgs>. <arg>-parameters</arg>. </compilerArgs>. </configuration>. </plugin>. </plugins>. </build>. ```
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
To update the legacy Java EE application to use Quarkus, we need to make several changes to the `pom.xml` file. The static code analysis information indicates that we should adopt the Maven Compiler plugin with specific configurations. This is important because Quarkus requires Java 11 or later, and we need to ensure that the Maven build is set up to compile the application using the correct Java version and with the necessary compiler arguments.

Since there is no 'Solved Example Problem Diff' provided, I will proceed with the information given in the 'Description' and 'Message' to update the `pom.xml` file.

Here are the steps we need to take:

1. Change the packaging type from `war` to `jar` because Quarkus applications are typically packaged as JARs.
2. Remove the Java EE dependencies as Quarkus provides its own set of APIs and dependencies.
3. Add the Quarkus BOM (Bill of Materials) to manage the versions of Quarkus dependencies.
4. Add the Maven Compiler plugin with the specified version and configuration to ensure the application is compiled with Java 11 and supports method parameter reflection.
5. Add the Quarkus Maven plugin to build and package the application.

Let's write the updated `pom.xml` in the form of a diff:

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
+   <packaging>jar</packaging>
    <name>coolstore-monolith</name>
    <properties>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <maven.build.timestamp.format>yyyyMMdd'T'HHmmss</maven.build.timestamp.format>
        <project.encoding>UTF-8</project.encoding>
        <maven.test.skip>true</maven.test.skip>
+       <compiler-plugin.version>3.10.1</compiler-plugin.version>
+       <maven.compiler.release>11</maven.compiler.release>
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
+       <dependency>
+           <groupId>io.quarkus</groupId>
+           <artifactId>quarkus-bom</artifactId>
+           <version>${quarkus.version}</version>
+           <type>pom</type>
+           <scope>import</scope>
+       </dependency>
    </dependencies>
+   <build>
+       <plugins>
+           <plugin>
+               <artifactId>maven-compiler-plugin</artifactId>
+               <version>${compiler-plugin.version}</version>
+               <configuration>
+                   <release>${maven.compiler.release}</release>
+                   <compilerArgs>
+                       <arg>-parameters</arg>
+                   </compilerArgs>
+               </configuration>
+           </plugin>
+           <plugin>
+               <groupId>io.quarkus</groupId>
+               <artifactId>quarkus-maven-plugin</artifactId>
+               <version>${quarkus.version}</version>
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
</project>
```

Please note that the `${quarkus.version}` placeholder should be replaced with the actual version of Quarkus you intend to use. You can find the latest version of Quarkus on their website or Maven Central.

