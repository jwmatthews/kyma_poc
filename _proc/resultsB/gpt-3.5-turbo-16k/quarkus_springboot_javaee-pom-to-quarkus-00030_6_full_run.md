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
in Markdown format, e.g.:

```diff
 ...
```


## Result:
The static code analysis tool has identified that the Maven Compiler plugin needs to be adopted in the `pom.xml` file. The tool suggests adding the following sections to the `pom.xml` file:

```xml
<properties>
    <compiler-plugin.version>3.10.1</compiler-plugin.version>
    <maven.compiler.release>11</maven.compiler.release>
</properties>
<build>
    <plugins>
        <plugin>
            <artifactId>maven-compiler-plugin</artifactId>
            <version>$</version>
            <configuration>
                <compilerArgs>
                    <arg>-parameters</arg>
                </compilerArgs>
            </configuration>
        </plugin>
    </plugins>
</build>
```

To update the `pom.xml` file to use Quarkus, we need to make the following changes:

1. Add the `properties` section with the `compiler-plugin.version` and `maven.compiler.release` properties.
2. Add the `build` section with the `plugins` section.
3. Add the `plugin` section with the `artifactId` set to `maven-compiler-plugin`.
4. Set the `version` of the `maven-compiler-plugin` to the appropriate version.
5. Add the `configuration` section within the `plugin` section.
6. Add the `compilerArgs` section within the `configuration` section.
7. Add the `-parameters` argument within the `compilerArgs` section.

Here is the updated `pom.xml` file:

```diff
<project>
  ...
  <properties>
+    <compiler-plugin.version>3.10.1</compiler-plugin.version>
+    <maven.compiler.release>11</maven.compiler.release>
  </properties>
  ...
  <build>
+    <plugins>
+      <plugin>
+        <artifactId>maven-compiler-plugin</artifactId>
+        <version>$</version>
+        <configuration>
+          <compilerArgs>
+            <arg>-parameters</arg>
+          </compilerArgs>
+        </configuration>
+      </plugin>
+    </plugins>
  </build>
  ...
</project>
```

Please note that the 'Solved Example Problem' and its diff were not provided, so we cannot refer to it for guidance.

