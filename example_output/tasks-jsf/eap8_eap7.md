# eap8/eap7
## Description
This ruleset provides analysis of Java EE applications that need to change certain CDI-related method calls.
* Source of rules: https://github.com/konveyor/rulesets/tree/main/default/generated
## Violations
Number of Violations: 20
### #0 - javaee-to-jakarta-namespaces-00001
* Category: mandatory
* Effort: 1
* Description: Replace the Java EE namespace, schemaLocation and version with the Jakarta equivalent
* Labels: konveyor.io/source, konveyor.io/target=eap, konveyor.io/target=eap8, konveyor.io/target=jakarta-ee, konveyor.io/target=jakarta-ee9+
* Links
  * Jakarta EE XML Schemas: https://jakarta.ee/xml/ns/jakartaee/#10
* Incidents
  * file:///tmp/source-code/src/main/webapp/WEB-INF/beans.xml
      * Line Number: 19
      * Message: 'Replace `http://xmlns.jcp.org/xml/ns/javaee` with `https://jakarta.ee/xml/ns/jakartaee` and change the schema version number'
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
      * Line Number: 21
      * Message: 'Replace `http://xmlns.jcp.org/xml/ns/javaee` with `https://jakarta.ee/xml/ns/jakartaee` and change the schema version number'
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
      * Line Number: 22
      * Message: 'Replace `http://xmlns.jcp.org/xml/ns/javaee` with `https://jakarta.ee/xml/ns/jakartaee` and change the schema version number'
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
  * file:///tmp/source-code/src/main/webapp/WEB-INF/faces-config.xml
      * Line Number: 18
      * Message: 'Replace `http://xmlns.jcp.org/xml/ns/javaee` with `https://jakarta.ee/xml/ns/jakartaee` and change the schema version number'
      * Code Snippet:
```java
  1  <?xml version="1.0"?>
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
 18  <faces-config version="2.2" xmlns="http://xmlns.jcp.org/xml/ns/javaee" xmlns:xi="http://www.w3.org/2001/XInclude"
 19      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-facesconfig_2_2.xsd">
 20  
 21      <navigation-rule>
 22          <from-view-id>/index.xhtml</from-view-id>
 23          <navigation-case>
 24              <from-action>#{authController.authenticate(username)}</from-action>
 25              <if>#{authController.logged}</if>
 26              <to-view-id>/tasks.xhtml</to-view-id>
 27              <redirect />
 28          </navigation-case>
 29      </navigation-rule>
 30  
 31      <navigation-rule>
 32          <from-view-id>/tasks.xhtml</from-view-id>
 33          <navigation-case>
 34              <from-action>#{authController.logout}</from-action>
 35              <if>#{!authController.logged}</if>
 36              <to-view-id>/index.xhtml</to-view-id>
 37              <redirect />
 38          </navigation-case>
 39      </navigation-rule>
 40  
 41  </faces-config>

```
  * file:///tmp/source-code/src/main/webapp/WEB-INF/faces-config.xml
      * Line Number: 19
      * Message: 'Replace `http://xmlns.jcp.org/xml/ns/javaee` with `https://jakarta.ee/xml/ns/jakartaee` and change the schema version number'
      * Code Snippet:
```java
  1  <?xml version="1.0"?>
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
 18  <faces-config version="2.2" xmlns="http://xmlns.jcp.org/xml/ns/javaee" xmlns:xi="http://www.w3.org/2001/XInclude"
 19      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-facesconfig_2_2.xsd">
 20  
 21      <navigation-rule>
 22          <from-view-id>/index.xhtml</from-view-id>
 23          <navigation-case>
 24              <from-action>#{authController.authenticate(username)}</from-action>
 25              <if>#{authController.logged}</if>
 26              <to-view-id>/tasks.xhtml</to-view-id>
 27              <redirect />
 28          </navigation-case>
 29      </navigation-rule>
 30  
 31      <navigation-rule>
 32          <from-view-id>/tasks.xhtml</from-view-id>
 33          <navigation-case>
 34              <from-action>#{authController.logout}</from-action>
 35              <if>#{!authController.logged}</if>
 36              <to-view-id>/index.xhtml</to-view-id>
 37              <redirect />
 38          </navigation-case>
 39      </navigation-rule>
 40  
 41  </faces-config>

```
  * file:///tmp/source-code/src/test/webapp/WEB-INF/beans.xml
      * Line Number: 19
      * Message: 'Replace `http://xmlns.jcp.org/xml/ns/javaee` with `https://jakarta.ee/xml/ns/jakartaee` and change the schema version number'
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
  * file:///tmp/source-code/src/test/webapp/WEB-INF/beans.xml
      * Line Number: 21
      * Message: 'Replace `http://xmlns.jcp.org/xml/ns/javaee` with `https://jakarta.ee/xml/ns/jakartaee` and change the schema version number'
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
  * file:///tmp/source-code/src/test/webapp/WEB-INF/beans.xml
      * Line Number: 22
      * Message: 'Replace `http://xmlns.jcp.org/xml/ns/javaee` with `https://jakarta.ee/xml/ns/jakartaee` and change the schema version number'
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
### #1 - javaee-to-jakarta-namespaces-00002
* Category: mandatory
* Effort: 1
* Description: Replace the Java EE persistence namespace, schemaLocation and version with the Jakarta equivalent
* Labels: konveyor.io/source, konveyor.io/target=eap, konveyor.io/target=eap8, konveyor.io/target=jakarta-ee, konveyor.io/target=jakarta-ee9+
* Links
  * Jakarta Persistence XML Schemas: https://jakarta.ee/xml/ns/persistence/#3
* Incidents
  * file:///tmp/source-code/src/main/resources/META-INF/persistence.xml
      * Line Number: 19
      * Message: 'Replace `http://xmlns.jcp.org/xml/ns/persistence` with `https://jakarta.ee/xml/ns/persistence` and change the schema version number'
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
 18  <persistence version="2.1"
 19     xmlns="http://xmlns.jcp.org/xml/ns/persistence" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 20     xsi:schemaLocation="
 21          http://xmlns.jcp.org/xml/ns/persistence
 22          http://xmlns.jcp.org/xml/ns/persistence/persistence_2_1.xsd">
 23     <persistence-unit name="primary">
 24        <!-- We use a different datasource for tests, so as to not overwrite
 25           production data. This is an unmanaged data source, backed by H2, an in memory
 26           database. Production applications should use a managed datasource. -->
 27        <!-- The datasource is deployed as WEB-INF/test-ds.xml,
 28           you can find it in the source at src/test/resources/test-ds.xml -->
 29        <jta-data-source>java:jboss/datasources/TasksJsfQuickstartDS</jta-data-source>
 30        <properties>
 31           <!-- Properties for Hibernate -->
 32           <property name="hibernate.hbm2ddl.auto" value="create-drop" />
 33           <property name="hibernate.show_sql" value="false" />
 34        </properties>
 35     </persistence-unit>
 36  </persistence>

```
  * file:///tmp/source-code/src/main/resources/META-INF/persistence.xml
      * Line Number: 21
      * Message: 'Replace `http://xmlns.jcp.org/xml/ns/persistence` with `https://jakarta.ee/xml/ns/persistence` and change the schema version number'
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
 18  <persistence version="2.1"
 19     xmlns="http://xmlns.jcp.org/xml/ns/persistence" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 20     xsi:schemaLocation="
 21          http://xmlns.jcp.org/xml/ns/persistence
 22          http://xmlns.jcp.org/xml/ns/persistence/persistence_2_1.xsd">
 23     <persistence-unit name="primary">
 24        <!-- We use a different datasource for tests, so as to not overwrite
 25           production data. This is an unmanaged data source, backed by H2, an in memory
 26           database. Production applications should use a managed datasource. -->
 27        <!-- The datasource is deployed as WEB-INF/test-ds.xml,
 28           you can find it in the source at src/test/resources/test-ds.xml -->
 29        <jta-data-source>java:jboss/datasources/TasksJsfQuickstartDS</jta-data-source>
 30        <properties>
 31           <!-- Properties for Hibernate -->
 32           <property name="hibernate.hbm2ddl.auto" value="create-drop" />
 33           <property name="hibernate.show_sql" value="false" />
 34        </properties>
 35     </persistence-unit>
 36  </persistence>

```
  * file:///tmp/source-code/src/main/resources/META-INF/persistence.xml
      * Line Number: 22
      * Message: 'Replace `http://xmlns.jcp.org/xml/ns/persistence` with `https://jakarta.ee/xml/ns/persistence` and change the schema version number'
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
 18  <persistence version="2.1"
 19     xmlns="http://xmlns.jcp.org/xml/ns/persistence" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 20     xsi:schemaLocation="
 21          http://xmlns.jcp.org/xml/ns/persistence
 22          http://xmlns.jcp.org/xml/ns/persistence/persistence_2_1.xsd">
 23     <persistence-unit name="primary">
 24        <!-- We use a different datasource for tests, so as to not overwrite
 25           production data. This is an unmanaged data source, backed by H2, an in memory
 26           database. Production applications should use a managed datasource. -->
 27        <!-- The datasource is deployed as WEB-INF/test-ds.xml,
 28           you can find it in the source at src/test/resources/test-ds.xml -->
 29        <jta-data-source>java:jboss/datasources/TasksJsfQuickstartDS</jta-data-source>
 30        <properties>
 31           <!-- Properties for Hibernate -->
 32           <property name="hibernate.hbm2ddl.auto" value="create-drop" />
 33           <property name="hibernate.show_sql" value="false" />
 34        </properties>
 35     </persistence-unit>
 36  </persistence>

```
### #2 - javaee-to-jakarta-namespaces-00006
* Category: mandatory
* Effort: 1
* Description: Replace the Java EE XSD with the Jakarta equivalent
* Labels: konveyor.io/source, konveyor.io/target=eap, konveyor.io/target=eap8, konveyor.io/target=jakarta-ee, konveyor.io/target=jakarta-ee9+
* Links
  * Jakarta XML Schemas: https://jakarta.ee/xml/ns/jakartaee/#9
* Incidents
  * file:///tmp/source-code/src/main/webapp/WEB-INF/beans.xml
      * Line Number: 22
      * Message: 'Replace `beans_1_1.xsd` with `beans_3_0.xsd` and update the version attribute to `"3.0"`'
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
  * file:///tmp/source-code/src/test/webapp/WEB-INF/beans.xml
      * Line Number: 22
      * Message: 'Replace `beans_1_1.xsd` with `beans_3_0.xsd` and update the version attribute to `"3.0"`'
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
### #3 - javaee-to-jakarta-namespaces-00021
* Category: mandatory
* Effort: 1
* Description: Replace the Java EE XSD with the Jakarta equivalent
* Labels: konveyor.io/source, konveyor.io/target=eap, konveyor.io/target=eap8, konveyor.io/target=jakarta-ee, konveyor.io/target=jakarta-ee9+
* Links
  * Jakarta XML Schemas: https://jakarta.ee/xml/ns/jakartaee/#9
* Incidents
  * file:///tmp/source-code/src/main/webapp/WEB-INF/faces-config.xml
      * Line Number: 19
      * Message: 'Replace `web-facesconfig_2_2.xsd` with `web-facesconfig_3_0.xsd` and update the version attribute to `"3.0"`'
      * Code Snippet:
```java
  1  <?xml version="1.0"?>
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
 18  <faces-config version="2.2" xmlns="http://xmlns.jcp.org/xml/ns/javaee" xmlns:xi="http://www.w3.org/2001/XInclude"
 19      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-facesconfig_2_2.xsd">
 20  
 21      <navigation-rule>
 22          <from-view-id>/index.xhtml</from-view-id>
 23          <navigation-case>
 24              <from-action>#{authController.authenticate(username)}</from-action>
 25              <if>#{authController.logged}</if>
 26              <to-view-id>/tasks.xhtml</to-view-id>
 27              <redirect />
 28          </navigation-case>
 29      </navigation-rule>
 30  
 31      <navigation-rule>
 32          <from-view-id>/tasks.xhtml</from-view-id>
 33          <navigation-case>
 34              <from-action>#{authController.logout}</from-action>
 35              <if>#{!authController.logged}</if>
 36              <to-view-id>/index.xhtml</to-view-id>
 37              <redirect />
 38          </navigation-case>
 39      </navigation-rule>
 40  
 41  </faces-config>

```
### #4 - javaee-to-jakarta-namespaces-00030
* Category: mandatory
* Effort: 1
* Description: Replace the Java EE XSD with the Jakarta equivalent
* Labels: konveyor.io/source, konveyor.io/target=eap, konveyor.io/target=eap8, konveyor.io/target=jakarta-ee, konveyor.io/target=jakarta-ee9+
* Links
  * Jakarta XML Schemas: https://jakarta.ee/xml/ns/jakartaee/#9
* Incidents
  * file:///tmp/source-code/src/main/resources/META-INF/persistence.xml
      * Line Number: 22
      * Message: 'Replace `persistence_2_1.xsd` with `persistence_3_0.xsd` and update the version attribute to `"3.0"`'
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
 18  <persistence version="2.1"
 19     xmlns="http://xmlns.jcp.org/xml/ns/persistence" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 20     xsi:schemaLocation="
 21          http://xmlns.jcp.org/xml/ns/persistence
 22          http://xmlns.jcp.org/xml/ns/persistence/persistence_2_1.xsd">
 23     <persistence-unit name="primary">
 24        <!-- We use a different datasource for tests, so as to not overwrite
 25           production data. This is an unmanaged data source, backed by H2, an in memory
 26           database. Production applications should use a managed datasource. -->
 27        <!-- The datasource is deployed as WEB-INF/test-ds.xml,
 28           you can find it in the source at src/test/resources/test-ds.xml -->
 29        <jta-data-source>java:jboss/datasources/TasksJsfQuickstartDS</jta-data-source>
 30        <properties>
 31           <!-- Properties for Hibernate -->
 32           <property name="hibernate.hbm2ddl.auto" value="create-drop" />
 33           <property name="hibernate.show_sql" value="false" />
 34        </properties>
 35     </persistence-unit>
 36  </persistence>

```
### #5 - javaee-to-jakarta-namespaces-00033
* Category: mandatory
* Effort: 1
* Description: Replace the Java EE version with the Jakarta equivalent
* Labels: konveyor.io/source, konveyor.io/target=eap, konveyor.io/target=eap8, konveyor.io/target=jakarta-ee, konveyor.io/target=jakarta-ee9+
* Incidents
  * file:///tmp/source-code/src/main/resources/META-INF/persistence.xml
      * Line Number: 18
      * Message: 'In the root tag, replace the `version` attribute value `2.1` with `3.0`'
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
 18  <persistence version="2.1"
 19     xmlns="http://xmlns.jcp.org/xml/ns/persistence" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 20     xsi:schemaLocation="
 21          http://xmlns.jcp.org/xml/ns/persistence
 22          http://xmlns.jcp.org/xml/ns/persistence/persistence_2_1.xsd">
 23     <persistence-unit name="primary">
 24        <!-- We use a different datasource for tests, so as to not overwrite
 25           production data. This is an unmanaged data source, backed by H2, an in memory
 26           database. Production applications should use a managed datasource. -->
 27        <!-- The datasource is deployed as WEB-INF/test-ds.xml,
 28           you can find it in the source at src/test/resources/test-ds.xml -->
 29        <jta-data-source>java:jboss/datasources/TasksJsfQuickstartDS</jta-data-source>
 30        <properties>
 31           <!-- Properties for Hibernate -->
 32           <property name="hibernate.hbm2ddl.auto" value="create-drop" />
 33           <property name="hibernate.show_sql" value="false" />
 34        </properties>
 35     </persistence-unit>
 36  </persistence>

```
  * file:///tmp/source-code/src/main/resources/META-INF/persistence.xml
      * Line Number: 26
      * Message: 'In the root tag, replace the `version` attribute value `2.1` with `3.0`'
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
 18  <persistence version="2.1"
 19     xmlns="http://xmlns.jcp.org/xml/ns/persistence" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 20     xsi:schemaLocation="
 21          http://xmlns.jcp.org/xml/ns/persistence
 22          http://xmlns.jcp.org/xml/ns/persistence/persistence_2_1.xsd">
 23     <persistence-unit name="primary">
 24        <!-- We use a different datasource for tests, so as to not overwrite
 25           production data. This is an unmanaged data source, backed by H2, an in memory
 26           database. Production applications should use a managed datasource. -->
 27        <!-- The datasource is deployed as WEB-INF/test-ds.xml,
 28           you can find it in the source at src/test/resources/test-ds.xml -->
 29        <jta-data-source>java:jboss/datasources/TasksJsfQuickstartDS</jta-data-source>
 30        <properties>
 31           <!-- Properties for Hibernate -->
 32           <property name="hibernate.hbm2ddl.auto" value="create-drop" />
 33           <property name="hibernate.show_sql" value="false" />
 34        </properties>
 35     </persistence-unit>
 36  </persistence>

```
### #6 - javaee-to-jakarta-namespaces-00036
* Category: mandatory
* Effort: 1
* Description: Replace the Java EE version with the Jakarta equivalent
* Labels: konveyor.io/source, konveyor.io/target=eap, konveyor.io/target=eap8, konveyor.io/target=jakarta-ee, konveyor.io/target=jakarta-ee9+
* Incidents
  * file:///tmp/source-code/src/test/resources/META-INF/test-persistence.xml
      * Line Number: 18
      * Message: '`beans_2_0.xsd`: In the root tag, replace the `version` attribute value with `3.0`'
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
 18  <persistence version="2.0"
 19     xmlns="http://java.sun.com/xml/ns/persistence" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 20     xsi:schemaLocation="
 21          http://java.sun.com/xml/ns/persistence
 22          http://java.sun.com/xml/ns/persistence/persistence_2_0.xsd">
 23     <persistence-unit name="primary">
 24        <!-- We use a different datasource for tests, so as to not overwrite
 25           production data. This is an unmanaged data source, backed by H2, an in memory
 26           database. Production applications should use a managed datasource. -->
 27        <!-- The datasource is deployed as WEB-INF/test-ds.xml,
 28           you can find it in the source at src/test/resources/test-ds.xml -->
 29        <jta-data-source>java:jboss/datasources/TasksJsfQuickstartTestDS</jta-data-source>
 30        <properties>
 31           <!-- Properties for Hibernate -->
 32           <property name="hibernate.hbm2ddl.auto" value="create-drop" />
 33           <property name="hibernate.show_sql" value="false" />
 34        </properties>
 35     </persistence-unit>
 36  </persistence>

```
### #7 - javaee-to-jakarta-namespaces-00048
* Category: mandatory
* Effort: 1
* Description: Replace the Java EE version with the Jakarta equivalent
* Labels: konveyor.io/source, konveyor.io/target=eap, konveyor.io/target=eap8, konveyor.io/target=jakarta-ee, konveyor.io/target=jakarta-ee9+
* Incidents
  * file:///tmp/source-code/src/main/webapp/WEB-INF/faces-config.xml
      * Line Number: 18
      * Message: '`web-facesconfig_2_2`: In the root tag, replace the `version` attribute value with `3.0`'
      * Code Snippet:
```java
  1  <?xml version="1.0"?>
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
 18  <faces-config version="2.2" xmlns="http://xmlns.jcp.org/xml/ns/javaee" xmlns:xi="http://www.w3.org/2001/XInclude"
 19      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-facesconfig_2_2.xsd">
 20  
 21      <navigation-rule>
 22          <from-view-id>/index.xhtml</from-view-id>
 23          <navigation-case>
 24              <from-action>#{authController.authenticate(username)}</from-action>
 25              <if>#{authController.logged}</if>
 26              <to-view-id>/tasks.xhtml</to-view-id>
 27              <redirect />
 28          </navigation-case>
 29      </navigation-rule>
 30  
 31      <navigation-rule>
 32          <from-view-id>/tasks.xhtml</from-view-id>
 33          <navigation-case>
 34              <from-action>#{authController.logout}</from-action>
 35              <if>#{!authController.logged}</if>
 36              <to-view-id>/index.xhtml</to-view-id>
 37              <redirect />
 38          </navigation-case>
 39      </navigation-rule>
 40  
 41  </faces-config>

