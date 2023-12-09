# quarkus/springboot
## Description
This ruleset gives hints to migrate from SpringBoot devtools to Quarkus
* Source of rules: https://github.com/konveyor/rulesets/tree/main/default/generated
## Violations
Number of Violations: 9
### #0 - cdi-to-quarkus-00030
* Category: potential
* Effort: 3
* Description: `beans.xml` descriptor content is ignored
`beans.xml` descriptor content is ignored and it could be removed from the application.. Refer to the guide referenced below to check the supported CDI feature in Quarkus.
* Labels: konveyor.io/source=java-ee, konveyor.io/target=quarkus
* Incidents
  * file:///tmp/source-code/src/main/webapp/WEB-INF/beans.xml
      * `beans.xml` descriptor content is ignored and it could be removed from the application.. Refer to the guide referenced below to check the supported CDI feature in Quarkus.
### #1 - dependency-removal-for-quarkus-00000
* Category: mandatory
* Effort: 1
* Description: Remove non-quarkus dependencies
Non-quarkus dependencies are no longer required and can be removed.
* Labels: konveyor.io/source=java-ee, konveyor.io/target=quarkus
* Links
  * Quarkus - Guide: https://quarkus.io/guides
* Incidents
  * file:///tmp/source-code/pom.xml
      * Non-quarkus dependencies are no longer required and can be removed.
      * Code Snippet:
```java
 41  		<product.name>JBoss EAP</product.name>
 42  		<product.version>7.4.0.GA</product.version>
 43  		<!-- A base list of dependency and plug-in version used in the various
 44  		quick starts. -->
 45  		<version.org.asciidoctor.asciidoctor-maven-plugin>2.1.0</version.org.asciidoctor.asciidoctor-maven-plugin>
 46  		<version.wildfly.maven.plugin>2.0.2.Final</version.wildfly.maven.plugin>
 47  		<version.org.wildfly.checkstyle-config>1.0.7.Final</version.org.wildfly.checkstyle-config>
 48  		<version.org.wildfly.quickstarts.documentation.plugin>2.3.0.Final</version.org.wildfly.quickstarts.documentation.plugin>
 49  		<!-- other plug-in versions -->
 50  		<version.com.mycyla.license>3.0</version.com.mycyla.license>
 51  		<version.checkstyle>8.5</version.checkstyle>
 52  		<version.jaxws-tools-maven-plugin>1.2.3.Final</version.jaxws-tools-maven-plugin>
 53  		<!-- Explicitly declaring the source encoding eliminates the following
 54  		message: [WARNING] Using platform encoding (UTF-8 actually) to copy
 55  		filtered resources, i.e. build is platform dependent! -->
 56  		<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
 57  
 58  		<!-- Protocol to use for communication with remote maven repositories.
 59  		You can set to 'http' if you are using a maven proxy and 'https'
 60  		interferes with that. Use 'https' for builds that will be released
 61                       to
 62  		non-snapshot public maven repos -->
 63  		<maven.repository.protocol>https</maven.repository.protocol>
 64  		<!-- The full remote maven repo URL; can be overridden via -D for
 65  		special use cases -->
 66  		<maven.repository.url>
 67  			${maven.repository.protocol}://repository.jboss.org/nexus/content/groups/public/</maven.repository.url>
 68  		<!-- https://access.redhat.com/maven-repository -->
 69  		<maven.redhat.repository.url>
 70  			${maven.repository.protocol}://maven.repository.redhat.com/ga/</maven.redhat.repository.url>
 71  
 72  		<!-- Version of BOMs
 73          note: a SNAPSHOT version *requires*
 74  		checkout of BOMs at https://github.com/wildfly/boms and build through
 75  		"mvn clean install"
 76          -->
 77  		<version.server.bom>7.4.0.GA</version.server.bom>
 78  
 79  		<!-- Versions of unmanaged dependencies -->
 80  		<version.arquillian.angularjs.graphene>1.2.0.Beta1</version.arquillian.angularjs.graphene>
 81  		<version.org.json>20150729</version.org.json>
 82  		<version.ro.isdc.wro4j>1.7.9</version.ro.isdc.wro4j>
 83  
 84  		<jboss.developer.drupal.url>http://rhdp-drupal.stage.redhat.com/</jboss.developer.drupal.url>
 85  		<linkXRef>false</linkXRef>
 86  		<version.microprofile.bom>3.0.0.GA</version.microprofile.bom>
 87  		<version.war.plugin>3.3.2</version.war.plugin>
 88  	</properties>
 89  	<repositories>
 90  		<repository>
 91  			<releases>
 92  				<enabled>true</enabled>
 93  				<updatePolicy>never</updatePolicy>
 94  			</releases>
 95  			<snapshots>
 96  				<enabled>true</enabled>
 97  				<updatePolicy>never</updatePolicy>
 98  			</snapshots>
 99  			<id>jboss-public-repository-group</id>
100  			<name>JBoss Public Repository Group</name>
101  			<url>${maven.repository.url}</url>
102  			<layout>default</layout>
103  		</repository>
104  		<repository>
105  			<releases>
106  				<enabled>true</enabled>
107  				<updatePolicy>never</updatePolicy>
108  			</releases>
109  			<snapshots>
110  				<enabled>true</enabled>
111  				<updatePolicy>never</updatePolicy>
112  			</snapshots>
113  			<id>jboss-enterprise-maven-repository</id>
114  			<name>JBoss Enterprise Maven Repository</name>
115  			<url>${maven.redhat.repository.url}</url>
116  			<layout>default</layout>
117  		</repository>
118  	</repositories>
119  	<dependencyManagement>
120  
121  		<dependencies>
122  			<!-- importing the jakartaee8-with-tools BOM adds specs and other
123  			useful artifacts as managed dependencies -->
124  			<dependency>
125  				<groupId>org.jboss.bom</groupId>
126  				<artifactId>jboss-eap-jakartaee8-with-tools</artifactId>
127  				<version>${version.server.bom}</version>
128  				<type>pom</type>
129  				<scope>import</scope>
130  			</dependency>
131  		</dependencies>
132  	</dependencyManagement>
133      <dependencies>
134          <dependency>
135              <groupId>jakarta.enterprise</groupId>
136              <artifactId>jakarta.enterprise.cdi-api</artifactId>
137              <scope>provided</scope>
138          </dependency>
139          <dependency>
140              <groupId>org.jboss.spec.javax.ejb</groupId>
141              <artifactId>jboss-ejb-api_3.2_spec</artifactId>
142              <scope>provided</scope>
143          </dependency>
144          <dependency>
145              <groupId>org.jboss.spec.javax.jms</groupId>
146              <artifactId>jboss-jms-api_2.0_spec</artifactId>
147              <scope>provided</scope>
148          </dependency>
149          <!-- Import the Servlet API, we use provided scope as the API is
150              included in JBoss EAP -->
151          <dependency>
152              <groupId>org.jboss.spec.javax.servlet</groupId>
153              <artifactId>jboss-servlet-api_4.0_spec</artifactId>
154              <scope>provided</scope>
155          </dependency>
156          <dependency>
157              <groupId>org.jboss.spec.javax.annotation</groupId>
158              <artifactId>jboss-annotations-api_1.3_spec</artifactId>
159              <scope>provided</scope>
160          </dependency>
161  
162      </dependencies>
163  <build>
164  		<!-- Set the name of the WAR, used as the context root when the app is
165  		deployed -->
166  		<finalName>${project.artifactId}</finalName>
167  		<plugins>
168  			<plugin>
169  				<artifactId>maven-war-plugin</artifactId>
170  				<version>2.4</version>
171  				<configuration>
172  					<failOnMissingWebXml>false</failOnMissingWebXml>
173  				</configuration>
174  			</plugin>
175  			<plugin>
176  				<groupId>org.wildfly.plugins</groupId>
177  				<artifactId>wildfly-maven-plugin</artifactId>
178  				<version>${version.wildfly.maven.plugin}</version>
179  			</plugin>
180  		</plugins>
181  	</build>
182  	<profiles>
183  		<profile>
184  			<!-- When built in OpenShift the 'openshift' profile will be
185                  used
186  			when invoking mvn. -->
187  			<!-- Use this profile for any OpenShift specific customization
188                  your
189  			app will ne    ed. -->
190  			<!-- By default that is to put the resulting archive into the
191  			'deployments' folder. -->
192  			<!--
193  			http://maven.apache.org/guides/mini/guide-building-for-different-environments.html -->
194  			<id>openshift</id>
195  			<build>
196  				<plugins>
197  					<plugin>
198  						<groupId>org.apache.maven.plugins</groupId>
199  						<artifactId>maven-war-plugin</artifactId>
200  						<version>${version.war.plugin}</version>
201  						<configuration>
202  							<warName>ROOT</warName>
203  						</configuration>
204  					</plugin>
205  					<plugin>
206  						<groupId>org.apache.maven.plugins</groupId>
207  						<artifactId>maven-source-plugin</artifactId>
208  						<executions>
209  							<execution>
210  								<id>attach-sources</id>
211  								<phase>none</phase>
212  							</execution>
213  						</executions>
214  					</plugin>
215  				</plugins>
216  			</build>
217  		</profile>
218  	</profiles>
219  </project>

```
  * file:///tmp/source-code/pom.xml
      * Non-quarkus dependencies are no longer required and can be removed.
      * Code Snippet:
