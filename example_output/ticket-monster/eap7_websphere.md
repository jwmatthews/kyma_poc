# eap7/websphere
## Description
Provides analysis of WebSphere proprietary classes and constructs that may require individual attention when migrating to JBoss EAP 7+.
* Source of rules: https://github.com/konveyor/rulesets/tree/main/default/generated
## Violations
Number of Violations: 5
### #0 - maven-javax-to-jakarta-00002
* Category: potential
* Effort: 1
* Description: Move to Jakarta EE Maven Artifacts - replace groupId javax.activation
If you migrate your application to JBoss EAP 7.3, or later, and want to ensure its Maven building, running or testing works as expected, use instead the Jakarta EE dependency with groupId `com.sun.activation`
* Labels: JakartaEE, konveyor.io/source, konveyor.io/target=eap, konveyor.io/target=eap7, konveyor.io/target=eap8, konveyor.io/target=jakarta-ee, konveyor.io/target=jakarta-ee8
* Links
  * Red Hat JBoss EAP 7.3 Migration Guide: Maven Artifact Changes for Jakarta EE: https://access.redhat.com/documentation/en-us/red_hat_jboss_enterprise_application_platform/7.3/html-single/migration_guide/index#maven-artifact-changes-for-jakarta-ee_default
* Incidents
  * file:///tmp/source-code/pom.xml
      * If you migrate your application to JBoss EAP 7.3, or later, and want to ensure its Maven building, running or testing works as expected, use instead the Jakarta EE dependency with groupId `com.sun.activation`
### #1 - maven-javax-to-jakarta-00004
* Category: potential
* Effort: 1
* Description: javax.{renamed-g} groupId has been replaced by jakarta.{renamed-g}

* Labels: JakartaEE, konveyor.io/source, konveyor.io/target=eap, konveyor.io/target=eap7, konveyor.io/target=eap8, konveyor.io/target=jakarta-ee, konveyor.io/target=jakarta-ee8
* Links
  * Red Hat JBoss EAP 7.3 Migration Guide: Maven Artifact Changes for Jakarta EE: https://access.redhat.com/documentation/en-us/red_hat_jboss_enterprise_application_platform/7.3/html-single/migration_guide/index#maven-artifact-changes-for-jakarta-ee_default
* Incidents
  * file:///tmp/source-code/backend-v1/pom.xml
      * If you migrate your application to JBoss EAP 7.3, or later, and want to ensure its Maven building, running or testing works as expected, use instead the Jakarta EE dependency - groupId `jakarta.`.
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
  * file:///tmp/source-code/backend-v1/pom.xml
      * If you migrate your application to JBoss EAP 7.3, or later, and want to ensure its Maven building, running or testing works as expected, use instead the Jakarta EE dependency - groupId `jakarta.`.
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
  * file:///tmp/source-code/backend-v1/pom.xml
      * If you migrate your application to JBoss EAP 7.3, or later, and want to ensure its Maven building, running or testing works as expected, use instead the Jakarta EE dependency - groupId `jakarta.`.
      * Code Snippet:
```java
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
238              <type>pom</type>
239              <scope>test</scope>
240          </dependency>
241  
242          <!-- RESTEasy dependencies that bring in Jackson Core and RESTEasy APIs+SPIs, which we use for
243              fine tuning the content of the JSON responses -->
```
  * file:///tmp/source-code/backend-v2/pom.xml
      * If you migrate your application to JBoss EAP 7.3, or later, and want to ensure its Maven building, running or testing works as expected, use instead the Jakarta EE dependency - groupId `jakarta.`.
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
  * file:///tmp/source-code/backend-v2/pom.xml
      * If you migrate your application to JBoss EAP 7.3, or later, and want to ensure its Maven building, running or testing works as expected, use instead the Jakarta EE dependency - groupId `jakarta.`.
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
  * file:///tmp/source-code/backend-v2/pom.xml
      * If you migrate your application to JBoss EAP 7.3, or later, and want to ensure its Maven building, running or testing works as expected, use instead the Jakarta EE dependency - groupId `jakarta.`.
      * Code Snippet:
