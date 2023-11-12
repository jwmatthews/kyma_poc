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
None
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
in Markdown format, e.g.:

```diff
 ...
```


## Result:
The given problem statement is about adding a Maven profile to run the Quarkus native build. The static code analysis information provides the necessary XML code to be added to the `pom.xml` file.

To solve this problem, we need to add the provided XML code to the `pom.xml` file. This can be done by following these steps:

1. Open the `pom.xml` file.
2. Locate the `<project>` tag and add the following XML code inside it:

```xml
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
```

This XML code defines a Maven profile with the id `native`. It is activated when the property `native` is set. Inside the profile, we set the properties `skipITs` to `false` and `quarkus.package.type` to `native`.

The updated `pom.xml` file should look like this:

```xml
<project>
  ...
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
  ...
</project>
```

This change adds the necessary Maven profile to run the Quarkus native build.