```java
 58  		<!-- Protocol to use for communication with remote maven repositories.
 59  		You can set to 'http' if you are using a maven proxy and 'https'
 60  		interferes with that. Use 'https' for builds that will be released
 61                       to
 62  		non-snapshot public maven repos -->
 63  		<maven.repository.protocol>https</maven.repository.protocol>
 64  		<!-- The full remote maven repo URL; can be overridden via -D for
 65  		special use cases -->
 66  		<maven.repository.url>
 67  			${maven.repository.protocol}://repository.jboss.org/nexus/content/groups/public/</maven.repository.url>
 68  		<!-- https://access.redhat.com/maven-repository -->
 69  		<maven.redhat.repository.url>
 70  			${maven.repository.protocol}://maven.repository.redhat.com/ga/</maven.redhat.repository.url>
 71  
 72  		<!-- Version of BOMs
 73          note: a SNAPSHOT version *requires*
 74  		checkout of BOMs at https://github.com/wildfly/boms and build through
 75  		"mvn clean install"
 76          -->
 77  		<version.server.bom>7.4.0.GA</version.server.bom>
 78  
 79  		<!-- Versions of unmanaged dependencies -->
 80  		<version.arquillian.angularjs.graphene>1.2.0.Beta1</version.arquillian.angularjs.graphene>
 81  		<version.org.json>20150729</version.org.json>
 82  		<version.ro.isdc.wro4j>1.7.9</version.ro.isdc.wro4j>
 83  
 84  		<jboss.developer.drupal.url>http://rhdp-drupal.stage.redhat.com/</jboss.developer.drupal.url>
 85  		<linkXRef>false</linkXRef>
 86  		<version.microprofile.bom>3.0.0.GA</version.microprofile.bom>
 87  		<version.war.plugin>3.3.2</version.war.plugin>
 88  	</properties>
 89  	<repositories>
 90  		<repository>
 91  			<releases>
 92  				<enabled>true</enabled>
 93  				<updatePolicy>never</updatePolicy>
 94  			</releases>
 95  			<snapshots>
 96  				<enabled>true</enabled>
 97  				<updatePolicy>never</updatePolicy>
 98  			</snapshots>
 99  			<id>jboss-public-repository-group</id>
100  			<name>JBoss Public Repository Group</name>
101  			<url>${maven.repository.url}</url>
102  			<layout>default</layout>
103  		</repository>
104  		<repository>
105  			<releases>
106  				<enabled>true</enabled>
107  				<updatePolicy>never</updatePolicy>
108  			</releases>
109  			<snapshots>
110  				<enabled>true</enabled>
111  				<updatePolicy>never</updatePolicy>
112  			</snapshots>
113  			<id>jboss-enterprise-maven-repository</id>
114  			<name>JBoss Enterprise Maven Repository</name>
115  			<url>${maven.redhat.repository.url}</url>
116  			<layout>default</layout>
117  		</repository>
118  	</repositories>
119  	<dependencyManagement>
120  
121  		<dependencies>
122  			<!-- importing the jakartaee8-with-tools BOM adds specs and other
123  			useful artifacts as managed dependencies -->
124  			<dependency>
125  				<groupId>org.jboss.bom</groupId>
126  				<artifactId>jboss-eap-jakartaee8-with-tools</artifactId>
127  				<version>${version.server.bom}</version>
128  				<type>pom</type>
129  				<scope>import</scope>
130  			</dependency>
131  		</dependencies>
132  	</dependencyManagement>
133      <dependencies>
134          <dependency>
135              <groupId>jakarta.enterprise</groupId>
136              <artifactId>jakarta.enterprise.cdi-api</artifactId>
137              <scope>provided</scope>
138          </dependency>
139          <dependency>
140              <groupId>org.jboss.spec.javax.ejb</groupId>
141              <artifactId>jboss-ejb-api_3.2_spec</artifactId>
142              <scope>provided</scope>
143          </dependency>
144          <dependency>
145              <groupId>org.jboss.spec.javax.jms</groupId>
146              <artifactId>jboss-jms-api_2.0_spec</artifactId>
147              <scope>provided</scope>
148          </dependency>
149          <!-- Import the Servlet API, we use provided scope as the API is
150              included in JBoss EAP -->
151          <dependency>
152              <groupId>org.jboss.spec.javax.servlet</groupId>
153              <artifactId>jboss-servlet-api_4.0_spec</artifactId>
154              <scope>provided</scope>
155          </dependency>
156          <dependency>
157              <groupId>org.jboss.spec.javax.annotation</groupId>
158              <artifactId>jboss-annotations-api_1.3_spec</artifactId>
159              <scope>provided</scope>
160          </dependency>
161  
162      </dependencies>
163  <build>
164  		<!-- Set the name of the WAR, used as the context root when the app is
165  		deployed -->
166  		<finalName>${project.artifactId}</finalName>
167  		<plugins>
168  			<plugin>
169  				<artifactId>maven-war-plugin</artifactId>
170  				<version>2.4</version>
171  				<configuration>
172  					<failOnMissingWebXml>false</failOnMissingWebXml>
173  				</configuration>
174  			</plugin>
175  			<plugin>
176  				<groupId>org.wildfly.plugins</groupId>
177  				<artifactId>wildfly-maven-plugin</artifactId>
178  				<version>${version.wildfly.maven.plugin}</version>
179  			</plugin>
180  		</plugins>
181  	</build>
182  	<profiles>
183  		<profile>
184  			<!-- When built in OpenShift the 'openshift' profile will be
185                  used
186  			when invoking mvn. -->
187  			<!-- Use this profile for any OpenShift specific customization
188                  your
189  			app will ne    ed. -->
190  			<!-- By default that is to put the resulting archive into the
191  			'deployments' folder. -->
192  			<!--
193  			http://maven.apache.org/guides/mini/guide-building-for-different-environments.html -->
194  			<id>openshift</id>
195  			<build>
196  				<plugins>
197  					<plugin>
198  						<groupId>org.apache.maven.plugins</groupId>
199  						<artifactId>maven-war-plugin</artifactId>
200  						<version>${version.war.plugin}</version>
201  						<configuration>
202  							<warName>ROOT</warName>
203  						</configuration>
204  					</plugin>
205  					<plugin>
206  						<groupId>org.apache.maven.plugins</groupId>
207  						<artifactId>maven-source-plugin</artifactId>
208  						<executions>
209  							<execution>
210  								<id>attach-sources</id>
211  								<phase>none</phase>
212  							</execution>
213  						</executions>
214  					</plugin>
215  				</plugins>
216  			</build>
217  		</profile>
218  	</profiles>
219  </project>

```
### #2 - javaee-pom-to-quarkus-00000
* Category: mandatory
* Effort: 1
* Description: The expected project artifact's extension is `jar`