```java
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
249  
250          <!-- Optional, but highly recommended -->
251          <!-- Arquillian allows you to test enterprise code such as EJBs and 
252              Transactional(JTA) JPA from JUnit/TestNG -->
253          <dependency>
254              <groupId>org.jboss.arquillian.junit</groupId>
```
  * file:///tmp/source-code/monolith/pom.xml
      * If you migrate your application to JBoss EAP 7.3, or later, and want to ensure its Maven building, running or testing works as expected, use instead the Jakarta EE dependency - groupId `jakarta.`.
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
  * file:///tmp/source-code/monolith/pom.xml
      * If you migrate your application to JBoss EAP 7.3, or later, and want to ensure its Maven building, running or testing works as expected, use instead the Jakarta EE dependency - groupId `jakarta.`.
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
  * file:///tmp/source-code/monolith/pom.xml
      * If you migrate your application to JBoss EAP 7.3, or later, and want to ensure its Maven building, running or testing works as expected, use instead the Jakarta EE dependency - groupId `jakarta.`.
      * Code Snippet:
```java
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
238              <type>pom</type>
239              <scope>test</scope>
240          </dependency>
241  
242          <!-- RESTEasy dependencies that bring in Jackson Core and RESTEasy APIs+SPIs, which we use for
243              fine tuning the content of the JSON responses -->
```
### #2 - maven-javax-to-jakarta-00006
* Category: potential
* Effort: 1
* Description: Move to Jakarta EE Maven Artifacts - replace artifactId cdi-api
If you migrate your application to JBoss EAP 7.3, or later, and want to ensure its Maven building, running or testing works as expected, use instead the Jakarta EE dependency with artifactId `jakarta.enterprise.cdi-api`
* Labels: JakartaEE, konveyor.io/source, konveyor.io/target=eap, konveyor.io/target=eap7, konveyor.io/target=eap8, konveyor.io/target=jakarta-ee, konveyor.io/target=jakarta-ee8
* Links
  * Red Hat JBoss EAP 7.3 Migration Guide: Maven Artifact Changes for Jakarta EE: https://access.redhat.com/documentation/en-us/red_hat_jboss_enterprise_application_platform/7.3/html-single/migration_guide/index#maven-artifact-changes-for-jakarta-ee_default
* Incidents
  * file:///tmp/source-code/backend-v1/pom.xml
      * If you migrate your application to JBoss EAP 7.3, or later, and want to ensure its Maven building, running or testing works as expected, use instead the Jakarta EE dependency with artifactId `jakarta.enterprise.cdi-api`
      * Code Snippet:
```java
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
232              <scope>test</scope>
```
  * file:///tmp/source-code/backend-v2/pom.xml
      * If you migrate your application to JBoss EAP 7.3, or later, and want to ensure its Maven building, running or testing works as expected, use instead the Jakarta EE dependency with artifactId `jakarta.enterprise.cdi-api`
      * Code Snippet:
```java
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
243          <dependency>
```
  * file:///tmp/source-code/monolith/pom.xml
      * If you migrate your application to JBoss EAP 7.3, or later, and want to ensure its Maven building, running or testing works as expected, use instead the Jakarta EE dependency with artifactId `jakarta.enterprise.cdi-api`
      * Code Snippet:
```java
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
232              <scope>test</scope>
```
### #3 - maven-javax-to-jakarta-00007
* Category: potential
* Effort: 1
* Description: Move to Jakarta EE Maven Artifacts - replace artifactId validation-api
If you migrate your application to JBoss EAP 7.3, or later, and want to ensure its Maven building, running or testing works as expected, use instead the Jakarta EE dependency with artifactId `jakarta.validation-api`
* Labels: JakartaEE, konveyor.io/source, konveyor.io/target=eap, konveyor.io/target=eap7, konveyor.io/target=eap8, konveyor.io/target=jakarta-ee, konveyor.io/target=jakarta-ee8
* Links
  * Red Hat JBoss EAP 7.3 Migration Guide: Maven Artifact Changes for Jakarta EE: https://access.redhat.com/documentation/en-us/red_hat_jboss_enterprise_application_platform/7.3/html-single/migration_guide/index#maven-artifact-changes-for-jakarta-ee_default
