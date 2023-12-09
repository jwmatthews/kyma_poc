# eap8/eap7
## Description
This ruleset provides analysis of Java EE applications that need to change certain CDI-related method calls.
* Source of rules: https://github.com/konveyor/rulesets/tree/main/default/generated
## Violations
Number of Violations: 3
### #0 - javaee-to-jakarta-namespaces-00001
* Category: mandatory
* Effort: 1
* Description: Replace the Java EE namespace, schemaLocation and version with the Jakarta equivalent
* Labels: konveyor.io/source, konveyor.io/target=eap, konveyor.io/target=eap8, konveyor.io/target=jakarta-ee, konveyor.io/target=jakarta-ee9+
* Links
  * Jakarta EE XML Schemas: https://jakarta.ee/xml/ns/jakartaee/#10
* Incidents
  * file:///tmp/source-code/src/main/webapp/WEB-INF/beans.xml
      * Replace `http://xmlns.jcp.org/xml/ns/javaee` with `https://jakarta.ee/xml/ns/jakartaee` and change the schema version number 
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
 24  </beans>

```
  * file:///tmp/source-code/src/main/webapp/WEB-INF/beans.xml
      * Replace `http://xmlns.jcp.org/xml/ns/javaee` with `https://jakarta.ee/xml/ns/jakartaee` and change the schema version number 
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
 24  </beans>

```
  * file:///tmp/source-code/src/main/webapp/WEB-INF/beans.xml
      * Replace `http://xmlns.jcp.org/xml/ns/javaee` with `https://jakarta.ee/xml/ns/jakartaee` and change the schema version number 
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
 24  </beans>