* Labels: konveyor.io/source=java-ee, konveyor.io/target=quarkus
* Links
  * Quarkus - Guide: https://quarkus.io/guides/maven-tooling#build-tool-maven
* Incidents
  * file:///tmp/source-code/pom.xml
      * The project artifact's current extension (i.e. `<packaging>` tag value) is `` but the expected value should be `jar`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <!--
  3      JBoss, Home of Professional Open Source
  4      Copyright 2015, Red Hat, Inc. and/or its affiliates, and individual
  5      contributors by the @authors tag. See the copyright.txt in the
  6      distribution for a full listing of individual contributors.
  7  
  8      Licensed under the Apache License, Version 2.0 (the "License");
  9      you may not use this file except in compliance with the License.
 10      You may obtain a copy of the License at
 11      http://www.apache.org/licenses/LICENSE-2.0
 12      Unless required by applicable law or agreed to in writing, software
 13      distributed under the License is distributed on an "AS IS" BASIS,
 14      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 15      See the License for the specific language governing permissions and
 16      limitations under the License.
 17  -->
 18  <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
 19      <modelVersion>4.0.0</modelVersion>
 20      <groupId>org.jboss.eap.quickstarts</groupId>
 21      <version>7.4.0.GA</version>
 22      <artifactId>helloworld-mdb</artifactId>
 23      <packaging>war</packaging>
 24      <name>Quickstart: helloworld-mdb</name>
 25      <description>This project demonstrates a hello world Message-Driven Bean with Servlet 3.0 as client</description>
 26  
 27      <licenses>
 28          <license>
 29              <name>Apache License, Version 2.0</name>
 30              <url>http://www.apache.org/licenses/LICENSE-2.0.html</url>
 31              <distribution>repo</distribution>
 32          </license>
 33      </licenses>
 34  <properties>
 35  
 36  		<maven.compiler.source>1.8</maven.compiler.source>
 37  		<maven.compiler.target>1.8</maven.compiler.target>
 38  
 39  		<root.dir>${project.basedir}</root.dir>
 40  		<jboss.home.name>EAP7_HOME</jboss.home.name>
 41  		<product.name>JBoss EAP</product.name>
 42  		<product.version>7.4.0.GA</product.version>
 43  		<!-- A base list of dependency and plug-in version used in the various
 44  		quick starts. -->
 45  		<version.org.asciidoctor.asciidoctor-maven-plugin>2.1.0</version.org.asciidoctor.asciidoctor-maven-plugin>
 46  		<version.wildfly.maven.plugin>2.0.2.Final</version.wildfly.maven.plugin>
 47  		<version.org.wildfly.checkstyle-config>1.0.7.Final</version.org.wildfly.checkstyle-config>
 48  		<version.org.wildfly.quickstarts.documentation.plugin>2.3.0.Final</version.org.wildfly.quickstarts.documentation.plugin>
 49  		<!-- other plug-in versions -->
 50  		<version.com.mycyla.license>3.0</version.com.mycyla.license>
 51  		<version.checkstyle>8.5</version.checkstyle>
 52  		<version.jaxws-tools-maven-plugin>1.2.3.Final</version.jaxws-tools-maven-plugin>
 53  		<!-- Explicitly declaring the source encoding eliminates the following
 54  		message: [WARNING] Using platform encoding (UTF-8 actually) to copy
 55  		filtered resources, i.e. build is platform dependent! -->
 56  		<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
 57  
 58  		<!-- Protocol to use for communication with remote maven repositories.
 59  		You can set to 'http' if you are using a maven proxy and 'https'
 60  		interferes with that. Use 'https' for builds that will be released
 61                       to
 62  		non-snapshot public maven repos -->
 63  		<maven.repository.protocol>https</maven.repository.protocol>
 64  		<!-- The full remote maven repo URL; can be overridden via -D for
 65  		special use cases -->
 66  		<maven.repository.url>
 67  			${maven.repository.protocol}://repository.jboss.org/nexus/content/groups/public/</maven.repository.url>
 68  		<!-- https://access.redhat.com/maven-repository -->
 69  		<maven.redhat.repository.url>
 70  			${maven.repository.protocol}://maven.repository.redhat.com/ga/</maven.redhat.repository.url>
 71  
 72  		<!-- Version of BOMs
 73          note: a SNAPSHOT version *requires*
 74  		checkout of BOMs at https://github.com/wildfly/boms and build through
 75  		"mvn clean install"
 76          -->
 77  		<version.server.bom>7.4.0.GA</version.server.bom>
 78  
 79  		<!-- Versions of unmanaged dependencies -->
 80  		<version.arquillian.angularjs.graphene>1.2.0.Beta1</version.arquillian.angularjs.graphene>
 81  		<version.org.json>20150729</version.org.json>
 82  		<version.ro.isdc.wro4j>1.7.9</version.ro.isdc.wro4j>
 83  
 84  		<jboss.developer.drupal.url>http://rhdp-drupal.stage.redhat.com/</jboss.developer.drupal.url>
 85  		<linkXRef>false</linkXRef>
 86  		<version.microprofile.bom>3.0.0.GA</version.microprofile.bom>
 87  		<version.war.plugin>3.3.2</version.war.plugin>
 88  	</properties>
 89  	<repositories>
 90  		<repository>
 91  			<releases>
 92  				<enabled>true</enabled>
 93  				<updatePolicy>never</updatePolicy>
 94  			</releases>
 95  			<snapshots>
 96  				<enabled>true</enabled>
 97  				<updatePolicy>never</updatePolicy>
 98  			</snapshots>
 99  			<id>jboss-public-repository-group</id>
