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
            <groupId>org.flywaydb</groupId>
            <artifactId>flyway-core</artifactId>
            <version>4.1.2</version>
        </dependency>
        <dependency>
            <groupId>org.jboss.spec.javax.rmi</groupId>
            <artifactId>jboss-rmi-api_1.0_spec</artifactId>
            <version>1.0.2.Final</version>
        </dependency>
    </dependencies>
    <build>
        <finalName>ROOT</finalName>
        <plugins>
            <plugin>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.0</version>
                <configuration>
                    <encoding>${project.encoding}</encoding>
                    <source>1.8</source>
                    <target>1.8</target>
                </configuration>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-war-plugin</artifactId>
                <version>3.2.0</version>
            </plugin>
        </plugins>
    </build>
    <profiles>
<!-- TODO: Add OpenShift profile here -->
    </profiles>
</project>

```

## Static Code Analysis Information:

You will be given information from a static code analysis tool which has assessed the 
Java EE application's suitability for adopting Quarkus and will highlight key issues it has found.

You will examine this analysis information and strongly consider it as an important 
issue we need to address when we rewrite the source code to Quarkus

### 'Description' of the problem: 
```
javax groupId has been replaced by jakarta.platform
Update group dependency by replacing the `javax` groupId with `jakarta.platform`
```

### 'Message' related to the issue we need to solve
```
Update group dependency by replacing the `javax` groupId with `jakarta.platform`
```

### 'Solved Problem'
The 'Solved Problem' will be presented as a diff from a git repo in a branch that has
the solved updates so the application can use Quarkus. Note that the solved problem is 
for a different application to our target application, but the application may have similiarities.
Pay attention to how the example was solved if it is present, we want to follow a similar 
pattern adapted to our specific source file.

The filename for the 'Solved Example Problem' is:
```
pom.xml
```

The diff for the 'Solved Example Problem Diff' is:
```
@@ -1,63 +1,151 @@
 <?xml version="1.0" encoding="UTF-8"?>
-<project 
-    xmlns="http://maven.apache.org/POM/4.0.0" 
-    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
-    <modelVersion>4.0.0</modelVersion>
-    <groupId>com.redhat.coolstore</groupId>
-    <artifactId>monolith</artifactId>
-    <version>1.0.0-SNAPSHOT</version>
-    <packaging>war</packaging>
-    <name>coolstore-monolith</name>
-    <properties>
-        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
-        <maven.build.timestamp.format>yyyyMMdd'T'HHmmss</maven.build.timestamp.format>
-        <project.encoding>UTF-8</project.encoding>
-        <maven.test.skip>true</maven.test.skip>
-    </properties>
+<project xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd" xmlns="http://maven.apache.org/POM/4.0.0"
+    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
+  <modelVersion>4.0.0</modelVersion>
+  <groupId>com.redhat.coolstore</groupId>
+  <artifactId>monolith</artifactId>
+  <version>1.0.0-SNAPSHOT</version>
+  <name>coolstore-monolith</name>
+  <properties>
+    <compiler-plugin.version>3.11.0</compiler-plugin.version>
+    <maven.compiler.release>17</maven.compiler.release>
+    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
+    <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
+    <quarkus.platform.artifact-id>quarkus-bom</quarkus.platform.artifact-id>
+    <quarkus.platform.group-id>io.quarkus.platform</quarkus.platform.group-id>
+    <quarkus.platform.version>3.3.1</quarkus.platform.version>
+    <skipITs>true</skipITs>
+    <surefire-plugin.version>3.1.2</surefire-plugin.version>
+  </properties>
+  <dependencyManagement>
     <dependencies>
