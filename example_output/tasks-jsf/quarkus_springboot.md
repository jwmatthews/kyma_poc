# quarkus/springboot
## Description
This ruleset gives hints to migrate from SpringBoot devtools to Quarkus
* Source of rules: https://github.com/konveyor/rulesets/tree/main/default/generated
## Violations
Number of Violations: 10
### #0 - cdi-to-quarkus-00030
* Category: potential
* Effort: 3
* Description: `beans.xml` descriptor content is ignored
* Labels: konveyor.io/source=java-ee, konveyor.io/target=quarkus
* Incidents
  * file:///tmp/source-code/src/main/webapp/WEB-INF/beans.xml
      * Message: '`beans.xml` descriptor content is ignored and it could be removed from the application. 
 Refer to the guide referenced below to check the supported CDI feature in Quarkus.'
  * file:///tmp/source-code/src/test/webapp/WEB-INF/beans.xml
      * Line Number: 23
      * Message: '`beans.xml` descriptor content is ignored and it could be removed from the application. 
 Refer to the guide referenced below to check the supported CDI feature in Quarkus.'
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
 18  <!-- Marker file indicating CDI should be enabled -->
 19  <beans xmlns="http://xmlns.jcp.org/xml/ns/javaee" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 20      xsi:schemaLocation="
 21        http://xmlns.jcp.org/xml/ns/javaee
 22        http://xmlns.jcp.org/xml/ns/javaee/beans_1_1.xsd"
 23      bean-discovery-mode="all">
 24      <alternatives>
 25          <stereotype>org.jboss.as.quickstarts.tasksJsf.Testing</stereotype>
 26      </alternatives>
 27  </beans>