100  			<name>JBoss Public Repository Group</name>
101  			<url>${maven.repository.url}</url>
102  			<layout>default</layout>
103  		</repository>
104  		<repository>
105  			<releases>
106  				<enabled>true</enabled>
107  				<updatePolicy>never</updatePolicy>
108  			</releases>
109  			<snapshots>
110  				<enabled>true</enabled>
111  				<updatePolicy>never</updatePolicy>
112  			</snapshots>
113  			<id>jboss-enterprise-maven-repository</id>
```
### #3 - javaee-pom-to-quarkus-00010
* Category: mandatory
* Effort: 1
* Description: Adopt Quarkus BOM

* Labels: konveyor.io/source=java-ee, konveyor.io/target=quarkus
* Links
  * Quarkus - Guide: https://quarkus.io/guides/maven-tooling#build-tool-maven
  * Quarkus - Releases: https://quarkus.io/blog/tag/release/
* Incidents
  * file:///tmp/source-code/pom.xml
      * Use the Quarkus BOM to omit the version of the different Quarkus dependencies.. Add the following sections to the `pom.xml` file:. ```xml. <properties>. <quarkus.platform.artifact-id>quarkus-bom</quarkus.platform.artifact-id>. <quarkus.platform.group-id>io.quarkus.platform</quarkus.platform.group-id>. <quarkus.platform.version>3.1.0.Final</quarkus.platform.version>. </properties>. <dependencyManagement>. <dependencies>. <dependency>. <groupId>$</groupId>. <artifactId>$</artifactId>. <version>$</version>. <type>pom</type>. <scope>import</scope>. </dependency>. </dependencies>. </dependencyManagement>. ```. Check the latest Quarkus version available from the `Quarkus - Releases` link below.
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <!--
  3      JBoss, Home of Professional Open Source
  4      Copyright 2015, Red Hat, Inc. and/or its affiliates, and individual
  5      contributors by the @authors tag. See the copyright.txt in the
  6      distribution for a full listing of individual contributors.
  7  
  8      Licensed under the Apache License, Version 2.0 (the "License");
  9      you may not use this file except in compliance with the License.
 10      You may obtain a copy of the License at
 11      http://www.apache.org/licenses/LICENSE-2.0
 12      Unless required by applicable law or agreed to in writing, software
 13      distributed under the License is distributed on an "AS IS" BASIS,
 14      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 15      See the License for the specific language governing permissions and
 16      limitations under the License.
 17  -->
 18  <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
 19      <modelVersion>4.0.0</modelVersion>
 20      <groupId>org.jboss.eap.quickstarts</groupId>
 21      <version>7.4.0.GA</version>
 22      <artifactId>helloworld-mdb</artifactId>
 23      <packaging>war</packaging>
 24      <name>Quickstart: helloworld-mdb</name>
 25      <description>This project demonstrates a hello world Message-Driven Bean with Servlet 3.0 as client</description>
 26  
 27      <licenses>
 28          <license>
 29              <name>Apache License, Version 2.0</name>
 30              <url>http://www.apache.org/licenses/LICENSE-2.0.html</url>
 31              <distribution>repo</distribution>
 32          </license>
 33      </licenses>
 34  <properties>
 35  
 36  		<maven.compiler.source>1.8</maven.compiler.source>
 37  		<maven.compiler.target>1.8</maven.compiler.target>
 38  
 39  		<root.dir>${project.basedir}</root.dir>
 40  		<jboss.home.name>EAP7_HOME</jboss.home.name>
 41  		<product.name>JBoss EAP</product.name>
 42  		<product.version>7.4.0.GA</product.version>
 43  		<!-- A base list of dependency and plug-in version used in the various
 44  		quick starts. -->
 45  		<version.org.asciidoctor.asciidoctor-maven-plugin>2.1.0</version.org.asciidoctor.asciidoctor-maven-plugin>
 46  		<version.wildfly.maven.plugin>2.0.2.Final</version.wildfly.maven.plugin>
 47  		<version.org.wildfly.checkstyle-config>1.0.7.Final</version.org.wildfly.checkstyle-config>
 48  		<version.org.wildfly.quickstarts.documentation.plugin>2.3.0.Final</version.org.wildfly.quickstarts.documentation.plugin>
 49  		<!-- other plug-in versions -->
 50  		<version.com.mycyla.license>3.0</version.com.mycyla.license>
 51  		<version.checkstyle>8.5</version.checkstyle>
 52  		<version.jaxws-tools-maven-plugin>1.2.3.Final</version.jaxws-tools-maven-plugin>
 53  		<!-- Explicitly declaring the source encoding eliminates the following
 54  		message: [WARNING] Using platform encoding (UTF-8 actually) to copy
 55  		filtered resources, i.e. build is platform dependent! -->
 56  		<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
 57  
 58  		<!-- Protocol to use for communication with remote maven repositories.
 59  		You can set to 'http' if you are using a maven proxy and 'https'
 60  		interferes with that. Use 'https' for builds that will be released
 61                       to
 62  		non-snapshot public maven repos -->
 63  		<maven.repository.protocol>https</maven.repository.protocol>
 64  		<!-- The full remote maven repo URL; can be overridden via -D for
 65  		special use cases -->
 66  		<maven.repository.url>
 67  			${maven.repository.protocol}://repository.jboss.org/nexus/content/groups/public/</maven.repository.url>
 68  		<!-- https://access.redhat.com/maven-repository -->
 69  		<maven.redhat.repository.url>
 70  			${maven.repository.protocol}://maven.repository.redhat.com/ga/</maven.redhat.repository.url>
 71  
 72  		<!-- Version of BOMs
 73          note: a SNAPSHOT version *requires*
 74  		checkout of BOMs at https://github.com/wildfly/boms and build through
 75  		"mvn clean install"
 76          -->
 77  		<version.server.bom>7.4.0.GA</version.server.bom>
 78  
 79  		<!-- Versions of unmanaged dependencies -->
 80  		<version.arquillian.angularjs.graphene>1.2.0.Beta1</version.arquillian.angularjs.graphene>
 81  		<version.org.json>20150729</version.org.json>
 82  		<version.ro.isdc.wro4j>1.7.9</version.ro.isdc.wro4j>
 83  
 84  		<jboss.developer.drupal.url>http://rhdp-drupal.stage.redhat.com/</jboss.developer.drupal.url>
 85  		<linkXRef>false</linkXRef>
 86  		<version.microprofile.bom>3.0.0.GA</version.microprofile.bom>
 87  		<version.war.plugin>3.3.2</version.war.plugin>
 88  	</properties>
 89  	<repositories>
 90  		<repository>
 91  			<releases>
 92  				<enabled>true</enabled>
 93  				<updatePolicy>never</updatePolicy>
 94  			</releases>
 95  			<snapshots>
 96  				<enabled>true</enabled>
 97  				<updatePolicy>never</updatePolicy>
 98  			</snapshots>
 99  			<id>jboss-public-repository-group</id>
100  			<name>JBoss Public Repository Group</name>
101  			<url>${maven.repository.url}</url>
102  			<layout>default</layout>
103  		</repository>
104  		<repository>
105  			<releases>
106  				<enabled>true</enabled>
107  				<updatePolicy>never</updatePolicy>
108  			</releases>
109  			<snapshots>
110  				<enabled>true</enabled>
111  				<updatePolicy>never</updatePolicy>
112  			</snapshots>
113  			<id>jboss-enterprise-maven-repository</id>
114  			<name>JBoss Enterprise Maven Repository</name>
115  			<url>${maven.redhat.repository.url}</url>
116  			<layout>default</layout>
117  		</repository>
118  	</repositories>
119  	<dependencyManagement>
120  
```
### #4 - javaee-pom-to-quarkus-00020
* Category: mandatory
* Effort: 1
* Description: Adopt Quarkus Maven plugin

* Labels: konveyor.io/source=java-ee, konveyor.io/target=quarkus
* Links
  * Quarkus - Guide: https://quarkus.io/guides/maven-tooling#build-tool-maven
