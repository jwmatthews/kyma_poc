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
            <groupId>io.quarkus</groupId>
            <artifactId>quarkus-resteasy</artifactId>
            <version>1.13.7.Final</version>
        </dependency>
        <dependency>
            <groupId>io.quarkus</groupId>
            <artifactId>quarkus-arc</artifactId>
            <version>1.13.7.Final</version>
        </dependency>
        <dependency>
            <groupId>io.quarkus</groupId>
            <artifactId>quarkus-junit5</artifactId>
            <version>1.13.7.Final</version>
            <scope>test</scope>
        </dependency>
    </dependencies>
    <profiles>
        <profile>
            <id>native</id>
            <activation>
                <property>
                    <name>native</name>
                </property>
            </activation>
            <properties>
                <skipITs>false</skipITs>
                <quarkus.package.type>native</quarkus.package.type>
            </properties>
        </profile>
    </profiles>
</project>
```

## Reasoning
The given code snippet is a `pom.xml` file of a Java EE application. To update it to use Quarkus, we need to make the following changes:

1. Add Quarkus dependencies: We need to add the necessary Quarkus dependencies to the `dependencies` section of the `pom.xml` file. These dependencies include `quarkus-resteasy`, `quarkus-arc`, and `quarkus-junit5`.

2. Add Maven profile for native build: We need to add a Maven profile to run the Quarkus native build. This profile will be activated when the `native` property is set. Inside the profile, we set the `skipITs` property to `false` and the `quarkus.package.type` property to `native`.

By adding these changes, the updated `pom.xml` file will be compatible with Quarkus and can be used to build the application.