-        <dependency>
-            <groupId>javax</groupId>
-            <artifactId>javaee-web-api</artifactId>
-            <version>7.0</version>
-            <scope>provided</scope>
-        </dependency>
-        <dependency>
-            <groupId>javax</groupId>
-            <artifactId>javaee-api</artifactId>
-            <version>7.0</version>
-            <scope>provided</scope>
-        </dependency>
-        <dependency>
-            <groupId>org.flywaydb</groupId>
-            <artifactId>flyway-core</artifactId>
-            <version>4.1.2</version>
-        </dependency>
-        <dependency>
-            <groupId>org.jboss.spec.javax.rmi</groupId>
-            <artifactId>jboss-rmi-api_1.0_spec</artifactId>
-            <version>1.0.2.Final</version>
-        </dependency>
+      <dependency>
+        <groupId>${quarkus.platform.group-id}</groupId>
+        <artifactId>${quarkus.platform.artifact-id}</artifactId>
+        <version>${quarkus.platform.version}</version>
+        <type>pom</type>
+        <scope>import</scope>
+      </dependency>
+      <dependency>
+        <groupId>${quarkus.platform.group-id}</groupId>
+        <artifactId>quarkus-qpid-jms-bom</artifactId>
+        <version>${quarkus.platform.version}</version>
+        <type>pom</type>
+        <scope>import</scope>
+      </dependency>
     </dependencies>
-    <build>
-        <finalName>ROOT</finalName>
-        <plugins>
-            <plugin>
-                <artifactId>maven-compiler-plugin</artifactId>
-                <version>3.0</version>
-                <configuration>
-                    <encoding>${project.encoding}</encoding>
-                    <source>1.8</source>
-                    <target>1.8</target>
-                </configuration>
-            </plugin>
-            <plugin>
-                <groupId>org.apache.maven.plugins</groupId>
-                <artifactId>maven-war-plugin</artifactId>
-                <version>3.2.0</version>
-            </plugin>
-        </plugins>
-    </build>
-    <profiles>
-<!-- TODO: Add OpenShift profile here -->
-    </profiles>
+  </dependencyManagement>
+  <dependencies>
+    <dependency>
+      <groupId>io.quarkus</groupId>
+      <artifactId>quarkus-arc</artifactId>
+    </dependency>
+    <dependency>
+      <groupId>io.quarkus</groupId>
+      <artifactId>quarkus-resteasy</artifactId>
+    </dependency>
+    <dependency>
+      <groupId>io.quarkus</groupId>
+      <artifactId>quarkus-hibernate-orm</artifactId>
+    </dependency>
+    <dependency>
+      <groupId>io.quarkus</groupId>
+      <artifactId>quarkus-jdbc-postgresql</artifactId>
+    </dependency>
+    <dependency>
+      <groupId>io.quarkus</groupId>
+      <artifactId>quarkus-flyway</artifactId>
+    </dependency>
+    <dependency>
+      <groupId>io.quarkus</groupId>
+      <artifactId>quarkus-resteasy-jsonb</artifactId>
+    </dependency>
+    <dependency>
+      <groupId>io.quarkus</groupId>
+      <artifactId>quarkus-smallrye-reactive-messaging-amqp</artifactId>
+    </dependency>
+    <dependency>
+      <groupId>io.quarkus</groupId>
+      <artifactId>quarkus-undertow</artifactId>
+    </dependency>
+    <dependency>
+      <groupId>io.quarkus</groupId>
+      <artifactId>quarkus-oidc</artifactId>
+    </dependency>
+    <dependency>
+      <groupId>io.quarkus</groupId>
+      <artifactId>quarkus-config-yaml</artifactId>
+    </dependency>
+    <dependency>
+      <groupId>org.amqphub.quarkus</groupId>
+      <artifactId>quarkus-qpid-jms</artifactId>
+    </dependency>
+    <dependency>
+      <groupId>io.quarkus</groupId>
+      <artifactId>quarkus-junit5</artifactId>
+      <scope>test</scope>
+    </dependency>
+    <dependency>
+      <groupId>io.rest-assured</groupId>
+      <artifactId>rest-assured</artifactId>
+      <scope>test</scope>
+    </dependency>
+  </dependencies>
+  <build>
+    <plugins>
+      <plugin>
+        <groupId>${quarkus.platform.group-id}</groupId>
+        <artifactId>quarkus-maven-plugin</artifactId>
+        <version>${quarkus.platform.version}</version>
+        <extensions>true</extensions>
+        <executions>
+          <execution>
+            <goals>
+              <goal>build</goal>
+              <goal>generate-code</goal>
+              <goal>generate-code-tests</goal>
+            </goals>
+          </execution>
+        </executions>
+      </plugin>
+      <plugin>
+        <artifactId>maven-compiler-plugin</artifactId>
+        <version>${compiler-plugin.version}</version>
+        <configuration>
+          <compilerArgs>
+            <arg>-parameters</arg>
+          </compilerArgs>
+        </configuration>
+      </plugin>
+      <plugin>
+        <artifactId>maven-surefire-plugin</artifactId>
+        <version>${surefire-plugin.version}</version>
+        <configuration>
+          <systemPropertyVariables>
+            <java.util.logging.manager>org.jboss.logmanager.LogManager</java.util.logging.manager>
+            <maven.home>${maven.home}</maven.home>
+          </systemPropertyVariables>
+        </configuration>
+      </plugin>
+      <plugin>
+        <artifactId>maven-failsafe-plugin</artifactId>
+        <version>${surefire-plugin.version}</version>
+        <executions>
+          <execution>
+            <goals>
+              <goal>integration-test</goal>
+              <goal>verify</goal>
+            </goals>
+            <configuration>
+              <systemPropertyVariables>
+                <native.image.path>${project.build.directory}/${project.build.finalName}-runner</native.image.path>
+                <java.util.logging.manager>org.jboss.logmanager.LogManager</java.util.logging.manager>
+                <maven.home>${maven.home}</maven.home>
+              </systemPropertyVariables>
+            </configuration>
+          </execution>
+        </executions>
+      </plugin>
+    </plugins>
+  </build>
 </project>

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
--- a/pom.xml
+++ b/pom.xml
@@ -1,63 +1,151 @@
 <?xml version="1.0" encoding="UTF-8"?>