* Incidents
  * file:///tmp/source-code/pom.xml
      * Use the Quarkus Maven plugin adding the following sections to the `pom.xml` file:. ```xml. <properties>. <quarkus.platform.group-id>io.quarkus.platform</quarkus.platform.group-id>. <quarkus.platform.version>3.1.0.Final</quarkus.platform.version>. </properties>. <build>. <plugins>. <plugin>. <groupId>$</groupId>. <artifactId>quarkus-maven-plugin</artifactId>. <version>$</version>. <extensions>true</extensions>. <executions>. <execution>. <goals>. <goal>build</goal>. <goal>generate-code</goal>. <goal>generate-code-tests</goal>. </goals>. </execution>. </executions>. </plugin>. </plugins>. </build>. ```
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <!--
  3      JBoss, Home of Professional Open Source
  4      Copyright 2015, Red Hat, Inc. and/or its affiliates, and individual
  5      contributors by the @authors tag. See the copyright.txt in the
  6      distribution for a full listing of individual contributors.
  7  
  8      Licensed under the Apache License, Version 2.0 (the "License");
  9      you may not use this file except in compliance with the License.
 10      You may obtain a copy of the License at
 11      http://www.apache.org/licenses/LICENSE-2.0
 12      Unless required by applicable law or agreed to in writing, software
 13      distributed under the License is distributed on an "AS IS" BASIS,
 14      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 15      See the License for the specific language governing permissions and
 16      limitations under the License.
 17  -->
 18  <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
 19      <modelVersion>4.0.0</modelVersion>
 20      <groupId>org.jboss.eap.quickstarts</groupId>
 21      <version>7.4.0.GA</version>
 22      <artifactId>helloworld-mdb</artifactId>
 23      <packaging>war</packaging>
 24      <name>Quickstart: helloworld-mdb</name>
 25      <description>This project demonstrates a hello world Message-Driven Bean with Servlet 3.0 as client</description>
 26  
 27      <licenses>
 28          <license>
 29              <name>Apache License, Version 2.0</name>
 30              <url>http://www.apache.org/licenses/LICENSE-2.0.html</url>
 31              <distribution>repo</distribution>
 32          </license>
 33      </licenses>
 34  <properties>
 35  
 36  		<maven.compiler.source>1.8</maven.compiler.source>
 37  		<maven.compiler.target>1.8</maven.compiler.target>
 38  
 39  		<root.dir>${project.basedir}</root.dir>
 40  		<jboss.home.name>EAP7_HOME</jboss.home.name>
 41  		<product.name>JBoss EAP</product.name>
 42  		<product.version>7.4.0.GA</product.version>
 43  		<!-- A base list of dependency and plug-in version used in the various
 44  		quick starts. -->
 45  		<version.org.asciidoctor.asciidoctor-maven-plugin>2.1.0</version.org.asciidoctor.asciidoctor-maven-plugin>
 46  		<version.wildfly.maven.plugin>2.0.2.Final</version.wildfly.maven.plugin>
 47  		<version.org.wildfly.checkstyle-config>1.0.7.Final</version.org.wildfly.checkstyle-config>
 48  		<version.org.wildfly.quickstarts.documentation.plugin>2.3.0.Final</version.org.wildfly.quickstarts.documentation.plugin>
 49  		<!-- other plug-in versions -->
 50  		<version.com.mycyla.license>3.0</version.com.mycyla.license>
 51  		<version.checkstyle>8.5</version.checkstyle>
 52  		<version.jaxws-tools-maven-plugin>1.2.3.Final</version.jaxws-tools-maven-plugin>
 53  		<!-- Explicitly declaring the source encoding eliminates the following
 54  		message: [WARNING] Using platform encoding (UTF-8 actually) to copy
 55  		filtered resources, i.e. build is platform dependent! -->
 56  		<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
 57  
 58  		<!-- Protocol to use for communication with remote maven repositories.
 59  		You can set to 'http' if you are using a maven proxy and 'https'
 60  		interferes with that. Use 'https' for builds that will be released
 61                       to
 62  		non-snapshot public maven repos -->
 63  		<maven.repository.protocol>https</maven.repository.protocol>
 64  		<!-- The full remote maven repo URL; can be overridden via -D for
 65  		special use cases -->
 66  		<maven.repository.url>
 67  			${maven.repository.protocol}://repository.jboss.org/nexus/content/groups/public/</maven.repository.url>
 68  		<!-- https://access.redhat.com/maven-repository -->
 69  		<maven.redhat.repository.url>
 70  			${maven.repository.protocol}://maven.repository.redhat.com/ga/</maven.redhat.repository.url>
 71  
 72  		<!-- Version of BOMs
 73          note: a SNAPSHOT version *requires*
 74  		checkout of BOMs at https://github.com/wildfly/boms and build through
 75  		"mvn clean install"
 76          -->
 77  		<version.server.bom>7.4.0.GA</version.server.bom>
 78  
 79  		<!-- Versions of unmanaged dependencies -->
 80  		<version.arquillian.angularjs.graphene>1.2.0.Beta1</version.arquillian.angularjs.graphene>
 81  		<version.org.json>20150729</version.org.json>
 82  		<version.ro.isdc.wro4j>1.7.9</version.ro.isdc.wro4j>
 83  
 84  		<jboss.developer.drupal.url>http://rhdp-drupal.stage.redhat.com/</jboss.developer.drupal.url>
 85  		<linkXRef>false</linkXRef>
 86  		<version.microprofile.bom>3.0.0.GA</version.microprofile.bom>
 87  		<version.war.plugin>3.3.2</version.war.plugin>
 88  	</properties>
 89  	<repositories>
 90  		<repository>
 91  			<releases>
 92  				<enabled>true</enabled>
 93  				<updatePolicy>never</updatePolicy>
 94  			</releases>
 95  			<snapshots>
 96  				<enabled>true</enabled>
 97  				<updatePolicy>never</updatePolicy>
 98  			</snapshots>
 99  			<id>jboss-public-repository-group</id>
100  			<name>JBoss Public Repository Group</name>
101  			<url>${maven.repository.url}</url>
102  			<layout>default</layout>
103  		</repository>
104  		<repository>
105  			<releases>
106  				<enabled>true</enabled>
107  				<updatePolicy>never</updatePolicy>
108  			</releases>
109  			<snapshots>
110  				<enabled>true</enabled>
111  				<updatePolicy>never</updatePolicy>
112  			</snapshots>
113  			<id>jboss-enterprise-maven-repository</id>
114  			<name>JBoss Enterprise Maven Repository</name>
115  			<url>${maven.redhat.repository.url}</url>
116  			<layout>default</layout>
117  		</repository>
118  	</repositories>
119  	<dependencyManagement>
120  
```
### #5 - javaee-pom-to-quarkus-00030
* Category: mandatory
* Effort: 1
* Description: Adopt Maven Compiler plugin

* Labels: konveyor.io/source=java-ee, konveyor.io/target=quarkus
* Links
  * Quarkus - Guide: https://quarkus.io/guides/maven-tooling#build-tool-maven
* Incidents
  * file:///tmp/source-code/pom.xml
      * Use the Maven Compiler plugin adding the following sections to the `pom.xml` file:. ```xml. <properties>. <compiler-plugin.version>3.10.1</compiler-plugin.version>. <maven.compiler.release>11</maven.compiler.release>. </properties>. <build>. <plugins>. <plugin>. <artifactId>maven-compiler-plugin</artifactId>. <version>$</version>. <configuration>. <compilerArgs>. <arg>-parameters</arg>. </compilerArgs>. </configuration>. </plugin>. </plugins>. </build>. ```
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <!--
  3      JBoss, Home of Professional Open Source
  4      Copyright 2015, Red Hat, Inc. and/or its affiliates, and individual
  5      contributors by the @authors tag. See the copyright.txt in the
  6      distribution for a full listing of individual contributors.
  7  
  8      Licensed under the Apache License, Version 2.0 (the "License");
  9      you may not use this file except in compliance with the License.
 10      You may obtain a copy of the License at
 11      http://www.apache.org/licenses/LICENSE-2.0
 12      Unless required by applicable law or agreed to in writing, software
 13      distributed under the License is distributed on an "AS IS" BASIS,
 14      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 15      See the License for the specific language governing permissions and
 16      limitations under the License.
 17  -->
 18  <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
 19      <modelVersion>4.0.0</modelVersion>
 20      <groupId>org.jboss.eap.quickstarts</groupId>
 21      <version>7.4.0.GA</version>
 22      <artifactId>helloworld-mdb</artifactId>
 23      <packaging>war</packaging>
 24      <name>Quickstart: helloworld-mdb</name>
 25      <description>This project demonstrates a hello world Message-Driven Bean with Servlet 3.0 as client</description>
 26  
 27      <licenses>
 28          <license>
 29              <name>Apache License, Version 2.0</name>
 30              <url>http://www.apache.org/licenses/LICENSE-2.0.html</url>
 31              <distribution>repo</distribution>
 32          </license>
 33      </licenses>
 34  <properties>
 35  
 36  		<maven.compiler.source>1.8</maven.compiler.source>
 37  		<maven.compiler.target>1.8</maven.compiler.target>
 38  
 39  		<root.dir>${project.basedir}</root.dir>
 40  		<jboss.home.name>EAP7_HOME</jboss.home.name>
 41  		<product.name>JBoss EAP</product.name>
 42  		<product.version>7.4.0.GA</product.version>
 43  		<!-- A base list of dependency and plug-in version used in the various
 44  		quick starts. -->
 45  		<version.org.asciidoctor.asciidoctor-maven-plugin>2.1.0</version.org.asciidoctor.asciidoctor-maven-plugin>
 46  		<version.wildfly.maven.plugin>2.0.2.Final</version.wildfly.maven.plugin>
 47  		<version.org.wildfly.checkstyle-config>1.0.7.Final</version.org.wildfly.checkstyle-config>
 48  		<version.org.wildfly.quickstarts.documentation.plugin>2.3.0.Final</version.org.wildfly.quickstarts.documentation.plugin>
 49  		<!-- other plug-in versions -->
 50  		<version.com.mycyla.license>3.0</version.com.mycyla.license>
 51  		<version.checkstyle>8.5</version.checkstyle>
 52  		<version.jaxws-tools-maven-plugin>1.2.3.Final</version.jaxws-tools-maven-plugin>
 53  		<!-- Explicitly declaring the source encoding eliminates the following
 54  		message: [WARNING] Using platform encoding (UTF-8 actually) to copy
 55  		filtered resources, i.e. build is platform dependent! -->
 56  		<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
 57  
 58  		<!-- Protocol to use for communication with remote maven repositories.
 59  		You can set to 'http' if you are using a maven proxy and 'https'
 60  		interferes with that. Use 'https' for builds that will be released
 61                       to
 62  		non-snapshot public maven repos -->
 63  		<maven.repository.protocol>https</maven.repository.protocol>
 64  		<!-- The full remote maven repo URL; can be overridden via -D for
 65  		special use cases -->
 66  		<maven.repository.url>
 67  			${maven.repository.protocol}://repository.jboss.org/nexus/content/groups/public/</maven.repository.url>
 68  		<!-- https://access.redhat.com/maven-repository -->
 69  		<maven.redhat.repository.url>
 70  			${maven.repository.protocol}://maven.repository.redhat.com/ga/</maven.redhat.repository.url>
 71  
 72  		<!-- Version of BOMs
 73          note: a SNAPSHOT version *requires*
 74  		checkout of BOMs at https://github.com/wildfly/boms and build through
 75  		"mvn clean install"
 76          -->
 77  		<version.server.bom>7.4.0.GA</version.server.bom>
 78  
 79  		<!-- Versions of unmanaged dependencies -->
 80  		<version.arquillian.angularjs.graphene>1.2.0.Beta1</version.arquillian.angularjs.graphene>
 81  		<version.org.json>20150729</version.org.json>
 82  		<version.ro.isdc.wro4j>1.7.9</version.ro.isdc.wro4j>
 83  
 84  		<jboss.developer.drupal.url>http://rhdp-drupal.stage.redhat.com/</jboss.developer.drupal.url>
 85  		<linkXRef>false</linkXRef>
 86  		<version.microprofile.bom>3.0.0.GA</version.microprofile.bom>
 87  		<version.war.plugin>3.3.2</version.war.plugin>
 88  	</properties>
 89  	<repositories>
 90  		<repository>
 91  			<releases>
 92  				<enabled>true</enabled>
 93  				<updatePolicy>never</updatePolicy>
 94  			</releases>
 95  			<snapshots>
 96  				<enabled>true</enabled>
 97  				<updatePolicy>never</updatePolicy>
 98  			</snapshots>
 99  			<id>jboss-public-repository-group</id>
100  			<name>JBoss Public Repository Group</name>
101  			<url>${maven.repository.url}</url>
102  			<layout>default</layout>
103  		</repository>
104  		<repository>
105  			<releases>
106  				<enabled>true</enabled>
107  				<updatePolicy>never</updatePolicy>
108  			</releases>
109  			<snapshots>
110  				<enabled>true</enabled>
111  				<updatePolicy>never</updatePolicy>
112  			</snapshots>
113  			<id>jboss-enterprise-maven-repository</id>
114  			<name>JBoss Enterprise Maven Repository</name>
115  			<url>${maven.redhat.repository.url}</url>
116  			<layout>default</layout>
117  		</repository>
118  	</repositories>
119  	<dependencyManagement>
120  
```
### #6 - javaee-pom-to-quarkus-00040
* Category: mandatory
* Effort: 1
* Description: Adopt Maven Surefire plugin