```
### #1 - javaee-to-jakarta-namespaces-00006
* Category: mandatory
* Effort: 1
* Description: Replace the Java EE XSD with the Jakarta equivalent
* Labels: konveyor.io/source, konveyor.io/target=eap, konveyor.io/target=eap8, konveyor.io/target=jakarta-ee, konveyor.io/target=jakarta-ee9+
* Links
  * Jakarta XML Schemas: https://jakarta.ee/xml/ns/jakartaee/#9
* Incidents
  * file:///tmp/source-code/src/main/webapp/WEB-INF/beans.xml
      * Replace `beans_1_1.xsd` with `beans_3_0.xsd` and update the version attribute to `"3.0"`
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
 24  </beans>

```
### #2 - javax-to-jakarta-import-00001
* Category: mandatory
* Effort: 1
* Description: javax.{renamed} has been replaced by jakarta.{renamed}
* Labels: konveyor.io/source, konveyor.io/target=eap, konveyor.io/target=eap8, konveyor.io/target=jakarta-ee, konveyor.io/target=jakarta-ee9+
* Incidents
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/mdb/HelloWorldQueueMDB.java
      * Replace the `javax.ejb` import statement with `jakarta.ejb` 
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
 17  package org.jboss.as.quickstarts.mdb;
 18  
 19  import java.util.logging.Logger;
 20  import javax.ejb.ActivationConfigProperty;
 21  import javax.ejb.MessageDriven;
 22  import javax.jms.JMSException;
 23  import javax.jms.Message;
 24  import javax.jms.MessageListener;
 25  import javax.jms.TextMessage;
 26  
 27  /**
 28   * <p>
 29   * A simple Message Driven Bean that asynchronously receives and processes the messages that are sent to the queue.
 30   * </p>
 31   *
 32   * @author Serge Pagop (spagop@redhat.com)
 33   */
 34  @MessageDriven(name = "HelloWorldQueueMDB", activationConfig = {
 35          @ActivationConfigProperty(propertyName = "destinationLookup", propertyValue = "queue/HELLOWORLDMDBQueue"),
 36          @ActivationConfigProperty(propertyName = "destinationType", propertyValue = "javax.jms.Queue"),
 37          @ActivationConfigProperty(propertyName = "acknowledgeMode", propertyValue = "Auto-acknowledge")})
 38  public class HelloWorldQueueMDB implements MessageListener {
 39  
 40      private static final Logger LOGGER = Logger.getLogger(HelloWorldQueueMDB.class.toString());
 41  
 42      /**
 43       * @see MessageListener#onMessage(Message)
 44       */
 45      public void onMessage(Message rcvMessage) {
 46          TextMessage msg = null;
 47          try {
 48              if (rcvMessage instanceof TextMessage) {
 49                  msg = (TextMessage) rcvMessage;
 50                  LOGGER.info("Received Message from queue: " + msg.getText());
 51              } else {
 52                  LOGGER.warning("Message of wrong type: " + rcvMessage.getClass().getName());
 53              }
 54          } catch (JMSException e) {
 55              throw new RuntimeException(e);
 56          }
 57      }
 58  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/mdb/HelloWorldQueueMDB.java
      * Replace the `javax.ejb` import statement with `jakarta.ejb` 
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
 17  package org.jboss.as.quickstarts.mdb;
 18  
 19  import java.util.logging.Logger;
 20  import javax.ejb.ActivationConfigProperty;
 21  import javax.ejb.MessageDriven;
 22  import javax.jms.JMSException;
 23  import javax.jms.Message;
 24  import javax.jms.MessageListener;
 25  import javax.jms.TextMessage;
 26  
 27  /**
 28   * <p>
 29   * A simple Message Driven Bean that asynchronously receives and processes the messages that are sent to the queue.
 30   * </p>
 31   *
 32   * @author Serge Pagop (spagop@redhat.com)
 33   */
 34  @MessageDriven(name = "HelloWorldQueueMDB", activationConfig = {
 35          @ActivationConfigProperty(propertyName = "destinationLookup", propertyValue = "queue/HELLOWORLDMDBQueue"),
 36          @ActivationConfigProperty(propertyName = "destinationType", propertyValue = "javax.jms.Queue"),
 37          @ActivationConfigProperty(propertyName = "acknowledgeMode", propertyValue = "Auto-acknowledge")})
 38  public class HelloWorldQueueMDB implements MessageListener {
 39  
 40      private static final Logger LOGGER = Logger.getLogger(HelloWorldQueueMDB.class.toString());
 41  
 42      /**
 43       * @see MessageListener#onMessage(Message)
 44       */
 45      public void onMessage(Message rcvMessage) {
 46          TextMessage msg = null;
 47          try {
 48              if (rcvMessage instanceof TextMessage) {
 49                  msg = (TextMessage) rcvMessage;
 50                  LOGGER.info("Received Message from queue: " + msg.getText());
 51              } else {
 52                  LOGGER.warning("Message of wrong type: " + rcvMessage.getClass().getName());
 53              }
 54          } catch (JMSException e) {
 55              throw new RuntimeException(e);
 56          }
 57      }
 58  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/mdb/HelloWorldQueueMDB.java
      * Replace the `javax.jms` import statement with `jakarta.jms` 
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
 17  package org.jboss.as.quickstarts.mdb;
 18  
 19  import java.util.logging.Logger;
 20  import javax.ejb.ActivationConfigProperty;
 21  import javax.ejb.MessageDriven;
 22  import javax.jms.JMSException;
 23  import javax.jms.Message;
 24  import javax.jms.MessageListener;
 25  import javax.jms.TextMessage;
 26  
 27  /**
 28   * <p>
 29   * A simple Message Driven Bean that asynchronously receives and processes the messages that are sent to the queue.
 30   * </p>
 31   *
 32   * @author Serge Pagop (spagop@redhat.com)
 33   */
 34  @MessageDriven(name = "HelloWorldQueueMDB", activationConfig = {
 35          @ActivationConfigProperty(propertyName = "destinationLookup", propertyValue = "queue/HELLOWORLDMDBQueue"),
 36          @ActivationConfigProperty(propertyName = "destinationType", propertyValue = "javax.jms.Queue"),
 37          @ActivationConfigProperty(propertyName = "acknowledgeMode", propertyValue = "Auto-acknowledge")})
 38  public class HelloWorldQueueMDB implements MessageListener {
 39  
 40      private static final Logger LOGGER = Logger.getLogger(HelloWorldQueueMDB.class.toString());
 41  
 42      /**
 43       * @see MessageListener#onMessage(Message)
 44       */
 45      public void onMessage(Message rcvMessage) {
 46          TextMessage msg = null;
 47          try {
 48              if (rcvMessage instanceof TextMessage) {
 49                  msg = (TextMessage) rcvMessage;
 50                  LOGGER.info("Received Message from queue: " + msg.getText());
 51              } else {
 52                  LOGGER.warning("Message of wrong type: " + rcvMessage.getClass().getName());
 53              }
 54          } catch (JMSException e) {
 55              throw new RuntimeException(e);
 56          }
 57      }
 58  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/mdb/HelloWorldQueueMDB.java
      * Replace the `javax.jms` import statement with `jakarta.jms` 
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
 17  package org.jboss.as.quickstarts.mdb;
 18  
 19  import java.util.logging.Logger;
 20  import javax.ejb.ActivationConfigProperty;
 21  import javax.ejb.MessageDriven;
 22  import javax.jms.JMSException;
 23  import javax.jms.Message;
 24  import javax.jms.MessageListener;
 25  import javax.jms.TextMessage;
 26  
 27  /**
 28   * <p>
 29   * A simple Message Driven Bean that asynchronously receives and processes the messages that are sent to the queue.
 30   * </p>
 31   *
 32   * @author Serge Pagop (spagop@redhat.com)
 33   */
 34  @MessageDriven(name = "HelloWorldQueueMDB", activationConfig = {
 35          @ActivationConfigProperty(propertyName = "destinationLookup", propertyValue = "queue/HELLOWORLDMDBQueue"),
 36          @ActivationConfigProperty(propertyName = "destinationType", propertyValue = "javax.jms.Queue"),
 37          @ActivationConfigProperty(propertyName = "acknowledgeMode", propertyValue = "Auto-acknowledge")})
 38  public class HelloWorldQueueMDB implements MessageListener {
 39  
 40      private static final Logger LOGGER = Logger.getLogger(HelloWorldQueueMDB.class.toString());
 41  
 42      /**
 43       * @see MessageListener#onMessage(Message)
 44       */
 45      public void onMessage(Message rcvMessage) {
 46          TextMessage msg = null;
 47          try {
 48              if (rcvMessage instanceof TextMessage) {
 49                  msg = (TextMessage) rcvMessage;
 50                  LOGGER.info("Received Message from queue: " + msg.getText());
 51              } else {
 52                  LOGGER.warning("Message of wrong type: " + rcvMessage.getClass().getName());
 53              }
 54          } catch (JMSException e) {
 55              throw new RuntimeException(e);
 56          }
 57      }
 58  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/mdb/HelloWorldQueueMDB.java
      * Replace the `javax.jms` import statement with `jakarta.jms` 
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
 17  package org.jboss.as.quickstarts.mdb;
 18  
 19  import java.util.logging.Logger;
 20  import javax.ejb.ActivationConfigProperty;
 21  import javax.ejb.MessageDriven;
 22  import javax.jms.JMSException;
 23  import javax.jms.Message;
 24  import javax.jms.MessageListener;
 25  import javax.jms.TextMessage;
 26  
 27  /**
 28   * <p>
 29   * A simple Message Driven Bean that asynchronously receives and processes the messages that are sent to the queue.
 30   * </p>
 31   *
 32   * @author Serge Pagop (spagop@redhat.com)
 33   */
 34  @MessageDriven(name = "HelloWorldQueueMDB", activationConfig = {
 35          @ActivationConfigProperty(propertyName = "destinationLookup", propertyValue = "queue/HELLOWORLDMDBQueue"),
 36          @ActivationConfigProperty(propertyName = "destinationType", propertyValue = "javax.jms.Queue"),
 37          @ActivationConfigProperty(propertyName = "acknowledgeMode", propertyValue = "Auto-acknowledge")})
 38  public class HelloWorldQueueMDB implements MessageListener {
 39  
 40      private static final Logger LOGGER = Logger.getLogger(HelloWorldQueueMDB.class.toString());
 41  
 42      /**
 43       * @see MessageListener#onMessage(Message)
 44       */
 45      public void onMessage(Message rcvMessage) {
 46          TextMessage msg = null;
 47          try {
 48              if (rcvMessage instanceof TextMessage) {
 49                  msg = (TextMessage) rcvMessage;
 50                  LOGGER.info("Received Message from queue: " + msg.getText());
 51              } else {
 52                  LOGGER.warning("Message of wrong type: " + rcvMessage.getClass().getName());
 53              }
 54          } catch (JMSException e) {
 55              throw new RuntimeException(e);
 56          }
 57      }
 58  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/mdb/HelloWorldQueueMDB.java
      * Replace the `javax.jms` import statement with `jakarta.jms` 
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
 17  package org.jboss.as.quickstarts.mdb;
 18  
 19  import java.util.logging.Logger;
 20  import javax.ejb.ActivationConfigProperty;
 21  import javax.ejb.MessageDriven;
 22  import javax.jms.JMSException;
 23  import javax.jms.Message;
 24  import javax.jms.MessageListener;
 25  import javax.jms.TextMessage;
 26  
 27  /**
 28   * <p>
 29   * A simple Message Driven Bean that asynchronously receives and processes the messages that are sent to the queue.
 30   * </p>
 31   *
 32   * @author Serge Pagop (spagop@redhat.com)
 33   */
 34  @MessageDriven(name = "HelloWorldQueueMDB", activationConfig = {
 35          @ActivationConfigProperty(propertyName = "destinationLookup", propertyValue = "queue/HELLOWORLDMDBQueue"),
 36          @ActivationConfigProperty(propertyName = "destinationType", propertyValue = "javax.jms.Queue"),
 37          @ActivationConfigProperty(propertyName = "acknowledgeMode", propertyValue = "Auto-acknowledge")})
 38  public class HelloWorldQueueMDB implements MessageListener {
 39  
 40      private static final Logger LOGGER = Logger.getLogger(HelloWorldQueueMDB.class.toString());
 41  
 42      /**
 43       * @see MessageListener#onMessage(Message)
 44       */
 45      public void onMessage(Message rcvMessage) {
 46          TextMessage msg = null;
 47          try {
 48              if (rcvMessage instanceof TextMessage) {
 49                  msg = (TextMessage) rcvMessage;
 50                  LOGGER.info("Received Message from queue: " + msg.getText());
 51              } else {
 52                  LOGGER.warning("Message of wrong type: " + rcvMessage.getClass().getName());
 53              }
 54          } catch (JMSException e) {
 55              throw new RuntimeException(e);
 56          }
 57      }
 58  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/mdb/HelloWorldTopicMDB.java
      * Replace the `javax.ejb` import statement with `jakarta.ejb` 
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
 17  package org.jboss.as.quickstarts.mdb;
 18  
 19  import java.util.logging.Logger;
 20  import javax.ejb.ActivationConfigProperty;
 21  import javax.ejb.MessageDriven;
 22  import javax.jms.JMSException;
 23  import javax.jms.Message;
 24  import javax.jms.MessageListener;
 25  import javax.jms.TextMessage;
 26  
 27  /**
 28   * <p>
 29   * A simple Message Driven Bean that asynchronously receives and processes the messages that are sent to the topic.
 30   * </p>
 31   *
 32   * @author Serge Pagop (spagop@redhat.com)
 33   */
 34  @MessageDriven(name = "HelloWorldQTopicMDB", activationConfig = {
 35          @ActivationConfigProperty(propertyName = "destinationLookup", propertyValue = "topic/HELLOWORLDMDBTopic"),
 36          @ActivationConfigProperty(propertyName = "destinationType", propertyValue = "javax.jms.Topic"),
 37          @ActivationConfigProperty(propertyName = "acknowledgeMode", propertyValue = "Auto-acknowledge")})
 38  public class HelloWorldTopicMDB implements MessageListener {
 39  
 40      private static final Logger LOGGER = Logger.getLogger(HelloWorldTopicMDB.class.toString());
 41  
 42      /**
 43       * @see MessageListener#onMessage(Message)
 44       */
 45      public void onMessage(Message rcvMessage) {
 46          TextMessage msg = null;
 47          try {
 48              if (rcvMessage instanceof TextMessage) {
 49                  msg = (TextMessage) rcvMessage;
 50                  LOGGER.info("Received Message from topic: " + msg.getText());
 51              } else {
 52                  LOGGER.warning("Message of wrong type: " + rcvMessage.getClass().getName());
 53              }
 54          } catch (JMSException e) {
 55              throw new RuntimeException(e);
 56          }
 57      }
 58  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/mdb/HelloWorldTopicMDB.java
      * Replace the `javax.ejb` import statement with `jakarta.ejb` 
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
 17  package org.jboss.as.quickstarts.mdb;
 18  
 19  import java.util.logging.Logger;
 20  import javax.ejb.ActivationConfigProperty;
 21  import javax.ejb.MessageDriven;
 22  import javax.jms.JMSException;
 23  import javax.jms.Message;
 24  import javax.jms.MessageListener;
 25  import javax.jms.TextMessage;
 26  
 27  /**
 28   * <p>
 29   * A simple Message Driven Bean that asynchronously receives and processes the messages that are sent to the topic.
 30   * </p>
 31   *
 32   * @author Serge Pagop (spagop@redhat.com)
 33   */
 34  @MessageDriven(name = "HelloWorldQTopicMDB", activationConfig = {
 35          @ActivationConfigProperty(propertyName = "destinationLookup", propertyValue = "topic/HELLOWORLDMDBTopic"),
 36          @ActivationConfigProperty(propertyName = "destinationType", propertyValue = "javax.jms.Topic"),
 37          @ActivationConfigProperty(propertyName = "acknowledgeMode", propertyValue = "Auto-acknowledge")})
 38  public class HelloWorldTopicMDB implements MessageListener {
 39  
 40      private static final Logger LOGGER = Logger.getLogger(HelloWorldTopicMDB.class.toString());
 41  
 42      /**
 43       * @see MessageListener#onMessage(Message)
 44       */
 45      public void onMessage(Message rcvMessage) {
 46          TextMessage msg = null;
 47          try {
 48              if (rcvMessage instanceof TextMessage) {
 49                  msg = (TextMessage) rcvMessage;
 50                  LOGGER.info("Received Message from topic: " + msg.getText());
 51              } else {
 52                  LOGGER.warning("Message of wrong type: " + rcvMessage.getClass().getName());
 53              }
 54          } catch (JMSException e) {
 55              throw new RuntimeException(e);
 56          }
 57      }
 58  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/mdb/HelloWorldTopicMDB.java
      * Replace the `javax.jms` import statement with `jakarta.jms` 
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
 17  package org.jboss.as.quickstarts.mdb;
 18  
 19  import java.util.logging.Logger;
 20  import javax.ejb.ActivationConfigProperty;
 21  import javax.ejb.MessageDriven;
 22  import javax.jms.JMSException;
 23  import javax.jms.Message;
 24  import javax.jms.MessageListener;
 25  import javax.jms.TextMessage;
 26  
 27  /**
 28   * <p>
 29   * A simple Message Driven Bean that asynchronously receives and processes the messages that are sent to the topic.
 30   * </p>
 31   *
 32   * @author Serge Pagop (spagop@redhat.com)
 33   */
 34  @MessageDriven(name = "HelloWorldQTopicMDB", activationConfig = {
 35          @ActivationConfigProperty(propertyName = "destinationLookup", propertyValue = "topic/HELLOWORLDMDBTopic"),
 36          @ActivationConfigProperty(propertyName = "destinationType", propertyValue = "javax.jms.Topic"),
 37          @ActivationConfigProperty(propertyName = "acknowledgeMode", propertyValue = "Auto-acknowledge")})
 38  public class HelloWorldTopicMDB implements MessageListener {
 39  
 40      private static final Logger LOGGER = Logger.getLogger(HelloWorldTopicMDB.class.toString());
 41  
 42      /**
 43       * @see MessageListener#onMessage(Message)
 44       */
 45      public void onMessage(Message rcvMessage) {
 46          TextMessage msg = null;
 47          try {
 48              if (rcvMessage instanceof TextMessage) {
 49                  msg = (TextMessage) rcvMessage;
 50                  LOGGER.info("Received Message from topic: " + msg.getText());
 51              } else {
 52                  LOGGER.warning("Message of wrong type: " + rcvMessage.getClass().getName());
 53              }
 54          } catch (JMSException e) {
 55              throw new RuntimeException(e);
 56          }
 57      }
 58  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/mdb/HelloWorldTopicMDB.java
      * Replace the `javax.jms` import statement with `jakarta.jms` 
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
 17  package org.jboss.as.quickstarts.mdb;
 18  
 19  import java.util.logging.Logger;
 20  import javax.ejb.ActivationConfigProperty;
 21  import javax.ejb.MessageDriven;
 22  import javax.jms.JMSException;
 23  import javax.jms.Message;
 24  import javax.jms.MessageListener;
 25  import javax.jms.TextMessage;
 26  
 27  /**
 28   * <p>
 29   * A simple Message Driven Bean that asynchronously receives and processes the messages that are sent to the topic.
 30   * </p>
 31   *
 32   * @author Serge Pagop (spagop@redhat.com)
 33   */
 34  @MessageDriven(name = "HelloWorldQTopicMDB", activationConfig = {
 35          @ActivationConfigProperty(propertyName = "destinationLookup", propertyValue = "topic/HELLOWORLDMDBTopic"),
 36          @ActivationConfigProperty(propertyName = "destinationType", propertyValue = "javax.jms.Topic"),
 37          @ActivationConfigProperty(propertyName = "acknowledgeMode", propertyValue = "Auto-acknowledge")})
 38  public class HelloWorldTopicMDB implements MessageListener {
 39  
 40      private static final Logger LOGGER = Logger.getLogger(HelloWorldTopicMDB.class.toString());
 41  
 42      /**
 43       * @see MessageListener#onMessage(Message)
 44       */
 45      public void onMessage(Message rcvMessage) {
 46          TextMessage msg = null;
 47          try {
 48              if (rcvMessage instanceof TextMessage) {
 49                  msg = (TextMessage) rcvMessage;
 50                  LOGGER.info("Received Message from topic: " + msg.getText());
 51              } else {
 52                  LOGGER.warning("Message of wrong type: " + rcvMessage.getClass().getName());
 53              }
 54          } catch (JMSException e) {
 55              throw new RuntimeException(e);
 56          }
 57      }
 58  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/mdb/HelloWorldTopicMDB.java
      * Replace the `javax.jms` import statement with `jakarta.jms` 
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
 17  package org.jboss.as.quickstarts.mdb;
 18  
 19  import java.util.logging.Logger;
 20  import javax.ejb.ActivationConfigProperty;
 21  import javax.ejb.MessageDriven;
 22  import javax.jms.JMSException;
 23  import javax.jms.Message;
 24  import javax.jms.MessageListener;
 25  import javax.jms.TextMessage;
 26  
 27  /**
 28   * <p>
 29   * A simple Message Driven Bean that asynchronously receives and processes the messages that are sent to the topic.
 30   * </p>
 31   *
 32   * @author Serge Pagop (spagop@redhat.com)
 33   */
 34  @MessageDriven(name = "HelloWorldQTopicMDB", activationConfig = {
 35          @ActivationConfigProperty(propertyName = "destinationLookup", propertyValue = "topic/HELLOWORLDMDBTopic"),
 36          @ActivationConfigProperty(propertyName = "destinationType", propertyValue = "javax.jms.Topic"),
 37          @ActivationConfigProperty(propertyName = "acknowledgeMode", propertyValue = "Auto-acknowledge")})
 38  public class HelloWorldTopicMDB implements MessageListener {
 39  
 40      private static final Logger LOGGER = Logger.getLogger(HelloWorldTopicMDB.class.toString());
 41  
 42      /**
 43       * @see MessageListener#onMessage(Message)
 44       */
 45      public void onMessage(Message rcvMessage) {
 46          TextMessage msg = null;
 47          try {
 48              if (rcvMessage instanceof TextMessage) {
 49                  msg = (TextMessage) rcvMessage;
 50                  LOGGER.info("Received Message from topic: " + msg.getText());
 51              } else {
 52                  LOGGER.warning("Message of wrong type: " + rcvMessage.getClass().getName());
 53              }
 54          } catch (JMSException e) {
 55              throw new RuntimeException(e);
 56          }
 57      }
 58  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/mdb/HelloWorldTopicMDB.java
      * Replace the `javax.jms` import statement with `jakarta.jms` 
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
 17  package org.jboss.as.quickstarts.mdb;
 18  
 19  import java.util.logging.Logger;
 20  import javax.ejb.ActivationConfigProperty;
 21  import javax.ejb.MessageDriven;
 22  import javax.jms.JMSException;
 23  import javax.jms.Message;
 24  import javax.jms.MessageListener;
 25  import javax.jms.TextMessage;
 26  
 27  /**
 28   * <p>
 29   * A simple Message Driven Bean that asynchronously receives and processes the messages that are sent to the topic.
 30   * </p>
 31   *
 32   * @author Serge Pagop (spagop@redhat.com)
 33   */
 34  @MessageDriven(name = "HelloWorldQTopicMDB", activationConfig = {
 35          @ActivationConfigProperty(propertyName = "destinationLookup", propertyValue = "topic/HELLOWORLDMDBTopic"),
 36          @ActivationConfigProperty(propertyName = "destinationType", propertyValue = "javax.jms.Topic"),
 37          @ActivationConfigProperty(propertyName = "acknowledgeMode", propertyValue = "Auto-acknowledge")})
 38  public class HelloWorldTopicMDB implements MessageListener {
 39  
 40      private static final Logger LOGGER = Logger.getLogger(HelloWorldTopicMDB.class.toString());
 41  
 42      /**
 43       * @see MessageListener#onMessage(Message)
 44       */
 45      public void onMessage(Message rcvMessage) {
 46          TextMessage msg = null;
 47          try {
 48              if (rcvMessage instanceof TextMessage) {
 49                  msg = (TextMessage) rcvMessage;
 50                  LOGGER.info("Received Message from topic: " + msg.getText());
 51              } else {
 52                  LOGGER.warning("Message of wrong type: " + rcvMessage.getClass().getName());
 53              }
 54          } catch (JMSException e) {
 55              throw new RuntimeException(e);
 56          }
 57      }
 58  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/servlet/HelloWorldMDBServletClient.java
      * Replace the `javax.annotation` import statement with `jakarta.annotation` 
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
 17  package org.jboss.as.quickstarts.servlet;
 18  
 19  import java.io.IOException;
 20  import java.io.PrintWriter;
 21  
 22  import javax.annotation.Resource;
 23  import javax.inject.Inject;
 24  import javax.jms.Destination;
 25  import javax.jms.JMSContext;
 26  import javax.jms.JMSDestinationDefinition;
 27  import javax.jms.JMSDestinationDefinitions;
 28  import javax.jms.Queue;
 29  import javax.jms.Topic;
 30  import javax.servlet.ServletException;
 31  import javax.servlet.annotation.WebServlet;
 32  import javax.servlet.http.HttpServlet;
 33  import javax.servlet.http.HttpServletRequest;
 34  import javax.servlet.http.HttpServletResponse;
 35  
 36  /**
 37   * Definition of the two JMS destinations used by the quickstart
 38   * (one queue and one topic).
 39   */
 40  @JMSDestinationDefinitions(
 41      value = {
 42          @JMSDestinationDefinition(
 43              name = "java:/queue/HELLOWORLDMDBQueue",
 44              interfaceName = "javax.jms.Queue",
 45              destinationName = "HelloWorldMDBQueue"
 46          ),
 47          @JMSDestinationDefinition(
 48              name = "java:/topic/HELLOWORLDMDBTopic",
 49              interfaceName = "javax.jms.Topic",
 50              destinationName = "HelloWorldMDBTopic"
 51          )
 52      }
 53  )
 54  
 55  /**
 56   * <p>
 57   * A simple servlet 3 as client that sends several messages to a queue or a topic.
 58   * </p>
 59   *
 60   * <p>
 61   * The servlet is registered and mapped to /HelloWorldMDBServletClient using the {@linkplain WebServlet
 62   * @HttpServlet}.
 63   * </p>
 64   *
 65   * @author Serge Pagop (spagop@redhat.com)
 66   *
 67   */
 68  @WebServlet("/HelloWorldMDBServletClient")
 69  public class HelloWorldMDBServletClient extends HttpServlet {
 70  
 71      private static final long serialVersionUID = -8314035702649252239L;
 72  
 73      private static final int MSG_COUNT = 5;
 74  
 75      @Inject
 76      private JMSContext context;
 77  
 78      @Resource(lookup = "java:/queue/HELLOWORLDMDBQueue")
 79      private Queue queue;
 80  
 81      @Resource(lookup = "java:/topic/HELLOWORLDMDBTopic")
 82      private Topic topic;
 83  
 84      @Override
 85      protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
 86          resp.setContentType("text/html");
 87          PrintWriter out = resp.getWriter();
 88          out.write("<h1>Quickstart: Example demonstrates the use of <strong>JMS 2.0</strong> and <strong>EJB 3.2 Message-Driven Bean</strong> in JBoss EAP.</h1>");
 89          try {
 90              boolean useTopic = req.getParameterMap().keySet().contains("topic");
 91              final Destination destination = useTopic ? topic : queue;
 92  
 93              out.write("<p>Sending messages to <em>" + destination + "</em></p>");
 94              out.write("<h2>The following messages will be sent to the destination:</h2>");
 95              for (int i = 0; i < MSG_COUNT; i++) {
 96                  String text = "This is message " + (i + 1);
 97                  context.createProducer().send(destination, text);
 98                  out.write("Message (" + i + "): " + text + "</br>");
 99              }
100              out.write("<p><i>Go to your JBoss EAP server console or server log to see the result of messages processing.</i></p>");
101          } finally {
102              if (out != null) {
103                  out.close();
104              }
105          }
106      }
107  
108      protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
109          doGet(req, resp);
110      }
111  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/servlet/HelloWorldMDBServletClient.java
      * Replace the `javax.inject` import statement with `jakarta.inject` 
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
 17  package org.jboss.as.quickstarts.servlet;
 18  
 19  import java.io.IOException;
 20  import java.io.PrintWriter;
 21  
 22  import javax.annotation.Resource;
 23  import javax.inject.Inject;
 24  import javax.jms.Destination;
 25  import javax.jms.JMSContext;
 26  import javax.jms.JMSDestinationDefinition;
 27  import javax.jms.JMSDestinationDefinitions;
 28  import javax.jms.Queue;
 29  import javax.jms.Topic;
 30  import javax.servlet.ServletException;
 31  import javax.servlet.annotation.WebServlet;
 32  import javax.servlet.http.HttpServlet;
 33  import javax.servlet.http.HttpServletRequest;
 34  import javax.servlet.http.HttpServletResponse;
 35  
 36  /**
 37   * Definition of the two JMS destinations used by the quickstart
 38   * (one queue and one topic).
 39   */
 40  @JMSDestinationDefinitions(
 41      value = {
 42          @JMSDestinationDefinition(
 43              name = "java:/queue/HELLOWORLDMDBQueue",
 44              interfaceName = "javax.jms.Queue",
 45              destinationName = "HelloWorldMDBQueue"
 46          ),
 47          @JMSDestinationDefinition(
 48              name = "java:/topic/HELLOWORLDMDBTopic",
 49              interfaceName = "javax.jms.Topic",
 50              destinationName = "HelloWorldMDBTopic"
 51          )
 52      }
 53  )
 54  
 55  /**
 56   * <p>
 57   * A simple servlet 3 as client that sends several messages to a queue or a topic.
 58   * </p>
 59   *
 60   * <p>
 61   * The servlet is registered and mapped to /HelloWorldMDBServletClient using the {@linkplain WebServlet
 62   * @HttpServlet}.
 63   * </p>
 64   *
 65   * @author Serge Pagop (spagop@redhat.com)
 66   *
 67   */
 68  @WebServlet("/HelloWorldMDBServletClient")
 69  public class HelloWorldMDBServletClient extends HttpServlet {
 70  
 71      private static final long serialVersionUID = -8314035702649252239L;
 72  
 73      private static final int MSG_COUNT = 5;
 74  
 75      @Inject
 76      private JMSContext context;
 77  
 78      @Resource(lookup = "java:/queue/HELLOWORLDMDBQueue")
 79      private Queue queue;
 80  
 81      @Resource(lookup = "java:/topic/HELLOWORLDMDBTopic")
 82      private Topic topic;
 83  
 84      @Override
 85      protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
 86          resp.setContentType("text/html");
 87          PrintWriter out = resp.getWriter();
 88          out.write("<h1>Quickstart: Example demonstrates the use of <strong>JMS 2.0</strong> and <strong>EJB 3.2 Message-Driven Bean</strong> in JBoss EAP.</h1>");
 89          try {
 90              boolean useTopic = req.getParameterMap().keySet().contains("topic");
 91              final Destination destination = useTopic ? topic : queue;
 92  
 93              out.write("<p>Sending messages to <em>" + destination + "</em></p>");
 94              out.write("<h2>The following messages will be sent to the destination:</h2>");
 95              for (int i = 0; i < MSG_COUNT; i++) {
 96                  String text = "This is message " + (i + 1);
 97                  context.createProducer().send(destination, text);
 98                  out.write("Message (" + i + "): " + text + "</br>");
 99              }
100              out.write("<p><i>Go to your JBoss EAP server console or server log to see the result of messages processing.</i></p>");
101          } finally {
102              if (out != null) {
103                  out.close();
104              }
105          }
106      }
107  
108      protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
109          doGet(req, resp);
110      }
111  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/servlet/HelloWorldMDBServletClient.java
      * Replace the `javax.jms` import statement with `jakarta.jms` 
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
 17  package org.jboss.as.quickstarts.servlet;
 18  
 19  import java.io.IOException;
 20  import java.io.PrintWriter;
 21  
 22  import javax.annotation.Resource;
 23  import javax.inject.Inject;
 24  import javax.jms.Destination;
 25  import javax.jms.JMSContext;
 26  import javax.jms.JMSDestinationDefinition;
 27  import javax.jms.JMSDestinationDefinitions;
 28  import javax.jms.Queue;
 29  import javax.jms.Topic;
 30  import javax.servlet.ServletException;
 31  import javax.servlet.annotation.WebServlet;
 32  import javax.servlet.http.HttpServlet;
 33  import javax.servlet.http.HttpServletRequest;
 34  import javax.servlet.http.HttpServletResponse;
 35  
 36  /**
 37   * Definition of the two JMS destinations used by the quickstart
 38   * (one queue and one topic).
 39   */
 40  @JMSDestinationDefinitions(
 41      value = {
 42          @JMSDestinationDefinition(
 43              name = "java:/queue/HELLOWORLDMDBQueue",
 44              interfaceName = "javax.jms.Queue",
 45              destinationName = "HelloWorldMDBQueue"
 46          ),
 47          @JMSDestinationDefinition(
 48              name = "java:/topic/HELLOWORLDMDBTopic",
 49              interfaceName = "javax.jms.Topic",
 50              destinationName = "HelloWorldMDBTopic"
 51          )
 52      }
 53  )
 54  
 55  /**
 56   * <p>
 57   * A simple servlet 3 as client that sends several messages to a queue or a topic.
 58   * </p>
 59   *
 60   * <p>
 61   * The servlet is registered and mapped to /HelloWorldMDBServletClient using the {@linkplain WebServlet
 62   * @HttpServlet}.
 63   * </p>
 64   *
 65   * @author Serge Pagop (spagop@redhat.com)
 66   *
 67   */
 68  @WebServlet("/HelloWorldMDBServletClient")
 69  public class HelloWorldMDBServletClient extends HttpServlet {
 70  
 71      private static final long serialVersionUID = -8314035702649252239L;
 72  
 73      private static final int MSG_COUNT = 5;
 74  
 75      @Inject
 76      private JMSContext context;
 77  
 78      @Resource(lookup = "java:/queue/HELLOWORLDMDBQueue")
 79      private Queue queue;
 80  
 81      @Resource(lookup = "java:/topic/HELLOWORLDMDBTopic")
 82      private Topic topic;
 83  
 84      @Override
 85      protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
 86          resp.setContentType("text/html");
 87          PrintWriter out = resp.getWriter();
 88          out.write("<h1>Quickstart: Example demonstrates the use of <strong>JMS 2.0</strong> and <strong>EJB 3.2 Message-Driven Bean</strong> in JBoss EAP.</h1>");
 89          try {
 90              boolean useTopic = req.getParameterMap().keySet().contains("topic");
 91              final Destination destination = useTopic ? topic : queue;
 92  
 93              out.write("<p>Sending messages to <em>" + destination + "</em></p>");
 94              out.write("<h2>The following messages will be sent to the destination:</h2>");
 95              for (int i = 0; i < MSG_COUNT; i++) {
 96                  String text = "This is message " + (i + 1);
 97                  context.createProducer().send(destination, text);
 98                  out.write("Message (" + i + "): " + text + "</br>");
 99              }
100              out.write("<p><i>Go to your JBoss EAP server console or server log to see the result of messages processing.</i></p>");
101          } finally {
102              if (out != null) {
103                  out.close();
104              }
105          }
106      }
107  
108      protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
109          doGet(req, resp);
110      }
111  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/servlet/HelloWorldMDBServletClient.java
      * Replace the `javax.jms` import statement with `jakarta.jms` 
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
 17  package org.jboss.as.quickstarts.servlet;
 18  
 19  import java.io.IOException;
 20  import java.io.PrintWriter;
 21  
 22  import javax.annotation.Resource;
 23  import javax.inject.Inject;
 24  import javax.jms.Destination;
 25  import javax.jms.JMSContext;
 26  import javax.jms.JMSDestinationDefinition;
 27  import javax.jms.JMSDestinationDefinitions;
 28  import javax.jms.Queue;
 29  import javax.jms.Topic;
 30  import javax.servlet.ServletException;
 31  import javax.servlet.annotation.WebServlet;
 32  import javax.servlet.http.HttpServlet;
 33  import javax.servlet.http.HttpServletRequest;
 34  import javax.servlet.http.HttpServletResponse;
 35  
 36  /**
 37   * Definition of the two JMS destinations used by the quickstart
 38   * (one queue and one topic).
 39   */
 40  @JMSDestinationDefinitions(
 41      value = {
 42          @JMSDestinationDefinition(
 43              name = "java:/queue/HELLOWORLDMDBQueue",
 44              interfaceName = "javax.jms.Queue",
 45              destinationName = "HelloWorldMDBQueue"
 46          ),
 47          @JMSDestinationDefinition(
 48              name = "java:/topic/HELLOWORLDMDBTopic",
 49              interfaceName = "javax.jms.Topic",
 50              destinationName = "HelloWorldMDBTopic"
 51          )
 52      }
 53  )
 54  
 55  /**
 56   * <p>
 57   * A simple servlet 3 as client that sends several messages to a queue or a topic.
 58   * </p>
 59   *
 60   * <p>
 61   * The servlet is registered and mapped to /HelloWorldMDBServletClient using the {@linkplain WebServlet
 62   * @HttpServlet}.
 63   * </p>
 64   *
 65   * @author Serge Pagop (spagop@redhat.com)
 66   *
 67   */
 68  @WebServlet("/HelloWorldMDBServletClient")
 69  public class HelloWorldMDBServletClient extends HttpServlet {
 70  
 71      private static final long serialVersionUID = -8314035702649252239L;
 72  
 73      private static final int MSG_COUNT = 5;
 74  
 75      @Inject
 76      private JMSContext context;
 77  
 78      @Resource(lookup = "java:/queue/HELLOWORLDMDBQueue")
 79      private Queue queue;
 80  
 81      @Resource(lookup = "java:/topic/HELLOWORLDMDBTopic")
 82      private Topic topic;
 83  
 84      @Override
 85      protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
 86          resp.setContentType("text/html");
 87          PrintWriter out = resp.getWriter();
 88          out.write("<h1>Quickstart: Example demonstrates the use of <strong>JMS 2.0</strong> and <strong>EJB 3.2 Message-Driven Bean</strong> in JBoss EAP.</h1>");
 89          try {
 90              boolean useTopic = req.getParameterMap().keySet().contains("topic");
 91              final Destination destination = useTopic ? topic : queue;
 92  
 93              out.write("<p>Sending messages to <em>" + destination + "</em></p>");
 94              out.write("<h2>The following messages will be sent to the destination:</h2>");
 95              for (int i = 0; i < MSG_COUNT; i++) {
 96                  String text = "This is message " + (i + 1);
 97                  context.createProducer().send(destination, text);
 98                  out.write("Message (" + i + "): " + text + "</br>");
 99              }
100              out.write("<p><i>Go to your JBoss EAP server console or server log to see the result of messages processing.</i></p>");
101          } finally {
102              if (out != null) {
103                  out.close();
104              }
105          }
106      }
107  
108      protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
109          doGet(req, resp);
110      }
111  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/servlet/HelloWorldMDBServletClient.java
      * Replace the `javax.jms` import statement with `jakarta.jms` 
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
 17  package org.jboss.as.quickstarts.servlet;
 18  
 19  import java.io.IOException;
 20  import java.io.PrintWriter;
 21  
 22  import javax.annotation.Resource;
 23  import javax.inject.Inject;
 24  import javax.jms.Destination;
 25  import javax.jms.JMSContext;
 26  import javax.jms.JMSDestinationDefinition;
 27  import javax.jms.JMSDestinationDefinitions;
 28  import javax.jms.Queue;
 29  import javax.jms.Topic;
 30  import javax.servlet.ServletException;
 31  import javax.servlet.annotation.WebServlet;
 32  import javax.servlet.http.HttpServlet;
 33  import javax.servlet.http.HttpServletRequest;
 34  import javax.servlet.http.HttpServletResponse;
 35  
 36  /**
 37   * Definition of the two JMS destinations used by the quickstart
 38   * (one queue and one topic).
 39   */
 40  @JMSDestinationDefinitions(
 41      value = {
 42          @JMSDestinationDefinition(
 43              name = "java:/queue/HELLOWORLDMDBQueue",
 44              interfaceName = "javax.jms.Queue",
 45              destinationName = "HelloWorldMDBQueue"
 46          ),
 47          @JMSDestinationDefinition(
 48              name = "java:/topic/HELLOWORLDMDBTopic",
 49              interfaceName = "javax.jms.Topic",
 50              destinationName = "HelloWorldMDBTopic"
 51          )
 52      }
 53  )
 54  
 55  /**
 56   * <p>
 57   * A simple servlet 3 as client that sends several messages to a queue or a topic.
 58   * </p>
 59   *
 60   * <p>
 61   * The servlet is registered and mapped to /HelloWorldMDBServletClient using the {@linkplain WebServlet
 62   * @HttpServlet}.
 63   * </p>
 64   *
 65   * @author Serge Pagop (spagop@redhat.com)
 66   *
 67   */
 68  @WebServlet("/HelloWorldMDBServletClient")
 69  public class HelloWorldMDBServletClient extends HttpServlet {
 70  
 71      private static final long serialVersionUID = -8314035702649252239L;
 72  
 73      private static final int MSG_COUNT = 5;
 74  
 75      @Inject
 76      private JMSContext context;
 77  
 78      @Resource(lookup = "java:/queue/HELLOWORLDMDBQueue")
 79      private Queue queue;
 80  
 81      @Resource(lookup = "java:/topic/HELLOWORLDMDBTopic")
 82      private Topic topic;
 83  
 84      @Override
 85      protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
 86          resp.setContentType("text/html");
 87          PrintWriter out = resp.getWriter();
 88          out.write("<h1>Quickstart: Example demonstrates the use of <strong>JMS 2.0</strong> and <strong>EJB 3.2 Message-Driven Bean</strong> in JBoss EAP.</h1>");
 89          try {
 90              boolean useTopic = req.getParameterMap().keySet().contains("topic");
 91              final Destination destination = useTopic ? topic : queue;
 92  
 93              out.write("<p>Sending messages to <em>" + destination + "</em></p>");
 94              out.write("<h2>The following messages will be sent to the destination:</h2>");
 95              for (int i = 0; i < MSG_COUNT; i++) {
 96                  String text = "This is message " + (i + 1);
 97                  context.createProducer().send(destination, text);
 98                  out.write("Message (" + i + "): " + text + "</br>");
 99              }
100              out.write("<p><i>Go to your JBoss EAP server console or server log to see the result of messages processing.</i></p>");
101          } finally {
102              if (out != null) {
103                  out.close();
104              }
105          }
106      }
107  
108      protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
109          doGet(req, resp);
110      }
111  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/servlet/HelloWorldMDBServletClient.java
      * Replace the `javax.jms` import statement with `jakarta.jms` 
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
 17  package org.jboss.as.quickstarts.servlet;
 18  
 19  import java.io.IOException;
 20  import java.io.PrintWriter;
 21  
 22  import javax.annotation.Resource;
 23  import javax.inject.Inject;
 24  import javax.jms.Destination;
 25  import javax.jms.JMSContext;
 26  import javax.jms.JMSDestinationDefinition;
 27  import javax.jms.JMSDestinationDefinitions;
 28  import javax.jms.Queue;
 29  import javax.jms.Topic;
 30  import javax.servlet.ServletException;
 31  import javax.servlet.annotation.WebServlet;
 32  import javax.servlet.http.HttpServlet;
 33  import javax.servlet.http.HttpServletRequest;
 34  import javax.servlet.http.HttpServletResponse;
 35  
 36  /**
 37   * Definition of the two JMS destinations used by the quickstart
 38   * (one queue and one topic).
 39   */
 40  @JMSDestinationDefinitions(
 41      value = {
 42          @JMSDestinationDefinition(
 43              name = "java:/queue/HELLOWORLDMDBQueue",
 44              interfaceName = "javax.jms.Queue",
 45              destinationName = "HelloWorldMDBQueue"
 46          ),
 47          @JMSDestinationDefinition(
 48              name = "java:/topic/HELLOWORLDMDBTopic",
 49              interfaceName = "javax.jms.Topic",
 50              destinationName = "HelloWorldMDBTopic"
 51          )
 52      }
 53  )
 54  
 55  /**
 56   * <p>
 57   * A simple servlet 3 as client that sends several messages to a queue or a topic.
 58   * </p>
 59   *
 60   * <p>
 61   * The servlet is registered and mapped to /HelloWorldMDBServletClient using the {@linkplain WebServlet
 62   * @HttpServlet}.
 63   * </p>
 64   *
 65   * @author Serge Pagop (spagop@redhat.com)
 66   *
 67   */
 68  @WebServlet("/HelloWorldMDBServletClient")
 69  public class HelloWorldMDBServletClient extends HttpServlet {
 70  
 71      private static final long serialVersionUID = -8314035702649252239L;
 72  
 73      private static final int MSG_COUNT = 5;
 74  
 75      @Inject
 76      private JMSContext context;
 77  
 78      @Resource(lookup = "java:/queue/HELLOWORLDMDBQueue")
 79      private Queue queue;
 80  
 81      @Resource(lookup = "java:/topic/HELLOWORLDMDBTopic")
 82      private Topic topic;
 83  
 84      @Override
 85      protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
 86          resp.setContentType("text/html");
 87          PrintWriter out = resp.getWriter();
 88          out.write("<h1>Quickstart: Example demonstrates the use of <strong>JMS 2.0</strong> and <strong>EJB 3.2 Message-Driven Bean</strong> in JBoss EAP.</h1>");
 89          try {
 90              boolean useTopic = req.getParameterMap().keySet().contains("topic");
 91              final Destination destination = useTopic ? topic : queue;
 92  
 93              out.write("<p>Sending messages to <em>" + destination + "</em></p>");
 94              out.write("<h2>The following messages will be sent to the destination:</h2>");
 95              for (int i = 0; i < MSG_COUNT; i++) {
 96                  String text = "This is message " + (i + 1);
 97                  context.createProducer().send(destination, text);
 98                  out.write("Message (" + i + "): " + text + "</br>");
 99              }
100              out.write("<p><i>Go to your JBoss EAP server console or server log to see the result of messages processing.</i></p>");
101          } finally {
102              if (out != null) {
103                  out.close();
104              }
105          }
106      }
107  
108      protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
109          doGet(req, resp);
110      }
111  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/servlet/HelloWorldMDBServletClient.java
      * Replace the `javax.jms` import statement with `jakarta.jms` 
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
 17  package org.jboss.as.quickstarts.servlet;
 18  
 19  import java.io.IOException;
 20  import java.io.PrintWriter;
 21  
 22  import javax.annotation.Resource;
 23  import javax.inject.Inject;
 24  import javax.jms.Destination;
 25  import javax.jms.JMSContext;
 26  import javax.jms.JMSDestinationDefinition;
 27  import javax.jms.JMSDestinationDefinitions;
 28  import javax.jms.Queue;
 29  import javax.jms.Topic;
 30  import javax.servlet.ServletException;
 31  import javax.servlet.annotation.WebServlet;
 32  import javax.servlet.http.HttpServlet;
 33  import javax.servlet.http.HttpServletRequest;
 34  import javax.servlet.http.HttpServletResponse;
 35  
 36  /**
 37   * Definition of the two JMS destinations used by the quickstart
 38   * (one queue and one topic).
 39   */
 40  @JMSDestinationDefinitions(
 41      value = {
 42          @JMSDestinationDefinition(
 43              name = "java:/queue/HELLOWORLDMDBQueue",
 44              interfaceName = "javax.jms.Queue",
 45              destinationName = "HelloWorldMDBQueue"
 46          ),
 47          @JMSDestinationDefinition(
 48              name = "java:/topic/HELLOWORLDMDBTopic",
 49              interfaceName = "javax.jms.Topic",
 50              destinationName = "HelloWorldMDBTopic"
 51          )
 52      }
 53  )
 54  
 55  /**
 56   * <p>
 57   * A simple servlet 3 as client that sends several messages to a queue or a topic.
 58   * </p>
 59   *
 60   * <p>
 61   * The servlet is registered and mapped to /HelloWorldMDBServletClient using the {@linkplain WebServlet
 62   * @HttpServlet}.
 63   * </p>
 64   *
 65   * @author Serge Pagop (spagop@redhat.com)
 66   *
 67   */
 68  @WebServlet("/HelloWorldMDBServletClient")
 69  public class HelloWorldMDBServletClient extends HttpServlet {
 70  
 71      private static final long serialVersionUID = -8314035702649252239L;
 72  
 73      private static final int MSG_COUNT = 5;
 74  
 75      @Inject
 76      private JMSContext context;
 77  
 78      @Resource(lookup = "java:/queue/HELLOWORLDMDBQueue")
 79      private Queue queue;
 80  
 81      @Resource(lookup = "java:/topic/HELLOWORLDMDBTopic")
 82      private Topic topic;
 83  
 84      @Override
 85      protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
 86          resp.setContentType("text/html");
 87          PrintWriter out = resp.getWriter();
 88          out.write("<h1>Quickstart: Example demonstrates the use of <strong>JMS 2.0</strong> and <strong>EJB 3.2 Message-Driven Bean</strong> in JBoss EAP.</h1>");
 89          try {
 90              boolean useTopic = req.getParameterMap().keySet().contains("topic");
 91              final Destination destination = useTopic ? topic : queue;
 92  
 93              out.write("<p>Sending messages to <em>" + destination + "</em></p>");
 94              out.write("<h2>The following messages will be sent to the destination:</h2>");
 95              for (int i = 0; i < MSG_COUNT; i++) {
 96                  String text = "This is message " + (i + 1);
 97                  context.createProducer().send(destination, text);
 98                  out.write("Message (" + i + "): " + text + "</br>");
 99              }
100              out.write("<p><i>Go to your JBoss EAP server console or server log to see the result of messages processing.</i></p>");
101          } finally {
102              if (out != null) {
103                  out.close();
104              }
105          }
106      }
107  
108      protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
109          doGet(req, resp);
110      }
111  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/servlet/HelloWorldMDBServletClient.java
      * Replace the `javax.jms` import statement with `jakarta.jms` 
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
 17  package org.jboss.as.quickstarts.servlet;
 18  
 19  import java.io.IOException;
 20  import java.io.PrintWriter;
 21  
 22  import javax.annotation.Resource;
 23  import javax.inject.Inject;
 24  import javax.jms.Destination;
 25  import javax.jms.JMSContext;
 26  import javax.jms.JMSDestinationDefinition;
 27  import javax.jms.JMSDestinationDefinitions;
 28  import javax.jms.Queue;
 29  import javax.jms.Topic;
 30  import javax.servlet.ServletException;
 31  import javax.servlet.annotation.WebServlet;
 32  import javax.servlet.http.HttpServlet;
 33  import javax.servlet.http.HttpServletRequest;
 34  import javax.servlet.http.HttpServletResponse;
 35  
 36  /**
 37   * Definition of the two JMS destinations used by the quickstart
 38   * (one queue and one topic).
 39   */
 40  @JMSDestinationDefinitions(
 41      value = {
 42          @JMSDestinationDefinition(
 43              name = "java:/queue/HELLOWORLDMDBQueue",
 44              interfaceName = "javax.jms.Queue",
 45              destinationName = "HelloWorldMDBQueue"
 46          ),
 47          @JMSDestinationDefinition(
 48              name = "java:/topic/HELLOWORLDMDBTopic",
 49              interfaceName = "javax.jms.Topic",
 50              destinationName = "HelloWorldMDBTopic"
 51          )
 52      }
 53  )
 54  
 55  /**
 56   * <p>
 57   * A simple servlet 3 as client that sends several messages to a queue or a topic.
 58   * </p>
 59   *
 60   * <p>
 61   * The servlet is registered and mapped to /HelloWorldMDBServletClient using the {@linkplain WebServlet
 62   * @HttpServlet}.
 63   * </p>
 64   *
 65   * @author Serge Pagop (spagop@redhat.com)
 66   *
 67   */
 68  @WebServlet("/HelloWorldMDBServletClient")
 69  public class HelloWorldMDBServletClient extends HttpServlet {
 70  
 71      private static final long serialVersionUID = -8314035702649252239L;
 72  
 73      private static final int MSG_COUNT = 5;
 74  
 75      @Inject
 76      private JMSContext context;
 77  
 78      @Resource(lookup = "java:/queue/HELLOWORLDMDBQueue")
 79      private Queue queue;
 80  
 81      @Resource(lookup = "java:/topic/HELLOWORLDMDBTopic")
 82      private Topic topic;
 83  
 84      @Override
 85      protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
 86          resp.setContentType("text/html");
 87          PrintWriter out = resp.getWriter();
 88          out.write("<h1>Quickstart: Example demonstrates the use of <strong>JMS 2.0</strong> and <strong>EJB 3.2 Message-Driven Bean</strong> in JBoss EAP.</h1>");
 89          try {
 90              boolean useTopic = req.getParameterMap().keySet().contains("topic");
 91              final Destination destination = useTopic ? topic : queue;
 92  
 93              out.write("<p>Sending messages to <em>" + destination + "</em></p>");
 94              out.write("<h2>The following messages will be sent to the destination:</h2>");
 95              for (int i = 0; i < MSG_COUNT; i++) {
 96                  String text = "This is message " + (i + 1);
 97                  context.createProducer().send(destination, text);
 98                  out.write("Message (" + i + "): " + text + "</br>");
 99              }
100              out.write("<p><i>Go to your JBoss EAP server console or server log to see the result of messages processing.</i></p>");
101          } finally {
102              if (out != null) {
103                  out.close();
104              }
105          }
106      }
107  
108      protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
109          doGet(req, resp);
110      }
111  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/servlet/HelloWorldMDBServletClient.java
      * Replace the `javax.servlet` import statement with `jakarta.servlet` 
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
 17  package org.jboss.as.quickstarts.servlet;
 18  
 19  import java.io.IOException;
 20  import java.io.PrintWriter;
 21  
 22  import javax.annotation.Resource;
 23  import javax.inject.Inject;
 24  import javax.jms.Destination;
 25  import javax.jms.JMSContext;
 26  import javax.jms.JMSDestinationDefinition;
 27  import javax.jms.JMSDestinationDefinitions;
 28  import javax.jms.Queue;
 29  import javax.jms.Topic;
 30  import javax.servlet.ServletException;
 31  import javax.servlet.annotation.WebServlet;
 32  import javax.servlet.http.HttpServlet;
 33  import javax.servlet.http.HttpServletRequest;
 34  import javax.servlet.http.HttpServletResponse;
 35  
 36  /**
 37   * Definition of the two JMS destinations used by the quickstart
 38   * (one queue and one topic).
 39   */
 40  @JMSDestinationDefinitions(
 41      value = {
 42          @JMSDestinationDefinition(
 43              name = "java:/queue/HELLOWORLDMDBQueue",
 44              interfaceName = "javax.jms.Queue",
 45              destinationName = "HelloWorldMDBQueue"
 46          ),
 47          @JMSDestinationDefinition(
 48              name = "java:/topic/HELLOWORLDMDBTopic",
 49              interfaceName = "javax.jms.Topic",
 50              destinationName = "HelloWorldMDBTopic"
 51          )
 52      }
 53  )
 54  
 55  /**
 56   * <p>
 57   * A simple servlet 3 as client that sends several messages to a queue or a topic.
 58   * </p>
 59   *
 60   * <p>
 61   * The servlet is registered and mapped to /HelloWorldMDBServletClient using the {@linkplain WebServlet
 62   * @HttpServlet}.
 63   * </p>
 64   *
 65   * @author Serge Pagop (spagop@redhat.com)
 66   *
 67   */
 68  @WebServlet("/HelloWorldMDBServletClient")
 69  public class HelloWorldMDBServletClient extends HttpServlet {
 70  
 71      private static final long serialVersionUID = -8314035702649252239L;
 72  
 73      private static final int MSG_COUNT = 5;
 74  
 75      @Inject
 76      private JMSContext context;
 77  
 78      @Resource(lookup = "java:/queue/HELLOWORLDMDBQueue")
 79      private Queue queue;
 80  
 81      @Resource(lookup = "java:/topic/HELLOWORLDMDBTopic")
 82      private Topic topic;
 83  
 84      @Override
 85      protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
 86          resp.setContentType("text/html");
 87          PrintWriter out = resp.getWriter();
 88          out.write("<h1>Quickstart: Example demonstrates the use of <strong>JMS 2.0</strong> and <strong>EJB 3.2 Message-Driven Bean</strong> in JBoss EAP.</h1>");
 89          try {
 90              boolean useTopic = req.getParameterMap().keySet().contains("topic");
 91              final Destination destination = useTopic ? topic : queue;
 92  
 93              out.write("<p>Sending messages to <em>" + destination + "</em></p>");
 94              out.write("<h2>The following messages will be sent to the destination:</h2>");
 95              for (int i = 0; i < MSG_COUNT; i++) {
 96                  String text = "This is message " + (i + 1);
 97                  context.createProducer().send(destination, text);
 98                  out.write("Message (" + i + "): " + text + "</br>");
 99              }
100              out.write("<p><i>Go to your JBoss EAP server console or server log to see the result of messages processing.</i></p>");
101          } finally {
102              if (out != null) {
103                  out.close();
104              }
105          }
106      }
107  
108      protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
109          doGet(req, resp);
110      }
111  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/servlet/HelloWorldMDBServletClient.java
      * Replace the `javax.servlet` import statement with `jakarta.servlet` 
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
 17  package org.jboss.as.quickstarts.servlet;
 18  
 19  import java.io.IOException;
 20  import java.io.PrintWriter;
 21  
 22  import javax.annotation.Resource;
 23  import javax.inject.Inject;
 24  import javax.jms.Destination;
 25  import javax.jms.JMSContext;
 26  import javax.jms.JMSDestinationDefinition;
 27  import javax.jms.JMSDestinationDefinitions;
 28  import javax.jms.Queue;
 29  import javax.jms.Topic;
 30  import javax.servlet.ServletException;
 31  import javax.servlet.annotation.WebServlet;
 32  import javax.servlet.http.HttpServlet;
 33  import javax.servlet.http.HttpServletRequest;
 34  import javax.servlet.http.HttpServletResponse;
 35  
 36  /**
 37   * Definition of the two JMS destinations used by the quickstart
 38   * (one queue and one topic).
 39   */
 40  @JMSDestinationDefinitions(
 41      value = {
 42          @JMSDestinationDefinition(
 43              name = "java:/queue/HELLOWORLDMDBQueue",
 44              interfaceName = "javax.jms.Queue",
 45              destinationName = "HelloWorldMDBQueue"
 46          ),
 47          @JMSDestinationDefinition(
 48              name = "java:/topic/HELLOWORLDMDBTopic",
 49              interfaceName = "javax.jms.Topic",
 50              destinationName = "HelloWorldMDBTopic"
 51          )
 52      }
 53  )
 54  
 55  /**
 56   * <p>
 57   * A simple servlet 3 as client that sends several messages to a queue or a topic.
 58   * </p>
 59   *
 60   * <p>
 61   * The servlet is registered and mapped to /HelloWorldMDBServletClient using the {@linkplain WebServlet
 62   * @HttpServlet}.
 63   * </p>
 64   *
 65   * @author Serge Pagop (spagop@redhat.com)
 66   *
 67   */
 68  @WebServlet("/HelloWorldMDBServletClient")
 69  public class HelloWorldMDBServletClient extends HttpServlet {
 70  
 71      private static final long serialVersionUID = -8314035702649252239L;
 72  
 73      private static final int MSG_COUNT = 5;
 74  
 75      @Inject
 76      private JMSContext context;
 77  
 78      @Resource(lookup = "java:/queue/HELLOWORLDMDBQueue")
 79      private Queue queue;
 80  
 81      @Resource(lookup = "java:/topic/HELLOWORLDMDBTopic")
 82      private Topic topic;
 83  
 84      @Override
 85      protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
 86          resp.setContentType("text/html");
 87          PrintWriter out = resp.getWriter();
 88          out.write("<h1>Quickstart: Example demonstrates the use of <strong>JMS 2.0</strong> and <strong>EJB 3.2 Message-Driven Bean</strong> in JBoss EAP.</h1>");
 89          try {
 90              boolean useTopic = req.getParameterMap().keySet().contains("topic");
 91              final Destination destination = useTopic ? topic : queue;
 92  
 93              out.write("<p>Sending messages to <em>" + destination + "</em></p>");
 94              out.write("<h2>The following messages will be sent to the destination:</h2>");
 95              for (int i = 0; i < MSG_COUNT; i++) {
 96                  String text = "This is message " + (i + 1);
 97                  context.createProducer().send(destination, text);
 98                  out.write("Message (" + i + "): " + text + "</br>");
 99              }
100              out.write("<p><i>Go to your JBoss EAP server console or server log to see the result of messages processing.</i></p>");
101          } finally {
102              if (out != null) {
103                  out.close();
104              }
105          }
106      }
107  
108      protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
109          doGet(req, resp);
110      }
111  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/servlet/HelloWorldMDBServletClient.java
      * Replace the `javax.servlet` import statement with `jakarta.servlet` 
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
 17  package org.jboss.as.quickstarts.servlet;
 18  
 19  import java.io.IOException;
 20  import java.io.PrintWriter;
 21  
 22  import javax.annotation.Resource;
 23  import javax.inject.Inject;
 24  import javax.jms.Destination;
 25  import javax.jms.JMSContext;
 26  import javax.jms.JMSDestinationDefinition;
 27  import javax.jms.JMSDestinationDefinitions;
 28  import javax.jms.Queue;
 29  import javax.jms.Topic;
 30  import javax.servlet.ServletException;
 31  import javax.servlet.annotation.WebServlet;
 32  import javax.servlet.http.HttpServlet;
 33  import javax.servlet.http.HttpServletRequest;
 34  import javax.servlet.http.HttpServletResponse;
 35  
 36  /**
 37   * Definition of the two JMS destinations used by the quickstart
 38   * (one queue and one topic).
 39   */
 40  @JMSDestinationDefinitions(
 41      value = {
 42          @JMSDestinationDefinition(
 43              name = "java:/queue/HELLOWORLDMDBQueue",
 44              interfaceName = "javax.jms.Queue",
 45              destinationName = "HelloWorldMDBQueue"
 46          ),
 47          @JMSDestinationDefinition(
 48              name = "java:/topic/HELLOWORLDMDBTopic",
 49              interfaceName = "javax.jms.Topic",
 50              destinationName = "HelloWorldMDBTopic"
 51          )
 52      }
 53  )
 54  
 55  /**
 56   * <p>
 57   * A simple servlet 3 as client that sends several messages to a queue or a topic.
 58   * </p>
 59   *
 60   * <p>
 61   * The servlet is registered and mapped to /HelloWorldMDBServletClient using the {@linkplain WebServlet
 62   * @HttpServlet}.
 63   * </p>
 64   *
 65   * @author Serge Pagop (spagop@redhat.com)
 66   *
 67   */
 68  @WebServlet("/HelloWorldMDBServletClient")
 69  public class HelloWorldMDBServletClient extends HttpServlet {
 70  
 71      private static final long serialVersionUID = -8314035702649252239L;
 72  
 73      private static final int MSG_COUNT = 5;
 74  
 75      @Inject
 76      private JMSContext context;
 77  
 78      @Resource(lookup = "java:/queue/HELLOWORLDMDBQueue")
 79      private Queue queue;
 80  
 81      @Resource(lookup = "java:/topic/HELLOWORLDMDBTopic")
 82      private Topic topic;
 83  
 84      @Override
 85      protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
 86          resp.setContentType("text/html");
 87          PrintWriter out = resp.getWriter();
 88          out.write("<h1>Quickstart: Example demonstrates the use of <strong>JMS 2.0</strong> and <strong>EJB 3.2 Message-Driven Bean</strong> in JBoss EAP.</h1>");
 89          try {
 90              boolean useTopic = req.getParameterMap().keySet().contains("topic");
 91              final Destination destination = useTopic ? topic : queue;
 92  
 93              out.write("<p>Sending messages to <em>" + destination + "</em></p>");
 94              out.write("<h2>The following messages will be sent to the destination:</h2>");
 95              for (int i = 0; i < MSG_COUNT; i++) {
 96                  String text = "This is message " + (i + 1);
 97                  context.createProducer().send(destination, text);
 98                  out.write("Message (" + i + "): " + text + "</br>");
 99              }
100              out.write("<p><i>Go to your JBoss EAP server console or server log to see the result of messages processing.</i></p>");
101          } finally {
102              if (out != null) {
103                  out.close();
104              }
105          }
106      }
107  
108      protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
109          doGet(req, resp);
110      }
111  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/servlet/HelloWorldMDBServletClient.java
      * Replace the `javax.servlet` import statement with `jakarta.servlet` 
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
 17  package org.jboss.as.quickstarts.servlet;
 18  
 19  import java.io.IOException;
 20  import java.io.PrintWriter;
 21  
 22  import javax.annotation.Resource;
 23  import javax.inject.Inject;
 24  import javax.jms.Destination;
 25  import javax.jms.JMSContext;
 26  import javax.jms.JMSDestinationDefinition;
 27  import javax.jms.JMSDestinationDefinitions;
 28  import javax.jms.Queue;
 29  import javax.jms.Topic;
 30  import javax.servlet.ServletException;
 31  import javax.servlet.annotation.WebServlet;
 32  import javax.servlet.http.HttpServlet;
 33  import javax.servlet.http.HttpServletRequest;
 34  import javax.servlet.http.HttpServletResponse;
 35  
 36  /**
 37   * Definition of the two JMS destinations used by the quickstart
 38   * (one queue and one topic).
 39   */
 40  @JMSDestinationDefinitions(
 41      value = {
 42          @JMSDestinationDefinition(
 43              name = "java:/queue/HELLOWORLDMDBQueue",
 44              interfaceName = "javax.jms.Queue",
 45              destinationName = "HelloWorldMDBQueue"
 46          ),
 47          @JMSDestinationDefinition(
 48              name = "java:/topic/HELLOWORLDMDBTopic",
 49              interfaceName = "javax.jms.Topic",
 50              destinationName = "HelloWorldMDBTopic"
 51          )
 52      }
 53  )
 54  
 55  /**
 56   * <p>
 57   * A simple servlet 3 as client that sends several messages to a queue or a topic.
 58   * </p>
 59   *
 60   * <p>
 61   * The servlet is registered and mapped to /HelloWorldMDBServletClient using the {@linkplain WebServlet
 62   * @HttpServlet}.
 63   * </p>
 64   *
 65   * @author Serge Pagop (spagop@redhat.com)
 66   *
 67   */
 68  @WebServlet("/HelloWorldMDBServletClient")
 69  public class HelloWorldMDBServletClient extends HttpServlet {
 70  
 71      private static final long serialVersionUID = -8314035702649252239L;
 72  
 73      private static final int MSG_COUNT = 5;
 74  
 75      @Inject
 76      private JMSContext context;
 77  
 78      @Resource(lookup = "java:/queue/HELLOWORLDMDBQueue")
 79      private Queue queue;
 80  
 81      @Resource(lookup = "java:/topic/HELLOWORLDMDBTopic")
 82      private Topic topic;
 83  
 84      @Override
 85      protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
 86          resp.setContentType("text/html");
 87          PrintWriter out = resp.getWriter();
 88          out.write("<h1>Quickstart: Example demonstrates the use of <strong>JMS 2.0</strong> and <strong>EJB 3.2 Message-Driven Bean</strong> in JBoss EAP.</h1>");
 89          try {
 90              boolean useTopic = req.getParameterMap().keySet().contains("topic");
 91              final Destination destination = useTopic ? topic : queue;
 92  
 93              out.write("<p>Sending messages to <em>" + destination + "</em></p>");
 94              out.write("<h2>The following messages will be sent to the destination:</h2>");
 95              for (int i = 0; i < MSG_COUNT; i++) {
 96                  String text = "This is message " + (i + 1);
 97                  context.createProducer().send(destination, text);
 98                  out.write("Message (" + i + "): " + text + "</br>");
 99              }
100              out.write("<p><i>Go to your JBoss EAP server console or server log to see the result of messages processing.</i></p>");
101          } finally {
102              if (out != null) {
103                  out.close();
104              }
105          }
106      }
107  
108      protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
109          doGet(req, resp);
110      }
111  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/servlet/HelloWorldMDBServletClient.java
      * Replace the `javax.servlet` import statement with `jakarta.servlet` 
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
 17  package org.jboss.as.quickstarts.servlet;
 18  
 19  import java.io.IOException;
 20  import java.io.PrintWriter;
 21  
 22  import javax.annotation.Resource;
 23  import javax.inject.Inject;
 24  import javax.jms.Destination;
 25  import javax.jms.JMSContext;
 26  import javax.jms.JMSDestinationDefinition;
 27  import javax.jms.JMSDestinationDefinitions;
 28  import javax.jms.Queue;
 29  import javax.jms.Topic;
 30  import javax.servlet.ServletException;
 31  import javax.servlet.annotation.WebServlet;
 32  import javax.servlet.http.HttpServlet;
 33  import javax.servlet.http.HttpServletRequest;
 34  import javax.servlet.http.HttpServletResponse;
 35  
 36  /**
 37   * Definition of the two JMS destinations used by the quickstart
 38   * (one queue and one topic).
 39   */
 40  @JMSDestinationDefinitions(
 41      value = {
 42          @JMSDestinationDefinition(
 43              name = "java:/queue/HELLOWORLDMDBQueue",
 44              interfaceName = "javax.jms.Queue",
 45              destinationName = "HelloWorldMDBQueue"
 46          ),
 47          @JMSDestinationDefinition(
 48              name = "java:/topic/HELLOWORLDMDBTopic",
 49              interfaceName = "javax.jms.Topic",
 50              destinationName = "HelloWorldMDBTopic"
 51          )
 52      }
 53  )
 54  
 55  /**
 56   * <p>
 57   * A simple servlet 3 as client that sends several messages to a queue or a topic.
 58   * </p>
 59   *
 60   * <p>
 61   * The servlet is registered and mapped to /HelloWorldMDBServletClient using the {@linkplain WebServlet
 62   * @HttpServlet}.
 63   * </p>
 64   *
 65   * @author Serge Pagop (spagop@redhat.com)
 66   *
 67   */
 68  @WebServlet("/HelloWorldMDBServletClient")
 69  public class HelloWorldMDBServletClient extends HttpServlet {
 70  
 71      private static final long serialVersionUID = -8314035702649252239L;
 72  
 73      private static final int MSG_COUNT = 5;
 74  
 75      @Inject
 76      private JMSContext context;
 77  
 78      @Resource(lookup = "java:/queue/HELLOWORLDMDBQueue")
 79      private Queue queue;
 80  
 81      @Resource(lookup = "java:/topic/HELLOWORLDMDBTopic")
 82      private Topic topic;
 83  
 84      @Override
 85      protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
 86          resp.setContentType("text/html");
 87          PrintWriter out = resp.getWriter();
 88          out.write("<h1>Quickstart: Example demonstrates the use of <strong>JMS 2.0</strong> and <strong>EJB 3.2 Message-Driven Bean</strong> in JBoss EAP.</h1>");
 89          try {
 90              boolean useTopic = req.getParameterMap().keySet().contains("topic");
 91              final Destination destination = useTopic ? topic : queue;
 92  
 93              out.write("<p>Sending messages to <em>" + destination + "</em></p>");
 94              out.write("<h2>The following messages will be sent to the destination:</h2>");
 95              for (int i = 0; i < MSG_COUNT; i++) {
 96                  String text = "This is message " + (i + 1);
 97                  context.createProducer().send(destination, text);
 98                  out.write("Message (" + i + "): " + text + "</br>");
 99              }
100              out.write("<p><i>Go to your JBoss EAP server console or server log to see the result of messages processing.</i></p>");
101          } finally {
102              if (out != null) {
103                  out.close();
104              }
105          }
106      }
107  
108      protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
109          doGet(req, resp);
110      }
111  }

```