```
  * file:///tmp/source-code/src/main/webapp/WEB-INF/faces-config.xml
      * Line Number: 20
      * Message: '`web-facesconfig_2_2`: In the root tag, replace the `version` attribute value with `3.0`'
      * Code Snippet:
```java
  1  <?xml version="1.0"?>
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
 18  <faces-config version="2.2" xmlns="http://xmlns.jcp.org/xml/ns/javaee" xmlns:xi="http://www.w3.org/2001/XInclude"
 19      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-facesconfig_2_2.xsd">
 20  
 21      <navigation-rule>
 22          <from-view-id>/index.xhtml</from-view-id>
 23          <navigation-case>
 24              <from-action>#{authController.authenticate(username)}</from-action>
 25              <if>#{authController.logged}</if>
 26              <to-view-id>/tasks.xhtml</to-view-id>
 27              <redirect />
 28          </navigation-case>
 29      </navigation-rule>
 30  
 31      <navigation-rule>
 32          <from-view-id>/tasks.xhtml</from-view-id>
 33          <navigation-case>
 34              <from-action>#{authController.logout}</from-action>
 35              <if>#{!authController.logged}</if>
 36              <to-view-id>/index.xhtml</to-view-id>
 37              <redirect />
 38          </navigation-case>
 39      </navigation-rule>
 40  
 41  </faces-config>

```
### #8 - javaee-to-jakarta-namespaces-00050
* Category: mandatory
* Effort: 1
* Description: Replace the Java EE version with the Jakarta equivalent
* Labels: konveyor.io/source, konveyor.io/target=eap, konveyor.io/target=eap8, konveyor.io/target=jakarta-ee, konveyor.io/target=jakarta-ee9+
* Incidents
  * file:///tmp/source-code/src/main/webapp/WEB-INF/faces-config.xml
      * Line Number: 18
      * Message: '`web-facelettaglibrary_2_2`: In the root tag, replace the `version` attribute value with `3.0`'
      * Code Snippet:
```java
  1  <?xml version="1.0"?>
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
 18  <faces-config version="2.2" xmlns="http://xmlns.jcp.org/xml/ns/javaee" xmlns:xi="http://www.w3.org/2001/XInclude"
 19      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-facesconfig_2_2.xsd">
 20  
 21      <navigation-rule>
 22          <from-view-id>/index.xhtml</from-view-id>
 23          <navigation-case>
 24              <from-action>#{authController.authenticate(username)}</from-action>
 25              <if>#{authController.logged}</if>
 26              <to-view-id>/tasks.xhtml</to-view-id>
 27              <redirect />
 28          </navigation-case>
 29      </navigation-rule>
 30  
 31      <navigation-rule>
 32          <from-view-id>/tasks.xhtml</from-view-id>
 33          <navigation-case>
 34              <from-action>#{authController.logout}</from-action>
 35              <if>#{!authController.logged}</if>
 36              <to-view-id>/index.xhtml</to-view-id>
 37              <redirect />
 38          </navigation-case>
 39      </navigation-rule>
 40  
 41  </faces-config>

```
### #9 - javaee-to-jakarta-namespaces-00052
* Category: mandatory
* Effort: 1
* Description: Replace the Java EE version with the Jakarta equivalent
* Labels: konveyor.io/source, konveyor.io/target=eap, konveyor.io/target=eap8, konveyor.io/target=jakarta-ee, konveyor.io/target=jakarta-ee9+
* Incidents
  * file:///tmp/source-code/src/main/resources/META-INF/persistence.xml
      * Line Number: 18
      * Message: '`web-jsptaglibrary_2_1`: In the root tag, replace the `version` attribute value with `3.0`'
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
 18  <persistence version="2.1"
 19     xmlns="http://xmlns.jcp.org/xml/ns/persistence" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 20     xsi:schemaLocation="
 21          http://xmlns.jcp.org/xml/ns/persistence
 22          http://xmlns.jcp.org/xml/ns/persistence/persistence_2_1.xsd">
 23     <persistence-unit name="primary">
 24        <!-- We use a different datasource for tests, so as to not overwrite
 25           production data. This is an unmanaged data source, backed by H2, an in memory
 26           database. Production applications should use a managed datasource. -->
 27        <!-- The datasource is deployed as WEB-INF/test-ds.xml,
 28           you can find it in the source at src/test/resources/test-ds.xml -->
 29        <jta-data-source>java:jboss/datasources/TasksJsfQuickstartDS</jta-data-source>
 30        <properties>
 31           <!-- Properties for Hibernate -->
 32           <property name="hibernate.hbm2ddl.auto" value="create-drop" />
 33           <property name="hibernate.show_sql" value="false" />
 34        </properties>
 35     </persistence-unit>
 36  </persistence>

```
### #10 - javaee-to-jakarta-namespaces-00053
* Category: mandatory
* Effort: 1
* Description: Replace the Java EE version with the Jakarta equivalent
* Labels: konveyor.io/source, konveyor.io/target=eap, konveyor.io/target=eap8, konveyor.io/target=jakarta-ee, konveyor.io/target=jakarta-ee9+
* Incidents
  * file:///tmp/source-code/src/test/resources/META-INF/test-persistence.xml
      * Line Number: 18
      * Message: '`validation-mapping-2.0`: In the root tag, replace the `version` attribute value with `3.0`'
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
 18  <persistence version="2.0"
 19     xmlns="http://java.sun.com/xml/ns/persistence" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 20     xsi:schemaLocation="
 21          http://java.sun.com/xml/ns/persistence
 22          http://java.sun.com/xml/ns/persistence/persistence_2_0.xsd">
 23     <persistence-unit name="primary">
 24        <!-- We use a different datasource for tests, so as to not overwrite
 25           production data. This is an unmanaged data source, backed by H2, an in memory
 26           database. Production applications should use a managed datasource. -->
 27        <!-- The datasource is deployed as WEB-INF/test-ds.xml,
 28           you can find it in the source at src/test/resources/test-ds.xml -->
 29        <jta-data-source>java:jboss/datasources/TasksJsfQuickstartTestDS</jta-data-source>
 30        <properties>
 31           <!-- Properties for Hibernate -->
 32           <property name="hibernate.hbm2ddl.auto" value="create-drop" />
 33           <property name="hibernate.show_sql" value="false" />
 34        </properties>
 35     </persistence-unit>
 36  </persistence>

```
### #11 - javaee-to-jakarta-namespaces-00054
* Category: mandatory
* Effort: 1
* Description: Replace the Java EE version with the Jakarta equivalent
* Labels: konveyor.io/source, konveyor.io/target=eap, konveyor.io/target=eap8, konveyor.io/target=jakarta-ee, konveyor.io/target=jakarta-ee9+
* Incidents
  * file:///tmp/source-code/src/test/resources/META-INF/test-persistence.xml
      * Line Number: 18
      * Message: '`validation-configuration-2.0`: In the root tag, replace the `version` attribute value with `3.0`'
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
 18  <persistence version="2.0"
 19     xmlns="http://java.sun.com/xml/ns/persistence" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 20     xsi:schemaLocation="
 21          http://java.sun.com/xml/ns/persistence
 22          http://java.sun.com/xml/ns/persistence/persistence_2_0.xsd">
 23     <persistence-unit name="primary">
 24        <!-- We use a different datasource for tests, so as to not overwrite
 25           production data. This is an unmanaged data source, backed by H2, an in memory
 26           database. Production applications should use a managed datasource. -->
 27        <!-- The datasource is deployed as WEB-INF/test-ds.xml,
 28           you can find it in the source at src/test/resources/test-ds.xml -->
 29        <jta-data-source>java:jboss/datasources/TasksJsfQuickstartTestDS</jta-data-source>
 30        <properties>
 31           <!-- Properties for Hibernate -->
 32           <property name="hibernate.hbm2ddl.auto" value="create-drop" />
 33           <property name="hibernate.show_sql" value="false" />
 34        </properties>
 35     </persistence-unit>
 36  </persistence>

```
### #12 - javaee-to-jakarta-namespaces-00055
* Category: mandatory
* Effort: 1
* Description: Replace the Java EE version with the Jakarta equivalent
* Labels: konveyor.io/source, konveyor.io/target=eap, konveyor.io/target=eap8, konveyor.io/target=jakarta-ee, konveyor.io/target=jakarta-ee9+
* Incidents
  * file:///tmp/source-code/src/main/resources/META-INF/persistence.xml
      * Line Number: 18
      * Message: '`orm_2_1`: In the root tag, replace the `version` attribute value with `3.0`'
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
 18  <persistence version="2.1"
 19     xmlns="http://xmlns.jcp.org/xml/ns/persistence" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 20     xsi:schemaLocation="
 21          http://xmlns.jcp.org/xml/ns/persistence
 22          http://xmlns.jcp.org/xml/ns/persistence/persistence_2_1.xsd">
 23     <persistence-unit name="primary">
 24        <!-- We use a different datasource for tests, so as to not overwrite
 25           production data. This is an unmanaged data source, backed by H2, an in memory
 26           database. Production applications should use a managed datasource. -->
 27        <!-- The datasource is deployed as WEB-INF/test-ds.xml,
 28           you can find it in the source at src/test/resources/test-ds.xml -->
 29        <jta-data-source>java:jboss/datasources/TasksJsfQuickstartDS</jta-data-source>
 30        <properties>
 31           <!-- Properties for Hibernate -->
 32           <property name="hibernate.hbm2ddl.auto" value="create-drop" />
 33           <property name="hibernate.show_sql" value="false" />
 34        </properties>
 35     </persistence-unit>
 36  </persistence>

```
### #13 - javaee-to-jakarta-namespaces-00056
* Category: mandatory
* Effort: 1
* Description: Replace the Java EE version with the Jakarta equivalent
* Labels: konveyor.io/source, konveyor.io/target=eap, konveyor.io/target=eap8, konveyor.io/target=jakarta-ee, konveyor.io/target=jakarta-ee9+
* Incidents
  * file:///tmp/source-code/src/main/webapp/WEB-INF/faces-config.xml
      * Line Number: 18
      * Message: '`orm_2_2`: In the root tag, replace the `version` attribute value with `3.0`'
      * Code Snippet:
```java
  1  <?xml version="1.0"?>
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
 18  <faces-config version="2.2" xmlns="http://xmlns.jcp.org/xml/ns/javaee" xmlns:xi="http://www.w3.org/2001/XInclude"
 19      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-facesconfig_2_2.xsd">
 20  
 21      <navigation-rule>
 22          <from-view-id>/index.xhtml</from-view-id>
 23          <navigation-case>
 24              <from-action>#{authController.authenticate(username)}</from-action>
 25              <if>#{authController.logged}</if>
 26              <to-view-id>/tasks.xhtml</to-view-id>
 27              <redirect />
 28          </navigation-case>
 29      </navigation-rule>
 30  
 31      <navigation-rule>
 32          <from-view-id>/tasks.xhtml</from-view-id>
 33          <navigation-case>
 34              <from-action>#{authController.logout}</from-action>
 35              <if>#{!authController.logged}</if>
 36              <to-view-id>/index.xhtml</to-view-id>
 37              <redirect />
 38          </navigation-case>
 39      </navigation-rule>
 40  
 41  </faces-config>