* Labels: konveyor.io/source=java-ee, konveyor.io/target=quarkus
* Links
  * Quarkus - Guide: https://quarkus.io/guides/maven-tooling#build-tool-maven
* Incidents
  * file:///tmp/source-code/pom.xml
      * Use the Maven Surefire plugin adding the following sections to the `pom.xml` file:. ```xml. <properties>. <surefire-plugin.version>3.0.0</compiler-plugin.version>. </properties>. <build>. <plugins>. <plugin>. <artifactId>maven-surefire-plugin</artifactId>. <version>$</version>. <configuration>. <systemPropertyVariables>. <java.util.logging.manager>org.jboss.logmanager.LogManager</java.util.logging.manager>. <maven.home>$</maven.home>. </systemPropertyVariables>. </configuration>. </plugin>. </plugins>. </build>. ```
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <!--
  3      JBoss, Home of Professional Open Source
  4      Copyright 2015, Red Hat, Inc. and/or its affiliates, and individual
  5      contributors by the @authors tag. See the copyright.txt in the
  6      distribution for a full listing of individual contributors.
  7  
  8      Licensed under the Apache License, Version 2.0 (the "License");
  9      you may not use this file except in compliance with the License.
 10      You may obtain a copy of the License at
 11      http://www.apache.org/licenses/LICENSE-2.0
 12      Unless required by applicable law or agreed to in writing, software
 13      distributed under the License is distributed on an "AS IS" BASIS,
 14      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 15      See the License for the specific language governing permissions and
 16      limitations under the License.
 17  -->
 18  <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
 19      <modelVersion>4.0.0</modelVersion>
 20      <groupId>org.jboss.eap.quickstarts</groupId>
 21      <version>7.4.0.GA</version>
 22      <artifactId>helloworld-mdb</artifactId>
 23      <packaging>war</packaging>
 24      <name>Quickstart: helloworld-mdb</name>
 25      <description>This project demonstrates a hello world Message-Driven Bean with Servlet 3.0 as client</description>
 26  
 27      <licenses>
 28          <license>
 29              <name>Apache License, Version 2.0</name>
 30              <url>http://www.apache.org/licenses/LICENSE-2.0.html</url>
 31              <distribution>repo</distribution>
 32          </license>
 33      </licenses>
 34  <properties>
 35  
 36  		<maven.compiler.source>1.8</maven.compiler.source>
 37  		<maven.compiler.target>1.8</maven.compiler.target>
 38  
 39  		<root.dir>${project.basedir}</root.dir>
 40  		<jboss.home.name>EAP7_HOME</jboss.home.name>
 41  		<product.name>JBoss EAP</product.name>
 42  		<product.version>7.4.0.GA</product.version>
 43  		<!-- A base list of dependency and plug-in version used in the various
 44  		quick starts. -->
 45  		<version.org.asciidoctor.asciidoctor-maven-plugin>2.1.0</version.org.asciidoctor.asciidoctor-maven-plugin>
 46  		<version.wildfly.maven.plugin>2.0.2.Final</version.wildfly.maven.plugin>
 47  		<version.org.wildfly.checkstyle-config>1.0.7.Final</version.org.wildfly.checkstyle-config>
 48  		<version.org.wildfly.quickstarts.documentation.plugin>2.3.0.Final</version.org.wildfly.quickstarts.documentation.plugin>
 49  		<!-- other plug-in versions -->
 50  		<version.com.mycyla.license>3.0</version.com.mycyla.license>
 51  		<version.checkstyle>8.5</version.checkstyle>
 52  		<version.jaxws-tools-maven-plugin>1.2.3.Final</version.jaxws-tools-maven-plugin>
 53  		<!-- Explicitly declaring the source encoding eliminates the following
 54  		message: [WARNING] Using platform encoding (UTF-8 actually) to copy
 55  		filtered resources, i.e. build is platform dependent! -->
 56  		<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
 57  
 58  		<!-- Protocol to use for communication with remote maven repositories.
 59  		You can set to 'http' if you are using a maven proxy and 'https'
 60  		interferes with that. Use 'https' for builds that will be released
 61                       to
 62  		non-snapshot public maven repos -->
 63  		<maven.repository.protocol>https</maven.repository.protocol>
 64  		<!-- The full remote maven repo URL; can be overridden via -D for
 65  		special use cases -->
 66  		<maven.repository.url>
 67  			${maven.repository.protocol}://repository.jboss.org/nexus/content/groups/public/</maven.repository.url>
 68  		<!-- https://access.redhat.com/maven-repository -->
 69  		<maven.redhat.repository.url>
 70  			${maven.repository.protocol}://maven.repository.redhat.com/ga/</maven.redhat.repository.url>
 71  
 72  		<!-- Version of BOMs
 73          note: a SNAPSHOT version *requires*
 74  		checkout of BOMs at https://github.com/wildfly/boms and build through
 75  		"mvn clean install"
 76          -->
 77  		<version.server.bom>7.4.0.GA</version.server.bom>
 78  
 79  		<!-- Versions of unmanaged dependencies -->
 80  		<version.arquillian.angularjs.graphene>1.2.0.Beta1</version.arquillian.angularjs.graphene>
 81  		<version.org.json>20150729</version.org.json>
 82  		<version.ro.isdc.wro4j>1.7.9</version.ro.isdc.wro4j>
 83  
 84  		<jboss.developer.drupal.url>http://rhdp-drupal.stage.redhat.com/</jboss.developer.drupal.url>
 85  		<linkXRef>false</linkXRef>
 86  		<version.microprofile.bom>3.0.0.GA</version.microprofile.bom>
 87  		<version.war.plugin>3.3.2</version.war.plugin>
 88  	</properties>
 89  	<repositories>
 90  		<repository>
 91  			<releases>
 92  				<enabled>true</enabled>
 93  				<updatePolicy>never</updatePolicy>
 94  			</releases>
 95  			<snapshots>
 96  				<enabled>true</enabled>
 97  				<updatePolicy>never</updatePolicy>
 98  			</snapshots>
 99  			<id>jboss-public-repository-group</id>
