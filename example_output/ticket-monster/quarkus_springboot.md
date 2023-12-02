# quarkus/springboot
## Description
This ruleset gives hints to migrate from Spring Scheduled to Quarkus spring-scheduled extension
* Source of rules: https://github.com/konveyor/rulesets/tree/main/default/generated
* Sample application: https://github.com/deewhyweb/eap-coolstore-monolith
## Violations
Number of Violations: 25
### #0 - cdi-to-quarkus-00000
* Category: mandatory
* Effort: 1
* Description: Replace javax.enterprise:cdi-api dependency
Dependency `javax.enterprise:cdi-api` has to be replaced with `io.quarkus:quarkus-arc` artifact.
* Labels: konveyor.io/source=java-ee, konveyor.io/target=quarkus
* Links
  * Quarkus - Guide: https://quarkus.io/guides/cdi-reference
* Incidents
  * file:///tmp/source-code/backend-v1/pom.xml
      * Dependency `javax.enterprise:cdi-api` has to be replaced with `io.quarkus:quarkus-arc` artifact.
      * Code Snippet:
```java
 31              </snapshots>
 32          </repository>
 33          <repository>
 34              <id>jboss-ga-repository</id>
 35              <url>http://maven.repository.redhat.com/techpreview/all</url>
 36              <releases>
 37                  <enabled>true</enabled>
 38              </releases>
 39              <snapshots>
 40                  <enabled>false</enabled>
 41              </snapshots>
 42          </repository>
 43          <repository>
 44              <id>jboss-earlyaccess-repository</id>
 45              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 46              <releases>
 47                  <enabled>true</enabled>
 48              </releases>
 49              <snapshots>
 50                  <enabled>false</enabled>
 51              </snapshots>
 52          </repository>
 53          <repository>
 54              <id>redhat.ea</id>
 55              <name>Red Hat Early Access Repository</name>
 56              <url>https://maven.repository.redhat.com/earlyaccess/all</url>
 57              <snapshots>
 58                  <enabled>false</enabled>
 59              </snapshots>
 60              <releases>
 61                  <enabled>true</enabled>
 62              </releases>
 63          </repository>
 64      </repositories>
 65  
 66      <pluginRepositories>
 67          <pluginRepository>
 68              <id>redhat-ga-repository</id>
 69              <url>https://maven.repository.redhat.com/ga/</url>
 70              <releases>
 71                  <enabled>true</enabled>
 72              </releases>
 73              <snapshots>
 74                  <enabled>false</enabled>
 75              </snapshots>
 76          </pluginRepository>
 77          <pluginRepository>
 78              <id>jboss-earlyaccess-plugin-repository</id>
 79              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 80              <releases>
 81                  <enabled>true</enabled>
 82              </releases>
 83              <snapshots>
 84                  <enabled>false</enabled>
 85              </snapshots>
 86          </pluginRepository>
 87      </pluginRepositories>
 88  
 89      <properties>
 90          <!-- Explicitly declaring the source encoding eliminates the following 
 91              message: -->
 92          <!-- [WARNING] Using platform encoding (UTF-8 actually) to copy filtered 
 93              resources, i.e. build is platform dependent! -->
 94          <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
 95          <!-- Timestamp format for the maven.build.timestamp property -->
 96          <!-- You can reference property in pom.xml or filtered resources 
 97              (must enable third-party plugin if using Maven < 2.1) -->
 98          <maven.build.timestamp.format>yyyyMMdd'T'HHmmss</maven.build.timestamp.format>
 99          <!-- Specify the JBoss EAP directory to be the JBOSS_HOME environment
100              variable -->
101          <jboss.home>${env.JBOSS_HOME}</jboss.home>
102          <version.jboss.bom.eap>7.0.7.GA</version.jboss.bom.eap>
103          <version.wildfly.maven.plugin>1.0.2.Final</version.wildfly.maven.plugin>
104          <version.surefire.plugin>2.10</version.surefire.plugin>
105          <buildhelper.plugin.version>1.7</buildhelper.plugin.version>
106          <fabric8.maven.plugin.version>3.5.25</fabric8.maven.plugin.version>
107          <docker.image.name>ceposta/%a:%l</docker.image.name>
108      </properties>
109  
110      <dependencyManagement>
111          <dependencies>
112              <dependency>
113                  <groupId>org.jboss.bom</groupId>
114                  <artifactId>jboss-eap-javaee7-with-tools</artifactId>
115                  <version>${version.jboss.bom.eap}</version>
116                  <type>pom</type>
117                  <scope>import</scope>
118              </dependency>
119          </dependencies>
120      </dependencyManagement>
121  
122      <dependencies>
123  
124          <!-- First declare the APIs we depend on and need for compilation. 
125              All of them are provided by JBoss EAP -->
126  
127          <!-- Import the CDI API, we use provided scope as the API is included 
128              in JBoss EAP -->
129          <dependency>
130              <groupId>javax.enterprise</groupId>
131              <artifactId>cdi-api</artifactId>
132              <scope>provided</scope>
133          </dependency>
134          
135          <dependency>
136              <groupId>javax.inject</groupId>
137              <artifactId>javax.inject</artifactId>
138              <scope>provided</scope>
139          </dependency>
140          
141          <dependency>
142              <groupId>javax.validation</groupId>
143              <artifactId>validation-api</artifactId>
144              <scope>provided</scope>
145          </dependency>
146         
147          <!-- Import the Common Annotations API (JSR-250), we use provided 
148              scope as the API is included in JBoss EAP -->
149          <dependency>
150              <groupId>org.jboss.spec.javax.annotation</groupId>
151              <artifactId>jboss-annotations-api_1.2_spec</artifactId>
152              <scope>provided</scope>
153          </dependency>
154  
155          <!-- Import the JAX-RS API, we use provided scope as the API is included 
156              in JBoss EAP -->
157          <dependency>
158              <groupId>org.jboss.spec.javax.ws.rs</groupId>
159              <artifactId>jboss-jaxrs-api_2.0_spec</artifactId>
160              <scope>provided</scope>
161          </dependency>
162  
163          <!-- Import the JPA API, we use provided scope as the API is included 
164              in JBoss EAP -->
165          <dependency>
166              <groupId>org.hibernate.javax.persistence</groupId>
167              <artifactId>hibernate-jpa-2.1-api</artifactId>
168              <scope>provided</scope>
169          </dependency>
170  
171          <!-- Import the EJB API, we use provided scope as the API is included 
172              in JBoss EAP -->
173          <dependency>
174              <groupId>org.jboss.spec.javax.ejb</groupId>
175              <artifactId>jboss-ejb-api_3.2_spec</artifactId>
176              <scope>provided</scope>
177          </dependency>
178  
179          <!-- Import the Servlet API, we use provided scope as the API is 
180              included in JBoss EAP -->
181          <dependency>
182              <groupId>org.jboss.spec.javax.servlet</groupId>
183              <artifactId>jboss-servlet-api_3.1_spec</artifactId>
184              <scope>provided</scope>
185          </dependency>
186  
187          <!-- JSR-303 (Bean Validation) Implementation -->
188          <!-- Provides portable constraints such as @Email -->
189          <!-- Hibernate Validator is shipped in JBoss EAP -->
190          <dependency>
191              <groupId>org.hibernate</groupId>
192              <artifactId>hibernate-validator</artifactId>
193              <scope>provided</scope>
194              <exclusions>
195                  <exclusion>
196                      <groupId>org.slf4j</groupId>
197                      <artifactId>slf4j-api</artifactId>
198                  </exclusion>
199              </exclusions>
200          </dependency>
201  
202  
203          <!-- Now we declare any tools needed -->
204  
205          <!-- Annotation processor to generate the JPA 2.0 metamodel classes 
206              for typesafe criteria queries -->
207          <dependency>
208              <groupId>org.hibernate</groupId>
209              <artifactId>hibernate-jpamodelgen</artifactId>
210              <scope>provided</scope>
211          </dependency>
212  
213          <!-- Needed for running tests (you may also use TestNG) -->
214          <dependency>
215              <groupId>junit</groupId>
216              <artifactId>junit</artifactId>
217              <scope>test</scope>
218          </dependency>
219  
220          <!-- Optional, but highly recommended -->
221          <!-- Arquillian allows you to test enterprise code such as EJBs and 
222              Transactional(JTA) JPA from JUnit/TestNG -->
223          <dependency>
224              <groupId>org.jboss.arquillian.junit</groupId>
225              <artifactId>arquillian-junit-container</artifactId>
226              <scope>test</scope>
227          </dependency>
228  
229          <dependency>
230              <groupId>org.jboss.arquillian.protocol</groupId>
231              <artifactId>arquillian-protocol-servlet</artifactId>
```
  * file:///tmp/source-code/backend-v2/pom.xml
      * Dependency `javax.enterprise:cdi-api` has to be replaced with `io.quarkus:quarkus-arc` artifact.
      * Code Snippet:
```java
 42          </repository>
 43          <repository>
 44              <id>jboss-earlyaccess-repository</id>
 45              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 46              <releases>
 47                  <enabled>true</enabled>
 48              </releases>
 49              <snapshots>
 50                  <enabled>false</enabled>
 51              </snapshots>
 52          </repository>
 53          <repository>
 54              <id>redhat.ea</id>
 55              <name>Red Hat Early Access Repository</name>
 56              <url>https://maven.repository.redhat.com/earlyaccess/all</url>
 57              <snapshots>
 58                  <enabled>false</enabled>
 59              </snapshots>
 60              <releases>
 61                  <enabled>true</enabled>
 62              </releases>
 63          </repository>
 64      </repositories>
 65  
 66      <pluginRepositories>
 67          <pluginRepository>
 68              <id>redhat-ga-repository</id>
 69              <url>https://maven.repository.redhat.com/ga/</url>
 70              <releases>
 71                  <enabled>true</enabled>
 72              </releases>
 73              <snapshots>
 74                  <enabled>false</enabled>
 75              </snapshots>
 76          </pluginRepository>
 77          <pluginRepository>
 78              <id>jboss-earlyaccess-plugin-repository</id>
 79              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 80              <releases>
 81                  <enabled>true</enabled>
 82              </releases>
 83              <snapshots>
 84                  <enabled>false</enabled>
 85              </snapshots>
 86          </pluginRepository>
 87      </pluginRepositories>
 88  
 89      <properties>
 90          <!-- Explicitly declaring the source encoding eliminates the following 
 91              message: -->
 92          <!-- [WARNING] Using platform encoding (UTF-8 actually) to copy filtered 
 93              resources, i.e. build is platform dependent! -->
 94          <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
 95          <!-- Timestamp format for the maven.build.timestamp property -->
 96          <!-- You can reference property in pom.xml or filtered resources 
 97              (must enable third-party plugin if using Maven < 2.1) -->
 98          <maven.build.timestamp.format>yyyyMMdd'T'HHmmss</maven.build.timestamp.format>
 99          <!-- Specify the JBoss EAP directory to be the JBOSS_HOME environment
100              variable -->
101          <jboss.home>${env.JBOSS_HOME}</jboss.home>
102          <version.jboss.bom.eap>7.0.7.GA</version.jboss.bom.eap>
103          <version.wildfly.maven.plugin>1.0.2.Final</version.wildfly.maven.plugin>
104          <version.surefire.plugin>2.10</version.surefire.plugin>
105          <buildhelper.plugin.version>1.7</buildhelper.plugin.version>
106          <fabric8.maven.plugin.version>3.5.25</fabric8.maven.plugin.version>
107          <docker.image.name>ceposta/%a:%l</docker.image.name>
108          <ffj4.version>1.6.5</ffj4.version>
109          <version.org.jboss.arquillian>1.1.12.Final</version.org.jboss.arquillian>
110          <version.org.wildfly.arquillian.container>2.0.0.Final</version.org.wildfly.arquillian.container>
111      </properties>
112  
113      <dependencyManagement>
114          <dependencies>
115              <dependency>
116                  <groupId>org.jboss.arquillian</groupId>
117                  <artifactId>arquillian-bom</artifactId>
118                  <version>${version.org.jboss.arquillian}</version>
119                  <type>pom</type>
120                  <scope>import</scope>
121              </dependency>
122              <dependency>
123                  <groupId>org.jboss.bom</groupId>
124                  <artifactId>jboss-eap-javaee7-with-tools</artifactId>
125                  <version>${version.jboss.bom.eap}</version>
126                  <type>pom</type>
127                  <scope>import</scope>
128              </dependency>
129  
130          </dependencies>
131      </dependencyManagement>
132  
133      <dependencies>
134  
135          <!-- First declare the APIs we depend on and need for compilation. 
136              All of them are provided by JBoss EAP -->
137  
138          <!-- Import the CDI API, we use provided scope as the API is included 
139              in JBoss EAP -->
140          <dependency>
141              <groupId>javax.enterprise</groupId>
142              <artifactId>cdi-api</artifactId>
143              <scope>provided</scope>
144          </dependency>
145          
146          <dependency>
147              <groupId>javax.inject</groupId>
148              <artifactId>javax.inject</artifactId>
149              <scope>provided</scope>
150          </dependency>
151          
152          <dependency>
153              <groupId>javax.validation</groupId>
154              <artifactId>validation-api</artifactId>
155              <scope>provided</scope>
156          </dependency>
157         
158          <!-- Import the Common Annotations API (JSR-250), we use provided 
159              scope as the API is included in JBoss EAP -->
160          <dependency>
161              <groupId>org.jboss.spec.javax.annotation</groupId>
162              <artifactId>jboss-annotations-api_1.2_spec</artifactId>
163              <scope>provided</scope>
164          </dependency>
165  
166          <!-- Import the JAX-RS API, we use provided scope as the API is included 
167              in JBoss EAP -->
168          <dependency>
169              <groupId>org.jboss.spec.javax.ws.rs</groupId>
170              <artifactId>jboss-jaxrs-api_2.0_spec</artifactId>
171              <scope>provided</scope>
172          </dependency>
173  
174          <!-- Import the JPA API, we use provided scope as the API is included 
175              in JBoss EAP -->
176          <dependency>
177              <groupId>org.hibernate.javax.persistence</groupId>
178              <artifactId>hibernate-jpa-2.1-api</artifactId>
179              <scope>provided</scope>
180          </dependency>
181  
182          <!-- Import the EJB API, we use provided scope as the API is included 
183              in JBoss EAP -->
184          <dependency>
185              <groupId>org.jboss.spec.javax.ejb</groupId>
186              <artifactId>jboss-ejb-api_3.2_spec</artifactId>
187              <scope>provided</scope>
188          </dependency>
189  
190          <!-- Import the Servlet API, we use provided scope as the API is 
191              included in JBoss EAP -->
192          <dependency>
193              <groupId>org.jboss.spec.javax.servlet</groupId>
194              <artifactId>jboss-servlet-api_3.1_spec</artifactId>
195              <scope>provided</scope>
196          </dependency>
197  
198          <dependency>
199              <groupId>org.ff4j</groupId>
200              <artifactId>ff4j-core</artifactId>
201              <version>${ffj4.version}</version>
202          </dependency>
203          <dependency>
204              <groupId>org.ff4j</groupId>
205              <artifactId>ff4j-web</artifactId>
206              <version>${ffj4.version}</version>
207          </dependency>
208  
209          <!-- JSR-303 (Bean Validation) Implementation -->
210          <!-- Provides portable constraints such as @Email -->
211          <!-- Hibernate Validator is shipped in JBoss EAP -->
212          <dependency>
213              <groupId>org.hibernate</groupId>
214              <artifactId>hibernate-validator</artifactId>
215              <scope>provided</scope>
216              <exclusions>
217                  <exclusion>
218                      <groupId>org.slf4j</groupId>
219                      <artifactId>slf4j-api</artifactId>
220                  </exclusion>
221              </exclusions>
222          </dependency>
223  
224  
225          <!-- Now we declare any tools needed -->
226  
227          <!-- Annotation processor to generate the JPA 2.0 metamodel classes 
228              for typesafe criteria queries -->
229          <dependency>
230              <groupId>org.hibernate</groupId>
231              <artifactId>hibernate-jpamodelgen</artifactId>
232              <scope>provided</scope>
233          </dependency>
234  
235          <!-- Needed for running tests (you may also use TestNG) -->
236          <dependency>
237              <groupId>junit</groupId>
238              <artifactId>junit</artifactId>
239              <scope>test</scope>
240          </dependency>
241  
242          <!-- For service virtualization/mocking-->
```
  * file:///tmp/source-code/monolith/pom.xml
      * Dependency `javax.enterprise:cdi-api` has to be replaced with `io.quarkus:quarkus-arc` artifact.
      * Code Snippet:
```java
 31              </snapshots>
 32          </repository>
 33          <repository>
 34              <id>jboss-ga-repository</id>
 35              <url>http://maven.repository.redhat.com/techpreview/all</url>
 36              <releases>
 37                  <enabled>true</enabled>
 38              </releases>
 39              <snapshots>
 40                  <enabled>false</enabled>
 41              </snapshots>
 42          </repository>
 43          <repository>
 44              <id>jboss-earlyaccess-repository</id>
 45              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 46              <releases>
 47                  <enabled>true</enabled>
 48              </releases>
 49              <snapshots>
 50                  <enabled>false</enabled>
 51              </snapshots>
 52          </repository>
 53          <repository>
 54              <id>redhat.ea</id>
 55              <name>Red Hat Early Access Repository</name>
 56              <url>https://maven.repository.redhat.com/earlyaccess/all</url>
 57              <snapshots>
 58                  <enabled>false</enabled>
 59              </snapshots>
 60              <releases>
 61                  <enabled>true</enabled>
 62              </releases>
 63          </repository>
 64      </repositories>
 65  
 66      <pluginRepositories>
 67          <pluginRepository>
 68              <id>redhat-ga-repository</id>
 69              <url>https://maven.repository.redhat.com/ga/</url>
 70              <releases>
 71                  <enabled>true</enabled>
 72              </releases>
 73              <snapshots>
 74                  <enabled>false</enabled>
 75              </snapshots>
 76          </pluginRepository>
 77          <pluginRepository>
 78              <id>jboss-earlyaccess-plugin-repository</id>
 79              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 80              <releases>
 81                  <enabled>true</enabled>
 82              </releases>
 83              <snapshots>
 84                  <enabled>false</enabled>
 85              </snapshots>
 86          </pluginRepository>
 87      </pluginRepositories>
 88  
 89      <properties>
 90          <!-- Explicitly declaring the source encoding eliminates the following 
 91              message: -->
 92          <!-- [WARNING] Using platform encoding (UTF-8 actually) to copy filtered 
 93              resources, i.e. build is platform dependent! -->
 94          <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
 95          <!-- Timestamp format for the maven.build.timestamp property -->
 96          <!-- You can reference property in pom.xml or filtered resources 
 97              (must enable third-party plugin if using Maven < 2.1) -->
 98          <maven.build.timestamp.format>yyyyMMdd'T'HHmmss</maven.build.timestamp.format>
 99          <!-- Specify the JBoss EAP directory to be the JBOSS_HOME environment
100              variable -->
101          <jboss.home>${env.JBOSS_HOME}</jboss.home>
102          <version.jboss.bom.eap>7.0.7.GA</version.jboss.bom.eap>
103          <version.wildfly.maven.plugin>1.0.2.Final</version.wildfly.maven.plugin>
104          <version.surefire.plugin>2.10</version.surefire.plugin>
105          <buildhelper.plugin.version>1.7</buildhelper.plugin.version>
106          <fabric8.maven.plugin.version>3.5.25</fabric8.maven.plugin.version>
107          <docker.image.name>%g/%a:%l</docker.image.name>
108      </properties>
109  
110      <dependencyManagement>
111          <dependencies>
112              <dependency>
113                  <groupId>org.jboss.bom</groupId>
114                  <artifactId>jboss-eap-javaee7-with-tools</artifactId>
115                  <version>${version.jboss.bom.eap}</version>
116                  <type>pom</type>
117                  <scope>import</scope>
118              </dependency>
119          </dependencies>
120      </dependencyManagement>
121  
122      <dependencies>
123  
124          <!-- First declare the APIs we depend on and need for compilation. 
125              All of them are provided by JBoss EAP -->
126  
127          <!-- Import the CDI API, we use provided scope as the API is included 
128              in JBoss EAP -->
129          <dependency>
130              <groupId>javax.enterprise</groupId>
131              <artifactId>cdi-api</artifactId>
132              <scope>provided</scope>
133          </dependency>
134  
135          <dependency>
136              <groupId>javax.inject</groupId>
137              <artifactId>javax.inject</artifactId>
138              <scope>provided</scope>
139          </dependency>
140  
141          <dependency>
142              <groupId>javax.validation</groupId>
143              <artifactId>validation-api</artifactId>
144              <scope>provided</scope>
145          </dependency>
146  
147          <!-- Import the Common Annotations API (JSR-250), we use provided 
148              scope as the API is included in JBoss EAP -->
149          <dependency>
150              <groupId>org.jboss.spec.javax.annotation</groupId>
151              <artifactId>jboss-annotations-api_1.2_spec</artifactId>
152              <scope>provided</scope>
153          </dependency>
154  
155          <!-- Import the JAX-RS API, we use provided scope as the API is included 
156              in JBoss EAP -->
157          <dependency>
158              <groupId>org.jboss.spec.javax.ws.rs</groupId>
159              <artifactId>jboss-jaxrs-api_2.0_spec</artifactId>
160              <scope>provided</scope>
161          </dependency>
162  
163          <!-- Import the JPA API, we use provided scope as the API is included 
164              in JBoss EAP -->
165          <dependency>
166              <groupId>org.hibernate.javax.persistence</groupId>
167              <artifactId>hibernate-jpa-2.1-api</artifactId>
168              <scope>provided</scope>
169          </dependency>
170  
171          <!-- Import the EJB API, we use provided scope as the API is included 
172              in JBoss EAP -->
173          <dependency>
174              <groupId>org.jboss.spec.javax.ejb</groupId>
175              <artifactId>jboss-ejb-api_3.2_spec</artifactId>
176              <scope>provided</scope>
177          </dependency>
178  
179          <!-- Import the Servlet API, we use provided scope as the API is 
180              included in JBoss EAP -->
181          <dependency>
182              <groupId>org.jboss.spec.javax.servlet</groupId>
183              <artifactId>jboss-servlet-api_3.1_spec</artifactId>
184              <scope>provided</scope>
185          </dependency>
186  
187          <!-- JSR-303 (Bean Validation) Implementation -->
188          <!-- Provides portable constraints such as @Email -->
189          <!-- Hibernate Validator is shipped in JBoss EAP -->
190          <dependency>
191              <groupId>org.hibernate</groupId>
192              <artifactId>hibernate-validator</artifactId>
193              <scope>provided</scope>
194              <exclusions>
195                  <exclusion>
196                      <groupId>org.slf4j</groupId>
197                      <artifactId>slf4j-api</artifactId>
198                  </exclusion>
199              </exclusions>
200          </dependency>
201  
202  
203          <!-- Now we declare any tools needed -->
204  
205          <!-- Annotation processor to generate the JPA 2.0 metamodel classes 
206              for typesafe criteria queries -->
207          <dependency>
208              <groupId>org.hibernate</groupId>
209              <artifactId>hibernate-jpamodelgen</artifactId>
210              <scope>provided</scope>
211          </dependency>
212  
213          <!-- Needed for running tests (you may also use TestNG) -->
214          <dependency>
215              <groupId>junit</groupId>
216              <artifactId>junit</artifactId>
217              <scope>test</scope>
218          </dependency>
219  
220          <!-- Optional, but highly recommended -->
221          <!-- Arquillian allows you to test enterprise code such as EJBs and 
222              Transactional(JTA) JPA from JUnit/TestNG -->
223          <dependency>
224              <groupId>org.jboss.arquillian.junit</groupId>
225              <artifactId>arquillian-junit-container</artifactId>
226              <scope>test</scope>
227          </dependency>
228  
229          <dependency>
230              <groupId>org.jboss.arquillian.protocol</groupId>
231              <artifactId>arquillian-protocol-servlet</artifactId>
```
### #1 - cdi-to-quarkus-00020
* Category: mandatory
* Effort: 1
* Description: Replace javax.inject:javax.inject dependency
Dependency `javax.inject:javax.inject` has to be replaced with `io.quarkus:quarkus-arc` artifact.
* Labels: konveyor.io/source=java-ee, konveyor.io/target=quarkus
* Links
  * Quarkus - Guide: https://quarkus.io/guides/cdi-reference
* Incidents
  * file:///tmp/source-code/backend-v1/pom.xml
      * Dependency `javax.inject:javax.inject` has to be replaced with `io.quarkus:quarkus-arc` artifact.
      * Code Snippet:
```java
 37                  <enabled>true</enabled>
 38              </releases>
 39              <snapshots>
 40                  <enabled>false</enabled>
 41              </snapshots>
 42          </repository>
 43          <repository>
 44              <id>jboss-earlyaccess-repository</id>
 45              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 46              <releases>
 47                  <enabled>true</enabled>
 48              </releases>
 49              <snapshots>
 50                  <enabled>false</enabled>
 51              </snapshots>
 52          </repository>
 53          <repository>
 54              <id>redhat.ea</id>
 55              <name>Red Hat Early Access Repository</name>
 56              <url>https://maven.repository.redhat.com/earlyaccess/all</url>
 57              <snapshots>
 58                  <enabled>false</enabled>
 59              </snapshots>
 60              <releases>
 61                  <enabled>true</enabled>
 62              </releases>
 63          </repository>
 64      </repositories>
 65  
 66      <pluginRepositories>
 67          <pluginRepository>
 68              <id>redhat-ga-repository</id>
 69              <url>https://maven.repository.redhat.com/ga/</url>
 70              <releases>
 71                  <enabled>true</enabled>
 72              </releases>
 73              <snapshots>
 74                  <enabled>false</enabled>
 75              </snapshots>
 76          </pluginRepository>
 77          <pluginRepository>
 78              <id>jboss-earlyaccess-plugin-repository</id>
 79              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 80              <releases>
 81                  <enabled>true</enabled>
 82              </releases>
 83              <snapshots>
 84                  <enabled>false</enabled>
 85              </snapshots>
 86          </pluginRepository>
 87      </pluginRepositories>
 88  
 89      <properties>
 90          <!-- Explicitly declaring the source encoding eliminates the following 
 91              message: -->
 92          <!-- [WARNING] Using platform encoding (UTF-8 actually) to copy filtered 
 93              resources, i.e. build is platform dependent! -->
 94          <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
 95          <!-- Timestamp format for the maven.build.timestamp property -->
 96          <!-- You can reference property in pom.xml or filtered resources 
 97              (must enable third-party plugin if using Maven < 2.1) -->
 98          <maven.build.timestamp.format>yyyyMMdd'T'HHmmss</maven.build.timestamp.format>
 99          <!-- Specify the JBoss EAP directory to be the JBOSS_HOME environment
100              variable -->
101          <jboss.home>${env.JBOSS_HOME}</jboss.home>
102          <version.jboss.bom.eap>7.0.7.GA</version.jboss.bom.eap>
103          <version.wildfly.maven.plugin>1.0.2.Final</version.wildfly.maven.plugin>
104          <version.surefire.plugin>2.10</version.surefire.plugin>
105          <buildhelper.plugin.version>1.7</buildhelper.plugin.version>
106          <fabric8.maven.plugin.version>3.5.25</fabric8.maven.plugin.version>
107          <docker.image.name>ceposta/%a:%l</docker.image.name>
108      </properties>
109  
110      <dependencyManagement>
111          <dependencies>
112              <dependency>
113                  <groupId>org.jboss.bom</groupId>
114                  <artifactId>jboss-eap-javaee7-with-tools</artifactId>
115                  <version>${version.jboss.bom.eap}</version>
116                  <type>pom</type>
117                  <scope>import</scope>
118              </dependency>
119          </dependencies>
120      </dependencyManagement>
121  
122      <dependencies>
123  
124          <!-- First declare the APIs we depend on and need for compilation. 
125              All of them are provided by JBoss EAP -->
126  
127          <!-- Import the CDI API, we use provided scope as the API is included 
128              in JBoss EAP -->
129          <dependency>
130              <groupId>javax.enterprise</groupId>
131              <artifactId>cdi-api</artifactId>
132              <scope>provided</scope>
133          </dependency>
134          
135          <dependency>
136              <groupId>javax.inject</groupId>
137              <artifactId>javax.inject</artifactId>
138              <scope>provided</scope>
139          </dependency>
140          
141          <dependency>
142              <groupId>javax.validation</groupId>
143              <artifactId>validation-api</artifactId>
144              <scope>provided</scope>
145          </dependency>
146         
147          <!-- Import the Common Annotations API (JSR-250), we use provided 
148              scope as the API is included in JBoss EAP -->
149          <dependency>
150              <groupId>org.jboss.spec.javax.annotation</groupId>
151              <artifactId>jboss-annotations-api_1.2_spec</artifactId>
152              <scope>provided</scope>
153          </dependency>
154  
155          <!-- Import the JAX-RS API, we use provided scope as the API is included 
156              in JBoss EAP -->
157          <dependency>
158              <groupId>org.jboss.spec.javax.ws.rs</groupId>
159              <artifactId>jboss-jaxrs-api_2.0_spec</artifactId>
160              <scope>provided</scope>
161          </dependency>
162  
163          <!-- Import the JPA API, we use provided scope as the API is included 
164              in JBoss EAP -->
165          <dependency>
166              <groupId>org.hibernate.javax.persistence</groupId>
167              <artifactId>hibernate-jpa-2.1-api</artifactId>
168              <scope>provided</scope>
169          </dependency>
170  
171          <!-- Import the EJB API, we use provided scope as the API is included 
172              in JBoss EAP -->
173          <dependency>
174              <groupId>org.jboss.spec.javax.ejb</groupId>
175              <artifactId>jboss-ejb-api_3.2_spec</artifactId>
176              <scope>provided</scope>
177          </dependency>
178  
179          <!-- Import the Servlet API, we use provided scope as the API is 
180              included in JBoss EAP -->
181          <dependency>
182              <groupId>org.jboss.spec.javax.servlet</groupId>
183              <artifactId>jboss-servlet-api_3.1_spec</artifactId>
184              <scope>provided</scope>
185          </dependency>
186  
187          <!-- JSR-303 (Bean Validation) Implementation -->
188          <!-- Provides portable constraints such as @Email -->
189          <!-- Hibernate Validator is shipped in JBoss EAP -->
190          <dependency>
191              <groupId>org.hibernate</groupId>
192              <artifactId>hibernate-validator</artifactId>
193              <scope>provided</scope>
194              <exclusions>
195                  <exclusion>
196                      <groupId>org.slf4j</groupId>
197                      <artifactId>slf4j-api</artifactId>
198                  </exclusion>
199              </exclusions>
200          </dependency>
201  
202  
203          <!-- Now we declare any tools needed -->
204  
205          <!-- Annotation processor to generate the JPA 2.0 metamodel classes 
206              for typesafe criteria queries -->
207          <dependency>
208              <groupId>org.hibernate</groupId>
209              <artifactId>hibernate-jpamodelgen</artifactId>
210              <scope>provided</scope>
211          </dependency>
212  
213          <!-- Needed for running tests (you may also use TestNG) -->
214          <dependency>
215              <groupId>junit</groupId>
216              <artifactId>junit</artifactId>
217              <scope>test</scope>
218          </dependency>
219  
220          <!-- Optional, but highly recommended -->
221          <!-- Arquillian allows you to test enterprise code such as EJBs and 
222              Transactional(JTA) JPA from JUnit/TestNG -->
223          <dependency>
224              <groupId>org.jboss.arquillian.junit</groupId>
225              <artifactId>arquillian-junit-container</artifactId>
226              <scope>test</scope>
227          </dependency>
228  
229          <dependency>
230              <groupId>org.jboss.arquillian.protocol</groupId>
231              <artifactId>arquillian-protocol-servlet</artifactId>
232              <scope>test</scope>
233          </dependency>
234          
235          <dependency>
236              <groupId>org.jboss.shrinkwrap.resolver</groupId>
237              <artifactId>shrinkwrap-resolver-depchain</artifactId>
```
  * file:///tmp/source-code/backend-v2/pom.xml
      * Dependency `javax.inject:javax.inject` has to be replaced with `io.quarkus:quarkus-arc` artifact.
      * Code Snippet:
```java
 48              </releases>
 49              <snapshots>
 50                  <enabled>false</enabled>
 51              </snapshots>
 52          </repository>
 53          <repository>
 54              <id>redhat.ea</id>
 55              <name>Red Hat Early Access Repository</name>
 56              <url>https://maven.repository.redhat.com/earlyaccess/all</url>
 57              <snapshots>
 58                  <enabled>false</enabled>
 59              </snapshots>
 60              <releases>
 61                  <enabled>true</enabled>
 62              </releases>
 63          </repository>
 64      </repositories>
 65  
 66      <pluginRepositories>
 67          <pluginRepository>
 68              <id>redhat-ga-repository</id>
 69              <url>https://maven.repository.redhat.com/ga/</url>
 70              <releases>
 71                  <enabled>true</enabled>
 72              </releases>
 73              <snapshots>
 74                  <enabled>false</enabled>
 75              </snapshots>
 76          </pluginRepository>
 77          <pluginRepository>
 78              <id>jboss-earlyaccess-plugin-repository</id>
 79              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 80              <releases>
 81                  <enabled>true</enabled>
 82              </releases>
 83              <snapshots>
 84                  <enabled>false</enabled>
 85              </snapshots>
 86          </pluginRepository>
 87      </pluginRepositories>
 88  
 89      <properties>
 90          <!-- Explicitly declaring the source encoding eliminates the following 
 91              message: -->
 92          <!-- [WARNING] Using platform encoding (UTF-8 actually) to copy filtered 
 93              resources, i.e. build is platform dependent! -->
 94          <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
 95          <!-- Timestamp format for the maven.build.timestamp property -->
 96          <!-- You can reference property in pom.xml or filtered resources 
 97              (must enable third-party plugin if using Maven < 2.1) -->
 98          <maven.build.timestamp.format>yyyyMMdd'T'HHmmss</maven.build.timestamp.format>
 99          <!-- Specify the JBoss EAP directory to be the JBOSS_HOME environment
100              variable -->
101          <jboss.home>${env.JBOSS_HOME}</jboss.home>
102          <version.jboss.bom.eap>7.0.7.GA</version.jboss.bom.eap>
103          <version.wildfly.maven.plugin>1.0.2.Final</version.wildfly.maven.plugin>
104          <version.surefire.plugin>2.10</version.surefire.plugin>
105          <buildhelper.plugin.version>1.7</buildhelper.plugin.version>
106          <fabric8.maven.plugin.version>3.5.25</fabric8.maven.plugin.version>
107          <docker.image.name>ceposta/%a:%l</docker.image.name>
108          <ffj4.version>1.6.5</ffj4.version>
109          <version.org.jboss.arquillian>1.1.12.Final</version.org.jboss.arquillian>
110          <version.org.wildfly.arquillian.container>2.0.0.Final</version.org.wildfly.arquillian.container>
111      </properties>
112  
113      <dependencyManagement>
114          <dependencies>
115              <dependency>
116                  <groupId>org.jboss.arquillian</groupId>
117                  <artifactId>arquillian-bom</artifactId>
118                  <version>${version.org.jboss.arquillian}</version>
119                  <type>pom</type>
120                  <scope>import</scope>
121              </dependency>
122              <dependency>
123                  <groupId>org.jboss.bom</groupId>
124                  <artifactId>jboss-eap-javaee7-with-tools</artifactId>
125                  <version>${version.jboss.bom.eap}</version>
126                  <type>pom</type>
127                  <scope>import</scope>
128              </dependency>
129  
130          </dependencies>
131      </dependencyManagement>
132  
133      <dependencies>
134  
135          <!-- First declare the APIs we depend on and need for compilation. 
136              All of them are provided by JBoss EAP -->
137  
138          <!-- Import the CDI API, we use provided scope as the API is included 
139              in JBoss EAP -->
140          <dependency>
141              <groupId>javax.enterprise</groupId>
142              <artifactId>cdi-api</artifactId>
143              <scope>provided</scope>
144          </dependency>
145          
146          <dependency>
147              <groupId>javax.inject</groupId>
148              <artifactId>javax.inject</artifactId>
149              <scope>provided</scope>
150          </dependency>
151          
152          <dependency>
153              <groupId>javax.validation</groupId>
154              <artifactId>validation-api</artifactId>
155              <scope>provided</scope>
156          </dependency>
157         
158          <!-- Import the Common Annotations API (JSR-250), we use provided 
159              scope as the API is included in JBoss EAP -->
160          <dependency>
161              <groupId>org.jboss.spec.javax.annotation</groupId>
162              <artifactId>jboss-annotations-api_1.2_spec</artifactId>
163              <scope>provided</scope>
164          </dependency>
165  
166          <!-- Import the JAX-RS API, we use provided scope as the API is included 
167              in JBoss EAP -->
168          <dependency>
169              <groupId>org.jboss.spec.javax.ws.rs</groupId>
170              <artifactId>jboss-jaxrs-api_2.0_spec</artifactId>
171              <scope>provided</scope>
172          </dependency>
173  
174          <!-- Import the JPA API, we use provided scope as the API is included 
175              in JBoss EAP -->
176          <dependency>
177              <groupId>org.hibernate.javax.persistence</groupId>
178              <artifactId>hibernate-jpa-2.1-api</artifactId>
179              <scope>provided</scope>
180          </dependency>
181  
182          <!-- Import the EJB API, we use provided scope as the API is included 
183              in JBoss EAP -->
184          <dependency>
185              <groupId>org.jboss.spec.javax.ejb</groupId>
186              <artifactId>jboss-ejb-api_3.2_spec</artifactId>
187              <scope>provided</scope>
188          </dependency>
189  
190          <!-- Import the Servlet API, we use provided scope as the API is 
191              included in JBoss EAP -->
192          <dependency>
193              <groupId>org.jboss.spec.javax.servlet</groupId>
194              <artifactId>jboss-servlet-api_3.1_spec</artifactId>
195              <scope>provided</scope>
196          </dependency>
197  
198          <dependency>
199              <groupId>org.ff4j</groupId>
200              <artifactId>ff4j-core</artifactId>
201              <version>${ffj4.version}</version>
202          </dependency>
203          <dependency>
204              <groupId>org.ff4j</groupId>
205              <artifactId>ff4j-web</artifactId>
206              <version>${ffj4.version}</version>
207          </dependency>
208  
209          <!-- JSR-303 (Bean Validation) Implementation -->
210          <!-- Provides portable constraints such as @Email -->
211          <!-- Hibernate Validator is shipped in JBoss EAP -->
212          <dependency>
213              <groupId>org.hibernate</groupId>
214              <artifactId>hibernate-validator</artifactId>
215              <scope>provided</scope>
216              <exclusions>
217                  <exclusion>
218                      <groupId>org.slf4j</groupId>
219                      <artifactId>slf4j-api</artifactId>
220                  </exclusion>
221              </exclusions>
222          </dependency>
223  
224  
225          <!-- Now we declare any tools needed -->
226  
227          <!-- Annotation processor to generate the JPA 2.0 metamodel classes 
228              for typesafe criteria queries -->
229          <dependency>
230              <groupId>org.hibernate</groupId>
231              <artifactId>hibernate-jpamodelgen</artifactId>
232              <scope>provided</scope>
233          </dependency>
234  
235          <!-- Needed for running tests (you may also use TestNG) -->
236          <dependency>
237              <groupId>junit</groupId>
238              <artifactId>junit</artifactId>
239              <scope>test</scope>
240          </dependency>
241  
242          <!-- For service virtualization/mocking-->
243          <dependency>
244              <groupId>io.specto</groupId>
245              <artifactId>hoverfly-java</artifactId>
246              <version>0.8.0</version>
247              <scope>test</scope>
248          </dependency>
```
  * file:///tmp/source-code/monolith/pom.xml
      * Dependency `javax.inject:javax.inject` has to be replaced with `io.quarkus:quarkus-arc` artifact.
      * Code Snippet:
```java
 37                  <enabled>true</enabled>
 38              </releases>
 39              <snapshots>
 40                  <enabled>false</enabled>
 41              </snapshots>
 42          </repository>
 43          <repository>
 44              <id>jboss-earlyaccess-repository</id>
 45              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 46              <releases>
 47                  <enabled>true</enabled>
 48              </releases>
 49              <snapshots>
 50                  <enabled>false</enabled>
 51              </snapshots>
 52          </repository>
 53          <repository>
 54              <id>redhat.ea</id>
 55              <name>Red Hat Early Access Repository</name>
 56              <url>https://maven.repository.redhat.com/earlyaccess/all</url>
 57              <snapshots>
 58                  <enabled>false</enabled>
 59              </snapshots>
 60              <releases>
 61                  <enabled>true</enabled>
 62              </releases>
 63          </repository>
 64      </repositories>
 65  
 66      <pluginRepositories>
 67          <pluginRepository>
 68              <id>redhat-ga-repository</id>
 69              <url>https://maven.repository.redhat.com/ga/</url>
 70              <releases>
 71                  <enabled>true</enabled>
 72              </releases>
 73              <snapshots>
 74                  <enabled>false</enabled>
 75              </snapshots>
 76          </pluginRepository>
 77          <pluginRepository>
 78              <id>jboss-earlyaccess-plugin-repository</id>
 79              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 80              <releases>
 81                  <enabled>true</enabled>
 82              </releases>
 83              <snapshots>
 84                  <enabled>false</enabled>
 85              </snapshots>
 86          </pluginRepository>
 87      </pluginRepositories>
 88  
 89      <properties>
 90          <!-- Explicitly declaring the source encoding eliminates the following 
 91              message: -->
 92          <!-- [WARNING] Using platform encoding (UTF-8 actually) to copy filtered 
 93              resources, i.e. build is platform dependent! -->
 94          <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
 95          <!-- Timestamp format for the maven.build.timestamp property -->
 96          <!-- You can reference property in pom.xml or filtered resources 
 97              (must enable third-party plugin if using Maven < 2.1) -->
 98          <maven.build.timestamp.format>yyyyMMdd'T'HHmmss</maven.build.timestamp.format>
 99          <!-- Specify the JBoss EAP directory to be the JBOSS_HOME environment
100              variable -->
101          <jboss.home>${env.JBOSS_HOME}</jboss.home>
102          <version.jboss.bom.eap>7.0.7.GA</version.jboss.bom.eap>
103          <version.wildfly.maven.plugin>1.0.2.Final</version.wildfly.maven.plugin>
104          <version.surefire.plugin>2.10</version.surefire.plugin>
105          <buildhelper.plugin.version>1.7</buildhelper.plugin.version>
106          <fabric8.maven.plugin.version>3.5.25</fabric8.maven.plugin.version>
107          <docker.image.name>%g/%a:%l</docker.image.name>
108      </properties>
109  
110      <dependencyManagement>
111          <dependencies>
112              <dependency>
113                  <groupId>org.jboss.bom</groupId>
114                  <artifactId>jboss-eap-javaee7-with-tools</artifactId>
115                  <version>${version.jboss.bom.eap}</version>
116                  <type>pom</type>
117                  <scope>import</scope>
118              </dependency>
119          </dependencies>
120      </dependencyManagement>
121  
122      <dependencies>
123  
124          <!-- First declare the APIs we depend on and need for compilation. 
125              All of them are provided by JBoss EAP -->
126  
127          <!-- Import the CDI API, we use provided scope as the API is included 
128              in JBoss EAP -->
129          <dependency>
130              <groupId>javax.enterprise</groupId>
131              <artifactId>cdi-api</artifactId>
132              <scope>provided</scope>
133          </dependency>
134  
135          <dependency>
136              <groupId>javax.inject</groupId>
137              <artifactId>javax.inject</artifactId>
138              <scope>provided</scope>
139          </dependency>
140  
141          <dependency>
142              <groupId>javax.validation</groupId>
143              <artifactId>validation-api</artifactId>
144              <scope>provided</scope>
145          </dependency>
146  
147          <!-- Import the Common Annotations API (JSR-250), we use provided 
148              scope as the API is included in JBoss EAP -->
149          <dependency>
150              <groupId>org.jboss.spec.javax.annotation</groupId>
151              <artifactId>jboss-annotations-api_1.2_spec</artifactId>
152              <scope>provided</scope>
153          </dependency>
154  
155          <!-- Import the JAX-RS API, we use provided scope as the API is included 
156              in JBoss EAP -->
157          <dependency>
158              <groupId>org.jboss.spec.javax.ws.rs</groupId>
159              <artifactId>jboss-jaxrs-api_2.0_spec</artifactId>
160              <scope>provided</scope>
161          </dependency>
162  
163          <!-- Import the JPA API, we use provided scope as the API is included 
164              in JBoss EAP -->
165          <dependency>
166              <groupId>org.hibernate.javax.persistence</groupId>
167              <artifactId>hibernate-jpa-2.1-api</artifactId>
168              <scope>provided</scope>
169          </dependency>
170  
171          <!-- Import the EJB API, we use provided scope as the API is included 
172              in JBoss EAP -->
173          <dependency>
174              <groupId>org.jboss.spec.javax.ejb</groupId>
175              <artifactId>jboss-ejb-api_3.2_spec</artifactId>
176              <scope>provided</scope>
177          </dependency>
178  
179          <!-- Import the Servlet API, we use provided scope as the API is 
180              included in JBoss EAP -->
181          <dependency>
182              <groupId>org.jboss.spec.javax.servlet</groupId>
183              <artifactId>jboss-servlet-api_3.1_spec</artifactId>
184              <scope>provided</scope>
185          </dependency>
186  
187          <!-- JSR-303 (Bean Validation) Implementation -->
188          <!-- Provides portable constraints such as @Email -->
189          <!-- Hibernate Validator is shipped in JBoss EAP -->
190          <dependency>
191              <groupId>org.hibernate</groupId>
192              <artifactId>hibernate-validator</artifactId>
193              <scope>provided</scope>
194              <exclusions>
195                  <exclusion>
196                      <groupId>org.slf4j</groupId>
197                      <artifactId>slf4j-api</artifactId>
198                  </exclusion>
199              </exclusions>
200          </dependency>
201  
202  
203          <!-- Now we declare any tools needed -->
204  
205          <!-- Annotation processor to generate the JPA 2.0 metamodel classes 
206              for typesafe criteria queries -->
207          <dependency>
208              <groupId>org.hibernate</groupId>
209              <artifactId>hibernate-jpamodelgen</artifactId>
210              <scope>provided</scope>
211          </dependency>
212  
213          <!-- Needed for running tests (you may also use TestNG) -->
214          <dependency>
215              <groupId>junit</groupId>
216              <artifactId>junit</artifactId>
217              <scope>test</scope>
218          </dependency>
219  
220          <!-- Optional, but highly recommended -->
221          <!-- Arquillian allows you to test enterprise code such as EJBs and 
222              Transactional(JTA) JPA from JUnit/TestNG -->
223          <dependency>
224              <groupId>org.jboss.arquillian.junit</groupId>
225              <artifactId>arquillian-junit-container</artifactId>
226              <scope>test</scope>
227          </dependency>
228  
229          <dependency>
230              <groupId>org.jboss.arquillian.protocol</groupId>
231              <artifactId>arquillian-protocol-servlet</artifactId>
232              <scope>test</scope>
233          </dependency>
234  
235          <dependency>
236              <groupId>org.jboss.shrinkwrap.resolver</groupId>
237              <artifactId>shrinkwrap-resolver-depchain</artifactId>
```
### #2 - cdi-to-quarkus-00030
* Category: potential
* Effort: 3
* Description: `beans.xml` descriptor content is ignored
`beans.xml` descriptor content is ignored and it could be removed from the application.. Refer to the guide referenced below to check the supported CDI feature in Quarkus.
* Labels: konveyor.io/source=java-ee, konveyor.io/target=quarkus
* Incidents
  * file:///tmp/source-code/backend-v1/src/main/webapp/WEB-INF/beans.xml
      * `beans.xml` descriptor content is ignored and it could be removed from the application.. Refer to the guide referenced below to check the supported CDI feature in Quarkus.
  * file:///tmp/source-code/backend-v2/src/main/webapp/WEB-INF/beans.xml
      * `beans.xml` descriptor content is ignored and it could be removed from the application.. Refer to the guide referenced below to check the supported CDI feature in Quarkus.
  * file:///tmp/source-code/monolith/src/main/webapp/WEB-INF/beans.xml
      * `beans.xml` descriptor content is ignored and it could be removed from the application.. Refer to the guide referenced below to check the supported CDI feature in Quarkus.
### #3 - cdi-to-quarkus-00040
* Category: potential
* Effort: 1
* Description: Producer annotation no longer required
In Quarkus, you can skip the @Produces annotation completely if the producer method is annotated with a scope annotation, a stereotype or a qualifier... This field could be accessed using a `@Named` getter method instead.
* Labels: konveyor.io/source=java-ee, konveyor.io/target=quarkus
* Links
  * Quarkus Simplified Producer Method Declaration: https://quarkus.io/guides/cdi-reference#simplified-producer-method-declaration
* Incidents
  * file:///tmp/source-code/backend-v1/src/main/java/org/jboss/examples/ticketmonster/util/Resources.java
      * In Quarkus, you can skip the @Produces annotation completely if the producer method is annotated with a scope annotation, a stereotype or a qualifier... This field could be accessed using a `@Named` getter method instead.
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.util;
  2  
  3  import java.util.logging.Logger;
  4  
  5  import javax.enterprise.inject.Produces;
  6  import javax.enterprise.inject.spi.InjectionPoint;
  7  import javax.persistence.EntityManager;
  8  import javax.persistence.PersistenceContext;
  9  
 10  /**
 11   * This class uses CDI to alias Java EE resources, such as the persistence context, to CDI beans
 12   * 
 13   * <p>
 14   * Example injection on a managed bean field:
 15   * </p>
 16   * 
 17   * <pre>
 18   * &#064;Inject
 19   * private EntityManager em;
 20   * </pre>
 21   */
 22  public class Resources {
 23  
 24      /**
 25       * Alias the persistence context
 26       */
 27      // use @SuppressWarnings to tell IDE to ignore warnings about field not being referenced directly
 28     @SuppressWarnings("unused")
 29     @Produces
 30     @PersistenceContext
 31     private EntityManager em;
 32     
 33     /**
 34      * Provider injectable loggers based around Java Util Logging.
 35      * @param injectionPoint
 36      * @return
 37      */
 38     @Produces
 39     public Logger produceLog(InjectionPoint injectionPoint) {
 40        return Logger.getLogger(injectionPoint.getMember().getDeclaringClass().getName());
 41     }
 42   
 43  }

```
  * file:///tmp/source-code/backend-v1/src/main/java/org/jboss/examples/ticketmonster/util/Resources.java
      * In Quarkus, you can skip the @Produces annotation completely if the producer method is annotated with a scope annotation, a stereotype or a qualifier... This field could be accessed using a `@Named` getter method instead.
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.util;
  2  
  3  import java.util.logging.Logger;
  4  
  5  import javax.enterprise.inject.Produces;
  6  import javax.enterprise.inject.spi.InjectionPoint;
  7  import javax.persistence.EntityManager;
  8  import javax.persistence.PersistenceContext;
  9  
 10  /**
 11   * This class uses CDI to alias Java EE resources, such as the persistence context, to CDI beans
 12   * 
 13   * <p>
 14   * Example injection on a managed bean field:
 15   * </p>
 16   * 
 17   * <pre>
 18   * &#064;Inject
 19   * private EntityManager em;
 20   * </pre>
 21   */
 22  public class Resources {
 23  
 24      /**
 25       * Alias the persistence context
 26       */
 27      // use @SuppressWarnings to tell IDE to ignore warnings about field not being referenced directly
 28     @SuppressWarnings("unused")
 29     @Produces
 30     @PersistenceContext
 31     private EntityManager em;
 32     
 33     /**
 34      * Provider injectable loggers based around Java Util Logging.
 35      * @param injectionPoint
 36      * @return
 37      */
 38     @Produces
 39     public Logger produceLog(InjectionPoint injectionPoint) {
 40        return Logger.getLogger(injectionPoint.getMember().getDeclaringClass().getName());
 41     }
 42   
 43  }

```
  * file:///tmp/source-code/backend-v2/src/main/java/org/jboss/examples/ticketmonster/util/FF4jFactory.java
      * In Quarkus, you can skip the @Produces annotation completely if the producer method is annotated with a scope annotation, a stereotype or a qualifier... This field could be accessed using a `@Named` getter method instead.
      * Code Snippet:
```java
  1  /**
  2   * Licensed to the Apache Software Foundation (ASF) under one or more
  3   * contributor license agreements.  See the NOTICE file distributed with
  4   * this work for additional information regarding copyright ownership.
  5   * The ASF licenses this file to You under the Apache License, Version 2.0
  6   * (the "License"); you may not use this file except in compliance with
  7   * the License.  You may obtain a copy of the License at
  8   * <p>
  9   * http://www.apache.org/licenses/LICENSE-2.0
 10   * <p>
 11   * Unless required by applicable law or agreed to in writing, software
 12   * distributed under the License is distributed on an "AS IS" BASIS,
 13   * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 14   * See the License for the specific language governing permissions and
 15   * limitations under the License.
 16   */
 17  package org.jboss.examples.ticketmonster.util;
 18  
 19  import org.ff4j.FF4j;
 20  import org.ff4j.web.FF4jProvider;
 21  
 22  import javax.enterprise.context.ApplicationScoped;
 23  import javax.enterprise.inject.Produces;
 24  
 25  /**
 26   * Created by ceposta 
 27   * <a href="http://christianposta.com/blog>http://christianposta.com/blog</a>.
 28   */
 29  @ApplicationScoped
 30  public class FF4jFactory implements FF4jProvider{
 31  
 32      private static FF4j rc = new FF4j("ff4j.xml");
 33  
 34      @Produces
 35      public static FF4j ff4j(){
 36          return rc;
 37      }
 38  
 39      @Override
 40      public FF4j getFF4j() {
 41          return rc;
 42      }
 43  }

```
  * file:///tmp/source-code/backend-v2/src/main/java/org/jboss/examples/ticketmonster/util/Resources.java
      * In Quarkus, you can skip the @Produces annotation completely if the producer method is annotated with a scope annotation, a stereotype or a qualifier... This field could be accessed using a `@Named` getter method instead.
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.util;
  2  
  3  import java.util.logging.Logger;
  4  
  5  import javax.enterprise.inject.Produces;
  6  import javax.enterprise.inject.spi.InjectionPoint;
  7  import javax.persistence.EntityManager;
  8  import javax.persistence.PersistenceContext;
  9  
 10  /**
 11   * This class uses CDI to alias Java EE resources, such as the persistence context, to CDI beans
 12   * 
 13   * <p>
 14   * Example injection on a managed bean field:
 15   * </p>
 16   * 
 17   * <pre>
 18   * &#064;Inject
 19   * private EntityManager em;
 20   * </pre>
 21   */
 22  public class Resources {
 23  
 24      /**
 25       * Alias the persistence context
 26       */
 27      // use @SuppressWarnings to tell IDE to ignore warnings about field not being referenced directly
 28     @SuppressWarnings("unused")
 29     @Produces
 30     @PersistenceContext
 31     private EntityManager em;
 32     
 33     /**
 34      * Provider injectable loggers based around Java Util Logging.
 35      * @param injectionPoint
 36      * @return
 37      */
 38     @Produces
 39     public Logger produceLog(InjectionPoint injectionPoint) {
 40        return Logger.getLogger(injectionPoint.getMember().getDeclaringClass().getName());
 41     }
 42   
 43  }

```
  * file:///tmp/source-code/backend-v2/src/main/java/org/jboss/examples/ticketmonster/util/Resources.java
      * In Quarkus, you can skip the @Produces annotation completely if the producer method is annotated with a scope annotation, a stereotype or a qualifier... This field could be accessed using a `@Named` getter method instead.
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.util;
  2  
  3  import java.util.logging.Logger;
  4  
  5  import javax.enterprise.inject.Produces;
  6  import javax.enterprise.inject.spi.InjectionPoint;
  7  import javax.persistence.EntityManager;
  8  import javax.persistence.PersistenceContext;
  9  
 10  /**
 11   * This class uses CDI to alias Java EE resources, such as the persistence context, to CDI beans
 12   * 
 13   * <p>
 14   * Example injection on a managed bean field:
 15   * </p>
 16   * 
 17   * <pre>
 18   * &#064;Inject
 19   * private EntityManager em;
 20   * </pre>
 21   */
 22  public class Resources {
 23  
 24      /**
 25       * Alias the persistence context
 26       */
 27      // use @SuppressWarnings to tell IDE to ignore warnings about field not being referenced directly
 28     @SuppressWarnings("unused")
 29     @Produces
 30     @PersistenceContext
 31     private EntityManager em;
 32     
 33     /**
 34      * Provider injectable loggers based around Java Util Logging.
 35      * @param injectionPoint
 36      * @return
 37      */
 38     @Produces
 39     public Logger produceLog(InjectionPoint injectionPoint) {
 40        return Logger.getLogger(injectionPoint.getMember().getDeclaringClass().getName());
 41     }
 42   
 43  }

```
  * file:///tmp/source-code/monolith/src/main/java/org/jboss/examples/ticketmonster/util/Resources.java
      * In Quarkus, you can skip the @Produces annotation completely if the producer method is annotated with a scope annotation, a stereotype or a qualifier... This field could be accessed using a `@Named` getter method instead.
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.util;
  2  
  3  import java.util.logging.Logger;
  4  
  5  import javax.enterprise.inject.Produces;
  6  import javax.enterprise.inject.spi.InjectionPoint;
  7  import javax.persistence.EntityManager;
  8  import javax.persistence.PersistenceContext;
  9  
 10  /**
 11   * This class uses CDI to alias Java EE resources, such as the persistence context, to CDI beans
 12   * 
 13   * <p>
 14   * Example injection on a managed bean field:
 15   * </p>
 16   * 
 17   * <pre>
 18   * &#064;Inject
 19   * private EntityManager em;
 20   * </pre>
 21   */
 22  public class Resources {
 23  
 24      /**
 25       * Alias the persistence context
 26       */
 27      // use @SuppressWarnings to tell IDE to ignore warnings about field not being referenced directly
 28     @SuppressWarnings("unused")
 29     @Produces
 30     @PersistenceContext
 31     private EntityManager em;
 32     
 33     /**
 34      * Provider injectable loggers based around Java Util Logging.
 35      * @param injectionPoint
 36      * @return
 37      */
 38     @Produces
 39     public Logger produceLog(InjectionPoint injectionPoint) {
 40        return Logger.getLogger(injectionPoint.getMember().getDeclaringClass().getName());
 41     }
 42   
 43  }

```
  * file:///tmp/source-code/monolith/src/main/java/org/jboss/examples/ticketmonster/util/Resources.java
      * In Quarkus, you can skip the @Produces annotation completely if the producer method is annotated with a scope annotation, a stereotype or a qualifier... This field could be accessed using a `@Named` getter method instead.
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.util;
  2  
  3  import java.util.logging.Logger;
  4  
  5  import javax.enterprise.inject.Produces;
  6  import javax.enterprise.inject.spi.InjectionPoint;
  7  import javax.persistence.EntityManager;
  8  import javax.persistence.PersistenceContext;
  9  
 10  /**
 11   * This class uses CDI to alias Java EE resources, such as the persistence context, to CDI beans
 12   * 
 13   * <p>
 14   * Example injection on a managed bean field:
 15   * </p>
 16   * 
 17   * <pre>
 18   * &#064;Inject
 19   * private EntityManager em;
 20   * </pre>
 21   */
 22  public class Resources {
 23  
 24      /**
 25       * Alias the persistence context
 26       */
 27      // use @SuppressWarnings to tell IDE to ignore warnings about field not being referenced directly
 28     @SuppressWarnings("unused")
 29     @Produces
 30     @PersistenceContext
 31     private EntityManager em;
 32     
 33     /**
 34      * Provider injectable loggers based around Java Util Logging.
 35      * @param injectionPoint
 36      * @return
 37      */
 38     @Produces
 39     public Logger produceLog(InjectionPoint injectionPoint) {
 40        return Logger.getLogger(injectionPoint.getMember().getDeclaringClass().getName());
 41     }
 42   
 43  }

```
### #4 - cdi-to-quarkus-00050
* Category: potential
* Effort: 1
* Description: Stateless annotation can be replaced with scope
Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
* Labels: konveyor.io/source=java-ee, konveyor.io/target=quarkus
* Links
  * Quarkus CDI reference: https://quarkus.io/guides/cdi-reference
* Incidents
  * file:///tmp/source-code/backend-v1/src/main/java/org/jboss/examples/ticketmonster/rest/BookingEndpoint.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import java.util.ArrayList;
  4  import java.util.List;
  5  
  6  import javax.ejb.Stateless;
  7  import javax.persistence.EntityManager;
  8  import javax.persistence.NoResultException;
  9  import javax.persistence.OptimisticLockException;
 10  import javax.persistence.PersistenceContext;
 11  import javax.persistence.TypedQuery;
 12  import javax.ws.rs.Consumes;
 13  import javax.ws.rs.DELETE;
 14  import javax.ws.rs.GET;
 15  import javax.ws.rs.POST;
 16  import javax.ws.rs.PUT;
 17  import javax.ws.rs.Path;
 18  import javax.ws.rs.PathParam;
 19  import javax.ws.rs.Produces;
 20  import javax.ws.rs.QueryParam;
 21  import javax.ws.rs.core.Response;
 22  import javax.ws.rs.core.Response.Status;
 23  import javax.ws.rs.core.UriBuilder;
 24  import org.jboss.examples.ticketmonster.rest.dto.BookingDTO;
 25  import org.jboss.examples.ticketmonster.model.Booking;
 26  
 27  /**
 28   * 
 29   */
 30  @Stateless
 31  @Path("forge/bookings")
 32  public class BookingEndpoint
 33  {
 34     @PersistenceContext(unitName = "primary")
 35     private EntityManager em;
 36  
 37     @POST
 38     @Consumes("application/json")
 39     public Response create(BookingDTO dto)
 40     {
 41        Booking entity = dto.fromDTO(null, em);
 42        em.persist(entity);
 43        return Response.created(UriBuilder.fromResource(BookingEndpoint.class).path(String.valueOf(entity.getId())).build()).build();
 44     }
 45  
 46     @DELETE
 47     @Path("/{id:[0-9][0-9]*}")
 48     public Response deleteById(@PathParam("id") Long id)
 49     {
 50        Booking entity = em.find(Booking.class, id);
 51        if (entity == null)
 52        {
 53           return Response.status(Status.NOT_FOUND).build();
 54        }
 55        em.remove(entity);
 56        return Response.noContent().build();
 57     }
 58  
 59     @GET
 60     @Path("/{id:[0-9][0-9]*}")
 61     @Produces("application/json")
 62     public Response findById(@PathParam("id") Long id)
 63     {
 64        TypedQuery<Booking> findByIdQuery = em.createQuery("SELECT DISTINCT b FROM Booking b LEFT JOIN FETCH b.tickets LEFT JOIN FETCH b.performance WHERE b.id = :entityId ORDER BY b.id", Booking.class);
 65        findByIdQuery.setParameter("entityId", id);
 66        Booking entity;
 67        try
 68        {
 69           entity = findByIdQuery.getSingleResult();
 70        }
 71        catch (NoResultException nre)
 72        {
 73           entity = null;
 74        }
 75        if (entity == null)
 76        {
 77           return Response.status(Status.NOT_FOUND).build();
 78        }
 79        BookingDTO dto = new BookingDTO(entity);
 80        return Response.ok(dto).build();
 81     }
 82  
 83     @GET
 84     @Produces("application/json")
 85     public List<BookingDTO> listAll(@QueryParam("start") Integer startPosition, @QueryParam("max") Integer maxResult)
 86     {
 87        TypedQuery<Booking> findAllQuery = em.createQuery("SELECT DISTINCT b FROM Booking b LEFT JOIN FETCH b.tickets LEFT JOIN FETCH b.performance ORDER BY b.id", Booking.class);
 88        if (startPosition != null)
 89        {
 90           findAllQuery.setFirstResult(startPosition);
 91        }
 92        if (maxResult != null)
 93        {
 94           findAllQuery.setMaxResults(maxResult);
 95        }
 96        final List<Booking> searchResults = findAllQuery.getResultList();
 97        final List<BookingDTO> results = new ArrayList<BookingDTO>();
 98        for (Booking searchResult : searchResults)
 99        {
100           BookingDTO dto = new BookingDTO(searchResult);
101           results.add(dto);
102        }
103        return results;
104     }
105  
106     @PUT
107     @Path("/{id:[0-9][0-9]*}")
108     @Consumes("application/json")
109     public Response update(@PathParam("id") Long id, BookingDTO dto)
110     {
111        TypedQuery<Booking> findByIdQuery = em.createQuery("SELECT DISTINCT b FROM Booking b LEFT JOIN FETCH b.tickets LEFT JOIN FETCH b.performance WHERE b.id = :entityId ORDER BY b.id", Booking.class);
112        findByIdQuery.setParameter("entityId", id);
113        Booking entity;
114        try
115        {
116           entity = findByIdQuery.getSingleResult();
117        }
118        catch (NoResultException nre)
119        {
120           entity = null;
121        }
122        entity = dto.fromDTO(entity, em);
123        try
124        {
125           entity = em.merge(entity);
126        }
127        catch (OptimisticLockException e)
128        {
129           return Response.status(Response.Status.CONFLICT).entity(e.getEntity()).build();
130        }
```
  * file:///tmp/source-code/backend-v1/src/main/java/org/jboss/examples/ticketmonster/rest/BookingService.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import java.util.ArrayList;
  4  import java.util.Collections;
  5  import java.util.HashMap;
  6  import java.util.List;
  7  import java.util.Map;
  8  import java.util.Set;
  9  import java.util.TreeMap;
 10  
 11  import javax.ejb.Stateless;
 12  import javax.enterprise.event.Event;
 13  import javax.inject.Inject;
 14  import javax.validation.ConstraintViolation;
 15  import javax.validation.ConstraintViolationException;
 16  import javax.ws.rs.Consumes;
 17  import javax.ws.rs.DELETE;
 18  import javax.ws.rs.POST;
 19  import javax.ws.rs.Path;
 20  import javax.ws.rs.PathParam;
 21  import javax.ws.rs.core.MediaType;
 22  import javax.ws.rs.core.MultivaluedHashMap;
 23  import javax.ws.rs.core.Response;
 24  
 25  import org.jboss.examples.ticketmonster.model.Booking;
 26  import org.jboss.examples.ticketmonster.model.Performance;
 27  import org.jboss.examples.ticketmonster.model.Seat;
 28  import org.jboss.examples.ticketmonster.model.Section;
 29  import org.jboss.examples.ticketmonster.model.Ticket;
 30  import org.jboss.examples.ticketmonster.model.TicketCategory;
 31  import org.jboss.examples.ticketmonster.model.TicketPrice;
 32  import org.jboss.examples.ticketmonster.service.AllocatedSeats;
 33  import org.jboss.examples.ticketmonster.service.SeatAllocationService;
 34  import org.jboss.examples.ticketmonster.util.qualifier.Cancelled;
 35  import org.jboss.examples.ticketmonster.util.qualifier.Created;
 36  
 37  /**
 38   * <p>
 39   *     A JAX-RS endpoint for handling {@link Booking}s. Inherits the GET
 40   *     methods from {@link BaseEntityService}, and implements additional REST methods.
 41   * </p>
 42   *
 43   * @author Marius Bogoevici
 44   * @author Pete Muir
 45   */
 46  @Path("/bookings")
 47  /**
 48   * <p>
 49   *     This is a stateless service, we declare it as an EJB for transaction demarcation
 50   * </p>
 51   */
 52  @Stateless
 53  public class BookingService extends BaseEntityService<Booking> {
 54  
 55      @Inject
 56      SeatAllocationService seatAllocationService;
 57  
 58      @Inject @Cancelled
 59      private Event<Booking> cancelledBookingEvent;
 60  
 61      @Inject @Created
 62      private Event<Booking> newBookingEvent;
 63      
 64      public BookingService() {
 65          super(Booking.class);
 66      }
 67      
 68      @DELETE
 69      public Response deleteAllBookings() {
 70      	List<Booking> bookings = getAll(new MultivaluedHashMap<String, String>());
 71      	for (Booking booking : bookings) {
 72      		deleteBooking(booking.getId());
 73      	}
 74          return Response.noContent().build();
 75      }
 76  
 77      /**
 78       * <p>
 79       * Delete a booking by id
 80       * </p>
 81       * @param id
 82       * @return
 83       */
 84      @DELETE
 85      @Path("/{id:[0-9][0-9]*}")
 86      public Response deleteBooking(@PathParam("id") Long id) {
 87          Booking booking = getEntityManager().find(Booking.class, id);
 88          if (booking == null) {
 89              return Response.status(Response.Status.NOT_FOUND).build();
 90          }
 91          getEntityManager().remove(booking);
 92          // Group together seats by section so that we can deallocate them in a group
 93          Map<Section, List<Seat>> seatsBySection = new TreeMap<Section, java.util.List<Seat>>(SectionComparator.instance());
 94          for (Ticket ticket : booking.getTickets()) {
 95              List<Seat> seats = seatsBySection.get(ticket.getSeat().getSection());
 96              if (seats == null) {
 97                  seats = new ArrayList<Seat>();
 98                  seatsBySection.put(ticket.getSeat().getSection(), seats);
 99              }
100              seats.add(ticket.getSeat());
101          }
102          // Deallocate each section block
103          for (Map.Entry<Section, List<Seat>> sectionListEntry : seatsBySection.entrySet()) {
104              seatAllocationService.deallocateSeats( sectionListEntry.getKey(),
105                      booking.getPerformance(), sectionListEntry.getValue());
106          }
107          cancelledBookingEvent.fire(booking);
108          return Response.noContent().build();
109      }
110  
111      /**
112       * <p>
113       *   Create a booking. Data is contained in the bookingRequest object
114       * </p>
115       * @param bookingRequest
116       * @return
117       */
118      @POST
119      /**
120       * <p> Data is received in JSON format. For easy handling, it will be unmarshalled in the support
121       * {@link BookingRequest} class.
122       */
123      @Consumes(MediaType.APPLICATION_JSON)
124      public Response createBooking(BookingRequest bookingRequest) {
125          try {
126              // identify the ticket price categories in this request
127              Set<Long> priceCategoryIds = bookingRequest.getUniquePriceCategoryIds();
128              
129              // load the entities that make up this booking's relationships
130              Performance performance = getEntityManager().find(Performance.class, bookingRequest.getPerformance());
131  
132              // As we can have a mix of ticket types in a booking, we need to load all of them that are relevant, 
133              // id
134              Map<Long, TicketPrice> ticketPricesById = loadTicketPrices(priceCategoryIds);
135  
136              // Now, start to create the booking from the posted data
137              // Set the simple stuff first!
138              Booking booking = new Booking();
139              booking.setContactEmail(bookingRequest.getEmail());
140              booking.setPerformance(performance);
141              booking.setCancellationCode("abc");
142  
143              // Now, we iterate over each ticket that was requested, and organize them by section and category
144              // we want to allocate ticket requests that belong to the same section contiguously
145              Map<Section, Map<TicketCategory, TicketRequest>> ticketRequestsPerSection
146                      = new TreeMap<Section, java.util.Map<TicketCategory, TicketRequest>>(SectionComparator.instance());
147              for (TicketRequest ticketRequest : bookingRequest.getTicketRequests()) {
148                  final TicketPrice ticketPrice = ticketPricesById.get(ticketRequest.getTicketPrice());
149                  if (!ticketRequestsPerSection.containsKey(ticketPrice.getSection())) {
150                      ticketRequestsPerSection
151                              .put(ticketPrice.getSection(), new HashMap<TicketCategory, TicketRequest>());
152                  }
```
  * file:///tmp/source-code/backend-v1/src/main/java/org/jboss/examples/ticketmonster/rest/EventCategoryEndpoint.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import java.util.ArrayList;
  4  import java.util.List;
  5  
  6  import javax.ejb.Stateless;
  7  import javax.persistence.EntityManager;
  8  import javax.persistence.NoResultException;
  9  import javax.persistence.OptimisticLockException;
 10  import javax.persistence.PersistenceContext;
 11  import javax.persistence.TypedQuery;
 12  import javax.ws.rs.Consumes;
 13  import javax.ws.rs.DELETE;
 14  import javax.ws.rs.GET;
 15  import javax.ws.rs.POST;
 16  import javax.ws.rs.PUT;
 17  import javax.ws.rs.Path;
 18  import javax.ws.rs.PathParam;
 19  import javax.ws.rs.Produces;
 20  import javax.ws.rs.QueryParam;
 21  import javax.ws.rs.core.Response;
 22  import javax.ws.rs.core.Response.Status;
 23  import javax.ws.rs.core.UriBuilder;
 24  import org.jboss.examples.ticketmonster.rest.dto.EventCategoryDTO;
 25  import org.jboss.examples.ticketmonster.model.EventCategory;
 26  
 27  /**
 28   * 
 29   */
 30  @Stateless
 31  @Path("/eventcategories")
 32  public class EventCategoryEndpoint
 33  {
 34     @PersistenceContext(unitName = "primary")
 35     private EntityManager em;
 36  
 37     @POST
 38     @Consumes("application/json")
 39     public Response create(EventCategoryDTO dto)
 40     {
 41        EventCategory entity = dto.fromDTO(null, em);
 42        em.persist(entity);
 43        return Response.created(UriBuilder.fromResource(EventCategoryEndpoint.class).path(String.valueOf(entity.getId())).build()).build();
 44     }
 45  
 46     @DELETE
 47     @Path("/{id:[0-9][0-9]*}")
 48     public Response deleteById(@PathParam("id") Long id)
 49     {
 50        EventCategory entity = em.find(EventCategory.class, id);
 51        if (entity == null)
 52        {
 53           return Response.status(Status.NOT_FOUND).build();
 54        }
 55        em.remove(entity);
 56        return Response.noContent().build();
 57     }
 58  
 59     @GET
 60     @Path("/{id:[0-9][0-9]*}")
 61     @Produces("application/json")
 62     public Response findById(@PathParam("id") Long id)
 63     {
 64        TypedQuery<EventCategory> findByIdQuery = em.createQuery("SELECT DISTINCT e FROM EventCategory e WHERE e.id = :entityId ORDER BY e.id", EventCategory.class);
 65        findByIdQuery.setParameter("entityId", id);
 66        EventCategory entity;
 67        try
 68        {
 69           entity = findByIdQuery.getSingleResult();
 70        }
 71        catch (NoResultException nre)
 72        {
 73           entity = null;
 74        }
 75        if (entity == null)
 76        {
 77           return Response.status(Status.NOT_FOUND).build();
 78        }
 79        EventCategoryDTO dto = new EventCategoryDTO(entity);
 80        return Response.ok(dto).build();
 81     }
 82  
 83     @GET
 84     @Produces("application/json")
 85     public List<EventCategoryDTO> listAll(@QueryParam("start") Integer startPosition, @QueryParam("max") Integer maxResult)
 86     {
 87        TypedQuery<EventCategory> findAllQuery = em.createQuery("SELECT DISTINCT e FROM EventCategory e ORDER BY e.id", EventCategory.class);
 88        if (startPosition != null)
 89        {
 90           findAllQuery.setFirstResult(startPosition);
 91        }
 92        if (maxResult != null)
 93        {
 94           findAllQuery.setMaxResults(maxResult);
 95        }
 96        final List<EventCategory> searchResults = findAllQuery.getResultList();
 97        final List<EventCategoryDTO> results = new ArrayList<EventCategoryDTO>();
 98        for (EventCategory searchResult : searchResults)
 99        {
100           EventCategoryDTO dto = new EventCategoryDTO(searchResult);
101           results.add(dto);
102        }
103        return results;
104     }
105  
106     @PUT
107     @Path("/{id:[0-9][0-9]*}")
108     @Consumes("application/json")
109     public Response update(@PathParam("id") Long id, EventCategoryDTO dto)
110     {
111        TypedQuery<EventCategory> findByIdQuery = em.createQuery("SELECT DISTINCT e FROM EventCategory e WHERE e.id = :entityId ORDER BY e.id", EventCategory.class);
112        findByIdQuery.setParameter("entityId", id);
113        EventCategory entity;
114        try
115        {
116           entity = findByIdQuery.getSingleResult();
117        }
118        catch (NoResultException nre)
119        {
120           entity = null;
121        }
122        entity = dto.fromDTO(entity, em);
123        try
124        {
125           entity = em.merge(entity);
126        }
127        catch (OptimisticLockException e)
128        {
129           return Response.status(Response.Status.CONFLICT).entity(e.getEntity()).build();
130        }
```
  * file:///tmp/source-code/backend-v1/src/main/java/org/jboss/examples/ticketmonster/rest/EventEndpoint.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import java.util.ArrayList;
  4  import java.util.List;
  5  
  6  import javax.ejb.Stateless;
  7  import javax.persistence.EntityManager;
  8  import javax.persistence.NoResultException;
  9  import javax.persistence.OptimisticLockException;
 10  import javax.persistence.PersistenceContext;
 11  import javax.persistence.TypedQuery;
 12  import javax.ws.rs.Consumes;
 13  import javax.ws.rs.DELETE;
 14  import javax.ws.rs.GET;
 15  import javax.ws.rs.POST;
 16  import javax.ws.rs.PUT;
 17  import javax.ws.rs.Path;
 18  import javax.ws.rs.PathParam;
 19  import javax.ws.rs.Produces;
 20  import javax.ws.rs.QueryParam;
 21  import javax.ws.rs.core.Response;
 22  import javax.ws.rs.core.Response.Status;
 23  import javax.ws.rs.core.UriBuilder;
 24  import org.jboss.examples.ticketmonster.rest.dto.EventDTO;
 25  import org.jboss.examples.ticketmonster.model.Event;
 26  
 27  /**
 28   * 
 29   */
 30  @Stateless
 31  @Path("forge/events")
 32  public class EventEndpoint
 33  {
 34     @PersistenceContext(unitName = "primary")
 35     private EntityManager em;
 36  
 37     @POST
 38     @Consumes("application/json")
 39     public Response create(EventDTO dto)
 40     {
 41        Event entity = dto.fromDTO(null, em);
 42        em.persist(entity);
 43        return Response.created(UriBuilder.fromResource(EventEndpoint.class).path(String.valueOf(entity.getId())).build()).build();
 44     }
 45  
 46     @DELETE
 47     @Path("/{id:[0-9][0-9]*}")
 48     public Response deleteById(@PathParam("id") Long id)
 49     {
 50        Event entity = em.find(Event.class, id);
 51        if (entity == null)
 52        {
 53           return Response.status(Status.NOT_FOUND).build();
 54        }
 55        em.remove(entity);
 56        return Response.noContent().build();
 57     }
 58  
 59     @GET
 60     @Path("/{id:[0-9][0-9]*}")
 61     @Produces("application/json")
 62     public Response findById(@PathParam("id") Long id)
 63     {
 64        TypedQuery<Event> findByIdQuery = em.createQuery("SELECT DISTINCT e FROM Event e LEFT JOIN FETCH e.mediaItem LEFT JOIN FETCH e.category WHERE e.id = :entityId ORDER BY e.id", Event.class);
 65        findByIdQuery.setParameter("entityId", id);
 66        Event entity;
 67        try
 68        {
 69           entity = findByIdQuery.getSingleResult();
 70        }
 71        catch (NoResultException nre)
 72        {
 73           entity = null;
 74        }
 75        if (entity == null)
 76        {
 77           return Response.status(Status.NOT_FOUND).build();
 78        }
 79        EventDTO dto = new EventDTO(entity);
 80        return Response.ok(dto).build();
 81     }
 82  
 83     @GET
 84     @Produces("application/json")
 85     public List<EventDTO> listAll(@QueryParam("start") Integer startPosition, @QueryParam("max") Integer maxResult)
 86     {
 87        TypedQuery<Event> findAllQuery = em.createQuery("SELECT DISTINCT e FROM Event e LEFT JOIN FETCH e.mediaItem LEFT JOIN FETCH e.category ORDER BY e.id", Event.class);
 88        if (startPosition != null)
 89        {
 90           findAllQuery.setFirstResult(startPosition);
 91        }
 92        if (maxResult != null)
 93        {
 94           findAllQuery.setMaxResults(maxResult);
 95        }
 96        final List<Event> searchResults = findAllQuery.getResultList();
 97        final List<EventDTO> results = new ArrayList<EventDTO>();
 98        for (Event searchResult : searchResults)
 99        {
100           EventDTO dto = new EventDTO(searchResult);
101           results.add(dto);
102        }
103        return results;
104     }
105  
106     @PUT
107     @Path("/{id:[0-9][0-9]*}")
108     @Consumes("application/json")
109     public Response update(@PathParam("id") Long id, EventDTO dto)
110     {
111        TypedQuery<Event> findByIdQuery = em.createQuery("SELECT DISTINCT e FROM Event e LEFT JOIN FETCH e.mediaItem LEFT JOIN FETCH e.category WHERE e.id = :entityId ORDER BY e.id", Event.class);
112        findByIdQuery.setParameter("entityId", id);
113        Event entity;
114        try
115        {
116           entity = findByIdQuery.getSingleResult();
117        }
118        catch (NoResultException nre)
119        {
120           entity = null;
121        }
122        entity = dto.fromDTO(entity, em);
123        try
124        {
125           entity = em.merge(entity);
126        }
127        catch (OptimisticLockException e)
128        {
129           return Response.status(Response.Status.CONFLICT).entity(e.getEntity()).build();
130        }
```
  * file:///tmp/source-code/backend-v1/src/main/java/org/jboss/examples/ticketmonster/rest/EventService.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import java.util.ArrayList;
  4  import java.util.List;
  5  
  6  import javax.ejb.Stateless;
  7  import javax.persistence.criteria.CriteriaBuilder;
  8  import javax.persistence.criteria.Predicate;
  9  import javax.persistence.criteria.Root;
 10  import javax.ws.rs.Path;
 11  import javax.ws.rs.core.MultivaluedMap;
 12  
 13  import org.jboss.examples.ticketmonster.model.Event;
 14  
 15  /**
 16   * <p>
 17   *     A JAX-RS endpoint for handling {@link Event}s. Inherits the actual
 18   *     methods from {@link BaseEntityService}, but implements additional search
 19   *     criteria.
 20   * </p>
 21   *
 22   * @author Marius Bogoevici
 23   */
 24  @Path("/events")
 25  /**
 26   * <p>
 27   *     This is a stateless service, we declare it as an EJB for transaction demarcation
 28   * </p>
 29   */
 30  @Stateless
 31  public class EventService extends BaseEntityService<Event> {
 32  
 33      public EventService() {
 34          super(Event.class);
 35      }
 36  
 37      /**
 38       * <p>
 39       *    We override the method from parent in order to add support for additional search
 40       *    criteria for events.
 41       * </p>
 42       * @param queryParameters - the HTTP query parameters received by the endpoint
 43       * @param criteriaBuilder - @{link CriteriaBuilder} used by the invoker
 44       * @param root  @{link Root} used by the invoker
 45       * @return
 46       */
 47      @Override
 48      protected Predicate[] extractPredicates(
 49              MultivaluedMap<String, String> queryParameters, 
 50              CriteriaBuilder criteriaBuilder, 
 51              Root<Event> root) {
 52          List<Predicate> predicates = new ArrayList<Predicate>() ;
 53          
 54          if (queryParameters.containsKey("category")) {
 55              String category = queryParameters.getFirst("category");
 56              predicates.add(criteriaBuilder.equal(root.get("category").get("id"), category));
 57          }
 58          
 59          return predicates.toArray(new Predicate[]{});
 60      }
 61  }

```
  * file:///tmp/source-code/backend-v1/src/main/java/org/jboss/examples/ticketmonster/rest/MediaItemEndpoint.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import java.util.ArrayList;
  4  import java.util.List;
  5  
  6  import javax.ejb.Stateless;
  7  import javax.persistence.EntityManager;
  8  import javax.persistence.NoResultException;
  9  import javax.persistence.OptimisticLockException;
 10  import javax.persistence.PersistenceContext;
 11  import javax.persistence.TypedQuery;
 12  import javax.ws.rs.Consumes;
 13  import javax.ws.rs.DELETE;
 14  import javax.ws.rs.GET;
 15  import javax.ws.rs.POST;
 16  import javax.ws.rs.PUT;
 17  import javax.ws.rs.Path;
 18  import javax.ws.rs.PathParam;
 19  import javax.ws.rs.Produces;
 20  import javax.ws.rs.QueryParam;
 21  import javax.ws.rs.core.Response;
 22  import javax.ws.rs.core.Response.Status;
 23  import javax.ws.rs.core.UriBuilder;
 24  import org.jboss.examples.ticketmonster.rest.dto.MediaItemDTO;
 25  import org.jboss.examples.ticketmonster.model.MediaItem;
 26  
 27  /**
 28   * 
 29   */
 30  @Stateless
 31  @Path("/mediaitems")
 32  public class MediaItemEndpoint
 33  {
 34     @PersistenceContext(unitName = "primary")
 35     private EntityManager em;
 36  
 37     @POST
 38     @Consumes("application/json")
 39     public Response create(MediaItemDTO dto)
 40     {
 41        MediaItem entity = dto.fromDTO(null, em);
 42        em.persist(entity);
 43        return Response.created(UriBuilder.fromResource(MediaItemEndpoint.class).path(String.valueOf(entity.getId())).build()).build();
 44     }
 45  
 46     @DELETE
 47     @Path("/{id:[0-9][0-9]*}")
 48     public Response deleteById(@PathParam("id") Long id)
 49     {
 50        MediaItem entity = em.find(MediaItem.class, id);
 51        if (entity == null)
 52        {
 53           return Response.status(Status.NOT_FOUND).build();
 54        }
 55        em.remove(entity);
 56        return Response.noContent().build();
 57     }
 58  
 59     @GET
 60     @Path("/{id:[0-9][0-9]*}")
 61     @Produces("application/json")
 62     public Response findById(@PathParam("id") Long id)
 63     {
 64        TypedQuery<MediaItem> findByIdQuery = em.createQuery("SELECT DISTINCT m FROM MediaItem m WHERE m.id = :entityId ORDER BY m.id", MediaItem.class);
 65        findByIdQuery.setParameter("entityId", id);
 66        MediaItem entity;
 67        try
 68        {
 69           entity = findByIdQuery.getSingleResult();
 70        }
 71        catch (NoResultException nre)
 72        {
 73           entity = null;
 74        }
 75        if (entity == null)
 76        {
 77           return Response.status(Status.NOT_FOUND).build();
 78        }
 79        MediaItemDTO dto = new MediaItemDTO(entity);
 80        return Response.ok(dto).build();
 81     }
 82  
 83     @GET
 84     @Produces("application/json")
 85     public List<MediaItemDTO> listAll(@QueryParam("start") Integer startPosition, @QueryParam("max") Integer maxResult)
 86     {
 87        TypedQuery<MediaItem> findAllQuery = em.createQuery("SELECT DISTINCT m FROM MediaItem m ORDER BY m.id", MediaItem.class);
 88        if (startPosition != null)
 89        {
 90           findAllQuery.setFirstResult(startPosition);
 91        }
 92        if (maxResult != null)
 93        {
 94           findAllQuery.setMaxResults(maxResult);
 95        }
 96        final List<MediaItem> searchResults = findAllQuery.getResultList();
 97        final List<MediaItemDTO> results = new ArrayList<MediaItemDTO>();
 98        for (MediaItem searchResult : searchResults)
 99        {
100           MediaItemDTO dto = new MediaItemDTO(searchResult);
101           results.add(dto);
102        }
103        return results;
104     }
105  
106     @PUT
107     @Path("/{id:[0-9][0-9]*}")
108     @Consumes("application/json")
109     public Response update(@PathParam("id") Long id, MediaItemDTO dto)
110     {
111        TypedQuery<MediaItem> findByIdQuery = em.createQuery("SELECT DISTINCT m FROM MediaItem m WHERE m.id = :entityId ORDER BY m.id", MediaItem.class);
112        findByIdQuery.setParameter("entityId", id);
113        MediaItem entity;
114        try
115        {
116           entity = findByIdQuery.getSingleResult();
117        }
118        catch (NoResultException nre)
119        {
120           entity = null;
121        }
122        entity = dto.fromDTO(entity, em);
123        try
124        {
125           entity = em.merge(entity);
126        }
127        catch (OptimisticLockException e)
128        {
129           return Response.status(Response.Status.CONFLICT).entity(e.getEntity()).build();
130        }
```
  * file:///tmp/source-code/backend-v1/src/main/java/org/jboss/examples/ticketmonster/rest/MetricsService.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import java.util.*;
  4  
  5  import javax.ejb.Stateless;
  6  import javax.inject.Inject;
  7  import javax.persistence.EntityManager;
  8  import javax.persistence.Query;
  9  import javax.persistence.TypedQuery;
 10  import javax.ws.rs.GET;
 11  import javax.ws.rs.Path;
 12  import javax.ws.rs.Produces;
 13  import javax.ws.rs.core.MediaType;
 14  
 15  import org.jboss.examples.ticketmonster.model.Show;
 16  
 17  /**
 18   * A read-only REST resource that provides a collection of metrics for shows occuring in the future. Updates to metrics via
 19   * POST/PUT etc. are not allowed, since they are not meant to be computed by consumers.
 20   * 
 21   * @author Vineet Reynolds
 22   * 
 23   */
 24  @Path("/metrics")
 25  @Stateless
 26  public class MetricsService {
 27  
 28      @Inject
 29      private EntityManager entityManager;
 30  
 31      /**
 32       * Retrieves a collection of metrics for Shows. Each metric in the collection contains
 33       * <ul>
 34       * <li>the show id,</li>
 35       * <li>the event name of the show,</li>
 36       * <li>the venue for the show,</li>
 37       * <li>the capacity for the venue</li>
 38       * <li>the performances for the show,
 39       * <ul>
 40       * <li>the timestamp for each performance,</li>
 41       * <li>the occupied count for each performance</li>
 42       * </ul>
 43       * </li>
 44       * </ul>
 45       * 
 46       * @return A JSON representation of metrics for shows.
 47       */
 48      @GET
 49      @Produces(MediaType.APPLICATION_JSON)
 50      public List<ShowMetric> getMetrics() {
 51          return retrieveMetricsFromShows(retrieveShows(),
 52              retrieveOccupiedCounts());
 53      }
 54  
 55      private List<ShowMetric> retrieveMetricsFromShows(List<Show> shows,
 56          Map<Long, Long> occupiedCounts) {
 57          List<ShowMetric> metrics = new ArrayList<ShowMetric>();
 58          for (Show show : shows) {
 59              metrics.add(new ShowMetric(show, occupiedCounts));
 60          }
 61          return metrics;
 62      }
 63  
 64      private List<Show> retrieveShows() {
 65          TypedQuery<Show> showQuery = entityManager
 66              .createQuery("select DISTINCT s from Show s JOIN s.performances p", Show.class);
 67          return showQuery.getResultList();
 68      }
 69  
 70      private Map<Long, Long> retrieveOccupiedCounts() {
 71          Map<Long, Long> occupiedCounts = new HashMap<Long, Long>();
 72  
 73          Query occupiedCountsQuery = entityManager
 74              .createQuery("select b.performance.id, SIZE(b.tickets) from Booking b "
 75                  + "GROUP BY b.performance.id");
 76  
 77          List<Object[]> results = occupiedCountsQuery.getResultList();
 78          for (Object[] result : results) {
 79              occupiedCounts.put((Long) result[0],
 80                  ((Integer) result[1]).longValue());
 81          }
 82  
 83          return occupiedCounts;
 84      }
 85  }

```
  * file:///tmp/source-code/backend-v1/src/main/java/org/jboss/examples/ticketmonster/rest/PerformanceEndpoint.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import java.util.ArrayList;
  4  import java.util.List;
  5  
  6  import javax.ejb.Stateless;
  7  import javax.persistence.EntityManager;
  8  import javax.persistence.NoResultException;
  9  import javax.persistence.OptimisticLockException;
 10  import javax.persistence.PersistenceContext;
 11  import javax.persistence.TypedQuery;
 12  import javax.persistence.criteria.CriteriaBuilder;
 13  import javax.persistence.criteria.CriteriaQuery;
 14  import javax.persistence.criteria.Predicate;
 15  import javax.persistence.criteria.Root;
 16  import javax.ws.rs.Consumes;
 17  import javax.ws.rs.DELETE;
 18  import javax.ws.rs.GET;
 19  import javax.ws.rs.POST;
 20  import javax.ws.rs.PUT;
 21  import javax.ws.rs.Path;
 22  import javax.ws.rs.PathParam;
 23  import javax.ws.rs.Produces;
 24  import javax.ws.rs.QueryParam;
 25  import javax.ws.rs.core.Response;
 26  import javax.ws.rs.core.Response.Status;
 27  import javax.ws.rs.core.UriBuilder;
 28  
 29  import org.jboss.examples.ticketmonster.rest.dto.PerformanceDTO;
 30  import org.jboss.examples.ticketmonster.model.Booking;
 31  import org.jboss.examples.ticketmonster.model.Performance;
 32  import org.jboss.examples.ticketmonster.model.SectionAllocation;
 33  import org.jboss.examples.ticketmonster.model.Show;
 34  
 35  /**
 36   * 
 37   */
 38  @Stateless
 39  @Path("/performances")
 40  public class PerformanceEndpoint
 41  {
 42     @PersistenceContext(unitName = "primary")
 43     private EntityManager em;
 44  
 45     @POST
 46     @Consumes("application/json")
 47     public Response create(PerformanceDTO dto)
 48     {
 49        Performance entity = dto.fromDTO(null, em);
 50        em.persist(entity);
 51        return Response.created(UriBuilder.fromResource(PerformanceEndpoint.class).path(String.valueOf(entity.getId())).build()).build();
 52     }
 53  
 54     @DELETE
 55     @Path("/{id:[0-9][0-9]*}")
 56     public Response deleteById(@PathParam("id") Long id)
 57     {
 58        Performance entity = em.find(Performance.class, id);
 59        if (entity == null)
 60        {
 61           return Response.status(Status.NOT_FOUND).build();
 62        }
 63        Show show = entity.getShow();
 64        show.getPerformances().remove(entity);
 65        entity.setShow(null);
 66        this.em.merge(show);
 67        List<SectionAllocation> sectionAllocations = findSectionAllocationsByPerformance(entity);
 68        for(SectionAllocation sectionAllocation: sectionAllocations) {
 69           this.em.remove(sectionAllocation);
 70        }
 71        List<Booking> bookings = findBookingsByPerformance(entity);
 72        for(Booking booking: bookings) {
 73           this.em.remove(booking);
 74        }
 75        em.remove(entity);
 76        return Response.noContent().build();
 77     }
 78  
 79     @GET
 80     @Path("/{id:[0-9][0-9]*}")
 81     @Produces("application/json")
 82     public Response findById(@PathParam("id") Long id)
 83     {
 84        TypedQuery<Performance> findByIdQuery = em.createQuery("SELECT DISTINCT p FROM Performance p LEFT JOIN FETCH p.show WHERE p.id = :entityId ORDER BY p.id", Performance.class);
 85        findByIdQuery.setParameter("entityId", id);
 86        Performance entity;
 87        try
 88        {
 89           entity = findByIdQuery.getSingleResult();
 90        }
 91        catch (NoResultException nre)
 92        {
 93           entity = null;
 94        }
 95        if (entity == null)
 96        {
 97           return Response.status(Status.NOT_FOUND).build();
 98        }
 99        PerformanceDTO dto = new PerformanceDTO(entity);
100        return Response.ok(dto).build();
101     }
102  
103     @GET
104     @Produces("application/json")
105     public List<PerformanceDTO> listAll(@QueryParam("start") Integer startPosition, @QueryParam("max") Integer maxResult)
106     {
107        TypedQuery<Performance> findAllQuery = em.createQuery("SELECT DISTINCT p FROM Performance p LEFT JOIN FETCH p.show ORDER BY p.id", Performance.class);
108        if (startPosition != null)
109        {
110           findAllQuery.setFirstResult(startPosition);
111        }
112        if (maxResult != null)
113        {
114           findAllQuery.setMaxResults(maxResult);
115        }
116        final List<Performance> searchResults = findAllQuery.getResultList();
117        final List<PerformanceDTO> results = new ArrayList<PerformanceDTO>();
118        for (Performance searchResult : searchResults)
119        {
120           PerformanceDTO dto = new PerformanceDTO(searchResult);
121           results.add(dto);
122        }
123        return results;
124     }
125  
126     @PUT
127     @Path("/{id:[0-9][0-9]*}")
128     @Consumes("application/json")
129     public Response update(@PathParam("id") Long id, PerformanceDTO dto)
130     {
131        TypedQuery<Performance> findByIdQuery = em.createQuery("SELECT DISTINCT p FROM Performance p LEFT JOIN FETCH p.show WHERE p.id = :entityId ORDER BY p.id", Performance.class);
132        findByIdQuery.setParameter("entityId", id);
133        Performance entity;
134        try
135        {
136           entity = findByIdQuery.getSingleResult();
137        }
138        catch (NoResultException nre)
```
  * file:///tmp/source-code/backend-v1/src/main/java/org/jboss/examples/ticketmonster/rest/PingService.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  /**
  2   * Licensed to the Apache Software Foundation (ASF) under one or more
  3   * contributor license agreements.  See the NOTICE file distributed with
  4   * this work for additional information regarding copyright ownership.
  5   * The ASF licenses this file to You under the Apache License, Version 2.0
  6   * (the "License"); you may not use this file except in compliance with
  7   * the License.  You may obtain a copy of the License at
  8   * <p>
  9   * http://www.apache.org/licenses/LICENSE-2.0
 10   * <p>
 11   * Unless required by applicable law or agreed to in writing, software
 12   * distributed under the License is distributed on an "AS IS" BASIS,
 13   * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 14   * See the License for the specific language governing permissions and
 15   * limitations under the License.
 16   */
 17  package org.jboss.examples.ticketmonster.rest;
 18  
 19  import javax.ejb.Stateless;
 20  import javax.ws.rs.GET;
 21  import javax.ws.rs.Path;
 22  
 23  /**
 24   * Created by ceposta 
 25   * <a href="http://christianposta.com/blog>http://christianposta.com/blog</a>.
 26   */
 27  @Path("/ping")
 28  @Stateless
 29  public class PingService {
 30  
 31      @GET
 32      public String ping(){
 33          return "pong";
 34      }
 35  }

```
  * file:///tmp/source-code/backend-v1/src/main/java/org/jboss/examples/ticketmonster/rest/SectionAllocationEndpoint.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import java.util.ArrayList;
  4  import java.util.List;
  5  
  6  import javax.ejb.Stateless;
  7  import javax.persistence.EntityManager;
  8  import javax.persistence.NoResultException;
  9  import javax.persistence.OptimisticLockException;
 10  import javax.persistence.PersistenceContext;
 11  import javax.persistence.TypedQuery;
 12  import javax.ws.rs.Consumes;
 13  import javax.ws.rs.DELETE;
 14  import javax.ws.rs.GET;
 15  import javax.ws.rs.POST;
 16  import javax.ws.rs.PUT;
 17  import javax.ws.rs.Path;
 18  import javax.ws.rs.PathParam;
 19  import javax.ws.rs.Produces;
 20  import javax.ws.rs.QueryParam;
 21  import javax.ws.rs.core.Response;
 22  import javax.ws.rs.core.Response.Status;
 23  import javax.ws.rs.core.UriBuilder;
 24  import org.jboss.examples.ticketmonster.rest.dto.SectionAllocationDTO;
 25  import org.jboss.examples.ticketmonster.model.SectionAllocation;
 26  
 27  /**
 28   * 
 29   */
 30  @Stateless
 31  @Path("/sectionallocations")
 32  public class SectionAllocationEndpoint
 33  {
 34     @PersistenceContext(unitName = "primary")
 35     private EntityManager em;
 36  
 37     @POST
 38     @Consumes("application/json")
 39     public Response create(SectionAllocationDTO dto)
 40     {
 41        SectionAllocation entity = dto.fromDTO(null, em);
 42        em.persist(entity);
 43        return Response.created(UriBuilder.fromResource(SectionAllocationEndpoint.class).path(String.valueOf(entity.getId())).build()).build();
 44     }
 45  
 46     @DELETE
 47     @Path("/{id:[0-9][0-9]*}")
 48     public Response deleteById(@PathParam("id") Long id)
 49     {
 50        SectionAllocation entity = em.find(SectionAllocation.class, id);
 51        if (entity == null)
 52        {
 53           return Response.status(Status.NOT_FOUND).build();
 54        }
 55        em.remove(entity);
 56        return Response.noContent().build();
 57     }
 58  
 59     @GET
 60     @Path("/{id:[0-9][0-9]*}")
 61     @Produces("application/json")
 62     public Response findById(@PathParam("id") Long id)
 63     {
 64        TypedQuery<SectionAllocation> findByIdQuery = em.createQuery("SELECT DISTINCT s FROM SectionAllocation s LEFT JOIN FETCH s.performance LEFT JOIN FETCH s.section WHERE s.id = :entityId ORDER BY s.id", SectionAllocation.class);
 65        findByIdQuery.setParameter("entityId", id);
 66        SectionAllocation entity;
 67        try
 68        {
 69           entity = findByIdQuery.getSingleResult();
 70        }
 71        catch (NoResultException nre)
 72        {
 73           entity = null;
 74        }
 75        if (entity == null)
 76        {
 77           return Response.status(Status.NOT_FOUND).build();
 78        }
 79        SectionAllocationDTO dto = new SectionAllocationDTO(entity);
 80        return Response.ok(dto).build();
 81     }
 82  
 83     @GET
 84     @Produces("application/json")
 85     public List<SectionAllocationDTO> listAll(@QueryParam("start") Integer startPosition, @QueryParam("max") Integer maxResult)
 86     {
 87        TypedQuery<SectionAllocation> findAllQuery = em.createQuery("SELECT DISTINCT s FROM SectionAllocation s LEFT JOIN FETCH s.performance LEFT JOIN FETCH s.section ORDER BY s.id", SectionAllocation.class);
 88        if (startPosition != null)
 89        {
 90           findAllQuery.setFirstResult(startPosition);
 91        }
 92        if (maxResult != null)
 93        {
 94           findAllQuery.setMaxResults(maxResult);
 95        }
 96        final List<SectionAllocation> searchResults = findAllQuery.getResultList();
 97        final List<SectionAllocationDTO> results = new ArrayList<SectionAllocationDTO>();
 98        for (SectionAllocation searchResult : searchResults)
 99        {
100           SectionAllocationDTO dto = new SectionAllocationDTO(searchResult);
101           results.add(dto);
102        }
103        return results;
104     }
105  
106     @PUT
107     @Path("/{id:[0-9][0-9]*}")
108     @Consumes("application/json")
109     public Response update(@PathParam("id") Long id, SectionAllocationDTO dto)
110     {
111        TypedQuery<SectionAllocation> findByIdQuery = em.createQuery("SELECT DISTINCT s FROM SectionAllocation s LEFT JOIN FETCH s.performance LEFT JOIN FETCH s.section WHERE s.id = :entityId ORDER BY s.id", SectionAllocation.class);
112        findByIdQuery.setParameter("entityId", id);
113        SectionAllocation entity;
114        try
115        {
116           entity = findByIdQuery.getSingleResult();
117        }
118        catch (NoResultException nre)
119        {
120           entity = null;
121        }
122        entity = dto.fromDTO(entity, em);
123        try
124        {
125           entity = em.merge(entity);
126        }
127        catch (OptimisticLockException e)
128        {
129           return Response.status(Response.Status.CONFLICT).entity(e.getEntity()).build();
130        }
```
  * file:///tmp/source-code/backend-v1/src/main/java/org/jboss/examples/ticketmonster/rest/SectionEndpoint.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import java.util.ArrayList;
  4  import java.util.List;
  5  
  6  import javax.ejb.Stateless;
  7  import javax.persistence.EntityManager;
  8  import javax.persistence.NoResultException;
  9  import javax.persistence.OptimisticLockException;
 10  import javax.persistence.PersistenceContext;
 11  import javax.persistence.TypedQuery;
 12  import javax.ws.rs.Consumes;
 13  import javax.ws.rs.DELETE;
 14  import javax.ws.rs.GET;
 15  import javax.ws.rs.POST;
 16  import javax.ws.rs.PUT;
 17  import javax.ws.rs.Path;
 18  import javax.ws.rs.PathParam;
 19  import javax.ws.rs.Produces;
 20  import javax.ws.rs.QueryParam;
 21  import javax.ws.rs.core.Response;
 22  import javax.ws.rs.core.Response.Status;
 23  import javax.ws.rs.core.UriBuilder;
 24  import org.jboss.examples.ticketmonster.rest.dto.SectionDTO;
 25  import org.jboss.examples.ticketmonster.model.Section;
 26  
 27  /**
 28   * 
 29   */
 30  @Stateless
 31  @Path("/sections")
 32  public class SectionEndpoint
 33  {
 34     @PersistenceContext(unitName = "primary")
 35     private EntityManager em;
 36  
 37     @POST
 38     @Consumes("application/json")
 39     public Response create(SectionDTO dto)
 40     {
 41        Section entity = dto.fromDTO(null, em);
 42        em.persist(entity);
 43        return Response.created(UriBuilder.fromResource(SectionEndpoint.class).path(String.valueOf(entity.getId())).build()).build();
 44     }
 45  
 46     @DELETE
 47     @Path("/{id:[0-9][0-9]*}")
 48     public Response deleteById(@PathParam("id") Long id)
 49     {
 50        Section entity = em.find(Section.class, id);
 51        if (entity == null)
 52        {
 53           return Response.status(Status.NOT_FOUND).build();
 54        }
 55        em.remove(entity);
 56        return Response.noContent().build();
 57     }
 58  
 59     @GET
 60     @Path("/{id:[0-9][0-9]*}")
 61     @Produces("application/json")
 62     public Response findById(@PathParam("id") Long id)
 63     {
 64        TypedQuery<Section> findByIdQuery = em.createQuery("SELECT DISTINCT s FROM Section s LEFT JOIN FETCH s.venue WHERE s.id = :entityId ORDER BY s.id", Section.class);
 65        findByIdQuery.setParameter("entityId", id);
 66        Section entity;
 67        try
 68        {
 69           entity = findByIdQuery.getSingleResult();
 70        }
 71        catch (NoResultException nre)
 72        {
 73           entity = null;
 74        }
 75        if (entity == null)
 76        {
 77           return Response.status(Status.NOT_FOUND).build();
 78        }
 79        SectionDTO dto = new SectionDTO(entity);
 80        return Response.ok(dto).build();
 81     }
 82  
 83     @GET
 84     @Produces("application/json")
 85     public List<SectionDTO> listAll(@QueryParam("start") Integer startPosition, @QueryParam("max") Integer maxResult)
 86     {
 87        TypedQuery<Section> findAllQuery = em.createQuery("SELECT DISTINCT s FROM Section s LEFT JOIN FETCH s.venue ORDER BY s.id", Section.class);
 88        if (startPosition != null)
 89        {
 90           findAllQuery.setFirstResult(startPosition);
 91        }
 92        if (maxResult != null)
 93        {
 94           findAllQuery.setMaxResults(maxResult);
 95        }
 96        final List<Section> searchResults = findAllQuery.getResultList();
 97        final List<SectionDTO> results = new ArrayList<SectionDTO>();
 98        for (Section searchResult : searchResults)
 99        {
100           SectionDTO dto = new SectionDTO(searchResult);
101           results.add(dto);
102        }
103        return results;
104     }
105  
106     @PUT
107     @Path("/{id:[0-9][0-9]*}")
108     @Consumes("application/json")
109     public Response update(@PathParam("id") Long id, SectionDTO dto)
110     {
111        TypedQuery<Section> findByIdQuery = em.createQuery("SELECT DISTINCT s FROM Section s LEFT JOIN FETCH s.venue WHERE s.id = :entityId ORDER BY s.id", Section.class);
112        findByIdQuery.setParameter("entityId", id);
113        Section entity;
114        try
115        {
116           entity = findByIdQuery.getSingleResult();
117        }
118        catch (NoResultException nre)
119        {
120           entity = null;
121        }
122        entity = dto.fromDTO(entity, em);
123        try
124        {
125           entity = em.merge(entity);
126        }
127        catch (OptimisticLockException e)
128        {
129           return Response.status(Response.Status.CONFLICT).entity(e.getEntity()).build();
130        }
```
  * file:///tmp/source-code/backend-v1/src/main/java/org/jboss/examples/ticketmonster/rest/ShowEndpoint.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import java.util.ArrayList;
  4  import java.util.List;
  5  
  6  import javax.ejb.Stateless;
  7  import javax.persistence.EntityManager;
  8  import javax.persistence.NoResultException;
  9  import javax.persistence.OptimisticLockException;
 10  import javax.persistence.PersistenceContext;
 11  import javax.persistence.TypedQuery;
 12  import javax.ws.rs.Consumes;
 13  import javax.ws.rs.DELETE;
 14  import javax.ws.rs.GET;
 15  import javax.ws.rs.POST;
 16  import javax.ws.rs.PUT;
 17  import javax.ws.rs.Path;
 18  import javax.ws.rs.PathParam;
 19  import javax.ws.rs.Produces;
 20  import javax.ws.rs.QueryParam;
 21  import javax.ws.rs.core.Response;
 22  import javax.ws.rs.core.Response.Status;
 23  import javax.ws.rs.core.UriBuilder;
 24  import org.jboss.examples.ticketmonster.rest.dto.ShowDTO;
 25  import org.jboss.examples.ticketmonster.model.Show;
 26  
 27  /**
 28   * 
 29   */
 30  @Stateless
 31  @Path("forge/shows")
 32  public class ShowEndpoint
 33  {
 34     @PersistenceContext(unitName = "primary")
 35     private EntityManager em;
 36  
 37     @POST
 38     @Consumes("application/json")
 39     public Response create(ShowDTO dto)
 40     {
 41        Show entity = dto.fromDTO(null, em);
 42        em.persist(entity);
 43        return Response.created(UriBuilder.fromResource(ShowEndpoint.class).path(String.valueOf(entity.getId())).build()).build();
 44     }
 45  
 46     @DELETE
 47     @Path("/{id:[0-9][0-9]*}")
 48     public Response deleteById(@PathParam("id") Long id)
 49     {
 50        Show entity = em.find(Show.class, id);
 51        if (entity == null)
 52        {
 53           return Response.status(Status.NOT_FOUND).build();
 54        }
 55        em.remove(entity);
 56        return Response.noContent().build();
 57     }
 58  
 59     @GET
 60     @Path("/{id:[0-9][0-9]*}")
 61     @Produces("application/json")
 62     public Response findById(@PathParam("id") Long id)
 63     {
 64        TypedQuery<Show> findByIdQuery = em.createQuery("SELECT DISTINCT s FROM Show s LEFT JOIN FETCH s.event LEFT JOIN FETCH s.venue LEFT JOIN FETCH s.performances LEFT JOIN FETCH s.ticketPrices WHERE s.id = :entityId ORDER BY s.id", Show.class);
 65        findByIdQuery.setParameter("entityId", id);
 66        Show entity;
 67        try
 68        {
 69           entity = findByIdQuery.getSingleResult();
 70        }
 71        catch (NoResultException nre)
 72        {
 73           entity = null;
 74        }
 75        if (entity == null)
 76        {
 77           return Response.status(Status.NOT_FOUND).build();
 78        }
 79        ShowDTO dto = new ShowDTO(entity);
 80        return Response.ok(dto).build();
 81     }
 82  
 83     @GET
 84     @Produces("application/json")
 85     public List<ShowDTO> listAll(@QueryParam("start") Integer startPosition, @QueryParam("max") Integer maxResult)
 86     {
 87        TypedQuery<Show> findAllQuery = em.createQuery("SELECT DISTINCT s FROM Show s LEFT JOIN FETCH s.event LEFT JOIN FETCH s.venue LEFT JOIN FETCH s.performances LEFT JOIN FETCH s.ticketPrices ORDER BY s.id", Show.class);
 88        if (startPosition != null)
 89        {
 90           findAllQuery.setFirstResult(startPosition);
 91        }
 92        if (maxResult != null)
 93        {
 94           findAllQuery.setMaxResults(maxResult);
 95        }
 96        final List<Show> searchResults = findAllQuery.getResultList();
 97        final List<ShowDTO> results = new ArrayList<ShowDTO>();
 98        for (Show searchResult : searchResults)
 99        {
100           ShowDTO dto = new ShowDTO(searchResult);
101           results.add(dto);
102        }
103        return results;
104     }
105  
106     @PUT
107     @Path("/{id:[0-9][0-9]*}")
108     @Consumes("application/json")
109     public Response update(@PathParam("id") Long id, ShowDTO dto)
110     {
111        TypedQuery<Show> findByIdQuery = em.createQuery("SELECT DISTINCT s FROM Show s LEFT JOIN FETCH s.event LEFT JOIN FETCH s.venue LEFT JOIN FETCH s.performances LEFT JOIN FETCH s.ticketPrices WHERE s.id = :entityId ORDER BY s.id", Show.class);
112        findByIdQuery.setParameter("entityId", id);
113        Show entity;
114        try
115        {
116           entity = findByIdQuery.getSingleResult();
117        }
118        catch (NoResultException nre)
119        {
120           entity = null;
121        }
122        entity = dto.fromDTO(entity, em);
123        try
124        {
125           entity = em.merge(entity);
126        }
127        catch (OptimisticLockException e)
128        {
129           return Response.status(Response.Status.CONFLICT).entity(e.getEntity()).build();
130        }
```
  * file:///tmp/source-code/backend-v1/src/main/java/org/jboss/examples/ticketmonster/rest/ShowService.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import java.util.ArrayList;
  4  import java.util.List;
  5  
  6  import javax.ejb.Stateless;
  7  import javax.persistence.Query;
  8  import javax.persistence.criteria.CriteriaBuilder;
  9  import javax.persistence.criteria.Predicate;
 10  import javax.persistence.criteria.Root;
 11  import javax.ws.rs.GET;
 12  import javax.ws.rs.Path;
 13  import javax.ws.rs.PathParam;
 14  import javax.ws.rs.Produces;
 15  import javax.ws.rs.core.MediaType;
 16  import javax.ws.rs.core.MultivaluedMap;
 17  
 18  import org.jboss.examples.ticketmonster.model.Show;
 19  
 20  /**
 21   * @author Marius Bogoevici
 22   */
 23  @Path("/shows")
 24  /**
 25   * <p>
 26   *     This is a stateless service, we declare it as an EJB for transaction demarcation
 27   * </p>
 28   */
 29  @Stateless
 30  public class ShowService extends BaseEntityService<Show> {
 31  
 32      public ShowService() {
 33          super(Show.class);
 34      }
 35  
 36      @Override
 37      protected Predicate[] extractPredicates(MultivaluedMap<String,
 38              String> queryParameters,
 39              CriteriaBuilder criteriaBuilder,
 40              Root<Show> root) {
 41  
 42          List<Predicate> predicates = new ArrayList<Predicate>();
 43  
 44          if (queryParameters.containsKey("venue")) {
 45              String venue = queryParameters.getFirst("venue");
 46              predicates.add(criteriaBuilder.equal(root.get("venue").get("id"), venue));
 47          }
 48  
 49          if (queryParameters.containsKey("event")) {
 50              String event = queryParameters.getFirst("event");
 51              predicates.add(criteriaBuilder.equal(root.get("event").get("id"), event));
 52          }
 53          return predicates.toArray(new Predicate[]{});
 54      }
 55  
 56      @GET
 57      @Path("/performance/{performanceId:[0-9][0-9]*}")
 58      @Produces(MediaType.APPLICATION_JSON)
 59      public Show getShowByPerformance(@PathParam("performanceId") Long performanceId) {
 60          Query query = getEntityManager().createQuery("select s from Show s where exists(select p from Performance p where p.show = s and p.id = :performanceId)");
 61          query.setParameter("performanceId", performanceId);
 62          return (Show) query.getSingleResult();
 63      }
 64  }

```
  * file:///tmp/source-code/backend-v1/src/main/java/org/jboss/examples/ticketmonster/rest/TicketCategoryEndpoint.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import java.util.ArrayList;
  4  import java.util.List;
  5  
  6  import javax.ejb.Stateless;
  7  import javax.persistence.EntityManager;
  8  import javax.persistence.NoResultException;
  9  import javax.persistence.OptimisticLockException;
 10  import javax.persistence.PersistenceContext;
 11  import javax.persistence.TypedQuery;
 12  import javax.ws.rs.Consumes;
 13  import javax.ws.rs.DELETE;
 14  import javax.ws.rs.GET;
 15  import javax.ws.rs.POST;
 16  import javax.ws.rs.PUT;
 17  import javax.ws.rs.Path;
 18  import javax.ws.rs.PathParam;
 19  import javax.ws.rs.Produces;
 20  import javax.ws.rs.QueryParam;
 21  import javax.ws.rs.core.Response;
 22  import javax.ws.rs.core.Response.Status;
 23  import javax.ws.rs.core.UriBuilder;
 24  import org.jboss.examples.ticketmonster.rest.dto.TicketCategoryDTO;
 25  import org.jboss.examples.ticketmonster.model.TicketCategory;
 26  
 27  /**
 28   * 
 29   */
 30  @Stateless
 31  @Path("/ticketcategories")
 32  public class TicketCategoryEndpoint
 33  {
 34     @PersistenceContext(unitName = "primary")
 35     private EntityManager em;
 36  
 37     @POST
 38     @Consumes("application/json")
 39     public Response create(TicketCategoryDTO dto)
 40     {
 41        TicketCategory entity = dto.fromDTO(null, em);
 42        em.persist(entity);
 43        return Response.created(UriBuilder.fromResource(TicketCategoryEndpoint.class).path(String.valueOf(entity.getId())).build()).build();
 44     }
 45  
 46     @DELETE
 47     @Path("/{id:[0-9][0-9]*}")
 48     public Response deleteById(@PathParam("id") Long id)
 49     {
 50        TicketCategory entity = em.find(TicketCategory.class, id);
 51        if (entity == null)
 52        {
 53           return Response.status(Status.NOT_FOUND).build();
 54        }
 55        em.remove(entity);
 56        return Response.noContent().build();
 57     }
 58  
 59     @GET
 60     @Path("/{id:[0-9][0-9]*}")
 61     @Produces("application/json")
 62     public Response findById(@PathParam("id") Long id)
 63     {
 64        TypedQuery<TicketCategory> findByIdQuery = em.createQuery("SELECT DISTINCT t FROM TicketCategory t WHERE t.id = :entityId ORDER BY t.id", TicketCategory.class);
 65        findByIdQuery.setParameter("entityId", id);
 66        TicketCategory entity;
 67        try
 68        {
 69           entity = findByIdQuery.getSingleResult();
 70        }
 71        catch (NoResultException nre)
 72        {
 73           entity = null;
 74        }
 75        if (entity == null)
 76        {
 77           return Response.status(Status.NOT_FOUND).build();
 78        }
 79        TicketCategoryDTO dto = new TicketCategoryDTO(entity);
 80        return Response.ok(dto).build();
 81     }
 82  
 83     @GET
 84     @Produces("application/json")
 85     public List<TicketCategoryDTO> listAll(@QueryParam("start") Integer startPosition, @QueryParam("max") Integer maxResult)
 86     {
 87        TypedQuery<TicketCategory> findAllQuery = em.createQuery("SELECT DISTINCT t FROM TicketCategory t ORDER BY t.id", TicketCategory.class);
 88        if (startPosition != null)
 89        {
 90           findAllQuery.setFirstResult(startPosition);
 91        }
 92        if (maxResult != null)
 93        {
 94           findAllQuery.setMaxResults(maxResult);
 95        }
 96        final List<TicketCategory> searchResults = findAllQuery.getResultList();
 97        final List<TicketCategoryDTO> results = new ArrayList<TicketCategoryDTO>();
 98        for (TicketCategory searchResult : searchResults)
 99        {
100           TicketCategoryDTO dto = new TicketCategoryDTO(searchResult);
101           results.add(dto);
102        }
103        return results;
104     }
105  
106     @PUT
107     @Path("/{id:[0-9][0-9]*}")
108     @Consumes("application/json")
109     public Response update(@PathParam("id") Long id, TicketCategoryDTO dto)
110     {
111        TypedQuery<TicketCategory> findByIdQuery = em.createQuery("SELECT DISTINCT t FROM TicketCategory t WHERE t.id = :entityId ORDER BY t.id", TicketCategory.class);
112        findByIdQuery.setParameter("entityId", id);
113        TicketCategory entity;
114        try
115        {
116           entity = findByIdQuery.getSingleResult();
117        }
118        catch (NoResultException nre)
119        {
120           entity = null;
121        }
122        entity = dto.fromDTO(entity, em);
123        try
124        {
125           entity = em.merge(entity);
126        }
127        catch (OptimisticLockException e)
128        {
129           return Response.status(Response.Status.CONFLICT).entity(e.getEntity()).build();
130        }
```
  * file:///tmp/source-code/backend-v1/src/main/java/org/jboss/examples/ticketmonster/rest/TicketEndpoint.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import java.util.ArrayList;
  4  import java.util.List;
  5  
  6  import javax.ejb.Stateless;
  7  import javax.persistence.EntityManager;
  8  import javax.persistence.NoResultException;
  9  import javax.persistence.OptimisticLockException;
 10  import javax.persistence.PersistenceContext;
 11  import javax.persistence.TypedQuery;
 12  import javax.ws.rs.Consumes;
 13  import javax.ws.rs.DELETE;
 14  import javax.ws.rs.GET;
 15  import javax.ws.rs.POST;
 16  import javax.ws.rs.PUT;
 17  import javax.ws.rs.Path;
 18  import javax.ws.rs.PathParam;
 19  import javax.ws.rs.Produces;
 20  import javax.ws.rs.QueryParam;
 21  import javax.ws.rs.core.Response;
 22  import javax.ws.rs.core.Response.Status;
 23  import javax.ws.rs.core.UriBuilder;
 24  import org.jboss.examples.ticketmonster.rest.dto.TicketDTO;
 25  import org.jboss.examples.ticketmonster.model.Ticket;
 26  
 27  /**
 28   * 
 29   */
 30  @Stateless
 31  @Path("/tickets")
 32  public class TicketEndpoint
 33  {
 34     @PersistenceContext(unitName = "primary")
 35     private EntityManager em;
 36  
 37     @POST
 38     @Consumes("application/json")
 39     public Response create(TicketDTO dto)
 40     {
 41        Ticket entity = dto.fromDTO(null, em);
 42        em.persist(entity);
 43        return Response.created(UriBuilder.fromResource(TicketEndpoint.class).path(String.valueOf(entity.getId())).build()).build();
 44     }
 45  
 46     @DELETE
 47     @Path("/{id:[0-9][0-9]*}")
 48     public Response deleteById(@PathParam("id") Long id)
 49     {
 50        Ticket entity = em.find(Ticket.class, id);
 51        if (entity == null)
 52        {
 53           return Response.status(Status.NOT_FOUND).build();
 54        }
 55        em.remove(entity);
 56        return Response.noContent().build();
 57     }
 58  
 59     @GET
 60     @Path("/{id:[0-9][0-9]*}")
 61     @Produces("application/json")
 62     public Response findById(@PathParam("id") Long id)
 63     {
 64        TypedQuery<Ticket> findByIdQuery = em.createQuery("SELECT DISTINCT t FROM Ticket t LEFT JOIN FETCH t.ticketCategory WHERE t.id = :entityId ORDER BY t.id", Ticket.class);
 65        findByIdQuery.setParameter("entityId", id);
 66        Ticket entity;
 67        try
 68        {
 69           entity = findByIdQuery.getSingleResult();
 70        }
 71        catch (NoResultException nre)
 72        {
 73           entity = null;
 74        }
 75        if (entity == null)
 76        {
 77           return Response.status(Status.NOT_FOUND).build();
 78        }
 79        TicketDTO dto = new TicketDTO(entity);
 80        return Response.ok(dto).build();
 81     }
 82  
 83     @GET
 84     @Produces("application/json")
 85     public List<TicketDTO> listAll(@QueryParam("start") Integer startPosition, @QueryParam("max") Integer maxResult)
 86     {
 87        TypedQuery<Ticket> findAllQuery = em.createQuery("SELECT DISTINCT t FROM Ticket t LEFT JOIN FETCH t.ticketCategory ORDER BY t.id", Ticket.class);
 88        if (startPosition != null)
 89        {
 90           findAllQuery.setFirstResult(startPosition);
 91        }
 92        if (maxResult != null)
 93        {
 94           findAllQuery.setMaxResults(maxResult);
 95        }
 96        final List<Ticket> searchResults = findAllQuery.getResultList();
 97        final List<TicketDTO> results = new ArrayList<TicketDTO>();
 98        for (Ticket searchResult : searchResults)
 99        {
100           TicketDTO dto = new TicketDTO(searchResult);
101           results.add(dto);
102        }
103        return results;
104     }
105  
106     @PUT
107     @Path("/{id:[0-9][0-9]*}")
108     @Consumes("application/json")
109     public Response update(@PathParam("id") Long id, TicketDTO dto)
110     {
111        TypedQuery<Ticket> findByIdQuery = em.createQuery("SELECT DISTINCT t FROM Ticket t LEFT JOIN FETCH t.ticketCategory WHERE t.id = :entityId ORDER BY t.id", Ticket.class);
112        findByIdQuery.setParameter("entityId", id);
113        Ticket entity;
114        try
115        {
116           entity = findByIdQuery.getSingleResult();
117        }
118        catch (NoResultException nre)
119        {
120           entity = null;
121        }
122        entity = dto.fromDTO(entity, em);
123        try
124        {
125           entity = em.merge(entity);
126        }
127        catch (OptimisticLockException e)
128        {
129           return Response.status(Response.Status.CONFLICT).entity(e.getEntity()).build();
130        }
```
  * file:///tmp/source-code/backend-v1/src/main/java/org/jboss/examples/ticketmonster/rest/TicketPriceEndpoint.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import java.util.ArrayList;
  4  import java.util.List;
  5  
  6  import javax.ejb.Stateless;
  7  import javax.persistence.EntityManager;
  8  import javax.persistence.NoResultException;
  9  import javax.persistence.OptimisticLockException;
 10  import javax.persistence.PersistenceContext;
 11  import javax.persistence.TypedQuery;
 12  import javax.ws.rs.Consumes;
 13  import javax.ws.rs.DELETE;
 14  import javax.ws.rs.GET;
 15  import javax.ws.rs.POST;
 16  import javax.ws.rs.PUT;
 17  import javax.ws.rs.Path;
 18  import javax.ws.rs.PathParam;
 19  import javax.ws.rs.Produces;
 20  import javax.ws.rs.QueryParam;
 21  import javax.ws.rs.core.Response;
 22  import javax.ws.rs.core.Response.Status;
 23  import javax.ws.rs.core.UriBuilder;
 24  import org.jboss.examples.ticketmonster.rest.dto.TicketPriceDTO;
 25  import org.jboss.examples.ticketmonster.model.TicketPrice;
 26  
 27  /**
 28   * 
 29   */
 30  @Stateless
 31  @Path("/ticketprices")
 32  public class TicketPriceEndpoint
 33  {
 34     @PersistenceContext(unitName = "primary")
 35     private EntityManager em;
 36  
 37     @POST
 38     @Consumes("application/json")
 39     public Response create(TicketPriceDTO dto)
 40     {
 41        TicketPrice entity = dto.fromDTO(null, em);
 42        em.persist(entity);
 43        return Response.created(UriBuilder.fromResource(TicketPriceEndpoint.class).path(String.valueOf(entity.getId())).build()).build();
 44     }
 45  
 46     @DELETE
 47     @Path("/{id:[0-9][0-9]*}")
 48     public Response deleteById(@PathParam("id") Long id)
 49     {
 50        TicketPrice entity = em.find(TicketPrice.class, id);
 51        if (entity == null)
 52        {
 53           return Response.status(Status.NOT_FOUND).build();
 54        }
 55        em.remove(entity);
 56        return Response.noContent().build();
 57     }
 58  
 59     @GET
 60     @Path("/{id:[0-9][0-9]*}")
 61     @Produces("application/json")
 62     public Response findById(@PathParam("id") Long id)
 63     {
 64        TypedQuery<TicketPrice> findByIdQuery = em.createQuery("SELECT DISTINCT t FROM TicketPrice t LEFT JOIN FETCH t.show LEFT JOIN FETCH t.section LEFT JOIN FETCH t.ticketCategory WHERE t.id = :entityId ORDER BY t.id", TicketPrice.class);
 65        findByIdQuery.setParameter("entityId", id);
 66        TicketPrice entity;
 67        try
 68        {
 69           entity = findByIdQuery.getSingleResult();
 70        }
 71        catch (NoResultException nre)
 72        {
 73           entity = null;
 74        }
 75        if (entity == null)
 76        {
 77           return Response.status(Status.NOT_FOUND).build();
 78        }
 79        TicketPriceDTO dto = new TicketPriceDTO(entity);
 80        return Response.ok(dto).build();
 81     }
 82  
 83     @GET
 84     @Produces("application/json")
 85     public List<TicketPriceDTO> listAll(@QueryParam("start") Integer startPosition, @QueryParam("max") Integer maxResult)
 86     {
 87        TypedQuery<TicketPrice> findAllQuery = em.createQuery("SELECT DISTINCT t FROM TicketPrice t LEFT JOIN FETCH t.show LEFT JOIN FETCH t.section LEFT JOIN FETCH t.ticketCategory ORDER BY t.id", TicketPrice.class);
 88        if (startPosition != null)
 89        {
 90           findAllQuery.setFirstResult(startPosition);
 91        }
 92        if (maxResult != null)
 93        {
 94           findAllQuery.setMaxResults(maxResult);
 95        }
 96        final List<TicketPrice> searchResults = findAllQuery.getResultList();
 97        final List<TicketPriceDTO> results = new ArrayList<TicketPriceDTO>();
 98        for (TicketPrice searchResult : searchResults)
 99        {
100           TicketPriceDTO dto = new TicketPriceDTO(searchResult);
101           results.add(dto);
102        }
103        return results;
104     }
105  
106     @PUT
107     @Path("/{id:[0-9][0-9]*}")
108     @Consumes("application/json")
109     public Response update(@PathParam("id") Long id, TicketPriceDTO dto)
110     {
111        TypedQuery<TicketPrice> findByIdQuery = em.createQuery("SELECT DISTINCT t FROM TicketPrice t LEFT JOIN FETCH t.show LEFT JOIN FETCH t.section LEFT JOIN FETCH t.ticketCategory WHERE t.id = :entityId ORDER BY t.id", TicketPrice.class);
112        findByIdQuery.setParameter("entityId", id);
113        TicketPrice entity;
114        try
115        {
116           entity = findByIdQuery.getSingleResult();
117        }
118        catch (NoResultException nre)
119        {
120           entity = null;
121        }
122        entity = dto.fromDTO(entity, em);
123        try
124        {
125           entity = em.merge(entity);
126        }
127        catch (OptimisticLockException e)
128        {
129           return Response.status(Response.Status.CONFLICT).entity(e.getEntity()).build();
130        }
```
  * file:///tmp/source-code/backend-v1/src/main/java/org/jboss/examples/ticketmonster/rest/VenueEndpoint.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import java.util.ArrayList;
  4  import java.util.List;
  5  
  6  import javax.ejb.Stateless;
  7  import javax.persistence.EntityManager;
  8  import javax.persistence.NoResultException;
  9  import javax.persistence.OptimisticLockException;
 10  import javax.persistence.PersistenceContext;
 11  import javax.persistence.TypedQuery;
 12  import javax.ws.rs.Consumes;
 13  import javax.ws.rs.DELETE;
 14  import javax.ws.rs.GET;
 15  import javax.ws.rs.POST;
 16  import javax.ws.rs.PUT;
 17  import javax.ws.rs.Path;
 18  import javax.ws.rs.PathParam;
 19  import javax.ws.rs.Produces;
 20  import javax.ws.rs.QueryParam;
 21  import javax.ws.rs.core.Response;
 22  import javax.ws.rs.core.Response.Status;
 23  import javax.ws.rs.core.UriBuilder;
 24  import org.jboss.examples.ticketmonster.rest.dto.VenueDTO;
 25  import org.jboss.examples.ticketmonster.model.Venue;
 26  
 27  /**
 28   * 
 29   */
 30  @Stateless
 31  @Path("forge/venues")
 32  public class VenueEndpoint
 33  {
 34     @PersistenceContext(unitName = "primary")
 35     private EntityManager em;
 36  
 37     @POST
 38     @Consumes("application/json")
 39     public Response create(VenueDTO dto)
 40     {
 41        Venue entity = dto.fromDTO(null, em);
 42        em.persist(entity);
 43        return Response.created(UriBuilder.fromResource(VenueEndpoint.class).path(String.valueOf(entity.getId())).build()).build();
 44     }
 45  
 46     @DELETE
 47     @Path("/{id:[0-9][0-9]*}")
 48     public Response deleteById(@PathParam("id") Long id)
 49     {
 50        Venue entity = em.find(Venue.class, id);
 51        if (entity == null)
 52        {
 53           return Response.status(Status.NOT_FOUND).build();
 54        }
 55        em.remove(entity);
 56        return Response.noContent().build();
 57     }
 58  
 59     @GET
 60     @Path("/{id:[0-9][0-9]*}")
 61     @Produces("application/json")
 62     public Response findById(@PathParam("id") Long id)
 63     {
 64        TypedQuery<Venue> findByIdQuery = em.createQuery("SELECT DISTINCT v FROM Venue v LEFT JOIN FETCH v.sections LEFT JOIN FETCH v.mediaItem WHERE v.id = :entityId ORDER BY v.id", Venue.class);
 65        findByIdQuery.setParameter("entityId", id);
 66        Venue entity;
 67        try
 68        {
 69           entity = findByIdQuery.getSingleResult();
 70        }
 71        catch (NoResultException nre)
 72        {
 73           entity = null;
 74        }
 75        if (entity == null)
 76        {
 77           return Response.status(Status.NOT_FOUND).build();
 78        }
 79        VenueDTO dto = new VenueDTO(entity);
 80        return Response.ok(dto).build();
 81     }
 82  
 83     @GET
 84     @Produces("application/json")
 85     public List<VenueDTO> listAll(@QueryParam("start") Integer startPosition, @QueryParam("max") Integer maxResult)
 86     {
 87        TypedQuery<Venue> findAllQuery = em.createQuery("SELECT DISTINCT v FROM Venue v LEFT JOIN FETCH v.sections LEFT JOIN FETCH v.mediaItem ORDER BY v.id", Venue.class);
 88        if (startPosition != null)
 89        {
 90           findAllQuery.setFirstResult(startPosition);
 91        }
 92        if (maxResult != null)
 93        {
 94           findAllQuery.setMaxResults(maxResult);
 95        }
 96        final List<Venue> searchResults = findAllQuery.getResultList();
 97        final List<VenueDTO> results = new ArrayList<VenueDTO>();
 98        for (Venue searchResult : searchResults)
 99        {
100           VenueDTO dto = new VenueDTO(searchResult);
101           results.add(dto);
102        }
103        return results;
104     }
105  
106     @PUT
107     @Path("/{id:[0-9][0-9]*}")
108     @Consumes("application/json")
109     public Response update(@PathParam("id") Long id, VenueDTO dto)
110     {
111        TypedQuery<Venue> findByIdQuery = em.createQuery("SELECT DISTINCT v FROM Venue v LEFT JOIN FETCH v.sections LEFT JOIN FETCH v.mediaItem WHERE v.id = :entityId ORDER BY v.id", Venue.class);
112        findByIdQuery.setParameter("entityId", id);
113        Venue entity;
114        try
115        {
116           entity = findByIdQuery.getSingleResult();
117        }
118        catch (NoResultException nre)
119        {
120           entity = null;
121        }
122        entity = dto.fromDTO(entity, em);
123        try
124        {
125           entity = em.merge(entity);
126        }
127        catch (OptimisticLockException e)
128        {
129           return Response.status(Response.Status.CONFLICT).entity(e.getEntity()).build();
130        }
```
  * file:///tmp/source-code/backend-v1/src/main/java/org/jboss/examples/ticketmonster/rest/VenueService.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import javax.ejb.Stateless;
  4  import javax.ws.rs.Path;
  5  
  6  import org.jboss.examples.ticketmonster.model.Venue;
  7  
  8  /**
  9   * <p>
 10   *     A JAX-RS endpoint for handling {@link Venue}s. Inherits the actual
 11   *     methods from {@link BaseEntityService}.
 12   * </p>
 13   *
 14   * @author Marius Bogoevici
 15   */
 16  @Path("/venues")
 17  /**
 18   * <p>
 19   *     This is a stateless service, we declare it as an EJB for transaction demarcation
 20   * </p>
 21   */
 22  @Stateless
 23  public class VenueService extends BaseEntityService<Venue> {
 24  
 25      public VenueService() {
 26          super(Venue.class);
 27      }
 28  
 29  }

```
  * file:///tmp/source-code/backend-v1/src/main/java/org/jboss/examples/ticketmonster/service/Bot.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.service;
  2  
  3  import java.util.ArrayList;
  4  import java.util.Collection;
  5  import java.util.Date;
  6  import java.util.List;
  7  import java.util.Map;
  8  import java.util.Random;
  9  import java.util.concurrent.TimeUnit;
 10  
 11  import javax.annotation.Resource;
 12  import javax.ejb.Stateless;
 13  import javax.ejb.Timeout;
 14  import javax.ejb.Timer;
 15  import javax.ejb.TimerConfig;
 16  import javax.ejb.TimerService;
 17  import javax.enterprise.event.Event;
 18  import javax.inject.Inject;
 19  import javax.ws.rs.core.MultivaluedHashMap;
 20  import javax.ws.rs.core.Response;
 21  
 22  import org.jboss.examples.ticketmonster.model.Performance;
 23  import org.jboss.examples.ticketmonster.model.Show;
 24  import org.jboss.examples.ticketmonster.model.TicketPrice;
 25  import org.jboss.examples.ticketmonster.rest.*;
 26  import org.jboss.examples.ticketmonster.util.qualifier.BotMessage;
 27  
 28  @Stateless
 29  public class Bot {
 30      
 31      private static final Random random = new Random(System.nanoTime());
 32      
 33      /** Frequency with which the bot will book **/
 34      public static final long DURATION = TimeUnit.SECONDS.toMillis(3);
 35      
 36      /** Maximum number of ticket requests that will be filed **/
 37      public static int MAX_TICKET_REQUESTS = 100;
 38      
 39      /** Maximum number of tickets per request **/
 40      public static int MAX_TICKETS_PER_REQUEST = 100;
 41      
 42      public static String [] BOOKERS = {"anne@acme.com", "george@acme.com", "william@acme.com", "victoria@acme.com", "edward@acme.com", "elizabeth@acme.com", "mary@acme.com", "charles@acme.com", "james@acme.com", "henry@acme.com", "richard@acme.com", "john@acme.com", "stephen@acme.com"}; 
 43  
 44      @Inject 
 45      private ShowService showService;
 46      
 47      @Inject
 48      private BookingService bookingService;
 49      
 50      @Inject @BotMessage
 51      Event<String> event;
 52      
 53      @Resource
 54      private TimerService timerService;
 55      
 56      public Timer start() {
 57          String startMessage = new StringBuilder("==========================\n")
 58                  .append("Bot started at ").append(new Date().toString()).append("\n")
 59                  .toString();
 60          event.fire(startMessage);
 61          return timerService.createIntervalTimer(0, DURATION, new TimerConfig(null, false));
 62      }
 63      
 64      public void stop(Timer timer) {
 65          String stopMessage = new StringBuilder("==========================\n")
 66                  .append("Bot stopped at ").append(new Date().toString()).append("\n")
 67                  .toString();
 68          event.fire(stopMessage);
 69          timer.cancel();
 70      }
 71      
 72      @Timeout
 73      public void book(Timer timer) {
 74          // Select a show at random
 75          Show show = selectAtRandom(showService.getAll(new MultivaluedHashMap<String, String>()));
 76  
 77          // Select a performance at random
 78          Performance performance = selectAtRandom(show.getPerformances());
 79          
 80          String requestor = selectAtRandom(BOOKERS);
 81  
 82          BookingRequest bookingRequest = new BookingRequest(performance, requestor);
 83  
 84          List<TicketPrice> possibleTicketPrices = new ArrayList<TicketPrice>(show.getTicketPrices());
 85          
 86          List<Integer> indicies = selectAtRandom(MAX_TICKET_REQUESTS < possibleTicketPrices.size() ? MAX_TICKET_REQUESTS : possibleTicketPrices.size());
 87          
 88          StringBuilder message = new StringBuilder("==========================\n")
 89          .append("Booking by ")
 90          .append(requestor)
 91          .append(" at ")
 92          .append(new Date().toString())
 93          .append("\n")
 94          .append(performance)
 95          .append("\n")
 96          .append("~~~~~~~~~~~~~~~~~~~~~~~~~\n");
 97          
 98          for (int index : indicies) {
 99              int no = random.nextInt(MAX_TICKETS_PER_REQUEST);
100              TicketPrice price = possibleTicketPrices.get(index);  
101              bookingRequest.addTicketRequest(new TicketRequest(price, no));
102              message
103                  .append(no)
104                  .append(" of ")
105                  .append(price.getSection())
106                  .append("\n");
107              
108          }
109          Response response = bookingService.createBooking(bookingRequest);
110          if(response.getStatus() == Response.Status.OK.getStatusCode()) {
111              message.append("SUCCESSFUL\n")
112                      .append("~~~~~~~~~~~~~~~~~~~~~~~~~\n");
113          }
114          else {
115              message.append("FAILED:\n")
116                          .append(((Map<String, Object>) response.getEntity()).get("errors"))
117                          .append("~~~~~~~~~~~~~~~~~~~~~~~~~\n");
118          }
119          event.fire(message.toString());
120      }
121      
122      
123      
124      private <T> T selectAtRandom(List<T> list) {
125          int i = random.nextInt(list.size());
126          return list.get(i);
127      }
128      
```
  * file:///tmp/source-code/backend-v2/src/main/java/org/jboss/examples/ticketmonster/rest/BookingEndpoint.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import java.util.ArrayList;
  4  import java.util.List;
  5  
  6  import javax.ejb.Stateless;
  7  import javax.persistence.EntityManager;
  8  import javax.persistence.NoResultException;
  9  import javax.persistence.OptimisticLockException;
 10  import javax.persistence.PersistenceContext;
 11  import javax.persistence.TypedQuery;
 12  import javax.ws.rs.Consumes;
 13  import javax.ws.rs.DELETE;
 14  import javax.ws.rs.GET;
 15  import javax.ws.rs.POST;
 16  import javax.ws.rs.PUT;
 17  import javax.ws.rs.Path;
 18  import javax.ws.rs.PathParam;
 19  import javax.ws.rs.Produces;
 20  import javax.ws.rs.QueryParam;
 21  import javax.ws.rs.core.Response;
 22  import javax.ws.rs.core.Response.Status;
 23  import javax.ws.rs.core.UriBuilder;
 24  import org.jboss.examples.ticketmonster.rest.dto.BookingDTO;
 25  import org.jboss.examples.ticketmonster.model.Booking;
 26  
 27  /**
 28   * 
 29   */
 30  @Stateless
 31  @Path("forge/bookings")
 32  public class BookingEndpoint
 33  {
 34     @PersistenceContext(unitName = "primary")
 35     private EntityManager em;
 36  
 37     @POST
 38     @Consumes("application/json")
 39     public Response create(BookingDTO dto)
 40     {
 41        Booking entity = dto.fromDTO(null, em);
 42        em.persist(entity);
 43        return Response.created(UriBuilder.fromResource(BookingEndpoint.class).path(String.valueOf(entity.getId())).build()).build();
 44     }
 45  
 46     @DELETE
 47     @Path("/{id:[0-9][0-9]*}")
 48     public Response deleteById(@PathParam("id") Long id)
 49     {
 50        Booking entity = em.find(Booking.class, id);
 51        if (entity == null)
 52        {
 53           return Response.status(Status.NOT_FOUND).build();
 54        }
 55        em.remove(entity);
 56        return Response.noContent().build();
 57     }
 58  
 59     @GET
 60     @Path("/{id:[0-9][0-9]*}")
 61     @Produces("application/json")
 62     public Response findById(@PathParam("id") Long id)
 63     {
 64        TypedQuery<Booking> findByIdQuery = em.createQuery("SELECT DISTINCT b FROM Booking b LEFT JOIN FETCH b.tickets LEFT JOIN FETCH b.performance WHERE b.id = :entityId ORDER BY b.id", Booking.class);
 65        findByIdQuery.setParameter("entityId", id);
 66        Booking entity;
 67        try
 68        {
 69           entity = findByIdQuery.getSingleResult();
 70        }
 71        catch (NoResultException nre)
 72        {
 73           entity = null;
 74        }
 75        if (entity == null)
 76        {
 77           return Response.status(Status.NOT_FOUND).build();
 78        }
 79        BookingDTO dto = new BookingDTO(entity);
 80        return Response.ok(dto).build();
 81     }
 82  
 83     @GET
 84     @Produces("application/json")
 85     public List<BookingDTO> listAll(@QueryParam("start") Integer startPosition, @QueryParam("max") Integer maxResult)
 86     {
 87        TypedQuery<Booking> findAllQuery = em.createQuery("SELECT DISTINCT b FROM Booking b LEFT JOIN FETCH b.tickets LEFT JOIN FETCH b.performance ORDER BY b.id", Booking.class);
 88        if (startPosition != null)
 89        {
 90           findAllQuery.setFirstResult(startPosition);
 91        }
 92        if (maxResult != null)
 93        {
 94           findAllQuery.setMaxResults(maxResult);
 95        }
 96        final List<Booking> searchResults = findAllQuery.getResultList();
 97        final List<BookingDTO> results = new ArrayList<BookingDTO>();
 98        for (Booking searchResult : searchResults)
 99        {
100           BookingDTO dto = new BookingDTO(searchResult);
101           results.add(dto);
102        }
103        return results;
104     }
105  
106     @PUT
107     @Path("/{id:[0-9][0-9]*}")
108     @Consumes("application/json")
109     public Response update(@PathParam("id") Long id, BookingDTO dto)
110     {
111        TypedQuery<Booking> findByIdQuery = em.createQuery("SELECT DISTINCT b FROM Booking b LEFT JOIN FETCH b.tickets LEFT JOIN FETCH b.performance WHERE b.id = :entityId ORDER BY b.id", Booking.class);
112        findByIdQuery.setParameter("entityId", id);
113        Booking entity;
114        try
115        {
116           entity = findByIdQuery.getSingleResult();
117        }
118        catch (NoResultException nre)
119        {
120           entity = null;
121        }
122        entity = dto.fromDTO(entity, em);
123        try
124        {
125           entity = em.merge(entity);
126        }
127        catch (OptimisticLockException e)
128        {
129           return Response.status(Response.Status.CONFLICT).entity(e.getEntity()).build();
130        }
```
  * file:///tmp/source-code/backend-v2/src/main/java/org/jboss/examples/ticketmonster/rest/BookingService.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import org.ff4j.FF4j;
  4  import org.jboss.examples.ticketmonster.model.*;
  5  import org.jboss.examples.ticketmonster.orders.OrdersRequestDTO;
  6  import org.jboss.examples.ticketmonster.service.AllocatedSeats;
  7  import org.jboss.examples.ticketmonster.service.SeatAllocationService;
  8  import org.jboss.examples.ticketmonster.util.qualifier.Cancelled;
  9  import org.jboss.examples.ticketmonster.util.qualifier.Created;
 10  import org.jboss.resteasy.client.jaxrs.ResteasyClient;
 11  import org.jboss.resteasy.client.jaxrs.ResteasyClientBuilder;
 12  
 13  import javax.ejb.Stateless;
 14  import javax.enterprise.event.Event;
 15  import javax.inject.Inject;
 16  import javax.validation.ConstraintViolation;
 17  import javax.validation.ConstraintViolationException;
 18  import javax.ws.rs.*;
 19  import javax.ws.rs.client.Client;
 20  import javax.ws.rs.client.ClientBuilder;
 21  import javax.ws.rs.client.Entity;
 22  import javax.ws.rs.core.MediaType;
 23  import javax.ws.rs.core.MultivaluedHashMap;
 24  import javax.ws.rs.core.Response;
 25  import java.util.*;
 26  
 27  /**
 28   * <p>
 29   *     A JAX-RS endpoint for handling {@link Booking}s. Inherits the GET
 30   *     methods from {@link BaseEntityService}, and implements additional REST methods.
 31   * </p>
 32   *
 33   * @author Marius Bogoevici
 34   * @author Pete Muir
 35   */
 36  @Path("/bookings")
 37  /**
 38   * <p>
 39   *     This is a stateless service, we declare it as an EJB for transaction demarcation
 40   * </p>
 41   */
 42  @Stateless
 43  public class BookingService extends BaseEntityService<Booking> {
 44  
 45      @Inject
 46      SeatAllocationService seatAllocationService;
 47  
 48      @Inject
 49      FF4j ff;
 50  
 51      @Inject @Cancelled
 52      private Event<Booking> cancelledBookingEvent;
 53  
 54      @Inject @Created
 55      private Event<Booking> newBookingEvent;
 56  
 57      private String ordersServiceUri = "http://localhost:9090/rest/bookings";
 58      
 59      public BookingService() {
 60          super(Booking.class);
 61      }
 62      
 63      @DELETE
 64      public Response deleteAllBookings() {
 65      	List<Booking> bookings = getAll(new MultivaluedHashMap<String, String>());
 66      	for (Booking booking : bookings) {
 67      		deleteBooking(booking.getId());
 68      	}
 69          return Response.noContent().build();
 70      }
 71  
 72      /**
 73       * <p>
 74       * Delete a booking by id
 75       * </p>
 76       * @param id
 77       * @return
 78       */
 79      @DELETE
 80      @Path("/{id:[0-9][0-9]*}")
 81      public Response deleteBooking(@PathParam("id") Long id) {
 82          Booking booking = getEntityManager().find(Booking.class, id);
 83          if (booking == null) {
 84              return Response.status(Response.Status.NOT_FOUND).build();
 85          }
 86          getEntityManager().remove(booking);
 87          // Group together seats by section so that we can deallocate them in a group
 88          Map<Section, List<Seat>> seatsBySection = new TreeMap<Section, java.util.List<Seat>>(SectionComparator.instance());
 89          for (Ticket ticket : booking.getTickets()) {
 90              List<Seat> seats = seatsBySection.get(ticket.getSeat().getSection());
 91              if (seats == null) {
 92                  seats = new ArrayList<Seat>();
 93                  seatsBySection.put(ticket.getSeat().getSection(), seats);
 94              }
 95              seats.add(ticket.getSeat());
 96          }
 97          // Deallocate each section block
 98          for (Map.Entry<Section, List<Seat>> sectionListEntry : seatsBySection.entrySet()) {
 99              seatAllocationService.deallocateSeats( sectionListEntry.getKey(),
100                      booking.getPerformance(), sectionListEntry.getValue());
101          }
102          cancelledBookingEvent.fire(booking);
103          return Response.noContent().build();
104      }
105  
106      /**
107       * <p>
108       *   Create a booking. Data is contained in the bookingRequest object
109       * </p>
110       * @param bookingRequest
111       * @return
112       */
113      @POST
114      /**
115       * <p> Data is received in JSON format. For easy handling, it will be unmarshalled in the support
116       * {@link BookingRequest} class.
117       */
118      @Consumes(MediaType.APPLICATION_JSON)
119      public Response createBooking(BookingRequest bookingRequest) {
120          Response response = null;
121  
122          if (ff.check("orders-internal")) {
123              System.out.println("Creating internal booking");
124              response = createBookingInternal(bookingRequest);
125          }
126  
127          if (ff.check("orders-service")) {
128              if (ff.check("orders-internal")) {
129                  createSyntheticBookingOrdersService(bookingRequest);
130  
131              }
132              else {
133                  response = createBookingOrdersService(bookingRequest);
134              }
135          }
136  
137          return response;
138      }
139  
140      /**
141       * Makes a call to the Orders Service, but lets it know that this is a synthetic transaction
142       * that has already been recorded (ie, here internally) and is sent just for exercising the orders
```
  * file:///tmp/source-code/backend-v2/src/main/java/org/jboss/examples/ticketmonster/rest/EventCategoryEndpoint.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import java.util.ArrayList;
  4  import java.util.List;
  5  
  6  import javax.ejb.Stateless;
  7  import javax.persistence.EntityManager;
  8  import javax.persistence.NoResultException;
  9  import javax.persistence.OptimisticLockException;
 10  import javax.persistence.PersistenceContext;
 11  import javax.persistence.TypedQuery;
 12  import javax.ws.rs.Consumes;
 13  import javax.ws.rs.DELETE;
 14  import javax.ws.rs.GET;
 15  import javax.ws.rs.POST;
 16  import javax.ws.rs.PUT;
 17  import javax.ws.rs.Path;
 18  import javax.ws.rs.PathParam;
 19  import javax.ws.rs.Produces;
 20  import javax.ws.rs.QueryParam;
 21  import javax.ws.rs.core.Response;
 22  import javax.ws.rs.core.Response.Status;
 23  import javax.ws.rs.core.UriBuilder;
 24  import org.jboss.examples.ticketmonster.rest.dto.EventCategoryDTO;
 25  import org.jboss.examples.ticketmonster.model.EventCategory;
 26  
 27  /**
 28   * 
 29   */
 30  @Stateless
 31  @Path("/eventcategories")
 32  public class EventCategoryEndpoint
 33  {
 34     @PersistenceContext(unitName = "primary")
 35     private EntityManager em;
 36  
 37     @POST
 38     @Consumes("application/json")
 39     public Response create(EventCategoryDTO dto)
 40     {
 41        EventCategory entity = dto.fromDTO(null, em);
 42        em.persist(entity);
 43        return Response.created(UriBuilder.fromResource(EventCategoryEndpoint.class).path(String.valueOf(entity.getId())).build()).build();
 44     }
 45  
 46     @DELETE
 47     @Path("/{id:[0-9][0-9]*}")
 48     public Response deleteById(@PathParam("id") Long id)
 49     {
 50        EventCategory entity = em.find(EventCategory.class, id);
 51        if (entity == null)
 52        {
 53           return Response.status(Status.NOT_FOUND).build();
 54        }
 55        em.remove(entity);
 56        return Response.noContent().build();
 57     }
 58  
 59     @GET
 60     @Path("/{id:[0-9][0-9]*}")
 61     @Produces("application/json")
 62     public Response findById(@PathParam("id") Long id)
 63     {
 64        TypedQuery<EventCategory> findByIdQuery = em.createQuery("SELECT DISTINCT e FROM EventCategory e WHERE e.id = :entityId ORDER BY e.id", EventCategory.class);
 65        findByIdQuery.setParameter("entityId", id);
 66        EventCategory entity;
 67        try
 68        {
 69           entity = findByIdQuery.getSingleResult();
 70        }
 71        catch (NoResultException nre)
 72        {
 73           entity = null;
 74        }
 75        if (entity == null)
 76        {
 77           return Response.status(Status.NOT_FOUND).build();
 78        }
 79        EventCategoryDTO dto = new EventCategoryDTO(entity);
 80        return Response.ok(dto).build();
 81     }
 82  
 83     @GET
 84     @Produces("application/json")
 85     public List<EventCategoryDTO> listAll(@QueryParam("start") Integer startPosition, @QueryParam("max") Integer maxResult)
 86     {
 87        TypedQuery<EventCategory> findAllQuery = em.createQuery("SELECT DISTINCT e FROM EventCategory e ORDER BY e.id", EventCategory.class);
 88        if (startPosition != null)
 89        {
 90           findAllQuery.setFirstResult(startPosition);
 91        }
 92        if (maxResult != null)
 93        {
 94           findAllQuery.setMaxResults(maxResult);
 95        }
 96        final List<EventCategory> searchResults = findAllQuery.getResultList();
 97        final List<EventCategoryDTO> results = new ArrayList<EventCategoryDTO>();
 98        for (EventCategory searchResult : searchResults)
 99        {
100           EventCategoryDTO dto = new EventCategoryDTO(searchResult);
101           results.add(dto);
102        }
103        return results;
104     }
105  
106     @PUT
107     @Path("/{id:[0-9][0-9]*}")
108     @Consumes("application/json")
109     public Response update(@PathParam("id") Long id, EventCategoryDTO dto)
110     {
111        TypedQuery<EventCategory> findByIdQuery = em.createQuery("SELECT DISTINCT e FROM EventCategory e WHERE e.id = :entityId ORDER BY e.id", EventCategory.class);
112        findByIdQuery.setParameter("entityId", id);
113        EventCategory entity;
114        try
115        {
116           entity = findByIdQuery.getSingleResult();
117        }
118        catch (NoResultException nre)
119        {
120           entity = null;
121        }
122        entity = dto.fromDTO(entity, em);
123        try
124        {
125           entity = em.merge(entity);
126        }
127        catch (OptimisticLockException e)
128        {
129           return Response.status(Response.Status.CONFLICT).entity(e.getEntity()).build();
130        }
```
  * file:///tmp/source-code/backend-v2/src/main/java/org/jboss/examples/ticketmonster/rest/EventEndpoint.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import java.util.ArrayList;
  4  import java.util.List;
  5  
  6  import javax.ejb.Stateless;
  7  import javax.persistence.EntityManager;
  8  import javax.persistence.NoResultException;
  9  import javax.persistence.OptimisticLockException;
 10  import javax.persistence.PersistenceContext;
 11  import javax.persistence.TypedQuery;
 12  import javax.ws.rs.Consumes;
 13  import javax.ws.rs.DELETE;
 14  import javax.ws.rs.GET;
 15  import javax.ws.rs.POST;
 16  import javax.ws.rs.PUT;
 17  import javax.ws.rs.Path;
 18  import javax.ws.rs.PathParam;
 19  import javax.ws.rs.Produces;
 20  import javax.ws.rs.QueryParam;
 21  import javax.ws.rs.core.Response;
 22  import javax.ws.rs.core.Response.Status;
 23  import javax.ws.rs.core.UriBuilder;
 24  import org.jboss.examples.ticketmonster.rest.dto.EventDTO;
 25  import org.jboss.examples.ticketmonster.model.Event;
 26  
 27  /**
 28   * 
 29   */
 30  @Stateless
 31  @Path("forge/events")
 32  public class EventEndpoint
 33  {
 34     @PersistenceContext(unitName = "primary")
 35     private EntityManager em;
 36  
 37     @POST
 38     @Consumes("application/json")
 39     public Response create(EventDTO dto)
 40     {
 41        Event entity = dto.fromDTO(null, em);
 42        em.persist(entity);
 43        return Response.created(UriBuilder.fromResource(EventEndpoint.class).path(String.valueOf(entity.getId())).build()).build();
 44     }
 45  
 46     @DELETE
 47     @Path("/{id:[0-9][0-9]*}")
 48     public Response deleteById(@PathParam("id") Long id)
 49     {
 50        Event entity = em.find(Event.class, id);
 51        if (entity == null)
 52        {
 53           return Response.status(Status.NOT_FOUND).build();
 54        }
 55        em.remove(entity);
 56        return Response.noContent().build();
 57     }
 58  
 59     @GET
 60     @Path("/{id:[0-9][0-9]*}")
 61     @Produces("application/json")
 62     public Response findById(@PathParam("id") Long id)
 63     {
 64        TypedQuery<Event> findByIdQuery = em.createQuery("SELECT DISTINCT e FROM Event e LEFT JOIN FETCH e.mediaItem LEFT JOIN FETCH e.category WHERE e.id = :entityId ORDER BY e.id", Event.class);
 65        findByIdQuery.setParameter("entityId", id);
 66        Event entity;
 67        try
 68        {
 69           entity = findByIdQuery.getSingleResult();
 70        }
 71        catch (NoResultException nre)
 72        {
 73           entity = null;
 74        }
 75        if (entity == null)
 76        {
 77           return Response.status(Status.NOT_FOUND).build();
 78        }
 79        EventDTO dto = new EventDTO(entity);
 80        return Response.ok(dto).build();
 81     }
 82  
 83     @GET
 84     @Produces("application/json")
 85     public List<EventDTO> listAll(@QueryParam("start") Integer startPosition, @QueryParam("max") Integer maxResult)
 86     {
 87        TypedQuery<Event> findAllQuery = em.createQuery("SELECT DISTINCT e FROM Event e LEFT JOIN FETCH e.mediaItem LEFT JOIN FETCH e.category ORDER BY e.id", Event.class);
 88        if (startPosition != null)
 89        {
 90           findAllQuery.setFirstResult(startPosition);
 91        }
 92        if (maxResult != null)
 93        {
 94           findAllQuery.setMaxResults(maxResult);
 95        }
 96        final List<Event> searchResults = findAllQuery.getResultList();
 97        final List<EventDTO> results = new ArrayList<EventDTO>();
 98        for (Event searchResult : searchResults)
 99        {
100           EventDTO dto = new EventDTO(searchResult);
101           results.add(dto);
102        }
103        return results;
104     }
105  
106     @PUT
107     @Path("/{id:[0-9][0-9]*}")
108     @Consumes("application/json")
109     public Response update(@PathParam("id") Long id, EventDTO dto)
110     {
111        TypedQuery<Event> findByIdQuery = em.createQuery("SELECT DISTINCT e FROM Event e LEFT JOIN FETCH e.mediaItem LEFT JOIN FETCH e.category WHERE e.id = :entityId ORDER BY e.id", Event.class);
112        findByIdQuery.setParameter("entityId", id);
113        Event entity;
114        try
115        {
116           entity = findByIdQuery.getSingleResult();
117        }
118        catch (NoResultException nre)
119        {
120           entity = null;
121        }
122        entity = dto.fromDTO(entity, em);
123        try
124        {
125           entity = em.merge(entity);
126        }
127        catch (OptimisticLockException e)
128        {
129           return Response.status(Response.Status.CONFLICT).entity(e.getEntity()).build();
130        }
```
  * file:///tmp/source-code/backend-v2/src/main/java/org/jboss/examples/ticketmonster/rest/EventService.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import java.util.ArrayList;
  4  import java.util.List;
  5  
  6  import javax.ejb.Stateless;
  7  import javax.persistence.criteria.CriteriaBuilder;
  8  import javax.persistence.criteria.Predicate;
  9  import javax.persistence.criteria.Root;
 10  import javax.ws.rs.Path;
 11  import javax.ws.rs.core.MultivaluedMap;
 12  
 13  import org.jboss.examples.ticketmonster.model.Event;
 14  
 15  /**
 16   * <p>
 17   *     A JAX-RS endpoint for handling {@link Event}s. Inherits the actual
 18   *     methods from {@link BaseEntityService}, but implements additional search
 19   *     criteria.
 20   * </p>
 21   *
 22   * @author Marius Bogoevici
 23   */
 24  @Path("/events")
 25  /**
 26   * <p>
 27   *     This is a stateless service, we declare it as an EJB for transaction demarcation
 28   * </p>
 29   */
 30  @Stateless
 31  public class EventService extends BaseEntityService<Event> {
 32  
 33      public EventService() {
 34          super(Event.class);
 35      }
 36  
 37      /**
 38       * <p>
 39       *    We override the method from parent in order to add support for additional search
 40       *    criteria for events.
 41       * </p>
 42       * @param queryParameters - the HTTP query parameters received by the endpoint
 43       * @param criteriaBuilder - @{link CriteriaBuilder} used by the invoker
 44       * @param root  @{link Root} used by the invoker
 45       * @return
 46       */
 47      @Override
 48      protected Predicate[] extractPredicates(
 49              MultivaluedMap<String, String> queryParameters, 
 50              CriteriaBuilder criteriaBuilder, 
 51              Root<Event> root) {
 52          List<Predicate> predicates = new ArrayList<Predicate>() ;
 53          
 54          if (queryParameters.containsKey("category")) {
 55              String category = queryParameters.getFirst("category");
 56              predicates.add(criteriaBuilder.equal(root.get("category").get("id"), category));
 57          }
 58          
 59          return predicates.toArray(new Predicate[]{});
 60      }
 61  }

```
  * file:///tmp/source-code/backend-v2/src/main/java/org/jboss/examples/ticketmonster/rest/MediaItemEndpoint.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import java.util.ArrayList;
  4  import java.util.List;
  5  
  6  import javax.ejb.Stateless;
  7  import javax.persistence.EntityManager;
  8  import javax.persistence.NoResultException;
  9  import javax.persistence.OptimisticLockException;
 10  import javax.persistence.PersistenceContext;
 11  import javax.persistence.TypedQuery;
 12  import javax.ws.rs.Consumes;
 13  import javax.ws.rs.DELETE;
 14  import javax.ws.rs.GET;
 15  import javax.ws.rs.POST;
 16  import javax.ws.rs.PUT;
 17  import javax.ws.rs.Path;
 18  import javax.ws.rs.PathParam;
 19  import javax.ws.rs.Produces;
 20  import javax.ws.rs.QueryParam;
 21  import javax.ws.rs.core.Response;
 22  import javax.ws.rs.core.Response.Status;
 23  import javax.ws.rs.core.UriBuilder;
 24  import org.jboss.examples.ticketmonster.rest.dto.MediaItemDTO;
 25  import org.jboss.examples.ticketmonster.model.MediaItem;
 26  
 27  /**
 28   * 
 29   */
 30  @Stateless
 31  @Path("/mediaitems")
 32  public class MediaItemEndpoint
 33  {
 34     @PersistenceContext(unitName = "primary")
 35     private EntityManager em;
 36  
 37     @POST
 38     @Consumes("application/json")
 39     public Response create(MediaItemDTO dto)
 40     {
 41        MediaItem entity = dto.fromDTO(null, em);
 42        em.persist(entity);
 43        return Response.created(UriBuilder.fromResource(MediaItemEndpoint.class).path(String.valueOf(entity.getId())).build()).build();
 44     }
 45  
 46     @DELETE
 47     @Path("/{id:[0-9][0-9]*}")
 48     public Response deleteById(@PathParam("id") Long id)
 49     {
 50        MediaItem entity = em.find(MediaItem.class, id);
 51        if (entity == null)
 52        {
 53           return Response.status(Status.NOT_FOUND).build();
 54        }
 55        em.remove(entity);
 56        return Response.noContent().build();
 57     }
 58  
 59     @GET
 60     @Path("/{id:[0-9][0-9]*}")
 61     @Produces("application/json")
 62     public Response findById(@PathParam("id") Long id)
 63     {
 64        TypedQuery<MediaItem> findByIdQuery = em.createQuery("SELECT DISTINCT m FROM MediaItem m WHERE m.id = :entityId ORDER BY m.id", MediaItem.class);
 65        findByIdQuery.setParameter("entityId", id);
 66        MediaItem entity;
 67        try
 68        {
 69           entity = findByIdQuery.getSingleResult();
 70        }
 71        catch (NoResultException nre)
 72        {
 73           entity = null;
 74        }
 75        if (entity == null)
 76        {
 77           return Response.status(Status.NOT_FOUND).build();
 78        }
 79        MediaItemDTO dto = new MediaItemDTO(entity);
 80        return Response.ok(dto).build();
 81     }
 82  
 83     @GET
 84     @Produces("application/json")
 85     public List<MediaItemDTO> listAll(@QueryParam("start") Integer startPosition, @QueryParam("max") Integer maxResult)
 86     {
 87        TypedQuery<MediaItem> findAllQuery = em.createQuery("SELECT DISTINCT m FROM MediaItem m ORDER BY m.id", MediaItem.class);
 88        if (startPosition != null)
 89        {
 90           findAllQuery.setFirstResult(startPosition);
 91        }
 92        if (maxResult != null)
 93        {
 94           findAllQuery.setMaxResults(maxResult);
 95        }
 96        final List<MediaItem> searchResults = findAllQuery.getResultList();
 97        final List<MediaItemDTO> results = new ArrayList<MediaItemDTO>();
 98        for (MediaItem searchResult : searchResults)
 99        {
100           MediaItemDTO dto = new MediaItemDTO(searchResult);
101           results.add(dto);
102        }
103        return results;
104     }
105  
106     @PUT
107     @Path("/{id:[0-9][0-9]*}")
108     @Consumes("application/json")
109     public Response update(@PathParam("id") Long id, MediaItemDTO dto)
110     {
111        TypedQuery<MediaItem> findByIdQuery = em.createQuery("SELECT DISTINCT m FROM MediaItem m WHERE m.id = :entityId ORDER BY m.id", MediaItem.class);
112        findByIdQuery.setParameter("entityId", id);
113        MediaItem entity;
114        try
115        {
116           entity = findByIdQuery.getSingleResult();
117        }
118        catch (NoResultException nre)
119        {
120           entity = null;
121        }
122        entity = dto.fromDTO(entity, em);
123        try
124        {
125           entity = em.merge(entity);
126        }
127        catch (OptimisticLockException e)
128        {
129           return Response.status(Response.Status.CONFLICT).entity(e.getEntity()).build();
130        }
```
  * file:///tmp/source-code/backend-v2/src/main/java/org/jboss/examples/ticketmonster/rest/MetricsService.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import java.util.*;
  4  
  5  import javax.ejb.Stateless;
  6  import javax.inject.Inject;
  7  import javax.persistence.EntityManager;
  8  import javax.persistence.Query;
  9  import javax.persistence.TypedQuery;
 10  import javax.ws.rs.GET;
 11  import javax.ws.rs.Path;
 12  import javax.ws.rs.Produces;
 13  import javax.ws.rs.core.MediaType;
 14  
 15  import org.jboss.examples.ticketmonster.model.Show;
 16  
 17  /**
 18   * A read-only REST resource that provides a collection of metrics for shows occuring in the future. Updates to metrics via
 19   * POST/PUT etc. are not allowed, since they are not meant to be computed by consumers.
 20   * 
 21   * @author Vineet Reynolds
 22   * 
 23   */
 24  @Path("/metrics")
 25  @Stateless
 26  public class MetricsService {
 27  
 28      @Inject
 29      private EntityManager entityManager;
 30  
 31      /**
 32       * Retrieves a collection of metrics for Shows. Each metric in the collection contains
 33       * <ul>
 34       * <li>the show id,</li>
 35       * <li>the event name of the show,</li>
 36       * <li>the venue for the show,</li>
 37       * <li>the capacity for the venue</li>
 38       * <li>the performances for the show,
 39       * <ul>
 40       * <li>the timestamp for each performance,</li>
 41       * <li>the occupied count for each performance</li>
 42       * </ul>
 43       * </li>
 44       * </ul>
 45       * 
 46       * @return A JSON representation of metrics for shows.
 47       */
 48      @GET
 49      @Produces(MediaType.APPLICATION_JSON)
 50      public List<ShowMetric> getMetrics() {
 51          return retrieveMetricsFromShows(retrieveShows(),
 52              retrieveOccupiedCounts());
 53      }
 54  
 55      private List<ShowMetric> retrieveMetricsFromShows(List<Show> shows,
 56          Map<Long, Long> occupiedCounts) {
 57          List<ShowMetric> metrics = new ArrayList<ShowMetric>();
 58          for (Show show : shows) {
 59              metrics.add(new ShowMetric(show, occupiedCounts));
 60          }
 61          return metrics;
 62      }
 63  
 64      private List<Show> retrieveShows() {
 65          TypedQuery<Show> showQuery = entityManager
 66              .createQuery("select DISTINCT s from Show s JOIN s.performances p", Show.class);
 67          return showQuery.getResultList();
 68      }
 69  
 70      private Map<Long, Long> retrieveOccupiedCounts() {
 71          Map<Long, Long> occupiedCounts = new HashMap<Long, Long>();
 72  
 73          Query occupiedCountsQuery = entityManager
 74              .createQuery("select b.performance.id, SIZE(b.tickets) from Booking b "
 75                  + "GROUP BY b.performance.id");
 76  
 77          List<Object[]> results = occupiedCountsQuery.getResultList();
 78          for (Object[] result : results) {
 79              occupiedCounts.put((Long) result[0],
 80                  ((Integer) result[1]).longValue());
 81          }
 82  
 83          return occupiedCounts;
 84      }
 85  }

```
  * file:///tmp/source-code/backend-v2/src/main/java/org/jboss/examples/ticketmonster/rest/PerformanceEndpoint.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import java.util.ArrayList;
  4  import java.util.List;
  5  
  6  import javax.ejb.Stateless;
  7  import javax.persistence.EntityManager;
  8  import javax.persistence.NoResultException;
  9  import javax.persistence.OptimisticLockException;
 10  import javax.persistence.PersistenceContext;
 11  import javax.persistence.TypedQuery;
 12  import javax.persistence.criteria.CriteriaBuilder;
 13  import javax.persistence.criteria.CriteriaQuery;
 14  import javax.persistence.criteria.Predicate;
 15  import javax.persistence.criteria.Root;
 16  import javax.ws.rs.Consumes;
 17  import javax.ws.rs.DELETE;
 18  import javax.ws.rs.GET;
 19  import javax.ws.rs.POST;
 20  import javax.ws.rs.PUT;
 21  import javax.ws.rs.Path;
 22  import javax.ws.rs.PathParam;
 23  import javax.ws.rs.Produces;
 24  import javax.ws.rs.QueryParam;
 25  import javax.ws.rs.core.Response;
 26  import javax.ws.rs.core.Response.Status;
 27  import javax.ws.rs.core.UriBuilder;
 28  
 29  import org.jboss.examples.ticketmonster.rest.dto.PerformanceDTO;
 30  import org.jboss.examples.ticketmonster.model.Booking;
 31  import org.jboss.examples.ticketmonster.model.Performance;
 32  import org.jboss.examples.ticketmonster.model.SectionAllocation;
 33  import org.jboss.examples.ticketmonster.model.Show;
 34  
 35  /**
 36   * 
 37   */
 38  @Stateless
 39  @Path("/performances")
 40  public class PerformanceEndpoint
 41  {
 42     @PersistenceContext(unitName = "primary")
 43     private EntityManager em;
 44  
 45     @POST
 46     @Consumes("application/json")
 47     public Response create(PerformanceDTO dto)
 48     {
 49        Performance entity = dto.fromDTO(null, em);
 50        em.persist(entity);
 51        return Response.created(UriBuilder.fromResource(PerformanceEndpoint.class).path(String.valueOf(entity.getId())).build()).build();
 52     }
 53  
 54     @DELETE
 55     @Path("/{id:[0-9][0-9]*}")
 56     public Response deleteById(@PathParam("id") Long id)
 57     {
 58        Performance entity = em.find(Performance.class, id);
 59        if (entity == null)
 60        {
 61           return Response.status(Status.NOT_FOUND).build();
 62        }
 63        Show show = entity.getShow();
 64        show.getPerformances().remove(entity);
 65        entity.setShow(null);
 66        this.em.merge(show);
 67        List<SectionAllocation> sectionAllocations = findSectionAllocationsByPerformance(entity);
 68        for(SectionAllocation sectionAllocation: sectionAllocations) {
 69           this.em.remove(sectionAllocation);
 70        }
 71        List<Booking> bookings = findBookingsByPerformance(entity);
 72        for(Booking booking: bookings) {
 73           this.em.remove(booking);
 74        }
 75        em.remove(entity);
 76        return Response.noContent().build();
 77     }
 78  
 79     @GET
 80     @Path("/{id:[0-9][0-9]*}")
 81     @Produces("application/json")
 82     public Response findById(@PathParam("id") Long id)
 83     {
 84        TypedQuery<Performance> findByIdQuery = em.createQuery("SELECT DISTINCT p FROM Performance p LEFT JOIN FETCH p.show WHERE p.id = :entityId ORDER BY p.id", Performance.class);
 85        findByIdQuery.setParameter("entityId", id);
 86        Performance entity;
 87        try
 88        {
 89           entity = findByIdQuery.getSingleResult();
 90        }
 91        catch (NoResultException nre)
 92        {
 93           entity = null;
 94        }
 95        if (entity == null)
 96        {
 97           return Response.status(Status.NOT_FOUND).build();
 98        }
 99        PerformanceDTO dto = new PerformanceDTO(entity);
100        return Response.ok(dto).build();
101     }
102  
103     @GET
104     @Produces("application/json")
105     public List<PerformanceDTO> listAll(@QueryParam("start") Integer startPosition, @QueryParam("max") Integer maxResult)
106     {
107        TypedQuery<Performance> findAllQuery = em.createQuery("SELECT DISTINCT p FROM Performance p LEFT JOIN FETCH p.show ORDER BY p.id", Performance.class);
108        if (startPosition != null)
109        {
110           findAllQuery.setFirstResult(startPosition);
111        }
112        if (maxResult != null)
113        {
114           findAllQuery.setMaxResults(maxResult);
115        }
116        final List<Performance> searchResults = findAllQuery.getResultList();
117        final List<PerformanceDTO> results = new ArrayList<PerformanceDTO>();
118        for (Performance searchResult : searchResults)
119        {
120           PerformanceDTO dto = new PerformanceDTO(searchResult);
121           results.add(dto);
122        }
123        return results;
124     }
125  
126     @PUT
127     @Path("/{id:[0-9][0-9]*}")
128     @Consumes("application/json")
129     public Response update(@PathParam("id") Long id, PerformanceDTO dto)
130     {
131        TypedQuery<Performance> findByIdQuery = em.createQuery("SELECT DISTINCT p FROM Performance p LEFT JOIN FETCH p.show WHERE p.id = :entityId ORDER BY p.id", Performance.class);
132        findByIdQuery.setParameter("entityId", id);
133        Performance entity;
134        try
135        {
136           entity = findByIdQuery.getSingleResult();
137        }
138        catch (NoResultException nre)
```
  * file:///tmp/source-code/backend-v2/src/main/java/org/jboss/examples/ticketmonster/rest/PingService.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  /**
  2   * Licensed to the Apache Software Foundation (ASF) under one or more
  3   * contributor license agreements.  See the NOTICE file distributed with
  4   * this work for additional information regarding copyright ownership.
  5   * The ASF licenses this file to You under the Apache License, Version 2.0
  6   * (the "License"); you may not use this file except in compliance with
  7   * the License.  You may obtain a copy of the License at
  8   * <p>
  9   * http://www.apache.org/licenses/LICENSE-2.0
 10   * <p>
 11   * Unless required by applicable law or agreed to in writing, software
 12   * distributed under the License is distributed on an "AS IS" BASIS,
 13   * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 14   * See the License for the specific language governing permissions and
 15   * limitations under the License.
 16   */
 17  package org.jboss.examples.ticketmonster.rest;
 18  
 19  import org.ff4j.FF4j;
 20  import org.ff4j.core.Feature;
 21  
 22  import javax.ejb.Stateless;
 23  import javax.inject.Inject;
 24  import javax.ws.rs.GET;
 25  import javax.ws.rs.Path;
 26  import java.util.Map;
 27  
 28  /**
 29   * Created by ceposta 
 30   * <a href="http://christianposta.com/blog>http://christianposta.com/blog</a>.
 31   */
 32  @Path("/ping")
 33  @Stateless
 34  public class PingService {
 35      @Inject
 36      FF4j ff;
 37  
 38      @GET
 39      public String ping(){
 40          StringBuilder sb = new StringBuilder("pong: ");
 41  
 42          Map<String, Feature> features = ff.getFeatures();
 43  
 44          for (Feature feature : features.values()) {
 45              if(feature.isEnable()){
 46                  sb.append("[");
 47                  sb.append(feature.getUid());
 48                  sb.append("] ");
 49              }
 50          }
 51          return sb.toString() + " " + ff.getVersion();
 52      }
 53  }

```
  * file:///tmp/source-code/backend-v2/src/main/java/org/jboss/examples/ticketmonster/rest/SectionAllocationEndpoint.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import java.util.ArrayList;
  4  import java.util.List;
  5  
  6  import javax.ejb.Stateless;
  7  import javax.persistence.EntityManager;
  8  import javax.persistence.NoResultException;
  9  import javax.persistence.OptimisticLockException;
 10  import javax.persistence.PersistenceContext;
 11  import javax.persistence.TypedQuery;
 12  import javax.ws.rs.Consumes;
 13  import javax.ws.rs.DELETE;
 14  import javax.ws.rs.GET;
 15  import javax.ws.rs.POST;
 16  import javax.ws.rs.PUT;
 17  import javax.ws.rs.Path;
 18  import javax.ws.rs.PathParam;
 19  import javax.ws.rs.Produces;
 20  import javax.ws.rs.QueryParam;
 21  import javax.ws.rs.core.Response;
 22  import javax.ws.rs.core.Response.Status;
 23  import javax.ws.rs.core.UriBuilder;
 24  import org.jboss.examples.ticketmonster.rest.dto.SectionAllocationDTO;
 25  import org.jboss.examples.ticketmonster.model.SectionAllocation;
 26  
 27  /**
 28   * 
 29   */
 30  @Stateless
 31  @Path("/sectionallocations")
 32  public class SectionAllocationEndpoint
 33  {
 34     @PersistenceContext(unitName = "primary")
 35     private EntityManager em;
 36  
 37     @POST
 38     @Consumes("application/json")
 39     public Response create(SectionAllocationDTO dto)
 40     {
 41        SectionAllocation entity = dto.fromDTO(null, em);
 42        em.persist(entity);
 43        return Response.created(UriBuilder.fromResource(SectionAllocationEndpoint.class).path(String.valueOf(entity.getId())).build()).build();
 44     }
 45  
 46     @DELETE
 47     @Path("/{id:[0-9][0-9]*}")
 48     public Response deleteById(@PathParam("id") Long id)
 49     {
 50        SectionAllocation entity = em.find(SectionAllocation.class, id);
 51        if (entity == null)
 52        {
 53           return Response.status(Status.NOT_FOUND).build();
 54        }
 55        em.remove(entity);
 56        return Response.noContent().build();
 57     }
 58  
 59     @GET
 60     @Path("/{id:[0-9][0-9]*}")
 61     @Produces("application/json")
 62     public Response findById(@PathParam("id") Long id)
 63     {
 64        TypedQuery<SectionAllocation> findByIdQuery = em.createQuery("SELECT DISTINCT s FROM SectionAllocation s LEFT JOIN FETCH s.performance LEFT JOIN FETCH s.section WHERE s.id = :entityId ORDER BY s.id", SectionAllocation.class);
 65        findByIdQuery.setParameter("entityId", id);
 66        SectionAllocation entity;
 67        try
 68        {
 69           entity = findByIdQuery.getSingleResult();
 70        }
 71        catch (NoResultException nre)
 72        {
 73           entity = null;
 74        }
 75        if (entity == null)
 76        {
 77           return Response.status(Status.NOT_FOUND).build();
 78        }
 79        SectionAllocationDTO dto = new SectionAllocationDTO(entity);
 80        return Response.ok(dto).build();
 81     }
 82  
 83     @GET
 84     @Produces("application/json")
 85     public List<SectionAllocationDTO> listAll(@QueryParam("start") Integer startPosition, @QueryParam("max") Integer maxResult)
 86     {
 87        TypedQuery<SectionAllocation> findAllQuery = em.createQuery("SELECT DISTINCT s FROM SectionAllocation s LEFT JOIN FETCH s.performance LEFT JOIN FETCH s.section ORDER BY s.id", SectionAllocation.class);
 88        if (startPosition != null)
 89        {
 90           findAllQuery.setFirstResult(startPosition);
 91        }
 92        if (maxResult != null)
 93        {
 94           findAllQuery.setMaxResults(maxResult);
 95        }
 96        final List<SectionAllocation> searchResults = findAllQuery.getResultList();
 97        final List<SectionAllocationDTO> results = new ArrayList<SectionAllocationDTO>();
 98        for (SectionAllocation searchResult : searchResults)
 99        {
100           SectionAllocationDTO dto = new SectionAllocationDTO(searchResult);
101           results.add(dto);
102        }
103        return results;
104     }
105  
106     @PUT
107     @Path("/{id:[0-9][0-9]*}")
108     @Consumes("application/json")
109     public Response update(@PathParam("id") Long id, SectionAllocationDTO dto)
110     {
111        TypedQuery<SectionAllocation> findByIdQuery = em.createQuery("SELECT DISTINCT s FROM SectionAllocation s LEFT JOIN FETCH s.performance LEFT JOIN FETCH s.section WHERE s.id = :entityId ORDER BY s.id", SectionAllocation.class);
112        findByIdQuery.setParameter("entityId", id);
113        SectionAllocation entity;
114        try
115        {
116           entity = findByIdQuery.getSingleResult();
117        }
118        catch (NoResultException nre)
119        {
120           entity = null;
121        }
122        entity = dto.fromDTO(entity, em);
123        try
124        {
125           entity = em.merge(entity);
126        }
127        catch (OptimisticLockException e)
128        {
129           return Response.status(Response.Status.CONFLICT).entity(e.getEntity()).build();
130        }
```
  * file:///tmp/source-code/backend-v2/src/main/java/org/jboss/examples/ticketmonster/rest/SectionEndpoint.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import java.util.ArrayList;
  4  import java.util.List;
  5  
  6  import javax.ejb.Stateless;
  7  import javax.persistence.EntityManager;
  8  import javax.persistence.NoResultException;
  9  import javax.persistence.OptimisticLockException;
 10  import javax.persistence.PersistenceContext;
 11  import javax.persistence.TypedQuery;
 12  import javax.ws.rs.Consumes;
 13  import javax.ws.rs.DELETE;
 14  import javax.ws.rs.GET;
 15  import javax.ws.rs.POST;
 16  import javax.ws.rs.PUT;
 17  import javax.ws.rs.Path;
 18  import javax.ws.rs.PathParam;
 19  import javax.ws.rs.Produces;
 20  import javax.ws.rs.QueryParam;
 21  import javax.ws.rs.core.Response;
 22  import javax.ws.rs.core.Response.Status;
 23  import javax.ws.rs.core.UriBuilder;
 24  import org.jboss.examples.ticketmonster.rest.dto.SectionDTO;
 25  import org.jboss.examples.ticketmonster.model.Section;
 26  
 27  /**
 28   * 
 29   */
 30  @Stateless
 31  @Path("/sections")
 32  public class SectionEndpoint
 33  {
 34     @PersistenceContext(unitName = "primary")
 35     private EntityManager em;
 36  
 37     @POST
 38     @Consumes("application/json")
 39     public Response create(SectionDTO dto)
 40     {
 41        Section entity = dto.fromDTO(null, em);
 42        em.persist(entity);
 43        return Response.created(UriBuilder.fromResource(SectionEndpoint.class).path(String.valueOf(entity.getId())).build()).build();
 44     }
 45  
 46     @DELETE
 47     @Path("/{id:[0-9][0-9]*}")
 48     public Response deleteById(@PathParam("id") Long id)
 49     {
 50        Section entity = em.find(Section.class, id);
 51        if (entity == null)
 52        {
 53           return Response.status(Status.NOT_FOUND).build();
 54        }
 55        em.remove(entity);
 56        return Response.noContent().build();
 57     }
 58  
 59     @GET
 60     @Path("/{id:[0-9][0-9]*}")
 61     @Produces("application/json")
 62     public Response findById(@PathParam("id") Long id)
 63     {
 64        TypedQuery<Section> findByIdQuery = em.createQuery("SELECT DISTINCT s FROM Section s LEFT JOIN FETCH s.venue WHERE s.id = :entityId ORDER BY s.id", Section.class);
 65        findByIdQuery.setParameter("entityId", id);
 66        Section entity;
 67        try
 68        {
 69           entity = findByIdQuery.getSingleResult();
 70        }
 71        catch (NoResultException nre)
 72        {
 73           entity = null;
 74        }
 75        if (entity == null)
 76        {
 77           return Response.status(Status.NOT_FOUND).build();
 78        }
 79        SectionDTO dto = new SectionDTO(entity);
 80        return Response.ok(dto).build();
 81     }
 82  
 83     @GET
 84     @Produces("application/json")
 85     public List<SectionDTO> listAll(@QueryParam("start") Integer startPosition, @QueryParam("max") Integer maxResult)
 86     {
 87        TypedQuery<Section> findAllQuery = em.createQuery("SELECT DISTINCT s FROM Section s LEFT JOIN FETCH s.venue ORDER BY s.id", Section.class);
 88        if (startPosition != null)
 89        {
 90           findAllQuery.setFirstResult(startPosition);
 91        }
 92        if (maxResult != null)
 93        {
 94           findAllQuery.setMaxResults(maxResult);
 95        }
 96        final List<Section> searchResults = findAllQuery.getResultList();
 97        final List<SectionDTO> results = new ArrayList<SectionDTO>();
 98        for (Section searchResult : searchResults)
 99        {
100           SectionDTO dto = new SectionDTO(searchResult);
101           results.add(dto);
102        }
103        return results;
104     }
105  
106     @PUT
107     @Path("/{id:[0-9][0-9]*}")
108     @Consumes("application/json")
109     public Response update(@PathParam("id") Long id, SectionDTO dto)
110     {
111        TypedQuery<Section> findByIdQuery = em.createQuery("SELECT DISTINCT s FROM Section s LEFT JOIN FETCH s.venue WHERE s.id = :entityId ORDER BY s.id", Section.class);
112        findByIdQuery.setParameter("entityId", id);
113        Section entity;
114        try
115        {
116           entity = findByIdQuery.getSingleResult();
117        }
118        catch (NoResultException nre)
119        {
120           entity = null;
121        }
122        entity = dto.fromDTO(entity, em);
123        try
124        {
125           entity = em.merge(entity);
126        }
127        catch (OptimisticLockException e)
128        {
129           return Response.status(Response.Status.CONFLICT).entity(e.getEntity()).build();
130        }
```
  * file:///tmp/source-code/backend-v2/src/main/java/org/jboss/examples/ticketmonster/rest/ShowEndpoint.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import java.util.ArrayList;
  4  import java.util.List;
  5  
  6  import javax.ejb.Stateless;
  7  import javax.persistence.EntityManager;
  8  import javax.persistence.NoResultException;
  9  import javax.persistence.OptimisticLockException;
 10  import javax.persistence.PersistenceContext;
 11  import javax.persistence.TypedQuery;
 12  import javax.ws.rs.Consumes;
 13  import javax.ws.rs.DELETE;
 14  import javax.ws.rs.GET;
 15  import javax.ws.rs.POST;
 16  import javax.ws.rs.PUT;
 17  import javax.ws.rs.Path;
 18  import javax.ws.rs.PathParam;
 19  import javax.ws.rs.Produces;
 20  import javax.ws.rs.QueryParam;
 21  import javax.ws.rs.core.Response;
 22  import javax.ws.rs.core.Response.Status;
 23  import javax.ws.rs.core.UriBuilder;
 24  import org.jboss.examples.ticketmonster.rest.dto.ShowDTO;
 25  import org.jboss.examples.ticketmonster.model.Show;
 26  
 27  /**
 28   * 
 29   */
 30  @Stateless
 31  @Path("forge/shows")
 32  public class ShowEndpoint
 33  {
 34     @PersistenceContext(unitName = "primary")
 35     private EntityManager em;
 36  
 37     @POST
 38     @Consumes("application/json")
 39     public Response create(ShowDTO dto)
 40     {
 41        Show entity = dto.fromDTO(null, em);
 42        em.persist(entity);
 43        return Response.created(UriBuilder.fromResource(ShowEndpoint.class).path(String.valueOf(entity.getId())).build()).build();
 44     }
 45  
 46     @DELETE
 47     @Path("/{id:[0-9][0-9]*}")
 48     public Response deleteById(@PathParam("id") Long id)
 49     {
 50        Show entity = em.find(Show.class, id);
 51        if (entity == null)
 52        {
 53           return Response.status(Status.NOT_FOUND).build();
 54        }
 55        em.remove(entity);
 56        return Response.noContent().build();
 57     }
 58  
 59     @GET
 60     @Path("/{id:[0-9][0-9]*}")
 61     @Produces("application/json")
 62     public Response findById(@PathParam("id") Long id)
 63     {
 64        TypedQuery<Show> findByIdQuery = em.createQuery("SELECT DISTINCT s FROM Show s LEFT JOIN FETCH s.event LEFT JOIN FETCH s.venue LEFT JOIN FETCH s.performances LEFT JOIN FETCH s.ticketPrices WHERE s.id = :entityId ORDER BY s.id", Show.class);
 65        findByIdQuery.setParameter("entityId", id);
 66        Show entity;
 67        try
 68        {
 69           entity = findByIdQuery.getSingleResult();
 70        }
 71        catch (NoResultException nre)
 72        {
 73           entity = null;
 74        }
 75        if (entity == null)
 76        {
 77           return Response.status(Status.NOT_FOUND).build();
 78        }
 79        ShowDTO dto = new ShowDTO(entity);
 80        return Response.ok(dto).build();
 81     }
 82  
 83     @GET
 84     @Produces("application/json")
 85     public List<ShowDTO> listAll(@QueryParam("start") Integer startPosition, @QueryParam("max") Integer maxResult)
 86     {
 87        TypedQuery<Show> findAllQuery = em.createQuery("SELECT DISTINCT s FROM Show s LEFT JOIN FETCH s.event LEFT JOIN FETCH s.venue LEFT JOIN FETCH s.performances LEFT JOIN FETCH s.ticketPrices ORDER BY s.id", Show.class);
 88        if (startPosition != null)
 89        {
 90           findAllQuery.setFirstResult(startPosition);
 91        }
 92        if (maxResult != null)
 93        {
 94           findAllQuery.setMaxResults(maxResult);
 95        }
 96        final List<Show> searchResults = findAllQuery.getResultList();
 97        final List<ShowDTO> results = new ArrayList<ShowDTO>();
 98        for (Show searchResult : searchResults)
 99        {
100           ShowDTO dto = new ShowDTO(searchResult);
101           results.add(dto);
102        }
103        return results;
104     }
105  
106     @PUT
107     @Path("/{id:[0-9][0-9]*}")
108     @Consumes("application/json")
109     public Response update(@PathParam("id") Long id, ShowDTO dto)
110     {
111        TypedQuery<Show> findByIdQuery = em.createQuery("SELECT DISTINCT s FROM Show s LEFT JOIN FETCH s.event LEFT JOIN FETCH s.venue LEFT JOIN FETCH s.performances LEFT JOIN FETCH s.ticketPrices WHERE s.id = :entityId ORDER BY s.id", Show.class);
112        findByIdQuery.setParameter("entityId", id);
113        Show entity;
114        try
115        {
116           entity = findByIdQuery.getSingleResult();
117        }
118        catch (NoResultException nre)
119        {
120           entity = null;
121        }
122        entity = dto.fromDTO(entity, em);
123        try
124        {
125           entity = em.merge(entity);
126        }
127        catch (OptimisticLockException e)
128        {
129           return Response.status(Response.Status.CONFLICT).entity(e.getEntity()).build();
130        }
```
  * file:///tmp/source-code/backend-v2/src/main/java/org/jboss/examples/ticketmonster/rest/ShowService.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import java.util.ArrayList;
  4  import java.util.List;
  5  
  6  import javax.ejb.Stateless;
  7  import javax.persistence.Query;
  8  import javax.persistence.criteria.CriteriaBuilder;
  9  import javax.persistence.criteria.Predicate;
 10  import javax.persistence.criteria.Root;
 11  import javax.ws.rs.GET;
 12  import javax.ws.rs.Path;
 13  import javax.ws.rs.PathParam;
 14  import javax.ws.rs.Produces;
 15  import javax.ws.rs.core.MediaType;
 16  import javax.ws.rs.core.MultivaluedMap;
 17  
 18  import org.jboss.examples.ticketmonster.model.Show;
 19  
 20  /**
 21   * @author Marius Bogoevici
 22   */
 23  @Path("/shows")
 24  /**
 25   * <p>
 26   *     This is a stateless service, we declare it as an EJB for transaction demarcation
 27   * </p>
 28   */
 29  @Stateless
 30  public class ShowService extends BaseEntityService<Show> {
 31  
 32      public ShowService() {
 33          super(Show.class);
 34      }
 35  
 36      @Override
 37      protected Predicate[] extractPredicates(MultivaluedMap<String,
 38              String> queryParameters,
 39              CriteriaBuilder criteriaBuilder,
 40              Root<Show> root) {
 41  
 42          List<Predicate> predicates = new ArrayList<Predicate>();
 43  
 44          if (queryParameters.containsKey("venue")) {
 45              String venue = queryParameters.getFirst("venue");
 46              predicates.add(criteriaBuilder.equal(root.get("venue").get("id"), venue));
 47          }
 48  
 49          if (queryParameters.containsKey("event")) {
 50              String event = queryParameters.getFirst("event");
 51              predicates.add(criteriaBuilder.equal(root.get("event").get("id"), event));
 52          }
 53          return predicates.toArray(new Predicate[]{});
 54      }
 55  
 56      @GET
 57      @Path("/performance/{performanceId:[0-9][0-9]*}")
 58      @Produces(MediaType.APPLICATION_JSON)
 59      public Show getShowByPerformance(@PathParam("performanceId") Long performanceId) {
 60          Query query = getEntityManager().createQuery("select s from Show s where exists(select p from Performance p where p.show = s and p.id = :performanceId)");
 61          query.setParameter("performanceId", performanceId);
 62          return (Show) query.getSingleResult();
 63      }
 64  }

```
  * file:///tmp/source-code/backend-v2/src/main/java/org/jboss/examples/ticketmonster/rest/TicketCategoryEndpoint.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import java.util.ArrayList;
  4  import java.util.List;
  5  
  6  import javax.ejb.Stateless;
  7  import javax.persistence.EntityManager;
  8  import javax.persistence.NoResultException;
  9  import javax.persistence.OptimisticLockException;
 10  import javax.persistence.PersistenceContext;
 11  import javax.persistence.TypedQuery;
 12  import javax.ws.rs.Consumes;
 13  import javax.ws.rs.DELETE;
 14  import javax.ws.rs.GET;
 15  import javax.ws.rs.POST;
 16  import javax.ws.rs.PUT;
 17  import javax.ws.rs.Path;
 18  import javax.ws.rs.PathParam;
 19  import javax.ws.rs.Produces;
 20  import javax.ws.rs.QueryParam;
 21  import javax.ws.rs.core.Response;
 22  import javax.ws.rs.core.Response.Status;
 23  import javax.ws.rs.core.UriBuilder;
 24  import org.jboss.examples.ticketmonster.rest.dto.TicketCategoryDTO;
 25  import org.jboss.examples.ticketmonster.model.TicketCategory;
 26  
 27  /**
 28   * 
 29   */
 30  @Stateless
 31  @Path("/ticketcategories")
 32  public class TicketCategoryEndpoint
 33  {
 34     @PersistenceContext(unitName = "primary")
 35     private EntityManager em;
 36  
 37     @POST
 38     @Consumes("application/json")
 39     public Response create(TicketCategoryDTO dto)
 40     {
 41        TicketCategory entity = dto.fromDTO(null, em);
 42        em.persist(entity);
 43        return Response.created(UriBuilder.fromResource(TicketCategoryEndpoint.class).path(String.valueOf(entity.getId())).build()).build();
 44     }
 45  
 46     @DELETE
 47     @Path("/{id:[0-9][0-9]*}")
 48     public Response deleteById(@PathParam("id") Long id)
 49     {
 50        TicketCategory entity = em.find(TicketCategory.class, id);
 51        if (entity == null)
 52        {
 53           return Response.status(Status.NOT_FOUND).build();
 54        }
 55        em.remove(entity);
 56        return Response.noContent().build();
 57     }
 58  
 59     @GET
 60     @Path("/{id:[0-9][0-9]*}")
 61     @Produces("application/json")
 62     public Response findById(@PathParam("id") Long id)
 63     {
 64        TypedQuery<TicketCategory> findByIdQuery = em.createQuery("SELECT DISTINCT t FROM TicketCategory t WHERE t.id = :entityId ORDER BY t.id", TicketCategory.class);
 65        findByIdQuery.setParameter("entityId", id);
 66        TicketCategory entity;
 67        try
 68        {
 69           entity = findByIdQuery.getSingleResult();
 70        }
 71        catch (NoResultException nre)
 72        {
 73           entity = null;
 74        }
 75        if (entity == null)
 76        {
 77           return Response.status(Status.NOT_FOUND).build();
 78        }
 79        TicketCategoryDTO dto = new TicketCategoryDTO(entity);
 80        return Response.ok(dto).build();
 81     }
 82  
 83     @GET
 84     @Produces("application/json")
 85     public List<TicketCategoryDTO> listAll(@QueryParam("start") Integer startPosition, @QueryParam("max") Integer maxResult)
 86     {
 87        TypedQuery<TicketCategory> findAllQuery = em.createQuery("SELECT DISTINCT t FROM TicketCategory t ORDER BY t.id", TicketCategory.class);
 88        if (startPosition != null)
 89        {
 90           findAllQuery.setFirstResult(startPosition);
 91        }
 92        if (maxResult != null)
 93        {
 94           findAllQuery.setMaxResults(maxResult);
 95        }
 96        final List<TicketCategory> searchResults = findAllQuery.getResultList();
 97        final List<TicketCategoryDTO> results = new ArrayList<TicketCategoryDTO>();
 98        for (TicketCategory searchResult : searchResults)
 99        {
100           TicketCategoryDTO dto = new TicketCategoryDTO(searchResult);
101           results.add(dto);
102        }
103        return results;
104     }
105  
106     @PUT
107     @Path("/{id:[0-9][0-9]*}")
108     @Consumes("application/json")
109     public Response update(@PathParam("id") Long id, TicketCategoryDTO dto)
110     {
111        TypedQuery<TicketCategory> findByIdQuery = em.createQuery("SELECT DISTINCT t FROM TicketCategory t WHERE t.id = :entityId ORDER BY t.id", TicketCategory.class);
112        findByIdQuery.setParameter("entityId", id);
113        TicketCategory entity;
114        try
115        {
116           entity = findByIdQuery.getSingleResult();
117        }
118        catch (NoResultException nre)
119        {
120           entity = null;
121        }
122        entity = dto.fromDTO(entity, em);
123        try
124        {
125           entity = em.merge(entity);
126        }
127        catch (OptimisticLockException e)
128        {
129           return Response.status(Response.Status.CONFLICT).entity(e.getEntity()).build();
130        }
```
  * file:///tmp/source-code/backend-v2/src/main/java/org/jboss/examples/ticketmonster/rest/TicketEndpoint.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import java.util.ArrayList;
  4  import java.util.List;
  5  
  6  import javax.ejb.Stateless;
  7  import javax.persistence.EntityManager;
  8  import javax.persistence.NoResultException;
  9  import javax.persistence.OptimisticLockException;
 10  import javax.persistence.PersistenceContext;
 11  import javax.persistence.TypedQuery;
 12  import javax.ws.rs.Consumes;
 13  import javax.ws.rs.DELETE;
 14  import javax.ws.rs.GET;
 15  import javax.ws.rs.POST;
 16  import javax.ws.rs.PUT;
 17  import javax.ws.rs.Path;
 18  import javax.ws.rs.PathParam;
 19  import javax.ws.rs.Produces;
 20  import javax.ws.rs.QueryParam;
 21  import javax.ws.rs.core.Response;
 22  import javax.ws.rs.core.Response.Status;
 23  import javax.ws.rs.core.UriBuilder;
 24  import org.jboss.examples.ticketmonster.rest.dto.TicketDTO;
 25  import org.jboss.examples.ticketmonster.model.Ticket;
 26  
 27  /**
 28   * 
 29   */
 30  @Stateless
 31  @Path("/tickets")
 32  public class TicketEndpoint
 33  {
 34     @PersistenceContext(unitName = "primary")
 35     private EntityManager em;
 36  
 37     @POST
 38     @Consumes("application/json")
 39     public Response create(TicketDTO dto)
 40     {
 41        Ticket entity = dto.fromDTO(null, em);
 42        em.persist(entity);
 43        return Response.created(UriBuilder.fromResource(TicketEndpoint.class).path(String.valueOf(entity.getId())).build()).build();
 44     }
 45  
 46     @DELETE
 47     @Path("/{id:[0-9][0-9]*}")
 48     public Response deleteById(@PathParam("id") Long id)
 49     {
 50        Ticket entity = em.find(Ticket.class, id);
 51        if (entity == null)
 52        {
 53           return Response.status(Status.NOT_FOUND).build();
 54        }
 55        em.remove(entity);
 56        return Response.noContent().build();
 57     }
 58  
 59     @GET
 60     @Path("/{id:[0-9][0-9]*}")
 61     @Produces("application/json")
 62     public Response findById(@PathParam("id") Long id)
 63     {
 64        TypedQuery<Ticket> findByIdQuery = em.createQuery("SELECT DISTINCT t FROM Ticket t LEFT JOIN FETCH t.ticketCategory WHERE t.id = :entityId ORDER BY t.id", Ticket.class);
 65        findByIdQuery.setParameter("entityId", id);
 66        Ticket entity;
 67        try
 68        {
 69           entity = findByIdQuery.getSingleResult();
 70        }
 71        catch (NoResultException nre)
 72        {
 73           entity = null;
 74        }
 75        if (entity == null)
 76        {
 77           return Response.status(Status.NOT_FOUND).build();
 78        }
 79        TicketDTO dto = new TicketDTO(entity);
 80        return Response.ok(dto).build();
 81     }
 82  
 83     @GET
 84     @Produces("application/json")
 85     public List<TicketDTO> listAll(@QueryParam("start") Integer startPosition, @QueryParam("max") Integer maxResult)
 86     {
 87        TypedQuery<Ticket> findAllQuery = em.createQuery("SELECT DISTINCT t FROM Ticket t LEFT JOIN FETCH t.ticketCategory ORDER BY t.id", Ticket.class);
 88        if (startPosition != null)
 89        {
 90           findAllQuery.setFirstResult(startPosition);
 91        }
 92        if (maxResult != null)
 93        {
 94           findAllQuery.setMaxResults(maxResult);
 95        }
 96        final List<Ticket> searchResults = findAllQuery.getResultList();
 97        final List<TicketDTO> results = new ArrayList<TicketDTO>();
 98        for (Ticket searchResult : searchResults)
 99        {
100           TicketDTO dto = new TicketDTO(searchResult);
101           results.add(dto);
102        }
103        return results;
104     }
105  
106     @PUT
107     @Path("/{id:[0-9][0-9]*}")
108     @Consumes("application/json")
109     public Response update(@PathParam("id") Long id, TicketDTO dto)
110     {
111        TypedQuery<Ticket> findByIdQuery = em.createQuery("SELECT DISTINCT t FROM Ticket t LEFT JOIN FETCH t.ticketCategory WHERE t.id = :entityId ORDER BY t.id", Ticket.class);
112        findByIdQuery.setParameter("entityId", id);
113        Ticket entity;
114        try
115        {
116           entity = findByIdQuery.getSingleResult();
117        }
118        catch (NoResultException nre)
119        {
120           entity = null;
121        }
122        entity = dto.fromDTO(entity, em);
123        try
124        {
125           entity = em.merge(entity);
126        }
127        catch (OptimisticLockException e)
128        {
129           return Response.status(Response.Status.CONFLICT).entity(e.getEntity()).build();
130        }
```
  * file:///tmp/source-code/backend-v2/src/main/java/org/jboss/examples/ticketmonster/rest/TicketPriceEndpoint.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import java.util.ArrayList;
  4  import java.util.List;
  5  
  6  import javax.ejb.Stateless;
  7  import javax.persistence.EntityManager;
  8  import javax.persistence.NoResultException;
  9  import javax.persistence.OptimisticLockException;
 10  import javax.persistence.PersistenceContext;
 11  import javax.persistence.TypedQuery;
 12  import javax.ws.rs.Consumes;
 13  import javax.ws.rs.DELETE;
 14  import javax.ws.rs.GET;
 15  import javax.ws.rs.POST;
 16  import javax.ws.rs.PUT;
 17  import javax.ws.rs.Path;
 18  import javax.ws.rs.PathParam;
 19  import javax.ws.rs.Produces;
 20  import javax.ws.rs.QueryParam;
 21  import javax.ws.rs.core.Response;
 22  import javax.ws.rs.core.Response.Status;
 23  import javax.ws.rs.core.UriBuilder;
 24  import org.jboss.examples.ticketmonster.rest.dto.TicketPriceDTO;
 25  import org.jboss.examples.ticketmonster.model.TicketPrice;
 26  
 27  /**
 28   * 
 29   */
 30  @Stateless
 31  @Path("/ticketprices")
 32  public class TicketPriceEndpoint
 33  {
 34     @PersistenceContext(unitName = "primary")
 35     private EntityManager em;
 36  
 37     @POST
 38     @Consumes("application/json")
 39     public Response create(TicketPriceDTO dto)
 40     {
 41        TicketPrice entity = dto.fromDTO(null, em);
 42        em.persist(entity);
 43        return Response.created(UriBuilder.fromResource(TicketPriceEndpoint.class).path(String.valueOf(entity.getId())).build()).build();
 44     }
 45  
 46     @DELETE
 47     @Path("/{id:[0-9][0-9]*}")
 48     public Response deleteById(@PathParam("id") Long id)
 49     {
 50        TicketPrice entity = em.find(TicketPrice.class, id);
 51        if (entity == null)
 52        {
 53           return Response.status(Status.NOT_FOUND).build();
 54        }
 55        em.remove(entity);
 56        return Response.noContent().build();
 57     }
 58  
 59     @GET
 60     @Path("/{id:[0-9][0-9]*}")
 61     @Produces("application/json")
 62     public Response findById(@PathParam("id") Long id)
 63     {
 64        TypedQuery<TicketPrice> findByIdQuery = em.createQuery("SELECT DISTINCT t FROM TicketPrice t LEFT JOIN FETCH t.show LEFT JOIN FETCH t.section LEFT JOIN FETCH t.ticketCategory WHERE t.id = :entityId ORDER BY t.id", TicketPrice.class);
 65        findByIdQuery.setParameter("entityId", id);
 66        TicketPrice entity;
 67        try
 68        {
 69           entity = findByIdQuery.getSingleResult();
 70        }
 71        catch (NoResultException nre)
 72        {
 73           entity = null;
 74        }
 75        if (entity == null)
 76        {
 77           return Response.status(Status.NOT_FOUND).build();
 78        }
 79        TicketPriceDTO dto = new TicketPriceDTO(entity);
 80        return Response.ok(dto).build();
 81     }
 82  
 83     @GET
 84     @Produces("application/json")
 85     public List<TicketPriceDTO> listAll(@QueryParam("start") Integer startPosition, @QueryParam("max") Integer maxResult)
 86     {
 87        TypedQuery<TicketPrice> findAllQuery = em.createQuery("SELECT DISTINCT t FROM TicketPrice t LEFT JOIN FETCH t.show LEFT JOIN FETCH t.section LEFT JOIN FETCH t.ticketCategory ORDER BY t.id", TicketPrice.class);
 88        if (startPosition != null)
 89        {
 90           findAllQuery.setFirstResult(startPosition);
 91        }
 92        if (maxResult != null)
 93        {
 94           findAllQuery.setMaxResults(maxResult);
 95        }
 96        final List<TicketPrice> searchResults = findAllQuery.getResultList();
 97        final List<TicketPriceDTO> results = new ArrayList<TicketPriceDTO>();
 98        for (TicketPrice searchResult : searchResults)
 99        {
100           TicketPriceDTO dto = new TicketPriceDTO(searchResult);
101           results.add(dto);
102        }
103        return results;
104     }
105  
106     @PUT
107     @Path("/{id:[0-9][0-9]*}")
108     @Consumes("application/json")
109     public Response update(@PathParam("id") Long id, TicketPriceDTO dto)
110     {
111        TypedQuery<TicketPrice> findByIdQuery = em.createQuery("SELECT DISTINCT t FROM TicketPrice t LEFT JOIN FETCH t.show LEFT JOIN FETCH t.section LEFT JOIN FETCH t.ticketCategory WHERE t.id = :entityId ORDER BY t.id", TicketPrice.class);
112        findByIdQuery.setParameter("entityId", id);
113        TicketPrice entity;
114        try
115        {
116           entity = findByIdQuery.getSingleResult();
117        }
118        catch (NoResultException nre)
119        {
120           entity = null;
121        }
122        entity = dto.fromDTO(entity, em);
123        try
124        {
125           entity = em.merge(entity);
126        }
127        catch (OptimisticLockException e)
128        {
129           return Response.status(Response.Status.CONFLICT).entity(e.getEntity()).build();
130        }
```
  * file:///tmp/source-code/backend-v2/src/main/java/org/jboss/examples/ticketmonster/rest/VenueEndpoint.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import java.util.ArrayList;
  4  import java.util.List;
  5  
  6  import javax.ejb.Stateless;
  7  import javax.persistence.EntityManager;
  8  import javax.persistence.NoResultException;
  9  import javax.persistence.OptimisticLockException;
 10  import javax.persistence.PersistenceContext;
 11  import javax.persistence.TypedQuery;
 12  import javax.ws.rs.Consumes;
 13  import javax.ws.rs.DELETE;
 14  import javax.ws.rs.GET;
 15  import javax.ws.rs.POST;
 16  import javax.ws.rs.PUT;
 17  import javax.ws.rs.Path;
 18  import javax.ws.rs.PathParam;
 19  import javax.ws.rs.Produces;
 20  import javax.ws.rs.QueryParam;
 21  import javax.ws.rs.core.Response;
 22  import javax.ws.rs.core.Response.Status;
 23  import javax.ws.rs.core.UriBuilder;
 24  import org.jboss.examples.ticketmonster.rest.dto.VenueDTO;
 25  import org.jboss.examples.ticketmonster.model.Venue;
 26  
 27  /**
 28   * 
 29   */
 30  @Stateless
 31  @Path("forge/venues")
 32  public class VenueEndpoint
 33  {
 34     @PersistenceContext(unitName = "primary")
 35     private EntityManager em;
 36  
 37     @POST
 38     @Consumes("application/json")
 39     public Response create(VenueDTO dto)
 40     {
 41        Venue entity = dto.fromDTO(null, em);
 42        em.persist(entity);
 43        return Response.created(UriBuilder.fromResource(VenueEndpoint.class).path(String.valueOf(entity.getId())).build()).build();
 44     }
 45  
 46     @DELETE
 47     @Path("/{id:[0-9][0-9]*}")
 48     public Response deleteById(@PathParam("id") Long id)
 49     {
 50        Venue entity = em.find(Venue.class, id);
 51        if (entity == null)
 52        {
 53           return Response.status(Status.NOT_FOUND).build();
 54        }
 55        em.remove(entity);
 56        return Response.noContent().build();
 57     }
 58  
 59     @GET
 60     @Path("/{id:[0-9][0-9]*}")
 61     @Produces("application/json")
 62     public Response findById(@PathParam("id") Long id)
 63     {
 64        TypedQuery<Venue> findByIdQuery = em.createQuery("SELECT DISTINCT v FROM Venue v LEFT JOIN FETCH v.sections LEFT JOIN FETCH v.mediaItem WHERE v.id = :entityId ORDER BY v.id", Venue.class);
 65        findByIdQuery.setParameter("entityId", id);
 66        Venue entity;
 67        try
 68        {
 69           entity = findByIdQuery.getSingleResult();
 70        }
 71        catch (NoResultException nre)
 72        {
 73           entity = null;
 74        }
 75        if (entity == null)
 76        {
 77           return Response.status(Status.NOT_FOUND).build();
 78        }
 79        VenueDTO dto = new VenueDTO(entity);
 80        return Response.ok(dto).build();
 81     }
 82  
 83     @GET
 84     @Produces("application/json")
 85     public List<VenueDTO> listAll(@QueryParam("start") Integer startPosition, @QueryParam("max") Integer maxResult)
 86     {
 87        TypedQuery<Venue> findAllQuery = em.createQuery("SELECT DISTINCT v FROM Venue v LEFT JOIN FETCH v.sections LEFT JOIN FETCH v.mediaItem ORDER BY v.id", Venue.class);
 88        if (startPosition != null)
 89        {
 90           findAllQuery.setFirstResult(startPosition);
 91        }
 92        if (maxResult != null)
 93        {
 94           findAllQuery.setMaxResults(maxResult);
 95        }
 96        final List<Venue> searchResults = findAllQuery.getResultList();
 97        final List<VenueDTO> results = new ArrayList<VenueDTO>();
 98        for (Venue searchResult : searchResults)
 99        {
100           VenueDTO dto = new VenueDTO(searchResult);
101           results.add(dto);
102        }
103        return results;
104     }
105  
106     @PUT
107     @Path("/{id:[0-9][0-9]*}")
108     @Consumes("application/json")
109     public Response update(@PathParam("id") Long id, VenueDTO dto)
110     {
111        TypedQuery<Venue> findByIdQuery = em.createQuery("SELECT DISTINCT v FROM Venue v LEFT JOIN FETCH v.sections LEFT JOIN FETCH v.mediaItem WHERE v.id = :entityId ORDER BY v.id", Venue.class);
112        findByIdQuery.setParameter("entityId", id);
113        Venue entity;
114        try
115        {
116           entity = findByIdQuery.getSingleResult();
117        }
118        catch (NoResultException nre)
119        {
120           entity = null;
121        }
122        entity = dto.fromDTO(entity, em);
123        try
124        {
125           entity = em.merge(entity);
126        }
127        catch (OptimisticLockException e)
128        {
129           return Response.status(Response.Status.CONFLICT).entity(e.getEntity()).build();
130        }
```
  * file:///tmp/source-code/backend-v2/src/main/java/org/jboss/examples/ticketmonster/rest/VenueService.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import javax.ejb.Stateless;
  4  import javax.ws.rs.Path;
  5  
  6  import org.jboss.examples.ticketmonster.model.Venue;
  7  
  8  /**
  9   * <p>
 10   *     A JAX-RS endpoint for handling {@link Venue}s. Inherits the actual
 11   *     methods from {@link BaseEntityService}.
 12   * </p>
 13   *
 14   * @author Marius Bogoevici
 15   */
 16  @Path("/venues")
 17  /**
 18   * <p>
 19   *     This is a stateless service, we declare it as an EJB for transaction demarcation
 20   * </p>
 21   */
 22  @Stateless
 23  public class VenueService extends BaseEntityService<Venue> {
 24  
 25      public VenueService() {
 26          super(Venue.class);
 27      }
 28  
 29  }

```
  * file:///tmp/source-code/backend-v2/src/main/java/org/jboss/examples/ticketmonster/service/Bot.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.service;
  2  
  3  import java.util.ArrayList;
  4  import java.util.Collection;
  5  import java.util.Date;
  6  import java.util.List;
  7  import java.util.Map;
  8  import java.util.Random;
  9  import java.util.concurrent.TimeUnit;
 10  
 11  import javax.annotation.Resource;
 12  import javax.ejb.Stateless;
 13  import javax.ejb.Timeout;
 14  import javax.ejb.Timer;
 15  import javax.ejb.TimerConfig;
 16  import javax.ejb.TimerService;
 17  import javax.enterprise.event.Event;
 18  import javax.inject.Inject;
 19  import javax.ws.rs.core.MultivaluedHashMap;
 20  import javax.ws.rs.core.Response;
 21  
 22  import org.jboss.examples.ticketmonster.model.Performance;
 23  import org.jboss.examples.ticketmonster.model.Show;
 24  import org.jboss.examples.ticketmonster.model.TicketPrice;
 25  import org.jboss.examples.ticketmonster.rest.*;
 26  import org.jboss.examples.ticketmonster.util.qualifier.BotMessage;
 27  
 28  @Stateless
 29  public class Bot {
 30      
 31      private static final Random random = new Random(System.nanoTime());
 32      
 33      /** Frequency with which the bot will book **/
 34      public static final long DURATION = TimeUnit.SECONDS.toMillis(3);
 35      
 36      /** Maximum number of ticket requests that will be filed **/
 37      public static int MAX_TICKET_REQUESTS = 100;
 38      
 39      /** Maximum number of tickets per request **/
 40      public static int MAX_TICKETS_PER_REQUEST = 100;
 41      
 42      public static String [] BOOKERS = {"anne@acme.com", "george@acme.com", "william@acme.com", "victoria@acme.com", "edward@acme.com", "elizabeth@acme.com", "mary@acme.com", "charles@acme.com", "james@acme.com", "henry@acme.com", "richard@acme.com", "john@acme.com", "stephen@acme.com"}; 
 43  
 44      @Inject 
 45      private ShowService showService;
 46      
 47      @Inject
 48      private BookingService bookingService;
 49      
 50      @Inject @BotMessage
 51      Event<String> event;
 52      
 53      @Resource
 54      private TimerService timerService;
 55      
 56      public Timer start() {
 57          String startMessage = new StringBuilder("==========================\n")
 58                  .append("Bot started at ").append(new Date().toString()).append("\n")
 59                  .toString();
 60          event.fire(startMessage);
 61          return timerService.createIntervalTimer(0, DURATION, new TimerConfig(null, false));
 62      }
 63      
 64      public void stop(Timer timer) {
 65          String stopMessage = new StringBuilder("==========================\n")
 66                  .append("Bot stopped at ").append(new Date().toString()).append("\n")
 67                  .toString();
 68          event.fire(stopMessage);
 69          timer.cancel();
 70      }
 71      
 72      @Timeout
 73      public void book(Timer timer) {
 74          // Select a show at random
 75          Show show = selectAtRandom(showService.getAll(new MultivaluedHashMap<String, String>()));
 76  
 77          // Select a performance at random
 78          Performance performance = selectAtRandom(show.getPerformances());
 79          
 80          String requestor = selectAtRandom(BOOKERS);
 81  
 82          BookingRequest bookingRequest = new BookingRequest(performance, requestor);
 83  
 84          List<TicketPrice> possibleTicketPrices = new ArrayList<TicketPrice>(show.getTicketPrices());
 85          
 86          List<Integer> indicies = selectAtRandom(MAX_TICKET_REQUESTS < possibleTicketPrices.size() ? MAX_TICKET_REQUESTS : possibleTicketPrices.size());
 87          
 88          StringBuilder message = new StringBuilder("==========================\n")
 89          .append("Booking by ")
 90          .append(requestor)
 91          .append(" at ")
 92          .append(new Date().toString())
 93          .append("\n")
 94          .append(performance)
 95          .append("\n")
 96          .append("~~~~~~~~~~~~~~~~~~~~~~~~~\n");
 97          
 98          for (int index : indicies) {
 99              int no = random.nextInt(MAX_TICKETS_PER_REQUEST);
100              TicketPrice price = possibleTicketPrices.get(index);  
101              bookingRequest.addTicketRequest(new TicketRequest(price, no));
102              message
103                  .append(no)
104                  .append(" of ")
105                  .append(price.getSection())
106                  .append("\n");
107              
108          }
109          Response response = bookingService.createBooking(bookingRequest);
110          if(response.getStatus() == Response.Status.OK.getStatusCode()) {
111              message.append("SUCCESSFUL\n")
112                      .append("~~~~~~~~~~~~~~~~~~~~~~~~~\n");
113          }
114          else {
115              message.append("FAILED:\n")
116                          .append(((Map<String, Object>) response.getEntity()).get("errors"))
117                          .append("~~~~~~~~~~~~~~~~~~~~~~~~~\n");
118          }
119          event.fire(message.toString());
120      }
121      
122      
123      
124      private <T> T selectAtRandom(List<T> list) {
125          int i = random.nextInt(list.size());
126          return list.get(i);
127      }
128      
```
  * file:///tmp/source-code/monolith/src/main/java/org/jboss/examples/ticketmonster/rest/BookingEndpoint.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import java.util.ArrayList;
  4  import java.util.List;
  5  
  6  import javax.ejb.Stateless;
  7  import javax.persistence.EntityManager;
  8  import javax.persistence.NoResultException;
  9  import javax.persistence.OptimisticLockException;
 10  import javax.persistence.PersistenceContext;
 11  import javax.persistence.TypedQuery;
 12  import javax.ws.rs.Consumes;
 13  import javax.ws.rs.DELETE;
 14  import javax.ws.rs.GET;
 15  import javax.ws.rs.POST;
 16  import javax.ws.rs.PUT;
 17  import javax.ws.rs.Path;
 18  import javax.ws.rs.PathParam;
 19  import javax.ws.rs.Produces;
 20  import javax.ws.rs.QueryParam;
 21  import javax.ws.rs.core.Response;
 22  import javax.ws.rs.core.Response.Status;
 23  import javax.ws.rs.core.UriBuilder;
 24  import org.jboss.examples.ticketmonster.rest.dto.BookingDTO;
 25  import org.jboss.examples.ticketmonster.model.Booking;
 26  
 27  /**
 28   * 
 29   */
 30  @Stateless
 31  @Path("forge/bookings")
 32  public class BookingEndpoint
 33  {
 34     @PersistenceContext(unitName = "primary")
 35     private EntityManager em;
 36  
 37     @POST
 38     @Consumes("application/json")
 39     public Response create(BookingDTO dto)
 40     {
 41        Booking entity = dto.fromDTO(null, em);
 42        em.persist(entity);
 43        return Response.created(UriBuilder.fromResource(BookingEndpoint.class).path(String.valueOf(entity.getId())).build()).build();
 44     }
 45  
 46     @DELETE
 47     @Path("/{id:[0-9][0-9]*}")
 48     public Response deleteById(@PathParam("id") Long id)
 49     {
 50        Booking entity = em.find(Booking.class, id);
 51        if (entity == null)
 52        {
 53           return Response.status(Status.NOT_FOUND).build();
 54        }
 55        em.remove(entity);
 56        return Response.noContent().build();
 57     }
 58  
 59     @GET
 60     @Path("/{id:[0-9][0-9]*}")
 61     @Produces("application/json")
 62     public Response findById(@PathParam("id") Long id)
 63     {
 64        TypedQuery<Booking> findByIdQuery = em.createQuery("SELECT DISTINCT b FROM Booking b LEFT JOIN FETCH b.tickets LEFT JOIN FETCH b.performance WHERE b.id = :entityId ORDER BY b.id", Booking.class);
 65        findByIdQuery.setParameter("entityId", id);
 66        Booking entity;
 67        try
 68        {
 69           entity = findByIdQuery.getSingleResult();
 70        }
 71        catch (NoResultException nre)
 72        {
 73           entity = null;
 74        }
 75        if (entity == null)
 76        {
 77           return Response.status(Status.NOT_FOUND).build();
 78        }
 79        BookingDTO dto = new BookingDTO(entity);
 80        return Response.ok(dto).build();
 81     }
 82  
 83     @GET
 84     @Produces("application/json")
 85     public List<BookingDTO> listAll(@QueryParam("start") Integer startPosition, @QueryParam("max") Integer maxResult)
 86     {
 87        TypedQuery<Booking> findAllQuery = em.createQuery("SELECT DISTINCT b FROM Booking b LEFT JOIN FETCH b.tickets LEFT JOIN FETCH b.performance ORDER BY b.id", Booking.class);
 88        if (startPosition != null)
 89        {
 90           findAllQuery.setFirstResult(startPosition);
 91        }
 92        if (maxResult != null)
 93        {
 94           findAllQuery.setMaxResults(maxResult);
 95        }
 96        final List<Booking> searchResults = findAllQuery.getResultList();
 97        final List<BookingDTO> results = new ArrayList<BookingDTO>();
 98        for (Booking searchResult : searchResults)
 99        {
100           BookingDTO dto = new BookingDTO(searchResult);
101           results.add(dto);
102        }
103        return results;
104     }
105  
106     @PUT
107     @Path("/{id:[0-9][0-9]*}")
108     @Consumes("application/json")
109     public Response update(@PathParam("id") Long id, BookingDTO dto)
110     {
111        TypedQuery<Booking> findByIdQuery = em.createQuery("SELECT DISTINCT b FROM Booking b LEFT JOIN FETCH b.tickets LEFT JOIN FETCH b.performance WHERE b.id = :entityId ORDER BY b.id", Booking.class);
112        findByIdQuery.setParameter("entityId", id);
113        Booking entity;
114        try
115        {
116           entity = findByIdQuery.getSingleResult();
117        }
118        catch (NoResultException nre)
119        {
120           entity = null;
121        }
122        entity = dto.fromDTO(entity, em);
123        try
124        {
125           entity = em.merge(entity);
126        }
127        catch (OptimisticLockException e)
128        {
129           return Response.status(Response.Status.CONFLICT).entity(e.getEntity()).build();
130        }
```
  * file:///tmp/source-code/monolith/src/main/java/org/jboss/examples/ticketmonster/rest/BookingService.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import java.util.ArrayList;
  4  import java.util.Collections;
  5  import java.util.HashMap;
  6  import java.util.List;
  7  import java.util.Map;
  8  import java.util.Set;
  9  import java.util.TreeMap;
 10  
 11  import javax.ejb.Stateless;
 12  import javax.enterprise.event.Event;
 13  import javax.inject.Inject;
 14  import javax.validation.ConstraintViolation;
 15  import javax.validation.ConstraintViolationException;
 16  import javax.ws.rs.Consumes;
 17  import javax.ws.rs.DELETE;
 18  import javax.ws.rs.POST;
 19  import javax.ws.rs.Path;
 20  import javax.ws.rs.PathParam;
 21  import javax.ws.rs.core.MediaType;
 22  import javax.ws.rs.core.MultivaluedHashMap;
 23  import javax.ws.rs.core.Response;
 24  
 25  import org.jboss.examples.ticketmonster.model.Booking;
 26  import org.jboss.examples.ticketmonster.model.Performance;
 27  import org.jboss.examples.ticketmonster.model.Seat;
 28  import org.jboss.examples.ticketmonster.model.Section;
 29  import org.jboss.examples.ticketmonster.model.Ticket;
 30  import org.jboss.examples.ticketmonster.model.TicketCategory;
 31  import org.jboss.examples.ticketmonster.model.TicketPrice;
 32  import org.jboss.examples.ticketmonster.service.AllocatedSeats;
 33  import org.jboss.examples.ticketmonster.service.SeatAllocationService;
 34  import org.jboss.examples.ticketmonster.util.qualifier.Cancelled;
 35  import org.jboss.examples.ticketmonster.util.qualifier.Created;
 36  
 37  /**
 38   * <p>
 39   *     A JAX-RS endpoint for handling {@link Booking}s. Inherits the GET
 40   *     methods from {@link BaseEntityService}, and implements additional REST methods.
 41   * </p>
 42   *
 43   * @author Marius Bogoevici
 44   * @author Pete Muir
 45   */
 46  @Path("/bookings")
 47  /**
 48   * <p>
 49   *     This is a stateless service, we declare it as an EJB for transaction demarcation
 50   * </p>
 51   */
 52  @Stateless
 53  public class BookingService extends BaseEntityService<Booking> {
 54  
 55      @Inject
 56      SeatAllocationService seatAllocationService;
 57  
 58      @Inject @Cancelled
 59      private Event<Booking> cancelledBookingEvent;
 60  
 61      @Inject @Created
 62      private Event<Booking> newBookingEvent;
 63      
 64      public BookingService() {
 65          super(Booking.class);
 66      }
 67      
 68      @DELETE
 69      public Response deleteAllBookings() {
 70      	List<Booking> bookings = getAll(new MultivaluedHashMap<String, String>());
 71      	for (Booking booking : bookings) {
 72      		deleteBooking(booking.getId());
 73      	}
 74          return Response.noContent().build();
 75      }
 76  
 77      /**
 78       * <p>
 79       * Delete a booking by id
 80       * </p>
 81       * @param id
 82       * @return
 83       */
 84      @DELETE
 85      @Path("/{id:[0-9][0-9]*}")
 86      public Response deleteBooking(@PathParam("id") Long id) {
 87          Booking booking = getEntityManager().find(Booking.class, id);
 88          if (booking == null) {
 89              return Response.status(Response.Status.NOT_FOUND).build();
 90          }
 91          getEntityManager().remove(booking);
 92          // Group together seats by section so that we can deallocate them in a group
 93          Map<Section, List<Seat>> seatsBySection = new TreeMap<Section, java.util.List<Seat>>(SectionComparator.instance());
 94          for (Ticket ticket : booking.getTickets()) {
 95              List<Seat> seats = seatsBySection.get(ticket.getSeat().getSection());
 96              if (seats == null) {
 97                  seats = new ArrayList<Seat>();
 98                  seatsBySection.put(ticket.getSeat().getSection(), seats);
 99              }
100              seats.add(ticket.getSeat());
101          }
102          // Deallocate each section block
103          for (Map.Entry<Section, List<Seat>> sectionListEntry : seatsBySection.entrySet()) {
104              seatAllocationService.deallocateSeats( sectionListEntry.getKey(),
105                      booking.getPerformance(), sectionListEntry.getValue());
106          }
107          cancelledBookingEvent.fire(booking);
108          return Response.noContent().build();
109      }
110  
111      /**
112       * <p>
113       *   Create a booking. Data is contained in the bookingRequest object
114       * </p>
115       * @param bookingRequest
116       * @return
117       */
118      @POST
119      /**
120       * <p> Data is received in JSON format. For easy handling, it will be unmarshalled in the support
121       * {@link BookingRequest} class.
122       */
123      @Consumes(MediaType.APPLICATION_JSON)
124      public Response createBooking(BookingRequest bookingRequest) {
125          try {
126              // identify the ticket price categories in this request
127              Set<Long> priceCategoryIds = bookingRequest.getUniquePriceCategoryIds();
128              
129              // load the entities that make up this booking's relationships
130              Performance performance = getEntityManager().find(Performance.class, bookingRequest.getPerformance());
131  
132              // As we can have a mix of ticket types in a booking, we need to load all of them that are relevant, 
133              // id
134              Map<Long, TicketPrice> ticketPricesById = loadTicketPrices(priceCategoryIds);
135  
136              // Now, start to create the booking from the posted data
137              // Set the simple stuff first!
138              Booking booking = new Booking();
139              booking.setContactEmail(bookingRequest.getEmail());
140              booking.setPerformance(performance);
141              booking.setCancellationCode("abc");
142  
143              // Now, we iterate over each ticket that was requested, and organize them by section and category
144              // we want to allocate ticket requests that belong to the same section contiguously
145              Map<Section, Map<TicketCategory, TicketRequest>> ticketRequestsPerSection
146                      = new TreeMap<Section, java.util.Map<TicketCategory, TicketRequest>>(SectionComparator.instance());
147              for (TicketRequest ticketRequest : bookingRequest.getTicketRequests()) {
148                  final TicketPrice ticketPrice = ticketPricesById.get(ticketRequest.getTicketPrice());
149                  if (!ticketRequestsPerSection.containsKey(ticketPrice.getSection())) {
150                      ticketRequestsPerSection
151                              .put(ticketPrice.getSection(), new HashMap<TicketCategory, TicketRequest>());
152                  }
```
  * file:///tmp/source-code/monolith/src/main/java/org/jboss/examples/ticketmonster/rest/EventCategoryEndpoint.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import java.util.ArrayList;
  4  import java.util.List;
  5  
  6  import javax.ejb.Stateless;
  7  import javax.persistence.EntityManager;
  8  import javax.persistence.NoResultException;
  9  import javax.persistence.OptimisticLockException;
 10  import javax.persistence.PersistenceContext;
 11  import javax.persistence.TypedQuery;
 12  import javax.ws.rs.Consumes;
 13  import javax.ws.rs.DELETE;
 14  import javax.ws.rs.GET;
 15  import javax.ws.rs.POST;
 16  import javax.ws.rs.PUT;
 17  import javax.ws.rs.Path;
 18  import javax.ws.rs.PathParam;
 19  import javax.ws.rs.Produces;
 20  import javax.ws.rs.QueryParam;
 21  import javax.ws.rs.core.Response;
 22  import javax.ws.rs.core.Response.Status;
 23  import javax.ws.rs.core.UriBuilder;
 24  import org.jboss.examples.ticketmonster.rest.dto.EventCategoryDTO;
 25  import org.jboss.examples.ticketmonster.model.EventCategory;
 26  
 27  /**
 28   * 
 29   */
 30  @Stateless
 31  @Path("/eventcategories")
 32  public class EventCategoryEndpoint
 33  {
 34     @PersistenceContext(unitName = "primary")
 35     private EntityManager em;
 36  
 37     @POST
 38     @Consumes("application/json")
 39     public Response create(EventCategoryDTO dto)
 40     {
 41        EventCategory entity = dto.fromDTO(null, em);
 42        em.persist(entity);
 43        return Response.created(UriBuilder.fromResource(EventCategoryEndpoint.class).path(String.valueOf(entity.getId())).build()).build();
 44     }
 45  
 46     @DELETE
 47     @Path("/{id:[0-9][0-9]*}")
 48     public Response deleteById(@PathParam("id") Long id)
 49     {
 50        EventCategory entity = em.find(EventCategory.class, id);
 51        if (entity == null)
 52        {
 53           return Response.status(Status.NOT_FOUND).build();
 54        }
 55        em.remove(entity);
 56        return Response.noContent().build();
 57     }
 58  
 59     @GET
 60     @Path("/{id:[0-9][0-9]*}")
 61     @Produces("application/json")
 62     public Response findById(@PathParam("id") Long id)
 63     {
 64        TypedQuery<EventCategory> findByIdQuery = em.createQuery("SELECT DISTINCT e FROM EventCategory e WHERE e.id = :entityId ORDER BY e.id", EventCategory.class);
 65        findByIdQuery.setParameter("entityId", id);
 66        EventCategory entity;
 67        try
 68        {
 69           entity = findByIdQuery.getSingleResult();
 70        }
 71        catch (NoResultException nre)
 72        {
 73           entity = null;
 74        }
 75        if (entity == null)
 76        {
 77           return Response.status(Status.NOT_FOUND).build();
 78        }
 79        EventCategoryDTO dto = new EventCategoryDTO(entity);
 80        return Response.ok(dto).build();
 81     }
 82  
 83     @GET
 84     @Produces("application/json")
 85     public List<EventCategoryDTO> listAll(@QueryParam("start") Integer startPosition, @QueryParam("max") Integer maxResult)
 86     {
 87        TypedQuery<EventCategory> findAllQuery = em.createQuery("SELECT DISTINCT e FROM EventCategory e ORDER BY e.id", EventCategory.class);
 88        if (startPosition != null)
 89        {
 90           findAllQuery.setFirstResult(startPosition);
 91        }
 92        if (maxResult != null)
 93        {
 94           findAllQuery.setMaxResults(maxResult);
 95        }
 96        final List<EventCategory> searchResults = findAllQuery.getResultList();
 97        final List<EventCategoryDTO> results = new ArrayList<EventCategoryDTO>();
 98        for (EventCategory searchResult : searchResults)
 99        {
100           EventCategoryDTO dto = new EventCategoryDTO(searchResult);
101           results.add(dto);
102        }
103        return results;
104     }
105  
106     @PUT
107     @Path("/{id:[0-9][0-9]*}")
108     @Consumes("application/json")
109     public Response update(@PathParam("id") Long id, EventCategoryDTO dto)
110     {
111        TypedQuery<EventCategory> findByIdQuery = em.createQuery("SELECT DISTINCT e FROM EventCategory e WHERE e.id = :entityId ORDER BY e.id", EventCategory.class);
112        findByIdQuery.setParameter("entityId", id);
113        EventCategory entity;
114        try
115        {
116           entity = findByIdQuery.getSingleResult();
117        }
118        catch (NoResultException nre)
119        {
120           entity = null;
121        }
122        entity = dto.fromDTO(entity, em);
123        try
124        {
125           entity = em.merge(entity);
126        }
127        catch (OptimisticLockException e)
128        {
129           return Response.status(Response.Status.CONFLICT).entity(e.getEntity()).build();
130        }
```
  * file:///tmp/source-code/monolith/src/main/java/org/jboss/examples/ticketmonster/rest/EventEndpoint.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import java.util.ArrayList;
  4  import java.util.List;
  5  
  6  import javax.ejb.Stateless;
  7  import javax.persistence.EntityManager;
  8  import javax.persistence.NoResultException;
  9  import javax.persistence.OptimisticLockException;
 10  import javax.persistence.PersistenceContext;
 11  import javax.persistence.TypedQuery;
 12  import javax.ws.rs.Consumes;
 13  import javax.ws.rs.DELETE;
 14  import javax.ws.rs.GET;
 15  import javax.ws.rs.POST;
 16  import javax.ws.rs.PUT;
 17  import javax.ws.rs.Path;
 18  import javax.ws.rs.PathParam;
 19  import javax.ws.rs.Produces;
 20  import javax.ws.rs.QueryParam;
 21  import javax.ws.rs.core.Response;
 22  import javax.ws.rs.core.Response.Status;
 23  import javax.ws.rs.core.UriBuilder;
 24  import org.jboss.examples.ticketmonster.rest.dto.EventDTO;
 25  import org.jboss.examples.ticketmonster.model.Event;
 26  
 27  /**
 28   * 
 29   */
 30  @Stateless
 31  @Path("forge/events")
 32  public class EventEndpoint
 33  {
 34     @PersistenceContext(unitName = "primary")
 35     private EntityManager em;
 36  
 37     @POST
 38     @Consumes("application/json")
 39     public Response create(EventDTO dto)
 40     {
 41        Event entity = dto.fromDTO(null, em);
 42        em.persist(entity);
 43        return Response.created(UriBuilder.fromResource(EventEndpoint.class).path(String.valueOf(entity.getId())).build()).build();
 44     }
 45  
 46     @DELETE
 47     @Path("/{id:[0-9][0-9]*}")
 48     public Response deleteById(@PathParam("id") Long id)
 49     {
 50        Event entity = em.find(Event.class, id);
 51        if (entity == null)
 52        {
 53           return Response.status(Status.NOT_FOUND).build();
 54        }
 55        em.remove(entity);
 56        return Response.noContent().build();
 57     }
 58  
 59     @GET
 60     @Path("/{id:[0-9][0-9]*}")
 61     @Produces("application/json")
 62     public Response findById(@PathParam("id") Long id)
 63     {
 64        TypedQuery<Event> findByIdQuery = em.createQuery("SELECT DISTINCT e FROM Event e LEFT JOIN FETCH e.mediaItem LEFT JOIN FETCH e.category WHERE e.id = :entityId ORDER BY e.id", Event.class);
 65        findByIdQuery.setParameter("entityId", id);
 66        Event entity;
 67        try
 68        {
 69           entity = findByIdQuery.getSingleResult();
 70        }
 71        catch (NoResultException nre)
 72        {
 73           entity = null;
 74        }
 75        if (entity == null)
 76        {
 77           return Response.status(Status.NOT_FOUND).build();
 78        }
 79        EventDTO dto = new EventDTO(entity);
 80        return Response.ok(dto).build();
 81     }
 82  
 83     @GET
 84     @Produces("application/json")
 85     public List<EventDTO> listAll(@QueryParam("start") Integer startPosition, @QueryParam("max") Integer maxResult)
 86     {
 87        TypedQuery<Event> findAllQuery = em.createQuery("SELECT DISTINCT e FROM Event e LEFT JOIN FETCH e.mediaItem LEFT JOIN FETCH e.category ORDER BY e.id", Event.class);
 88        if (startPosition != null)
 89        {
 90           findAllQuery.setFirstResult(startPosition);
 91        }
 92        if (maxResult != null)
 93        {
 94           findAllQuery.setMaxResults(maxResult);
 95        }
 96        final List<Event> searchResults = findAllQuery.getResultList();
 97        final List<EventDTO> results = new ArrayList<EventDTO>();
 98        for (Event searchResult : searchResults)
 99        {
100           EventDTO dto = new EventDTO(searchResult);
101           results.add(dto);
102        }
103        return results;
104     }
105  
106     @PUT
107     @Path("/{id:[0-9][0-9]*}")
108     @Consumes("application/json")
109     public Response update(@PathParam("id") Long id, EventDTO dto)
110     {
111        TypedQuery<Event> findByIdQuery = em.createQuery("SELECT DISTINCT e FROM Event e LEFT JOIN FETCH e.mediaItem LEFT JOIN FETCH e.category WHERE e.id = :entityId ORDER BY e.id", Event.class);
112        findByIdQuery.setParameter("entityId", id);
113        Event entity;
114        try
115        {
116           entity = findByIdQuery.getSingleResult();
117        }
118        catch (NoResultException nre)
119        {
120           entity = null;
121        }
122        entity = dto.fromDTO(entity, em);
123        try
124        {
125           entity = em.merge(entity);
126        }
127        catch (OptimisticLockException e)
128        {
129           return Response.status(Response.Status.CONFLICT).entity(e.getEntity()).build();
130        }
```
  * file:///tmp/source-code/monolith/src/main/java/org/jboss/examples/ticketmonster/rest/EventService.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import java.util.ArrayList;
  4  import java.util.List;
  5  
  6  import javax.ejb.Stateless;
  7  import javax.persistence.criteria.CriteriaBuilder;
  8  import javax.persistence.criteria.Predicate;
  9  import javax.persistence.criteria.Root;
 10  import javax.ws.rs.Path;
 11  import javax.ws.rs.core.MultivaluedMap;
 12  
 13  import org.jboss.examples.ticketmonster.model.Event;
 14  
 15  /**
 16   * <p>
 17   *     A JAX-RS endpoint for handling {@link Event}s. Inherits the actual
 18   *     methods from {@link BaseEntityService}, but implements additional search
 19   *     criteria.
 20   * </p>
 21   *
 22   * @author Marius Bogoevici
 23   */
 24  @Path("/events")
 25  /**
 26   * <p>
 27   *     This is a stateless service, we declare it as an EJB for transaction demarcation
 28   * </p>
 29   */
 30  @Stateless
 31  public class EventService extends BaseEntityService<Event> {
 32  
 33      public EventService() {
 34          super(Event.class);
 35      }
 36  
 37      /**
 38       * <p>
 39       *    We override the method from parent in order to add support for additional search
 40       *    criteria for events.
 41       * </p>
 42       * @param queryParameters - the HTTP query parameters received by the endpoint
 43       * @param criteriaBuilder - @{link CriteriaBuilder} used by the invoker
 44       * @param root  @{link Root} used by the invoker
 45       * @return
 46       */
 47      @Override
 48      protected Predicate[] extractPredicates(
 49              MultivaluedMap<String, String> queryParameters, 
 50              CriteriaBuilder criteriaBuilder, 
 51              Root<Event> root) {
 52          List<Predicate> predicates = new ArrayList<Predicate>() ;
 53          
 54          if (queryParameters.containsKey("category")) {
 55              String category = queryParameters.getFirst("category");
 56              predicates.add(criteriaBuilder.equal(root.get("category").get("id"), category));
 57          }
 58          
 59          return predicates.toArray(new Predicate[]{});
 60      }
 61  }

```
  * file:///tmp/source-code/monolith/src/main/java/org/jboss/examples/ticketmonster/rest/MediaItemEndpoint.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import java.util.ArrayList;
  4  import java.util.List;
  5  
  6  import javax.ejb.Stateless;
  7  import javax.persistence.EntityManager;
  8  import javax.persistence.NoResultException;
  9  import javax.persistence.OptimisticLockException;
 10  import javax.persistence.PersistenceContext;
 11  import javax.persistence.TypedQuery;
 12  import javax.ws.rs.Consumes;
 13  import javax.ws.rs.DELETE;
 14  import javax.ws.rs.GET;
 15  import javax.ws.rs.POST;
 16  import javax.ws.rs.PUT;
 17  import javax.ws.rs.Path;
 18  import javax.ws.rs.PathParam;
 19  import javax.ws.rs.Produces;
 20  import javax.ws.rs.QueryParam;
 21  import javax.ws.rs.core.Response;
 22  import javax.ws.rs.core.Response.Status;
 23  import javax.ws.rs.core.UriBuilder;
 24  import org.jboss.examples.ticketmonster.rest.dto.MediaItemDTO;
 25  import org.jboss.examples.ticketmonster.model.MediaItem;
 26  
 27  /**
 28   * 
 29   */
 30  @Stateless
 31  @Path("/mediaitems")
 32  public class MediaItemEndpoint
 33  {
 34     @PersistenceContext(unitName = "primary")
 35     private EntityManager em;
 36  
 37     @POST
 38     @Consumes("application/json")
 39     public Response create(MediaItemDTO dto)
 40     {
 41        MediaItem entity = dto.fromDTO(null, em);
 42        em.persist(entity);
 43        return Response.created(UriBuilder.fromResource(MediaItemEndpoint.class).path(String.valueOf(entity.getId())).build()).build();
 44     }
 45  
 46     @DELETE
 47     @Path("/{id:[0-9][0-9]*}")
 48     public Response deleteById(@PathParam("id") Long id)
 49     {
 50        MediaItem entity = em.find(MediaItem.class, id);
 51        if (entity == null)
 52        {
 53           return Response.status(Status.NOT_FOUND).build();
 54        }
 55        em.remove(entity);
 56        return Response.noContent().build();
 57     }
 58  
 59     @GET
 60     @Path("/{id:[0-9][0-9]*}")
 61     @Produces("application/json")
 62     public Response findById(@PathParam("id") Long id)
 63     {
 64        TypedQuery<MediaItem> findByIdQuery = em.createQuery("SELECT DISTINCT m FROM MediaItem m WHERE m.id = :entityId ORDER BY m.id", MediaItem.class);
 65        findByIdQuery.setParameter("entityId", id);
 66        MediaItem entity;
 67        try
 68        {
 69           entity = findByIdQuery.getSingleResult();
 70        }
 71        catch (NoResultException nre)
 72        {
 73           entity = null;
 74        }
 75        if (entity == null)
 76        {
 77           return Response.status(Status.NOT_FOUND).build();
 78        }
 79        MediaItemDTO dto = new MediaItemDTO(entity);
 80        return Response.ok(dto).build();
 81     }
 82  
 83     @GET
 84     @Produces("application/json")
 85     public List<MediaItemDTO> listAll(@QueryParam("start") Integer startPosition, @QueryParam("max") Integer maxResult)
 86     {
 87        TypedQuery<MediaItem> findAllQuery = em.createQuery("SELECT DISTINCT m FROM MediaItem m ORDER BY m.id", MediaItem.class);
 88        if (startPosition != null)
 89        {
 90           findAllQuery.setFirstResult(startPosition);
 91        }
 92        if (maxResult != null)
 93        {
 94           findAllQuery.setMaxResults(maxResult);
 95        }
 96        final List<MediaItem> searchResults = findAllQuery.getResultList();
 97        final List<MediaItemDTO> results = new ArrayList<MediaItemDTO>();
 98        for (MediaItem searchResult : searchResults)
 99        {
100           MediaItemDTO dto = new MediaItemDTO(searchResult);
101           results.add(dto);
102        }
103        return results;
104     }
105  
106     @PUT
107     @Path("/{id:[0-9][0-9]*}")
108     @Consumes("application/json")
109     public Response update(@PathParam("id") Long id, MediaItemDTO dto)
110     {
111        TypedQuery<MediaItem> findByIdQuery = em.createQuery("SELECT DISTINCT m FROM MediaItem m WHERE m.id = :entityId ORDER BY m.id", MediaItem.class);
112        findByIdQuery.setParameter("entityId", id);
113        MediaItem entity;
114        try
115        {
116           entity = findByIdQuery.getSingleResult();
117        }
118        catch (NoResultException nre)
119        {
120           entity = null;
121        }
122        entity = dto.fromDTO(entity, em);
123        try
124        {
125           entity = em.merge(entity);
126        }
127        catch (OptimisticLockException e)
128        {
129           return Response.status(Response.Status.CONFLICT).entity(e.getEntity()).build();
130        }
```
  * file:///tmp/source-code/monolith/src/main/java/org/jboss/examples/ticketmonster/rest/MetricsService.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import java.util.*;
  4  
  5  import javax.ejb.Stateless;
  6  import javax.inject.Inject;
  7  import javax.persistence.EntityManager;
  8  import javax.persistence.Query;
  9  import javax.persistence.TypedQuery;
 10  import javax.ws.rs.GET;
 11  import javax.ws.rs.Path;
 12  import javax.ws.rs.Produces;
 13  import javax.ws.rs.core.MediaType;
 14  
 15  import org.jboss.examples.ticketmonster.model.Show;
 16  
 17  /**
 18   * A read-only REST resource that provides a collection of metrics for shows occuring in the future. Updates to metrics via
 19   * POST/PUT etc. are not allowed, since they are not meant to be computed by consumers.
 20   * 
 21   * @author Vineet Reynolds
 22   * 
 23   */
 24  @Path("/metrics")
 25  @Stateless
 26  public class MetricsService {
 27  
 28      @Inject
 29      private EntityManager entityManager;
 30  
 31      /**
 32       * Retrieves a collection of metrics for Shows. Each metric in the collection contains
 33       * <ul>
 34       * <li>the show id,</li>
 35       * <li>the event name of the show,</li>
 36       * <li>the venue for the show,</li>
 37       * <li>the capacity for the venue</li>
 38       * <li>the performances for the show,
 39       * <ul>
 40       * <li>the timestamp for each performance,</li>
 41       * <li>the occupied count for each performance</li>
 42       * </ul>
 43       * </li>
 44       * </ul>
 45       * 
 46       * @return A JSON representation of metrics for shows.
 47       */
 48      @GET
 49      @Produces(MediaType.APPLICATION_JSON)
 50      public List<ShowMetric> getMetrics() {
 51          return retrieveMetricsFromShows(retrieveShows(),
 52              retrieveOccupiedCounts());
 53      }
 54  
 55      private List<ShowMetric> retrieveMetricsFromShows(List<Show> shows,
 56          Map<Long, Long> occupiedCounts) {
 57          List<ShowMetric> metrics = new ArrayList<ShowMetric>();
 58          for (Show show : shows) {
 59              metrics.add(new ShowMetric(show, occupiedCounts));
 60          }
 61          return metrics;
 62      }
 63  
 64      private List<Show> retrieveShows() {
 65          TypedQuery<Show> showQuery = entityManager
 66              .createQuery("select DISTINCT s from Show s JOIN s.performances p", Show.class);
 67          return showQuery.getResultList();
 68      }
 69  
 70      private Map<Long, Long> retrieveOccupiedCounts() {
 71          Map<Long, Long> occupiedCounts = new HashMap<Long, Long>();
 72  
 73          Query occupiedCountsQuery = entityManager
 74              .createQuery("select b.performance.id, SIZE(b.tickets) from Booking b "
 75                  + "GROUP BY b.performance.id");
 76  
 77          List<Object[]> results = occupiedCountsQuery.getResultList();
 78          for (Object[] result : results) {
 79              occupiedCounts.put((Long) result[0],
 80                  ((Integer) result[1]).longValue());
 81          }
 82  
 83          return occupiedCounts;
 84      }
 85  }

```
  * file:///tmp/source-code/monolith/src/main/java/org/jboss/examples/ticketmonster/rest/PerformanceEndpoint.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import java.util.ArrayList;
  4  import java.util.List;
  5  
  6  import javax.ejb.Stateless;
  7  import javax.persistence.EntityManager;
  8  import javax.persistence.NoResultException;
  9  import javax.persistence.OptimisticLockException;
 10  import javax.persistence.PersistenceContext;
 11  import javax.persistence.TypedQuery;
 12  import javax.persistence.criteria.CriteriaBuilder;
 13  import javax.persistence.criteria.CriteriaQuery;
 14  import javax.persistence.criteria.Predicate;
 15  import javax.persistence.criteria.Root;
 16  import javax.ws.rs.Consumes;
 17  import javax.ws.rs.DELETE;
 18  import javax.ws.rs.GET;
 19  import javax.ws.rs.POST;
 20  import javax.ws.rs.PUT;
 21  import javax.ws.rs.Path;
 22  import javax.ws.rs.PathParam;
 23  import javax.ws.rs.Produces;
 24  import javax.ws.rs.QueryParam;
 25  import javax.ws.rs.core.Response;
 26  import javax.ws.rs.core.Response.Status;
 27  import javax.ws.rs.core.UriBuilder;
 28  
 29  import org.jboss.examples.ticketmonster.rest.dto.PerformanceDTO;
 30  import org.jboss.examples.ticketmonster.model.Booking;
 31  import org.jboss.examples.ticketmonster.model.Performance;
 32  import org.jboss.examples.ticketmonster.model.SectionAllocation;
 33  import org.jboss.examples.ticketmonster.model.Show;
 34  
 35  /**
 36   * 
 37   */
 38  @Stateless
 39  @Path("/performances")
 40  public class PerformanceEndpoint
 41  {
 42     @PersistenceContext(unitName = "primary")
 43     private EntityManager em;
 44  
 45     @POST
 46     @Consumes("application/json")
 47     public Response create(PerformanceDTO dto)
 48     {
 49        Performance entity = dto.fromDTO(null, em);
 50        em.persist(entity);
 51        return Response.created(UriBuilder.fromResource(PerformanceEndpoint.class).path(String.valueOf(entity.getId())).build()).build();
 52     }
 53  
 54     @DELETE
 55     @Path("/{id:[0-9][0-9]*}")
 56     public Response deleteById(@PathParam("id") Long id)
 57     {
 58        Performance entity = em.find(Performance.class, id);
 59        if (entity == null)
 60        {
 61           return Response.status(Status.NOT_FOUND).build();
 62        }
 63        Show show = entity.getShow();
 64        show.getPerformances().remove(entity);
 65        entity.setShow(null);
 66        this.em.merge(show);
 67        List<SectionAllocation> sectionAllocations = findSectionAllocationsByPerformance(entity);
 68        for(SectionAllocation sectionAllocation: sectionAllocations) {
 69           this.em.remove(sectionAllocation);
 70        }
 71        List<Booking> bookings = findBookingsByPerformance(entity);
 72        for(Booking booking: bookings) {
 73           this.em.remove(booking);
 74        }
 75        em.remove(entity);
 76        return Response.noContent().build();
 77     }
 78  
 79     @GET
 80     @Path("/{id:[0-9][0-9]*}")
 81     @Produces("application/json")
 82     public Response findById(@PathParam("id") Long id)
 83     {
 84        TypedQuery<Performance> findByIdQuery = em.createQuery("SELECT DISTINCT p FROM Performance p LEFT JOIN FETCH p.show WHERE p.id = :entityId ORDER BY p.id", Performance.class);
 85        findByIdQuery.setParameter("entityId", id);
 86        Performance entity;
 87        try
 88        {
 89           entity = findByIdQuery.getSingleResult();
 90        }
 91        catch (NoResultException nre)
 92        {
 93           entity = null;
 94        }
 95        if (entity == null)
 96        {
 97           return Response.status(Status.NOT_FOUND).build();
 98        }
 99        PerformanceDTO dto = new PerformanceDTO(entity);
100        return Response.ok(dto).build();
101     }
102  
103     @GET
104     @Produces("application/json")
105     public List<PerformanceDTO> listAll(@QueryParam("start") Integer startPosition, @QueryParam("max") Integer maxResult)
106     {
107        TypedQuery<Performance> findAllQuery = em.createQuery("SELECT DISTINCT p FROM Performance p LEFT JOIN FETCH p.show ORDER BY p.id", Performance.class);
108        if (startPosition != null)
109        {
110           findAllQuery.setFirstResult(startPosition);
111        }
112        if (maxResult != null)
113        {
114           findAllQuery.setMaxResults(maxResult);
115        }
116        final List<Performance> searchResults = findAllQuery.getResultList();
117        final List<PerformanceDTO> results = new ArrayList<PerformanceDTO>();
118        for (Performance searchResult : searchResults)
119        {
120           PerformanceDTO dto = new PerformanceDTO(searchResult);
121           results.add(dto);
122        }
123        return results;
124     }
125  
126     @PUT
127     @Path("/{id:[0-9][0-9]*}")
128     @Consumes("application/json")
129     public Response update(@PathParam("id") Long id, PerformanceDTO dto)
130     {
131        TypedQuery<Performance> findByIdQuery = em.createQuery("SELECT DISTINCT p FROM Performance p LEFT JOIN FETCH p.show WHERE p.id = :entityId ORDER BY p.id", Performance.class);
132        findByIdQuery.setParameter("entityId", id);
133        Performance entity;
134        try
135        {
136           entity = findByIdQuery.getSingleResult();
137        }
138        catch (NoResultException nre)
```
  * file:///tmp/source-code/monolith/src/main/java/org/jboss/examples/ticketmonster/rest/SectionAllocationEndpoint.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import java.util.ArrayList;
  4  import java.util.List;
  5  
  6  import javax.ejb.Stateless;
  7  import javax.persistence.EntityManager;
  8  import javax.persistence.NoResultException;
  9  import javax.persistence.OptimisticLockException;
 10  import javax.persistence.PersistenceContext;
 11  import javax.persistence.TypedQuery;
 12  import javax.ws.rs.Consumes;
 13  import javax.ws.rs.DELETE;
 14  import javax.ws.rs.GET;
 15  import javax.ws.rs.POST;
 16  import javax.ws.rs.PUT;
 17  import javax.ws.rs.Path;
 18  import javax.ws.rs.PathParam;
 19  import javax.ws.rs.Produces;
 20  import javax.ws.rs.QueryParam;
 21  import javax.ws.rs.core.Response;
 22  import javax.ws.rs.core.Response.Status;
 23  import javax.ws.rs.core.UriBuilder;
 24  import org.jboss.examples.ticketmonster.rest.dto.SectionAllocationDTO;
 25  import org.jboss.examples.ticketmonster.model.SectionAllocation;
 26  
 27  /**
 28   * 
 29   */
 30  @Stateless
 31  @Path("/sectionallocations")
 32  public class SectionAllocationEndpoint
 33  {
 34     @PersistenceContext(unitName = "primary")
 35     private EntityManager em;
 36  
 37     @POST
 38     @Consumes("application/json")
 39     public Response create(SectionAllocationDTO dto)
 40     {
 41        SectionAllocation entity = dto.fromDTO(null, em);
 42        em.persist(entity);
 43        return Response.created(UriBuilder.fromResource(SectionAllocationEndpoint.class).path(String.valueOf(entity.getId())).build()).build();
 44     }
 45  
 46     @DELETE
 47     @Path("/{id:[0-9][0-9]*}")
 48     public Response deleteById(@PathParam("id") Long id)
 49     {
 50        SectionAllocation entity = em.find(SectionAllocation.class, id);
 51        if (entity == null)
 52        {
 53           return Response.status(Status.NOT_FOUND).build();
 54        }
 55        em.remove(entity);
 56        return Response.noContent().build();
 57     }
 58  
 59     @GET
 60     @Path("/{id:[0-9][0-9]*}")
 61     @Produces("application/json")
 62     public Response findById(@PathParam("id") Long id)
 63     {
 64        TypedQuery<SectionAllocation> findByIdQuery = em.createQuery("SELECT DISTINCT s FROM SectionAllocation s LEFT JOIN FETCH s.performance LEFT JOIN FETCH s.section WHERE s.id = :entityId ORDER BY s.id", SectionAllocation.class);
 65        findByIdQuery.setParameter("entityId", id);
 66        SectionAllocation entity;
 67        try
 68        {
 69           entity = findByIdQuery.getSingleResult();
 70        }
 71        catch (NoResultException nre)
 72        {
 73           entity = null;
 74        }
 75        if (entity == null)
 76        {
 77           return Response.status(Status.NOT_FOUND).build();
 78        }
 79        SectionAllocationDTO dto = new SectionAllocationDTO(entity);
 80        return Response.ok(dto).build();
 81     }
 82  
 83     @GET
 84     @Produces("application/json")
 85     public List<SectionAllocationDTO> listAll(@QueryParam("start") Integer startPosition, @QueryParam("max") Integer maxResult)
 86     {
 87        TypedQuery<SectionAllocation> findAllQuery = em.createQuery("SELECT DISTINCT s FROM SectionAllocation s LEFT JOIN FETCH s.performance LEFT JOIN FETCH s.section ORDER BY s.id", SectionAllocation.class);
 88        if (startPosition != null)
 89        {
 90           findAllQuery.setFirstResult(startPosition);
 91        }
 92        if (maxResult != null)
 93        {
 94           findAllQuery.setMaxResults(maxResult);
 95        }
 96        final List<SectionAllocation> searchResults = findAllQuery.getResultList();
 97        final List<SectionAllocationDTO> results = new ArrayList<SectionAllocationDTO>();
 98        for (SectionAllocation searchResult : searchResults)
 99        {
100           SectionAllocationDTO dto = new SectionAllocationDTO(searchResult);
101           results.add(dto);
102        }
103        return results;
104     }
105  
106     @PUT
107     @Path("/{id:[0-9][0-9]*}")
108     @Consumes("application/json")
109     public Response update(@PathParam("id") Long id, SectionAllocationDTO dto)
110     {
111        TypedQuery<SectionAllocation> findByIdQuery = em.createQuery("SELECT DISTINCT s FROM SectionAllocation s LEFT JOIN FETCH s.performance LEFT JOIN FETCH s.section WHERE s.id = :entityId ORDER BY s.id", SectionAllocation.class);
112        findByIdQuery.setParameter("entityId", id);
113        SectionAllocation entity;
114        try
115        {
116           entity = findByIdQuery.getSingleResult();
117        }
118        catch (NoResultException nre)
119        {
120           entity = null;
121        }
122        entity = dto.fromDTO(entity, em);
123        try
124        {
125           entity = em.merge(entity);
126        }
127        catch (OptimisticLockException e)
128        {
129           return Response.status(Response.Status.CONFLICT).entity(e.getEntity()).build();
130        }
```
  * file:///tmp/source-code/monolith/src/main/java/org/jboss/examples/ticketmonster/rest/SectionEndpoint.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import java.util.ArrayList;
  4  import java.util.List;
  5  
  6  import javax.ejb.Stateless;
  7  import javax.persistence.EntityManager;
  8  import javax.persistence.NoResultException;
  9  import javax.persistence.OptimisticLockException;
 10  import javax.persistence.PersistenceContext;
 11  import javax.persistence.TypedQuery;
 12  import javax.ws.rs.Consumes;
 13  import javax.ws.rs.DELETE;
 14  import javax.ws.rs.GET;
 15  import javax.ws.rs.POST;
 16  import javax.ws.rs.PUT;
 17  import javax.ws.rs.Path;
 18  import javax.ws.rs.PathParam;
 19  import javax.ws.rs.Produces;
 20  import javax.ws.rs.QueryParam;
 21  import javax.ws.rs.core.Response;
 22  import javax.ws.rs.core.Response.Status;
 23  import javax.ws.rs.core.UriBuilder;
 24  import org.jboss.examples.ticketmonster.rest.dto.SectionDTO;
 25  import org.jboss.examples.ticketmonster.model.Section;
 26  
 27  /**
 28   * 
 29   */
 30  @Stateless
 31  @Path("/sections")
 32  public class SectionEndpoint
 33  {
 34     @PersistenceContext(unitName = "primary")
 35     private EntityManager em;
 36  
 37     @POST
 38     @Consumes("application/json")
 39     public Response create(SectionDTO dto)
 40     {
 41        Section entity = dto.fromDTO(null, em);
 42        em.persist(entity);
 43        return Response.created(UriBuilder.fromResource(SectionEndpoint.class).path(String.valueOf(entity.getId())).build()).build();
 44     }
 45  
 46     @DELETE
 47     @Path("/{id:[0-9][0-9]*}")
 48     public Response deleteById(@PathParam("id") Long id)
 49     {
 50        Section entity = em.find(Section.class, id);
 51        if (entity == null)
 52        {
 53           return Response.status(Status.NOT_FOUND).build();
 54        }
 55        em.remove(entity);
 56        return Response.noContent().build();
 57     }
 58  
 59     @GET
 60     @Path("/{id:[0-9][0-9]*}")
 61     @Produces("application/json")
 62     public Response findById(@PathParam("id") Long id)
 63     {
 64        TypedQuery<Section> findByIdQuery = em.createQuery("SELECT DISTINCT s FROM Section s LEFT JOIN FETCH s.venue WHERE s.id = :entityId ORDER BY s.id", Section.class);
 65        findByIdQuery.setParameter("entityId", id);
 66        Section entity;
 67        try
 68        {
 69           entity = findByIdQuery.getSingleResult();
 70        }
 71        catch (NoResultException nre)
 72        {
 73           entity = null;
 74        }
 75        if (entity == null)
 76        {
 77           return Response.status(Status.NOT_FOUND).build();
 78        }
 79        SectionDTO dto = new SectionDTO(entity);
 80        return Response.ok(dto).build();
 81     }
 82  
 83     @GET
 84     @Produces("application/json")
 85     public List<SectionDTO> listAll(@QueryParam("start") Integer startPosition, @QueryParam("max") Integer maxResult)
 86     {
 87        TypedQuery<Section> findAllQuery = em.createQuery("SELECT DISTINCT s FROM Section s LEFT JOIN FETCH s.venue ORDER BY s.id", Section.class);
 88        if (startPosition != null)
 89        {
 90           findAllQuery.setFirstResult(startPosition);
 91        }
 92        if (maxResult != null)
 93        {
 94           findAllQuery.setMaxResults(maxResult);
 95        }
 96        final List<Section> searchResults = findAllQuery.getResultList();
 97        final List<SectionDTO> results = new ArrayList<SectionDTO>();
 98        for (Section searchResult : searchResults)
 99        {
100           SectionDTO dto = new SectionDTO(searchResult);
101           results.add(dto);
102        }
103        return results;
104     }
105  
106     @PUT
107     @Path("/{id:[0-9][0-9]*}")
108     @Consumes("application/json")
109     public Response update(@PathParam("id") Long id, SectionDTO dto)
110     {
111        TypedQuery<Section> findByIdQuery = em.createQuery("SELECT DISTINCT s FROM Section s LEFT JOIN FETCH s.venue WHERE s.id = :entityId ORDER BY s.id", Section.class);
112        findByIdQuery.setParameter("entityId", id);
113        Section entity;
114        try
115        {
116           entity = findByIdQuery.getSingleResult();
117        }
118        catch (NoResultException nre)
119        {
120           entity = null;
121        }
122        entity = dto.fromDTO(entity, em);
123        try
124        {
125           entity = em.merge(entity);
126        }
127        catch (OptimisticLockException e)
128        {
129           return Response.status(Response.Status.CONFLICT).entity(e.getEntity()).build();
130        }
```
  * file:///tmp/source-code/monolith/src/main/java/org/jboss/examples/ticketmonster/rest/ShowEndpoint.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import java.util.ArrayList;
  4  import java.util.List;
  5  
  6  import javax.ejb.Stateless;
  7  import javax.persistence.EntityManager;
  8  import javax.persistence.NoResultException;
  9  import javax.persistence.OptimisticLockException;
 10  import javax.persistence.PersistenceContext;
 11  import javax.persistence.TypedQuery;
 12  import javax.ws.rs.Consumes;
 13  import javax.ws.rs.DELETE;
 14  import javax.ws.rs.GET;
 15  import javax.ws.rs.POST;
 16  import javax.ws.rs.PUT;
 17  import javax.ws.rs.Path;
 18  import javax.ws.rs.PathParam;
 19  import javax.ws.rs.Produces;
 20  import javax.ws.rs.QueryParam;
 21  import javax.ws.rs.core.Response;
 22  import javax.ws.rs.core.Response.Status;
 23  import javax.ws.rs.core.UriBuilder;
 24  import org.jboss.examples.ticketmonster.rest.dto.ShowDTO;
 25  import org.jboss.examples.ticketmonster.model.Show;
 26  
 27  /**
 28   * 
 29   */
 30  @Stateless
 31  @Path("forge/shows")
 32  public class ShowEndpoint
 33  {
 34     @PersistenceContext(unitName = "primary")
 35     private EntityManager em;
 36  
 37     @POST
 38     @Consumes("application/json")
 39     public Response create(ShowDTO dto)
 40     {
 41        Show entity = dto.fromDTO(null, em);
 42        em.persist(entity);
 43        return Response.created(UriBuilder.fromResource(ShowEndpoint.class).path(String.valueOf(entity.getId())).build()).build();
 44     }
 45  
 46     @DELETE
 47     @Path("/{id:[0-9][0-9]*}")
 48     public Response deleteById(@PathParam("id") Long id)
 49     {
 50        Show entity = em.find(Show.class, id);
 51        if (entity == null)
 52        {
 53           return Response.status(Status.NOT_FOUND).build();
 54        }
 55        em.remove(entity);
 56        return Response.noContent().build();
 57     }
 58  
 59     @GET
 60     @Path("/{id:[0-9][0-9]*}")
 61     @Produces("application/json")
 62     public Response findById(@PathParam("id") Long id)
 63     {
 64        TypedQuery<Show> findByIdQuery = em.createQuery("SELECT DISTINCT s FROM Show s LEFT JOIN FETCH s.event LEFT JOIN FETCH s.venue LEFT JOIN FETCH s.performances LEFT JOIN FETCH s.ticketPrices WHERE s.id = :entityId ORDER BY s.id", Show.class);
 65        findByIdQuery.setParameter("entityId", id);
 66        Show entity;
 67        try
 68        {
 69           entity = findByIdQuery.getSingleResult();
 70        }
 71        catch (NoResultException nre)
 72        {
 73           entity = null;
 74        }
 75        if (entity == null)
 76        {
 77           return Response.status(Status.NOT_FOUND).build();
 78        }
 79        ShowDTO dto = new ShowDTO(entity);
 80        return Response.ok(dto).build();
 81     }
 82  
 83     @GET
 84     @Produces("application/json")
 85     public List<ShowDTO> listAll(@QueryParam("start") Integer startPosition, @QueryParam("max") Integer maxResult)
 86     {
 87        TypedQuery<Show> findAllQuery = em.createQuery("SELECT DISTINCT s FROM Show s LEFT JOIN FETCH s.event LEFT JOIN FETCH s.venue LEFT JOIN FETCH s.performances LEFT JOIN FETCH s.ticketPrices ORDER BY s.id", Show.class);
 88        if (startPosition != null)
 89        {
 90           findAllQuery.setFirstResult(startPosition);
 91        }
 92        if (maxResult != null)
 93        {
 94           findAllQuery.setMaxResults(maxResult);
 95        }
 96        final List<Show> searchResults = findAllQuery.getResultList();
 97        final List<ShowDTO> results = new ArrayList<ShowDTO>();
 98        for (Show searchResult : searchResults)
 99        {
100           ShowDTO dto = new ShowDTO(searchResult);
101           results.add(dto);
102        }
103        return results;
104     }
105  
106     @PUT
107     @Path("/{id:[0-9][0-9]*}")
108     @Consumes("application/json")
109     public Response update(@PathParam("id") Long id, ShowDTO dto)
110     {
111        TypedQuery<Show> findByIdQuery = em.createQuery("SELECT DISTINCT s FROM Show s LEFT JOIN FETCH s.event LEFT JOIN FETCH s.venue LEFT JOIN FETCH s.performances LEFT JOIN FETCH s.ticketPrices WHERE s.id = :entityId ORDER BY s.id", Show.class);
112        findByIdQuery.setParameter("entityId", id);
113        Show entity;
114        try
115        {
116           entity = findByIdQuery.getSingleResult();
117        }
118        catch (NoResultException nre)
119        {
120           entity = null;
121        }
122        entity = dto.fromDTO(entity, em);
123        try
124        {
125           entity = em.merge(entity);
126        }
127        catch (OptimisticLockException e)
128        {
129           return Response.status(Response.Status.CONFLICT).entity(e.getEntity()).build();
130        }
```
  * file:///tmp/source-code/monolith/src/main/java/org/jboss/examples/ticketmonster/rest/ShowService.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import java.util.ArrayList;
  4  import java.util.List;
  5  
  6  import javax.ejb.Stateless;
  7  import javax.persistence.Query;
  8  import javax.persistence.criteria.CriteriaBuilder;
  9  import javax.persistence.criteria.Predicate;
 10  import javax.persistence.criteria.Root;
 11  import javax.ws.rs.GET;
 12  import javax.ws.rs.Path;
 13  import javax.ws.rs.PathParam;
 14  import javax.ws.rs.Produces;
 15  import javax.ws.rs.core.MediaType;
 16  import javax.ws.rs.core.MultivaluedMap;
 17  
 18  import org.jboss.examples.ticketmonster.model.Show;
 19  
 20  /**
 21   * @author Marius Bogoevici
 22   */
 23  @Path("/shows")
 24  /**
 25   * <p>
 26   *     This is a stateless service, we declare it as an EJB for transaction demarcation
 27   * </p>
 28   */
 29  @Stateless
 30  public class ShowService extends BaseEntityService<Show> {
 31  
 32      public ShowService() {
 33          super(Show.class);
 34      }
 35  
 36      @Override
 37      protected Predicate[] extractPredicates(MultivaluedMap<String,
 38              String> queryParameters,
 39              CriteriaBuilder criteriaBuilder,
 40              Root<Show> root) {
 41  
 42          List<Predicate> predicates = new ArrayList<Predicate>();
 43  
 44          if (queryParameters.containsKey("venue")) {
 45              String venue = queryParameters.getFirst("venue");
 46              predicates.add(criteriaBuilder.equal(root.get("venue").get("id"), venue));
 47          }
 48  
 49          if (queryParameters.containsKey("event")) {
 50              String event = queryParameters.getFirst("event");
 51              predicates.add(criteriaBuilder.equal(root.get("event").get("id"), event));
 52          }
 53          return predicates.toArray(new Predicate[]{});
 54      }
 55  
 56      @GET
 57      @Path("/performance/{performanceId:[0-9][0-9]*}")
 58      @Produces(MediaType.APPLICATION_JSON)
 59      public Show getShowByPerformance(@PathParam("performanceId") Long performanceId) {
 60          Query query = getEntityManager().createQuery("select s from Show s where exists(select p from Performance p where p.show = s and p.id = :performanceId)");
 61          query.setParameter("performanceId", performanceId);
 62          return (Show) query.getSingleResult();
 63      }
 64  }

```
  * file:///tmp/source-code/monolith/src/main/java/org/jboss/examples/ticketmonster/rest/TicketCategoryEndpoint.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import java.util.ArrayList;
  4  import java.util.List;
  5  
  6  import javax.ejb.Stateless;
  7  import javax.persistence.EntityManager;
  8  import javax.persistence.NoResultException;
  9  import javax.persistence.OptimisticLockException;
 10  import javax.persistence.PersistenceContext;
 11  import javax.persistence.TypedQuery;
 12  import javax.ws.rs.Consumes;
 13  import javax.ws.rs.DELETE;
 14  import javax.ws.rs.GET;
 15  import javax.ws.rs.POST;
 16  import javax.ws.rs.PUT;
 17  import javax.ws.rs.Path;
 18  import javax.ws.rs.PathParam;
 19  import javax.ws.rs.Produces;
 20  import javax.ws.rs.QueryParam;
 21  import javax.ws.rs.core.Response;
 22  import javax.ws.rs.core.Response.Status;
 23  import javax.ws.rs.core.UriBuilder;
 24  import org.jboss.examples.ticketmonster.rest.dto.TicketCategoryDTO;
 25  import org.jboss.examples.ticketmonster.model.TicketCategory;
 26  
 27  /**
 28   * 
 29   */
 30  @Stateless
 31  @Path("/ticketcategories")
 32  public class TicketCategoryEndpoint
 33  {
 34     @PersistenceContext(unitName = "primary")
 35     private EntityManager em;
 36  
 37     @POST
 38     @Consumes("application/json")
 39     public Response create(TicketCategoryDTO dto)
 40     {
 41        TicketCategory entity = dto.fromDTO(null, em);
 42        em.persist(entity);
 43        return Response.created(UriBuilder.fromResource(TicketCategoryEndpoint.class).path(String.valueOf(entity.getId())).build()).build();
 44     }
 45  
 46     @DELETE
 47     @Path("/{id:[0-9][0-9]*}")
 48     public Response deleteById(@PathParam("id") Long id)
 49     {
 50        TicketCategory entity = em.find(TicketCategory.class, id);
 51        if (entity == null)
 52        {
 53           return Response.status(Status.NOT_FOUND).build();
 54        }
 55        em.remove(entity);
 56        return Response.noContent().build();
 57     }
 58  
 59     @GET
 60     @Path("/{id:[0-9][0-9]*}")
 61     @Produces("application/json")
 62     public Response findById(@PathParam("id") Long id)
 63     {
 64        TypedQuery<TicketCategory> findByIdQuery = em.createQuery("SELECT DISTINCT t FROM TicketCategory t WHERE t.id = :entityId ORDER BY t.id", TicketCategory.class);
 65        findByIdQuery.setParameter("entityId", id);
 66        TicketCategory entity;
 67        try
 68        {
 69           entity = findByIdQuery.getSingleResult();
 70        }
 71        catch (NoResultException nre)
 72        {
 73           entity = null;
 74        }
 75        if (entity == null)
 76        {
 77           return Response.status(Status.NOT_FOUND).build();
 78        }
 79        TicketCategoryDTO dto = new TicketCategoryDTO(entity);
 80        return Response.ok(dto).build();
 81     }
 82  
 83     @GET
 84     @Produces("application/json")
 85     public List<TicketCategoryDTO> listAll(@QueryParam("start") Integer startPosition, @QueryParam("max") Integer maxResult)
 86     {
 87        TypedQuery<TicketCategory> findAllQuery = em.createQuery("SELECT DISTINCT t FROM TicketCategory t ORDER BY t.id", TicketCategory.class);
 88        if (startPosition != null)
 89        {
 90           findAllQuery.setFirstResult(startPosition);
 91        }
 92        if (maxResult != null)
 93        {
 94           findAllQuery.setMaxResults(maxResult);
 95        }
 96        final List<TicketCategory> searchResults = findAllQuery.getResultList();
 97        final List<TicketCategoryDTO> results = new ArrayList<TicketCategoryDTO>();
 98        for (TicketCategory searchResult : searchResults)
 99        {
100           TicketCategoryDTO dto = new TicketCategoryDTO(searchResult);
101           results.add(dto);
102        }
103        return results;
104     }
105  
106     @PUT
107     @Path("/{id:[0-9][0-9]*}")
108     @Consumes("application/json")
109     public Response update(@PathParam("id") Long id, TicketCategoryDTO dto)
110     {
111        TypedQuery<TicketCategory> findByIdQuery = em.createQuery("SELECT DISTINCT t FROM TicketCategory t WHERE t.id = :entityId ORDER BY t.id", TicketCategory.class);
112        findByIdQuery.setParameter("entityId", id);
113        TicketCategory entity;
114        try
115        {
116           entity = findByIdQuery.getSingleResult();
117        }
118        catch (NoResultException nre)
119        {
120           entity = null;
121        }
122        entity = dto.fromDTO(entity, em);
123        try
124        {
125           entity = em.merge(entity);
126        }
127        catch (OptimisticLockException e)
128        {
129           return Response.status(Response.Status.CONFLICT).entity(e.getEntity()).build();
130        }
```
  * file:///tmp/source-code/monolith/src/main/java/org/jboss/examples/ticketmonster/rest/TicketEndpoint.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import java.util.ArrayList;
  4  import java.util.List;
  5  
  6  import javax.ejb.Stateless;
  7  import javax.persistence.EntityManager;
  8  import javax.persistence.NoResultException;
  9  import javax.persistence.OptimisticLockException;
 10  import javax.persistence.PersistenceContext;
 11  import javax.persistence.TypedQuery;
 12  import javax.ws.rs.Consumes;
 13  import javax.ws.rs.DELETE;
 14  import javax.ws.rs.GET;
 15  import javax.ws.rs.POST;
 16  import javax.ws.rs.PUT;
 17  import javax.ws.rs.Path;
 18  import javax.ws.rs.PathParam;
 19  import javax.ws.rs.Produces;
 20  import javax.ws.rs.QueryParam;
 21  import javax.ws.rs.core.Response;
 22  import javax.ws.rs.core.Response.Status;
 23  import javax.ws.rs.core.UriBuilder;
 24  import org.jboss.examples.ticketmonster.rest.dto.TicketDTO;
 25  import org.jboss.examples.ticketmonster.model.Ticket;
 26  
 27  /**
 28   * 
 29   */
 30  @Stateless
 31  @Path("/tickets")
 32  public class TicketEndpoint
 33  {
 34     @PersistenceContext(unitName = "primary")
 35     private EntityManager em;
 36  
 37     @POST
 38     @Consumes("application/json")
 39     public Response create(TicketDTO dto)
 40     {
 41        Ticket entity = dto.fromDTO(null, em);
 42        em.persist(entity);
 43        return Response.created(UriBuilder.fromResource(TicketEndpoint.class).path(String.valueOf(entity.getId())).build()).build();
 44     }
 45  
 46     @DELETE
 47     @Path("/{id:[0-9][0-9]*}")
 48     public Response deleteById(@PathParam("id") Long id)
 49     {
 50        Ticket entity = em.find(Ticket.class, id);
 51        if (entity == null)
 52        {
 53           return Response.status(Status.NOT_FOUND).build();
 54        }
 55        em.remove(entity);
 56        return Response.noContent().build();
 57     }
 58  
 59     @GET
 60     @Path("/{id:[0-9][0-9]*}")
 61     @Produces("application/json")
 62     public Response findById(@PathParam("id") Long id)
 63     {
 64        TypedQuery<Ticket> findByIdQuery = em.createQuery("SELECT DISTINCT t FROM Ticket t LEFT JOIN FETCH t.ticketCategory WHERE t.id = :entityId ORDER BY t.id", Ticket.class);
 65        findByIdQuery.setParameter("entityId", id);
 66        Ticket entity;
 67        try
 68        {
 69           entity = findByIdQuery.getSingleResult();
 70        }
 71        catch (NoResultException nre)
 72        {
 73           entity = null;
 74        }
 75        if (entity == null)
 76        {
 77           return Response.status(Status.NOT_FOUND).build();
 78        }
 79        TicketDTO dto = new TicketDTO(entity);
 80        return Response.ok(dto).build();
 81     }
 82  
 83     @GET
 84     @Produces("application/json")
 85     public List<TicketDTO> listAll(@QueryParam("start") Integer startPosition, @QueryParam("max") Integer maxResult)
 86     {
 87        TypedQuery<Ticket> findAllQuery = em.createQuery("SELECT DISTINCT t FROM Ticket t LEFT JOIN FETCH t.ticketCategory ORDER BY t.id", Ticket.class);
 88        if (startPosition != null)
 89        {
 90           findAllQuery.setFirstResult(startPosition);
 91        }
 92        if (maxResult != null)
 93        {
 94           findAllQuery.setMaxResults(maxResult);
 95        }
 96        final List<Ticket> searchResults = findAllQuery.getResultList();
 97        final List<TicketDTO> results = new ArrayList<TicketDTO>();
 98        for (Ticket searchResult : searchResults)
 99        {
100           TicketDTO dto = new TicketDTO(searchResult);
101           results.add(dto);
102        }
103        return results;
104     }
105  
106     @PUT
107     @Path("/{id:[0-9][0-9]*}")
108     @Consumes("application/json")
109     public Response update(@PathParam("id") Long id, TicketDTO dto)
110     {
111        TypedQuery<Ticket> findByIdQuery = em.createQuery("SELECT DISTINCT t FROM Ticket t LEFT JOIN FETCH t.ticketCategory WHERE t.id = :entityId ORDER BY t.id", Ticket.class);
112        findByIdQuery.setParameter("entityId", id);
113        Ticket entity;
114        try
115        {
116           entity = findByIdQuery.getSingleResult();
117        }
118        catch (NoResultException nre)
119        {
120           entity = null;
121        }
122        entity = dto.fromDTO(entity, em);
123        try
124        {
125           entity = em.merge(entity);
126        }
127        catch (OptimisticLockException e)
128        {
129           return Response.status(Response.Status.CONFLICT).entity(e.getEntity()).build();
130        }
```
  * file:///tmp/source-code/monolith/src/main/java/org/jboss/examples/ticketmonster/rest/TicketPriceEndpoint.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import java.util.ArrayList;
  4  import java.util.List;
  5  
  6  import javax.ejb.Stateless;
  7  import javax.persistence.EntityManager;
  8  import javax.persistence.NoResultException;
  9  import javax.persistence.OptimisticLockException;
 10  import javax.persistence.PersistenceContext;
 11  import javax.persistence.TypedQuery;
 12  import javax.ws.rs.Consumes;
 13  import javax.ws.rs.DELETE;
 14  import javax.ws.rs.GET;
 15  import javax.ws.rs.POST;
 16  import javax.ws.rs.PUT;
 17  import javax.ws.rs.Path;
 18  import javax.ws.rs.PathParam;
 19  import javax.ws.rs.Produces;
 20  import javax.ws.rs.QueryParam;
 21  import javax.ws.rs.core.Response;
 22  import javax.ws.rs.core.Response.Status;
 23  import javax.ws.rs.core.UriBuilder;
 24  import org.jboss.examples.ticketmonster.rest.dto.TicketPriceDTO;
 25  import org.jboss.examples.ticketmonster.model.TicketPrice;
 26  
 27  /**
 28   * 
 29   */
 30  @Stateless
 31  @Path("/ticketprices")
 32  public class TicketPriceEndpoint
 33  {
 34     @PersistenceContext(unitName = "primary")
 35     private EntityManager em;
 36  
 37     @POST
 38     @Consumes("application/json")
 39     public Response create(TicketPriceDTO dto)
 40     {
 41        TicketPrice entity = dto.fromDTO(null, em);
 42        em.persist(entity);
 43        return Response.created(UriBuilder.fromResource(TicketPriceEndpoint.class).path(String.valueOf(entity.getId())).build()).build();
 44     }
 45  
 46     @DELETE
 47     @Path("/{id:[0-9][0-9]*}")
 48     public Response deleteById(@PathParam("id") Long id)
 49     {
 50        TicketPrice entity = em.find(TicketPrice.class, id);
 51        if (entity == null)
 52        {
 53           return Response.status(Status.NOT_FOUND).build();
 54        }
 55        em.remove(entity);
 56        return Response.noContent().build();
 57     }
 58  
 59     @GET
 60     @Path("/{id:[0-9][0-9]*}")
 61     @Produces("application/json")
 62     public Response findById(@PathParam("id") Long id)
 63     {
 64        TypedQuery<TicketPrice> findByIdQuery = em.createQuery("SELECT DISTINCT t FROM TicketPrice t LEFT JOIN FETCH t.show LEFT JOIN FETCH t.section LEFT JOIN FETCH t.ticketCategory WHERE t.id = :entityId ORDER BY t.id", TicketPrice.class);
 65        findByIdQuery.setParameter("entityId", id);
 66        TicketPrice entity;
 67        try
 68        {
 69           entity = findByIdQuery.getSingleResult();
 70        }
 71        catch (NoResultException nre)
 72        {
 73           entity = null;
 74        }
 75        if (entity == null)
 76        {
 77           return Response.status(Status.NOT_FOUND).build();
 78        }
 79        TicketPriceDTO dto = new TicketPriceDTO(entity);
 80        return Response.ok(dto).build();
 81     }
 82  
 83     @GET
 84     @Produces("application/json")
 85     public List<TicketPriceDTO> listAll(@QueryParam("start") Integer startPosition, @QueryParam("max") Integer maxResult)
 86     {
 87        TypedQuery<TicketPrice> findAllQuery = em.createQuery("SELECT DISTINCT t FROM TicketPrice t LEFT JOIN FETCH t.show LEFT JOIN FETCH t.section LEFT JOIN FETCH t.ticketCategory ORDER BY t.id", TicketPrice.class);
 88        if (startPosition != null)
 89        {
 90           findAllQuery.setFirstResult(startPosition);
 91        }
 92        if (maxResult != null)
 93        {
 94           findAllQuery.setMaxResults(maxResult);
 95        }
 96        final List<TicketPrice> searchResults = findAllQuery.getResultList();
 97        final List<TicketPriceDTO> results = new ArrayList<TicketPriceDTO>();
 98        for (TicketPrice searchResult : searchResults)
 99        {
100           TicketPriceDTO dto = new TicketPriceDTO(searchResult);
101           results.add(dto);
102        }
103        return results;
104     }
105  
106     @PUT
107     @Path("/{id:[0-9][0-9]*}")
108     @Consumes("application/json")
109     public Response update(@PathParam("id") Long id, TicketPriceDTO dto)
110     {
111        TypedQuery<TicketPrice> findByIdQuery = em.createQuery("SELECT DISTINCT t FROM TicketPrice t LEFT JOIN FETCH t.show LEFT JOIN FETCH t.section LEFT JOIN FETCH t.ticketCategory WHERE t.id = :entityId ORDER BY t.id", TicketPrice.class);
112        findByIdQuery.setParameter("entityId", id);
113        TicketPrice entity;
114        try
115        {
116           entity = findByIdQuery.getSingleResult();
117        }
118        catch (NoResultException nre)
119        {
120           entity = null;
121        }
122        entity = dto.fromDTO(entity, em);
123        try
124        {
125           entity = em.merge(entity);
126        }
127        catch (OptimisticLockException e)
128        {
129           return Response.status(Response.Status.CONFLICT).entity(e.getEntity()).build();
130        }
```
  * file:///tmp/source-code/monolith/src/main/java/org/jboss/examples/ticketmonster/rest/VenueEndpoint.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import java.util.ArrayList;
  4  import java.util.List;
  5  
  6  import javax.ejb.Stateless;
  7  import javax.persistence.EntityManager;
  8  import javax.persistence.NoResultException;
  9  import javax.persistence.OptimisticLockException;
 10  import javax.persistence.PersistenceContext;
 11  import javax.persistence.TypedQuery;
 12  import javax.ws.rs.Consumes;
 13  import javax.ws.rs.DELETE;
 14  import javax.ws.rs.GET;
 15  import javax.ws.rs.POST;
 16  import javax.ws.rs.PUT;
 17  import javax.ws.rs.Path;
 18  import javax.ws.rs.PathParam;
 19  import javax.ws.rs.Produces;
 20  import javax.ws.rs.QueryParam;
 21  import javax.ws.rs.core.Response;
 22  import javax.ws.rs.core.Response.Status;
 23  import javax.ws.rs.core.UriBuilder;
 24  import org.jboss.examples.ticketmonster.rest.dto.VenueDTO;
 25  import org.jboss.examples.ticketmonster.model.Venue;
 26  
 27  /**
 28   * 
 29   */
 30  @Stateless
 31  @Path("forge/venues")
 32  public class VenueEndpoint
 33  {
 34     @PersistenceContext(unitName = "primary")
 35     private EntityManager em;
 36  
 37     @POST
 38     @Consumes("application/json")
 39     public Response create(VenueDTO dto)
 40     {
 41        Venue entity = dto.fromDTO(null, em);
 42        em.persist(entity);
 43        return Response.created(UriBuilder.fromResource(VenueEndpoint.class).path(String.valueOf(entity.getId())).build()).build();
 44     }
 45  
 46     @DELETE
 47     @Path("/{id:[0-9][0-9]*}")
 48     public Response deleteById(@PathParam("id") Long id)
 49     {
 50        Venue entity = em.find(Venue.class, id);
 51        if (entity == null)
 52        {
 53           return Response.status(Status.NOT_FOUND).build();
 54        }
 55        em.remove(entity);
 56        return Response.noContent().build();
 57     }
 58  
 59     @GET
 60     @Path("/{id:[0-9][0-9]*}")
 61     @Produces("application/json")
 62     public Response findById(@PathParam("id") Long id)
 63     {
 64        TypedQuery<Venue> findByIdQuery = em.createQuery("SELECT DISTINCT v FROM Venue v LEFT JOIN FETCH v.sections LEFT JOIN FETCH v.mediaItem WHERE v.id = :entityId ORDER BY v.id", Venue.class);
 65        findByIdQuery.setParameter("entityId", id);
 66        Venue entity;
 67        try
 68        {
 69           entity = findByIdQuery.getSingleResult();
 70        }
 71        catch (NoResultException nre)
 72        {
 73           entity = null;
 74        }
 75        if (entity == null)
 76        {
 77           return Response.status(Status.NOT_FOUND).build();
 78        }
 79        VenueDTO dto = new VenueDTO(entity);
 80        return Response.ok(dto).build();
 81     }
 82  
 83     @GET
 84     @Produces("application/json")
 85     public List<VenueDTO> listAll(@QueryParam("start") Integer startPosition, @QueryParam("max") Integer maxResult)
 86     {
 87        TypedQuery<Venue> findAllQuery = em.createQuery("SELECT DISTINCT v FROM Venue v LEFT JOIN FETCH v.sections LEFT JOIN FETCH v.mediaItem ORDER BY v.id", Venue.class);
 88        if (startPosition != null)
 89        {
 90           findAllQuery.setFirstResult(startPosition);
 91        }
 92        if (maxResult != null)
 93        {
 94           findAllQuery.setMaxResults(maxResult);
 95        }
 96        final List<Venue> searchResults = findAllQuery.getResultList();
 97        final List<VenueDTO> results = new ArrayList<VenueDTO>();
 98        for (Venue searchResult : searchResults)
 99        {
100           VenueDTO dto = new VenueDTO(searchResult);
101           results.add(dto);
102        }
103        return results;
104     }
105  
106     @PUT
107     @Path("/{id:[0-9][0-9]*}")
108     @Consumes("application/json")
109     public Response update(@PathParam("id") Long id, VenueDTO dto)
110     {
111        TypedQuery<Venue> findByIdQuery = em.createQuery("SELECT DISTINCT v FROM Venue v LEFT JOIN FETCH v.sections LEFT JOIN FETCH v.mediaItem WHERE v.id = :entityId ORDER BY v.id", Venue.class);
112        findByIdQuery.setParameter("entityId", id);
113        Venue entity;
114        try
115        {
116           entity = findByIdQuery.getSingleResult();
117        }
118        catch (NoResultException nre)
119        {
120           entity = null;
121        }
122        entity = dto.fromDTO(entity, em);
123        try
124        {
125           entity = em.merge(entity);
126        }
127        catch (OptimisticLockException e)
128        {
129           return Response.status(Response.Status.CONFLICT).entity(e.getEntity()).build();
130        }
```
  * file:///tmp/source-code/monolith/src/main/java/org/jboss/examples/ticketmonster/rest/VenueService.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import javax.ejb.Stateless;
  4  import javax.ws.rs.Path;
  5  
  6  import org.jboss.examples.ticketmonster.model.Venue;
  7  
  8  /**
  9   * <p>
 10   *     A JAX-RS endpoint for handling {@link Venue}s. Inherits the actual
 11   *     methods from {@link BaseEntityService}.
 12   * </p>
 13   *
 14   * @author Marius Bogoevici
 15   */
 16  @Path("/venues")
 17  /**
 18   * <p>
 19   *     This is a stateless service, we declare it as an EJB for transaction demarcation
 20   * </p>
 21   */
 22  @Stateless
 23  public class VenueService extends BaseEntityService<Venue> {
 24  
 25      public VenueService() {
 26          super(Venue.class);
 27      }
 28  
 29  }

```
  * file:///tmp/source-code/monolith/src/main/java/org/jboss/examples/ticketmonster/service/Bot.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.service;
  2  
  3  import java.util.ArrayList;
  4  import java.util.Collection;
  5  import java.util.Date;
  6  import java.util.List;
  7  import java.util.Map;
  8  import java.util.Random;
  9  import java.util.concurrent.TimeUnit;
 10  
 11  import javax.annotation.Resource;
 12  import javax.ejb.Stateless;
 13  import javax.ejb.Timeout;
 14  import javax.ejb.Timer;
 15  import javax.ejb.TimerConfig;
 16  import javax.ejb.TimerService;
 17  import javax.enterprise.event.Event;
 18  import javax.inject.Inject;
 19  import javax.ws.rs.core.MultivaluedHashMap;
 20  import javax.ws.rs.core.Response;
 21  
 22  import org.jboss.examples.ticketmonster.model.Performance;
 23  import org.jboss.examples.ticketmonster.model.Show;
 24  import org.jboss.examples.ticketmonster.model.TicketPrice;
 25  import org.jboss.examples.ticketmonster.rest.*;
 26  import org.jboss.examples.ticketmonster.util.qualifier.BotMessage;
 27  
 28  @Stateless
 29  public class Bot {
 30      
 31      private static final Random random = new Random(System.nanoTime());
 32      
 33      /** Frequency with which the bot will book **/
 34      public static final long DURATION = TimeUnit.SECONDS.toMillis(3);
 35      
 36      /** Maximum number of ticket requests that will be filed **/
 37      public static int MAX_TICKET_REQUESTS = 100;
 38      
 39      /** Maximum number of tickets per request **/
 40      public static int MAX_TICKETS_PER_REQUEST = 100;
 41      
 42      public static String [] BOOKERS = {"anne@acme.com", "george@acme.com", "william@acme.com", "victoria@acme.com", "edward@acme.com", "elizabeth@acme.com", "mary@acme.com", "charles@acme.com", "james@acme.com", "henry@acme.com", "richard@acme.com", "john@acme.com", "stephen@acme.com"}; 
 43  
 44      @Inject 
 45      private ShowService showService;
 46      
 47      @Inject
 48      private BookingService bookingService;
 49      
 50      @Inject @BotMessage
 51      Event<String> event;
 52      
 53      @Resource
 54      private TimerService timerService;
 55      
 56      public Timer start() {
 57          String startMessage = new StringBuilder("==========================\n")
 58                  .append("Bot started at ").append(new Date().toString()).append("\n")
 59                  .toString();
 60          event.fire(startMessage);
 61          return timerService.createIntervalTimer(0, DURATION, new TimerConfig(null, false));
 62      }
 63      
 64      public void stop(Timer timer) {
 65          String stopMessage = new StringBuilder("==========================\n")
 66                  .append("Bot stopped at ").append(new Date().toString()).append("\n")
 67                  .toString();
 68          event.fire(stopMessage);
 69          timer.cancel();
 70      }
 71      
 72      @Timeout
 73      public void book(Timer timer) {
 74          // Select a show at random
 75          Show show = selectAtRandom(showService.getAll(new MultivaluedHashMap<String, String>()));
 76  
 77          // Select a performance at random
 78          Performance performance = selectAtRandom(show.getPerformances());
 79          
 80          String requestor = selectAtRandom(BOOKERS);
 81  
 82          BookingRequest bookingRequest = new BookingRequest(performance, requestor);
 83  
 84          List<TicketPrice> possibleTicketPrices = new ArrayList<TicketPrice>(show.getTicketPrices());
 85          
 86          List<Integer> indicies = selectAtRandom(MAX_TICKET_REQUESTS < possibleTicketPrices.size() ? MAX_TICKET_REQUESTS : possibleTicketPrices.size());
 87          
 88          StringBuilder message = new StringBuilder("==========================\n")
 89          .append("Booking by ")
 90          .append(requestor)
 91          .append(" at ")
 92          .append(new Date().toString())
 93          .append("\n")
 94          .append(performance)
 95          .append("\n")
 96          .append("~~~~~~~~~~~~~~~~~~~~~~~~~\n");
 97          
 98          for (int index : indicies) {
 99              int no = random.nextInt(MAX_TICKETS_PER_REQUEST);
100              TicketPrice price = possibleTicketPrices.get(index);  
101              bookingRequest.addTicketRequest(new TicketRequest(price, no));
102              message
103                  .append(no)
104                  .append(" of ")
105                  .append(price.getSection())
106                  .append("\n");
107              
108          }
109          Response response = bookingService.createBooking(bookingRequest);
110          if(response.getStatus() == Response.Status.OK.getStatusCode()) {
111              message.append("SUCCESSFUL\n")
112                      .append("~~~~~~~~~~~~~~~~~~~~~~~~~\n");
113          }
114          else {
115              message.append("FAILED:\n")
116                          .append(((Map<String, Object>) response.getEntity()).get("errors"))
117                          .append("~~~~~~~~~~~~~~~~~~~~~~~~~\n");
118          }
119          event.fire(message.toString());
120      }
121      
122      
123      
124      private <T> T selectAtRandom(List<T> list) {
125          int i = random.nextInt(list.size());
126          return list.get(i);
127      }
128      
```
### #5 - dependency-removal-for-quarkus-00000
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
### #6 - javaee-pom-to-quarkus-00000
* Category: mandatory
* Effort: 1
* Description: The expected project artifact's extension is `jar`

* Labels: konveyor.io/source=java-ee, konveyor.io/target=quarkus
* Links
  * Quarkus - Guide: https://quarkus.io/guides/maven-tooling#build-tool-maven
* Incidents
  * file:///tmp/source-code/backend-v1/pom.xml
      * The project artifact's current extension (i.e. `<packaging>` tag value) is `` but the expected value should be `jar`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  3      <modelVersion>4.0.0</modelVersion>
  4      <groupId>org.jboss.examples.eap</groupId>
  5      <artifactId>backend-v1</artifactId>
  6      <version>1.0</version>
  7      <packaging>war</packaging>
  8      <name>ticket-monster backend</name>
  9      <description>A starter HTML5 + REST webapp project for use on JBoss EAP.</description>
 10  
 11      <!-- Activate JBoss Product Maven repository.
 12  
 13          NOTE: Configuring the Maven repository in the pom.xml file is not a recommended procedure
 14          and is only done here to make it easier to use the quickstarts.
 15  
 16          For more information about how to configure Maven for your application,
 17          see the section entitled 'Use the Maven Repository'
 18          in the Development Guide for Red Hat JBoss Enterprise Application Platform located here:
 19  
 20          https://access.redhat.com/documentation/en-US/JBoss_Enterprise_Application_Platform/
 21      -->
 22      <repositories>
 23          <repository>
 24              <id>redhat-ga-repository</id>
 25              <url>https://maven.repository.redhat.com/ga/</url>
 26              <releases>
 27                  <enabled>true</enabled>
 28              </releases>
 29              <snapshots>
 30                  <enabled>false</enabled>
 31              </snapshots>
 32          </repository>
 33          <repository>
 34              <id>jboss-ga-repository</id>
 35              <url>http://maven.repository.redhat.com/techpreview/all</url>
 36              <releases>
 37                  <enabled>true</enabled>
 38              </releases>
 39              <snapshots>
 40                  <enabled>false</enabled>
 41              </snapshots>
 42          </repository>
 43          <repository>
 44              <id>jboss-earlyaccess-repository</id>
 45              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 46              <releases>
 47                  <enabled>true</enabled>
 48              </releases>
 49              <snapshots>
 50                  <enabled>false</enabled>
 51              </snapshots>
 52          </repository>
 53          <repository>
 54              <id>redhat.ea</id>
 55              <name>Red Hat Early Access Repository</name>
 56              <url>https://maven.repository.redhat.com/earlyaccess/all</url>
 57              <snapshots>
 58                  <enabled>false</enabled>
 59              </snapshots>
 60              <releases>
 61                  <enabled>true</enabled>
 62              </releases>
 63          </repository>
 64      </repositories>
 65  
 66      <pluginRepositories>
 67          <pluginRepository>
 68              <id>redhat-ga-repository</id>
 69              <url>https://maven.repository.redhat.com/ga/</url>
 70              <releases>
 71                  <enabled>true</enabled>
 72              </releases>
 73              <snapshots>
 74                  <enabled>false</enabled>
 75              </snapshots>
 76          </pluginRepository>
 77          <pluginRepository>
 78              <id>jboss-earlyaccess-plugin-repository</id>
 79              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 80              <releases>
 81                  <enabled>true</enabled>
 82              </releases>
 83              <snapshots>
 84                  <enabled>false</enabled>
 85              </snapshots>
 86          </pluginRepository>
 87      </pluginRepositories>
 88  
 89      <properties>
 90          <!-- Explicitly declaring the source encoding eliminates the following 
 91              message: -->
 92          <!-- [WARNING] Using platform encoding (UTF-8 actually) to copy filtered 
 93              resources, i.e. build is platform dependent! -->
 94          <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
 95          <!-- Timestamp format for the maven.build.timestamp property -->
 96          <!-- You can reference property in pom.xml or filtered resources 
 97              (must enable third-party plugin if using Maven < 2.1) -->
 98          <maven.build.timestamp.format>yyyyMMdd'T'HHmmss</maven.build.timestamp.format>
 99          <!-- Specify the JBoss EAP directory to be the JBOSS_HOME environment
100              variable -->
101          <jboss.home>${env.JBOSS_HOME}</jboss.home>
102          <version.jboss.bom.eap>7.0.7.GA</version.jboss.bom.eap>
103          <version.wildfly.maven.plugin>1.0.2.Final</version.wildfly.maven.plugin>
104          <version.surefire.plugin>2.10</version.surefire.plugin>
105          <buildhelper.plugin.version>1.7</buildhelper.plugin.version>
106          <fabric8.maven.plugin.version>3.5.25</fabric8.maven.plugin.version>
107          <docker.image.name>ceposta/%a:%l</docker.image.name>
108      </properties>
```
  * file:///tmp/source-code/backend-v2/pom.xml
      * The project artifact's current extension (i.e. `<packaging>` tag value) is `` but the expected value should be `jar`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  3      <modelVersion>4.0.0</modelVersion>
  4      <groupId>org.jboss.examples.eap</groupId>
  5      <artifactId>backend-v2</artifactId>
  6      <version>2.0</version>
  7      <packaging>war</packaging>
  8      <name>ticket-monster backend v2</name>
  9      <description>A starter HTML5 + REST webapp project for use on JBoss EAP.</description>
 10  
 11      <!-- Activate JBoss Product Maven repository.
 12  
 13          NOTE: Configuring the Maven repository in the pom.xml file is not a recommended procedure
 14          and is only done here to make it easier to use the quickstarts.
 15  
 16          For more information about how to configure Maven for your application,
 17          see the section entitled 'Use the Maven Repository'
 18          in the Development Guide for Red Hat JBoss Enterprise Application Platform located here:
 19  
 20          https://access.redhat.com/documentation/en-US/JBoss_Enterprise_Application_Platform/
 21      -->
 22      <repositories>
 23          <repository>
 24              <id>redhat-ga-repository</id>
 25              <url>https://maven.repository.redhat.com/ga/</url>
 26              <releases>
 27                  <enabled>true</enabled>
 28              </releases>
 29              <snapshots>
 30                  <enabled>false</enabled>
 31              </snapshots>
 32          </repository>
 33          <repository>
 34              <id>jboss-ga-repository</id>
 35              <url>http://maven.repository.redhat.com/techpreview/all</url>
 36              <releases>
 37                  <enabled>true</enabled>
 38              </releases>
 39              <snapshots>
 40                  <enabled>false</enabled>
 41              </snapshots>
 42          </repository>
 43          <repository>
 44              <id>jboss-earlyaccess-repository</id>
 45              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 46              <releases>
 47                  <enabled>true</enabled>
 48              </releases>
 49              <snapshots>
 50                  <enabled>false</enabled>
 51              </snapshots>
 52          </repository>
 53          <repository>
 54              <id>redhat.ea</id>
 55              <name>Red Hat Early Access Repository</name>
 56              <url>https://maven.repository.redhat.com/earlyaccess/all</url>
 57              <snapshots>
 58                  <enabled>false</enabled>
 59              </snapshots>
 60              <releases>
 61                  <enabled>true</enabled>
 62              </releases>
 63          </repository>
 64      </repositories>
 65  
 66      <pluginRepositories>
 67          <pluginRepository>
 68              <id>redhat-ga-repository</id>
 69              <url>https://maven.repository.redhat.com/ga/</url>
 70              <releases>
 71                  <enabled>true</enabled>
 72              </releases>
 73              <snapshots>
 74                  <enabled>false</enabled>
 75              </snapshots>
 76          </pluginRepository>
 77          <pluginRepository>
 78              <id>jboss-earlyaccess-plugin-repository</id>
 79              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 80              <releases>
 81                  <enabled>true</enabled>
 82              </releases>
 83              <snapshots>
 84                  <enabled>false</enabled>
 85              </snapshots>
 86          </pluginRepository>
 87      </pluginRepositories>
 88  
 89      <properties>
 90          <!-- Explicitly declaring the source encoding eliminates the following 
 91              message: -->
 92          <!-- [WARNING] Using platform encoding (UTF-8 actually) to copy filtered 
 93              resources, i.e. build is platform dependent! -->
 94          <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
 95          <!-- Timestamp format for the maven.build.timestamp property -->
 96          <!-- You can reference property in pom.xml or filtered resources 
 97              (must enable third-party plugin if using Maven < 2.1) -->
 98          <maven.build.timestamp.format>yyyyMMdd'T'HHmmss</maven.build.timestamp.format>
 99          <!-- Specify the JBoss EAP directory to be the JBOSS_HOME environment
100              variable -->
101          <jboss.home>${env.JBOSS_HOME}</jboss.home>
102          <version.jboss.bom.eap>7.0.7.GA</version.jboss.bom.eap>
103          <version.wildfly.maven.plugin>1.0.2.Final</version.wildfly.maven.plugin>
104          <version.surefire.plugin>2.10</version.surefire.plugin>
105          <buildhelper.plugin.version>1.7</buildhelper.plugin.version>
106          <fabric8.maven.plugin.version>3.5.25</fabric8.maven.plugin.version>
107          <docker.image.name>ceposta/%a:%l</docker.image.name>
108          <ffj4.version>1.6.5</ffj4.version>
```
  * file:///tmp/source-code/monolith/pom.xml
      * The project artifact's current extension (i.e. `<packaging>` tag value) is `` but the expected value should be `jar`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  3      <modelVersion>4.0.0</modelVersion>
  4      <groupId>org.jboss.examples.eap</groupId>
  5      <artifactId>ticket-monster</artifactId>
  6      <version>3.0.0-SNAPSHOT</version>
  7      <packaging>war</packaging>
  8      <name>ticket-monster</name>
  9      <description>A starter HTML5 + REST webapp project for use on JBoss EAP.</description>
 10  
 11      <!-- Activate JBoss Product Maven repository.
 12  
 13          NOTE: Configuring the Maven repository in the pom.xml file is not a recommended procedure
 14          and is only done here to make it easier to use the quickstarts.
 15  
 16          For more information about how to configure Maven for your application,
 17          see the section entitled 'Use the Maven Repository'
 18          in the Development Guide for Red Hat JBoss Enterprise Application Platform located here:
 19  
 20          https://access.redhat.com/documentation/en-US/JBoss_Enterprise_Application_Platform/
 21      -->
 22      <repositories>
 23          <repository>
 24              <id>redhat-ga-repository</id>
 25              <url>https://maven.repository.redhat.com/ga/</url>
 26              <releases>
 27                  <enabled>true</enabled>
 28              </releases>
 29              <snapshots>
 30                  <enabled>false</enabled>
 31              </snapshots>
 32          </repository>
 33          <repository>
 34              <id>jboss-ga-repository</id>
 35              <url>http://maven.repository.redhat.com/techpreview/all</url>
 36              <releases>
 37                  <enabled>true</enabled>
 38              </releases>
 39              <snapshots>
 40                  <enabled>false</enabled>
 41              </snapshots>
 42          </repository>
 43          <repository>
 44              <id>jboss-earlyaccess-repository</id>
 45              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 46              <releases>
 47                  <enabled>true</enabled>
 48              </releases>
 49              <snapshots>
 50                  <enabled>false</enabled>
 51              </snapshots>
 52          </repository>
 53          <repository>
 54              <id>redhat.ea</id>
 55              <name>Red Hat Early Access Repository</name>
 56              <url>https://maven.repository.redhat.com/earlyaccess/all</url>
 57              <snapshots>
 58                  <enabled>false</enabled>
 59              </snapshots>
 60              <releases>
 61                  <enabled>true</enabled>
 62              </releases>
 63          </repository>
 64      </repositories>
 65  
 66      <pluginRepositories>
 67          <pluginRepository>
 68              <id>redhat-ga-repository</id>
 69              <url>https://maven.repository.redhat.com/ga/</url>
 70              <releases>
 71                  <enabled>true</enabled>
 72              </releases>
 73              <snapshots>
 74                  <enabled>false</enabled>
 75              </snapshots>
 76          </pluginRepository>
 77          <pluginRepository>
 78              <id>jboss-earlyaccess-plugin-repository</id>
 79              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 80              <releases>
 81                  <enabled>true</enabled>
 82              </releases>
 83              <snapshots>
 84                  <enabled>false</enabled>
 85              </snapshots>
 86          </pluginRepository>
 87      </pluginRepositories>
 88  
 89      <properties>
 90          <!-- Explicitly declaring the source encoding eliminates the following 
 91              message: -->
 92          <!-- [WARNING] Using platform encoding (UTF-8 actually) to copy filtered 
 93              resources, i.e. build is platform dependent! -->
 94          <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
 95          <!-- Timestamp format for the maven.build.timestamp property -->
 96          <!-- You can reference property in pom.xml or filtered resources 
 97              (must enable third-party plugin if using Maven < 2.1) -->
 98          <maven.build.timestamp.format>yyyyMMdd'T'HHmmss</maven.build.timestamp.format>
 99          <!-- Specify the JBoss EAP directory to be the JBOSS_HOME environment
100              variable -->
101          <jboss.home>${env.JBOSS_HOME}</jboss.home>
102          <version.jboss.bom.eap>7.0.7.GA</version.jboss.bom.eap>
103          <version.wildfly.maven.plugin>1.0.2.Final</version.wildfly.maven.plugin>
104          <version.surefire.plugin>2.10</version.surefire.plugin>
105          <buildhelper.plugin.version>1.7</buildhelper.plugin.version>
106          <fabric8.maven.plugin.version>3.5.25</fabric8.maven.plugin.version>
107          <docker.image.name>%g/%a:%l</docker.image.name>
108      </properties>
```
  * file:///tmp/source-code/pom.xml
      * The project artifact's current extension (i.e. `<packaging>` tag value) is `` but the expected value should be `jar`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  3      <modelVersion>4.0.0</modelVersion>
  4      <groupId>org.jboss.examples.eap</groupId>
  5      <artifactId>ticket-monster-parent</artifactId>
  6      <version>3.0.0-SNAPSHOT</version>
  7      <modules>
  8          <module>monolith</module>
  9          <module>backend-v1</module>
 10          <module>backend-v2</module>
 11          <module>orders-service</module>
 12      </modules>
 13      <packaging>pom</packaging>
 14      <name>Ticket Monster Parent</name>
 15      <description>A starter HTML5 + REST webapp project for use on JBoss EAP.</description>
 16  
 17      <!-- Activate JBoss Product Maven repository.
 18  
 19          NOTE: Configuring the Maven repository in the pom.xml file is not a recommended procedure
 20          and is only done here to make it easier to use the quickstarts.
 21  
 22          For more information about how to configure Maven for your application,
 23          see the section entitled 'Use the Maven Repository'
 24          in the Development Guide for Red Hat JBoss Enterprise Application Platform located here:
 25  
 26          https://access.redhat.com/documentation/en-US/JBoss_Enterprise_Application_Platform/
 27      -->
 28      <repositories>
 29          <repository>
 30              <id>redhat-ga-repository</id>
 31              <url>https://maven.repository.redhat.com/ga/</url>
 32              <releases>
 33                  <enabled>true</enabled>
 34              </releases>
 35              <snapshots>
 36                  <enabled>false</enabled>
 37              </snapshots>
 38          </repository>
 39          <repository>
 40              <id>jboss-ga-repository</id>
 41              <url>http://maven.repository.redhat.com/techpreview/all</url>
 42              <releases>
 43                  <enabled>true</enabled>
 44              </releases>
 45              <snapshots>
 46                  <enabled>false</enabled>
 47              </snapshots>
 48          </repository>
 49          <repository>
 50              <id>jboss-earlyaccess-repository</id>
 51              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 52              <releases>
 53                  <enabled>true</enabled>
 54              </releases>
 55              <snapshots>
 56                  <enabled>false</enabled>
 57              </snapshots>
 58          </repository>
 59          <repository>
 60              <id>redhat.ea</id>
 61              <name>Red Hat Early Access Repository</name>
 62              <url>https://maven.repository.redhat.com/earlyaccess/all</url>
 63              <snapshots>
 64                  <enabled>false</enabled>
 65              </snapshots>
 66              <releases>
 67                  <enabled>true</enabled>
 68              </releases>
 69          </repository>
 70      </repositories>
 71  
 72      <pluginRepositories>
 73          <pluginRepository>
 74              <id>redhat-ga-repository</id>
 75              <url>https://maven.repository.redhat.com/ga/</url>
 76              <releases>
 77                  <enabled>true</enabled>
 78              </releases>
 79              <snapshots>
 80                  <enabled>false</enabled>
 81              </snapshots>
 82          </pluginRepository>
 83          <pluginRepository>
 84              <id>jboss-earlyaccess-plugin-repository</id>
 85              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 86              <releases>
 87                  <enabled>true</enabled>
 88              </releases>
 89              <snapshots>
 90                  <enabled>false</enabled>
 91              </snapshots>
 92          </pluginRepository>
 93      </pluginRepositories>
 94  
 95      <build>
 96          <plugins>
 97              <plugin>
 98                  <artifactId>maven-compiler-plugin</artifactId>
 99                  <version>2.3.1</version>
100                  <configuration>
101                      <source>1.8</source>
102                      <target>1.8</target>
103                  </configuration>
104              </plugin>
105          </plugins>
106      </build>
107  
108  </project>

```
### #7 - javaee-pom-to-quarkus-00010
* Category: mandatory
* Effort: 1
* Description: Adopt Quarkus BOM

* Labels: konveyor.io/source=java-ee, konveyor.io/target=quarkus
* Links
  * Quarkus - Guide: https://quarkus.io/guides/maven-tooling#build-tool-maven
  * Quarkus - Releases: https://quarkus.io/blog/tag/release/
* Incidents
  * file:///tmp/source-code/backend-v1/pom.xml
      * Use the Quarkus BOM to omit the version of the different Quarkus dependencies.. Add the following sections to the `pom.xml` file:. ```xml. <properties>. <quarkus.platform.artifact-id>quarkus-bom</quarkus.platform.artifact-id>. <quarkus.platform.group-id>io.quarkus.platform</quarkus.platform.group-id>. <quarkus.platform.version>3.1.0.Final</quarkus.platform.version>. </properties>. <dependencyManagement>. <dependencies>. <dependency>. <groupId>$</groupId>. <artifactId>$</artifactId>. <version>$</version>. <type>pom</type>. <scope>import</scope>. </dependency>. </dependencies>. </dependencyManagement>. ```. Check the latest Quarkus version available from the `Quarkus - Releases` link below.
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  3      <modelVersion>4.0.0</modelVersion>
  4      <groupId>org.jboss.examples.eap</groupId>
  5      <artifactId>backend-v1</artifactId>
  6      <version>1.0</version>
  7      <packaging>war</packaging>
  8      <name>ticket-monster backend</name>
  9      <description>A starter HTML5 + REST webapp project for use on JBoss EAP.</description>
 10  
 11      <!-- Activate JBoss Product Maven repository.
 12  
 13          NOTE: Configuring the Maven repository in the pom.xml file is not a recommended procedure
 14          and is only done here to make it easier to use the quickstarts.
 15  
 16          For more information about how to configure Maven for your application,
 17          see the section entitled 'Use the Maven Repository'
 18          in the Development Guide for Red Hat JBoss Enterprise Application Platform located here:
 19  
 20          https://access.redhat.com/documentation/en-US/JBoss_Enterprise_Application_Platform/
 21      -->
 22      <repositories>
 23          <repository>
 24              <id>redhat-ga-repository</id>
 25              <url>https://maven.repository.redhat.com/ga/</url>
 26              <releases>
 27                  <enabled>true</enabled>
 28              </releases>
 29              <snapshots>
 30                  <enabled>false</enabled>
 31              </snapshots>
 32          </repository>
 33          <repository>
 34              <id>jboss-ga-repository</id>
 35              <url>http://maven.repository.redhat.com/techpreview/all</url>
 36              <releases>
 37                  <enabled>true</enabled>
 38              </releases>
 39              <snapshots>
 40                  <enabled>false</enabled>
 41              </snapshots>
 42          </repository>
 43          <repository>
 44              <id>jboss-earlyaccess-repository</id>
 45              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 46              <releases>
 47                  <enabled>true</enabled>
 48              </releases>
 49              <snapshots>
 50                  <enabled>false</enabled>
 51              </snapshots>
 52          </repository>
 53          <repository>
 54              <id>redhat.ea</id>
 55              <name>Red Hat Early Access Repository</name>
 56              <url>https://maven.repository.redhat.com/earlyaccess/all</url>
 57              <snapshots>
 58                  <enabled>false</enabled>
 59              </snapshots>
 60              <releases>
 61                  <enabled>true</enabled>
 62              </releases>
 63          </repository>
 64      </repositories>
 65  
 66      <pluginRepositories>
 67          <pluginRepository>
 68              <id>redhat-ga-repository</id>
 69              <url>https://maven.repository.redhat.com/ga/</url>
 70              <releases>
 71                  <enabled>true</enabled>
 72              </releases>
 73              <snapshots>
 74                  <enabled>false</enabled>
 75              </snapshots>
 76          </pluginRepository>
 77          <pluginRepository>
 78              <id>jboss-earlyaccess-plugin-repository</id>
 79              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 80              <releases>
 81                  <enabled>true</enabled>
 82              </releases>
 83              <snapshots>
 84                  <enabled>false</enabled>
 85              </snapshots>
 86          </pluginRepository>
 87      </pluginRepositories>
 88  
 89      <properties>
 90          <!-- Explicitly declaring the source encoding eliminates the following 
 91              message: -->
 92          <!-- [WARNING] Using platform encoding (UTF-8 actually) to copy filtered 
 93              resources, i.e. build is platform dependent! -->
 94          <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
 95          <!-- Timestamp format for the maven.build.timestamp property -->
 96          <!-- You can reference property in pom.xml or filtered resources 
 97              (must enable third-party plugin if using Maven < 2.1) -->
 98          <maven.build.timestamp.format>yyyyMMdd'T'HHmmss</maven.build.timestamp.format>
 99          <!-- Specify the JBoss EAP directory to be the JBOSS_HOME environment
100              variable -->
101          <jboss.home>${env.JBOSS_HOME}</jboss.home>
102          <version.jboss.bom.eap>7.0.7.GA</version.jboss.bom.eap>
103          <version.wildfly.maven.plugin>1.0.2.Final</version.wildfly.maven.plugin>
104          <version.surefire.plugin>2.10</version.surefire.plugin>
```
  * file:///tmp/source-code/backend-v2/pom.xml
      * Use the Quarkus BOM to omit the version of the different Quarkus dependencies.. Add the following sections to the `pom.xml` file:. ```xml. <properties>. <quarkus.platform.artifact-id>quarkus-bom</quarkus.platform.artifact-id>. <quarkus.platform.group-id>io.quarkus.platform</quarkus.platform.group-id>. <quarkus.platform.version>3.1.0.Final</quarkus.platform.version>. </properties>. <dependencyManagement>. <dependencies>. <dependency>. <groupId>$</groupId>. <artifactId>$</artifactId>. <version>$</version>. <type>pom</type>. <scope>import</scope>. </dependency>. </dependencies>. </dependencyManagement>. ```. Check the latest Quarkus version available from the `Quarkus - Releases` link below.
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  3      <modelVersion>4.0.0</modelVersion>
  4      <groupId>org.jboss.examples.eap</groupId>
  5      <artifactId>backend-v2</artifactId>
  6      <version>2.0</version>
  7      <packaging>war</packaging>
  8      <name>ticket-monster backend v2</name>
  9      <description>A starter HTML5 + REST webapp project for use on JBoss EAP.</description>
 10  
 11      <!-- Activate JBoss Product Maven repository.
 12  
 13          NOTE: Configuring the Maven repository in the pom.xml file is not a recommended procedure
 14          and is only done here to make it easier to use the quickstarts.
 15  
 16          For more information about how to configure Maven for your application,
 17          see the section entitled 'Use the Maven Repository'
 18          in the Development Guide for Red Hat JBoss Enterprise Application Platform located here:
 19  
 20          https://access.redhat.com/documentation/en-US/JBoss_Enterprise_Application_Platform/
 21      -->
 22      <repositories>
 23          <repository>
 24              <id>redhat-ga-repository</id>
 25              <url>https://maven.repository.redhat.com/ga/</url>
 26              <releases>
 27                  <enabled>true</enabled>
 28              </releases>
 29              <snapshots>
 30                  <enabled>false</enabled>
 31              </snapshots>
 32          </repository>
 33          <repository>
 34              <id>jboss-ga-repository</id>
 35              <url>http://maven.repository.redhat.com/techpreview/all</url>
 36              <releases>
 37                  <enabled>true</enabled>
 38              </releases>
 39              <snapshots>
 40                  <enabled>false</enabled>
 41              </snapshots>
 42          </repository>
 43          <repository>
 44              <id>jboss-earlyaccess-repository</id>
 45              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 46              <releases>
 47                  <enabled>true</enabled>
 48              </releases>
 49              <snapshots>
 50                  <enabled>false</enabled>
 51              </snapshots>
 52          </repository>
 53          <repository>
 54              <id>redhat.ea</id>
 55              <name>Red Hat Early Access Repository</name>
 56              <url>https://maven.repository.redhat.com/earlyaccess/all</url>
 57              <snapshots>
 58                  <enabled>false</enabled>
 59              </snapshots>
 60              <releases>
 61                  <enabled>true</enabled>
 62              </releases>
 63          </repository>
 64      </repositories>
 65  
 66      <pluginRepositories>
 67          <pluginRepository>
 68              <id>redhat-ga-repository</id>
 69              <url>https://maven.repository.redhat.com/ga/</url>
 70              <releases>
 71                  <enabled>true</enabled>
 72              </releases>
 73              <snapshots>
 74                  <enabled>false</enabled>
 75              </snapshots>
 76          </pluginRepository>
 77          <pluginRepository>
 78              <id>jboss-earlyaccess-plugin-repository</id>
 79              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 80              <releases>
 81                  <enabled>true</enabled>
 82              </releases>
 83              <snapshots>
 84                  <enabled>false</enabled>
 85              </snapshots>
 86          </pluginRepository>
 87      </pluginRepositories>
 88  
 89      <properties>
 90          <!-- Explicitly declaring the source encoding eliminates the following 
 91              message: -->
 92          <!-- [WARNING] Using platform encoding (UTF-8 actually) to copy filtered 
 93              resources, i.e. build is platform dependent! -->
 94          <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
 95          <!-- Timestamp format for the maven.build.timestamp property -->
 96          <!-- You can reference property in pom.xml or filtered resources 
 97              (must enable third-party plugin if using Maven < 2.1) -->
 98          <maven.build.timestamp.format>yyyyMMdd'T'HHmmss</maven.build.timestamp.format>
 99          <!-- Specify the JBoss EAP directory to be the JBOSS_HOME environment
100              variable -->
101          <jboss.home>${env.JBOSS_HOME}</jboss.home>
102          <version.jboss.bom.eap>7.0.7.GA</version.jboss.bom.eap>
103          <version.wildfly.maven.plugin>1.0.2.Final</version.wildfly.maven.plugin>
104          <version.surefire.plugin>2.10</version.surefire.plugin>
```
  * file:///tmp/source-code/monolith/pom.xml
      * Use the Quarkus BOM to omit the version of the different Quarkus dependencies.. Add the following sections to the `pom.xml` file:. ```xml. <properties>. <quarkus.platform.artifact-id>quarkus-bom</quarkus.platform.artifact-id>. <quarkus.platform.group-id>io.quarkus.platform</quarkus.platform.group-id>. <quarkus.platform.version>3.1.0.Final</quarkus.platform.version>. </properties>. <dependencyManagement>. <dependencies>. <dependency>. <groupId>$</groupId>. <artifactId>$</artifactId>. <version>$</version>. <type>pom</type>. <scope>import</scope>. </dependency>. </dependencies>. </dependencyManagement>. ```. Check the latest Quarkus version available from the `Quarkus - Releases` link below.
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  3      <modelVersion>4.0.0</modelVersion>
  4      <groupId>org.jboss.examples.eap</groupId>
  5      <artifactId>ticket-monster</artifactId>
  6      <version>3.0.0-SNAPSHOT</version>
  7      <packaging>war</packaging>
  8      <name>ticket-monster</name>
  9      <description>A starter HTML5 + REST webapp project for use on JBoss EAP.</description>
 10  
 11      <!-- Activate JBoss Product Maven repository.
 12  
 13          NOTE: Configuring the Maven repository in the pom.xml file is not a recommended procedure
 14          and is only done here to make it easier to use the quickstarts.
 15  
 16          For more information about how to configure Maven for your application,
 17          see the section entitled 'Use the Maven Repository'
 18          in the Development Guide for Red Hat JBoss Enterprise Application Platform located here:
 19  
 20          https://access.redhat.com/documentation/en-US/JBoss_Enterprise_Application_Platform/
 21      -->
 22      <repositories>
 23          <repository>
 24              <id>redhat-ga-repository</id>
 25              <url>https://maven.repository.redhat.com/ga/</url>
 26              <releases>
 27                  <enabled>true</enabled>
 28              </releases>
 29              <snapshots>
 30                  <enabled>false</enabled>
 31              </snapshots>
 32          </repository>
 33          <repository>
 34              <id>jboss-ga-repository</id>
 35              <url>http://maven.repository.redhat.com/techpreview/all</url>
 36              <releases>
 37                  <enabled>true</enabled>
 38              </releases>
 39              <snapshots>
 40                  <enabled>false</enabled>
 41              </snapshots>
 42          </repository>
 43          <repository>
 44              <id>jboss-earlyaccess-repository</id>
 45              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 46              <releases>
 47                  <enabled>true</enabled>
 48              </releases>
 49              <snapshots>
 50                  <enabled>false</enabled>
 51              </snapshots>
 52          </repository>
 53          <repository>
 54              <id>redhat.ea</id>
 55              <name>Red Hat Early Access Repository</name>
 56              <url>https://maven.repository.redhat.com/earlyaccess/all</url>
 57              <snapshots>
 58                  <enabled>false</enabled>
 59              </snapshots>
 60              <releases>
 61                  <enabled>true</enabled>
 62              </releases>
 63          </repository>
 64      </repositories>
 65  
 66      <pluginRepositories>
 67          <pluginRepository>
 68              <id>redhat-ga-repository</id>
 69              <url>https://maven.repository.redhat.com/ga/</url>
 70              <releases>
 71                  <enabled>true</enabled>
 72              </releases>
 73              <snapshots>
 74                  <enabled>false</enabled>
 75              </snapshots>
 76          </pluginRepository>
 77          <pluginRepository>
 78              <id>jboss-earlyaccess-plugin-repository</id>
 79              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 80              <releases>
 81                  <enabled>true</enabled>
 82              </releases>
 83              <snapshots>
 84                  <enabled>false</enabled>
 85              </snapshots>
 86          </pluginRepository>
 87      </pluginRepositories>
 88  
 89      <properties>
 90          <!-- Explicitly declaring the source encoding eliminates the following 
 91              message: -->
 92          <!-- [WARNING] Using platform encoding (UTF-8 actually) to copy filtered 
 93              resources, i.e. build is platform dependent! -->
 94          <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
 95          <!-- Timestamp format for the maven.build.timestamp property -->
 96          <!-- You can reference property in pom.xml or filtered resources 
 97              (must enable third-party plugin if using Maven < 2.1) -->
 98          <maven.build.timestamp.format>yyyyMMdd'T'HHmmss</maven.build.timestamp.format>
 99          <!-- Specify the JBoss EAP directory to be the JBOSS_HOME environment
100              variable -->
101          <jboss.home>${env.JBOSS_HOME}</jboss.home>
102          <version.jboss.bom.eap>7.0.7.GA</version.jboss.bom.eap>
103          <version.wildfly.maven.plugin>1.0.2.Final</version.wildfly.maven.plugin>
104          <version.surefire.plugin>2.10</version.surefire.plugin>
```
  * file:///tmp/source-code/orders-service/pom.xml
      * Use the Quarkus BOM to omit the version of the different Quarkus dependencies.. Add the following sections to the `pom.xml` file:. ```xml. <properties>. <quarkus.platform.artifact-id>quarkus-bom</quarkus.platform.artifact-id>. <quarkus.platform.group-id>io.quarkus.platform</quarkus.platform.group-id>. <quarkus.platform.version>3.1.0.Final</quarkus.platform.version>. </properties>. <dependencyManagement>. <dependencies>. <dependency>. <groupId>$</groupId>. <artifactId>$</artifactId>. <version>$</version>. <type>pom</type>. <scope>import</scope>. </dependency>. </dependencies>. </dependencyManagement>. ```. Check the latest Quarkus version available from the `Quarkus - Releases` link below.
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <project xmlns="http://maven.apache.org/POM/4.0.0"
  3           xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  4           xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  5    <artifactId>orders-service</artifactId>
  6    <groupId>org.ticketmonster.orders</groupId>
  7    <version>1.0.0-SNAPSHOT</version>
  8    <modelVersion>4.0.0</modelVersion>
  9  
 10    <properties>
 11      <spring-boot.version>1.5.6.RELEASE</spring-boot.version>
 12      <docker-maven-plugin.version>0.20.1</docker-maven-plugin.version>
 13      <mysql-server.version>5.7</mysql-server.version>
 14      <mysql.user>ticket</mysql.user>
 15      <mysql.password>monster</mysql.password>
 16      <mysql.port>3306</mysql.port>
 17      <mysql.init.timeout>60000</mysql.init.timeout>
 18      <skipITs>true</skipITs>
 19      <fabric8.maven.plugin.version>3.5.25</fabric8.maven.plugin.version>
 20      <docker.image.name>ceposta/%a:%l</docker.image.name>
 21    </properties>
 22  
 23    <dependencyManagement>
 24      <dependencies>
 25        <dependency>
 26          <!-- Import dependency management from Spring Boot -->
 27          <groupId>org.springframework.boot</groupId>
 28          <artifactId>spring-boot-dependencies</artifactId>
 29          <version>${spring-boot.version}</version>
 30          <type>pom</type>
 31          <scope>import</scope>
 32        </dependency>
 33      </dependencies>
 34    </dependencyManagement>
 35  
 36  
 37    <dependencies>
 38      <dependency>
 39        <groupId>org.springframework.boot</groupId>
 40        <artifactId>spring-boot-starter-web</artifactId>
 41      </dependency>
 42      <dependency>
 43        <groupId>org.springframework.boot</groupId>
 44        <artifactId>spring-boot-starter-actuator</artifactId>
 45      </dependency>
 46      <dependency>
 47        <groupId>org.springframework.boot</groupId>
 48        <artifactId>spring-boot-starter-data-jpa</artifactId>
 49      </dependency>
 50      <dependency>
 51        <groupId>org.teiid.spring</groupId>
 52        <artifactId>teiid-spring-boot-starter</artifactId>
 53        <version>1.0.0-SNAPSHOT</version>
 54      </dependency>
 55  
 56  
 57  
 58      <!-- Testing -->
 59      <dependency>
 60        <groupId>io.rest-assured</groupId>
 61        <artifactId>rest-assured</artifactId>
 62        <version>3.0.3</version>
 63        <scope>test</scope>
 64      </dependency>
 65      <dependency>
 66        <groupId>io.rest-assured</groupId>
 67        <artifactId>json-schema-validator</artifactId>
 68        <version>3.0.3</version>
 69        <scope>test</scope>
 70      </dependency>
 71      <dependency>
 72        <groupId>io.specto</groupId>
 73        <artifactId>hoverfly-java</artifactId>
 74        <version>0.8.0</version>
 75        <scope>test</scope>
 76      </dependency>
 77      <dependency>
 78        <groupId>org.springframework.boot</groupId>
 79        <artifactId>spring-boot-starter-test</artifactId>
 80        <scope>test</scope>
 81      </dependency>
 82      <dependency>
 83        <groupId>com.h2database</groupId>
 84        <artifactId>h2</artifactId>
 85        <scope>test</scope>
 86      </dependency>
 87  
 88      <dependency>
 89        <groupId>au.com.dius</groupId>
 90        <artifactId>pact-jvm-provider-junit_2.11</artifactId>
 91        <version>3.5.0</version>
 92      </dependency>
 93    </dependencies>
 94  
 95    <build>
 96      <plugins>
 97        <plugin>
 98          <groupId>org.springframework.boot</groupId>
 99          <artifactId>spring-boot-maven-plugin</artifactId>
100          <version>${spring-boot.version}</version>
101          <executions>
102            <execution>
103              <goals>
104                <goal>repackage</goal>
105              </goals>
106            </execution>
```
  * file:///tmp/source-code/pom.xml
      * Use the Quarkus BOM to omit the version of the different Quarkus dependencies.. Add the following sections to the `pom.xml` file:. ```xml. <properties>. <quarkus.platform.artifact-id>quarkus-bom</quarkus.platform.artifact-id>. <quarkus.platform.group-id>io.quarkus.platform</quarkus.platform.group-id>. <quarkus.platform.version>3.1.0.Final</quarkus.platform.version>. </properties>. <dependencyManagement>. <dependencies>. <dependency>. <groupId>$</groupId>. <artifactId>$</artifactId>. <version>$</version>. <type>pom</type>. <scope>import</scope>. </dependency>. </dependencies>. </dependencyManagement>. ```. Check the latest Quarkus version available from the `Quarkus - Releases` link below.
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  3      <modelVersion>4.0.0</modelVersion>
  4      <groupId>org.jboss.examples.eap</groupId>
  5      <artifactId>ticket-monster-parent</artifactId>
  6      <version>3.0.0-SNAPSHOT</version>
  7      <modules>
  8          <module>monolith</module>
  9          <module>backend-v1</module>
 10          <module>backend-v2</module>
 11          <module>orders-service</module>
 12      </modules>
 13      <packaging>pom</packaging>
 14      <name>Ticket Monster Parent</name>
 15      <description>A starter HTML5 + REST webapp project for use on JBoss EAP.</description>
 16  
 17      <!-- Activate JBoss Product Maven repository.
 18  
 19          NOTE: Configuring the Maven repository in the pom.xml file is not a recommended procedure
 20          and is only done here to make it easier to use the quickstarts.
 21  
 22          For more information about how to configure Maven for your application,
 23          see the section entitled 'Use the Maven Repository'
 24          in the Development Guide for Red Hat JBoss Enterprise Application Platform located here:
 25  
 26          https://access.redhat.com/documentation/en-US/JBoss_Enterprise_Application_Platform/
 27      -->
 28      <repositories>
 29          <repository>
 30              <id>redhat-ga-repository</id>
 31              <url>https://maven.repository.redhat.com/ga/</url>
 32              <releases>
 33                  <enabled>true</enabled>
 34              </releases>
 35              <snapshots>
 36                  <enabled>false</enabled>
 37              </snapshots>
 38          </repository>
 39          <repository>
 40              <id>jboss-ga-repository</id>
 41              <url>http://maven.repository.redhat.com/techpreview/all</url>
 42              <releases>
 43                  <enabled>true</enabled>
 44              </releases>
 45              <snapshots>
 46                  <enabled>false</enabled>
 47              </snapshots>
 48          </repository>
 49          <repository>
 50              <id>jboss-earlyaccess-repository</id>
 51              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 52              <releases>
 53                  <enabled>true</enabled>
 54              </releases>
 55              <snapshots>
 56                  <enabled>false</enabled>
 57              </snapshots>
 58          </repository>
 59          <repository>
 60              <id>redhat.ea</id>
 61              <name>Red Hat Early Access Repository</name>
 62              <url>https://maven.repository.redhat.com/earlyaccess/all</url>
 63              <snapshots>
 64                  <enabled>false</enabled>
 65              </snapshots>
 66              <releases>
 67                  <enabled>true</enabled>
 68              </releases>
 69          </repository>
 70      </repositories>
 71  
 72      <pluginRepositories>
 73          <pluginRepository>
 74              <id>redhat-ga-repository</id>
 75              <url>https://maven.repository.redhat.com/ga/</url>
 76              <releases>
 77                  <enabled>true</enabled>
 78              </releases>
 79              <snapshots>
 80                  <enabled>false</enabled>
 81              </snapshots>
 82          </pluginRepository>
 83          <pluginRepository>
 84              <id>jboss-earlyaccess-plugin-repository</id>
 85              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 86              <releases>
 87                  <enabled>true</enabled>
 88              </releases>
 89              <snapshots>
 90                  <enabled>false</enabled>
 91              </snapshots>
 92          </pluginRepository>
 93      </pluginRepositories>
 94  
 95      <build>
 96          <plugins>
 97              <plugin>
 98                  <artifactId>maven-compiler-plugin</artifactId>
 99                  <version>2.3.1</version>
100                  <configuration>
101                      <source>1.8</source>
102                      <target>1.8</target>
103                  </configuration>
104              </plugin>
```
### #8 - javaee-pom-to-quarkus-00020
* Category: mandatory
* Effort: 1
* Description: Adopt Quarkus Maven plugin

* Labels: konveyor.io/source=java-ee, konveyor.io/target=quarkus
* Links
  * Quarkus - Guide: https://quarkus.io/guides/maven-tooling#build-tool-maven
* Incidents
  * file:///tmp/source-code/backend-v1/pom.xml
      * Use the Quarkus Maven plugin adding the following sections to the `pom.xml` file:. ```xml. <properties>. <quarkus.platform.group-id>io.quarkus.platform</quarkus.platform.group-id>. <quarkus.platform.version>3.1.0.Final</quarkus.platform.version>. </properties>. <build>. <plugins>. <plugin>. <groupId>$</groupId>. <artifactId>quarkus-maven-plugin</artifactId>. <version>$</version>. <extensions>true</extensions>. <executions>. <execution>. <goals>. <goal>build</goal>. <goal>generate-code</goal>. <goal>generate-code-tests</goal>. </goals>. </execution>. </executions>. </plugin>. </plugins>. </build>. ```
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  3      <modelVersion>4.0.0</modelVersion>
  4      <groupId>org.jboss.examples.eap</groupId>
  5      <artifactId>backend-v1</artifactId>
  6      <version>1.0</version>
  7      <packaging>war</packaging>
  8      <name>ticket-monster backend</name>
  9      <description>A starter HTML5 + REST webapp project for use on JBoss EAP.</description>
 10  
 11      <!-- Activate JBoss Product Maven repository.
 12  
 13          NOTE: Configuring the Maven repository in the pom.xml file is not a recommended procedure
 14          and is only done here to make it easier to use the quickstarts.
 15  
 16          For more information about how to configure Maven for your application,
 17          see the section entitled 'Use the Maven Repository'
 18          in the Development Guide for Red Hat JBoss Enterprise Application Platform located here:
 19  
 20          https://access.redhat.com/documentation/en-US/JBoss_Enterprise_Application_Platform/
 21      -->
 22      <repositories>
 23          <repository>
 24              <id>redhat-ga-repository</id>
 25              <url>https://maven.repository.redhat.com/ga/</url>
 26              <releases>
 27                  <enabled>true</enabled>
 28              </releases>
 29              <snapshots>
 30                  <enabled>false</enabled>
 31              </snapshots>
 32          </repository>
 33          <repository>
 34              <id>jboss-ga-repository</id>
 35              <url>http://maven.repository.redhat.com/techpreview/all</url>
 36              <releases>
 37                  <enabled>true</enabled>
 38              </releases>
 39              <snapshots>
 40                  <enabled>false</enabled>
 41              </snapshots>
 42          </repository>
 43          <repository>
 44              <id>jboss-earlyaccess-repository</id>
 45              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 46              <releases>
 47                  <enabled>true</enabled>
 48              </releases>
 49              <snapshots>
 50                  <enabled>false</enabled>
 51              </snapshots>
 52          </repository>
 53          <repository>
 54              <id>redhat.ea</id>
 55              <name>Red Hat Early Access Repository</name>
 56              <url>https://maven.repository.redhat.com/earlyaccess/all</url>
 57              <snapshots>
 58                  <enabled>false</enabled>
 59              </snapshots>
 60              <releases>
 61                  <enabled>true</enabled>
 62              </releases>
 63          </repository>
 64      </repositories>
 65  
 66      <pluginRepositories>
 67          <pluginRepository>
 68              <id>redhat-ga-repository</id>
 69              <url>https://maven.repository.redhat.com/ga/</url>
 70              <releases>
 71                  <enabled>true</enabled>
 72              </releases>
 73              <snapshots>
 74                  <enabled>false</enabled>
 75              </snapshots>
 76          </pluginRepository>
 77          <pluginRepository>
 78              <id>jboss-earlyaccess-plugin-repository</id>
 79              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 80              <releases>
 81                  <enabled>true</enabled>
 82              </releases>
 83              <snapshots>
 84                  <enabled>false</enabled>
 85              </snapshots>
 86          </pluginRepository>
 87      </pluginRepositories>
 88  
 89      <properties>
 90          <!-- Explicitly declaring the source encoding eliminates the following 
 91              message: -->
 92          <!-- [WARNING] Using platform encoding (UTF-8 actually) to copy filtered 
 93              resources, i.e. build is platform dependent! -->
 94          <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
 95          <!-- Timestamp format for the maven.build.timestamp property -->
 96          <!-- You can reference property in pom.xml or filtered resources 
 97              (must enable third-party plugin if using Maven < 2.1) -->
 98          <maven.build.timestamp.format>yyyyMMdd'T'HHmmss</maven.build.timestamp.format>
 99          <!-- Specify the JBoss EAP directory to be the JBOSS_HOME environment
100              variable -->
101          <jboss.home>${env.JBOSS_HOME}</jboss.home>
102          <version.jboss.bom.eap>7.0.7.GA</version.jboss.bom.eap>
103          <version.wildfly.maven.plugin>1.0.2.Final</version.wildfly.maven.plugin>
104          <version.surefire.plugin>2.10</version.surefire.plugin>
```
  * file:///tmp/source-code/backend-v2/pom.xml
      * Use the Quarkus Maven plugin adding the following sections to the `pom.xml` file:. ```xml. <properties>. <quarkus.platform.group-id>io.quarkus.platform</quarkus.platform.group-id>. <quarkus.platform.version>3.1.0.Final</quarkus.platform.version>. </properties>. <build>. <plugins>. <plugin>. <groupId>$</groupId>. <artifactId>quarkus-maven-plugin</artifactId>. <version>$</version>. <extensions>true</extensions>. <executions>. <execution>. <goals>. <goal>build</goal>. <goal>generate-code</goal>. <goal>generate-code-tests</goal>. </goals>. </execution>. </executions>. </plugin>. </plugins>. </build>. ```
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  3      <modelVersion>4.0.0</modelVersion>
  4      <groupId>org.jboss.examples.eap</groupId>
  5      <artifactId>backend-v2</artifactId>
  6      <version>2.0</version>
  7      <packaging>war</packaging>
  8      <name>ticket-monster backend v2</name>
  9      <description>A starter HTML5 + REST webapp project for use on JBoss EAP.</description>
 10  
 11      <!-- Activate JBoss Product Maven repository.
 12  
 13          NOTE: Configuring the Maven repository in the pom.xml file is not a recommended procedure
 14          and is only done here to make it easier to use the quickstarts.
 15  
 16          For more information about how to configure Maven for your application,
 17          see the section entitled 'Use the Maven Repository'
 18          in the Development Guide for Red Hat JBoss Enterprise Application Platform located here:
 19  
 20          https://access.redhat.com/documentation/en-US/JBoss_Enterprise_Application_Platform/
 21      -->
 22      <repositories>
 23          <repository>
 24              <id>redhat-ga-repository</id>
 25              <url>https://maven.repository.redhat.com/ga/</url>
 26              <releases>
 27                  <enabled>true</enabled>
 28              </releases>
 29              <snapshots>
 30                  <enabled>false</enabled>
 31              </snapshots>
 32          </repository>
 33          <repository>
 34              <id>jboss-ga-repository</id>
 35              <url>http://maven.repository.redhat.com/techpreview/all</url>
 36              <releases>
 37                  <enabled>true</enabled>
 38              </releases>
 39              <snapshots>
 40                  <enabled>false</enabled>
 41              </snapshots>
 42          </repository>
 43          <repository>
 44              <id>jboss-earlyaccess-repository</id>
 45              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 46              <releases>
 47                  <enabled>true</enabled>
 48              </releases>
 49              <snapshots>
 50                  <enabled>false</enabled>
 51              </snapshots>
 52          </repository>
 53          <repository>
 54              <id>redhat.ea</id>
 55              <name>Red Hat Early Access Repository</name>
 56              <url>https://maven.repository.redhat.com/earlyaccess/all</url>
 57              <snapshots>
 58                  <enabled>false</enabled>
 59              </snapshots>
 60              <releases>
 61                  <enabled>true</enabled>
 62              </releases>
 63          </repository>
 64      </repositories>
 65  
 66      <pluginRepositories>
 67          <pluginRepository>
 68              <id>redhat-ga-repository</id>
 69              <url>https://maven.repository.redhat.com/ga/</url>
 70              <releases>
 71                  <enabled>true</enabled>
 72              </releases>
 73              <snapshots>
 74                  <enabled>false</enabled>
 75              </snapshots>
 76          </pluginRepository>
 77          <pluginRepository>
 78              <id>jboss-earlyaccess-plugin-repository</id>
 79              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 80              <releases>
 81                  <enabled>true</enabled>
 82              </releases>
 83              <snapshots>
 84                  <enabled>false</enabled>
 85              </snapshots>
 86          </pluginRepository>
 87      </pluginRepositories>
 88  
 89      <properties>
 90          <!-- Explicitly declaring the source encoding eliminates the following 
 91              message: -->
 92          <!-- [WARNING] Using platform encoding (UTF-8 actually) to copy filtered 
 93              resources, i.e. build is platform dependent! -->
 94          <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
 95          <!-- Timestamp format for the maven.build.timestamp property -->
 96          <!-- You can reference property in pom.xml or filtered resources 
 97              (must enable third-party plugin if using Maven < 2.1) -->
 98          <maven.build.timestamp.format>yyyyMMdd'T'HHmmss</maven.build.timestamp.format>
 99          <!-- Specify the JBoss EAP directory to be the JBOSS_HOME environment
100              variable -->
101          <jboss.home>${env.JBOSS_HOME}</jboss.home>
102          <version.jboss.bom.eap>7.0.7.GA</version.jboss.bom.eap>
103          <version.wildfly.maven.plugin>1.0.2.Final</version.wildfly.maven.plugin>
104          <version.surefire.plugin>2.10</version.surefire.plugin>
```
  * file:///tmp/source-code/monolith/pom.xml
      * Use the Quarkus Maven plugin adding the following sections to the `pom.xml` file:. ```xml. <properties>. <quarkus.platform.group-id>io.quarkus.platform</quarkus.platform.group-id>. <quarkus.platform.version>3.1.0.Final</quarkus.platform.version>. </properties>. <build>. <plugins>. <plugin>. <groupId>$</groupId>. <artifactId>quarkus-maven-plugin</artifactId>. <version>$</version>. <extensions>true</extensions>. <executions>. <execution>. <goals>. <goal>build</goal>. <goal>generate-code</goal>. <goal>generate-code-tests</goal>. </goals>. </execution>. </executions>. </plugin>. </plugins>. </build>. ```
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  3      <modelVersion>4.0.0</modelVersion>
  4      <groupId>org.jboss.examples.eap</groupId>
  5      <artifactId>ticket-monster</artifactId>
  6      <version>3.0.0-SNAPSHOT</version>
  7      <packaging>war</packaging>
  8      <name>ticket-monster</name>
  9      <description>A starter HTML5 + REST webapp project for use on JBoss EAP.</description>
 10  
 11      <!-- Activate JBoss Product Maven repository.
 12  
 13          NOTE: Configuring the Maven repository in the pom.xml file is not a recommended procedure
 14          and is only done here to make it easier to use the quickstarts.
 15  
 16          For more information about how to configure Maven for your application,
 17          see the section entitled 'Use the Maven Repository'
 18          in the Development Guide for Red Hat JBoss Enterprise Application Platform located here:
 19  
 20          https://access.redhat.com/documentation/en-US/JBoss_Enterprise_Application_Platform/
 21      -->
 22      <repositories>
 23          <repository>
 24              <id>redhat-ga-repository</id>
 25              <url>https://maven.repository.redhat.com/ga/</url>
 26              <releases>
 27                  <enabled>true</enabled>
 28              </releases>
 29              <snapshots>
 30                  <enabled>false</enabled>
 31              </snapshots>
 32          </repository>
 33          <repository>
 34              <id>jboss-ga-repository</id>
 35              <url>http://maven.repository.redhat.com/techpreview/all</url>
 36              <releases>
 37                  <enabled>true</enabled>
 38              </releases>
 39              <snapshots>
 40                  <enabled>false</enabled>
 41              </snapshots>
 42          </repository>
 43          <repository>
 44              <id>jboss-earlyaccess-repository</id>
 45              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 46              <releases>
 47                  <enabled>true</enabled>
 48              </releases>
 49              <snapshots>
 50                  <enabled>false</enabled>
 51              </snapshots>
 52          </repository>
 53          <repository>
 54              <id>redhat.ea</id>
 55              <name>Red Hat Early Access Repository</name>
 56              <url>https://maven.repository.redhat.com/earlyaccess/all</url>
 57              <snapshots>
 58                  <enabled>false</enabled>
 59              </snapshots>
 60              <releases>
 61                  <enabled>true</enabled>
 62              </releases>
 63          </repository>
 64      </repositories>
 65  
 66      <pluginRepositories>
 67          <pluginRepository>
 68              <id>redhat-ga-repository</id>
 69              <url>https://maven.repository.redhat.com/ga/</url>
 70              <releases>
 71                  <enabled>true</enabled>
 72              </releases>
 73              <snapshots>
 74                  <enabled>false</enabled>
 75              </snapshots>
 76          </pluginRepository>
 77          <pluginRepository>
 78              <id>jboss-earlyaccess-plugin-repository</id>
 79              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 80              <releases>
 81                  <enabled>true</enabled>
 82              </releases>
 83              <snapshots>
 84                  <enabled>false</enabled>
 85              </snapshots>
 86          </pluginRepository>
 87      </pluginRepositories>
 88  
 89      <properties>
 90          <!-- Explicitly declaring the source encoding eliminates the following 
 91              message: -->
 92          <!-- [WARNING] Using platform encoding (UTF-8 actually) to copy filtered 
 93              resources, i.e. build is platform dependent! -->
 94          <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
 95          <!-- Timestamp format for the maven.build.timestamp property -->
 96          <!-- You can reference property in pom.xml or filtered resources 
 97              (must enable third-party plugin if using Maven < 2.1) -->
 98          <maven.build.timestamp.format>yyyyMMdd'T'HHmmss</maven.build.timestamp.format>
 99          <!-- Specify the JBoss EAP directory to be the JBOSS_HOME environment
100              variable -->
101          <jboss.home>${env.JBOSS_HOME}</jboss.home>
102          <version.jboss.bom.eap>7.0.7.GA</version.jboss.bom.eap>
103          <version.wildfly.maven.plugin>1.0.2.Final</version.wildfly.maven.plugin>
104          <version.surefire.plugin>2.10</version.surefire.plugin>
```
  * file:///tmp/source-code/orders-service/pom.xml
      * Use the Quarkus Maven plugin adding the following sections to the `pom.xml` file:. ```xml. <properties>. <quarkus.platform.group-id>io.quarkus.platform</quarkus.platform.group-id>. <quarkus.platform.version>3.1.0.Final</quarkus.platform.version>. </properties>. <build>. <plugins>. <plugin>. <groupId>$</groupId>. <artifactId>quarkus-maven-plugin</artifactId>. <version>$</version>. <extensions>true</extensions>. <executions>. <execution>. <goals>. <goal>build</goal>. <goal>generate-code</goal>. <goal>generate-code-tests</goal>. </goals>. </execution>. </executions>. </plugin>. </plugins>. </build>. ```
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <project xmlns="http://maven.apache.org/POM/4.0.0"
  3           xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  4           xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  5    <artifactId>orders-service</artifactId>
  6    <groupId>org.ticketmonster.orders</groupId>
  7    <version>1.0.0-SNAPSHOT</version>
  8    <modelVersion>4.0.0</modelVersion>
  9  
 10    <properties>
 11      <spring-boot.version>1.5.6.RELEASE</spring-boot.version>
 12      <docker-maven-plugin.version>0.20.1</docker-maven-plugin.version>
 13      <mysql-server.version>5.7</mysql-server.version>
 14      <mysql.user>ticket</mysql.user>
 15      <mysql.password>monster</mysql.password>
 16      <mysql.port>3306</mysql.port>
 17      <mysql.init.timeout>60000</mysql.init.timeout>
 18      <skipITs>true</skipITs>
 19      <fabric8.maven.plugin.version>3.5.25</fabric8.maven.plugin.version>
 20      <docker.image.name>ceposta/%a:%l</docker.image.name>
 21    </properties>
 22  
 23    <dependencyManagement>
 24      <dependencies>
 25        <dependency>
 26          <!-- Import dependency management from Spring Boot -->
 27          <groupId>org.springframework.boot</groupId>
 28          <artifactId>spring-boot-dependencies</artifactId>
 29          <version>${spring-boot.version}</version>
 30          <type>pom</type>
 31          <scope>import</scope>
 32        </dependency>
 33      </dependencies>
 34    </dependencyManagement>
 35  
 36  
 37    <dependencies>
 38      <dependency>
 39        <groupId>org.springframework.boot</groupId>
 40        <artifactId>spring-boot-starter-web</artifactId>
 41      </dependency>
 42      <dependency>
 43        <groupId>org.springframework.boot</groupId>
 44        <artifactId>spring-boot-starter-actuator</artifactId>
 45      </dependency>
 46      <dependency>
 47        <groupId>org.springframework.boot</groupId>
 48        <artifactId>spring-boot-starter-data-jpa</artifactId>
 49      </dependency>
 50      <dependency>
 51        <groupId>org.teiid.spring</groupId>
 52        <artifactId>teiid-spring-boot-starter</artifactId>
 53        <version>1.0.0-SNAPSHOT</version>
 54      </dependency>
 55  
 56  
 57  
 58      <!-- Testing -->
 59      <dependency>
 60        <groupId>io.rest-assured</groupId>
 61        <artifactId>rest-assured</artifactId>
 62        <version>3.0.3</version>
 63        <scope>test</scope>
 64      </dependency>
 65      <dependency>
 66        <groupId>io.rest-assured</groupId>
 67        <artifactId>json-schema-validator</artifactId>
 68        <version>3.0.3</version>
 69        <scope>test</scope>
 70      </dependency>
 71      <dependency>
 72        <groupId>io.specto</groupId>
 73        <artifactId>hoverfly-java</artifactId>
 74        <version>0.8.0</version>
 75        <scope>test</scope>
 76      </dependency>
 77      <dependency>
 78        <groupId>org.springframework.boot</groupId>
 79        <artifactId>spring-boot-starter-test</artifactId>
 80        <scope>test</scope>
 81      </dependency>
 82      <dependency>
 83        <groupId>com.h2database</groupId>
 84        <artifactId>h2</artifactId>
 85        <scope>test</scope>
 86      </dependency>
 87  
 88      <dependency>
 89        <groupId>au.com.dius</groupId>
 90        <artifactId>pact-jvm-provider-junit_2.11</artifactId>
 91        <version>3.5.0</version>
 92      </dependency>
 93    </dependencies>
 94  
 95    <build>
 96      <plugins>
 97        <plugin>
 98          <groupId>org.springframework.boot</groupId>
 99          <artifactId>spring-boot-maven-plugin</artifactId>
100          <version>${spring-boot.version}</version>
101          <executions>
102            <execution>
103              <goals>
104                <goal>repackage</goal>
105              </goals>
106            </execution>
```
  * file:///tmp/source-code/pom.xml
      * Use the Quarkus Maven plugin adding the following sections to the `pom.xml` file:. ```xml. <properties>. <quarkus.platform.group-id>io.quarkus.platform</quarkus.platform.group-id>. <quarkus.platform.version>3.1.0.Final</quarkus.platform.version>. </properties>. <build>. <plugins>. <plugin>. <groupId>$</groupId>. <artifactId>quarkus-maven-plugin</artifactId>. <version>$</version>. <extensions>true</extensions>. <executions>. <execution>. <goals>. <goal>build</goal>. <goal>generate-code</goal>. <goal>generate-code-tests</goal>. </goals>. </execution>. </executions>. </plugin>. </plugins>. </build>. ```
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  3      <modelVersion>4.0.0</modelVersion>
  4      <groupId>org.jboss.examples.eap</groupId>
  5      <artifactId>ticket-monster-parent</artifactId>
  6      <version>3.0.0-SNAPSHOT</version>
  7      <modules>
  8          <module>monolith</module>
  9          <module>backend-v1</module>
 10          <module>backend-v2</module>
 11          <module>orders-service</module>
 12      </modules>
 13      <packaging>pom</packaging>
 14      <name>Ticket Monster Parent</name>
 15      <description>A starter HTML5 + REST webapp project for use on JBoss EAP.</description>
 16  
 17      <!-- Activate JBoss Product Maven repository.
 18  
 19          NOTE: Configuring the Maven repository in the pom.xml file is not a recommended procedure
 20          and is only done here to make it easier to use the quickstarts.
 21  
 22          For more information about how to configure Maven for your application,
 23          see the section entitled 'Use the Maven Repository'
 24          in the Development Guide for Red Hat JBoss Enterprise Application Platform located here:
 25  
 26          https://access.redhat.com/documentation/en-US/JBoss_Enterprise_Application_Platform/
 27      -->
 28      <repositories>
 29          <repository>
 30              <id>redhat-ga-repository</id>
 31              <url>https://maven.repository.redhat.com/ga/</url>
 32              <releases>
 33                  <enabled>true</enabled>
 34              </releases>
 35              <snapshots>
 36                  <enabled>false</enabled>
 37              </snapshots>
 38          </repository>
 39          <repository>
 40              <id>jboss-ga-repository</id>
 41              <url>http://maven.repository.redhat.com/techpreview/all</url>
 42              <releases>
 43                  <enabled>true</enabled>
 44              </releases>
 45              <snapshots>
 46                  <enabled>false</enabled>
 47              </snapshots>
 48          </repository>
 49          <repository>
 50              <id>jboss-earlyaccess-repository</id>
 51              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 52              <releases>
 53                  <enabled>true</enabled>
 54              </releases>
 55              <snapshots>
 56                  <enabled>false</enabled>
 57              </snapshots>
 58          </repository>
 59          <repository>
 60              <id>redhat.ea</id>
 61              <name>Red Hat Early Access Repository</name>
 62              <url>https://maven.repository.redhat.com/earlyaccess/all</url>
 63              <snapshots>
 64                  <enabled>false</enabled>
 65              </snapshots>
 66              <releases>
 67                  <enabled>true</enabled>
 68              </releases>
 69          </repository>
 70      </repositories>
 71  
 72      <pluginRepositories>
 73          <pluginRepository>
 74              <id>redhat-ga-repository</id>
 75              <url>https://maven.repository.redhat.com/ga/</url>
 76              <releases>
 77                  <enabled>true</enabled>
 78              </releases>
 79              <snapshots>
 80                  <enabled>false</enabled>
 81              </snapshots>
 82          </pluginRepository>
 83          <pluginRepository>
 84              <id>jboss-earlyaccess-plugin-repository</id>
 85              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 86              <releases>
 87                  <enabled>true</enabled>
 88              </releases>
 89              <snapshots>
 90                  <enabled>false</enabled>
 91              </snapshots>
 92          </pluginRepository>
 93      </pluginRepositories>
 94  
 95      <build>
 96          <plugins>
 97              <plugin>
 98                  <artifactId>maven-compiler-plugin</artifactId>
 99                  <version>2.3.1</version>
100                  <configuration>
101                      <source>1.8</source>
102                      <target>1.8</target>
103                  </configuration>
104              </plugin>
```
### #9 - javaee-pom-to-quarkus-00030
* Category: mandatory
* Effort: 1
* Description: Adopt Maven Compiler plugin

* Labels: konveyor.io/source=java-ee, konveyor.io/target=quarkus
* Links
  * Quarkus - Guide: https://quarkus.io/guides/maven-tooling#build-tool-maven
* Incidents
  * file:///tmp/source-code/backend-v1/pom.xml
      * Use the Maven Compiler plugin adding the following sections to the `pom.xml` file:. ```xml. <properties>. <compiler-plugin.version>3.10.1</compiler-plugin.version>. <maven.compiler.release>11</maven.compiler.release>. </properties>. <build>. <plugins>. <plugin>. <artifactId>maven-compiler-plugin</artifactId>. <version>$</version>. <configuration>. <compilerArgs>. <arg>-parameters</arg>. </compilerArgs>. </configuration>. </plugin>. </plugins>. </build>. ```
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  3      <modelVersion>4.0.0</modelVersion>
  4      <groupId>org.jboss.examples.eap</groupId>
  5      <artifactId>backend-v1</artifactId>
  6      <version>1.0</version>
  7      <packaging>war</packaging>
  8      <name>ticket-monster backend</name>
  9      <description>A starter HTML5 + REST webapp project for use on JBoss EAP.</description>
 10  
 11      <!-- Activate JBoss Product Maven repository.
 12  
 13          NOTE: Configuring the Maven repository in the pom.xml file is not a recommended procedure
 14          and is only done here to make it easier to use the quickstarts.
 15  
 16          For more information about how to configure Maven for your application,
 17          see the section entitled 'Use the Maven Repository'
 18          in the Development Guide for Red Hat JBoss Enterprise Application Platform located here:
 19  
 20          https://access.redhat.com/documentation/en-US/JBoss_Enterprise_Application_Platform/
 21      -->
 22      <repositories>
 23          <repository>
 24              <id>redhat-ga-repository</id>
 25              <url>https://maven.repository.redhat.com/ga/</url>
 26              <releases>
 27                  <enabled>true</enabled>
 28              </releases>
 29              <snapshots>
 30                  <enabled>false</enabled>
 31              </snapshots>
 32          </repository>
 33          <repository>
 34              <id>jboss-ga-repository</id>
 35              <url>http://maven.repository.redhat.com/techpreview/all</url>
 36              <releases>
 37                  <enabled>true</enabled>
 38              </releases>
 39              <snapshots>
 40                  <enabled>false</enabled>
 41              </snapshots>
 42          </repository>
 43          <repository>
 44              <id>jboss-earlyaccess-repository</id>
 45              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 46              <releases>
 47                  <enabled>true</enabled>
 48              </releases>
 49              <snapshots>
 50                  <enabled>false</enabled>
 51              </snapshots>
 52          </repository>
 53          <repository>
 54              <id>redhat.ea</id>
 55              <name>Red Hat Early Access Repository</name>
 56              <url>https://maven.repository.redhat.com/earlyaccess/all</url>
 57              <snapshots>
 58                  <enabled>false</enabled>
 59              </snapshots>
 60              <releases>
 61                  <enabled>true</enabled>
 62              </releases>
 63          </repository>
 64      </repositories>
 65  
 66      <pluginRepositories>
 67          <pluginRepository>
 68              <id>redhat-ga-repository</id>
 69              <url>https://maven.repository.redhat.com/ga/</url>
 70              <releases>
 71                  <enabled>true</enabled>
 72              </releases>
 73              <snapshots>
 74                  <enabled>false</enabled>
 75              </snapshots>
 76          </pluginRepository>
 77          <pluginRepository>
 78              <id>jboss-earlyaccess-plugin-repository</id>
 79              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 80              <releases>
 81                  <enabled>true</enabled>
 82              </releases>
 83              <snapshots>
 84                  <enabled>false</enabled>
 85              </snapshots>
 86          </pluginRepository>
 87      </pluginRepositories>
 88  
 89      <properties>
 90          <!-- Explicitly declaring the source encoding eliminates the following 
 91              message: -->
 92          <!-- [WARNING] Using platform encoding (UTF-8 actually) to copy filtered 
 93              resources, i.e. build is platform dependent! -->
 94          <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
 95          <!-- Timestamp format for the maven.build.timestamp property -->
 96          <!-- You can reference property in pom.xml or filtered resources 
 97              (must enable third-party plugin if using Maven < 2.1) -->
 98          <maven.build.timestamp.format>yyyyMMdd'T'HHmmss</maven.build.timestamp.format>
 99          <!-- Specify the JBoss EAP directory to be the JBOSS_HOME environment
100              variable -->
101          <jboss.home>${env.JBOSS_HOME}</jboss.home>
102          <version.jboss.bom.eap>7.0.7.GA</version.jboss.bom.eap>
103          <version.wildfly.maven.plugin>1.0.2.Final</version.wildfly.maven.plugin>
104          <version.surefire.plugin>2.10</version.surefire.plugin>
```
  * file:///tmp/source-code/backend-v2/pom.xml
      * Use the Maven Compiler plugin adding the following sections to the `pom.xml` file:. ```xml. <properties>. <compiler-plugin.version>3.10.1</compiler-plugin.version>. <maven.compiler.release>11</maven.compiler.release>. </properties>. <build>. <plugins>. <plugin>. <artifactId>maven-compiler-plugin</artifactId>. <version>$</version>. <configuration>. <compilerArgs>. <arg>-parameters</arg>. </compilerArgs>. </configuration>. </plugin>. </plugins>. </build>. ```
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  3      <modelVersion>4.0.0</modelVersion>
  4      <groupId>org.jboss.examples.eap</groupId>
  5      <artifactId>backend-v2</artifactId>
  6      <version>2.0</version>
  7      <packaging>war</packaging>
  8      <name>ticket-monster backend v2</name>
  9      <description>A starter HTML5 + REST webapp project for use on JBoss EAP.</description>
 10  
 11      <!-- Activate JBoss Product Maven repository.
 12  
 13          NOTE: Configuring the Maven repository in the pom.xml file is not a recommended procedure
 14          and is only done here to make it easier to use the quickstarts.
 15  
 16          For more information about how to configure Maven for your application,
 17          see the section entitled 'Use the Maven Repository'
 18          in the Development Guide for Red Hat JBoss Enterprise Application Platform located here:
 19  
 20          https://access.redhat.com/documentation/en-US/JBoss_Enterprise_Application_Platform/
 21      -->
 22      <repositories>
 23          <repository>
 24              <id>redhat-ga-repository</id>
 25              <url>https://maven.repository.redhat.com/ga/</url>
 26              <releases>
 27                  <enabled>true</enabled>
 28              </releases>
 29              <snapshots>
 30                  <enabled>false</enabled>
 31              </snapshots>
 32          </repository>
 33          <repository>
 34              <id>jboss-ga-repository</id>
 35              <url>http://maven.repository.redhat.com/techpreview/all</url>
 36              <releases>
 37                  <enabled>true</enabled>
 38              </releases>
 39              <snapshots>
 40                  <enabled>false</enabled>
 41              </snapshots>
 42          </repository>
 43          <repository>
 44              <id>jboss-earlyaccess-repository</id>
 45              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 46              <releases>
 47                  <enabled>true</enabled>
 48              </releases>
 49              <snapshots>
 50                  <enabled>false</enabled>
 51              </snapshots>
 52          </repository>
 53          <repository>
 54              <id>redhat.ea</id>
 55              <name>Red Hat Early Access Repository</name>
 56              <url>https://maven.repository.redhat.com/earlyaccess/all</url>
 57              <snapshots>
 58                  <enabled>false</enabled>
 59              </snapshots>
 60              <releases>
 61                  <enabled>true</enabled>
 62              </releases>
 63          </repository>
 64      </repositories>
 65  
 66      <pluginRepositories>
 67          <pluginRepository>
 68              <id>redhat-ga-repository</id>
 69              <url>https://maven.repository.redhat.com/ga/</url>
 70              <releases>
 71                  <enabled>true</enabled>
 72              </releases>
 73              <snapshots>
 74                  <enabled>false</enabled>
 75              </snapshots>
 76          </pluginRepository>
 77          <pluginRepository>
 78              <id>jboss-earlyaccess-plugin-repository</id>
 79              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 80              <releases>
 81                  <enabled>true</enabled>
 82              </releases>
 83              <snapshots>
 84                  <enabled>false</enabled>
 85              </snapshots>
 86          </pluginRepository>
 87      </pluginRepositories>
 88  
 89      <properties>
 90          <!-- Explicitly declaring the source encoding eliminates the following 
 91              message: -->
 92          <!-- [WARNING] Using platform encoding (UTF-8 actually) to copy filtered 
 93              resources, i.e. build is platform dependent! -->
 94          <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
 95          <!-- Timestamp format for the maven.build.timestamp property -->
 96          <!-- You can reference property in pom.xml or filtered resources 
 97              (must enable third-party plugin if using Maven < 2.1) -->
 98          <maven.build.timestamp.format>yyyyMMdd'T'HHmmss</maven.build.timestamp.format>
 99          <!-- Specify the JBoss EAP directory to be the JBOSS_HOME environment
100              variable -->
101          <jboss.home>${env.JBOSS_HOME}</jboss.home>
102          <version.jboss.bom.eap>7.0.7.GA</version.jboss.bom.eap>
103          <version.wildfly.maven.plugin>1.0.2.Final</version.wildfly.maven.plugin>
104          <version.surefire.plugin>2.10</version.surefire.plugin>
```
  * file:///tmp/source-code/monolith/pom.xml
      * Use the Maven Compiler plugin adding the following sections to the `pom.xml` file:. ```xml. <properties>. <compiler-plugin.version>3.10.1</compiler-plugin.version>. <maven.compiler.release>11</maven.compiler.release>. </properties>. <build>. <plugins>. <plugin>. <artifactId>maven-compiler-plugin</artifactId>. <version>$</version>. <configuration>. <compilerArgs>. <arg>-parameters</arg>. </compilerArgs>. </configuration>. </plugin>. </plugins>. </build>. ```
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  3      <modelVersion>4.0.0</modelVersion>
  4      <groupId>org.jboss.examples.eap</groupId>
  5      <artifactId>ticket-monster</artifactId>
  6      <version>3.0.0-SNAPSHOT</version>
  7      <packaging>war</packaging>
  8      <name>ticket-monster</name>
  9      <description>A starter HTML5 + REST webapp project for use on JBoss EAP.</description>
 10  
 11      <!-- Activate JBoss Product Maven repository.
 12  
 13          NOTE: Configuring the Maven repository in the pom.xml file is not a recommended procedure
 14          and is only done here to make it easier to use the quickstarts.
 15  
 16          For more information about how to configure Maven for your application,
 17          see the section entitled 'Use the Maven Repository'
 18          in the Development Guide for Red Hat JBoss Enterprise Application Platform located here:
 19  
 20          https://access.redhat.com/documentation/en-US/JBoss_Enterprise_Application_Platform/
 21      -->
 22      <repositories>
 23          <repository>
 24              <id>redhat-ga-repository</id>
 25              <url>https://maven.repository.redhat.com/ga/</url>
 26              <releases>
 27                  <enabled>true</enabled>
 28              </releases>
 29              <snapshots>
 30                  <enabled>false</enabled>
 31              </snapshots>
 32          </repository>
 33          <repository>
 34              <id>jboss-ga-repository</id>
 35              <url>http://maven.repository.redhat.com/techpreview/all</url>
 36              <releases>
 37                  <enabled>true</enabled>
 38              </releases>
 39              <snapshots>
 40                  <enabled>false</enabled>
 41              </snapshots>
 42          </repository>
 43          <repository>
 44              <id>jboss-earlyaccess-repository</id>
 45              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 46              <releases>
 47                  <enabled>true</enabled>
 48              </releases>
 49              <snapshots>
 50                  <enabled>false</enabled>
 51              </snapshots>
 52          </repository>
 53          <repository>
 54              <id>redhat.ea</id>
 55              <name>Red Hat Early Access Repository</name>
 56              <url>https://maven.repository.redhat.com/earlyaccess/all</url>
 57              <snapshots>
 58                  <enabled>false</enabled>
 59              </snapshots>
 60              <releases>
 61                  <enabled>true</enabled>
 62              </releases>
 63          </repository>
 64      </repositories>
 65  
 66      <pluginRepositories>
 67          <pluginRepository>
 68              <id>redhat-ga-repository</id>
 69              <url>https://maven.repository.redhat.com/ga/</url>
 70              <releases>
 71                  <enabled>true</enabled>
 72              </releases>
 73              <snapshots>
 74                  <enabled>false</enabled>
 75              </snapshots>
 76          </pluginRepository>
 77          <pluginRepository>
 78              <id>jboss-earlyaccess-plugin-repository</id>
 79              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 80              <releases>
 81                  <enabled>true</enabled>
 82              </releases>
 83              <snapshots>
 84                  <enabled>false</enabled>
 85              </snapshots>
 86          </pluginRepository>
 87      </pluginRepositories>
 88  
 89      <properties>
 90          <!-- Explicitly declaring the source encoding eliminates the following 
 91              message: -->
 92          <!-- [WARNING] Using platform encoding (UTF-8 actually) to copy filtered 
 93              resources, i.e. build is platform dependent! -->
 94          <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
 95          <!-- Timestamp format for the maven.build.timestamp property -->
 96          <!-- You can reference property in pom.xml or filtered resources 
 97              (must enable third-party plugin if using Maven < 2.1) -->
 98          <maven.build.timestamp.format>yyyyMMdd'T'HHmmss</maven.build.timestamp.format>
 99          <!-- Specify the JBoss EAP directory to be the JBOSS_HOME environment
100              variable -->
101          <jboss.home>${env.JBOSS_HOME}</jboss.home>
102          <version.jboss.bom.eap>7.0.7.GA</version.jboss.bom.eap>
103          <version.wildfly.maven.plugin>1.0.2.Final</version.wildfly.maven.plugin>
104          <version.surefire.plugin>2.10</version.surefire.plugin>
```
  * file:///tmp/source-code/orders-service/pom.xml
      * Use the Maven Compiler plugin adding the following sections to the `pom.xml` file:. ```xml. <properties>. <compiler-plugin.version>3.10.1</compiler-plugin.version>. <maven.compiler.release>11</maven.compiler.release>. </properties>. <build>. <plugins>. <plugin>. <artifactId>maven-compiler-plugin</artifactId>. <version>$</version>. <configuration>. <compilerArgs>. <arg>-parameters</arg>. </compilerArgs>. </configuration>. </plugin>. </plugins>. </build>. ```
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <project xmlns="http://maven.apache.org/POM/4.0.0"
  3           xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  4           xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  5    <artifactId>orders-service</artifactId>
  6    <groupId>org.ticketmonster.orders</groupId>
  7    <version>1.0.0-SNAPSHOT</version>
  8    <modelVersion>4.0.0</modelVersion>
  9  
 10    <properties>
 11      <spring-boot.version>1.5.6.RELEASE</spring-boot.version>
 12      <docker-maven-plugin.version>0.20.1</docker-maven-plugin.version>
 13      <mysql-server.version>5.7</mysql-server.version>
 14      <mysql.user>ticket</mysql.user>
 15      <mysql.password>monster</mysql.password>
 16      <mysql.port>3306</mysql.port>
 17      <mysql.init.timeout>60000</mysql.init.timeout>
 18      <skipITs>true</skipITs>
 19      <fabric8.maven.plugin.version>3.5.25</fabric8.maven.plugin.version>
 20      <docker.image.name>ceposta/%a:%l</docker.image.name>
 21    </properties>
 22  
 23    <dependencyManagement>
 24      <dependencies>
 25        <dependency>
 26          <!-- Import dependency management from Spring Boot -->
 27          <groupId>org.springframework.boot</groupId>
 28          <artifactId>spring-boot-dependencies</artifactId>
 29          <version>${spring-boot.version}</version>
 30          <type>pom</type>
 31          <scope>import</scope>
 32        </dependency>
 33      </dependencies>
 34    </dependencyManagement>
 35  
 36  
 37    <dependencies>
 38      <dependency>
 39        <groupId>org.springframework.boot</groupId>
 40        <artifactId>spring-boot-starter-web</artifactId>
 41      </dependency>
 42      <dependency>
 43        <groupId>org.springframework.boot</groupId>
 44        <artifactId>spring-boot-starter-actuator</artifactId>
 45      </dependency>
 46      <dependency>
 47        <groupId>org.springframework.boot</groupId>
 48        <artifactId>spring-boot-starter-data-jpa</artifactId>
 49      </dependency>
 50      <dependency>
 51        <groupId>org.teiid.spring</groupId>
 52        <artifactId>teiid-spring-boot-starter</artifactId>
 53        <version>1.0.0-SNAPSHOT</version>
 54      </dependency>
 55  
 56  
 57  
 58      <!-- Testing -->
 59      <dependency>
 60        <groupId>io.rest-assured</groupId>
 61        <artifactId>rest-assured</artifactId>
 62        <version>3.0.3</version>
 63        <scope>test</scope>
 64      </dependency>
 65      <dependency>
 66        <groupId>io.rest-assured</groupId>
 67        <artifactId>json-schema-validator</artifactId>
 68        <version>3.0.3</version>
 69        <scope>test</scope>
 70      </dependency>
 71      <dependency>
 72        <groupId>io.specto</groupId>
 73        <artifactId>hoverfly-java</artifactId>
 74        <version>0.8.0</version>
 75        <scope>test</scope>
 76      </dependency>
 77      <dependency>
 78        <groupId>org.springframework.boot</groupId>
 79        <artifactId>spring-boot-starter-test</artifactId>
 80        <scope>test</scope>
 81      </dependency>
 82      <dependency>
 83        <groupId>com.h2database</groupId>
 84        <artifactId>h2</artifactId>
 85        <scope>test</scope>
 86      </dependency>
 87  
 88      <dependency>
 89        <groupId>au.com.dius</groupId>
 90        <artifactId>pact-jvm-provider-junit_2.11</artifactId>
 91        <version>3.5.0</version>
 92      </dependency>
 93    </dependencies>
 94  
 95    <build>
 96      <plugins>
 97        <plugin>
 98          <groupId>org.springframework.boot</groupId>
 99          <artifactId>spring-boot-maven-plugin</artifactId>
100          <version>${spring-boot.version}</version>
101          <executions>
102            <execution>
103              <goals>
104                <goal>repackage</goal>
105              </goals>
106            </execution>
```
  * file:///tmp/source-code/pom.xml
      * Use the Maven Compiler plugin adding the following sections to the `pom.xml` file:. ```xml. <properties>. <compiler-plugin.version>3.10.1</compiler-plugin.version>. <maven.compiler.release>11</maven.compiler.release>. </properties>. <build>. <plugins>. <plugin>. <artifactId>maven-compiler-plugin</artifactId>. <version>$</version>. <configuration>. <compilerArgs>. <arg>-parameters</arg>. </compilerArgs>. </configuration>. </plugin>. </plugins>. </build>. ```
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  3      <modelVersion>4.0.0</modelVersion>
  4      <groupId>org.jboss.examples.eap</groupId>
  5      <artifactId>ticket-monster-parent</artifactId>
  6      <version>3.0.0-SNAPSHOT</version>
  7      <modules>
  8          <module>monolith</module>
  9          <module>backend-v1</module>
 10          <module>backend-v2</module>
 11          <module>orders-service</module>
 12      </modules>
 13      <packaging>pom</packaging>
 14      <name>Ticket Monster Parent</name>
 15      <description>A starter HTML5 + REST webapp project for use on JBoss EAP.</description>
 16  
 17      <!-- Activate JBoss Product Maven repository.
 18  
 19          NOTE: Configuring the Maven repository in the pom.xml file is not a recommended procedure
 20          and is only done here to make it easier to use the quickstarts.
 21  
 22          For more information about how to configure Maven for your application,
 23          see the section entitled 'Use the Maven Repository'
 24          in the Development Guide for Red Hat JBoss Enterprise Application Platform located here:
 25  
 26          https://access.redhat.com/documentation/en-US/JBoss_Enterprise_Application_Platform/
 27      -->
 28      <repositories>
 29          <repository>
 30              <id>redhat-ga-repository</id>
 31              <url>https://maven.repository.redhat.com/ga/</url>
 32              <releases>
 33                  <enabled>true</enabled>
 34              </releases>
 35              <snapshots>
 36                  <enabled>false</enabled>
 37              </snapshots>
 38          </repository>
 39          <repository>
 40              <id>jboss-ga-repository</id>
 41              <url>http://maven.repository.redhat.com/techpreview/all</url>
 42              <releases>
 43                  <enabled>true</enabled>
 44              </releases>
 45              <snapshots>
 46                  <enabled>false</enabled>
 47              </snapshots>
 48          </repository>
 49          <repository>
 50              <id>jboss-earlyaccess-repository</id>
 51              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 52              <releases>
 53                  <enabled>true</enabled>
 54              </releases>
 55              <snapshots>
 56                  <enabled>false</enabled>
 57              </snapshots>
 58          </repository>
 59          <repository>
 60              <id>redhat.ea</id>
 61              <name>Red Hat Early Access Repository</name>
 62              <url>https://maven.repository.redhat.com/earlyaccess/all</url>
 63              <snapshots>
 64                  <enabled>false</enabled>
 65              </snapshots>
 66              <releases>
 67                  <enabled>true</enabled>
 68              </releases>
 69          </repository>
 70      </repositories>
 71  
 72      <pluginRepositories>
 73          <pluginRepository>
 74              <id>redhat-ga-repository</id>
 75              <url>https://maven.repository.redhat.com/ga/</url>
 76              <releases>
 77                  <enabled>true</enabled>
 78              </releases>
 79              <snapshots>
 80                  <enabled>false</enabled>
 81              </snapshots>
 82          </pluginRepository>
 83          <pluginRepository>
 84              <id>jboss-earlyaccess-plugin-repository</id>
 85              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 86              <releases>
 87                  <enabled>true</enabled>
 88              </releases>
 89              <snapshots>
 90                  <enabled>false</enabled>
 91              </snapshots>
 92          </pluginRepository>
 93      </pluginRepositories>
 94  
 95      <build>
 96          <plugins>
 97              <plugin>
 98                  <artifactId>maven-compiler-plugin</artifactId>
 99                  <version>2.3.1</version>
100                  <configuration>
101                      <source>1.8</source>
102                      <target>1.8</target>
103                  </configuration>
104              </plugin>
```
### #10 - javaee-pom-to-quarkus-00040
* Category: mandatory
* Effort: 1
* Description: Adopt Maven Surefire plugin

* Labels: konveyor.io/source=java-ee, konveyor.io/target=quarkus
* Links
  * Quarkus - Guide: https://quarkus.io/guides/maven-tooling#build-tool-maven
* Incidents
  * file:///tmp/source-code/backend-v1/pom.xml
      * Use the Maven Surefire plugin adding the following sections to the `pom.xml` file:. ```xml. <properties>. <surefire-plugin.version>3.0.0</compiler-plugin.version>. </properties>. <build>. <plugins>. <plugin>. <artifactId>maven-surefire-plugin</artifactId>. <version>$</version>. <configuration>. <systemPropertyVariables>. <java.util.logging.manager>org.jboss.logmanager.LogManager</java.util.logging.manager>. <maven.home>$</maven.home>. </systemPropertyVariables>. </configuration>. </plugin>. </plugins>. </build>. ```
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  3      <modelVersion>4.0.0</modelVersion>
  4      <groupId>org.jboss.examples.eap</groupId>
  5      <artifactId>backend-v1</artifactId>
  6      <version>1.0</version>
  7      <packaging>war</packaging>
  8      <name>ticket-monster backend</name>
  9      <description>A starter HTML5 + REST webapp project for use on JBoss EAP.</description>
 10  
 11      <!-- Activate JBoss Product Maven repository.
 12  
 13          NOTE: Configuring the Maven repository in the pom.xml file is not a recommended procedure
 14          and is only done here to make it easier to use the quickstarts.
 15  
 16          For more information about how to configure Maven for your application,
 17          see the section entitled 'Use the Maven Repository'
 18          in the Development Guide for Red Hat JBoss Enterprise Application Platform located here:
 19  
 20          https://access.redhat.com/documentation/en-US/JBoss_Enterprise_Application_Platform/
 21      -->
 22      <repositories>
 23          <repository>
 24              <id>redhat-ga-repository</id>
 25              <url>https://maven.repository.redhat.com/ga/</url>
 26              <releases>
 27                  <enabled>true</enabled>
 28              </releases>
 29              <snapshots>
 30                  <enabled>false</enabled>
 31              </snapshots>
 32          </repository>
 33          <repository>
 34              <id>jboss-ga-repository</id>
 35              <url>http://maven.repository.redhat.com/techpreview/all</url>
 36              <releases>
 37                  <enabled>true</enabled>
 38              </releases>
 39              <snapshots>
 40                  <enabled>false</enabled>
 41              </snapshots>
 42          </repository>
 43          <repository>
 44              <id>jboss-earlyaccess-repository</id>
 45              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 46              <releases>
 47                  <enabled>true</enabled>
 48              </releases>
 49              <snapshots>
 50                  <enabled>false</enabled>
 51              </snapshots>
 52          </repository>
 53          <repository>
 54              <id>redhat.ea</id>
 55              <name>Red Hat Early Access Repository</name>
 56              <url>https://maven.repository.redhat.com/earlyaccess/all</url>
 57              <snapshots>
 58                  <enabled>false</enabled>
 59              </snapshots>
 60              <releases>
 61                  <enabled>true</enabled>
 62              </releases>
 63          </repository>
 64      </repositories>
 65  
 66      <pluginRepositories>
 67          <pluginRepository>
 68              <id>redhat-ga-repository</id>
 69              <url>https://maven.repository.redhat.com/ga/</url>
 70              <releases>
 71                  <enabled>true</enabled>
 72              </releases>
 73              <snapshots>
 74                  <enabled>false</enabled>
 75              </snapshots>
 76          </pluginRepository>
 77          <pluginRepository>
 78              <id>jboss-earlyaccess-plugin-repository</id>
 79              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 80              <releases>
 81                  <enabled>true</enabled>
 82              </releases>
 83              <snapshots>
 84                  <enabled>false</enabled>
 85              </snapshots>
 86          </pluginRepository>
 87      </pluginRepositories>
 88  
 89      <properties>
 90          <!-- Explicitly declaring the source encoding eliminates the following 
 91              message: -->
 92          <!-- [WARNING] Using platform encoding (UTF-8 actually) to copy filtered 
 93              resources, i.e. build is platform dependent! -->
 94          <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
 95          <!-- Timestamp format for the maven.build.timestamp property -->
 96          <!-- You can reference property in pom.xml or filtered resources 
 97              (must enable third-party plugin if using Maven < 2.1) -->
 98          <maven.build.timestamp.format>yyyyMMdd'T'HHmmss</maven.build.timestamp.format>
 99          <!-- Specify the JBoss EAP directory to be the JBOSS_HOME environment
100              variable -->
101          <jboss.home>${env.JBOSS_HOME}</jboss.home>
102          <version.jboss.bom.eap>7.0.7.GA</version.jboss.bom.eap>
103          <version.wildfly.maven.plugin>1.0.2.Final</version.wildfly.maven.plugin>
104          <version.surefire.plugin>2.10</version.surefire.plugin>
```
  * file:///tmp/source-code/backend-v2/pom.xml
      * Use the Maven Surefire plugin adding the following sections to the `pom.xml` file:. ```xml. <properties>. <surefire-plugin.version>3.0.0</compiler-plugin.version>. </properties>. <build>. <plugins>. <plugin>. <artifactId>maven-surefire-plugin</artifactId>. <version>$</version>. <configuration>. <systemPropertyVariables>. <java.util.logging.manager>org.jboss.logmanager.LogManager</java.util.logging.manager>. <maven.home>$</maven.home>. </systemPropertyVariables>. </configuration>. </plugin>. </plugins>. </build>. ```
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  3      <modelVersion>4.0.0</modelVersion>
  4      <groupId>org.jboss.examples.eap</groupId>
  5      <artifactId>backend-v2</artifactId>
  6      <version>2.0</version>
  7      <packaging>war</packaging>
  8      <name>ticket-monster backend v2</name>
  9      <description>A starter HTML5 + REST webapp project for use on JBoss EAP.</description>
 10  
 11      <!-- Activate JBoss Product Maven repository.
 12  
 13          NOTE: Configuring the Maven repository in the pom.xml file is not a recommended procedure
 14          and is only done here to make it easier to use the quickstarts.
 15  
 16          For more information about how to configure Maven for your application,
 17          see the section entitled 'Use the Maven Repository'
 18          in the Development Guide for Red Hat JBoss Enterprise Application Platform located here:
 19  
 20          https://access.redhat.com/documentation/en-US/JBoss_Enterprise_Application_Platform/
 21      -->
 22      <repositories>
 23          <repository>
 24              <id>redhat-ga-repository</id>
 25              <url>https://maven.repository.redhat.com/ga/</url>
 26              <releases>
 27                  <enabled>true</enabled>
 28              </releases>
 29              <snapshots>
 30                  <enabled>false</enabled>
 31              </snapshots>
 32          </repository>
 33          <repository>
 34              <id>jboss-ga-repository</id>
 35              <url>http://maven.repository.redhat.com/techpreview/all</url>
 36              <releases>
 37                  <enabled>true</enabled>
 38              </releases>
 39              <snapshots>
 40                  <enabled>false</enabled>
 41              </snapshots>
 42          </repository>
 43          <repository>
 44              <id>jboss-earlyaccess-repository</id>
 45              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 46              <releases>
 47                  <enabled>true</enabled>
 48              </releases>
 49              <snapshots>
 50                  <enabled>false</enabled>
 51              </snapshots>
 52          </repository>
 53          <repository>
 54              <id>redhat.ea</id>
 55              <name>Red Hat Early Access Repository</name>
 56              <url>https://maven.repository.redhat.com/earlyaccess/all</url>
 57              <snapshots>
 58                  <enabled>false</enabled>
 59              </snapshots>
 60              <releases>
 61                  <enabled>true</enabled>
 62              </releases>
 63          </repository>
 64      </repositories>
 65  
 66      <pluginRepositories>
 67          <pluginRepository>
 68              <id>redhat-ga-repository</id>
 69              <url>https://maven.repository.redhat.com/ga/</url>
 70              <releases>
 71                  <enabled>true</enabled>
 72              </releases>
 73              <snapshots>
 74                  <enabled>false</enabled>
 75              </snapshots>
 76          </pluginRepository>
 77          <pluginRepository>
 78              <id>jboss-earlyaccess-plugin-repository</id>
 79              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 80              <releases>
 81                  <enabled>true</enabled>
 82              </releases>
 83              <snapshots>
 84                  <enabled>false</enabled>
 85              </snapshots>
 86          </pluginRepository>
 87      </pluginRepositories>
 88  
 89      <properties>
 90          <!-- Explicitly declaring the source encoding eliminates the following 
 91              message: -->
 92          <!-- [WARNING] Using platform encoding (UTF-8 actually) to copy filtered 
 93              resources, i.e. build is platform dependent! -->
 94          <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
 95          <!-- Timestamp format for the maven.build.timestamp property -->
 96          <!-- You can reference property in pom.xml or filtered resources 
 97              (must enable third-party plugin if using Maven < 2.1) -->
 98          <maven.build.timestamp.format>yyyyMMdd'T'HHmmss</maven.build.timestamp.format>
 99          <!-- Specify the JBoss EAP directory to be the JBOSS_HOME environment
100              variable -->
101          <jboss.home>${env.JBOSS_HOME}</jboss.home>
102          <version.jboss.bom.eap>7.0.7.GA</version.jboss.bom.eap>
103          <version.wildfly.maven.plugin>1.0.2.Final</version.wildfly.maven.plugin>
104          <version.surefire.plugin>2.10</version.surefire.plugin>
```
  * file:///tmp/source-code/monolith/pom.xml
      * Use the Maven Surefire plugin adding the following sections to the `pom.xml` file:. ```xml. <properties>. <surefire-plugin.version>3.0.0</compiler-plugin.version>. </properties>. <build>. <plugins>. <plugin>. <artifactId>maven-surefire-plugin</artifactId>. <version>$</version>. <configuration>. <systemPropertyVariables>. <java.util.logging.manager>org.jboss.logmanager.LogManager</java.util.logging.manager>. <maven.home>$</maven.home>. </systemPropertyVariables>. </configuration>. </plugin>. </plugins>. </build>. ```
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  3      <modelVersion>4.0.0</modelVersion>
  4      <groupId>org.jboss.examples.eap</groupId>
  5      <artifactId>ticket-monster</artifactId>
  6      <version>3.0.0-SNAPSHOT</version>
  7      <packaging>war</packaging>
  8      <name>ticket-monster</name>
  9      <description>A starter HTML5 + REST webapp project for use on JBoss EAP.</description>
 10  
 11      <!-- Activate JBoss Product Maven repository.
 12  
 13          NOTE: Configuring the Maven repository in the pom.xml file is not a recommended procedure
 14          and is only done here to make it easier to use the quickstarts.
 15  
 16          For more information about how to configure Maven for your application,
 17          see the section entitled 'Use the Maven Repository'
 18          in the Development Guide for Red Hat JBoss Enterprise Application Platform located here:
 19  
 20          https://access.redhat.com/documentation/en-US/JBoss_Enterprise_Application_Platform/
 21      -->
 22      <repositories>
 23          <repository>
 24              <id>redhat-ga-repository</id>
 25              <url>https://maven.repository.redhat.com/ga/</url>
 26              <releases>
 27                  <enabled>true</enabled>
 28              </releases>
 29              <snapshots>
 30                  <enabled>false</enabled>
 31              </snapshots>
 32          </repository>
 33          <repository>
 34              <id>jboss-ga-repository</id>
 35              <url>http://maven.repository.redhat.com/techpreview/all</url>
 36              <releases>
 37                  <enabled>true</enabled>
 38              </releases>
 39              <snapshots>
 40                  <enabled>false</enabled>
 41              </snapshots>
 42          </repository>
 43          <repository>
 44              <id>jboss-earlyaccess-repository</id>
 45              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 46              <releases>
 47                  <enabled>true</enabled>
 48              </releases>
 49              <snapshots>
 50                  <enabled>false</enabled>
 51              </snapshots>
 52          </repository>
 53          <repository>
 54              <id>redhat.ea</id>
 55              <name>Red Hat Early Access Repository</name>
 56              <url>https://maven.repository.redhat.com/earlyaccess/all</url>
 57              <snapshots>
 58                  <enabled>false</enabled>
 59              </snapshots>
 60              <releases>
 61                  <enabled>true</enabled>
 62              </releases>
 63          </repository>
 64      </repositories>
 65  
 66      <pluginRepositories>
 67          <pluginRepository>
 68              <id>redhat-ga-repository</id>
 69              <url>https://maven.repository.redhat.com/ga/</url>
 70              <releases>
 71                  <enabled>true</enabled>
 72              </releases>
 73              <snapshots>
 74                  <enabled>false</enabled>
 75              </snapshots>
 76          </pluginRepository>
 77          <pluginRepository>
 78              <id>jboss-earlyaccess-plugin-repository</id>
 79              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 80              <releases>
 81                  <enabled>true</enabled>
 82              </releases>
 83              <snapshots>
 84                  <enabled>false</enabled>
 85              </snapshots>
 86          </pluginRepository>
 87      </pluginRepositories>
 88  
 89      <properties>
 90          <!-- Explicitly declaring the source encoding eliminates the following 
 91              message: -->
 92          <!-- [WARNING] Using platform encoding (UTF-8 actually) to copy filtered 
 93              resources, i.e. build is platform dependent! -->
 94          <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
 95          <!-- Timestamp format for the maven.build.timestamp property -->
 96          <!-- You can reference property in pom.xml or filtered resources 
 97              (must enable third-party plugin if using Maven < 2.1) -->
 98          <maven.build.timestamp.format>yyyyMMdd'T'HHmmss</maven.build.timestamp.format>
 99          <!-- Specify the JBoss EAP directory to be the JBOSS_HOME environment
100              variable -->
101          <jboss.home>${env.JBOSS_HOME}</jboss.home>
102          <version.jboss.bom.eap>7.0.7.GA</version.jboss.bom.eap>
103          <version.wildfly.maven.plugin>1.0.2.Final</version.wildfly.maven.plugin>
104          <version.surefire.plugin>2.10</version.surefire.plugin>
```
  * file:///tmp/source-code/orders-service/pom.xml
      * Use the Maven Surefire plugin adding the following sections to the `pom.xml` file:. ```xml. <properties>. <surefire-plugin.version>3.0.0</compiler-plugin.version>. </properties>. <build>. <plugins>. <plugin>. <artifactId>maven-surefire-plugin</artifactId>. <version>$</version>. <configuration>. <systemPropertyVariables>. <java.util.logging.manager>org.jboss.logmanager.LogManager</java.util.logging.manager>. <maven.home>$</maven.home>. </systemPropertyVariables>. </configuration>. </plugin>. </plugins>. </build>. ```
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <project xmlns="http://maven.apache.org/POM/4.0.0"
  3           xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  4           xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  5    <artifactId>orders-service</artifactId>
  6    <groupId>org.ticketmonster.orders</groupId>
  7    <version>1.0.0-SNAPSHOT</version>
  8    <modelVersion>4.0.0</modelVersion>
  9  
 10    <properties>
 11      <spring-boot.version>1.5.6.RELEASE</spring-boot.version>
 12      <docker-maven-plugin.version>0.20.1</docker-maven-plugin.version>
 13      <mysql-server.version>5.7</mysql-server.version>
 14      <mysql.user>ticket</mysql.user>
 15      <mysql.password>monster</mysql.password>
 16      <mysql.port>3306</mysql.port>
 17      <mysql.init.timeout>60000</mysql.init.timeout>
 18      <skipITs>true</skipITs>
 19      <fabric8.maven.plugin.version>3.5.25</fabric8.maven.plugin.version>
 20      <docker.image.name>ceposta/%a:%l</docker.image.name>
 21    </properties>
 22  
 23    <dependencyManagement>
 24      <dependencies>
 25        <dependency>
 26          <!-- Import dependency management from Spring Boot -->
 27          <groupId>org.springframework.boot</groupId>
 28          <artifactId>spring-boot-dependencies</artifactId>
 29          <version>${spring-boot.version}</version>
 30          <type>pom</type>
 31          <scope>import</scope>
 32        </dependency>
 33      </dependencies>
 34    </dependencyManagement>
 35  
 36  
 37    <dependencies>
 38      <dependency>
 39        <groupId>org.springframework.boot</groupId>
 40        <artifactId>spring-boot-starter-web</artifactId>
 41      </dependency>
 42      <dependency>
 43        <groupId>org.springframework.boot</groupId>
 44        <artifactId>spring-boot-starter-actuator</artifactId>
 45      </dependency>
 46      <dependency>
 47        <groupId>org.springframework.boot</groupId>
 48        <artifactId>spring-boot-starter-data-jpa</artifactId>
 49      </dependency>
 50      <dependency>
 51        <groupId>org.teiid.spring</groupId>
 52        <artifactId>teiid-spring-boot-starter</artifactId>
 53        <version>1.0.0-SNAPSHOT</version>
 54      </dependency>
 55  
 56  
 57  
 58      <!-- Testing -->
 59      <dependency>
 60        <groupId>io.rest-assured</groupId>
 61        <artifactId>rest-assured</artifactId>
 62        <version>3.0.3</version>
 63        <scope>test</scope>
 64      </dependency>
 65      <dependency>
 66        <groupId>io.rest-assured</groupId>
 67        <artifactId>json-schema-validator</artifactId>
 68        <version>3.0.3</version>
 69        <scope>test</scope>
 70      </dependency>
 71      <dependency>
 72        <groupId>io.specto</groupId>
 73        <artifactId>hoverfly-java</artifactId>
 74        <version>0.8.0</version>
 75        <scope>test</scope>
 76      </dependency>
 77      <dependency>
 78        <groupId>org.springframework.boot</groupId>
 79        <artifactId>spring-boot-starter-test</artifactId>
 80        <scope>test</scope>
 81      </dependency>
 82      <dependency>
 83        <groupId>com.h2database</groupId>
 84        <artifactId>h2</artifactId>
 85        <scope>test</scope>
 86      </dependency>
 87  
 88      <dependency>
 89        <groupId>au.com.dius</groupId>
 90        <artifactId>pact-jvm-provider-junit_2.11</artifactId>
 91        <version>3.5.0</version>
 92      </dependency>
 93    </dependencies>
 94  
 95    <build>
 96      <plugins>
 97        <plugin>
 98          <groupId>org.springframework.boot</groupId>
 99          <artifactId>spring-boot-maven-plugin</artifactId>
100          <version>${spring-boot.version}</version>
101          <executions>
102            <execution>
103              <goals>
104                <goal>repackage</goal>
105              </goals>
106            </execution>
```
  * file:///tmp/source-code/pom.xml
      * Use the Maven Surefire plugin adding the following sections to the `pom.xml` file:. ```xml. <properties>. <surefire-plugin.version>3.0.0</compiler-plugin.version>. </properties>. <build>. <plugins>. <plugin>. <artifactId>maven-surefire-plugin</artifactId>. <version>$</version>. <configuration>. <systemPropertyVariables>. <java.util.logging.manager>org.jboss.logmanager.LogManager</java.util.logging.manager>. <maven.home>$</maven.home>. </systemPropertyVariables>. </configuration>. </plugin>. </plugins>. </build>. ```
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  3      <modelVersion>4.0.0</modelVersion>
  4      <groupId>org.jboss.examples.eap</groupId>
  5      <artifactId>ticket-monster-parent</artifactId>
  6      <version>3.0.0-SNAPSHOT</version>
  7      <modules>
  8          <module>monolith</module>
  9          <module>backend-v1</module>
 10          <module>backend-v2</module>
 11          <module>orders-service</module>
 12      </modules>
 13      <packaging>pom</packaging>
 14      <name>Ticket Monster Parent</name>
 15      <description>A starter HTML5 + REST webapp project for use on JBoss EAP.</description>
 16  
 17      <!-- Activate JBoss Product Maven repository.
 18  
 19          NOTE: Configuring the Maven repository in the pom.xml file is not a recommended procedure
 20          and is only done here to make it easier to use the quickstarts.
 21  
 22          For more information about how to configure Maven for your application,
 23          see the section entitled 'Use the Maven Repository'
 24          in the Development Guide for Red Hat JBoss Enterprise Application Platform located here:
 25  
 26          https://access.redhat.com/documentation/en-US/JBoss_Enterprise_Application_Platform/
 27      -->
 28      <repositories>
 29          <repository>
 30              <id>redhat-ga-repository</id>
 31              <url>https://maven.repository.redhat.com/ga/</url>
 32              <releases>
 33                  <enabled>true</enabled>
 34              </releases>
 35              <snapshots>
 36                  <enabled>false</enabled>
 37              </snapshots>
 38          </repository>
 39          <repository>
 40              <id>jboss-ga-repository</id>
 41              <url>http://maven.repository.redhat.com/techpreview/all</url>
 42              <releases>
 43                  <enabled>true</enabled>
 44              </releases>
 45              <snapshots>
 46                  <enabled>false</enabled>
 47              </snapshots>
 48          </repository>
 49          <repository>
 50              <id>jboss-earlyaccess-repository</id>
 51              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 52              <releases>
 53                  <enabled>true</enabled>
 54              </releases>
 55              <snapshots>
 56                  <enabled>false</enabled>
 57              </snapshots>
 58          </repository>
 59          <repository>
 60              <id>redhat.ea</id>
 61              <name>Red Hat Early Access Repository</name>
 62              <url>https://maven.repository.redhat.com/earlyaccess/all</url>
 63              <snapshots>
 64                  <enabled>false</enabled>
 65              </snapshots>
 66              <releases>
 67                  <enabled>true</enabled>
 68              </releases>
 69          </repository>
 70      </repositories>
 71  
 72      <pluginRepositories>
 73          <pluginRepository>
 74              <id>redhat-ga-repository</id>
 75              <url>https://maven.repository.redhat.com/ga/</url>
 76              <releases>
 77                  <enabled>true</enabled>
 78              </releases>
 79              <snapshots>
 80                  <enabled>false</enabled>
 81              </snapshots>
 82          </pluginRepository>
 83          <pluginRepository>
 84              <id>jboss-earlyaccess-plugin-repository</id>
 85              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 86              <releases>
 87                  <enabled>true</enabled>
 88              </releases>
 89              <snapshots>
 90                  <enabled>false</enabled>
 91              </snapshots>
 92          </pluginRepository>
 93      </pluginRepositories>
 94  
 95      <build>
 96          <plugins>
 97              <plugin>
 98                  <artifactId>maven-compiler-plugin</artifactId>
 99                  <version>2.3.1</version>
100                  <configuration>
101                      <source>1.8</source>
102                      <target>1.8</target>
103                  </configuration>
104              </plugin>
```
### #11 - javaee-pom-to-quarkus-00050
* Category: mandatory
* Effort: 1
* Description: Adopt Maven Failsafe plugin

* Labels: konveyor.io/source=java-ee, konveyor.io/target=quarkus
* Links
  * Quarkus - Guide: https://quarkus.io/guides/maven-tooling#build-tool-maven
* Incidents
  * file:///tmp/source-code/backend-v1/pom.xml
      * Use the Maven Failsafe plugin adding the following sections to the `pom.xml` file:. ```xml. <properties>. <surefire-plugin.version>3.0.0</compiler-plugin.version>. </properties>. <build>. <plugins>. <plugin>. <artifactId>maven-failsafe-plugin</artifactId>. <version>$</version>. <executions>. <execution>. <goals>. <goals>integration-test</goal>. <goals>verify</goal>. </goals>. <configuration>. <systemPropertyVariables>. <native.image.path>$/$-runner</native.image.path>. <java.util.logging.manager>org.jboss.logmanager.LogManager</java.util.logging.manager>. <maven.home>$</maven.home>. </systemPropertyVariables>. </configuration>. </execution>. </executions>. </plugin>. </plugins>. </build>. ```
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  3      <modelVersion>4.0.0</modelVersion>
  4      <groupId>org.jboss.examples.eap</groupId>
  5      <artifactId>backend-v1</artifactId>
  6      <version>1.0</version>
  7      <packaging>war</packaging>
  8      <name>ticket-monster backend</name>
  9      <description>A starter HTML5 + REST webapp project for use on JBoss EAP.</description>
 10  
 11      <!-- Activate JBoss Product Maven repository.
 12  
 13          NOTE: Configuring the Maven repository in the pom.xml file is not a recommended procedure
 14          and is only done here to make it easier to use the quickstarts.
 15  
 16          For more information about how to configure Maven for your application,
 17          see the section entitled 'Use the Maven Repository'
 18          in the Development Guide for Red Hat JBoss Enterprise Application Platform located here:
 19  
 20          https://access.redhat.com/documentation/en-US/JBoss_Enterprise_Application_Platform/
 21      -->
 22      <repositories>
 23          <repository>
 24              <id>redhat-ga-repository</id>
 25              <url>https://maven.repository.redhat.com/ga/</url>
 26              <releases>
 27                  <enabled>true</enabled>
 28              </releases>
 29              <snapshots>
 30                  <enabled>false</enabled>
 31              </snapshots>
 32          </repository>
 33          <repository>
 34              <id>jboss-ga-repository</id>
 35              <url>http://maven.repository.redhat.com/techpreview/all</url>
 36              <releases>
 37                  <enabled>true</enabled>
 38              </releases>
 39              <snapshots>
 40                  <enabled>false</enabled>
 41              </snapshots>
 42          </repository>
 43          <repository>
 44              <id>jboss-earlyaccess-repository</id>
 45              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 46              <releases>
 47                  <enabled>true</enabled>
 48              </releases>
 49              <snapshots>
 50                  <enabled>false</enabled>
 51              </snapshots>
 52          </repository>
 53          <repository>
 54              <id>redhat.ea</id>
 55              <name>Red Hat Early Access Repository</name>
 56              <url>https://maven.repository.redhat.com/earlyaccess/all</url>
 57              <snapshots>
 58                  <enabled>false</enabled>
 59              </snapshots>
 60              <releases>
 61                  <enabled>true</enabled>
 62              </releases>
 63          </repository>
 64      </repositories>
 65  
 66      <pluginRepositories>
 67          <pluginRepository>
 68              <id>redhat-ga-repository</id>
 69              <url>https://maven.repository.redhat.com/ga/</url>
 70              <releases>
 71                  <enabled>true</enabled>
 72              </releases>
 73              <snapshots>
 74                  <enabled>false</enabled>
 75              </snapshots>
 76          </pluginRepository>
 77          <pluginRepository>
 78              <id>jboss-earlyaccess-plugin-repository</id>
 79              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 80              <releases>
 81                  <enabled>true</enabled>
 82              </releases>
 83              <snapshots>
 84                  <enabled>false</enabled>
 85              </snapshots>
 86          </pluginRepository>
 87      </pluginRepositories>
 88  
 89      <properties>
 90          <!-- Explicitly declaring the source encoding eliminates the following 
 91              message: -->
 92          <!-- [WARNING] Using platform encoding (UTF-8 actually) to copy filtered 
 93              resources, i.e. build is platform dependent! -->
 94          <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
 95          <!-- Timestamp format for the maven.build.timestamp property -->
 96          <!-- You can reference property in pom.xml or filtered resources 
 97              (must enable third-party plugin if using Maven < 2.1) -->
 98          <maven.build.timestamp.format>yyyyMMdd'T'HHmmss</maven.build.timestamp.format>
 99          <!-- Specify the JBoss EAP directory to be the JBOSS_HOME environment
100              variable -->
101          <jboss.home>${env.JBOSS_HOME}</jboss.home>
102          <version.jboss.bom.eap>7.0.7.GA</version.jboss.bom.eap>
103          <version.wildfly.maven.plugin>1.0.2.Final</version.wildfly.maven.plugin>
104          <version.surefire.plugin>2.10</version.surefire.plugin>
```
  * file:///tmp/source-code/backend-v2/pom.xml
      * Use the Maven Failsafe plugin adding the following sections to the `pom.xml` file:. ```xml. <properties>. <surefire-plugin.version>3.0.0</compiler-plugin.version>. </properties>. <build>. <plugins>. <plugin>. <artifactId>maven-failsafe-plugin</artifactId>. <version>$</version>. <executions>. <execution>. <goals>. <goals>integration-test</goal>. <goals>verify</goal>. </goals>. <configuration>. <systemPropertyVariables>. <native.image.path>$/$-runner</native.image.path>. <java.util.logging.manager>org.jboss.logmanager.LogManager</java.util.logging.manager>. <maven.home>$</maven.home>. </systemPropertyVariables>. </configuration>. </execution>. </executions>. </plugin>. </plugins>. </build>. ```
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  3      <modelVersion>4.0.0</modelVersion>
  4      <groupId>org.jboss.examples.eap</groupId>
  5      <artifactId>backend-v2</artifactId>
  6      <version>2.0</version>
  7      <packaging>war</packaging>
  8      <name>ticket-monster backend v2</name>
  9      <description>A starter HTML5 + REST webapp project for use on JBoss EAP.</description>
 10  
 11      <!-- Activate JBoss Product Maven repository.
 12  
 13          NOTE: Configuring the Maven repository in the pom.xml file is not a recommended procedure
 14          and is only done here to make it easier to use the quickstarts.
 15  
 16          For more information about how to configure Maven for your application,
 17          see the section entitled 'Use the Maven Repository'
 18          in the Development Guide for Red Hat JBoss Enterprise Application Platform located here:
 19  
 20          https://access.redhat.com/documentation/en-US/JBoss_Enterprise_Application_Platform/
 21      -->
 22      <repositories>
 23          <repository>
 24              <id>redhat-ga-repository</id>
 25              <url>https://maven.repository.redhat.com/ga/</url>
 26              <releases>
 27                  <enabled>true</enabled>
 28              </releases>
 29              <snapshots>
 30                  <enabled>false</enabled>
 31              </snapshots>
 32          </repository>
 33          <repository>
 34              <id>jboss-ga-repository</id>
 35              <url>http://maven.repository.redhat.com/techpreview/all</url>
 36              <releases>
 37                  <enabled>true</enabled>
 38              </releases>
 39              <snapshots>
 40                  <enabled>false</enabled>
 41              </snapshots>
 42          </repository>
 43          <repository>
 44              <id>jboss-earlyaccess-repository</id>
 45              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 46              <releases>
 47                  <enabled>true</enabled>
 48              </releases>
 49              <snapshots>
 50                  <enabled>false</enabled>
 51              </snapshots>
 52          </repository>
 53          <repository>
 54              <id>redhat.ea</id>
 55              <name>Red Hat Early Access Repository</name>
 56              <url>https://maven.repository.redhat.com/earlyaccess/all</url>
 57              <snapshots>
 58                  <enabled>false</enabled>
 59              </snapshots>
 60              <releases>
 61                  <enabled>true</enabled>
 62              </releases>
 63          </repository>
 64      </repositories>
 65  
 66      <pluginRepositories>
 67          <pluginRepository>
 68              <id>redhat-ga-repository</id>
 69              <url>https://maven.repository.redhat.com/ga/</url>
 70              <releases>
 71                  <enabled>true</enabled>
 72              </releases>
 73              <snapshots>
 74                  <enabled>false</enabled>
 75              </snapshots>
 76          </pluginRepository>
 77          <pluginRepository>
 78              <id>jboss-earlyaccess-plugin-repository</id>
 79              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 80              <releases>
 81                  <enabled>true</enabled>
 82              </releases>
 83              <snapshots>
 84                  <enabled>false</enabled>
 85              </snapshots>
 86          </pluginRepository>
 87      </pluginRepositories>
 88  
 89      <properties>
 90          <!-- Explicitly declaring the source encoding eliminates the following 
 91              message: -->
 92          <!-- [WARNING] Using platform encoding (UTF-8 actually) to copy filtered 
 93              resources, i.e. build is platform dependent! -->
 94          <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
 95          <!-- Timestamp format for the maven.build.timestamp property -->
 96          <!-- You can reference property in pom.xml or filtered resources 
 97              (must enable third-party plugin if using Maven < 2.1) -->
 98          <maven.build.timestamp.format>yyyyMMdd'T'HHmmss</maven.build.timestamp.format>
 99          <!-- Specify the JBoss EAP directory to be the JBOSS_HOME environment
100              variable -->
101          <jboss.home>${env.JBOSS_HOME}</jboss.home>
102          <version.jboss.bom.eap>7.0.7.GA</version.jboss.bom.eap>
103          <version.wildfly.maven.plugin>1.0.2.Final</version.wildfly.maven.plugin>
104          <version.surefire.plugin>2.10</version.surefire.plugin>
```
  * file:///tmp/source-code/monolith/pom.xml
      * Use the Maven Failsafe plugin adding the following sections to the `pom.xml` file:. ```xml. <properties>. <surefire-plugin.version>3.0.0</compiler-plugin.version>. </properties>. <build>. <plugins>. <plugin>. <artifactId>maven-failsafe-plugin</artifactId>. <version>$</version>. <executions>. <execution>. <goals>. <goals>integration-test</goal>. <goals>verify</goal>. </goals>. <configuration>. <systemPropertyVariables>. <native.image.path>$/$-runner</native.image.path>. <java.util.logging.manager>org.jboss.logmanager.LogManager</java.util.logging.manager>. <maven.home>$</maven.home>. </systemPropertyVariables>. </configuration>. </execution>. </executions>. </plugin>. </plugins>. </build>. ```
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  3      <modelVersion>4.0.0</modelVersion>
  4      <groupId>org.jboss.examples.eap</groupId>
  5      <artifactId>ticket-monster</artifactId>
  6      <version>3.0.0-SNAPSHOT</version>
  7      <packaging>war</packaging>
  8      <name>ticket-monster</name>
  9      <description>A starter HTML5 + REST webapp project for use on JBoss EAP.</description>
 10  
 11      <!-- Activate JBoss Product Maven repository.
 12  
 13          NOTE: Configuring the Maven repository in the pom.xml file is not a recommended procedure
 14          and is only done here to make it easier to use the quickstarts.
 15  
 16          For more information about how to configure Maven for your application,
 17          see the section entitled 'Use the Maven Repository'
 18          in the Development Guide for Red Hat JBoss Enterprise Application Platform located here:
 19  
 20          https://access.redhat.com/documentation/en-US/JBoss_Enterprise_Application_Platform/
 21      -->
 22      <repositories>
 23          <repository>
 24              <id>redhat-ga-repository</id>
 25              <url>https://maven.repository.redhat.com/ga/</url>
 26              <releases>
 27                  <enabled>true</enabled>
 28              </releases>
 29              <snapshots>
 30                  <enabled>false</enabled>
 31              </snapshots>
 32          </repository>
 33          <repository>
 34              <id>jboss-ga-repository</id>
 35              <url>http://maven.repository.redhat.com/techpreview/all</url>
 36              <releases>
 37                  <enabled>true</enabled>
 38              </releases>
 39              <snapshots>
 40                  <enabled>false</enabled>
 41              </snapshots>
 42          </repository>
 43          <repository>
 44              <id>jboss-earlyaccess-repository</id>
 45              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 46              <releases>
 47                  <enabled>true</enabled>
 48              </releases>
 49              <snapshots>
 50                  <enabled>false</enabled>
 51              </snapshots>
 52          </repository>
 53          <repository>
 54              <id>redhat.ea</id>
 55              <name>Red Hat Early Access Repository</name>
 56              <url>https://maven.repository.redhat.com/earlyaccess/all</url>
 57              <snapshots>
 58                  <enabled>false</enabled>
 59              </snapshots>
 60              <releases>
 61                  <enabled>true</enabled>
 62              </releases>
 63          </repository>
 64      </repositories>
 65  
 66      <pluginRepositories>
 67          <pluginRepository>
 68              <id>redhat-ga-repository</id>
 69              <url>https://maven.repository.redhat.com/ga/</url>
 70              <releases>
 71                  <enabled>true</enabled>
 72              </releases>
 73              <snapshots>
 74                  <enabled>false</enabled>
 75              </snapshots>
 76          </pluginRepository>
 77          <pluginRepository>
 78              <id>jboss-earlyaccess-plugin-repository</id>
 79              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 80              <releases>
 81                  <enabled>true</enabled>
 82              </releases>
 83              <snapshots>
 84                  <enabled>false</enabled>
 85              </snapshots>
 86          </pluginRepository>
 87      </pluginRepositories>
 88  
 89      <properties>
 90          <!-- Explicitly declaring the source encoding eliminates the following 
 91              message: -->
 92          <!-- [WARNING] Using platform encoding (UTF-8 actually) to copy filtered 
 93              resources, i.e. build is platform dependent! -->
 94          <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
 95          <!-- Timestamp format for the maven.build.timestamp property -->
 96          <!-- You can reference property in pom.xml or filtered resources 
 97              (must enable third-party plugin if using Maven < 2.1) -->
 98          <maven.build.timestamp.format>yyyyMMdd'T'HHmmss</maven.build.timestamp.format>
 99          <!-- Specify the JBoss EAP directory to be the JBOSS_HOME environment
100              variable -->
101          <jboss.home>${env.JBOSS_HOME}</jboss.home>
102          <version.jboss.bom.eap>7.0.7.GA</version.jboss.bom.eap>
103          <version.wildfly.maven.plugin>1.0.2.Final</version.wildfly.maven.plugin>
104          <version.surefire.plugin>2.10</version.surefire.plugin>
```
  * file:///tmp/source-code/orders-service/pom.xml
      * Use the Maven Failsafe plugin adding the following sections to the `pom.xml` file:. ```xml. <properties>. <surefire-plugin.version>3.0.0</compiler-plugin.version>. </properties>. <build>. <plugins>. <plugin>. <artifactId>maven-failsafe-plugin</artifactId>. <version>$</version>. <executions>. <execution>. <goals>. <goals>integration-test</goal>. <goals>verify</goal>. </goals>. <configuration>. <systemPropertyVariables>. <native.image.path>$/$-runner</native.image.path>. <java.util.logging.manager>org.jboss.logmanager.LogManager</java.util.logging.manager>. <maven.home>$</maven.home>. </systemPropertyVariables>. </configuration>. </execution>. </executions>. </plugin>. </plugins>. </build>. ```
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <project xmlns="http://maven.apache.org/POM/4.0.0"
  3           xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  4           xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  5    <artifactId>orders-service</artifactId>
  6    <groupId>org.ticketmonster.orders</groupId>
  7    <version>1.0.0-SNAPSHOT</version>
  8    <modelVersion>4.0.0</modelVersion>
  9  
 10    <properties>
 11      <spring-boot.version>1.5.6.RELEASE</spring-boot.version>
 12      <docker-maven-plugin.version>0.20.1</docker-maven-plugin.version>
 13      <mysql-server.version>5.7</mysql-server.version>
 14      <mysql.user>ticket</mysql.user>
 15      <mysql.password>monster</mysql.password>
 16      <mysql.port>3306</mysql.port>
 17      <mysql.init.timeout>60000</mysql.init.timeout>
 18      <skipITs>true</skipITs>
 19      <fabric8.maven.plugin.version>3.5.25</fabric8.maven.plugin.version>
 20      <docker.image.name>ceposta/%a:%l</docker.image.name>
 21    </properties>
 22  
 23    <dependencyManagement>
 24      <dependencies>
 25        <dependency>
 26          <!-- Import dependency management from Spring Boot -->
 27          <groupId>org.springframework.boot</groupId>
 28          <artifactId>spring-boot-dependencies</artifactId>
 29          <version>${spring-boot.version}</version>
 30          <type>pom</type>
 31          <scope>import</scope>
 32        </dependency>
 33      </dependencies>
 34    </dependencyManagement>
 35  
 36  
 37    <dependencies>
 38      <dependency>
 39        <groupId>org.springframework.boot</groupId>
 40        <artifactId>spring-boot-starter-web</artifactId>
 41      </dependency>
 42      <dependency>
 43        <groupId>org.springframework.boot</groupId>
 44        <artifactId>spring-boot-starter-actuator</artifactId>
 45      </dependency>
 46      <dependency>
 47        <groupId>org.springframework.boot</groupId>
 48        <artifactId>spring-boot-starter-data-jpa</artifactId>
 49      </dependency>
 50      <dependency>
 51        <groupId>org.teiid.spring</groupId>
 52        <artifactId>teiid-spring-boot-starter</artifactId>
 53        <version>1.0.0-SNAPSHOT</version>
 54      </dependency>
 55  
 56  
 57  
 58      <!-- Testing -->
 59      <dependency>
 60        <groupId>io.rest-assured</groupId>
 61        <artifactId>rest-assured</artifactId>
 62        <version>3.0.3</version>
 63        <scope>test</scope>
 64      </dependency>
 65      <dependency>
 66        <groupId>io.rest-assured</groupId>
 67        <artifactId>json-schema-validator</artifactId>
 68        <version>3.0.3</version>
 69        <scope>test</scope>
 70      </dependency>
 71      <dependency>
 72        <groupId>io.specto</groupId>
 73        <artifactId>hoverfly-java</artifactId>
 74        <version>0.8.0</version>
 75        <scope>test</scope>
 76      </dependency>
 77      <dependency>
 78        <groupId>org.springframework.boot</groupId>
 79        <artifactId>spring-boot-starter-test</artifactId>
 80        <scope>test</scope>
 81      </dependency>
 82      <dependency>
 83        <groupId>com.h2database</groupId>
 84        <artifactId>h2</artifactId>
 85        <scope>test</scope>
 86      </dependency>
 87  
 88      <dependency>
 89        <groupId>au.com.dius</groupId>
 90        <artifactId>pact-jvm-provider-junit_2.11</artifactId>
 91        <version>3.5.0</version>
 92      </dependency>
 93    </dependencies>
 94  
 95    <build>
 96      <plugins>
 97        <plugin>
 98          <groupId>org.springframework.boot</groupId>
 99          <artifactId>spring-boot-maven-plugin</artifactId>
100          <version>${spring-boot.version}</version>
101          <executions>
102            <execution>
103              <goals>
104                <goal>repackage</goal>
105              </goals>
106            </execution>
```
  * file:///tmp/source-code/pom.xml
      * Use the Maven Failsafe plugin adding the following sections to the `pom.xml` file:. ```xml. <properties>. <surefire-plugin.version>3.0.0</compiler-plugin.version>. </properties>. <build>. <plugins>. <plugin>. <artifactId>maven-failsafe-plugin</artifactId>. <version>$</version>. <executions>. <execution>. <goals>. <goals>integration-test</goal>. <goals>verify</goal>. </goals>. <configuration>. <systemPropertyVariables>. <native.image.path>$/$-runner</native.image.path>. <java.util.logging.manager>org.jboss.logmanager.LogManager</java.util.logging.manager>. <maven.home>$</maven.home>. </systemPropertyVariables>. </configuration>. </execution>. </executions>. </plugin>. </plugins>. </build>. ```
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  3      <modelVersion>4.0.0</modelVersion>
  4      <groupId>org.jboss.examples.eap</groupId>
  5      <artifactId>ticket-monster-parent</artifactId>
  6      <version>3.0.0-SNAPSHOT</version>
  7      <modules>
  8          <module>monolith</module>
  9          <module>backend-v1</module>
 10          <module>backend-v2</module>
 11          <module>orders-service</module>
 12      </modules>
 13      <packaging>pom</packaging>
 14      <name>Ticket Monster Parent</name>
 15      <description>A starter HTML5 + REST webapp project for use on JBoss EAP.</description>
 16  
 17      <!-- Activate JBoss Product Maven repository.
 18  
 19          NOTE: Configuring the Maven repository in the pom.xml file is not a recommended procedure
 20          and is only done here to make it easier to use the quickstarts.
 21  
 22          For more information about how to configure Maven for your application,
 23          see the section entitled 'Use the Maven Repository'
 24          in the Development Guide for Red Hat JBoss Enterprise Application Platform located here:
 25  
 26          https://access.redhat.com/documentation/en-US/JBoss_Enterprise_Application_Platform/
 27      -->
 28      <repositories>
 29          <repository>
 30              <id>redhat-ga-repository</id>
 31              <url>https://maven.repository.redhat.com/ga/</url>
 32              <releases>
 33                  <enabled>true</enabled>
 34              </releases>
 35              <snapshots>
 36                  <enabled>false</enabled>
 37              </snapshots>
 38          </repository>
 39          <repository>
 40              <id>jboss-ga-repository</id>
 41              <url>http://maven.repository.redhat.com/techpreview/all</url>
 42              <releases>
 43                  <enabled>true</enabled>
 44              </releases>
 45              <snapshots>
 46                  <enabled>false</enabled>
 47              </snapshots>
 48          </repository>
 49          <repository>
 50              <id>jboss-earlyaccess-repository</id>
 51              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 52              <releases>
 53                  <enabled>true</enabled>
 54              </releases>
 55              <snapshots>
 56                  <enabled>false</enabled>
 57              </snapshots>
 58          </repository>
 59          <repository>
 60              <id>redhat.ea</id>
 61              <name>Red Hat Early Access Repository</name>
 62              <url>https://maven.repository.redhat.com/earlyaccess/all</url>
 63              <snapshots>
 64                  <enabled>false</enabled>
 65              </snapshots>
 66              <releases>
 67                  <enabled>true</enabled>
 68              </releases>
 69          </repository>
 70      </repositories>
 71  
 72      <pluginRepositories>
 73          <pluginRepository>
 74              <id>redhat-ga-repository</id>
 75              <url>https://maven.repository.redhat.com/ga/</url>
 76              <releases>
 77                  <enabled>true</enabled>
 78              </releases>
 79              <snapshots>
 80                  <enabled>false</enabled>
 81              </snapshots>
 82          </pluginRepository>
 83          <pluginRepository>
 84              <id>jboss-earlyaccess-plugin-repository</id>
 85              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 86              <releases>
 87                  <enabled>true</enabled>
 88              </releases>
 89              <snapshots>
 90                  <enabled>false</enabled>
 91              </snapshots>
 92          </pluginRepository>
 93      </pluginRepositories>
 94  
 95      <build>
 96          <plugins>
 97              <plugin>
 98                  <artifactId>maven-compiler-plugin</artifactId>
 99                  <version>2.3.1</version>
100                  <configuration>
101                      <source>1.8</source>
102                      <target>1.8</target>
103                  </configuration>
104              </plugin>
```
### #12 - javaee-pom-to-quarkus-00060
* Category: mandatory
* Effort: 1
* Description: Add Maven profile to run the Quarkus native build
Leverage a Maven profile to run the Quarkus native build adding the following section to the `pom.xml` file:. ```xml. <profiles>. <profile>. <id>native</id>. <activation>. <property>. <name>native</name>. </property>. </activation>. <properties>. <skipITs>false</skipITs>. <quarkus.package.type>native</quarkus.package.type>. </properties>. </profile>. </profiles>. ```
* Labels: konveyor.io/source=java-ee, konveyor.io/target=quarkus
* Links
  * Quarkus - Guide: https://quarkus.io/guides/maven-tooling#build-tool-maven
* Incidents
  * file:///tmp/source-code/backend-v1/pom.xml
      * Leverage a Maven profile to run the Quarkus native build adding the following section to the `pom.xml` file:. ```xml. <profiles>. <profile>. <id>native</id>. <activation>. <property>. <name>native</name>. </property>. </activation>. <properties>. <skipITs>false</skipITs>. <quarkus.package.type>native</quarkus.package.type>. </properties>. </profile>. </profiles>. ```
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  3      <modelVersion>4.0.0</modelVersion>
  4      <groupId>org.jboss.examples.eap</groupId>
  5      <artifactId>backend-v1</artifactId>
  6      <version>1.0</version>
  7      <packaging>war</packaging>
  8      <name>ticket-monster backend</name>
  9      <description>A starter HTML5 + REST webapp project for use on JBoss EAP.</description>
 10  
 11      <!-- Activate JBoss Product Maven repository.
 12  
 13          NOTE: Configuring the Maven repository in the pom.xml file is not a recommended procedure
 14          and is only done here to make it easier to use the quickstarts.
 15  
 16          For more information about how to configure Maven for your application,
 17          see the section entitled 'Use the Maven Repository'
 18          in the Development Guide for Red Hat JBoss Enterprise Application Platform located here:
 19  
 20          https://access.redhat.com/documentation/en-US/JBoss_Enterprise_Application_Platform/
 21      -->
 22      <repositories>
 23          <repository>
 24              <id>redhat-ga-repository</id>
 25              <url>https://maven.repository.redhat.com/ga/</url>
 26              <releases>
 27                  <enabled>true</enabled>
 28              </releases>
 29              <snapshots>
 30                  <enabled>false</enabled>
 31              </snapshots>
 32          </repository>
 33          <repository>
 34              <id>jboss-ga-repository</id>
 35              <url>http://maven.repository.redhat.com/techpreview/all</url>
 36              <releases>
 37                  <enabled>true</enabled>
 38              </releases>
 39              <snapshots>
 40                  <enabled>false</enabled>
 41              </snapshots>
 42          </repository>
 43          <repository>
 44              <id>jboss-earlyaccess-repository</id>
 45              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 46              <releases>
 47                  <enabled>true</enabled>
 48              </releases>
 49              <snapshots>
 50                  <enabled>false</enabled>
 51              </snapshots>
 52          </repository>
 53          <repository>
 54              <id>redhat.ea</id>
 55              <name>Red Hat Early Access Repository</name>
 56              <url>https://maven.repository.redhat.com/earlyaccess/all</url>
 57              <snapshots>
 58                  <enabled>false</enabled>
 59              </snapshots>
 60              <releases>
 61                  <enabled>true</enabled>
 62              </releases>
 63          </repository>
 64      </repositories>
 65  
 66      <pluginRepositories>
 67          <pluginRepository>
 68              <id>redhat-ga-repository</id>
 69              <url>https://maven.repository.redhat.com/ga/</url>
 70              <releases>
 71                  <enabled>true</enabled>
 72              </releases>
 73              <snapshots>
 74                  <enabled>false</enabled>
 75              </snapshots>
 76          </pluginRepository>
 77          <pluginRepository>
 78              <id>jboss-earlyaccess-plugin-repository</id>
 79              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 80              <releases>
 81                  <enabled>true</enabled>
 82              </releases>
 83              <snapshots>
 84                  <enabled>false</enabled>
 85              </snapshots>
 86          </pluginRepository>
 87      </pluginRepositories>
 88  
 89      <properties>
 90          <!-- Explicitly declaring the source encoding eliminates the following 
 91              message: -->
 92          <!-- [WARNING] Using platform encoding (UTF-8 actually) to copy filtered 
 93              resources, i.e. build is platform dependent! -->
 94          <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
 95          <!-- Timestamp format for the maven.build.timestamp property -->
 96          <!-- You can reference property in pom.xml or filtered resources 
 97              (must enable third-party plugin if using Maven < 2.1) -->
 98          <maven.build.timestamp.format>yyyyMMdd'T'HHmmss</maven.build.timestamp.format>
 99          <!-- Specify the JBoss EAP directory to be the JBOSS_HOME environment
100              variable -->
101          <jboss.home>${env.JBOSS_HOME}</jboss.home>
102          <version.jboss.bom.eap>7.0.7.GA</version.jboss.bom.eap>
103          <version.wildfly.maven.plugin>1.0.2.Final</version.wildfly.maven.plugin>
104          <version.surefire.plugin>2.10</version.surefire.plugin>
```
  * file:///tmp/source-code/backend-v2/pom.xml
      * Leverage a Maven profile to run the Quarkus native build adding the following section to the `pom.xml` file:. ```xml. <profiles>. <profile>. <id>native</id>. <activation>. <property>. <name>native</name>. </property>. </activation>. <properties>. <skipITs>false</skipITs>. <quarkus.package.type>native</quarkus.package.type>. </properties>. </profile>. </profiles>. ```
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  3      <modelVersion>4.0.0</modelVersion>
  4      <groupId>org.jboss.examples.eap</groupId>
  5      <artifactId>backend-v2</artifactId>
  6      <version>2.0</version>
  7      <packaging>war</packaging>
  8      <name>ticket-monster backend v2</name>
  9      <description>A starter HTML5 + REST webapp project for use on JBoss EAP.</description>
 10  
 11      <!-- Activate JBoss Product Maven repository.
 12  
 13          NOTE: Configuring the Maven repository in the pom.xml file is not a recommended procedure
 14          and is only done here to make it easier to use the quickstarts.
 15  
 16          For more information about how to configure Maven for your application,
 17          see the section entitled 'Use the Maven Repository'
 18          in the Development Guide for Red Hat JBoss Enterprise Application Platform located here:
 19  
 20          https://access.redhat.com/documentation/en-US/JBoss_Enterprise_Application_Platform/
 21      -->
 22      <repositories>
 23          <repository>
 24              <id>redhat-ga-repository</id>
 25              <url>https://maven.repository.redhat.com/ga/</url>
 26              <releases>
 27                  <enabled>true</enabled>
 28              </releases>
 29              <snapshots>
 30                  <enabled>false</enabled>
 31              </snapshots>
 32          </repository>
 33          <repository>
 34              <id>jboss-ga-repository</id>
 35              <url>http://maven.repository.redhat.com/techpreview/all</url>
 36              <releases>
 37                  <enabled>true</enabled>
 38              </releases>
 39              <snapshots>
 40                  <enabled>false</enabled>
 41              </snapshots>
 42          </repository>
 43          <repository>
 44              <id>jboss-earlyaccess-repository</id>
 45              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 46              <releases>
 47                  <enabled>true</enabled>
 48              </releases>
 49              <snapshots>
 50                  <enabled>false</enabled>
 51              </snapshots>
 52          </repository>
 53          <repository>
 54              <id>redhat.ea</id>
 55              <name>Red Hat Early Access Repository</name>
 56              <url>https://maven.repository.redhat.com/earlyaccess/all</url>
 57              <snapshots>
 58                  <enabled>false</enabled>
 59              </snapshots>
 60              <releases>
 61                  <enabled>true</enabled>
 62              </releases>
 63          </repository>
 64      </repositories>
 65  
 66      <pluginRepositories>
 67          <pluginRepository>
 68              <id>redhat-ga-repository</id>
 69              <url>https://maven.repository.redhat.com/ga/</url>
 70              <releases>
 71                  <enabled>true</enabled>
 72              </releases>
 73              <snapshots>
 74                  <enabled>false</enabled>
 75              </snapshots>
 76          </pluginRepository>
 77          <pluginRepository>
 78              <id>jboss-earlyaccess-plugin-repository</id>
 79              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 80              <releases>
 81                  <enabled>true</enabled>
 82              </releases>
 83              <snapshots>
 84                  <enabled>false</enabled>
 85              </snapshots>
 86          </pluginRepository>
 87      </pluginRepositories>
 88  
 89      <properties>
 90          <!-- Explicitly declaring the source encoding eliminates the following 
 91              message: -->
 92          <!-- [WARNING] Using platform encoding (UTF-8 actually) to copy filtered 
 93              resources, i.e. build is platform dependent! -->
 94          <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
 95          <!-- Timestamp format for the maven.build.timestamp property -->
 96          <!-- You can reference property in pom.xml or filtered resources 
 97              (must enable third-party plugin if using Maven < 2.1) -->
 98          <maven.build.timestamp.format>yyyyMMdd'T'HHmmss</maven.build.timestamp.format>
 99          <!-- Specify the JBoss EAP directory to be the JBOSS_HOME environment
100              variable -->
101          <jboss.home>${env.JBOSS_HOME}</jboss.home>
102          <version.jboss.bom.eap>7.0.7.GA</version.jboss.bom.eap>
103          <version.wildfly.maven.plugin>1.0.2.Final</version.wildfly.maven.plugin>
104          <version.surefire.plugin>2.10</version.surefire.plugin>
```
  * file:///tmp/source-code/monolith/pom.xml
      * Leverage a Maven profile to run the Quarkus native build adding the following section to the `pom.xml` file:. ```xml. <profiles>. <profile>. <id>native</id>. <activation>. <property>. <name>native</name>. </property>. </activation>. <properties>. <skipITs>false</skipITs>. <quarkus.package.type>native</quarkus.package.type>. </properties>. </profile>. </profiles>. ```
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  3      <modelVersion>4.0.0</modelVersion>
  4      <groupId>org.jboss.examples.eap</groupId>
  5      <artifactId>ticket-monster</artifactId>
  6      <version>3.0.0-SNAPSHOT</version>
  7      <packaging>war</packaging>
  8      <name>ticket-monster</name>
  9      <description>A starter HTML5 + REST webapp project for use on JBoss EAP.</description>
 10  
 11      <!-- Activate JBoss Product Maven repository.
 12  
 13          NOTE: Configuring the Maven repository in the pom.xml file is not a recommended procedure
 14          and is only done here to make it easier to use the quickstarts.
 15  
 16          For more information about how to configure Maven for your application,
 17          see the section entitled 'Use the Maven Repository'
 18          in the Development Guide for Red Hat JBoss Enterprise Application Platform located here:
 19  
 20          https://access.redhat.com/documentation/en-US/JBoss_Enterprise_Application_Platform/
 21      -->
 22      <repositories>
 23          <repository>
 24              <id>redhat-ga-repository</id>
 25              <url>https://maven.repository.redhat.com/ga/</url>
 26              <releases>
 27                  <enabled>true</enabled>
 28              </releases>
 29              <snapshots>
 30                  <enabled>false</enabled>
 31              </snapshots>
 32          </repository>
 33          <repository>
 34              <id>jboss-ga-repository</id>
 35              <url>http://maven.repository.redhat.com/techpreview/all</url>
 36              <releases>
 37                  <enabled>true</enabled>
 38              </releases>
 39              <snapshots>
 40                  <enabled>false</enabled>
 41              </snapshots>
 42          </repository>
 43          <repository>
 44              <id>jboss-earlyaccess-repository</id>
 45              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 46              <releases>
 47                  <enabled>true</enabled>
 48              </releases>
 49              <snapshots>
 50                  <enabled>false</enabled>
 51              </snapshots>
 52          </repository>
 53          <repository>
 54              <id>redhat.ea</id>
 55              <name>Red Hat Early Access Repository</name>
 56              <url>https://maven.repository.redhat.com/earlyaccess/all</url>
 57              <snapshots>
 58                  <enabled>false</enabled>
 59              </snapshots>
 60              <releases>
 61                  <enabled>true</enabled>
 62              </releases>
 63          </repository>
 64      </repositories>
 65  
 66      <pluginRepositories>
 67          <pluginRepository>
 68              <id>redhat-ga-repository</id>
 69              <url>https://maven.repository.redhat.com/ga/</url>
 70              <releases>
 71                  <enabled>true</enabled>
 72              </releases>
 73              <snapshots>
 74                  <enabled>false</enabled>
 75              </snapshots>
 76          </pluginRepository>
 77          <pluginRepository>
 78              <id>jboss-earlyaccess-plugin-repository</id>
 79              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 80              <releases>
 81                  <enabled>true</enabled>
 82              </releases>
 83              <snapshots>
 84                  <enabled>false</enabled>
 85              </snapshots>
 86          </pluginRepository>
 87      </pluginRepositories>
 88  
 89      <properties>
 90          <!-- Explicitly declaring the source encoding eliminates the following 
 91              message: -->
 92          <!-- [WARNING] Using platform encoding (UTF-8 actually) to copy filtered 
 93              resources, i.e. build is platform dependent! -->
 94          <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
 95          <!-- Timestamp format for the maven.build.timestamp property -->
 96          <!-- You can reference property in pom.xml or filtered resources 
 97              (must enable third-party plugin if using Maven < 2.1) -->
 98          <maven.build.timestamp.format>yyyyMMdd'T'HHmmss</maven.build.timestamp.format>
 99          <!-- Specify the JBoss EAP directory to be the JBOSS_HOME environment
100              variable -->
101          <jboss.home>${env.JBOSS_HOME}</jboss.home>
102          <version.jboss.bom.eap>7.0.7.GA</version.jboss.bom.eap>
103          <version.wildfly.maven.plugin>1.0.2.Final</version.wildfly.maven.plugin>
104          <version.surefire.plugin>2.10</version.surefire.plugin>
```
  * file:///tmp/source-code/orders-service/pom.xml
      * Leverage a Maven profile to run the Quarkus native build adding the following section to the `pom.xml` file:. ```xml. <profiles>. <profile>. <id>native</id>. <activation>. <property>. <name>native</name>. </property>. </activation>. <properties>. <skipITs>false</skipITs>. <quarkus.package.type>native</quarkus.package.type>. </properties>. </profile>. </profiles>. ```
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <project xmlns="http://maven.apache.org/POM/4.0.0"
  3           xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  4           xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  5    <artifactId>orders-service</artifactId>
  6    <groupId>org.ticketmonster.orders</groupId>
  7    <version>1.0.0-SNAPSHOT</version>
  8    <modelVersion>4.0.0</modelVersion>
  9  
 10    <properties>
 11      <spring-boot.version>1.5.6.RELEASE</spring-boot.version>
 12      <docker-maven-plugin.version>0.20.1</docker-maven-plugin.version>
 13      <mysql-server.version>5.7</mysql-server.version>
 14      <mysql.user>ticket</mysql.user>
 15      <mysql.password>monster</mysql.password>
 16      <mysql.port>3306</mysql.port>
 17      <mysql.init.timeout>60000</mysql.init.timeout>
 18      <skipITs>true</skipITs>
 19      <fabric8.maven.plugin.version>3.5.25</fabric8.maven.plugin.version>
 20      <docker.image.name>ceposta/%a:%l</docker.image.name>
 21    </properties>
 22  
 23    <dependencyManagement>
 24      <dependencies>
 25        <dependency>
 26          <!-- Import dependency management from Spring Boot -->
 27          <groupId>org.springframework.boot</groupId>
 28          <artifactId>spring-boot-dependencies</artifactId>
 29          <version>${spring-boot.version}</version>
 30          <type>pom</type>
 31          <scope>import</scope>
 32        </dependency>
 33      </dependencies>
 34    </dependencyManagement>
 35  
 36  
 37    <dependencies>
 38      <dependency>
 39        <groupId>org.springframework.boot</groupId>
 40        <artifactId>spring-boot-starter-web</artifactId>
 41      </dependency>
 42      <dependency>
 43        <groupId>org.springframework.boot</groupId>
 44        <artifactId>spring-boot-starter-actuator</artifactId>
 45      </dependency>
 46      <dependency>
 47        <groupId>org.springframework.boot</groupId>
 48        <artifactId>spring-boot-starter-data-jpa</artifactId>
 49      </dependency>
 50      <dependency>
 51        <groupId>org.teiid.spring</groupId>
 52        <artifactId>teiid-spring-boot-starter</artifactId>
 53        <version>1.0.0-SNAPSHOT</version>
 54      </dependency>
 55  
 56  
 57  
 58      <!-- Testing -->
 59      <dependency>
 60        <groupId>io.rest-assured</groupId>
 61        <artifactId>rest-assured</artifactId>
 62        <version>3.0.3</version>
 63        <scope>test</scope>
 64      </dependency>
 65      <dependency>
 66        <groupId>io.rest-assured</groupId>
 67        <artifactId>json-schema-validator</artifactId>
 68        <version>3.0.3</version>
 69        <scope>test</scope>
 70      </dependency>
 71      <dependency>
 72        <groupId>io.specto</groupId>
 73        <artifactId>hoverfly-java</artifactId>
 74        <version>0.8.0</version>
 75        <scope>test</scope>
 76      </dependency>
 77      <dependency>
 78        <groupId>org.springframework.boot</groupId>
 79        <artifactId>spring-boot-starter-test</artifactId>
 80        <scope>test</scope>
 81      </dependency>
 82      <dependency>
 83        <groupId>com.h2database</groupId>
 84        <artifactId>h2</artifactId>
 85        <scope>test</scope>
 86      </dependency>
 87  
 88      <dependency>
 89        <groupId>au.com.dius</groupId>
 90        <artifactId>pact-jvm-provider-junit_2.11</artifactId>
 91        <version>3.5.0</version>
 92      </dependency>
 93    </dependencies>
 94  
 95    <build>
 96      <plugins>
 97        <plugin>
 98          <groupId>org.springframework.boot</groupId>
 99          <artifactId>spring-boot-maven-plugin</artifactId>
100          <version>${spring-boot.version}</version>
101          <executions>
102            <execution>
103              <goals>
104                <goal>repackage</goal>
105              </goals>
106            </execution>
```
  * file:///tmp/source-code/pom.xml
      * Leverage a Maven profile to run the Quarkus native build adding the following section to the `pom.xml` file:. ```xml. <profiles>. <profile>. <id>native</id>. <activation>. <property>. <name>native</name>. </property>. </activation>. <properties>. <skipITs>false</skipITs>. <quarkus.package.type>native</quarkus.package.type>. </properties>. </profile>. </profiles>. ```
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  3      <modelVersion>4.0.0</modelVersion>
  4      <groupId>org.jboss.examples.eap</groupId>
  5      <artifactId>ticket-monster-parent</artifactId>
  6      <version>3.0.0-SNAPSHOT</version>
  7      <modules>
  8          <module>monolith</module>
  9          <module>backend-v1</module>
 10          <module>backend-v2</module>
 11          <module>orders-service</module>
 12      </modules>
 13      <packaging>pom</packaging>
 14      <name>Ticket Monster Parent</name>
 15      <description>A starter HTML5 + REST webapp project for use on JBoss EAP.</description>
 16  
 17      <!-- Activate JBoss Product Maven repository.
 18  
 19          NOTE: Configuring the Maven repository in the pom.xml file is not a recommended procedure
 20          and is only done here to make it easier to use the quickstarts.
 21  
 22          For more information about how to configure Maven for your application,
 23          see the section entitled 'Use the Maven Repository'
 24          in the Development Guide for Red Hat JBoss Enterprise Application Platform located here:
 25  
 26          https://access.redhat.com/documentation/en-US/JBoss_Enterprise_Application_Platform/
 27      -->
 28      <repositories>
 29          <repository>
 30              <id>redhat-ga-repository</id>
 31              <url>https://maven.repository.redhat.com/ga/</url>
 32              <releases>
 33                  <enabled>true</enabled>
 34              </releases>
 35              <snapshots>
 36                  <enabled>false</enabled>
 37              </snapshots>
 38          </repository>
 39          <repository>
 40              <id>jboss-ga-repository</id>
 41              <url>http://maven.repository.redhat.com/techpreview/all</url>
 42              <releases>
 43                  <enabled>true</enabled>
 44              </releases>
 45              <snapshots>
 46                  <enabled>false</enabled>
 47              </snapshots>
 48          </repository>
 49          <repository>
 50              <id>jboss-earlyaccess-repository</id>
 51              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 52              <releases>
 53                  <enabled>true</enabled>
 54              </releases>
 55              <snapshots>
 56                  <enabled>false</enabled>
 57              </snapshots>
 58          </repository>
 59          <repository>
 60              <id>redhat.ea</id>
 61              <name>Red Hat Early Access Repository</name>
 62              <url>https://maven.repository.redhat.com/earlyaccess/all</url>
 63              <snapshots>
 64                  <enabled>false</enabled>
 65              </snapshots>
 66              <releases>
 67                  <enabled>true</enabled>
 68              </releases>
 69          </repository>
 70      </repositories>
 71  
 72      <pluginRepositories>
 73          <pluginRepository>
 74              <id>redhat-ga-repository</id>
 75              <url>https://maven.repository.redhat.com/ga/</url>
 76              <releases>
 77                  <enabled>true</enabled>
 78              </releases>
 79              <snapshots>
 80                  <enabled>false</enabled>
 81              </snapshots>
 82          </pluginRepository>
 83          <pluginRepository>
 84              <id>jboss-earlyaccess-plugin-repository</id>
 85              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 86              <releases>
 87                  <enabled>true</enabled>
 88              </releases>
 89              <snapshots>
 90                  <enabled>false</enabled>
 91              </snapshots>
 92          </pluginRepository>
 93      </pluginRepositories>
 94  
 95      <build>
 96          <plugins>
 97              <plugin>
 98                  <artifactId>maven-compiler-plugin</artifactId>
 99                  <version>2.3.1</version>
100                  <configuration>
101                      <source>1.8</source>
102                      <target>1.8</target>
103                  </configuration>
104              </plugin>
```
### #13 - javaee-pom-to-quarkus-00070
* Category: mandatory
* Effort: 1
* Description: Configure Quarkus hibernate-orm
Configure Quarkus 'hibernate-orm` and jakarta persistence.. Add the `quarkus-hibernate-orm` section and one for your preferred jdbc solution to the `pom.xml` file, eg for postgres:. ```. <!-- Hibernate ORM specific dependencies -->. <dependency>. <groupId>io.quarkus</groupId>. <artifactId>quarkus-hibernate-orm</artifactId>. </dependency>. <!-- JDBC driver dependencies -->. <dependency>. <groupId>io.quarkus</groupId>. <artifactId>quarkus-jdbc-postgresql</artifactId>. </dependency>. ```
* Labels: konveyor.io/source=java-ee, konveyor.io/target=quarkus
* Links
  * Using hibernate-orm and jakarta persistence: https://quarkus.io/guides/hibernate-orm
* Incidents
  * file:///tmp/source-code/backend-v1/pom.xml
      * Configure Quarkus 'hibernate-orm` and jakarta persistence.. Add the `quarkus-hibernate-orm` section and one for your preferred jdbc solution to the `pom.xml` file, eg for postgres:. ```. <!-- Hibernate ORM specific dependencies -->. <dependency>. <groupId>io.quarkus</groupId>. <artifactId>quarkus-hibernate-orm</artifactId>. </dependency>. <!-- JDBC driver dependencies -->. <dependency>. <groupId>io.quarkus</groupId>. <artifactId>quarkus-jdbc-postgresql</artifactId>. </dependency>. ```
      * Code Snippet:
```java
 67          <pluginRepository>
 68              <id>redhat-ga-repository</id>
 69              <url>https://maven.repository.redhat.com/ga/</url>
 70              <releases>
 71                  <enabled>true</enabled>
 72              </releases>
 73              <snapshots>
 74                  <enabled>false</enabled>
 75              </snapshots>
 76          </pluginRepository>
 77          <pluginRepository>
 78              <id>jboss-earlyaccess-plugin-repository</id>
 79              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 80              <releases>
 81                  <enabled>true</enabled>
 82              </releases>
 83              <snapshots>
 84                  <enabled>false</enabled>
 85              </snapshots>
 86          </pluginRepository>
 87      </pluginRepositories>
 88  
 89      <properties>
 90          <!-- Explicitly declaring the source encoding eliminates the following 
 91              message: -->
 92          <!-- [WARNING] Using platform encoding (UTF-8 actually) to copy filtered 
 93              resources, i.e. build is platform dependent! -->
 94          <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
 95          <!-- Timestamp format for the maven.build.timestamp property -->
 96          <!-- You can reference property in pom.xml or filtered resources 
 97              (must enable third-party plugin if using Maven < 2.1) -->
 98          <maven.build.timestamp.format>yyyyMMdd'T'HHmmss</maven.build.timestamp.format>
 99          <!-- Specify the JBoss EAP directory to be the JBOSS_HOME environment
100              variable -->
101          <jboss.home>${env.JBOSS_HOME}</jboss.home>
102          <version.jboss.bom.eap>7.0.7.GA</version.jboss.bom.eap>
103          <version.wildfly.maven.plugin>1.0.2.Final</version.wildfly.maven.plugin>
104          <version.surefire.plugin>2.10</version.surefire.plugin>
105          <buildhelper.plugin.version>1.7</buildhelper.plugin.version>
106          <fabric8.maven.plugin.version>3.5.25</fabric8.maven.plugin.version>
107          <docker.image.name>ceposta/%a:%l</docker.image.name>
108      </properties>
109  
110      <dependencyManagement>
111          <dependencies>
112              <dependency>
113                  <groupId>org.jboss.bom</groupId>
114                  <artifactId>jboss-eap-javaee7-with-tools</artifactId>
115                  <version>${version.jboss.bom.eap}</version>
116                  <type>pom</type>
117                  <scope>import</scope>
118              </dependency>
119          </dependencies>
120      </dependencyManagement>
121  
122      <dependencies>
123  
124          <!-- First declare the APIs we depend on and need for compilation. 
125              All of them are provided by JBoss EAP -->
126  
127          <!-- Import the CDI API, we use provided scope as the API is included 
128              in JBoss EAP -->
129          <dependency>
130              <groupId>javax.enterprise</groupId>
131              <artifactId>cdi-api</artifactId>
132              <scope>provided</scope>
133          </dependency>
134          
135          <dependency>
136              <groupId>javax.inject</groupId>
137              <artifactId>javax.inject</artifactId>
138              <scope>provided</scope>
139          </dependency>
140          
141          <dependency>
142              <groupId>javax.validation</groupId>
143              <artifactId>validation-api</artifactId>
144              <scope>provided</scope>
145          </dependency>
146         
147          <!-- Import the Common Annotations API (JSR-250), we use provided 
148              scope as the API is included in JBoss EAP -->
149          <dependency>
150              <groupId>org.jboss.spec.javax.annotation</groupId>
151              <artifactId>jboss-annotations-api_1.2_spec</artifactId>
152              <scope>provided</scope>
153          </dependency>
154  
155          <!-- Import the JAX-RS API, we use provided scope as the API is included 
156              in JBoss EAP -->
157          <dependency>
158              <groupId>org.jboss.spec.javax.ws.rs</groupId>
159              <artifactId>jboss-jaxrs-api_2.0_spec</artifactId>
160              <scope>provided</scope>
161          </dependency>
162  
163          <!-- Import the JPA API, we use provided scope as the API is included 
164              in JBoss EAP -->
165          <dependency>
166              <groupId>org.hibernate.javax.persistence</groupId>
167              <artifactId>hibernate-jpa-2.1-api</artifactId>
168              <scope>provided</scope>
169          </dependency>
170  
171          <!-- Import the EJB API, we use provided scope as the API is included 
172              in JBoss EAP -->
173          <dependency>
174              <groupId>org.jboss.spec.javax.ejb</groupId>
175              <artifactId>jboss-ejb-api_3.2_spec</artifactId>
176              <scope>provided</scope>
177          </dependency>
178  
179          <!-- Import the Servlet API, we use provided scope as the API is 
180              included in JBoss EAP -->
181          <dependency>
182              <groupId>org.jboss.spec.javax.servlet</groupId>
183              <artifactId>jboss-servlet-api_3.1_spec</artifactId>
184              <scope>provided</scope>
185          </dependency>
186  
187          <!-- JSR-303 (Bean Validation) Implementation -->
188          <!-- Provides portable constraints such as @Email -->
189          <!-- Hibernate Validator is shipped in JBoss EAP -->
190          <dependency>
191              <groupId>org.hibernate</groupId>
192              <artifactId>hibernate-validator</artifactId>
193              <scope>provided</scope>
194              <exclusions>
195                  <exclusion>
196                      <groupId>org.slf4j</groupId>
197                      <artifactId>slf4j-api</artifactId>
198                  </exclusion>
199              </exclusions>
200          </dependency>
201  
202  
203          <!-- Now we declare any tools needed -->
204  
205          <!-- Annotation processor to generate the JPA 2.0 metamodel classes 
206              for typesafe criteria queries -->
207          <dependency>
208              <groupId>org.hibernate</groupId>
209              <artifactId>hibernate-jpamodelgen</artifactId>
210              <scope>provided</scope>
211          </dependency>
212  
213          <!-- Needed for running tests (you may also use TestNG) -->
214          <dependency>
215              <groupId>junit</groupId>
216              <artifactId>junit</artifactId>
217              <scope>test</scope>
218          </dependency>
219  
220          <!-- Optional, but highly recommended -->
221          <!-- Arquillian allows you to test enterprise code such as EJBs and 
222              Transactional(JTA) JPA from JUnit/TestNG -->
223          <dependency>
224              <groupId>org.jboss.arquillian.junit</groupId>
225              <artifactId>arquillian-junit-container</artifactId>
226              <scope>test</scope>
227          </dependency>
228  
229          <dependency>
230              <groupId>org.jboss.arquillian.protocol</groupId>
231              <artifactId>arquillian-protocol-servlet</artifactId>
232              <scope>test</scope>
233          </dependency>
234          
235          <dependency>
236              <groupId>org.jboss.shrinkwrap.resolver</groupId>
237              <artifactId>shrinkwrap-resolver-depchain</artifactId>
238              <type>pom</type>
239              <scope>test</scope>
240          </dependency>
241  
242          <!-- RESTEasy dependencies that bring in Jackson Core and RESTEasy APIs+SPIs, which we use for
243              fine tuning the content of the JSON responses -->
244          <dependency>
245              <groupId>org.jboss.resteasy</groupId>
246              <artifactId>resteasy-jackson2-provider</artifactId>
247              <scope>provided</scope>
248          </dependency>
249          <dependency>
250              <groupId>org.jboss.resteasy</groupId>
251              <artifactId>resteasy-jaxrs</artifactId>
252              <scope>provided</scope>
253          </dependency>
254  
255      </dependencies>
256  
257      <build>
258          <!-- Maven will append the version to the finalName (which is the
259         name given to the generated war, and hence the context root) -->
260          <finalName>ROOT</finalName>
261          <pluginManagement>
262  
263              <plugins>
264                  <!-- Compiler plugin enforces Java 1.8 compatibility and activates
265                annotation processors -->
266                  <plugin>
267                      <artifactId>maven-compiler-plugin</artifactId>
```
  * file:///tmp/source-code/backend-v2/pom.xml
      * Configure Quarkus 'hibernate-orm` and jakarta persistence.. Add the `quarkus-hibernate-orm` section and one for your preferred jdbc solution to the `pom.xml` file, eg for postgres:. ```. <!-- Hibernate ORM specific dependencies -->. <dependency>. <groupId>io.quarkus</groupId>. <artifactId>quarkus-hibernate-orm</artifactId>. </dependency>. <!-- JDBC driver dependencies -->. <dependency>. <groupId>io.quarkus</groupId>. <artifactId>quarkus-jdbc-postgresql</artifactId>. </dependency>. ```
      * Code Snippet:
```java
 78              <id>jboss-earlyaccess-plugin-repository</id>
 79              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 80              <releases>
 81                  <enabled>true</enabled>
 82              </releases>
 83              <snapshots>
 84                  <enabled>false</enabled>
 85              </snapshots>
 86          </pluginRepository>
 87      </pluginRepositories>
 88  
 89      <properties>
 90          <!-- Explicitly declaring the source encoding eliminates the following 
 91              message: -->
 92          <!-- [WARNING] Using platform encoding (UTF-8 actually) to copy filtered 
 93              resources, i.e. build is platform dependent! -->
 94          <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
 95          <!-- Timestamp format for the maven.build.timestamp property -->
 96          <!-- You can reference property in pom.xml or filtered resources 
 97              (must enable third-party plugin if using Maven < 2.1) -->
 98          <maven.build.timestamp.format>yyyyMMdd'T'HHmmss</maven.build.timestamp.format>
 99          <!-- Specify the JBoss EAP directory to be the JBOSS_HOME environment
100              variable -->
101          <jboss.home>${env.JBOSS_HOME}</jboss.home>
102          <version.jboss.bom.eap>7.0.7.GA</version.jboss.bom.eap>
103          <version.wildfly.maven.plugin>1.0.2.Final</version.wildfly.maven.plugin>
104          <version.surefire.plugin>2.10</version.surefire.plugin>
105          <buildhelper.plugin.version>1.7</buildhelper.plugin.version>
106          <fabric8.maven.plugin.version>3.5.25</fabric8.maven.plugin.version>
107          <docker.image.name>ceposta/%a:%l</docker.image.name>
108          <ffj4.version>1.6.5</ffj4.version>
109          <version.org.jboss.arquillian>1.1.12.Final</version.org.jboss.arquillian>
110          <version.org.wildfly.arquillian.container>2.0.0.Final</version.org.wildfly.arquillian.container>
111      </properties>
112  
113      <dependencyManagement>
114          <dependencies>
115              <dependency>
116                  <groupId>org.jboss.arquillian</groupId>
117                  <artifactId>arquillian-bom</artifactId>
118                  <version>${version.org.jboss.arquillian}</version>
119                  <type>pom</type>
120                  <scope>import</scope>
121              </dependency>
122              <dependency>
123                  <groupId>org.jboss.bom</groupId>
124                  <artifactId>jboss-eap-javaee7-with-tools</artifactId>
125                  <version>${version.jboss.bom.eap}</version>
126                  <type>pom</type>
127                  <scope>import</scope>
128              </dependency>
129  
130          </dependencies>
131      </dependencyManagement>
132  
133      <dependencies>
134  
135          <!-- First declare the APIs we depend on and need for compilation. 
136              All of them are provided by JBoss EAP -->
137  
138          <!-- Import the CDI API, we use provided scope as the API is included 
139              in JBoss EAP -->
140          <dependency>
141              <groupId>javax.enterprise</groupId>
142              <artifactId>cdi-api</artifactId>
143              <scope>provided</scope>
144          </dependency>
145          
146          <dependency>
147              <groupId>javax.inject</groupId>
148              <artifactId>javax.inject</artifactId>
149              <scope>provided</scope>
150          </dependency>
151          
152          <dependency>
153              <groupId>javax.validation</groupId>
154              <artifactId>validation-api</artifactId>
155              <scope>provided</scope>
156          </dependency>
157         
158          <!-- Import the Common Annotations API (JSR-250), we use provided 
159              scope as the API is included in JBoss EAP -->
160          <dependency>
161              <groupId>org.jboss.spec.javax.annotation</groupId>
162              <artifactId>jboss-annotations-api_1.2_spec</artifactId>
163              <scope>provided</scope>
164          </dependency>
165  
166          <!-- Import the JAX-RS API, we use provided scope as the API is included 
167              in JBoss EAP -->
168          <dependency>
169              <groupId>org.jboss.spec.javax.ws.rs</groupId>
170              <artifactId>jboss-jaxrs-api_2.0_spec</artifactId>
171              <scope>provided</scope>
172          </dependency>
173  
174          <!-- Import the JPA API, we use provided scope as the API is included 
175              in JBoss EAP -->
176          <dependency>
177              <groupId>org.hibernate.javax.persistence</groupId>
178              <artifactId>hibernate-jpa-2.1-api</artifactId>
179              <scope>provided</scope>
180          </dependency>
181  
182          <!-- Import the EJB API, we use provided scope as the API is included 
183              in JBoss EAP -->
184          <dependency>
185              <groupId>org.jboss.spec.javax.ejb</groupId>
186              <artifactId>jboss-ejb-api_3.2_spec</artifactId>
187              <scope>provided</scope>
188          </dependency>
189  
190          <!-- Import the Servlet API, we use provided scope as the API is 
191              included in JBoss EAP -->
192          <dependency>
193              <groupId>org.jboss.spec.javax.servlet</groupId>
194              <artifactId>jboss-servlet-api_3.1_spec</artifactId>
195              <scope>provided</scope>
196          </dependency>
197  
198          <dependency>
199              <groupId>org.ff4j</groupId>
200              <artifactId>ff4j-core</artifactId>
201              <version>${ffj4.version}</version>
202          </dependency>
203          <dependency>
204              <groupId>org.ff4j</groupId>
205              <artifactId>ff4j-web</artifactId>
206              <version>${ffj4.version}</version>
207          </dependency>
208  
209          <!-- JSR-303 (Bean Validation) Implementation -->
210          <!-- Provides portable constraints such as @Email -->
211          <!-- Hibernate Validator is shipped in JBoss EAP -->
212          <dependency>
213              <groupId>org.hibernate</groupId>
214              <artifactId>hibernate-validator</artifactId>
215              <scope>provided</scope>
216              <exclusions>
217                  <exclusion>
218                      <groupId>org.slf4j</groupId>
219                      <artifactId>slf4j-api</artifactId>
220                  </exclusion>
221              </exclusions>
222          </dependency>
223  
224  
225          <!-- Now we declare any tools needed -->
226  
227          <!-- Annotation processor to generate the JPA 2.0 metamodel classes 
228              for typesafe criteria queries -->
229          <dependency>
230              <groupId>org.hibernate</groupId>
231              <artifactId>hibernate-jpamodelgen</artifactId>
232              <scope>provided</scope>
233          </dependency>
234  
235          <!-- Needed for running tests (you may also use TestNG) -->
236          <dependency>
237              <groupId>junit</groupId>
238              <artifactId>junit</artifactId>
239              <scope>test</scope>
240          </dependency>
241  
242          <!-- For service virtualization/mocking-->
243          <dependency>
244              <groupId>io.specto</groupId>
245              <artifactId>hoverfly-java</artifactId>
246              <version>0.8.0</version>
247              <scope>test</scope>
248          </dependency>
249  
250          <!-- Optional, but highly recommended -->
251          <!-- Arquillian allows you to test enterprise code such as EJBs and 
252              Transactional(JTA) JPA from JUnit/TestNG -->
253          <dependency>
254              <groupId>org.jboss.arquillian.junit</groupId>
255              <artifactId>arquillian-junit-container</artifactId>
256              <scope>test</scope>
257          </dependency>
258  
259          <dependency>
260              <groupId>org.jboss.arquillian.protocol</groupId>
261              <artifactId>arquillian-protocol-servlet</artifactId>
262              <scope>test</scope>
263          </dependency>
264          
265          <dependency>
266              <groupId>org.jboss.shrinkwrap.resolver</groupId>
267              <artifactId>shrinkwrap-resolver-depchain</artifactId>
268              <type>pom</type>
269              <scope>test</scope>
270          </dependency>
271  
272          <!-- RESTEasy dependencies that bring in Jackson Core and RESTEasy APIs+SPIs, which we use for
273              fine tuning the content of the JSON responses -->
274          <dependency>
275              <groupId>org.jboss.resteasy</groupId>
276              <artifactId>resteasy-jackson2-provider</artifactId>
277              <scope>provided</scope>
278              <exclusions>
```
  * file:///tmp/source-code/monolith/pom.xml
      * Configure Quarkus 'hibernate-orm` and jakarta persistence.. Add the `quarkus-hibernate-orm` section and one for your preferred jdbc solution to the `pom.xml` file, eg for postgres:. ```. <!-- Hibernate ORM specific dependencies -->. <dependency>. <groupId>io.quarkus</groupId>. <artifactId>quarkus-hibernate-orm</artifactId>. </dependency>. <!-- JDBC driver dependencies -->. <dependency>. <groupId>io.quarkus</groupId>. <artifactId>quarkus-jdbc-postgresql</artifactId>. </dependency>. ```
      * Code Snippet:
```java
 67          <pluginRepository>
 68              <id>redhat-ga-repository</id>
 69              <url>https://maven.repository.redhat.com/ga/</url>
 70              <releases>
 71                  <enabled>true</enabled>
 72              </releases>
 73              <snapshots>
 74                  <enabled>false</enabled>
 75              </snapshots>
 76          </pluginRepository>
 77          <pluginRepository>
 78              <id>jboss-earlyaccess-plugin-repository</id>
 79              <url>http://maven.repository.redhat.com/earlyaccess/all/</url>
 80              <releases>
 81                  <enabled>true</enabled>
 82              </releases>
 83              <snapshots>
 84                  <enabled>false</enabled>
 85              </snapshots>
 86          </pluginRepository>
 87      </pluginRepositories>
 88  
 89      <properties>
 90          <!-- Explicitly declaring the source encoding eliminates the following 
 91              message: -->
 92          <!-- [WARNING] Using platform encoding (UTF-8 actually) to copy filtered 
 93              resources, i.e. build is platform dependent! -->
 94          <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
 95          <!-- Timestamp format for the maven.build.timestamp property -->
 96          <!-- You can reference property in pom.xml or filtered resources 
 97              (must enable third-party plugin if using Maven < 2.1) -->
 98          <maven.build.timestamp.format>yyyyMMdd'T'HHmmss</maven.build.timestamp.format>
 99          <!-- Specify the JBoss EAP directory to be the JBOSS_HOME environment
100              variable -->
101          <jboss.home>${env.JBOSS_HOME}</jboss.home>
102          <version.jboss.bom.eap>7.0.7.GA</version.jboss.bom.eap>
103          <version.wildfly.maven.plugin>1.0.2.Final</version.wildfly.maven.plugin>
104          <version.surefire.plugin>2.10</version.surefire.plugin>
105          <buildhelper.plugin.version>1.7</buildhelper.plugin.version>
106          <fabric8.maven.plugin.version>3.5.25</fabric8.maven.plugin.version>
107          <docker.image.name>%g/%a:%l</docker.image.name>
108      </properties>
109  
110      <dependencyManagement>
111          <dependencies>
112              <dependency>
113                  <groupId>org.jboss.bom</groupId>
114                  <artifactId>jboss-eap-javaee7-with-tools</artifactId>
115                  <version>${version.jboss.bom.eap}</version>
116                  <type>pom</type>
117                  <scope>import</scope>
118              </dependency>
119          </dependencies>
120      </dependencyManagement>
121  
122      <dependencies>
123  
124          <!-- First declare the APIs we depend on and need for compilation. 
125              All of them are provided by JBoss EAP -->
126  
127          <!-- Import the CDI API, we use provided scope as the API is included 
128              in JBoss EAP -->
129          <dependency>
130              <groupId>javax.enterprise</groupId>
131              <artifactId>cdi-api</artifactId>
132              <scope>provided</scope>
133          </dependency>
134  
135          <dependency>
136              <groupId>javax.inject</groupId>
137              <artifactId>javax.inject</artifactId>
138              <scope>provided</scope>
139          </dependency>
140  
141          <dependency>
142              <groupId>javax.validation</groupId>
143              <artifactId>validation-api</artifactId>
144              <scope>provided</scope>
145          </dependency>
146  
147          <!-- Import the Common Annotations API (JSR-250), we use provided 
148              scope as the API is included in JBoss EAP -->
149          <dependency>
150              <groupId>org.jboss.spec.javax.annotation</groupId>
151              <artifactId>jboss-annotations-api_1.2_spec</artifactId>
152              <scope>provided</scope>
153          </dependency>
154  
155          <!-- Import the JAX-RS API, we use provided scope as the API is included 
156              in JBoss EAP -->
157          <dependency>
158              <groupId>org.jboss.spec.javax.ws.rs</groupId>
159              <artifactId>jboss-jaxrs-api_2.0_spec</artifactId>
160              <scope>provided</scope>
161          </dependency>
162  
163          <!-- Import the JPA API, we use provided scope as the API is included 
164              in JBoss EAP -->
165          <dependency>
166              <groupId>org.hibernate.javax.persistence</groupId>
167              <artifactId>hibernate-jpa-2.1-api</artifactId>
168              <scope>provided</scope>
169          </dependency>
170  
171          <!-- Import the EJB API, we use provided scope as the API is included 
172              in JBoss EAP -->
173          <dependency>
174              <groupId>org.jboss.spec.javax.ejb</groupId>
175              <artifactId>jboss-ejb-api_3.2_spec</artifactId>
176              <scope>provided</scope>
177          </dependency>
178  
179          <!-- Import the Servlet API, we use provided scope as the API is 
180              included in JBoss EAP -->
181          <dependency>
182              <groupId>org.jboss.spec.javax.servlet</groupId>
183              <artifactId>jboss-servlet-api_3.1_spec</artifactId>
184              <scope>provided</scope>
185          </dependency>
186  
187          <!-- JSR-303 (Bean Validation) Implementation -->
188          <!-- Provides portable constraints such as @Email -->
189          <!-- Hibernate Validator is shipped in JBoss EAP -->
190          <dependency>
191              <groupId>org.hibernate</groupId>
192              <artifactId>hibernate-validator</artifactId>
193              <scope>provided</scope>
194              <exclusions>
195                  <exclusion>
196                      <groupId>org.slf4j</groupId>
197                      <artifactId>slf4j-api</artifactId>
198                  </exclusion>
199              </exclusions>
200          </dependency>
201  
202  
203          <!-- Now we declare any tools needed -->
204  
205          <!-- Annotation processor to generate the JPA 2.0 metamodel classes 
206              for typesafe criteria queries -->
207          <dependency>
208              <groupId>org.hibernate</groupId>
209              <artifactId>hibernate-jpamodelgen</artifactId>
210              <scope>provided</scope>
211          </dependency>
212  
213          <!-- Needed for running tests (you may also use TestNG) -->
214          <dependency>
215              <groupId>junit</groupId>
216              <artifactId>junit</artifactId>
217              <scope>test</scope>
218          </dependency>
219  
220          <!-- Optional, but highly recommended -->
221          <!-- Arquillian allows you to test enterprise code such as EJBs and 
222              Transactional(JTA) JPA from JUnit/TestNG -->
223          <dependency>
224              <groupId>org.jboss.arquillian.junit</groupId>
225              <artifactId>arquillian-junit-container</artifactId>
226              <scope>test</scope>
227          </dependency>
228  
229          <dependency>
230              <groupId>org.jboss.arquillian.protocol</groupId>
231              <artifactId>arquillian-protocol-servlet</artifactId>
232              <scope>test</scope>
233          </dependency>
234  
235          <dependency>
236              <groupId>org.jboss.shrinkwrap.resolver</groupId>
237              <artifactId>shrinkwrap-resolver-depchain</artifactId>
238              <type>pom</type>
239              <scope>test</scope>
240          </dependency>
241  
242          <!-- RESTEasy dependencies that bring in Jackson Core and RESTEasy APIs+SPIs, which we use for
243              fine tuning the content of the JSON responses -->
244          <dependency>
245              <groupId>org.jboss.resteasy</groupId>
246              <artifactId>resteasy-jackson2-provider</artifactId>
247              <scope>provided</scope>
248          </dependency>
249          <dependency>
250              <groupId>org.jboss.resteasy</groupId>
251              <artifactId>resteasy-jaxrs</artifactId>
252              <scope>provided</scope>
253          </dependency>
254  
255      </dependencies>
256  
257      <build>
258          <!-- Maven will append the version to the finalName (which is the
259         name given to the generated war, and hence the context root) -->
260          <finalName>${project.artifactId}</finalName>
261          <pluginManagement>
262  
263              <plugins>
264                  <!-- Compiler plugin enforces Java 1.8 compatibility and activates
265                annotation processors -->
266                  <plugin>
267                      <artifactId>maven-compiler-plugin</artifactId>
```
### #14 - javaee-pom-to-quarkus-00080
* Category: mandatory
* Effort: 1
* Description: Use Quarkus junit artifact
Use Quarkus junit artifact:. ```. <!-- Quarkus junit specific dependency -->. <dependency>. <groupId>io.quarkus</groupId>. <artifactId>quarkus-junit5</artifactId>. <scope>test</scope>. </dependency>. ```
* Labels: konveyor.io/source=java-ee, konveyor.io/target=quarkus
* Links
  * Quarkus - Testing your application: https://quarkus.io/guides/getting-started-testing
  * Testing your Quarkus application with JUnit: https://access.redhat.com/documentation/en-us/red_hat_build_of_quarkus/1.3/html/getting_started_with_quarkus/proc-quarkus-junit-testing_quarkus-getting-started
* Incidents
  * file:///tmp/source-code/pom.xml
      * Use Quarkus junit artifact:. ```. <!-- Quarkus junit specific dependency -->. <dependency>. <groupId>io.quarkus</groupId>. <artifactId>quarkus-junit5</artifactId>. <scope>test</scope>. </dependency>. ```
### #15 - jaxrs-to-quarkus-00020
* Category: optional
* Effort: 1
* Description: JAX-RS activation is no longer necessary
JAX-RS activation is no longer necessary. You can set a root path like this but you don't have to.
* Labels: konveyor.io/source=java-ee, konveyor.io/target=quarkus
* Links
  * Quarkus - Guide: https://quarkus.io/guides/resteasy-reactive#declaring-endpoints-uri-mapping
* Incidents
  * file:///tmp/source-code/backend-v1/src/main/java/org/jboss/examples/ticketmonster/rest/JaxRsActivator.java
      * JAX-RS activation is no longer necessary. You can set a root path like this but you don't have to.
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import javax.ws.rs.ApplicationPath;
  4  import javax.ws.rs.core.Application;
  5  
  6  /**
  7   * A class extending {@link Application} and annotated with @ApplicationPath is the Java EE
  8   * "no XML" approach to activating JAX-RS.
  9   * 
 10   * <p>
 11   * Resources are served relative to the servlet path specified in the {@link ApplicationPath}
 12   * annotation.
 13   * </p>
 14   */
 15  @ApplicationPath("/rest")
 16  public class JaxRsActivator extends Application {
 17     /* class body intentionally left blank */
 18  }

```
  * file:///tmp/source-code/backend-v1/src/main/java/org/jboss/examples/ticketmonster/rest/JaxRsActivator.java
      * JAX-RS activation is no longer necessary. You can set a root path like this but you don't have to.
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import javax.ws.rs.ApplicationPath;
  4  import javax.ws.rs.core.Application;
  5  
  6  /**
  7   * A class extending {@link Application} and annotated with @ApplicationPath is the Java EE
  8   * "no XML" approach to activating JAX-RS.
  9   * 
 10   * <p>
 11   * Resources are served relative to the servlet path specified in the {@link ApplicationPath}
 12   * annotation.
 13   * </p>
 14   */
 15  @ApplicationPath("/rest")
 16  public class JaxRsActivator extends Application {
 17     /* class body intentionally left blank */
 18  }

```
  * file:///tmp/source-code/backend-v2/src/main/java/org/jboss/examples/ticketmonster/rest/JaxRsActivator.java
      * JAX-RS activation is no longer necessary. You can set a root path like this but you don't have to.
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import javax.ws.rs.ApplicationPath;
  4  import javax.ws.rs.core.Application;
  5  
  6  /**
  7   * A class extending {@link Application} and annotated with @ApplicationPath is the Java EE
  8   * "no XML" approach to activating JAX-RS.
  9   * 
 10   * <p>
 11   * Resources are served relative to the servlet path specified in the {@link ApplicationPath}
 12   * annotation.
 13   * </p>
 14   */
 15  @ApplicationPath("/rest")
 16  public class JaxRsActivator extends Application {
 17     /* class body intentionally left blank */
 18  }

```
  * file:///tmp/source-code/backend-v2/src/main/java/org/jboss/examples/ticketmonster/rest/JaxRsActivator.java
      * JAX-RS activation is no longer necessary. You can set a root path like this but you don't have to.
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import javax.ws.rs.ApplicationPath;
  4  import javax.ws.rs.core.Application;
  5  
  6  /**
  7   * A class extending {@link Application} and annotated with @ApplicationPath is the Java EE
  8   * "no XML" approach to activating JAX-RS.
  9   * 
 10   * <p>
 11   * Resources are served relative to the servlet path specified in the {@link ApplicationPath}
 12   * annotation.
 13   * </p>
 14   */
 15  @ApplicationPath("/rest")
 16  public class JaxRsActivator extends Application {
 17     /* class body intentionally left blank */
 18  }

```
  * file:///tmp/source-code/monolith/src/main/java/org/jboss/examples/ticketmonster/rest/JaxRsActivator.java
      * JAX-RS activation is no longer necessary. You can set a root path like this but you don't have to.
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import javax.ws.rs.ApplicationPath;
  4  import javax.ws.rs.core.Application;
  5  
  6  /**
  7   * A class extending {@link Application} and annotated with @ApplicationPath is the Java EE
  8   * "no XML" approach to activating JAX-RS.
  9   * 
 10   * <p>
 11   * Resources are served relative to the servlet path specified in the {@link ApplicationPath}
 12   * annotation.
 13   * </p>
 14   */
 15  @ApplicationPath("/rest")
 16  public class JaxRsActivator extends Application {
 17     /* class body intentionally left blank */
 18  }

```
  * file:///tmp/source-code/monolith/src/main/java/org/jboss/examples/ticketmonster/rest/JaxRsActivator.java
      * JAX-RS activation is no longer necessary. You can set a root path like this but you don't have to.
      * Code Snippet:
```java
  1  package org.jboss.examples.ticketmonster.rest;
  2  
  3  import javax.ws.rs.ApplicationPath;
  4  import javax.ws.rs.core.Application;
  5  
  6  /**
  7   * A class extending {@link Application} and annotated with @ApplicationPath is the Java EE
  8   * "no XML" approach to activating JAX-RS.
  9   * 
 10   * <p>
 11   * Resources are served relative to the servlet path specified in the {@link ApplicationPath}
 12   * annotation.
 13   * </p>
 14   */
 15  @ApplicationPath("/rest")
 16  public class JaxRsActivator extends Application {
 17     /* class body intentionally left blank */
 18  }

```
### #16 - springboot-actuator-to-quarkus-0100
* Category: mandatory
* Effort: 5
* Description: Replace the Spring Boot Actuator dependency with Quarkus Smallrye Health extension
Replace the Spring Boot Actuator dependency with Quarkus Smallrye Health extension.. It has to be replaced by `io.quarkus:quarkus-smallrye-health` artifact.
* Labels: konveyor.io/source=springboot, konveyor.io/target=quarkus
* Links
  * Quarkus - Smallrye Health: https://quarkus.io/guides/smallrye-health
* Incidents
  * file:///tmp/source-code/pom.xml
      * Replace the Spring Boot Actuator dependency with Quarkus Smallrye Health extension.. It has to be replaced by `io.quarkus:quarkus-smallrye-health` artifact.
### #17 - springboot-annotations-to-quarkus-00000
* Category: mandatory
* Effort: 1
* Description: Remove the SpringBoot @SpringBootApplication annotation
Remove the SpringBoot @SpringBootApplication annotation.. A Spring Boot application contains a "main" class with the @SpringBootApplication annotation. A Quarkus application does not have such a class. Two different alternatives can be followed - either. to remove the "main" class associated with the annotation, or add the `org.springframework.boot:spring-boot-autoconfigure` dependency as an `optional` Maven dependency. An optional dependency. is available when an application compiles but is not packaged with the application at runtime. Doing this would allow the application to compile without modification, but you. would also need to maintain a Spring version along with the Quarkus application.
* Labels: konveyor.io/source=springboot, konveyor.io/target=quarkus
* Incidents
  * file:///tmp/source-code/orders-service/src/main/java/org/ticketmonster/orders/Application.java
      * Remove the SpringBoot @SpringBootApplication annotation.. A Spring Boot application contains a "main" class with the @SpringBootApplication annotation. A Quarkus application does not have such a class. Two different alternatives can be followed - either. to remove the "main" class associated with the annotation, or add the `org.springframework.boot:spring-boot-autoconfigure` dependency as an `optional` Maven dependency. An optional dependency. is available when an application compiles but is not packaged with the application at runtime. Doing this would allow the application to compile without modification, but you. would also need to maintain a Spring version along with the Quarkus application.
      * Code Snippet:
```java
  1  /**
  2   * Licensed to the Apache Software Foundation (ASF) under one or more
  3   * contributor license agreements.  See the NOTICE file distributed with
  4   * this work for additional information regarding copyright ownership.
  5   * The ASF licenses this file to You under the Apache License, Version 2.0
  6   * (the "License"); you may not use this file except in compliance with
  7   * the License.  You may obtain a copy of the License at
  8   * <p>
  9   * http://www.apache.org/licenses/LICENSE-2.0
 10   * <p>
 11   * Unless required by applicable law or agreed to in writing, software
 12   * distributed under the License is distributed on an "AS IS" BASIS,
 13   * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 14   * See the License for the specific language governing permissions and
 15   * limitations under the License.
 16   */
 17  package org.ticketmonster.orders;
 18  
 19  import org.springframework.boot.SpringApplication;
 20  import org.springframework.boot.autoconfigure.SpringBootApplication;
 21  
 22  /**
 23   * Created by ceposta 
 24   * <a href="http://christianposta.com/blog>http://christianposta.com/blog</a>.
 25   */
 26  @SpringBootApplication
 27  public class Application {
 28  
 29      public static void main(String[] args) {
 30          SpringApplication.run(Application.class, args);
 31      }
 32  
 33      // enable h2 UI
 34  //    @Bean
 35  //    ServletRegistrationBean h2servletRegistration(){
 36  //        ServletRegistrationBean registrationBean = new ServletRegistrationBean( new WebServlet());
 37  //        registrationBean.addUrlMappings("/console/*");
 38  //        return registrationBean;
 39  //    }
 40  }

```
### #18 - springboot-di-to-quarkus-00000
* Category: potential
* Effort: 1
* Description: Replace the SpringBoot Dependency Injection artifact with Quarkus 'spring-di' extension
Replace the SpringBoot Dependency Injection artifact with Quarkus `spring-di` extension. Spring DI is in spring-beans artifact brought transitively by any `org.springframework.boot:spring-boot-*` dependency. Add Quarkus dependency `io.quarkus:quarkus-spring-di`
* Labels: konveyor.io/source=springboot, konveyor.io/target=quarkus
* Links
  * Quarkus DI Guide: https://quarkus.io/guides/spring-di
* Incidents
  * file:///tmp/source-code/pom.xml
      * Replace the SpringBoot Dependency Injection artifact with Quarkus `spring-di` extension. Spring DI is in spring-beans artifact brought transitively by any `org.springframework.boot:spring-boot-*` dependency. Add Quarkus dependency `io.quarkus:quarkus-spring-di`
### #19 - springboot-jpa-to-quarkus-00000
* Category: mandatory
* Effort: 1
* Description: Replace the SpringBoot Data JPA artifact with Quarkus 'spring-data-jpa' extension
Replace the SpringBoot JPA artifact with Quarkus `spring-data-jpa` extension. Spring Data JPA is in spring-data-jpa artifact brought transitively by any `org.springframework.data:spring-data-*` dependency. Add Quarkus dependency `io.quarkus:quarkus-spring-data-jpa`
* Labels: konveyor.io/source=springboot, konveyor.io/target=quarkus
* Links
  * Quarkus JPA Guide: https://quarkus.io/guides/spring-data-jpa
* Incidents
  * file:///tmp/source-code/pom.xml
      * Replace the SpringBoot JPA artifact with Quarkus `spring-data-jpa` extension. Spring Data JPA is in spring-data-jpa artifact brought transitively by any `org.springframework.data:spring-data-*` dependency. Add Quarkus dependency `io.quarkus:quarkus-spring-data-jpa`
### #20 - springboot-plugins-to-quarkus-0000
* Category: mandatory
* Effort: 2
* Description: Replace the spring-boot-maven-plugin dependency
Replace the `spring-boot-maven-plugin` dependency.. The `spring-boot-maven-plugin` dependency needs to be replaced with `quarkus-maven-plugin`, so that the application is built with Quarkus, both for running on the JVM and in native mode.
* Labels: konveyor.io/source=springboot, konveyor.io/target=quarkus
* Links
  * Building Quarkus with maven: https://quarkus.io/guides/maven-tooling#build-tool-maven
* Incidents
  * file:///tmp/source-code/orders-service/pom.xml
      * Replace the `spring-boot-maven-plugin` dependency.. The `spring-boot-maven-plugin` dependency needs to be replaced with `quarkus-maven-plugin`, so that the application is built with Quarkus, both for running on the JVM and in native mode.
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <project xmlns="http://maven.apache.org/POM/4.0.0"
  3           xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  4           xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  5    <artifactId>orders-service</artifactId>
  6    <groupId>org.ticketmonster.orders</groupId>
  7    <version>1.0.0-SNAPSHOT</version>
  8    <modelVersion>4.0.0</modelVersion>
  9  
 10    <properties>
 11      <spring-boot.version>1.5.6.RELEASE</spring-boot.version>
 12      <docker-maven-plugin.version>0.20.1</docker-maven-plugin.version>
 13      <mysql-server.version>5.7</mysql-server.version>
 14      <mysql.user>ticket</mysql.user>
 15      <mysql.password>monster</mysql.password>
 16      <mysql.port>3306</mysql.port>
 17      <mysql.init.timeout>60000</mysql.init.timeout>
 18      <skipITs>true</skipITs>
 19      <fabric8.maven.plugin.version>3.5.25</fabric8.maven.plugin.version>
 20      <docker.image.name>ceposta/%a:%l</docker.image.name>
 21    </properties>
 22  
 23    <dependencyManagement>
 24      <dependencies>
 25        <dependency>
 26          <!-- Import dependency management from Spring Boot -->
 27          <groupId>org.springframework.boot</groupId>
 28          <artifactId>spring-boot-dependencies</artifactId>
 29          <version>${spring-boot.version}</version>
 30          <type>pom</type>
 31          <scope>import</scope>
 32        </dependency>
 33      </dependencies>
 34    </dependencyManagement>
 35  
 36  
 37    <dependencies>
 38      <dependency>
 39        <groupId>org.springframework.boot</groupId>
 40        <artifactId>spring-boot-starter-web</artifactId>
 41      </dependency>
 42      <dependency>
 43        <groupId>org.springframework.boot</groupId>
 44        <artifactId>spring-boot-starter-actuator</artifactId>
 45      </dependency>
 46      <dependency>
 47        <groupId>org.springframework.boot</groupId>
 48        <artifactId>spring-boot-starter-data-jpa</artifactId>
 49      </dependency>
 50      <dependency>
 51        <groupId>org.teiid.spring</groupId>
 52        <artifactId>teiid-spring-boot-starter</artifactId>
 53        <version>1.0.0-SNAPSHOT</version>
 54      </dependency>
 55  
 56  
 57  
 58      <!-- Testing -->
 59      <dependency>
 60        <groupId>io.rest-assured</groupId>
 61        <artifactId>rest-assured</artifactId>
 62        <version>3.0.3</version>
 63        <scope>test</scope>
 64      </dependency>
 65      <dependency>
 66        <groupId>io.rest-assured</groupId>
 67        <artifactId>json-schema-validator</artifactId>
 68        <version>3.0.3</version>
 69        <scope>test</scope>
 70      </dependency>
 71      <dependency>
 72        <groupId>io.specto</groupId>
 73        <artifactId>hoverfly-java</artifactId>
 74        <version>0.8.0</version>
 75        <scope>test</scope>
 76      </dependency>
 77      <dependency>
 78        <groupId>org.springframework.boot</groupId>
 79        <artifactId>spring-boot-starter-test</artifactId>
 80        <scope>test</scope>
 81      </dependency>
 82      <dependency>
 83        <groupId>com.h2database</groupId>
 84        <artifactId>h2</artifactId>
 85        <scope>test</scope>
 86      </dependency>
 87  
 88      <dependency>
 89        <groupId>au.com.dius</groupId>
 90        <artifactId>pact-jvm-provider-junit_2.11</artifactId>
 91        <version>3.5.0</version>
 92      </dependency>
 93    </dependencies>
 94  
 95    <build>
 96      <plugins>
 97        <plugin>
 98          <groupId>org.springframework.boot</groupId>
 99          <artifactId>spring-boot-maven-plugin</artifactId>
100          <version>${spring-boot.version}</version>
101          <executions>
102            <execution>
103              <goals>
104                <goal>repackage</goal>
105              </goals>
106            </execution>
107          </executions>
108          <configuration>
109            <classifier>exec</classifier>
110          </configuration>
111        </plugin>
112        <plugin>
113          <artifactId>maven-compiler-plugin</artifactId>
114          <version>2.3.1</version>
115          <configuration>
116            <source>1.8</source>
117            <target>1.8</target>
118          </configuration>
119        </plugin>
120      </plugins>
121    </build>
122  
123    <profiles>
124      <profile>
125        <id>default</id>
126        <activation>
127          <activeByDefault>true</activeByDefault>
128        </activation>
129        <dependencies>
130          <dependency>
131            <groupId>com.h2database</groupId>
132            <artifactId>h2</artifactId>
133          </dependency>
134        </dependencies>
135      </profile>
136      <profile>
137        <id>mysql</id>
138        <properties>
139          <spring.profiles.active>mysql</spring.profiles.active>
140          <skipITs>false</skipITs>
141        </properties>
142        <dependencies>
143          <dependency>
144            <groupId>mysql</groupId>
145            <artifactId>mysql-connector-java</artifactId>
146            <version>5.1.44</version>
147          </dependency>
148        </dependencies>
149        <build>
150          <plugins>
151            <plugin>
152              <groupId>org.springframework.boot</groupId>
153              <artifactId>spring-boot-maven-plugin</artifactId>
154              <executions>
155                <execution>
156                  <goals>
157                    <goal>repackage</goal>
158                  </goals>
159                </execution>
160              </executions>
161              <configuration>
162                <profiles>
163                  <profile>mysql</profile>
164                </profiles>
165              </configuration>
166            </plugin>
167            <plugin>
168              <groupId>io.fabric8</groupId>
169              <artifactId>docker-maven-plugin</artifactId>
170              <version>${docker-maven-plugin.version}</version>
171              <configuration>
172                <images>
173                  <image>
174                    <name>tm-orders/mysql-test-database</name>
175                    <run>
176                      <env>
177                        <MYSQL_ROOT_PASSWORD>admin</MYSQL_ROOT_PASSWORD>
178                        <MYSQL_DATABASE>ticketmonster</MYSQL_DATABASE>
179                        <MYSQL_USER>${mysql.user}</MYSQL_USER>
180                        <MYSQL_PASSWORD>${mysql.password}</MYSQL_PASSWORD>
181                      </env>
182                      <ports>
183                        <port>${mysql.port}:3306</port>
184                      </ports>
185                      <log>
186                        <prefix>mysql</prefix>
187                        <enabled>true</enabled>
188                        <color>yellow</color>
189                      </log>
190                      <wait>
191                        <log>MySQL init process done. Ready for start up.</log>
192                        <time>${mysql.init.timeout}</time>
193                      </wait>
194                    </run>
195                    <build>
196                      <from>mysql/mysql-server:${mysql-server.version}</from>
197                      <assembly>
198                        <inline>
199                          <fileSets>
```
### #21 - springboot-properties-to-quarkus-00000
* Category: mandatory
* Effort: 1
* Description: Replace the SpringBoot artifact with Quarkus 'spring-boot-properties' extension
Replace the SpringBoot artifact with Quarkus `spring-boot-properties` extension. Spring Configuration Properties is in spring-boot artifact brought transitively by any `org.springframework.boot:spring-boot-*` dependency. Add Quarkus dependency `io.quarkus:quarkus-spring-boot-properties`
* Labels: konveyor.io/source=springboot, konveyor.io/target=quarkus
* Links
  * Quarkus Spring Configuration Properties Guide: https://quarkus.io/guides/spring-boot-properties
* Incidents
  * file:///tmp/source-code/pom.xml
      * Replace the SpringBoot artifact with Quarkus `spring-boot-properties` extension. Spring Configuration Properties is in spring-boot artifact brought transitively by any `org.springframework.boot:spring-boot-*` dependency. Add Quarkus dependency `io.quarkus:quarkus-spring-boot-properties`
### #22 - springboot-properties-to-quarkus-00002
* Category: mandatory
* Effort: 1
* Description: Replace Spring datasource property key/value pairs with Quarkus properties
Spring datasource property key/value pairs have been detected in the application property file.. View advice in the Quarkus datasource guide to convert these to Quarkus datasource properties.
* Labels: konveyor.io/source=springboot, konveyor.io/target=quarkus
* Links
  * Quarkus Datasources Guide: https://quarkus.io/guides/datasource
* Incidents
  * file:///tmp/source-code/orders-service/src/main/resources/application-kube.properties
      * Spring datasource property key/value pairs have been detected in the application property file.. View advice in the Quarkus datasource guide to convert these to Quarkus datasource properties.
      * Code Snippet:
```java
  1  spring.datasource.legacyDS.url=jdbc:mysql://mysql-backend:3306/ticketmonster?useSSL=false
  2  spring.datasource.legacyDS.username=ticket
  3  spring.datasource.legacyDS.password=monster
  4  spring.datasource.legacyDS.driverClassName=com.mysql.jdbc.Driver
  5  
  6  spring.datasource.ordersDS.url=jdbc:mysql://mysql-orders:3306/orders?useSSL=false
  7  spring.datasource.ordersDS.username=ticket
  8  spring.datasource.ordersDS.password=monster
  9  spring.datasource.ordersDS.driverClassName=com.mysql.jdbc.Driver
 10  
 11  spring.jpa.hibernate.ddl-auto=none
 12  spring.jpa.properties.hibernate.dialect=org.teiid.dialect.TeiidDialect
 13  #spring.jpa.database-platform=org.teiid.dialect.TeiidDialect
 14  
 15  
 16  spring.teiid.model.package=org.ticketmonster.orders.domain

```
  * file:///tmp/source-code/orders-service/src/main/resources/application-kube.properties
      * Spring datasource property key/value pairs have been detected in the application property file.. View advice in the Quarkus datasource guide to convert these to Quarkus datasource properties.
      * Code Snippet:
```java
  1  spring.datasource.legacyDS.url=jdbc:mysql://mysql-backend:3306/ticketmonster?useSSL=false
  2  spring.datasource.legacyDS.username=ticket
  3  spring.datasource.legacyDS.password=monster
  4  spring.datasource.legacyDS.driverClassName=com.mysql.jdbc.Driver
  5  
  6  spring.datasource.ordersDS.url=jdbc:mysql://mysql-orders:3306/orders?useSSL=false
  7  spring.datasource.ordersDS.username=ticket
  8  spring.datasource.ordersDS.password=monster
  9  spring.datasource.ordersDS.driverClassName=com.mysql.jdbc.Driver
 10  
 11  spring.jpa.hibernate.ddl-auto=none
 12  spring.jpa.properties.hibernate.dialect=org.teiid.dialect.TeiidDialect
 13  #spring.jpa.database-platform=org.teiid.dialect.TeiidDialect
 14  
 15  
 16  spring.teiid.model.package=org.ticketmonster.orders.domain

```
  * file:///tmp/source-code/orders-service/src/main/resources/application-kube.properties
      * Spring datasource property key/value pairs have been detected in the application property file.. View advice in the Quarkus datasource guide to convert these to Quarkus datasource properties.
      * Code Snippet:
```java
  1  spring.datasource.legacyDS.url=jdbc:mysql://mysql-backend:3306/ticketmonster?useSSL=false
  2  spring.datasource.legacyDS.username=ticket
  3  spring.datasource.legacyDS.password=monster
  4  spring.datasource.legacyDS.driverClassName=com.mysql.jdbc.Driver
  5  
  6  spring.datasource.ordersDS.url=jdbc:mysql://mysql-orders:3306/orders?useSSL=false
  7  spring.datasource.ordersDS.username=ticket
  8  spring.datasource.ordersDS.password=monster
  9  spring.datasource.ordersDS.driverClassName=com.mysql.jdbc.Driver
 10  
 11  spring.jpa.hibernate.ddl-auto=none
 12  spring.jpa.properties.hibernate.dialect=org.teiid.dialect.TeiidDialect
 13  #spring.jpa.database-platform=org.teiid.dialect.TeiidDialect
 14  
 15  
 16  spring.teiid.model.package=org.ticketmonster.orders.domain

```
  * file:///tmp/source-code/orders-service/src/main/resources/application-kube.properties
      * Spring datasource property key/value pairs have been detected in the application property file.. View advice in the Quarkus datasource guide to convert these to Quarkus datasource properties.
      * Code Snippet:
```java
  1  spring.datasource.legacyDS.url=jdbc:mysql://mysql-backend:3306/ticketmonster?useSSL=false
  2  spring.datasource.legacyDS.username=ticket
  3  spring.datasource.legacyDS.password=monster
  4  spring.datasource.legacyDS.driverClassName=com.mysql.jdbc.Driver
  5  
  6  spring.datasource.ordersDS.url=jdbc:mysql://mysql-orders:3306/orders?useSSL=false
  7  spring.datasource.ordersDS.username=ticket
  8  spring.datasource.ordersDS.password=monster
  9  spring.datasource.ordersDS.driverClassName=com.mysql.jdbc.Driver
 10  
 11  spring.jpa.hibernate.ddl-auto=none
 12  spring.jpa.properties.hibernate.dialect=org.teiid.dialect.TeiidDialect
 13  #spring.jpa.database-platform=org.teiid.dialect.TeiidDialect
 14  
 15  
 16  spring.teiid.model.package=org.ticketmonster.orders.domain

```
  * file:///tmp/source-code/orders-service/src/main/resources/application-kube.properties
      * Spring datasource property key/value pairs have been detected in the application property file.. View advice in the Quarkus datasource guide to convert these to Quarkus datasource properties.
      * Code Snippet:
```java
  1  spring.datasource.legacyDS.url=jdbc:mysql://mysql-backend:3306/ticketmonster?useSSL=false
  2  spring.datasource.legacyDS.username=ticket
  3  spring.datasource.legacyDS.password=monster
  4  spring.datasource.legacyDS.driverClassName=com.mysql.jdbc.Driver
  5  
  6  spring.datasource.ordersDS.url=jdbc:mysql://mysql-orders:3306/orders?useSSL=false
  7  spring.datasource.ordersDS.username=ticket
  8  spring.datasource.ordersDS.password=monster
  9  spring.datasource.ordersDS.driverClassName=com.mysql.jdbc.Driver
 10  
 11  spring.jpa.hibernate.ddl-auto=none
 12  spring.jpa.properties.hibernate.dialect=org.teiid.dialect.TeiidDialect
 13  #spring.jpa.database-platform=org.teiid.dialect.TeiidDialect
 14  
 15  
 16  spring.teiid.model.package=org.ticketmonster.orders.domain

```
  * file:///tmp/source-code/orders-service/src/main/resources/application-kube.properties
      * Spring datasource property key/value pairs have been detected in the application property file.. View advice in the Quarkus datasource guide to convert these to Quarkus datasource properties.
      * Code Snippet:
```java
  1  spring.datasource.legacyDS.url=jdbc:mysql://mysql-backend:3306/ticketmonster?useSSL=false
  2  spring.datasource.legacyDS.username=ticket
  3  spring.datasource.legacyDS.password=monster
  4  spring.datasource.legacyDS.driverClassName=com.mysql.jdbc.Driver
  5  
  6  spring.datasource.ordersDS.url=jdbc:mysql://mysql-orders:3306/orders?useSSL=false
  7  spring.datasource.ordersDS.username=ticket
  8  spring.datasource.ordersDS.password=monster
  9  spring.datasource.ordersDS.driverClassName=com.mysql.jdbc.Driver
 10  
 11  spring.jpa.hibernate.ddl-auto=none
 12  spring.jpa.properties.hibernate.dialect=org.teiid.dialect.TeiidDialect
 13  #spring.jpa.database-platform=org.teiid.dialect.TeiidDialect
 14  
 15  
 16  spring.teiid.model.package=org.ticketmonster.orders.domain

```
  * file:///tmp/source-code/orders-service/src/main/resources/application-kube.properties
      * Spring datasource property key/value pairs have been detected in the application property file.. View advice in the Quarkus datasource guide to convert these to Quarkus datasource properties.
      * Code Snippet:
```java
  1  spring.datasource.legacyDS.url=jdbc:mysql://mysql-backend:3306/ticketmonster?useSSL=false
  2  spring.datasource.legacyDS.username=ticket
  3  spring.datasource.legacyDS.password=monster
  4  spring.datasource.legacyDS.driverClassName=com.mysql.jdbc.Driver
  5  
  6  spring.datasource.ordersDS.url=jdbc:mysql://mysql-orders:3306/orders?useSSL=false
  7  spring.datasource.ordersDS.username=ticket
  8  spring.datasource.ordersDS.password=monster
  9  spring.datasource.ordersDS.driverClassName=com.mysql.jdbc.Driver
 10  
 11  spring.jpa.hibernate.ddl-auto=none
 12  spring.jpa.properties.hibernate.dialect=org.teiid.dialect.TeiidDialect
 13  #spring.jpa.database-platform=org.teiid.dialect.TeiidDialect
 14  
 15  
 16  spring.teiid.model.package=org.ticketmonster.orders.domain

```
  * file:///tmp/source-code/orders-service/src/main/resources/application-kube.properties
      * Spring datasource property key/value pairs have been detected in the application property file.. View advice in the Quarkus datasource guide to convert these to Quarkus datasource properties.
      * Code Snippet:
```java
  1  spring.datasource.legacyDS.url=jdbc:mysql://mysql-backend:3306/ticketmonster?useSSL=false
  2  spring.datasource.legacyDS.username=ticket
  3  spring.datasource.legacyDS.password=monster
  4  spring.datasource.legacyDS.driverClassName=com.mysql.jdbc.Driver
  5  
  6  spring.datasource.ordersDS.url=jdbc:mysql://mysql-orders:3306/orders?useSSL=false
  7  spring.datasource.ordersDS.username=ticket
  8  spring.datasource.ordersDS.password=monster
  9  spring.datasource.ordersDS.driverClassName=com.mysql.jdbc.Driver
 10  
 11  spring.jpa.hibernate.ddl-auto=none
 12  spring.jpa.properties.hibernate.dialect=org.teiid.dialect.TeiidDialect
 13  #spring.jpa.database-platform=org.teiid.dialect.TeiidDialect
 14  
 15  
 16  spring.teiid.model.package=org.ticketmonster.orders.domain

```
  * file:///tmp/source-code/orders-service/src/main/resources/application-mysql.properties
      * Spring datasource property key/value pairs have been detected in the application property file.. View advice in the Quarkus datasource guide to convert these to Quarkus datasource properties.
      * Code Snippet:
```java
  1  spring.datasource.legacyDS.url=jdbc:mysql://localhost:3306/ticketmonster?useSSL=false
  2  spring.datasource.legacyDS.username=ticket
  3  spring.datasource.legacyDS.password=monster
  4  spring.datasource.legacyDS.driverClassName=com.mysql.jdbc.Driver
  5  
  6  spring.datasource.ordersDS.url=jdbc:mysql://localhost:3306/orders?useSSL=false
  7  spring.datasource.ordersDS.username=ticket
  8  spring.datasource.ordersDS.password=monster
  9  spring.datasource.ordersDS.driverClassName=com.mysql.jdbc.Driver
 10  
 11  spring.jpa.hibernate.ddl-auto=none
 12  spring.jpa.properties.hibernate.dialect=org.teiid.dialect.TeiidDialect
 13  #spring.jpa.database-platform=org.teiid.dialect.TeiidDialect
 14  
 15  
 16  spring.teiid.model.package=org.ticketmonster.orders.domain

```
  * file:///tmp/source-code/orders-service/src/main/resources/application-mysql.properties
      * Spring datasource property key/value pairs have been detected in the application property file.. View advice in the Quarkus datasource guide to convert these to Quarkus datasource properties.
      * Code Snippet:
```java
  1  spring.datasource.legacyDS.url=jdbc:mysql://localhost:3306/ticketmonster?useSSL=false
  2  spring.datasource.legacyDS.username=ticket
  3  spring.datasource.legacyDS.password=monster
  4  spring.datasource.legacyDS.driverClassName=com.mysql.jdbc.Driver
  5  
  6  spring.datasource.ordersDS.url=jdbc:mysql://localhost:3306/orders?useSSL=false
  7  spring.datasource.ordersDS.username=ticket
  8  spring.datasource.ordersDS.password=monster
  9  spring.datasource.ordersDS.driverClassName=com.mysql.jdbc.Driver
 10  
 11  spring.jpa.hibernate.ddl-auto=none
 12  spring.jpa.properties.hibernate.dialect=org.teiid.dialect.TeiidDialect
 13  #spring.jpa.database-platform=org.teiid.dialect.TeiidDialect
 14  
 15  
 16  spring.teiid.model.package=org.ticketmonster.orders.domain

```
  * file:///tmp/source-code/orders-service/src/main/resources/application-mysql.properties
      * Spring datasource property key/value pairs have been detected in the application property file.. View advice in the Quarkus datasource guide to convert these to Quarkus datasource properties.
      * Code Snippet:
```java
  1  spring.datasource.legacyDS.url=jdbc:mysql://localhost:3306/ticketmonster?useSSL=false
  2  spring.datasource.legacyDS.username=ticket
  3  spring.datasource.legacyDS.password=monster
  4  spring.datasource.legacyDS.driverClassName=com.mysql.jdbc.Driver
  5  
  6  spring.datasource.ordersDS.url=jdbc:mysql://localhost:3306/orders?useSSL=false
  7  spring.datasource.ordersDS.username=ticket
  8  spring.datasource.ordersDS.password=monster
  9  spring.datasource.ordersDS.driverClassName=com.mysql.jdbc.Driver
 10  
 11  spring.jpa.hibernate.ddl-auto=none
 12  spring.jpa.properties.hibernate.dialect=org.teiid.dialect.TeiidDialect
 13  #spring.jpa.database-platform=org.teiid.dialect.TeiidDialect
 14  
 15  
 16  spring.teiid.model.package=org.ticketmonster.orders.domain

```
  * file:///tmp/source-code/orders-service/src/main/resources/application-mysql.properties
      * Spring datasource property key/value pairs have been detected in the application property file.. View advice in the Quarkus datasource guide to convert these to Quarkus datasource properties.
      * Code Snippet:
```java
  1  spring.datasource.legacyDS.url=jdbc:mysql://localhost:3306/ticketmonster?useSSL=false
  2  spring.datasource.legacyDS.username=ticket
  3  spring.datasource.legacyDS.password=monster
  4  spring.datasource.legacyDS.driverClassName=com.mysql.jdbc.Driver
  5  
  6  spring.datasource.ordersDS.url=jdbc:mysql://localhost:3306/orders?useSSL=false
  7  spring.datasource.ordersDS.username=ticket
  8  spring.datasource.ordersDS.password=monster
  9  spring.datasource.ordersDS.driverClassName=com.mysql.jdbc.Driver
 10  
 11  spring.jpa.hibernate.ddl-auto=none
 12  spring.jpa.properties.hibernate.dialect=org.teiid.dialect.TeiidDialect
 13  #spring.jpa.database-platform=org.teiid.dialect.TeiidDialect
 14  
 15  
 16  spring.teiid.model.package=org.ticketmonster.orders.domain

```
  * file:///tmp/source-code/orders-service/src/main/resources/application-mysql.properties
      * Spring datasource property key/value pairs have been detected in the application property file.. View advice in the Quarkus datasource guide to convert these to Quarkus datasource properties.
      * Code Snippet:
```java
  1  spring.datasource.legacyDS.url=jdbc:mysql://localhost:3306/ticketmonster?useSSL=false
  2  spring.datasource.legacyDS.username=ticket
  3  spring.datasource.legacyDS.password=monster
  4  spring.datasource.legacyDS.driverClassName=com.mysql.jdbc.Driver
  5  
  6  spring.datasource.ordersDS.url=jdbc:mysql://localhost:3306/orders?useSSL=false
  7  spring.datasource.ordersDS.username=ticket
  8  spring.datasource.ordersDS.password=monster
  9  spring.datasource.ordersDS.driverClassName=com.mysql.jdbc.Driver
 10  
 11  spring.jpa.hibernate.ddl-auto=none
 12  spring.jpa.properties.hibernate.dialect=org.teiid.dialect.TeiidDialect
 13  #spring.jpa.database-platform=org.teiid.dialect.TeiidDialect
 14  
 15  
 16  spring.teiid.model.package=org.ticketmonster.orders.domain

```
  * file:///tmp/source-code/orders-service/src/main/resources/application-mysql.properties
      * Spring datasource property key/value pairs have been detected in the application property file.. View advice in the Quarkus datasource guide to convert these to Quarkus datasource properties.
      * Code Snippet:
```java
  1  spring.datasource.legacyDS.url=jdbc:mysql://localhost:3306/ticketmonster?useSSL=false
  2  spring.datasource.legacyDS.username=ticket
  3  spring.datasource.legacyDS.password=monster
  4  spring.datasource.legacyDS.driverClassName=com.mysql.jdbc.Driver
  5  
  6  spring.datasource.ordersDS.url=jdbc:mysql://localhost:3306/orders?useSSL=false
  7  spring.datasource.ordersDS.username=ticket
  8  spring.datasource.ordersDS.password=monster
  9  spring.datasource.ordersDS.driverClassName=com.mysql.jdbc.Driver
 10  
 11  spring.jpa.hibernate.ddl-auto=none
 12  spring.jpa.properties.hibernate.dialect=org.teiid.dialect.TeiidDialect
 13  #spring.jpa.database-platform=org.teiid.dialect.TeiidDialect
 14  
 15  
 16  spring.teiid.model.package=org.ticketmonster.orders.domain

```
  * file:///tmp/source-code/orders-service/src/main/resources/application-mysql.properties
      * Spring datasource property key/value pairs have been detected in the application property file.. View advice in the Quarkus datasource guide to convert these to Quarkus datasource properties.
      * Code Snippet:
```java
  1  spring.datasource.legacyDS.url=jdbc:mysql://localhost:3306/ticketmonster?useSSL=false
  2  spring.datasource.legacyDS.username=ticket
  3  spring.datasource.legacyDS.password=monster
  4  spring.datasource.legacyDS.driverClassName=com.mysql.jdbc.Driver
  5  
  6  spring.datasource.ordersDS.url=jdbc:mysql://localhost:3306/orders?useSSL=false
  7  spring.datasource.ordersDS.username=ticket
  8  spring.datasource.ordersDS.password=monster
  9  spring.datasource.ordersDS.driverClassName=com.mysql.jdbc.Driver
 10  
 11  spring.jpa.hibernate.ddl-auto=none
 12  spring.jpa.properties.hibernate.dialect=org.teiid.dialect.TeiidDialect
 13  #spring.jpa.database-platform=org.teiid.dialect.TeiidDialect
 14  
 15  
 16  spring.teiid.model.package=org.ticketmonster.orders.domain

```
  * file:///tmp/source-code/orders-service/src/main/resources/application-mysql.properties
      * Spring datasource property key/value pairs have been detected in the application property file.. View advice in the Quarkus datasource guide to convert these to Quarkus datasource properties.
      * Code Snippet:
```java
  1  spring.datasource.legacyDS.url=jdbc:mysql://localhost:3306/ticketmonster?useSSL=false
  2  spring.datasource.legacyDS.username=ticket
  3  spring.datasource.legacyDS.password=monster
  4  spring.datasource.legacyDS.driverClassName=com.mysql.jdbc.Driver
  5  
  6  spring.datasource.ordersDS.url=jdbc:mysql://localhost:3306/orders?useSSL=false
  7  spring.datasource.ordersDS.username=ticket
  8  spring.datasource.ordersDS.password=monster
  9  spring.datasource.ordersDS.driverClassName=com.mysql.jdbc.Driver
 10  
 11  spring.jpa.hibernate.ddl-auto=none
 12  spring.jpa.properties.hibernate.dialect=org.teiid.dialect.TeiidDialect
 13  #spring.jpa.database-platform=org.teiid.dialect.TeiidDialect
 14  
 15  
 16  spring.teiid.model.package=org.ticketmonster.orders.domain

```
  * file:///tmp/source-code/orders-service/target/classes/application-kube.properties
      * Spring datasource property key/value pairs have been detected in the application property file.. View advice in the Quarkus datasource guide to convert these to Quarkus datasource properties.
      * Code Snippet:
```java
  1  spring.datasource.legacyDS.url=jdbc:mysql://mysql-backend:3306/ticketmonster?useSSL=false
  2  spring.datasource.legacyDS.username=ticket
  3  spring.datasource.legacyDS.password=monster
  4  spring.datasource.legacyDS.driverClassName=com.mysql.jdbc.Driver
  5  
  6  spring.datasource.ordersDS.url=jdbc:mysql://mysql-orders:3306/orders?useSSL=false
  7  spring.datasource.ordersDS.username=ticket
  8  spring.datasource.ordersDS.password=monster
  9  spring.datasource.ordersDS.driverClassName=com.mysql.jdbc.Driver
 10  
 11  spring.jpa.hibernate.ddl-auto=none
 12  spring.jpa.properties.hibernate.dialect=org.teiid.dialect.TeiidDialect
 13  #spring.jpa.database-platform=org.teiid.dialect.TeiidDialect
 14  
 15  
 16  spring.teiid.model.package=org.ticketmonster.orders.domain

```
  * file:///tmp/source-code/orders-service/target/classes/application-kube.properties
      * Spring datasource property key/value pairs have been detected in the application property file.. View advice in the Quarkus datasource guide to convert these to Quarkus datasource properties.
      * Code Snippet:
```java
  1  spring.datasource.legacyDS.url=jdbc:mysql://mysql-backend:3306/ticketmonster?useSSL=false
  2  spring.datasource.legacyDS.username=ticket
  3  spring.datasource.legacyDS.password=monster
  4  spring.datasource.legacyDS.driverClassName=com.mysql.jdbc.Driver
  5  
  6  spring.datasource.ordersDS.url=jdbc:mysql://mysql-orders:3306/orders?useSSL=false
  7  spring.datasource.ordersDS.username=ticket
  8  spring.datasource.ordersDS.password=monster
  9  spring.datasource.ordersDS.driverClassName=com.mysql.jdbc.Driver
 10  
 11  spring.jpa.hibernate.ddl-auto=none
 12  spring.jpa.properties.hibernate.dialect=org.teiid.dialect.TeiidDialect
 13  #spring.jpa.database-platform=org.teiid.dialect.TeiidDialect
 14  
 15  
 16  spring.teiid.model.package=org.ticketmonster.orders.domain

```
  * file:///tmp/source-code/orders-service/target/classes/application-kube.properties
      * Spring datasource property key/value pairs have been detected in the application property file.. View advice in the Quarkus datasource guide to convert these to Quarkus datasource properties.
      * Code Snippet:
```java
  1  spring.datasource.legacyDS.url=jdbc:mysql://mysql-backend:3306/ticketmonster?useSSL=false
  2  spring.datasource.legacyDS.username=ticket
  3  spring.datasource.legacyDS.password=monster
  4  spring.datasource.legacyDS.driverClassName=com.mysql.jdbc.Driver
  5  
  6  spring.datasource.ordersDS.url=jdbc:mysql://mysql-orders:3306/orders?useSSL=false
  7  spring.datasource.ordersDS.username=ticket
  8  spring.datasource.ordersDS.password=monster
  9  spring.datasource.ordersDS.driverClassName=com.mysql.jdbc.Driver
 10  
 11  spring.jpa.hibernate.ddl-auto=none
 12  spring.jpa.properties.hibernate.dialect=org.teiid.dialect.TeiidDialect
 13  #spring.jpa.database-platform=org.teiid.dialect.TeiidDialect
 14  
 15  
 16  spring.teiid.model.package=org.ticketmonster.orders.domain

```
  * file:///tmp/source-code/orders-service/target/classes/application-kube.properties
      * Spring datasource property key/value pairs have been detected in the application property file.. View advice in the Quarkus datasource guide to convert these to Quarkus datasource properties.
      * Code Snippet:
```java
  1  spring.datasource.legacyDS.url=jdbc:mysql://mysql-backend:3306/ticketmonster?useSSL=false
  2  spring.datasource.legacyDS.username=ticket
  3  spring.datasource.legacyDS.password=monster
  4  spring.datasource.legacyDS.driverClassName=com.mysql.jdbc.Driver
  5  
  6  spring.datasource.ordersDS.url=jdbc:mysql://mysql-orders:3306/orders?useSSL=false
  7  spring.datasource.ordersDS.username=ticket
  8  spring.datasource.ordersDS.password=monster
  9  spring.datasource.ordersDS.driverClassName=com.mysql.jdbc.Driver
 10  
 11  spring.jpa.hibernate.ddl-auto=none
 12  spring.jpa.properties.hibernate.dialect=org.teiid.dialect.TeiidDialect
 13  #spring.jpa.database-platform=org.teiid.dialect.TeiidDialect
 14  
 15  
 16  spring.teiid.model.package=org.ticketmonster.orders.domain

```
  * file:///tmp/source-code/orders-service/target/classes/application-kube.properties
      * Spring datasource property key/value pairs have been detected in the application property file.. View advice in the Quarkus datasource guide to convert these to Quarkus datasource properties.
      * Code Snippet:
```java
  1  spring.datasource.legacyDS.url=jdbc:mysql://mysql-backend:3306/ticketmonster?useSSL=false
  2  spring.datasource.legacyDS.username=ticket
  3  spring.datasource.legacyDS.password=monster
  4  spring.datasource.legacyDS.driverClassName=com.mysql.jdbc.Driver
  5  
  6  spring.datasource.ordersDS.url=jdbc:mysql://mysql-orders:3306/orders?useSSL=false
  7  spring.datasource.ordersDS.username=ticket
  8  spring.datasource.ordersDS.password=monster
  9  spring.datasource.ordersDS.driverClassName=com.mysql.jdbc.Driver
 10  
 11  spring.jpa.hibernate.ddl-auto=none
 12  spring.jpa.properties.hibernate.dialect=org.teiid.dialect.TeiidDialect
 13  #spring.jpa.database-platform=org.teiid.dialect.TeiidDialect
 14  
 15  
 16  spring.teiid.model.package=org.ticketmonster.orders.domain

```
  * file:///tmp/source-code/orders-service/target/classes/application-kube.properties
      * Spring datasource property key/value pairs have been detected in the application property file.. View advice in the Quarkus datasource guide to convert these to Quarkus datasource properties.
      * Code Snippet:
```java
  1  spring.datasource.legacyDS.url=jdbc:mysql://mysql-backend:3306/ticketmonster?useSSL=false
  2  spring.datasource.legacyDS.username=ticket
  3  spring.datasource.legacyDS.password=monster
  4  spring.datasource.legacyDS.driverClassName=com.mysql.jdbc.Driver
  5  
  6  spring.datasource.ordersDS.url=jdbc:mysql://mysql-orders:3306/orders?useSSL=false
  7  spring.datasource.ordersDS.username=ticket
  8  spring.datasource.ordersDS.password=monster
  9  spring.datasource.ordersDS.driverClassName=com.mysql.jdbc.Driver
 10  
 11  spring.jpa.hibernate.ddl-auto=none
 12  spring.jpa.properties.hibernate.dialect=org.teiid.dialect.TeiidDialect
 13  #spring.jpa.database-platform=org.teiid.dialect.TeiidDialect
 14  
 15  
 16  spring.teiid.model.package=org.ticketmonster.orders.domain

```
  * file:///tmp/source-code/orders-service/target/classes/application-kube.properties
      * Spring datasource property key/value pairs have been detected in the application property file.. View advice in the Quarkus datasource guide to convert these to Quarkus datasource properties.
      * Code Snippet:
```java
  1  spring.datasource.legacyDS.url=jdbc:mysql://mysql-backend:3306/ticketmonster?useSSL=false
  2  spring.datasource.legacyDS.username=ticket
  3  spring.datasource.legacyDS.password=monster
  4  spring.datasource.legacyDS.driverClassName=com.mysql.jdbc.Driver
  5  
  6  spring.datasource.ordersDS.url=jdbc:mysql://mysql-orders:3306/orders?useSSL=false
  7  spring.datasource.ordersDS.username=ticket
  8  spring.datasource.ordersDS.password=monster
  9  spring.datasource.ordersDS.driverClassName=com.mysql.jdbc.Driver
 10  
 11  spring.jpa.hibernate.ddl-auto=none
 12  spring.jpa.properties.hibernate.dialect=org.teiid.dialect.TeiidDialect
 13  #spring.jpa.database-platform=org.teiid.dialect.TeiidDialect
 14  
 15  
 16  spring.teiid.model.package=org.ticketmonster.orders.domain

```
  * file:///tmp/source-code/orders-service/target/classes/application-kube.properties
      * Spring datasource property key/value pairs have been detected in the application property file.. View advice in the Quarkus datasource guide to convert these to Quarkus datasource properties.
      * Code Snippet:
```java
  1  spring.datasource.legacyDS.url=jdbc:mysql://mysql-backend:3306/ticketmonster?useSSL=false
  2  spring.datasource.legacyDS.username=ticket
  3  spring.datasource.legacyDS.password=monster
  4  spring.datasource.legacyDS.driverClassName=com.mysql.jdbc.Driver
  5  
  6  spring.datasource.ordersDS.url=jdbc:mysql://mysql-orders:3306/orders?useSSL=false
  7  spring.datasource.ordersDS.username=ticket
  8  spring.datasource.ordersDS.password=monster
  9  spring.datasource.ordersDS.driverClassName=com.mysql.jdbc.Driver
 10  
 11  spring.jpa.hibernate.ddl-auto=none
 12  spring.jpa.properties.hibernate.dialect=org.teiid.dialect.TeiidDialect
 13  #spring.jpa.database-platform=org.teiid.dialect.TeiidDialect
 14  
 15  
 16  spring.teiid.model.package=org.ticketmonster.orders.domain

```
  * file:///tmp/source-code/orders-service/target/classes/application-mysql.properties
      * Spring datasource property key/value pairs have been detected in the application property file.. View advice in the Quarkus datasource guide to convert these to Quarkus datasource properties.
      * Code Snippet:
```java
  1  spring.datasource.legacyDS.url=jdbc:mysql://localhost:3306/ticketmonster?useSSL=false
  2  spring.datasource.legacyDS.username=ticket
  3  spring.datasource.legacyDS.password=monster
  4  spring.datasource.legacyDS.driverClassName=com.mysql.jdbc.Driver
  5  
  6  spring.datasource.ordersDS.url=jdbc:mysql://localhost:3306/orders?useSSL=false
  7  spring.datasource.ordersDS.username=ticket
  8  spring.datasource.ordersDS.password=monster
  9  spring.datasource.ordersDS.driverClassName=com.mysql.jdbc.Driver
 10  
 11  spring.jpa.hibernate.ddl-auto=none
 12  spring.jpa.properties.hibernate.dialect=org.teiid.dialect.TeiidDialect
 13  #spring.jpa.database-platform=org.teiid.dialect.TeiidDialect
 14  
 15  
 16  spring.teiid.model.package=org.ticketmonster.orders.domain

```
  * file:///tmp/source-code/orders-service/target/classes/application-mysql.properties
      * Spring datasource property key/value pairs have been detected in the application property file.. View advice in the Quarkus datasource guide to convert these to Quarkus datasource properties.
      * Code Snippet:
```java
  1  spring.datasource.legacyDS.url=jdbc:mysql://localhost:3306/ticketmonster?useSSL=false
  2  spring.datasource.legacyDS.username=ticket
  3  spring.datasource.legacyDS.password=monster
  4  spring.datasource.legacyDS.driverClassName=com.mysql.jdbc.Driver
  5  
  6  spring.datasource.ordersDS.url=jdbc:mysql://localhost:3306/orders?useSSL=false
  7  spring.datasource.ordersDS.username=ticket
  8  spring.datasource.ordersDS.password=monster
  9  spring.datasource.ordersDS.driverClassName=com.mysql.jdbc.Driver
 10  
 11  spring.jpa.hibernate.ddl-auto=none
 12  spring.jpa.properties.hibernate.dialect=org.teiid.dialect.TeiidDialect
 13  #spring.jpa.database-platform=org.teiid.dialect.TeiidDialect
 14  
 15  
 16  spring.teiid.model.package=org.ticketmonster.orders.domain

```
  * file:///tmp/source-code/orders-service/target/classes/application-mysql.properties
      * Spring datasource property key/value pairs have been detected in the application property file.. View advice in the Quarkus datasource guide to convert these to Quarkus datasource properties.
      * Code Snippet:
```java
  1  spring.datasource.legacyDS.url=jdbc:mysql://localhost:3306/ticketmonster?useSSL=false
  2  spring.datasource.legacyDS.username=ticket
  3  spring.datasource.legacyDS.password=monster
  4  spring.datasource.legacyDS.driverClassName=com.mysql.jdbc.Driver
  5  
  6  spring.datasource.ordersDS.url=jdbc:mysql://localhost:3306/orders?useSSL=false
  7  spring.datasource.ordersDS.username=ticket
  8  spring.datasource.ordersDS.password=monster
  9  spring.datasource.ordersDS.driverClassName=com.mysql.jdbc.Driver
 10  
 11  spring.jpa.hibernate.ddl-auto=none
 12  spring.jpa.properties.hibernate.dialect=org.teiid.dialect.TeiidDialect
 13  #spring.jpa.database-platform=org.teiid.dialect.TeiidDialect
 14  
 15  
 16  spring.teiid.model.package=org.ticketmonster.orders.domain

```
  * file:///tmp/source-code/orders-service/target/classes/application-mysql.properties
      * Spring datasource property key/value pairs have been detected in the application property file.. View advice in the Quarkus datasource guide to convert these to Quarkus datasource properties.
      * Code Snippet:
```java
  1  spring.datasource.legacyDS.url=jdbc:mysql://localhost:3306/ticketmonster?useSSL=false
  2  spring.datasource.legacyDS.username=ticket
  3  spring.datasource.legacyDS.password=monster
  4  spring.datasource.legacyDS.driverClassName=com.mysql.jdbc.Driver
  5  
  6  spring.datasource.ordersDS.url=jdbc:mysql://localhost:3306/orders?useSSL=false
  7  spring.datasource.ordersDS.username=ticket
  8  spring.datasource.ordersDS.password=monster
  9  spring.datasource.ordersDS.driverClassName=com.mysql.jdbc.Driver
 10  
 11  spring.jpa.hibernate.ddl-auto=none
 12  spring.jpa.properties.hibernate.dialect=org.teiid.dialect.TeiidDialect
 13  #spring.jpa.database-platform=org.teiid.dialect.TeiidDialect
 14  
 15  
 16  spring.teiid.model.package=org.ticketmonster.orders.domain

```
  * file:///tmp/source-code/orders-service/target/classes/application-mysql.properties
      * Spring datasource property key/value pairs have been detected in the application property file.. View advice in the Quarkus datasource guide to convert these to Quarkus datasource properties.
      * Code Snippet:
```java
  1  spring.datasource.legacyDS.url=jdbc:mysql://localhost:3306/ticketmonster?useSSL=false
  2  spring.datasource.legacyDS.username=ticket
  3  spring.datasource.legacyDS.password=monster
  4  spring.datasource.legacyDS.driverClassName=com.mysql.jdbc.Driver
  5  
  6  spring.datasource.ordersDS.url=jdbc:mysql://localhost:3306/orders?useSSL=false
  7  spring.datasource.ordersDS.username=ticket
  8  spring.datasource.ordersDS.password=monster
  9  spring.datasource.ordersDS.driverClassName=com.mysql.jdbc.Driver
 10  
 11  spring.jpa.hibernate.ddl-auto=none
 12  spring.jpa.properties.hibernate.dialect=org.teiid.dialect.TeiidDialect
 13  #spring.jpa.database-platform=org.teiid.dialect.TeiidDialect
 14  
 15  
 16  spring.teiid.model.package=org.ticketmonster.orders.domain

```
  * file:///tmp/source-code/orders-service/target/classes/application-mysql.properties
      * Spring datasource property key/value pairs have been detected in the application property file.. View advice in the Quarkus datasource guide to convert these to Quarkus datasource properties.
      * Code Snippet:
```java
  1  spring.datasource.legacyDS.url=jdbc:mysql://localhost:3306/ticketmonster?useSSL=false
  2  spring.datasource.legacyDS.username=ticket
  3  spring.datasource.legacyDS.password=monster
  4  spring.datasource.legacyDS.driverClassName=com.mysql.jdbc.Driver
  5  
  6  spring.datasource.ordersDS.url=jdbc:mysql://localhost:3306/orders?useSSL=false
  7  spring.datasource.ordersDS.username=ticket
  8  spring.datasource.ordersDS.password=monster
  9  spring.datasource.ordersDS.driverClassName=com.mysql.jdbc.Driver
 10  
 11  spring.jpa.hibernate.ddl-auto=none
 12  spring.jpa.properties.hibernate.dialect=org.teiid.dialect.TeiidDialect
 13  #spring.jpa.database-platform=org.teiid.dialect.TeiidDialect
 14  
 15  
 16  spring.teiid.model.package=org.ticketmonster.orders.domain

```
  * file:///tmp/source-code/orders-service/target/classes/application-mysql.properties
      * Spring datasource property key/value pairs have been detected in the application property file.. View advice in the Quarkus datasource guide to convert these to Quarkus datasource properties.
      * Code Snippet:
```java
  1  spring.datasource.legacyDS.url=jdbc:mysql://localhost:3306/ticketmonster?useSSL=false
  2  spring.datasource.legacyDS.username=ticket
  3  spring.datasource.legacyDS.password=monster
  4  spring.datasource.legacyDS.driverClassName=com.mysql.jdbc.Driver
  5  
  6  spring.datasource.ordersDS.url=jdbc:mysql://localhost:3306/orders?useSSL=false
  7  spring.datasource.ordersDS.username=ticket
  8  spring.datasource.ordersDS.password=monster
  9  spring.datasource.ordersDS.driverClassName=com.mysql.jdbc.Driver
 10  
 11  spring.jpa.hibernate.ddl-auto=none
 12  spring.jpa.properties.hibernate.dialect=org.teiid.dialect.TeiidDialect
 13  #spring.jpa.database-platform=org.teiid.dialect.TeiidDialect
 14  
 15  
 16  spring.teiid.model.package=org.ticketmonster.orders.domain

```
  * file:///tmp/source-code/orders-service/target/classes/application-mysql.properties
      * Spring datasource property key/value pairs have been detected in the application property file.. View advice in the Quarkus datasource guide to convert these to Quarkus datasource properties.
      * Code Snippet:
```java
  1  spring.datasource.legacyDS.url=jdbc:mysql://localhost:3306/ticketmonster?useSSL=false
  2  spring.datasource.legacyDS.username=ticket
  3  spring.datasource.legacyDS.password=monster
  4  spring.datasource.legacyDS.driverClassName=com.mysql.jdbc.Driver
  5  
  6  spring.datasource.ordersDS.url=jdbc:mysql://localhost:3306/orders?useSSL=false
  7  spring.datasource.ordersDS.username=ticket
  8  spring.datasource.ordersDS.password=monster
  9  spring.datasource.ordersDS.driverClassName=com.mysql.jdbc.Driver
 10  
 11  spring.jpa.hibernate.ddl-auto=none
 12  spring.jpa.properties.hibernate.dialect=org.teiid.dialect.TeiidDialect
 13  #spring.jpa.database-platform=org.teiid.dialect.TeiidDialect
 14  
 15  
 16  spring.teiid.model.package=org.ticketmonster.orders.domain

```
### #23 - springboot-properties-to-quarkus-00003
* Category: mandatory
* Effort: 1
* Description: Replace Spring log level property with Quarkus property
Spring log level property configuration have been detected in the application property file.. View advice in the Quarkus datasource guide to convert these to Quarkus log level properties.
* Labels: konveyor.io/source=springboot, konveyor.io/target=quarkus
* Links
  * Quarkus Configuring Logging Guide: https://quarkus.io/guides/logging#runtime-configuration
* Incidents
  * file:///tmp/source-code/orders-service/src/main/resources/application.properties
      * Spring log level property configuration have been detected in the application property file.. View advice in the Quarkus datasource guide to convert these to Quarkus log level properties.
      * Code Snippet:
```java
  1  spring.jpa.hibernate.ddl-auto=none
  2  spring.teiid.model.package=org.ticketmonster.orders.domain
  3  
  4  management.security.enabled=false
  5  server.port=8080
  6  
  7  #logging.level.org.springframework=DEBUG
  8  logging.level.org.teiid.spring=DEBUG

```
  * file:///tmp/source-code/orders-service/src/test/resources/application.properties
      * Spring log level property configuration have been detected in the application property file.. View advice in the Quarkus datasource guide to convert these to Quarkus log level properties.
      * Code Snippet:
```java
  1  spring.teiid.model.package=org.ticketmonster.orders.domain
  2  endpoints.mappings.sensitive=false
  3  #logging.level.org.springframework=DEBUG
  4  logging.level.org.teiid.spring=DEBUG
  5  
  6  spring.jpa.hibernate.ddl-auto=none

```
  * file:///tmp/source-code/orders-service/target/classes/application.properties
      * Spring log level property configuration have been detected in the application property file.. View advice in the Quarkus datasource guide to convert these to Quarkus log level properties.
      * Code Snippet:
```java
  1  spring.jpa.hibernate.ddl-auto=none
  2  spring.teiid.model.package=org.ticketmonster.orders.domain
  3  
  4  management.security.enabled=false
  5  server.port=8080
  6  
  7  #logging.level.org.springframework=DEBUG
  8  logging.level.org.teiid.spring=DEBUG

```
  * file:///tmp/source-code/orders-service/target/test-classes/application.properties
      * Spring log level property configuration have been detected in the application property file.. View advice in the Quarkus datasource guide to convert these to Quarkus log level properties.
      * Code Snippet:
```java
  1  spring.teiid.model.package=org.ticketmonster.orders.domain
  2  endpoints.mappings.sensitive=false
  3  #logging.level.org.springframework=DEBUG
  4  logging.level.org.teiid.spring=DEBUG
  5  
  6  spring.jpa.hibernate.ddl-auto=none

```
### #24 - springboot-web-to-quarkus-00000
* Category: mandatory
* Effort: 1
* Description: Replace the Spring Web artifact with Quarkus 'spring-web' extension
Replace the Spring Web artifact with Quarkus `spring-web` extension. Spring Web is a spring-web artifact brought transitively by any `org.springframework:spring-web*` dependency. Add Quarkus dependency `io.quarkus:quarkus-spring-web`. Starting with Quarkus version 2.5, the underlying JAX-RS engine must be chosen. For performance reasons,. the `quarkus-resteasy-reactive-jackson` dependency should be used.
* Labels: konveyor.io/source=springboot, konveyor.io/target=quarkus
* Links
  * Quarkus Migration Guide 2.5: https://github.com/quarkusio/quarkus/wiki/Migration-Guide-2.5#spring-web
  * Quarkus Spring Web Guide: https://quarkus.io/guides/spring-web
* Incidents
  * file:///tmp/source-code/pom.xml
      * Replace the Spring Web artifact with Quarkus `spring-web` extension. Spring Web is a spring-web artifact brought transitively by any `org.springframework:spring-web*` dependency. Add Quarkus dependency `io.quarkus:quarkus-spring-web`. Starting with Quarkus version 2.5, the underlying JAX-RS engine must be chosen. For performance reasons,. the `quarkus-resteasy-reactive-jackson` dependency should be used.