```
### #1 - cdi-to-quarkus-00040
* Category: potential
* Effort: 1
* Description: Producer annotation no longer required
* Labels: konveyor.io/source=java-ee, konveyor.io/target=quarkus
* Links
  * Quarkus Simplified Producer Method Declaration: https://quarkus.io/guides/cdi-reference#simplified-producer-method-declaration
* Incidents
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/tasksJsf/AuthController.java
      * Line Number: 64
      * Message: 'In Quarkus, you can skip the @Produces annotation completely if the producer method is annotated with a scope annotation, a stereotype or a qualifier..
 This field could be accessed using a `@Named` getter method instead.'
      * Code Snippet:
```java
  1  /*
  2   * JBoss, Home of Professional Open Source
  3   * Copyright 2015, Red Hat, Inc. and/or its affiliates, and individual
  4   * contributors by the @authors tag. See the copyright.txt in the
  5   * distribution for a full listing of individual contributors.
  6   *
  7   * Licensed under the Apache License, Version 2.0 (the "License");
  8   * you may not use this file except in compliance with the License.
  9   * You may obtain a copy of the License at
 10   * http://www.apache.org/licenses/LICENSE-2.0
 11   * Unless required by applicable law or agreed to in writing, software
 12   * distributed under the License is distributed on an "AS IS" BASIS,
 13   * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 14   * See the License for the specific language governing permissions and
 15   * limitations under the License.
 16   */
 17  package org.jboss.as.quickstarts.tasksJsf;
 18  
 19  import javax.enterprise.context.Conversation;
 20  import javax.enterprise.context.RequestScoped;
 21  import javax.enterprise.inject.Produces;
 22  import javax.faces.application.FacesMessage;
 23  import javax.faces.context.FacesContext;
 24  import javax.inject.Inject;
 25  import javax.inject.Named;
 26  
 27  /**
 28   * Provides authentication operations with current user store: {@link Authentication}.
 29   *
 30   * @author Lukas Fryc
 31   *
 32   */
 33  @Named
 34  @RequestScoped
 35  public class AuthController {
 36  
 37      @Inject
 38      private Authentication authentication;
 39  
 40      @Inject
 41      private UserDao userDao;
 42  
 43      @Inject
 44      private FacesContext facesContext;
 45  
 46      @Inject
 47      private Conversation conversation;
 48  
 49      /**
 50       * <p>
 51       * Provides current user to the context available for injection using:
 52       * </p>
 53       *
 54       * <p>
 55       * <code>@Inject @CurrentUser currentUser;</code>
 56       * </p>
 57       *
 58       * <p>
 59       * or from the Expression Language context using an expression <code>#{currentUser}</code>.
 60       * </p>
 61       *
 62       * @return current authenticated user
 63       */
 64      @Produces
 65      @Named
 66      @CurrentUser
 67      public User getCurrentUser() {
 68          return authentication.getCurrentUser();
 69      }
 70  
 71      /**
 72       * <p>
 73       * Authenticates current user with 'username' against user data store
 74       * </p>
 75       *
 76       * <p>
 77       * Starts the new conversation.
 78       * </p>
 79       *
 80       * @param username the username of the user to authenticate
 81       */
 82      public void authenticate(String username) {
 83          if (isLogged()) {
 84              throw new IllegalStateException("User is logged and tries to authenticate again");
 85          }
 86  
 87          User user = userDao.getForUsername(username);
 88          if (user == null) {
 89              user = createUser(username);
 90          }
 91          authentication.setCurrentUser(user);
 92          conversation.begin();
 93      }
 94  
 95      /**
 96       * Logs current user out and ends the current conversation.
 97       */
 98      public void logout() {
 99          authentication.setCurrentUser(null);
100          conversation.end();
101      }
102  
103      /**
104       * Returns true if user is logged in
105       *
106       * @return true if user is logged in; false otherwise
107       */
108      public boolean isLogged() {
109          return authentication.getCurrentUser() != null;
110      }
111  
112      private User createUser(String username) {
113          try {
114              User user = new User(username);
115              userDao.createUser(user);
116              facesContext.addMessage(null, new FacesMessage("User successfully created"));
117              return user;
118          } catch (Exception e) {
119              facesContext.addMessage(null, new FacesMessage("Failed to create user '" + username + "'", e.getMessage()));
120              return null;
121          }
122      }
123  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/tasksJsf/CurrentTaskStore.java
      * Line Number: 54
      * Message: 'In Quarkus, you can skip the @Produces annotation completely if the producer method is annotated with a scope annotation, a stereotype or a qualifier..
 This field could be accessed using a `@Named` getter method instead.'
      * Code Snippet:
```java
  1  /*
  2   * JBoss, Home of Professional Open Source
  3   * Copyright 2015, Red Hat, Inc. and/or its affiliates, and individual
  4   * contributors by the @authors tag. See the copyright.txt in the
  5   * distribution for a full listing of individual contributors.
  6   *
  7   * Licensed under the Apache License, Version 2.0 (the "License");
  8   * you may not use this file except in compliance with the License.
  9   * You may obtain a copy of the License at
 10   * http://www.apache.org/licenses/LICENSE-2.0
 11   * Unless required by applicable law or agreed to in writing, software
 12   * distributed under the License is distributed on an "AS IS" BASIS,
 13   * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 14   * See the License for the specific language governing permissions and
 15   * limitations under the License.
 16   */
 17  package org.jboss.as.quickstarts.tasksJsf;
 18  
 19  import java.io.Serializable;
 20  
 21  import javax.enterprise.context.ConversationScoped;
 22  import javax.enterprise.inject.Produces;
 23  import javax.inject.Named;
 24  
 25  /**
 26   * <p>
 27   * Holds current task in context of conversation
 28   * </p>
 29   *
 30   * @author Lukas Fryc
 31   *
 32   */
 33  @SuppressWarnings("serial")
 34  @ConversationScoped
 35  public class CurrentTaskStore implements Serializable {
 36  
 37      private Task currentTask;
 38  
 39      /**
 40       * <p>
 41       * Provides current task to the context available for injection using:
 42       * </p>
 43       *
 44       * <p>
 45       * <code>@Inject @CurrentTask currentTask;</code>
 46       * </p>
 47       *
 48       * <p>
 49       * or from the Expression Language context using an expression <code>#{currentTask}</code>.
 50       * </p>
 51       *
 52       * @return current authenticated user
 53       */
 54      @Produces
 55      @CurrentTask
 56      @Named("currentTask")
 57      public Task get() {
 58          return currentTask;
 59      }
 60  
 61      /**
 62       * Setup current task
 63       *
 64       * @param currentTask task to setup as current
 65       */
 66      public void set(Task currentTask) {
 67          this.currentTask = currentTask;
 68      }
 69  
 70      public void unset() {
 71          this.currentTask = null;
 72      }
 73  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/tasksJsf/Resources.java
      * Line Number: 49
      * Message: 'In Quarkus, you can skip the @Produces annotation completely if the producer method is annotated with a scope annotation, a stereotype or a qualifier..
 This field could be accessed using a `@Named` getter method instead.'
      * Code Snippet:
```java
  1  /*
  2   * JBoss, Home of Professional Open Source
  3   * Copyright 2015, Red Hat, Inc. and/or its affiliates, and individual
  4   * contributors by the @authors tag. See the copyright.txt in the
  5   * distribution for a full listing of individual contributors.
  6   *
  7   * Licensed under the Apache License, Version 2.0 (the "License");
  8   * you may not use this file except in compliance with the License.
  9   * You may obtain a copy of the License at
 10   * http://www.apache.org/licenses/LICENSE-2.0
 11   * Unless required by applicable law or agreed to in writing, software
 12   * distributed under the License is distributed on an "AS IS" BASIS,
 13   * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 14   * See the License for the specific language governing permissions and
 15   * limitations under the License.
 16   */
 17  package org.jboss.as.quickstarts.tasksJsf;
 18  
 19  import java.util.logging.Logger;
 20  
 21  import javax.ejb.Stateful;
 22  import javax.enterprise.context.RequestScoped;
 23  import javax.enterprise.inject.Produces;
 24  import javax.enterprise.inject.spi.InjectionPoint;
 25  import javax.faces.context.FacesContext;
 26  import javax.persistence.EntityManager;
 27  import javax.persistence.PersistenceContext;
 28  import javax.persistence.PersistenceContextType;
 29  
 30  /**
 31   * This class uses CDI to alias Jakarta EE resources, such as the persistence context, to CDI beans. As it is a stateful bean, it
 32   * can produce extended persistence contexts.
 33   *
 34   * Example injection on a managed bean field:
 35   *
 36   * &#064;Inject private EntityManager em;
 37   *
 38   * @author Pete Muir
 39   * @author Lukas Fryc
 40   *
 41   */
 42  @Stateful
 43  @RequestScoped
 44  public class Resources {
 45  
 46      @PersistenceContext(type = PersistenceContextType.EXTENDED)
 47      private EntityManager em;
 48  
 49      @Produces
 50      public EntityManager getEm() {
 51          return em;
 52      }
 53  
 54      @Produces
 55      public Logger getLogger(InjectionPoint ip) {
 56          String category = ip.getMember().getDeclaringClass().getName();
 57          return Logger.getLogger(category);
 58      }
 59  
 60      @Produces
 61      public FacesContext getFacesContext() {
 62          return FacesContext.getCurrentInstance();
 63      }
 64  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/tasksJsf/Resources.java
      * Line Number: 54
      * Message: 'In Quarkus, you can skip the @Produces annotation completely if the producer method is annotated with a scope annotation, a stereotype or a qualifier..
 This field could be accessed using a `@Named` getter method instead.'
      * Code Snippet:
```java
  1  /*
  2   * JBoss, Home of Professional Open Source
  3   * Copyright 2015, Red Hat, Inc. and/or its affiliates, and individual
  4   * contributors by the @authors tag. See the copyright.txt in the
  5   * distribution for a full listing of individual contributors.
  6   *
  7   * Licensed under the Apache License, Version 2.0 (the "License");
  8   * you may not use this file except in compliance with the License.
  9   * You may obtain a copy of the License at
 10   * http://www.apache.org/licenses/LICENSE-2.0
 11   * Unless required by applicable law or agreed to in writing, software
 12   * distributed under the License is distributed on an "AS IS" BASIS,
 13   * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 14   * See the License for the specific language governing permissions and
 15   * limitations under the License.
 16   */
 17  package org.jboss.as.quickstarts.tasksJsf;
 18  
 19  import java.util.logging.Logger;
 20  
 21  import javax.ejb.Stateful;
 22  import javax.enterprise.context.RequestScoped;
 23  import javax.enterprise.inject.Produces;
 24  import javax.enterprise.inject.spi.InjectionPoint;
 25  import javax.faces.context.FacesContext;
 26  import javax.persistence.EntityManager;
 27  import javax.persistence.PersistenceContext;
 28  import javax.persistence.PersistenceContextType;
 29  
 30  /**
 31   * This class uses CDI to alias Jakarta EE resources, such as the persistence context, to CDI beans. As it is a stateful bean, it
 32   * can produce extended persistence contexts.
 33   *
 34   * Example injection on a managed bean field:
 35   *
 36   * &#064;Inject private EntityManager em;
 37   *
 38   * @author Pete Muir
 39   * @author Lukas Fryc
 40   *
 41   */
 42  @Stateful
 43  @RequestScoped
 44  public class Resources {
 45  
 46      @PersistenceContext(type = PersistenceContextType.EXTENDED)
 47      private EntityManager em;
 48  
 49      @Produces
 50      public EntityManager getEm() {
 51          return em;
 52      }
 53  
 54      @Produces
 55      public Logger getLogger(InjectionPoint ip) {
 56          String category = ip.getMember().getDeclaringClass().getName();
 57          return Logger.getLogger(category);
 58      }
 59  
 60      @Produces
 61      public FacesContext getFacesContext() {
 62          return FacesContext.getCurrentInstance();
 63      }
 64  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/tasksJsf/Resources.java
      * Line Number: 60
      * Message: 'In Quarkus, you can skip the @Produces annotation completely if the producer method is annotated with a scope annotation, a stereotype or a qualifier..
 This field could be accessed using a `@Named` getter method instead.'
      * Code Snippet:
```java
  1  /*
  2   * JBoss, Home of Professional Open Source
  3   * Copyright 2015, Red Hat, Inc. and/or its affiliates, and individual
  4   * contributors by the @authors tag. See the copyright.txt in the
  5   * distribution for a full listing of individual contributors.
  6   *
  7   * Licensed under the Apache License, Version 2.0 (the "License");
  8   * you may not use this file except in compliance with the License.
  9   * You may obtain a copy of the License at
 10   * http://www.apache.org/licenses/LICENSE-2.0
 11   * Unless required by applicable law or agreed to in writing, software
 12   * distributed under the License is distributed on an "AS IS" BASIS,
 13   * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 14   * See the License for the specific language governing permissions and
 15   * limitations under the License.
 16   */
 17  package org.jboss.as.quickstarts.tasksJsf;
 18  
 19  import java.util.logging.Logger;
 20  
 21  import javax.ejb.Stateful;
 22  import javax.enterprise.context.RequestScoped;
 23  import javax.enterprise.inject.Produces;
 24  import javax.enterprise.inject.spi.InjectionPoint;
 25  import javax.faces.context.FacesContext;
 26  import javax.persistence.EntityManager;
 27  import javax.persistence.PersistenceContext;
 28  import javax.persistence.PersistenceContextType;
 29  
 30  /**
 31   * This class uses CDI to alias Jakarta EE resources, such as the persistence context, to CDI beans. As it is a stateful bean, it
 32   * can produce extended persistence contexts.
 33   *
 34   * Example injection on a managed bean field:
 35   *
 36   * &#064;Inject private EntityManager em;
 37   *
 38   * @author Pete Muir
 39   * @author Lukas Fryc
 40   *
 41   */
 42  @Stateful
 43  @RequestScoped
 44  public class Resources {
 45  
 46      @PersistenceContext(type = PersistenceContextType.EXTENDED)
 47      private EntityManager em;
 48  
 49      @Produces
 50      public EntityManager getEm() {
 51          return em;
 52      }
 53  
 54      @Produces
 55      public Logger getLogger(InjectionPoint ip) {
 56          String category = ip.getMember().getDeclaringClass().getName();
 57          return Logger.getLogger(category);
 58      }
 59  
 60      @Produces
 61      public FacesContext getFacesContext() {
 62          return FacesContext.getCurrentInstance();
 63      }
 64  }

```
### #2 - javaee-faces-to-quarkus-00000
* Category: mandatory
* Effort: 1
* Description: Replace JSF Dependency with MyFaces
* Labels: konveyor.io/source=java-ee, konveyor.io/target=quarkus
* Links
  * Apache MyFaces: Getting Started on Quarkus: https://myfaces.apache.org/#/coregettingstarted?id=quarkus
* Incidents
  * file:///tmp/source-code/pom.xml
      * Line Number: 88
      * Message: 'JSF Dependencies with groupId `org.jboss.spec.javax.faces` should be replaced with 
 
 ```
 <!-- Quarkus MyFaces dependencies --> 
 <dependency>
 <groupId>org.apache.myfaces.core.extensions.quarkus</groupId>
 <artifactId>myfaces-quarkus</artifactId>
 <version>4.0.1</version>
 </dependency>
 
 <!-- Quarkus Faces utilities and components extensions -->
 <dependency>
 <groupId>io.quarkiverse.primefaces</groupId>
 <artifactId>quarkus-primefaces</artifactId>
 <version>3.13.1</version>
 </dependency>
 <dependency>
 <groupId>io.quarkiverse.omnifaces</groupId>
 <artifactId>quarkus-omnifaces</artifactId>
 <version>4.2.0</version>
 </dependency>
 ```'
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
 18  <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
 19      <modelVersion>4.0.0</modelVersion>
 20      <parent>
 21          <groupId>org.jboss.eap.quickstarts</groupId>
 22          <artifactId>quickstart-parent</artifactId>
 23          <!--
 24          Maintain separation between the artifact id and the version to help prevent
 25          merge conflicts between commits changing the GA and those changing the V.
 26          -->
 27          <version>7.4.0.GA</version>
 28          <relativePath>../pom.xml</relativePath>
 29      </parent>
 30  
 31      <artifactId>tasks-jsf</artifactId>
 32      <packaging>war</packaging>
 33      <name>Quickstart: tasks-jsf</name>
 34      <description>This project demonstrates how to use JPA persistence to manage tasks with JSF as view layer</description>
 35  
 36      <licenses>
 37          <license>
 38              <name>Apache License, Version 2.0</name>
 39              <url>http://www.apache.org/licenses/LICENSE-2.0.html</url>
 40              <distribution>repo</distribution>
 41          </license>
 42      </licenses>
 43  
 44      <dependencies>
 45  
 46          <!-- Import the CDI API, we use provided scope as the API is included in JBoss EAP -->
 47          <dependency>
 48              <groupId>jakarta.enterprise</groupId>
 49              <artifactId>jakarta.enterprise.cdi-api</artifactId>
 50              <scope>provided</scope>
 51          </dependency>
 52  
 53          <!-- Test dependencies -->
 54          <dependency>
 55              <groupId>junit</groupId>
 56              <artifactId>junit</artifactId>
 57              <scope>test</scope>
 58          </dependency>
 59  
 60          <!-- Import the JPA API, we use provided scope as the API is included in JBoss EAP -->
 61          <dependency>
 62              <groupId>jakarta.persistence</groupId>
 63              <artifactId>jakarta.persistence-api</artifactId>
 64              <scope>provided</scope>
 65          </dependency>
 66  
 67          <dependency>
 68              <groupId>org.jboss.arquillian.junit</groupId>
 69              <artifactId>arquillian-junit-container</artifactId>
 70              <scope>test</scope>
 71          </dependency>
 72  
 73          <dependency>
 74              <groupId>org.jboss.arquillian.protocol</groupId>
 75              <artifactId>arquillian-protocol-servlet</artifactId>
 76              <scope>test</scope>
 77          </dependency>
 78  
 79          <!-- Import the EJB API, we use provided scope as the API is included in JBoss EAP -->
 80          <dependency>
 81              <groupId>org.jboss.spec.javax.ejb</groupId>
 82              <artifactId>jboss-ejb-api_3.2_spec</artifactId>
 83              <scope>provided</scope>
 84          </dependency>
 85  
 86          <!-- Import the JSF API, we use provided scope as the API is included in JBoss EAP -->
 87          <dependency>
 88              <groupId>org.jboss.spec.javax.faces</groupId>
 89              <artifactId>jboss-jsf-api_2.3_spec</artifactId>
 90              <scope>provided</scope>
 91          </dependency>
 92  
 93      </dependencies>
 94  
 95      <build>
 96          <!-- Set the name of the WAR, used as the context root when the app is deployed -->
 97          <finalName>${project.artifactId}</finalName>
 98      </build>
 99  
100  </project>

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
      * Line Number: 19
      * Message: 'Use the Quarkus BOM to omit the version of the different Quarkus dependencies. 
 Add the following sections to the `pom.xml` file: 

 ```xml
 <properties> 
 <quarkus.platform.artifact-id>quarkus-bom</quarkus.platform.artifact-id> 
 <quarkus.platform.group-id>io.quarkus.platform</quarkus.platform.group-id> 
 <quarkus.platform.version>3.1.0.Final</quarkus.platform.version>
 </properties> 
 <dependencyManagement> 
 <dependencies> 
 <dependency> 
 <groupId>$</groupId> 
 <artifactId>$</artifactId> 
 <version>$</version> 
 <type>pom</type> 
 <scope>import</scope> 
 </dependency> 
 </dependencies> 
 </dependencyManagement> 
 ```
 Check the latest Quarkus version available from the `Quarkus - Releases` link below.'
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
 18  <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
 19      <modelVersion>4.0.0</modelVersion>
 20      <parent>
 21          <groupId>org.jboss.eap.quickstarts</groupId>
 22          <artifactId>quickstart-parent</artifactId>
 23          <!--
 24          Maintain separation between the artifact id and the version to help prevent
 25          merge conflicts between commits changing the GA and those changing the V.
 26          -->
 27          <version>7.4.0.GA</version>
 28          <relativePath>../pom.xml</relativePath>
 29      </parent>
 30  
 31      <artifactId>tasks-jsf</artifactId>
 32      <packaging>war</packaging>
 33      <name>Quickstart: tasks-jsf</name>
 34      <description>This project demonstrates how to use JPA persistence to manage tasks with JSF as view layer</description>
 35  
 36      <licenses>
 37          <license>
 38              <name>Apache License, Version 2.0</name>
 39              <url>http://www.apache.org/licenses/LICENSE-2.0.html</url>
 40              <distribution>repo</distribution>
 41          </license>
 42      </licenses>
 43  
 44      <dependencies>
 45  
 46          <!-- Import the CDI API, we use provided scope as the API is included in JBoss EAP -->
 47          <dependency>
 48              <groupId>jakarta.enterprise</groupId>
 49              <artifactId>jakarta.enterprise.cdi-api</artifactId>
 50              <scope>provided</scope>
 51          </dependency>
 52  
 53          <!-- Test dependencies -->
 54          <dependency>
 55              <groupId>junit</groupId>
 56              <artifactId>junit</artifactId>
 57              <scope>test</scope>
 58          </dependency>
 59  
 60          <!-- Import the JPA API, we use provided scope as the API is included in JBoss EAP -->
 61          <dependency>
 62              <groupId>jakarta.persistence</groupId>
 63              <artifactId>jakarta.persistence-api</artifactId>
 64              <scope>provided</scope>
 65          </dependency>
 66  
 67          <dependency>
 68              <groupId>org.jboss.arquillian.junit</groupId>
 69              <artifactId>arquillian-junit-container</artifactId>
 70              <scope>test</scope>
 71          </dependency>
 72  
 73          <dependency>
 74              <groupId>org.jboss.arquillian.protocol</groupId>
 75              <artifactId>arquillian-protocol-servlet</artifactId>
 76              <scope>test</scope>
 77          </dependency>
 78  
 79          <!-- Import the EJB API, we use provided scope as the API is included in JBoss EAP -->
 80          <dependency>
 81              <groupId>org.jboss.spec.javax.ejb</groupId>
 82              <artifactId>jboss-ejb-api_3.2_spec</artifactId>
 83              <scope>provided</scope>
 84          </dependency>
 85  
 86          <!-- Import the JSF API, we use provided scope as the API is included in JBoss EAP -->
 87          <dependency>
 88              <groupId>org.jboss.spec.javax.faces</groupId>
 89              <artifactId>jboss-jsf-api_2.3_spec</artifactId>
 90              <scope>provided</scope>
 91          </dependency>
 92  
 93      </dependencies>
 94  
 95      <build>
 96          <!-- Set the name of the WAR, used as the context root when the app is deployed -->
 97          <finalName>${project.artifactId}</finalName>
 98      </build>
 99  
100  </project>

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
      * Line Number: 19
      * Message: 'Use the Quarkus Maven plugin adding the following sections to the `pom.xml` file: 

 ```xml
 <properties> 
 <quarkus.platform.group-id>io.quarkus.platform</quarkus.platform.group-id> 
 <quarkus.platform.version>3.1.0.Final</quarkus.platform.version>
 </properties> 
 <build>
 <plugins>
 <plugin>
 <groupId>$</groupId>
 <artifactId>quarkus-maven-plugin</artifactId>
 <version>$</version>
 <extensions>true</extensions>
 <executions>
 <execution>
 <goals>
 <goal>build</goal>
 <goal>generate-code</goal>
 <goal>generate-code-tests</goal>
 </goals>
 </execution>
 </executions>
 </plugin>
 </plugins>
 </build>
 ```'
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
 18  <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
 19      <modelVersion>4.0.0</modelVersion>
 20      <parent>
 21          <groupId>org.jboss.eap.quickstarts</groupId>
 22          <artifactId>quickstart-parent</artifactId>
 23          <!--
 24          Maintain separation between the artifact id and the version to help prevent
 25          merge conflicts between commits changing the GA and those changing the V.
 26          -->
 27          <version>7.4.0.GA</version>
 28          <relativePath>../pom.xml</relativePath>
 29      </parent>
 30  
 31      <artifactId>tasks-jsf</artifactId>
 32      <packaging>war</packaging>
 33      <name>Quickstart: tasks-jsf</name>
 34      <description>This project demonstrates how to use JPA persistence to manage tasks with JSF as view layer</description>
 35  
 36      <licenses>
 37          <license>
 38              <name>Apache License, Version 2.0</name>
 39              <url>http://www.apache.org/licenses/LICENSE-2.0.html</url>
 40              <distribution>repo</distribution>
 41          </license>
 42      </licenses>
 43  
 44      <dependencies>
 45  
 46          <!-- Import the CDI API, we use provided scope as the API is included in JBoss EAP -->
 47          <dependency>
 48              <groupId>jakarta.enterprise</groupId>
 49              <artifactId>jakarta.enterprise.cdi-api</artifactId>
 50              <scope>provided</scope>
 51          </dependency>
 52  
 53          <!-- Test dependencies -->
 54          <dependency>
 55              <groupId>junit</groupId>
 56              <artifactId>junit</artifactId>
 57              <scope>test</scope>
 58          </dependency>
 59  
 60          <!-- Import the JPA API, we use provided scope as the API is included in JBoss EAP -->
 61          <dependency>
 62              <groupId>jakarta.persistence</groupId>
 63              <artifactId>jakarta.persistence-api</artifactId>
 64              <scope>provided</scope>
 65          </dependency>
 66  
 67          <dependency>
 68              <groupId>org.jboss.arquillian.junit</groupId>
 69              <artifactId>arquillian-junit-container</artifactId>
 70              <scope>test</scope>
 71          </dependency>
 72  
 73          <dependency>
 74              <groupId>org.jboss.arquillian.protocol</groupId>
 75              <artifactId>arquillian-protocol-servlet</artifactId>
 76              <scope>test</scope>
 77          </dependency>
 78  
 79          <!-- Import the EJB API, we use provided scope as the API is included in JBoss EAP -->
 80          <dependency>
 81              <groupId>org.jboss.spec.javax.ejb</groupId>
 82              <artifactId>jboss-ejb-api_3.2_spec</artifactId>
 83              <scope>provided</scope>
 84          </dependency>
 85  
 86          <!-- Import the JSF API, we use provided scope as the API is included in JBoss EAP -->
 87          <dependency>
 88              <groupId>org.jboss.spec.javax.faces</groupId>
 89              <artifactId>jboss-jsf-api_2.3_spec</artifactId>
 90              <scope>provided</scope>
 91          </dependency>
 92  
 93      </dependencies>
 94  
 95      <build>
 96          <!-- Set the name of the WAR, used as the context root when the app is deployed -->
 97          <finalName>${project.artifactId}</finalName>
 98      </build>
 99  
100  </project>

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
      * Line Number: 19
      * Message: 'Use the Maven Compiler plugin adding the following sections to the `pom.xml` file: 

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
 ```'
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
 18  <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
 19      <modelVersion>4.0.0</modelVersion>
 20      <parent>
 21          <groupId>org.jboss.eap.quickstarts</groupId>
 22          <artifactId>quickstart-parent</artifactId>
 23          <!--
 24          Maintain separation between the artifact id and the version to help prevent
 25          merge conflicts between commits changing the GA and those changing the V.
 26          -->
 27          <version>7.4.0.GA</version>
 28          <relativePath>../pom.xml</relativePath>
 29      </parent>
 30  
 31      <artifactId>tasks-jsf</artifactId>
 32      <packaging>war</packaging>
 33      <name>Quickstart: tasks-jsf</name>
 34      <description>This project demonstrates how to use JPA persistence to manage tasks with JSF as view layer</description>
 35  
 36      <licenses>
 37          <license>
 38              <name>Apache License, Version 2.0</name>
 39              <url>http://www.apache.org/licenses/LICENSE-2.0.html</url>
 40              <distribution>repo</distribution>
 41          </license>
 42      </licenses>
 43  
 44      <dependencies>
 45  
 46          <!-- Import the CDI API, we use provided scope as the API is included in JBoss EAP -->
 47          <dependency>
 48              <groupId>jakarta.enterprise</groupId>
 49              <artifactId>jakarta.enterprise.cdi-api</artifactId>
 50              <scope>provided</scope>
 51          </dependency>
 52  
 53          <!-- Test dependencies -->
 54          <dependency>
 55              <groupId>junit</groupId>
 56              <artifactId>junit</artifactId>
 57              <scope>test</scope>
 58          </dependency>
 59  
 60          <!-- Import the JPA API, we use provided scope as the API is included in JBoss EAP -->
 61          <dependency>
 62              <groupId>jakarta.persistence</groupId>
 63              <artifactId>jakarta.persistence-api</artifactId>
 64              <scope>provided</scope>
 65          </dependency>
 66  
 67          <dependency>
 68              <groupId>org.jboss.arquillian.junit</groupId>
 69              <artifactId>arquillian-junit-container</artifactId>
 70              <scope>test</scope>
 71          </dependency>
 72  
 73          <dependency>
 74              <groupId>org.jboss.arquillian.protocol</groupId>
 75              <artifactId>arquillian-protocol-servlet</artifactId>
 76              <scope>test</scope>
 77          </dependency>
 78  
 79          <!-- Import the EJB API, we use provided scope as the API is included in JBoss EAP -->
 80          <dependency>
 81              <groupId>org.jboss.spec.javax.ejb</groupId>
 82              <artifactId>jboss-ejb-api_3.2_spec</artifactId>
 83              <scope>provided</scope>
 84          </dependency>
 85  
 86          <!-- Import the JSF API, we use provided scope as the API is included in JBoss EAP -->
 87          <dependency>
 88              <groupId>org.jboss.spec.javax.faces</groupId>
 89              <artifactId>jboss-jsf-api_2.3_spec</artifactId>
 90              <scope>provided</scope>
 91          </dependency>
 92  
 93      </dependencies>
 94  
 95      <build>
 96          <!-- Set the name of the WAR, used as the context root when the app is deployed -->
 97          <finalName>${project.artifactId}</finalName>
 98      </build>
 99  
100  </project>

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
      * Line Number: 19
      * Message: 'Use the Maven Surefire plugin adding the following sections to the `pom.xml` file: 

 ```xml
 <properties> 
 <surefire-plugin.version>3.0.0</compiler-plugin.version>
 </properties> 
 <build>
 <plugins>
 <plugin>
 <artifactId>maven-surefire-plugin</artifactId>
 <version>$</version>
 <configuration>
 <systemPropertyVariables>
 <java.util.logging.manager>org.jboss.logmanager.LogManager</java.util.logging.manager>
 <maven.home>$</maven.home>
 </systemPropertyVariables>
 </configuration>
 </plugin>
 </plugins>
 </build>
 ```'
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
 18  <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
 19      <modelVersion>4.0.0</modelVersion>
 20      <parent>
 21          <groupId>org.jboss.eap.quickstarts</groupId>
 22          <artifactId>quickstart-parent</artifactId>
 23          <!--
 24          Maintain separation between the artifact id and the version to help prevent
 25          merge conflicts between commits changing the GA and those changing the V.
 26          -->
 27          <version>7.4.0.GA</version>
 28          <relativePath>../pom.xml</relativePath>
 29      </parent>
 30  
 31      <artifactId>tasks-jsf</artifactId>
 32      <packaging>war</packaging>
 33      <name>Quickstart: tasks-jsf</name>
 34      <description>This project demonstrates how to use JPA persistence to manage tasks with JSF as view layer</description>
 35  
 36      <licenses>
 37          <license>
 38              <name>Apache License, Version 2.0</name>
 39              <url>http://www.apache.org/licenses/LICENSE-2.0.html</url>
 40              <distribution>repo</distribution>
 41          </license>
 42      </licenses>
 43  
 44      <dependencies>
 45  
 46          <!-- Import the CDI API, we use provided scope as the API is included in JBoss EAP -->
 47          <dependency>
 48              <groupId>jakarta.enterprise</groupId>
 49              <artifactId>jakarta.enterprise.cdi-api</artifactId>
 50              <scope>provided</scope>
 51          </dependency>
 52  
 53          <!-- Test dependencies -->
 54          <dependency>
 55              <groupId>junit</groupId>
 56              <artifactId>junit</artifactId>
 57              <scope>test</scope>
 58          </dependency>
 59  
 60          <!-- Import the JPA API, we use provided scope as the API is included in JBoss EAP -->
 61          <dependency>
 62              <groupId>jakarta.persistence</groupId>
 63              <artifactId>jakarta.persistence-api</artifactId>
 64              <scope>provided</scope>
 65          </dependency>
 66  
 67          <dependency>
 68              <groupId>org.jboss.arquillian.junit</groupId>
 69              <artifactId>arquillian-junit-container</artifactId>
 70              <scope>test</scope>
 71          </dependency>
 72  
 73          <dependency>
 74              <groupId>org.jboss.arquillian.protocol</groupId>
 75              <artifactId>arquillian-protocol-servlet</artifactId>
 76              <scope>test</scope>
 77          </dependency>
 78  
 79          <!-- Import the EJB API, we use provided scope as the API is included in JBoss EAP -->
 80          <dependency>
 81              <groupId>org.jboss.spec.javax.ejb</groupId>
 82              <artifactId>jboss-ejb-api_3.2_spec</artifactId>
 83              <scope>provided</scope>
 84          </dependency>
 85  
 86          <!-- Import the JSF API, we use provided scope as the API is included in JBoss EAP -->
 87          <dependency>
 88              <groupId>org.jboss.spec.javax.faces</groupId>
 89              <artifactId>jboss-jsf-api_2.3_spec</artifactId>
 90              <scope>provided</scope>
 91          </dependency>
 92  
 93      </dependencies>
 94  
 95      <build>
 96          <!-- Set the name of the WAR, used as the context root when the app is deployed -->
 97          <finalName>${project.artifactId}</finalName>
 98      </build>
 99  
100  </project>

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
      * Line Number: 19
      * Message: 'Use the Maven Failsafe plugin adding the following sections to the `pom.xml` file: 

 ```xml
 <properties> 
 <surefire-plugin.version>3.0.0</compiler-plugin.version>
 </properties> 
 <build>
 <plugins>
 <plugin>
 <artifactId>maven-failsafe-plugin</artifactId>
 <version>$</version>
 <executions>
 <execution>
 <goals>
 <goals>integration-test</goal>
 <goals>verify</goal>
 </goals>
 <configuration>
 <systemPropertyVariables>
 <native.image.path>$/$-runner</native.image.path>
 <java.util.logging.manager>org.jboss.logmanager.LogManager</java.util.logging.manager>
 <maven.home>$</maven.home>
 </systemPropertyVariables>
 </configuration>
 </execution>
 </executions>
 </plugin>
 </plugins>
 </build>
 ```'
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
 18  <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
 19      <modelVersion>4.0.0</modelVersion>
 20      <parent>
 21          <groupId>org.jboss.eap.quickstarts</groupId>
 22          <artifactId>quickstart-parent</artifactId>
 23          <!--
 24          Maintain separation between the artifact id and the version to help prevent
 25          merge conflicts between commits changing the GA and those changing the V.
 26          -->
 27          <version>7.4.0.GA</version>
 28          <relativePath>../pom.xml</relativePath>
 29      </parent>
 30  
 31      <artifactId>tasks-jsf</artifactId>
 32      <packaging>war</packaging>
 33      <name>Quickstart: tasks-jsf</name>
 34      <description>This project demonstrates how to use JPA persistence to manage tasks with JSF as view layer</description>
 35  
 36      <licenses>
 37          <license>
 38              <name>Apache License, Version 2.0</name>
 39              <url>http://www.apache.org/licenses/LICENSE-2.0.html</url>
 40              <distribution>repo</distribution>
 41          </license>
 42      </licenses>
 43  
 44      <dependencies>
 45  
 46          <!-- Import the CDI API, we use provided scope as the API is included in JBoss EAP -->
 47          <dependency>
 48              <groupId>jakarta.enterprise</groupId>
 49              <artifactId>jakarta.enterprise.cdi-api</artifactId>
 50              <scope>provided</scope>
 51          </dependency>
 52  
 53          <!-- Test dependencies -->
 54          <dependency>
 55              <groupId>junit</groupId>
 56              <artifactId>junit</artifactId>
 57              <scope>test</scope>
 58          </dependency>
 59  
 60          <!-- Import the JPA API, we use provided scope as the API is included in JBoss EAP -->
 61          <dependency>
 62              <groupId>jakarta.persistence</groupId>
 63              <artifactId>jakarta.persistence-api</artifactId>
 64              <scope>provided</scope>
 65          </dependency>
 66  
 67          <dependency>
 68              <groupId>org.jboss.arquillian.junit</groupId>
 69              <artifactId>arquillian-junit-container</artifactId>
 70              <scope>test</scope>
 71          </dependency>
 72  
 73          <dependency>
 74              <groupId>org.jboss.arquillian.protocol</groupId>
 75              <artifactId>arquillian-protocol-servlet</artifactId>
 76              <scope>test</scope>
 77          </dependency>
 78  
 79          <!-- Import the EJB API, we use provided scope as the API is included in JBoss EAP -->
 80          <dependency>
 81              <groupId>org.jboss.spec.javax.ejb</groupId>
 82              <artifactId>jboss-ejb-api_3.2_spec</artifactId>
 83              <scope>provided</scope>
 84          </dependency>
 85  
 86          <!-- Import the JSF API, we use provided scope as the API is included in JBoss EAP -->
 87          <dependency>
 88              <groupId>org.jboss.spec.javax.faces</groupId>
 89              <artifactId>jboss-jsf-api_2.3_spec</artifactId>
 90              <scope>provided</scope>
 91          </dependency>
 92  
 93      </dependencies>
 94  
 95      <build>
 96          <!-- Set the name of the WAR, used as the context root when the app is deployed -->
 97          <finalName>${project.artifactId}</finalName>
 98      </build>
 99  
100  </project>

```
### #8 - javaee-pom-to-quarkus-00060
* Category: mandatory
* Effort: 1
* Description: Add Maven profile to run the Quarkus native build
* Labels: konveyor.io/source=java-ee, konveyor.io/target=quarkus
* Links
  * Quarkus - Guide: https://quarkus.io/guides/maven-tooling#build-tool-maven
* Incidents
  * file:///tmp/source-code/pom.xml
      * Line Number: 19
      * Message: 'Leverage a Maven profile to run the Quarkus native build adding the following section to the `pom.xml` file: 

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
 ```'
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
 18  <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
 19      <modelVersion>4.0.0</modelVersion>
 20      <parent>
 21          <groupId>org.jboss.eap.quickstarts</groupId>
 22          <artifactId>quickstart-parent</artifactId>
 23          <!--
 24          Maintain separation between the artifact id and the version to help prevent
 25          merge conflicts between commits changing the GA and those changing the V.
 26          -->
 27          <version>7.4.0.GA</version>
 28          <relativePath>../pom.xml</relativePath>
 29      </parent>
 30  
 31      <artifactId>tasks-jsf</artifactId>
 32      <packaging>war</packaging>
 33      <name>Quickstart: tasks-jsf</name>
 34      <description>This project demonstrates how to use JPA persistence to manage tasks with JSF as view layer</description>
 35  
 36      <licenses>
 37          <license>
 38              <name>Apache License, Version 2.0</name>
 39              <url>http://www.apache.org/licenses/LICENSE-2.0.html</url>
 40              <distribution>repo</distribution>
 41          </license>
 42      </licenses>
 43  
 44      <dependencies>
 45  
 46          <!-- Import the CDI API, we use provided scope as the API is included in JBoss EAP -->
 47          <dependency>
 48              <groupId>jakarta.enterprise</groupId>
 49              <artifactId>jakarta.enterprise.cdi-api</artifactId>
 50              <scope>provided</scope>
 51          </dependency>
 52  
 53          <!-- Test dependencies -->
 54          <dependency>
 55              <groupId>junit</groupId>
 56              <artifactId>junit</artifactId>
 57              <scope>test</scope>
 58          </dependency>
 59  
 60          <!-- Import the JPA API, we use provided scope as the API is included in JBoss EAP -->
 61          <dependency>
 62              <groupId>jakarta.persistence</groupId>
 63              <artifactId>jakarta.persistence-api</artifactId>
 64              <scope>provided</scope>
 65          </dependency>
 66  
 67          <dependency>
 68              <groupId>org.jboss.arquillian.junit</groupId>
 69              <artifactId>arquillian-junit-container</artifactId>
 70              <scope>test</scope>
 71          </dependency>
 72  
 73          <dependency>
 74              <groupId>org.jboss.arquillian.protocol</groupId>
 75              <artifactId>arquillian-protocol-servlet</artifactId>
 76              <scope>test</scope>
 77          </dependency>
 78  
 79          <!-- Import the EJB API, we use provided scope as the API is included in JBoss EAP -->
 80          <dependency>
 81              <groupId>org.jboss.spec.javax.ejb</groupId>
 82              <artifactId>jboss-ejb-api_3.2_spec</artifactId>
 83              <scope>provided</scope>
 84          </dependency>
 85  
 86          <!-- Import the JSF API, we use provided scope as the API is included in JBoss EAP -->
 87          <dependency>
 88              <groupId>org.jboss.spec.javax.faces</groupId>
 89              <artifactId>jboss-jsf-api_2.3_spec</artifactId>
 90              <scope>provided</scope>
 91          </dependency>
 92  
 93      </dependencies>
 94  
 95      <build>
 96          <!-- Set the name of the WAR, used as the context root when the app is deployed -->
 97          <finalName>${project.artifactId}</finalName>
 98      </build>
 99  
100  </project>

```
### #9 - javaee-pom-to-quarkus-00070
* Category: mandatory
* Effort: 1
* Description: Configure Quarkus hibernate-orm
* Labels: konveyor.io/source=java-ee, konveyor.io/target=quarkus
* Links
  * Using hibernate-orm and jakarta persistence: https://quarkus.io/guides/hibernate-orm
* Incidents
  * file:///tmp/source-code/pom.xml
      * Line Number: 62
      * Message: 'Configure Quarkus 'hibernate-orm` and jakarta persistence. 
 Add the `quarkus-hibernate-orm` section and one for your preferred jdbc solution to the `pom.xml` file, eg for postgres: 

 ```
 <!-- Hibernate ORM specific dependencies -->
 <dependency>
 <groupId>io.quarkus</groupId>
 <artifactId>quarkus-hibernate-orm</artifactId>
 </dependency>
 
 <!-- JDBC driver dependencies -->
 <dependency>
 <groupId>io.quarkus</groupId>
 <artifactId>quarkus-jdbc-postgresql</artifactId>
 </dependency> 
 ```'
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
 18  <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
 19      <modelVersion>4.0.0</modelVersion>
 20      <parent>
 21          <groupId>org.jboss.eap.quickstarts</groupId>
 22          <artifactId>quickstart-parent</artifactId>
 23          <!--
 24          Maintain separation between the artifact id and the version to help prevent
 25          merge conflicts between commits changing the GA and those changing the V.
 26          -->
 27          <version>7.4.0.GA</version>
 28          <relativePath>../pom.xml</relativePath>
 29      </parent>
 30  
 31      <artifactId>tasks-jsf</artifactId>
 32      <packaging>war</packaging>
 33      <name>Quickstart: tasks-jsf</name>
 34      <description>This project demonstrates how to use JPA persistence to manage tasks with JSF as view layer</description>
 35  
 36      <licenses>
 37          <license>
 38              <name>Apache License, Version 2.0</name>
 39              <url>http://www.apache.org/licenses/LICENSE-2.0.html</url>
 40              <distribution>repo</distribution>
 41          </license>
 42      </licenses>
 43  
 44      <dependencies>
 45  
 46          <!-- Import the CDI API, we use provided scope as the API is included in JBoss EAP -->
 47          <dependency>
 48              <groupId>jakarta.enterprise</groupId>
 49              <artifactId>jakarta.enterprise.cdi-api</artifactId>
 50              <scope>provided</scope>
 51          </dependency>
 52  
 53          <!-- Test dependencies -->
 54          <dependency>
 55              <groupId>junit</groupId>
 56              <artifactId>junit</artifactId>
 57              <scope>test</scope>
 58          </dependency>
 59  
 60          <!-- Import the JPA API, we use provided scope as the API is included in JBoss EAP -->
 61          <dependency>
 62              <groupId>jakarta.persistence</groupId>
 63              <artifactId>jakarta.persistence-api</artifactId>
 64              <scope>provided</scope>
 65          </dependency>
 66  
 67          <dependency>
 68              <groupId>org.jboss.arquillian.junit</groupId>
 69              <artifactId>arquillian-junit-container</artifactId>
 70              <scope>test</scope>
 71          </dependency>
 72  
 73          <dependency>
 74              <groupId>org.jboss.arquillian.protocol</groupId>
 75              <artifactId>arquillian-protocol-servlet</artifactId>
 76              <scope>test</scope>
 77          </dependency>
 78  
 79          <!-- Import the EJB API, we use provided scope as the API is included in JBoss EAP -->
 80          <dependency>
 81              <groupId>org.jboss.spec.javax.ejb</groupId>
 82              <artifactId>jboss-ejb-api_3.2_spec</artifactId>
 83              <scope>provided</scope>
 84          </dependency>
 85  
 86          <!-- Import the JSF API, we use provided scope as the API is included in JBoss EAP -->
 87          <dependency>
 88              <groupId>org.jboss.spec.javax.faces</groupId>
 89              <artifactId>jboss-jsf-api_2.3_spec</artifactId>
 90              <scope>provided</scope>
 91          </dependency>
 92  
 93      </dependencies>
 94  
 95      <build>
 96          <!-- Set the name of the WAR, used as the context root when the app is deployed -->
 97          <finalName>${project.artifactId}</finalName>
 98      </build>
 99  
100  </project>

```