100  			<name>JBoss Public Repository Group</name>
101  			<url>${maven.repository.url}</url>
102  			<layout>default</layout>
103  		</repository>
104  		<repository>
105  			<releases>
106  				<enabled>true</enabled>
107  				<updatePolicy>never</updatePolicy>
108  			</releases>
109  			<snapshots>
110  				<enabled>true</enabled>
111  				<updatePolicy>never</updatePolicy>
112  			</snapshots>
113  			<id>jboss-enterprise-maven-repository</id>
114  			<name>JBoss Enterprise Maven Repository</name>
115  			<url>${maven.redhat.repository.url}</url>
116  			<layout>default</layout>
117  		</repository>
118  	</repositories>
119  	<dependencyManagement>
120  
```
### #7 - javaee-pom-to-quarkus-00050
* Category: mandatory
* Effort: 1
* Description: Adopt Maven Failsafe plugin

* Labels: konveyor.io/source=java-ee, konveyor.io/target=quarkus
* Links
  * Quarkus - Guide: https://quarkus.io/guides/maven-tooling#build-tool-maven
* Incidents
  * file:///tmp/source-code/pom.xml
      * Use the Maven Failsafe plugin adding the following sections to the `pom.xml` file:. ```xml. <properties>. <surefire-plugin.version>3.0.0</compiler-plugin.version>. </properties>. <build>. <plugins>. <plugin>. <artifactId>maven-failsafe-plugin</artifactId>. <version>$</version>. <executions>. <execution>. <goals>. <goals>integration-test</goal>. <goals>verify</goal>. </goals>. <configuration>. <systemPropertyVariables>. <native.image.path>$/$-runner</native.image.path>. <java.util.logging.manager>org.jboss.logmanager.LogManager</java.util.logging.manager>. <maven.home>$</maven.home>. </systemPropertyVariables>. </configuration>. </execution>. </executions>. </plugin>. </plugins>. </build>. ```
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <!--
  3      JBoss, Home of Professional Open Source
  4      Copyright 2015, Red Hat, Inc. and/or its affiliates, and individual
  5      contributors by the @authors tag. See the copyright.txt in the
  6      distribution for a full listing of individual contributors.
  7  
  8      Licensed under the Apache License, Version 2.0 (the "License");
  9      you may not use this file except in compliance with the License.
 10      You may obtain a copy of the License at
 11      http://www.apache.org/licenses/LICENSE-2.0
 12      Unless required by applicable law or agreed to in writing, software
 13      distributed under the License is distributed on an "AS IS" BASIS,
 14      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 15      See the License for the specific language governing permissions and
 16      limitations under the License.
 17  -->
 18  <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
 19      <modelVersion>4.0.0</modelVersion>
 20      <groupId>org.jboss.eap.quickstarts</groupId>
 21      <version>7.4.0.GA</version>
 22      <artifactId>helloworld-mdb</artifactId>
 23      <packaging>war</packaging>
 24      <name>Quickstart: helloworld-mdb</name>
 25      <description>This project demonstrates a hello world Message-Driven Bean with Servlet 3.0 as client</description>
 26  
 27      <licenses>
 28          <license>
 29              <name>Apache License, Version 2.0</name>
 30              <url>http://www.apache.org/licenses/LICENSE-2.0.html</url>
 31              <distribution>repo</distribution>
 32          </license>
 33      </licenses>
 34  <properties>
 35  
 36  		<maven.compiler.source>1.8</maven.compiler.source>
 37  		<maven.compiler.target>1.8</maven.compiler.target>
 38  
 39  		<root.dir>${project.basedir}</root.dir>
 40  		<jboss.home.name>EAP7_HOME</jboss.home.name>
 41  		<product.name>JBoss EAP</product.name>
 42  		<product.version>7.4.0.GA</product.version>
 43  		<!-- A base list of dependency and plug-in version used in the various
 44  		quick starts. -->
 45  		<version.org.asciidoctor.asciidoctor-maven-plugin>2.1.0</version.org.asciidoctor.asciidoctor-maven-plugin>
 46  		<version.wildfly.maven.plugin>2.0.2.Final</version.wildfly.maven.plugin>
 47  		<version.org.wildfly.checkstyle-config>1.0.7.Final</version.org.wildfly.checkstyle-config>
 48  		<version.org.wildfly.quickstarts.documentation.plugin>2.3.0.Final</version.org.wildfly.quickstarts.documentation.plugin>
 49  		<!-- other plug-in versions -->
 50  		<version.com.mycyla.license>3.0</version.com.mycyla.license>
 51  		<version.checkstyle>8.5</version.checkstyle>
 52  		<version.jaxws-tools-maven-plugin>1.2.3.Final</version.jaxws-tools-maven-plugin>
 53  		<!-- Explicitly declaring the source encoding eliminates the following
 54  		message: [WARNING] Using platform encoding (UTF-8 actually) to copy
 55  		filtered resources, i.e. build is platform dependent! -->
 56  		<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
 57  
 58  		<!-- Protocol to use for communication with remote maven repositories.
 59  		You can set to 'http' if you are using a maven proxy and 'https'
 60  		interferes with that. Use 'https' for builds that will be released
 61                       to
 62  		non-snapshot public maven repos -->
 63  		<maven.repository.protocol>https</maven.repository.protocol>
 64  		<!-- The full remote maven repo URL; can be overridden via -D for
 65  		special use cases -->
 66  		<maven.repository.url>
 67  			${maven.repository.protocol}://repository.jboss.org/nexus/content/groups/public/</maven.repository.url>
 68  		<!-- https://access.redhat.com/maven-repository -->
 69  		<maven.redhat.repository.url>
 70  			${maven.repository.protocol}://maven.repository.redhat.com/ga/</maven.redhat.repository.url>
 71  
 72  		<!-- Version of BOMs
 73          note: a SNAPSHOT version *requires*
 74  		checkout of BOMs at https://github.com/wildfly/boms and build through
 75  		"mvn clean install"
 76          -->
 77  		<version.server.bom>7.4.0.GA</version.server.bom>
 78  
 79  		<!-- Versions of unmanaged dependencies -->
 80  		<version.arquillian.angularjs.graphene>1.2.0.Beta1</version.arquillian.angularjs.graphene>
 81  		<version.org.json>20150729</version.org.json>
 82  		<version.ro.isdc.wro4j>1.7.9</version.ro.isdc.wro4j>
 83  
 84  		<jboss.developer.drupal.url>http://rhdp-drupal.stage.redhat.com/</jboss.developer.drupal.url>
 85  		<linkXRef>false</linkXRef>
 86  		<version.microprofile.bom>3.0.0.GA</version.microprofile.bom>
 87  		<version.war.plugin>3.3.2</version.war.plugin>
 88  	</properties>
 89  	<repositories>
 90  		<repository>
 91  			<releases>
 92  				<enabled>true</enabled>
 93  				<updatePolicy>never</updatePolicy>
 94  			</releases>
 95  			<snapshots>
 96  				<enabled>true</enabled>
 97  				<updatePolicy>never</updatePolicy>
 98  			</snapshots>
 99  			<id>jboss-public-repository-group</id>
100  			<name>JBoss Public Repository Group</name>
101  			<url>${maven.repository.url}</url>
102  			<layout>default</layout>
103  		</repository>
104  		<repository>
105  			<releases>
106  				<enabled>true</enabled>
107  				<updatePolicy>never</updatePolicy>
108  			</releases>
109  			<snapshots>
110  				<enabled>true</enabled>
111  				<updatePolicy>never</updatePolicy>
112  			</snapshots>
113  			<id>jboss-enterprise-maven-repository</id>
114  			<name>JBoss Enterprise Maven Repository</name>
115  			<url>${maven.redhat.repository.url}</url>
116  			<layout>default</layout>
117  		</repository>
118  	</repositories>
119  	<dependencyManagement>
120  
```
### #8 - javaee-pom-to-quarkus-00060
* Category: mandatory
* Effort: 1
* Description: Add Maven profile to run the Quarkus native build
Leverage a Maven profile to run the Quarkus native build adding the following section to the `pom.xml` file:. ```xml. <profiles>. <profile>. <id>native</id>. <activation>. <property>. <name>native</name>. </property>. </activation>. <properties>. <skipITs>false</skipITs>. <quarkus.package.type>native</quarkus.package.type>. </properties>. </profile>. </profiles>. ```
* Labels: konveyor.io/source=java-ee, konveyor.io/target=quarkus
* Links
  * Quarkus - Guide: https://quarkus.io/guides/maven-tooling#build-tool-maven