-<project 
-    xmlns="http://maven.apache.org/POM/4.0.0" 
-    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
-    <modelVersion>4.0.0</modelVersion>
-    <groupId>com.redhat.coolstore</groupId>
-    <artifactId>monolith</artifactId>
-    <version>1.0.0-SNAPSHOT</version>
-    <packaging>war</packaging>
-    <name>coolstore-monolith</name>
-    <properties>
-        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
-        <maven.build.timestamp.format>yyyyMMdd'T'HHmmss</maven.build.timestamp.format>
-        <project.encoding>UTF-8</project.encoding>
-        <maven.test.skip>true</maven.test.skip>
-    </properties>
+<project xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd" xmlns="http://maven.apache.org/POM/4.0.0"
+    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
+  <modelVersion>4.0.0</modelVersion>
+  <groupId>com.redhat.coolstore</groupId>
+  <artifactId>monolith</artifactId>
+  <version>1.0.0-SNAPSHOT</version>
+  <name>coolstore-monolith</name>
+  <properties>
+    <compiler-plugin.version>3.11.0</compiler-plugin.version>
+    <maven.compiler.release>17</maven.compiler.release>
+    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
+    <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
+    <quarkus.platform.artifact-id>quarkus-bom</quarkus.platform.artifact-id>
+    <quarkus.platform.group-id>io.quarkus.platform</quarkus.platform.group-id>
+    <quarkus.platform.version>3.3.1</quarkus.platform.version>
+    <skipITs>true</skipITs>
+    <surefire-plugin.version>3.1.2</surefire-plugin.version>
+  </properties>
+  <dependencyManagement>
+    <dependencies>
+      <dependency>
+        <groupId>${quarkus.platform.group-id}</groupId>
+        <artifactId>${quarkus.platform.artifact-id}</artifactId>
+        <version>${quarkus.platform.version}</version>
+        <type>pom</type>
+        <scope>import</scope>
+      </dependency>
+      <dependency>
+        <groupId>${quarkus.platform.group-id}</groupId>
+        <artifactId>quarkus-qpid-jms-bom</artifactId>
+        <version>${quarkus.platform.version}</version>
+        <type>pom</type>
+        <scope>import</scope>
+      </dependency>
+    </dependencies>
+  </dependencyManagement>
+  <dependencies>
+    <dependency>
+      <groupId>io.quarkus</groupId>
+      <artifactId>quarkus-arc</artifactId>
+    </dependency>
+    <dependency>
+      <groupId>io.quarkus</groupId>
+      <artifactId>quarkus-resteasy</artifactId>
+    </dependency>
+    <dependency>
+      <groupId>io.quarkus</groupId>
+      <artifactId>quarkus-hibernate-orm</artifactId>
+    </dependency>
+    <dependency>
+      <groupId>io.quarkus</groupId>
+      <artifactId>quarkus-jdbc-postgresql</artifactId>
+    </dependency>
+    <dependency>
+      <groupId>io.quarkus</groupId>
+      <artifactId>quarkus-flyway</artifactId>
+    </dependency>
+    <dependency>
+      <groupId>io.quarkus</groupId>
+      <artifactId>quarkus-resteasy-jsonb</artifactId>
+    </dependency>
+    <dependency>
+      <groupId>io.quarkus</groupId>
+      <artifactId>quarkus-smallrye-reactive-messaging-amqp</artifactId>
+    </dependency>
+    <dependency>
+      <groupId>io.quarkus</groupId>
+      <artifactId>quarkus-undertow</artifactId>
+    </dependency>
+    <dependency>
+      <groupId>io.quarkus</groupId>
+      <artifactId>quarkus-oidc</artifactId>
+    </dependency>
+    <dependency>
+      <groupId>io.quarkus</groupId>
+      <artifactId>quarkus-config-yaml</artifactId>
+    </dependency>
+    <dependency>
+      <groupId>org.amqphub.quarkus</groupId>
+      <artifactId>quarkus-qpid-jms</artifactId>
+    </dependency>
+    <dependency>
+      <groupId>io.quarkus</groupId>
+      <artifactId>quarkus-junit5</artifactId>
+      <scope>test</scope>
+    </dependency>
+    <dependency>
+      <groupId>io.rest-assured</groupId>
+      <artifactId>rest-assured</artifactId>
+      <scope>test</scope>
+    </dependency>
+  </dependencies>
+  <build>
+    <plugins>
+      <plugin>
+        <groupId>${quarkus.platform.group-id}</groupId>
+        <artifactId>quarkus-maven-plugin</artifactId>
+        <version>${quarkus.platform.version}</version>
+        <extensions>true</extensions>
+        <executions>
+          <execution>
+            <goals>
+              <goal>build</goal>
+              <goal>generate-code</goal>
+              <goal>generate-code-tests</goal>
+            </goals>
+          </execution>
+        </executions>
+      </plugin>
+      <plugin>
+        <artifactId>maven-compiler-plugin</artifactId>
+        <version>${compiler-plugin.version}</version>
+        <configuration>
+          <compilerArgs>
+            <arg>-parameters</arg>
+          </compilerArgs>
+        </configuration>
+      </plugin>
+      <plugin>
+        <artifactId>maven-surefire-plugin</artifactId>
+        <version>${surefire-plugin.version}</version>
+        <configuration>
+          <systemPropertyVariables>
+            <java.util.logging.manager>org.jboss.logmanager.LogManager</java.util.logging.manager>
+            <maven.home>${maven.home}</maven.home>
+          </systemPropertyVariables>
+        </configuration>
+      </plugin>
+      <plugin>
+        <artifactId>maven-failsafe-plugin</artifactId>
+        <version>${surefire-plugin.version}</version>
+        <executions>
+          <execution>
+            <goals>
+              <goal>integration-test</goal>
+              <goal>verify</goal>
+            </goals>
+            <configuration>
+              <systemPropertyVariables>
+                <native.image.path>${project.build.directory}/${project.build.finalName}-runner</native.image.path>
+                <java.util.logging.manager>org.jboss.logmanager.LogManager</java.util.logging.manager>
+                <maven.home>${maven.home}</maven.home>
+              </systemPropertyVariables>
+            </configuration>
+          </execution>
+        </executions>
+      </plugin>
+    </plugins>
+  </build>
 </project>
```

