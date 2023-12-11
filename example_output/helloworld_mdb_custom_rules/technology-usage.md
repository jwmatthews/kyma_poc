# technology-usage
## Description
This ruleset provides analysis of logging libraries.
* Source of rules: https://github.com/konveyor/rulesets/tree/main/default/generated
## Violations
Number of Violations: 1
### #0 - javaee-technology-usage-00120
* Category: potential
* Description: Java Servlet
* Labels: konveyor.io/include=always
* Incidents
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/servlet/HelloWorldMDBServletClient.java
      * Line Number: 30
      * Message: 'The application uses Java Servlets'
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
      * Line Number: 31
      * Message: 'The application uses Java Servlets'
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
      * Line Number: 32
      * Message: 'The application uses Java Servlets'
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
      * Line Number: 33
      * Message: 'The application uses Java Servlets'
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
      * Line Number: 34
      * Message: 'The application uses Java Servlets'
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