```
### #14 - javax-to-jakarta-import-00001
* Category: mandatory
* Effort: 1
* Description: The package 'javax' has been replaced by 'jakarta'.
* Labels: konveyor.io/source, konveyor.io/target=eap, konveyor.io/target=eap8, konveyor.io/target=jakarta-ee, konveyor.io/target=jakarta-ee9+
* Incidents
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/tasksJsf/AuthController.java
      * Line Number: 19
      * Message: 'Replace the `javax.enterprise` import statement with `jakarta.enterprise`'
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
```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/tasksJsf/AuthController.java
      * Line Number: 20
      * Message: 'Replace the `javax.enterprise` import statement with `jakarta.enterprise`'
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
```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/tasksJsf/AuthController.java
      * Line Number: 21
      * Message: 'Replace the `javax.enterprise` import statement with `jakarta.enterprise`'
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
```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/tasksJsf/AuthController.java
      * Line Number: 22
      * Message: 'Replace the `javax.faces` import statement with `jakarta.faces`'
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
```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/tasksJsf/AuthController.java
      * Line Number: 23
      * Message: 'Replace the `javax.faces` import statement with `jakarta.faces`'
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
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/tasksJsf/AuthController.java
      * Line Number: 24
      * Message: 'Replace the `javax.inject` import statement with `jakarta.inject`'
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
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/tasksJsf/AuthController.java
      * Line Number: 25
      * Message: 'Replace the `javax.inject` import statement with `jakarta.inject`'
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
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/tasksJsf/Authentication.java
      * Line Number: 21
      * Message: 'Replace the `javax.enterprise` import statement with `jakarta.enterprise`'
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
 22  
 23  /**
 24   * Store for current authenticated user
 25   *
 26   * @author Lukas Fryc
 27   *
 28   */
 29  @SuppressWarnings("serial")
 30  @ConversationScoped
 31  public class Authentication implements Serializable {
 32  
 33      private User currentUser;
 34  
 35      public User getCurrentUser() {
 36          return currentUser;
 37      }
 38  
 39      public void setCurrentUser(User user) {
 40          currentUser = user;
 41      }
 42  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/tasksJsf/CurrentTask.java
      * Line Number: 24
      * Message: 'Replace the `javax.inject` import statement with `jakarta.inject`'
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
 19  import java.lang.annotation.ElementType;
 20  import java.lang.annotation.Retention;
 21  import java.lang.annotation.RetentionPolicy;
 22  import java.lang.annotation.Target;
 23  
 24  import javax.inject.Qualifier;
 25  
 26  /**
 27   * Qualifier for current task
 28   *
 29   * @author Lukas Fryc
 30   *
 31   */
 32  @Qualifier
 33  @Target({ ElementType.TYPE, ElementType.METHOD, ElementType.FIELD, ElementType.PARAMETER })
 34  @Retention(RetentionPolicy.RUNTIME)
 35  public @interface CurrentTask {
 36  
 37  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/tasksJsf/CurrentTaskStore.java
      * Line Number: 21
      * Message: 'Replace the `javax.enterprise` import statement with `jakarta.enterprise`'
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
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/tasksJsf/CurrentTaskStore.java
      * Line Number: 22
      * Message: 'Replace the `javax.enterprise` import statement with `jakarta.enterprise`'
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
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/tasksJsf/CurrentTaskStore.java
      * Line Number: 23
      * Message: 'Replace the `javax.inject` import statement with `jakarta.inject`'
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
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/tasksJsf/CurrentUser.java
      * Line Number: 24
      * Message: 'Replace the `javax.inject` import statement with `jakarta.inject`'
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
 19  import java.lang.annotation.ElementType;
 20  import java.lang.annotation.Retention;
 21  import java.lang.annotation.RetentionPolicy;
 22  import java.lang.annotation.Target;
 23  
 24  import javax.inject.Qualifier;
 25  
 26  /**
 27   * Qualifier for current user
 28   *
 29   * @author Lukas Fryc
 30   *
 31   */
 32  @Qualifier
 33  @Target({ ElementType.TYPE, ElementType.METHOD, ElementType.FIELD, ElementType.PARAMETER })
 34  @Retention(RetentionPolicy.RUNTIME)
 35  public @interface CurrentUser {
 36  
 37  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/tasksJsf/Resources.java
      * Line Number: 21
      * Message: 'Replace the `javax.ejb` import statement with `jakarta.ejb`'
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
      * Line Number: 22
      * Message: 'Replace the `javax.enterprise` import statement with `jakarta.enterprise`'
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
      * Line Number: 23
      * Message: 'Replace the `javax.enterprise` import statement with `jakarta.enterprise`'
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
      * Line Number: 24
      * Message: 'Replace the `javax.enterprise` import statement with `jakarta.enterprise`'
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
      * Line Number: 25
      * Message: 'Replace the `javax.faces` import statement with `jakarta.faces`'
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
      * Line Number: 26
      * Message: 'Replace the `javax.persistence` import statement with `jakarta.persistence`'
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
      * Line Number: 27
      * Message: 'Replace the `javax.persistence` import statement with `jakarta.persistence`'
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
      * Line Number: 28
      * Message: 'Replace the `javax.persistence` import statement with `jakarta.persistence`'
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
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/tasksJsf/Task.java
      * Line Number: 19
      * Message: 'Replace the `javax.persistence` import statement with `jakarta.persistence`'
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
 19  import static javax.persistence.GenerationType.IDENTITY;
 20  
 21  import java.io.Serializable;
 22  
 23  import javax.persistence.Entity;
 24  import javax.persistence.GeneratedValue;
 25  import javax.persistence.Id;
 26  import javax.persistence.ManyToOne;
 27  
 28  /**
 29   * User's task entity
 30   *
 31   * @author Oliver Kiss
 32   */
 33  @SuppressWarnings("serial")
 34  @Entity
 35  public class Task implements Serializable {
 36  
 37      @Id
 38      @GeneratedValue(strategy = IDENTITY)
 39      private Long id;
 40  
 41      @ManyToOne
 42      private User owner;
 43  
 44      private String title;
 45  
 46      public Task() {
 47      }
 48  
 49      public Task(String title) {
 50          super();
 51          this.title = title;
 52      }
 53  
 54      public Long getId() {
 55          return id;
 56      }
 57  
 58      public void setId(Long id) {
 59          this.id = id;
 60      }
 61  
 62      public User getOwner() {
 63          return owner;
 64      }
 65  
 66      public void setOwner(User owner) {
 67          this.owner = owner;
 68      }
 69  
 70      public String getTitle() {
 71          return title;
 72      }
 73  
 74      public void setTitle(String title) {
 75          this.title = title;
 76      }
 77  
 78      @Override
 79      public int hashCode() {
 80          final int prime = 31;
 81          int result = 1;
 82          result = prime * result + ((owner == null) ? 0 : owner.hashCode());
 83          result = prime * result + ((title == null) ? 0 : title.hashCode());
 84          return result;
 85      }
 86  
 87      @Override
 88      public boolean equals(Object obj) {
 89          if (this == obj) {
 90              return true;
 91          }
 92          if (obj == null) {
 93              return false;
 94          }
 95          if (getClass() != obj.getClass()) {
 96              return false;
 97          }
 98          Task other = (Task) obj;
 99          if (owner == null) {
100              if (other.owner != null) {
101                  return false;
102              }
103          } else if (!owner.equals(other.owner)) {
104              return false;
105          }
106          if (title == null) {
107              if (other.title != null) {
108                  return false;
109              }
110          } else if (!title.equals(other.title)) {
111              return false;
112          }
113          return true;
114      }
115  
116  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/tasksJsf/Task.java
      * Line Number: 23
      * Message: 'Replace the `javax.persistence` import statement with `jakarta.persistence`'
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
 19  import static javax.persistence.GenerationType.IDENTITY;
 20  
 21  import java.io.Serializable;
 22  
 23  import javax.persistence.Entity;
 24  import javax.persistence.GeneratedValue;
 25  import javax.persistence.Id;
 26  import javax.persistence.ManyToOne;
 27  
 28  /**
 29   * User's task entity
 30   *
 31   * @author Oliver Kiss
 32   */
 33  @SuppressWarnings("serial")
 34  @Entity
 35  public class Task implements Serializable {
 36  
 37      @Id
 38      @GeneratedValue(strategy = IDENTITY)
 39      private Long id;
 40  
 41      @ManyToOne
 42      private User owner;
 43  
 44      private String title;
 45  
 46      public Task() {
 47      }
 48  
 49      public Task(String title) {
 50          super();
 51          this.title = title;
 52      }
 53  
 54      public Long getId() {
 55          return id;
 56      }
 57  
 58      public void setId(Long id) {
 59          this.id = id;
 60      }
 61  
 62      public User getOwner() {
 63          return owner;
 64      }
 65  
 66      public void setOwner(User owner) {
 67          this.owner = owner;
 68      }
 69  
 70      public String getTitle() {
 71          return title;
 72      }
 73  
 74      public void setTitle(String title) {
 75          this.title = title;
 76      }
 77  
 78      @Override
 79      public int hashCode() {
 80          final int prime = 31;
 81          int result = 1;
 82          result = prime * result + ((owner == null) ? 0 : owner.hashCode());
 83          result = prime * result + ((title == null) ? 0 : title.hashCode());
 84          return result;
 85      }
 86  
 87      @Override
 88      public boolean equals(Object obj) {
 89          if (this == obj) {
 90              return true;
 91          }
 92          if (obj == null) {
 93              return false;
 94          }
 95          if (getClass() != obj.getClass()) {
 96              return false;
 97          }
 98          Task other = (Task) obj;
 99          if (owner == null) {
100              if (other.owner != null) {
101                  return false;
102              }
103          } else if (!owner.equals(other.owner)) {
104              return false;
105          }
106          if (title == null) {
107              if (other.title != null) {
108                  return false;
109              }
110          } else if (!title.equals(other.title)) {
111              return false;
112          }
113          return true;
114      }
115  
116  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/tasksJsf/Task.java
      * Line Number: 24
      * Message: 'Replace the `javax.persistence` import statement with `jakarta.persistence`'
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
 19  import static javax.persistence.GenerationType.IDENTITY;
 20  
 21  import java.io.Serializable;
 22  
 23  import javax.persistence.Entity;
 24  import javax.persistence.GeneratedValue;
 25  import javax.persistence.Id;
 26  import javax.persistence.ManyToOne;
 27  
 28  /**
 29   * User's task entity
 30   *
 31   * @author Oliver Kiss
 32   */
 33  @SuppressWarnings("serial")
 34  @Entity
 35  public class Task implements Serializable {
 36  
 37      @Id
 38      @GeneratedValue(strategy = IDENTITY)
 39      private Long id;
 40  
 41      @ManyToOne
 42      private User owner;
 43  
 44      private String title;
 45  
 46      public Task() {
 47      }
 48  
 49      public Task(String title) {
 50          super();
 51          this.title = title;
 52      }
 53  
 54      public Long getId() {
 55          return id;
 56      }
 57  
 58      public void setId(Long id) {
 59          this.id = id;
 60      }
 61  
 62      public User getOwner() {
 63          return owner;
 64      }
 65  
 66      public void setOwner(User owner) {
 67          this.owner = owner;
 68      }
 69  
 70      public String getTitle() {
 71          return title;
 72      }
 73  
 74      public void setTitle(String title) {
 75          this.title = title;
 76      }
 77  
 78      @Override
 79      public int hashCode() {
 80          final int prime = 31;
 81          int result = 1;
 82          result = prime * result + ((owner == null) ? 0 : owner.hashCode());
 83          result = prime * result + ((title == null) ? 0 : title.hashCode());
 84          return result;
 85      }
 86  
 87      @Override
 88      public boolean equals(Object obj) {
 89          if (this == obj) {
 90              return true;
 91          }
 92          if (obj == null) {
 93              return false;
 94          }
 95          if (getClass() != obj.getClass()) {
 96              return false;
 97          }
 98          Task other = (Task) obj;
 99          if (owner == null) {
100              if (other.owner != null) {
101                  return false;
102              }
103          } else if (!owner.equals(other.owner)) {
104              return false;
105          }
106          if (title == null) {
107              if (other.title != null) {
108                  return false;
109              }
110          } else if (!title.equals(other.title)) {
111              return false;
112          }
113          return true;
114      }
115  
116  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/tasksJsf/Task.java
      * Line Number: 25
      * Message: 'Replace the `javax.persistence` import statement with `jakarta.persistence`'
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
 19  import static javax.persistence.GenerationType.IDENTITY;
 20  
 21  import java.io.Serializable;
 22  
 23  import javax.persistence.Entity;
 24  import javax.persistence.GeneratedValue;
 25  import javax.persistence.Id;
 26  import javax.persistence.ManyToOne;
 27  
 28  /**
 29   * User's task entity
 30   *
 31   * @author Oliver Kiss
 32   */
 33  @SuppressWarnings("serial")
 34  @Entity
 35  public class Task implements Serializable {
 36  
 37      @Id
 38      @GeneratedValue(strategy = IDENTITY)
 39      private Long id;
 40  
 41      @ManyToOne
 42      private User owner;
 43  
 44      private String title;
 45  
 46      public Task() {
 47      }
 48  
 49      public Task(String title) {
 50          super();
 51          this.title = title;
 52      }
 53  
 54      public Long getId() {
 55          return id;
 56      }
 57  
 58      public void setId(Long id) {
 59          this.id = id;
 60      }
 61  
 62      public User getOwner() {
 63          return owner;
 64      }
 65  
 66      public void setOwner(User owner) {
 67          this.owner = owner;
 68      }
 69  
 70      public String getTitle() {
 71          return title;
 72      }
 73  
 74      public void setTitle(String title) {
 75          this.title = title;
 76      }
 77  
 78      @Override
 79      public int hashCode() {
 80          final int prime = 31;
 81          int result = 1;
 82          result = prime * result + ((owner == null) ? 0 : owner.hashCode());
 83          result = prime * result + ((title == null) ? 0 : title.hashCode());
 84          return result;
 85      }
 86  
 87      @Override
 88      public boolean equals(Object obj) {
 89          if (this == obj) {
 90              return true;
 91          }
 92          if (obj == null) {
 93              return false;
 94          }
 95          if (getClass() != obj.getClass()) {
 96              return false;
 97          }
 98          Task other = (Task) obj;
 99          if (owner == null) {
100              if (other.owner != null) {
101                  return false;
102              }
103          } else if (!owner.equals(other.owner)) {
104              return false;
105          }
106          if (title == null) {
107              if (other.title != null) {
108                  return false;
109              }
110          } else if (!title.equals(other.title)) {
111              return false;
112          }
113          return true;
114      }
115  
116  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/tasksJsf/Task.java
      * Line Number: 26
      * Message: 'Replace the `javax.persistence` import statement with `jakarta.persistence`'
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
 19  import static javax.persistence.GenerationType.IDENTITY;
 20  
 21  import java.io.Serializable;
 22  
 23  import javax.persistence.Entity;
 24  import javax.persistence.GeneratedValue;
 25  import javax.persistence.Id;
 26  import javax.persistence.ManyToOne;
 27  
 28  /**
 29   * User's task entity
 30   *
 31   * @author Oliver Kiss
 32   */
 33  @SuppressWarnings("serial")
 34  @Entity
 35  public class Task implements Serializable {
 36  
 37      @Id
 38      @GeneratedValue(strategy = IDENTITY)
 39      private Long id;
 40  
 41      @ManyToOne
 42      private User owner;
 43  
 44      private String title;
 45  
 46      public Task() {
 47      }
 48  
 49      public Task(String title) {
 50          super();
 51          this.title = title;
 52      }
 53  
 54      public Long getId() {
 55          return id;
 56      }
 57  
 58      public void setId(Long id) {
 59          this.id = id;
 60      }
 61  
 62      public User getOwner() {
 63          return owner;
 64      }
 65  
 66      public void setOwner(User owner) {
 67          this.owner = owner;
 68      }
 69  
 70      public String getTitle() {
 71          return title;
 72      }
 73  
 74      public void setTitle(String title) {
 75          this.title = title;
 76      }
 77  
 78      @Override
 79      public int hashCode() {
 80          final int prime = 31;
 81          int result = 1;
 82          result = prime * result + ((owner == null) ? 0 : owner.hashCode());
 83          result = prime * result + ((title == null) ? 0 : title.hashCode());
 84          return result;
 85      }
 86  
 87      @Override
 88      public boolean equals(Object obj) {
 89          if (this == obj) {
 90              return true;
 91          }
 92          if (obj == null) {
 93              return false;
 94          }
 95          if (getClass() != obj.getClass()) {
 96              return false;
 97          }
 98          Task other = (Task) obj;
 99          if (owner == null) {
100              if (other.owner != null) {
101                  return false;
102              }
103          } else if (!owner.equals(other.owner)) {
104              return false;
105          }
106          if (title == null) {
107              if (other.title != null) {
108                  return false;
109              }
110          } else if (!title.equals(other.title)) {
111              return false;
112          }
113          return true;
114      }
115  
116  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/tasksJsf/TaskController.java
      * Line Number: 19
      * Message: 'Replace the `javax.enterprise` import statement with `jakarta.enterprise`'
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
 19  import javax.enterprise.context.RequestScoped;
 20  import javax.enterprise.inject.Instance;
 21  import javax.inject.Inject;
 22  import javax.inject.Named;
 23  
 24  /**
 25   * <p>
 26   * Basic operations for tasks owned by current user - additions, deletions/
 27   * </p>
 28   *
 29   * @author Lukas Fryc
 30   *
 31   */
 32  @RequestScoped
 33  @Named
 34  public class TaskController {
 35  
 36      @Inject
 37      private TaskDao taskDao;
 38  
 39      @Inject
 40      private TaskList taskList;
 41  
 42      /**
 43       * Injects current user, which is provided by {@link AuthController}.
 44       */
 45      @Inject
 46      @CurrentUser
 47      private Instance<User> currentUser;
 48  
 49      /**
 50       * Injects current user stored in the conversation scope
 51       */
 52      @Inject
 53      private CurrentTaskStore currentTaskStore;
 54  
 55      /**
 56       * Set the current task to the context
 57       *
 58       * @param task current task to be set to context
 59       */
 60      public void setCurrentTask(Task task) {
 61          currentTaskStore.set(task);
 62      }
 63  
 64      /**
 65       * Creates new task and, if no task is selected as current, selects it.
 66       *
 67       * @param taskTitle
 68       */
 69      public void createTask(String taskTitle) {
 70          taskList.invalidate();
 71          Task task = new Task(taskTitle);
 72          taskDao.createTask(currentUser.get(), task);
 73          if (currentTaskStore.get() == null) {
 74              currentTaskStore.set(task);
 75          }
 76      }
 77  
 78      /**
 79       * Deletes given task
 80       *
 81       * @param task to delete
 82       */
 83      public void deleteTask(Task task) {
 84          taskList.invalidate();
 85          if (task.equals(currentTaskStore.get())) {
 86              currentTaskStore.unset();
 87          }
 88          taskDao.deleteTask(task);
 89      }
 90  
 91      /**
 92       * Deletes given task
 93       *
 94       * @param task to delete
 95       */
 96      public void deleteCurrentTask() {
 97          deleteTask(currentTaskStore.get());
 98      }
 99  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/tasksJsf/TaskController.java
      * Line Number: 20
      * Message: 'Replace the `javax.enterprise` import statement with `jakarta.enterprise`'
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
 19  import javax.enterprise.context.RequestScoped;
 20  import javax.enterprise.inject.Instance;
 21  import javax.inject.Inject;
 22  import javax.inject.Named;
 23  
 24  /**
 25   * <p>
 26   * Basic operations for tasks owned by current user - additions, deletions/
 27   * </p>
 28   *
 29   * @author Lukas Fryc
 30   *
 31   */
 32  @RequestScoped
 33  @Named
 34  public class TaskController {
 35  
 36      @Inject
 37      private TaskDao taskDao;
 38  
 39      @Inject
 40      private TaskList taskList;
 41  
 42      /**
 43       * Injects current user, which is provided by {@link AuthController}.
 44       */
 45      @Inject
 46      @CurrentUser
 47      private Instance<User> currentUser;
 48  
 49      /**
 50       * Injects current user stored in the conversation scope
 51       */
 52      @Inject
 53      private CurrentTaskStore currentTaskStore;
 54  
 55      /**
 56       * Set the current task to the context
 57       *
 58       * @param task current task to be set to context
 59       */
 60      public void setCurrentTask(Task task) {
 61          currentTaskStore.set(task);
 62      }
 63  
 64      /**
 65       * Creates new task and, if no task is selected as current, selects it.
 66       *
 67       * @param taskTitle
 68       */
 69      public void createTask(String taskTitle) {
 70          taskList.invalidate();
 71          Task task = new Task(taskTitle);
 72          taskDao.createTask(currentUser.get(), task);
 73          if (currentTaskStore.get() == null) {
 74              currentTaskStore.set(task);
 75          }
 76      }
 77  
 78      /**
 79       * Deletes given task
 80       *
 81       * @param task to delete
 82       */
 83      public void deleteTask(Task task) {
 84          taskList.invalidate();
 85          if (task.equals(currentTaskStore.get())) {
 86              currentTaskStore.unset();
 87          }
 88          taskDao.deleteTask(task);
 89      }
 90  
 91      /**
 92       * Deletes given task
 93       *
 94       * @param task to delete
 95       */
 96      public void deleteCurrentTask() {
 97          deleteTask(currentTaskStore.get());
 98      }
 99  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/tasksJsf/TaskController.java
      * Line Number: 21
      * Message: 'Replace the `javax.inject` import statement with `jakarta.inject`'
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
 19  import javax.enterprise.context.RequestScoped;
 20  import javax.enterprise.inject.Instance;
 21  import javax.inject.Inject;
 22  import javax.inject.Named;
 23  
 24  /**
 25   * <p>
 26   * Basic operations for tasks owned by current user - additions, deletions/
 27   * </p>
 28   *
 29   * @author Lukas Fryc
 30   *
 31   */
 32  @RequestScoped
 33  @Named
 34  public class TaskController {
 35  
 36      @Inject
 37      private TaskDao taskDao;
 38  
 39      @Inject
 40      private TaskList taskList;
 41  
 42      /**
 43       * Injects current user, which is provided by {@link AuthController}.
 44       */
 45      @Inject
 46      @CurrentUser
 47      private Instance<User> currentUser;
 48  
 49      /**
 50       * Injects current user stored in the conversation scope
 51       */
 52      @Inject
 53      private CurrentTaskStore currentTaskStore;
 54  
 55      /**
 56       * Set the current task to the context
 57       *
 58       * @param task current task to be set to context
 59       */
 60      public void setCurrentTask(Task task) {
 61          currentTaskStore.set(task);
 62      }
 63  
 64      /**
 65       * Creates new task and, if no task is selected as current, selects it.
 66       *
 67       * @param taskTitle
 68       */
 69      public void createTask(String taskTitle) {
 70          taskList.invalidate();
 71          Task task = new Task(taskTitle);
 72          taskDao.createTask(currentUser.get(), task);
 73          if (currentTaskStore.get() == null) {
 74              currentTaskStore.set(task);
 75          }
 76      }
 77  
 78      /**
 79       * Deletes given task
 80       *
 81       * @param task to delete
 82       */
 83      public void deleteTask(Task task) {
 84          taskList.invalidate();
 85          if (task.equals(currentTaskStore.get())) {
 86              currentTaskStore.unset();
 87          }
 88          taskDao.deleteTask(task);
 89      }
 90  
 91      /**
 92       * Deletes given task
 93       *
 94       * @param task to delete
 95       */
 96      public void deleteCurrentTask() {
 97          deleteTask(currentTaskStore.get());
 98      }
 99  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/tasksJsf/TaskController.java
      * Line Number: 22
      * Message: 'Replace the `javax.inject` import statement with `jakarta.inject`'
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
 19  import javax.enterprise.context.RequestScoped;
 20  import javax.enterprise.inject.Instance;
 21  import javax.inject.Inject;
 22  import javax.inject.Named;
 23  
 24  /**
 25   * <p>
 26   * Basic operations for tasks owned by current user - additions, deletions/
 27   * </p>
 28   *
 29   * @author Lukas Fryc
 30   *
 31   */
 32  @RequestScoped
 33  @Named
 34  public class TaskController {
 35  
 36      @Inject
 37      private TaskDao taskDao;
 38  
 39      @Inject
 40      private TaskList taskList;
 41  
 42      /**
 43       * Injects current user, which is provided by {@link AuthController}.
 44       */
 45      @Inject
 46      @CurrentUser
 47      private Instance<User> currentUser;
 48  
 49      /**
 50       * Injects current user stored in the conversation scope
 51       */
 52      @Inject
 53      private CurrentTaskStore currentTaskStore;
 54  
 55      /**
 56       * Set the current task to the context
 57       *
 58       * @param task current task to be set to context
 59       */
 60      public void setCurrentTask(Task task) {
 61          currentTaskStore.set(task);
 62      }
 63  
 64      /**
 65       * Creates new task and, if no task is selected as current, selects it.
 66       *
 67       * @param taskTitle
 68       */
 69      public void createTask(String taskTitle) {
 70          taskList.invalidate();
 71          Task task = new Task(taskTitle);
 72          taskDao.createTask(currentUser.get(), task);
 73          if (currentTaskStore.get() == null) {
 74              currentTaskStore.set(task);
 75          }
 76      }
 77  
 78      /**
 79       * Deletes given task
 80       *
 81       * @param task to delete
 82       */
 83      public void deleteTask(Task task) {
 84          taskList.invalidate();
 85          if (task.equals(currentTaskStore.get())) {
 86              currentTaskStore.unset();
 87          }
 88          taskDao.deleteTask(task);
 89      }
 90  
 91      /**
 92       * Deletes given task
 93       *
 94       * @param task to delete
 95       */
 96      public void deleteCurrentTask() {
 97          deleteTask(currentTaskStore.get());
 98      }
 99  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/tasksJsf/TaskDao.java
      * Line Number: 21
      * Message: 'Replace the `javax.ejb` import statement with `jakarta.ejb`'
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
 19  import java.util.List;
 20  
 21  import javax.ejb.Local;
 22  
 23  /**
 24   * Basic operations for manipulation of tasks
 25   *
 26   * @author Lukas Fryc
 27   *
 28   */
 29  @Local
 30  public interface TaskDao {
 31  
 32      void createTask(User user, Task task);
 33  
 34      List<Task> getAll(User user);
 35  
 36      List<Task> getRange(User user, int offset, int count);
 37  
 38      List<Task> getForTitle(User user, String title);
 39  
 40      void deleteTask(Task task);
 41  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/tasksJsf/TaskDaoImpl.java
      * Line Number: 21
      * Message: 'Replace the `javax.ejb` import statement with `jakarta.ejb`'
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
 19  import java.util.List;
 20  
 21  import javax.ejb.Stateful;
 22  import javax.inject.Inject;
 23  import javax.persistence.EntityManager;
 24  import javax.persistence.TypedQuery;
 25  
 26  /**
 27   * Provides functionality for manipulation with tasks using the persistence context from {@link Resources}.
 28   *
 29   * @author Lukas Fryc
 30   * @author Oliver Kiss
 31   *
 32   */
 33  @Stateful
 34  public class TaskDaoImpl implements TaskDao {
 35  
 36      @Inject
 37      private EntityManager em;
 38  
 39      @Override
 40      public void createTask(User user, Task task) {
 41          if (!em.contains(user)) {
 42              user = em.merge(user);
 43          }
 44          user.getTasks().add(task);
 45          task.setOwner(user);
 46          em.persist(task);
 47      }
 48  
 49      @Override
 50      public List<Task> getAll(User user) {
 51          TypedQuery<Task> query = querySelectAllTasksFromUser(user);
 52          return query.getResultList();
 53      }
 54  
 55      @Override
 56      public List<Task> getRange(User user, int offset, int count) {
 57          TypedQuery<Task> query = querySelectAllTasksFromUser(user);
 58          query.setMaxResults(count);
 59          query.setFirstResult(offset);
 60          return query.getResultList();
 61      }
 62  
 63      @Override
 64      public List<Task> getForTitle(User user, String title) {
 65          String lowerCaseTitle = "%" + title.toLowerCase() + "%";
 66          return em.createQuery("SELECT t FROM Task t WHERE t.owner = ?1 AND LOWER(t.title) LIKE ?2", Task.class)
 67              .setParameter(1, user).setParameter(2, lowerCaseTitle).getResultList();
 68      }
 69  
 70      @Override
 71      public void deleteTask(Task task) {
 72          if (!em.contains(task)) {
 73              task = em.merge(task);
 74          }
 75          em.remove(task);
 76      }
 77  
 78      private TypedQuery<Task> querySelectAllTasksFromUser(User user) {
 79          return em.createQuery("SELECT t FROM Task t WHERE t.owner = ?1", Task.class).setParameter(1, user);
 80      }
 81  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/tasksJsf/TaskDaoImpl.java
      * Line Number: 22
      * Message: 'Replace the `javax.inject` import statement with `jakarta.inject`'
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
 19  import java.util.List;
 20  
 21  import javax.ejb.Stateful;
 22  import javax.inject.Inject;
 23  import javax.persistence.EntityManager;
 24  import javax.persistence.TypedQuery;
 25  
 26  /**
 27   * Provides functionality for manipulation with tasks using the persistence context from {@link Resources}.
 28   *
 29   * @author Lukas Fryc
 30   * @author Oliver Kiss
 31   *
 32   */
 33  @Stateful
 34  public class TaskDaoImpl implements TaskDao {
 35  
 36      @Inject
 37      private EntityManager em;
 38  
 39      @Override
 40      public void createTask(User user, Task task) {
 41          if (!em.contains(user)) {
 42              user = em.merge(user);
 43          }
 44          user.getTasks().add(task);
 45          task.setOwner(user);
 46          em.persist(task);
 47      }
 48  
 49      @Override
 50      public List<Task> getAll(User user) {
 51          TypedQuery<Task> query = querySelectAllTasksFromUser(user);
 52          return query.getResultList();
 53      }
 54  
 55      @Override
 56      public List<Task> getRange(User user, int offset, int count) {
 57          TypedQuery<Task> query = querySelectAllTasksFromUser(user);
 58          query.setMaxResults(count);
 59          query.setFirstResult(offset);
 60          return query.getResultList();
 61      }
 62  
 63      @Override
 64      public List<Task> getForTitle(User user, String title) {
 65          String lowerCaseTitle = "%" + title.toLowerCase() + "%";
 66          return em.createQuery("SELECT t FROM Task t WHERE t.owner = ?1 AND LOWER(t.title) LIKE ?2", Task.class)
 67              .setParameter(1, user).setParameter(2, lowerCaseTitle).getResultList();
 68      }
 69  
 70      @Override
 71      public void deleteTask(Task task) {
 72          if (!em.contains(task)) {
 73              task = em.merge(task);
 74          }
 75          em.remove(task);
 76      }
 77  
 78      private TypedQuery<Task> querySelectAllTasksFromUser(User user) {
 79          return em.createQuery("SELECT t FROM Task t WHERE t.owner = ?1", Task.class).setParameter(1, user);
 80      }
 81  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/tasksJsf/TaskDaoImpl.java
      * Line Number: 23
      * Message: 'Replace the `javax.persistence` import statement with `jakarta.persistence`'
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
 19  import java.util.List;
 20  
 21  import javax.ejb.Stateful;
 22  import javax.inject.Inject;
 23  import javax.persistence.EntityManager;
 24  import javax.persistence.TypedQuery;
 25  
 26  /**
 27   * Provides functionality for manipulation with tasks using the persistence context from {@link Resources}.
 28   *
 29   * @author Lukas Fryc
 30   * @author Oliver Kiss
 31   *
 32   */
 33  @Stateful
 34  public class TaskDaoImpl implements TaskDao {
 35  
 36      @Inject
 37      private EntityManager em;
 38  
 39      @Override
 40      public void createTask(User user, Task task) {
 41          if (!em.contains(user)) {
 42              user = em.merge(user);
 43          }
 44          user.getTasks().add(task);
 45          task.setOwner(user);
 46          em.persist(task);
 47      }
 48  
 49      @Override
 50      public List<Task> getAll(User user) {
 51          TypedQuery<Task> query = querySelectAllTasksFromUser(user);
 52          return query.getResultList();
 53      }
 54  
 55      @Override
 56      public List<Task> getRange(User user, int offset, int count) {
 57          TypedQuery<Task> query = querySelectAllTasksFromUser(user);
 58          query.setMaxResults(count);
 59          query.setFirstResult(offset);
 60          return query.getResultList();
 61      }
 62  
 63      @Override
 64      public List<Task> getForTitle(User user, String title) {
 65          String lowerCaseTitle = "%" + title.toLowerCase() + "%";
 66          return em.createQuery("SELECT t FROM Task t WHERE t.owner = ?1 AND LOWER(t.title) LIKE ?2", Task.class)
 67              .setParameter(1, user).setParameter(2, lowerCaseTitle).getResultList();
 68      }
 69  
 70      @Override
 71      public void deleteTask(Task task) {
 72          if (!em.contains(task)) {
 73              task = em.merge(task);
 74          }
 75          em.remove(task);
 76      }
 77  
 78      private TypedQuery<Task> querySelectAllTasksFromUser(User user) {
 79          return em.createQuery("SELECT t FROM Task t WHERE t.owner = ?1", Task.class).setParameter(1, user);
 80      }
 81  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/tasksJsf/TaskDaoImpl.java
      * Line Number: 24
      * Message: 'Replace the `javax.persistence` import statement with `jakarta.persistence`'
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
 19  import java.util.List;
 20  
 21  import javax.ejb.Stateful;
 22  import javax.inject.Inject;
 23  import javax.persistence.EntityManager;
 24  import javax.persistence.TypedQuery;
 25  
 26  /**
 27   * Provides functionality for manipulation with tasks using the persistence context from {@link Resources}.
 28   *
 29   * @author Lukas Fryc
 30   * @author Oliver Kiss
 31   *
 32   */
 33  @Stateful
 34  public class TaskDaoImpl implements TaskDao {
 35  
 36      @Inject
 37      private EntityManager em;
 38  
 39      @Override
 40      public void createTask(User user, Task task) {
 41          if (!em.contains(user)) {
 42              user = em.merge(user);
 43          }
 44          user.getTasks().add(task);
 45          task.setOwner(user);
 46          em.persist(task);
 47      }
 48  
 49      @Override
 50      public List<Task> getAll(User user) {
 51          TypedQuery<Task> query = querySelectAllTasksFromUser(user);
 52          return query.getResultList();
 53      }
 54  
 55      @Override
 56      public List<Task> getRange(User user, int offset, int count) {
 57          TypedQuery<Task> query = querySelectAllTasksFromUser(user);
 58          query.setMaxResults(count);
 59          query.setFirstResult(offset);
 60          return query.getResultList();
 61      }
 62  
 63      @Override
 64      public List<Task> getForTitle(User user, String title) {
 65          String lowerCaseTitle = "%" + title.toLowerCase() + "%";
 66          return em.createQuery("SELECT t FROM Task t WHERE t.owner = ?1 AND LOWER(t.title) LIKE ?2", Task.class)
 67              .setParameter(1, user).setParameter(2, lowerCaseTitle).getResultList();
 68      }
 69  
 70      @Override
 71      public void deleteTask(Task task) {
 72          if (!em.contains(task)) {
 73              task = em.merge(task);
 74          }
 75          em.remove(task);
 76      }
 77  
 78      private TypedQuery<Task> querySelectAllTasksFromUser(User user) {
 79          return em.createQuery("SELECT t FROM Task t WHERE t.owner = ?1", Task.class).setParameter(1, user);
 80      }
 81  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/tasksJsf/TaskListBean.java
      * Line Number: 21
      * Message: 'Replace the `javax.enterprise` import statement with `jakarta.enterprise`'
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
 19  import java.util.List;
 20  
 21  import javax.enterprise.context.RequestScoped;
 22  import javax.inject.Inject;
 23  import javax.inject.Named;
 24  
 25  /**
 26   * <p>
 27   * Operations with cached list of tasks for current user.
 28   * </p>
 29   *
 30   * <p>
 31   * Delegates to {@link TaskDao} for persistence operations.
 32   * </p>
 33   *
 34   * <p>
 35   * This bean ensures that task list will be obtained at most once per request or additionally after each invalidation (
 36   * {@link #invalidate()}).
 37   * </p>
 38   *
 39   * <p>
 40   * This behavior prevents unnecessary delegations to the persistence layer, since {{@link #getAll()} can be called several times
 41   * per request when used in view layer.
 42   * </p>
 43   *
 44   * @author Lukas Fryc
 45   */
 46  @Named("taskList")
 47  @RequestScoped
 48  public class TaskListBean implements TaskList {
 49  
 50      private List<Task> tasks;
 51  
 52      @Inject
 53      private TaskDao taskDao;
 54  
 55      @Inject
 56      @CurrentUser
 57      private User currentUser;
 58  
 59      @Override
 60      public List<Task> getAll() {
 61          if (tasks == null) {
 62              tasks = taskDao.getAll(currentUser);
 63          }
 64          return tasks;
 65      }
 66  
 67      @Override
 68      public void invalidate() {
 69          tasks = null;
 70      }
 71  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/tasksJsf/TaskListBean.java
      * Line Number: 22
      * Message: 'Replace the `javax.inject` import statement with `jakarta.inject`'
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
 19  import java.util.List;
 20  
 21  import javax.enterprise.context.RequestScoped;
 22  import javax.inject.Inject;
 23  import javax.inject.Named;
 24  
 25  /**
 26   * <p>
 27   * Operations with cached list of tasks for current user.
 28   * </p>
 29   *
 30   * <p>
 31   * Delegates to {@link TaskDao} for persistence operations.
 32   * </p>
 33   *
 34   * <p>
 35   * This bean ensures that task list will be obtained at most once per request or additionally after each invalidation (
 36   * {@link #invalidate()}).
 37   * </p>
 38   *
 39   * <p>
 40   * This behavior prevents unnecessary delegations to the persistence layer, since {{@link #getAll()} can be called several times
 41   * per request when used in view layer.
 42   * </p>
 43   *
 44   * @author Lukas Fryc
 45   */
 46  @Named("taskList")
 47  @RequestScoped
 48  public class TaskListBean implements TaskList {
 49  
 50      private List<Task> tasks;
 51  
 52      @Inject
 53      private TaskDao taskDao;
 54  
 55      @Inject
 56      @CurrentUser
 57      private User currentUser;
 58  
 59      @Override
 60      public List<Task> getAll() {
 61          if (tasks == null) {
 62              tasks = taskDao.getAll(currentUser);
 63          }
 64          return tasks;
 65      }
 66  
 67      @Override
 68      public void invalidate() {
 69          tasks = null;
 70      }
 71  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/tasksJsf/TaskListBean.java
      * Line Number: 23
      * Message: 'Replace the `javax.inject` import statement with `jakarta.inject`'
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
 19  import java.util.List;
 20  
 21  import javax.enterprise.context.RequestScoped;
 22  import javax.inject.Inject;
 23  import javax.inject.Named;
 24  
 25  /**
 26   * <p>
 27   * Operations with cached list of tasks for current user.
 28   * </p>
 29   *
 30   * <p>
 31   * Delegates to {@link TaskDao} for persistence operations.
 32   * </p>
 33   *
 34   * <p>
 35   * This bean ensures that task list will be obtained at most once per request or additionally after each invalidation (
 36   * {@link #invalidate()}).
 37   * </p>
 38   *
 39   * <p>
 40   * This behavior prevents unnecessary delegations to the persistence layer, since {{@link #getAll()} can be called several times
 41   * per request when used in view layer.
 42   * </p>
 43   *
 44   * @author Lukas Fryc
 45   */
 46  @Named("taskList")
 47  @RequestScoped
 48  public class TaskListBean implements TaskList {
 49  
 50      private List<Task> tasks;
 51  
 52      @Inject
 53      private TaskDao taskDao;
 54  
 55      @Inject
 56      @CurrentUser
 57      private User currentUser;
 58  
 59      @Override
 60      public List<Task> getAll() {
 61          if (tasks == null) {
 62              tasks = taskDao.getAll(currentUser);
 63          }
 64          return tasks;
 65      }
 66  
 67      @Override
 68      public void invalidate() {
 69          tasks = null;
 70      }
 71  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/tasksJsf/User.java
      * Line Number: 19
      * Message: 'Replace the `javax.persistence` import statement with `jakarta.persistence`'
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
 19  import static javax.persistence.CascadeType.ALL;
 20  import static javax.persistence.GenerationType.IDENTITY;
 21  
 22  import java.io.Serializable;
 23  import java.util.ArrayList;
 24  import java.util.List;
 25  
 26  import javax.persistence.Column;
 27  import javax.persistence.Entity;
 28  import javax.persistence.GeneratedValue;
 29  import javax.persistence.Id;
 30  import javax.persistence.OneToMany;
 31  
 32  /**
 33   * User entity
 34   *
 35   * @author Oliver Kiss
 36   */
 37  @SuppressWarnings("serial")
 38  @Entity
 39  public class User implements Serializable {
 40  
 41      @Id
 42      @GeneratedValue(strategy = IDENTITY)
 43      private Long id;
 44  
 45      @Column(unique = true)
 46      private String username;
 47  
 48      @OneToMany(cascade = ALL, mappedBy = "owner")
 49      @Column(updatable = false)
 50      private List<Task> tasks = new ArrayList<>();
 51  
 52      public User() {
 53      }
 54  
 55      public User(String username) {
 56          this.username = username;
 57      }
 58  
 59      public Long getId() {
 60          return id;
 61      }
 62  
 63      public void setId(Long id) {
 64          this.id = id;
 65      }
 66  
 67      public String getUsername() {
 68          return username;
 69      }
 70  
 71      public void setUsername(String username) {
 72          this.username = username;
 73      }
 74  
 75      public List<Task> getTasks() {
 76          return tasks;
 77      }
 78  
 79      public void setTasks(List<Task> tasks) {
 80          this.tasks = tasks;
 81      }
 82  
 83      @Override
 84      public int hashCode() {
 85          final int prime = 31;
 86          int result = 1;
 87          result = prime * result + ((username == null) ? 0 : username.hashCode());
 88          return result;
 89      }
 90  
 91      @Override
 92      public boolean equals(Object obj) {
 93          if (this == obj)
 94              return true;
 95          if (obj == null)
 96              return false;
 97          if (getClass() != obj.getClass())
 98              return false;
 99          User other = (User) obj;
100          if (username == null) {
101              if (other.username != null)
102                  return false;
103          } else if (!username.equals(other.username))
104              return false;
105          return true;
106      }
107  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/tasksJsf/User.java
      * Line Number: 20
      * Message: 'Replace the `javax.persistence` import statement with `jakarta.persistence`'
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
 19  import static javax.persistence.CascadeType.ALL;
 20  import static javax.persistence.GenerationType.IDENTITY;
 21  
 22  import java.io.Serializable;
 23  import java.util.ArrayList;
 24  import java.util.List;
 25  
 26  import javax.persistence.Column;
 27  import javax.persistence.Entity;
 28  import javax.persistence.GeneratedValue;
 29  import javax.persistence.Id;
 30  import javax.persistence.OneToMany;
 31  
 32  /**
 33   * User entity
 34   *
 35   * @author Oliver Kiss
 36   */
 37  @SuppressWarnings("serial")
 38  @Entity
 39  public class User implements Serializable {
 40  
 41      @Id
 42      @GeneratedValue(strategy = IDENTITY)
 43      private Long id;
 44  
 45      @Column(unique = true)
 46      private String username;
 47  
 48      @OneToMany(cascade = ALL, mappedBy = "owner")
 49      @Column(updatable = false)
 50      private List<Task> tasks = new ArrayList<>();
 51  
 52      public User() {
 53      }
 54  
 55      public User(String username) {
 56          this.username = username;
 57      }
 58  
 59      public Long getId() {
 60          return id;
 61      }
 62  
 63      public void setId(Long id) {
 64          this.id = id;
 65      }
 66  
 67      public String getUsername() {
 68          return username;
 69      }
 70  
 71      public void setUsername(String username) {
 72          this.username = username;
 73      }
 74  
 75      public List<Task> getTasks() {
 76          return tasks;
 77      }
 78  
 79      public void setTasks(List<Task> tasks) {
 80          this.tasks = tasks;
 81      }
 82  
 83      @Override
 84      public int hashCode() {
 85          final int prime = 31;
 86          int result = 1;
 87          result = prime * result + ((username == null) ? 0 : username.hashCode());
 88          return result;
 89      }
 90  
 91      @Override
 92      public boolean equals(Object obj) {
 93          if (this == obj)
 94              return true;
 95          if (obj == null)
 96              return false;
 97          if (getClass() != obj.getClass())
 98              return false;
 99          User other = (User) obj;
100          if (username == null) {
101              if (other.username != null)
102                  return false;
103          } else if (!username.equals(other.username))
104              return false;
105          return true;
106      }
107  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/tasksJsf/User.java
      * Line Number: 26
      * Message: 'Replace the `javax.persistence` import statement with `jakarta.persistence`'
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
 19  import static javax.persistence.CascadeType.ALL;
 20  import static javax.persistence.GenerationType.IDENTITY;
 21  
 22  import java.io.Serializable;
 23  import java.util.ArrayList;
 24  import java.util.List;
 25  
 26  import javax.persistence.Column;
 27  import javax.persistence.Entity;
 28  import javax.persistence.GeneratedValue;
 29  import javax.persistence.Id;
 30  import javax.persistence.OneToMany;
 31  
 32  /**
 33   * User entity
 34   *
 35   * @author Oliver Kiss
 36   */
 37  @SuppressWarnings("serial")
 38  @Entity
 39  public class User implements Serializable {
 40  
 41      @Id
 42      @GeneratedValue(strategy = IDENTITY)
 43      private Long id;
 44  
 45      @Column(unique = true)
 46      private String username;
 47  
 48      @OneToMany(cascade = ALL, mappedBy = "owner")
 49      @Column(updatable = false)
 50      private List<Task> tasks = new ArrayList<>();
 51  
 52      public User() {
 53      }
 54  
 55      public User(String username) {
 56          this.username = username;
 57      }
 58  
 59      public Long getId() {
 60          return id;
 61      }
 62  
 63      public void setId(Long id) {
 64          this.id = id;
 65      }
 66  
 67      public String getUsername() {
 68          return username;
 69      }
 70  
 71      public void setUsername(String username) {
 72          this.username = username;
 73      }
 74  
 75      public List<Task> getTasks() {
 76          return tasks;
 77      }
 78  
 79      public void setTasks(List<Task> tasks) {
 80          this.tasks = tasks;
 81      }
 82  
 83      @Override
 84      public int hashCode() {
 85          final int prime = 31;
 86          int result = 1;
 87          result = prime * result + ((username == null) ? 0 : username.hashCode());
 88          return result;
 89      }
 90  
 91      @Override
 92      public boolean equals(Object obj) {
 93          if (this == obj)
 94              return true;
 95          if (obj == null)
 96              return false;
 97          if (getClass() != obj.getClass())
 98              return false;
 99          User other = (User) obj;
100          if (username == null) {
101              if (other.username != null)
102                  return false;
103          } else if (!username.equals(other.username))
104              return false;
105          return true;
106      }
107  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/tasksJsf/User.java
      * Line Number: 27
      * Message: 'Replace the `javax.persistence` import statement with `jakarta.persistence`'
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
 19  import static javax.persistence.CascadeType.ALL;
 20  import static javax.persistence.GenerationType.IDENTITY;
 21  
 22  import java.io.Serializable;
 23  import java.util.ArrayList;
 24  import java.util.List;
 25  
 26  import javax.persistence.Column;
 27  import javax.persistence.Entity;
 28  import javax.persistence.GeneratedValue;
 29  import javax.persistence.Id;
 30  import javax.persistence.OneToMany;
 31  
 32  /**
 33   * User entity
 34   *
 35   * @author Oliver Kiss
 36   */
 37  @SuppressWarnings("serial")
 38  @Entity
 39  public class User implements Serializable {
 40  
 41      @Id
 42      @GeneratedValue(strategy = IDENTITY)
 43      private Long id;
 44  
 45      @Column(unique = true)
 46      private String username;
 47  
 48      @OneToMany(cascade = ALL, mappedBy = "owner")
 49      @Column(updatable = false)
 50      private List<Task> tasks = new ArrayList<>();
 51  
 52      public User() {
 53      }
 54  
 55      public User(String username) {
 56          this.username = username;
 57      }
 58  
 59      public Long getId() {
 60          return id;
 61      }
 62  
 63      public void setId(Long id) {
 64          this.id = id;
 65      }
 66  
 67      public String getUsername() {
 68          return username;
 69      }
 70  
 71      public void setUsername(String username) {
 72          this.username = username;
 73      }
 74  
 75      public List<Task> getTasks() {
 76          return tasks;
 77      }
 78  
 79      public void setTasks(List<Task> tasks) {
 80          this.tasks = tasks;
 81      }
 82  
 83      @Override
 84      public int hashCode() {
 85          final int prime = 31;
 86          int result = 1;
 87          result = prime * result + ((username == null) ? 0 : username.hashCode());
 88          return result;
 89      }
 90  
 91      @Override
 92      public boolean equals(Object obj) {
 93          if (this == obj)
 94              return true;
 95          if (obj == null)
 96              return false;
 97          if (getClass() != obj.getClass())
 98              return false;
 99          User other = (User) obj;
100          if (username == null) {
101              if (other.username != null)
102                  return false;
103          } else if (!username.equals(other.username))
104              return false;
105          return true;
106      }
107  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/tasksJsf/User.java
      * Line Number: 28
      * Message: 'Replace the `javax.persistence` import statement with `jakarta.persistence`'
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
 19  import static javax.persistence.CascadeType.ALL;
 20  import static javax.persistence.GenerationType.IDENTITY;
 21  
 22  import java.io.Serializable;
 23  import java.util.ArrayList;
 24  import java.util.List;
 25  
 26  import javax.persistence.Column;
 27  import javax.persistence.Entity;
 28  import javax.persistence.GeneratedValue;
 29  import javax.persistence.Id;
 30  import javax.persistence.OneToMany;
 31  
 32  /**
 33   * User entity
 34   *
 35   * @author Oliver Kiss
 36   */
 37  @SuppressWarnings("serial")
 38  @Entity
 39  public class User implements Serializable {
 40  
 41      @Id
 42      @GeneratedValue(strategy = IDENTITY)
 43      private Long id;
 44  
 45      @Column(unique = true)
 46      private String username;
 47  
 48      @OneToMany(cascade = ALL, mappedBy = "owner")
 49      @Column(updatable = false)
 50      private List<Task> tasks = new ArrayList<>();
 51  
 52      public User() {
 53      }
 54  
 55      public User(String username) {
 56          this.username = username;
 57      }
 58  
 59      public Long getId() {
 60          return id;
 61      }
 62  
 63      public void setId(Long id) {
 64          this.id = id;
 65      }
 66  
 67      public String getUsername() {
 68          return username;
 69      }
 70  
 71      public void setUsername(String username) {
 72          this.username = username;
 73      }
 74  
 75      public List<Task> getTasks() {
 76          return tasks;
 77      }
 78  
 79      public void setTasks(List<Task> tasks) {
 80          this.tasks = tasks;
 81      }
 82  
 83      @Override
 84      public int hashCode() {
 85          final int prime = 31;
 86          int result = 1;
 87          result = prime * result + ((username == null) ? 0 : username.hashCode());
 88          return result;
 89      }
 90  
 91      @Override
 92      public boolean equals(Object obj) {
 93          if (this == obj)
 94              return true;
 95          if (obj == null)
 96              return false;
 97          if (getClass() != obj.getClass())
 98              return false;
 99          User other = (User) obj;
100          if (username == null) {
101              if (other.username != null)
102                  return false;
103          } else if (!username.equals(other.username))
104              return false;
105          return true;
106      }
107  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/tasksJsf/User.java
      * Line Number: 29
      * Message: 'Replace the `javax.persistence` import statement with `jakarta.persistence`'
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
 19  import static javax.persistence.CascadeType.ALL;
 20  import static javax.persistence.GenerationType.IDENTITY;
 21  
 22  import java.io.Serializable;
 23  import java.util.ArrayList;
 24  import java.util.List;
 25  
 26  import javax.persistence.Column;
 27  import javax.persistence.Entity;
 28  import javax.persistence.GeneratedValue;
 29  import javax.persistence.Id;
 30  import javax.persistence.OneToMany;
 31  
 32  /**
 33   * User entity
 34   *
 35   * @author Oliver Kiss
 36   */
 37  @SuppressWarnings("serial")
 38  @Entity
 39  public class User implements Serializable {
 40  
 41      @Id
 42      @GeneratedValue(strategy = IDENTITY)
 43      private Long id;
 44  
 45      @Column(unique = true)
 46      private String username;
 47  
 48      @OneToMany(cascade = ALL, mappedBy = "owner")
 49      @Column(updatable = false)
 50      private List<Task> tasks = new ArrayList<>();
 51  
 52      public User() {
 53      }
 54  
 55      public User(String username) {
 56          this.username = username;
 57      }
 58  
 59      public Long getId() {
 60          return id;
 61      }
 62  
 63      public void setId(Long id) {
 64          this.id = id;
 65      }
 66  
 67      public String getUsername() {
 68          return username;
 69      }
 70  
 71      public void setUsername(String username) {
 72          this.username = username;
 73      }
 74  
 75      public List<Task> getTasks() {
 76          return tasks;
 77      }
 78  
 79      public void setTasks(List<Task> tasks) {
 80          this.tasks = tasks;
 81      }
 82  
 83      @Override
 84      public int hashCode() {
 85          final int prime = 31;
 86          int result = 1;
 87          result = prime * result + ((username == null) ? 0 : username.hashCode());
 88          return result;
 89      }
 90  
 91      @Override
 92      public boolean equals(Object obj) {
 93          if (this == obj)
 94              return true;
 95          if (obj == null)
 96              return false;
 97          if (getClass() != obj.getClass())
 98              return false;
 99          User other = (User) obj;
100          if (username == null) {
101              if (other.username != null)
102                  return false;
103          } else if (!username.equals(other.username))
104              return false;
105          return true;
106      }
107  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/tasksJsf/User.java
      * Line Number: 30
      * Message: 'Replace the `javax.persistence` import statement with `jakarta.persistence`'
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
 19  import static javax.persistence.CascadeType.ALL;
 20  import static javax.persistence.GenerationType.IDENTITY;
 21  
 22  import java.io.Serializable;
 23  import java.util.ArrayList;
 24  import java.util.List;
 25  
 26  import javax.persistence.Column;
 27  import javax.persistence.Entity;
 28  import javax.persistence.GeneratedValue;
 29  import javax.persistence.Id;
 30  import javax.persistence.OneToMany;
 31  
 32  /**
 33   * User entity
 34   *
 35   * @author Oliver Kiss
 36   */
 37  @SuppressWarnings("serial")
 38  @Entity
 39  public class User implements Serializable {
 40  
 41      @Id
 42      @GeneratedValue(strategy = IDENTITY)
 43      private Long id;
 44  
 45      @Column(unique = true)
 46      private String username;
 47  
 48      @OneToMany(cascade = ALL, mappedBy = "owner")
 49      @Column(updatable = false)
 50      private List<Task> tasks = new ArrayList<>();
 51  
 52      public User() {
 53      }
 54  
 55      public User(String username) {
 56          this.username = username;
 57      }
 58  
 59      public Long getId() {
 60          return id;
 61      }
 62  
 63      public void setId(Long id) {
 64          this.id = id;
 65      }
 66  
 67      public String getUsername() {
 68          return username;
 69      }
 70  
 71      public void setUsername(String username) {
 72          this.username = username;
 73      }
 74  
 75      public List<Task> getTasks() {
 76          return tasks;
 77      }
 78  
 79      public void setTasks(List<Task> tasks) {
 80          this.tasks = tasks;
 81      }
 82  
 83      @Override
 84      public int hashCode() {
 85          final int prime = 31;
 86          int result = 1;
 87          result = prime * result + ((username == null) ? 0 : username.hashCode());
 88          return result;
 89      }
 90  
 91      @Override
 92      public boolean equals(Object obj) {
 93          if (this == obj)
 94              return true;
 95          if (obj == null)
 96              return false;
 97          if (getClass() != obj.getClass())
 98              return false;
 99          User other = (User) obj;
100          if (username == null) {
101              if (other.username != null)
102                  return false;
103          } else if (!username.equals(other.username))
104              return false;
105          return true;
106      }
107  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/tasksJsf/UserDao.java
      * Line Number: 19
      * Message: 'Replace the `javax.ejb` import statement with `jakarta.ejb`'
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
 19  import javax.ejb.Local;
 20  
 21  /**
 22   * Basic operations for manipulation with users
 23   *
 24   * @author Lukas Fryc
 25   *
 26   */
 27  @Local
 28  public interface UserDao {
 29  
 30      User getForUsername(String username);
 31  
 32      void createUser(User user);
 33  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/tasksJsf/UserDaoImpl.java
      * Line Number: 21
      * Message: 'Replace the `javax.ejb` import statement with `jakarta.ejb`'
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
 19  import java.util.List;
 20  
 21  import javax.ejb.Stateful;
 22  import javax.inject.Inject;
 23  import javax.persistence.EntityManager;
 24  
 25  /**
 26   * Provides functionality for manipulation with users using persistence context from {@link Resources}.
 27   *
 28   * @author Lukas Fryc
 29   * @author Oliver Kiss
 30   *
 31   */
 32  @Stateful
 33  public class UserDaoImpl implements UserDao {
 34  
 35      @Inject
 36      private EntityManager em;
 37  
 38      public User getForUsername(String username) {
 39          List<User> result = em.createQuery("select u from User u where u.username = ?1", User.class).setParameter(1, username)
 40              .getResultList();
 41  
 42          if (result.isEmpty()) {
 43              return null;
 44          }
 45          return result.get(0);
 46      }
 47  
 48      public void createUser(User user) {
 49          em.persist(user);
 50      }
 51  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/tasksJsf/UserDaoImpl.java
      * Line Number: 22
      * Message: 'Replace the `javax.inject` import statement with `jakarta.inject`'
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
 19  import java.util.List;
 20  
 21  import javax.ejb.Stateful;
 22  import javax.inject.Inject;
 23  import javax.persistence.EntityManager;
 24  
 25  /**
 26   * Provides functionality for manipulation with users using persistence context from {@link Resources}.
 27   *
 28   * @author Lukas Fryc
 29   * @author Oliver Kiss
 30   *
 31   */
 32  @Stateful
 33  public class UserDaoImpl implements UserDao {
 34  
 35      @Inject
 36      private EntityManager em;
 37  
 38      public User getForUsername(String username) {
 39          List<User> result = em.createQuery("select u from User u where u.username = ?1", User.class).setParameter(1, username)
 40              .getResultList();
 41  
 42          if (result.isEmpty()) {
 43              return null;
 44          }
 45          return result.get(0);
 46      }
 47  
 48      public void createUser(User user) {
 49          em.persist(user);
 50      }
 51  }

```
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/tasksJsf/UserDaoImpl.java
      * Line Number: 23
      * Message: 'Replace the `javax.persistence` import statement with `jakarta.persistence`'
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
 19  import java.util.List;
 20  
 21  import javax.ejb.Stateful;
 22  import javax.inject.Inject;
 23  import javax.persistence.EntityManager;
 24  
 25  /**
 26   * Provides functionality for manipulation with users using persistence context from {@link Resources}.
 27   *
 28   * @author Lukas Fryc
 29   * @author Oliver Kiss
 30   *
 31   */
 32  @Stateful
 33  public class UserDaoImpl implements UserDao {
 34  
 35      @Inject
 36      private EntityManager em;
 37  
 38      public User getForUsername(String username) {
 39          List<User> result = em.createQuery("select u from User u where u.username = ?1", User.class).setParameter(1, username)
 40              .getResultList();
 41  
 42          if (result.isEmpty()) {
 43              return null;
 44          }
 45          return result.get(0);
 46      }
 47  
 48      public void createUser(User user) {
 49          em.persist(user);
 50      }
 51  }