* Incidents
  * file:///tmp/source-code/backend-v1/pom.xml
      * If you migrate your application to JBoss EAP 7.3, or later, and want to ensure its Maven building, running or testing works as expected, use instead the Jakarta EE dependency with artifactId `jakarta.validation-api`
      * Code Snippet:
```java
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
238              <type>pom</type>
239              <scope>test</scope>
240          </dependency>
241  
242          <!-- RESTEasy dependencies that bring in Jackson Core and RESTEasy APIs+SPIs, which we use for
243              fine tuning the content of the JSON responses -->
244          <dependency>
```
  * file:///tmp/source-code/backend-v2/pom.xml
      * If you migrate your application to JBoss EAP 7.3, or later, and want to ensure its Maven building, running or testing works as expected, use instead the Jakarta EE dependency with artifactId `jakarta.validation-api`
      * Code Snippet:
```java
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
249  
250          <!-- Optional, but highly recommended -->
251          <!-- Arquillian allows you to test enterprise code such as EJBs and 
252              Transactional(JTA) JPA from JUnit/TestNG -->
253          <dependency>
254              <groupId>org.jboss.arquillian.junit</groupId>
255              <artifactId>arquillian-junit-container</artifactId>
```
  * file:///tmp/source-code/monolith/pom.xml
      * If you migrate your application to JBoss EAP 7.3, or later, and want to ensure its Maven building, running or testing works as expected, use instead the Jakarta EE dependency with artifactId `jakarta.validation-api`
      * Code Snippet:
```java
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
238              <type>pom</type>
239              <scope>test</scope>
240          </dependency>
241  
242          <!-- RESTEasy dependencies that bring in Jackson Core and RESTEasy APIs+SPIs, which we use for
243              fine tuning the content of the JSON responses -->
244          <dependency>
```
### #4 - maven-javax-to-jakarta-00008
* Category: potential
* Effort: 1
* Description: Move to Jakarta EE Maven Artifacts - replace artifactId javax.inject
If you migrate your application to JBoss EAP 7.3, or later, and want to ensure its Maven building, running or testing works as expected, use instead the Jakarta EE dependency with artifactId `jakarta.inject-api`
* Labels: JakartaEE, konveyor.io/source, konveyor.io/target=eap, konveyor.io/target=eap7, konveyor.io/target=eap8, konveyor.io/target=jakarta-ee, konveyor.io/target=jakarta-ee8
* Links
  * Red Hat JBoss EAP 7.3 Migration Guide: Maven Artifact Changes for Jakarta EE: https://access.redhat.com/documentation/en-us/red_hat_jboss_enterprise_application_platform/7.3/html-single/migration_guide/index#maven-artifact-changes-for-jakarta-ee_default
* Incidents
  * file:///tmp/source-code/backend-v1/pom.xml
      * If you migrate your application to JBoss EAP 7.3, or later, and want to ensure its Maven building, running or testing works as expected, use instead the Jakarta EE dependency with artifactId `jakarta.inject-api`
      * Code Snippet:
```java
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
238              <type>pom</type>
```
  * file:///tmp/source-code/backend-v2/pom.xml
      * If you migrate your application to JBoss EAP 7.3, or later, and want to ensure its Maven building, running or testing works as expected, use instead the Jakarta EE dependency with artifactId `jakarta.inject-api`
      * Code Snippet:
```java
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
249  
```
  * file:///tmp/source-code/monolith/pom.xml
      * If you migrate your application to JBoss EAP 7.3, or later, and want to ensure its Maven building, running or testing works as expected, use instead the Jakarta EE dependency with artifactId `jakarta.inject-api`
      * Code Snippet:
```java
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
238              <type>pom</type>
```