* Incidents
  * file:///tmp/source-code/pom.xml
      * Leverage a Maven profile to run the Quarkus native build adding the following section to the `pom.xml` file:. ```xml. <profiles>. <profile>. <id>native</id>. <activation>. <property>. <name>native</name>. </property>. </activation>. <properties>. <skipITs>false</skipITs>. <quarkus.package.type>native</quarkus.package.type>. </properties>. </profile>. </profiles>. ```
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <!--
  3      JBoss, Home of Professional Open Source
  4      Copyright 2015, Red Hat, Inc. and/or its affiliates, and individual
  5      contributors by the @authors tag. See the copyright.txt in the
  6      distribution for a full listing of individual contributors.
  7  
  8      Licensed under the Apache License, Version 2.0 (the "License");
  9      you may not use this file except in compliance with the License.
 10      You may obtain a copy of the License at
 11      http://www.apache.org/licenses/LICENSE-2.0
 12      Unless required by applicable law or agreed to in writing, software
 13      distributed under the License is distributed on an "AS IS" BASIS,
 14      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 15      See the License for the specific language governing permissions and
 16      limitations under the License.
 17  -->
 18  <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
 19      <modelVersion>4.0.0</modelVersion>
 20      <groupId>org.jboss.eap.quickstarts</groupId>
 21      <version>7.4.0.GA</version>
 22      <artifactId>helloworld-mdb</artifactId>
 23      <packaging>war</packaging>
 24      <name>Quickstart: helloworld-mdb</name>
 25      <description>This project demonstrates a hello world Message-Driven Bean with Servlet 3.0 as client</description>
 26  
 27      <licenses>
 28          <license>
 29              <name>Apache License, Version 2.0</name>
 30              <url>http://www.apache.org/licenses/LICENSE-2.0.html</url>
 31              <distribution>repo</distribution>
 32          </license>
 33      </licenses>
 34  <properties>
 35  
 36  		<maven.compiler.source>1.8</maven.compiler.source>
 37  		<maven.compiler.target>1.8</maven.compiler.target>
 38  
 39  		<root.dir>${project.basedir}</root.dir>
 40  		<jboss.home.name>EAP7_HOME</jboss.home.name>
 41  		<product.name>JBoss EAP</product.name>
 42  		<product.version>7.4.0.GA</product.version>
 43  		<!-- A base list of dependency and plug-in version used in the various
 44  		quick starts. -->
 45  		<version.org.asciidoctor.asciidoctor-maven-plugin>2.1.0</version.org.asciidoctor.asciidoctor-maven-plugin>
 46  		<version.wildfly.maven.plugin>2.0.2.Final</version.wildfly.maven.plugin>
 47  		<version.org.wildfly.checkstyle-config>1.0.7.Final</version.org.wildfly.checkstyle-config>
 48  		<version.org.wildfly.quickstarts.documentation.plugin>2.3.0.Final</version.org.wildfly.quickstarts.documentation.plugin>
 49  		<!-- other plug-in versions -->
 50  		<version.com.mycyla.license>3.0</version.com.mycyla.license>
 51  		<version.checkstyle>8.5</version.checkstyle>
 52  		<version.jaxws-tools-maven-plugin>1.2.3.Final</version.jaxws-tools-maven-plugin>
 53  		<!-- Explicitly declaring the source encoding eliminates the following
 54  		message: [WARNING] Using platform encoding (UTF-8 actually) to copy
 55  		filtered resources, i.e. build is platform dependent! -->
 56  		<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
 57  
 58  		<!-- Protocol to use for communication with remote maven repositories.
 59  		You can set to 'http' if you are using a maven proxy and 'https'
 60  		interferes with that. Use 'https' for builds that will be released
 61                       to
 62  		non-snapshot public maven repos -->
 63  		<maven.repository.protocol>https</maven.repository.protocol>
 64  		<!-- The full remote maven repo URL; can be overridden via -D for
 65  		special use cases -->
 66  		<maven.repository.url>
 67  			${maven.repository.protocol}://repository.jboss.org/nexus/content/groups/public/</maven.repository.url>
 68  		<!-- https://access.redhat.com/maven-repository -->
 69  		<maven.redhat.repository.url>
 70  			${maven.repository.protocol}://maven.repository.redhat.com/ga/</maven.redhat.repository.url>
 71  
 72  		<!-- Version of BOMs
 73          note: a SNAPSHOT version *requires*
 74  		checkout of BOMs at https://github.com/wildfly/boms and build through
 75  		"mvn clean install"
 76          -->
 77  		<version.server.bom>7.4.0.GA</version.server.bom>
 78  
 79  		<!-- Versions of unmanaged dependencies -->
 80  		<version.arquillian.angularjs.graphene>1.2.0.Beta1</version.arquillian.angularjs.graphene>
 81  		<version.org.json>20150729</version.org.json>
 82  		<version.ro.isdc.wro4j>1.7.9</version.ro.isdc.wro4j>
 83  
 84  		<jboss.developer.drupal.url>http://rhdp-drupal.stage.redhat.com/</jboss.developer.drupal.url>
 85  		<linkXRef>false</linkXRef>
 86  		<version.microprofile.bom>3.0.0.GA</version.microprofile.bom>
 87  		<version.war.plugin>3.3.2</version.war.plugin>
 88  	</properties>
 89  	<repositories>
 90  		<repository>
 91  			<releases>
 92  				<enabled>true</enabled>
 93  				<updatePolicy>never</updatePolicy>
 94  			</releases>
 95  			<snapshots>
 96  				<enabled>true</enabled>
 97  				<updatePolicy>never</updatePolicy>
 98  			</snapshots>
 99  			<id>jboss-public-repository-group</id>
100  			<name>JBoss Public Repository Group</name>
101  			<url>${maven.repository.url}</url>
102  			<layout>default</layout>
103  		</repository>
104  		<repository>
105  			<releases>
106  				<enabled>true</enabled>
107  				<updatePolicy>never</updatePolicy>
108  			</releases>
109  			<snapshots>
110  				<enabled>true</enabled>
111  				<updatePolicy>never</updatePolicy>
112  			</snapshots>
113  			<id>jboss-enterprise-maven-repository</id>
114  			<name>JBoss Enterprise Maven Repository</name>
115  			<url>${maven.redhat.repository.url}</url>
116  			<layout>default</layout>
117  		</repository>
118  	</repositories>
119  	<dependencyManagement>
120  
```