```
  * file:///tmp/source-code/src/test/java/org/jboss/as/quickstarts/tasksJsf/FacesContextStub.java
      * Line Number: 21
      * Message: 'Replace the `javax.faces` import statement with `jakarta.faces`'
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
 19  import java.util.Iterator;
 20  
 21  import javax.faces.application.Application;
 22  import javax.faces.application.FacesMessage;
 23  import javax.faces.application.FacesMessage.Severity;
 24  import javax.faces.component.UIViewRoot;
 25  import javax.faces.context.ExternalContext;
 26  import javax.faces.context.FacesContext;
 27  import javax.faces.context.ResponseStream;
 28  import javax.faces.context.ResponseWriter;
 29  import javax.faces.render.RenderKit;
 30  
 31  /**
 32   * Stub of {@link FacesContext} to allow testing without real JSF session.
 33   *
 34   * @author Lukas Fryc
 35   *
 36   */
 37  public class FacesContextStub extends FacesContext {
 38  
 39      FacesContextStub(String test) {
 40      }
 41  
 42      public static void setCurrentInstance(FacesContext facesContext) {
 43          FacesContext.setCurrentInstance(facesContext);
 44      }
 45  
 46      @Override
 47      public Application getApplication() {
 48          return null;
 49      }
 50  
 51      @Override
 52      public Iterator<String> getClientIdsWithMessages() {
 53          return null;
 54      }
 55  
 56      @Override
 57      public ExternalContext getExternalContext() {
 58          return null;
 59      }
 60  
 61      @Override
 62      public Severity getMaximumSeverity() {
 63          return null;
 64      }
 65  
 66      @Override
 67      public Iterator<FacesMessage> getMessages() {
 68          return null;
 69      }
 70  
 71      @Override
 72      public Iterator<FacesMessage> getMessages(String clientId) {
 73          return null;
 74      }
 75  
 76      @Override
 77      public RenderKit getRenderKit() {
 78          return null;
 79      }
 80  
 81      @Override
 82      public boolean getRenderResponse() {
 83          return false;
 84      }
 85  
 86      @Override
 87      public boolean getResponseComplete() {
 88          return false;
 89      }
 90  
 91      @Override
 92      public ResponseStream getResponseStream() {
 93  
 94          return null;
 95      }
 96  
 97      @Override
 98      public void setResponseStream(ResponseStream responseStream) {
 99  
100      }
101  
102      @Override
103      public ResponseWriter getResponseWriter() {
104  
105          return null;
106      }
107  
108      @Override
109      public void setResponseWriter(ResponseWriter responseWriter) {
110  
111      }
112  
113      @Override
114      public UIViewRoot getViewRoot() {
115  
116          return null;
117      }
118  
119      @Override
120      public void setViewRoot(UIViewRoot root) {
121  
```
  * file:///tmp/source-code/src/test/java/org/jboss/as/quickstarts/tasksJsf/FacesContextStub.java
      * Line Number: 22
      * Message: 'Replace the `javax.faces` import statement with `jakarta.faces`'
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
 19  import java.util.Iterator;
 20  
 21  import javax.faces.application.Application;
 22  import javax.faces.application.FacesMessage;
 23  import javax.faces.application.FacesMessage.Severity;
 24  import javax.faces.component.UIViewRoot;
 25  import javax.faces.context.ExternalContext;
 26  import javax.faces.context.FacesContext;
 27  import javax.faces.context.ResponseStream;
 28  import javax.faces.context.ResponseWriter;
 29  import javax.faces.render.RenderKit;
 30  
 31  /**
 32   * Stub of {@link FacesContext} to allow testing without real JSF session.
 33   *
 34   * @author Lukas Fryc
 35   *
 36   */
 37  public class FacesContextStub extends FacesContext {
 38  
 39      FacesContextStub(String test) {
 40      }
 41  
 42      public static void setCurrentInstance(FacesContext facesContext) {
 43          FacesContext.setCurrentInstance(facesContext);
 44      }
 45  
 46      @Override
 47      public Application getApplication() {
 48          return null;
 49      }
 50  
 51      @Override
 52      public Iterator<String> getClientIdsWithMessages() {
 53          return null;
 54      }
 55  
 56      @Override
 57      public ExternalContext getExternalContext() {
 58          return null;
 59      }
 60  
 61      @Override
 62      public Severity getMaximumSeverity() {
 63          return null;
 64      }
 65  
 66      @Override
 67      public Iterator<FacesMessage> getMessages() {
 68          return null;
 69      }
 70  
 71      @Override
 72      public Iterator<FacesMessage> getMessages(String clientId) {
 73          return null;
 74      }
 75  
 76      @Override
 77      public RenderKit getRenderKit() {
 78          return null;
 79      }
 80  
 81      @Override
 82      public boolean getRenderResponse() {
 83          return false;
 84      }
 85  
 86      @Override
 87      public boolean getResponseComplete() {
 88          return false;
 89      }
 90  
 91      @Override
 92      public ResponseStream getResponseStream() {
 93  
 94          return null;
 95      }
 96  
 97      @Override
 98      public void setResponseStream(ResponseStream responseStream) {
 99  
100      }
101  
102      @Override
103      public ResponseWriter getResponseWriter() {
104  
105          return null;
106      }
107  
108      @Override
109      public void setResponseWriter(ResponseWriter responseWriter) {
110  
111      }
112  
113      @Override
114      public UIViewRoot getViewRoot() {
115  
116          return null;
117      }
118  
119      @Override
120      public void setViewRoot(UIViewRoot root) {
121  
122      }
```
  * file:///tmp/source-code/src/test/java/org/jboss/as/quickstarts/tasksJsf/FacesContextStub.java
      * Line Number: 23
      * Message: 'Replace the `javax.faces` import statement with `jakarta.faces`'
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
 19  import java.util.Iterator;
 20  
 21  import javax.faces.application.Application;
 22  import javax.faces.application.FacesMessage;
 23  import javax.faces.application.FacesMessage.Severity;
 24  import javax.faces.component.UIViewRoot;
 25  import javax.faces.context.ExternalContext;
 26  import javax.faces.context.FacesContext;
 27  import javax.faces.context.ResponseStream;
 28  import javax.faces.context.ResponseWriter;
 29  import javax.faces.render.RenderKit;
 30  
 31  /**
 32   * Stub of {@link FacesContext} to allow testing without real JSF session.
 33   *
 34   * @author Lukas Fryc
 35   *
 36   */
 37  public class FacesContextStub extends FacesContext {
 38  
 39      FacesContextStub(String test) {
 40      }
 41  
 42      public static void setCurrentInstance(FacesContext facesContext) {
 43          FacesContext.setCurrentInstance(facesContext);
 44      }
 45  
 46      @Override
 47      public Application getApplication() {
 48          return null;
 49      }
 50  
 51      @Override
 52      public Iterator<String> getClientIdsWithMessages() {
 53          return null;
 54      }
 55  
 56      @Override
 57      public ExternalContext getExternalContext() {
 58          return null;
 59      }
 60  
 61      @Override
 62      public Severity getMaximumSeverity() {
 63          return null;
 64      }
 65  
 66      @Override
 67      public Iterator<FacesMessage> getMessages() {
 68          return null;
 69      }
 70  
 71      @Override
 72      public Iterator<FacesMessage> getMessages(String clientId) {
 73          return null;
 74      }
 75  
 76      @Override
 77      public RenderKit getRenderKit() {
 78          return null;
 79      }
 80  
 81      @Override
 82      public boolean getRenderResponse() {
 83          return false;
 84      }
 85  
 86      @Override
 87      public boolean getResponseComplete() {
 88          return false;
 89      }
 90  
 91      @Override
 92      public ResponseStream getResponseStream() {
 93  
 94          return null;
 95      }
 96  
 97      @Override
 98      public void setResponseStream(ResponseStream responseStream) {
 99  
100      }
101  
102      @Override
103      public ResponseWriter getResponseWriter() {
104  
105          return null;
106      }
107  
108      @Override
109      public void setResponseWriter(ResponseWriter responseWriter) {
110  
111      }
112  
113      @Override
114      public UIViewRoot getViewRoot() {
115  
116          return null;
117      }
118  
119      @Override
120      public void setViewRoot(UIViewRoot root) {
121  
122      }
123  
```
  * file:///tmp/source-code/src/test/java/org/jboss/as/quickstarts/tasksJsf/FacesContextStub.java
      * Line Number: 24
      * Message: 'Replace the `javax.faces` import statement with `jakarta.faces`'
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
 19  import java.util.Iterator;
 20  
 21  import javax.faces.application.Application;
 22  import javax.faces.application.FacesMessage;
 23  import javax.faces.application.FacesMessage.Severity;
 24  import javax.faces.component.UIViewRoot;
 25  import javax.faces.context.ExternalContext;
 26  import javax.faces.context.FacesContext;
 27  import javax.faces.context.ResponseStream;
 28  import javax.faces.context.ResponseWriter;
 29  import javax.faces.render.RenderKit;
 30  
 31  /**
 32   * Stub of {@link FacesContext} to allow testing without real JSF session.
 33   *
 34   * @author Lukas Fryc
 35   *
 36   */
 37  public class FacesContextStub extends FacesContext {
 38  
 39      FacesContextStub(String test) {
 40      }
 41  
 42      public static void setCurrentInstance(FacesContext facesContext) {
 43          FacesContext.setCurrentInstance(facesContext);
 44      }
 45  
 46      @Override
 47      public Application getApplication() {
 48          return null;
 49      }
 50  
 51      @Override
 52      public Iterator<String> getClientIdsWithMessages() {
 53          return null;
 54      }
 55  
 56      @Override
 57      public ExternalContext getExternalContext() {
 58          return null;
 59      }
 60  
 61      @Override
 62      public Severity getMaximumSeverity() {
 63          return null;
 64      }
 65  
 66      @Override
 67      public Iterator<FacesMessage> getMessages() {
 68          return null;
 69      }
 70  
 71      @Override
 72      public Iterator<FacesMessage> getMessages(String clientId) {
 73          return null;
 74      }
 75  
 76      @Override
 77      public RenderKit getRenderKit() {
 78          return null;
 79      }
 80  
 81      @Override
 82      public boolean getRenderResponse() {
 83          return false;
 84      }
 85  
 86      @Override
 87      public boolean getResponseComplete() {
 88          return false;
 89      }
 90  
 91      @Override
 92      public ResponseStream getResponseStream() {
 93  
 94          return null;
 95      }
 96  
 97      @Override
 98      public void setResponseStream(ResponseStream responseStream) {
 99  
100      }
101  
102      @Override
103      public ResponseWriter getResponseWriter() {
104  
105          return null;
106      }
107  
108      @Override
109      public void setResponseWriter(ResponseWriter responseWriter) {
110  
111      }
112  
113      @Override
114      public UIViewRoot getViewRoot() {
115  
116          return null;
117      }
118  
119      @Override
120      public void setViewRoot(UIViewRoot root) {
121  
122      }
123  
124      @Override
```
  * file:///tmp/source-code/src/test/java/org/jboss/as/quickstarts/tasksJsf/FacesContextStub.java
      * Line Number: 25
      * Message: 'Replace the `javax.faces` import statement with `jakarta.faces`'
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
 19  import java.util.Iterator;
 20  
 21  import javax.faces.application.Application;
 22  import javax.faces.application.FacesMessage;
 23  import javax.faces.application.FacesMessage.Severity;
 24  import javax.faces.component.UIViewRoot;
 25  import javax.faces.context.ExternalContext;
 26  import javax.faces.context.FacesContext;
 27  import javax.faces.context.ResponseStream;
 28  import javax.faces.context.ResponseWriter;
 29  import javax.faces.render.RenderKit;
 30  
 31  /**
 32   * Stub of {@link FacesContext} to allow testing without real JSF session.
 33   *
 34   * @author Lukas Fryc
 35   *
 36   */
 37  public class FacesContextStub extends FacesContext {
 38  
 39      FacesContextStub(String test) {
 40      }
 41  
 42      public static void setCurrentInstance(FacesContext facesContext) {
 43          FacesContext.setCurrentInstance(facesContext);
 44      }
 45  
 46      @Override
 47      public Application getApplication() {
 48          return null;
 49      }
 50  
 51      @Override
 52      public Iterator<String> getClientIdsWithMessages() {
 53          return null;
 54      }
 55  
 56      @Override
 57      public ExternalContext getExternalContext() {
 58          return null;
 59      }
 60  
 61      @Override
 62      public Severity getMaximumSeverity() {
 63          return null;
 64      }
 65  
 66      @Override
 67      public Iterator<FacesMessage> getMessages() {
 68          return null;
 69      }
 70  
 71      @Override
 72      public Iterator<FacesMessage> getMessages(String clientId) {
 73          return null;
 74      }
 75  
 76      @Override
 77      public RenderKit getRenderKit() {
 78          return null;
 79      }
 80  
 81      @Override
 82      public boolean getRenderResponse() {
 83          return false;
 84      }
 85  
 86      @Override
 87      public boolean getResponseComplete() {
 88          return false;
 89      }
 90  
 91      @Override
 92      public ResponseStream getResponseStream() {
 93  
 94          return null;
 95      }
 96  
 97      @Override
 98      public void setResponseStream(ResponseStream responseStream) {
 99  
100      }
101  
102      @Override
103      public ResponseWriter getResponseWriter() {
104  
105          return null;
106      }
107  
108      @Override
109      public void setResponseWriter(ResponseWriter responseWriter) {
110  
111      }
112  
113      @Override
114      public UIViewRoot getViewRoot() {
115  
116          return null;
117      }
118  
119      @Override
120      public void setViewRoot(UIViewRoot root) {
121  
122      }
123  
124      @Override
125      public void addMessage(String clientId, FacesMessage message) {
```
  * file:///tmp/source-code/src/test/java/org/jboss/as/quickstarts/tasksJsf/FacesContextStub.java
      * Line Number: 26
      * Message: 'Replace the `javax.faces` import statement with `jakarta.faces`'
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
 19  import java.util.Iterator;
 20  
 21  import javax.faces.application.Application;
 22  import javax.faces.application.FacesMessage;
 23  import javax.faces.application.FacesMessage.Severity;
 24  import javax.faces.component.UIViewRoot;
 25  import javax.faces.context.ExternalContext;
 26  import javax.faces.context.FacesContext;
 27  import javax.faces.context.ResponseStream;
 28  import javax.faces.context.ResponseWriter;
 29  import javax.faces.render.RenderKit;
 30  
 31  /**
 32   * Stub of {@link FacesContext} to allow testing without real JSF session.
 33   *
 34   * @author Lukas Fryc
 35   *
 36   */
 37  public class FacesContextStub extends FacesContext {
 38  
 39      FacesContextStub(String test) {
 40      }
 41  
 42      public static void setCurrentInstance(FacesContext facesContext) {
 43          FacesContext.setCurrentInstance(facesContext);
 44      }
 45  
 46      @Override
 47      public Application getApplication() {
 48          return null;
 49      }
 50  
 51      @Override
 52      public Iterator<String> getClientIdsWithMessages() {
 53          return null;
 54      }
 55  
 56      @Override
 57      public ExternalContext getExternalContext() {
 58          return null;
 59      }
 60  
 61      @Override
 62      public Severity getMaximumSeverity() {
 63          return null;
 64      }
 65  
 66      @Override
 67      public Iterator<FacesMessage> getMessages() {
 68          return null;
 69      }
 70  
 71      @Override
 72      public Iterator<FacesMessage> getMessages(String clientId) {
 73          return null;
 74      }
 75  
 76      @Override
 77      public RenderKit getRenderKit() {
 78          return null;
 79      }
 80  
 81      @Override
 82      public boolean getRenderResponse() {
 83          return false;
 84      }
 85  
 86      @Override
 87      public boolean getResponseComplete() {
 88          return false;
 89      }
 90  
 91      @Override
 92      public ResponseStream getResponseStream() {
 93  
 94          return null;
 95      }
 96  
 97      @Override
 98      public void setResponseStream(ResponseStream responseStream) {
 99  
100      }
101  
102      @Override
103      public ResponseWriter getResponseWriter() {
104  
105          return null;
106      }
107  
108      @Override
109      public void setResponseWriter(ResponseWriter responseWriter) {
110  
111      }
112  
113      @Override
114      public UIViewRoot getViewRoot() {
115  
116          return null;
117      }
118  
119      @Override
120      public void setViewRoot(UIViewRoot root) {
121  
122      }
123  
124      @Override
125      public void addMessage(String clientId, FacesMessage message) {
126  
```
  * file:///tmp/source-code/src/test/java/org/jboss/as/quickstarts/tasksJsf/FacesContextStub.java
      * Line Number: 27
      * Message: 'Replace the `javax.faces` import statement with `jakarta.faces`'
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
 19  import java.util.Iterator;
 20  
 21  import javax.faces.application.Application;
 22  import javax.faces.application.FacesMessage;
 23  import javax.faces.application.FacesMessage.Severity;
 24  import javax.faces.component.UIViewRoot;
 25  import javax.faces.context.ExternalContext;
 26  import javax.faces.context.FacesContext;
 27  import javax.faces.context.ResponseStream;
 28  import javax.faces.context.ResponseWriter;
 29  import javax.faces.render.RenderKit;
 30  
 31  /**
 32   * Stub of {@link FacesContext} to allow testing without real JSF session.
 33   *
 34   * @author Lukas Fryc
 35   *
 36   */
 37  public class FacesContextStub extends FacesContext {
 38  
 39      FacesContextStub(String test) {
 40      }
 41  
 42      public static void setCurrentInstance(FacesContext facesContext) {
 43          FacesContext.setCurrentInstance(facesContext);
 44      }
 45  
 46      @Override
 47      public Application getApplication() {
 48          return null;
 49      }
 50  
 51      @Override
 52      public Iterator<String> getClientIdsWithMessages() {
 53          return null;
 54      }
 55  
 56      @Override
 57      public ExternalContext getExternalContext() {
 58          return null;
 59      }
 60  
 61      @Override
 62      public Severity getMaximumSeverity() {
 63          return null;
 64      }
 65  
 66      @Override
 67      public Iterator<FacesMessage> getMessages() {
 68          return null;
 69      }
 70  
 71      @Override
 72      public Iterator<FacesMessage> getMessages(String clientId) {
 73          return null;
 74      }
 75  
 76      @Override
 77      public RenderKit getRenderKit() {
 78          return null;
 79      }
 80  
 81      @Override
 82      public boolean getRenderResponse() {
 83          return false;
 84      }
 85  
 86      @Override
 87      public boolean getResponseComplete() {
 88          return false;
 89      }
 90  
 91      @Override
 92      public ResponseStream getResponseStream() {
 93  
 94          return null;
 95      }
 96  
 97      @Override
 98      public void setResponseStream(ResponseStream responseStream) {
 99  
100      }
101  
102      @Override
103      public ResponseWriter getResponseWriter() {
104  
105          return null;
106      }
107  
108      @Override
109      public void setResponseWriter(ResponseWriter responseWriter) {
110  
111      }
112  
113      @Override
114      public UIViewRoot getViewRoot() {
115  
116          return null;
117      }
118  
119      @Override
120      public void setViewRoot(UIViewRoot root) {
121  
122      }
123  
124      @Override
125      public void addMessage(String clientId, FacesMessage message) {
126  
127      }
```
  * file:///tmp/source-code/src/test/java/org/jboss/as/quickstarts/tasksJsf/FacesContextStub.java
      * Line Number: 28
      * Message: 'Replace the `javax.faces` import statement with `jakarta.faces`'
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
 19  import java.util.Iterator;
 20  
 21  import javax.faces.application.Application;
 22  import javax.faces.application.FacesMessage;
 23  import javax.faces.application.FacesMessage.Severity;
 24  import javax.faces.component.UIViewRoot;
 25  import javax.faces.context.ExternalContext;
 26  import javax.faces.context.FacesContext;
 27  import javax.faces.context.ResponseStream;
 28  import javax.faces.context.ResponseWriter;
 29  import javax.faces.render.RenderKit;
 30  
 31  /**
 32   * Stub of {@link FacesContext} to allow testing without real JSF session.
 33   *
 34   * @author Lukas Fryc
 35   *
 36   */
 37  public class FacesContextStub extends FacesContext {
 38  
 39      FacesContextStub(String test) {
 40      }
 41  
 42      public static void setCurrentInstance(FacesContext facesContext) {
 43          FacesContext.setCurrentInstance(facesContext);
 44      }
 45  
 46      @Override
 47      public Application getApplication() {
 48          return null;
 49      }
 50  
 51      @Override
 52      public Iterator<String> getClientIdsWithMessages() {
 53          return null;
 54      }
 55  
 56      @Override
 57      public ExternalContext getExternalContext() {
 58          return null;
 59      }
 60  
 61      @Override
 62      public Severity getMaximumSeverity() {
 63          return null;
 64      }
 65  
 66      @Override
 67      public Iterator<FacesMessage> getMessages() {
 68          return null;
 69      }
 70  
 71      @Override
 72      public Iterator<FacesMessage> getMessages(String clientId) {
 73          return null;
 74      }
 75  
 76      @Override
 77      public RenderKit getRenderKit() {
 78          return null;
 79      }
 80  
 81      @Override
 82      public boolean getRenderResponse() {
 83          return false;
 84      }
 85  
 86      @Override
 87      public boolean getResponseComplete() {
 88          return false;
 89      }
 90  
 91      @Override
 92      public ResponseStream getResponseStream() {
 93  
 94          return null;
 95      }
 96  
 97      @Override
 98      public void setResponseStream(ResponseStream responseStream) {
 99  
100      }
101  
102      @Override
103      public ResponseWriter getResponseWriter() {
104  
105          return null;
106      }
107  
108      @Override
109      public void setResponseWriter(ResponseWriter responseWriter) {
110  
111      }
112  
113      @Override
114      public UIViewRoot getViewRoot() {
115  
116          return null;
117      }
118  
119      @Override
120      public void setViewRoot(UIViewRoot root) {
121  
122      }
123  
124      @Override
125      public void addMessage(String clientId, FacesMessage message) {
126  
127      }
128  
```
  * file:///tmp/source-code/src/test/java/org/jboss/as/quickstarts/tasksJsf/FacesContextStub.java
      * Line Number: 29
      * Message: 'Replace the `javax.faces` import statement with `jakarta.faces`'
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
 19  import java.util.Iterator;
 20  
 21  import javax.faces.application.Application;
 22  import javax.faces.application.FacesMessage;
 23  import javax.faces.application.FacesMessage.Severity;
 24  import javax.faces.component.UIViewRoot;
 25  import javax.faces.context.ExternalContext;
 26  import javax.faces.context.FacesContext;
 27  import javax.faces.context.ResponseStream;
 28  import javax.faces.context.ResponseWriter;
 29  import javax.faces.render.RenderKit;
 30  
 31  /**
 32   * Stub of {@link FacesContext} to allow testing without real JSF session.
 33   *
 34   * @author Lukas Fryc
 35   *
 36   */
 37  public class FacesContextStub extends FacesContext {
 38  
 39      FacesContextStub(String test) {
 40      }
 41  
 42      public static void setCurrentInstance(FacesContext facesContext) {
 43          FacesContext.setCurrentInstance(facesContext);
 44      }
 45  
 46      @Override
 47      public Application getApplication() {
 48          return null;
 49      }
 50  
 51      @Override
 52      public Iterator<String> getClientIdsWithMessages() {
 53          return null;
 54      }
 55  
 56      @Override
 57      public ExternalContext getExternalContext() {
 58          return null;
 59      }
 60  
 61      @Override
 62      public Severity getMaximumSeverity() {
 63          return null;
 64      }
 65  
 66      @Override
 67      public Iterator<FacesMessage> getMessages() {
 68          return null;
 69      }
 70  
 71      @Override
 72      public Iterator<FacesMessage> getMessages(String clientId) {
 73          return null;
 74      }
 75  
 76      @Override
 77      public RenderKit getRenderKit() {
 78          return null;
 79      }
 80  
 81      @Override
 82      public boolean getRenderResponse() {
 83          return false;
 84      }
 85  
 86      @Override
 87      public boolean getResponseComplete() {
 88          return false;
 89      }
 90  
 91      @Override
 92      public ResponseStream getResponseStream() {
 93  
 94          return null;
 95      }
 96  
 97      @Override
 98      public void setResponseStream(ResponseStream responseStream) {
 99  
100      }
101  
102      @Override
103      public ResponseWriter getResponseWriter() {
104  
105          return null;
106      }
107  
108      @Override
109      public void setResponseWriter(ResponseWriter responseWriter) {
110  
111      }
112  
113      @Override
114      public UIViewRoot getViewRoot() {
115  
116          return null;
117      }
118  
119      @Override
120      public void setViewRoot(UIViewRoot root) {
121  
122      }
123  
124      @Override
125      public void addMessage(String clientId, FacesMessage message) {
126  
127      }
128  
129      @Override
```
  * file:///tmp/source-code/src/test/java/org/jboss/as/quickstarts/tasksJsf/ResourcesIT.java
      * Line Number: 27
      * Message: 'Replace the `javax.enterprise` import statement with `jakarta.enterprise`'
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
 19  import static org.junit.Assert.assertNotNull;
 20  import static org.junit.Assert.assertNull;
 21  import static org.junit.Assert.assertTrue;
 22  
 23  import java.io.FileNotFoundException;
 24  import java.util.logging.Level;
 25  import java.util.logging.Logger;
 26  
 27  import javax.enterprise.inject.Instance;
 28  import javax.faces.context.FacesContext;
 29  import javax.inject.Inject;
 30  
 31  import org.jboss.arquillian.container.test.api.Deployment;
 32  import org.jboss.arquillian.junit.Arquillian;
 33  import org.jboss.shrinkwrap.api.spec.WebArchive;
 34  import org.junit.Test;
 35  import org.junit.runner.RunWith;
 36  
 37  /**
 38   * @author Lukas Fryc
 39   */
 40  @RunWith(Arquillian.class)
 41  public class ResourcesIT {
 42  
 43      public static final String WEBAPP_SRC = "src/main/webapp";
 44  
 45      @Deployment
 46      public static WebArchive deployment() throws IllegalArgumentException, FileNotFoundException {
 47          return new DefaultDeployment().withPersistence().withFaces().getArchive()
 48              .addClasses(Resources.class, FacesContextStub.class);
 49      }
 50  
 51      @Inject
 52      private Instance<FacesContext> facesContextInstance;
 53  
 54      @Inject
 55      private Instance<Logger> loggerInstance;
 56  
 57      @Test
 58      public void facesContext_should_be_provided_from_current_context() {
 59          FacesContextStub.setCurrentInstance(new FacesContextStub("stub"));
 60  
 61          FacesContext facesContext = facesContextInstance.get();
 62          assertNotNull(facesContext);
 63          assertTrue(facesContext instanceof FacesContextStub);
 64  
 65          FacesContextStub.setCurrentInstance(null);
 66  
 67          facesContext = facesContextInstance.get();
 68          assertNull(facesContext);
 69      }
 70  
 71      @Test
 72      public void logger_should_be_provided_and_be_able_to_log_information_message() {
 73          Logger logger = loggerInstance.get();
 74          assertNotNull(logger);
 75          assertTrue(logger instanceof Logger);
 76          logger.log(Level.INFO, "test message");
 77      }
 78  
 79  }

```
  * file:///tmp/source-code/src/test/java/org/jboss/as/quickstarts/tasksJsf/ResourcesIT.java
      * Line Number: 28
      * Message: 'Replace the `javax.faces` import statement with `jakarta.faces`'
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
 19  import static org.junit.Assert.assertNotNull;
 20  import static org.junit.Assert.assertNull;
 21  import static org.junit.Assert.assertTrue;
 22  
 23  import java.io.FileNotFoundException;
 24  import java.util.logging.Level;
 25  import java.util.logging.Logger;
 26  
 27  import javax.enterprise.inject.Instance;
 28  import javax.faces.context.FacesContext;
 29  import javax.inject.Inject;
 30  
 31  import org.jboss.arquillian.container.test.api.Deployment;
 32  import org.jboss.arquillian.junit.Arquillian;
 33  import org.jboss.shrinkwrap.api.spec.WebArchive;
 34  import org.junit.Test;
 35  import org.junit.runner.RunWith;
 36  
 37  /**
 38   * @author Lukas Fryc
 39   */
 40  @RunWith(Arquillian.class)
 41  public class ResourcesIT {
 42  
 43      public static final String WEBAPP_SRC = "src/main/webapp";
 44  
 45      @Deployment
 46      public static WebArchive deployment() throws IllegalArgumentException, FileNotFoundException {
 47          return new DefaultDeployment().withPersistence().withFaces().getArchive()
 48              .addClasses(Resources.class, FacesContextStub.class);
 49      }
 50  
 51      @Inject
 52      private Instance<FacesContext> facesContextInstance;
 53  
 54      @Inject
 55      private Instance<Logger> loggerInstance;
 56  
 57      @Test
 58      public void facesContext_should_be_provided_from_current_context() {
 59          FacesContextStub.setCurrentInstance(new FacesContextStub("stub"));
 60  
 61          FacesContext facesContext = facesContextInstance.get();
 62          assertNotNull(facesContext);
 63          assertTrue(facesContext instanceof FacesContextStub);
 64  
 65          FacesContextStub.setCurrentInstance(null);
 66  
 67          facesContext = facesContextInstance.get();
 68          assertNull(facesContext);
 69      }
 70  
 71      @Test
 72      public void logger_should_be_provided_and_be_able_to_log_information_message() {
 73          Logger logger = loggerInstance.get();
 74          assertNotNull(logger);
 75          assertTrue(logger instanceof Logger);
 76          logger.log(Level.INFO, "test message");
 77      }
 78  
 79  }

```
  * file:///tmp/source-code/src/test/java/org/jboss/as/quickstarts/tasksJsf/ResourcesIT.java
      * Line Number: 29
      * Message: 'Replace the `javax.inject` import statement with `jakarta.inject`'
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
 19  import static org.junit.Assert.assertNotNull;
 20  import static org.junit.Assert.assertNull;
 21  import static org.junit.Assert.assertTrue;
 22  
 23  import java.io.FileNotFoundException;
 24  import java.util.logging.Level;
 25  import java.util.logging.Logger;
 26  
 27  import javax.enterprise.inject.Instance;
 28  import javax.faces.context.FacesContext;
 29  import javax.inject.Inject;
 30  
 31  import org.jboss.arquillian.container.test.api.Deployment;
 32  import org.jboss.arquillian.junit.Arquillian;
 33  import org.jboss.shrinkwrap.api.spec.WebArchive;
 34  import org.junit.Test;
 35  import org.junit.runner.RunWith;
 36  
 37  /**
 38   * @author Lukas Fryc
 39   */
 40  @RunWith(Arquillian.class)
 41  public class ResourcesIT {
 42  
 43      public static final String WEBAPP_SRC = "src/main/webapp";
 44  
 45      @Deployment
 46      public static WebArchive deployment() throws IllegalArgumentException, FileNotFoundException {
 47          return new DefaultDeployment().withPersistence().withFaces().getArchive()
 48              .addClasses(Resources.class, FacesContextStub.class);
 49      }
 50  
 51      @Inject
 52      private Instance<FacesContext> facesContextInstance;
 53  
 54      @Inject
 55      private Instance<Logger> loggerInstance;
 56  
 57      @Test
 58      public void facesContext_should_be_provided_from_current_context() {
 59          FacesContextStub.setCurrentInstance(new FacesContextStub("stub"));
 60  
 61          FacesContext facesContext = facesContextInstance.get();
 62          assertNotNull(facesContext);
 63          assertTrue(facesContext instanceof FacesContextStub);
 64  
 65          FacesContextStub.setCurrentInstance(null);
 66  
 67          facesContext = facesContextInstance.get();
 68          assertNull(facesContext);
 69      }
 70  
 71      @Test
 72      public void logger_should_be_provided_and_be_able_to_log_information_message() {
 73          Logger logger = loggerInstance.get();
 74          assertNotNull(logger);
 75          assertTrue(logger instanceof Logger);
 76          logger.log(Level.INFO, "test message");
 77      }
 78  
 79  }

```
  * file:///tmp/source-code/src/test/java/org/jboss/as/quickstarts/tasksJsf/TaskDaoIT.java
      * Line Number: 24
      * Message: 'Replace the `javax.inject` import statement with `jakarta.inject`'
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
 19  import static org.junit.Assert.assertEquals;
 20  import static org.junit.Assert.assertTrue;
 21  
 22  import java.io.FileNotFoundException;
 23  import java.util.List;
 24  import javax.inject.Inject;
 25  import javax.persistence.EntityManager;
 26  
 27  import org.jboss.arquillian.container.test.api.Deployment;
 28  import org.jboss.arquillian.junit.Arquillian;
 29  import org.jboss.arquillian.junit.InSequence;
 30  import org.jboss.shrinkwrap.api.spec.WebArchive;
 31  import org.junit.Before;
 32  import org.junit.Test;
 33  import org.junit.runner.RunWith;
 34  
 35  /**
 36   * @author Lukas Fryc
 37   * @author Oliver Kiss
 38   */
 39  @RunWith(Arquillian.class)
 40  public class TaskDaoIT {
 41  
 42      @Deployment
 43      public static WebArchive deployment() throws IllegalArgumentException, FileNotFoundException {
 44          return new DefaultDeployment().withPersistence().withImportedData().getArchive()
 45                  .addClasses(Resources.class, User.class, UserDao.class, Task.class, TaskDao.class, TaskDaoImpl.class);
 46      }
 47  
 48      @Inject
 49      private EntityManager em;
 50  
 51      @Inject
 52      private TaskDao taskDao;
 53  
 54      private User detachedUser;
 55  
 56      @Before
 57      public void setUp() throws Exception {
 58          detachedUser = new User("jdoe");
 59          detachedUser.setId(1L);
 60      }
 61  
 62      @Test
 63      @InSequence(1)
 64      public void user_should_be_created_with_one_task_attached() throws Exception {
 65          // given
 66          User user = new User("New user");
 67          Task task = new Task("New task");
 68  
 69          // when
 70          em.persist(user);
 71          taskDao.createTask(user, task);
 72          List<Task> userTasks = em.createQuery("SELECT t FROM Task t WHERE t.owner = :owner", Task.class)
 73                  .setParameter("owner", user).getResultList();
 74  
 75          // then
 76          assertEquals(1, userTasks.size());
 77          assertEquals(task, userTasks.get(0));
 78      }
 79  
 80      @Test
 81      @InSequence(2)
 82      public void all_tasks_should_be_obtained_from_detachedUser() {
 83          // when
 84          List<Task> userTasks = taskDao.getAll(detachedUser);
 85  
 86          // then
 87          assertEquals(2, userTasks.size());
 88      }
 89  
 90      @Test
 91      @InSequence(3)
 92      public void range_of_tasks_should_be_provided_by_taskDao() {
 93          // when
 94          List<Task> headOfTasks = taskDao.getRange(detachedUser, 0, 1);
 95          List<Task> tailOfTasks = taskDao.getRange(detachedUser, 1, 1);
 96  
 97          // then
 98          assertEquals(1, headOfTasks.size());
 99          assertEquals(1, tailOfTasks.size());
100          assertTrue(headOfTasks.get(0).getTitle().contains("first"));
101          assertTrue(tailOfTasks.get(0).getTitle().contains("second"));
102      }
103  
104      @Test
105      @InSequence(4)
106      public void taskDao_should_provide_basic_case_insensitive_full_text_search() {
107          // given
108          String taskTitlePart = "FIRST";
109  
110          // when
111          List<Task> titledTasks = taskDao.getForTitle(detachedUser, taskTitlePart);
112  
113          // then
114          assertEquals(1, titledTasks.size());
115          assertTrue(titledTasks.get(0).getTitle().contains("first"));
116      }
117  
118      @Test
119      @InSequence(5)
120      public void taskDao_should_remove_task_from_detachedUser() {
121          // given
122          Task task = new Task();
123          task.setId(1L);
124          task.setOwner(detachedUser);
```
  * file:///tmp/source-code/src/test/java/org/jboss/as/quickstarts/tasksJsf/TaskDaoIT.java
      * Line Number: 25
      * Message: 'Replace the `javax.persistence` import statement with `jakarta.persistence`'
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
 19  import static org.junit.Assert.assertEquals;
 20  import static org.junit.Assert.assertTrue;
 21  
 22  import java.io.FileNotFoundException;
 23  import java.util.List;
 24  import javax.inject.Inject;
 25  import javax.persistence.EntityManager;
 26  
 27  import org.jboss.arquillian.container.test.api.Deployment;
 28  import org.jboss.arquillian.junit.Arquillian;
 29  import org.jboss.arquillian.junit.InSequence;
 30  import org.jboss.shrinkwrap.api.spec.WebArchive;
 31  import org.junit.Before;
 32  import org.junit.Test;
 33  import org.junit.runner.RunWith;
 34  
 35  /**
 36   * @author Lukas Fryc
 37   * @author Oliver Kiss
 38   */
 39  @RunWith(Arquillian.class)
 40  public class TaskDaoIT {
 41  
 42      @Deployment
 43      public static WebArchive deployment() throws IllegalArgumentException, FileNotFoundException {
 44          return new DefaultDeployment().withPersistence().withImportedData().getArchive()
 45                  .addClasses(Resources.class, User.class, UserDao.class, Task.class, TaskDao.class, TaskDaoImpl.class);
 46      }
 47  
 48      @Inject
 49      private EntityManager em;
 50  
 51      @Inject
 52      private TaskDao taskDao;
 53  
 54      private User detachedUser;
 55  
 56      @Before
 57      public void setUp() throws Exception {
 58          detachedUser = new User("jdoe");
 59          detachedUser.setId(1L);
 60      }
 61  
 62      @Test
 63      @InSequence(1)
 64      public void user_should_be_created_with_one_task_attached() throws Exception {
 65          // given
 66          User user = new User("New user");
 67          Task task = new Task("New task");
 68  
 69          // when
 70          em.persist(user);
 71          taskDao.createTask(user, task);
 72          List<Task> userTasks = em.createQuery("SELECT t FROM Task t WHERE t.owner = :owner", Task.class)
 73                  .setParameter("owner", user).getResultList();
 74  
 75          // then
 76          assertEquals(1, userTasks.size());
 77          assertEquals(task, userTasks.get(0));
 78      }
 79  
 80      @Test
 81      @InSequence(2)
 82      public void all_tasks_should_be_obtained_from_detachedUser() {
 83          // when
 84          List<Task> userTasks = taskDao.getAll(detachedUser);
 85  
 86          // then
 87          assertEquals(2, userTasks.size());
 88      }
 89  
 90      @Test
 91      @InSequence(3)
 92      public void range_of_tasks_should_be_provided_by_taskDao() {
 93          // when
 94          List<Task> headOfTasks = taskDao.getRange(detachedUser, 0, 1);
 95          List<Task> tailOfTasks = taskDao.getRange(detachedUser, 1, 1);
 96  
 97          // then
 98          assertEquals(1, headOfTasks.size());
 99          assertEquals(1, tailOfTasks.size());
100          assertTrue(headOfTasks.get(0).getTitle().contains("first"));
101          assertTrue(tailOfTasks.get(0).getTitle().contains("second"));
102      }
103  
104      @Test
105      @InSequence(4)
106      public void taskDao_should_provide_basic_case_insensitive_full_text_search() {
107          // given
108          String taskTitlePart = "FIRST";
109  
110          // when
111          List<Task> titledTasks = taskDao.getForTitle(detachedUser, taskTitlePart);
112  
113          // then
114          assertEquals(1, titledTasks.size());
115          assertTrue(titledTasks.get(0).getTitle().contains("first"));
116      }
117  
118      @Test
119      @InSequence(5)
120      public void taskDao_should_remove_task_from_detachedUser() {
121          // given
122          Task task = new Task();
123          task.setId(1L);
124          task.setOwner(detachedUser);
125          assertEquals(2, taskDao.getAll(detachedUser).size());
```
  * file:///tmp/source-code/src/test/java/org/jboss/as/quickstarts/tasksJsf/TaskListBeanIT.java
      * Line Number: 22
      * Message: 'Replace the `javax.inject` import statement with `jakarta.inject`'
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
 19  import static org.junit.Assert.assertEquals;
 20  
 21  import java.io.FileNotFoundException;
 22  import javax.inject.Inject;
 23  
 24  import org.jboss.arquillian.container.test.api.Deployment;
 25  import org.jboss.arquillian.junit.Arquillian;
 26  import org.jboss.shrinkwrap.api.spec.WebArchive;
 27  import org.junit.Test;
 28  import org.junit.runner.RunWith;
 29  
 30  /**
 31   * @author Lukas Fryc
 32   */
 33  @RunWith(Arquillian.class)
 34  public class TaskListBeanIT {
 35  
 36      public static final String WEBAPP_SRC = "src/main/webapp";
 37  
 38      @Deployment
 39      public static WebArchive deployment() throws IllegalArgumentException, FileNotFoundException {
 40          return new DefaultDeployment(true).withPersistence().withImportedData().getArchive()
 41                  .addClasses(User.class, Task.class, TaskList.class, TaskListBean.class, TaskDao.class, TaskDaoStub.class, Testing.class);
 42      }
 43  
 44      @Inject
 45      private TaskDao taskDaoStub;
 46  
 47      @Inject
 48      private TaskList taskList;
 49  
 50      @Test
 51      public void dao_method_getAll_should_be_called_only_once_on() {
 52          taskList.getAll();
 53          taskList.getAll();
 54          taskList.getAll();
 55          assertEquals(1, ((TaskDaoStub) taskDaoStub).getGetAllCallsCount());
 56      }
 57  
 58      @Test
 59      public void dao_method_getAll_should_be_called_after_invalidation() {
 60          taskList.getAll();
 61          taskList.getAll();
 62          assertEquals(1, ((TaskDaoStub) taskDaoStub).getGetAllCallsCount());
 63          taskList.invalidate();
 64          assertEquals(1, ((TaskDaoStub) taskDaoStub).getGetAllCallsCount());
 65          taskList.getAll();
 66          taskList.getAll();
 67          assertEquals(2, ((TaskDaoStub) taskDaoStub).getGetAllCallsCount());
 68      }
 69  }

```
  * file:///tmp/source-code/src/test/java/org/jboss/as/quickstarts/tasksJsf/Testing.java
      * Line Number: 24
      * Message: 'Replace the `javax.enterprise` import statement with `jakarta.enterprise`'
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
 19  import java.lang.annotation.Documented;
 20  import java.lang.annotation.Inherited;
 21  import java.lang.annotation.Retention;
 22  import java.lang.annotation.Target;
 23  
 24  import javax.enterprise.context.RequestScoped;
 25  import javax.enterprise.inject.Alternative;
 26  import javax.enterprise.inject.Stereotype;
 27  
 28  import static java.lang.annotation.ElementType.FIELD;
 29  import static java.lang.annotation.ElementType.METHOD;
 30  import static java.lang.annotation.ElementType.TYPE;
 31  import static java.lang.annotation.RetentionPolicy.RUNTIME;
 32  
 33  /**
 34   * Alternative testing annotation, used to enable all testing alternatives.
 35   * @author jporter
 36   */
 37  @Stereotype
 38  @Inherited
 39  @Alternative
 40  @RequestScoped
 41  @Target({ TYPE, METHOD, FIELD })
 42  @Retention(RUNTIME)
 43  @Documented
 44  public @interface Testing {
 45  
 46  }

```
  * file:///tmp/source-code/src/test/java/org/jboss/as/quickstarts/tasksJsf/Testing.java
      * Line Number: 25
      * Message: 'Replace the `javax.enterprise` import statement with `jakarta.enterprise`'
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
 19  import java.lang.annotation.Documented;
 20  import java.lang.annotation.Inherited;
 21  import java.lang.annotation.Retention;
 22  import java.lang.annotation.Target;
 23  
 24  import javax.enterprise.context.RequestScoped;
 25  import javax.enterprise.inject.Alternative;
 26  import javax.enterprise.inject.Stereotype;
 27  
 28  import static java.lang.annotation.ElementType.FIELD;
 29  import static java.lang.annotation.ElementType.METHOD;
 30  import static java.lang.annotation.ElementType.TYPE;
 31  import static java.lang.annotation.RetentionPolicy.RUNTIME;
 32  
 33  /**
 34   * Alternative testing annotation, used to enable all testing alternatives.
 35   * @author jporter
 36   */
 37  @Stereotype
 38  @Inherited
 39  @Alternative
 40  @RequestScoped
 41  @Target({ TYPE, METHOD, FIELD })
 42  @Retention(RUNTIME)
 43  @Documented
 44  public @interface Testing {
 45  
 46  }

```
  * file:///tmp/source-code/src/test/java/org/jboss/as/quickstarts/tasksJsf/Testing.java
      * Line Number: 26
      * Message: 'Replace the `javax.enterprise` import statement with `jakarta.enterprise`'
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
 19  import java.lang.annotation.Documented;
 20  import java.lang.annotation.Inherited;
 21  import java.lang.annotation.Retention;
 22  import java.lang.annotation.Target;
 23  
 24  import javax.enterprise.context.RequestScoped;
 25  import javax.enterprise.inject.Alternative;
 26  import javax.enterprise.inject.Stereotype;
 27  
 28  import static java.lang.annotation.ElementType.FIELD;
 29  import static java.lang.annotation.ElementType.METHOD;
 30  import static java.lang.annotation.ElementType.TYPE;
 31  import static java.lang.annotation.RetentionPolicy.RUNTIME;
 32  
 33  /**
 34   * Alternative testing annotation, used to enable all testing alternatives.
 35   * @author jporter
 36   */
 37  @Stereotype
 38  @Inherited
 39  @Alternative
 40  @RequestScoped
 41  @Target({ TYPE, METHOD, FIELD })
 42  @Retention(RUNTIME)
 43  @Documented
 44  public @interface Testing {
 45  
 46  }

```
  * file:///tmp/source-code/src/test/java/org/jboss/as/quickstarts/tasksJsf/UserDaoIT.java
      * Line Number: 23
      * Message: 'Replace the `javax.inject` import statement with `jakarta.inject`'
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
 19  import static org.junit.Assert.assertNull;
 20  import static org.junit.Assert.assertTrue;
 21  
 22  import java.io.FileNotFoundException;
 23  import javax.inject.Inject;
 24  import javax.persistence.EntityManager;
 25  
 26  import org.jboss.arquillian.container.test.api.Deployment;
 27  import org.jboss.arquillian.junit.Arquillian;
 28  import org.jboss.shrinkwrap.api.spec.WebArchive;
 29  import org.junit.Assert;
 30  import org.junit.Test;
 31  import org.junit.runner.RunWith;
 32  
 33  /**
 34   * @author Lukas Fryc
 35   * @author Oliver Kiss
 36   */
 37  @RunWith(Arquillian.class)
 38  public class UserDaoIT {
 39  
 40      @Deployment
 41      public static WebArchive deployment() throws IllegalArgumentException, FileNotFoundException {
 42          return new DefaultDeployment().withPersistence().withImportedData().getArchive()
 43                  .addClasses(Resources.class, User.class, UserDao.class, Task.class, TaskDao.class, UserDaoImpl.class);
 44      }
 45  
 46      @Inject
 47      private UserDao userDao;
 48  
 49      @Inject
 50      private EntityManager em;
 51  
 52      @Test
 53      public void userDao_should_create_user_so_it_could_be_retrieved_from_userDao_by_username() {
 54          // given
 55          User created = new User("username1");
 56  
 57          // when
 58          userDao.createUser(created);
 59          User retrieved = userDao.getForUsername("username1");
 60  
 61          // then
 62          assertTrue(em.contains(created));
 63          assertTrue(em.contains(retrieved));
 64          Assert.assertEquals(created, retrieved);
 65      }
 66  
 67      @Test
 68      public void user_should_be_retrievable_from_userDao_by_username() {
 69          // given
 70          String username = "jdoe";
 71  
 72          // when
 73          User retrieved = userDao.getForUsername(username);
 74  
 75          // then
 76          Assert.assertEquals(username, retrieved.getUsername());
 77      }
 78  
 79      @Test
 80      public void userDao_should_return_null_when_searching_for_non_existent_user() {
 81          // given
 82          String nonExistent = "nonExistent";
 83  
 84          // when
 85          User retrieved = userDao.getForUsername(nonExistent);
 86  
 87          // then
 88          assertNull(retrieved);
 89      }
 90  }

```
  * file:///tmp/source-code/src/test/java/org/jboss/as/quickstarts/tasksJsf/UserDaoIT.java
      * Line Number: 24
      * Message: 'Replace the `javax.persistence` import statement with `jakarta.persistence`'
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
 19  import static org.junit.Assert.assertNull;
 20  import static org.junit.Assert.assertTrue;
 21  
 22  import java.io.FileNotFoundException;
 23  import javax.inject.Inject;
 24  import javax.persistence.EntityManager;
 25  
 26  import org.jboss.arquillian.container.test.api.Deployment;
 27  import org.jboss.arquillian.junit.Arquillian;
 28  import org.jboss.shrinkwrap.api.spec.WebArchive;
 29  import org.junit.Assert;
 30  import org.junit.Test;
 31  import org.junit.runner.RunWith;
 32  
 33  /**
 34   * @author Lukas Fryc
 35   * @author Oliver Kiss
 36   */
 37  @RunWith(Arquillian.class)
 38  public class UserDaoIT {
 39  
 40      @Deployment
 41      public static WebArchive deployment() throws IllegalArgumentException, FileNotFoundException {
 42          return new DefaultDeployment().withPersistence().withImportedData().getArchive()
 43                  .addClasses(Resources.class, User.class, UserDao.class, Task.class, TaskDao.class, UserDaoImpl.class);
 44      }
 45  
 46      @Inject
 47      private UserDao userDao;
 48  
 49      @Inject
 50      private EntityManager em;
 51  
 52      @Test
 53      public void userDao_should_create_user_so_it_could_be_retrieved_from_userDao_by_username() {
 54          // given
 55          User created = new User("username1");
 56  
 57          // when
 58          userDao.createUser(created);
 59          User retrieved = userDao.getForUsername("username1");
 60  
 61          // then
 62          assertTrue(em.contains(created));
 63          assertTrue(em.contains(retrieved));
 64          Assert.assertEquals(created, retrieved);
 65      }
 66  
 67      @Test
 68      public void user_should_be_retrievable_from_userDao_by_username() {
 69          // given
 70          String username = "jdoe";
 71  
 72          // when
 73          User retrieved = userDao.getForUsername(username);
 74  
 75          // then
 76          Assert.assertEquals(username, retrieved.getUsername());
 77      }
 78  
 79      @Test
 80      public void userDao_should_return_null_when_searching_for_non_existent_user() {
 81          // given
 82          String nonExistent = "nonExistent";
 83  
 84          // when
 85          User retrieved = userDao.getForUsername(nonExistent);
 86  
 87          // then
 88          assertNull(retrieved);
 89      }
 90  }

```
### #15 - javax-to-jakarta-servlet-00060
* Category: mandatory
* Effort: 1
* Description: Method in javax.servlet.ServletRequestWrapper has been removed
* Labels: konveyor.io/source, konveyor.io/target=eap, konveyor.io/target=eap8, konveyor.io/target=jakarta-ee, konveyor.io/target=jakarta-ee9+
* Links
  * Red Hat JBoss EAP Application Migration from Jakarta EE 8 to EE 10 - Jakarta Servlet: https://access.redhat.com/articles/6980265#servlet
* Incidents
  * file:///tmp/source-code/src/test/java/org/jboss/as/quickstarts/tasksJsf/FacesContextStub.java
      * Line Number: 39
      * Message: 'Method `getRealPath` in javax.servlet.ServletRequestWrapper has been removed. It can be replaced with `ServletContext.getRealPath(String path)`.'
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
 19  import java.util.Iterator;
 20  
 21  import javax.faces.application.Application;
 22  import javax.faces.application.FacesMessage;
 23  import javax.faces.application.FacesMessage.Severity;
 24  import javax.faces.component.UIViewRoot;
 25  import javax.faces.context.ExternalContext;
 26  import javax.faces.context.FacesContext;
 27  import javax.faces.context.ResponseStream;
 28  import javax.faces.context.ResponseWriter;
 29  import javax.faces.render.RenderKit;
 30  
 31  /**
 32   * Stub of {@link FacesContext} to allow testing without real JSF session.
 33   *
 34   * @author Lukas Fryc
 35   *
 36   */
 37  public class FacesContextStub extends FacesContext {
 38  
 39      FacesContextStub(String test) {
 40      }
 41  
 42      public static void setCurrentInstance(FacesContext facesContext) {
 43          FacesContext.setCurrentInstance(facesContext);
 44      }
 45  
 46      @Override
 47      public Application getApplication() {
 48          return null;
 49      }
 50  
 51      @Override
 52      public Iterator<String> getClientIdsWithMessages() {
 53          return null;
 54      }
 55  
 56      @Override
 57      public ExternalContext getExternalContext() {
 58          return null;
 59      }
 60  
 61      @Override
 62      public Severity getMaximumSeverity() {
 63          return null;
 64      }
 65  
 66      @Override
 67      public Iterator<FacesMessage> getMessages() {
 68          return null;
 69      }
 70  
 71      @Override
 72      public Iterator<FacesMessage> getMessages(String clientId) {
 73          return null;
 74      }
 75  
 76      @Override
 77      public RenderKit getRenderKit() {
 78          return null;
 79      }
 80  
 81      @Override
 82      public boolean getRenderResponse() {
 83          return false;
 84      }
 85  
 86      @Override
 87      public boolean getResponseComplete() {
 88          return false;
 89      }
 90  
 91      @Override
 92      public ResponseStream getResponseStream() {
 93  
 94          return null;
 95      }
 96  
 97      @Override
 98      public void setResponseStream(ResponseStream responseStream) {
 99  
100      }
101  
102      @Override
103      public ResponseWriter getResponseWriter() {
104  
105          return null;
106      }
107  
108      @Override
109      public void setResponseWriter(ResponseWriter responseWriter) {
110  
111      }
112  
113      @Override
114      public UIViewRoot getViewRoot() {
115  
116          return null;
117      }
118  
119      @Override
120      public void setViewRoot(UIViewRoot root) {
121  
122      }
123  
124      @Override
125      public void addMessage(String clientId, FacesMessage message) {
126  
127      }
128  
129      @Override
130      public void release() {
131  
132      }
133  
134      @Override
135      public void renderResponse() {
136  
137      }
138  
139      @Override
```
### #16 - javax-to-jakarta-servlet-00100
* Category: mandatory
* Effort: 1
* Description: Method encodeUrl in javax.servlet.http.HttpServletResponse has been removed
* Labels: konveyor.io/source, konveyor.io/target=eap, konveyor.io/target=eap8, konveyor.io/target=jakarta-ee, konveyor.io/target=jakarta-ee9+
* Links
  * Red Hat JBoss EAP Application Migration from Jakarta EE 8 to EE 10 - Jakarta Servlet: https://access.redhat.com/articles/6980265#servlet
* Incidents
  * file:///tmp/source-code/src/test/java/org/jboss/as/quickstarts/tasksJsf/FacesContextStub.java
      * Line Number: 39
      * Message: 'Method encodeURL in javax.servlet.http.HttpServletResponse has been removed. Use encodeURL(String) instead.'
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
 19  import java.util.Iterator;
 20  
 21  import javax.faces.application.Application;
 22  import javax.faces.application.FacesMessage;
 23  import javax.faces.application.FacesMessage.Severity;
 24  import javax.faces.component.UIViewRoot;
 25  import javax.faces.context.ExternalContext;
 26  import javax.faces.context.FacesContext;
 27  import javax.faces.context.ResponseStream;
 28  import javax.faces.context.ResponseWriter;
 29  import javax.faces.render.RenderKit;
 30  
 31  /**
 32   * Stub of {@link FacesContext} to allow testing without real JSF session.
 33   *
 34   * @author Lukas Fryc
 35   *
 36   */
 37  public class FacesContextStub extends FacesContext {
 38  
 39      FacesContextStub(String test) {
 40      }
 41  
 42      public static void setCurrentInstance(FacesContext facesContext) {
 43          FacesContext.setCurrentInstance(facesContext);
 44      }
 45  
 46      @Override
 47      public Application getApplication() {
 48          return null;
 49      }
 50  
 51      @Override
 52      public Iterator<String> getClientIdsWithMessages() {
 53          return null;
 54      }
 55  
 56      @Override
 57      public ExternalContext getExternalContext() {
 58          return null;
 59      }
 60  
 61      @Override
 62      public Severity getMaximumSeverity() {
 63          return null;
 64      }
 65  
 66      @Override
 67      public Iterator<FacesMessage> getMessages() {
 68          return null;
 69      }
 70  
 71      @Override
 72      public Iterator<FacesMessage> getMessages(String clientId) {
 73          return null;
 74      }
 75  
 76      @Override
 77      public RenderKit getRenderKit() {
 78          return null;
 79      }
 80  
 81      @Override
 82      public boolean getRenderResponse() {
 83          return false;
 84      }
 85  
 86      @Override
 87      public boolean getResponseComplete() {
 88          return false;
 89      }
 90  
 91      @Override
 92      public ResponseStream getResponseStream() {
 93  
 94          return null;
 95      }
 96  
 97      @Override
 98      public void setResponseStream(ResponseStream responseStream) {
 99  
100      }
101  
102      @Override
103      public ResponseWriter getResponseWriter() {
104  
105          return null;
106      }
107  
108      @Override
109      public void setResponseWriter(ResponseWriter responseWriter) {
110  
111      }
112  
113      @Override
114      public UIViewRoot getViewRoot() {
115  
116          return null;
117      }
118  
119      @Override
120      public void setViewRoot(UIViewRoot root) {
121  
122      }
123  
124      @Override
125      public void addMessage(String clientId, FacesMessage message) {
126  
127      }
128  
129      @Override
130      public void release() {
131  
132      }
133  
134      @Override
135      public void renderResponse() {
136  
137      }
138  
139      @Override
```
### #17 - javax-to-jakarta-servlet-00101
* Category: mandatory
* Effort: 1
* Description: Method encodeRedirectUrl in javax.servlet.http.HttpServletResponse has been removed
* Labels: konveyor.io/source, konveyor.io/target=eap, konveyor.io/target=eap8, konveyor.io/target=jakarta-ee, konveyor.io/target=jakarta-ee9+
* Links
  * Red Hat JBoss EAP Application Migration from Jakarta EE 8 to EE 10 - Jakarta Servlet: https://access.redhat.com/articles/6980265#servlet
* Incidents
  * file:///tmp/source-code/src/test/java/org/jboss/as/quickstarts/tasksJsf/FacesContextStub.java
      * Line Number: 39
      * Message: 'Method encodeRedirectUrl(String) in javax.servlet.http.HttpServletResponse has been removed. Use encodeRedirectURL(String) instead.'
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
 19  import java.util.Iterator;
 20  
 21  import javax.faces.application.Application;
 22  import javax.faces.application.FacesMessage;
 23  import javax.faces.application.FacesMessage.Severity;
 24  import javax.faces.component.UIViewRoot;
 25  import javax.faces.context.ExternalContext;
 26  import javax.faces.context.FacesContext;
 27  import javax.faces.context.ResponseStream;
 28  import javax.faces.context.ResponseWriter;
 29  import javax.faces.render.RenderKit;
 30  
 31  /**
 32   * Stub of {@link FacesContext} to allow testing without real JSF session.
 33   *
 34   * @author Lukas Fryc
 35   *
 36   */
 37  public class FacesContextStub extends FacesContext {
 38  
 39      FacesContextStub(String test) {
 40      }
 41  
 42      public static void setCurrentInstance(FacesContext facesContext) {
 43          FacesContext.setCurrentInstance(facesContext);
 44      }
 45  
 46      @Override
 47      public Application getApplication() {
 48          return null;
 49      }
 50  
 51      @Override
 52      public Iterator<String> getClientIdsWithMessages() {
 53          return null;
 54      }
 55  
 56      @Override
 57      public ExternalContext getExternalContext() {
 58          return null;
 59      }
 60  
 61      @Override
 62      public Severity getMaximumSeverity() {
 63          return null;
 64      }
 65  
 66      @Override
 67      public Iterator<FacesMessage> getMessages() {
 68          return null;
 69      }
 70  
 71      @Override
 72      public Iterator<FacesMessage> getMessages(String clientId) {
 73          return null;
 74      }
 75  
 76      @Override
 77      public RenderKit getRenderKit() {
 78          return null;
 79      }
 80  
 81      @Override
 82      public boolean getRenderResponse() {
 83          return false;
 84      }
 85  
 86      @Override
 87      public boolean getResponseComplete() {
 88          return false;
 89      }
 90  
 91      @Override
 92      public ResponseStream getResponseStream() {
 93  
 94          return null;
 95      }
 96  
 97      @Override
 98      public void setResponseStream(ResponseStream responseStream) {
 99  
100      }
101  
102      @Override
103      public ResponseWriter getResponseWriter() {
104  
105          return null;
106      }
107  
108      @Override
109      public void setResponseWriter(ResponseWriter responseWriter) {
110  
111      }
112  
113      @Override
114      public UIViewRoot getViewRoot() {
115  
116          return null;
117      }
118  
119      @Override
120      public void setViewRoot(UIViewRoot root) {
121  
122      }
123  
124      @Override
125      public void addMessage(String clientId, FacesMessage message) {
126  
127      }
128  
129      @Override
130      public void release() {
131  
132      }
133  
134      @Override
135      public void renderResponse() {
136  
137      }
138  
139      @Override
```
### #18 - javax-to-jakarta-servlet-00110
* Category: mandatory
* Effort: 1
* Description: Method encodeUrl in javax.servlet.http.HttpServletResponseWrapper has been removed
* Labels: konveyor.io/source, konveyor.io/target=eap, konveyor.io/target=eap8, konveyor.io/target=jakarta-ee, konveyor.io/target=jakarta-ee9+
* Links
  * Red Hat JBoss EAP Application Migration from Jakarta EE 8 to EE 10 - Jakarta Servlet: https://access.redhat.com/articles/6980265#servlet
* Incidents
  * file:///tmp/source-code/src/test/java/org/jboss/as/quickstarts/tasksJsf/FacesContextStub.java
      * Line Number: 39
      * Message: 'Method encodeUrl in javax.servlet.http.HttpServletResponseWrapper has been removed. Use encodeURL instead.'
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
 19  import java.util.Iterator;
 20  
 21  import javax.faces.application.Application;
 22  import javax.faces.application.FacesMessage;
 23  import javax.faces.application.FacesMessage.Severity;
 24  import javax.faces.component.UIViewRoot;
 25  import javax.faces.context.ExternalContext;
 26  import javax.faces.context.FacesContext;
 27  import javax.faces.context.ResponseStream;
 28  import javax.faces.context.ResponseWriter;
 29  import javax.faces.render.RenderKit;
 30  
 31  /**
 32   * Stub of {@link FacesContext} to allow testing without real JSF session.
 33   *
 34   * @author Lukas Fryc
 35   *
 36   */
 37  public class FacesContextStub extends FacesContext {
 38  
 39      FacesContextStub(String test) {
 40      }
 41  
 42      public static void setCurrentInstance(FacesContext facesContext) {
 43          FacesContext.setCurrentInstance(facesContext);
 44      }
 45  
 46      @Override
 47      public Application getApplication() {
 48          return null;
 49      }
 50  
 51      @Override
 52      public Iterator<String> getClientIdsWithMessages() {
 53          return null;
 54      }
 55  
 56      @Override
 57      public ExternalContext getExternalContext() {
 58          return null;
 59      }
 60  
 61      @Override
 62      public Severity getMaximumSeverity() {
 63          return null;
 64      }
 65  
 66      @Override
 67      public Iterator<FacesMessage> getMessages() {
 68          return null;
 69      }
 70  
 71      @Override
 72      public Iterator<FacesMessage> getMessages(String clientId) {
 73          return null;
 74      }
 75  
 76      @Override
 77      public RenderKit getRenderKit() {
 78          return null;
 79      }
 80  
 81      @Override
 82      public boolean getRenderResponse() {
 83          return false;
 84      }
 85  
 86      @Override
 87      public boolean getResponseComplete() {
 88          return false;
 89      }
 90  
 91      @Override
 92      public ResponseStream getResponseStream() {
 93  
 94          return null;
 95      }
 96  
 97      @Override
 98      public void setResponseStream(ResponseStream responseStream) {
 99  
100      }
101  
102      @Override
103      public ResponseWriter getResponseWriter() {
104  
105          return null;
106      }
107  
108      @Override
109      public void setResponseWriter(ResponseWriter responseWriter) {
110  
111      }
112  
113      @Override
114      public UIViewRoot getViewRoot() {
115  
116          return null;
117      }
118  
119      @Override
120      public void setViewRoot(UIViewRoot root) {
121  
122      }
123  
124      @Override
125      public void addMessage(String clientId, FacesMessage message) {
126  
127      }
128  
129      @Override
130      public void release() {
131  
132      }
133  
134      @Override
135      public void renderResponse() {
136  
137      }
138  
139      @Override
```
### #19 - javax-to-jakarta-servlet-00111
* Category: mandatory
* Effort: 1
* Description: Method encodeRedirectUrl in javax.servlet.http.HttpServletResponseWrapper has been removed
* Labels: konveyor.io/source, konveyor.io/target=eap, konveyor.io/target=eap8, konveyor.io/target=jakarta-ee, konveyor.io/target=jakarta-ee9+
* Links
  * Red Hat JBoss EAP Application Migration from Jakarta EE 8 to EE 10 - Jakarta Servlet: https://access.redhat.com/articles/6980265#servlet
* Incidents
  * file:///tmp/source-code/src/test/java/org/jboss/as/quickstarts/tasksJsf/FacesContextStub.java
      * Line Number: 39
      * Message: 'Method encodeRedirectUrl in javax.servlet.http.HttpServletResponseWrapper has been removed. Use encodeRedirectURL instead.'
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
 19  import java.util.Iterator;
 20  
 21  import javax.faces.application.Application;
 22  import javax.faces.application.FacesMessage;
 23  import javax.faces.application.FacesMessage.Severity;
 24  import javax.faces.component.UIViewRoot;
 25  import javax.faces.context.ExternalContext;
 26  import javax.faces.context.FacesContext;
 27  import javax.faces.context.ResponseStream;
 28  import javax.faces.context.ResponseWriter;
 29  import javax.faces.render.RenderKit;
 30  
 31  /**
 32   * Stub of {@link FacesContext} to allow testing without real JSF session.
 33   *
 34   * @author Lukas Fryc
 35   *
 36   */
 37  public class FacesContextStub extends FacesContext {
 38  
 39      FacesContextStub(String test) {
 40      }
 41  
 42      public static void setCurrentInstance(FacesContext facesContext) {
 43          FacesContext.setCurrentInstance(facesContext);
 44      }
 45  
 46      @Override
 47      public Application getApplication() {
 48          return null;
 49      }
 50  
 51      @Override
 52      public Iterator<String> getClientIdsWithMessages() {
 53          return null;
 54      }
 55  
 56      @Override
 57      public ExternalContext getExternalContext() {
 58          return null;
 59      }
 60  
 61      @Override
 62      public Severity getMaximumSeverity() {
 63          return null;
 64      }
 65  
 66      @Override
 67      public Iterator<FacesMessage> getMessages() {
 68          return null;
 69      }
 70  
 71      @Override
 72      public Iterator<FacesMessage> getMessages(String clientId) {
 73          return null;
 74      }
 75  
 76      @Override
 77      public RenderKit getRenderKit() {
 78          return null;
 79      }
 80  
 81      @Override
 82      public boolean getRenderResponse() {
 83          return false;
 84      }
 85  
 86      @Override
 87      public boolean getResponseComplete() {
 88          return false;
 89      }
 90  
 91      @Override
 92      public ResponseStream getResponseStream() {
 93  
 94          return null;
 95      }
 96  
 97      @Override
 98      public void setResponseStream(ResponseStream responseStream) {
 99  
100      }
101  
102      @Override
103      public ResponseWriter getResponseWriter() {
104  
105          return null;
106      }
107  
108      @Override
109      public void setResponseWriter(ResponseWriter responseWriter) {
110  
111      }
112  
113      @Override
114      public UIViewRoot getViewRoot() {
115  
116          return null;
117      }
118  
119      @Override
120      public void setViewRoot(UIViewRoot root) {
121  
122      }
123  
124      @Override
125      public void addMessage(String clientId, FacesMessage message) {
126  
127      }
128  
129      @Override
130      public void release() {
131  
132      }
133  
134      @Override
135      public void renderResponse() {
136  
137      }
138  
139      @Override
```
