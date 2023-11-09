# eap8/eap7
## Description
This ruleset provides rules to support the migration to hibernate search 6.0. Developed under WINDUPRULE-900
* Source of rules: https://github.com/konveyor/rulesets/tree/main/default/generated/quarkus
* Sample application: https://github.com/deewhyweb/eap-coolstore-monolith
## Violations
Number of Violations: 13
### #0 - javaee-to-jakarta-namespaces-00001
* Category: mandatory
* Effort: 1
* Description: Replace the Java EE namespace, schemaLocation and version with the Jakarta equivalent
Replace `http://xmlns.jcp.org/xml/ns/javaee` with `https://jakarta.ee/xml/ns/jakartaee` and change the schema version number
* Labels: konveyor.io/target=jakarta-ee9+, konveyor.io/target=jakarta-ee, konveyor.io/target=eap8, konveyor.io/target=eap, konveyor.io/source
* Links
  * Jakarta EE XML Schemas: https://jakarta.ee/xml/ns/jakartaee/#10
* Incidents
  * file:///opt/input/source/src/main/webapp/WEB-INF/beans.xml
      * Replace `http://xmlns.jcp.org/xml/ns/javaee` with `https://jakarta.ee/xml/ns/jakartaee` and change the schema version number
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <!--
  3      JBoss, Home of Professional Open Source
  4      Copyright 2015, Red Hat, Inc. and/or its affiliates, and individual
  5      contributors by the @authors tag. See the copyright.txt in the
  6      distribution for a full listing of individual contributors.
  7      Licensed under the Apache License, Version 2.0 (the "License");
  8      you may not use this file except in compliance with the License.
  9      You may obtain a copy of the License at
 10      http://www.apache.org/licenses/LICENSE-2.0
 11      Unless required by applicable law or agreed to in writing, software
 12      distributed under the License is distributed on an "AS IS" BASIS,
 13      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 14      See the License for the specific language governing permissions and
 15      limitations under the License.
 16  -->
 17  <!-- Marker file indicating CDI should be enabled -->
 18  <beans xmlns="http://xmlns.jcp.org/xml/ns/javaee" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 19  	   xsi:schemaLocation="
 20        http://xmlns.jcp.org/xml/ns/javaee
 21        http://xmlns.jcp.org/xml/ns/javaee/beans_1_1.xsd"
 22  	   bean-discovery-mode="all">
 23  </beans>

```
  * file:///opt/input/source/src/main/webapp/WEB-INF/beans.xml
      * Replace `http://xmlns.jcp.org/xml/ns/javaee` with `https://jakarta.ee/xml/ns/jakartaee` and change the schema version number
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <!--
  3      JBoss, Home of Professional Open Source
  4      Copyright 2015, Red Hat, Inc. and/or its affiliates, and individual
  5      contributors by the @authors tag. See the copyright.txt in the
  6      distribution for a full listing of individual contributors.
  7      Licensed under the Apache License, Version 2.0 (the "License");
  8      you may not use this file except in compliance with the License.
  9      You may obtain a copy of the License at
 10      http://www.apache.org/licenses/LICENSE-2.0
 11      Unless required by applicable law or agreed to in writing, software
 12      distributed under the License is distributed on an "AS IS" BASIS,
 13      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 14      See the License for the specific language governing permissions and
 15      limitations under the License.
 16  -->
 17  <!-- Marker file indicating CDI should be enabled -->
 18  <beans xmlns="http://xmlns.jcp.org/xml/ns/javaee" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 19  	   xsi:schemaLocation="
 20        http://xmlns.jcp.org/xml/ns/javaee
 21        http://xmlns.jcp.org/xml/ns/javaee/beans_1_1.xsd"
 22  	   bean-discovery-mode="all">
 23  </beans>

```
  * file:///opt/input/source/src/main/webapp/WEB-INF/beans.xml
      * Replace `http://xmlns.jcp.org/xml/ns/javaee` with `https://jakarta.ee/xml/ns/jakartaee` and change the schema version number
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <!--
  3      JBoss, Home of Professional Open Source
  4      Copyright 2015, Red Hat, Inc. and/or its affiliates, and individual
  5      contributors by the @authors tag. See the copyright.txt in the
  6      distribution for a full listing of individual contributors.
  7      Licensed under the Apache License, Version 2.0 (the "License");
  8      you may not use this file except in compliance with the License.
  9      You may obtain a copy of the License at
 10      http://www.apache.org/licenses/LICENSE-2.0
 11      Unless required by applicable law or agreed to in writing, software
 12      distributed under the License is distributed on an "AS IS" BASIS,
 13      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 14      See the License for the specific language governing permissions and
 15      limitations under the License.
 16  -->
 17  <!-- Marker file indicating CDI should be enabled -->
 18  <beans xmlns="http://xmlns.jcp.org/xml/ns/javaee" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 19  	   xsi:schemaLocation="
 20        http://xmlns.jcp.org/xml/ns/javaee
 21        http://xmlns.jcp.org/xml/ns/javaee/beans_1_1.xsd"
 22  	   bean-discovery-mode="all">
 23  </beans>

```
### #1 - javaee-to-jakarta-namespaces-00002
* Category: mandatory
* Effort: 1
* Description: Replace the Java EE persistence namespace, schemaLocation and version with the Jakarta equivalent
Replace `http://xmlns.jcp.org/xml/ns/persistence` with `https://jakarta.ee/xml/ns/persistence` and change the schema version number
* Labels: konveyor.io/target=jakarta-ee9+, konveyor.io/target=jakarta-ee, konveyor.io/target=eap8, konveyor.io/target=eap, konveyor.io/source
* Links
  * Jakarta Persistence XML Schemas: https://jakarta.ee/xml/ns/persistence/#3
* Incidents
  * file:///opt/input/source/target/classes/META-INF/persistence.xml
      * Replace `http://xmlns.jcp.org/xml/ns/persistence` with `https://jakarta.ee/xml/ns/persistence` and change the schema version number
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <persistence version="2.1"
  3               xmlns="http://xmlns.jcp.org/xml/ns/persistence" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  4               xsi:schemaLocation="
  5          http://xmlns.jcp.org/xml/ns/persistence
  6          http://xmlns.jcp.org/xml/ns/persistence/persistence_2_1.xsd">
  7      <persistence-unit name="primary">
  8          <jta-data-source>java:jboss/datasources/CoolstoreDS</jta-data-source>
  9          <properties>
 10              <property name="javax.persistence.schema-generation.database.action" value="none"/>
 11              <property name="hibernate.show_sql" value="false" />
 12          </properties>
 13      </persistence-unit>
 14  </persistence>

```
  * file:///opt/input/source/target/classes/META-INF/persistence.xml
      * Replace `http://xmlns.jcp.org/xml/ns/persistence` with `https://jakarta.ee/xml/ns/persistence` and change the schema version number
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <persistence version="2.1"
  3               xmlns="http://xmlns.jcp.org/xml/ns/persistence" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  4               xsi:schemaLocation="
  5          http://xmlns.jcp.org/xml/ns/persistence
  6          http://xmlns.jcp.org/xml/ns/persistence/persistence_2_1.xsd">
  7      <persistence-unit name="primary">
  8          <jta-data-source>java:jboss/datasources/CoolstoreDS</jta-data-source>
  9          <properties>
 10              <property name="javax.persistence.schema-generation.database.action" value="none"/>
 11              <property name="hibernate.show_sql" value="false" />
 12          </properties>
 13      </persistence-unit>
 14  </persistence>

```
  * file:///opt/input/source/target/classes/META-INF/persistence.xml
      * Replace `http://xmlns.jcp.org/xml/ns/persistence` with `https://jakarta.ee/xml/ns/persistence` and change the schema version number
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <persistence version="2.1"
  3               xmlns="http://xmlns.jcp.org/xml/ns/persistence" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  4               xsi:schemaLocation="
  5          http://xmlns.jcp.org/xml/ns/persistence
  6          http://xmlns.jcp.org/xml/ns/persistence/persistence_2_1.xsd">
  7      <persistence-unit name="primary">
  8          <jta-data-source>java:jboss/datasources/CoolstoreDS</jta-data-source>
  9          <properties>
 10              <property name="javax.persistence.schema-generation.database.action" value="none"/>
 11              <property name="hibernate.show_sql" value="false" />
 12          </properties>
 13      </persistence-unit>
 14  </persistence>

```
  * file:///opt/input/source/src/main/resources/META-INF/persistence.xml
      * Replace `http://xmlns.jcp.org/xml/ns/persistence` with `https://jakarta.ee/xml/ns/persistence` and change the schema version number
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <persistence version="2.1"
  3               xmlns="http://xmlns.jcp.org/xml/ns/persistence" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  4               xsi:schemaLocation="
  5          http://xmlns.jcp.org/xml/ns/persistence
  6          http://xmlns.jcp.org/xml/ns/persistence/persistence_2_1.xsd">
  7      <persistence-unit name="primary">
  8          <jta-data-source>java:jboss/datasources/CoolstoreDS</jta-data-source>
  9          <properties>
 10              <property name="javax.persistence.schema-generation.database.action" value="none"/>
 11              <property name="hibernate.show_sql" value="false" />
 12          </properties>
 13      </persistence-unit>
 14  </persistence>

```
  * file:///opt/input/source/src/main/resources/META-INF/persistence.xml
      * Replace `http://xmlns.jcp.org/xml/ns/persistence` with `https://jakarta.ee/xml/ns/persistence` and change the schema version number
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <persistence version="2.1"
  3               xmlns="http://xmlns.jcp.org/xml/ns/persistence" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  4               xsi:schemaLocation="
  5          http://xmlns.jcp.org/xml/ns/persistence
  6          http://xmlns.jcp.org/xml/ns/persistence/persistence_2_1.xsd">
  7      <persistence-unit name="primary">
  8          <jta-data-source>java:jboss/datasources/CoolstoreDS</jta-data-source>
  9          <properties>
 10              <property name="javax.persistence.schema-generation.database.action" value="none"/>
 11              <property name="hibernate.show_sql" value="false" />
 12          </properties>
 13      </persistence-unit>
 14  </persistence>

```
  * file:///opt/input/source/src/main/resources/META-INF/persistence.xml
      * Replace `http://xmlns.jcp.org/xml/ns/persistence` with `https://jakarta.ee/xml/ns/persistence` and change the schema version number
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <persistence version="2.1"
  3               xmlns="http://xmlns.jcp.org/xml/ns/persistence" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  4               xsi:schemaLocation="
  5          http://xmlns.jcp.org/xml/ns/persistence
  6          http://xmlns.jcp.org/xml/ns/persistence/persistence_2_1.xsd">
  7      <persistence-unit name="primary">
  8          <jta-data-source>java:jboss/datasources/CoolstoreDS</jta-data-source>
  9          <properties>
 10              <property name="javax.persistence.schema-generation.database.action" value="none"/>
 11              <property name="hibernate.show_sql" value="false" />
 12          </properties>
 13      </persistence-unit>
 14  </persistence>

```
### #2 - javaee-to-jakarta-namespaces-00006
* Category: mandatory
* Effort: 1
* Description: Replace the Java EE XSD with the Jakarta equivalent
Replace `beans_1_1.xsd` with `beans_3_0.xsd` and update the version attribute to `"3.0"`
* Labels: konveyor.io/target=jakarta-ee9+, konveyor.io/target=jakarta-ee, konveyor.io/target=eap8, konveyor.io/target=eap, konveyor.io/source
* Links
  * Jakarta XML Schemas: https://jakarta.ee/xml/ns/jakartaee/#9
* Incidents
  * file:///opt/input/source/src/main/webapp/WEB-INF/beans.xml
      * Replace `beans_1_1.xsd` with `beans_3_0.xsd` and update the version attribute to `"3.0"`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <!--
  3      JBoss, Home of Professional Open Source
  4      Copyright 2015, Red Hat, Inc. and/or its affiliates, and individual
  5      contributors by the @authors tag. See the copyright.txt in the
  6      distribution for a full listing of individual contributors.
  7      Licensed under the Apache License, Version 2.0 (the "License");
  8      you may not use this file except in compliance with the License.
  9      You may obtain a copy of the License at
 10      http://www.apache.org/licenses/LICENSE-2.0
 11      Unless required by applicable law or agreed to in writing, software
 12      distributed under the License is distributed on an "AS IS" BASIS,
 13      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 14      See the License for the specific language governing permissions and
 15      limitations under the License.
 16  -->
 17  <!-- Marker file indicating CDI should be enabled -->
 18  <beans xmlns="http://xmlns.jcp.org/xml/ns/javaee" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 19  	   xsi:schemaLocation="
 20        http://xmlns.jcp.org/xml/ns/javaee
 21        http://xmlns.jcp.org/xml/ns/javaee/beans_1_1.xsd"
 22  	   bean-discovery-mode="all">
 23  </beans>

```
### #3 - javaee-to-jakarta-namespaces-00030
* Category: mandatory
* Effort: 1
* Description: Replace the Java EE XSD with the Jakarta equivalent
Replace `persistence_2_1.xsd` with `persistence_3_0.xsd` and update the version attribute to `"3.0"`
* Labels: konveyor.io/target=jakarta-ee9+, konveyor.io/target=jakarta-ee, konveyor.io/target=eap8, konveyor.io/target=eap, konveyor.io/source
* Links
  * Jakarta XML Schemas: https://jakarta.ee/xml/ns/jakartaee/#9
* Incidents
  * file:///opt/input/source/target/classes/META-INF/persistence.xml
      * Replace `persistence_2_1.xsd` with `persistence_3_0.xsd` and update the version attribute to `"3.0"`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <persistence version="2.1"
  3               xmlns="http://xmlns.jcp.org/xml/ns/persistence" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  4               xsi:schemaLocation="
  5          http://xmlns.jcp.org/xml/ns/persistence
  6          http://xmlns.jcp.org/xml/ns/persistence/persistence_2_1.xsd">
  7      <persistence-unit name="primary">
  8          <jta-data-source>java:jboss/datasources/CoolstoreDS</jta-data-source>
  9          <properties>
 10              <property name="javax.persistence.schema-generation.database.action" value="none"/>
 11              <property name="hibernate.show_sql" value="false" />
 12          </properties>
 13      </persistence-unit>
 14  </persistence>

```
  * file:///opt/input/source/src/main/resources/META-INF/persistence.xml
      * Replace `persistence_2_1.xsd` with `persistence_3_0.xsd` and update the version attribute to `"3.0"`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <persistence version="2.1"
  3               xmlns="http://xmlns.jcp.org/xml/ns/persistence" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  4               xsi:schemaLocation="
  5          http://xmlns.jcp.org/xml/ns/persistence
  6          http://xmlns.jcp.org/xml/ns/persistence/persistence_2_1.xsd">
  7      <persistence-unit name="primary">
  8          <jta-data-source>java:jboss/datasources/CoolstoreDS</jta-data-source>
  9          <properties>
 10              <property name="javax.persistence.schema-generation.database.action" value="none"/>
 11              <property name="hibernate.show_sql" value="false" />
 12          </properties>
 13      </persistence-unit>
 14  </persistence>

```
### #4 - javaee-to-jakarta-namespaces-00033
* Category: mandatory
* Effort: 1
* Description: Replace the Java EE version with the Jakarta equivalent
In the root tag, replace the `version` attribute value `2.1` with `3.0`
* Labels: konveyor.io/target=jakarta-ee9+, konveyor.io/target=jakarta-ee, konveyor.io/target=eap8, konveyor.io/target=eap, konveyor.io/source
* Incidents
  * file:///opt/input/source/src/main/resources/META-INF/persistence.xml
      * In the root tag, replace the `version` attribute value `2.1` with `3.0`
  * file:///opt/input/source/target/classes/META-INF/persistence.xml
      * In the root tag, replace the `version` attribute value `2.1` with `3.0`
  * file:///opt/input/source/target/classes/META-INF/persistence.xml
      * In the root tag, replace the `version` attribute value `2.1` with `3.0`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <persistence version="2.1"
  3               xmlns="http://xmlns.jcp.org/xml/ns/persistence" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  4               xsi:schemaLocation="
  5          http://xmlns.jcp.org/xml/ns/persistence
  6          http://xmlns.jcp.org/xml/ns/persistence/persistence_2_1.xsd">
  7      <persistence-unit name="primary">
  8          <jta-data-source>java:jboss/datasources/CoolstoreDS</jta-data-source>
  9          <properties>
 10              <property name="javax.persistence.schema-generation.database.action" value="none"/>
 11              <property name="hibernate.show_sql" value="false" />
 12          </properties>
 13      </persistence-unit>
 14  </persistence>

```
  * file:///opt/input/source/src/main/resources/META-INF/persistence.xml
      * In the root tag, replace the `version` attribute value `2.1` with `3.0`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <persistence version="2.1"
  3               xmlns="http://xmlns.jcp.org/xml/ns/persistence" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  4               xsi:schemaLocation="
  5          http://xmlns.jcp.org/xml/ns/persistence
  6          http://xmlns.jcp.org/xml/ns/persistence/persistence_2_1.xsd">
  7      <persistence-unit name="primary">
  8          <jta-data-source>java:jboss/datasources/CoolstoreDS</jta-data-source>
  9          <properties>
 10              <property name="javax.persistence.schema-generation.database.action" value="none"/>
 11              <property name="hibernate.show_sql" value="false" />
 12          </properties>
 13      </persistence-unit>
 14  </persistence>

```
### #5 - javaee-to-jakarta-namespaces-00035
* Category: mandatory
* Effort: 1
* Description: Replace the Java EE version with the Jakarta equivalent
`beans_1_1.xsd`: In the root tag, replace the `version` attribute value with `3.0`
* Labels: konveyor.io/target=jakarta-ee9+, konveyor.io/target=jakarta-ee, konveyor.io/target=eap8, konveyor.io/target=eap, konveyor.io/source
* Incidents
  * file:///opt/input/source/src/main/webapp/bower_components/patternfly/dist/img/RH_Atomic-Logo-NoText.svg
      * `beans_1_1.xsd`: In the root tag, replace the `version` attribute value with `3.0`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="utf-8"?>
  2  <!-- Generator: Adobe Illustrator 19.2.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
  3  <svg version="1.1"
  4  	 id="svg4242" xmlns:cc="http://creativecommons.org/ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
  5  	 xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 200 199.7"
  6  	 style="enable-background:new 0 0 200 199.7;" xml:space="preserve">
  7  <style type="text/css">
  8  	.st0{fill:#00B9E4;}
  9  	.st1{fill:#0088CE;}
 10  </style>
 11  <g>
 12  	<g>
 13  		<path class="st0" d="M88.1,136.7c-0.4,0.3-0.7,0.6-1,0.8c-2.5,2.5-4.9,4.8-7.1,6.9c1.4,0.8,2.4,2.1,3,3.7c2.7-2.4,5.5-5,8.4-7.9
 14  			c0.6-0.6,1.1-2.2-0.1-3.3C90.4,136.2,89,136,88.1,136.7z"/>
 15  		<path class="st0" d="M60.3,77.4c0.7,1.1,2.2,1.5,3.3,0.7c1.2-0.8,1-2.4,0.6-2.9C54.5,58.7,50.1,46,54,43c2.4-1.9,7.6,0.2,14.5,5.3
 16  			c0.7-2.2,2.3-4,4.3-5c-11.1-8.3-19.9-11.8-24-8.6c-5.8,4.5-1,21.1,11.1,42.1C60,77,60.2,77.2,60.3,77.4z"/>
 17  		<path class="st0" d="M140.3,123.2c2.9-0.4,5.7-0.8,8.3-1.3l0,0l0,0l0,0c0.7-0.7,1.2-1.7,1.2-2.8c0-1.8-1.3-3.3-2.9-3.7l0,0
 18  			c-3.2,0.5-6.7,1-10.4,1.4l0,0l0,0c-5.7-9.3-12.7-19.4-20.6-29.5c-2.3-3.2-7.4-9.1-11.3-13.6l0.1-0.1C124,52.2,141,39.1,146,42.9
 19  			c3.8,3-0.5,15.6-10.3,32.2c-0.3,0.5-0.6,2.1,0.6,2.9c1.2,0.8,2.7,0.4,3.3-0.7c0.1-0.2,0.3-0.4,0.4-0.6c12-21,16.9-37.6,11.1-42.1
 20  			c-7-5.5-27.8,8.6-50.3,32.9c0,0-0.3,0.4-1,1.1c-0.6-0.6-1-1.1-1-1.1c-4.9-5.2-9.7-10.1-14.2-14.2l0,0c-0.1-0.1-0.1-0.1-0.1-0.1
 21  			c-0.2-0.1-0.4-0.1-0.6-0.1c-2.1,0-3.8,1.7-3.8,3.8c0,0.5,0.1,1.1,0.3,1.5l0,0c4.7,4.4,9.6,9.5,14.8,15.2l0.1,0.1
 22  			c-4,4.5-9,10.4-11.3,13.6c-7.9,10.1-14.9,20.1-20.6,29.5c-21.9-2.5-36.6-7.1-36.5-12.4c0-5.4,15.6-10.1,38.4-12.4
 23  			c0.3-0.1,0.4-0.1,0.7-0.1c1.2-0.2,1.9-1.4,1.8-2.3c0-1.2-0.9-2.4-2.6-2.4c-28.3,3.2-48,10.2-48,18.3c-0.1,7.6,17.2,14.2,42.6,17.7
 24  			c-11.9,20.9-16.7,37.3-10.9,41.8c4.2,3.3,13.3-0.4,24.7-9.1l0,0c0,0,0,0,0.1,0c0.1-0.3,0.1-0.5,0.1-0.8c0-1.5-1.3-2.8-2.8-2.8
 25  			c-0.2,0-0.3,0-0.4,0.1l0,0l0,0c-7.1,5.2-12.4,7.5-14.8,5.6c-4-3.1,0.8-16.4,11.4-33.8c9.8,1.1,20.7,1.6,32.1,1.7l0,0
 26  			c0.2,0,0.3,0,0.5,0l0,0l0,0c0.1,0,0.3,0,0.4,0l0,0h0.1l0,0h0.1c0.1,0,0.3,0,0.4,0c0.2,0,0.3,0,0.5,0l0,0
 27  			c11.4-0.1,22.3-0.6,32.1-1.7c10.5,17.5,15.4,30.8,11.4,33.8c-4.1,3.2-16.5-5.2-31.5-20.4c-0.3-0.3-0.6-0.6-1-0.8
 28  			c-1-0.7-2.3-0.5-3,0.2c-1.2,1.2-0.8,2.7-0.1,3.3c19.4,19.2,36.3,29.6,42.5,24.8C157,160.5,152.2,144.1,140.3,123.2L140.3,123.2z
 29  			 M100.3,118.8c-0.1,0-0.2,0-0.3,0s-0.2,0-0.3,0c-10.2,0-20-0.4-28.7-1.2c5.2-8.2,11.5-16.9,18.6-25.9c3.2-4,6.4-7.9,9.5-11.5l0,0
 30  			c0.3-0.4,0.6-0.7,0.9-1.1c0.3,0.4,0.6,0.7,0.9,1.1l0,0c3.1,3.7,6.3,7.5,9.5,11.5c7.1,9,13.3,17.8,18.6,25.9l0,0
 31  			C120.2,118.4,110.5,118.8,100.3,118.8z"/>
 32  		<path class="st0" d="M134.9,87.2c-1.7-0.1-2.6,1.2-2.6,2.4c-0.1,1,0.6,2.1,1.8,2.3c0.2,0.1,0.4,0.1,0.7,0.1
 33  			c22.8,2.4,38.3,7,38.4,12.4c0,1.9-1.9,3.7-5.4,5.4c1.1,1.7,1.8,3.9,1.8,6.1c0,0.2,0,0.4-0.1,0.5c8.5-3.2,13.3-7,13.3-11
 34  			C182.9,97.3,163.2,90.4,134.9,87.2z"/>
 35  	</g>
 36  	<g>
 37  		<path class="st1" d="M76.6,42.4c-4.7,0-8.6,3.8-8.6,8.6c0,4.7,3.8,8.6,8.6,8.6c1.4,0,2.8-0.4,3.9-1c-0.2-0.5-0.3-1-0.3-1.5
 38  			c0-2.1,1.7-3.8,3.8-3.8c0.2,0,0.4,0,0.6,0.1c0.1,0.1,0.1,0.1,0.1,0.1c0.2-0.8,0.4-1.6,0.4-2.4C85.2,46.2,81.4,42.4,76.6,42.4z"/>
 39  		<path class="st1" d="M99.1,67.6c-0.4-0.4-0.7-0.8-1.2-1.2l-4.4,5.3c0.6,0.7,1.3,1.4,1.9,2.1l0.1,0.1c1.9-2.2,3.6-4.1,4.6-5.2
 40  			C99.4,68,99.1,67.6,99.1,67.6z"/>
 41  		<path class="st1" d="M100,79.1L100,79.1c0.3,0.4,0.6,0.7,0.9,1.1l0,0c1,1.2,2,2.3,3,3.5l4.6-5.4c-1.3-1.5-2.6-3-3.8-4.4L100,79.1z
 42  			"/>
 43  		<path class="st1" d="M158.3,104.7c-6,0-11,4.8-11.3,10.7c1.7,0.4,2.9,1.9,2.9,3.7c0,1.1-0.5,2.1-1.2,2.8l0,0
 44  			c2,3.2,5.6,5.4,9.6,5.4c6.2,0,11.3-5.1,11.3-11.3C169.6,109.7,164.5,104.7,158.3,104.7z"/>
 45  		<path class="st1" d="M59.7,123.2c-1.2,2.1-2.3,4.1-3.3,6.1l7,0.9c1.1-2,2.3-4,3.5-6.1L59.7,123.2L59.7,123.2z"/>
 46  		<path class="st1" d="M71,117.6c0.4-0.7,0.9-1.4,1.4-2.1l-7.5-0.9c-0.5,0.7-1,1.5-1.4,2.2l0,0L71,117.6L71,117.6z"/>
 47  		<path class="st1" d="M136.6,116.9c-0.5-0.8-1-1.6-1.5-2.3l-7.5,1c0.5,0.7,1,1.5,1.4,2.2l0,0l0,0L136.6,116.9L136.6,116.9z"/>
 48  		<path class="st1" d="M133.1,124.1L133.1,124.1c1.2,2.1,2.4,4.1,3.5,6l7-0.9c-1-2-2.1-4-3.3-6L133.1,124.1z"/>
 49  		<path class="st1" d="M76.6,143.5c-3.7,0-6.6,3-6.6,6.6c0,0.8,0.2,1.5,0.4,2.2l0,0c0.1,0,0.3-0.1,0.4-0.1c1.5,0,2.8,1.3,2.8,2.8
 50  			c0,0.3-0.1,0.5-0.1,0.8c0,0,0,0-0.1,0c1,0.5,2,0.8,3.2,0.8c3.7,0,6.6-3,6.6-6.6C83.2,146.5,80.3,143.5,76.6,143.5z"/>
 51  	</g>
 52  </g>
 53  </svg>

```
  * file:///opt/input/source/src/main/webapp/bower_components/patternfly/dist/img/OpenShift-Logo-Text.svg
      * `beans_1_1.xsd`: In the root tag, replace the `version` attribute value with `3.0`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="utf-8"?>
  2  <!-- Generator: Adobe Illustrator 19.2.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
  3  <svg version="1.1"
  4  	 id="svg4242" xmlns:cc="http://creativecommons.org/ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
  5  	 xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 200 199.7"
  6  	 style="enable-background:new 0 0 200 199.7;" xml:space="preserve">
  7  <style type="text/css">
  8  	.st0{fill:#C32034;}
  9  	.st1{fill:#DB212F;}
 10  	.st2{fill:#EA2227;}
 11  	.st3{fill:#AD213A;}
 12  	.st4{fill:#BA2034;}
 13  	.st5{fill:#231F20;}
 14  </style>
 15  <g>
 16  	<g id="g3921">
 17  		<g id="g3927" transform="translate(304.96 416.03)">
 18  			<path id="path3929" class="st0" d="M-238.7-345.3l-23.3,8.5c0.3,3.8,0.9,7.5,1.9,11.1l22.1-8C-238.7-337.7-239-341.5-238.7-345.3
 19  				"/>
 20  		</g>
 21  		<g id="g3931" transform="translate(418.75 444.5)">
 22  			<path id="path3933" class="st0" d="M-249.5-399.6c-1.6-3.3-3.5-6.6-5.6-9.6l-23.3,8.5c2.7,2.8,5,5.9,6.9,9.2
 23  				C-271.7-391.6-249.5-399.6-249.5-399.6z"/>
 24  		</g>
 25  		<g id="g3935" transform="translate(362.11 451.79)">
 26  			<path id="path3937" class="st1" d="M-244.2-413.5c4.8,2.2,9,5.4,12.6,9l23.3-8.5c-6.4-9-15.3-16.6-26-21.6
 27  				c-33.3-15.5-73-1.1-88.5,32.2c-5,10.8-6.9,22.2-6,33.3l23.3-8.5c0.4-5.1,1.6-10.1,3.9-15C-291.6-414.2-265.8-423.5-244.2-413.5"
 28  				/>
 29  		</g>
 30  		<g id="g3939" transform="translate(282.86 395.05)">
 31  			<path id="path3941" class="st2" d="M-236.6-305.4l-22.1,8c2,8,5.6,15.7,10.4,22.6l23.2-8.5C-231-289.4-235-297.1-236.6-305.4"/>
 32  		</g>
 33  		<g id="g3943" transform="translate(389.56 404.75)">
 34  			<path id="path3945" class="st1" d="M-246.7-323.9c-0.4,5.1-1.7,10.1-3.9,15c-10.1,21.6-35.9,31.1-57.5,20.9
 35  				c-4.8-2.2-9-5.4-12.6-9l-23.2,8.5c6.4,9,15.2,16.6,26,21.6c33.3,15.5,73,1.1,88.5-32.2c5-10.8,6.9-22.2,6-33.3L-246.7-323.9
 36  				L-246.7-323.9z"/>
 37  		</g>
 38  		<g id="g3947" transform="translate(395.89 436.18)">
 39  			<path id="path3949" class="st2" d="M-247.3-383.8l-22.1,8c4.1,7.4,6.1,15.9,5.4,24.4l23.2-8.5
 40  				C-241.5-368.1-243.7-376.2-247.3-383.8"/>
 41  		</g>
 42  		<g id="g3951" transform="translate(279.22 406.66)">
 43  			<path id="path3953" class="st3" d="M-236.2-327.6l23.2-8.4l-0.1,4.6l-22.4,8.3C-235.5-323-236.2-327.6-236.2-327.6z"/>
 44  		</g>
 45  		<g id="g3955" transform="translate(386.73 445.86)">
 46  			<path id="path3957" class="st3" d="M-246.5-402.2l23.6-8l2.5,3.6l-22.9,8C-243.4-398.5-246.5-402.2-246.5-402.2z"/>
 47  		</g>
 48  		<g id="g3959" transform="translate(282.04 365.71)">
 49  			<path id="path3961" class="st4" d="M-236.5-249.5l23.2-8.3l7,6.5l-24.4,9C-230.6-242.3-236.5-249.5-236.5-249.5z"/>
 50  		</g>
 51  		<g id="g3963" transform="translate(415.68 414.03)">
 52  			<path id="path3965" class="st4" d="M-249.2-341.5l-23.6,8.4l-1.7,9.3l25.2-8.8C-249.4-332.7-249.2-341.5-249.2-341.5z"/>
 53  		</g>
 54  	</g>
 55  	<g>
 56  		<g id="text3967" transform="scale(1,-1)">
 57  			<path id="path3359" class="st5" d="M20.5-188.8c-1.2,0-2.2,0.1-3.2,0.4c-0.9,0.3-1.7,0.7-2.5,1.2c-0.7,0.5-1.3,1.2-1.8,1.9
 58  				c-0.5,0.7-0.9,1.5-1.2,2.3c-0.3,0.9-0.6,1.7-0.7,2.6c-0.1,0.9-0.2,1.8-0.2,2.7s0.1,1.8,0.2,2.7c0.1,0.9,0.4,1.8,0.7,2.6
 59  				c0.3,0.9,0.7,1.6,1.2,2.3c0.5,0.7,1.1,1.4,1.8,1.9c0.7,0.5,1.5,0.9,2.5,1.2s2,0.4,3.2,0.4c1.2,0,2.2-0.1,3.1-0.4
 60  				c0.9-0.3,1.7-0.7,2.5-1.2c0.7-0.5,1.3-1.2,1.8-1.9c0.5-0.7,0.9-1.5,1.2-2.3c0.3-0.8,0.6-1.7,0.7-2.6c0.1-0.9,0.2-1.8,0.2-2.7
 61  				s-0.1-1.8-0.2-2.7c-0.1-0.9-0.4-1.7-0.7-2.6c-0.3-0.8-0.7-1.6-1.2-2.3c-0.5-0.7-1.1-1.4-1.8-1.9c-0.7-0.5-1.5-0.9-2.5-1.2
 62  				C22.7-188.6,21.7-188.8,20.5-188.8 M20.5-184.7c0.9,0,1.8,0.2,2.5,0.7c0.7,0.4,1.2,1,1.6,1.7c0.4,0.7,0.7,1.4,0.9,2.3
 63  				c0.2,0.9,0.3,1.7,0.3,2.5c0,0.6-0.1,1.1-0.1,1.7c-0.1,0.6-0.2,1.2-0.4,1.7c-0.1,0.5-0.4,1-0.7,1.5c-0.3,0.5-0.6,0.9-1,1.2
 64  				c-0.4,0.4-0.9,0.7-1.4,0.9c-0.5,0.2-1.1,0.3-1.7,0.3c-0.7,0-1.2-0.1-1.7-0.3s-0.9-0.5-1.4-0.9c-0.4-0.4-0.7-0.8-1-1.2
 65  				c-0.3-0.5-0.5-1-0.7-1.5c-0.1-0.5-0.3-1.1-0.4-1.7s-0.1-1.1-0.1-1.6c0-0.8,0.1-1.7,0.3-2.5c0.2-0.9,0.5-1.6,0.9-2.3
 66  				c0.4-0.7,0.9-1.2,1.6-1.7C18.7-184.5,19.5-184.7,20.5-184.7"/>
 67  			<path id="path3361" class="st5" d="M35.4-188.4v21.7h9.3c1.4,0,2.5-0.2,3.5-0.6c0.9-0.4,1.7-0.9,2.3-1.6c0.6-0.7,1-1.4,1.2-2.2
 68  				c0.3-0.8,0.4-1.7,0.4-2.5c0-0.5-0.1-1.1-0.2-1.6c-0.1-0.5-0.3-1.1-0.6-1.6c-0.2-0.5-0.6-1-0.9-1.4s-0.9-0.9-1.4-1.2
 69  				c-0.6-0.4-1.2-0.6-1.9-0.8s-1.5-0.3-2.4-0.3h-5.1v-8H35.4 M44.9-176.4c0.5,0,1,0.1,1.4,0.3c0.4,0.1,0.7,0.4,0.9,0.7
 70  				c0.2,0.3,0.4,0.6,0.5,0.9c0.1,0.4,0.1,0.7,0.1,1c0,0.3-0.1,0.7-0.1,0.9c-0.1,0.4-0.2,0.7-0.4,0.9c-0.2,0.3-0.5,0.5-0.9,0.7
 71  				c-0.4,0.2-0.9,0.3-1.4,0.3h-5.3v-5.8H44.9"/>
 72  			<path id="path3363" class="st5" d="M57.9-188.4v21.7h14.8v-4H62.1v-4.6h6.2v-4h-6.2v-5.2h11.3v-4H57.9"/>
 73  			<path id="path3365" class="st5" d="M93.1-188.4l-8.6,12.7c-0.1,0.2-0.3,0.4-0.4,0.8c-0.1,0.3-0.3,0.6-0.4,0.9
 74  				c0-0.2,0.1-0.5,0.1-0.8c0-0.3,0-0.6,0-0.8v-12.7h-4.2v21.7h3.9l8.4-12.5c0.1-0.2,0.3-0.4,0.4-0.7c0.1-0.3,0.3-0.6,0.4-0.9
 75  				c0,0.3-0.1,0.6-0.1,0.9s0,0.6,0,0.7v12.5h4.1v-21.7L93.1-188.4"/>
 76  		</g>
 77  		<g id="text3971" transform="scale(1,-1)">
 78  			<path id="path3348" class="st5" d="M114.3-171.6c-0.1,0.3-0.3,0.6-0.6,0.9c-0.2,0.3-0.5,0.5-0.9,0.7c-0.4,0.2-0.7,0.4-1.2,0.4
 79  				c-0.4,0.1-0.9,0.1-1.4,0.1c-1,0-1.9-0.2-2.5-0.7c-0.6-0.4-0.9-1.1-0.9-2c0-0.5,0.1-0.9,0.5-1.3c0.3-0.4,0.7-0.7,1.3-0.9
 80  				c0.5-0.3,1.1-0.5,1.8-0.7c0.7-0.2,1.4-0.4,2-0.7c0.7-0.3,1.4-0.6,2-0.9c0.7-0.4,1.3-0.8,1.8-1.3c0.5-0.5,0.9-1.1,1.3-1.8
 81  				c0.3-0.7,0.5-1.5,0.5-2.5c0-1-0.2-2-0.6-2.8c-0.4-0.8-0.9-1.4-1.6-2c-0.7-0.6-1.4-0.9-2.4-1.2c-0.9-0.3-1.9-0.4-2.9-0.4
 82  				c-0.9,0-1.9,0.1-2.8,0.4s-1.6,0.6-2.3,1c-0.7,0.4-1.2,1-1.7,1.7s-0.9,1.4-1.2,2.2l3,1.1c0.2-0.5,0.5-0.9,0.8-1.3
 83  				c0.4-0.4,0.7-0.7,1.2-1c0.4-0.3,0.9-0.5,1.4-0.7c0.5-0.1,1.1-0.2,1.7-0.2c0.6,0,1.1,0.1,1.6,0.2c0.5,0.1,0.9,0.4,1.2,0.7
 84  				c0.4,0.3,0.6,0.7,0.8,1c0.2,0.4,0.3,0.9,0.3,1.4c0,0.7-0.1,1.2-0.5,1.6c-0.3,0.4-0.7,0.8-1.3,1.2c-0.5,0.3-1.2,0.6-1.8,0.9
 85  				c-0.7,0.2-1.4,0.5-2,0.7c-0.7,0.2-1.4,0.5-2,0.9c-0.7,0.3-1.2,0.7-1.8,1.2c-0.5,0.4-0.9,1-1.3,1.7c-0.3,0.7-0.5,1.4-0.5,2.3
 86  				c0,0.8,0.1,1.5,0.4,2.2c0.3,0.7,0.8,1.3,1.4,1.8c0.6,0.5,1.3,0.9,2.2,1.2c0.9,0.3,1.8,0.4,3,0.4c0.9,0,1.7-0.1,2.5-0.4
 87  				c0.7-0.2,1.4-0.5,2-0.9c0.6-0.4,1-0.9,1.4-1.4s0.7-1.1,0.9-1.7L114.3-171.6"/>
 88  			<path id="path3350" class="st5" d="M137.1-188.4v9.7h-9.9v-9.7h-3.3v21.7h3.3v-9h9.9v9h3.3v-21.7H137.1"/>
 89  			<path id="path3352" class="st5" d="M146.9-188.4v21.7h3.3v-21.7H146.9"/>
 90  			<path id="path3354" class="st5" d="M156.6-188.4v21.7h13.5v-3h-10.3v-5.9h6.6v-3h-6.6v-9.7H156.6"/>
 91  			<path id="path3356" class="st5" d="M183-169.8v-18.6h-3.3v18.6h-6.2v3.1h15.5v-3.1L183-169.8"/>
 92  		</g>
 93  	</g>
 94  </g>
 95  </svg>

```
  * file:///opt/input/source/src/main/webapp/bower_components/patternfly/dist/img/OpenShift-logo.svg
      * `beans_1_1.xsd`: In the root tag, replace the `version` attribute value with `3.0`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8" standalone="no"?>
  2  <!-- Created with Inkscape (http://www.inkscape.org/) -->
  3  <svg id="svg4242" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns="http://www.w3.org/2000/svg" height="285.79" viewBox="0 0 286.28177 285.78885" width="286.28" version="1.1" xmlns:cc="http://creativecommons.org/ns#" xmlns:dc="http://purl.org/dc/elements/1.1/">
  4   <defs id="defs4244">
  5    <clipPath id="clipPath3923" clipPathUnits="userSpaceOnUse">
  6     <path id="path3925" d="m0 768h1024v-768h-1024v768z"/>
  7    </clipPath>
  8   </defs>
  9   <metadata id="metadata4247">
 10    <rdf:RDF>
 11     <cc:Work rdf:about="">
 12      <dc:format>image/svg+xml</dc:format>
 13      <dc:type rdf:resource="http://purl.org/dc/dcmitype/StillImage"/>
 14      <dc:title/>
 15     </cc:Work>
 16    </rdf:RDF>
 17   </metadata>
 18   <g id="layer1" transform="translate(448.86 -589.47)">
 19    <g id="g3367" transform="matrix(1.25 0 0 -1.25 -733.56 1212.1)">
 20     <g id="g3919">
 21      <g id="g3921" clip-path="url(#clipPath3923)">
 22       <g id="g3927" transform="translate(304.96 416.03)">
 23        <path id="path3929" d="m0 0-25.748-9.369c0.33-4.128 1.041-8.206 2.042-12.201l24.456 8.906c-0.793 4.135-1.076 8.396-0.75 12.664" fill="#c32034"/>
 24       </g>
 25       <g id="g3931" transform="translate(418.75 444.5)">
 26        <path id="path3933" d="m0 0c-1.795 3.704-3.873 7.284-6.279 10.657l-25.741-9.369c2.995-3.064 5.508-6.508 7.563-10.191l24.457 8.903z" fill="#c32034"/>
 27       </g>
 28       <g id="g3935" transform="translate(362.11 451.79)">
 29        <path id="path3937" d="m0 0c5.356-2.499 9.995-5.908 13.907-9.906l25.742 9.37c-7.13 10.005-16.842 18.366-28.743 23.919-36.797 17.159-80.702 1.18-97.861-35.613-5.553-11.907-7.617-24.556-6.648-36.801l25.745 9.368c0.427 5.578 1.789 11.167 4.284 16.526 11.151 23.909 39.669 34.283 63.575 23.137" fill="#db212f"/>
 30       </g>
 31       <g id="g3939" transform="translate(282.86 395.05)">
 32        <path id="path3941" d="m0 0-24.46-8.909c2.248-8.918 6.145-17.391 11.502-24.932l25.688 9.351c-6.595 6.771-10.979 15.337-12.73 24.49" fill="#ea2227"/>
 33       </g>
 34       <g id="g3943" transform="translate(389.56 404.75)">
 35        <path id="path3945" d="m0 0c-0.409-5.575-1.817-11.167-4.319-16.53-11.15-23.91-39.668-34.285-63.574-23.136-5.363 2.501-10.035 5.883-13.936 9.888l-25.687-9.352c7.113-10.006 16.816-18.369 28.721-23.926 36.799-17.156 80.698-1.177 97.857 35.619 5.557 11.905 7.608 24.549 6.626 36.785l-25.69-9.348z" fill="#db212f"/>
 36       </g>
 37       <g id="g3947" transform="translate(395.89 436.18)">
 38        <path id="path3949" d="m0 0-24.458-8.903c4.542-8.139 6.689-17.513 5.986-26.938l25.688 9.345c-0.735 9.219-3.195 18.217-7.216 26.496" fill="#ea2227"/>
 39       </g>
 40       <g id="g3951" transform="translate(279.22 406.66)">
 41        <path id="path3953" d="m0 0 25.684 9.263-0.105-5.08-24.78-9.213-0.799 5.03z" fill="#ad213a"/>
 42       </g>
 43       <g id="g3955" transform="translate(386.73 445.86)">
 44        <path id="path3957" d="m0 0 26.085 8.814 2.712-4.028-25.345-8.821-3.452 4.035z" fill="#ad213a"/>
 45       </g>
 46       <g id="g3959" transform="translate(282.04 365.71)">
 47        <path id="path3961" d="m0 0 25.716 9.213 7.777-7.225-26.967-9.967-6.526 7.979z" fill="#ba2034"/>
 48       </g>
 49       <g id="g3963" transform="translate(415.68 414.03)">
 50        <path id="path3965" d="m0 0-26.119-9.274-1.924-10.293 27.848 9.771 0.195 9.796z" fill="#ba2034"/>
 51       </g>
 52      </g>
 53     </g>
 54     <g id="text3967" transform="scale(1,-1)" fill="#231f20">
 55      <path id="path3359" d="m254.37-285.44c-1.2952 0-2.4565-0.16749-3.4837-0.50246-1.0273-0.34614-1.9373-0.80952-2.73-1.3901-0.78161-0.59178-1.4516-1.2841-2.0098-2.0768-0.5583-0.80393-1.0161-1.6637-1.3734-2.5793-0.34614-0.92675-0.60296-1.887-0.77044-2.8808-0.15632-1.0049-0.23448-2.0042-0.23448-2.998 0-0.98257 0.0782-1.9707 0.23448-2.9645 0.16748-1.0049 0.4243-1.9652 0.77044-2.8808 0.3573-0.92674 0.81509-1.7865 1.3734-2.5793 0.55828-0.80391 1.2282-1.4962 2.0098-2.0768 0.79276-0.59176 1.7028-1.0551 2.73-1.3901 1.0272-0.34611 2.1885-0.51918 3.4837-0.51921 1.2952 0.00003 2.4509 0.1731 3.467 0.51921 1.0272 0.335 1.9317 0.79838 2.7133 1.3901 0.78158 0.58064 1.4515 1.2729 2.0098 2.0768 0.55826 0.79279 1.0105 1.6526 1.3566 2.5793 0.35728 0.91561 0.61409 1.8759 0.77043 2.8808 0.16747 0.99377 0.25121 1.9819 0.25123 2.9645-0.00002 0.99376-0.0838 1.9931-0.25123 2.998-0.15634 0.99376-0.41315 1.954-0.77043 2.8808-0.34617 0.9156-0.79838 1.7754-1.3566 2.5793-0.55831 0.79277-1.2283 1.485-2.0098 2.0768-0.78162 0.58062-1.686 1.044-2.7133 1.3901-1.0161 0.33497-2.1718 0.50246-3.467 0.50246m0-4.4719c1.0719 0.00001 1.9708-0.25122 2.6965-0.75369 0.73693-0.50245 1.3287-1.1445 1.7754-1.9261 0.45778-0.78159 0.78717-1.6358 0.98817-2.5625 0.20096-0.93791 0.30146-1.8423 0.30147-2.7133-0.00001-0.6141-0.0447-1.2338-0.13398-1.8591-0.0782-0.63643-0.21217-1.245-0.40197-1.8256-0.18984-0.59177-0.43548-1.1445-0.73694-1.6581-0.30149-0.52478-0.66438-0.97699-1.0887-1.3566-0.42432-0.39078-0.92119-0.69784-1.4906-0.92118-0.5583-0.22329-1.1948-0.33495-1.9094-0.33497-0.72578 0.00002-1.3734 0.11726-1.9428 0.35172-0.5583 0.2345-1.0552 0.55273-1.4906 0.95467-0.4243 0.39082-0.78719 0.84862-1.0887 1.3734-0.30148 0.52481-0.54713 1.0831-0.73694 1.6749-0.18982 0.5918-0.32939 1.1948-0.41871 1.8088-0.0782 0.61413-0.11725 1.2115-0.11724 1.7921-0.00001 0.9156 0.10048 1.8479 0.30147 2.797 0.20098 0.93794 0.52479 1.7921 0.97142 2.5625 0.45779 0.75928 1.0552 1.3846 1.7921 1.8758 0.73693 0.48013 1.6469 0.7202 2.73 0.72019"/>
 56      <path id="path3361" d="m270.86-285.86v-24.018h10.3c1.5185 0.00003 2.797 0.22334 3.8354 0.66995 1.0384 0.43548 1.8814 1.0161 2.529 1.7418 0.6476 0.71463 1.111 1.5242 1.3901 2.4286 0.29029 0.90444 0.43544 1.82 0.43546 2.7468-0.00002 0.58064-0.067 1.1724-0.20098 1.7754-0.13401 0.5918-0.34058 1.1724-0.6197 1.7419-0.27916 0.5583-0.63647 1.0831-1.0719 1.5744-0.43549 0.4913-0.96028 0.92676-1.5744 1.3064-0.60297 0.36848-1.3008 0.65879-2.0936 0.87093-0.78162 0.21216-1.6581 0.31823-2.6295 0.31822h-5.661v8.8433h-4.6394m10.501-13.248c0.59178 0.00002 1.0886-0.0949 1.4906-0.28472 0.40196-0.18981 0.72576-0.43545 0.97142-0.73694 0.2568-0.30146 0.44103-0.64202 0.55271-1.0217 0.11164-0.37962 0.16747-0.75926 0.16749-1.1389-0.00002-0.34612-0.0503-0.70342-0.15074-1.0719-0.0893-0.37962-0.25683-0.72576-0.50246-1.0384-0.2345-0.31262-0.5583-0.56943-0.97142-0.77043-0.41315-0.20097-0.93236-0.30146-1.5576-0.30148h-5.862v6.3645h5.862"/>
 57      <path id="path3363" d="m295.76-285.86v-24.018h16.397v4.4049h-11.758v5.0413h6.9172v4.3881h-6.9172v5.795h12.478v4.3881h-17.117"/>
 58      <path id="path3365" d="m334.66-285.86-9.53-14.002c-0.15633-0.23446-0.3294-0.51919-0.51921-0.85418-0.17866-0.34612-0.33498-0.66434-0.46896-0.95467 0.0335 0.25683 0.0558 0.5583 0.067 0.90443 0.0223 0.34615 0.0335 0.64763 0.0335 0.90442v14.002h-4.6059v-24.018h4.3546l9.2955 13.834c0.14514 0.22333 0.31263 0.50247 0.50246 0.83743 0.1898 0.33499 0.35729 0.65879 0.50246 0.97142-0.0335-0.32379-0.0614-0.6476-0.0837-0.97142-0.0112-0.33496-0.0168-0.6141-0.0168-0.83743v-13.834h4.5891v24.018h-4.1202"/>
 59     </g>
 60     <g id="text3971" transform="scale(1,-1)" fill="#231f20">
 61      <path id="path3348" d="m358.06-304.42c-0.14517-0.34612-0.34615-0.66435-0.60295-0.95468-0.25683-0.30145-0.56947-0.55826-0.93793-0.77043-0.36848-0.2233-0.79278-0.39637-1.2729-0.51921-0.46897-0.1228-0.99376-0.18421-1.5744-0.18424-1.1501 0.00003-2.0489 0.25125-2.6965 0.75369-0.64762 0.50248-0.97143 1.2115-0.97142 2.1271-0.00001 0.56947 0.17864 1.0552 0.53595 1.4571 0.3573 0.39082 0.82626 0.73696 1.4069 1.0384 0.58061 0.30149 1.2394 0.58063 1.9763 0.83743 0.74809 0.24566 1.5074 0.51922 2.2778 0.82068 0.78159 0.29032 1.5409 0.63088 2.2778 1.0217 0.7481 0.37964 1.4125 0.84861 1.9931 1.4069 0.5806 0.54713 1.0496 1.2115 1.4069 1.9931 0.35728 0.77045 0.53594 1.6972 0.53595 2.7803-0.00001 1.1501-0.21216 2.1718-0.63644 3.065-0.41315 0.8821-0.98819 1.6302-1.7251 2.2443-0.73696 0.60295-1.6079 1.0663-2.6128 1.3901-0.99377 0.31264-2.0657 0.46896-3.2157 0.46896-1.0719 0-2.0768-0.13957-3.0148-0.41872-0.92677-0.26798-1.7698-0.65319-2.529-1.1556-0.74811-0.51363-1.3957-1.1277-1.9428-1.8424-0.54712-0.72577-0.97142-1.5353-1.2729-2.4286l3.3665-1.2226c0.24564 0.53597 0.54712 1.0273 0.90443 1.4739 0.36846 0.44664 0.78718 0.83186 1.2562 1.1557 0.46895 0.31264 0.98257 0.55829 1.5409 0.73694 0.56944 0.17865 1.178 0.26798 1.8256 0.26798s1.2394-0.0782 1.7754-0.23448c0.53594-0.15632 0.99374-0.3908 1.3734-0.70345 0.37963-0.31263 0.67552-0.69785 0.88768-1.1556 0.21214-0.46896 0.31821-1.0049 0.31823-1.6079-0.00002-0.7146-0.17867-1.312-0.53596-1.7921-0.35732-0.49129-0.82628-0.91559-1.4069-1.2729-0.58063-0.35729-1.245-0.66994-1.9931-0.93792-0.73695-0.26797-1.4962-0.54153-2.2778-0.82069-0.77044-0.27913-1.5297-0.59177-2.2778-0.93792-0.73695-0.34613-1.3957-0.77042-1.9763-1.2729-0.58062-0.50244-1.0496-1.1054-1.4069-1.8088-0.3573-0.70343-0.53595-1.5632-0.53595-2.5793 0-0.84858 0.16748-1.6525 0.50246-2.4118 0.34613-0.75925 0.84301-1.4236 1.4906-1.9931 0.6476-0.58059 1.446-1.0384 2.395-1.3734 0.94908-0.33495 2.0322-0.50243 3.2492-0.50246 1.0161 0.00003 1.9372 0.12285 2.7635 0.36847 0.82625 0.23451 1.5464 0.5639 2.1606 0.98817 0.62527 0.42432 1.1445 0.92678 1.5576 1.5074 0.41311 0.58064 0.72575 1.2115 0.93792 1.8926l-3.2995 1.1054"/>
 62      <path id="path3350" d="m383.24-285.86v-10.702h-10.954v10.702h-3.5675v-24.018h3.5675v9.9487h10.954v-9.9487h3.5674v24.018h-3.5674"/>
 63      <path id="path3352" d="m394.08-285.86v-24.018h3.5675v24.018h-3.5675"/>
 64      <path id="path3354" d="m404.81-285.86v-24.018h14.89v3.3665h-11.322v6.5822h7.3192v3.3665h-7.3192v10.702h-3.5675"/>
 65      <path id="path3356" d="m434.01-306.44v20.584h-3.5675v-20.584h-6.8v-3.4335h17.151v3.4335h-6.7832"/>
 66     </g>
 67    </g>
 68   </g>
 69  </svg>

```
  * file:///opt/input/source/src/main/webapp/bower_components/patternfly/dist/img/OpenShift-Logo-NoText.svg
      * `beans_1_1.xsd`: In the root tag, replace the `version` attribute value with `3.0`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="utf-8"?>
  2  <!-- Generator: Adobe Illustrator 19.2.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
  3  <svg version="1.1"
  4  	 id="svg4242" xmlns:cc="http://creativecommons.org/ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
  5  	 xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 200 199.7"
  6  	 style="enable-background:new 0 0 200 199.7;" xml:space="preserve">
  7  <style type="text/css">
  8  	.st0{fill:#C32034;}
  9  	.st1{fill:#DB212F;}
 10  	.st2{fill:#EA2227;}
 11  	.st3{fill:#AD213A;}
 12  	.st4{fill:#BA2034;}
 13  </style>
 14  <g id="g3921">
 15  	<g id="g3927" transform="translate(304.96 416.03)">
 16  		<path id="path3929" class="st0" d="M-235.4-323l-23.3,8.5c0.3,3.8,0.9,7.5,1.9,11.1l22.1-8C-235.4-315.4-235.7-319.2-235.4-323"/>
 17  	</g>
 18  	<g id="g3931" transform="translate(418.75 444.5)">
 19  		<path id="path3933" class="st0" d="M-246.2-377.3c-1.6-3.3-3.5-6.6-5.6-9.6l-23.3,8.5c2.7,2.8,5,5.9,6.9,9.2
 20  			C-268.3-369.3-246.2-377.3-246.2-377.3z"/>
 21  	</g>
 22  	<g id="g3935" transform="translate(362.11 451.79)">
 23  		<path id="path3937" class="st1" d="M-240.8-391.2c4.8,2.2,9,5.4,12.6,9l23.3-8.5c-6.4-9-15.3-16.6-26-21.6
 24  			c-33.3-15.5-73-1.1-88.5,32.2c-5,10.8-6.9,22.2-6,33.3l23.3-8.5c0.4-5.1,1.6-10.1,3.9-15C-288.2-391.9-262.5-401.2-240.8-391.2"/>
 25  	</g>
 26  	<g id="g3939" transform="translate(282.86 395.05)">
 27  		<path id="path3941" class="st2" d="M-233.3-283.1l-22.1,8c2,8,5.6,15.7,10.4,22.6l23.2-8.5C-227.7-267.1-231.7-274.8-233.3-283.1"
 28  			/>
 29  	</g>
 30  	<g id="g3943" transform="translate(389.56 404.75)">
 31  		<path id="path3945" class="st1" d="M-243.4-301.6c-0.4,5.1-1.7,10.1-3.9,15c-10.1,21.6-35.9,31.1-57.5,20.9c-4.8-2.2-9-5.4-12.6-9
 32  			l-23.2,8.5c6.4,9,15.2,16.6,26,21.6c33.3,15.5,73,1.1,88.5-32.2c5-10.8,6.9-22.2,6-33.3L-243.4-301.6L-243.4-301.6z"/>
 33  	</g>
 34  	<g id="g3947" transform="translate(395.89 436.18)">
 35  		<path id="path3949" class="st2" d="M-244-361.5l-22.1,8c4.1,7.4,6.1,15.9,5.4,24.4l23.2-8.5C-238.1-345.8-240.4-353.9-244-361.5"
 36  			/>
 37  	</g>
 38  	<g id="g3951" transform="translate(279.22 406.66)">
 39  		<path id="path3953" class="st3" d="M-232.9-305.2l23.2-8.4l-0.1,4.6l-22.4,8.3C-232.2-300.7-232.9-305.2-232.9-305.2z"/>
 40  	</g>
 41  	<g id="g3955" transform="translate(386.73 445.86)">
 42  		<path id="path3957" class="st3" d="M-243.1-379.9l23.6-8l2.5,3.6l-22.9,8C-240-376.2-243.1-379.9-243.1-379.9z"/>
 43  	</g>
 44  	<g id="g3959" transform="translate(282.04 365.71)">
 45  		<path id="path3961" class="st4" d="M-233.2-227.2l23.2-8.3l7,6.5l-24.4,9C-227.3-220-233.2-227.2-233.2-227.2z"/>
 46  	</g>
 47  	<g id="g3963" transform="translate(415.68 414.03)">
 48  		<path id="path3965" class="st4" d="M-245.9-319.2l-23.6,8.4l-1.7,9.3l25.2-8.8C-246.1-310.4-245.9-319.2-245.9-319.2z"/>
 49  	</g>
 50  </g>
 51  </svg>

```
  * file:///opt/input/source/src/main/webapp/bower_components/patternfly/dist/img/kubernetes.svg
      * `beans_1_1.xsd`: In the root tag, replace the `version` attribute value with `3.0`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8" standalone="no"?>
  2  <svg width="256px" height="249px" viewBox="0 0 256 249" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" preserveAspectRatio="xMidYMid">
  3  	<g>
  4  		<path d="M82.0851613,244.934194 C76.1393548,244.934194 70.523871,242.291613 66.7251613,237.501935 L8.91870968,165.656774 C5.12,160.867097 3.63354839,154.756129 5.12,148.810323 L25.7651613,59.1277419 C27.0864516,53.1819355 31.0503226,48.3922581 36.5006452,45.7496774 L120.072258,5.78064516 C122.714839,4.45935484 125.687742,3.79870968 128.660645,3.79870968 C131.633548,3.79870968 134.606452,4.45935484 137.249032,5.78064516 L220.820645,45.5845161 C226.270968,48.2270968 230.234839,53.0167742 231.556129,58.9625806 L252.20129,148.645161 C253.522581,154.590968 252.20129,160.701935 248.402581,165.491613 L190.596129,237.336774 C186.797419,241.96129 181.181935,244.769032 175.236129,244.769032 L82.0851613,244.934194 L82.0851613,244.934194 Z" fill="#326DE6"></path>
  5  		<path d="M128.495484,7.92774194 C130.807742,7.92774194 133.12,8.42322581 135.267097,9.41419355 L218.83871,49.2180645 C223.132903,51.3651613 226.436129,55.3290323 227.427097,59.9535484 L248.072258,149.636129 C249.228387,154.425806 248.072258,159.380645 244.934194,163.179355 L187.127742,235.024516 C184.154839,238.823226 179.530323,240.970323 174.740645,240.970323 L82.0851613,240.970323 C77.2954839,240.970323 72.6709677,238.823226 69.6980645,235.024516 L11.8916129,163.179355 C8.91870968,159.380645 7.76258065,154.425806 8.75354839,149.636129 L29.3987097,59.9535484 C30.5548387,55.163871 33.6929032,51.2 37.9870968,49.2180645 L121.55871,9.24903226 C123.705806,8.42322581 126.183226,7.92774194 128.495484,7.92774194 L128.495484,7.92774194 Z M128.495484,0.16516129 L128.495484,0.16516129 C125.027097,0.16516129 121.55871,0.990967742 118.255484,2.47741935 L34.683871,42.4464516 C28.0774194,45.5845161 23.4529032,51.3651613 21.8012903,58.4670968 L1.15612903,148.149677 C-0.495483871,155.251613 1.15612903,162.51871 5.78064516,168.299355 L63.5870968,240.144516 C68.0464516,245.76 74.8180645,248.898065 81.92,248.898065 L174.575484,248.898065 C181.677419,248.898065 188.449032,245.76 192.908387,240.144516 L250.714839,168.299355 C255.339355,162.683871 256.990968,155.251613 255.339355,148.149677 L234.694194,58.4670968 C233.042581,51.3651613 228.418065,45.5845161 221.811613,42.4464516 L138.570323,2.47741935 C135.432258,0.990967742 131.963871,0.16516129 128.495484,0.16516129 L128.495484,0.16516129 L128.495484,0.16516129 Z" fill="#FFFFFF"></path>
  6  		<path d="M212.232258,142.534194 L212.232258,142.534194 L212.232258,142.534194 C212.067097,142.534194 212.067097,142.534194 212.232258,142.534194 L212.067097,142.534194 C211.901935,142.534194 211.736774,142.534194 211.736774,142.369032 C211.406452,142.369032 211.076129,142.203871 210.745806,142.203871 C209.589677,142.03871 208.59871,141.873548 207.607742,141.873548 C207.112258,141.873548 206.616774,141.873548 205.956129,141.708387 L205.790968,141.708387 C202.322581,141.378065 199.514839,141.047742 196.872258,140.221935 C195.716129,139.726452 195.385806,139.065806 195.055484,138.405161 C195.055484,138.24 194.890323,138.24 194.890323,138.074839 L194.890323,138.074839 L192.743226,137.414194 C193.734194,129.816774 193.403871,121.889032 191.587097,114.126452 C189.770323,106.363871 186.632258,99.0967742 182.338065,92.4903226 L183.989677,91.003871 L183.989677,90.6735484 C183.989677,89.8477419 184.154839,89.0219355 184.815484,88.196129 C186.797419,86.3793548 189.274839,84.8929032 192.247742,83.076129 L192.247742,83.076129 C192.743226,82.7458065 193.23871,82.5806452 193.734194,82.2503226 C194.725161,81.7548387 195.550968,81.2593548 196.541935,80.5987097 C196.707097,80.4335484 197.037419,80.2683871 197.367742,79.9380645 C197.532903,79.7729032 197.698065,79.7729032 197.698065,79.6077419 L197.698065,79.6077419 C200.010323,77.6258065 200.505806,74.3225806 198.854194,72.1754839 C198.028387,71.0193548 196.541935,70.3587097 195.055484,70.3587097 C193.734194,70.3587097 192.578065,70.8541935 191.421935,71.68 L191.421935,71.68 L191.421935,71.68 C191.256774,71.8451613 191.256774,71.8451613 191.091613,72.0103226 C190.76129,72.1754839 190.596129,72.5058065 190.265806,72.6709677 C189.44,73.4967742 188.779355,74.1574194 188.11871,74.9832258 C187.788387,75.3135484 187.458065,75.8090323 186.962581,76.1393548 L186.962581,76.1393548 C184.650323,78.6167742 182.503226,80.5987097 180.356129,82.0851613 C179.860645,82.4154839 179.365161,82.5806452 178.869677,82.5806452 C178.539355,82.5806452 178.209032,82.5806452 177.87871,82.4154839 L177.548387,82.4154839 L177.548387,82.4154839 L175.566452,83.7367742 C173.419355,81.4245161 171.107097,79.4425806 168.794839,77.4606452 C158.885161,69.6980645 146.828387,64.9083871 134.276129,63.7522581 L134.110968,61.6051613 C133.945806,61.44 133.945806,61.44 133.780645,61.2748387 C133.285161,60.7793548 132.624516,60.283871 132.459355,59.1277419 C132.294194,56.4851613 132.624516,53.5122581 132.954839,50.2090323 L132.954839,50.043871 C132.954839,49.5483871 133.12,48.8877419 133.285161,48.3922581 C133.450323,47.4012903 133.615484,46.4103226 133.780645,45.2541935 L133.780645,44.2632258 L133.780645,43.7677419 L133.780645,43.7677419 L133.780645,43.7677419 C133.780645,40.7948387 131.468387,38.3174194 128.660645,38.3174194 C127.339355,38.3174194 126.018065,38.9780645 125.027097,39.9690323 C124.036129,40.96 123.540645,42.2812903 123.540645,43.7677419 L123.540645,43.7677419 L123.540645,43.7677419 L123.540645,44.0980645 L123.540645,45.0890323 C123.540645,46.2451613 123.705806,47.236129 124.036129,48.2270968 C124.20129,48.7225806 124.20129,49.2180645 124.366452,49.8787097 L124.366452,50.043871 C124.696774,53.3470968 125.192258,56.32 124.861935,58.9625806 C124.696774,60.1187097 124.036129,60.6141935 123.540645,61.1096774 C123.375484,61.2748387 123.375484,61.2748387 123.210323,61.44 L123.210323,61.44 L123.045161,63.5870968 C120.072258,63.9174194 117.099355,64.2477419 114.126452,64.9083871 C101.409032,67.716129 90.1780645,74.1574194 81.4245161,83.4064516 L79.7729032,82.2503226 L79.4425806,82.2503226 C79.1122581,82.2503226 78.7819355,82.4154839 78.4516129,82.4154839 C77.956129,82.4154839 77.4606452,82.2503226 76.9651613,81.92 C74.8180645,80.4335484 72.6709677,78.2864516 70.3587097,75.8090323 L70.3587097,75.8090323 C70.0283871,75.4787097 69.6980645,74.9832258 69.2025806,74.6529032 C68.5419355,73.8270968 67.8812903,73.1664516 67.0554839,72.3406452 C66.8903226,72.1754839 66.56,72.0103226 66.2296774,71.68 C66.0645161,71.5148387 65.8993548,71.5148387 65.8993548,71.3496774 L65.8993548,71.3496774 C64.9083871,70.523871 63.5870968,70.0283871 62.2658065,70.0283871 C60.7793548,70.0283871 59.2929032,70.6890323 58.4670968,71.8451613 C56.8154839,73.9922581 57.3109677,77.2954839 59.6232258,79.2774194 L59.6232258,79.2774194 L59.6232258,79.2774194 C59.7883871,79.2774194 59.7883871,79.4425806 59.9535484,79.4425806 C60.283871,79.6077419 60.4490323,79.9380645 60.7793548,80.1032258 C61.7703226,80.763871 62.596129,81.2593548 63.5870968,81.7548387 C64.0825806,81.92 64.5780645,82.2503226 65.0735484,82.5806452 L65.0735484,82.5806452 C68.0464516,84.3974194 70.523871,85.883871 72.5058065,87.7006452 C73.3316129,88.5264516 73.3316129,89.3522581 73.3316129,90.1780645 L73.3316129,90.5083871 L73.3316129,90.5083871 L74.9832258,91.9948387 C74.6529032,92.4903226 74.3225806,92.8206452 74.1574194,93.316129 C65.8993548,106.363871 62.7612903,121.723871 64.9083871,136.91871 L62.7612903,137.579355 C62.7612903,137.744516 62.596129,137.744516 62.596129,137.909677 C62.2658065,138.570323 61.7703226,139.230968 60.7793548,139.726452 C58.3019355,140.552258 55.3290323,140.882581 51.8606452,141.212903 L51.6954839,141.212903 C51.2,141.212903 50.5393548,141.212903 50.043871,141.378065 C49.0529032,141.378065 48.0619355,141.543226 46.9058065,141.708387 C46.5754839,141.708387 46.2451613,141.873548 45.9148387,141.873548 C45.7496774,141.873548 45.5845161,141.873548 45.4193548,142.03871 L45.4193548,142.03871 L45.4193548,142.03871 C42.4464516,142.699355 40.6296774,145.507097 41.1251613,148.149677 C41.6206452,150.461935 43.7677419,151.948387 46.4103226,151.948387 C46.9058065,151.948387 47.236129,151.948387 47.7316129,151.783226 L47.7316129,151.783226 L47.7316129,151.783226 C47.8967742,151.783226 48.0619355,151.783226 48.0619355,151.618065 C48.3922581,151.618065 48.7225806,151.452903 49.0529032,151.452903 C50.2090323,151.122581 51.0348387,150.792258 52.0258065,150.296774 C52.5212903,150.131613 53.0167742,149.80129 53.5122581,149.636129 L53.6774194,149.636129 C56.8154839,148.48 59.6232258,147.489032 62.2658065,147.15871 L62.596129,147.15871 C63.5870968,147.15871 64.2477419,147.654194 64.7432258,147.984516 C64.9083871,147.984516 64.9083871,148.149677 65.0735484,148.149677 L65.0735484,148.149677 L67.3858065,147.819355 C71.3496774,160.04129 78.9470968,170.941935 89.0219355,178.869677 C91.3341935,180.686452 93.6464516,182.172903 96.123871,183.659355 L95.1329032,185.806452 C95.1329032,185.971613 95.2980645,185.971613 95.2980645,186.136774 C95.6283871,186.797419 95.9587097,187.623226 95.6283871,188.779355 C94.6374194,191.256774 93.1509677,193.734194 91.3341935,196.541935 L91.3341935,196.707097 C91.003871,197.202581 90.6735484,197.532903 90.3432258,198.028387 C89.6825806,198.854194 89.1870968,199.68 88.5264516,200.670968 C88.3612903,200.836129 88.196129,201.166452 88.0309677,201.496774 C88.0309677,201.661935 87.8658065,201.827097 87.8658065,201.827097 L87.8658065,201.827097 L87.8658065,201.827097 C86.5445161,204.634839 87.5354839,207.772903 90.0129032,208.929032 C90.6735484,209.259355 91.3341935,209.424516 91.9948387,209.424516 C93.9767742,209.424516 95.9587097,208.103226 96.9496774,206.286452 L96.9496774,206.286452 L96.9496774,206.286452 C96.9496774,206.12129 97.1148387,205.956129 97.1148387,205.956129 C97.28,205.625806 97.4451613,205.295484 97.6103226,205.130323 C98.1058065,203.974194 98.2709677,203.148387 98.6012903,202.157419 C98.7664516,201.661935 98.9316129,201.166452 99.0967742,200.670968 L99.0967742,200.670968 C100.252903,197.367742 101.07871,194.725161 102.565161,192.412903 C103.225806,191.421935 104.051613,191.256774 104.712258,190.926452 C104.877419,190.926452 104.877419,190.926452 105.042581,190.76129 L105.042581,190.76129 L106.19871,188.614194 C113.465806,191.421935 121.393548,192.908387 129.32129,192.908387 C134.110968,192.908387 139.065806,192.412903 143.690323,191.256774 C146.663226,190.596129 149.470968,189.770323 152.27871,188.779355 L153.269677,190.596129 C153.434839,190.596129 153.434839,190.596129 153.6,190.76129 C154.425806,190.926452 155.086452,191.256774 155.747097,192.247742 C157.068387,194.56 158.059355,197.367742 159.215484,200.505806 L159.215484,200.670968 C159.380645,201.166452 159.545806,201.661935 159.710968,202.157419 C160.04129,203.148387 160.206452,204.139355 160.701935,205.130323 C160.867097,205.460645 161.032258,205.625806 161.197419,205.956129 C161.197419,206.12129 161.362581,206.286452 161.362581,206.286452 L161.362581,206.286452 L161.362581,206.286452 C162.353548,208.268387 164.335484,209.424516 166.317419,209.424516 C166.978065,209.424516 167.63871,209.259355 168.299355,208.929032 C169.455484,208.268387 170.446452,207.277419 170.776774,205.956129 C171.107097,204.634839 171.107097,203.148387 170.446452,201.827097 L170.446452,201.827097 L170.446452,201.827097 C170.446452,201.661935 170.28129,201.661935 170.28129,201.496774 C170.116129,201.166452 169.950968,200.836129 169.785806,200.670968 C169.290323,199.68 168.629677,198.854194 167.969032,198.028387 C167.63871,197.532903 167.308387,197.202581 166.978065,196.707097 L166.978065,196.541935 C165.16129,193.734194 163.509677,191.256774 162.683871,188.779355 C162.353548,187.623226 162.683871,186.962581 162.849032,186.136774 C162.849032,185.971613 163.014194,185.971613 163.014194,185.806452 L163.014194,185.806452 L162.188387,183.824516 C170.941935,178.704516 178.374194,171.437419 183.989677,162.51871 C186.962581,157.894194 189.274839,152.774194 190.926452,147.654194 L192.908387,147.984516 C193.073548,147.984516 193.073548,147.819355 193.23871,147.819355 C193.899355,147.489032 194.394839,146.993548 195.385806,146.993548 L195.716129,146.993548 C198.35871,147.323871 201.166452,148.314839 204.304516,149.470968 L204.469677,149.470968 C204.965161,149.636129 205.460645,149.966452 205.956129,150.131613 C206.947097,150.627097 207.772903,150.957419 208.929032,151.287742 C209.259355,151.287742 209.589677,151.452903 209.92,151.452903 C210.085161,151.452903 210.250323,151.452903 210.415484,151.618065 L210.415484,151.618065 C210.910968,151.783226 211.24129,151.783226 211.736774,151.783226 C214.214194,151.783226 216.36129,150.131613 217.021935,147.984516 C217.021935,146.002581 215.205161,143.36 212.232258,142.534194 L212.232258,142.534194 Z M135.762581,134.44129 L128.495484,137.909677 L121.228387,134.44129 L119.411613,126.67871 L124.366452,120.402581 L132.459355,120.402581 L137.414194,126.67871 L135.762581,134.44129 L135.762581,134.44129 Z M178.869677,117.264516 C180.190968,122.88 180.52129,128.495484 180.025806,133.945806 L154.756129,126.67871 C152.443871,126.018065 151.122581,123.705806 151.618065,121.393548 C151.783226,120.732903 152.113548,120.072258 152.609032,119.576774 L172.593548,101.574194 C175.40129,106.19871 177.548387,111.483871 178.869677,117.264516 L178.869677,117.264516 Z M164.665806,91.6645161 L143.029677,107.024516 C141.212903,108.180645 138.735484,107.850323 137.249032,106.033548 C136.753548,105.538065 136.588387,104.877419 136.423226,104.216774 L134.936774,77.2954839 C146.332903,78.6167742 156.738065,83.7367742 164.665806,91.6645161 L164.665806,91.6645161 Z M116.769032,78.1212903 C118.585806,77.7909677 120.237419,77.4606452 122.054194,77.1303226 L120.567742,103.556129 C120.402581,105.868387 118.585806,107.850323 116.108387,107.850323 C115.447742,107.850323 114.621935,107.685161 114.126452,107.354839 L92.16,91.6645161 C98.9316129,84.8929032 107.354839,80.2683871 116.769032,78.1212903 L116.769032,78.1212903 Z M84.2322581,101.574194 L103.886452,119.08129 C105.703226,120.567742 105.868387,123.375484 104.381935,125.192258 C103.886452,125.852903 103.225806,126.348387 102.4,126.513548 L76.8,133.945806 C75.8090323,122.714839 78.2864516,111.31871 84.2322581,101.574194 L84.2322581,101.574194 Z M79.7729032,146.332903 L106.033548,141.873548 C108.180645,141.708387 110.162581,143.194839 110.658065,145.341935 C110.823226,146.332903 110.823226,147.15871 110.492903,147.984516 L110.492903,147.984516 L100.418065,172.263226 C91.1690323,166.317419 83.7367742,157.233548 79.7729032,146.332903 L79.7729032,146.332903 Z M140.056774,179.2 C136.258065,180.025806 132.459355,180.52129 128.495484,180.52129 C122.714839,180.52129 117.099355,179.530323 111.814194,177.87871 L124.861935,154.260645 C126.183226,152.774194 128.330323,152.113548 130.147097,153.104516 C130.972903,153.6 131.633548,154.260645 132.129032,154.92129 L132.129032,154.92129 L144.846452,177.87871 C143.36,178.374194 141.708387,178.704516 140.056774,179.2 L140.056774,179.2 Z M172.263226,156.242581 C168.134194,162.849032 162.683871,168.134194 156.407742,172.263226 L146.002581,147.323871 C145.507097,145.341935 146.332903,143.194839 148.314839,142.203871 C148.975484,141.873548 149.80129,141.708387 150.627097,141.708387 L177.052903,146.167742 C176.061935,149.80129 174.410323,153.104516 172.263226,156.242581 L172.263226,156.242581 Z" fill="#FFFFFF"></path>
  7  	</g>
  8  </svg>

```
  * file:///opt/input/source/src/main/webapp/bower_components/patternfly/dist/img/kubernetes-Logo.svg
      * `beans_1_1.xsd`: In the root tag, replace the `version` attribute value with `3.0`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="utf-8"?>
  2  <!-- Generator: Adobe Illustrator 19.2.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
  3  <svg version="1.1"
  4  	 id="svg4242" xmlns:cc="http://creativecommons.org/ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
  5  	 xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 200 199.7"
  6  	 style="enable-background:new 0 0 200 199.7;" xml:space="preserve">
  7  <style type="text/css">
  8  	.st0{fill:#326DE6;}
  9  	.st1{fill:#FFFFFF;}
 10  </style>
 11  <g>
 12  	<path class="st0" d="M70.9,175.8c-3.8,0-7.3-1.7-9.7-4.7l-36.5-45.3c-2.4-3-3.3-6.9-2.4-10.6l13-56.6c0.8-3.8,3.3-6.8,6.8-8.4
 13  		l52.7-25.2c1.7-0.8,3.5-1.3,5.4-1.3c1.9,0,3.8,0.4,5.4,1.3L158.4,50c3.4,1.7,5.9,4.7,6.8,8.4l13,56.6c0.8,3.8,0,7.6-2.4,10.6
 14  		L139.3,171c-2.4,2.9-5.9,4.7-9.7,4.7L70.9,175.8L70.9,175.8z"/>
 15  	<path class="st1" d="M100.2,26.3c1.5,0,2.9,0.3,4.3,0.9l52.7,25.1c2.7,1.4,4.8,3.9,5.4,6.8l13,56.6c0.7,3,0,6.1-2,8.5l-36.5,45.3
 16  		c-1.9,2.4-4.8,3.8-7.8,3.8H70.9c-3,0-5.9-1.4-7.8-3.8l-36.5-45.3c-1.9-2.4-2.6-5.5-2-8.5l13-56.6c0.7-3,2.7-5.5,5.4-6.8l52.7-25.2
 17  		C97.1,26.6,98.7,26.3,100.2,26.3L100.2,26.3z M100.2,21.4L100.2,21.4c-2.2,0-4.4,0.5-6.5,1.5L41,48.1c-4.2,2-7.1,5.6-8.1,10.1
 18  		l-13,56.6c-1,4.5,0,9.1,2.9,12.7l36.5,45.3c2.8,3.5,7.1,5.5,11.6,5.5h58.5c4.5,0,8.8-2,11.6-5.5l36.5-45.3c2.9-3.5,4-8.2,2.9-12.7
 19  		l-13-56.6c-1-4.5-4-8.1-8.1-10.1l-52.5-25.2C104.5,21.9,102.3,21.4,100.2,21.4L100.2,21.4L100.2,21.4z"/>
 20  	<path class="st1" d="M153,111.2L153,111.2L153,111.2C152.9,111.2,152.9,111.2,153,111.2h-0.1c-0.1,0-0.2,0-0.2-0.1
 21  		c-0.2,0-0.4-0.1-0.6-0.1c-0.7-0.1-1.4-0.2-2-0.2c-0.3,0-0.6,0-1-0.1h-0.1c-2.2-0.2-4-0.4-5.6-0.9c-0.7-0.3-0.9-0.7-1.1-1.1
 22  		c0-0.1-0.1-0.1-0.1-0.2l0,0l-1.4-0.4c0.6-4.8,0.4-9.8-0.7-14.7c-1.1-4.9-3.1-9.5-5.8-13.7l1-0.9v-0.2c0-0.5,0.1-1,0.5-1.6
 23  		c1.3-1.1,2.8-2.1,4.7-3.2l0,0c0.3-0.2,0.6-0.3,0.9-0.5c0.6-0.3,1.1-0.6,1.8-1c0.1-0.1,0.3-0.2,0.5-0.4c0.1-0.1,0.2-0.1,0.2-0.2l0,0
 24  		c1.5-1.3,1.8-3.3,0.7-4.7c-0.5-0.7-1.5-1.1-2.4-1.1c-0.8,0-1.6,0.3-2.3,0.8l0,0l0,0c-0.1,0.1-0.1,0.1-0.2,0.2
 25  		c-0.2,0.1-0.3,0.3-0.5,0.4c-0.5,0.5-0.9,0.9-1.4,1.5c-0.2,0.2-0.4,0.5-0.7,0.7l0,0c-1.5,1.6-2.8,2.8-4.2,3.8
 26  		c-0.3,0.2-0.6,0.3-0.9,0.3c-0.2,0-0.4,0-0.6-0.1h-0.2l0,0l-1.3,0.8c-1.4-1.5-2.8-2.7-4.3-4c-6.3-4.9-13.9-7.9-21.8-8.6l-0.1-1.4
 27  		c-0.1-0.1-0.1-0.1-0.2-0.2c-0.3-0.3-0.7-0.6-0.8-1.4c-0.1-1.7,0.1-3.5,0.3-5.6v-0.1c0-0.3,0.1-0.7,0.2-1c0.1-0.6,0.2-1.3,0.3-2
 28  		v-0.6v-0.3l0,0l0,0c0-1.9-1.5-3.4-3.2-3.4c-0.8,0-1.7,0.4-2.3,1C97.3,47.1,97,48,97,48.9l0,0l0,0v0.2v0.6c0,0.7,0.1,1.4,0.3,2
 29  		c0.1,0.3,0.1,0.6,0.2,1v0.1c0.2,2.1,0.5,4,0.3,5.6c-0.1,0.7-0.5,1-0.8,1.4c-0.1,0.1-0.1,0.1-0.2,0.2l0,0l-0.1,1.4
 30  		c-1.9,0.2-3.8,0.4-5.6,0.8c-8,1.8-15.1,5.8-20.6,11.7l-1-0.7h-0.2c-0.2,0-0.4,0.1-0.6,0.1c-0.3,0-0.6-0.1-0.9-0.3
 31  		c-1.4-0.9-2.7-2.3-4.2-3.9l0,0c-0.2-0.2-0.4-0.5-0.7-0.7c-0.4-0.5-0.8-0.9-1.4-1.5c-0.1-0.1-0.3-0.2-0.5-0.4
 32  		c-0.1-0.1-0.2-0.1-0.2-0.2l0,0c-0.6-0.5-1.5-0.8-2.3-0.8c-0.9,0-1.9,0.4-2.4,1.1c-1,1.4-0.7,3.4,0.7,4.7l0,0l0,0
 33  		c0.1,0,0.1,0.1,0.2,0.1c0.2,0.1,0.3,0.3,0.5,0.4c0.6,0.4,1.1,0.7,1.8,1c0.3,0.1,0.6,0.3,0.9,0.5l0,0c1.9,1.1,3.4,2.1,4.7,3.2
 34  		c0.5,0.5,0.5,1,0.5,1.6v0.2l0,0l1,0.9c-0.2,0.3-0.4,0.5-0.5,0.8c-5.2,8.2-7.2,17.9-5.8,27.5l-1.4,0.4c0,0.1-0.1,0.1-0.1,0.2
 35  		c-0.2,0.4-0.5,0.8-1.1,1.1c-1.6,0.5-3.4,0.7-5.6,0.9h-0.1c-0.3,0-0.7,0-1,0.1c-0.6,0-1.3,0.1-2,0.2c-0.2,0-0.4,0.1-0.6,0.1
 36  		c-0.1,0-0.2,0-0.3,0.1l0,0l0,0c-1.9,0.4-3,2.2-2.7,3.9c0.3,1.5,1.7,2.4,3.3,2.4c0.3,0,0.5,0,0.8-0.1l0,0l0,0c0.1,0,0.2,0,0.2-0.1
 37  		c0.2,0,0.4-0.1,0.6-0.1c0.7-0.2,1.3-0.4,1.9-0.7c0.3-0.1,0.6-0.3,0.9-0.4H53c2-0.7,3.8-1.4,5.4-1.6h0.2c0.6,0,1,0.3,1.4,0.5
 38  		c0.1,0,0.1,0.1,0.2,0.1l0,0l1.5-0.2c2.5,7.7,7.3,14.6,13.7,19.6c1.5,1.1,2.9,2.1,4.5,3l-0.6,1.4c0,0.1,0.1,0.1,0.1,0.2
 39  		c0.2,0.4,0.4,0.9,0.2,1.7c-0.6,1.6-1.6,3.1-2.7,4.9v0.1c-0.2,0.3-0.4,0.5-0.6,0.8c-0.4,0.5-0.7,1-1.1,1.7c-0.1,0.1-0.2,0.3-0.3,0.5
 40  		c0,0.1-0.1,0.2-0.1,0.2l0,0l0,0c-0.8,1.8-0.2,3.8,1.4,4.5c0.4,0.2,0.8,0.3,1.3,0.3c1.3,0,2.5-0.8,3.1-2l0,0l0,0
 41  		c0-0.1,0.1-0.2,0.1-0.2c0.1-0.2,0.2-0.4,0.3-0.5c0.3-0.7,0.4-1.3,0.6-1.9c0.1-0.3,0.2-0.6,0.3-0.9l0,0c0.7-2.1,1.3-3.8,2.2-5.2
 42  		c0.4-0.6,0.9-0.7,1.4-0.9c0.1,0,0.1,0,0.2-0.1l0,0l0.7-1.4c4.6,1.8,9.6,2.7,14.6,2.7c3,0,6.1-0.3,9.1-1c1.9-0.4,3.6-0.9,5.4-1.6
 43  		l0.6,1.1c0.1,0,0.1,0,0.2,0.1c0.5,0.1,0.9,0.3,1.4,0.9c0.8,1.5,1.5,3.2,2.2,5.2v0.1c0.1,0.3,0.2,0.6,0.3,0.9
 44  		c0.2,0.6,0.3,1.3,0.6,1.9c0.1,0.2,0.2,0.3,0.3,0.5c0,0.1,0.1,0.2,0.1,0.2l0,0l0,0c0.6,1.3,1.9,2,3.1,2c0.4,0,0.8-0.1,1.3-0.3
 45  		c0.7-0.4,1.4-1,1.6-1.9c0.2-0.8,0.2-1.8-0.2-2.6l0,0l0,0c0-0.1-0.1-0.1-0.1-0.2c-0.1-0.2-0.2-0.4-0.3-0.5c-0.3-0.6-0.7-1.1-1.1-1.7
 46  		c-0.2-0.3-0.4-0.5-0.6-0.8v-0.1c-1.1-1.8-2.2-3.3-2.7-4.9c-0.2-0.7,0-1.1,0.1-1.7c0-0.1,0.1-0.1,0.1-0.2l0,0l-0.5-1.3
 47  		c5.5-3.2,10.2-7.8,13.8-13.4c1.9-2.9,3.3-6.1,4.4-9.4l1.3,0.2c0.1,0,0.1-0.1,0.2-0.1c0.4-0.2,0.7-0.5,1.4-0.5h0.2
 48  		c1.7,0.2,3.4,0.8,5.4,1.6h0.1c0.3,0.1,0.6,0.3,0.9,0.4c0.6,0.3,1.1,0.5,1.9,0.7c0.2,0,0.4,0.1,0.6,0.1c0.1,0,0.2,0,0.3,0.1l0,0
 49  		c0.3,0.1,0.5,0.1,0.8,0.1c1.6,0,2.9-1,3.3-2.4C156,113.4,154.9,111.7,153,111.2L153,111.2z M104.7,106.1l-4.6,2.2l-4.6-2.2
 50  		l-1.1-4.9l3.1-4h5.1l3.1,4L104.7,106.1L104.7,106.1z M131.9,95.3c0.8,3.5,1,7.1,0.7,10.5l-15.9-4.6c-1.5-0.4-2.3-1.9-2-3.3
 51  		c0.1-0.4,0.3-0.8,0.6-1.1L128,85.4C129.8,88.3,131.1,91.6,131.9,95.3L131.9,95.3z M123,79.1l-13.7,9.7c-1.1,0.7-2.7,0.5-3.6-0.6
 52  		c-0.3-0.3-0.4-0.7-0.5-1.1l-0.9-17C111.4,70.9,118,74.1,123,79.1L123,79.1z M92.8,70.6c1.1-0.2,2.2-0.4,3.3-0.6l-0.9,16.7
 53  		c-0.1,1.5-1.3,2.7-2.8,2.7c-0.4,0-0.9-0.1-1.3-0.3l-13.9-9.9C81.5,74.8,86.8,71.9,92.8,70.6L92.8,70.6z M72.2,85.4l12.4,11
 54  		c1.1,0.9,1.3,2.7,0.3,3.9c-0.3,0.4-0.7,0.7-1.3,0.8l-16.2,4.7C66.9,98.7,68.5,91.5,72.2,85.4L72.2,85.4z M69.4,113.6l16.6-2.8
 55  		c1.4-0.1,2.6,0.8,2.9,2.2c0.1,0.6,0.1,1.1-0.1,1.7l0,0L82.4,130C76.6,126.2,71.9,120.5,69.4,113.6L69.4,113.6z M107.5,134.3
 56  		c-2.4,0.5-4.8,0.8-7.3,0.8c-3.6,0-7.2-0.6-10.5-1.7l8.2-14.9c0.8-0.9,2.2-1.4,3.3-0.7c0.5,0.3,0.9,0.7,1.3,1.1l0,0l8,14.5
 57  		C109.5,133.8,108.5,134,107.5,134.3L107.5,134.3z M127.8,119.9c-2.6,4.2-6,7.5-10,10.1l-6.6-15.7c-0.3-1.3,0.2-2.6,1.5-3.2
 58  		c0.4-0.2,0.9-0.3,1.5-0.3l16.7,2.8C130.2,115.8,129.1,117.9,127.8,119.9L127.8,119.9z"/>
 59  </g>
 60  </svg>

```
  * file:///opt/input/source/src/main/webapp/bower_components/patternfly/dist/img/RH_Atomic-Logo-Text.svg
      * `beans_1_1.xsd`: In the root tag, replace the `version` attribute value with `3.0`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="utf-8"?>
  2  <!-- Generator: Adobe Illustrator 19.2.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
  3  <svg version="1.1"
  4  	 id="svg4242" xmlns:cc="http://creativecommons.org/ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
  5  	 xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 200 199.7"
  6  	 style="enable-background:new 0 0 200 199.7;" xml:space="preserve">
  7  <style type="text/css">
  8  	.st0{fill:#00B9E4;}
  9  	.st1{fill:#0088CE;}
 10  </style>
 11  <g>
 12  	<g>
 13  		<g>
 14  			<path class="st0" d="M88.1,117.9c-0.4,0.3-0.7,0.6-1,0.8c-2.5,2.5-4.9,4.8-7.1,6.9c1.4,0.8,2.4,2.1,3,3.7c2.7-2.4,5.5-5,8.4-7.9
 15  				c0.6-0.6,1.1-2.2-0.1-3.3C90.4,117.4,89,117.2,88.1,117.9z"/>
 16  			<path class="st0" d="M60.3,58.6c0.7,1.1,2.2,1.5,3.3,0.7c1.2-0.8,1-2.4,0.6-2.9C54.5,39.9,50.1,27.2,54,24.2
 17  				c2.4-1.9,7.6,0.2,14.5,5.3c0.7-2.2,2.3-4,4.3-5c-11.1-8.3-19.9-11.8-24-8.6C43,20.4,47.8,37,59.9,58C60,58.2,60.2,58.4,60.3,58.6
 18  				z"/>
 19  			<path class="st0" d="M140.3,104.4c2.9-0.4,5.7-0.8,8.3-1.3l0,0l0,0l0,0c0.7-0.7,1.2-1.7,1.2-2.8c0-1.8-1.3-3.3-2.9-3.7l0,0
 20  				c-3.2,0.5-6.7,1-10.4,1.4l0,0l0,0c-5.7-9.3-12.7-19.4-20.6-29.5c-2.3-3.2-7.4-9.1-11.3-13.6l0.1-0.1C124,33.4,141,20.3,146,24.1
 21  				c3.8,3-0.5,15.6-10.3,32.2c-0.3,0.5-0.6,2.1,0.6,2.9c1.2,0.8,2.7,0.4,3.3-0.7c0.1-0.2,0.3-0.4,0.4-0.6c12-21,16.9-37.6,11.1-42.1
 22  				c-7-5.5-27.8,8.6-50.3,32.9c0,0-0.3,0.4-1,1.1c-0.6-0.6-1-1.1-1-1.1c-4.9-5.2-9.7-10.1-14.2-14.2l0,0c-0.1-0.1-0.1-0.1-0.1-0.1
 23  				c-0.2-0.1-0.4-0.1-0.6-0.1c-2.1,0-3.8,1.7-3.8,3.8c0,0.5,0.1,1.1,0.3,1.5l0,0c4.7,4.4,9.6,9.5,14.8,15.2l0.1,0.1
 24  				c-4,4.5-9,10.4-11.3,13.6C76.1,78.6,69.1,88.6,63.4,98c-21.9-2.5-36.6-7.1-36.5-12.4c0-5.4,15.6-10.1,38.4-12.4
 25  				c0.3-0.1,0.4-0.1,0.7-0.1c1.2-0.2,1.9-1.4,1.8-2.3c0-1.2-0.9-2.4-2.6-2.4c-28.3,3.2-48,10.2-48,18.3
 26  				c-0.1,7.6,17.2,14.2,42.6,17.7c-11.9,20.9-16.7,37.3-10.9,41.8c4.2,3.3,13.3-0.4,24.7-9.1l0,0c0,0,0,0,0.1,0
 27  				c0.1-0.3,0.1-0.5,0.1-0.8c0-1.5-1.3-2.8-2.8-2.8c-0.2,0-0.3,0-0.4,0.1l0,0l0,0c-7.1,5.2-12.4,7.5-14.8,5.6
 28  				c-4-3.1,0.8-16.4,11.4-33.8c9.8,1.1,20.7,1.6,32.1,1.7l0,0c0.2,0,0.3,0,0.5,0l0,0l0,0c0.1,0,0.3,0,0.4,0l0,0h0.1l0,0h0.1
 29  				c0.1,0,0.3,0,0.4,0c0.2,0,0.3,0,0.5,0l0,0c11.4-0.1,22.3-0.6,32.1-1.7c10.5,17.5,15.4,30.8,11.4,33.8
 30  				c-4.1,3.2-16.5-5.2-31.5-20.4c-0.3-0.3-0.6-0.6-1-0.8c-1-0.7-2.3-0.5-3,0.2c-1.2,1.2-0.8,2.7-0.1,3.3
 31  				c19.4,19.2,36.3,29.6,42.5,24.8C157,141.7,152.2,125.3,140.3,104.4L140.3,104.4z M100.3,100c-0.1,0-0.2,0-0.3,0s-0.2,0-0.3,0
 32  				c-10.2,0-20-0.4-28.7-1.2c5.2-8.2,11.5-16.9,18.6-25.9c3.2-4,6.4-7.9,9.5-11.5l0,0c0.3-0.4,0.6-0.7,0.9-1.1
 33  				c0.3,0.4,0.6,0.7,0.9,1.1l0,0c3.1,3.7,6.3,7.5,9.5,11.5c7.1,9,13.3,17.8,18.6,25.9l0,0C120.2,99.6,110.5,100,100.3,100z"/>
 34  			<path class="st0" d="M134.9,68.4c-1.7-0.1-2.6,1.2-2.6,2.4c-0.1,1,0.6,2.1,1.8,2.3c0.2,0.1,0.4,0.1,0.7,0.1
 35  				c22.8,2.4,38.3,7,38.4,12.4c0,1.9-1.9,3.7-5.4,5.4c1.1,1.7,1.8,3.9,1.8,6.1c0,0.2,0,0.4-0.1,0.5c8.5-3.2,13.3-7,13.3-11
 36  				C182.9,78.5,163.2,71.6,134.9,68.4z"/>
 37  		</g>
 38  		<g>
 39  			<path class="st1" d="M76.6,23.6c-4.7,0-8.6,3.8-8.6,8.6c0,4.7,3.8,8.6,8.6,8.6c1.4,0,2.8-0.4,3.9-1c-0.2-0.5-0.3-1-0.3-1.5
 40  				c0-2.1,1.7-3.8,3.8-3.8c0.2,0,0.4,0,0.6,0.1c0.1,0.1,0.1,0.1,0.1,0.1c0.2-0.8,0.4-1.6,0.4-2.4C85.2,27.4,81.4,23.6,76.6,23.6z"/>
 41  			<path class="st1" d="M99.1,48.8c-0.4-0.4-0.7-0.8-1.2-1.2l-4.4,5.3c0.6,0.7,1.3,1.4,1.9,2.1l0.1,0.1c1.9-2.2,3.6-4.1,4.6-5.2
 42  				C99.4,49.2,99.1,48.8,99.1,48.8z"/>
 43  			<path class="st1" d="M100,60.3L100,60.3c0.3,0.4,0.6,0.7,0.9,1.1l0,0c1,1.2,2,2.3,3,3.5l4.6-5.4c-1.3-1.5-2.6-3-3.8-4.4L100,60.3
 44  				z"/>
 45  			<path class="st1" d="M158.3,85.9c-6,0-11,4.8-11.3,10.7c1.7,0.4,2.9,1.9,2.9,3.7c0,1.1-0.5,2.1-1.2,2.8l0,0
 46  				c2,3.2,5.6,5.4,9.6,5.4c6.2,0,11.3-5.1,11.3-11.3C169.6,90.9,164.5,85.9,158.3,85.9z"/>
 47  			<path class="st1" d="M59.7,104.4c-1.2,2.1-2.3,4.1-3.3,6.1l7,0.9c1.1-2,2.3-4,3.5-6.1L59.7,104.4L59.7,104.4z"/>
 48  			<path class="st1" d="M71,98.8c0.4-0.7,0.9-1.4,1.4-2.1l-7.5-0.9c-0.5,0.7-1,1.5-1.4,2.2l0,0L71,98.8L71,98.8z"/>
 49  			<path class="st1" d="M136.6,98.1c-0.5-0.8-1-1.6-1.5-2.3l-7.5,1c0.5,0.7,1,1.5,1.4,2.2l0,0l0,0L136.6,98.1L136.6,98.1z"/>
 50  			<path class="st1" d="M133.1,105.3L133.1,105.3c1.2,2.1,2.4,4.1,3.5,6l7-0.9c-1-2-2.1-4-3.3-6L133.1,105.3z"/>
 51  			<path class="st1" d="M76.6,124.7c-3.7,0-6.6,3-6.6,6.6c0,0.8,0.2,1.5,0.4,2.2l0,0c0.1,0,0.3-0.1,0.4-0.1c1.5,0,2.8,1.3,2.8,2.8
 52  				c0,0.3-0.1,0.5-0.1,0.8c0,0,0,0-0.1,0c1,0.5,2,0.8,3.2,0.8c3.7,0,6.6-3,6.6-6.6C83.2,127.7,80.3,124.7,76.6,124.7z"/>
 53  		</g>
 54  	</g>
 55  	<g>
 56  		<path class="st0" d="M34.2,184.7l-2.1-4.2h-2.3v4.2h-2.3v-11.6h5.4c0.5,0,1.1,0.1,1.5,0.2c0.5,0.2,0.9,0.4,1.3,0.7
 57  			c0.4,0.3,0.6,0.7,0.8,1.2c0.2,0.5,0.3,1,0.3,1.6c0,0.9-0.2,1.6-0.6,2.2c-0.4,0.6-1,1-1.7,1.3l2.2,4.5H34.2z M34.1,175.7
 58  			c-0.3-0.2-0.7-0.3-1.2-0.3h-3.1v3h3.1c1.1,0,1.7-0.5,1.7-1.5C34.5,176.3,34.4,175.9,34.1,175.7z"/>
 59  		<path class="st0" d="M39.8,184.7v-11.6h8.1v2.3h-5.8v2h3.3v2.3h-3.3v2.8h6v2.3L39.8,184.7L39.8,184.7z"/>
 60  		<path class="st0" d="M60.1,181.5c-0.3,0.7-0.8,1.3-1.3,1.8c-0.6,0.5-1.2,0.8-1.9,1.1c-0.7,0.2-1.4,0.3-2.2,0.3h-3.5v-11.6h3.7
 61  			c0.8,0,1.6,0.1,2.3,0.3c0.7,0.2,1.3,0.5,1.9,1c0.5,0.5,0.9,1.1,1.2,1.8s0.4,1.6,0.4,2.7C60.6,179.9,60.4,180.8,60.1,181.5z
 62  			 M57.4,176.2c-0.5-0.6-1.4-0.9-2.6-0.9h-1.2v7.1h1.2c0.6,0,1.2-0.1,1.6-0.3c0.5-0.2,0.8-0.4,1.1-0.7c0.3-0.3,0.5-0.7,0.6-1.1
 63  			c0.2-0.4,0.2-0.9,0.2-1.4C58.2,177.7,57.9,176.9,57.4,176.2z"/>
 64  		<path class="st0" d="M75.8,184.7v-4.9h-4.8v4.9h-2.3v-11.6h2.3v4.4h4.8v-4.4h2.3v11.6H75.8z"/>
 65  		<path class="st0" d="M89.4,184.7l-0.9-2.6h-4.2l-0.9,2.6h-2.5l4.4-11.6h2.3l4.4,11.6H89.4z M87,177.8c-0.1-0.3-0.2-0.7-0.3-1
 66  			c-0.1-0.3-0.2-0.6-0.3-0.8c-0.1,0.2-0.2,0.5-0.3,0.8s-0.2,0.6-0.3,1l-0.7,2.1h2.6L87,177.8z"/>
 67  		<path class="st0" d="M97.9,175.4v9.4h-2.3v-9.4h-3.3v-2.3h9v2.3H97.9z"/>
 68  		<path class="st0" d="M117.1,184.7l-0.9-2.6h-4.2l-0.9,2.6h-2.5l4.4-11.6h2.3l4.4,11.6H117.1z M114.6,177.8c-0.1-0.3-0.2-0.7-0.3-1
 69  			c-0.1-0.3-0.2-0.6-0.3-0.8c-0.1,0.2-0.2,0.5-0.3,0.8s-0.2,0.6-0.3,1l-0.7,2.1h2.6L114.6,177.8z"/>
 70  		<path class="st0" d="M125.6,175.4v9.4h-2.3v-9.4H120v-2.3h9v2.3H125.6z"/>
 71  		<path class="st0" d="M140.4,181.4c-0.3,0.7-0.6,1.4-1.1,1.9s-1,0.9-1.6,1.2c-0.6,0.3-1.3,0.4-2.1,0.4s-1.5-0.2-2.1-0.4
 72  			c-0.6-0.3-1.2-0.7-1.6-1.2c-0.4-0.5-0.8-1.2-1.1-1.9c-0.3-0.7-0.4-1.6-0.4-2.5c0-1,0.1-1.8,0.4-2.5c0.3-0.7,0.6-1.4,1.1-1.9
 73  			c0.5-0.5,1-0.9,1.6-1.2c0.6-0.3,1.3-0.4,2.1-0.4c0.7,0,1.4,0.2,2.1,0.4s1.2,0.7,1.6,1.2c0.4,0.5,0.8,1.2,1.1,1.9
 74  			c0.3,0.7,0.4,1.6,0.4,2.5C140.8,179.8,140.6,180.7,140.4,181.4z M137.6,176.2c-0.5-0.6-1.2-1-2-1c-0.8,0-1.5,0.3-2,1
 75  			c-0.5,0.6-0.7,1.5-0.7,2.7c0,1.2,0.3,2.1,0.7,2.8c0.5,0.6,1.2,1,2,1c0.8,0,1.5-0.3,2-1c0.5-0.6,0.7-1.5,0.7-2.7
 76  			C138.4,177.8,138.1,176.8,137.6,176.2z"/>
 77  		<path class="st0" d="M152.2,184.7v-4.3c0-0.2,0-0.4,0-0.6c0-0.3,0-0.5,0-0.7s0-0.5,0-0.7c0-0.2,0-0.4,0-0.5
 78  			c-0.1,0.2-0.2,0.5-0.4,0.9c-0.2,0.4-0.3,0.7-0.5,1.1l-2.4,5.2l-2.3-5.2c-0.2-0.3-0.3-0.7-0.5-1.1c-0.2-0.4-0.3-0.6-0.4-0.9
 79  			c0,0.1,0,0.3,0,0.5s0,0.5,0,0.7s0,0.5,0,0.7c0,0.3,0,0.4,0,0.6v4.3h-2.3v-11.6h2.2l2.4,5.3c0.1,0.2,0.2,0.3,0.2,0.5
 80  			s0.2,0.4,0.2,0.5c0.1,0.2,0.2,0.3,0.2,0.5c0.1,0.2,0.1,0.3,0.2,0.4c0.1-0.2,0.2-0.5,0.3-0.9c0.2-0.4,0.3-0.7,0.5-1.1l2.3-5.3h2.3
 81  			v11.6L152.2,184.7L152.2,184.7z"/>
 82  		<path class="st0" d="M158.1,184.7v-11.6h2.3v11.6H158.1z"/>
 83  		<path class="st0" d="M170.8,176.5c-0.2-0.4-0.5-0.7-0.8-1c-0.3-0.2-0.8-0.3-1.3-0.3c-0.4,0-0.8,0.1-1.2,0.3
 84  			c-0.4,0.2-0.6,0.4-0.8,0.7c-0.2,0.3-0.4,0.7-0.5,1.2c-0.1,0.5-0.2,1-0.2,1.5s0.1,1,0.2,1.4s0.3,0.8,0.5,1.2
 85  			c0.2,0.3,0.5,0.6,0.8,0.8s0.7,0.3,1.2,0.3c0.5,0,1-0.1,1.3-0.4c0.3-0.2,0.7-0.6,1-1.1l2,1.2c-0.4,0.8-1,1.5-1.6,2
 86  			c-0.7,0.5-1.6,0.7-2.6,0.7c-0.7,0-1.5-0.2-2.1-0.4c-0.6-0.3-1.2-0.7-1.6-1.2c-0.5-0.5-0.8-1.2-1.1-1.9c-0.3-0.7-0.4-1.6-0.4-2.5
 87  			c0-0.9,0.1-1.7,0.4-2.4c0.3-0.7,0.6-1.4,1.1-1.9c0.5-0.5,1-1,1.6-1.2c0.6-0.3,1.3-0.4,2.1-0.4c0.5,0,1.1,0.1,1.5,0.2
 88  			c0.4,0.1,0.8,0.3,1.2,0.5s0.6,0.5,0.9,0.8c0.3,0.3,0.5,0.7,0.7,1.1L170.8,176.5z"/>
 89  	</g>
 90  </g>
 91  </svg>

```
  * file:///opt/input/source/src/main/webapp/bower_components/patternfly/dist/img/RH_atomic.svg
      * `beans_1_1.xsd`: In the root tag, replace the `version` attribute value with `3.0`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="utf-8"?>
  2  <!-- Generator: Adobe Illustrator 18.0.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
  3  <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
  4  <svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
  5  	 width="612px" height="792px" viewBox="0 0 612 792" enable-background="new 0 0 612 792" xml:space="preserve">
  6  <g>
  7  	<g>
  8  		<path fill="#00B9E4" d="M290.9,389.7c-0.7,0.5-1.3,1.2-1.8,1.6c-4.7,4.7-9.2,9-13.5,13c2.6,1.5,4.6,4,5.6,6.9
  9  			c5.1-4.6,10.4-9.5,15.8-14.9c1.2-1.1,2-4.1-0.2-6.2C295.2,388.7,292.6,388.4,290.9,389.7z"/>
 10  		<path fill="#00B9E4" d="M238.3,277.7c1.3,2,4.2,2.9,6.3,1.4c2.3-1.5,1.8-4.5,1.2-5.5c-18.4-31.3-26.7-55.2-19.4-60.9
 11  			c4.5-3.5,14.3,0.4,27.4,10c1.3-4.1,4.3-7.5,8.1-9.5c-21-15.7-37.6-22.3-45.4-16.2c-10.9,8.5-1.7,39.8,21,79.5
 12  			C237.8,276.9,238.1,277.3,238.3,277.7z"/>
 13  		<path fill="#00B9E4" d="M389.5,364.1c5.5-0.7,10.7-1.6,15.7-2.5c0,0,0,0,0,0c0,0,0,0,0,0c0,0,0,0,0,0c1.4-1.3,2.3-3.2,2.3-5.3
 14  			c0-3.4-2.4-6.2-5.5-6.9c0,0,0,0,0,0c-6.1,1-12.7,1.9-19.7,2.7l0,0l0,0c-10.8-17.6-24-36.6-39-55.7c-4.4-6-13.9-17.1-21.4-25.6
 15  			l0.1-0.1c36.6-40.7,68.9-65.5,78.2-58.2c7.2,5.6-1,29.5-19.4,60.9c-0.6,1-1.1,4,1.2,5.5c2.2,1.5,5.1,0.7,6.3-1.4
 16  			c0.2-0.3,0.5-0.8,0.7-1.1c22.7-39.7,31.9-71,21-79.5c-13.3-10.4-52.5,16.2-95,62.1c0,0-0.6,0.7-1.8,2c-1.1-1.2-1.8-2-1.8-2
 17  			c-9.2-9.9-18.3-19-26.9-26.9v0c-0.1-0.1-0.1-0.1-0.2-0.2c-0.4-0.1-0.8-0.1-1.2-0.1c-4,0-7.2,3.2-7.2,7.2c0,1,0.2,2,0.6,2.8l0,0
 18  			c8.8,8.3,18.2,18,28,28.8l0.1,0.1c-7.5,8.5-17,19.6-21.4,25.6c-15,19.1-28.2,38-39,55.7c-41.3-4.7-69.1-13.4-69-23.4
 19  			c0-10.2,29.4-19,72.5-23.5c0.5-0.1,0.8-0.2,1.3-0.2c2.3-0.4,3.5-2.6,3.4-4.4c0-2.3-1.7-4.6-4.9-4.5c-53.5,6-90.6,19.2-90.7,34.5
 20  			c-0.1,14.4,32.4,26.9,80.4,33.5c-22.5,39.4-31.5,70.4-20.6,78.9c7.9,6.2,25.1-0.7,46.6-17.1l0,0c0,0,0,0,0.1,0
 21  			c0.1-0.5,0.2-1,0.2-1.5c0-2.9-2.4-5.3-5.3-5.3c-0.3,0-0.5,0-0.7,0.1c0,0,0,0,0,0v0c-13.4,9.9-23.5,14.1-28,10.5
 22  			c-7.5-5.9,1.6-30.9,21.5-63.9c18.6,2,39.1,3.1,60.7,3.2v0c0.3,0,0.6,0,0.9,0c0,0,0,0,0,0l0,0c0.2,0,0.5,0,0.7,0h0h0.2c0,0,0,0,0,0
 23  			h0.2c0.2,0,0.5,0,0.7,0c0.3,0,0.6,0,0.9,0v0c21.5-0.1,42.1-1.2,60.7-3.2c19.9,33,29,58.1,21.5,63.9c-7.7,6-31.1-9.8-59.6-38.5
 24  			c-0.5-0.5-1.1-1.1-1.8-1.6c-1.8-1.3-4.3-1-5.7,0.4c-2.2,2.2-1.5,5.1-0.2,6.2c36.6,36.3,68.5,56,80.2,46.8
 25  			C421,434.6,412,403.6,389.5,364.1L389.5,364.1z M313.9,355.9c-0.2,0-0.3,0-0.5,0c-0.2,0-0.3,0-0.5,0c-19.3,0-37.7-0.8-54.3-2.3
 26  			c9.9-15.4,21.8-32,35.1-49c6-7.6,12-14.9,17.9-21.8v0c0.6-0.7,1.2-1.4,1.7-2c0.6,0.7,1.2,1.4,1.7,2v0c5.9,6.9,11.9,14.2,17.9,21.8
 27  			c13.4,17,25.2,33.6,35.1,49l0,0C351.6,355,333.2,355.8,313.9,355.9z"/>
 28  		<path fill="#00B9E4" d="M379.3,296.2c-3.2-0.1-4.9,2.2-4.9,4.5c-0.1,1.8,1.2,4,3.4,4.4c0.4,0.1,0.8,0.2,1.3,0.2
 29  			c43.1,4.5,72.4,13.3,72.5,23.5c0,3.6-3.6,7-10.2,10.2c2.1,3.3,3.4,7.3,3.4,11.5c0,0.3,0,0.7-0.1,1c16-6,25.2-13.2,25.2-20.8
 30  			C469.9,315.3,432.7,302.2,379.3,296.2z"/>
 31  	</g>
 32  	<g>
 33  		<path fill="#0088CE" d="M269.2,211.5c-8.9,0-16.2,7.2-16.2,16.2c0,8.9,7.2,16.2,16.2,16.2c2.7,0,5.2-0.7,7.4-1.8
 34  			c-0.4-0.9-0.6-1.8-0.6-2.8c0-4,3.2-7.2,7.2-7.2c0.4,0,0.8,0,1.2,0.1c0.1,0.1,0.1,0.1,0.2,0.2c0.4-1.5,0.7-3,0.7-4.6
 35  			C285.4,218.7,278.2,211.5,269.2,211.5z"/>
 36  		<path fill="#0088CE" d="M311.6,259.2c-0.7-0.8-1.4-1.5-2.2-2.3l-8.4,10c1.2,1.3,2.4,2.6,3.6,3.9l0.1,0.1c3.6-4.2,6.8-7.7,8.7-9.8
 37  			C312.3,259.9,311.6,259.2,311.6,259.2z"/>
 38  		<path fill="#0088CE" d="M313.4,280.8C313.4,280.8,313.4,280.8,313.4,280.8c0.6,0.7,1.2,1.4,1.7,2.1v0c1.9,2.2,3.7,4.4,5.6,6.6
 39  			l8.6-10.2c-2.5-2.9-4.9-5.7-7.2-8.3L313.4,280.8z"/>
 40  		<path fill="#0088CE" d="M423.4,329.2c-11.4,0-20.8,9-21.3,20.3c3.2,0.7,5.5,3.5,5.5,6.9c0,2.1-0.9,4-2.3,5.3c0,0,0,0,0,0
 41  			c3.8,6.1,10.5,10.2,18.1,10.2c11.8,0,21.3-9.6,21.3-21.3C444.8,338.7,435.2,329.2,423.4,329.2z"/>
 42  		<path fill="#0088CE" d="M237.3,364.1c-2.3,4-4.3,7.8-6.3,11.6l13.3,1.7c2.1-3.7,4.3-7.6,6.7-11.6L237.3,364.1L237.3,364.1z"/>
 43  		<path fill="#0088CE" d="M258.6,353.6c0.8-1.3,1.7-2.6,2.6-3.9L247,348c-0.9,1.4-1.8,2.8-2.7,4.2v0L258.6,353.6L258.6,353.6z"/>
 44  		<path fill="#0088CE" d="M382.5,352.2c-0.9-1.5-1.9-3-2.8-4.4l-14.2,1.8c0.9,1.4,1.9,2.8,2.7,4.1l0,0c0,0,0,0,0,0L382.5,352.2
 45  			L382.5,352.2z"/>
 46  		<path fill="#0088CE" d="M375.8,365.8C375.8,365.8,375.8,365.8,375.8,365.8c2.3,3.9,4.5,7.7,6.6,11.3l13.3-1.7
 47  			c-1.9-3.7-4-7.5-6.2-11.4L375.8,365.8z"/>
 48  		<path fill="#0088CE" d="M269.2,402.6c-6.9,0-12.5,5.6-12.5,12.5c0,1.5,0.3,2.9,0.7,4.2c0,0,0,0,0,0c0.2,0,0.5-0.1,0.7-0.1
 49  			c2.9,0,5.3,2.4,5.3,5.3c0,0.5-0.1,1-0.2,1.5c0,0,0,0-0.1,0c1.8,1,3.8,1.5,6,1.5c6.9,0,12.5-5.6,12.5-12.5
 50  			C281.7,408.2,276.1,402.6,269.2,402.6z"/>
 51  	</g>
 52  </g>
 53  <g>
 54  	<path fill="#00B9E4" d="M189.1,535.6l-3.9-7.9h-4.4v7.9h-4.4v-22h10.2c1,0,2,0.1,2.9,0.4c0.9,0.3,1.7,0.7,2.4,1.3
 55  		c0.7,0.6,1.2,1.3,1.6,2.2c0.4,0.9,0.6,1.9,0.6,3.1c0,1.7-0.4,3-1.1,4.1c-0.7,1.1-1.8,1.9-3.2,2.4l4.2,8.5H189.1z M188.8,518.6
 56  		c-0.6-0.4-1.3-0.6-2.3-0.6h-5.8v5.6h5.8c2.1,0,3.2-0.9,3.2-2.8C189.7,519.8,189.4,519,188.8,518.6z"/>
 57  	<path fill="#00B9E4" d="M199.7,535.6v-22H215v4.3h-10.9v3.8h6.3v4.3h-6.3v5.3h11.3v4.3H199.7z"/>
 58  	<path fill="#00B9E4" d="M237.9,529.6c-0.6,1.4-1.5,2.5-2.5,3.4c-1.1,0.9-2.3,1.5-3.6,2c-1.3,0.4-2.7,0.6-4.1,0.6h-6.6v-22h6.9
 59  		c1.6,0,3,0.2,4.3,0.6c1.3,0.4,2.5,1,3.5,1.9c1,0.9,1.7,2,2.3,3.4c0.6,1.4,0.8,3.1,0.8,5.1C238.9,526.6,238.6,528.2,237.9,529.6z
 60  		 M232.8,519.6c-1-1.1-2.7-1.7-5-1.7h-2.3v13.4h2.2c1.2,0,2.2-0.2,3-0.5c0.9-0.3,1.5-0.8,2.1-1.4c0.5-0.6,1-1.3,1.2-2.1
 61  		c0.3-0.8,0.4-1.7,0.4-2.7C234.4,522.4,233.9,520.8,232.8,519.6z"/>
 62  	<path fill="#00B9E4" d="M267.7,535.6v-9.2h-9v9.2h-4.4v-22h4.4v8.4h9v-8.4h4.4v22H267.7z"/>
 63  	<path fill="#00B9E4" d="M293.3,535.6l-1.7-4.9h-8l-1.7,4.9h-4.7l8.4-22h4.3l8.4,22H293.3z M288.7,522.6c-0.2-0.6-0.4-1.3-0.6-1.9
 64  		c-0.2-0.6-0.4-1.1-0.5-1.5c-0.1,0.4-0.3,0.9-0.5,1.5c-0.2,0.6-0.4,1.2-0.6,1.9l-1.4,4h5L288.7,522.6z"/>
 65  	<path fill="#00B9E4" d="M309.4,518v17.7h-4.4V518h-6.3v-4.3h17v4.3H309.4z"/>
 66  	<path fill="#00B9E4" d="M345.6,535.6l-1.7-4.9h-8l-1.7,4.9h-4.7l8.4-22h4.3l8.4,22H345.6z M341,522.6c-0.2-0.6-0.4-1.3-0.6-1.9
 67  		c-0.2-0.6-0.4-1.1-0.5-1.5c-0.1,0.4-0.3,0.9-0.5,1.5c-0.2,0.6-0.4,1.2-0.6,1.9l-1.4,4h5L341,522.6z"/>
 68  	<path fill="#00B9E4" d="M361.8,518v17.7h-4.4V518h-6.3v-4.3h17v4.3H361.8z"/>
 69  	<path fill="#00B9E4" d="M389.7,529.4c-0.5,1.4-1.1,2.6-2,3.6c-0.9,1-1.9,1.7-3.1,2.2c-1.2,0.5-2.5,0.8-3.9,0.8
 70  		c-1.4,0-2.8-0.3-3.9-0.8c-1.2-0.5-2.2-1.3-3-2.2c-0.8-1-1.5-2.2-2-3.5c-0.5-1.4-0.7-3-0.7-4.8c0-1.8,0.2-3.4,0.7-4.8
 71  		c0.5-1.4,1.1-2.6,2-3.6c0.9-1,1.9-1.7,3.1-2.2c1.2-0.5,2.5-0.8,4-0.8c1.4,0,2.7,0.3,3.9,0.8c1.2,0.5,2.2,1.3,3,2.2
 72  		c0.8,1,1.5,2.2,2,3.5c0.5,1.4,0.7,3,0.7,4.8C390.4,526.4,390.1,528,389.7,529.4z M384.4,519.5c-1-1.2-2.2-1.8-3.8-1.8
 73  		c-1.5,0-2.8,0.6-3.7,1.8c-0.9,1.2-1.4,2.9-1.4,5.1c0,2.2,0.5,4,1.4,5.2c1,1.2,2.2,1.8,3.8,1.8c1.5,0,2.8-0.6,3.7-1.8
 74  		c0.9-1.2,1.4-2.9,1.4-5.1C385.9,522.5,385.4,520.7,384.4,519.5z"/>
 75  	<path fill="#00B9E4" d="M411.9,535.6v-8.1c0-0.3,0-0.7,0-1.1c0-0.5,0-0.9,0-1.4c0-0.5,0-0.9,0-1.4c0-0.4,0-0.7,0-0.9
 76  		c-0.2,0.4-0.4,1-0.7,1.7c-0.3,0.7-0.6,1.4-0.9,2l-4.5,9.8l-4.4-9.8c-0.3-0.6-0.6-1.3-0.9-2c-0.3-0.7-0.5-1.2-0.7-1.7
 77  		c0,0.2,0,0.5,0,0.9c0,0.4,0,0.9,0,1.4c0,0.5,0,1,0,1.4c0,0.5,0,0.8,0,1.1v8.1h-4.3v-22h4.2l4.6,10c0.1,0.3,0.3,0.6,0.4,1
 78  		s0.3,0.7,0.4,1c0.1,0.3,0.3,0.6,0.4,0.9c0.1,0.3,0.2,0.5,0.3,0.7c0.1-0.4,0.4-1,0.6-1.7c0.3-0.7,0.6-1.4,0.9-2l4.4-10h4.3v22H411.9
 79  		z"/>
 80  	<path fill="#00B9E4" d="M423.2,535.6v-22h4.4v22H423.2z"/>
 81  	<path fill="#00B9E4" d="M447.1,520.1c-0.4-0.8-0.9-1.3-1.6-1.8c-0.6-0.4-1.5-0.6-2.5-0.6c-0.8,0-1.5,0.2-2.2,0.5s-1.2,0.8-1.6,1.4
 82  		c-0.4,0.6-0.8,1.3-1,2.2c-0.2,0.9-0.3,1.8-0.3,2.8c0,1,0.1,1.9,0.3,2.7c0.2,0.8,0.6,1.6,1,2.2c0.4,0.6,1,1.1,1.6,1.5
 83  		c0.6,0.4,1.4,0.5,2.2,0.5c1,0,1.8-0.2,2.5-0.7c0.6-0.4,1.3-1.2,1.8-2.1l3.7,2.2c-0.8,1.6-1.8,2.8-3.1,3.7c-1.3,0.9-3,1.3-5,1.3
 84  		c-1.4,0-2.8-0.3-3.9-0.8c-1.2-0.5-2.2-1.3-3-2.3c-0.9-1-1.5-2.2-2-3.6c-0.5-1.4-0.7-3-0.7-4.7c0-1.7,0.2-3.2,0.7-4.6
 85  		c0.5-1.4,1.2-2.6,2-3.6c0.9-1,1.9-1.8,3.1-2.3c1.2-0.6,2.5-0.8,4-0.8c1,0,2,0.1,2.8,0.4c0.8,0.2,1.6,0.6,2.2,1s1.2,0.9,1.7,1.5
 86  		c0.5,0.6,0.9,1.3,1.3,2L447.1,520.1z"/>
 87  </g>
 88  </svg>

```
  * file:///opt/input/source/src/main/webapp/bower_components/patternfly/dist/img/logo-alt.svg
      * `beans_1_1.xsd`: In the root tag, replace the `version` attribute value with `3.0`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="utf-8"?>
  2  <!-- Generator: Adobe Illustrator 16.0.4, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
  3  <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
  4  <svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
  5  	 width="37px" height="35px" viewBox="0 0 37 35" enable-background="new 0 0 37 35" xml:space="preserve">
  6  <linearGradient id="SVGID_1_" gradientUnits="userSpaceOnUse" x1="231.8955" y1="-269.5547" x2="231.8955" y2="-301.7199" gradientTransform="matrix(1 0 0 -1 -213.5 -268.5)">
  7  	<stop  offset="0" style="stop-color:#60EFFF"/>
  8  	<stop  offset="1" style="stop-color:#1F89C7"/>
  9  </linearGradient>
 10  <path fill="url(#SVGID_1_)" d="M36.792,17.992L18.398,0L0,17.992l7.333,10.39l5.595-1.285l5.503,7.737l5.493-7.724l5.533,1.27
 11  	L36.792,17.992z M17.634,3.336L15.25,25.355l-4.549-6.205L17.634,3.336z M10.202,18.47l-2.833-3.866l9.743-11.833L10.202,18.47z
 12  	 M14.495,25.562L14.495,25.562l0.265,0.365l-1.52,0.348l-3.507-4.93l0.626-1.424L14.495,25.562z M18.396,3.044l2.395,23.345
 13  	l-2.4,3.288L16,26.389L18.396,3.044z M22.296,25.562l4.181-5.702l0.654,1.485l-3.517,4.944l-1.58-0.362l0.264-0.363L22.296,25.562z
 14  	 M21.542,25.355L19.189,3.318l6.946,15.77L21.542,25.355z M19.744,2.767l9.679,11.837l-2.787,3.802L19.744,2.767z M7.647,27.56
 15  	l-6.692-9.48L14.051,5.278l-7.605,9.302l3.417,4.661l-0.964,2.188l3.572,5.023L7.647,27.56z M18.432,33.573l-4.733-6.653
 16  	l1.528-0.352l3.162,4.351l3.173-4.351l1.592,0.367L18.432,33.573z M24.384,26.466l3.581-5.037l-0.99-2.248l3.372-4.6l-7.605-9.302
 17  	l13.095,12.801l-6.692,9.48L24.384,26.466z"/>
 18  </svg>

```
  * file:///opt/input/source/src/main/webapp/bower_components/patternfly/dist/img/brand.svg
      * `beans_1_1.xsd`: In the root tag, replace the `version` attribute value with `3.0`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="utf-8"?>
  2  <!-- Generator: Adobe Illustrator 16.0.4, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
  3  <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
  4  <svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
  5  	 width="270px" height="10px" viewBox="0 0 270 10" enable-background="new 0 0 270 10" xml:space="preserve">
  6  <g>
  7  	<g>
  8  		<path fill="#FFFFFF" d="M121.965,9.413h-4.883V0.656h4.883v0.903h-3.862V4.38h3.63v0.898h-3.63V8.5h3.862V9.413z"/>
  9  		<path fill="#FFFFFF" d="M130.988,9.413h-1.158l-4.789-7.352h-0.046c0.062,0.864,0.095,1.655,0.095,2.374v4.978h-0.94V0.656h1.15
 10  			l4.774,7.317h0.045c-0.006-0.107-0.022-0.453-0.051-1.041c-0.028-0.582-0.039-0.998-0.028-1.254V0.656h0.951v8.753h-0.003V9.413
 11  			L130.988,9.413z"/>
 12  		<path fill="#FFFFFF" d="M136.339,9.413h-1.018V1.561h-2.771V0.656h6.564v0.903h-2.771v7.852h-0.002v0.002H136.339z"/>
 13  		<path fill="#FFFFFF" d="M145.554,9.413h-4.877V0.656h4.877v0.903h-3.859V4.38h3.631v0.898h-3.631V8.5h3.859V9.413z"/>
 14  		<path fill="#FFFFFF" d="M148.761,5.769v3.641h-1.018V0.656h2.402c1.074,0,1.865,0.204,2.379,0.614
 15  			c0.514,0.412,0.771,1.032,0.771,1.858c0,1.156-0.586,1.94-1.764,2.349l2.383,3.934h-1.207l-2.121-3.645h-1.826V5.769
 16  			L148.761,5.769z M148.761,4.897h1.396c0.719,0,1.244-0.142,1.582-0.428c0.334-0.286,0.504-0.714,0.504-1.285
 17  			c0-0.582-0.17-0.997-0.512-1.254c-0.34-0.255-0.889-0.381-1.643-0.381h-1.324v3.349h-0.004V4.897z"/>
 18  		<path fill="#FFFFFF" d="M161.124,3.209c0,0.884-0.301,1.567-0.904,2.046c-0.605,0.477-1.475,0.714-2.6,0.714h-1.031v3.444h-1.016
 19  			V0.656h2.27C160.03,0.656,161.124,1.504,161.124,3.209z M156.589,5.092h0.92c0.898,0,1.555-0.146,1.959-0.435
 20  			c0.4-0.293,0.604-0.759,0.604-1.404c0-0.577-0.188-1.006-0.568-1.295c-0.381-0.279-0.973-0.423-1.773-0.423h-1.139v3.557H156.589z
 21  			"/>
 22  		<path fill="#FFFFFF" d="M164.22,5.769v3.641h-1.02V0.656h2.402c1.074,0,1.865,0.204,2.383,0.614
 23  			c0.512,0.412,0.771,1.032,0.771,1.858c0,1.156-0.588,1.94-1.762,2.349l2.379,3.934h-1.205l-2.119-3.645h-1.826v0.002H164.22z
 24  			 M164.22,4.897h1.395c0.719,0,1.244-0.142,1.582-0.428c0.334-0.286,0.504-0.714,0.504-1.285c0-0.582-0.17-0.997-0.51-1.254
 25  			c-0.34-0.255-0.887-0.381-1.645-0.381h-1.322v3.349h-0.004V4.897z"/>
 26  		<path fill="#FFFFFF" d="M171.03,9.413V0.656h1.018v8.753h-1.018V9.413z"/>
 27  		<path fill="#FFFFFF" d="M179.636,7.081c0,0.773-0.281,1.374-0.838,1.805c-0.561,0.434-1.318,0.646-2.277,0.646
 28  			c-1.039,0-1.836-0.134-2.395-0.4V8.147c0.357,0.152,0.75,0.272,1.174,0.357c0.422,0.088,0.844,0.131,1.258,0.131
 29  			c0.68,0,1.188-0.129,1.531-0.384c0.346-0.257,0.514-0.62,0.514-1.073c0-0.304-0.061-0.556-0.184-0.748
 30  			c-0.119-0.194-0.318-0.375-0.607-0.537c-0.285-0.162-0.721-0.351-1.301-0.558c-0.816-0.29-1.398-0.636-1.748-1.036
 31  			c-0.352-0.398-0.525-0.92-0.525-1.562c0-0.674,0.254-1.211,0.764-1.611c0.508-0.398,1.178-0.599,2.014-0.599
 32  			c0.869,0,1.672,0.161,2.398,0.48l-0.316,0.884c-0.725-0.3-1.428-0.454-2.109-0.454c-0.539,0-0.959,0.114-1.266,0.347
 33  			c-0.303,0.231-0.453,0.553-0.453,0.965c0,0.305,0.057,0.551,0.168,0.745c0.115,0.195,0.303,0.372,0.566,0.533
 34  			c0.268,0.161,0.672,0.34,1.221,0.535c0.92,0.327,1.551,0.679,1.896,1.056C179.462,5.995,179.636,6.483,179.636,7.081z"/>
 35  		<path fill="#FFFFFF" d="M186.556,9.413h-4.881V0.656h4.881v0.903h-3.863V4.38h3.633v0.898h-3.633V8.5h3.863V9.413z"/>
 36  		<path fill="#FFFFFF" d="M197.677,9.413l-1.09-2.785h-3.51l-1.078,2.785h-1.031l3.463-8.793h0.854l3.443,8.793H197.677z
 37  			 M196.267,5.71l-1.018-2.712c-0.131-0.345-0.271-0.766-0.406-1.263c-0.09,0.383-0.211,0.804-0.377,1.263l-1.031,2.712H196.267z"/>
 38  		<path fill="#FFFFFF" d="M205.733,3.209c0,0.884-0.303,1.567-0.908,2.046c-0.607,0.477-1.473,0.714-2.596,0.714h-1.031v3.444
 39  			h-1.021V0.656h2.273C204.642,0.656,205.733,1.504,205.733,3.209z M201.2,5.092h0.914c0.902,0,1.557-0.146,1.961-0.435
 40  			c0.398-0.293,0.605-0.759,0.605-1.404c0-0.577-0.189-1.006-0.57-1.295c-0.381-0.279-0.969-0.423-1.773-0.423H201.2V5.092
 41  			L201.2,5.092z"/>
 42  		<path fill="#FFFFFF" d="M213.366,3.209c0,0.884-0.307,1.567-0.908,2.046c-0.607,0.477-1.473,0.714-2.598,0.714h-1.031v3.444h-1.02
 43  			V0.656h2.271C212.269,0.656,213.366,1.504,213.366,3.209z M208.827,5.092h0.918c0.904,0,1.559-0.146,1.959-0.435
 44  			c0.404-0.293,0.604-0.759,0.604-1.404c0-0.577-0.188-1.006-0.566-1.295c-0.381-0.279-0.971-0.423-1.773-0.423h-1.141V5.092
 45  			L208.827,5.092z"/>
 46  		<path fill="#FFFFFF" d="M215.44,9.413V0.656h1.021v7.832h3.857V9.41h-4.879V9.413z"/>
 47  		<path fill="#FFFFFF" d="M222.052,9.413V0.656h1.021v8.753h-1.021V9.413z"/>
 48  		<path fill="#FFFFFF" d="M229.466,1.44c-0.959,0-1.721,0.32-2.279,0.959c-0.557,0.642-0.834,1.518-0.834,2.633
 49  			c0,1.146,0.27,2.031,0.807,2.656c0.537,0.621,1.303,0.937,2.299,0.937c0.611,0,1.309-0.108,2.09-0.327v0.891
 50  			c-0.605,0.229-1.355,0.343-2.244,0.343c-1.289,0-2.285-0.396-2.988-1.181c-0.699-0.776-1.051-1.891-1.051-3.333
 51  			c0-0.902,0.17-1.69,0.506-2.371c0.336-0.678,0.824-1.202,1.461-1.569s1.387-0.551,2.248-0.551c0.918,0,1.719,0.168,2.408,0.504
 52  			l-0.432,0.875C230.798,1.594,230.13,1.44,229.466,1.44z"/>
 53  		<path fill="#FFFFFF" d="M239.204,9.413l-1.09-2.785h-3.512l-1.074,2.785h-1.031l3.459-8.793h0.857l3.445,8.793H239.204z
 54  			 M237.798,5.71l-1.018-2.712c-0.133-0.345-0.27-0.766-0.406-1.263c-0.088,0.383-0.215,0.804-0.377,1.263l-1.033,2.712H237.798z"/>
 55  		<path fill="#FFFFFF" d="M244.401,9.413h-1.016V1.561h-2.773V0.656h6.564v0.903h-2.771v7.852h-0.004V9.413z"/>
 56  		<path fill="#FFFFFF" d="M248.743,9.413V0.656h1.018v8.753h-1.018V9.413z"/>
 57  		<path fill="#FFFFFF" d="M260.005,5.021c0,1.402-0.354,2.503-1.062,3.305c-0.707,0.806-1.691,1.206-2.955,1.206
 58  			c-1.291,0-2.285-0.396-2.988-1.186c-0.699-0.789-1.051-1.901-1.051-3.338c0-1.424,0.354-2.532,1.057-3.312
 59  			c0.699-0.785,1.703-1.18,2.99-1.18c1.262,0,2.24,0.399,2.951,1.2C259.655,2.513,260.005,3.614,260.005,5.021z M253.03,5.021
 60  			c0,1.186,0.25,2.085,0.754,2.697c0.508,0.613,1.242,0.922,2.203,0.922c0.973,0,1.705-0.311,2.201-0.918
 61  			c0.494-0.615,0.738-1.516,0.738-2.702c0-1.179-0.244-2.072-0.736-2.681c-0.49-0.61-1.223-0.914-2.189-0.914
 62  			c-0.969,0-1.705,0.306-2.213,0.918C253.282,2.96,253.03,3.851,253.03,5.021z"/>
 63  		<path fill="#FFFFFF" d="M269.044,9.413h-1.162l-4.783-7.352h-0.049c0.061,0.864,0.094,1.655,0.094,2.374v4.978H262.2V0.656h1.152
 64  			l4.771,7.319h0.049c-0.012-0.108-0.025-0.455-0.055-1.041c-0.027-0.582-0.041-0.998-0.029-1.256V0.656h0.951v8.755h0.006v0.002
 65  			H269.044z"/>
 66  	</g>
 67  	<g>
 68  		<path fill="#FFFFFF" d="M7.533,3.368c0,1.013-0.298,1.796-0.896,2.348C6.04,6.269,5.191,6.544,4.093,6.544H3.403v3.008H0.954
 69  			V0.485h3.139c1.145,0,2.005,0.25,2.58,0.75C7.246,1.736,7.533,2.447,7.533,3.368z M3.403,4.547h0.447
 70  			c0.368,0,0.66-0.103,0.877-0.31s0.326-0.492,0.326-0.856c0-0.612-0.339-0.918-1.018-0.918H3.403V4.547z"/>
 71  		<path fill="#FFFFFF" d="M17.652,9.552l-0.446-1.699h-2.944l-0.459,1.699h-2.691l2.958-9.104h3.268l2.995,9.104H17.652z
 72  			 M16.697,5.843l-0.39-1.489c-0.092-0.33-0.202-0.758-0.333-1.283c-0.13-0.525-0.216-0.901-0.257-1.128
 73  			c-0.037,0.211-0.111,0.558-0.221,1.042c-0.108,0.483-0.353,1.437-0.729,2.857H16.697z"/>
 74  		<path fill="#FFFFFF" d="M28.423,9.552h-2.449V2.488H23.76V0.485h6.871v2.003h-2.208V9.552z"/>
 75  		<path fill="#FFFFFF" d="M39.037,9.552h-2.449V2.488h-2.214V0.485h6.871v2.003h-2.208V9.552z"/>
 76  		<path fill="#FFFFFF" d="M51.035,9.552h-5.382V0.485h5.382V2.45h-2.933v1.427h2.716v1.966h-2.716v1.711h2.933V9.552z"/>
 77  		<path fill="#FFFFFF" d="M58.184,6.253v3.299h-2.449V0.485h2.97c2.464,0,3.696,0.893,3.696,2.679c0,1.05-0.513,1.862-1.538,2.437
 78  			l2.642,3.951h-2.777l-1.922-3.299H58.184z M58.184,4.41h0.459c0.855,0,1.284-0.378,1.284-1.135c0-0.625-0.42-0.937-1.26-0.937
 79  			h-0.483V4.41z"/>
 80  		<path fill="#FFFFFF" d="M76.072,9.552H72.86L69.55,3.164h-0.057c0.079,1.004,0.118,1.771,0.118,2.301v4.086h-2.17V0.485h3.2
 81  			l3.299,6.301h0.037c-0.059-0.914-0.086-1.648-0.086-2.202V0.485h2.183v9.066H76.072z"/>
 82  		<path fill="#FFFFFF" d="M83.557,9.552h-2.412V0.485h5.356V2.45h-2.944v1.73h2.716v1.965h-2.716V9.552z"/>
 83  		<path fill="#FFFFFF" d="M91.102,9.552V0.485h2.449v7.088h3.49v1.979H91.102z"/>
 84  		<path fill="#FFFFFF" d="M104.842,3.846l1.562-3.361h2.654l-2.983,5.525v3.541h-2.468V6.085l-2.983-5.6h2.667L104.842,3.846z"/>
 85  	</g>
 86  </g>
 87  </svg>

```
  * file:///opt/input/source/src/main/webapp/bower_components/patternfly/dist/img/bg-navbar-pf-alt.svg
      * `beans_1_1.xsd`: In the root tag, replace the `version` attribute value with `3.0`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="utf-8"?>
  2  <!-- Generator: Adobe Illustrator 16.0.4, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
  3  <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
  4  <svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
  5  	 width="615.598px" height="57px" viewBox="25.562 0 615.598 57" enable-background="new 25.562 0 615.598 57" xml:space="preserve"
  6  	>
  7  <polygon opacity="0.1" fill="#FFFFFF" enable-background="new    " points="566.242,56.969 623.205,0 641.16,0 584.68,56.969 "/>
  8  <polygon opacity="0.1" fill="#FFFFFF" enable-background="new    " points="25.562,57 25.562,0 611.034,0 554.554,56.95 "/>
  9  </svg>

```
  * file:///opt/input/source/src/main/webapp/bower_components/patternfly/dist/img/brand-alt.svg
      * `beans_1_1.xsd`: In the root tag, replace the `version` attribute value with `3.0`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="utf-8"?>
  2  <!-- Generator: Adobe Illustrator 16.0.4, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
  3  <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
  4  <svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
  5  	 width="324px" height="11px" viewBox="1.145 0.538 324 11" enable-background="new 1.145 0.538 324 11" xml:space="preserve">
  6  <g>
  7  	<g>
  8  		<path fill="#FFFFFF" d="M147.351,11.368h-5.899V0.789h5.899V1.88h-4.666v3.408h4.386v1.085h-4.386v3.894h4.666V11.368z"/>
  9  		<path fill="#FFFFFF" d="M158.252,11.368h-1.399l-5.786-8.882h-0.056c0.075,1.044,0.115,2,0.115,2.868v6.014h-1.136V0.789h1.39
 10  			l5.768,8.84h0.054c-0.007-0.129-0.027-0.548-0.062-1.258c-0.034-0.702-0.047-1.205-0.034-1.515V0.789h1.149v10.576h-0.004V11.368
 11  			L158.252,11.368z"/>
 12  		<path fill="#FFFFFF" d="M164.719,11.368h-1.23V1.882h-3.349V0.789h7.932V1.88h-3.349v9.486h-0.002v0.002H164.719z"/>
 13  		<path fill="#FFFFFF" d="M175.852,11.368h-5.893V0.789h5.893V1.88h-4.662v3.408h4.386v1.085h-4.386v3.894h4.662V11.368z"/>
 14  		<path fill="#FFFFFF" d="M179.727,6.967v4.398h-1.231V0.789h2.903c1.298,0,2.253,0.247,2.875,0.742
 15  			c0.62,0.498,0.931,1.247,0.931,2.245c0,1.396-0.708,2.344-2.131,2.838l2.879,4.753h-1.459l-2.562-4.403h-2.206v0.004H179.727z
 16  			 M179.727,5.913h1.687c0.868,0,1.503-0.172,1.911-0.517c0.404-0.346,0.608-0.863,0.608-1.553c0-0.703-0.204-1.205-0.618-1.515
 17  			c-0.41-0.308-1.075-0.46-1.985-0.46h-1.6v4.046h-0.005V5.913H179.727z"/>
 18  		<path fill="#FFFFFF" d="M194.663,3.873c0,1.068-0.363,1.894-1.093,2.473c-0.73,0.576-1.781,0.861-3.141,0.861h-1.246v4.161h-1.228
 19  			V0.789h2.743C193.342,0.789,194.663,1.813,194.663,3.873z M189.184,6.148h1.111c1.085,0,1.88-0.176,2.367-0.525
 20  			c0.483-0.354,0.729-0.917,0.729-1.696c0-0.697-0.227-1.216-0.687-1.565c-0.46-0.337-1.175-0.511-2.142-0.511h-1.376v4.298H189.184
 21  			z"/>
 22  		<path fill="#FFFFFF" d="M198.404,6.967v4.398h-1.233V0.789h2.902c1.298,0,2.254,0.247,2.879,0.742
 23  			c0.619,0.498,0.933,1.247,0.933,2.245c0,1.396-0.711,2.344-2.13,2.838l2.875,4.753h-1.456l-2.561-4.403h-2.206v0.003
 24  			L198.404,6.967L198.404,6.967z M198.404,5.913h1.686c0.868,0,1.502-0.172,1.911-0.517c0.403-0.346,0.608-0.863,0.608-1.553
 25  			c0-0.703-0.205-1.205-0.616-1.515c-0.411-0.308-1.072-0.46-1.987-0.46h-1.598v4.046L198.404,5.913L198.404,5.913z"/>
 26  		<path fill="#FFFFFF" d="M206.632,11.368V0.789h1.229v10.576h-1.229V11.368z"/>
 27  		<path fill="#FFFFFF" d="M217.028,8.552c0,0.934-0.338,1.66-1.012,2.181c-0.677,0.524-1.592,0.78-2.751,0.78
 28  			c-1.256,0-2.218-0.162-2.894-0.482V9.84c0.431,0.184,0.906,0.329,1.418,0.432c0.51,0.105,1.021,0.157,1.521,0.157
 29  			c0.821,0,1.435-0.155,1.85-0.463c0.418-0.312,0.622-0.75,0.622-1.297c0-0.367-0.075-0.672-0.223-0.904
 30  			c-0.145-0.233-0.386-0.453-0.733-0.647c-0.345-0.197-0.871-0.425-1.572-0.675c-0.986-0.35-1.689-0.769-2.112-1.251
 31  			c-0.426-0.481-0.634-1.112-0.634-1.888c0-0.814,0.307-1.463,0.922-1.946c0.614-0.48,1.424-0.724,2.435-0.724
 32  			c1.05,0,2.02,0.195,2.897,0.58l-0.382,1.068c-0.876-0.362-1.726-0.548-2.549-0.548c-0.65,0-1.158,0.138-1.53,0.418
 33  			c-0.365,0.279-0.546,0.668-0.546,1.167c0,0.369,0.068,0.666,0.202,0.9c0.14,0.235,0.366,0.449,0.685,0.644
 34  			c0.323,0.194,0.812,0.411,1.475,0.646c1.111,0.395,1.874,0.82,2.291,1.276C216.819,7.239,217.028,7.829,217.028,8.552z"/>
 35  		<path fill="#FFFFFF" d="M225.391,11.368h-5.898V0.789h5.898V1.88h-4.668v3.408h4.391v1.085h-4.391v3.894h4.668V11.368z"/>
 36  		<path fill="#FFFFFF" d="M238.827,11.368l-1.317-3.364h-4.241l-1.303,3.364h-1.244l4.184-10.623h1.031l4.16,10.623H238.827z
 37  			 M237.123,6.895l-1.229-3.276c-0.159-0.417-0.328-0.926-0.491-1.526c-0.109,0.462-0.255,0.971-0.455,1.526l-1.246,3.276H237.123z"
 38  			/>
 39  		<path fill="#FFFFFF" d="M248.56,3.873c0,1.068-0.366,1.894-1.097,2.473c-0.733,0.576-1.779,0.861-3.137,0.861h-1.245v4.161h-1.233
 40  			V0.789h2.745C247.241,0.789,248.56,1.813,248.56,3.873z M243.083,6.148h1.104c1.09,0,1.881-0.176,2.37-0.525
 41  			c0.479-0.354,0.73-0.917,0.73-1.696c0-0.697-0.229-1.216-0.689-1.565c-0.46-0.337-1.17-0.511-2.142-0.511h-1.374V6.148
 42  			L243.083,6.148z"/>
 43  		<path fill="#FFFFFF" d="M257.782,3.873c0,1.068-0.371,1.894-1.098,2.473c-0.733,0.576-1.779,0.861-3.139,0.861h-1.245v4.161
 44  			h-1.232V0.789h2.743C256.457,0.789,257.782,1.813,257.782,3.873z M252.298,6.148h1.108c1.094,0,1.884-0.176,2.368-0.525
 45  			c0.487-0.354,0.729-0.917,0.729-1.696c0-0.697-0.228-1.216-0.685-1.565c-0.46-0.337-1.172-0.511-2.142-0.511H252.3v4.298H252.298z
 46  			"/>
 47  		<path fill="#FFFFFF" d="M260.287,11.368V0.789h1.235v9.463h4.659v1.113h-5.895V11.368L260.287,11.368z"/>
 48  		<path fill="#FFFFFF" d="M268.277,11.368V0.789h1.232v10.576h-1.232V11.368z"/>
 49  		<path fill="#FFFFFF" d="M277.234,1.736c-1.158,0-2.079,0.386-2.753,1.159c-0.674,0.776-1.009,1.833-1.009,3.181
 50  			c0,1.385,0.326,2.454,0.976,3.209c0.648,0.75,1.575,1.132,2.777,1.132c0.738,0,1.582-0.13,2.526-0.396v1.077
 51  			c-0.732,0.276-1.639,0.414-2.712,0.414c-1.558,0-2.761-0.479-3.61-1.427c-0.844-0.938-1.27-2.284-1.27-4.027
 52  			c0-1.089,0.205-2.042,0.61-2.865c0.407-0.819,0.996-1.452,1.766-1.896c0.77-0.444,1.676-0.666,2.716-0.666
 53  			c1.109,0,2.077,0.203,2.909,0.609l-0.521,1.057C278.843,1.922,278.037,1.736,277.234,1.736z"/>
 54  		<path fill="#FFFFFF" d="M289,11.368l-1.317-3.364h-4.243l-1.298,3.364h-1.245l4.18-10.623h1.035l4.162,10.623H289z M287.301,6.895
 55  			l-1.229-3.276c-0.162-0.417-0.327-0.926-0.492-1.526c-0.106,0.462-0.26,0.971-0.455,1.526l-1.248,3.276H287.301z"/>
 56  		<path fill="#FFFFFF" d="M295.279,11.368h-1.228V1.882h-3.351V0.789h7.931V1.88h-3.348v9.486h-0.005V11.368z"/>
 57  		<path fill="#FFFFFF" d="M300.525,11.368V0.789h1.229v10.576h-1.229V11.368z"/>
 58  		<path fill="#FFFFFF" d="M314.132,6.063c0,1.693-0.428,3.024-1.283,3.993c-0.854,0.975-2.043,1.457-3.57,1.457
 59  			c-1.56,0-2.761-0.479-3.61-1.433c-0.844-0.953-1.27-2.297-1.27-4.033c0-1.721,0.428-3.06,1.277-4.002
 60  			c0.844-0.948,2.057-1.426,3.612-1.426c1.525,0,2.706,0.482,3.565,1.45C313.709,3.033,314.132,4.363,314.132,6.063z M305.705,6.063
 61  			c0,1.432,0.301,2.519,0.91,3.258c0.614,0.74,1.501,1.114,2.662,1.114c1.175,0,2.06-0.377,2.658-1.109
 62  			c0.598-0.743,0.893-1.832,0.893-3.265c0-1.424-0.295-2.503-0.89-3.239c-0.592-0.737-1.478-1.104-2.645-1.104
 63  			c-1.17,0-2.06,0.37-2.675,1.109C306.009,3.572,305.705,4.649,305.705,6.063z"/>
 64  		<path fill="#FFFFFF" d="M325.053,11.368h-1.404l-5.778-8.882h-0.06c0.074,1.044,0.113,2,0.113,2.868v6.014h-1.141V0.789h1.393
 65  			l5.765,8.843h0.059c-0.015-0.131-0.03-0.551-0.066-1.259c-0.032-0.701-0.05-1.205-0.034-1.517V0.789h1.148v10.578h0.008v0.002
 66  			H325.053z"/>
 67  	</g>
 68  	<g>
 69  		<path fill="#FFFFFF" d="M9.094,4.065c0,1.224-0.36,2.17-1.083,2.837C7.29,7.571,6.264,7.903,4.938,7.903H4.104v3.634H1.145V0.583
 70  			h3.792c1.383,0,2.422,0.302,3.117,0.906C8.747,2.094,9.094,2.953,9.094,4.065z M4.104,5.49h0.541c0.444,0,0.797-0.125,1.059-0.375
 71  			c0.262-0.25,0.394-0.595,0.394-1.035c0-0.739-0.41-1.109-1.23-1.109H4.104V5.49z"/>
 72  		<path fill="#FFFFFF" d="M21.32,11.537l-0.54-2.053h-3.557l-0.555,2.053h-3.251l3.573-11h3.949l3.619,11H21.32z M20.166,7.056
 73  			l-0.472-1.799c-0.111-0.399-0.244-0.916-0.402-1.55c-0.157-0.634-0.261-1.088-0.311-1.363c-0.045,0.255-0.134,0.674-0.267,1.259
 74  			c-0.13,0.583-0.427,1.736-0.881,3.451h2.333V7.056z"/>
 75  		<path fill="#FFFFFF" d="M34.333,11.537h-2.959V3.002h-2.675V0.583h8.302v2.419h-2.668V11.537z"/>
 76  		<path fill="#FFFFFF" d="M47.157,11.537h-2.958V3.002h-2.675V0.583h8.301v2.419h-2.668V11.537z"/>
 77  		<path fill="#FFFFFF" d="M61.653,11.537H55.15V0.583h6.503v2.374h-3.544v1.724h3.281v2.375h-3.281v2.067h3.544V11.537z"/>
 78  		<path fill="#FFFFFF" d="M70.291,7.552v3.985h-2.959V0.583h3.588c2.977,0,4.466,1.079,4.466,3.237c0,1.268-0.62,2.25-1.858,2.943
 79  			l3.192,4.774h-3.355l-2.322-3.985H70.291z M70.291,5.325h0.554c1.033,0,1.552-0.457,1.552-1.371c0-0.755-0.508-1.132-1.522-1.132
 80  			h-0.583V5.325z"/>
 81  		<path fill="#FFFFFF" d="M91.903,11.537h-3.881l-3.999-7.718h-0.069c0.095,1.213,0.143,2.139,0.143,2.78v4.936h-2.622V0.583h3.866
 82  			l3.986,7.612h0.044c-0.071-1.103-0.104-1.99-0.104-2.659V0.583h2.637v10.953h-0.002V11.537z"/>
 83  		<path fill="#FFFFFF" d="M100.946,11.537h-2.914V0.583h6.471v2.374h-3.557v2.09h3.282v2.374h-3.282V11.537z"/>
 84  		<path fill="#FFFFFF" d="M110.062,11.537V0.583h2.959v8.564h4.217v2.391H110.062z"/>
 85  		<path fill="#FFFFFF" d="M126.663,4.643l1.887-4.061h3.207l-3.604,6.675v4.277h-2.982V7.348l-3.604-6.765h3.222L126.663,4.643z"/>
 86  	</g>
 87  </g>
 88  </svg>

```
  * file:///opt/input/source/src/main/webapp/bower_components/patternfly/dist/img/logo.svg
      * `beans_1_1.xsd`: In the root tag, replace the `version` attribute value with `3.0`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="utf-8"?>
  2  <!-- Generator: Adobe Illustrator 16.0.3, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
  3  <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
  4  <svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
  5  	 width="73px" height="69px" viewBox="0 0 73 69" enable-background="new 0 0 73 69" xml:space="preserve">
  6  <g>
  7  	<linearGradient id="SVGID_1_" gradientUnits="userSpaceOnUse" x1="36.2046" y1="2.1504" x2="36.2046" y2="68.6623">
  8  		<stop  offset="0" style="stop-color:#60EFFF"/>
  9  		<stop  offset="1" style="stop-color:#1F89C7"/>
 10  	</linearGradient>
 11  	<path fill="url(#SVGID_1_)" d="M36.287,0.137l0.008-0.063l-0.031,0.039l-0.012-0.012L36.262,0l-0.057,0.056L36.148,0l0.011,0.101
 12  		l-0.013,0.012l-0.03-0.039l0.007,0.063L0,35.447l14.307,20.267l11.05-2.538l10.848,15.255l10.85-15.255l11.05,2.538l8.861-12.554
 13  		l5.444-7.713L36.287,0.137z M35.108,4.282L30.174,50.52l-9.642-13.151L35.108,4.282z M20.059,36.725l-6.068-8.277L35.057,2.683
 14  		L20.059,36.725z M29.967,51.407l-4.313,0.99l-7.251-10.193l1.807-4.104L29.967,51.407z M36.092,2.051l0.113-0.258l0.114,0.257
 15  		l5.102,49.711l-0.015-0.01l-4.999,7.387l-5.409-7.396l-0.007,0.004L36.092,2.051z M42.237,50.521L37.303,4.281l14.576,33.087
 16  		L42.237,50.521z M52.201,38.101l1.808,4.104l-7.251,10.193l-4.312-0.99L52.201,38.101z M37.355,2.684L58.42,28.448l-6.067,8.277
 17  		L37.355,2.684z M14.605,54.935L0.907,35.53L32.779,4.374L13.114,28.425l6.623,9.03l-2.127,4.83l7.312,10.28L14.605,54.935z
 18  		 M36.205,67.235L26.086,53.009l4.326-0.992l0.072,0.099l-0.045,0.034l5.988,8.191l5.552-8.201l-0.048-0.032L42,52.017l4.324,0.992
 19  		L36.205,67.235z M66.4,42.762l-8.594,12.173l-10.317-2.369l7.312-10.28l-2.127-4.83l6.622-9.03L39.633,4.374L71.504,35.53
 20  		L66.4,42.762z"/>
 21  </g>
 22  </svg>

```
  * file:///opt/input/source/src/main/webapp/bower_components/patternfly/src/img/RH_Atomic-Logo-NoText.svg
      * `beans_1_1.xsd`: In the root tag, replace the `version` attribute value with `3.0`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="utf-8"?>
  2  <!-- Generator: Adobe Illustrator 19.2.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
  3  <svg version="1.1"
  4  	 id="svg4242" xmlns:cc="http://creativecommons.org/ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
  5  	 xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 200 199.7"
  6  	 style="enable-background:new 0 0 200 199.7;" xml:space="preserve">
  7  <style type="text/css">
  8  	.st0{fill:#00B9E4;}
  9  	.st1{fill:#0088CE;}
 10  </style>
 11  <g>
 12  	<g>
 13  		<path class="st0" d="M88.1,136.7c-0.4,0.3-0.7,0.6-1,0.8c-2.5,2.5-4.9,4.8-7.1,6.9c1.4,0.8,2.4,2.1,3,3.7c2.7-2.4,5.5-5,8.4-7.9
 14  			c0.6-0.6,1.1-2.2-0.1-3.3C90.4,136.2,89,136,88.1,136.7z"/>
 15  		<path class="st0" d="M60.3,77.4c0.7,1.1,2.2,1.5,3.3,0.7c1.2-0.8,1-2.4,0.6-2.9C54.5,58.7,50.1,46,54,43c2.4-1.9,7.6,0.2,14.5,5.3
 16  			c0.7-2.2,2.3-4,4.3-5c-11.1-8.3-19.9-11.8-24-8.6c-5.8,4.5-1,21.1,11.1,42.1C60,77,60.2,77.2,60.3,77.4z"/>
 17  		<path class="st0" d="M140.3,123.2c2.9-0.4,5.7-0.8,8.3-1.3l0,0l0,0l0,0c0.7-0.7,1.2-1.7,1.2-2.8c0-1.8-1.3-3.3-2.9-3.7l0,0
 18  			c-3.2,0.5-6.7,1-10.4,1.4l0,0l0,0c-5.7-9.3-12.7-19.4-20.6-29.5c-2.3-3.2-7.4-9.1-11.3-13.6l0.1-0.1C124,52.2,141,39.1,146,42.9
 19  			c3.8,3-0.5,15.6-10.3,32.2c-0.3,0.5-0.6,2.1,0.6,2.9c1.2,0.8,2.7,0.4,3.3-0.7c0.1-0.2,0.3-0.4,0.4-0.6c12-21,16.9-37.6,11.1-42.1
 20  			c-7-5.5-27.8,8.6-50.3,32.9c0,0-0.3,0.4-1,1.1c-0.6-0.6-1-1.1-1-1.1c-4.9-5.2-9.7-10.1-14.2-14.2l0,0c-0.1-0.1-0.1-0.1-0.1-0.1
 21  			c-0.2-0.1-0.4-0.1-0.6-0.1c-2.1,0-3.8,1.7-3.8,3.8c0,0.5,0.1,1.1,0.3,1.5l0,0c4.7,4.4,9.6,9.5,14.8,15.2l0.1,0.1
 22  			c-4,4.5-9,10.4-11.3,13.6c-7.9,10.1-14.9,20.1-20.6,29.5c-21.9-2.5-36.6-7.1-36.5-12.4c0-5.4,15.6-10.1,38.4-12.4
 23  			c0.3-0.1,0.4-0.1,0.7-0.1c1.2-0.2,1.9-1.4,1.8-2.3c0-1.2-0.9-2.4-2.6-2.4c-28.3,3.2-48,10.2-48,18.3c-0.1,7.6,17.2,14.2,42.6,17.7
 24  			c-11.9,20.9-16.7,37.3-10.9,41.8c4.2,3.3,13.3-0.4,24.7-9.1l0,0c0,0,0,0,0.1,0c0.1-0.3,0.1-0.5,0.1-0.8c0-1.5-1.3-2.8-2.8-2.8
 25  			c-0.2,0-0.3,0-0.4,0.1l0,0l0,0c-7.1,5.2-12.4,7.5-14.8,5.6c-4-3.1,0.8-16.4,11.4-33.8c9.8,1.1,20.7,1.6,32.1,1.7l0,0
 26  			c0.2,0,0.3,0,0.5,0l0,0l0,0c0.1,0,0.3,0,0.4,0l0,0h0.1l0,0h0.1c0.1,0,0.3,0,0.4,0c0.2,0,0.3,0,0.5,0l0,0
 27  			c11.4-0.1,22.3-0.6,32.1-1.7c10.5,17.5,15.4,30.8,11.4,33.8c-4.1,3.2-16.5-5.2-31.5-20.4c-0.3-0.3-0.6-0.6-1-0.8
 28  			c-1-0.7-2.3-0.5-3,0.2c-1.2,1.2-0.8,2.7-0.1,3.3c19.4,19.2,36.3,29.6,42.5,24.8C157,160.5,152.2,144.1,140.3,123.2L140.3,123.2z
 29  			 M100.3,118.8c-0.1,0-0.2,0-0.3,0s-0.2,0-0.3,0c-10.2,0-20-0.4-28.7-1.2c5.2-8.2,11.5-16.9,18.6-25.9c3.2-4,6.4-7.9,9.5-11.5l0,0
 30  			c0.3-0.4,0.6-0.7,0.9-1.1c0.3,0.4,0.6,0.7,0.9,1.1l0,0c3.1,3.7,6.3,7.5,9.5,11.5c7.1,9,13.3,17.8,18.6,25.9l0,0
 31  			C120.2,118.4,110.5,118.8,100.3,118.8z"/>
 32  		<path class="st0" d="M134.9,87.2c-1.7-0.1-2.6,1.2-2.6,2.4c-0.1,1,0.6,2.1,1.8,2.3c0.2,0.1,0.4,0.1,0.7,0.1
 33  			c22.8,2.4,38.3,7,38.4,12.4c0,1.9-1.9,3.7-5.4,5.4c1.1,1.7,1.8,3.9,1.8,6.1c0,0.2,0,0.4-0.1,0.5c8.5-3.2,13.3-7,13.3-11
 34  			C182.9,97.3,163.2,90.4,134.9,87.2z"/>
 35  	</g>
 36  	<g>
 37  		<path class="st1" d="M76.6,42.4c-4.7,0-8.6,3.8-8.6,8.6c0,4.7,3.8,8.6,8.6,8.6c1.4,0,2.8-0.4,3.9-1c-0.2-0.5-0.3-1-0.3-1.5
 38  			c0-2.1,1.7-3.8,3.8-3.8c0.2,0,0.4,0,0.6,0.1c0.1,0.1,0.1,0.1,0.1,0.1c0.2-0.8,0.4-1.6,0.4-2.4C85.2,46.2,81.4,42.4,76.6,42.4z"/>
 39  		<path class="st1" d="M99.1,67.6c-0.4-0.4-0.7-0.8-1.2-1.2l-4.4,5.3c0.6,0.7,1.3,1.4,1.9,2.1l0.1,0.1c1.9-2.2,3.6-4.1,4.6-5.2
 40  			C99.4,68,99.1,67.6,99.1,67.6z"/>
 41  		<path class="st1" d="M100,79.1L100,79.1c0.3,0.4,0.6,0.7,0.9,1.1l0,0c1,1.2,2,2.3,3,3.5l4.6-5.4c-1.3-1.5-2.6-3-3.8-4.4L100,79.1z
 42  			"/>
 43  		<path class="st1" d="M158.3,104.7c-6,0-11,4.8-11.3,10.7c1.7,0.4,2.9,1.9,2.9,3.7c0,1.1-0.5,2.1-1.2,2.8l0,0
 44  			c2,3.2,5.6,5.4,9.6,5.4c6.2,0,11.3-5.1,11.3-11.3C169.6,109.7,164.5,104.7,158.3,104.7z"/>
 45  		<path class="st1" d="M59.7,123.2c-1.2,2.1-2.3,4.1-3.3,6.1l7,0.9c1.1-2,2.3-4,3.5-6.1L59.7,123.2L59.7,123.2z"/>
 46  		<path class="st1" d="M71,117.6c0.4-0.7,0.9-1.4,1.4-2.1l-7.5-0.9c-0.5,0.7-1,1.5-1.4,2.2l0,0L71,117.6L71,117.6z"/>
 47  		<path class="st1" d="M136.6,116.9c-0.5-0.8-1-1.6-1.5-2.3l-7.5,1c0.5,0.7,1,1.5,1.4,2.2l0,0l0,0L136.6,116.9L136.6,116.9z"/>
 48  		<path class="st1" d="M133.1,124.1L133.1,124.1c1.2,2.1,2.4,4.1,3.5,6l7-0.9c-1-2-2.1-4-3.3-6L133.1,124.1z"/>
 49  		<path class="st1" d="M76.6,143.5c-3.7,0-6.6,3-6.6,6.6c0,0.8,0.2,1.5,0.4,2.2l0,0c0.1,0,0.3-0.1,0.4-0.1c1.5,0,2.8,1.3,2.8,2.8
 50  			c0,0.3-0.1,0.5-0.1,0.8c0,0,0,0-0.1,0c1,0.5,2,0.8,3.2,0.8c3.7,0,6.6-3,6.6-6.6C83.2,146.5,80.3,143.5,76.6,143.5z"/>
 51  	</g>
 52  </g>
 53  </svg>

```
  * file:///opt/input/source/src/main/webapp/bower_components/patternfly/src/img/OpenShift-Logo-Text.svg
      * `beans_1_1.xsd`: In the root tag, replace the `version` attribute value with `3.0`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="utf-8"?>
  2  <!-- Generator: Adobe Illustrator 19.2.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
  3  <svg version="1.1"
  4  	 id="svg4242" xmlns:cc="http://creativecommons.org/ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
  5  	 xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 200 199.7"
  6  	 style="enable-background:new 0 0 200 199.7;" xml:space="preserve">
  7  <style type="text/css">
  8  	.st0{fill:#C32034;}
  9  	.st1{fill:#DB212F;}
 10  	.st2{fill:#EA2227;}
 11  	.st3{fill:#AD213A;}
 12  	.st4{fill:#BA2034;}
 13  	.st5{fill:#231F20;}
 14  </style>
 15  <g>
 16  	<g id="g3921">
 17  		<g id="g3927" transform="translate(304.96 416.03)">
 18  			<path id="path3929" class="st0" d="M-238.7-345.3l-23.3,8.5c0.3,3.8,0.9,7.5,1.9,11.1l22.1-8C-238.7-337.7-239-341.5-238.7-345.3
 19  				"/>
 20  		</g>
 21  		<g id="g3931" transform="translate(418.75 444.5)">
 22  			<path id="path3933" class="st0" d="M-249.5-399.6c-1.6-3.3-3.5-6.6-5.6-9.6l-23.3,8.5c2.7,2.8,5,5.9,6.9,9.2
 23  				C-271.7-391.6-249.5-399.6-249.5-399.6z"/>
 24  		</g>
 25  		<g id="g3935" transform="translate(362.11 451.79)">
 26  			<path id="path3937" class="st1" d="M-244.2-413.5c4.8,2.2,9,5.4,12.6,9l23.3-8.5c-6.4-9-15.3-16.6-26-21.6
 27  				c-33.3-15.5-73-1.1-88.5,32.2c-5,10.8-6.9,22.2-6,33.3l23.3-8.5c0.4-5.1,1.6-10.1,3.9-15C-291.6-414.2-265.8-423.5-244.2-413.5"
 28  				/>
 29  		</g>
 30  		<g id="g3939" transform="translate(282.86 395.05)">
 31  			<path id="path3941" class="st2" d="M-236.6-305.4l-22.1,8c2,8,5.6,15.7,10.4,22.6l23.2-8.5C-231-289.4-235-297.1-236.6-305.4"/>
 32  		</g>
 33  		<g id="g3943" transform="translate(389.56 404.75)">
 34  			<path id="path3945" class="st1" d="M-246.7-323.9c-0.4,5.1-1.7,10.1-3.9,15c-10.1,21.6-35.9,31.1-57.5,20.9
 35  				c-4.8-2.2-9-5.4-12.6-9l-23.2,8.5c6.4,9,15.2,16.6,26,21.6c33.3,15.5,73,1.1,88.5-32.2c5-10.8,6.9-22.2,6-33.3L-246.7-323.9
 36  				L-246.7-323.9z"/>
 37  		</g>
 38  		<g id="g3947" transform="translate(395.89 436.18)">
 39  			<path id="path3949" class="st2" d="M-247.3-383.8l-22.1,8c4.1,7.4,6.1,15.9,5.4,24.4l23.2-8.5
 40  				C-241.5-368.1-243.7-376.2-247.3-383.8"/>
 41  		</g>
 42  		<g id="g3951" transform="translate(279.22 406.66)">
 43  			<path id="path3953" class="st3" d="M-236.2-327.6l23.2-8.4l-0.1,4.6l-22.4,8.3C-235.5-323-236.2-327.6-236.2-327.6z"/>
 44  		</g>
 45  		<g id="g3955" transform="translate(386.73 445.86)">
 46  			<path id="path3957" class="st3" d="M-246.5-402.2l23.6-8l2.5,3.6l-22.9,8C-243.4-398.5-246.5-402.2-246.5-402.2z"/>
 47  		</g>
 48  		<g id="g3959" transform="translate(282.04 365.71)">
 49  			<path id="path3961" class="st4" d="M-236.5-249.5l23.2-8.3l7,6.5l-24.4,9C-230.6-242.3-236.5-249.5-236.5-249.5z"/>
 50  		</g>
 51  		<g id="g3963" transform="translate(415.68 414.03)">
 52  			<path id="path3965" class="st4" d="M-249.2-341.5l-23.6,8.4l-1.7,9.3l25.2-8.8C-249.4-332.7-249.2-341.5-249.2-341.5z"/>
 53  		</g>
 54  	</g>
 55  	<g>
 56  		<g id="text3967" transform="scale(1,-1)">
 57  			<path id="path3359" class="st5" d="M20.5-188.8c-1.2,0-2.2,0.1-3.2,0.4c-0.9,0.3-1.7,0.7-2.5,1.2c-0.7,0.5-1.3,1.2-1.8,1.9
 58  				c-0.5,0.7-0.9,1.5-1.2,2.3c-0.3,0.9-0.6,1.7-0.7,2.6c-0.1,0.9-0.2,1.8-0.2,2.7s0.1,1.8,0.2,2.7c0.1,0.9,0.4,1.8,0.7,2.6
 59  				c0.3,0.9,0.7,1.6,1.2,2.3c0.5,0.7,1.1,1.4,1.8,1.9c0.7,0.5,1.5,0.9,2.5,1.2s2,0.4,3.2,0.4c1.2,0,2.2-0.1,3.1-0.4
 60  				c0.9-0.3,1.7-0.7,2.5-1.2c0.7-0.5,1.3-1.2,1.8-1.9c0.5-0.7,0.9-1.5,1.2-2.3c0.3-0.8,0.6-1.7,0.7-2.6c0.1-0.9,0.2-1.8,0.2-2.7
 61  				s-0.1-1.8-0.2-2.7c-0.1-0.9-0.4-1.7-0.7-2.6c-0.3-0.8-0.7-1.6-1.2-2.3c-0.5-0.7-1.1-1.4-1.8-1.9c-0.7-0.5-1.5-0.9-2.5-1.2
 62  				C22.7-188.6,21.7-188.8,20.5-188.8 M20.5-184.7c0.9,0,1.8,0.2,2.5,0.7c0.7,0.4,1.2,1,1.6,1.7c0.4,0.7,0.7,1.4,0.9,2.3
 63  				c0.2,0.9,0.3,1.7,0.3,2.5c0,0.6-0.1,1.1-0.1,1.7c-0.1,0.6-0.2,1.2-0.4,1.7c-0.1,0.5-0.4,1-0.7,1.5c-0.3,0.5-0.6,0.9-1,1.2
 64  				c-0.4,0.4-0.9,0.7-1.4,0.9c-0.5,0.2-1.1,0.3-1.7,0.3c-0.7,0-1.2-0.1-1.7-0.3s-0.9-0.5-1.4-0.9c-0.4-0.4-0.7-0.8-1-1.2
 65  				c-0.3-0.5-0.5-1-0.7-1.5c-0.1-0.5-0.3-1.1-0.4-1.7s-0.1-1.1-0.1-1.6c0-0.8,0.1-1.7,0.3-2.5c0.2-0.9,0.5-1.6,0.9-2.3
 66  				c0.4-0.7,0.9-1.2,1.6-1.7C18.7-184.5,19.5-184.7,20.5-184.7"/>
 67  			<path id="path3361" class="st5" d="M35.4-188.4v21.7h9.3c1.4,0,2.5-0.2,3.5-0.6c0.9-0.4,1.7-0.9,2.3-1.6c0.6-0.7,1-1.4,1.2-2.2
 68  				c0.3-0.8,0.4-1.7,0.4-2.5c0-0.5-0.1-1.1-0.2-1.6c-0.1-0.5-0.3-1.1-0.6-1.6c-0.2-0.5-0.6-1-0.9-1.4s-0.9-0.9-1.4-1.2
 69  				c-0.6-0.4-1.2-0.6-1.9-0.8s-1.5-0.3-2.4-0.3h-5.1v-8H35.4 M44.9-176.4c0.5,0,1,0.1,1.4,0.3c0.4,0.1,0.7,0.4,0.9,0.7
 70  				c0.2,0.3,0.4,0.6,0.5,0.9c0.1,0.4,0.1,0.7,0.1,1c0,0.3-0.1,0.7-0.1,0.9c-0.1,0.4-0.2,0.7-0.4,0.9c-0.2,0.3-0.5,0.5-0.9,0.7
 71  				c-0.4,0.2-0.9,0.3-1.4,0.3h-5.3v-5.8H44.9"/>
 72  			<path id="path3363" class="st5" d="M57.9-188.4v21.7h14.8v-4H62.1v-4.6h6.2v-4h-6.2v-5.2h11.3v-4H57.9"/>
 73  			<path id="path3365" class="st5" d="M93.1-188.4l-8.6,12.7c-0.1,0.2-0.3,0.4-0.4,0.8c-0.1,0.3-0.3,0.6-0.4,0.9
 74  				c0-0.2,0.1-0.5,0.1-0.8c0-0.3,0-0.6,0-0.8v-12.7h-4.2v21.7h3.9l8.4-12.5c0.1-0.2,0.3-0.4,0.4-0.7c0.1-0.3,0.3-0.6,0.4-0.9
 75  				c0,0.3-0.1,0.6-0.1,0.9s0,0.6,0,0.7v12.5h4.1v-21.7L93.1-188.4"/>
 76  		</g>
 77  		<g id="text3971" transform="scale(1,-1)">
 78  			<path id="path3348" class="st5" d="M114.3-171.6c-0.1,0.3-0.3,0.6-0.6,0.9c-0.2,0.3-0.5,0.5-0.9,0.7c-0.4,0.2-0.7,0.4-1.2,0.4
 79  				c-0.4,0.1-0.9,0.1-1.4,0.1c-1,0-1.9-0.2-2.5-0.7c-0.6-0.4-0.9-1.1-0.9-2c0-0.5,0.1-0.9,0.5-1.3c0.3-0.4,0.7-0.7,1.3-0.9
 80  				c0.5-0.3,1.1-0.5,1.8-0.7c0.7-0.2,1.4-0.4,2-0.7c0.7-0.3,1.4-0.6,2-0.9c0.7-0.4,1.3-0.8,1.8-1.3c0.5-0.5,0.9-1.1,1.3-1.8
 81  				c0.3-0.7,0.5-1.5,0.5-2.5c0-1-0.2-2-0.6-2.8c-0.4-0.8-0.9-1.4-1.6-2c-0.7-0.6-1.4-0.9-2.4-1.2c-0.9-0.3-1.9-0.4-2.9-0.4
 82  				c-0.9,0-1.9,0.1-2.8,0.4s-1.6,0.6-2.3,1c-0.7,0.4-1.2,1-1.7,1.7s-0.9,1.4-1.2,2.2l3,1.1c0.2-0.5,0.5-0.9,0.8-1.3
 83  				c0.4-0.4,0.7-0.7,1.2-1c0.4-0.3,0.9-0.5,1.4-0.7c0.5-0.1,1.1-0.2,1.7-0.2c0.6,0,1.1,0.1,1.6,0.2c0.5,0.1,0.9,0.4,1.2,0.7
 84  				c0.4,0.3,0.6,0.7,0.8,1c0.2,0.4,0.3,0.9,0.3,1.4c0,0.7-0.1,1.2-0.5,1.6c-0.3,0.4-0.7,0.8-1.3,1.2c-0.5,0.3-1.2,0.6-1.8,0.9
 85  				c-0.7,0.2-1.4,0.5-2,0.7c-0.7,0.2-1.4,0.5-2,0.9c-0.7,0.3-1.2,0.7-1.8,1.2c-0.5,0.4-0.9,1-1.3,1.7c-0.3,0.7-0.5,1.4-0.5,2.3
 86  				c0,0.8,0.1,1.5,0.4,2.2c0.3,0.7,0.8,1.3,1.4,1.8c0.6,0.5,1.3,0.9,2.2,1.2c0.9,0.3,1.8,0.4,3,0.4c0.9,0,1.7-0.1,2.5-0.4
 87  				c0.7-0.2,1.4-0.5,2-0.9c0.6-0.4,1-0.9,1.4-1.4s0.7-1.1,0.9-1.7L114.3-171.6"/>
 88  			<path id="path3350" class="st5" d="M137.1-188.4v9.7h-9.9v-9.7h-3.3v21.7h3.3v-9h9.9v9h3.3v-21.7H137.1"/>
 89  			<path id="path3352" class="st5" d="M146.9-188.4v21.7h3.3v-21.7H146.9"/>
 90  			<path id="path3354" class="st5" d="M156.6-188.4v21.7h13.5v-3h-10.3v-5.9h6.6v-3h-6.6v-9.7H156.6"/>
 91  			<path id="path3356" class="st5" d="M183-169.8v-18.6h-3.3v18.6h-6.2v3.1h15.5v-3.1L183-169.8"/>
 92  		</g>
 93  	</g>
 94  </g>
 95  </svg>

```
  * file:///opt/input/source/src/main/webapp/bower_components/patternfly/src/img/OpenShift-logo.svg
      * `beans_1_1.xsd`: In the root tag, replace the `version` attribute value with `3.0`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8" standalone="no"?>
  2  <!-- Created with Inkscape (http://www.inkscape.org/) -->
  3  <svg id="svg4242" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns="http://www.w3.org/2000/svg" height="285.79" viewBox="0 0 286.28177 285.78885" width="286.28" version="1.1" xmlns:cc="http://creativecommons.org/ns#" xmlns:dc="http://purl.org/dc/elements/1.1/">
  4   <defs id="defs4244">
  5    <clipPath id="clipPath3923" clipPathUnits="userSpaceOnUse">
  6     <path id="path3925" d="m0 768h1024v-768h-1024v768z"/>
  7    </clipPath>
  8   </defs>
  9   <metadata id="metadata4247">
 10    <rdf:RDF>
 11     <cc:Work rdf:about="">
 12      <dc:format>image/svg+xml</dc:format>
 13      <dc:type rdf:resource="http://purl.org/dc/dcmitype/StillImage"/>
 14      <dc:title/>
 15     </cc:Work>
 16    </rdf:RDF>
 17   </metadata>
 18   <g id="layer1" transform="translate(448.86 -589.47)">
 19    <g id="g3367" transform="matrix(1.25 0 0 -1.25 -733.56 1212.1)">
 20     <g id="g3919">
 21      <g id="g3921" clip-path="url(#clipPath3923)">
 22       <g id="g3927" transform="translate(304.96 416.03)">
 23        <path id="path3929" d="m0 0-25.748-9.369c0.33-4.128 1.041-8.206 2.042-12.201l24.456 8.906c-0.793 4.135-1.076 8.396-0.75 12.664" fill="#c32034"/>
 24       </g>
 25       <g id="g3931" transform="translate(418.75 444.5)">
 26        <path id="path3933" d="m0 0c-1.795 3.704-3.873 7.284-6.279 10.657l-25.741-9.369c2.995-3.064 5.508-6.508 7.563-10.191l24.457 8.903z" fill="#c32034"/>
 27       </g>
 28       <g id="g3935" transform="translate(362.11 451.79)">
 29        <path id="path3937" d="m0 0c5.356-2.499 9.995-5.908 13.907-9.906l25.742 9.37c-7.13 10.005-16.842 18.366-28.743 23.919-36.797 17.159-80.702 1.18-97.861-35.613-5.553-11.907-7.617-24.556-6.648-36.801l25.745 9.368c0.427 5.578 1.789 11.167 4.284 16.526 11.151 23.909 39.669 34.283 63.575 23.137" fill="#db212f"/>
 30       </g>
 31       <g id="g3939" transform="translate(282.86 395.05)">
 32        <path id="path3941" d="m0 0-24.46-8.909c2.248-8.918 6.145-17.391 11.502-24.932l25.688 9.351c-6.595 6.771-10.979 15.337-12.73 24.49" fill="#ea2227"/>
 33       </g>
 34       <g id="g3943" transform="translate(389.56 404.75)">
 35        <path id="path3945" d="m0 0c-0.409-5.575-1.817-11.167-4.319-16.53-11.15-23.91-39.668-34.285-63.574-23.136-5.363 2.501-10.035 5.883-13.936 9.888l-25.687-9.352c7.113-10.006 16.816-18.369 28.721-23.926 36.799-17.156 80.698-1.177 97.857 35.619 5.557 11.905 7.608 24.549 6.626 36.785l-25.69-9.348z" fill="#db212f"/>
 36       </g>
 37       <g id="g3947" transform="translate(395.89 436.18)">
 38        <path id="path3949" d="m0 0-24.458-8.903c4.542-8.139 6.689-17.513 5.986-26.938l25.688 9.345c-0.735 9.219-3.195 18.217-7.216 26.496" fill="#ea2227"/>
 39       </g>
 40       <g id="g3951" transform="translate(279.22 406.66)">
 41        <path id="path3953" d="m0 0 25.684 9.263-0.105-5.08-24.78-9.213-0.799 5.03z" fill="#ad213a"/>
 42       </g>
 43       <g id="g3955" transform="translate(386.73 445.86)">
 44        <path id="path3957" d="m0 0 26.085 8.814 2.712-4.028-25.345-8.821-3.452 4.035z" fill="#ad213a"/>
 45       </g>
 46       <g id="g3959" transform="translate(282.04 365.71)">
 47        <path id="path3961" d="m0 0 25.716 9.213 7.777-7.225-26.967-9.967-6.526 7.979z" fill="#ba2034"/>
 48       </g>
 49       <g id="g3963" transform="translate(415.68 414.03)">
 50        <path id="path3965" d="m0 0-26.119-9.274-1.924-10.293 27.848 9.771 0.195 9.796z" fill="#ba2034"/>
 51       </g>
 52      </g>
 53     </g>
 54     <g id="text3967" transform="scale(1,-1)" fill="#231f20">
 55      <path id="path3359" d="m254.37-285.44c-1.2952 0-2.4565-0.16749-3.4837-0.50246-1.0273-0.34614-1.9373-0.80952-2.73-1.3901-0.78161-0.59178-1.4516-1.2841-2.0098-2.0768-0.5583-0.80393-1.0161-1.6637-1.3734-2.5793-0.34614-0.92675-0.60296-1.887-0.77044-2.8808-0.15632-1.0049-0.23448-2.0042-0.23448-2.998 0-0.98257 0.0782-1.9707 0.23448-2.9645 0.16748-1.0049 0.4243-1.9652 0.77044-2.8808 0.3573-0.92674 0.81509-1.7865 1.3734-2.5793 0.55828-0.80391 1.2282-1.4962 2.0098-2.0768 0.79276-0.59176 1.7028-1.0551 2.73-1.3901 1.0272-0.34611 2.1885-0.51918 3.4837-0.51921 1.2952 0.00003 2.4509 0.1731 3.467 0.51921 1.0272 0.335 1.9317 0.79838 2.7133 1.3901 0.78158 0.58064 1.4515 1.2729 2.0098 2.0768 0.55826 0.79279 1.0105 1.6526 1.3566 2.5793 0.35728 0.91561 0.61409 1.8759 0.77043 2.8808 0.16747 0.99377 0.25121 1.9819 0.25123 2.9645-0.00002 0.99376-0.0838 1.9931-0.25123 2.998-0.15634 0.99376-0.41315 1.954-0.77043 2.8808-0.34617 0.9156-0.79838 1.7754-1.3566 2.5793-0.55831 0.79277-1.2283 1.485-2.0098 2.0768-0.78162 0.58062-1.686 1.044-2.7133 1.3901-1.0161 0.33497-2.1718 0.50246-3.467 0.50246m0-4.4719c1.0719 0.00001 1.9708-0.25122 2.6965-0.75369 0.73693-0.50245 1.3287-1.1445 1.7754-1.9261 0.45778-0.78159 0.78717-1.6358 0.98817-2.5625 0.20096-0.93791 0.30146-1.8423 0.30147-2.7133-0.00001-0.6141-0.0447-1.2338-0.13398-1.8591-0.0782-0.63643-0.21217-1.245-0.40197-1.8256-0.18984-0.59177-0.43548-1.1445-0.73694-1.6581-0.30149-0.52478-0.66438-0.97699-1.0887-1.3566-0.42432-0.39078-0.92119-0.69784-1.4906-0.92118-0.5583-0.22329-1.1948-0.33495-1.9094-0.33497-0.72578 0.00002-1.3734 0.11726-1.9428 0.35172-0.5583 0.2345-1.0552 0.55273-1.4906 0.95467-0.4243 0.39082-0.78719 0.84862-1.0887 1.3734-0.30148 0.52481-0.54713 1.0831-0.73694 1.6749-0.18982 0.5918-0.32939 1.1948-0.41871 1.8088-0.0782 0.61413-0.11725 1.2115-0.11724 1.7921-0.00001 0.9156 0.10048 1.8479 0.30147 2.797 0.20098 0.93794 0.52479 1.7921 0.97142 2.5625 0.45779 0.75928 1.0552 1.3846 1.7921 1.8758 0.73693 0.48013 1.6469 0.7202 2.73 0.72019"/>
 56      <path id="path3361" d="m270.86-285.86v-24.018h10.3c1.5185 0.00003 2.797 0.22334 3.8354 0.66995 1.0384 0.43548 1.8814 1.0161 2.529 1.7418 0.6476 0.71463 1.111 1.5242 1.3901 2.4286 0.29029 0.90444 0.43544 1.82 0.43546 2.7468-0.00002 0.58064-0.067 1.1724-0.20098 1.7754-0.13401 0.5918-0.34058 1.1724-0.6197 1.7419-0.27916 0.5583-0.63647 1.0831-1.0719 1.5744-0.43549 0.4913-0.96028 0.92676-1.5744 1.3064-0.60297 0.36848-1.3008 0.65879-2.0936 0.87093-0.78162 0.21216-1.6581 0.31823-2.6295 0.31822h-5.661v8.8433h-4.6394m10.501-13.248c0.59178 0.00002 1.0886-0.0949 1.4906-0.28472 0.40196-0.18981 0.72576-0.43545 0.97142-0.73694 0.2568-0.30146 0.44103-0.64202 0.55271-1.0217 0.11164-0.37962 0.16747-0.75926 0.16749-1.1389-0.00002-0.34612-0.0503-0.70342-0.15074-1.0719-0.0893-0.37962-0.25683-0.72576-0.50246-1.0384-0.2345-0.31262-0.5583-0.56943-0.97142-0.77043-0.41315-0.20097-0.93236-0.30146-1.5576-0.30148h-5.862v6.3645h5.862"/>
 57      <path id="path3363" d="m295.76-285.86v-24.018h16.397v4.4049h-11.758v5.0413h6.9172v4.3881h-6.9172v5.795h12.478v4.3881h-17.117"/>
 58      <path id="path3365" d="m334.66-285.86-9.53-14.002c-0.15633-0.23446-0.3294-0.51919-0.51921-0.85418-0.17866-0.34612-0.33498-0.66434-0.46896-0.95467 0.0335 0.25683 0.0558 0.5583 0.067 0.90443 0.0223 0.34615 0.0335 0.64763 0.0335 0.90442v14.002h-4.6059v-24.018h4.3546l9.2955 13.834c0.14514 0.22333 0.31263 0.50247 0.50246 0.83743 0.1898 0.33499 0.35729 0.65879 0.50246 0.97142-0.0335-0.32379-0.0614-0.6476-0.0837-0.97142-0.0112-0.33496-0.0168-0.6141-0.0168-0.83743v-13.834h4.5891v24.018h-4.1202"/>
 59     </g>
 60     <g id="text3971" transform="scale(1,-1)" fill="#231f20">
 61      <path id="path3348" d="m358.06-304.42c-0.14517-0.34612-0.34615-0.66435-0.60295-0.95468-0.25683-0.30145-0.56947-0.55826-0.93793-0.77043-0.36848-0.2233-0.79278-0.39637-1.2729-0.51921-0.46897-0.1228-0.99376-0.18421-1.5744-0.18424-1.1501 0.00003-2.0489 0.25125-2.6965 0.75369-0.64762 0.50248-0.97143 1.2115-0.97142 2.1271-0.00001 0.56947 0.17864 1.0552 0.53595 1.4571 0.3573 0.39082 0.82626 0.73696 1.4069 1.0384 0.58061 0.30149 1.2394 0.58063 1.9763 0.83743 0.74809 0.24566 1.5074 0.51922 2.2778 0.82068 0.78159 0.29032 1.5409 0.63088 2.2778 1.0217 0.7481 0.37964 1.4125 0.84861 1.9931 1.4069 0.5806 0.54713 1.0496 1.2115 1.4069 1.9931 0.35728 0.77045 0.53594 1.6972 0.53595 2.7803-0.00001 1.1501-0.21216 2.1718-0.63644 3.065-0.41315 0.8821-0.98819 1.6302-1.7251 2.2443-0.73696 0.60295-1.6079 1.0663-2.6128 1.3901-0.99377 0.31264-2.0657 0.46896-3.2157 0.46896-1.0719 0-2.0768-0.13957-3.0148-0.41872-0.92677-0.26798-1.7698-0.65319-2.529-1.1556-0.74811-0.51363-1.3957-1.1277-1.9428-1.8424-0.54712-0.72577-0.97142-1.5353-1.2729-2.4286l3.3665-1.2226c0.24564 0.53597 0.54712 1.0273 0.90443 1.4739 0.36846 0.44664 0.78718 0.83186 1.2562 1.1557 0.46895 0.31264 0.98257 0.55829 1.5409 0.73694 0.56944 0.17865 1.178 0.26798 1.8256 0.26798s1.2394-0.0782 1.7754-0.23448c0.53594-0.15632 0.99374-0.3908 1.3734-0.70345 0.37963-0.31263 0.67552-0.69785 0.88768-1.1556 0.21214-0.46896 0.31821-1.0049 0.31823-1.6079-0.00002-0.7146-0.17867-1.312-0.53596-1.7921-0.35732-0.49129-0.82628-0.91559-1.4069-1.2729-0.58063-0.35729-1.245-0.66994-1.9931-0.93792-0.73695-0.26797-1.4962-0.54153-2.2778-0.82069-0.77044-0.27913-1.5297-0.59177-2.2778-0.93792-0.73695-0.34613-1.3957-0.77042-1.9763-1.2729-0.58062-0.50244-1.0496-1.1054-1.4069-1.8088-0.3573-0.70343-0.53595-1.5632-0.53595-2.5793 0-0.84858 0.16748-1.6525 0.50246-2.4118 0.34613-0.75925 0.84301-1.4236 1.4906-1.9931 0.6476-0.58059 1.446-1.0384 2.395-1.3734 0.94908-0.33495 2.0322-0.50243 3.2492-0.50246 1.0161 0.00003 1.9372 0.12285 2.7635 0.36847 0.82625 0.23451 1.5464 0.5639 2.1606 0.98817 0.62527 0.42432 1.1445 0.92678 1.5576 1.5074 0.41311 0.58064 0.72575 1.2115 0.93792 1.8926l-3.2995 1.1054"/>
 62      <path id="path3350" d="m383.24-285.86v-10.702h-10.954v10.702h-3.5675v-24.018h3.5675v9.9487h10.954v-9.9487h3.5674v24.018h-3.5674"/>
 63      <path id="path3352" d="m394.08-285.86v-24.018h3.5675v24.018h-3.5675"/>
 64      <path id="path3354" d="m404.81-285.86v-24.018h14.89v3.3665h-11.322v6.5822h7.3192v3.3665h-7.3192v10.702h-3.5675"/>
 65      <path id="path3356" d="m434.01-306.44v20.584h-3.5675v-20.584h-6.8v-3.4335h17.151v3.4335h-6.7832"/>
 66     </g>
 67    </g>
 68   </g>
 69  </svg>

```
  * file:///opt/input/source/src/main/webapp/bower_components/patternfly/src/img/OpenShift-Logo-NoText.svg
      * `beans_1_1.xsd`: In the root tag, replace the `version` attribute value with `3.0`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="utf-8"?>
  2  <!-- Generator: Adobe Illustrator 19.2.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
  3  <svg version="1.1"
  4  	 id="svg4242" xmlns:cc="http://creativecommons.org/ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
  5  	 xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 200 199.7"
  6  	 style="enable-background:new 0 0 200 199.7;" xml:space="preserve">
  7  <style type="text/css">
  8  	.st0{fill:#C32034;}
  9  	.st1{fill:#DB212F;}
 10  	.st2{fill:#EA2227;}
 11  	.st3{fill:#AD213A;}
 12  	.st4{fill:#BA2034;}
 13  </style>
 14  <g id="g3921">
 15  	<g id="g3927" transform="translate(304.96 416.03)">
 16  		<path id="path3929" class="st0" d="M-235.4-323l-23.3,8.5c0.3,3.8,0.9,7.5,1.9,11.1l22.1-8C-235.4-315.4-235.7-319.2-235.4-323"/>
 17  	</g>
 18  	<g id="g3931" transform="translate(418.75 444.5)">
 19  		<path id="path3933" class="st0" d="M-246.2-377.3c-1.6-3.3-3.5-6.6-5.6-9.6l-23.3,8.5c2.7,2.8,5,5.9,6.9,9.2
 20  			C-268.3-369.3-246.2-377.3-246.2-377.3z"/>
 21  	</g>
 22  	<g id="g3935" transform="translate(362.11 451.79)">
 23  		<path id="path3937" class="st1" d="M-240.8-391.2c4.8,2.2,9,5.4,12.6,9l23.3-8.5c-6.4-9-15.3-16.6-26-21.6
 24  			c-33.3-15.5-73-1.1-88.5,32.2c-5,10.8-6.9,22.2-6,33.3l23.3-8.5c0.4-5.1,1.6-10.1,3.9-15C-288.2-391.9-262.5-401.2-240.8-391.2"/>
 25  	</g>
 26  	<g id="g3939" transform="translate(282.86 395.05)">
 27  		<path id="path3941" class="st2" d="M-233.3-283.1l-22.1,8c2,8,5.6,15.7,10.4,22.6l23.2-8.5C-227.7-267.1-231.7-274.8-233.3-283.1"
 28  			/>
 29  	</g>
 30  	<g id="g3943" transform="translate(389.56 404.75)">
 31  		<path id="path3945" class="st1" d="M-243.4-301.6c-0.4,5.1-1.7,10.1-3.9,15c-10.1,21.6-35.9,31.1-57.5,20.9c-4.8-2.2-9-5.4-12.6-9
 32  			l-23.2,8.5c6.4,9,15.2,16.6,26,21.6c33.3,15.5,73,1.1,88.5-32.2c5-10.8,6.9-22.2,6-33.3L-243.4-301.6L-243.4-301.6z"/>
 33  	</g>
 34  	<g id="g3947" transform="translate(395.89 436.18)">
 35  		<path id="path3949" class="st2" d="M-244-361.5l-22.1,8c4.1,7.4,6.1,15.9,5.4,24.4l23.2-8.5C-238.1-345.8-240.4-353.9-244-361.5"
 36  			/>
 37  	</g>
 38  	<g id="g3951" transform="translate(279.22 406.66)">
 39  		<path id="path3953" class="st3" d="M-232.9-305.2l23.2-8.4l-0.1,4.6l-22.4,8.3C-232.2-300.7-232.9-305.2-232.9-305.2z"/>
 40  	</g>
 41  	<g id="g3955" transform="translate(386.73 445.86)">
 42  		<path id="path3957" class="st3" d="M-243.1-379.9l23.6-8l2.5,3.6l-22.9,8C-240-376.2-243.1-379.9-243.1-379.9z"/>
 43  	</g>
 44  	<g id="g3959" transform="translate(282.04 365.71)">
 45  		<path id="path3961" class="st4" d="M-233.2-227.2l23.2-8.3l7,6.5l-24.4,9C-227.3-220-233.2-227.2-233.2-227.2z"/>
 46  	</g>
 47  	<g id="g3963" transform="translate(415.68 414.03)">
 48  		<path id="path3965" class="st4" d="M-245.9-319.2l-23.6,8.4l-1.7,9.3l25.2-8.8C-246.1-310.4-245.9-319.2-245.9-319.2z"/>
 49  	</g>
 50  </g>
 51  </svg>

```
  * file:///opt/input/source/src/main/webapp/bower_components/patternfly/src/img/kubernetes.svg
      * `beans_1_1.xsd`: In the root tag, replace the `version` attribute value with `3.0`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8" standalone="no"?>
  2  <svg width="256px" height="249px" viewBox="0 0 256 249" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" preserveAspectRatio="xMidYMid">
  3  	<g>
  4  		<path d="M82.0851613,244.934194 C76.1393548,244.934194 70.523871,242.291613 66.7251613,237.501935 L8.91870968,165.656774 C5.12,160.867097 3.63354839,154.756129 5.12,148.810323 L25.7651613,59.1277419 C27.0864516,53.1819355 31.0503226,48.3922581 36.5006452,45.7496774 L120.072258,5.78064516 C122.714839,4.45935484 125.687742,3.79870968 128.660645,3.79870968 C131.633548,3.79870968 134.606452,4.45935484 137.249032,5.78064516 L220.820645,45.5845161 C226.270968,48.2270968 230.234839,53.0167742 231.556129,58.9625806 L252.20129,148.645161 C253.522581,154.590968 252.20129,160.701935 248.402581,165.491613 L190.596129,237.336774 C186.797419,241.96129 181.181935,244.769032 175.236129,244.769032 L82.0851613,244.934194 L82.0851613,244.934194 Z" fill="#326DE6"></path>
  5  		<path d="M128.495484,7.92774194 C130.807742,7.92774194 133.12,8.42322581 135.267097,9.41419355 L218.83871,49.2180645 C223.132903,51.3651613 226.436129,55.3290323 227.427097,59.9535484 L248.072258,149.636129 C249.228387,154.425806 248.072258,159.380645 244.934194,163.179355 L187.127742,235.024516 C184.154839,238.823226 179.530323,240.970323 174.740645,240.970323 L82.0851613,240.970323 C77.2954839,240.970323 72.6709677,238.823226 69.6980645,235.024516 L11.8916129,163.179355 C8.91870968,159.380645 7.76258065,154.425806 8.75354839,149.636129 L29.3987097,59.9535484 C30.5548387,55.163871 33.6929032,51.2 37.9870968,49.2180645 L121.55871,9.24903226 C123.705806,8.42322581 126.183226,7.92774194 128.495484,7.92774194 L128.495484,7.92774194 Z M128.495484,0.16516129 L128.495484,0.16516129 C125.027097,0.16516129 121.55871,0.990967742 118.255484,2.47741935 L34.683871,42.4464516 C28.0774194,45.5845161 23.4529032,51.3651613 21.8012903,58.4670968 L1.15612903,148.149677 C-0.495483871,155.251613 1.15612903,162.51871 5.78064516,168.299355 L63.5870968,240.144516 C68.0464516,245.76 74.8180645,248.898065 81.92,248.898065 L174.575484,248.898065 C181.677419,248.898065 188.449032,245.76 192.908387,240.144516 L250.714839,168.299355 C255.339355,162.683871 256.990968,155.251613 255.339355,148.149677 L234.694194,58.4670968 C233.042581,51.3651613 228.418065,45.5845161 221.811613,42.4464516 L138.570323,2.47741935 C135.432258,0.990967742 131.963871,0.16516129 128.495484,0.16516129 L128.495484,0.16516129 L128.495484,0.16516129 Z" fill="#FFFFFF"></path>
  6  		<path d="M212.232258,142.534194 L212.232258,142.534194 L212.232258,142.534194 C212.067097,142.534194 212.067097,142.534194 212.232258,142.534194 L212.067097,142.534194 C211.901935,142.534194 211.736774,142.534194 211.736774,142.369032 C211.406452,142.369032 211.076129,142.203871 210.745806,142.203871 C209.589677,142.03871 208.59871,141.873548 207.607742,141.873548 C207.112258,141.873548 206.616774,141.873548 205.956129,141.708387 L205.790968,141.708387 C202.322581,141.378065 199.514839,141.047742 196.872258,140.221935 C195.716129,139.726452 195.385806,139.065806 195.055484,138.405161 C195.055484,138.24 194.890323,138.24 194.890323,138.074839 L194.890323,138.074839 L192.743226,137.414194 C193.734194,129.816774 193.403871,121.889032 191.587097,114.126452 C189.770323,106.363871 186.632258,99.0967742 182.338065,92.4903226 L183.989677,91.003871 L183.989677,90.6735484 C183.989677,89.8477419 184.154839,89.0219355 184.815484,88.196129 C186.797419,86.3793548 189.274839,84.8929032 192.247742,83.076129 L192.247742,83.076129 C192.743226,82.7458065 193.23871,82.5806452 193.734194,82.2503226 C194.725161,81.7548387 195.550968,81.2593548 196.541935,80.5987097 C196.707097,80.4335484 197.037419,80.2683871 197.367742,79.9380645 C197.532903,79.7729032 197.698065,79.7729032 197.698065,79.6077419 L197.698065,79.6077419 C200.010323,77.6258065 200.505806,74.3225806 198.854194,72.1754839 C198.028387,71.0193548 196.541935,70.3587097 195.055484,70.3587097 C193.734194,70.3587097 192.578065,70.8541935 191.421935,71.68 L191.421935,71.68 L191.421935,71.68 C191.256774,71.8451613 191.256774,71.8451613 191.091613,72.0103226 C190.76129,72.1754839 190.596129,72.5058065 190.265806,72.6709677 C189.44,73.4967742 188.779355,74.1574194 188.11871,74.9832258 C187.788387,75.3135484 187.458065,75.8090323 186.962581,76.1393548 L186.962581,76.1393548 C184.650323,78.6167742 182.503226,80.5987097 180.356129,82.0851613 C179.860645,82.4154839 179.365161,82.5806452 178.869677,82.5806452 C178.539355,82.5806452 178.209032,82.5806452 177.87871,82.4154839 L177.548387,82.4154839 L177.548387,82.4154839 L175.566452,83.7367742 C173.419355,81.4245161 171.107097,79.4425806 168.794839,77.4606452 C158.885161,69.6980645 146.828387,64.9083871 134.276129,63.7522581 L134.110968,61.6051613 C133.945806,61.44 133.945806,61.44 133.780645,61.2748387 C133.285161,60.7793548 132.624516,60.283871 132.459355,59.1277419 C132.294194,56.4851613 132.624516,53.5122581 132.954839,50.2090323 L132.954839,50.043871 C132.954839,49.5483871 133.12,48.8877419 133.285161,48.3922581 C133.450323,47.4012903 133.615484,46.4103226 133.780645,45.2541935 L133.780645,44.2632258 L133.780645,43.7677419 L133.780645,43.7677419 L133.780645,43.7677419 C133.780645,40.7948387 131.468387,38.3174194 128.660645,38.3174194 C127.339355,38.3174194 126.018065,38.9780645 125.027097,39.9690323 C124.036129,40.96 123.540645,42.2812903 123.540645,43.7677419 L123.540645,43.7677419 L123.540645,43.7677419 L123.540645,44.0980645 L123.540645,45.0890323 C123.540645,46.2451613 123.705806,47.236129 124.036129,48.2270968 C124.20129,48.7225806 124.20129,49.2180645 124.366452,49.8787097 L124.366452,50.043871 C124.696774,53.3470968 125.192258,56.32 124.861935,58.9625806 C124.696774,60.1187097 124.036129,60.6141935 123.540645,61.1096774 C123.375484,61.2748387 123.375484,61.2748387 123.210323,61.44 L123.210323,61.44 L123.045161,63.5870968 C120.072258,63.9174194 117.099355,64.2477419 114.126452,64.9083871 C101.409032,67.716129 90.1780645,74.1574194 81.4245161,83.4064516 L79.7729032,82.2503226 L79.4425806,82.2503226 C79.1122581,82.2503226 78.7819355,82.4154839 78.4516129,82.4154839 C77.956129,82.4154839 77.4606452,82.2503226 76.9651613,81.92 C74.8180645,80.4335484 72.6709677,78.2864516 70.3587097,75.8090323 L70.3587097,75.8090323 C70.0283871,75.4787097 69.6980645,74.9832258 69.2025806,74.6529032 C68.5419355,73.8270968 67.8812903,73.1664516 67.0554839,72.3406452 C66.8903226,72.1754839 66.56,72.0103226 66.2296774,71.68 C66.0645161,71.5148387 65.8993548,71.5148387 65.8993548,71.3496774 L65.8993548,71.3496774 C64.9083871,70.523871 63.5870968,70.0283871 62.2658065,70.0283871 C60.7793548,70.0283871 59.2929032,70.6890323 58.4670968,71.8451613 C56.8154839,73.9922581 57.3109677,77.2954839 59.6232258,79.2774194 L59.6232258,79.2774194 L59.6232258,79.2774194 C59.7883871,79.2774194 59.7883871,79.4425806 59.9535484,79.4425806 C60.283871,79.6077419 60.4490323,79.9380645 60.7793548,80.1032258 C61.7703226,80.763871 62.596129,81.2593548 63.5870968,81.7548387 C64.0825806,81.92 64.5780645,82.2503226 65.0735484,82.5806452 L65.0735484,82.5806452 C68.0464516,84.3974194 70.523871,85.883871 72.5058065,87.7006452 C73.3316129,88.5264516 73.3316129,89.3522581 73.3316129,90.1780645 L73.3316129,90.5083871 L73.3316129,90.5083871 L74.9832258,91.9948387 C74.6529032,92.4903226 74.3225806,92.8206452 74.1574194,93.316129 C65.8993548,106.363871 62.7612903,121.723871 64.9083871,136.91871 L62.7612903,137.579355 C62.7612903,137.744516 62.596129,137.744516 62.596129,137.909677 C62.2658065,138.570323 61.7703226,139.230968 60.7793548,139.726452 C58.3019355,140.552258 55.3290323,140.882581 51.8606452,141.212903 L51.6954839,141.212903 C51.2,141.212903 50.5393548,141.212903 50.043871,141.378065 C49.0529032,141.378065 48.0619355,141.543226 46.9058065,141.708387 C46.5754839,141.708387 46.2451613,141.873548 45.9148387,141.873548 C45.7496774,141.873548 45.5845161,141.873548 45.4193548,142.03871 L45.4193548,142.03871 L45.4193548,142.03871 C42.4464516,142.699355 40.6296774,145.507097 41.1251613,148.149677 C41.6206452,150.461935 43.7677419,151.948387 46.4103226,151.948387 C46.9058065,151.948387 47.236129,151.948387 47.7316129,151.783226 L47.7316129,151.783226 L47.7316129,151.783226 C47.8967742,151.783226 48.0619355,151.783226 48.0619355,151.618065 C48.3922581,151.618065 48.7225806,151.452903 49.0529032,151.452903 C50.2090323,151.122581 51.0348387,150.792258 52.0258065,150.296774 C52.5212903,150.131613 53.0167742,149.80129 53.5122581,149.636129 L53.6774194,149.636129 C56.8154839,148.48 59.6232258,147.489032 62.2658065,147.15871 L62.596129,147.15871 C63.5870968,147.15871 64.2477419,147.654194 64.7432258,147.984516 C64.9083871,147.984516 64.9083871,148.149677 65.0735484,148.149677 L65.0735484,148.149677 L67.3858065,147.819355 C71.3496774,160.04129 78.9470968,170.941935 89.0219355,178.869677 C91.3341935,180.686452 93.6464516,182.172903 96.123871,183.659355 L95.1329032,185.806452 C95.1329032,185.971613 95.2980645,185.971613 95.2980645,186.136774 C95.6283871,186.797419 95.9587097,187.623226 95.6283871,188.779355 C94.6374194,191.256774 93.1509677,193.734194 91.3341935,196.541935 L91.3341935,196.707097 C91.003871,197.202581 90.6735484,197.532903 90.3432258,198.028387 C89.6825806,198.854194 89.1870968,199.68 88.5264516,200.670968 C88.3612903,200.836129 88.196129,201.166452 88.0309677,201.496774 C88.0309677,201.661935 87.8658065,201.827097 87.8658065,201.827097 L87.8658065,201.827097 L87.8658065,201.827097 C86.5445161,204.634839 87.5354839,207.772903 90.0129032,208.929032 C90.6735484,209.259355 91.3341935,209.424516 91.9948387,209.424516 C93.9767742,209.424516 95.9587097,208.103226 96.9496774,206.286452 L96.9496774,206.286452 L96.9496774,206.286452 C96.9496774,206.12129 97.1148387,205.956129 97.1148387,205.956129 C97.28,205.625806 97.4451613,205.295484 97.6103226,205.130323 C98.1058065,203.974194 98.2709677,203.148387 98.6012903,202.157419 C98.7664516,201.661935 98.9316129,201.166452 99.0967742,200.670968 L99.0967742,200.670968 C100.252903,197.367742 101.07871,194.725161 102.565161,192.412903 C103.225806,191.421935 104.051613,191.256774 104.712258,190.926452 C104.877419,190.926452 104.877419,190.926452 105.042581,190.76129 L105.042581,190.76129 L106.19871,188.614194 C113.465806,191.421935 121.393548,192.908387 129.32129,192.908387 C134.110968,192.908387 139.065806,192.412903 143.690323,191.256774 C146.663226,190.596129 149.470968,189.770323 152.27871,188.779355 L153.269677,190.596129 C153.434839,190.596129 153.434839,190.596129 153.6,190.76129 C154.425806,190.926452 155.086452,191.256774 155.747097,192.247742 C157.068387,194.56 158.059355,197.367742 159.215484,200.505806 L159.215484,200.670968 C159.380645,201.166452 159.545806,201.661935 159.710968,202.157419 C160.04129,203.148387 160.206452,204.139355 160.701935,205.130323 C160.867097,205.460645 161.032258,205.625806 161.197419,205.956129 C161.197419,206.12129 161.362581,206.286452 161.362581,206.286452 L161.362581,206.286452 L161.362581,206.286452 C162.353548,208.268387 164.335484,209.424516 166.317419,209.424516 C166.978065,209.424516 167.63871,209.259355 168.299355,208.929032 C169.455484,208.268387 170.446452,207.277419 170.776774,205.956129 C171.107097,204.634839 171.107097,203.148387 170.446452,201.827097 L170.446452,201.827097 L170.446452,201.827097 C170.446452,201.661935 170.28129,201.661935 170.28129,201.496774 C170.116129,201.166452 169.950968,200.836129 169.785806,200.670968 C169.290323,199.68 168.629677,198.854194 167.969032,198.028387 C167.63871,197.532903 167.308387,197.202581 166.978065,196.707097 L166.978065,196.541935 C165.16129,193.734194 163.509677,191.256774 162.683871,188.779355 C162.353548,187.623226 162.683871,186.962581 162.849032,186.136774 C162.849032,185.971613 163.014194,185.971613 163.014194,185.806452 L163.014194,185.806452 L162.188387,183.824516 C170.941935,178.704516 178.374194,171.437419 183.989677,162.51871 C186.962581,157.894194 189.274839,152.774194 190.926452,147.654194 L192.908387,147.984516 C193.073548,147.984516 193.073548,147.819355 193.23871,147.819355 C193.899355,147.489032 194.394839,146.993548 195.385806,146.993548 L195.716129,146.993548 C198.35871,147.323871 201.166452,148.314839 204.304516,149.470968 L204.469677,149.470968 C204.965161,149.636129 205.460645,149.966452 205.956129,150.131613 C206.947097,150.627097 207.772903,150.957419 208.929032,151.287742 C209.259355,151.287742 209.589677,151.452903 209.92,151.452903 C210.085161,151.452903 210.250323,151.452903 210.415484,151.618065 L210.415484,151.618065 C210.910968,151.783226 211.24129,151.783226 211.736774,151.783226 C214.214194,151.783226 216.36129,150.131613 217.021935,147.984516 C217.021935,146.002581 215.205161,143.36 212.232258,142.534194 L212.232258,142.534194 Z M135.762581,134.44129 L128.495484,137.909677 L121.228387,134.44129 L119.411613,126.67871 L124.366452,120.402581 L132.459355,120.402581 L137.414194,126.67871 L135.762581,134.44129 L135.762581,134.44129 Z M178.869677,117.264516 C180.190968,122.88 180.52129,128.495484 180.025806,133.945806 L154.756129,126.67871 C152.443871,126.018065 151.122581,123.705806 151.618065,121.393548 C151.783226,120.732903 152.113548,120.072258 152.609032,119.576774 L172.593548,101.574194 C175.40129,106.19871 177.548387,111.483871 178.869677,117.264516 L178.869677,117.264516 Z M164.665806,91.6645161 L143.029677,107.024516 C141.212903,108.180645 138.735484,107.850323 137.249032,106.033548 C136.753548,105.538065 136.588387,104.877419 136.423226,104.216774 L134.936774,77.2954839 C146.332903,78.6167742 156.738065,83.7367742 164.665806,91.6645161 L164.665806,91.6645161 Z M116.769032,78.1212903 C118.585806,77.7909677 120.237419,77.4606452 122.054194,77.1303226 L120.567742,103.556129 C120.402581,105.868387 118.585806,107.850323 116.108387,107.850323 C115.447742,107.850323 114.621935,107.685161 114.126452,107.354839 L92.16,91.6645161 C98.9316129,84.8929032 107.354839,80.2683871 116.769032,78.1212903 L116.769032,78.1212903 Z M84.2322581,101.574194 L103.886452,119.08129 C105.703226,120.567742 105.868387,123.375484 104.381935,125.192258 C103.886452,125.852903 103.225806,126.348387 102.4,126.513548 L76.8,133.945806 C75.8090323,122.714839 78.2864516,111.31871 84.2322581,101.574194 L84.2322581,101.574194 Z M79.7729032,146.332903 L106.033548,141.873548 C108.180645,141.708387 110.162581,143.194839 110.658065,145.341935 C110.823226,146.332903 110.823226,147.15871 110.492903,147.984516 L110.492903,147.984516 L100.418065,172.263226 C91.1690323,166.317419 83.7367742,157.233548 79.7729032,146.332903 L79.7729032,146.332903 Z M140.056774,179.2 C136.258065,180.025806 132.459355,180.52129 128.495484,180.52129 C122.714839,180.52129 117.099355,179.530323 111.814194,177.87871 L124.861935,154.260645 C126.183226,152.774194 128.330323,152.113548 130.147097,153.104516 C130.972903,153.6 131.633548,154.260645 132.129032,154.92129 L132.129032,154.92129 L144.846452,177.87871 C143.36,178.374194 141.708387,178.704516 140.056774,179.2 L140.056774,179.2 Z M172.263226,156.242581 C168.134194,162.849032 162.683871,168.134194 156.407742,172.263226 L146.002581,147.323871 C145.507097,145.341935 146.332903,143.194839 148.314839,142.203871 C148.975484,141.873548 149.80129,141.708387 150.627097,141.708387 L177.052903,146.167742 C176.061935,149.80129 174.410323,153.104516 172.263226,156.242581 L172.263226,156.242581 Z" fill="#FFFFFF"></path>
  7  	</g>
  8  </svg>

```
  * file:///opt/input/source/src/main/webapp/bower_components/patternfly/src/img/kubernetes-Logo.svg
      * `beans_1_1.xsd`: In the root tag, replace the `version` attribute value with `3.0`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="utf-8"?>
  2  <!-- Generator: Adobe Illustrator 19.2.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
  3  <svg version="1.1"
  4  	 id="svg4242" xmlns:cc="http://creativecommons.org/ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
  5  	 xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 200 199.7"
  6  	 style="enable-background:new 0 0 200 199.7;" xml:space="preserve">
  7  <style type="text/css">
  8  	.st0{fill:#326DE6;}
  9  	.st1{fill:#FFFFFF;}
 10  </style>
 11  <g>
 12  	<path class="st0" d="M70.9,175.8c-3.8,0-7.3-1.7-9.7-4.7l-36.5-45.3c-2.4-3-3.3-6.9-2.4-10.6l13-56.6c0.8-3.8,3.3-6.8,6.8-8.4
 13  		l52.7-25.2c1.7-0.8,3.5-1.3,5.4-1.3c1.9,0,3.8,0.4,5.4,1.3L158.4,50c3.4,1.7,5.9,4.7,6.8,8.4l13,56.6c0.8,3.8,0,7.6-2.4,10.6
 14  		L139.3,171c-2.4,2.9-5.9,4.7-9.7,4.7L70.9,175.8L70.9,175.8z"/>
 15  	<path class="st1" d="M100.2,26.3c1.5,0,2.9,0.3,4.3,0.9l52.7,25.1c2.7,1.4,4.8,3.9,5.4,6.8l13,56.6c0.7,3,0,6.1-2,8.5l-36.5,45.3
 16  		c-1.9,2.4-4.8,3.8-7.8,3.8H70.9c-3,0-5.9-1.4-7.8-3.8l-36.5-45.3c-1.9-2.4-2.6-5.5-2-8.5l13-56.6c0.7-3,2.7-5.5,5.4-6.8l52.7-25.2
 17  		C97.1,26.6,98.7,26.3,100.2,26.3L100.2,26.3z M100.2,21.4L100.2,21.4c-2.2,0-4.4,0.5-6.5,1.5L41,48.1c-4.2,2-7.1,5.6-8.1,10.1
 18  		l-13,56.6c-1,4.5,0,9.1,2.9,12.7l36.5,45.3c2.8,3.5,7.1,5.5,11.6,5.5h58.5c4.5,0,8.8-2,11.6-5.5l36.5-45.3c2.9-3.5,4-8.2,2.9-12.7
 19  		l-13-56.6c-1-4.5-4-8.1-8.1-10.1l-52.5-25.2C104.5,21.9,102.3,21.4,100.2,21.4L100.2,21.4L100.2,21.4z"/>
 20  	<path class="st1" d="M153,111.2L153,111.2L153,111.2C152.9,111.2,152.9,111.2,153,111.2h-0.1c-0.1,0-0.2,0-0.2-0.1
 21  		c-0.2,0-0.4-0.1-0.6-0.1c-0.7-0.1-1.4-0.2-2-0.2c-0.3,0-0.6,0-1-0.1h-0.1c-2.2-0.2-4-0.4-5.6-0.9c-0.7-0.3-0.9-0.7-1.1-1.1
 22  		c0-0.1-0.1-0.1-0.1-0.2l0,0l-1.4-0.4c0.6-4.8,0.4-9.8-0.7-14.7c-1.1-4.9-3.1-9.5-5.8-13.7l1-0.9v-0.2c0-0.5,0.1-1,0.5-1.6
 23  		c1.3-1.1,2.8-2.1,4.7-3.2l0,0c0.3-0.2,0.6-0.3,0.9-0.5c0.6-0.3,1.1-0.6,1.8-1c0.1-0.1,0.3-0.2,0.5-0.4c0.1-0.1,0.2-0.1,0.2-0.2l0,0
 24  		c1.5-1.3,1.8-3.3,0.7-4.7c-0.5-0.7-1.5-1.1-2.4-1.1c-0.8,0-1.6,0.3-2.3,0.8l0,0l0,0c-0.1,0.1-0.1,0.1-0.2,0.2
 25  		c-0.2,0.1-0.3,0.3-0.5,0.4c-0.5,0.5-0.9,0.9-1.4,1.5c-0.2,0.2-0.4,0.5-0.7,0.7l0,0c-1.5,1.6-2.8,2.8-4.2,3.8
 26  		c-0.3,0.2-0.6,0.3-0.9,0.3c-0.2,0-0.4,0-0.6-0.1h-0.2l0,0l-1.3,0.8c-1.4-1.5-2.8-2.7-4.3-4c-6.3-4.9-13.9-7.9-21.8-8.6l-0.1-1.4
 27  		c-0.1-0.1-0.1-0.1-0.2-0.2c-0.3-0.3-0.7-0.6-0.8-1.4c-0.1-1.7,0.1-3.5,0.3-5.6v-0.1c0-0.3,0.1-0.7,0.2-1c0.1-0.6,0.2-1.3,0.3-2
 28  		v-0.6v-0.3l0,0l0,0c0-1.9-1.5-3.4-3.2-3.4c-0.8,0-1.7,0.4-2.3,1C97.3,47.1,97,48,97,48.9l0,0l0,0v0.2v0.6c0,0.7,0.1,1.4,0.3,2
 29  		c0.1,0.3,0.1,0.6,0.2,1v0.1c0.2,2.1,0.5,4,0.3,5.6c-0.1,0.7-0.5,1-0.8,1.4c-0.1,0.1-0.1,0.1-0.2,0.2l0,0l-0.1,1.4
 30  		c-1.9,0.2-3.8,0.4-5.6,0.8c-8,1.8-15.1,5.8-20.6,11.7l-1-0.7h-0.2c-0.2,0-0.4,0.1-0.6,0.1c-0.3,0-0.6-0.1-0.9-0.3
 31  		c-1.4-0.9-2.7-2.3-4.2-3.9l0,0c-0.2-0.2-0.4-0.5-0.7-0.7c-0.4-0.5-0.8-0.9-1.4-1.5c-0.1-0.1-0.3-0.2-0.5-0.4
 32  		c-0.1-0.1-0.2-0.1-0.2-0.2l0,0c-0.6-0.5-1.5-0.8-2.3-0.8c-0.9,0-1.9,0.4-2.4,1.1c-1,1.4-0.7,3.4,0.7,4.7l0,0l0,0
 33  		c0.1,0,0.1,0.1,0.2,0.1c0.2,0.1,0.3,0.3,0.5,0.4c0.6,0.4,1.1,0.7,1.8,1c0.3,0.1,0.6,0.3,0.9,0.5l0,0c1.9,1.1,3.4,2.1,4.7,3.2
 34  		c0.5,0.5,0.5,1,0.5,1.6v0.2l0,0l1,0.9c-0.2,0.3-0.4,0.5-0.5,0.8c-5.2,8.2-7.2,17.9-5.8,27.5l-1.4,0.4c0,0.1-0.1,0.1-0.1,0.2
 35  		c-0.2,0.4-0.5,0.8-1.1,1.1c-1.6,0.5-3.4,0.7-5.6,0.9h-0.1c-0.3,0-0.7,0-1,0.1c-0.6,0-1.3,0.1-2,0.2c-0.2,0-0.4,0.1-0.6,0.1
 36  		c-0.1,0-0.2,0-0.3,0.1l0,0l0,0c-1.9,0.4-3,2.2-2.7,3.9c0.3,1.5,1.7,2.4,3.3,2.4c0.3,0,0.5,0,0.8-0.1l0,0l0,0c0.1,0,0.2,0,0.2-0.1
 37  		c0.2,0,0.4-0.1,0.6-0.1c0.7-0.2,1.3-0.4,1.9-0.7c0.3-0.1,0.6-0.3,0.9-0.4H53c2-0.7,3.8-1.4,5.4-1.6h0.2c0.6,0,1,0.3,1.4,0.5
 38  		c0.1,0,0.1,0.1,0.2,0.1l0,0l1.5-0.2c2.5,7.7,7.3,14.6,13.7,19.6c1.5,1.1,2.9,2.1,4.5,3l-0.6,1.4c0,0.1,0.1,0.1,0.1,0.2
 39  		c0.2,0.4,0.4,0.9,0.2,1.7c-0.6,1.6-1.6,3.1-2.7,4.9v0.1c-0.2,0.3-0.4,0.5-0.6,0.8c-0.4,0.5-0.7,1-1.1,1.7c-0.1,0.1-0.2,0.3-0.3,0.5
 40  		c0,0.1-0.1,0.2-0.1,0.2l0,0l0,0c-0.8,1.8-0.2,3.8,1.4,4.5c0.4,0.2,0.8,0.3,1.3,0.3c1.3,0,2.5-0.8,3.1-2l0,0l0,0
 41  		c0-0.1,0.1-0.2,0.1-0.2c0.1-0.2,0.2-0.4,0.3-0.5c0.3-0.7,0.4-1.3,0.6-1.9c0.1-0.3,0.2-0.6,0.3-0.9l0,0c0.7-2.1,1.3-3.8,2.2-5.2
 42  		c0.4-0.6,0.9-0.7,1.4-0.9c0.1,0,0.1,0,0.2-0.1l0,0l0.7-1.4c4.6,1.8,9.6,2.7,14.6,2.7c3,0,6.1-0.3,9.1-1c1.9-0.4,3.6-0.9,5.4-1.6
 43  		l0.6,1.1c0.1,0,0.1,0,0.2,0.1c0.5,0.1,0.9,0.3,1.4,0.9c0.8,1.5,1.5,3.2,2.2,5.2v0.1c0.1,0.3,0.2,0.6,0.3,0.9
 44  		c0.2,0.6,0.3,1.3,0.6,1.9c0.1,0.2,0.2,0.3,0.3,0.5c0,0.1,0.1,0.2,0.1,0.2l0,0l0,0c0.6,1.3,1.9,2,3.1,2c0.4,0,0.8-0.1,1.3-0.3
 45  		c0.7-0.4,1.4-1,1.6-1.9c0.2-0.8,0.2-1.8-0.2-2.6l0,0l0,0c0-0.1-0.1-0.1-0.1-0.2c-0.1-0.2-0.2-0.4-0.3-0.5c-0.3-0.6-0.7-1.1-1.1-1.7
 46  		c-0.2-0.3-0.4-0.5-0.6-0.8v-0.1c-1.1-1.8-2.2-3.3-2.7-4.9c-0.2-0.7,0-1.1,0.1-1.7c0-0.1,0.1-0.1,0.1-0.2l0,0l-0.5-1.3
 47  		c5.5-3.2,10.2-7.8,13.8-13.4c1.9-2.9,3.3-6.1,4.4-9.4l1.3,0.2c0.1,0,0.1-0.1,0.2-0.1c0.4-0.2,0.7-0.5,1.4-0.5h0.2
 48  		c1.7,0.2,3.4,0.8,5.4,1.6h0.1c0.3,0.1,0.6,0.3,0.9,0.4c0.6,0.3,1.1,0.5,1.9,0.7c0.2,0,0.4,0.1,0.6,0.1c0.1,0,0.2,0,0.3,0.1l0,0
 49  		c0.3,0.1,0.5,0.1,0.8,0.1c1.6,0,2.9-1,3.3-2.4C156,113.4,154.9,111.7,153,111.2L153,111.2z M104.7,106.1l-4.6,2.2l-4.6-2.2
 50  		l-1.1-4.9l3.1-4h5.1l3.1,4L104.7,106.1L104.7,106.1z M131.9,95.3c0.8,3.5,1,7.1,0.7,10.5l-15.9-4.6c-1.5-0.4-2.3-1.9-2-3.3
 51  		c0.1-0.4,0.3-0.8,0.6-1.1L128,85.4C129.8,88.3,131.1,91.6,131.9,95.3L131.9,95.3z M123,79.1l-13.7,9.7c-1.1,0.7-2.7,0.5-3.6-0.6
 52  		c-0.3-0.3-0.4-0.7-0.5-1.1l-0.9-17C111.4,70.9,118,74.1,123,79.1L123,79.1z M92.8,70.6c1.1-0.2,2.2-0.4,3.3-0.6l-0.9,16.7
 53  		c-0.1,1.5-1.3,2.7-2.8,2.7c-0.4,0-0.9-0.1-1.3-0.3l-13.9-9.9C81.5,74.8,86.8,71.9,92.8,70.6L92.8,70.6z M72.2,85.4l12.4,11
 54  		c1.1,0.9,1.3,2.7,0.3,3.9c-0.3,0.4-0.7,0.7-1.3,0.8l-16.2,4.7C66.9,98.7,68.5,91.5,72.2,85.4L72.2,85.4z M69.4,113.6l16.6-2.8
 55  		c1.4-0.1,2.6,0.8,2.9,2.2c0.1,0.6,0.1,1.1-0.1,1.7l0,0L82.4,130C76.6,126.2,71.9,120.5,69.4,113.6L69.4,113.6z M107.5,134.3
 56  		c-2.4,0.5-4.8,0.8-7.3,0.8c-3.6,0-7.2-0.6-10.5-1.7l8.2-14.9c0.8-0.9,2.2-1.4,3.3-0.7c0.5,0.3,0.9,0.7,1.3,1.1l0,0l8,14.5
 57  		C109.5,133.8,108.5,134,107.5,134.3L107.5,134.3z M127.8,119.9c-2.6,4.2-6,7.5-10,10.1l-6.6-15.7c-0.3-1.3,0.2-2.6,1.5-3.2
 58  		c0.4-0.2,0.9-0.3,1.5-0.3l16.7,2.8C130.2,115.8,129.1,117.9,127.8,119.9L127.8,119.9z"/>
 59  </g>
 60  </svg>

```
  * file:///opt/input/source/src/main/webapp/bower_components/patternfly/src/img/RH_Atomic-Logo-Text.svg
      * `beans_1_1.xsd`: In the root tag, replace the `version` attribute value with `3.0`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="utf-8"?>
  2  <!-- Generator: Adobe Illustrator 19.2.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
  3  <svg version="1.1"
  4  	 id="svg4242" xmlns:cc="http://creativecommons.org/ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
  5  	 xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 200 199.7"
  6  	 style="enable-background:new 0 0 200 199.7;" xml:space="preserve">
  7  <style type="text/css">
  8  	.st0{fill:#00B9E4;}
  9  	.st1{fill:#0088CE;}
 10  </style>
 11  <g>
 12  	<g>
 13  		<g>
 14  			<path class="st0" d="M88.1,117.9c-0.4,0.3-0.7,0.6-1,0.8c-2.5,2.5-4.9,4.8-7.1,6.9c1.4,0.8,2.4,2.1,3,3.7c2.7-2.4,5.5-5,8.4-7.9
 15  				c0.6-0.6,1.1-2.2-0.1-3.3C90.4,117.4,89,117.2,88.1,117.9z"/>
 16  			<path class="st0" d="M60.3,58.6c0.7,1.1,2.2,1.5,3.3,0.7c1.2-0.8,1-2.4,0.6-2.9C54.5,39.9,50.1,27.2,54,24.2
 17  				c2.4-1.9,7.6,0.2,14.5,5.3c0.7-2.2,2.3-4,4.3-5c-11.1-8.3-19.9-11.8-24-8.6C43,20.4,47.8,37,59.9,58C60,58.2,60.2,58.4,60.3,58.6
 18  				z"/>
 19  			<path class="st0" d="M140.3,104.4c2.9-0.4,5.7-0.8,8.3-1.3l0,0l0,0l0,0c0.7-0.7,1.2-1.7,1.2-2.8c0-1.8-1.3-3.3-2.9-3.7l0,0
 20  				c-3.2,0.5-6.7,1-10.4,1.4l0,0l0,0c-5.7-9.3-12.7-19.4-20.6-29.5c-2.3-3.2-7.4-9.1-11.3-13.6l0.1-0.1C124,33.4,141,20.3,146,24.1
 21  				c3.8,3-0.5,15.6-10.3,32.2c-0.3,0.5-0.6,2.1,0.6,2.9c1.2,0.8,2.7,0.4,3.3-0.7c0.1-0.2,0.3-0.4,0.4-0.6c12-21,16.9-37.6,11.1-42.1
 22  				c-7-5.5-27.8,8.6-50.3,32.9c0,0-0.3,0.4-1,1.1c-0.6-0.6-1-1.1-1-1.1c-4.9-5.2-9.7-10.1-14.2-14.2l0,0c-0.1-0.1-0.1-0.1-0.1-0.1
 23  				c-0.2-0.1-0.4-0.1-0.6-0.1c-2.1,0-3.8,1.7-3.8,3.8c0,0.5,0.1,1.1,0.3,1.5l0,0c4.7,4.4,9.6,9.5,14.8,15.2l0.1,0.1
 24  				c-4,4.5-9,10.4-11.3,13.6C76.1,78.6,69.1,88.6,63.4,98c-21.9-2.5-36.6-7.1-36.5-12.4c0-5.4,15.6-10.1,38.4-12.4
 25  				c0.3-0.1,0.4-0.1,0.7-0.1c1.2-0.2,1.9-1.4,1.8-2.3c0-1.2-0.9-2.4-2.6-2.4c-28.3,3.2-48,10.2-48,18.3
 26  				c-0.1,7.6,17.2,14.2,42.6,17.7c-11.9,20.9-16.7,37.3-10.9,41.8c4.2,3.3,13.3-0.4,24.7-9.1l0,0c0,0,0,0,0.1,0
 27  				c0.1-0.3,0.1-0.5,0.1-0.8c0-1.5-1.3-2.8-2.8-2.8c-0.2,0-0.3,0-0.4,0.1l0,0l0,0c-7.1,5.2-12.4,7.5-14.8,5.6
 28  				c-4-3.1,0.8-16.4,11.4-33.8c9.8,1.1,20.7,1.6,32.1,1.7l0,0c0.2,0,0.3,0,0.5,0l0,0l0,0c0.1,0,0.3,0,0.4,0l0,0h0.1l0,0h0.1
 29  				c0.1,0,0.3,0,0.4,0c0.2,0,0.3,0,0.5,0l0,0c11.4-0.1,22.3-0.6,32.1-1.7c10.5,17.5,15.4,30.8,11.4,33.8
 30  				c-4.1,3.2-16.5-5.2-31.5-20.4c-0.3-0.3-0.6-0.6-1-0.8c-1-0.7-2.3-0.5-3,0.2c-1.2,1.2-0.8,2.7-0.1,3.3
 31  				c19.4,19.2,36.3,29.6,42.5,24.8C157,141.7,152.2,125.3,140.3,104.4L140.3,104.4z M100.3,100c-0.1,0-0.2,0-0.3,0s-0.2,0-0.3,0
 32  				c-10.2,0-20-0.4-28.7-1.2c5.2-8.2,11.5-16.9,18.6-25.9c3.2-4,6.4-7.9,9.5-11.5l0,0c0.3-0.4,0.6-0.7,0.9-1.1
 33  				c0.3,0.4,0.6,0.7,0.9,1.1l0,0c3.1,3.7,6.3,7.5,9.5,11.5c7.1,9,13.3,17.8,18.6,25.9l0,0C120.2,99.6,110.5,100,100.3,100z"/>
 34  			<path class="st0" d="M134.9,68.4c-1.7-0.1-2.6,1.2-2.6,2.4c-0.1,1,0.6,2.1,1.8,2.3c0.2,0.1,0.4,0.1,0.7,0.1
 35  				c22.8,2.4,38.3,7,38.4,12.4c0,1.9-1.9,3.7-5.4,5.4c1.1,1.7,1.8,3.9,1.8,6.1c0,0.2,0,0.4-0.1,0.5c8.5-3.2,13.3-7,13.3-11
 36  				C182.9,78.5,163.2,71.6,134.9,68.4z"/>
 37  		</g>
 38  		<g>
 39  			<path class="st1" d="M76.6,23.6c-4.7,0-8.6,3.8-8.6,8.6c0,4.7,3.8,8.6,8.6,8.6c1.4,0,2.8-0.4,3.9-1c-0.2-0.5-0.3-1-0.3-1.5
 40  				c0-2.1,1.7-3.8,3.8-3.8c0.2,0,0.4,0,0.6,0.1c0.1,0.1,0.1,0.1,0.1,0.1c0.2-0.8,0.4-1.6,0.4-2.4C85.2,27.4,81.4,23.6,76.6,23.6z"/>
 41  			<path class="st1" d="M99.1,48.8c-0.4-0.4-0.7-0.8-1.2-1.2l-4.4,5.3c0.6,0.7,1.3,1.4,1.9,2.1l0.1,0.1c1.9-2.2,3.6-4.1,4.6-5.2
 42  				C99.4,49.2,99.1,48.8,99.1,48.8z"/>
 43  			<path class="st1" d="M100,60.3L100,60.3c0.3,0.4,0.6,0.7,0.9,1.1l0,0c1,1.2,2,2.3,3,3.5l4.6-5.4c-1.3-1.5-2.6-3-3.8-4.4L100,60.3
 44  				z"/>
 45  			<path class="st1" d="M158.3,85.9c-6,0-11,4.8-11.3,10.7c1.7,0.4,2.9,1.9,2.9,3.7c0,1.1-0.5,2.1-1.2,2.8l0,0
 46  				c2,3.2,5.6,5.4,9.6,5.4c6.2,0,11.3-5.1,11.3-11.3C169.6,90.9,164.5,85.9,158.3,85.9z"/>
 47  			<path class="st1" d="M59.7,104.4c-1.2,2.1-2.3,4.1-3.3,6.1l7,0.9c1.1-2,2.3-4,3.5-6.1L59.7,104.4L59.7,104.4z"/>
 48  			<path class="st1" d="M71,98.8c0.4-0.7,0.9-1.4,1.4-2.1l-7.5-0.9c-0.5,0.7-1,1.5-1.4,2.2l0,0L71,98.8L71,98.8z"/>
 49  			<path class="st1" d="M136.6,98.1c-0.5-0.8-1-1.6-1.5-2.3l-7.5,1c0.5,0.7,1,1.5,1.4,2.2l0,0l0,0L136.6,98.1L136.6,98.1z"/>
 50  			<path class="st1" d="M133.1,105.3L133.1,105.3c1.2,2.1,2.4,4.1,3.5,6l7-0.9c-1-2-2.1-4-3.3-6L133.1,105.3z"/>
 51  			<path class="st1" d="M76.6,124.7c-3.7,0-6.6,3-6.6,6.6c0,0.8,0.2,1.5,0.4,2.2l0,0c0.1,0,0.3-0.1,0.4-0.1c1.5,0,2.8,1.3,2.8,2.8
 52  				c0,0.3-0.1,0.5-0.1,0.8c0,0,0,0-0.1,0c1,0.5,2,0.8,3.2,0.8c3.7,0,6.6-3,6.6-6.6C83.2,127.7,80.3,124.7,76.6,124.7z"/>
 53  		</g>
 54  	</g>
 55  	<g>
 56  		<path class="st0" d="M34.2,184.7l-2.1-4.2h-2.3v4.2h-2.3v-11.6h5.4c0.5,0,1.1,0.1,1.5,0.2c0.5,0.2,0.9,0.4,1.3,0.7
 57  			c0.4,0.3,0.6,0.7,0.8,1.2c0.2,0.5,0.3,1,0.3,1.6c0,0.9-0.2,1.6-0.6,2.2c-0.4,0.6-1,1-1.7,1.3l2.2,4.5H34.2z M34.1,175.7
 58  			c-0.3-0.2-0.7-0.3-1.2-0.3h-3.1v3h3.1c1.1,0,1.7-0.5,1.7-1.5C34.5,176.3,34.4,175.9,34.1,175.7z"/>
 59  		<path class="st0" d="M39.8,184.7v-11.6h8.1v2.3h-5.8v2h3.3v2.3h-3.3v2.8h6v2.3L39.8,184.7L39.8,184.7z"/>
 60  		<path class="st0" d="M60.1,181.5c-0.3,0.7-0.8,1.3-1.3,1.8c-0.6,0.5-1.2,0.8-1.9,1.1c-0.7,0.2-1.4,0.3-2.2,0.3h-3.5v-11.6h3.7
 61  			c0.8,0,1.6,0.1,2.3,0.3c0.7,0.2,1.3,0.5,1.9,1c0.5,0.5,0.9,1.1,1.2,1.8s0.4,1.6,0.4,2.7C60.6,179.9,60.4,180.8,60.1,181.5z
 62  			 M57.4,176.2c-0.5-0.6-1.4-0.9-2.6-0.9h-1.2v7.1h1.2c0.6,0,1.2-0.1,1.6-0.3c0.5-0.2,0.8-0.4,1.1-0.7c0.3-0.3,0.5-0.7,0.6-1.1
 63  			c0.2-0.4,0.2-0.9,0.2-1.4C58.2,177.7,57.9,176.9,57.4,176.2z"/>
 64  		<path class="st0" d="M75.8,184.7v-4.9h-4.8v4.9h-2.3v-11.6h2.3v4.4h4.8v-4.4h2.3v11.6H75.8z"/>
 65  		<path class="st0" d="M89.4,184.7l-0.9-2.6h-4.2l-0.9,2.6h-2.5l4.4-11.6h2.3l4.4,11.6H89.4z M87,177.8c-0.1-0.3-0.2-0.7-0.3-1
 66  			c-0.1-0.3-0.2-0.6-0.3-0.8c-0.1,0.2-0.2,0.5-0.3,0.8s-0.2,0.6-0.3,1l-0.7,2.1h2.6L87,177.8z"/>
 67  		<path class="st0" d="M97.9,175.4v9.4h-2.3v-9.4h-3.3v-2.3h9v2.3H97.9z"/>
 68  		<path class="st0" d="M117.1,184.7l-0.9-2.6h-4.2l-0.9,2.6h-2.5l4.4-11.6h2.3l4.4,11.6H117.1z M114.6,177.8c-0.1-0.3-0.2-0.7-0.3-1
 69  			c-0.1-0.3-0.2-0.6-0.3-0.8c-0.1,0.2-0.2,0.5-0.3,0.8s-0.2,0.6-0.3,1l-0.7,2.1h2.6L114.6,177.8z"/>
 70  		<path class="st0" d="M125.6,175.4v9.4h-2.3v-9.4H120v-2.3h9v2.3H125.6z"/>
 71  		<path class="st0" d="M140.4,181.4c-0.3,0.7-0.6,1.4-1.1,1.9s-1,0.9-1.6,1.2c-0.6,0.3-1.3,0.4-2.1,0.4s-1.5-0.2-2.1-0.4
 72  			c-0.6-0.3-1.2-0.7-1.6-1.2c-0.4-0.5-0.8-1.2-1.1-1.9c-0.3-0.7-0.4-1.6-0.4-2.5c0-1,0.1-1.8,0.4-2.5c0.3-0.7,0.6-1.4,1.1-1.9
 73  			c0.5-0.5,1-0.9,1.6-1.2c0.6-0.3,1.3-0.4,2.1-0.4c0.7,0,1.4,0.2,2.1,0.4s1.2,0.7,1.6,1.2c0.4,0.5,0.8,1.2,1.1,1.9
 74  			c0.3,0.7,0.4,1.6,0.4,2.5C140.8,179.8,140.6,180.7,140.4,181.4z M137.6,176.2c-0.5-0.6-1.2-1-2-1c-0.8,0-1.5,0.3-2,1
 75  			c-0.5,0.6-0.7,1.5-0.7,2.7c0,1.2,0.3,2.1,0.7,2.8c0.5,0.6,1.2,1,2,1c0.8,0,1.5-0.3,2-1c0.5-0.6,0.7-1.5,0.7-2.7
 76  			C138.4,177.8,138.1,176.8,137.6,176.2z"/>
 77  		<path class="st0" d="M152.2,184.7v-4.3c0-0.2,0-0.4,0-0.6c0-0.3,0-0.5,0-0.7s0-0.5,0-0.7c0-0.2,0-0.4,0-0.5
 78  			c-0.1,0.2-0.2,0.5-0.4,0.9c-0.2,0.4-0.3,0.7-0.5,1.1l-2.4,5.2l-2.3-5.2c-0.2-0.3-0.3-0.7-0.5-1.1c-0.2-0.4-0.3-0.6-0.4-0.9
 79  			c0,0.1,0,0.3,0,0.5s0,0.5,0,0.7s0,0.5,0,0.7c0,0.3,0,0.4,0,0.6v4.3h-2.3v-11.6h2.2l2.4,5.3c0.1,0.2,0.2,0.3,0.2,0.5
 80  			s0.2,0.4,0.2,0.5c0.1,0.2,0.2,0.3,0.2,0.5c0.1,0.2,0.1,0.3,0.2,0.4c0.1-0.2,0.2-0.5,0.3-0.9c0.2-0.4,0.3-0.7,0.5-1.1l2.3-5.3h2.3
 81  			v11.6L152.2,184.7L152.2,184.7z"/>
 82  		<path class="st0" d="M158.1,184.7v-11.6h2.3v11.6H158.1z"/>
 83  		<path class="st0" d="M170.8,176.5c-0.2-0.4-0.5-0.7-0.8-1c-0.3-0.2-0.8-0.3-1.3-0.3c-0.4,0-0.8,0.1-1.2,0.3
 84  			c-0.4,0.2-0.6,0.4-0.8,0.7c-0.2,0.3-0.4,0.7-0.5,1.2c-0.1,0.5-0.2,1-0.2,1.5s0.1,1,0.2,1.4s0.3,0.8,0.5,1.2
 85  			c0.2,0.3,0.5,0.6,0.8,0.8s0.7,0.3,1.2,0.3c0.5,0,1-0.1,1.3-0.4c0.3-0.2,0.7-0.6,1-1.1l2,1.2c-0.4,0.8-1,1.5-1.6,2
 86  			c-0.7,0.5-1.6,0.7-2.6,0.7c-0.7,0-1.5-0.2-2.1-0.4c-0.6-0.3-1.2-0.7-1.6-1.2c-0.5-0.5-0.8-1.2-1.1-1.9c-0.3-0.7-0.4-1.6-0.4-2.5
 87  			c0-0.9,0.1-1.7,0.4-2.4c0.3-0.7,0.6-1.4,1.1-1.9c0.5-0.5,1-1,1.6-1.2c0.6-0.3,1.3-0.4,2.1-0.4c0.5,0,1.1,0.1,1.5,0.2
 88  			c0.4,0.1,0.8,0.3,1.2,0.5s0.6,0.5,0.9,0.8c0.3,0.3,0.5,0.7,0.7,1.1L170.8,176.5z"/>
 89  	</g>
 90  </g>
 91  </svg>

```
  * file:///opt/input/source/src/main/webapp/bower_components/patternfly/src/img/RH_atomic.svg
      * `beans_1_1.xsd`: In the root tag, replace the `version` attribute value with `3.0`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="utf-8"?>
  2  <!-- Generator: Adobe Illustrator 18.0.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
  3  <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
  4  <svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
  5  	 width="612px" height="792px" viewBox="0 0 612 792" enable-background="new 0 0 612 792" xml:space="preserve">
  6  <g>
  7  	<g>
  8  		<path fill="#00B9E4" d="M290.9,389.7c-0.7,0.5-1.3,1.2-1.8,1.6c-4.7,4.7-9.2,9-13.5,13c2.6,1.5,4.6,4,5.6,6.9
  9  			c5.1-4.6,10.4-9.5,15.8-14.9c1.2-1.1,2-4.1-0.2-6.2C295.2,388.7,292.6,388.4,290.9,389.7z"/>
 10  		<path fill="#00B9E4" d="M238.3,277.7c1.3,2,4.2,2.9,6.3,1.4c2.3-1.5,1.8-4.5,1.2-5.5c-18.4-31.3-26.7-55.2-19.4-60.9
 11  			c4.5-3.5,14.3,0.4,27.4,10c1.3-4.1,4.3-7.5,8.1-9.5c-21-15.7-37.6-22.3-45.4-16.2c-10.9,8.5-1.7,39.8,21,79.5
 12  			C237.8,276.9,238.1,277.3,238.3,277.7z"/>
 13  		<path fill="#00B9E4" d="M389.5,364.1c5.5-0.7,10.7-1.6,15.7-2.5c0,0,0,0,0,0c0,0,0,0,0,0c0,0,0,0,0,0c1.4-1.3,2.3-3.2,2.3-5.3
 14  			c0-3.4-2.4-6.2-5.5-6.9c0,0,0,0,0,0c-6.1,1-12.7,1.9-19.7,2.7l0,0l0,0c-10.8-17.6-24-36.6-39-55.7c-4.4-6-13.9-17.1-21.4-25.6
 15  			l0.1-0.1c36.6-40.7,68.9-65.5,78.2-58.2c7.2,5.6-1,29.5-19.4,60.9c-0.6,1-1.1,4,1.2,5.5c2.2,1.5,5.1,0.7,6.3-1.4
 16  			c0.2-0.3,0.5-0.8,0.7-1.1c22.7-39.7,31.9-71,21-79.5c-13.3-10.4-52.5,16.2-95,62.1c0,0-0.6,0.7-1.8,2c-1.1-1.2-1.8-2-1.8-2
 17  			c-9.2-9.9-18.3-19-26.9-26.9v0c-0.1-0.1-0.1-0.1-0.2-0.2c-0.4-0.1-0.8-0.1-1.2-0.1c-4,0-7.2,3.2-7.2,7.2c0,1,0.2,2,0.6,2.8l0,0
 18  			c8.8,8.3,18.2,18,28,28.8l0.1,0.1c-7.5,8.5-17,19.6-21.4,25.6c-15,19.1-28.2,38-39,55.7c-41.3-4.7-69.1-13.4-69-23.4
 19  			c0-10.2,29.4-19,72.5-23.5c0.5-0.1,0.8-0.2,1.3-0.2c2.3-0.4,3.5-2.6,3.4-4.4c0-2.3-1.7-4.6-4.9-4.5c-53.5,6-90.6,19.2-90.7,34.5
 20  			c-0.1,14.4,32.4,26.9,80.4,33.5c-22.5,39.4-31.5,70.4-20.6,78.9c7.9,6.2,25.1-0.7,46.6-17.1l0,0c0,0,0,0,0.1,0
 21  			c0.1-0.5,0.2-1,0.2-1.5c0-2.9-2.4-5.3-5.3-5.3c-0.3,0-0.5,0-0.7,0.1c0,0,0,0,0,0v0c-13.4,9.9-23.5,14.1-28,10.5
 22  			c-7.5-5.9,1.6-30.9,21.5-63.9c18.6,2,39.1,3.1,60.7,3.2v0c0.3,0,0.6,0,0.9,0c0,0,0,0,0,0l0,0c0.2,0,0.5,0,0.7,0h0h0.2c0,0,0,0,0,0
 23  			h0.2c0.2,0,0.5,0,0.7,0c0.3,0,0.6,0,0.9,0v0c21.5-0.1,42.1-1.2,60.7-3.2c19.9,33,29,58.1,21.5,63.9c-7.7,6-31.1-9.8-59.6-38.5
 24  			c-0.5-0.5-1.1-1.1-1.8-1.6c-1.8-1.3-4.3-1-5.7,0.4c-2.2,2.2-1.5,5.1-0.2,6.2c36.6,36.3,68.5,56,80.2,46.8
 25  			C421,434.6,412,403.6,389.5,364.1L389.5,364.1z M313.9,355.9c-0.2,0-0.3,0-0.5,0c-0.2,0-0.3,0-0.5,0c-19.3,0-37.7-0.8-54.3-2.3
 26  			c9.9-15.4,21.8-32,35.1-49c6-7.6,12-14.9,17.9-21.8v0c0.6-0.7,1.2-1.4,1.7-2c0.6,0.7,1.2,1.4,1.7,2v0c5.9,6.9,11.9,14.2,17.9,21.8
 27  			c13.4,17,25.2,33.6,35.1,49l0,0C351.6,355,333.2,355.8,313.9,355.9z"/>
 28  		<path fill="#00B9E4" d="M379.3,296.2c-3.2-0.1-4.9,2.2-4.9,4.5c-0.1,1.8,1.2,4,3.4,4.4c0.4,0.1,0.8,0.2,1.3,0.2
 29  			c43.1,4.5,72.4,13.3,72.5,23.5c0,3.6-3.6,7-10.2,10.2c2.1,3.3,3.4,7.3,3.4,11.5c0,0.3,0,0.7-0.1,1c16-6,25.2-13.2,25.2-20.8
 30  			C469.9,315.3,432.7,302.2,379.3,296.2z"/>
 31  	</g>
 32  	<g>
 33  		<path fill="#0088CE" d="M269.2,211.5c-8.9,0-16.2,7.2-16.2,16.2c0,8.9,7.2,16.2,16.2,16.2c2.7,0,5.2-0.7,7.4-1.8
 34  			c-0.4-0.9-0.6-1.8-0.6-2.8c0-4,3.2-7.2,7.2-7.2c0.4,0,0.8,0,1.2,0.1c0.1,0.1,0.1,0.1,0.2,0.2c0.4-1.5,0.7-3,0.7-4.6
 35  			C285.4,218.7,278.2,211.5,269.2,211.5z"/>
 36  		<path fill="#0088CE" d="M311.6,259.2c-0.7-0.8-1.4-1.5-2.2-2.3l-8.4,10c1.2,1.3,2.4,2.6,3.6,3.9l0.1,0.1c3.6-4.2,6.8-7.7,8.7-9.8
 37  			C312.3,259.9,311.6,259.2,311.6,259.2z"/>
 38  		<path fill="#0088CE" d="M313.4,280.8C313.4,280.8,313.4,280.8,313.4,280.8c0.6,0.7,1.2,1.4,1.7,2.1v0c1.9,2.2,3.7,4.4,5.6,6.6
 39  			l8.6-10.2c-2.5-2.9-4.9-5.7-7.2-8.3L313.4,280.8z"/>
 40  		<path fill="#0088CE" d="M423.4,329.2c-11.4,0-20.8,9-21.3,20.3c3.2,0.7,5.5,3.5,5.5,6.9c0,2.1-0.9,4-2.3,5.3c0,0,0,0,0,0
 41  			c3.8,6.1,10.5,10.2,18.1,10.2c11.8,0,21.3-9.6,21.3-21.3C444.8,338.7,435.2,329.2,423.4,329.2z"/>
 42  		<path fill="#0088CE" d="M237.3,364.1c-2.3,4-4.3,7.8-6.3,11.6l13.3,1.7c2.1-3.7,4.3-7.6,6.7-11.6L237.3,364.1L237.3,364.1z"/>
 43  		<path fill="#0088CE" d="M258.6,353.6c0.8-1.3,1.7-2.6,2.6-3.9L247,348c-0.9,1.4-1.8,2.8-2.7,4.2v0L258.6,353.6L258.6,353.6z"/>
 44  		<path fill="#0088CE" d="M382.5,352.2c-0.9-1.5-1.9-3-2.8-4.4l-14.2,1.8c0.9,1.4,1.9,2.8,2.7,4.1l0,0c0,0,0,0,0,0L382.5,352.2
 45  			L382.5,352.2z"/>
 46  		<path fill="#0088CE" d="M375.8,365.8C375.8,365.8,375.8,365.8,375.8,365.8c2.3,3.9,4.5,7.7,6.6,11.3l13.3-1.7
 47  			c-1.9-3.7-4-7.5-6.2-11.4L375.8,365.8z"/>
 48  		<path fill="#0088CE" d="M269.2,402.6c-6.9,0-12.5,5.6-12.5,12.5c0,1.5,0.3,2.9,0.7,4.2c0,0,0,0,0,0c0.2,0,0.5-0.1,0.7-0.1
 49  			c2.9,0,5.3,2.4,5.3,5.3c0,0.5-0.1,1-0.2,1.5c0,0,0,0-0.1,0c1.8,1,3.8,1.5,6,1.5c6.9,0,12.5-5.6,12.5-12.5
 50  			C281.7,408.2,276.1,402.6,269.2,402.6z"/>
 51  	</g>
 52  </g>
 53  <g>
 54  	<path fill="#00B9E4" d="M189.1,535.6l-3.9-7.9h-4.4v7.9h-4.4v-22h10.2c1,0,2,0.1,2.9,0.4c0.9,0.3,1.7,0.7,2.4,1.3
 55  		c0.7,0.6,1.2,1.3,1.6,2.2c0.4,0.9,0.6,1.9,0.6,3.1c0,1.7-0.4,3-1.1,4.1c-0.7,1.1-1.8,1.9-3.2,2.4l4.2,8.5H189.1z M188.8,518.6
 56  		c-0.6-0.4-1.3-0.6-2.3-0.6h-5.8v5.6h5.8c2.1,0,3.2-0.9,3.2-2.8C189.7,519.8,189.4,519,188.8,518.6z"/>
 57  	<path fill="#00B9E4" d="M199.7,535.6v-22H215v4.3h-10.9v3.8h6.3v4.3h-6.3v5.3h11.3v4.3H199.7z"/>
 58  	<path fill="#00B9E4" d="M237.9,529.6c-0.6,1.4-1.5,2.5-2.5,3.4c-1.1,0.9-2.3,1.5-3.6,2c-1.3,0.4-2.7,0.6-4.1,0.6h-6.6v-22h6.9
 59  		c1.6,0,3,0.2,4.3,0.6c1.3,0.4,2.5,1,3.5,1.9c1,0.9,1.7,2,2.3,3.4c0.6,1.4,0.8,3.1,0.8,5.1C238.9,526.6,238.6,528.2,237.9,529.6z
 60  		 M232.8,519.6c-1-1.1-2.7-1.7-5-1.7h-2.3v13.4h2.2c1.2,0,2.2-0.2,3-0.5c0.9-0.3,1.5-0.8,2.1-1.4c0.5-0.6,1-1.3,1.2-2.1
 61  		c0.3-0.8,0.4-1.7,0.4-2.7C234.4,522.4,233.9,520.8,232.8,519.6z"/>
 62  	<path fill="#00B9E4" d="M267.7,535.6v-9.2h-9v9.2h-4.4v-22h4.4v8.4h9v-8.4h4.4v22H267.7z"/>
 63  	<path fill="#00B9E4" d="M293.3,535.6l-1.7-4.9h-8l-1.7,4.9h-4.7l8.4-22h4.3l8.4,22H293.3z M288.7,522.6c-0.2-0.6-0.4-1.3-0.6-1.9
 64  		c-0.2-0.6-0.4-1.1-0.5-1.5c-0.1,0.4-0.3,0.9-0.5,1.5c-0.2,0.6-0.4,1.2-0.6,1.9l-1.4,4h5L288.7,522.6z"/>
 65  	<path fill="#00B9E4" d="M309.4,518v17.7h-4.4V518h-6.3v-4.3h17v4.3H309.4z"/>
 66  	<path fill="#00B9E4" d="M345.6,535.6l-1.7-4.9h-8l-1.7,4.9h-4.7l8.4-22h4.3l8.4,22H345.6z M341,522.6c-0.2-0.6-0.4-1.3-0.6-1.9
 67  		c-0.2-0.6-0.4-1.1-0.5-1.5c-0.1,0.4-0.3,0.9-0.5,1.5c-0.2,0.6-0.4,1.2-0.6,1.9l-1.4,4h5L341,522.6z"/>
 68  	<path fill="#00B9E4" d="M361.8,518v17.7h-4.4V518h-6.3v-4.3h17v4.3H361.8z"/>
 69  	<path fill="#00B9E4" d="M389.7,529.4c-0.5,1.4-1.1,2.6-2,3.6c-0.9,1-1.9,1.7-3.1,2.2c-1.2,0.5-2.5,0.8-3.9,0.8
 70  		c-1.4,0-2.8-0.3-3.9-0.8c-1.2-0.5-2.2-1.3-3-2.2c-0.8-1-1.5-2.2-2-3.5c-0.5-1.4-0.7-3-0.7-4.8c0-1.8,0.2-3.4,0.7-4.8
 71  		c0.5-1.4,1.1-2.6,2-3.6c0.9-1,1.9-1.7,3.1-2.2c1.2-0.5,2.5-0.8,4-0.8c1.4,0,2.7,0.3,3.9,0.8c1.2,0.5,2.2,1.3,3,2.2
 72  		c0.8,1,1.5,2.2,2,3.5c0.5,1.4,0.7,3,0.7,4.8C390.4,526.4,390.1,528,389.7,529.4z M384.4,519.5c-1-1.2-2.2-1.8-3.8-1.8
 73  		c-1.5,0-2.8,0.6-3.7,1.8c-0.9,1.2-1.4,2.9-1.4,5.1c0,2.2,0.5,4,1.4,5.2c1,1.2,2.2,1.8,3.8,1.8c1.5,0,2.8-0.6,3.7-1.8
 74  		c0.9-1.2,1.4-2.9,1.4-5.1C385.9,522.5,385.4,520.7,384.4,519.5z"/>
 75  	<path fill="#00B9E4" d="M411.9,535.6v-8.1c0-0.3,0-0.7,0-1.1c0-0.5,0-0.9,0-1.4c0-0.5,0-0.9,0-1.4c0-0.4,0-0.7,0-0.9
 76  		c-0.2,0.4-0.4,1-0.7,1.7c-0.3,0.7-0.6,1.4-0.9,2l-4.5,9.8l-4.4-9.8c-0.3-0.6-0.6-1.3-0.9-2c-0.3-0.7-0.5-1.2-0.7-1.7
 77  		c0,0.2,0,0.5,0,0.9c0,0.4,0,0.9,0,1.4c0,0.5,0,1,0,1.4c0,0.5,0,0.8,0,1.1v8.1h-4.3v-22h4.2l4.6,10c0.1,0.3,0.3,0.6,0.4,1
 78  		s0.3,0.7,0.4,1c0.1,0.3,0.3,0.6,0.4,0.9c0.1,0.3,0.2,0.5,0.3,0.7c0.1-0.4,0.4-1,0.6-1.7c0.3-0.7,0.6-1.4,0.9-2l4.4-10h4.3v22H411.9
 79  		z"/>
 80  	<path fill="#00B9E4" d="M423.2,535.6v-22h4.4v22H423.2z"/>
 81  	<path fill="#00B9E4" d="M447.1,520.1c-0.4-0.8-0.9-1.3-1.6-1.8c-0.6-0.4-1.5-0.6-2.5-0.6c-0.8,0-1.5,0.2-2.2,0.5s-1.2,0.8-1.6,1.4
 82  		c-0.4,0.6-0.8,1.3-1,2.2c-0.2,0.9-0.3,1.8-0.3,2.8c0,1,0.1,1.9,0.3,2.7c0.2,0.8,0.6,1.6,1,2.2c0.4,0.6,1,1.1,1.6,1.5
 83  		c0.6,0.4,1.4,0.5,2.2,0.5c1,0,1.8-0.2,2.5-0.7c0.6-0.4,1.3-1.2,1.8-2.1l3.7,2.2c-0.8,1.6-1.8,2.8-3.1,3.7c-1.3,0.9-3,1.3-5,1.3
 84  		c-1.4,0-2.8-0.3-3.9-0.8c-1.2-0.5-2.2-1.3-3-2.3c-0.9-1-1.5-2.2-2-3.6c-0.5-1.4-0.7-3-0.7-4.7c0-1.7,0.2-3.2,0.7-4.6
 85  		c0.5-1.4,1.2-2.6,2-3.6c0.9-1,1.9-1.8,3.1-2.3c1.2-0.6,2.5-0.8,4-0.8c1,0,2,0.1,2.8,0.4c0.8,0.2,1.6,0.6,2.2,1s1.2,0.9,1.7,1.5
 86  		c0.5,0.6,0.9,1.3,1.3,2L447.1,520.1z"/>
 87  </g>
 88  </svg>

```
  * file:///opt/input/source/src/main/webapp/bower_components/patternfly/src/img/logo-alt.svg
      * `beans_1_1.xsd`: In the root tag, replace the `version` attribute value with `3.0`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="utf-8"?>
  2  <!-- Generator: Adobe Illustrator 16.0.4, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
  3  <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
  4  <svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
  5  	 width="37px" height="35px" viewBox="0 0 37 35" enable-background="new 0 0 37 35" xml:space="preserve">
  6  <linearGradient id="SVGID_1_" gradientUnits="userSpaceOnUse" x1="231.8955" y1="-269.5547" x2="231.8955" y2="-301.7199" gradientTransform="matrix(1 0 0 -1 -213.5 -268.5)">
  7  	<stop  offset="0" style="stop-color:#60EFFF"/>
  8  	<stop  offset="1" style="stop-color:#1F89C7"/>
  9  </linearGradient>
 10  <path fill="url(#SVGID_1_)" d="M36.792,17.992L18.398,0L0,17.992l7.333,10.39l5.595-1.285l5.503,7.737l5.493-7.724l5.533,1.27
 11  	L36.792,17.992z M17.634,3.336L15.25,25.355l-4.549-6.205L17.634,3.336z M10.202,18.47l-2.833-3.866l9.743-11.833L10.202,18.47z
 12  	 M14.495,25.562L14.495,25.562l0.265,0.365l-1.52,0.348l-3.507-4.93l0.626-1.424L14.495,25.562z M18.396,3.044l2.395,23.345
 13  	l-2.4,3.288L16,26.389L18.396,3.044z M22.296,25.562l4.181-5.702l0.654,1.485l-3.517,4.944l-1.58-0.362l0.264-0.363L22.296,25.562z
 14  	 M21.542,25.355L19.189,3.318l6.946,15.77L21.542,25.355z M19.744,2.767l9.679,11.837l-2.787,3.802L19.744,2.767z M7.647,27.56
 15  	l-6.692-9.48L14.051,5.278l-7.605,9.302l3.417,4.661l-0.964,2.188l3.572,5.023L7.647,27.56z M18.432,33.573l-4.733-6.653
 16  	l1.528-0.352l3.162,4.351l3.173-4.351l1.592,0.367L18.432,33.573z M24.384,26.466l3.581-5.037l-0.99-2.248l3.372-4.6l-7.605-9.302
 17  	l13.095,12.801l-6.692,9.48L24.384,26.466z"/>
 18  </svg>

```
  * file:///opt/input/source/src/main/webapp/bower_components/patternfly/src/img/brand.svg
      * `beans_1_1.xsd`: In the root tag, replace the `version` attribute value with `3.0`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="utf-8"?>
  2  <!-- Generator: Adobe Illustrator 16.0.4, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
  3  <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
  4  <svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
  5  	 width="270px" height="10px" viewBox="0 0 270 10" enable-background="new 0 0 270 10" xml:space="preserve">
  6  <g>
  7  	<g>
  8  		<path fill="#FFFFFF" d="M121.965,9.413h-4.883V0.656h4.883v0.903h-3.862V4.38h3.63v0.898h-3.63V8.5h3.862V9.413z"/>
  9  		<path fill="#FFFFFF" d="M130.988,9.413h-1.158l-4.789-7.352h-0.046c0.062,0.864,0.095,1.655,0.095,2.374v4.978h-0.94V0.656h1.15
 10  			l4.774,7.317h0.045c-0.006-0.107-0.022-0.453-0.051-1.041c-0.028-0.582-0.039-0.998-0.028-1.254V0.656h0.951v8.753h-0.003V9.413
 11  			L130.988,9.413z"/>
 12  		<path fill="#FFFFFF" d="M136.339,9.413h-1.018V1.561h-2.771V0.656h6.564v0.903h-2.771v7.852h-0.002v0.002H136.339z"/>
 13  		<path fill="#FFFFFF" d="M145.554,9.413h-4.877V0.656h4.877v0.903h-3.859V4.38h3.631v0.898h-3.631V8.5h3.859V9.413z"/>
 14  		<path fill="#FFFFFF" d="M148.761,5.769v3.641h-1.018V0.656h2.402c1.074,0,1.865,0.204,2.379,0.614
 15  			c0.514,0.412,0.771,1.032,0.771,1.858c0,1.156-0.586,1.94-1.764,2.349l2.383,3.934h-1.207l-2.121-3.645h-1.826V5.769
 16  			L148.761,5.769z M148.761,4.897h1.396c0.719,0,1.244-0.142,1.582-0.428c0.334-0.286,0.504-0.714,0.504-1.285
 17  			c0-0.582-0.17-0.997-0.512-1.254c-0.34-0.255-0.889-0.381-1.643-0.381h-1.324v3.349h-0.004V4.897z"/>
 18  		<path fill="#FFFFFF" d="M161.124,3.209c0,0.884-0.301,1.567-0.904,2.046c-0.605,0.477-1.475,0.714-2.6,0.714h-1.031v3.444h-1.016
 19  			V0.656h2.27C160.03,0.656,161.124,1.504,161.124,3.209z M156.589,5.092h0.92c0.898,0,1.555-0.146,1.959-0.435
 20  			c0.4-0.293,0.604-0.759,0.604-1.404c0-0.577-0.188-1.006-0.568-1.295c-0.381-0.279-0.973-0.423-1.773-0.423h-1.139v3.557H156.589z
 21  			"/>
 22  		<path fill="#FFFFFF" d="M164.22,5.769v3.641h-1.02V0.656h2.402c1.074,0,1.865,0.204,2.383,0.614
 23  			c0.512,0.412,0.771,1.032,0.771,1.858c0,1.156-0.588,1.94-1.762,2.349l2.379,3.934h-1.205l-2.119-3.645h-1.826v0.002H164.22z
 24  			 M164.22,4.897h1.395c0.719,0,1.244-0.142,1.582-0.428c0.334-0.286,0.504-0.714,0.504-1.285c0-0.582-0.17-0.997-0.51-1.254
 25  			c-0.34-0.255-0.887-0.381-1.645-0.381h-1.322v3.349h-0.004V4.897z"/>
 26  		<path fill="#FFFFFF" d="M171.03,9.413V0.656h1.018v8.753h-1.018V9.413z"/>
 27  		<path fill="#FFFFFF" d="M179.636,7.081c0,0.773-0.281,1.374-0.838,1.805c-0.561,0.434-1.318,0.646-2.277,0.646
 28  			c-1.039,0-1.836-0.134-2.395-0.4V8.147c0.357,0.152,0.75,0.272,1.174,0.357c0.422,0.088,0.844,0.131,1.258,0.131
 29  			c0.68,0,1.188-0.129,1.531-0.384c0.346-0.257,0.514-0.62,0.514-1.073c0-0.304-0.061-0.556-0.184-0.748
 30  			c-0.119-0.194-0.318-0.375-0.607-0.537c-0.285-0.162-0.721-0.351-1.301-0.558c-0.816-0.29-1.398-0.636-1.748-1.036
 31  			c-0.352-0.398-0.525-0.92-0.525-1.562c0-0.674,0.254-1.211,0.764-1.611c0.508-0.398,1.178-0.599,2.014-0.599
 32  			c0.869,0,1.672,0.161,2.398,0.48l-0.316,0.884c-0.725-0.3-1.428-0.454-2.109-0.454c-0.539,0-0.959,0.114-1.266,0.347
 33  			c-0.303,0.231-0.453,0.553-0.453,0.965c0,0.305,0.057,0.551,0.168,0.745c0.115,0.195,0.303,0.372,0.566,0.533
 34  			c0.268,0.161,0.672,0.34,1.221,0.535c0.92,0.327,1.551,0.679,1.896,1.056C179.462,5.995,179.636,6.483,179.636,7.081z"/>
 35  		<path fill="#FFFFFF" d="M186.556,9.413h-4.881V0.656h4.881v0.903h-3.863V4.38h3.633v0.898h-3.633V8.5h3.863V9.413z"/>
 36  		<path fill="#FFFFFF" d="M197.677,9.413l-1.09-2.785h-3.51l-1.078,2.785h-1.031l3.463-8.793h0.854l3.443,8.793H197.677z
 37  			 M196.267,5.71l-1.018-2.712c-0.131-0.345-0.271-0.766-0.406-1.263c-0.09,0.383-0.211,0.804-0.377,1.263l-1.031,2.712H196.267z"/>
 38  		<path fill="#FFFFFF" d="M205.733,3.209c0,0.884-0.303,1.567-0.908,2.046c-0.607,0.477-1.473,0.714-2.596,0.714h-1.031v3.444
 39  			h-1.021V0.656h2.273C204.642,0.656,205.733,1.504,205.733,3.209z M201.2,5.092h0.914c0.902,0,1.557-0.146,1.961-0.435
 40  			c0.398-0.293,0.605-0.759,0.605-1.404c0-0.577-0.189-1.006-0.57-1.295c-0.381-0.279-0.969-0.423-1.773-0.423H201.2V5.092
 41  			L201.2,5.092z"/>
 42  		<path fill="#FFFFFF" d="M213.366,3.209c0,0.884-0.307,1.567-0.908,2.046c-0.607,0.477-1.473,0.714-2.598,0.714h-1.031v3.444h-1.02
 43  			V0.656h2.271C212.269,0.656,213.366,1.504,213.366,3.209z M208.827,5.092h0.918c0.904,0,1.559-0.146,1.959-0.435
 44  			c0.404-0.293,0.604-0.759,0.604-1.404c0-0.577-0.188-1.006-0.566-1.295c-0.381-0.279-0.971-0.423-1.773-0.423h-1.141V5.092
 45  			L208.827,5.092z"/>
 46  		<path fill="#FFFFFF" d="M215.44,9.413V0.656h1.021v7.832h3.857V9.41h-4.879V9.413z"/>
 47  		<path fill="#FFFFFF" d="M222.052,9.413V0.656h1.021v8.753h-1.021V9.413z"/>
 48  		<path fill="#FFFFFF" d="M229.466,1.44c-0.959,0-1.721,0.32-2.279,0.959c-0.557,0.642-0.834,1.518-0.834,2.633
 49  			c0,1.146,0.27,2.031,0.807,2.656c0.537,0.621,1.303,0.937,2.299,0.937c0.611,0,1.309-0.108,2.09-0.327v0.891
 50  			c-0.605,0.229-1.355,0.343-2.244,0.343c-1.289,0-2.285-0.396-2.988-1.181c-0.699-0.776-1.051-1.891-1.051-3.333
 51  			c0-0.902,0.17-1.69,0.506-2.371c0.336-0.678,0.824-1.202,1.461-1.569s1.387-0.551,2.248-0.551c0.918,0,1.719,0.168,2.408,0.504
 52  			l-0.432,0.875C230.798,1.594,230.13,1.44,229.466,1.44z"/>
 53  		<path fill="#FFFFFF" d="M239.204,9.413l-1.09-2.785h-3.512l-1.074,2.785h-1.031l3.459-8.793h0.857l3.445,8.793H239.204z
 54  			 M237.798,5.71l-1.018-2.712c-0.133-0.345-0.27-0.766-0.406-1.263c-0.088,0.383-0.215,0.804-0.377,1.263l-1.033,2.712H237.798z"/>
 55  		<path fill="#FFFFFF" d="M244.401,9.413h-1.016V1.561h-2.773V0.656h6.564v0.903h-2.771v7.852h-0.004V9.413z"/>
 56  		<path fill="#FFFFFF" d="M248.743,9.413V0.656h1.018v8.753h-1.018V9.413z"/>
 57  		<path fill="#FFFFFF" d="M260.005,5.021c0,1.402-0.354,2.503-1.062,3.305c-0.707,0.806-1.691,1.206-2.955,1.206
 58  			c-1.291,0-2.285-0.396-2.988-1.186c-0.699-0.789-1.051-1.901-1.051-3.338c0-1.424,0.354-2.532,1.057-3.312
 59  			c0.699-0.785,1.703-1.18,2.99-1.18c1.262,0,2.24,0.399,2.951,1.2C259.655,2.513,260.005,3.614,260.005,5.021z M253.03,5.021
 60  			c0,1.186,0.25,2.085,0.754,2.697c0.508,0.613,1.242,0.922,2.203,0.922c0.973,0,1.705-0.311,2.201-0.918
 61  			c0.494-0.615,0.738-1.516,0.738-2.702c0-1.179-0.244-2.072-0.736-2.681c-0.49-0.61-1.223-0.914-2.189-0.914
 62  			c-0.969,0-1.705,0.306-2.213,0.918C253.282,2.96,253.03,3.851,253.03,5.021z"/>
 63  		<path fill="#FFFFFF" d="M269.044,9.413h-1.162l-4.783-7.352h-0.049c0.061,0.864,0.094,1.655,0.094,2.374v4.978H262.2V0.656h1.152
 64  			l4.771,7.319h0.049c-0.012-0.108-0.025-0.455-0.055-1.041c-0.027-0.582-0.041-0.998-0.029-1.256V0.656h0.951v8.755h0.006v0.002
 65  			H269.044z"/>
 66  	</g>
 67  	<g>
 68  		<path fill="#FFFFFF" d="M7.533,3.368c0,1.013-0.298,1.796-0.896,2.348C6.04,6.269,5.191,6.544,4.093,6.544H3.403v3.008H0.954
 69  			V0.485h3.139c1.145,0,2.005,0.25,2.58,0.75C7.246,1.736,7.533,2.447,7.533,3.368z M3.403,4.547h0.447
 70  			c0.368,0,0.66-0.103,0.877-0.31s0.326-0.492,0.326-0.856c0-0.612-0.339-0.918-1.018-0.918H3.403V4.547z"/>
 71  		<path fill="#FFFFFF" d="M17.652,9.552l-0.446-1.699h-2.944l-0.459,1.699h-2.691l2.958-9.104h3.268l2.995,9.104H17.652z
 72  			 M16.697,5.843l-0.39-1.489c-0.092-0.33-0.202-0.758-0.333-1.283c-0.13-0.525-0.216-0.901-0.257-1.128
 73  			c-0.037,0.211-0.111,0.558-0.221,1.042c-0.108,0.483-0.353,1.437-0.729,2.857H16.697z"/>
 74  		<path fill="#FFFFFF" d="M28.423,9.552h-2.449V2.488H23.76V0.485h6.871v2.003h-2.208V9.552z"/>
 75  		<path fill="#FFFFFF" d="M39.037,9.552h-2.449V2.488h-2.214V0.485h6.871v2.003h-2.208V9.552z"/>
 76  		<path fill="#FFFFFF" d="M51.035,9.552h-5.382V0.485h5.382V2.45h-2.933v1.427h2.716v1.966h-2.716v1.711h2.933V9.552z"/>
 77  		<path fill="#FFFFFF" d="M58.184,6.253v3.299h-2.449V0.485h2.97c2.464,0,3.696,0.893,3.696,2.679c0,1.05-0.513,1.862-1.538,2.437
 78  			l2.642,3.951h-2.777l-1.922-3.299H58.184z M58.184,4.41h0.459c0.855,0,1.284-0.378,1.284-1.135c0-0.625-0.42-0.937-1.26-0.937
 79  			h-0.483V4.41z"/>
 80  		<path fill="#FFFFFF" d="M76.072,9.552H72.86L69.55,3.164h-0.057c0.079,1.004,0.118,1.771,0.118,2.301v4.086h-2.17V0.485h3.2
 81  			l3.299,6.301h0.037c-0.059-0.914-0.086-1.648-0.086-2.202V0.485h2.183v9.066H76.072z"/>
 82  		<path fill="#FFFFFF" d="M83.557,9.552h-2.412V0.485h5.356V2.45h-2.944v1.73h2.716v1.965h-2.716V9.552z"/>
 83  		<path fill="#FFFFFF" d="M91.102,9.552V0.485h2.449v7.088h3.49v1.979H91.102z"/>
 84  		<path fill="#FFFFFF" d="M104.842,3.846l1.562-3.361h2.654l-2.983,5.525v3.541h-2.468V6.085l-2.983-5.6h2.667L104.842,3.846z"/>
 85  	</g>
 86  </g>
 87  </svg>

```
  * file:///opt/input/source/src/main/webapp/bower_components/patternfly/src/img/bg-navbar-pf-alt.svg
      * `beans_1_1.xsd`: In the root tag, replace the `version` attribute value with `3.0`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="utf-8"?>
  2  <!-- Generator: Adobe Illustrator 16.0.4, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
  3  <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
  4  <svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
  5  	 width="615.598px" height="57px" viewBox="25.562 0 615.598 57" enable-background="new 25.562 0 615.598 57" xml:space="preserve"
  6  	>
  7  <polygon opacity="0.1" fill="#FFFFFF" enable-background="new    " points="566.242,56.969 623.205,0 641.16,0 584.68,56.969 "/>
  8  <polygon opacity="0.1" fill="#FFFFFF" enable-background="new    " points="25.562,57 25.562,0 611.034,0 554.554,56.95 "/>
  9  </svg>

```
  * file:///opt/input/source/src/main/webapp/bower_components/patternfly/src/img/brand-alt.svg
      * `beans_1_1.xsd`: In the root tag, replace the `version` attribute value with `3.0`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="utf-8"?>
  2  <!-- Generator: Adobe Illustrator 16.0.4, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
  3  <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
  4  <svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
  5  	 width="324px" height="11px" viewBox="1.145 0.538 324 11" enable-background="new 1.145 0.538 324 11" xml:space="preserve">
  6  <g>
  7  	<g>
  8  		<path fill="#FFFFFF" d="M147.351,11.368h-5.899V0.789h5.899V1.88h-4.666v3.408h4.386v1.085h-4.386v3.894h4.666V11.368z"/>
  9  		<path fill="#FFFFFF" d="M158.252,11.368h-1.399l-5.786-8.882h-0.056c0.075,1.044,0.115,2,0.115,2.868v6.014h-1.136V0.789h1.39
 10  			l5.768,8.84h0.054c-0.007-0.129-0.027-0.548-0.062-1.258c-0.034-0.702-0.047-1.205-0.034-1.515V0.789h1.149v10.576h-0.004V11.368
 11  			L158.252,11.368z"/>
 12  		<path fill="#FFFFFF" d="M164.719,11.368h-1.23V1.882h-3.349V0.789h7.932V1.88h-3.349v9.486h-0.002v0.002H164.719z"/>
 13  		<path fill="#FFFFFF" d="M175.852,11.368h-5.893V0.789h5.893V1.88h-4.662v3.408h4.386v1.085h-4.386v3.894h4.662V11.368z"/>
 14  		<path fill="#FFFFFF" d="M179.727,6.967v4.398h-1.231V0.789h2.903c1.298,0,2.253,0.247,2.875,0.742
 15  			c0.62,0.498,0.931,1.247,0.931,2.245c0,1.396-0.708,2.344-2.131,2.838l2.879,4.753h-1.459l-2.562-4.403h-2.206v0.004H179.727z
 16  			 M179.727,5.913h1.687c0.868,0,1.503-0.172,1.911-0.517c0.404-0.346,0.608-0.863,0.608-1.553c0-0.703-0.204-1.205-0.618-1.515
 17  			c-0.41-0.308-1.075-0.46-1.985-0.46h-1.6v4.046h-0.005V5.913H179.727z"/>
 18  		<path fill="#FFFFFF" d="M194.663,3.873c0,1.068-0.363,1.894-1.093,2.473c-0.73,0.576-1.781,0.861-3.141,0.861h-1.246v4.161h-1.228
 19  			V0.789h2.743C193.342,0.789,194.663,1.813,194.663,3.873z M189.184,6.148h1.111c1.085,0,1.88-0.176,2.367-0.525
 20  			c0.483-0.354,0.729-0.917,0.729-1.696c0-0.697-0.227-1.216-0.687-1.565c-0.46-0.337-1.175-0.511-2.142-0.511h-1.376v4.298H189.184
 21  			z"/>
 22  		<path fill="#FFFFFF" d="M198.404,6.967v4.398h-1.233V0.789h2.902c1.298,0,2.254,0.247,2.879,0.742
 23  			c0.619,0.498,0.933,1.247,0.933,2.245c0,1.396-0.711,2.344-2.13,2.838l2.875,4.753h-1.456l-2.561-4.403h-2.206v0.003
 24  			L198.404,6.967L198.404,6.967z M198.404,5.913h1.686c0.868,0,1.502-0.172,1.911-0.517c0.403-0.346,0.608-0.863,0.608-1.553
 25  			c0-0.703-0.205-1.205-0.616-1.515c-0.411-0.308-1.072-0.46-1.987-0.46h-1.598v4.046L198.404,5.913L198.404,5.913z"/>
 26  		<path fill="#FFFFFF" d="M206.632,11.368V0.789h1.229v10.576h-1.229V11.368z"/>
 27  		<path fill="#FFFFFF" d="M217.028,8.552c0,0.934-0.338,1.66-1.012,2.181c-0.677,0.524-1.592,0.78-2.751,0.78
 28  			c-1.256,0-2.218-0.162-2.894-0.482V9.84c0.431,0.184,0.906,0.329,1.418,0.432c0.51,0.105,1.021,0.157,1.521,0.157
 29  			c0.821,0,1.435-0.155,1.85-0.463c0.418-0.312,0.622-0.75,0.622-1.297c0-0.367-0.075-0.672-0.223-0.904
 30  			c-0.145-0.233-0.386-0.453-0.733-0.647c-0.345-0.197-0.871-0.425-1.572-0.675c-0.986-0.35-1.689-0.769-2.112-1.251
 31  			c-0.426-0.481-0.634-1.112-0.634-1.888c0-0.814,0.307-1.463,0.922-1.946c0.614-0.48,1.424-0.724,2.435-0.724
 32  			c1.05,0,2.02,0.195,2.897,0.58l-0.382,1.068c-0.876-0.362-1.726-0.548-2.549-0.548c-0.65,0-1.158,0.138-1.53,0.418
 33  			c-0.365,0.279-0.546,0.668-0.546,1.167c0,0.369,0.068,0.666,0.202,0.9c0.14,0.235,0.366,0.449,0.685,0.644
 34  			c0.323,0.194,0.812,0.411,1.475,0.646c1.111,0.395,1.874,0.82,2.291,1.276C216.819,7.239,217.028,7.829,217.028,8.552z"/>
 35  		<path fill="#FFFFFF" d="M225.391,11.368h-5.898V0.789h5.898V1.88h-4.668v3.408h4.391v1.085h-4.391v3.894h4.668V11.368z"/>
 36  		<path fill="#FFFFFF" d="M238.827,11.368l-1.317-3.364h-4.241l-1.303,3.364h-1.244l4.184-10.623h1.031l4.16,10.623H238.827z
 37  			 M237.123,6.895l-1.229-3.276c-0.159-0.417-0.328-0.926-0.491-1.526c-0.109,0.462-0.255,0.971-0.455,1.526l-1.246,3.276H237.123z"
 38  			/>
 39  		<path fill="#FFFFFF" d="M248.56,3.873c0,1.068-0.366,1.894-1.097,2.473c-0.733,0.576-1.779,0.861-3.137,0.861h-1.245v4.161h-1.233
 40  			V0.789h2.745C247.241,0.789,248.56,1.813,248.56,3.873z M243.083,6.148h1.104c1.09,0,1.881-0.176,2.37-0.525
 41  			c0.479-0.354,0.73-0.917,0.73-1.696c0-0.697-0.229-1.216-0.689-1.565c-0.46-0.337-1.17-0.511-2.142-0.511h-1.374V6.148
 42  			L243.083,6.148z"/>
 43  		<path fill="#FFFFFF" d="M257.782,3.873c0,1.068-0.371,1.894-1.098,2.473c-0.733,0.576-1.779,0.861-3.139,0.861h-1.245v4.161
 44  			h-1.232V0.789h2.743C256.457,0.789,257.782,1.813,257.782,3.873z M252.298,6.148h1.108c1.094,0,1.884-0.176,2.368-0.525
 45  			c0.487-0.354,0.729-0.917,0.729-1.696c0-0.697-0.228-1.216-0.685-1.565c-0.46-0.337-1.172-0.511-2.142-0.511H252.3v4.298H252.298z
 46  			"/>
 47  		<path fill="#FFFFFF" d="M260.287,11.368V0.789h1.235v9.463h4.659v1.113h-5.895V11.368L260.287,11.368z"/>
 48  		<path fill="#FFFFFF" d="M268.277,11.368V0.789h1.232v10.576h-1.232V11.368z"/>
 49  		<path fill="#FFFFFF" d="M277.234,1.736c-1.158,0-2.079,0.386-2.753,1.159c-0.674,0.776-1.009,1.833-1.009,3.181
 50  			c0,1.385,0.326,2.454,0.976,3.209c0.648,0.75,1.575,1.132,2.777,1.132c0.738,0,1.582-0.13,2.526-0.396v1.077
 51  			c-0.732,0.276-1.639,0.414-2.712,0.414c-1.558,0-2.761-0.479-3.61-1.427c-0.844-0.938-1.27-2.284-1.27-4.027
 52  			c0-1.089,0.205-2.042,0.61-2.865c0.407-0.819,0.996-1.452,1.766-1.896c0.77-0.444,1.676-0.666,2.716-0.666
 53  			c1.109,0,2.077,0.203,2.909,0.609l-0.521,1.057C278.843,1.922,278.037,1.736,277.234,1.736z"/>
 54  		<path fill="#FFFFFF" d="M289,11.368l-1.317-3.364h-4.243l-1.298,3.364h-1.245l4.18-10.623h1.035l4.162,10.623H289z M287.301,6.895
 55  			l-1.229-3.276c-0.162-0.417-0.327-0.926-0.492-1.526c-0.106,0.462-0.26,0.971-0.455,1.526l-1.248,3.276H287.301z"/>
 56  		<path fill="#FFFFFF" d="M295.279,11.368h-1.228V1.882h-3.351V0.789h7.931V1.88h-3.348v9.486h-0.005V11.368z"/>
 57  		<path fill="#FFFFFF" d="M300.525,11.368V0.789h1.229v10.576h-1.229V11.368z"/>
 58  		<path fill="#FFFFFF" d="M314.132,6.063c0,1.693-0.428,3.024-1.283,3.993c-0.854,0.975-2.043,1.457-3.57,1.457
 59  			c-1.56,0-2.761-0.479-3.61-1.433c-0.844-0.953-1.27-2.297-1.27-4.033c0-1.721,0.428-3.06,1.277-4.002
 60  			c0.844-0.948,2.057-1.426,3.612-1.426c1.525,0,2.706,0.482,3.565,1.45C313.709,3.033,314.132,4.363,314.132,6.063z M305.705,6.063
 61  			c0,1.432,0.301,2.519,0.91,3.258c0.614,0.74,1.501,1.114,2.662,1.114c1.175,0,2.06-0.377,2.658-1.109
 62  			c0.598-0.743,0.893-1.832,0.893-3.265c0-1.424-0.295-2.503-0.89-3.239c-0.592-0.737-1.478-1.104-2.645-1.104
 63  			c-1.17,0-2.06,0.37-2.675,1.109C306.009,3.572,305.705,4.649,305.705,6.063z"/>
 64  		<path fill="#FFFFFF" d="M325.053,11.368h-1.404l-5.778-8.882h-0.06c0.074,1.044,0.113,2,0.113,2.868v6.014h-1.141V0.789h1.393
 65  			l5.765,8.843h0.059c-0.015-0.131-0.03-0.551-0.066-1.259c-0.032-0.701-0.05-1.205-0.034-1.517V0.789h1.148v10.578h0.008v0.002
 66  			H325.053z"/>
 67  	</g>
 68  	<g>
 69  		<path fill="#FFFFFF" d="M9.094,4.065c0,1.224-0.36,2.17-1.083,2.837C7.29,7.571,6.264,7.903,4.938,7.903H4.104v3.634H1.145V0.583
 70  			h3.792c1.383,0,2.422,0.302,3.117,0.906C8.747,2.094,9.094,2.953,9.094,4.065z M4.104,5.49h0.541c0.444,0,0.797-0.125,1.059-0.375
 71  			c0.262-0.25,0.394-0.595,0.394-1.035c0-0.739-0.41-1.109-1.23-1.109H4.104V5.49z"/>
 72  		<path fill="#FFFFFF" d="M21.32,11.537l-0.54-2.053h-3.557l-0.555,2.053h-3.251l3.573-11h3.949l3.619,11H21.32z M20.166,7.056
 73  			l-0.472-1.799c-0.111-0.399-0.244-0.916-0.402-1.55c-0.157-0.634-0.261-1.088-0.311-1.363c-0.045,0.255-0.134,0.674-0.267,1.259
 74  			c-0.13,0.583-0.427,1.736-0.881,3.451h2.333V7.056z"/>
 75  		<path fill="#FFFFFF" d="M34.333,11.537h-2.959V3.002h-2.675V0.583h8.302v2.419h-2.668V11.537z"/>
 76  		<path fill="#FFFFFF" d="M47.157,11.537h-2.958V3.002h-2.675V0.583h8.301v2.419h-2.668V11.537z"/>
 77  		<path fill="#FFFFFF" d="M61.653,11.537H55.15V0.583h6.503v2.374h-3.544v1.724h3.281v2.375h-3.281v2.067h3.544V11.537z"/>
 78  		<path fill="#FFFFFF" d="M70.291,7.552v3.985h-2.959V0.583h3.588c2.977,0,4.466,1.079,4.466,3.237c0,1.268-0.62,2.25-1.858,2.943
 79  			l3.192,4.774h-3.355l-2.322-3.985H70.291z M70.291,5.325h0.554c1.033,0,1.552-0.457,1.552-1.371c0-0.755-0.508-1.132-1.522-1.132
 80  			h-0.583V5.325z"/>
 81  		<path fill="#FFFFFF" d="M91.903,11.537h-3.881l-3.999-7.718h-0.069c0.095,1.213,0.143,2.139,0.143,2.78v4.936h-2.622V0.583h3.866
 82  			l3.986,7.612h0.044c-0.071-1.103-0.104-1.99-0.104-2.659V0.583h2.637v10.953h-0.002V11.537z"/>
 83  		<path fill="#FFFFFF" d="M100.946,11.537h-2.914V0.583h6.471v2.374h-3.557v2.09h3.282v2.374h-3.282V11.537z"/>
 84  		<path fill="#FFFFFF" d="M110.062,11.537V0.583h2.959v8.564h4.217v2.391H110.062z"/>
 85  		<path fill="#FFFFFF" d="M126.663,4.643l1.887-4.061h3.207l-3.604,6.675v4.277h-2.982V7.348l-3.604-6.765h3.222L126.663,4.643z"/>
 86  	</g>
 87  </g>
 88  </svg>

```
  * file:///opt/input/source/src/main/webapp/bower_components/patternfly/src/img/logo.svg
      * `beans_1_1.xsd`: In the root tag, replace the `version` attribute value with `3.0`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="utf-8"?>
  2  <!-- Generator: Adobe Illustrator 16.0.3, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
  3  <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
  4  <svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
  5  	 width="73px" height="69px" viewBox="0 0 73 69" enable-background="new 0 0 73 69" xml:space="preserve">
  6  <g>
  7  	<linearGradient id="SVGID_1_" gradientUnits="userSpaceOnUse" x1="36.2046" y1="2.1504" x2="36.2046" y2="68.6623">
  8  		<stop  offset="0" style="stop-color:#60EFFF"/>
  9  		<stop  offset="1" style="stop-color:#1F89C7"/>
 10  	</linearGradient>
 11  	<path fill="url(#SVGID_1_)" d="M36.287,0.137l0.008-0.063l-0.031,0.039l-0.012-0.012L36.262,0l-0.057,0.056L36.148,0l0.011,0.101
 12  		l-0.013,0.012l-0.03-0.039l0.007,0.063L0,35.447l14.307,20.267l11.05-2.538l10.848,15.255l10.85-15.255l11.05,2.538l8.861-12.554
 13  		l5.444-7.713L36.287,0.137z M35.108,4.282L30.174,50.52l-9.642-13.151L35.108,4.282z M20.059,36.725l-6.068-8.277L35.057,2.683
 14  		L20.059,36.725z M29.967,51.407l-4.313,0.99l-7.251-10.193l1.807-4.104L29.967,51.407z M36.092,2.051l0.113-0.258l0.114,0.257
 15  		l5.102,49.711l-0.015-0.01l-4.999,7.387l-5.409-7.396l-0.007,0.004L36.092,2.051z M42.237,50.521L37.303,4.281l14.576,33.087
 16  		L42.237,50.521z M52.201,38.101l1.808,4.104l-7.251,10.193l-4.312-0.99L52.201,38.101z M37.355,2.684L58.42,28.448l-6.067,8.277
 17  		L37.355,2.684z M14.605,54.935L0.907,35.53L32.779,4.374L13.114,28.425l6.623,9.03l-2.127,4.83l7.312,10.28L14.605,54.935z
 18  		 M36.205,67.235L26.086,53.009l4.326-0.992l0.072,0.099l-0.045,0.034l5.988,8.191l5.552-8.201l-0.048-0.032L42,52.017l4.324,0.992
 19  		L36.205,67.235z M66.4,42.762l-8.594,12.173l-10.317-2.369l7.312-10.28l-2.127-4.83l6.622-9.03L39.633,4.374L71.504,35.53
 20  		L66.4,42.762z"/>
 21  </g>
 22  </svg>

```
  * file:///opt/input/source/src/main/webapp/bower_components/angular-patternfly/dist/docs/img/RH_Atomic-Logo-NoText.svg
      * `beans_1_1.xsd`: In the root tag, replace the `version` attribute value with `3.0`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="utf-8"?>
  2  <!-- Generator: Adobe Illustrator 19.2.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
  3  <svg version="1.1"
  4  	 id="svg4242" xmlns:cc="http://creativecommons.org/ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
  5  	 xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 200 199.7"
  6  	 style="enable-background:new 0 0 200 199.7;" xml:space="preserve">
  7  <style type="text/css">
  8  	.st0{fill:#00B9E4;}
  9  	.st1{fill:#0088CE;}
 10  </style>
 11  <g>
 12  	<g>
 13  		<path class="st0" d="M88.1,136.7c-0.4,0.3-0.7,0.6-1,0.8c-2.5,2.5-4.9,4.8-7.1,6.9c1.4,0.8,2.4,2.1,3,3.7c2.7-2.4,5.5-5,8.4-7.9
 14  			c0.6-0.6,1.1-2.2-0.1-3.3C90.4,136.2,89,136,88.1,136.7z"/>
 15  		<path class="st0" d="M60.3,77.4c0.7,1.1,2.2,1.5,3.3,0.7c1.2-0.8,1-2.4,0.6-2.9C54.5,58.7,50.1,46,54,43c2.4-1.9,7.6,0.2,14.5,5.3
 16  			c0.7-2.2,2.3-4,4.3-5c-11.1-8.3-19.9-11.8-24-8.6c-5.8,4.5-1,21.1,11.1,42.1C60,77,60.2,77.2,60.3,77.4z"/>
 17  		<path class="st0" d="M140.3,123.2c2.9-0.4,5.7-0.8,8.3-1.3l0,0l0,0l0,0c0.7-0.7,1.2-1.7,1.2-2.8c0-1.8-1.3-3.3-2.9-3.7l0,0
 18  			c-3.2,0.5-6.7,1-10.4,1.4l0,0l0,0c-5.7-9.3-12.7-19.4-20.6-29.5c-2.3-3.2-7.4-9.1-11.3-13.6l0.1-0.1C124,52.2,141,39.1,146,42.9
 19  			c3.8,3-0.5,15.6-10.3,32.2c-0.3,0.5-0.6,2.1,0.6,2.9c1.2,0.8,2.7,0.4,3.3-0.7c0.1-0.2,0.3-0.4,0.4-0.6c12-21,16.9-37.6,11.1-42.1
 20  			c-7-5.5-27.8,8.6-50.3,32.9c0,0-0.3,0.4-1,1.1c-0.6-0.6-1-1.1-1-1.1c-4.9-5.2-9.7-10.1-14.2-14.2l0,0c-0.1-0.1-0.1-0.1-0.1-0.1
 21  			c-0.2-0.1-0.4-0.1-0.6-0.1c-2.1,0-3.8,1.7-3.8,3.8c0,0.5,0.1,1.1,0.3,1.5l0,0c4.7,4.4,9.6,9.5,14.8,15.2l0.1,0.1
 22  			c-4,4.5-9,10.4-11.3,13.6c-7.9,10.1-14.9,20.1-20.6,29.5c-21.9-2.5-36.6-7.1-36.5-12.4c0-5.4,15.6-10.1,38.4-12.4
 23  			c0.3-0.1,0.4-0.1,0.7-0.1c1.2-0.2,1.9-1.4,1.8-2.3c0-1.2-0.9-2.4-2.6-2.4c-28.3,3.2-48,10.2-48,18.3c-0.1,7.6,17.2,14.2,42.6,17.7
 24  			c-11.9,20.9-16.7,37.3-10.9,41.8c4.2,3.3,13.3-0.4,24.7-9.1l0,0c0,0,0,0,0.1,0c0.1-0.3,0.1-0.5,0.1-0.8c0-1.5-1.3-2.8-2.8-2.8
 25  			c-0.2,0-0.3,0-0.4,0.1l0,0l0,0c-7.1,5.2-12.4,7.5-14.8,5.6c-4-3.1,0.8-16.4,11.4-33.8c9.8,1.1,20.7,1.6,32.1,1.7l0,0
 26  			c0.2,0,0.3,0,0.5,0l0,0l0,0c0.1,0,0.3,0,0.4,0l0,0h0.1l0,0h0.1c0.1,0,0.3,0,0.4,0c0.2,0,0.3,0,0.5,0l0,0
 27  			c11.4-0.1,22.3-0.6,32.1-1.7c10.5,17.5,15.4,30.8,11.4,33.8c-4.1,3.2-16.5-5.2-31.5-20.4c-0.3-0.3-0.6-0.6-1-0.8
 28  			c-1-0.7-2.3-0.5-3,0.2c-1.2,1.2-0.8,2.7-0.1,3.3c19.4,19.2,36.3,29.6,42.5,24.8C157,160.5,152.2,144.1,140.3,123.2L140.3,123.2z
 29  			 M100.3,118.8c-0.1,0-0.2,0-0.3,0s-0.2,0-0.3,0c-10.2,0-20-0.4-28.7-1.2c5.2-8.2,11.5-16.9,18.6-25.9c3.2-4,6.4-7.9,9.5-11.5l0,0
 30  			c0.3-0.4,0.6-0.7,0.9-1.1c0.3,0.4,0.6,0.7,0.9,1.1l0,0c3.1,3.7,6.3,7.5,9.5,11.5c7.1,9,13.3,17.8,18.6,25.9l0,0
 31  			C120.2,118.4,110.5,118.8,100.3,118.8z"/>
 32  		<path class="st0" d="M134.9,87.2c-1.7-0.1-2.6,1.2-2.6,2.4c-0.1,1,0.6,2.1,1.8,2.3c0.2,0.1,0.4,0.1,0.7,0.1
 33  			c22.8,2.4,38.3,7,38.4,12.4c0,1.9-1.9,3.7-5.4,5.4c1.1,1.7,1.8,3.9,1.8,6.1c0,0.2,0,0.4-0.1,0.5c8.5-3.2,13.3-7,13.3-11
 34  			C182.9,97.3,163.2,90.4,134.9,87.2z"/>
 35  	</g>
 36  	<g>
 37  		<path class="st1" d="M76.6,42.4c-4.7,0-8.6,3.8-8.6,8.6c0,4.7,3.8,8.6,8.6,8.6c1.4,0,2.8-0.4,3.9-1c-0.2-0.5-0.3-1-0.3-1.5
 38  			c0-2.1,1.7-3.8,3.8-3.8c0.2,0,0.4,0,0.6,0.1c0.1,0.1,0.1,0.1,0.1,0.1c0.2-0.8,0.4-1.6,0.4-2.4C85.2,46.2,81.4,42.4,76.6,42.4z"/>
 39  		<path class="st1" d="M99.1,67.6c-0.4-0.4-0.7-0.8-1.2-1.2l-4.4,5.3c0.6,0.7,1.3,1.4,1.9,2.1l0.1,0.1c1.9-2.2,3.6-4.1,4.6-5.2
 40  			C99.4,68,99.1,67.6,99.1,67.6z"/>
 41  		<path class="st1" d="M100,79.1L100,79.1c0.3,0.4,0.6,0.7,0.9,1.1l0,0c1,1.2,2,2.3,3,3.5l4.6-5.4c-1.3-1.5-2.6-3-3.8-4.4L100,79.1z
 42  			"/>
 43  		<path class="st1" d="M158.3,104.7c-6,0-11,4.8-11.3,10.7c1.7,0.4,2.9,1.9,2.9,3.7c0,1.1-0.5,2.1-1.2,2.8l0,0
 44  			c2,3.2,5.6,5.4,9.6,5.4c6.2,0,11.3-5.1,11.3-11.3C169.6,109.7,164.5,104.7,158.3,104.7z"/>
 45  		<path class="st1" d="M59.7,123.2c-1.2,2.1-2.3,4.1-3.3,6.1l7,0.9c1.1-2,2.3-4,3.5-6.1L59.7,123.2L59.7,123.2z"/>
 46  		<path class="st1" d="M71,117.6c0.4-0.7,0.9-1.4,1.4-2.1l-7.5-0.9c-0.5,0.7-1,1.5-1.4,2.2l0,0L71,117.6L71,117.6z"/>
 47  		<path class="st1" d="M136.6,116.9c-0.5-0.8-1-1.6-1.5-2.3l-7.5,1c0.5,0.7,1,1.5,1.4,2.2l0,0l0,0L136.6,116.9L136.6,116.9z"/>
 48  		<path class="st1" d="M133.1,124.1L133.1,124.1c1.2,2.1,2.4,4.1,3.5,6l7-0.9c-1-2-2.1-4-3.3-6L133.1,124.1z"/>
 49  		<path class="st1" d="M76.6,143.5c-3.7,0-6.6,3-6.6,6.6c0,0.8,0.2,1.5,0.4,2.2l0,0c0.1,0,0.3-0.1,0.4-0.1c1.5,0,2.8,1.3,2.8,2.8
 50  			c0,0.3-0.1,0.5-0.1,0.8c0,0,0,0-0.1,0c1,0.5,2,0.8,3.2,0.8c3.7,0,6.6-3,6.6-6.6C83.2,146.5,80.3,143.5,76.6,143.5z"/>
 51  	</g>
 52  </g>
 53  </svg>

```
  * file:///opt/input/source/src/main/webapp/bower_components/angular-patternfly/dist/docs/img/OpenShift-Logo-Text.svg
      * `beans_1_1.xsd`: In the root tag, replace the `version` attribute value with `3.0`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="utf-8"?>
  2  <!-- Generator: Adobe Illustrator 19.2.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
  3  <svg version="1.1"
  4  	 id="svg4242" xmlns:cc="http://creativecommons.org/ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
  5  	 xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 200 199.7"
  6  	 style="enable-background:new 0 0 200 199.7;" xml:space="preserve">
  7  <style type="text/css">
  8  	.st0{fill:#C32034;}
  9  	.st1{fill:#DB212F;}
 10  	.st2{fill:#EA2227;}
 11  	.st3{fill:#AD213A;}
 12  	.st4{fill:#BA2034;}
 13  	.st5{fill:#231F20;}
 14  </style>
 15  <g>
 16  	<g id="g3921">
 17  		<g id="g3927" transform="translate(304.96 416.03)">
 18  			<path id="path3929" class="st0" d="M-238.7-345.3l-23.3,8.5c0.3,3.8,0.9,7.5,1.9,11.1l22.1-8C-238.7-337.7-239-341.5-238.7-345.3
 19  				"/>
 20  		</g>
 21  		<g id="g3931" transform="translate(418.75 444.5)">
 22  			<path id="path3933" class="st0" d="M-249.5-399.6c-1.6-3.3-3.5-6.6-5.6-9.6l-23.3,8.5c2.7,2.8,5,5.9,6.9,9.2
 23  				C-271.7-391.6-249.5-399.6-249.5-399.6z"/>
 24  		</g>
 25  		<g id="g3935" transform="translate(362.11 451.79)">
 26  			<path id="path3937" class="st1" d="M-244.2-413.5c4.8,2.2,9,5.4,12.6,9l23.3-8.5c-6.4-9-15.3-16.6-26-21.6
 27  				c-33.3-15.5-73-1.1-88.5,32.2c-5,10.8-6.9,22.2-6,33.3l23.3-8.5c0.4-5.1,1.6-10.1,3.9-15C-291.6-414.2-265.8-423.5-244.2-413.5"
 28  				/>
 29  		</g>
 30  		<g id="g3939" transform="translate(282.86 395.05)">
 31  			<path id="path3941" class="st2" d="M-236.6-305.4l-22.1,8c2,8,5.6,15.7,10.4,22.6l23.2-8.5C-231-289.4-235-297.1-236.6-305.4"/>
 32  		</g>
 33  		<g id="g3943" transform="translate(389.56 404.75)">
 34  			<path id="path3945" class="st1" d="M-246.7-323.9c-0.4,5.1-1.7,10.1-3.9,15c-10.1,21.6-35.9,31.1-57.5,20.9
 35  				c-4.8-2.2-9-5.4-12.6-9l-23.2,8.5c6.4,9,15.2,16.6,26,21.6c33.3,15.5,73,1.1,88.5-32.2c5-10.8,6.9-22.2,6-33.3L-246.7-323.9
 36  				L-246.7-323.9z"/>
 37  		</g>
 38  		<g id="g3947" transform="translate(395.89 436.18)">
 39  			<path id="path3949" class="st2" d="M-247.3-383.8l-22.1,8c4.1,7.4,6.1,15.9,5.4,24.4l23.2-8.5
 40  				C-241.5-368.1-243.7-376.2-247.3-383.8"/>
 41  		</g>
 42  		<g id="g3951" transform="translate(279.22 406.66)">
 43  			<path id="path3953" class="st3" d="M-236.2-327.6l23.2-8.4l-0.1,4.6l-22.4,8.3C-235.5-323-236.2-327.6-236.2-327.6z"/>
 44  		</g>
 45  		<g id="g3955" transform="translate(386.73 445.86)">
 46  			<path id="path3957" class="st3" d="M-246.5-402.2l23.6-8l2.5,3.6l-22.9,8C-243.4-398.5-246.5-402.2-246.5-402.2z"/>
 47  		</g>
 48  		<g id="g3959" transform="translate(282.04 365.71)">
 49  			<path id="path3961" class="st4" d="M-236.5-249.5l23.2-8.3l7,6.5l-24.4,9C-230.6-242.3-236.5-249.5-236.5-249.5z"/>
 50  		</g>
 51  		<g id="g3963" transform="translate(415.68 414.03)">
 52  			<path id="path3965" class="st4" d="M-249.2-341.5l-23.6,8.4l-1.7,9.3l25.2-8.8C-249.4-332.7-249.2-341.5-249.2-341.5z"/>
 53  		</g>
 54  	</g>
 55  	<g>
 56  		<g id="text3967" transform="scale(1,-1)">
 57  			<path id="path3359" class="st5" d="M20.5-188.8c-1.2,0-2.2,0.1-3.2,0.4c-0.9,0.3-1.7,0.7-2.5,1.2c-0.7,0.5-1.3,1.2-1.8,1.9
 58  				c-0.5,0.7-0.9,1.5-1.2,2.3c-0.3,0.9-0.6,1.7-0.7,2.6c-0.1,0.9-0.2,1.8-0.2,2.7s0.1,1.8,0.2,2.7c0.1,0.9,0.4,1.8,0.7,2.6
 59  				c0.3,0.9,0.7,1.6,1.2,2.3c0.5,0.7,1.1,1.4,1.8,1.9c0.7,0.5,1.5,0.9,2.5,1.2s2,0.4,3.2,0.4c1.2,0,2.2-0.1,3.1-0.4
 60  				c0.9-0.3,1.7-0.7,2.5-1.2c0.7-0.5,1.3-1.2,1.8-1.9c0.5-0.7,0.9-1.5,1.2-2.3c0.3-0.8,0.6-1.7,0.7-2.6c0.1-0.9,0.2-1.8,0.2-2.7
 61  				s-0.1-1.8-0.2-2.7c-0.1-0.9-0.4-1.7-0.7-2.6c-0.3-0.8-0.7-1.6-1.2-2.3c-0.5-0.7-1.1-1.4-1.8-1.9c-0.7-0.5-1.5-0.9-2.5-1.2
 62  				C22.7-188.6,21.7-188.8,20.5-188.8 M20.5-184.7c0.9,0,1.8,0.2,2.5,0.7c0.7,0.4,1.2,1,1.6,1.7c0.4,0.7,0.7,1.4,0.9,2.3
 63  				c0.2,0.9,0.3,1.7,0.3,2.5c0,0.6-0.1,1.1-0.1,1.7c-0.1,0.6-0.2,1.2-0.4,1.7c-0.1,0.5-0.4,1-0.7,1.5c-0.3,0.5-0.6,0.9-1,1.2
 64  				c-0.4,0.4-0.9,0.7-1.4,0.9c-0.5,0.2-1.1,0.3-1.7,0.3c-0.7,0-1.2-0.1-1.7-0.3s-0.9-0.5-1.4-0.9c-0.4-0.4-0.7-0.8-1-1.2
 65  				c-0.3-0.5-0.5-1-0.7-1.5c-0.1-0.5-0.3-1.1-0.4-1.7s-0.1-1.1-0.1-1.6c0-0.8,0.1-1.7,0.3-2.5c0.2-0.9,0.5-1.6,0.9-2.3
 66  				c0.4-0.7,0.9-1.2,1.6-1.7C18.7-184.5,19.5-184.7,20.5-184.7"/>
 67  			<path id="path3361" class="st5" d="M35.4-188.4v21.7h9.3c1.4,0,2.5-0.2,3.5-0.6c0.9-0.4,1.7-0.9,2.3-1.6c0.6-0.7,1-1.4,1.2-2.2
 68  				c0.3-0.8,0.4-1.7,0.4-2.5c0-0.5-0.1-1.1-0.2-1.6c-0.1-0.5-0.3-1.1-0.6-1.6c-0.2-0.5-0.6-1-0.9-1.4s-0.9-0.9-1.4-1.2
 69  				c-0.6-0.4-1.2-0.6-1.9-0.8s-1.5-0.3-2.4-0.3h-5.1v-8H35.4 M44.9-176.4c0.5,0,1,0.1,1.4,0.3c0.4,0.1,0.7,0.4,0.9,0.7
 70  				c0.2,0.3,0.4,0.6,0.5,0.9c0.1,0.4,0.1,0.7,0.1,1c0,0.3-0.1,0.7-0.1,0.9c-0.1,0.4-0.2,0.7-0.4,0.9c-0.2,0.3-0.5,0.5-0.9,0.7
 71  				c-0.4,0.2-0.9,0.3-1.4,0.3h-5.3v-5.8H44.9"/>
 72  			<path id="path3363" class="st5" d="M57.9-188.4v21.7h14.8v-4H62.1v-4.6h6.2v-4h-6.2v-5.2h11.3v-4H57.9"/>
 73  			<path id="path3365" class="st5" d="M93.1-188.4l-8.6,12.7c-0.1,0.2-0.3,0.4-0.4,0.8c-0.1,0.3-0.3,0.6-0.4,0.9
 74  				c0-0.2,0.1-0.5,0.1-0.8c0-0.3,0-0.6,0-0.8v-12.7h-4.2v21.7h3.9l8.4-12.5c0.1-0.2,0.3-0.4,0.4-0.7c0.1-0.3,0.3-0.6,0.4-0.9
 75  				c0,0.3-0.1,0.6-0.1,0.9s0,0.6,0,0.7v12.5h4.1v-21.7L93.1-188.4"/>
 76  		</g>
 77  		<g id="text3971" transform="scale(1,-1)">
 78  			<path id="path3348" class="st5" d="M114.3-171.6c-0.1,0.3-0.3,0.6-0.6,0.9c-0.2,0.3-0.5,0.5-0.9,0.7c-0.4,0.2-0.7,0.4-1.2,0.4
 79  				c-0.4,0.1-0.9,0.1-1.4,0.1c-1,0-1.9-0.2-2.5-0.7c-0.6-0.4-0.9-1.1-0.9-2c0-0.5,0.1-0.9,0.5-1.3c0.3-0.4,0.7-0.7,1.3-0.9
 80  				c0.5-0.3,1.1-0.5,1.8-0.7c0.7-0.2,1.4-0.4,2-0.7c0.7-0.3,1.4-0.6,2-0.9c0.7-0.4,1.3-0.8,1.8-1.3c0.5-0.5,0.9-1.1,1.3-1.8
 81  				c0.3-0.7,0.5-1.5,0.5-2.5c0-1-0.2-2-0.6-2.8c-0.4-0.8-0.9-1.4-1.6-2c-0.7-0.6-1.4-0.9-2.4-1.2c-0.9-0.3-1.9-0.4-2.9-0.4
 82  				c-0.9,0-1.9,0.1-2.8,0.4s-1.6,0.6-2.3,1c-0.7,0.4-1.2,1-1.7,1.7s-0.9,1.4-1.2,2.2l3,1.1c0.2-0.5,0.5-0.9,0.8-1.3
 83  				c0.4-0.4,0.7-0.7,1.2-1c0.4-0.3,0.9-0.5,1.4-0.7c0.5-0.1,1.1-0.2,1.7-0.2c0.6,0,1.1,0.1,1.6,0.2c0.5,0.1,0.9,0.4,1.2,0.7
 84  				c0.4,0.3,0.6,0.7,0.8,1c0.2,0.4,0.3,0.9,0.3,1.4c0,0.7-0.1,1.2-0.5,1.6c-0.3,0.4-0.7,0.8-1.3,1.2c-0.5,0.3-1.2,0.6-1.8,0.9
 85  				c-0.7,0.2-1.4,0.5-2,0.7c-0.7,0.2-1.4,0.5-2,0.9c-0.7,0.3-1.2,0.7-1.8,1.2c-0.5,0.4-0.9,1-1.3,1.7c-0.3,0.7-0.5,1.4-0.5,2.3
 86  				c0,0.8,0.1,1.5,0.4,2.2c0.3,0.7,0.8,1.3,1.4,1.8c0.6,0.5,1.3,0.9,2.2,1.2c0.9,0.3,1.8,0.4,3,0.4c0.9,0,1.7-0.1,2.5-0.4
 87  				c0.7-0.2,1.4-0.5,2-0.9c0.6-0.4,1-0.9,1.4-1.4s0.7-1.1,0.9-1.7L114.3-171.6"/>
 88  			<path id="path3350" class="st5" d="M137.1-188.4v9.7h-9.9v-9.7h-3.3v21.7h3.3v-9h9.9v9h3.3v-21.7H137.1"/>
 89  			<path id="path3352" class="st5" d="M146.9-188.4v21.7h3.3v-21.7H146.9"/>
 90  			<path id="path3354" class="st5" d="M156.6-188.4v21.7h13.5v-3h-10.3v-5.9h6.6v-3h-6.6v-9.7H156.6"/>
 91  			<path id="path3356" class="st5" d="M183-169.8v-18.6h-3.3v18.6h-6.2v3.1h15.5v-3.1L183-169.8"/>
 92  		</g>
 93  	</g>
 94  </g>
 95  </svg>

```
  * file:///opt/input/source/src/main/webapp/bower_components/angular-patternfly/dist/docs/img/OpenShift-logo.svg
      * `beans_1_1.xsd`: In the root tag, replace the `version` attribute value with `3.0`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8" standalone="no"?>
  2  <!-- Created with Inkscape (http://www.inkscape.org/) -->
  3  <svg id="svg4242" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns="http://www.w3.org/2000/svg" height="285.79" viewBox="0 0 286.28177 285.78885" width="286.28" version="1.1" xmlns:cc="http://creativecommons.org/ns#" xmlns:dc="http://purl.org/dc/elements/1.1/">
  4   <defs id="defs4244">
  5    <clipPath id="clipPath3923" clipPathUnits="userSpaceOnUse">
  6     <path id="path3925" d="m0 768h1024v-768h-1024v768z"/>
  7    </clipPath>
  8   </defs>
  9   <metadata id="metadata4247">
 10    <rdf:RDF>
 11     <cc:Work rdf:about="">
 12      <dc:format>image/svg+xml</dc:format>
 13      <dc:type rdf:resource="http://purl.org/dc/dcmitype/StillImage"/>
 14      <dc:title/>
 15     </cc:Work>
 16    </rdf:RDF>
 17   </metadata>
 18   <g id="layer1" transform="translate(448.86 -589.47)">
 19    <g id="g3367" transform="matrix(1.25 0 0 -1.25 -733.56 1212.1)">
 20     <g id="g3919">
 21      <g id="g3921" clip-path="url(#clipPath3923)">
 22       <g id="g3927" transform="translate(304.96 416.03)">
 23        <path id="path3929" d="m0 0-25.748-9.369c0.33-4.128 1.041-8.206 2.042-12.201l24.456 8.906c-0.793 4.135-1.076 8.396-0.75 12.664" fill="#c32034"/>
 24       </g>
 25       <g id="g3931" transform="translate(418.75 444.5)">
 26        <path id="path3933" d="m0 0c-1.795 3.704-3.873 7.284-6.279 10.657l-25.741-9.369c2.995-3.064 5.508-6.508 7.563-10.191l24.457 8.903z" fill="#c32034"/>
 27       </g>
 28       <g id="g3935" transform="translate(362.11 451.79)">
 29        <path id="path3937" d="m0 0c5.356-2.499 9.995-5.908 13.907-9.906l25.742 9.37c-7.13 10.005-16.842 18.366-28.743 23.919-36.797 17.159-80.702 1.18-97.861-35.613-5.553-11.907-7.617-24.556-6.648-36.801l25.745 9.368c0.427 5.578 1.789 11.167 4.284 16.526 11.151 23.909 39.669 34.283 63.575 23.137" fill="#db212f"/>
 30       </g>
 31       <g id="g3939" transform="translate(282.86 395.05)">
 32        <path id="path3941" d="m0 0-24.46-8.909c2.248-8.918 6.145-17.391 11.502-24.932l25.688 9.351c-6.595 6.771-10.979 15.337-12.73 24.49" fill="#ea2227"/>
 33       </g>
 34       <g id="g3943" transform="translate(389.56 404.75)">
 35        <path id="path3945" d="m0 0c-0.409-5.575-1.817-11.167-4.319-16.53-11.15-23.91-39.668-34.285-63.574-23.136-5.363 2.501-10.035 5.883-13.936 9.888l-25.687-9.352c7.113-10.006 16.816-18.369 28.721-23.926 36.799-17.156 80.698-1.177 97.857 35.619 5.557 11.905 7.608 24.549 6.626 36.785l-25.69-9.348z" fill="#db212f"/>
 36       </g>
 37       <g id="g3947" transform="translate(395.89 436.18)">
 38        <path id="path3949" d="m0 0-24.458-8.903c4.542-8.139 6.689-17.513 5.986-26.938l25.688 9.345c-0.735 9.219-3.195 18.217-7.216 26.496" fill="#ea2227"/>
 39       </g>
 40       <g id="g3951" transform="translate(279.22 406.66)">
 41        <path id="path3953" d="m0 0 25.684 9.263-0.105-5.08-24.78-9.213-0.799 5.03z" fill="#ad213a"/>
 42       </g>
 43       <g id="g3955" transform="translate(386.73 445.86)">
 44        <path id="path3957" d="m0 0 26.085 8.814 2.712-4.028-25.345-8.821-3.452 4.035z" fill="#ad213a"/>
 45       </g>
 46       <g id="g3959" transform="translate(282.04 365.71)">
 47        <path id="path3961" d="m0 0 25.716 9.213 7.777-7.225-26.967-9.967-6.526 7.979z" fill="#ba2034"/>
 48       </g>
 49       <g id="g3963" transform="translate(415.68 414.03)">
 50        <path id="path3965" d="m0 0-26.119-9.274-1.924-10.293 27.848 9.771 0.195 9.796z" fill="#ba2034"/>
 51       </g>
 52      </g>
 53     </g>
 54     <g id="text3967" transform="scale(1,-1)" fill="#231f20">
 55      <path id="path3359" d="m254.37-285.44c-1.2952 0-2.4565-0.16749-3.4837-0.50246-1.0273-0.34614-1.9373-0.80952-2.73-1.3901-0.78161-0.59178-1.4516-1.2841-2.0098-2.0768-0.5583-0.80393-1.0161-1.6637-1.3734-2.5793-0.34614-0.92675-0.60296-1.887-0.77044-2.8808-0.15632-1.0049-0.23448-2.0042-0.23448-2.998 0-0.98257 0.0782-1.9707 0.23448-2.9645 0.16748-1.0049 0.4243-1.9652 0.77044-2.8808 0.3573-0.92674 0.81509-1.7865 1.3734-2.5793 0.55828-0.80391 1.2282-1.4962 2.0098-2.0768 0.79276-0.59176 1.7028-1.0551 2.73-1.3901 1.0272-0.34611 2.1885-0.51918 3.4837-0.51921 1.2952 0.00003 2.4509 0.1731 3.467 0.51921 1.0272 0.335 1.9317 0.79838 2.7133 1.3901 0.78158 0.58064 1.4515 1.2729 2.0098 2.0768 0.55826 0.79279 1.0105 1.6526 1.3566 2.5793 0.35728 0.91561 0.61409 1.8759 0.77043 2.8808 0.16747 0.99377 0.25121 1.9819 0.25123 2.9645-0.00002 0.99376-0.0838 1.9931-0.25123 2.998-0.15634 0.99376-0.41315 1.954-0.77043 2.8808-0.34617 0.9156-0.79838 1.7754-1.3566 2.5793-0.55831 0.79277-1.2283 1.485-2.0098 2.0768-0.78162 0.58062-1.686 1.044-2.7133 1.3901-1.0161 0.33497-2.1718 0.50246-3.467 0.50246m0-4.4719c1.0719 0.00001 1.9708-0.25122 2.6965-0.75369 0.73693-0.50245 1.3287-1.1445 1.7754-1.9261 0.45778-0.78159 0.78717-1.6358 0.98817-2.5625 0.20096-0.93791 0.30146-1.8423 0.30147-2.7133-0.00001-0.6141-0.0447-1.2338-0.13398-1.8591-0.0782-0.63643-0.21217-1.245-0.40197-1.8256-0.18984-0.59177-0.43548-1.1445-0.73694-1.6581-0.30149-0.52478-0.66438-0.97699-1.0887-1.3566-0.42432-0.39078-0.92119-0.69784-1.4906-0.92118-0.5583-0.22329-1.1948-0.33495-1.9094-0.33497-0.72578 0.00002-1.3734 0.11726-1.9428 0.35172-0.5583 0.2345-1.0552 0.55273-1.4906 0.95467-0.4243 0.39082-0.78719 0.84862-1.0887 1.3734-0.30148 0.52481-0.54713 1.0831-0.73694 1.6749-0.18982 0.5918-0.32939 1.1948-0.41871 1.8088-0.0782 0.61413-0.11725 1.2115-0.11724 1.7921-0.00001 0.9156 0.10048 1.8479 0.30147 2.797 0.20098 0.93794 0.52479 1.7921 0.97142 2.5625 0.45779 0.75928 1.0552 1.3846 1.7921 1.8758 0.73693 0.48013 1.6469 0.7202 2.73 0.72019"/>
 56      <path id="path3361" d="m270.86-285.86v-24.018h10.3c1.5185 0.00003 2.797 0.22334 3.8354 0.66995 1.0384 0.43548 1.8814 1.0161 2.529 1.7418 0.6476 0.71463 1.111 1.5242 1.3901 2.4286 0.29029 0.90444 0.43544 1.82 0.43546 2.7468-0.00002 0.58064-0.067 1.1724-0.20098 1.7754-0.13401 0.5918-0.34058 1.1724-0.6197 1.7419-0.27916 0.5583-0.63647 1.0831-1.0719 1.5744-0.43549 0.4913-0.96028 0.92676-1.5744 1.3064-0.60297 0.36848-1.3008 0.65879-2.0936 0.87093-0.78162 0.21216-1.6581 0.31823-2.6295 0.31822h-5.661v8.8433h-4.6394m10.501-13.248c0.59178 0.00002 1.0886-0.0949 1.4906-0.28472 0.40196-0.18981 0.72576-0.43545 0.97142-0.73694 0.2568-0.30146 0.44103-0.64202 0.55271-1.0217 0.11164-0.37962 0.16747-0.75926 0.16749-1.1389-0.00002-0.34612-0.0503-0.70342-0.15074-1.0719-0.0893-0.37962-0.25683-0.72576-0.50246-1.0384-0.2345-0.31262-0.5583-0.56943-0.97142-0.77043-0.41315-0.20097-0.93236-0.30146-1.5576-0.30148h-5.862v6.3645h5.862"/>
 57      <path id="path3363" d="m295.76-285.86v-24.018h16.397v4.4049h-11.758v5.0413h6.9172v4.3881h-6.9172v5.795h12.478v4.3881h-17.117"/>
 58      <path id="path3365" d="m334.66-285.86-9.53-14.002c-0.15633-0.23446-0.3294-0.51919-0.51921-0.85418-0.17866-0.34612-0.33498-0.66434-0.46896-0.95467 0.0335 0.25683 0.0558 0.5583 0.067 0.90443 0.0223 0.34615 0.0335 0.64763 0.0335 0.90442v14.002h-4.6059v-24.018h4.3546l9.2955 13.834c0.14514 0.22333 0.31263 0.50247 0.50246 0.83743 0.1898 0.33499 0.35729 0.65879 0.50246 0.97142-0.0335-0.32379-0.0614-0.6476-0.0837-0.97142-0.0112-0.33496-0.0168-0.6141-0.0168-0.83743v-13.834h4.5891v24.018h-4.1202"/>
 59     </g>
 60     <g id="text3971" transform="scale(1,-1)" fill="#231f20">
 61      <path id="path3348" d="m358.06-304.42c-0.14517-0.34612-0.34615-0.66435-0.60295-0.95468-0.25683-0.30145-0.56947-0.55826-0.93793-0.77043-0.36848-0.2233-0.79278-0.39637-1.2729-0.51921-0.46897-0.1228-0.99376-0.18421-1.5744-0.18424-1.1501 0.00003-2.0489 0.25125-2.6965 0.75369-0.64762 0.50248-0.97143 1.2115-0.97142 2.1271-0.00001 0.56947 0.17864 1.0552 0.53595 1.4571 0.3573 0.39082 0.82626 0.73696 1.4069 1.0384 0.58061 0.30149 1.2394 0.58063 1.9763 0.83743 0.74809 0.24566 1.5074 0.51922 2.2778 0.82068 0.78159 0.29032 1.5409 0.63088 2.2778 1.0217 0.7481 0.37964 1.4125 0.84861 1.9931 1.4069 0.5806 0.54713 1.0496 1.2115 1.4069 1.9931 0.35728 0.77045 0.53594 1.6972 0.53595 2.7803-0.00001 1.1501-0.21216 2.1718-0.63644 3.065-0.41315 0.8821-0.98819 1.6302-1.7251 2.2443-0.73696 0.60295-1.6079 1.0663-2.6128 1.3901-0.99377 0.31264-2.0657 0.46896-3.2157 0.46896-1.0719 0-2.0768-0.13957-3.0148-0.41872-0.92677-0.26798-1.7698-0.65319-2.529-1.1556-0.74811-0.51363-1.3957-1.1277-1.9428-1.8424-0.54712-0.72577-0.97142-1.5353-1.2729-2.4286l3.3665-1.2226c0.24564 0.53597 0.54712 1.0273 0.90443 1.4739 0.36846 0.44664 0.78718 0.83186 1.2562 1.1557 0.46895 0.31264 0.98257 0.55829 1.5409 0.73694 0.56944 0.17865 1.178 0.26798 1.8256 0.26798s1.2394-0.0782 1.7754-0.23448c0.53594-0.15632 0.99374-0.3908 1.3734-0.70345 0.37963-0.31263 0.67552-0.69785 0.88768-1.1556 0.21214-0.46896 0.31821-1.0049 0.31823-1.6079-0.00002-0.7146-0.17867-1.312-0.53596-1.7921-0.35732-0.49129-0.82628-0.91559-1.4069-1.2729-0.58063-0.35729-1.245-0.66994-1.9931-0.93792-0.73695-0.26797-1.4962-0.54153-2.2778-0.82069-0.77044-0.27913-1.5297-0.59177-2.2778-0.93792-0.73695-0.34613-1.3957-0.77042-1.9763-1.2729-0.58062-0.50244-1.0496-1.1054-1.4069-1.8088-0.3573-0.70343-0.53595-1.5632-0.53595-2.5793 0-0.84858 0.16748-1.6525 0.50246-2.4118 0.34613-0.75925 0.84301-1.4236 1.4906-1.9931 0.6476-0.58059 1.446-1.0384 2.395-1.3734 0.94908-0.33495 2.0322-0.50243 3.2492-0.50246 1.0161 0.00003 1.9372 0.12285 2.7635 0.36847 0.82625 0.23451 1.5464 0.5639 2.1606 0.98817 0.62527 0.42432 1.1445 0.92678 1.5576 1.5074 0.41311 0.58064 0.72575 1.2115 0.93792 1.8926l-3.2995 1.1054"/>
 62      <path id="path3350" d="m383.24-285.86v-10.702h-10.954v10.702h-3.5675v-24.018h3.5675v9.9487h10.954v-9.9487h3.5674v24.018h-3.5674"/>
 63      <path id="path3352" d="m394.08-285.86v-24.018h3.5675v24.018h-3.5675"/>
 64      <path id="path3354" d="m404.81-285.86v-24.018h14.89v3.3665h-11.322v6.5822h7.3192v3.3665h-7.3192v10.702h-3.5675"/>
 65      <path id="path3356" d="m434.01-306.44v20.584h-3.5675v-20.584h-6.8v-3.4335h17.151v3.4335h-6.7832"/>
 66     </g>
 67    </g>
 68   </g>
 69  </svg>

```
  * file:///opt/input/source/src/main/webapp/bower_components/angular-patternfly/dist/docs/img/OpenShift-Logo-NoText.svg
      * `beans_1_1.xsd`: In the root tag, replace the `version` attribute value with `3.0`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="utf-8"?>
  2  <!-- Generator: Adobe Illustrator 19.2.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
  3  <svg version="1.1"
  4  	 id="svg4242" xmlns:cc="http://creativecommons.org/ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
  5  	 xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 200 199.7"
  6  	 style="enable-background:new 0 0 200 199.7;" xml:space="preserve">
  7  <style type="text/css">
  8  	.st0{fill:#C32034;}
  9  	.st1{fill:#DB212F;}
 10  	.st2{fill:#EA2227;}
 11  	.st3{fill:#AD213A;}
 12  	.st4{fill:#BA2034;}
 13  </style>
 14  <g id="g3921">
 15  	<g id="g3927" transform="translate(304.96 416.03)">
 16  		<path id="path3929" class="st0" d="M-235.4-323l-23.3,8.5c0.3,3.8,0.9,7.5,1.9,11.1l22.1-8C-235.4-315.4-235.7-319.2-235.4-323"/>
 17  	</g>
 18  	<g id="g3931" transform="translate(418.75 444.5)">
 19  		<path id="path3933" class="st0" d="M-246.2-377.3c-1.6-3.3-3.5-6.6-5.6-9.6l-23.3,8.5c2.7,2.8,5,5.9,6.9,9.2
 20  			C-268.3-369.3-246.2-377.3-246.2-377.3z"/>
 21  	</g>
 22  	<g id="g3935" transform="translate(362.11 451.79)">
 23  		<path id="path3937" class="st1" d="M-240.8-391.2c4.8,2.2,9,5.4,12.6,9l23.3-8.5c-6.4-9-15.3-16.6-26-21.6
 24  			c-33.3-15.5-73-1.1-88.5,32.2c-5,10.8-6.9,22.2-6,33.3l23.3-8.5c0.4-5.1,1.6-10.1,3.9-15C-288.2-391.9-262.5-401.2-240.8-391.2"/>
 25  	</g>
 26  	<g id="g3939" transform="translate(282.86 395.05)">
 27  		<path id="path3941" class="st2" d="M-233.3-283.1l-22.1,8c2,8,5.6,15.7,10.4,22.6l23.2-8.5C-227.7-267.1-231.7-274.8-233.3-283.1"
 28  			/>
 29  	</g>
 30  	<g id="g3943" transform="translate(389.56 404.75)">
 31  		<path id="path3945" class="st1" d="M-243.4-301.6c-0.4,5.1-1.7,10.1-3.9,15c-10.1,21.6-35.9,31.1-57.5,20.9c-4.8-2.2-9-5.4-12.6-9
 32  			l-23.2,8.5c6.4,9,15.2,16.6,26,21.6c33.3,15.5,73,1.1,88.5-32.2c5-10.8,6.9-22.2,6-33.3L-243.4-301.6L-243.4-301.6z"/>
 33  	</g>
 34  	<g id="g3947" transform="translate(395.89 436.18)">
 35  		<path id="path3949" class="st2" d="M-244-361.5l-22.1,8c4.1,7.4,6.1,15.9,5.4,24.4l23.2-8.5C-238.1-345.8-240.4-353.9-244-361.5"
 36  			/>
 37  	</g>
 38  	<g id="g3951" transform="translate(279.22 406.66)">
 39  		<path id="path3953" class="st3" d="M-232.9-305.2l23.2-8.4l-0.1,4.6l-22.4,8.3C-232.2-300.7-232.9-305.2-232.9-305.2z"/>
 40  	</g>
 41  	<g id="g3955" transform="translate(386.73 445.86)">
 42  		<path id="path3957" class="st3" d="M-243.1-379.9l23.6-8l2.5,3.6l-22.9,8C-240-376.2-243.1-379.9-243.1-379.9z"/>
 43  	</g>
 44  	<g id="g3959" transform="translate(282.04 365.71)">
 45  		<path id="path3961" class="st4" d="M-233.2-227.2l23.2-8.3l7,6.5l-24.4,9C-227.3-220-233.2-227.2-233.2-227.2z"/>
 46  	</g>
 47  	<g id="g3963" transform="translate(415.68 414.03)">
 48  		<path id="path3965" class="st4" d="M-245.9-319.2l-23.6,8.4l-1.7,9.3l25.2-8.8C-246.1-310.4-245.9-319.2-245.9-319.2z"/>
 49  	</g>
 50  </g>
 51  </svg>

```
  * file:///opt/input/source/src/main/webapp/bower_components/angular-patternfly/dist/docs/img/kubernetes.svg
      * `beans_1_1.xsd`: In the root tag, replace the `version` attribute value with `3.0`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8" standalone="no"?>
  2  <svg width="256px" height="249px" viewBox="0 0 256 249" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" preserveAspectRatio="xMidYMid">
  3  	<g>
  4  		<path d="M82.0851613,244.934194 C76.1393548,244.934194 70.523871,242.291613 66.7251613,237.501935 L8.91870968,165.656774 C5.12,160.867097 3.63354839,154.756129 5.12,148.810323 L25.7651613,59.1277419 C27.0864516,53.1819355 31.0503226,48.3922581 36.5006452,45.7496774 L120.072258,5.78064516 C122.714839,4.45935484 125.687742,3.79870968 128.660645,3.79870968 C131.633548,3.79870968 134.606452,4.45935484 137.249032,5.78064516 L220.820645,45.5845161 C226.270968,48.2270968 230.234839,53.0167742 231.556129,58.9625806 L252.20129,148.645161 C253.522581,154.590968 252.20129,160.701935 248.402581,165.491613 L190.596129,237.336774 C186.797419,241.96129 181.181935,244.769032 175.236129,244.769032 L82.0851613,244.934194 L82.0851613,244.934194 Z" fill="#326DE6"></path>
  5  		<path d="M128.495484,7.92774194 C130.807742,7.92774194 133.12,8.42322581 135.267097,9.41419355 L218.83871,49.2180645 C223.132903,51.3651613 226.436129,55.3290323 227.427097,59.9535484 L248.072258,149.636129 C249.228387,154.425806 248.072258,159.380645 244.934194,163.179355 L187.127742,235.024516 C184.154839,238.823226 179.530323,240.970323 174.740645,240.970323 L82.0851613,240.970323 C77.2954839,240.970323 72.6709677,238.823226 69.6980645,235.024516 L11.8916129,163.179355 C8.91870968,159.380645 7.76258065,154.425806 8.75354839,149.636129 L29.3987097,59.9535484 C30.5548387,55.163871 33.6929032,51.2 37.9870968,49.2180645 L121.55871,9.24903226 C123.705806,8.42322581 126.183226,7.92774194 128.495484,7.92774194 L128.495484,7.92774194 Z M128.495484,0.16516129 L128.495484,0.16516129 C125.027097,0.16516129 121.55871,0.990967742 118.255484,2.47741935 L34.683871,42.4464516 C28.0774194,45.5845161 23.4529032,51.3651613 21.8012903,58.4670968 L1.15612903,148.149677 C-0.495483871,155.251613 1.15612903,162.51871 5.78064516,168.299355 L63.5870968,240.144516 C68.0464516,245.76 74.8180645,248.898065 81.92,248.898065 L174.575484,248.898065 C181.677419,248.898065 188.449032,245.76 192.908387,240.144516 L250.714839,168.299355 C255.339355,162.683871 256.990968,155.251613 255.339355,148.149677 L234.694194,58.4670968 C233.042581,51.3651613 228.418065,45.5845161 221.811613,42.4464516 L138.570323,2.47741935 C135.432258,0.990967742 131.963871,0.16516129 128.495484,0.16516129 L128.495484,0.16516129 L128.495484,0.16516129 Z" fill="#FFFFFF"></path>
  6  		<path d="M212.232258,142.534194 L212.232258,142.534194 L212.232258,142.534194 C212.067097,142.534194 212.067097,142.534194 212.232258,142.534194 L212.067097,142.534194 C211.901935,142.534194 211.736774,142.534194 211.736774,142.369032 C211.406452,142.369032 211.076129,142.203871 210.745806,142.203871 C209.589677,142.03871 208.59871,141.873548 207.607742,141.873548 C207.112258,141.873548 206.616774,141.873548 205.956129,141.708387 L205.790968,141.708387 C202.322581,141.378065 199.514839,141.047742 196.872258,140.221935 C195.716129,139.726452 195.385806,139.065806 195.055484,138.405161 C195.055484,138.24 194.890323,138.24 194.890323,138.074839 L194.890323,138.074839 L192.743226,137.414194 C193.734194,129.816774 193.403871,121.889032 191.587097,114.126452 C189.770323,106.363871 186.632258,99.0967742 182.338065,92.4903226 L183.989677,91.003871 L183.989677,90.6735484 C183.989677,89.8477419 184.154839,89.0219355 184.815484,88.196129 C186.797419,86.3793548 189.274839,84.8929032 192.247742,83.076129 L192.247742,83.076129 C192.743226,82.7458065 193.23871,82.5806452 193.734194,82.2503226 C194.725161,81.7548387 195.550968,81.2593548 196.541935,80.5987097 C196.707097,80.4335484 197.037419,80.2683871 197.367742,79.9380645 C197.532903,79.7729032 197.698065,79.7729032 197.698065,79.6077419 L197.698065,79.6077419 C200.010323,77.6258065 200.505806,74.3225806 198.854194,72.1754839 C198.028387,71.0193548 196.541935,70.3587097 195.055484,70.3587097 C193.734194,70.3587097 192.578065,70.8541935 191.421935,71.68 L191.421935,71.68 L191.421935,71.68 C191.256774,71.8451613 191.256774,71.8451613 191.091613,72.0103226 C190.76129,72.1754839 190.596129,72.5058065 190.265806,72.6709677 C189.44,73.4967742 188.779355,74.1574194 188.11871,74.9832258 C187.788387,75.3135484 187.458065,75.8090323 186.962581,76.1393548 L186.962581,76.1393548 C184.650323,78.6167742 182.503226,80.5987097 180.356129,82.0851613 C179.860645,82.4154839 179.365161,82.5806452 178.869677,82.5806452 C178.539355,82.5806452 178.209032,82.5806452 177.87871,82.4154839 L177.548387,82.4154839 L177.548387,82.4154839 L175.566452,83.7367742 C173.419355,81.4245161 171.107097,79.4425806 168.794839,77.4606452 C158.885161,69.6980645 146.828387,64.9083871 134.276129,63.7522581 L134.110968,61.6051613 C133.945806,61.44 133.945806,61.44 133.780645,61.2748387 C133.285161,60.7793548 132.624516,60.283871 132.459355,59.1277419 C132.294194,56.4851613 132.624516,53.5122581 132.954839,50.2090323 L132.954839,50.043871 C132.954839,49.5483871 133.12,48.8877419 133.285161,48.3922581 C133.450323,47.4012903 133.615484,46.4103226 133.780645,45.2541935 L133.780645,44.2632258 L133.780645,43.7677419 L133.780645,43.7677419 L133.780645,43.7677419 C133.780645,40.7948387 131.468387,38.3174194 128.660645,38.3174194 C127.339355,38.3174194 126.018065,38.9780645 125.027097,39.9690323 C124.036129,40.96 123.540645,42.2812903 123.540645,43.7677419 L123.540645,43.7677419 L123.540645,43.7677419 L123.540645,44.0980645 L123.540645,45.0890323 C123.540645,46.2451613 123.705806,47.236129 124.036129,48.2270968 C124.20129,48.7225806 124.20129,49.2180645 124.366452,49.8787097 L124.366452,50.043871 C124.696774,53.3470968 125.192258,56.32 124.861935,58.9625806 C124.696774,60.1187097 124.036129,60.6141935 123.540645,61.1096774 C123.375484,61.2748387 123.375484,61.2748387 123.210323,61.44 L123.210323,61.44 L123.045161,63.5870968 C120.072258,63.9174194 117.099355,64.2477419 114.126452,64.9083871 C101.409032,67.716129 90.1780645,74.1574194 81.4245161,83.4064516 L79.7729032,82.2503226 L79.4425806,82.2503226 C79.1122581,82.2503226 78.7819355,82.4154839 78.4516129,82.4154839 C77.956129,82.4154839 77.4606452,82.2503226 76.9651613,81.92 C74.8180645,80.4335484 72.6709677,78.2864516 70.3587097,75.8090323 L70.3587097,75.8090323 C70.0283871,75.4787097 69.6980645,74.9832258 69.2025806,74.6529032 C68.5419355,73.8270968 67.8812903,73.1664516 67.0554839,72.3406452 C66.8903226,72.1754839 66.56,72.0103226 66.2296774,71.68 C66.0645161,71.5148387 65.8993548,71.5148387 65.8993548,71.3496774 L65.8993548,71.3496774 C64.9083871,70.523871 63.5870968,70.0283871 62.2658065,70.0283871 C60.7793548,70.0283871 59.2929032,70.6890323 58.4670968,71.8451613 C56.8154839,73.9922581 57.3109677,77.2954839 59.6232258,79.2774194 L59.6232258,79.2774194 L59.6232258,79.2774194 C59.7883871,79.2774194 59.7883871,79.4425806 59.9535484,79.4425806 C60.283871,79.6077419 60.4490323,79.9380645 60.7793548,80.1032258 C61.7703226,80.763871 62.596129,81.2593548 63.5870968,81.7548387 C64.0825806,81.92 64.5780645,82.2503226 65.0735484,82.5806452 L65.0735484,82.5806452 C68.0464516,84.3974194 70.523871,85.883871 72.5058065,87.7006452 C73.3316129,88.5264516 73.3316129,89.3522581 73.3316129,90.1780645 L73.3316129,90.5083871 L73.3316129,90.5083871 L74.9832258,91.9948387 C74.6529032,92.4903226 74.3225806,92.8206452 74.1574194,93.316129 C65.8993548,106.363871 62.7612903,121.723871 64.9083871,136.91871 L62.7612903,137.579355 C62.7612903,137.744516 62.596129,137.744516 62.596129,137.909677 C62.2658065,138.570323 61.7703226,139.230968 60.7793548,139.726452 C58.3019355,140.552258 55.3290323,140.882581 51.8606452,141.212903 L51.6954839,141.212903 C51.2,141.212903 50.5393548,141.212903 50.043871,141.378065 C49.0529032,141.378065 48.0619355,141.543226 46.9058065,141.708387 C46.5754839,141.708387 46.2451613,141.873548 45.9148387,141.873548 C45.7496774,141.873548 45.5845161,141.873548 45.4193548,142.03871 L45.4193548,142.03871 L45.4193548,142.03871 C42.4464516,142.699355 40.6296774,145.507097 41.1251613,148.149677 C41.6206452,150.461935 43.7677419,151.948387 46.4103226,151.948387 C46.9058065,151.948387 47.236129,151.948387 47.7316129,151.783226 L47.7316129,151.783226 L47.7316129,151.783226 C47.8967742,151.783226 48.0619355,151.783226 48.0619355,151.618065 C48.3922581,151.618065 48.7225806,151.452903 49.0529032,151.452903 C50.2090323,151.122581 51.0348387,150.792258 52.0258065,150.296774 C52.5212903,150.131613 53.0167742,149.80129 53.5122581,149.636129 L53.6774194,149.636129 C56.8154839,148.48 59.6232258,147.489032 62.2658065,147.15871 L62.596129,147.15871 C63.5870968,147.15871 64.2477419,147.654194 64.7432258,147.984516 C64.9083871,147.984516 64.9083871,148.149677 65.0735484,148.149677 L65.0735484,148.149677 L67.3858065,147.819355 C71.3496774,160.04129 78.9470968,170.941935 89.0219355,178.869677 C91.3341935,180.686452 93.6464516,182.172903 96.123871,183.659355 L95.1329032,185.806452 C95.1329032,185.971613 95.2980645,185.971613 95.2980645,186.136774 C95.6283871,186.797419 95.9587097,187.623226 95.6283871,188.779355 C94.6374194,191.256774 93.1509677,193.734194 91.3341935,196.541935 L91.3341935,196.707097 C91.003871,197.202581 90.6735484,197.532903 90.3432258,198.028387 C89.6825806,198.854194 89.1870968,199.68 88.5264516,200.670968 C88.3612903,200.836129 88.196129,201.166452 88.0309677,201.496774 C88.0309677,201.661935 87.8658065,201.827097 87.8658065,201.827097 L87.8658065,201.827097 L87.8658065,201.827097 C86.5445161,204.634839 87.5354839,207.772903 90.0129032,208.929032 C90.6735484,209.259355 91.3341935,209.424516 91.9948387,209.424516 C93.9767742,209.424516 95.9587097,208.103226 96.9496774,206.286452 L96.9496774,206.286452 L96.9496774,206.286452 C96.9496774,206.12129 97.1148387,205.956129 97.1148387,205.956129 C97.28,205.625806 97.4451613,205.295484 97.6103226,205.130323 C98.1058065,203.974194 98.2709677,203.148387 98.6012903,202.157419 C98.7664516,201.661935 98.9316129,201.166452 99.0967742,200.670968 L99.0967742,200.670968 C100.252903,197.367742 101.07871,194.725161 102.565161,192.412903 C103.225806,191.421935 104.051613,191.256774 104.712258,190.926452 C104.877419,190.926452 104.877419,190.926452 105.042581,190.76129 L105.042581,190.76129 L106.19871,188.614194 C113.465806,191.421935 121.393548,192.908387 129.32129,192.908387 C134.110968,192.908387 139.065806,192.412903 143.690323,191.256774 C146.663226,190.596129 149.470968,189.770323 152.27871,188.779355 L153.269677,190.596129 C153.434839,190.596129 153.434839,190.596129 153.6,190.76129 C154.425806,190.926452 155.086452,191.256774 155.747097,192.247742 C157.068387,194.56 158.059355,197.367742 159.215484,200.505806 L159.215484,200.670968 C159.380645,201.166452 159.545806,201.661935 159.710968,202.157419 C160.04129,203.148387 160.206452,204.139355 160.701935,205.130323 C160.867097,205.460645 161.032258,205.625806 161.197419,205.956129 C161.197419,206.12129 161.362581,206.286452 161.362581,206.286452 L161.362581,206.286452 L161.362581,206.286452 C162.353548,208.268387 164.335484,209.424516 166.317419,209.424516 C166.978065,209.424516 167.63871,209.259355 168.299355,208.929032 C169.455484,208.268387 170.446452,207.277419 170.776774,205.956129 C171.107097,204.634839 171.107097,203.148387 170.446452,201.827097 L170.446452,201.827097 L170.446452,201.827097 C170.446452,201.661935 170.28129,201.661935 170.28129,201.496774 C170.116129,201.166452 169.950968,200.836129 169.785806,200.670968 C169.290323,199.68 168.629677,198.854194 167.969032,198.028387 C167.63871,197.532903 167.308387,197.202581 166.978065,196.707097 L166.978065,196.541935 C165.16129,193.734194 163.509677,191.256774 162.683871,188.779355 C162.353548,187.623226 162.683871,186.962581 162.849032,186.136774 C162.849032,185.971613 163.014194,185.971613 163.014194,185.806452 L163.014194,185.806452 L162.188387,183.824516 C170.941935,178.704516 178.374194,171.437419 183.989677,162.51871 C186.962581,157.894194 189.274839,152.774194 190.926452,147.654194 L192.908387,147.984516 C193.073548,147.984516 193.073548,147.819355 193.23871,147.819355 C193.899355,147.489032 194.394839,146.993548 195.385806,146.993548 L195.716129,146.993548 C198.35871,147.323871 201.166452,148.314839 204.304516,149.470968 L204.469677,149.470968 C204.965161,149.636129 205.460645,149.966452 205.956129,150.131613 C206.947097,150.627097 207.772903,150.957419 208.929032,151.287742 C209.259355,151.287742 209.589677,151.452903 209.92,151.452903 C210.085161,151.452903 210.250323,151.452903 210.415484,151.618065 L210.415484,151.618065 C210.910968,151.783226 211.24129,151.783226 211.736774,151.783226 C214.214194,151.783226 216.36129,150.131613 217.021935,147.984516 C217.021935,146.002581 215.205161,143.36 212.232258,142.534194 L212.232258,142.534194 Z M135.762581,134.44129 L128.495484,137.909677 L121.228387,134.44129 L119.411613,126.67871 L124.366452,120.402581 L132.459355,120.402581 L137.414194,126.67871 L135.762581,134.44129 L135.762581,134.44129 Z M178.869677,117.264516 C180.190968,122.88 180.52129,128.495484 180.025806,133.945806 L154.756129,126.67871 C152.443871,126.018065 151.122581,123.705806 151.618065,121.393548 C151.783226,120.732903 152.113548,120.072258 152.609032,119.576774 L172.593548,101.574194 C175.40129,106.19871 177.548387,111.483871 178.869677,117.264516 L178.869677,117.264516 Z M164.665806,91.6645161 L143.029677,107.024516 C141.212903,108.180645 138.735484,107.850323 137.249032,106.033548 C136.753548,105.538065 136.588387,104.877419 136.423226,104.216774 L134.936774,77.2954839 C146.332903,78.6167742 156.738065,83.7367742 164.665806,91.6645161 L164.665806,91.6645161 Z M116.769032,78.1212903 C118.585806,77.7909677 120.237419,77.4606452 122.054194,77.1303226 L120.567742,103.556129 C120.402581,105.868387 118.585806,107.850323 116.108387,107.850323 C115.447742,107.850323 114.621935,107.685161 114.126452,107.354839 L92.16,91.6645161 C98.9316129,84.8929032 107.354839,80.2683871 116.769032,78.1212903 L116.769032,78.1212903 Z M84.2322581,101.574194 L103.886452,119.08129 C105.703226,120.567742 105.868387,123.375484 104.381935,125.192258 C103.886452,125.852903 103.225806,126.348387 102.4,126.513548 L76.8,133.945806 C75.8090323,122.714839 78.2864516,111.31871 84.2322581,101.574194 L84.2322581,101.574194 Z M79.7729032,146.332903 L106.033548,141.873548 C108.180645,141.708387 110.162581,143.194839 110.658065,145.341935 C110.823226,146.332903 110.823226,147.15871 110.492903,147.984516 L110.492903,147.984516 L100.418065,172.263226 C91.1690323,166.317419 83.7367742,157.233548 79.7729032,146.332903 L79.7729032,146.332903 Z M140.056774,179.2 C136.258065,180.025806 132.459355,180.52129 128.495484,180.52129 C122.714839,180.52129 117.099355,179.530323 111.814194,177.87871 L124.861935,154.260645 C126.183226,152.774194 128.330323,152.113548 130.147097,153.104516 C130.972903,153.6 131.633548,154.260645 132.129032,154.92129 L132.129032,154.92129 L144.846452,177.87871 C143.36,178.374194 141.708387,178.704516 140.056774,179.2 L140.056774,179.2 Z M172.263226,156.242581 C168.134194,162.849032 162.683871,168.134194 156.407742,172.263226 L146.002581,147.323871 C145.507097,145.341935 146.332903,143.194839 148.314839,142.203871 C148.975484,141.873548 149.80129,141.708387 150.627097,141.708387 L177.052903,146.167742 C176.061935,149.80129 174.410323,153.104516 172.263226,156.242581 L172.263226,156.242581 Z" fill="#FFFFFF"></path>
  7  	</g>
  8  </svg>

```
  * file:///opt/input/source/src/main/webapp/bower_components/angular-patternfly/dist/docs/img/kubernetes-Logo.svg
      * `beans_1_1.xsd`: In the root tag, replace the `version` attribute value with `3.0`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="utf-8"?>
  2  <!-- Generator: Adobe Illustrator 19.2.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
  3  <svg version="1.1"
  4  	 id="svg4242" xmlns:cc="http://creativecommons.org/ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
  5  	 xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 200 199.7"
  6  	 style="enable-background:new 0 0 200 199.7;" xml:space="preserve">
  7  <style type="text/css">
  8  	.st0{fill:#326DE6;}
  9  	.st1{fill:#FFFFFF;}
 10  </style>
 11  <g>
 12  	<path class="st0" d="M70.9,175.8c-3.8,0-7.3-1.7-9.7-4.7l-36.5-45.3c-2.4-3-3.3-6.9-2.4-10.6l13-56.6c0.8-3.8,3.3-6.8,6.8-8.4
 13  		l52.7-25.2c1.7-0.8,3.5-1.3,5.4-1.3c1.9,0,3.8,0.4,5.4,1.3L158.4,50c3.4,1.7,5.9,4.7,6.8,8.4l13,56.6c0.8,3.8,0,7.6-2.4,10.6
 14  		L139.3,171c-2.4,2.9-5.9,4.7-9.7,4.7L70.9,175.8L70.9,175.8z"/>
 15  	<path class="st1" d="M100.2,26.3c1.5,0,2.9,0.3,4.3,0.9l52.7,25.1c2.7,1.4,4.8,3.9,5.4,6.8l13,56.6c0.7,3,0,6.1-2,8.5l-36.5,45.3
 16  		c-1.9,2.4-4.8,3.8-7.8,3.8H70.9c-3,0-5.9-1.4-7.8-3.8l-36.5-45.3c-1.9-2.4-2.6-5.5-2-8.5l13-56.6c0.7-3,2.7-5.5,5.4-6.8l52.7-25.2
 17  		C97.1,26.6,98.7,26.3,100.2,26.3L100.2,26.3z M100.2,21.4L100.2,21.4c-2.2,0-4.4,0.5-6.5,1.5L41,48.1c-4.2,2-7.1,5.6-8.1,10.1
 18  		l-13,56.6c-1,4.5,0,9.1,2.9,12.7l36.5,45.3c2.8,3.5,7.1,5.5,11.6,5.5h58.5c4.5,0,8.8-2,11.6-5.5l36.5-45.3c2.9-3.5,4-8.2,2.9-12.7
 19  		l-13-56.6c-1-4.5-4-8.1-8.1-10.1l-52.5-25.2C104.5,21.9,102.3,21.4,100.2,21.4L100.2,21.4L100.2,21.4z"/>
 20  	<path class="st1" d="M153,111.2L153,111.2L153,111.2C152.9,111.2,152.9,111.2,153,111.2h-0.1c-0.1,0-0.2,0-0.2-0.1
 21  		c-0.2,0-0.4-0.1-0.6-0.1c-0.7-0.1-1.4-0.2-2-0.2c-0.3,0-0.6,0-1-0.1h-0.1c-2.2-0.2-4-0.4-5.6-0.9c-0.7-0.3-0.9-0.7-1.1-1.1
 22  		c0-0.1-0.1-0.1-0.1-0.2l0,0l-1.4-0.4c0.6-4.8,0.4-9.8-0.7-14.7c-1.1-4.9-3.1-9.5-5.8-13.7l1-0.9v-0.2c0-0.5,0.1-1,0.5-1.6
 23  		c1.3-1.1,2.8-2.1,4.7-3.2l0,0c0.3-0.2,0.6-0.3,0.9-0.5c0.6-0.3,1.1-0.6,1.8-1c0.1-0.1,0.3-0.2,0.5-0.4c0.1-0.1,0.2-0.1,0.2-0.2l0,0
 24  		c1.5-1.3,1.8-3.3,0.7-4.7c-0.5-0.7-1.5-1.1-2.4-1.1c-0.8,0-1.6,0.3-2.3,0.8l0,0l0,0c-0.1,0.1-0.1,0.1-0.2,0.2
 25  		c-0.2,0.1-0.3,0.3-0.5,0.4c-0.5,0.5-0.9,0.9-1.4,1.5c-0.2,0.2-0.4,0.5-0.7,0.7l0,0c-1.5,1.6-2.8,2.8-4.2,3.8
 26  		c-0.3,0.2-0.6,0.3-0.9,0.3c-0.2,0-0.4,0-0.6-0.1h-0.2l0,0l-1.3,0.8c-1.4-1.5-2.8-2.7-4.3-4c-6.3-4.9-13.9-7.9-21.8-8.6l-0.1-1.4
 27  		c-0.1-0.1-0.1-0.1-0.2-0.2c-0.3-0.3-0.7-0.6-0.8-1.4c-0.1-1.7,0.1-3.5,0.3-5.6v-0.1c0-0.3,0.1-0.7,0.2-1c0.1-0.6,0.2-1.3,0.3-2
 28  		v-0.6v-0.3l0,0l0,0c0-1.9-1.5-3.4-3.2-3.4c-0.8,0-1.7,0.4-2.3,1C97.3,47.1,97,48,97,48.9l0,0l0,0v0.2v0.6c0,0.7,0.1,1.4,0.3,2
 29  		c0.1,0.3,0.1,0.6,0.2,1v0.1c0.2,2.1,0.5,4,0.3,5.6c-0.1,0.7-0.5,1-0.8,1.4c-0.1,0.1-0.1,0.1-0.2,0.2l0,0l-0.1,1.4
 30  		c-1.9,0.2-3.8,0.4-5.6,0.8c-8,1.8-15.1,5.8-20.6,11.7l-1-0.7h-0.2c-0.2,0-0.4,0.1-0.6,0.1c-0.3,0-0.6-0.1-0.9-0.3
 31  		c-1.4-0.9-2.7-2.3-4.2-3.9l0,0c-0.2-0.2-0.4-0.5-0.7-0.7c-0.4-0.5-0.8-0.9-1.4-1.5c-0.1-0.1-0.3-0.2-0.5-0.4
 32  		c-0.1-0.1-0.2-0.1-0.2-0.2l0,0c-0.6-0.5-1.5-0.8-2.3-0.8c-0.9,0-1.9,0.4-2.4,1.1c-1,1.4-0.7,3.4,0.7,4.7l0,0l0,0
 33  		c0.1,0,0.1,0.1,0.2,0.1c0.2,0.1,0.3,0.3,0.5,0.4c0.6,0.4,1.1,0.7,1.8,1c0.3,0.1,0.6,0.3,0.9,0.5l0,0c1.9,1.1,3.4,2.1,4.7,3.2
 34  		c0.5,0.5,0.5,1,0.5,1.6v0.2l0,0l1,0.9c-0.2,0.3-0.4,0.5-0.5,0.8c-5.2,8.2-7.2,17.9-5.8,27.5l-1.4,0.4c0,0.1-0.1,0.1-0.1,0.2
 35  		c-0.2,0.4-0.5,0.8-1.1,1.1c-1.6,0.5-3.4,0.7-5.6,0.9h-0.1c-0.3,0-0.7,0-1,0.1c-0.6,0-1.3,0.1-2,0.2c-0.2,0-0.4,0.1-0.6,0.1
 36  		c-0.1,0-0.2,0-0.3,0.1l0,0l0,0c-1.9,0.4-3,2.2-2.7,3.9c0.3,1.5,1.7,2.4,3.3,2.4c0.3,0,0.5,0,0.8-0.1l0,0l0,0c0.1,0,0.2,0,0.2-0.1
 37  		c0.2,0,0.4-0.1,0.6-0.1c0.7-0.2,1.3-0.4,1.9-0.7c0.3-0.1,0.6-0.3,0.9-0.4H53c2-0.7,3.8-1.4,5.4-1.6h0.2c0.6,0,1,0.3,1.4,0.5
 38  		c0.1,0,0.1,0.1,0.2,0.1l0,0l1.5-0.2c2.5,7.7,7.3,14.6,13.7,19.6c1.5,1.1,2.9,2.1,4.5,3l-0.6,1.4c0,0.1,0.1,0.1,0.1,0.2
 39  		c0.2,0.4,0.4,0.9,0.2,1.7c-0.6,1.6-1.6,3.1-2.7,4.9v0.1c-0.2,0.3-0.4,0.5-0.6,0.8c-0.4,0.5-0.7,1-1.1,1.7c-0.1,0.1-0.2,0.3-0.3,0.5
 40  		c0,0.1-0.1,0.2-0.1,0.2l0,0l0,0c-0.8,1.8-0.2,3.8,1.4,4.5c0.4,0.2,0.8,0.3,1.3,0.3c1.3,0,2.5-0.8,3.1-2l0,0l0,0
 41  		c0-0.1,0.1-0.2,0.1-0.2c0.1-0.2,0.2-0.4,0.3-0.5c0.3-0.7,0.4-1.3,0.6-1.9c0.1-0.3,0.2-0.6,0.3-0.9l0,0c0.7-2.1,1.3-3.8,2.2-5.2
 42  		c0.4-0.6,0.9-0.7,1.4-0.9c0.1,0,0.1,0,0.2-0.1l0,0l0.7-1.4c4.6,1.8,9.6,2.7,14.6,2.7c3,0,6.1-0.3,9.1-1c1.9-0.4,3.6-0.9,5.4-1.6
 43  		l0.6,1.1c0.1,0,0.1,0,0.2,0.1c0.5,0.1,0.9,0.3,1.4,0.9c0.8,1.5,1.5,3.2,2.2,5.2v0.1c0.1,0.3,0.2,0.6,0.3,0.9
 44  		c0.2,0.6,0.3,1.3,0.6,1.9c0.1,0.2,0.2,0.3,0.3,0.5c0,0.1,0.1,0.2,0.1,0.2l0,0l0,0c0.6,1.3,1.9,2,3.1,2c0.4,0,0.8-0.1,1.3-0.3
 45  		c0.7-0.4,1.4-1,1.6-1.9c0.2-0.8,0.2-1.8-0.2-2.6l0,0l0,0c0-0.1-0.1-0.1-0.1-0.2c-0.1-0.2-0.2-0.4-0.3-0.5c-0.3-0.6-0.7-1.1-1.1-1.7
 46  		c-0.2-0.3-0.4-0.5-0.6-0.8v-0.1c-1.1-1.8-2.2-3.3-2.7-4.9c-0.2-0.7,0-1.1,0.1-1.7c0-0.1,0.1-0.1,0.1-0.2l0,0l-0.5-1.3
 47  		c5.5-3.2,10.2-7.8,13.8-13.4c1.9-2.9,3.3-6.1,4.4-9.4l1.3,0.2c0.1,0,0.1-0.1,0.2-0.1c0.4-0.2,0.7-0.5,1.4-0.5h0.2
 48  		c1.7,0.2,3.4,0.8,5.4,1.6h0.1c0.3,0.1,0.6,0.3,0.9,0.4c0.6,0.3,1.1,0.5,1.9,0.7c0.2,0,0.4,0.1,0.6,0.1c0.1,0,0.2,0,0.3,0.1l0,0
 49  		c0.3,0.1,0.5,0.1,0.8,0.1c1.6,0,2.9-1,3.3-2.4C156,113.4,154.9,111.7,153,111.2L153,111.2z M104.7,106.1l-4.6,2.2l-4.6-2.2
 50  		l-1.1-4.9l3.1-4h5.1l3.1,4L104.7,106.1L104.7,106.1z M131.9,95.3c0.8,3.5,1,7.1,0.7,10.5l-15.9-4.6c-1.5-0.4-2.3-1.9-2-3.3
 51  		c0.1-0.4,0.3-0.8,0.6-1.1L128,85.4C129.8,88.3,131.1,91.6,131.9,95.3L131.9,95.3z M123,79.1l-13.7,9.7c-1.1,0.7-2.7,0.5-3.6-0.6
 52  		c-0.3-0.3-0.4-0.7-0.5-1.1l-0.9-17C111.4,70.9,118,74.1,123,79.1L123,79.1z M92.8,70.6c1.1-0.2,2.2-0.4,3.3-0.6l-0.9,16.7
 53  		c-0.1,1.5-1.3,2.7-2.8,2.7c-0.4,0-0.9-0.1-1.3-0.3l-13.9-9.9C81.5,74.8,86.8,71.9,92.8,70.6L92.8,70.6z M72.2,85.4l12.4,11
 54  		c1.1,0.9,1.3,2.7,0.3,3.9c-0.3,0.4-0.7,0.7-1.3,0.8l-16.2,4.7C66.9,98.7,68.5,91.5,72.2,85.4L72.2,85.4z M69.4,113.6l16.6-2.8
 55  		c1.4-0.1,2.6,0.8,2.9,2.2c0.1,0.6,0.1,1.1-0.1,1.7l0,0L82.4,130C76.6,126.2,71.9,120.5,69.4,113.6L69.4,113.6z M107.5,134.3
 56  		c-2.4,0.5-4.8,0.8-7.3,0.8c-3.6,0-7.2-0.6-10.5-1.7l8.2-14.9c0.8-0.9,2.2-1.4,3.3-0.7c0.5,0.3,0.9,0.7,1.3,1.1l0,0l8,14.5
 57  		C109.5,133.8,108.5,134,107.5,134.3L107.5,134.3z M127.8,119.9c-2.6,4.2-6,7.5-10,10.1l-6.6-15.7c-0.3-1.3,0.2-2.6,1.5-3.2
 58  		c0.4-0.2,0.9-0.3,1.5-0.3l16.7,2.8C130.2,115.8,129.1,117.9,127.8,119.9L127.8,119.9z"/>
 59  </g>
 60  </svg>

```
  * file:///opt/input/source/src/main/webapp/bower_components/angular-patternfly/dist/docs/img/RH_Atomic-Logo-Text.svg
      * `beans_1_1.xsd`: In the root tag, replace the `version` attribute value with `3.0`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="utf-8"?>
  2  <!-- Generator: Adobe Illustrator 19.2.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
  3  <svg version="1.1"
  4  	 id="svg4242" xmlns:cc="http://creativecommons.org/ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
  5  	 xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 200 199.7"
  6  	 style="enable-background:new 0 0 200 199.7;" xml:space="preserve">
  7  <style type="text/css">
  8  	.st0{fill:#00B9E4;}
  9  	.st1{fill:#0088CE;}
 10  </style>
 11  <g>
 12  	<g>
 13  		<g>
 14  			<path class="st0" d="M88.1,117.9c-0.4,0.3-0.7,0.6-1,0.8c-2.5,2.5-4.9,4.8-7.1,6.9c1.4,0.8,2.4,2.1,3,3.7c2.7-2.4,5.5-5,8.4-7.9
 15  				c0.6-0.6,1.1-2.2-0.1-3.3C90.4,117.4,89,117.2,88.1,117.9z"/>
 16  			<path class="st0" d="M60.3,58.6c0.7,1.1,2.2,1.5,3.3,0.7c1.2-0.8,1-2.4,0.6-2.9C54.5,39.9,50.1,27.2,54,24.2
 17  				c2.4-1.9,7.6,0.2,14.5,5.3c0.7-2.2,2.3-4,4.3-5c-11.1-8.3-19.9-11.8-24-8.6C43,20.4,47.8,37,59.9,58C60,58.2,60.2,58.4,60.3,58.6
 18  				z"/>
 19  			<path class="st0" d="M140.3,104.4c2.9-0.4,5.7-0.8,8.3-1.3l0,0l0,0l0,0c0.7-0.7,1.2-1.7,1.2-2.8c0-1.8-1.3-3.3-2.9-3.7l0,0
 20  				c-3.2,0.5-6.7,1-10.4,1.4l0,0l0,0c-5.7-9.3-12.7-19.4-20.6-29.5c-2.3-3.2-7.4-9.1-11.3-13.6l0.1-0.1C124,33.4,141,20.3,146,24.1
 21  				c3.8,3-0.5,15.6-10.3,32.2c-0.3,0.5-0.6,2.1,0.6,2.9c1.2,0.8,2.7,0.4,3.3-0.7c0.1-0.2,0.3-0.4,0.4-0.6c12-21,16.9-37.6,11.1-42.1
 22  				c-7-5.5-27.8,8.6-50.3,32.9c0,0-0.3,0.4-1,1.1c-0.6-0.6-1-1.1-1-1.1c-4.9-5.2-9.7-10.1-14.2-14.2l0,0c-0.1-0.1-0.1-0.1-0.1-0.1
 23  				c-0.2-0.1-0.4-0.1-0.6-0.1c-2.1,0-3.8,1.7-3.8,3.8c0,0.5,0.1,1.1,0.3,1.5l0,0c4.7,4.4,9.6,9.5,14.8,15.2l0.1,0.1
 24  				c-4,4.5-9,10.4-11.3,13.6C76.1,78.6,69.1,88.6,63.4,98c-21.9-2.5-36.6-7.1-36.5-12.4c0-5.4,15.6-10.1,38.4-12.4
 25  				c0.3-0.1,0.4-0.1,0.7-0.1c1.2-0.2,1.9-1.4,1.8-2.3c0-1.2-0.9-2.4-2.6-2.4c-28.3,3.2-48,10.2-48,18.3
 26  				c-0.1,7.6,17.2,14.2,42.6,17.7c-11.9,20.9-16.7,37.3-10.9,41.8c4.2,3.3,13.3-0.4,24.7-9.1l0,0c0,0,0,0,0.1,0
 27  				c0.1-0.3,0.1-0.5,0.1-0.8c0-1.5-1.3-2.8-2.8-2.8c-0.2,0-0.3,0-0.4,0.1l0,0l0,0c-7.1,5.2-12.4,7.5-14.8,5.6
 28  				c-4-3.1,0.8-16.4,11.4-33.8c9.8,1.1,20.7,1.6,32.1,1.7l0,0c0.2,0,0.3,0,0.5,0l0,0l0,0c0.1,0,0.3,0,0.4,0l0,0h0.1l0,0h0.1
 29  				c0.1,0,0.3,0,0.4,0c0.2,0,0.3,0,0.5,0l0,0c11.4-0.1,22.3-0.6,32.1-1.7c10.5,17.5,15.4,30.8,11.4,33.8
 30  				c-4.1,3.2-16.5-5.2-31.5-20.4c-0.3-0.3-0.6-0.6-1-0.8c-1-0.7-2.3-0.5-3,0.2c-1.2,1.2-0.8,2.7-0.1,3.3
 31  				c19.4,19.2,36.3,29.6,42.5,24.8C157,141.7,152.2,125.3,140.3,104.4L140.3,104.4z M100.3,100c-0.1,0-0.2,0-0.3,0s-0.2,0-0.3,0
 32  				c-10.2,0-20-0.4-28.7-1.2c5.2-8.2,11.5-16.9,18.6-25.9c3.2-4,6.4-7.9,9.5-11.5l0,0c0.3-0.4,0.6-0.7,0.9-1.1
 33  				c0.3,0.4,0.6,0.7,0.9,1.1l0,0c3.1,3.7,6.3,7.5,9.5,11.5c7.1,9,13.3,17.8,18.6,25.9l0,0C120.2,99.6,110.5,100,100.3,100z"/>
 34  			<path class="st0" d="M134.9,68.4c-1.7-0.1-2.6,1.2-2.6,2.4c-0.1,1,0.6,2.1,1.8,2.3c0.2,0.1,0.4,0.1,0.7,0.1
 35  				c22.8,2.4,38.3,7,38.4,12.4c0,1.9-1.9,3.7-5.4,5.4c1.1,1.7,1.8,3.9,1.8,6.1c0,0.2,0,0.4-0.1,0.5c8.5-3.2,13.3-7,13.3-11
 36  				C182.9,78.5,163.2,71.6,134.9,68.4z"/>
 37  		</g>
 38  		<g>
 39  			<path class="st1" d="M76.6,23.6c-4.7,0-8.6,3.8-8.6,8.6c0,4.7,3.8,8.6,8.6,8.6c1.4,0,2.8-0.4,3.9-1c-0.2-0.5-0.3-1-0.3-1.5
 40  				c0-2.1,1.7-3.8,3.8-3.8c0.2,0,0.4,0,0.6,0.1c0.1,0.1,0.1,0.1,0.1,0.1c0.2-0.8,0.4-1.6,0.4-2.4C85.2,27.4,81.4,23.6,76.6,23.6z"/>
 41  			<path class="st1" d="M99.1,48.8c-0.4-0.4-0.7-0.8-1.2-1.2l-4.4,5.3c0.6,0.7,1.3,1.4,1.9,2.1l0.1,0.1c1.9-2.2,3.6-4.1,4.6-5.2
 42  				C99.4,49.2,99.1,48.8,99.1,48.8z"/>
 43  			<path class="st1" d="M100,60.3L100,60.3c0.3,0.4,0.6,0.7,0.9,1.1l0,0c1,1.2,2,2.3,3,3.5l4.6-5.4c-1.3-1.5-2.6-3-3.8-4.4L100,60.3
 44  				z"/>
 45  			<path class="st1" d="M158.3,85.9c-6,0-11,4.8-11.3,10.7c1.7,0.4,2.9,1.9,2.9,3.7c0,1.1-0.5,2.1-1.2,2.8l0,0
 46  				c2,3.2,5.6,5.4,9.6,5.4c6.2,0,11.3-5.1,11.3-11.3C169.6,90.9,164.5,85.9,158.3,85.9z"/>
 47  			<path class="st1" d="M59.7,104.4c-1.2,2.1-2.3,4.1-3.3,6.1l7,0.9c1.1-2,2.3-4,3.5-6.1L59.7,104.4L59.7,104.4z"/>
 48  			<path class="st1" d="M71,98.8c0.4-0.7,0.9-1.4,1.4-2.1l-7.5-0.9c-0.5,0.7-1,1.5-1.4,2.2l0,0L71,98.8L71,98.8z"/>
 49  			<path class="st1" d="M136.6,98.1c-0.5-0.8-1-1.6-1.5-2.3l-7.5,1c0.5,0.7,1,1.5,1.4,2.2l0,0l0,0L136.6,98.1L136.6,98.1z"/>
 50  			<path class="st1" d="M133.1,105.3L133.1,105.3c1.2,2.1,2.4,4.1,3.5,6l7-0.9c-1-2-2.1-4-3.3-6L133.1,105.3z"/>
 51  			<path class="st1" d="M76.6,124.7c-3.7,0-6.6,3-6.6,6.6c0,0.8,0.2,1.5,0.4,2.2l0,0c0.1,0,0.3-0.1,0.4-0.1c1.5,0,2.8,1.3,2.8,2.8
 52  				c0,0.3-0.1,0.5-0.1,0.8c0,0,0,0-0.1,0c1,0.5,2,0.8,3.2,0.8c3.7,0,6.6-3,6.6-6.6C83.2,127.7,80.3,124.7,76.6,124.7z"/>
 53  		</g>
 54  	</g>
 55  	<g>
 56  		<path class="st0" d="M34.2,184.7l-2.1-4.2h-2.3v4.2h-2.3v-11.6h5.4c0.5,0,1.1,0.1,1.5,0.2c0.5,0.2,0.9,0.4,1.3,0.7
 57  			c0.4,0.3,0.6,0.7,0.8,1.2c0.2,0.5,0.3,1,0.3,1.6c0,0.9-0.2,1.6-0.6,2.2c-0.4,0.6-1,1-1.7,1.3l2.2,4.5H34.2z M34.1,175.7
 58  			c-0.3-0.2-0.7-0.3-1.2-0.3h-3.1v3h3.1c1.1,0,1.7-0.5,1.7-1.5C34.5,176.3,34.4,175.9,34.1,175.7z"/>
 59  		<path class="st0" d="M39.8,184.7v-11.6h8.1v2.3h-5.8v2h3.3v2.3h-3.3v2.8h6v2.3L39.8,184.7L39.8,184.7z"/>
 60  		<path class="st0" d="M60.1,181.5c-0.3,0.7-0.8,1.3-1.3,1.8c-0.6,0.5-1.2,0.8-1.9,1.1c-0.7,0.2-1.4,0.3-2.2,0.3h-3.5v-11.6h3.7
 61  			c0.8,0,1.6,0.1,2.3,0.3c0.7,0.2,1.3,0.5,1.9,1c0.5,0.5,0.9,1.1,1.2,1.8s0.4,1.6,0.4,2.7C60.6,179.9,60.4,180.8,60.1,181.5z
 62  			 M57.4,176.2c-0.5-0.6-1.4-0.9-2.6-0.9h-1.2v7.1h1.2c0.6,0,1.2-0.1,1.6-0.3c0.5-0.2,0.8-0.4,1.1-0.7c0.3-0.3,0.5-0.7,0.6-1.1
 63  			c0.2-0.4,0.2-0.9,0.2-1.4C58.2,177.7,57.9,176.9,57.4,176.2z"/>
 64  		<path class="st0" d="M75.8,184.7v-4.9h-4.8v4.9h-2.3v-11.6h2.3v4.4h4.8v-4.4h2.3v11.6H75.8z"/>
 65  		<path class="st0" d="M89.4,184.7l-0.9-2.6h-4.2l-0.9,2.6h-2.5l4.4-11.6h2.3l4.4,11.6H89.4z M87,177.8c-0.1-0.3-0.2-0.7-0.3-1
 66  			c-0.1-0.3-0.2-0.6-0.3-0.8c-0.1,0.2-0.2,0.5-0.3,0.8s-0.2,0.6-0.3,1l-0.7,2.1h2.6L87,177.8z"/>
 67  		<path class="st0" d="M97.9,175.4v9.4h-2.3v-9.4h-3.3v-2.3h9v2.3H97.9z"/>
 68  		<path class="st0" d="M117.1,184.7l-0.9-2.6h-4.2l-0.9,2.6h-2.5l4.4-11.6h2.3l4.4,11.6H117.1z M114.6,177.8c-0.1-0.3-0.2-0.7-0.3-1
 69  			c-0.1-0.3-0.2-0.6-0.3-0.8c-0.1,0.2-0.2,0.5-0.3,0.8s-0.2,0.6-0.3,1l-0.7,2.1h2.6L114.6,177.8z"/>
 70  		<path class="st0" d="M125.6,175.4v9.4h-2.3v-9.4H120v-2.3h9v2.3H125.6z"/>
 71  		<path class="st0" d="M140.4,181.4c-0.3,0.7-0.6,1.4-1.1,1.9s-1,0.9-1.6,1.2c-0.6,0.3-1.3,0.4-2.1,0.4s-1.5-0.2-2.1-0.4
 72  			c-0.6-0.3-1.2-0.7-1.6-1.2c-0.4-0.5-0.8-1.2-1.1-1.9c-0.3-0.7-0.4-1.6-0.4-2.5c0-1,0.1-1.8,0.4-2.5c0.3-0.7,0.6-1.4,1.1-1.9
 73  			c0.5-0.5,1-0.9,1.6-1.2c0.6-0.3,1.3-0.4,2.1-0.4c0.7,0,1.4,0.2,2.1,0.4s1.2,0.7,1.6,1.2c0.4,0.5,0.8,1.2,1.1,1.9
 74  			c0.3,0.7,0.4,1.6,0.4,2.5C140.8,179.8,140.6,180.7,140.4,181.4z M137.6,176.2c-0.5-0.6-1.2-1-2-1c-0.8,0-1.5,0.3-2,1
 75  			c-0.5,0.6-0.7,1.5-0.7,2.7c0,1.2,0.3,2.1,0.7,2.8c0.5,0.6,1.2,1,2,1c0.8,0,1.5-0.3,2-1c0.5-0.6,0.7-1.5,0.7-2.7
 76  			C138.4,177.8,138.1,176.8,137.6,176.2z"/>
 77  		<path class="st0" d="M152.2,184.7v-4.3c0-0.2,0-0.4,0-0.6c0-0.3,0-0.5,0-0.7s0-0.5,0-0.7c0-0.2,0-0.4,0-0.5
 78  			c-0.1,0.2-0.2,0.5-0.4,0.9c-0.2,0.4-0.3,0.7-0.5,1.1l-2.4,5.2l-2.3-5.2c-0.2-0.3-0.3-0.7-0.5-1.1c-0.2-0.4-0.3-0.6-0.4-0.9
 79  			c0,0.1,0,0.3,0,0.5s0,0.5,0,0.7s0,0.5,0,0.7c0,0.3,0,0.4,0,0.6v4.3h-2.3v-11.6h2.2l2.4,5.3c0.1,0.2,0.2,0.3,0.2,0.5
 80  			s0.2,0.4,0.2,0.5c0.1,0.2,0.2,0.3,0.2,0.5c0.1,0.2,0.1,0.3,0.2,0.4c0.1-0.2,0.2-0.5,0.3-0.9c0.2-0.4,0.3-0.7,0.5-1.1l2.3-5.3h2.3
 81  			v11.6L152.2,184.7L152.2,184.7z"/>
 82  		<path class="st0" d="M158.1,184.7v-11.6h2.3v11.6H158.1z"/>
 83  		<path class="st0" d="M170.8,176.5c-0.2-0.4-0.5-0.7-0.8-1c-0.3-0.2-0.8-0.3-1.3-0.3c-0.4,0-0.8,0.1-1.2,0.3
 84  			c-0.4,0.2-0.6,0.4-0.8,0.7c-0.2,0.3-0.4,0.7-0.5,1.2c-0.1,0.5-0.2,1-0.2,1.5s0.1,1,0.2,1.4s0.3,0.8,0.5,1.2
 85  			c0.2,0.3,0.5,0.6,0.8,0.8s0.7,0.3,1.2,0.3c0.5,0,1-0.1,1.3-0.4c0.3-0.2,0.7-0.6,1-1.1l2,1.2c-0.4,0.8-1,1.5-1.6,2
 86  			c-0.7,0.5-1.6,0.7-2.6,0.7c-0.7,0-1.5-0.2-2.1-0.4c-0.6-0.3-1.2-0.7-1.6-1.2c-0.5-0.5-0.8-1.2-1.1-1.9c-0.3-0.7-0.4-1.6-0.4-2.5
 87  			c0-0.9,0.1-1.7,0.4-2.4c0.3-0.7,0.6-1.4,1.1-1.9c0.5-0.5,1-1,1.6-1.2c0.6-0.3,1.3-0.4,2.1-0.4c0.5,0,1.1,0.1,1.5,0.2
 88  			c0.4,0.1,0.8,0.3,1.2,0.5s0.6,0.5,0.9,0.8c0.3,0.3,0.5,0.7,0.7,1.1L170.8,176.5z"/>
 89  	</g>
 90  </g>
 91  </svg>

```
  * file:///opt/input/source/src/main/webapp/bower_components/angular-patternfly/dist/docs/img/RH_atomic.svg
      * `beans_1_1.xsd`: In the root tag, replace the `version` attribute value with `3.0`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="utf-8"?>
  2  <!-- Generator: Adobe Illustrator 18.0.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
  3  <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
  4  <svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
  5  	 width="612px" height="792px" viewBox="0 0 612 792" enable-background="new 0 0 612 792" xml:space="preserve">
  6  <g>
  7  	<g>
  8  		<path fill="#00B9E4" d="M290.9,389.7c-0.7,0.5-1.3,1.2-1.8,1.6c-4.7,4.7-9.2,9-13.5,13c2.6,1.5,4.6,4,5.6,6.9
  9  			c5.1-4.6,10.4-9.5,15.8-14.9c1.2-1.1,2-4.1-0.2-6.2C295.2,388.7,292.6,388.4,290.9,389.7z"/>
 10  		<path fill="#00B9E4" d="M238.3,277.7c1.3,2,4.2,2.9,6.3,1.4c2.3-1.5,1.8-4.5,1.2-5.5c-18.4-31.3-26.7-55.2-19.4-60.9
 11  			c4.5-3.5,14.3,0.4,27.4,10c1.3-4.1,4.3-7.5,8.1-9.5c-21-15.7-37.6-22.3-45.4-16.2c-10.9,8.5-1.7,39.8,21,79.5
 12  			C237.8,276.9,238.1,277.3,238.3,277.7z"/>
 13  		<path fill="#00B9E4" d="M389.5,364.1c5.5-0.7,10.7-1.6,15.7-2.5c0,0,0,0,0,0c0,0,0,0,0,0c0,0,0,0,0,0c1.4-1.3,2.3-3.2,2.3-5.3
 14  			c0-3.4-2.4-6.2-5.5-6.9c0,0,0,0,0,0c-6.1,1-12.7,1.9-19.7,2.7l0,0l0,0c-10.8-17.6-24-36.6-39-55.7c-4.4-6-13.9-17.1-21.4-25.6
 15  			l0.1-0.1c36.6-40.7,68.9-65.5,78.2-58.2c7.2,5.6-1,29.5-19.4,60.9c-0.6,1-1.1,4,1.2,5.5c2.2,1.5,5.1,0.7,6.3-1.4
 16  			c0.2-0.3,0.5-0.8,0.7-1.1c22.7-39.7,31.9-71,21-79.5c-13.3-10.4-52.5,16.2-95,62.1c0,0-0.6,0.7-1.8,2c-1.1-1.2-1.8-2-1.8-2
 17  			c-9.2-9.9-18.3-19-26.9-26.9v0c-0.1-0.1-0.1-0.1-0.2-0.2c-0.4-0.1-0.8-0.1-1.2-0.1c-4,0-7.2,3.2-7.2,7.2c0,1,0.2,2,0.6,2.8l0,0
 18  			c8.8,8.3,18.2,18,28,28.8l0.1,0.1c-7.5,8.5-17,19.6-21.4,25.6c-15,19.1-28.2,38-39,55.7c-41.3-4.7-69.1-13.4-69-23.4
 19  			c0-10.2,29.4-19,72.5-23.5c0.5-0.1,0.8-0.2,1.3-0.2c2.3-0.4,3.5-2.6,3.4-4.4c0-2.3-1.7-4.6-4.9-4.5c-53.5,6-90.6,19.2-90.7,34.5
 20  			c-0.1,14.4,32.4,26.9,80.4,33.5c-22.5,39.4-31.5,70.4-20.6,78.9c7.9,6.2,25.1-0.7,46.6-17.1l0,0c0,0,0,0,0.1,0
 21  			c0.1-0.5,0.2-1,0.2-1.5c0-2.9-2.4-5.3-5.3-5.3c-0.3,0-0.5,0-0.7,0.1c0,0,0,0,0,0v0c-13.4,9.9-23.5,14.1-28,10.5
 22  			c-7.5-5.9,1.6-30.9,21.5-63.9c18.6,2,39.1,3.1,60.7,3.2v0c0.3,0,0.6,0,0.9,0c0,0,0,0,0,0l0,0c0.2,0,0.5,0,0.7,0h0h0.2c0,0,0,0,0,0
 23  			h0.2c0.2,0,0.5,0,0.7,0c0.3,0,0.6,0,0.9,0v0c21.5-0.1,42.1-1.2,60.7-3.2c19.9,33,29,58.1,21.5,63.9c-7.7,6-31.1-9.8-59.6-38.5
 24  			c-0.5-0.5-1.1-1.1-1.8-1.6c-1.8-1.3-4.3-1-5.7,0.4c-2.2,2.2-1.5,5.1-0.2,6.2c36.6,36.3,68.5,56,80.2,46.8
 25  			C421,434.6,412,403.6,389.5,364.1L389.5,364.1z M313.9,355.9c-0.2,0-0.3,0-0.5,0c-0.2,0-0.3,0-0.5,0c-19.3,0-37.7-0.8-54.3-2.3
 26  			c9.9-15.4,21.8-32,35.1-49c6-7.6,12-14.9,17.9-21.8v0c0.6-0.7,1.2-1.4,1.7-2c0.6,0.7,1.2,1.4,1.7,2v0c5.9,6.9,11.9,14.2,17.9,21.8
 27  			c13.4,17,25.2,33.6,35.1,49l0,0C351.6,355,333.2,355.8,313.9,355.9z"/>
 28  		<path fill="#00B9E4" d="M379.3,296.2c-3.2-0.1-4.9,2.2-4.9,4.5c-0.1,1.8,1.2,4,3.4,4.4c0.4,0.1,0.8,0.2,1.3,0.2
 29  			c43.1,4.5,72.4,13.3,72.5,23.5c0,3.6-3.6,7-10.2,10.2c2.1,3.3,3.4,7.3,3.4,11.5c0,0.3,0,0.7-0.1,1c16-6,25.2-13.2,25.2-20.8
 30  			C469.9,315.3,432.7,302.2,379.3,296.2z"/>
 31  	</g>
 32  	<g>
 33  		<path fill="#0088CE" d="M269.2,211.5c-8.9,0-16.2,7.2-16.2,16.2c0,8.9,7.2,16.2,16.2,16.2c2.7,0,5.2-0.7,7.4-1.8
 34  			c-0.4-0.9-0.6-1.8-0.6-2.8c0-4,3.2-7.2,7.2-7.2c0.4,0,0.8,0,1.2,0.1c0.1,0.1,0.1,0.1,0.2,0.2c0.4-1.5,0.7-3,0.7-4.6
 35  			C285.4,218.7,278.2,211.5,269.2,211.5z"/>
 36  		<path fill="#0088CE" d="M311.6,259.2c-0.7-0.8-1.4-1.5-2.2-2.3l-8.4,10c1.2,1.3,2.4,2.6,3.6,3.9l0.1,0.1c3.6-4.2,6.8-7.7,8.7-9.8
 37  			C312.3,259.9,311.6,259.2,311.6,259.2z"/>
 38  		<path fill="#0088CE" d="M313.4,280.8C313.4,280.8,313.4,280.8,313.4,280.8c0.6,0.7,1.2,1.4,1.7,2.1v0c1.9,2.2,3.7,4.4,5.6,6.6
 39  			l8.6-10.2c-2.5-2.9-4.9-5.7-7.2-8.3L313.4,280.8z"/>
 40  		<path fill="#0088CE" d="M423.4,329.2c-11.4,0-20.8,9-21.3,20.3c3.2,0.7,5.5,3.5,5.5,6.9c0,2.1-0.9,4-2.3,5.3c0,0,0,0,0,0
 41  			c3.8,6.1,10.5,10.2,18.1,10.2c11.8,0,21.3-9.6,21.3-21.3C444.8,338.7,435.2,329.2,423.4,329.2z"/>
 42  		<path fill="#0088CE" d="M237.3,364.1c-2.3,4-4.3,7.8-6.3,11.6l13.3,1.7c2.1-3.7,4.3-7.6,6.7-11.6L237.3,364.1L237.3,364.1z"/>
 43  		<path fill="#0088CE" d="M258.6,353.6c0.8-1.3,1.7-2.6,2.6-3.9L247,348c-0.9,1.4-1.8,2.8-2.7,4.2v0L258.6,353.6L258.6,353.6z"/>
 44  		<path fill="#0088CE" d="M382.5,352.2c-0.9-1.5-1.9-3-2.8-4.4l-14.2,1.8c0.9,1.4,1.9,2.8,2.7,4.1l0,0c0,0,0,0,0,0L382.5,352.2
 45  			L382.5,352.2z"/>
 46  		<path fill="#0088CE" d="M375.8,365.8C375.8,365.8,375.8,365.8,375.8,365.8c2.3,3.9,4.5,7.7,6.6,11.3l13.3-1.7
 47  			c-1.9-3.7-4-7.5-6.2-11.4L375.8,365.8z"/>
 48  		<path fill="#0088CE" d="M269.2,402.6c-6.9,0-12.5,5.6-12.5,12.5c0,1.5,0.3,2.9,0.7,4.2c0,0,0,0,0,0c0.2,0,0.5-0.1,0.7-0.1
 49  			c2.9,0,5.3,2.4,5.3,5.3c0,0.5-0.1,1-0.2,1.5c0,0,0,0-0.1,0c1.8,1,3.8,1.5,6,1.5c6.9,0,12.5-5.6,12.5-12.5
 50  			C281.7,408.2,276.1,402.6,269.2,402.6z"/>
 51  	</g>
 52  </g>
 53  <g>
 54  	<path fill="#00B9E4" d="M189.1,535.6l-3.9-7.9h-4.4v7.9h-4.4v-22h10.2c1,0,2,0.1,2.9,0.4c0.9,0.3,1.7,0.7,2.4,1.3
 55  		c0.7,0.6,1.2,1.3,1.6,2.2c0.4,0.9,0.6,1.9,0.6,3.1c0,1.7-0.4,3-1.1,4.1c-0.7,1.1-1.8,1.9-3.2,2.4l4.2,8.5H189.1z M188.8,518.6
 56  		c-0.6-0.4-1.3-0.6-2.3-0.6h-5.8v5.6h5.8c2.1,0,3.2-0.9,3.2-2.8C189.7,519.8,189.4,519,188.8,518.6z"/>
 57  	<path fill="#00B9E4" d="M199.7,535.6v-22H215v4.3h-10.9v3.8h6.3v4.3h-6.3v5.3h11.3v4.3H199.7z"/>
 58  	<path fill="#00B9E4" d="M237.9,529.6c-0.6,1.4-1.5,2.5-2.5,3.4c-1.1,0.9-2.3,1.5-3.6,2c-1.3,0.4-2.7,0.6-4.1,0.6h-6.6v-22h6.9
 59  		c1.6,0,3,0.2,4.3,0.6c1.3,0.4,2.5,1,3.5,1.9c1,0.9,1.7,2,2.3,3.4c0.6,1.4,0.8,3.1,0.8,5.1C238.9,526.6,238.6,528.2,237.9,529.6z
 60  		 M232.8,519.6c-1-1.1-2.7-1.7-5-1.7h-2.3v13.4h2.2c1.2,0,2.2-0.2,3-0.5c0.9-0.3,1.5-0.8,2.1-1.4c0.5-0.6,1-1.3,1.2-2.1
 61  		c0.3-0.8,0.4-1.7,0.4-2.7C234.4,522.4,233.9,520.8,232.8,519.6z"/>
 62  	<path fill="#00B9E4" d="M267.7,535.6v-9.2h-9v9.2h-4.4v-22h4.4v8.4h9v-8.4h4.4v22H267.7z"/>
 63  	<path fill="#00B9E4" d="M293.3,535.6l-1.7-4.9h-8l-1.7,4.9h-4.7l8.4-22h4.3l8.4,22H293.3z M288.7,522.6c-0.2-0.6-0.4-1.3-0.6-1.9
 64  		c-0.2-0.6-0.4-1.1-0.5-1.5c-0.1,0.4-0.3,0.9-0.5,1.5c-0.2,0.6-0.4,1.2-0.6,1.9l-1.4,4h5L288.7,522.6z"/>
 65  	<path fill="#00B9E4" d="M309.4,518v17.7h-4.4V518h-6.3v-4.3h17v4.3H309.4z"/>
 66  	<path fill="#00B9E4" d="M345.6,535.6l-1.7-4.9h-8l-1.7,4.9h-4.7l8.4-22h4.3l8.4,22H345.6z M341,522.6c-0.2-0.6-0.4-1.3-0.6-1.9
 67  		c-0.2-0.6-0.4-1.1-0.5-1.5c-0.1,0.4-0.3,0.9-0.5,1.5c-0.2,0.6-0.4,1.2-0.6,1.9l-1.4,4h5L341,522.6z"/>
 68  	<path fill="#00B9E4" d="M361.8,518v17.7h-4.4V518h-6.3v-4.3h17v4.3H361.8z"/>
 69  	<path fill="#00B9E4" d="M389.7,529.4c-0.5,1.4-1.1,2.6-2,3.6c-0.9,1-1.9,1.7-3.1,2.2c-1.2,0.5-2.5,0.8-3.9,0.8
 70  		c-1.4,0-2.8-0.3-3.9-0.8c-1.2-0.5-2.2-1.3-3-2.2c-0.8-1-1.5-2.2-2-3.5c-0.5-1.4-0.7-3-0.7-4.8c0-1.8,0.2-3.4,0.7-4.8
 71  		c0.5-1.4,1.1-2.6,2-3.6c0.9-1,1.9-1.7,3.1-2.2c1.2-0.5,2.5-0.8,4-0.8c1.4,0,2.7,0.3,3.9,0.8c1.2,0.5,2.2,1.3,3,2.2
 72  		c0.8,1,1.5,2.2,2,3.5c0.5,1.4,0.7,3,0.7,4.8C390.4,526.4,390.1,528,389.7,529.4z M384.4,519.5c-1-1.2-2.2-1.8-3.8-1.8
 73  		c-1.5,0-2.8,0.6-3.7,1.8c-0.9,1.2-1.4,2.9-1.4,5.1c0,2.2,0.5,4,1.4,5.2c1,1.2,2.2,1.8,3.8,1.8c1.5,0,2.8-0.6,3.7-1.8
 74  		c0.9-1.2,1.4-2.9,1.4-5.1C385.9,522.5,385.4,520.7,384.4,519.5z"/>
 75  	<path fill="#00B9E4" d="M411.9,535.6v-8.1c0-0.3,0-0.7,0-1.1c0-0.5,0-0.9,0-1.4c0-0.5,0-0.9,0-1.4c0-0.4,0-0.7,0-0.9
 76  		c-0.2,0.4-0.4,1-0.7,1.7c-0.3,0.7-0.6,1.4-0.9,2l-4.5,9.8l-4.4-9.8c-0.3-0.6-0.6-1.3-0.9-2c-0.3-0.7-0.5-1.2-0.7-1.7
 77  		c0,0.2,0,0.5,0,0.9c0,0.4,0,0.9,0,1.4c0,0.5,0,1,0,1.4c0,0.5,0,0.8,0,1.1v8.1h-4.3v-22h4.2l4.6,10c0.1,0.3,0.3,0.6,0.4,1
 78  		s0.3,0.7,0.4,1c0.1,0.3,0.3,0.6,0.4,0.9c0.1,0.3,0.2,0.5,0.3,0.7c0.1-0.4,0.4-1,0.6-1.7c0.3-0.7,0.6-1.4,0.9-2l4.4-10h4.3v22H411.9
 79  		z"/>
 80  	<path fill="#00B9E4" d="M423.2,535.6v-22h4.4v22H423.2z"/>
 81  	<path fill="#00B9E4" d="M447.1,520.1c-0.4-0.8-0.9-1.3-1.6-1.8c-0.6-0.4-1.5-0.6-2.5-0.6c-0.8,0-1.5,0.2-2.2,0.5s-1.2,0.8-1.6,1.4
 82  		c-0.4,0.6-0.8,1.3-1,2.2c-0.2,0.9-0.3,1.8-0.3,2.8c0,1,0.1,1.9,0.3,2.7c0.2,0.8,0.6,1.6,1,2.2c0.4,0.6,1,1.1,1.6,1.5
 83  		c0.6,0.4,1.4,0.5,2.2,0.5c1,0,1.8-0.2,2.5-0.7c0.6-0.4,1.3-1.2,1.8-2.1l3.7,2.2c-0.8,1.6-1.8,2.8-3.1,3.7c-1.3,0.9-3,1.3-5,1.3
 84  		c-1.4,0-2.8-0.3-3.9-0.8c-1.2-0.5-2.2-1.3-3-2.3c-0.9-1-1.5-2.2-2-3.6c-0.5-1.4-0.7-3-0.7-4.7c0-1.7,0.2-3.2,0.7-4.6
 85  		c0.5-1.4,1.2-2.6,2-3.6c0.9-1,1.9-1.8,3.1-2.3c1.2-0.6,2.5-0.8,4-0.8c1,0,2,0.1,2.8,0.4c0.8,0.2,1.6,0.6,2.2,1s1.2,0.9,1.7,1.5
 86  		c0.5,0.6,0.9,1.3,1.3,2L447.1,520.1z"/>
 87  </g>
 88  </svg>

```
  * file:///opt/input/source/src/main/webapp/bower_components/angular-patternfly/dist/docs/img/logo-alt.svg
      * `beans_1_1.xsd`: In the root tag, replace the `version` attribute value with `3.0`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="utf-8"?>
  2  <!-- Generator: Adobe Illustrator 16.0.4, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
  3  <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
  4  <svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
  5  	 width="37px" height="35px" viewBox="0 0 37 35" enable-background="new 0 0 37 35" xml:space="preserve">
  6  <linearGradient id="SVGID_1_" gradientUnits="userSpaceOnUse" x1="231.8955" y1="-269.5547" x2="231.8955" y2="-301.7199" gradientTransform="matrix(1 0 0 -1 -213.5 -268.5)">
  7  	<stop  offset="0" style="stop-color:#60EFFF"/>
  8  	<stop  offset="1" style="stop-color:#1F89C7"/>
  9  </linearGradient>
 10  <path fill="url(#SVGID_1_)" d="M36.792,17.992L18.398,0L0,17.992l7.333,10.39l5.595-1.285l5.503,7.737l5.493-7.724l5.533,1.27
 11  	L36.792,17.992z M17.634,3.336L15.25,25.355l-4.549-6.205L17.634,3.336z M10.202,18.47l-2.833-3.866l9.743-11.833L10.202,18.47z
 12  	 M14.495,25.562L14.495,25.562l0.265,0.365l-1.52,0.348l-3.507-4.93l0.626-1.424L14.495,25.562z M18.396,3.044l2.395,23.345
 13  	l-2.4,3.288L16,26.389L18.396,3.044z M22.296,25.562l4.181-5.702l0.654,1.485l-3.517,4.944l-1.58-0.362l0.264-0.363L22.296,25.562z
 14  	 M21.542,25.355L19.189,3.318l6.946,15.77L21.542,25.355z M19.744,2.767l9.679,11.837l-2.787,3.802L19.744,2.767z M7.647,27.56
 15  	l-6.692-9.48L14.051,5.278l-7.605,9.302l3.417,4.661l-0.964,2.188l3.572,5.023L7.647,27.56z M18.432,33.573l-4.733-6.653
 16  	l1.528-0.352l3.162,4.351l3.173-4.351l1.592,0.367L18.432,33.573z M24.384,26.466l3.581-5.037l-0.99-2.248l3.372-4.6l-7.605-9.302
 17  	l13.095,12.801l-6.692,9.48L24.384,26.466z"/>
 18  </svg>

```
  * file:///opt/input/source/src/main/webapp/bower_components/angular-patternfly/dist/docs/img/brand.svg
      * `beans_1_1.xsd`: In the root tag, replace the `version` attribute value with `3.0`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="utf-8"?>
  2  <!-- Generator: Adobe Illustrator 16.0.4, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
  3  <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
  4  <svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
  5  	 width="270px" height="10px" viewBox="0 0 270 10" enable-background="new 0 0 270 10" xml:space="preserve">
  6  <g>
  7  	<g>
  8  		<path fill="#FFFFFF" d="M121.965,9.413h-4.883V0.656h4.883v0.903h-3.862V4.38h3.63v0.898h-3.63V8.5h3.862V9.413z"/>
  9  		<path fill="#FFFFFF" d="M130.988,9.413h-1.158l-4.789-7.352h-0.046c0.062,0.864,0.095,1.655,0.095,2.374v4.978h-0.94V0.656h1.15
 10  			l4.774,7.317h0.045c-0.006-0.107-0.022-0.453-0.051-1.041c-0.028-0.582-0.039-0.998-0.028-1.254V0.656h0.951v8.753h-0.003V9.413
 11  			L130.988,9.413z"/>
 12  		<path fill="#FFFFFF" d="M136.339,9.413h-1.018V1.561h-2.771V0.656h6.564v0.903h-2.771v7.852h-0.002v0.002H136.339z"/>
 13  		<path fill="#FFFFFF" d="M145.554,9.413h-4.877V0.656h4.877v0.903h-3.859V4.38h3.631v0.898h-3.631V8.5h3.859V9.413z"/>
 14  		<path fill="#FFFFFF" d="M148.761,5.769v3.641h-1.018V0.656h2.402c1.074,0,1.865,0.204,2.379,0.614
 15  			c0.514,0.412,0.771,1.032,0.771,1.858c0,1.156-0.586,1.94-1.764,2.349l2.383,3.934h-1.207l-2.121-3.645h-1.826V5.769
 16  			L148.761,5.769z M148.761,4.897h1.396c0.719,0,1.244-0.142,1.582-0.428c0.334-0.286,0.504-0.714,0.504-1.285
 17  			c0-0.582-0.17-0.997-0.512-1.254c-0.34-0.255-0.889-0.381-1.643-0.381h-1.324v3.349h-0.004V4.897z"/>
 18  		<path fill="#FFFFFF" d="M161.124,3.209c0,0.884-0.301,1.567-0.904,2.046c-0.605,0.477-1.475,0.714-2.6,0.714h-1.031v3.444h-1.016
 19  			V0.656h2.27C160.03,0.656,161.124,1.504,161.124,3.209z M156.589,5.092h0.92c0.898,0,1.555-0.146,1.959-0.435
 20  			c0.4-0.293,0.604-0.759,0.604-1.404c0-0.577-0.188-1.006-0.568-1.295c-0.381-0.279-0.973-0.423-1.773-0.423h-1.139v3.557H156.589z
 21  			"/>
 22  		<path fill="#FFFFFF" d="M164.22,5.769v3.641h-1.02V0.656h2.402c1.074,0,1.865,0.204,2.383,0.614
 23  			c0.512,0.412,0.771,1.032,0.771,1.858c0,1.156-0.588,1.94-1.762,2.349l2.379,3.934h-1.205l-2.119-3.645h-1.826v0.002H164.22z
 24  			 M164.22,4.897h1.395c0.719,0,1.244-0.142,1.582-0.428c0.334-0.286,0.504-0.714,0.504-1.285c0-0.582-0.17-0.997-0.51-1.254
 25  			c-0.34-0.255-0.887-0.381-1.645-0.381h-1.322v3.349h-0.004V4.897z"/>
 26  		<path fill="#FFFFFF" d="M171.03,9.413V0.656h1.018v8.753h-1.018V9.413z"/>
 27  		<path fill="#FFFFFF" d="M179.636,7.081c0,0.773-0.281,1.374-0.838,1.805c-0.561,0.434-1.318,0.646-2.277,0.646
 28  			c-1.039,0-1.836-0.134-2.395-0.4V8.147c0.357,0.152,0.75,0.272,1.174,0.357c0.422,0.088,0.844,0.131,1.258,0.131
 29  			c0.68,0,1.188-0.129,1.531-0.384c0.346-0.257,0.514-0.62,0.514-1.073c0-0.304-0.061-0.556-0.184-0.748
 30  			c-0.119-0.194-0.318-0.375-0.607-0.537c-0.285-0.162-0.721-0.351-1.301-0.558c-0.816-0.29-1.398-0.636-1.748-1.036
 31  			c-0.352-0.398-0.525-0.92-0.525-1.562c0-0.674,0.254-1.211,0.764-1.611c0.508-0.398,1.178-0.599,2.014-0.599
 32  			c0.869,0,1.672,0.161,2.398,0.48l-0.316,0.884c-0.725-0.3-1.428-0.454-2.109-0.454c-0.539,0-0.959,0.114-1.266,0.347
 33  			c-0.303,0.231-0.453,0.553-0.453,0.965c0,0.305,0.057,0.551,0.168,0.745c0.115,0.195,0.303,0.372,0.566,0.533
 34  			c0.268,0.161,0.672,0.34,1.221,0.535c0.92,0.327,1.551,0.679,1.896,1.056C179.462,5.995,179.636,6.483,179.636,7.081z"/>
 35  		<path fill="#FFFFFF" d="M186.556,9.413h-4.881V0.656h4.881v0.903h-3.863V4.38h3.633v0.898h-3.633V8.5h3.863V9.413z"/>
 36  		<path fill="#FFFFFF" d="M197.677,9.413l-1.09-2.785h-3.51l-1.078,2.785h-1.031l3.463-8.793h0.854l3.443,8.793H197.677z
 37  			 M196.267,5.71l-1.018-2.712c-0.131-0.345-0.271-0.766-0.406-1.263c-0.09,0.383-0.211,0.804-0.377,1.263l-1.031,2.712H196.267z"/>
 38  		<path fill="#FFFFFF" d="M205.733,3.209c0,0.884-0.303,1.567-0.908,2.046c-0.607,0.477-1.473,0.714-2.596,0.714h-1.031v3.444
 39  			h-1.021V0.656h2.273C204.642,0.656,205.733,1.504,205.733,3.209z M201.2,5.092h0.914c0.902,0,1.557-0.146,1.961-0.435
 40  			c0.398-0.293,0.605-0.759,0.605-1.404c0-0.577-0.189-1.006-0.57-1.295c-0.381-0.279-0.969-0.423-1.773-0.423H201.2V5.092
 41  			L201.2,5.092z"/>
 42  		<path fill="#FFFFFF" d="M213.366,3.209c0,0.884-0.307,1.567-0.908,2.046c-0.607,0.477-1.473,0.714-2.598,0.714h-1.031v3.444h-1.02
 43  			V0.656h2.271C212.269,0.656,213.366,1.504,213.366,3.209z M208.827,5.092h0.918c0.904,0,1.559-0.146,1.959-0.435
 44  			c0.404-0.293,0.604-0.759,0.604-1.404c0-0.577-0.188-1.006-0.566-1.295c-0.381-0.279-0.971-0.423-1.773-0.423h-1.141V5.092
 45  			L208.827,5.092z"/>
 46  		<path fill="#FFFFFF" d="M215.44,9.413V0.656h1.021v7.832h3.857V9.41h-4.879V9.413z"/>
 47  		<path fill="#FFFFFF" d="M222.052,9.413V0.656h1.021v8.753h-1.021V9.413z"/>
 48  		<path fill="#FFFFFF" d="M229.466,1.44c-0.959,0-1.721,0.32-2.279,0.959c-0.557,0.642-0.834,1.518-0.834,2.633
 49  			c0,1.146,0.27,2.031,0.807,2.656c0.537,0.621,1.303,0.937,2.299,0.937c0.611,0,1.309-0.108,2.09-0.327v0.891
 50  			c-0.605,0.229-1.355,0.343-2.244,0.343c-1.289,0-2.285-0.396-2.988-1.181c-0.699-0.776-1.051-1.891-1.051-3.333
 51  			c0-0.902,0.17-1.69,0.506-2.371c0.336-0.678,0.824-1.202,1.461-1.569s1.387-0.551,2.248-0.551c0.918,0,1.719,0.168,2.408,0.504
 52  			l-0.432,0.875C230.798,1.594,230.13,1.44,229.466,1.44z"/>
 53  		<path fill="#FFFFFF" d="M239.204,9.413l-1.09-2.785h-3.512l-1.074,2.785h-1.031l3.459-8.793h0.857l3.445,8.793H239.204z
 54  			 M237.798,5.71l-1.018-2.712c-0.133-0.345-0.27-0.766-0.406-1.263c-0.088,0.383-0.215,0.804-0.377,1.263l-1.033,2.712H237.798z"/>
 55  		<path fill="#FFFFFF" d="M244.401,9.413h-1.016V1.561h-2.773V0.656h6.564v0.903h-2.771v7.852h-0.004V9.413z"/>
 56  		<path fill="#FFFFFF" d="M248.743,9.413V0.656h1.018v8.753h-1.018V9.413z"/>
 57  		<path fill="#FFFFFF" d="M260.005,5.021c0,1.402-0.354,2.503-1.062,3.305c-0.707,0.806-1.691,1.206-2.955,1.206
 58  			c-1.291,0-2.285-0.396-2.988-1.186c-0.699-0.789-1.051-1.901-1.051-3.338c0-1.424,0.354-2.532,1.057-3.312
 59  			c0.699-0.785,1.703-1.18,2.99-1.18c1.262,0,2.24,0.399,2.951,1.2C259.655,2.513,260.005,3.614,260.005,5.021z M253.03,5.021
 60  			c0,1.186,0.25,2.085,0.754,2.697c0.508,0.613,1.242,0.922,2.203,0.922c0.973,0,1.705-0.311,2.201-0.918
 61  			c0.494-0.615,0.738-1.516,0.738-2.702c0-1.179-0.244-2.072-0.736-2.681c-0.49-0.61-1.223-0.914-2.189-0.914
 62  			c-0.969,0-1.705,0.306-2.213,0.918C253.282,2.96,253.03,3.851,253.03,5.021z"/>
 63  		<path fill="#FFFFFF" d="M269.044,9.413h-1.162l-4.783-7.352h-0.049c0.061,0.864,0.094,1.655,0.094,2.374v4.978H262.2V0.656h1.152
 64  			l4.771,7.319h0.049c-0.012-0.108-0.025-0.455-0.055-1.041c-0.027-0.582-0.041-0.998-0.029-1.256V0.656h0.951v8.755h0.006v0.002
 65  			H269.044z"/>
 66  	</g>
 67  	<g>
 68  		<path fill="#FFFFFF" d="M7.533,3.368c0,1.013-0.298,1.796-0.896,2.348C6.04,6.269,5.191,6.544,4.093,6.544H3.403v3.008H0.954
 69  			V0.485h3.139c1.145,0,2.005,0.25,2.58,0.75C7.246,1.736,7.533,2.447,7.533,3.368z M3.403,4.547h0.447
 70  			c0.368,0,0.66-0.103,0.877-0.31s0.326-0.492,0.326-0.856c0-0.612-0.339-0.918-1.018-0.918H3.403V4.547z"/>
 71  		<path fill="#FFFFFF" d="M17.652,9.552l-0.446-1.699h-2.944l-0.459,1.699h-2.691l2.958-9.104h3.268l2.995,9.104H17.652z
 72  			 M16.697,5.843l-0.39-1.489c-0.092-0.33-0.202-0.758-0.333-1.283c-0.13-0.525-0.216-0.901-0.257-1.128
 73  			c-0.037,0.211-0.111,0.558-0.221,1.042c-0.108,0.483-0.353,1.437-0.729,2.857H16.697z"/>
 74  		<path fill="#FFFFFF" d="M28.423,9.552h-2.449V2.488H23.76V0.485h6.871v2.003h-2.208V9.552z"/>
 75  		<path fill="#FFFFFF" d="M39.037,9.552h-2.449V2.488h-2.214V0.485h6.871v2.003h-2.208V9.552z"/>
 76  		<path fill="#FFFFFF" d="M51.035,9.552h-5.382V0.485h5.382V2.45h-2.933v1.427h2.716v1.966h-2.716v1.711h2.933V9.552z"/>
 77  		<path fill="#FFFFFF" d="M58.184,6.253v3.299h-2.449V0.485h2.97c2.464,0,3.696,0.893,3.696,2.679c0,1.05-0.513,1.862-1.538,2.437
 78  			l2.642,3.951h-2.777l-1.922-3.299H58.184z M58.184,4.41h0.459c0.855,0,1.284-0.378,1.284-1.135c0-0.625-0.42-0.937-1.26-0.937
 79  			h-0.483V4.41z"/>
 80  		<path fill="#FFFFFF" d="M76.072,9.552H72.86L69.55,3.164h-0.057c0.079,1.004,0.118,1.771,0.118,2.301v4.086h-2.17V0.485h3.2
 81  			l3.299,6.301h0.037c-0.059-0.914-0.086-1.648-0.086-2.202V0.485h2.183v9.066H76.072z"/>
 82  		<path fill="#FFFFFF" d="M83.557,9.552h-2.412V0.485h5.356V2.45h-2.944v1.73h2.716v1.965h-2.716V9.552z"/>
 83  		<path fill="#FFFFFF" d="M91.102,9.552V0.485h2.449v7.088h3.49v1.979H91.102z"/>
 84  		<path fill="#FFFFFF" d="M104.842,3.846l1.562-3.361h2.654l-2.983,5.525v3.541h-2.468V6.085l-2.983-5.6h2.667L104.842,3.846z"/>
 85  	</g>
 86  </g>
 87  </svg>

```
  * file:///opt/input/source/src/main/webapp/bower_components/angular-patternfly/dist/docs/img/bg-navbar-pf-alt.svg
      * `beans_1_1.xsd`: In the root tag, replace the `version` attribute value with `3.0`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="utf-8"?>
  2  <!-- Generator: Adobe Illustrator 16.0.4, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
  3  <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
  4  <svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
  5  	 width="615.598px" height="57px" viewBox="25.562 0 615.598 57" enable-background="new 25.562 0 615.598 57" xml:space="preserve"
  6  	>
  7  <polygon opacity="0.1" fill="#FFFFFF" enable-background="new    " points="566.242,56.969 623.205,0 641.16,0 584.68,56.969 "/>
  8  <polygon opacity="0.1" fill="#FFFFFF" enable-background="new    " points="25.562,57 25.562,0 611.034,0 554.554,56.95 "/>
  9  </svg>

```
  * file:///opt/input/source/src/main/webapp/bower_components/angular-patternfly/dist/docs/img/brand-alt.svg
      * `beans_1_1.xsd`: In the root tag, replace the `version` attribute value with `3.0`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="utf-8"?>
  2  <!-- Generator: Adobe Illustrator 16.0.4, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
  3  <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
  4  <svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
  5  	 width="324px" height="11px" viewBox="1.145 0.538 324 11" enable-background="new 1.145 0.538 324 11" xml:space="preserve">
  6  <g>
  7  	<g>
  8  		<path fill="#FFFFFF" d="M147.351,11.368h-5.899V0.789h5.899V1.88h-4.666v3.408h4.386v1.085h-4.386v3.894h4.666V11.368z"/>
  9  		<path fill="#FFFFFF" d="M158.252,11.368h-1.399l-5.786-8.882h-0.056c0.075,1.044,0.115,2,0.115,2.868v6.014h-1.136V0.789h1.39
 10  			l5.768,8.84h0.054c-0.007-0.129-0.027-0.548-0.062-1.258c-0.034-0.702-0.047-1.205-0.034-1.515V0.789h1.149v10.576h-0.004V11.368
 11  			L158.252,11.368z"/>
 12  		<path fill="#FFFFFF" d="M164.719,11.368h-1.23V1.882h-3.349V0.789h7.932V1.88h-3.349v9.486h-0.002v0.002H164.719z"/>
 13  		<path fill="#FFFFFF" d="M175.852,11.368h-5.893V0.789h5.893V1.88h-4.662v3.408h4.386v1.085h-4.386v3.894h4.662V11.368z"/>
 14  		<path fill="#FFFFFF" d="M179.727,6.967v4.398h-1.231V0.789h2.903c1.298,0,2.253,0.247,2.875,0.742
 15  			c0.62,0.498,0.931,1.247,0.931,2.245c0,1.396-0.708,2.344-2.131,2.838l2.879,4.753h-1.459l-2.562-4.403h-2.206v0.004H179.727z
 16  			 M179.727,5.913h1.687c0.868,0,1.503-0.172,1.911-0.517c0.404-0.346,0.608-0.863,0.608-1.553c0-0.703-0.204-1.205-0.618-1.515
 17  			c-0.41-0.308-1.075-0.46-1.985-0.46h-1.6v4.046h-0.005V5.913H179.727z"/>
 18  		<path fill="#FFFFFF" d="M194.663,3.873c0,1.068-0.363,1.894-1.093,2.473c-0.73,0.576-1.781,0.861-3.141,0.861h-1.246v4.161h-1.228
 19  			V0.789h2.743C193.342,0.789,194.663,1.813,194.663,3.873z M189.184,6.148h1.111c1.085,0,1.88-0.176,2.367-0.525
 20  			c0.483-0.354,0.729-0.917,0.729-1.696c0-0.697-0.227-1.216-0.687-1.565c-0.46-0.337-1.175-0.511-2.142-0.511h-1.376v4.298H189.184
 21  			z"/>
 22  		<path fill="#FFFFFF" d="M198.404,6.967v4.398h-1.233V0.789h2.902c1.298,0,2.254,0.247,2.879,0.742
 23  			c0.619,0.498,0.933,1.247,0.933,2.245c0,1.396-0.711,2.344-2.13,2.838l2.875,4.753h-1.456l-2.561-4.403h-2.206v0.003
 24  			L198.404,6.967L198.404,6.967z M198.404,5.913h1.686c0.868,0,1.502-0.172,1.911-0.517c0.403-0.346,0.608-0.863,0.608-1.553
 25  			c0-0.703-0.205-1.205-0.616-1.515c-0.411-0.308-1.072-0.46-1.987-0.46h-1.598v4.046L198.404,5.913L198.404,5.913z"/>
 26  		<path fill="#FFFFFF" d="M206.632,11.368V0.789h1.229v10.576h-1.229V11.368z"/>
 27  		<path fill="#FFFFFF" d="M217.028,8.552c0,0.934-0.338,1.66-1.012,2.181c-0.677,0.524-1.592,0.78-2.751,0.78
 28  			c-1.256,0-2.218-0.162-2.894-0.482V9.84c0.431,0.184,0.906,0.329,1.418,0.432c0.51,0.105,1.021,0.157,1.521,0.157
 29  			c0.821,0,1.435-0.155,1.85-0.463c0.418-0.312,0.622-0.75,0.622-1.297c0-0.367-0.075-0.672-0.223-0.904
 30  			c-0.145-0.233-0.386-0.453-0.733-0.647c-0.345-0.197-0.871-0.425-1.572-0.675c-0.986-0.35-1.689-0.769-2.112-1.251
 31  			c-0.426-0.481-0.634-1.112-0.634-1.888c0-0.814,0.307-1.463,0.922-1.946c0.614-0.48,1.424-0.724,2.435-0.724
 32  			c1.05,0,2.02,0.195,2.897,0.58l-0.382,1.068c-0.876-0.362-1.726-0.548-2.549-0.548c-0.65,0-1.158,0.138-1.53,0.418
 33  			c-0.365,0.279-0.546,0.668-0.546,1.167c0,0.369,0.068,0.666,0.202,0.9c0.14,0.235,0.366,0.449,0.685,0.644
 34  			c0.323,0.194,0.812,0.411,1.475,0.646c1.111,0.395,1.874,0.82,2.291,1.276C216.819,7.239,217.028,7.829,217.028,8.552z"/>
 35  		<path fill="#FFFFFF" d="M225.391,11.368h-5.898V0.789h5.898V1.88h-4.668v3.408h4.391v1.085h-4.391v3.894h4.668V11.368z"/>
 36  		<path fill="#FFFFFF" d="M238.827,11.368l-1.317-3.364h-4.241l-1.303,3.364h-1.244l4.184-10.623h1.031l4.16,10.623H238.827z
 37  			 M237.123,6.895l-1.229-3.276c-0.159-0.417-0.328-0.926-0.491-1.526c-0.109,0.462-0.255,0.971-0.455,1.526l-1.246,3.276H237.123z"
 38  			/>
 39  		<path fill="#FFFFFF" d="M248.56,3.873c0,1.068-0.366,1.894-1.097,2.473c-0.733,0.576-1.779,0.861-3.137,0.861h-1.245v4.161h-1.233
 40  			V0.789h2.745C247.241,0.789,248.56,1.813,248.56,3.873z M243.083,6.148h1.104c1.09,0,1.881-0.176,2.37-0.525
 41  			c0.479-0.354,0.73-0.917,0.73-1.696c0-0.697-0.229-1.216-0.689-1.565c-0.46-0.337-1.17-0.511-2.142-0.511h-1.374V6.148
 42  			L243.083,6.148z"/>
 43  		<path fill="#FFFFFF" d="M257.782,3.873c0,1.068-0.371,1.894-1.098,2.473c-0.733,0.576-1.779,0.861-3.139,0.861h-1.245v4.161
 44  			h-1.232V0.789h2.743C256.457,0.789,257.782,1.813,257.782,3.873z M252.298,6.148h1.108c1.094,0,1.884-0.176,2.368-0.525
 45  			c0.487-0.354,0.729-0.917,0.729-1.696c0-0.697-0.228-1.216-0.685-1.565c-0.46-0.337-1.172-0.511-2.142-0.511H252.3v4.298H252.298z
 46  			"/>
 47  		<path fill="#FFFFFF" d="M260.287,11.368V0.789h1.235v9.463h4.659v1.113h-5.895V11.368L260.287,11.368z"/>
 48  		<path fill="#FFFFFF" d="M268.277,11.368V0.789h1.232v10.576h-1.232V11.368z"/>
 49  		<path fill="#FFFFFF" d="M277.234,1.736c-1.158,0-2.079,0.386-2.753,1.159c-0.674,0.776-1.009,1.833-1.009,3.181
 50  			c0,1.385,0.326,2.454,0.976,3.209c0.648,0.75,1.575,1.132,2.777,1.132c0.738,0,1.582-0.13,2.526-0.396v1.077
 51  			c-0.732,0.276-1.639,0.414-2.712,0.414c-1.558,0-2.761-0.479-3.61-1.427c-0.844-0.938-1.27-2.284-1.27-4.027
 52  			c0-1.089,0.205-2.042,0.61-2.865c0.407-0.819,0.996-1.452,1.766-1.896c0.77-0.444,1.676-0.666,2.716-0.666
 53  			c1.109,0,2.077,0.203,2.909,0.609l-0.521,1.057C278.843,1.922,278.037,1.736,277.234,1.736z"/>
 54  		<path fill="#FFFFFF" d="M289,11.368l-1.317-3.364h-4.243l-1.298,3.364h-1.245l4.18-10.623h1.035l4.162,10.623H289z M287.301,6.895
 55  			l-1.229-3.276c-0.162-0.417-0.327-0.926-0.492-1.526c-0.106,0.462-0.26,0.971-0.455,1.526l-1.248,3.276H287.301z"/>
 56  		<path fill="#FFFFFF" d="M295.279,11.368h-1.228V1.882h-3.351V0.789h7.931V1.88h-3.348v9.486h-0.005V11.368z"/>
 57  		<path fill="#FFFFFF" d="M300.525,11.368V0.789h1.229v10.576h-1.229V11.368z"/>
 58  		<path fill="#FFFFFF" d="M314.132,6.063c0,1.693-0.428,3.024-1.283,3.993c-0.854,0.975-2.043,1.457-3.57,1.457
 59  			c-1.56,0-2.761-0.479-3.61-1.433c-0.844-0.953-1.27-2.297-1.27-4.033c0-1.721,0.428-3.06,1.277-4.002
 60  			c0.844-0.948,2.057-1.426,3.612-1.426c1.525,0,2.706,0.482,3.565,1.45C313.709,3.033,314.132,4.363,314.132,6.063z M305.705,6.063
 61  			c0,1.432,0.301,2.519,0.91,3.258c0.614,0.74,1.501,1.114,2.662,1.114c1.175,0,2.06-0.377,2.658-1.109
 62  			c0.598-0.743,0.893-1.832,0.893-3.265c0-1.424-0.295-2.503-0.89-3.239c-0.592-0.737-1.478-1.104-2.645-1.104
 63  			c-1.17,0-2.06,0.37-2.675,1.109C306.009,3.572,305.705,4.649,305.705,6.063z"/>
 64  		<path fill="#FFFFFF" d="M325.053,11.368h-1.404l-5.778-8.882h-0.06c0.074,1.044,0.113,2,0.113,2.868v6.014h-1.141V0.789h1.393
 65  			l5.765,8.843h0.059c-0.015-0.131-0.03-0.551-0.066-1.259c-0.032-0.701-0.05-1.205-0.034-1.517V0.789h1.148v10.578h0.008v0.002
 66  			H325.053z"/>
 67  	</g>
 68  	<g>
 69  		<path fill="#FFFFFF" d="M9.094,4.065c0,1.224-0.36,2.17-1.083,2.837C7.29,7.571,6.264,7.903,4.938,7.903H4.104v3.634H1.145V0.583
 70  			h3.792c1.383,0,2.422,0.302,3.117,0.906C8.747,2.094,9.094,2.953,9.094,4.065z M4.104,5.49h0.541c0.444,0,0.797-0.125,1.059-0.375
 71  			c0.262-0.25,0.394-0.595,0.394-1.035c0-0.739-0.41-1.109-1.23-1.109H4.104V5.49z"/>
 72  		<path fill="#FFFFFF" d="M21.32,11.537l-0.54-2.053h-3.557l-0.555,2.053h-3.251l3.573-11h3.949l3.619,11H21.32z M20.166,7.056
 73  			l-0.472-1.799c-0.111-0.399-0.244-0.916-0.402-1.55c-0.157-0.634-0.261-1.088-0.311-1.363c-0.045,0.255-0.134,0.674-0.267,1.259
 74  			c-0.13,0.583-0.427,1.736-0.881,3.451h2.333V7.056z"/>
 75  		<path fill="#FFFFFF" d="M34.333,11.537h-2.959V3.002h-2.675V0.583h8.302v2.419h-2.668V11.537z"/>
 76  		<path fill="#FFFFFF" d="M47.157,11.537h-2.958V3.002h-2.675V0.583h8.301v2.419h-2.668V11.537z"/>
 77  		<path fill="#FFFFFF" d="M61.653,11.537H55.15V0.583h6.503v2.374h-3.544v1.724h3.281v2.375h-3.281v2.067h3.544V11.537z"/>
 78  		<path fill="#FFFFFF" d="M70.291,7.552v3.985h-2.959V0.583h3.588c2.977,0,4.466,1.079,4.466,3.237c0,1.268-0.62,2.25-1.858,2.943
 79  			l3.192,4.774h-3.355l-2.322-3.985H70.291z M70.291,5.325h0.554c1.033,0,1.552-0.457,1.552-1.371c0-0.755-0.508-1.132-1.522-1.132
 80  			h-0.583V5.325z"/>
 81  		<path fill="#FFFFFF" d="M91.903,11.537h-3.881l-3.999-7.718h-0.069c0.095,1.213,0.143,2.139,0.143,2.78v4.936h-2.622V0.583h3.866
 82  			l3.986,7.612h0.044c-0.071-1.103-0.104-1.99-0.104-2.659V0.583h2.637v10.953h-0.002V11.537z"/>
 83  		<path fill="#FFFFFF" d="M100.946,11.537h-2.914V0.583h6.471v2.374h-3.557v2.09h3.282v2.374h-3.282V11.537z"/>
 84  		<path fill="#FFFFFF" d="M110.062,11.537V0.583h2.959v8.564h4.217v2.391H110.062z"/>
 85  		<path fill="#FFFFFF" d="M126.663,4.643l1.887-4.061h3.207l-3.604,6.675v4.277h-2.982V7.348l-3.604-6.765h3.222L126.663,4.643z"/>
 86  	</g>
 87  </g>
 88  </svg>

```
  * file:///opt/input/source/src/main/webapp/bower_components/angular-patternfly/dist/docs/img/logo.svg
      * `beans_1_1.xsd`: In the root tag, replace the `version` attribute value with `3.0`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="utf-8"?>
  2  <!-- Generator: Adobe Illustrator 16.0.3, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
  3  <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
  4  <svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
  5  	 width="73px" height="69px" viewBox="0 0 73 69" enable-background="new 0 0 73 69" xml:space="preserve">
  6  <g>
  7  	<linearGradient id="SVGID_1_" gradientUnits="userSpaceOnUse" x1="36.2046" y1="2.1504" x2="36.2046" y2="68.6623">
  8  		<stop  offset="0" style="stop-color:#60EFFF"/>
  9  		<stop  offset="1" style="stop-color:#1F89C7"/>
 10  	</linearGradient>
 11  	<path fill="url(#SVGID_1_)" d="M36.287,0.137l0.008-0.063l-0.031,0.039l-0.012-0.012L36.262,0l-0.057,0.056L36.148,0l0.011,0.101
 12  		l-0.013,0.012l-0.03-0.039l0.007,0.063L0,35.447l14.307,20.267l11.05-2.538l10.848,15.255l10.85-15.255l11.05,2.538l8.861-12.554
 13  		l5.444-7.713L36.287,0.137z M35.108,4.282L30.174,50.52l-9.642-13.151L35.108,4.282z M20.059,36.725l-6.068-8.277L35.057,2.683
 14  		L20.059,36.725z M29.967,51.407l-4.313,0.99l-7.251-10.193l1.807-4.104L29.967,51.407z M36.092,2.051l0.113-0.258l0.114,0.257
 15  		l5.102,49.711l-0.015-0.01l-4.999,7.387l-5.409-7.396l-0.007,0.004L36.092,2.051z M42.237,50.521L37.303,4.281l14.576,33.087
 16  		L42.237,50.521z M52.201,38.101l1.808,4.104l-7.251,10.193l-4.312-0.99L52.201,38.101z M37.355,2.684L58.42,28.448l-6.067,8.277
 17  		L37.355,2.684z M14.605,54.935L0.907,35.53L32.779,4.374L13.114,28.425l6.623,9.03l-2.127,4.83l7.312,10.28L14.605,54.935z
 18  		 M36.205,67.235L26.086,53.009l4.326-0.992l0.072,0.099l-0.045,0.034l5.988,8.191l5.552-8.201l-0.048-0.032L42,52.017l4.324,0.992
 19  		L36.205,67.235z M66.4,42.762l-8.594,12.173l-10.317-2.369l7.312-10.28l-2.127-4.83l6.622-9.03L39.633,4.374L71.504,35.53
 20  		L66.4,42.762z"/>
 21  </g>
 22  </svg>

```
  * file:///opt/input/source/src/main/webapp/bower_components/angular-patternfly/dist/docs/img/patternfly-orb.svg
      * `beans_1_1.xsd`: In the root tag, replace the `version` attribute value with `3.0`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="utf-8"?>
  2  <!-- Generator: Adobe Illustrator 16.0.4, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
  3  <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
  4  <svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
  5  	 width="320px" height="320px" viewBox="0 0 320 320" enable-background="new 0 0 320 320" xml:space="preserve">
  6  <linearGradient id="SVGID_1_" gradientUnits="userSpaceOnUse" x1="160" y1="320" x2="160" y2="0">
  7  	<stop  offset="0" style="stop-color:#E6E6E6"/>
  8  	<stop  offset="0.75" style="stop-color:#FFFFFF"/>
  9  </linearGradient>
 10  <circle fill="url(#SVGID_1_)" cx="160" cy="160" r="160"/>
 11  <g>
 12  	<linearGradient id="SVGID_2_" gradientUnits="userSpaceOnUse" x1="160" y1="54.8711" x2="160" y2="272.935">
 13  		<stop  offset="0" style="stop-color:#54EEFF"/>
 14  		<stop  offset="1" style="stop-color:#1C75BC"/>
 15  	</linearGradient>
 16  	<path fill="url(#SVGID_2_)" d="M160.27,48.269l0.022-0.206l-0.102,0.126l-0.04-0.039l0.034-0.328l-0.184,0.181l-0.188-0.181
 17  		l0.035,0.328l-0.04,0.039l-0.102-0.126l0.022,0.206L41.296,164.039L88.2,230.485l36.231-8.319l35.569,50.012l35.568-50.012
 18  		l36.231,8.319l29.053-41.16l17.851-25.287L160.27,48.269z M156.403,61.86l-16.178,151.596l-31.613-43.118L156.403,61.86z
 19  		 M107.062,168.225l-19.895-27.136l69.065-84.474L107.062,168.225z M139.543,216.366l-14.142,3.245l-23.771-33.421l5.924-13.449
 20  		L139.543,216.366z M159.627,54.544l0.374-0.848l0.372,0.844l16.728,162.987l-0.051-0.034l-16.39,24.219l-17.733-24.254
 21  		l-0.021,0.016L159.627,54.544z M179.774,213.458L163.597,61.856l47.79,108.482L179.774,213.458z M212.445,172.741l5.926,13.449
 22  		L194.6,219.611l-14.143-3.245L212.445,172.741z M163.77,56.619l69.063,84.47l-19.894,27.136L163.77,56.619z M89.178,227.93
 23  		l-44.909-63.619l104.499-102.15l-64.473,78.853l21.711,29.61l-6.974,15.831l23.974,33.708L89.178,227.93z M160.001,268.26
 24  		l-33.176-46.645l14.181-3.256l0.238,0.327l-0.152,0.112l19.64,26.859l18.199-26.891l-0.155-0.105l0.221-0.302l14.179,3.256
 25  		L160.001,268.26z M258.999,188.017l-28.177,39.913l-33.826-7.767l23.972-33.708l-6.972-15.831l21.711-29.61l-64.473-78.852
 26  		L275.73,164.311L258.999,188.017z"/>
 27  </g>
 28  </svg>

```
### #6 - javaee-to-jakarta-namespaces-00052
* Category: mandatory
* Effort: 1
* Description: Replace the Java EE version with the Jakarta equivalent
`web-jsptaglibrary_2_1`: In the root tag, replace the `version` attribute value with `3.0`
* Labels: konveyor.io/target=jakarta-ee9+, konveyor.io/target=jakarta-ee, konveyor.io/target=eap8, konveyor.io/target=eap, konveyor.io/source
* Incidents
  * file:///opt/input/source/target/classes/META-INF/persistence.xml
      * `web-jsptaglibrary_2_1`: In the root tag, replace the `version` attribute value with `3.0`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <persistence version="2.1"
  3               xmlns="http://xmlns.jcp.org/xml/ns/persistence" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  4               xsi:schemaLocation="
  5          http://xmlns.jcp.org/xml/ns/persistence
  6          http://xmlns.jcp.org/xml/ns/persistence/persistence_2_1.xsd">
  7      <persistence-unit name="primary">
  8          <jta-data-source>java:jboss/datasources/CoolstoreDS</jta-data-source>
  9          <properties>
 10              <property name="javax.persistence.schema-generation.database.action" value="none"/>
 11              <property name="hibernate.show_sql" value="false" />
 12          </properties>
 13      </persistence-unit>
 14  </persistence>

```
  * file:///opt/input/source/src/main/resources/META-INF/persistence.xml
      * `web-jsptaglibrary_2_1`: In the root tag, replace the `version` attribute value with `3.0`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <persistence version="2.1"
  3               xmlns="http://xmlns.jcp.org/xml/ns/persistence" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  4               xsi:schemaLocation="
  5          http://xmlns.jcp.org/xml/ns/persistence
  6          http://xmlns.jcp.org/xml/ns/persistence/persistence_2_1.xsd">
  7      <persistence-unit name="primary">
  8          <jta-data-source>java:jboss/datasources/CoolstoreDS</jta-data-source>
  9          <properties>
 10              <property name="javax.persistence.schema-generation.database.action" value="none"/>
 11              <property name="hibernate.show_sql" value="false" />
 12          </properties>
 13      </persistence-unit>
 14  </persistence>

```
### #7 - javaee-to-jakarta-namespaces-00055
* Category: mandatory
* Effort: 1
* Description: Replace the Java EE version with the Jakarta equivalent
`orm_2_1`: In the root tag, replace the `version` attribute value with `3.0`
* Labels: konveyor.io/target=jakarta-ee9+, konveyor.io/target=jakarta-ee, konveyor.io/target=eap8, konveyor.io/target=eap, konveyor.io/source
* Incidents
  * file:///opt/input/source/target/classes/META-INF/persistence.xml
      * `orm_2_1`: In the root tag, replace the `version` attribute value with `3.0`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <persistence version="2.1"
  3               xmlns="http://xmlns.jcp.org/xml/ns/persistence" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  4               xsi:schemaLocation="
  5          http://xmlns.jcp.org/xml/ns/persistence
  6          http://xmlns.jcp.org/xml/ns/persistence/persistence_2_1.xsd">
  7      <persistence-unit name="primary">
  8          <jta-data-source>java:jboss/datasources/CoolstoreDS</jta-data-source>
  9          <properties>
 10              <property name="javax.persistence.schema-generation.database.action" value="none"/>
 11              <property name="hibernate.show_sql" value="false" />
 12          </properties>
 13      </persistence-unit>
 14  </persistence>

```
  * file:///opt/input/source/src/main/resources/META-INF/persistence.xml
      * `orm_2_1`: In the root tag, replace the `version` attribute value with `3.0`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <persistence version="2.1"
  3               xmlns="http://xmlns.jcp.org/xml/ns/persistence" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  4               xsi:schemaLocation="
  5          http://xmlns.jcp.org/xml/ns/persistence
  6          http://xmlns.jcp.org/xml/ns/persistence/persistence_2_1.xsd">
  7      <persistence-unit name="primary">
  8          <jta-data-source>java:jboss/datasources/CoolstoreDS</jta-data-source>
  9          <properties>
 10              <property name="javax.persistence.schema-generation.database.action" value="none"/>
 11              <property name="hibernate.show_sql" value="false" />
 12          </properties>
 13      </persistence-unit>
 14  </persistence>

```
### #8 - javax-to-jakarta-dependencies-00006
* Category: mandatory
* Effort: 1
* Description: javax groupId has been replaced by jakarta.platform
Update group dependency by replacing the `javax` groupId with `jakarta.platform`
* Labels: konveyor.io/target=jakarta-ee9+, konveyor.io/target=jakarta-ee, konveyor.io/target=eap8, konveyor.io/target=eap, konveyor.io/source
* Links
  * Jakarta EE: https://jakarta.ee/
* Incidents
  * file:///opt/input/source/pom.xml
      * Update group dependency by replacing the `javax` groupId with `jakarta.platform`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <project 
  3      xmlns="http://maven.apache.org/POM/4.0.0" 
  4      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  5      <modelVersion>4.0.0</modelVersion>
  6      <groupId>com.redhat.coolstore</groupId>
  7      <artifactId>monolith</artifactId>
  8      <version>1.0.0-SNAPSHOT</version>
  9      <packaging>war</packaging>
 10      <name>coolstore-monolith</name>
 11      <properties>
 12          <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
 13          <maven.build.timestamp.format>yyyyMMdd'T'HHmmss</maven.build.timestamp.format>
 14          <project.encoding>UTF-8</project.encoding>
 15          <maven.test.skip>true</maven.test.skip>
 16      </properties>
 17      <dependencies>
 18          <dependency>
 19              <groupId>javax</groupId>
 20              <artifactId>javaee-web-api</artifactId>
 21              <version>7.0</version>
 22              <scope>provided</scope>
 23          </dependency>
 24          <dependency>
 25              <groupId>javax</groupId>
 26              <artifactId>javaee-api</artifactId>
 27              <version>7.0</version>
 28              <scope>provided</scope>
 29          </dependency>
 30          <dependency>
 31              <groupId>org.flywaydb</groupId>
 32              <artifactId>flyway-core</artifactId>
 33              <version>4.1.2</version>
 34          </dependency>
 35          <dependency>
 36              <groupId>org.jboss.spec.javax.rmi</groupId>
 37              <artifactId>jboss-rmi-api_1.0_spec</artifactId>
 38              <version>1.0.2.Final</version>
 39          </dependency>
 40      </dependencies>
 41      <build>
 42          <finalName>ROOT</finalName>
 43          <plugins>
 44              <plugin>
 45                  <artifactId>maven-compiler-plugin</artifactId>
 46                  <version>3.0</version>
 47                  <configuration>
 48                      <encoding>${project.encoding}</encoding>
 49                      <source>1.8</source>
 50                      <target>1.8</target>
 51                  </configuration>
 52              </plugin>
 53              <plugin>
 54                  <groupId>org.apache.maven.plugins</groupId>
 55                  <artifactId>maven-war-plugin</artifactId>
 56                  <version>3.2.0</version>
 57              </plugin>
 58          </plugins>
 59      </build>
 60      <profiles>
 61  <!-- TODO: Add OpenShift profile here -->
 62      </profiles>
 63  </project>

```
  * file:///opt/input/source/pom.xml
      * Update group dependency by replacing the `javax` groupId with `jakarta.platform`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <project 
  3      xmlns="http://maven.apache.org/POM/4.0.0" 
  4      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  5      <modelVersion>4.0.0</modelVersion>
  6      <groupId>com.redhat.coolstore</groupId>
  7      <artifactId>monolith</artifactId>
  8      <version>1.0.0-SNAPSHOT</version>
  9      <packaging>war</packaging>
 10      <name>coolstore-monolith</name>
 11      <properties>
 12          <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
 13          <maven.build.timestamp.format>yyyyMMdd'T'HHmmss</maven.build.timestamp.format>
 14          <project.encoding>UTF-8</project.encoding>
 15          <maven.test.skip>true</maven.test.skip>
 16      </properties>
 17      <dependencies>
 18          <dependency>
 19              <groupId>javax</groupId>
 20              <artifactId>javaee-web-api</artifactId>
 21              <version>7.0</version>
 22              <scope>provided</scope>
 23          </dependency>
 24          <dependency>
 25              <groupId>javax</groupId>
 26              <artifactId>javaee-api</artifactId>
 27              <version>7.0</version>
 28              <scope>provided</scope>
 29          </dependency>
 30          <dependency>
 31              <groupId>org.flywaydb</groupId>
 32              <artifactId>flyway-core</artifactId>
 33              <version>4.1.2</version>
 34          </dependency>
 35          <dependency>
 36              <groupId>org.jboss.spec.javax.rmi</groupId>
 37              <artifactId>jboss-rmi-api_1.0_spec</artifactId>
 38              <version>1.0.2.Final</version>
 39          </dependency>
 40      </dependencies>
 41      <build>
 42          <finalName>ROOT</finalName>
 43          <plugins>
 44              <plugin>
 45                  <artifactId>maven-compiler-plugin</artifactId>
 46                  <version>3.0</version>
 47                  <configuration>
 48                      <encoding>${project.encoding}</encoding>
 49                      <source>1.8</source>
 50                      <target>1.8</target>
 51                  </configuration>
 52              </plugin>
 53              <plugin>
 54                  <groupId>org.apache.maven.plugins</groupId>
 55                  <artifactId>maven-war-plugin</artifactId>
 56                  <version>3.2.0</version>
 57              </plugin>
 58          </plugins>
 59      </build>
 60      <profiles>
 61  <!-- TODO: Add OpenShift profile here -->
 62      </profiles>
 63  </project>

```
### #9 - javax-to-jakarta-dependencies-00007
* Category: mandatory
* Effort: 1
* Description: javax javaee-api artifactId has been replaced by jakarta.platform jakarta.jakartaee-api
Update artifact dependency by replacing the `javaee-api` artifactId with `jakarta.jakartaee-api`
* Labels: konveyor.io/target=jakarta-ee9+, konveyor.io/target=jakarta-ee, konveyor.io/target=eap8, konveyor.io/target=eap, konveyor.io/source
* Links
  * Jakarta EE: https://jakarta.ee/
* Incidents
  * file:///opt/input/source/pom.xml
      * Update artifact dependency by replacing the `javaee-api` artifactId with `jakarta.jakartaee-api`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <project 
  3      xmlns="http://maven.apache.org/POM/4.0.0" 
  4      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  5      <modelVersion>4.0.0</modelVersion>
  6      <groupId>com.redhat.coolstore</groupId>
  7      <artifactId>monolith</artifactId>
  8      <version>1.0.0-SNAPSHOT</version>
  9      <packaging>war</packaging>
 10      <name>coolstore-monolith</name>
 11      <properties>
 12          <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
 13          <maven.build.timestamp.format>yyyyMMdd'T'HHmmss</maven.build.timestamp.format>
 14          <project.encoding>UTF-8</project.encoding>
 15          <maven.test.skip>true</maven.test.skip>
 16      </properties>
 17      <dependencies>
 18          <dependency>
 19              <groupId>javax</groupId>
 20              <artifactId>javaee-web-api</artifactId>
 21              <version>7.0</version>
 22              <scope>provided</scope>
 23          </dependency>
 24          <dependency>
 25              <groupId>javax</groupId>
 26              <artifactId>javaee-api</artifactId>
 27              <version>7.0</version>
 28              <scope>provided</scope>
 29          </dependency>
 30          <dependency>
 31              <groupId>org.flywaydb</groupId>
 32              <artifactId>flyway-core</artifactId>
 33              <version>4.1.2</version>
 34          </dependency>
 35          <dependency>
 36              <groupId>org.jboss.spec.javax.rmi</groupId>
 37              <artifactId>jboss-rmi-api_1.0_spec</artifactId>
 38              <version>1.0.2.Final</version>
 39          </dependency>
 40      </dependencies>
 41      <build>
 42          <finalName>ROOT</finalName>
 43          <plugins>
 44              <plugin>
 45                  <artifactId>maven-compiler-plugin</artifactId>
 46                  <version>3.0</version>
 47                  <configuration>
 48                      <encoding>${project.encoding}</encoding>
 49                      <source>1.8</source>
 50                      <target>1.8</target>
 51                  </configuration>
 52              </plugin>
 53              <plugin>
 54                  <groupId>org.apache.maven.plugins</groupId>
 55                  <artifactId>maven-war-plugin</artifactId>
 56                  <version>3.2.0</version>
 57              </plugin>
 58          </plugins>
 59      </build>
 60      <profiles>
 61  <!-- TODO: Add OpenShift profile here -->
 62      </profiles>
 63  </project>

```
### #10 - javax-to-jakarta-dependencies-00008
* Category: mandatory
* Effort: 1
* Description: javax javaee-web-api artifactId has been replaced by jakarta.platform jakarta.jakartaee-web-api
Update artifact dependency by replacing the `javaee-web-api` artifactId with `jakarta.jakartaee-web-api`
* Labels: konveyor.io/target=jakarta-ee9+, konveyor.io/target=jakarta-ee, konveyor.io/target=eap8, konveyor.io/target=eap, konveyor.io/source
* Links
  * Jakarta EE: https://jakarta.ee/
* Incidents
  * file:///opt/input/source/pom.xml
      * Update artifact dependency by replacing the `javaee-web-api` artifactId with `jakarta.jakartaee-web-api`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <project 
  3      xmlns="http://maven.apache.org/POM/4.0.0" 
  4      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  5      <modelVersion>4.0.0</modelVersion>
  6      <groupId>com.redhat.coolstore</groupId>
  7      <artifactId>monolith</artifactId>
  8      <version>1.0.0-SNAPSHOT</version>
  9      <packaging>war</packaging>
 10      <name>coolstore-monolith</name>
 11      <properties>
 12          <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
 13          <maven.build.timestamp.format>yyyyMMdd'T'HHmmss</maven.build.timestamp.format>
 14          <project.encoding>UTF-8</project.encoding>
 15          <maven.test.skip>true</maven.test.skip>
 16      </properties>
 17      <dependencies>
 18          <dependency>
 19              <groupId>javax</groupId>
 20              <artifactId>javaee-web-api</artifactId>
 21              <version>7.0</version>
 22              <scope>provided</scope>
 23          </dependency>
 24          <dependency>
 25              <groupId>javax</groupId>
 26              <artifactId>javaee-api</artifactId>
 27              <version>7.0</version>
 28              <scope>provided</scope>
 29          </dependency>
 30          <dependency>
 31              <groupId>org.flywaydb</groupId>
 32              <artifactId>flyway-core</artifactId>
 33              <version>4.1.2</version>
 34          </dependency>
 35          <dependency>
 36              <groupId>org.jboss.spec.javax.rmi</groupId>
 37              <artifactId>jboss-rmi-api_1.0_spec</artifactId>
 38              <version>1.0.2.Final</version>
 39          </dependency>
 40      </dependencies>
 41      <build>
 42          <finalName>ROOT</finalName>
 43          <plugins>
 44              <plugin>
 45                  <artifactId>maven-compiler-plugin</artifactId>
 46                  <version>3.0</version>
 47                  <configuration>
 48                      <encoding>${project.encoding}</encoding>
 49                      <source>1.8</source>
 50                      <target>1.8</target>
 51                  </configuration>
 52              </plugin>
 53              <plugin>
 54                  <groupId>org.apache.maven.plugins</groupId>
 55                  <artifactId>maven-war-plugin</artifactId>
 56                  <version>3.2.0</version>
 57              </plugin>
 58          </plugins>
 59      </build>
 60      <profiles>
 61  <!-- TODO: Add OpenShift profile here -->
 62      </profiles>
 63  </project>

```
### #11 - javax-to-jakarta-import-00001
* Category: mandatory
* Effort: 1
* Description: javax.{renamed} has been replaced by jakarta.{renamed}

* Labels: konveyor.io/target=jakarta-ee9+, konveyor.io/target=jakarta-ee, konveyor.io/target=eap8, konveyor.io/target=eap, konveyor.io/source
* Incidents
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/model/InventoryEntity.java
      * Replace the `javax.persistence` import statement with `jakarta.persistence`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.model;
  2  
  3  import java.io.Serializable;
  4  
  5  import javax.persistence.Column;
  6  import javax.persistence.Entity;
  7  import javax.persistence.Id;
  8  import javax.persistence.Table;
  9  import javax.persistence.UniqueConstraint;
 10  import javax.xml.bind.annotation.XmlRootElement;
 11  
 12  @Entity
 13  @XmlRootElement
 14  @Table(name = "INVENTORY", uniqueConstraints = @UniqueConstraint(columnNames = "itemId"))
 15  public class InventoryEntity implements Serializable {
 16  
 17  	private static final long serialVersionUID = 7526472295622776147L; 
 18  
 19      @Id
 20      private String itemId;
 21  
 22  
 23      @Column
 24      private String location;
 25  
 26  
 27      @Column
 28      private int quantity;
 29  
 30  
 31      @Column
 32      private String link;
 33  
 34      public InventoryEntity() {
 35  
 36      }
 37  
 38      public String getItemId() {
 39  		return itemId;
 40  	}
 41  
 42  	public void setItemId(String itemId) {
 43  		this.itemId = itemId;
 44  	}
 45  
 46  	public String getLocation() {
 47  		return location;
 48  	}
 49  
 50  	public void setLocation(String location) {
 51  		this.location = location;
 52  	}
 53  
 54  	public int getQuantity() {
 55  		return quantity;
 56  	}
 57  
 58  	public void setQuantity(int quantity) {
 59  		this.quantity = quantity;
 60  	}
 61  
 62  	public String getLink() {
 63  		return link;
 64  	}
 65  
 66  	public void setLink(String link) {
 67  		this.link = link;
 68  	}
 69  
 70  	@Override
 71      public String toString() {
 72          return "InventoryEntity [itemId=" + itemId + ", availability=" + quantity + "/" + location + " link=" + link + "]";
 73      }
 74  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/model/InventoryEntity.java
      * Replace the `javax.persistence` import statement with `jakarta.persistence`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.model;
  2  
  3  import java.io.Serializable;
  4  
  5  import javax.persistence.Column;
  6  import javax.persistence.Entity;
  7  import javax.persistence.Id;
  8  import javax.persistence.Table;
  9  import javax.persistence.UniqueConstraint;
 10  import javax.xml.bind.annotation.XmlRootElement;
 11  
 12  @Entity
 13  @XmlRootElement
 14  @Table(name = "INVENTORY", uniqueConstraints = @UniqueConstraint(columnNames = "itemId"))
 15  public class InventoryEntity implements Serializable {
 16  
 17  	private static final long serialVersionUID = 7526472295622776147L; 
 18  
 19      @Id
 20      private String itemId;
 21  
 22  
 23      @Column
 24      private String location;
 25  
 26  
 27      @Column
 28      private int quantity;
 29  
 30  
 31      @Column
 32      private String link;
 33  
 34      public InventoryEntity() {
 35  
 36      }
 37  
 38      public String getItemId() {
 39  		return itemId;
 40  	}
 41  
 42  	public void setItemId(String itemId) {
 43  		this.itemId = itemId;
 44  	}
 45  
 46  	public String getLocation() {
 47  		return location;
 48  	}
 49  
 50  	public void setLocation(String location) {
 51  		this.location = location;
 52  	}
 53  
 54  	public int getQuantity() {
 55  		return quantity;
 56  	}
 57  
 58  	public void setQuantity(int quantity) {
 59  		this.quantity = quantity;
 60  	}
 61  
 62  	public String getLink() {
 63  		return link;
 64  	}
 65  
 66  	public void setLink(String link) {
 67  		this.link = link;
 68  	}
 69  
 70  	@Override
 71      public String toString() {
 72          return "InventoryEntity [itemId=" + itemId + ", availability=" + quantity + "/" + location + " link=" + link + "]";
 73      }
 74  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/model/InventoryEntity.java
      * Replace the `javax.persistence` import statement with `jakarta.persistence`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.model;
  2  
  3  import java.io.Serializable;
  4  
  5  import javax.persistence.Column;
  6  import javax.persistence.Entity;
  7  import javax.persistence.Id;
  8  import javax.persistence.Table;
  9  import javax.persistence.UniqueConstraint;
 10  import javax.xml.bind.annotation.XmlRootElement;
 11  
 12  @Entity
 13  @XmlRootElement
 14  @Table(name = "INVENTORY", uniqueConstraints = @UniqueConstraint(columnNames = "itemId"))
 15  public class InventoryEntity implements Serializable {
 16  
 17  	private static final long serialVersionUID = 7526472295622776147L; 
 18  
 19      @Id
 20      private String itemId;
 21  
 22  
 23      @Column
 24      private String location;
 25  
 26  
 27      @Column
 28      private int quantity;
 29  
 30  
 31      @Column
 32      private String link;
 33  
 34      public InventoryEntity() {
 35  
 36      }
 37  
 38      public String getItemId() {
 39  		return itemId;
 40  	}
 41  
 42  	public void setItemId(String itemId) {
 43  		this.itemId = itemId;
 44  	}
 45  
 46  	public String getLocation() {
 47  		return location;
 48  	}
 49  
 50  	public void setLocation(String location) {
 51  		this.location = location;
 52  	}
 53  
 54  	public int getQuantity() {
 55  		return quantity;
 56  	}
 57  
 58  	public void setQuantity(int quantity) {
 59  		this.quantity = quantity;
 60  	}
 61  
 62  	public String getLink() {
 63  		return link;
 64  	}
 65  
 66  	public void setLink(String link) {
 67  		this.link = link;
 68  	}
 69  
 70  	@Override
 71      public String toString() {
 72          return "InventoryEntity [itemId=" + itemId + ", availability=" + quantity + "/" + location + " link=" + link + "]";
 73      }
 74  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/model/InventoryEntity.java
      * Replace the `javax.xml` import statement with `jakarta.xml`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.model;
  2  
  3  import java.io.Serializable;
  4  
  5  import javax.persistence.Column;
  6  import javax.persistence.Entity;
  7  import javax.persistence.Id;
  8  import javax.persistence.Table;
  9  import javax.persistence.UniqueConstraint;
 10  import javax.xml.bind.annotation.XmlRootElement;
 11  
 12  @Entity
 13  @XmlRootElement
 14  @Table(name = "INVENTORY", uniqueConstraints = @UniqueConstraint(columnNames = "itemId"))
 15  public class InventoryEntity implements Serializable {
 16  
 17  	private static final long serialVersionUID = 7526472295622776147L; 
 18  
 19      @Id
 20      private String itemId;
 21  
 22  
 23      @Column
 24      private String location;
 25  
 26  
 27      @Column
 28      private int quantity;
 29  
 30  
 31      @Column
 32      private String link;
 33  
 34      public InventoryEntity() {
 35  
 36      }
 37  
 38      public String getItemId() {
 39  		return itemId;
 40  	}
 41  
 42  	public void setItemId(String itemId) {
 43  		this.itemId = itemId;
 44  	}
 45  
 46  	public String getLocation() {
 47  		return location;
 48  	}
 49  
 50  	public void setLocation(String location) {
 51  		this.location = location;
 52  	}
 53  
 54  	public int getQuantity() {
 55  		return quantity;
 56  	}
 57  
 58  	public void setQuantity(int quantity) {
 59  		this.quantity = quantity;
 60  	}
 61  
 62  	public String getLink() {
 63  		return link;
 64  	}
 65  
 66  	public void setLink(String link) {
 67  		this.link = link;
 68  	}
 69  
 70  	@Override
 71      public String toString() {
 72          return "InventoryEntity [itemId=" + itemId + ", availability=" + quantity + "/" + location + " link=" + link + "]";
 73      }
 74  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/model/InventoryEntity.java
      * Replace the `javax.persistence` import statement with `jakarta.persistence`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.model;
  2  
  3  import java.io.Serializable;
  4  
  5  import javax.persistence.Column;
  6  import javax.persistence.Entity;
  7  import javax.persistence.Id;
  8  import javax.persistence.Table;
  9  import javax.persistence.UniqueConstraint;
 10  import javax.xml.bind.annotation.XmlRootElement;
 11  
 12  @Entity
 13  @XmlRootElement
 14  @Table(name = "INVENTORY", uniqueConstraints = @UniqueConstraint(columnNames = "itemId"))
 15  public class InventoryEntity implements Serializable {
 16  
 17  	private static final long serialVersionUID = 7526472295622776147L; 
 18  
 19      @Id
 20      private String itemId;
 21  
 22  
 23      @Column
 24      private String location;
 25  
 26  
 27      @Column
 28      private int quantity;
 29  
 30  
 31      @Column
 32      private String link;
 33  
 34      public InventoryEntity() {
 35  
 36      }
 37  
 38      public String getItemId() {
 39  		return itemId;
 40  	}
 41  
 42  	public void setItemId(String itemId) {
 43  		this.itemId = itemId;
 44  	}
 45  
 46  	public String getLocation() {
 47  		return location;
 48  	}
 49  
 50  	public void setLocation(String location) {
 51  		this.location = location;
 52  	}
 53  
 54  	public int getQuantity() {
 55  		return quantity;
 56  	}
 57  
 58  	public void setQuantity(int quantity) {
 59  		this.quantity = quantity;
 60  	}
 61  
 62  	public String getLink() {
 63  		return link;
 64  	}
 65  
 66  	public void setLink(String link) {
 67  		this.link = link;
 68  	}
 69  
 70  	@Override
 71      public String toString() {
 72          return "InventoryEntity [itemId=" + itemId + ", availability=" + quantity + "/" + location + " link=" + link + "]";
 73      }
 74  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/model/InventoryEntity.java
      * Replace the `javax.persistence` import statement with `jakarta.persistence`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.model;
  2  
  3  import java.io.Serializable;
  4  
  5  import javax.persistence.Column;
  6  import javax.persistence.Entity;
  7  import javax.persistence.Id;
  8  import javax.persistence.Table;
  9  import javax.persistence.UniqueConstraint;
 10  import javax.xml.bind.annotation.XmlRootElement;
 11  
 12  @Entity
 13  @XmlRootElement
 14  @Table(name = "INVENTORY", uniqueConstraints = @UniqueConstraint(columnNames = "itemId"))
 15  public class InventoryEntity implements Serializable {
 16  
 17  	private static final long serialVersionUID = 7526472295622776147L; 
 18  
 19      @Id
 20      private String itemId;
 21  
 22  
 23      @Column
 24      private String location;
 25  
 26  
 27      @Column
 28      private int quantity;
 29  
 30  
 31      @Column
 32      private String link;
 33  
 34      public InventoryEntity() {
 35  
 36      }
 37  
 38      public String getItemId() {
 39  		return itemId;
 40  	}
 41  
 42  	public void setItemId(String itemId) {
 43  		this.itemId = itemId;
 44  	}
 45  
 46  	public String getLocation() {
 47  		return location;
 48  	}
 49  
 50  	public void setLocation(String location) {
 51  		this.location = location;
 52  	}
 53  
 54  	public int getQuantity() {
 55  		return quantity;
 56  	}
 57  
 58  	public void setQuantity(int quantity) {
 59  		this.quantity = quantity;
 60  	}
 61  
 62  	public String getLink() {
 63  		return link;
 64  	}
 65  
 66  	public void setLink(String link) {
 67  		this.link = link;
 68  	}
 69  
 70  	@Override
 71      public String toString() {
 72          return "InventoryEntity [itemId=" + itemId + ", availability=" + quantity + "/" + location + " link=" + link + "]";
 73      }
 74  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/model/Order.java
      * Replace the `javax.persistence` import statement with `jakarta.persistence`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.model;
  2  
  3  import java.io.Serializable;
  4  import java.util.ArrayList;
  5  import java.util.List;
  6  
  7  import javax.persistence.CascadeType;
  8  import javax.persistence.Column;
  9  import javax.persistence.Entity;
 10  import javax.persistence.FetchType;
 11  import javax.persistence.GeneratedValue;
 12  import javax.persistence.Id;
 13  import javax.persistence.JoinColumn;
 14  import javax.persistence.OneToMany;
 15  import javax.persistence.Table;
 16  
 17  @Entity
 18  @Table(name = "ORDERS")
 19  public class Order implements Serializable {
 20  
 21  	private static final long serialVersionUID = -1L;
 22  
 23  	@Id
 24  	@GeneratedValue
 25  	private long orderId;
 26  
 27  	private String customerName;
 28  
 29  	private String customerEmail;
 30  
 31  	private double orderValue;
 32  
 33  	private double retailPrice;
 34  
 35  	private double discount;
 36  
 37  	private double shippingFee;
 38  
 39  	private double shippingDiscount;
 40  
 41  	@Column(name="TOTAL_PRICE")
 42  
 43  	
 44  	@OneToMany(fetch = FetchType.EAGER, cascade = CascadeType.ALL, orphanRemoval = true)
 45  	@JoinColumn(name="ORDER_ID")
 46  	private List<OrderItem> itemList = new ArrayList<>();
 47  
 48  	public Order() {}
 49  
 50  	public long getOrderId() {
 51  		return orderId;
 52  	}
 53  
 54  	public void setOrderId(long orderId) {
 55  		this.orderId = orderId;
 56  	}
 57  
 58  	public String getCustomerName() {
 59  		return customerName;
 60  	}
 61  
 62  	public void setCustomerName(String customerName) {
 63  		this.customerName = customerName;
 64  	}
 65  
 66  	public String getCustomerEmail() {
 67  		return customerEmail;
 68  	}
 69  
 70  	public void setCustomerEmail(String customerEmail) {
 71  		this.customerEmail = customerEmail;
 72  	}
 73  
 74  	public double getOrderValue() {
 75  		return orderValue;
 76  	}
 77  
 78  	public void setOrderValue(double orderValue) {
 79  		this.orderValue = orderValue;
 80  	}
 81  
 82  	public double getRetailPrice() {
 83  		return retailPrice;
 84  	}
 85  
 86  	public void setRetailPrice(double retailPrice) {
 87  		this.retailPrice = retailPrice;
 88  	}
 89  
 90  	public double getDiscount() {
 91  		return discount;
 92  	}
 93  
 94  	public void setDiscount(double discount) {
 95  		this.discount = discount;
 96  	}
 97  
 98  	public double getShippingFee() {
 99  		return shippingFee;
100  	}
101  
102  	public void setShippingFee(double shippingFee) {
103  		this.shippingFee = shippingFee;
104  	}
105  
106  	public double getShippingDiscount() {
107  		return shippingDiscount;
108  	}
109  
110  	public void setShippingDiscount(double shippingDiscount) {
```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/model/Order.java
      * Replace the `javax.persistence` import statement with `jakarta.persistence`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.model;
  2  
  3  import java.io.Serializable;
  4  import java.util.ArrayList;
  5  import java.util.List;
  6  
  7  import javax.persistence.CascadeType;
  8  import javax.persistence.Column;
  9  import javax.persistence.Entity;
 10  import javax.persistence.FetchType;
 11  import javax.persistence.GeneratedValue;
 12  import javax.persistence.Id;
 13  import javax.persistence.JoinColumn;
 14  import javax.persistence.OneToMany;
 15  import javax.persistence.Table;
 16  
 17  @Entity
 18  @Table(name = "ORDERS")
 19  public class Order implements Serializable {
 20  
 21  	private static final long serialVersionUID = -1L;
 22  
 23  	@Id
 24  	@GeneratedValue
 25  	private long orderId;
 26  
 27  	private String customerName;
 28  
 29  	private String customerEmail;
 30  
 31  	private double orderValue;
 32  
 33  	private double retailPrice;
 34  
 35  	private double discount;
 36  
 37  	private double shippingFee;
 38  
 39  	private double shippingDiscount;
 40  
 41  	@Column(name="TOTAL_PRICE")
 42  
 43  	
 44  	@OneToMany(fetch = FetchType.EAGER, cascade = CascadeType.ALL, orphanRemoval = true)
 45  	@JoinColumn(name="ORDER_ID")
 46  	private List<OrderItem> itemList = new ArrayList<>();
 47  
 48  	public Order() {}
 49  
 50  	public long getOrderId() {
 51  		return orderId;
 52  	}
 53  
 54  	public void setOrderId(long orderId) {
 55  		this.orderId = orderId;
 56  	}
 57  
 58  	public String getCustomerName() {
 59  		return customerName;
 60  	}
 61  
 62  	public void setCustomerName(String customerName) {
 63  		this.customerName = customerName;
 64  	}
 65  
 66  	public String getCustomerEmail() {
 67  		return customerEmail;
 68  	}
 69  
 70  	public void setCustomerEmail(String customerEmail) {
 71  		this.customerEmail = customerEmail;
 72  	}
 73  
 74  	public double getOrderValue() {
 75  		return orderValue;
 76  	}
 77  
 78  	public void setOrderValue(double orderValue) {
 79  		this.orderValue = orderValue;
 80  	}
 81  
 82  	public double getRetailPrice() {
 83  		return retailPrice;
 84  	}
 85  
 86  	public void setRetailPrice(double retailPrice) {
 87  		this.retailPrice = retailPrice;
 88  	}
 89  
 90  	public double getDiscount() {
 91  		return discount;
 92  	}
 93  
 94  	public void setDiscount(double discount) {
 95  		this.discount = discount;
 96  	}
 97  
 98  	public double getShippingFee() {
 99  		return shippingFee;
100  	}
101  
102  	public void setShippingFee(double shippingFee) {
103  		this.shippingFee = shippingFee;
104  	}
105  
106  	public double getShippingDiscount() {
107  		return shippingDiscount;
108  	}
109  
110  	public void setShippingDiscount(double shippingDiscount) {
111  		this.shippingDiscount = shippingDiscount;
112  	}
113  
114  	public void setItemList(List<OrderItem> itemList) {
115  		this.itemList = itemList;
```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/model/Order.java
      * Replace the `javax.persistence` import statement with `jakarta.persistence`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.model;
  2  
  3  import java.io.Serializable;
  4  import java.util.ArrayList;
  5  import java.util.List;
  6  
  7  import javax.persistence.CascadeType;
  8  import javax.persistence.Column;
  9  import javax.persistence.Entity;
 10  import javax.persistence.FetchType;
 11  import javax.persistence.GeneratedValue;
 12  import javax.persistence.Id;
 13  import javax.persistence.JoinColumn;
 14  import javax.persistence.OneToMany;
 15  import javax.persistence.Table;
 16  
 17  @Entity
 18  @Table(name = "ORDERS")
 19  public class Order implements Serializable {
 20  
 21  	private static final long serialVersionUID = -1L;
 22  
 23  	@Id
 24  	@GeneratedValue
 25  	private long orderId;
 26  
 27  	private String customerName;
 28  
 29  	private String customerEmail;
 30  
 31  	private double orderValue;
 32  
 33  	private double retailPrice;
 34  
 35  	private double discount;
 36  
 37  	private double shippingFee;
 38  
 39  	private double shippingDiscount;
 40  
 41  	@Column(name="TOTAL_PRICE")
 42  
 43  	
 44  	@OneToMany(fetch = FetchType.EAGER, cascade = CascadeType.ALL, orphanRemoval = true)
 45  	@JoinColumn(name="ORDER_ID")
 46  	private List<OrderItem> itemList = new ArrayList<>();
 47  
 48  	public Order() {}
 49  
 50  	public long getOrderId() {
 51  		return orderId;
 52  	}
 53  
 54  	public void setOrderId(long orderId) {
 55  		this.orderId = orderId;
 56  	}
 57  
 58  	public String getCustomerName() {
 59  		return customerName;
 60  	}
 61  
 62  	public void setCustomerName(String customerName) {
 63  		this.customerName = customerName;
 64  	}
 65  
 66  	public String getCustomerEmail() {
 67  		return customerEmail;
 68  	}
 69  
 70  	public void setCustomerEmail(String customerEmail) {
 71  		this.customerEmail = customerEmail;
 72  	}
 73  
 74  	public double getOrderValue() {
 75  		return orderValue;
 76  	}
 77  
 78  	public void setOrderValue(double orderValue) {
 79  		this.orderValue = orderValue;
 80  	}
 81  
 82  	public double getRetailPrice() {
 83  		return retailPrice;
 84  	}
 85  
 86  	public void setRetailPrice(double retailPrice) {
 87  		this.retailPrice = retailPrice;
 88  	}
 89  
 90  	public double getDiscount() {
 91  		return discount;
 92  	}
 93  
 94  	public void setDiscount(double discount) {
 95  		this.discount = discount;
 96  	}
 97  
 98  	public double getShippingFee() {
 99  		return shippingFee;
100  	}
101  
102  	public void setShippingFee(double shippingFee) {
103  		this.shippingFee = shippingFee;
104  	}
105  
106  	public double getShippingDiscount() {
107  		return shippingDiscount;
108  	}
109  
110  	public void setShippingDiscount(double shippingDiscount) {
111  		this.shippingDiscount = shippingDiscount;
```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/model/Order.java
      * Replace the `javax.persistence` import statement with `jakarta.persistence`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.model;
  2  
  3  import java.io.Serializable;
  4  import java.util.ArrayList;
  5  import java.util.List;
  6  
  7  import javax.persistence.CascadeType;
  8  import javax.persistence.Column;
  9  import javax.persistence.Entity;
 10  import javax.persistence.FetchType;
 11  import javax.persistence.GeneratedValue;
 12  import javax.persistence.Id;
 13  import javax.persistence.JoinColumn;
 14  import javax.persistence.OneToMany;
 15  import javax.persistence.Table;
 16  
 17  @Entity
 18  @Table(name = "ORDERS")
 19  public class Order implements Serializable {
 20  
 21  	private static final long serialVersionUID = -1L;
 22  
 23  	@Id
 24  	@GeneratedValue
 25  	private long orderId;
 26  
 27  	private String customerName;
 28  
 29  	private String customerEmail;
 30  
 31  	private double orderValue;
 32  
 33  	private double retailPrice;
 34  
 35  	private double discount;
 36  
 37  	private double shippingFee;
 38  
 39  	private double shippingDiscount;
 40  
 41  	@Column(name="TOTAL_PRICE")
 42  
 43  	
 44  	@OneToMany(fetch = FetchType.EAGER, cascade = CascadeType.ALL, orphanRemoval = true)
 45  	@JoinColumn(name="ORDER_ID")
 46  	private List<OrderItem> itemList = new ArrayList<>();
 47  
 48  	public Order() {}
 49  
 50  	public long getOrderId() {
 51  		return orderId;
 52  	}
 53  
 54  	public void setOrderId(long orderId) {
 55  		this.orderId = orderId;
 56  	}
 57  
 58  	public String getCustomerName() {
 59  		return customerName;
 60  	}
 61  
 62  	public void setCustomerName(String customerName) {
 63  		this.customerName = customerName;
 64  	}
 65  
 66  	public String getCustomerEmail() {
 67  		return customerEmail;
 68  	}
 69  
 70  	public void setCustomerEmail(String customerEmail) {
 71  		this.customerEmail = customerEmail;
 72  	}
 73  
 74  	public double getOrderValue() {
 75  		return orderValue;
 76  	}
 77  
 78  	public void setOrderValue(double orderValue) {
 79  		this.orderValue = orderValue;
 80  	}
 81  
 82  	public double getRetailPrice() {
 83  		return retailPrice;
 84  	}
 85  
 86  	public void setRetailPrice(double retailPrice) {
 87  		this.retailPrice = retailPrice;
 88  	}
 89  
 90  	public double getDiscount() {
 91  		return discount;
 92  	}
 93  
 94  	public void setDiscount(double discount) {
 95  		this.discount = discount;
 96  	}
 97  
 98  	public double getShippingFee() {
 99  		return shippingFee;
100  	}
101  
102  	public void setShippingFee(double shippingFee) {
103  		this.shippingFee = shippingFee;
104  	}
105  
106  	public double getShippingDiscount() {
107  		return shippingDiscount;
108  	}
109  
110  	public void setShippingDiscount(double shippingDiscount) {
111  		this.shippingDiscount = shippingDiscount;
112  	}
113  
114  	public void setItemList(List<OrderItem> itemList) {
```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/model/Order.java
      * Replace the `javax.persistence` import statement with `jakarta.persistence`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.model;
  2  
  3  import java.io.Serializable;
  4  import java.util.ArrayList;
  5  import java.util.List;
  6  
  7  import javax.persistence.CascadeType;
  8  import javax.persistence.Column;
  9  import javax.persistence.Entity;
 10  import javax.persistence.FetchType;
 11  import javax.persistence.GeneratedValue;
 12  import javax.persistence.Id;
 13  import javax.persistence.JoinColumn;
 14  import javax.persistence.OneToMany;
 15  import javax.persistence.Table;
 16  
 17  @Entity
 18  @Table(name = "ORDERS")
 19  public class Order implements Serializable {
 20  
 21  	private static final long serialVersionUID = -1L;
 22  
 23  	@Id
 24  	@GeneratedValue
 25  	private long orderId;
 26  
 27  	private String customerName;
 28  
 29  	private String customerEmail;
 30  
 31  	private double orderValue;
 32  
 33  	private double retailPrice;
 34  
 35  	private double discount;
 36  
 37  	private double shippingFee;
 38  
 39  	private double shippingDiscount;
 40  
 41  	@Column(name="TOTAL_PRICE")
 42  
 43  	
 44  	@OneToMany(fetch = FetchType.EAGER, cascade = CascadeType.ALL, orphanRemoval = true)
 45  	@JoinColumn(name="ORDER_ID")
 46  	private List<OrderItem> itemList = new ArrayList<>();
 47  
 48  	public Order() {}
 49  
 50  	public long getOrderId() {
 51  		return orderId;
 52  	}
 53  
 54  	public void setOrderId(long orderId) {
 55  		this.orderId = orderId;
 56  	}
 57  
 58  	public String getCustomerName() {
 59  		return customerName;
 60  	}
 61  
 62  	public void setCustomerName(String customerName) {
 63  		this.customerName = customerName;
 64  	}
 65  
 66  	public String getCustomerEmail() {
 67  		return customerEmail;
 68  	}
 69  
 70  	public void setCustomerEmail(String customerEmail) {
 71  		this.customerEmail = customerEmail;
 72  	}
 73  
 74  	public double getOrderValue() {
 75  		return orderValue;
 76  	}
 77  
 78  	public void setOrderValue(double orderValue) {
 79  		this.orderValue = orderValue;
 80  	}
 81  
 82  	public double getRetailPrice() {
 83  		return retailPrice;
 84  	}
 85  
 86  	public void setRetailPrice(double retailPrice) {
 87  		this.retailPrice = retailPrice;
 88  	}
 89  
 90  	public double getDiscount() {
 91  		return discount;
 92  	}
 93  
 94  	public void setDiscount(double discount) {
 95  		this.discount = discount;
 96  	}
 97  
 98  	public double getShippingFee() {
 99  		return shippingFee;
100  	}
101  
102  	public void setShippingFee(double shippingFee) {
103  		this.shippingFee = shippingFee;
104  	}
105  
106  	public double getShippingDiscount() {
107  		return shippingDiscount;
108  	}
109  
```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/model/Order.java
      * Replace the `javax.persistence` import statement with `jakarta.persistence`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.model;
  2  
  3  import java.io.Serializable;
  4  import java.util.ArrayList;
  5  import java.util.List;
  6  
  7  import javax.persistence.CascadeType;
  8  import javax.persistence.Column;
  9  import javax.persistence.Entity;
 10  import javax.persistence.FetchType;
 11  import javax.persistence.GeneratedValue;
 12  import javax.persistence.Id;
 13  import javax.persistence.JoinColumn;
 14  import javax.persistence.OneToMany;
 15  import javax.persistence.Table;
 16  
 17  @Entity
 18  @Table(name = "ORDERS")
 19  public class Order implements Serializable {
 20  
 21  	private static final long serialVersionUID = -1L;
 22  
 23  	@Id
 24  	@GeneratedValue
 25  	private long orderId;
 26  
 27  	private String customerName;
 28  
 29  	private String customerEmail;
 30  
 31  	private double orderValue;
 32  
 33  	private double retailPrice;
 34  
 35  	private double discount;
 36  
 37  	private double shippingFee;
 38  
 39  	private double shippingDiscount;
 40  
 41  	@Column(name="TOTAL_PRICE")
 42  
 43  	
 44  	@OneToMany(fetch = FetchType.EAGER, cascade = CascadeType.ALL, orphanRemoval = true)
 45  	@JoinColumn(name="ORDER_ID")
 46  	private List<OrderItem> itemList = new ArrayList<>();
 47  
 48  	public Order() {}
 49  
 50  	public long getOrderId() {
 51  		return orderId;
 52  	}
 53  
 54  	public void setOrderId(long orderId) {
 55  		this.orderId = orderId;
 56  	}
 57  
 58  	public String getCustomerName() {
 59  		return customerName;
 60  	}
 61  
 62  	public void setCustomerName(String customerName) {
 63  		this.customerName = customerName;
 64  	}
 65  
 66  	public String getCustomerEmail() {
 67  		return customerEmail;
 68  	}
 69  
 70  	public void setCustomerEmail(String customerEmail) {
 71  		this.customerEmail = customerEmail;
 72  	}
 73  
 74  	public double getOrderValue() {
 75  		return orderValue;
 76  	}
 77  
 78  	public void setOrderValue(double orderValue) {
 79  		this.orderValue = orderValue;
 80  	}
 81  
 82  	public double getRetailPrice() {
 83  		return retailPrice;
 84  	}
 85  
 86  	public void setRetailPrice(double retailPrice) {
 87  		this.retailPrice = retailPrice;
 88  	}
 89  
 90  	public double getDiscount() {
 91  		return discount;
 92  	}
 93  
 94  	public void setDiscount(double discount) {
 95  		this.discount = discount;
 96  	}
 97  
 98  	public double getShippingFee() {
 99  		return shippingFee;
100  	}
101  
102  	public void setShippingFee(double shippingFee) {
103  		this.shippingFee = shippingFee;
104  	}
105  
106  	public double getShippingDiscount() {
107  		return shippingDiscount;
108  	}
109  
110  	public void setShippingDiscount(double shippingDiscount) {
111  		this.shippingDiscount = shippingDiscount;
112  	}
```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/model/Order.java
      * Replace the `javax.persistence` import statement with `jakarta.persistence`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.model;
  2  
  3  import java.io.Serializable;
  4  import java.util.ArrayList;
  5  import java.util.List;
  6  
  7  import javax.persistence.CascadeType;
  8  import javax.persistence.Column;
  9  import javax.persistence.Entity;
 10  import javax.persistence.FetchType;
 11  import javax.persistence.GeneratedValue;
 12  import javax.persistence.Id;
 13  import javax.persistence.JoinColumn;
 14  import javax.persistence.OneToMany;
 15  import javax.persistence.Table;
 16  
 17  @Entity
 18  @Table(name = "ORDERS")
 19  public class Order implements Serializable {
 20  
 21  	private static final long serialVersionUID = -1L;
 22  
 23  	@Id
 24  	@GeneratedValue
 25  	private long orderId;
 26  
 27  	private String customerName;
 28  
 29  	private String customerEmail;
 30  
 31  	private double orderValue;
 32  
 33  	private double retailPrice;
 34  
 35  	private double discount;
 36  
 37  	private double shippingFee;
 38  
 39  	private double shippingDiscount;
 40  
 41  	@Column(name="TOTAL_PRICE")
 42  
 43  	
 44  	@OneToMany(fetch = FetchType.EAGER, cascade = CascadeType.ALL, orphanRemoval = true)
 45  	@JoinColumn(name="ORDER_ID")
 46  	private List<OrderItem> itemList = new ArrayList<>();
 47  
 48  	public Order() {}
 49  
 50  	public long getOrderId() {
 51  		return orderId;
 52  	}
 53  
 54  	public void setOrderId(long orderId) {
 55  		this.orderId = orderId;
 56  	}
 57  
 58  	public String getCustomerName() {
 59  		return customerName;
 60  	}
 61  
 62  	public void setCustomerName(String customerName) {
 63  		this.customerName = customerName;
 64  	}
 65  
 66  	public String getCustomerEmail() {
 67  		return customerEmail;
 68  	}
 69  
 70  	public void setCustomerEmail(String customerEmail) {
 71  		this.customerEmail = customerEmail;
 72  	}
 73  
 74  	public double getOrderValue() {
 75  		return orderValue;
 76  	}
 77  
 78  	public void setOrderValue(double orderValue) {
 79  		this.orderValue = orderValue;
 80  	}
 81  
 82  	public double getRetailPrice() {
 83  		return retailPrice;
 84  	}
 85  
 86  	public void setRetailPrice(double retailPrice) {
 87  		this.retailPrice = retailPrice;
 88  	}
 89  
 90  	public double getDiscount() {
 91  		return discount;
 92  	}
 93  
 94  	public void setDiscount(double discount) {
 95  		this.discount = discount;
 96  	}
 97  
 98  	public double getShippingFee() {
 99  		return shippingFee;
100  	}
101  
102  	public void setShippingFee(double shippingFee) {
103  		this.shippingFee = shippingFee;
104  	}
105  
106  	public double getShippingDiscount() {
107  		return shippingDiscount;
108  	}
```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/model/Order.java
      * Replace the `javax.persistence` import statement with `jakarta.persistence`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.model;
  2  
  3  import java.io.Serializable;
  4  import java.util.ArrayList;
  5  import java.util.List;
  6  
  7  import javax.persistence.CascadeType;
  8  import javax.persistence.Column;
  9  import javax.persistence.Entity;
 10  import javax.persistence.FetchType;
 11  import javax.persistence.GeneratedValue;
 12  import javax.persistence.Id;
 13  import javax.persistence.JoinColumn;
 14  import javax.persistence.OneToMany;
 15  import javax.persistence.Table;
 16  
 17  @Entity
 18  @Table(name = "ORDERS")
 19  public class Order implements Serializable {
 20  
 21  	private static final long serialVersionUID = -1L;
 22  
 23  	@Id
 24  	@GeneratedValue
 25  	private long orderId;
 26  
 27  	private String customerName;
 28  
 29  	private String customerEmail;
 30  
 31  	private double orderValue;
 32  
 33  	private double retailPrice;
 34  
 35  	private double discount;
 36  
 37  	private double shippingFee;
 38  
 39  	private double shippingDiscount;
 40  
 41  	@Column(name="TOTAL_PRICE")
 42  
 43  	
 44  	@OneToMany(fetch = FetchType.EAGER, cascade = CascadeType.ALL, orphanRemoval = true)
 45  	@JoinColumn(name="ORDER_ID")
 46  	private List<OrderItem> itemList = new ArrayList<>();
 47  
 48  	public Order() {}
 49  
 50  	public long getOrderId() {
 51  		return orderId;
 52  	}
 53  
 54  	public void setOrderId(long orderId) {
 55  		this.orderId = orderId;
 56  	}
 57  
 58  	public String getCustomerName() {
 59  		return customerName;
 60  	}
 61  
 62  	public void setCustomerName(String customerName) {
 63  		this.customerName = customerName;
 64  	}
 65  
 66  	public String getCustomerEmail() {
 67  		return customerEmail;
 68  	}
 69  
 70  	public void setCustomerEmail(String customerEmail) {
 71  		this.customerEmail = customerEmail;
 72  	}
 73  
 74  	public double getOrderValue() {
 75  		return orderValue;
 76  	}
 77  
 78  	public void setOrderValue(double orderValue) {
 79  		this.orderValue = orderValue;
 80  	}
 81  
 82  	public double getRetailPrice() {
 83  		return retailPrice;
 84  	}
 85  
 86  	public void setRetailPrice(double retailPrice) {
 87  		this.retailPrice = retailPrice;
 88  	}
 89  
 90  	public double getDiscount() {
 91  		return discount;
 92  	}
 93  
 94  	public void setDiscount(double discount) {
 95  		this.discount = discount;
 96  	}
 97  
 98  	public double getShippingFee() {
 99  		return shippingFee;
100  	}
101  
102  	public void setShippingFee(double shippingFee) {
103  		this.shippingFee = shippingFee;
104  	}
105  
106  	public double getShippingDiscount() {
107  		return shippingDiscount;
108  	}
109  
110  	public void setShippingDiscount(double shippingDiscount) {
111  		this.shippingDiscount = shippingDiscount;
112  	}
113  
```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/model/Order.java
      * Replace the `javax.persistence` import statement with `jakarta.persistence`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.model;
  2  
  3  import java.io.Serializable;
  4  import java.util.ArrayList;
  5  import java.util.List;
  6  
  7  import javax.persistence.CascadeType;
  8  import javax.persistence.Column;
  9  import javax.persistence.Entity;
 10  import javax.persistence.FetchType;
 11  import javax.persistence.GeneratedValue;
 12  import javax.persistence.Id;
 13  import javax.persistence.JoinColumn;
 14  import javax.persistence.OneToMany;
 15  import javax.persistence.Table;
 16  
 17  @Entity
 18  @Table(name = "ORDERS")
 19  public class Order implements Serializable {
 20  
 21  	private static final long serialVersionUID = -1L;
 22  
 23  	@Id
 24  	@GeneratedValue
 25  	private long orderId;
 26  
 27  	private String customerName;
 28  
 29  	private String customerEmail;
 30  
 31  	private double orderValue;
 32  
 33  	private double retailPrice;
 34  
 35  	private double discount;
 36  
 37  	private double shippingFee;
 38  
 39  	private double shippingDiscount;
 40  
 41  	@Column(name="TOTAL_PRICE")
 42  
 43  	
 44  	@OneToMany(fetch = FetchType.EAGER, cascade = CascadeType.ALL, orphanRemoval = true)
 45  	@JoinColumn(name="ORDER_ID")
 46  	private List<OrderItem> itemList = new ArrayList<>();
 47  
 48  	public Order() {}
 49  
 50  	public long getOrderId() {
 51  		return orderId;
 52  	}
 53  
 54  	public void setOrderId(long orderId) {
 55  		this.orderId = orderId;
 56  	}
 57  
 58  	public String getCustomerName() {
 59  		return customerName;
 60  	}
 61  
 62  	public void setCustomerName(String customerName) {
 63  		this.customerName = customerName;
 64  	}
 65  
 66  	public String getCustomerEmail() {
 67  		return customerEmail;
 68  	}
 69  
 70  	public void setCustomerEmail(String customerEmail) {
 71  		this.customerEmail = customerEmail;
 72  	}
 73  
 74  	public double getOrderValue() {
 75  		return orderValue;
 76  	}
 77  
 78  	public void setOrderValue(double orderValue) {
 79  		this.orderValue = orderValue;
 80  	}
 81  
 82  	public double getRetailPrice() {
 83  		return retailPrice;
 84  	}
 85  
 86  	public void setRetailPrice(double retailPrice) {
 87  		this.retailPrice = retailPrice;
 88  	}
 89  
 90  	public double getDiscount() {
 91  		return discount;
 92  	}
 93  
 94  	public void setDiscount(double discount) {
 95  		this.discount = discount;
 96  	}
 97  
 98  	public double getShippingFee() {
 99  		return shippingFee;
100  	}
101  
102  	public void setShippingFee(double shippingFee) {
103  		this.shippingFee = shippingFee;
104  	}
105  
106  	public double getShippingDiscount() {
107  		return shippingDiscount;
```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/model/OrderItem.java
      * Replace the `javax.persistence` import statement with `jakarta.persistence`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.model;
  2  
  3  import java.io.Serializable;
  4  
  5  import javax.persistence.Column;
  6  import javax.persistence.Entity;
  7  import javax.persistence.GeneratedValue;
  8  import javax.persistence.Id;
  9  import javax.persistence.Table;
 10  
 11  @Entity
 12  @Table(name = "ORDER_ITEMS")
 13  public class OrderItem implements Serializable {
 14  	private static final long serialVersionUID = 64565445665456666L;
 15  
 16  	@Id
 17  	@Column(name="ID")
 18  	@GeneratedValue
 19  	private long id;
 20  
 21  	private int quantity;
 22  
 23  	private String productId;
 24  
 25  	public OrderItem() {}
 26  
 27  	public String getProductId() {
 28  		return productId;
 29  	}
 30  
 31  	public void setProductId(String productId) {
 32  		this.productId = productId;
 33  	}
 34  
 35  	public int getQuantity() {
 36  		return quantity;
 37  	}
 38  
 39  	public void setQuantity(int quantity) {
 40  		this.quantity = quantity;
 41  	}
 42  
 43  	@Override
 44  	public String toString() {
 45  		return "OrderItem [productId=" + productId + ", quantity=" + quantity + "]";
 46  	}
 47  
 48  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/model/OrderItem.java
      * Replace the `javax.persistence` import statement with `jakarta.persistence`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.model;
  2  
  3  import java.io.Serializable;
  4  
  5  import javax.persistence.Column;
  6  import javax.persistence.Entity;
  7  import javax.persistence.GeneratedValue;
  8  import javax.persistence.Id;
  9  import javax.persistence.Table;
 10  
 11  @Entity
 12  @Table(name = "ORDER_ITEMS")
 13  public class OrderItem implements Serializable {
 14  	private static final long serialVersionUID = 64565445665456666L;
 15  
 16  	@Id
 17  	@Column(name="ID")
 18  	@GeneratedValue
 19  	private long id;
 20  
 21  	private int quantity;
 22  
 23  	private String productId;
 24  
 25  	public OrderItem() {}
 26  
 27  	public String getProductId() {
 28  		return productId;
 29  	}
 30  
 31  	public void setProductId(String productId) {
 32  		this.productId = productId;
 33  	}
 34  
 35  	public int getQuantity() {
 36  		return quantity;
 37  	}
 38  
 39  	public void setQuantity(int quantity) {
 40  		this.quantity = quantity;
 41  	}
 42  
 43  	@Override
 44  	public String toString() {
 45  		return "OrderItem [productId=" + productId + ", quantity=" + quantity + "]";
 46  	}
 47  
 48  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/model/OrderItem.java
      * Replace the `javax.persistence` import statement with `jakarta.persistence`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.model;
  2  
  3  import java.io.Serializable;
  4  
  5  import javax.persistence.Column;
  6  import javax.persistence.Entity;
  7  import javax.persistence.GeneratedValue;
  8  import javax.persistence.Id;
  9  import javax.persistence.Table;
 10  
 11  @Entity
 12  @Table(name = "ORDER_ITEMS")
 13  public class OrderItem implements Serializable {
 14  	private static final long serialVersionUID = 64565445665456666L;
 15  
 16  	@Id
 17  	@Column(name="ID")
 18  	@GeneratedValue
 19  	private long id;
 20  
 21  	private int quantity;
 22  
 23  	private String productId;
 24  
 25  	public OrderItem() {}
 26  
 27  	public String getProductId() {
 28  		return productId;
 29  	}
 30  
 31  	public void setProductId(String productId) {
 32  		this.productId = productId;
 33  	}
 34  
 35  	public int getQuantity() {
 36  		return quantity;
 37  	}
 38  
 39  	public void setQuantity(int quantity) {
 40  		this.quantity = quantity;
 41  	}
 42  
 43  	@Override
 44  	public String toString() {
 45  		return "OrderItem [productId=" + productId + ", quantity=" + quantity + "]";
 46  	}
 47  
 48  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/model/OrderItem.java
      * Replace the `javax.persistence` import statement with `jakarta.persistence`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.model;
  2  
  3  import java.io.Serializable;
  4  
  5  import javax.persistence.Column;
  6  import javax.persistence.Entity;
  7  import javax.persistence.GeneratedValue;
  8  import javax.persistence.Id;
  9  import javax.persistence.Table;
 10  
 11  @Entity
 12  @Table(name = "ORDER_ITEMS")
 13  public class OrderItem implements Serializable {
 14  	private static final long serialVersionUID = 64565445665456666L;
 15  
 16  	@Id
 17  	@Column(name="ID")
 18  	@GeneratedValue
 19  	private long id;
 20  
 21  	private int quantity;
 22  
 23  	private String productId;
 24  
 25  	public OrderItem() {}
 26  
 27  	public String getProductId() {
 28  		return productId;
 29  	}
 30  
 31  	public void setProductId(String productId) {
 32  		this.productId = productId;
 33  	}
 34  
 35  	public int getQuantity() {
 36  		return quantity;
 37  	}
 38  
 39  	public void setQuantity(int quantity) {
 40  		this.quantity = quantity;
 41  	}
 42  
 43  	@Override
 44  	public String toString() {
 45  		return "OrderItem [productId=" + productId + ", quantity=" + quantity + "]";
 46  	}
 47  
 48  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/model/OrderItem.java
      * Replace the `javax.persistence` import statement with `jakarta.persistence`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.model;
  2  
  3  import java.io.Serializable;
  4  
  5  import javax.persistence.Column;
  6  import javax.persistence.Entity;
  7  import javax.persistence.GeneratedValue;
  8  import javax.persistence.Id;
  9  import javax.persistence.Table;
 10  
 11  @Entity
 12  @Table(name = "ORDER_ITEMS")
 13  public class OrderItem implements Serializable {
 14  	private static final long serialVersionUID = 64565445665456666L;
 15  
 16  	@Id
 17  	@Column(name="ID")
 18  	@GeneratedValue
 19  	private long id;
 20  
 21  	private int quantity;
 22  
 23  	private String productId;
 24  
 25  	public OrderItem() {}
 26  
 27  	public String getProductId() {
 28  		return productId;
 29  	}
 30  
 31  	public void setProductId(String productId) {
 32  		this.productId = productId;
 33  	}
 34  
 35  	public int getQuantity() {
 36  		return quantity;
 37  	}
 38  
 39  	public void setQuantity(int quantity) {
 40  		this.quantity = quantity;
 41  	}
 42  
 43  	@Override
 44  	public String toString() {
 45  		return "OrderItem [productId=" + productId + ", quantity=" + quantity + "]";
 46  	}
 47  
 48  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/model/ShoppingCart.java
      * Replace the `javax.enterprise` import statement with `jakarta.enterprise`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.model;
  2  
  3  import java.io.Serializable;
  4  import java.util.ArrayList;
  5  import java.util.List;
  6  import java.util.stream.Collectors;
  7  
  8  import javax.enterprise.context.Dependent;
  9  
 10  @Dependent
 11  public class ShoppingCart implements Serializable {
 12  
 13  	private static final long serialVersionUID = -1108043957592113528L;
 14  
 15  	private double cartItemTotal;
 16  
 17  	private double cartItemPromoSavings;
 18  	
 19  	private double shippingTotal;
 20  	
 21  	private double shippingPromoSavings;
 22  	
 23  	private double cartTotal;
 24  			
 25  	private List<ShoppingCartItem> shoppingCartItemList = new ArrayList<ShoppingCartItem>();
 26  
 27  	public ShoppingCart() {
 28  		
 29  	}
 30  	
 31  	public List<ShoppingCartItem> getShoppingCartItemList() {
 32  		return shoppingCartItemList;
 33  	}
 34  
 35  	public void setShoppingCartItemList(List<ShoppingCartItem> shoppingCartItemList) {
 36  		this.shoppingCartItemList = shoppingCartItemList;
 37  	}
 38  
 39  	public void resetShoppingCartItemList() {
 40  		shoppingCartItemList = new ArrayList<ShoppingCartItem>();
 41  	}
 42  
 43  	public void addShoppingCartItem(ShoppingCartItem sci) {
 44  		
 45  		if ( sci != null ) {
 46  			
 47  			shoppingCartItemList.add(sci);
 48  			
 49  		}
 50  		
 51  	}
 52  	
 53  	public boolean removeShoppingCartItem(ShoppingCartItem sci) {
 54  		
 55  		boolean removed = false;
 56  		
 57  		if ( sci != null ) {
 58  			
 59  			removed = shoppingCartItemList.remove(sci);
 60  			
 61  		}
 62  		
 63  		return removed;
 64  		
 65  	}
 66  
 67  	public double getCartItemTotal() {
 68  		return cartItemTotal;
 69  	}
 70  
 71  	public void setCartItemTotal(double cartItemTotal) {
 72  		this.cartItemTotal = cartItemTotal;
 73  	}
 74  
 75  	public double getShippingTotal() {
 76  		return shippingTotal;
 77  	}
 78  
 79  	public void setShippingTotal(double shippingTotal) {
 80  		this.shippingTotal = shippingTotal;
 81  	}
 82  
 83  	public double getCartTotal() {
 84  		return cartTotal;
 85  	}
 86  
 87  	public void setCartTotal(double cartTotal) {
 88  		this.cartTotal = cartTotal;
 89  	}
 90  
 91  	public double getCartItemPromoSavings() {
 92  		return cartItemPromoSavings;
 93  	}
 94  
 95  	public void setCartItemPromoSavings(double cartItemPromoSavings) {
 96  		this.cartItemPromoSavings = cartItemPromoSavings;
 97  	}
 98  
 99  	public double getShippingPromoSavings() {
100  		return shippingPromoSavings;
101  	}
102  
103  	public void setShippingPromoSavings(double shippingPromoSavings) {
104  		this.shippingPromoSavings = shippingPromoSavings;
105  	}
106  
107  	@Override
108  	public String toString() {
```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/rest/CartEndpoint.java
      * Replace the `javax.ws` import statement with `jakarta.ws`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.rest;
  2  
  3  import java.io.Serializable;
  4  import java.util.ArrayList;
  5  import java.util.HashMap;
  6  import java.util.List;
  7  import java.util.Map;
  8  
  9  import javax.enterprise.context.SessionScoped;
 10  import javax.inject.Inject;
 11  import javax.jms.JMSDestinationDefinition;
 12  import javax.jms.JMSDestinationDefinitions;
 13  import javax.ws.rs.DELETE;
 14  import javax.ws.rs.GET;
 15  import javax.ws.rs.POST;
 16  import javax.ws.rs.Path;
 17  import javax.ws.rs.PathParam;
 18  import javax.ws.rs.Produces;
 19  import javax.ws.rs.core.MediaType;
 20  
 21  import com.redhat.coolstore.model.Product;
 22  import com.redhat.coolstore.model.ShoppingCart;
 23  import com.redhat.coolstore.model.ShoppingCartItem;
 24  import com.redhat.coolstore.service.ShoppingCartService;
 25  
 26  @SessionScoped
 27  @Path("/cart")
 28  @JMSDestinationDefinitions(
 29  	value = {
 30  		@JMSDestinationDefinition(
 31  			name = "java:/jms/queue/orders",
 32  			interfaceName = "javax.jms.Queue",
 33  			destinationName = "ordersQueue"
 34  		)
 35  	}
 36  )
 37  public class CartEndpoint implements Serializable {
 38  
 39  	private static final long serialVersionUID = -7227732980791688773L;
 40  
 41  	@Inject
 42  	private ShoppingCartService shoppingCartService;
 43  
 44  	@GET
 45  	@Path("/{cartId}")
 46  	@Produces(MediaType.APPLICATION_JSON)
 47  	public ShoppingCart getCart(@PathParam("cartId") String cartId) {
 48  		return shoppingCartService.getShoppingCart(cartId);
 49  	}
 50  
 51  	@POST
 52  	@Path("/checkout/{cartId}")
 53  	@Produces(MediaType.APPLICATION_JSON)
 54  	public ShoppingCart checkout(@PathParam("cartId") String cartId) {
 55  		return shoppingCartService.checkOutShoppingCart(cartId);
 56  	}
 57  
 58  	@POST
 59  	@Path("/{cartId}/{itemId}/{quantity}")
 60  	@Produces(MediaType.APPLICATION_JSON)
 61  	public ShoppingCart add(@PathParam("cartId") String cartId,
 62  							@PathParam("itemId") String itemId,
 63  							@PathParam("quantity") int quantity) throws Exception {
 64  		ShoppingCart cart = shoppingCartService.getShoppingCart(cartId);
 65  
 66  		Product product = shoppingCartService.getProduct(itemId);
 67  
 68  		ShoppingCartItem sci = new ShoppingCartItem();
 69  		sci.setProduct(product);
 70  		sci.setQuantity(quantity);
 71  		sci.setPrice(product.getPrice());
 72  		cart.addShoppingCartItem(sci);
 73  
 74  		try {
 75  			shoppingCartService.priceShoppingCart(cart);
 76  			cart.setShoppingCartItemList(dedupeCartItems(cart.getShoppingCartItemList()));
 77  		} catch (Exception ex) {
 78  			cart.removeShoppingCartItem(sci);
 79  			throw ex;
 80  		}
 81  
 82  		return cart;
 83  	}
 84  
 85  	@POST
 86  	@Path("/{cartId}/{tmpId}")
 87  	@Produces(MediaType.APPLICATION_JSON)
 88  	public ShoppingCart set(@PathParam("cartId") String cartId,
 89  							@PathParam("tmpId") String tmpId) throws Exception {
 90  
 91  		ShoppingCart cart = shoppingCartService.getShoppingCart(cartId);
 92  		ShoppingCart tmpCart = shoppingCartService.getShoppingCart(tmpId);
 93  
 94  		if (tmpCart != null) {
 95  			cart.resetShoppingCartItemList();
 96  			cart.setShoppingCartItemList(tmpCart.getShoppingCartItemList());
 97  		}
 98  
 99  		try {
100  			shoppingCartService.priceShoppingCart(cart);
101  			cart.setShoppingCartItemList(dedupeCartItems(cart.getShoppingCartItemList()));
102  		} catch (Exception ex) {
103  			throw ex;
104  		}
105  
106  		return cart;
107  	}
108  
109  	@DELETE
110  	@Path("/{cartId}/{itemId}/{quantity}")
111  	@Produces(MediaType.APPLICATION_JSON)
112  	public ShoppingCart delete(@PathParam("cartId") String cartId,
113  							   @PathParam("itemId") String itemId,
```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/rest/CartEndpoint.java
      * Replace the `javax.ws` import statement with `jakarta.ws`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.rest;
  2  
  3  import java.io.Serializable;
  4  import java.util.ArrayList;
  5  import java.util.HashMap;
  6  import java.util.List;
  7  import java.util.Map;
  8  
  9  import javax.enterprise.context.SessionScoped;
 10  import javax.inject.Inject;
 11  import javax.jms.JMSDestinationDefinition;
 12  import javax.jms.JMSDestinationDefinitions;
 13  import javax.ws.rs.DELETE;
 14  import javax.ws.rs.GET;
 15  import javax.ws.rs.POST;
 16  import javax.ws.rs.Path;
 17  import javax.ws.rs.PathParam;
 18  import javax.ws.rs.Produces;
 19  import javax.ws.rs.core.MediaType;
 20  
 21  import com.redhat.coolstore.model.Product;
 22  import com.redhat.coolstore.model.ShoppingCart;
 23  import com.redhat.coolstore.model.ShoppingCartItem;
 24  import com.redhat.coolstore.service.ShoppingCartService;
 25  
 26  @SessionScoped
 27  @Path("/cart")
 28  @JMSDestinationDefinitions(
 29  	value = {
 30  		@JMSDestinationDefinition(
 31  			name = "java:/jms/queue/orders",
 32  			interfaceName = "javax.jms.Queue",
 33  			destinationName = "ordersQueue"
 34  		)
 35  	}
 36  )
 37  public class CartEndpoint implements Serializable {
 38  
 39  	private static final long serialVersionUID = -7227732980791688773L;
 40  
 41  	@Inject
 42  	private ShoppingCartService shoppingCartService;
 43  
 44  	@GET
 45  	@Path("/{cartId}")
 46  	@Produces(MediaType.APPLICATION_JSON)
 47  	public ShoppingCart getCart(@PathParam("cartId") String cartId) {
 48  		return shoppingCartService.getShoppingCart(cartId);
 49  	}
 50  
 51  	@POST
 52  	@Path("/checkout/{cartId}")
 53  	@Produces(MediaType.APPLICATION_JSON)
 54  	public ShoppingCart checkout(@PathParam("cartId") String cartId) {
 55  		return shoppingCartService.checkOutShoppingCart(cartId);
 56  	}
 57  
 58  	@POST
 59  	@Path("/{cartId}/{itemId}/{quantity}")
 60  	@Produces(MediaType.APPLICATION_JSON)
 61  	public ShoppingCart add(@PathParam("cartId") String cartId,
 62  							@PathParam("itemId") String itemId,
 63  							@PathParam("quantity") int quantity) throws Exception {
 64  		ShoppingCart cart = shoppingCartService.getShoppingCart(cartId);
 65  
 66  		Product product = shoppingCartService.getProduct(itemId);
 67  
 68  		ShoppingCartItem sci = new ShoppingCartItem();
 69  		sci.setProduct(product);
 70  		sci.setQuantity(quantity);
 71  		sci.setPrice(product.getPrice());
 72  		cart.addShoppingCartItem(sci);
 73  
 74  		try {
 75  			shoppingCartService.priceShoppingCart(cart);
 76  			cart.setShoppingCartItemList(dedupeCartItems(cart.getShoppingCartItemList()));
 77  		} catch (Exception ex) {
 78  			cart.removeShoppingCartItem(sci);
 79  			throw ex;
 80  		}
 81  
 82  		return cart;
 83  	}
 84  
 85  	@POST
 86  	@Path("/{cartId}/{tmpId}")
 87  	@Produces(MediaType.APPLICATION_JSON)
 88  	public ShoppingCart set(@PathParam("cartId") String cartId,
 89  							@PathParam("tmpId") String tmpId) throws Exception {
 90  
 91  		ShoppingCart cart = shoppingCartService.getShoppingCart(cartId);
 92  		ShoppingCart tmpCart = shoppingCartService.getShoppingCart(tmpId);
 93  
 94  		if (tmpCart != null) {
 95  			cart.resetShoppingCartItemList();
 96  			cart.setShoppingCartItemList(tmpCart.getShoppingCartItemList());
 97  		}
 98  
 99  		try {
100  			shoppingCartService.priceShoppingCart(cart);
101  			cart.setShoppingCartItemList(dedupeCartItems(cart.getShoppingCartItemList()));
102  		} catch (Exception ex) {
103  			throw ex;
104  		}
105  
106  		return cart;
107  	}
108  
109  	@DELETE
110  	@Path("/{cartId}/{itemId}/{quantity}")
111  	@Produces(MediaType.APPLICATION_JSON)
112  	public ShoppingCart delete(@PathParam("cartId") String cartId,
113  							   @PathParam("itemId") String itemId,
114  							   @PathParam("quantity") int quantity) throws Exception {
115  
116  		List<ShoppingCartItem> toRemoveList = new ArrayList<>();
117  
118  		ShoppingCart cart = shoppingCartService.getShoppingCart(cartId);
```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/rest/CartEndpoint.java
      * Replace the `javax.ws` import statement with `jakarta.ws`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.rest;
  2  
  3  import java.io.Serializable;
  4  import java.util.ArrayList;
  5  import java.util.HashMap;
  6  import java.util.List;
  7  import java.util.Map;
  8  
  9  import javax.enterprise.context.SessionScoped;
 10  import javax.inject.Inject;
 11  import javax.jms.JMSDestinationDefinition;
 12  import javax.jms.JMSDestinationDefinitions;
 13  import javax.ws.rs.DELETE;
 14  import javax.ws.rs.GET;
 15  import javax.ws.rs.POST;
 16  import javax.ws.rs.Path;
 17  import javax.ws.rs.PathParam;
 18  import javax.ws.rs.Produces;
 19  import javax.ws.rs.core.MediaType;
 20  
 21  import com.redhat.coolstore.model.Product;
 22  import com.redhat.coolstore.model.ShoppingCart;
 23  import com.redhat.coolstore.model.ShoppingCartItem;
 24  import com.redhat.coolstore.service.ShoppingCartService;
 25  
 26  @SessionScoped
 27  @Path("/cart")
 28  @JMSDestinationDefinitions(
 29  	value = {
 30  		@JMSDestinationDefinition(
 31  			name = "java:/jms/queue/orders",
 32  			interfaceName = "javax.jms.Queue",
 33  			destinationName = "ordersQueue"
 34  		)
 35  	}
 36  )
 37  public class CartEndpoint implements Serializable {
 38  
 39  	private static final long serialVersionUID = -7227732980791688773L;
 40  
 41  	@Inject
 42  	private ShoppingCartService shoppingCartService;
 43  
 44  	@GET
 45  	@Path("/{cartId}")
 46  	@Produces(MediaType.APPLICATION_JSON)
 47  	public ShoppingCart getCart(@PathParam("cartId") String cartId) {
 48  		return shoppingCartService.getShoppingCart(cartId);
 49  	}
 50  
 51  	@POST
 52  	@Path("/checkout/{cartId}")
 53  	@Produces(MediaType.APPLICATION_JSON)
 54  	public ShoppingCart checkout(@PathParam("cartId") String cartId) {
 55  		return shoppingCartService.checkOutShoppingCart(cartId);
 56  	}
 57  
 58  	@POST
 59  	@Path("/{cartId}/{itemId}/{quantity}")
 60  	@Produces(MediaType.APPLICATION_JSON)
 61  	public ShoppingCart add(@PathParam("cartId") String cartId,
 62  							@PathParam("itemId") String itemId,
 63  							@PathParam("quantity") int quantity) throws Exception {
 64  		ShoppingCart cart = shoppingCartService.getShoppingCart(cartId);
 65  
 66  		Product product = shoppingCartService.getProduct(itemId);
 67  
 68  		ShoppingCartItem sci = new ShoppingCartItem();
 69  		sci.setProduct(product);
 70  		sci.setQuantity(quantity);
 71  		sci.setPrice(product.getPrice());
 72  		cart.addShoppingCartItem(sci);
 73  
 74  		try {
 75  			shoppingCartService.priceShoppingCart(cart);
 76  			cart.setShoppingCartItemList(dedupeCartItems(cart.getShoppingCartItemList()));
 77  		} catch (Exception ex) {
 78  			cart.removeShoppingCartItem(sci);
 79  			throw ex;
 80  		}
 81  
 82  		return cart;
 83  	}
 84  
 85  	@POST
 86  	@Path("/{cartId}/{tmpId}")
 87  	@Produces(MediaType.APPLICATION_JSON)
 88  	public ShoppingCart set(@PathParam("cartId") String cartId,
 89  							@PathParam("tmpId") String tmpId) throws Exception {
 90  
 91  		ShoppingCart cart = shoppingCartService.getShoppingCart(cartId);
 92  		ShoppingCart tmpCart = shoppingCartService.getShoppingCart(tmpId);
 93  
 94  		if (tmpCart != null) {
 95  			cart.resetShoppingCartItemList();
 96  			cart.setShoppingCartItemList(tmpCart.getShoppingCartItemList());
 97  		}
 98  
 99  		try {
100  			shoppingCartService.priceShoppingCart(cart);
101  			cart.setShoppingCartItemList(dedupeCartItems(cart.getShoppingCartItemList()));
102  		} catch (Exception ex) {
103  			throw ex;
104  		}
105  
106  		return cart;
107  	}
108  
109  	@DELETE
110  	@Path("/{cartId}/{itemId}/{quantity}")
111  	@Produces(MediaType.APPLICATION_JSON)
112  	public ShoppingCart delete(@PathParam("cartId") String cartId,
113  							   @PathParam("itemId") String itemId,
114  							   @PathParam("quantity") int quantity) throws Exception {
115  
116  		List<ShoppingCartItem> toRemoveList = new ArrayList<>();
117  
```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/rest/CartEndpoint.java
      * Replace the `javax.ws` import statement with `jakarta.ws`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.rest;
  2  
  3  import java.io.Serializable;
  4  import java.util.ArrayList;
  5  import java.util.HashMap;
  6  import java.util.List;
  7  import java.util.Map;
  8  
  9  import javax.enterprise.context.SessionScoped;
 10  import javax.inject.Inject;
 11  import javax.jms.JMSDestinationDefinition;
 12  import javax.jms.JMSDestinationDefinitions;
 13  import javax.ws.rs.DELETE;
 14  import javax.ws.rs.GET;
 15  import javax.ws.rs.POST;
 16  import javax.ws.rs.Path;
 17  import javax.ws.rs.PathParam;
 18  import javax.ws.rs.Produces;
 19  import javax.ws.rs.core.MediaType;
 20  
 21  import com.redhat.coolstore.model.Product;
 22  import com.redhat.coolstore.model.ShoppingCart;
 23  import com.redhat.coolstore.model.ShoppingCartItem;
 24  import com.redhat.coolstore.service.ShoppingCartService;
 25  
 26  @SessionScoped
 27  @Path("/cart")
 28  @JMSDestinationDefinitions(
 29  	value = {
 30  		@JMSDestinationDefinition(
 31  			name = "java:/jms/queue/orders",
 32  			interfaceName = "javax.jms.Queue",
 33  			destinationName = "ordersQueue"
 34  		)
 35  	}
 36  )
 37  public class CartEndpoint implements Serializable {
 38  
 39  	private static final long serialVersionUID = -7227732980791688773L;
 40  
 41  	@Inject
 42  	private ShoppingCartService shoppingCartService;
 43  
 44  	@GET
 45  	@Path("/{cartId}")
 46  	@Produces(MediaType.APPLICATION_JSON)
 47  	public ShoppingCart getCart(@PathParam("cartId") String cartId) {
 48  		return shoppingCartService.getShoppingCart(cartId);
 49  	}
 50  
 51  	@POST
 52  	@Path("/checkout/{cartId}")
 53  	@Produces(MediaType.APPLICATION_JSON)
 54  	public ShoppingCart checkout(@PathParam("cartId") String cartId) {
 55  		return shoppingCartService.checkOutShoppingCart(cartId);
 56  	}
 57  
 58  	@POST
 59  	@Path("/{cartId}/{itemId}/{quantity}")
 60  	@Produces(MediaType.APPLICATION_JSON)
 61  	public ShoppingCart add(@PathParam("cartId") String cartId,
 62  							@PathParam("itemId") String itemId,
 63  							@PathParam("quantity") int quantity) throws Exception {
 64  		ShoppingCart cart = shoppingCartService.getShoppingCart(cartId);
 65  
 66  		Product product = shoppingCartService.getProduct(itemId);
 67  
 68  		ShoppingCartItem sci = new ShoppingCartItem();
 69  		sci.setProduct(product);
 70  		sci.setQuantity(quantity);
 71  		sci.setPrice(product.getPrice());
 72  		cart.addShoppingCartItem(sci);
 73  
 74  		try {
 75  			shoppingCartService.priceShoppingCart(cart);
 76  			cart.setShoppingCartItemList(dedupeCartItems(cart.getShoppingCartItemList()));
 77  		} catch (Exception ex) {
 78  			cart.removeShoppingCartItem(sci);
 79  			throw ex;
 80  		}
 81  
 82  		return cart;
 83  	}
 84  
 85  	@POST
 86  	@Path("/{cartId}/{tmpId}")
 87  	@Produces(MediaType.APPLICATION_JSON)
 88  	public ShoppingCart set(@PathParam("cartId") String cartId,
 89  							@PathParam("tmpId") String tmpId) throws Exception {
 90  
 91  		ShoppingCart cart = shoppingCartService.getShoppingCart(cartId);
 92  		ShoppingCart tmpCart = shoppingCartService.getShoppingCart(tmpId);
 93  
 94  		if (tmpCart != null) {
 95  			cart.resetShoppingCartItemList();
 96  			cart.setShoppingCartItemList(tmpCart.getShoppingCartItemList());
 97  		}
 98  
 99  		try {
100  			shoppingCartService.priceShoppingCart(cart);
101  			cart.setShoppingCartItemList(dedupeCartItems(cart.getShoppingCartItemList()));
102  		} catch (Exception ex) {
103  			throw ex;
104  		}
105  
106  		return cart;
107  	}
108  
109  	@DELETE
110  	@Path("/{cartId}/{itemId}/{quantity}")
111  	@Produces(MediaType.APPLICATION_JSON)
112  	public ShoppingCart delete(@PathParam("cartId") String cartId,
113  							   @PathParam("itemId") String itemId,
114  							   @PathParam("quantity") int quantity) throws Exception {
115  
```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/rest/CartEndpoint.java
      * Replace the `javax.ws` import statement with `jakarta.ws`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.rest;
  2  
  3  import java.io.Serializable;
  4  import java.util.ArrayList;
  5  import java.util.HashMap;
  6  import java.util.List;
  7  import java.util.Map;
  8  
  9  import javax.enterprise.context.SessionScoped;
 10  import javax.inject.Inject;
 11  import javax.jms.JMSDestinationDefinition;
 12  import javax.jms.JMSDestinationDefinitions;
 13  import javax.ws.rs.DELETE;
 14  import javax.ws.rs.GET;
 15  import javax.ws.rs.POST;
 16  import javax.ws.rs.Path;
 17  import javax.ws.rs.PathParam;
 18  import javax.ws.rs.Produces;
 19  import javax.ws.rs.core.MediaType;
 20  
 21  import com.redhat.coolstore.model.Product;
 22  import com.redhat.coolstore.model.ShoppingCart;
 23  import com.redhat.coolstore.model.ShoppingCartItem;
 24  import com.redhat.coolstore.service.ShoppingCartService;
 25  
 26  @SessionScoped
 27  @Path("/cart")
 28  @JMSDestinationDefinitions(
 29  	value = {
 30  		@JMSDestinationDefinition(
 31  			name = "java:/jms/queue/orders",
 32  			interfaceName = "javax.jms.Queue",
 33  			destinationName = "ordersQueue"
 34  		)
 35  	}
 36  )
 37  public class CartEndpoint implements Serializable {
 38  
 39  	private static final long serialVersionUID = -7227732980791688773L;
 40  
 41  	@Inject
 42  	private ShoppingCartService shoppingCartService;
 43  
 44  	@GET
 45  	@Path("/{cartId}")
 46  	@Produces(MediaType.APPLICATION_JSON)
 47  	public ShoppingCart getCart(@PathParam("cartId") String cartId) {
 48  		return shoppingCartService.getShoppingCart(cartId);
 49  	}
 50  
 51  	@POST
 52  	@Path("/checkout/{cartId}")
 53  	@Produces(MediaType.APPLICATION_JSON)
 54  	public ShoppingCart checkout(@PathParam("cartId") String cartId) {
 55  		return shoppingCartService.checkOutShoppingCart(cartId);
 56  	}
 57  
 58  	@POST
 59  	@Path("/{cartId}/{itemId}/{quantity}")
 60  	@Produces(MediaType.APPLICATION_JSON)
 61  	public ShoppingCart add(@PathParam("cartId") String cartId,
 62  							@PathParam("itemId") String itemId,
 63  							@PathParam("quantity") int quantity) throws Exception {
 64  		ShoppingCart cart = shoppingCartService.getShoppingCart(cartId);
 65  
 66  		Product product = shoppingCartService.getProduct(itemId);
 67  
 68  		ShoppingCartItem sci = new ShoppingCartItem();
 69  		sci.setProduct(product);
 70  		sci.setQuantity(quantity);
 71  		sci.setPrice(product.getPrice());
 72  		cart.addShoppingCartItem(sci);
 73  
 74  		try {
 75  			shoppingCartService.priceShoppingCart(cart);
 76  			cart.setShoppingCartItemList(dedupeCartItems(cart.getShoppingCartItemList()));
 77  		} catch (Exception ex) {
 78  			cart.removeShoppingCartItem(sci);
 79  			throw ex;
 80  		}
 81  
 82  		return cart;
 83  	}
 84  
 85  	@POST
 86  	@Path("/{cartId}/{tmpId}")
 87  	@Produces(MediaType.APPLICATION_JSON)
 88  	public ShoppingCart set(@PathParam("cartId") String cartId,
 89  							@PathParam("tmpId") String tmpId) throws Exception {
 90  
 91  		ShoppingCart cart = shoppingCartService.getShoppingCart(cartId);
 92  		ShoppingCart tmpCart = shoppingCartService.getShoppingCart(tmpId);
 93  
 94  		if (tmpCart != null) {
 95  			cart.resetShoppingCartItemList();
 96  			cart.setShoppingCartItemList(tmpCart.getShoppingCartItemList());
 97  		}
 98  
 99  		try {
100  			shoppingCartService.priceShoppingCart(cart);
101  			cart.setShoppingCartItemList(dedupeCartItems(cart.getShoppingCartItemList()));
102  		} catch (Exception ex) {
103  			throw ex;
104  		}
105  
106  		return cart;
107  	}
108  
109  	@DELETE
110  	@Path("/{cartId}/{itemId}/{quantity}")
111  	@Produces(MediaType.APPLICATION_JSON)
112  	public ShoppingCart delete(@PathParam("cartId") String cartId,
113  							   @PathParam("itemId") String itemId,
114  							   @PathParam("quantity") int quantity) throws Exception {
115  
116  		List<ShoppingCartItem> toRemoveList = new ArrayList<>();
117  
118  		ShoppingCart cart = shoppingCartService.getShoppingCart(cartId);
119  
```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/rest/CartEndpoint.java
      * Replace the `javax.jms` import statement with `jakarta.jms`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.rest;
  2  
  3  import java.io.Serializable;
  4  import java.util.ArrayList;
  5  import java.util.HashMap;
  6  import java.util.List;
  7  import java.util.Map;
  8  
  9  import javax.enterprise.context.SessionScoped;
 10  import javax.inject.Inject;
 11  import javax.jms.JMSDestinationDefinition;
 12  import javax.jms.JMSDestinationDefinitions;
 13  import javax.ws.rs.DELETE;
 14  import javax.ws.rs.GET;
 15  import javax.ws.rs.POST;
 16  import javax.ws.rs.Path;
 17  import javax.ws.rs.PathParam;
 18  import javax.ws.rs.Produces;
 19  import javax.ws.rs.core.MediaType;
 20  
 21  import com.redhat.coolstore.model.Product;
 22  import com.redhat.coolstore.model.ShoppingCart;
 23  import com.redhat.coolstore.model.ShoppingCartItem;
 24  import com.redhat.coolstore.service.ShoppingCartService;
 25  
 26  @SessionScoped
 27  @Path("/cart")
 28  @JMSDestinationDefinitions(
 29  	value = {
 30  		@JMSDestinationDefinition(
 31  			name = "java:/jms/queue/orders",
 32  			interfaceName = "javax.jms.Queue",
 33  			destinationName = "ordersQueue"
 34  		)
 35  	}
 36  )
 37  public class CartEndpoint implements Serializable {
 38  
 39  	private static final long serialVersionUID = -7227732980791688773L;
 40  
 41  	@Inject
 42  	private ShoppingCartService shoppingCartService;
 43  
 44  	@GET
 45  	@Path("/{cartId}")
 46  	@Produces(MediaType.APPLICATION_JSON)
 47  	public ShoppingCart getCart(@PathParam("cartId") String cartId) {
 48  		return shoppingCartService.getShoppingCart(cartId);
 49  	}
 50  
 51  	@POST
 52  	@Path("/checkout/{cartId}")
 53  	@Produces(MediaType.APPLICATION_JSON)
 54  	public ShoppingCart checkout(@PathParam("cartId") String cartId) {
 55  		return shoppingCartService.checkOutShoppingCart(cartId);
 56  	}
 57  
 58  	@POST
 59  	@Path("/{cartId}/{itemId}/{quantity}")
 60  	@Produces(MediaType.APPLICATION_JSON)
 61  	public ShoppingCart add(@PathParam("cartId") String cartId,
 62  							@PathParam("itemId") String itemId,
 63  							@PathParam("quantity") int quantity) throws Exception {
 64  		ShoppingCart cart = shoppingCartService.getShoppingCart(cartId);
 65  
 66  		Product product = shoppingCartService.getProduct(itemId);
 67  
 68  		ShoppingCartItem sci = new ShoppingCartItem();
 69  		sci.setProduct(product);
 70  		sci.setQuantity(quantity);
 71  		sci.setPrice(product.getPrice());
 72  		cart.addShoppingCartItem(sci);
 73  
 74  		try {
 75  			shoppingCartService.priceShoppingCart(cart);
 76  			cart.setShoppingCartItemList(dedupeCartItems(cart.getShoppingCartItemList()));
 77  		} catch (Exception ex) {
 78  			cart.removeShoppingCartItem(sci);
 79  			throw ex;
 80  		}
 81  
 82  		return cart;
 83  	}
 84  
 85  	@POST
 86  	@Path("/{cartId}/{tmpId}")
 87  	@Produces(MediaType.APPLICATION_JSON)
 88  	public ShoppingCart set(@PathParam("cartId") String cartId,
 89  							@PathParam("tmpId") String tmpId) throws Exception {
 90  
 91  		ShoppingCart cart = shoppingCartService.getShoppingCart(cartId);
 92  		ShoppingCart tmpCart = shoppingCartService.getShoppingCart(tmpId);
 93  
 94  		if (tmpCart != null) {
 95  			cart.resetShoppingCartItemList();
 96  			cart.setShoppingCartItemList(tmpCart.getShoppingCartItemList());
 97  		}
 98  
 99  		try {
100  			shoppingCartService.priceShoppingCart(cart);
101  			cart.setShoppingCartItemList(dedupeCartItems(cart.getShoppingCartItemList()));
102  		} catch (Exception ex) {
103  			throw ex;
104  		}
105  
106  		return cart;
107  	}
108  
109  	@DELETE
110  	@Path("/{cartId}/{itemId}/{quantity}")
111  	@Produces(MediaType.APPLICATION_JSON)
```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/rest/CartEndpoint.java
      * Replace the `javax.enterprise` import statement with `jakarta.enterprise`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.rest;
  2  
  3  import java.io.Serializable;
  4  import java.util.ArrayList;
  5  import java.util.HashMap;
  6  import java.util.List;
  7  import java.util.Map;
  8  
  9  import javax.enterprise.context.SessionScoped;
 10  import javax.inject.Inject;
 11  import javax.jms.JMSDestinationDefinition;
 12  import javax.jms.JMSDestinationDefinitions;
 13  import javax.ws.rs.DELETE;
 14  import javax.ws.rs.GET;
 15  import javax.ws.rs.POST;
 16  import javax.ws.rs.Path;
 17  import javax.ws.rs.PathParam;
 18  import javax.ws.rs.Produces;
 19  import javax.ws.rs.core.MediaType;
 20  
 21  import com.redhat.coolstore.model.Product;
 22  import com.redhat.coolstore.model.ShoppingCart;
 23  import com.redhat.coolstore.model.ShoppingCartItem;
 24  import com.redhat.coolstore.service.ShoppingCartService;
 25  
 26  @SessionScoped
 27  @Path("/cart")
 28  @JMSDestinationDefinitions(
 29  	value = {
 30  		@JMSDestinationDefinition(
 31  			name = "java:/jms/queue/orders",
 32  			interfaceName = "javax.jms.Queue",
 33  			destinationName = "ordersQueue"
 34  		)
 35  	}
 36  )
 37  public class CartEndpoint implements Serializable {
 38  
 39  	private static final long serialVersionUID = -7227732980791688773L;
 40  
 41  	@Inject
 42  	private ShoppingCartService shoppingCartService;
 43  
 44  	@GET
 45  	@Path("/{cartId}")
 46  	@Produces(MediaType.APPLICATION_JSON)
 47  	public ShoppingCart getCart(@PathParam("cartId") String cartId) {
 48  		return shoppingCartService.getShoppingCart(cartId);
 49  	}
 50  
 51  	@POST
 52  	@Path("/checkout/{cartId}")
 53  	@Produces(MediaType.APPLICATION_JSON)
 54  	public ShoppingCart checkout(@PathParam("cartId") String cartId) {
 55  		return shoppingCartService.checkOutShoppingCart(cartId);
 56  	}
 57  
 58  	@POST
 59  	@Path("/{cartId}/{itemId}/{quantity}")
 60  	@Produces(MediaType.APPLICATION_JSON)
 61  	public ShoppingCart add(@PathParam("cartId") String cartId,
 62  							@PathParam("itemId") String itemId,
 63  							@PathParam("quantity") int quantity) throws Exception {
 64  		ShoppingCart cart = shoppingCartService.getShoppingCart(cartId);
 65  
 66  		Product product = shoppingCartService.getProduct(itemId);
 67  
 68  		ShoppingCartItem sci = new ShoppingCartItem();
 69  		sci.setProduct(product);
 70  		sci.setQuantity(quantity);
 71  		sci.setPrice(product.getPrice());
 72  		cart.addShoppingCartItem(sci);
 73  
 74  		try {
 75  			shoppingCartService.priceShoppingCart(cart);
 76  			cart.setShoppingCartItemList(dedupeCartItems(cart.getShoppingCartItemList()));
 77  		} catch (Exception ex) {
 78  			cart.removeShoppingCartItem(sci);
 79  			throw ex;
 80  		}
 81  
 82  		return cart;
 83  	}
 84  
 85  	@POST
 86  	@Path("/{cartId}/{tmpId}")
 87  	@Produces(MediaType.APPLICATION_JSON)
 88  	public ShoppingCart set(@PathParam("cartId") String cartId,
 89  							@PathParam("tmpId") String tmpId) throws Exception {
 90  
 91  		ShoppingCart cart = shoppingCartService.getShoppingCart(cartId);
 92  		ShoppingCart tmpCart = shoppingCartService.getShoppingCart(tmpId);
 93  
 94  		if (tmpCart != null) {
 95  			cart.resetShoppingCartItemList();
 96  			cart.setShoppingCartItemList(tmpCart.getShoppingCartItemList());
 97  		}
 98  
 99  		try {
100  			shoppingCartService.priceShoppingCart(cart);
101  			cart.setShoppingCartItemList(dedupeCartItems(cart.getShoppingCartItemList()));
102  		} catch (Exception ex) {
103  			throw ex;
104  		}
105  
106  		return cart;
107  	}
108  
109  	@DELETE
```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/rest/CartEndpoint.java
      * Replace the `javax.inject` import statement with `jakarta.inject`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.rest;
  2  
  3  import java.io.Serializable;
  4  import java.util.ArrayList;
  5  import java.util.HashMap;
  6  import java.util.List;
  7  import java.util.Map;
  8  
  9  import javax.enterprise.context.SessionScoped;
 10  import javax.inject.Inject;
 11  import javax.jms.JMSDestinationDefinition;
 12  import javax.jms.JMSDestinationDefinitions;
 13  import javax.ws.rs.DELETE;
 14  import javax.ws.rs.GET;
 15  import javax.ws.rs.POST;
 16  import javax.ws.rs.Path;
 17  import javax.ws.rs.PathParam;
 18  import javax.ws.rs.Produces;
 19  import javax.ws.rs.core.MediaType;
 20  
 21  import com.redhat.coolstore.model.Product;
 22  import com.redhat.coolstore.model.ShoppingCart;
 23  import com.redhat.coolstore.model.ShoppingCartItem;
 24  import com.redhat.coolstore.service.ShoppingCartService;
 25  
 26  @SessionScoped
 27  @Path("/cart")
 28  @JMSDestinationDefinitions(
 29  	value = {
 30  		@JMSDestinationDefinition(
 31  			name = "java:/jms/queue/orders",
 32  			interfaceName = "javax.jms.Queue",
 33  			destinationName = "ordersQueue"
 34  		)
 35  	}
 36  )
 37  public class CartEndpoint implements Serializable {
 38  
 39  	private static final long serialVersionUID = -7227732980791688773L;
 40  
 41  	@Inject
 42  	private ShoppingCartService shoppingCartService;
 43  
 44  	@GET
 45  	@Path("/{cartId}")
 46  	@Produces(MediaType.APPLICATION_JSON)
 47  	public ShoppingCart getCart(@PathParam("cartId") String cartId) {
 48  		return shoppingCartService.getShoppingCart(cartId);
 49  	}
 50  
 51  	@POST
 52  	@Path("/checkout/{cartId}")
 53  	@Produces(MediaType.APPLICATION_JSON)
 54  	public ShoppingCart checkout(@PathParam("cartId") String cartId) {
 55  		return shoppingCartService.checkOutShoppingCart(cartId);
 56  	}
 57  
 58  	@POST
 59  	@Path("/{cartId}/{itemId}/{quantity}")
 60  	@Produces(MediaType.APPLICATION_JSON)
 61  	public ShoppingCart add(@PathParam("cartId") String cartId,
 62  							@PathParam("itemId") String itemId,
 63  							@PathParam("quantity") int quantity) throws Exception {
 64  		ShoppingCart cart = shoppingCartService.getShoppingCart(cartId);
 65  
 66  		Product product = shoppingCartService.getProduct(itemId);
 67  
 68  		ShoppingCartItem sci = new ShoppingCartItem();
 69  		sci.setProduct(product);
 70  		sci.setQuantity(quantity);
 71  		sci.setPrice(product.getPrice());
 72  		cart.addShoppingCartItem(sci);
 73  
 74  		try {
 75  			shoppingCartService.priceShoppingCart(cart);
 76  			cart.setShoppingCartItemList(dedupeCartItems(cart.getShoppingCartItemList()));
 77  		} catch (Exception ex) {
 78  			cart.removeShoppingCartItem(sci);
 79  			throw ex;
 80  		}
 81  
 82  		return cart;
 83  	}
 84  
 85  	@POST
 86  	@Path("/{cartId}/{tmpId}")
 87  	@Produces(MediaType.APPLICATION_JSON)
 88  	public ShoppingCart set(@PathParam("cartId") String cartId,
 89  							@PathParam("tmpId") String tmpId) throws Exception {
 90  
 91  		ShoppingCart cart = shoppingCartService.getShoppingCart(cartId);
 92  		ShoppingCart tmpCart = shoppingCartService.getShoppingCart(tmpId);
 93  
 94  		if (tmpCart != null) {
 95  			cart.resetShoppingCartItemList();
 96  			cart.setShoppingCartItemList(tmpCart.getShoppingCartItemList());
 97  		}
 98  
 99  		try {
100  			shoppingCartService.priceShoppingCart(cart);
101  			cart.setShoppingCartItemList(dedupeCartItems(cart.getShoppingCartItemList()));
102  		} catch (Exception ex) {
103  			throw ex;
104  		}
105  
106  		return cart;
107  	}
108  
109  	@DELETE
110  	@Path("/{cartId}/{itemId}/{quantity}")
```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/rest/CartEndpoint.java
      * Replace the `javax.jms` import statement with `jakarta.jms`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.rest;
  2  
  3  import java.io.Serializable;
  4  import java.util.ArrayList;
  5  import java.util.HashMap;
  6  import java.util.List;
  7  import java.util.Map;
  8  
  9  import javax.enterprise.context.SessionScoped;
 10  import javax.inject.Inject;
 11  import javax.jms.JMSDestinationDefinition;
 12  import javax.jms.JMSDestinationDefinitions;
 13  import javax.ws.rs.DELETE;
 14  import javax.ws.rs.GET;
 15  import javax.ws.rs.POST;
 16  import javax.ws.rs.Path;
 17  import javax.ws.rs.PathParam;
 18  import javax.ws.rs.Produces;
 19  import javax.ws.rs.core.MediaType;
 20  
 21  import com.redhat.coolstore.model.Product;
 22  import com.redhat.coolstore.model.ShoppingCart;
 23  import com.redhat.coolstore.model.ShoppingCartItem;
 24  import com.redhat.coolstore.service.ShoppingCartService;
 25  
 26  @SessionScoped
 27  @Path("/cart")
 28  @JMSDestinationDefinitions(
 29  	value = {
 30  		@JMSDestinationDefinition(
 31  			name = "java:/jms/queue/orders",
 32  			interfaceName = "javax.jms.Queue",
 33  			destinationName = "ordersQueue"
 34  		)
 35  	}
 36  )
 37  public class CartEndpoint implements Serializable {
 38  
 39  	private static final long serialVersionUID = -7227732980791688773L;
 40  
 41  	@Inject
 42  	private ShoppingCartService shoppingCartService;
 43  
 44  	@GET
 45  	@Path("/{cartId}")
 46  	@Produces(MediaType.APPLICATION_JSON)
 47  	public ShoppingCart getCart(@PathParam("cartId") String cartId) {
 48  		return shoppingCartService.getShoppingCart(cartId);
 49  	}
 50  
 51  	@POST
 52  	@Path("/checkout/{cartId}")
 53  	@Produces(MediaType.APPLICATION_JSON)
 54  	public ShoppingCart checkout(@PathParam("cartId") String cartId) {
 55  		return shoppingCartService.checkOutShoppingCart(cartId);
 56  	}
 57  
 58  	@POST
 59  	@Path("/{cartId}/{itemId}/{quantity}")
 60  	@Produces(MediaType.APPLICATION_JSON)
 61  	public ShoppingCart add(@PathParam("cartId") String cartId,
 62  							@PathParam("itemId") String itemId,
 63  							@PathParam("quantity") int quantity) throws Exception {
 64  		ShoppingCart cart = shoppingCartService.getShoppingCart(cartId);
 65  
 66  		Product product = shoppingCartService.getProduct(itemId);
 67  
 68  		ShoppingCartItem sci = new ShoppingCartItem();
 69  		sci.setProduct(product);
 70  		sci.setQuantity(quantity);
 71  		sci.setPrice(product.getPrice());
 72  		cart.addShoppingCartItem(sci);
 73  
 74  		try {
 75  			shoppingCartService.priceShoppingCart(cart);
 76  			cart.setShoppingCartItemList(dedupeCartItems(cart.getShoppingCartItemList()));
 77  		} catch (Exception ex) {
 78  			cart.removeShoppingCartItem(sci);
 79  			throw ex;
 80  		}
 81  
 82  		return cart;
 83  	}
 84  
 85  	@POST
 86  	@Path("/{cartId}/{tmpId}")
 87  	@Produces(MediaType.APPLICATION_JSON)
 88  	public ShoppingCart set(@PathParam("cartId") String cartId,
 89  							@PathParam("tmpId") String tmpId) throws Exception {
 90  
 91  		ShoppingCart cart = shoppingCartService.getShoppingCart(cartId);
 92  		ShoppingCart tmpCart = shoppingCartService.getShoppingCart(tmpId);
 93  
 94  		if (tmpCart != null) {
 95  			cart.resetShoppingCartItemList();
 96  			cart.setShoppingCartItemList(tmpCart.getShoppingCartItemList());
 97  		}
 98  
 99  		try {
100  			shoppingCartService.priceShoppingCart(cart);
101  			cart.setShoppingCartItemList(dedupeCartItems(cart.getShoppingCartItemList()));
102  		} catch (Exception ex) {
103  			throw ex;
104  		}
105  
106  		return cart;
107  	}
108  
109  	@DELETE
110  	@Path("/{cartId}/{itemId}/{quantity}")
111  	@Produces(MediaType.APPLICATION_JSON)
112  	public ShoppingCart delete(@PathParam("cartId") String cartId,
```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/rest/CartEndpoint.java
      * Replace the `javax.ws` import statement with `jakarta.ws`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.rest;
  2  
  3  import java.io.Serializable;
  4  import java.util.ArrayList;
  5  import java.util.HashMap;
  6  import java.util.List;
  7  import java.util.Map;
  8  
  9  import javax.enterprise.context.SessionScoped;
 10  import javax.inject.Inject;
 11  import javax.jms.JMSDestinationDefinition;
 12  import javax.jms.JMSDestinationDefinitions;
 13  import javax.ws.rs.DELETE;
 14  import javax.ws.rs.GET;
 15  import javax.ws.rs.POST;
 16  import javax.ws.rs.Path;
 17  import javax.ws.rs.PathParam;
 18  import javax.ws.rs.Produces;
 19  import javax.ws.rs.core.MediaType;
 20  
 21  import com.redhat.coolstore.model.Product;
 22  import com.redhat.coolstore.model.ShoppingCart;
 23  import com.redhat.coolstore.model.ShoppingCartItem;
 24  import com.redhat.coolstore.service.ShoppingCartService;
 25  
 26  @SessionScoped
 27  @Path("/cart")
 28  @JMSDestinationDefinitions(
 29  	value = {
 30  		@JMSDestinationDefinition(
 31  			name = "java:/jms/queue/orders",
 32  			interfaceName = "javax.jms.Queue",
 33  			destinationName = "ordersQueue"
 34  		)
 35  	}
 36  )
 37  public class CartEndpoint implements Serializable {
 38  
 39  	private static final long serialVersionUID = -7227732980791688773L;
 40  
 41  	@Inject
 42  	private ShoppingCartService shoppingCartService;
 43  
 44  	@GET
 45  	@Path("/{cartId}")
 46  	@Produces(MediaType.APPLICATION_JSON)
 47  	public ShoppingCart getCart(@PathParam("cartId") String cartId) {
 48  		return shoppingCartService.getShoppingCart(cartId);
 49  	}
 50  
 51  	@POST
 52  	@Path("/checkout/{cartId}")
 53  	@Produces(MediaType.APPLICATION_JSON)
 54  	public ShoppingCart checkout(@PathParam("cartId") String cartId) {
 55  		return shoppingCartService.checkOutShoppingCart(cartId);
 56  	}
 57  
 58  	@POST
 59  	@Path("/{cartId}/{itemId}/{quantity}")
 60  	@Produces(MediaType.APPLICATION_JSON)
 61  	public ShoppingCart add(@PathParam("cartId") String cartId,
 62  							@PathParam("itemId") String itemId,
 63  							@PathParam("quantity") int quantity) throws Exception {
 64  		ShoppingCart cart = shoppingCartService.getShoppingCart(cartId);
 65  
 66  		Product product = shoppingCartService.getProduct(itemId);
 67  
 68  		ShoppingCartItem sci = new ShoppingCartItem();
 69  		sci.setProduct(product);
 70  		sci.setQuantity(quantity);
 71  		sci.setPrice(product.getPrice());
 72  		cart.addShoppingCartItem(sci);
 73  
 74  		try {
 75  			shoppingCartService.priceShoppingCart(cart);
 76  			cart.setShoppingCartItemList(dedupeCartItems(cart.getShoppingCartItemList()));
 77  		} catch (Exception ex) {
 78  			cart.removeShoppingCartItem(sci);
 79  			throw ex;
 80  		}
 81  
 82  		return cart;
 83  	}
 84  
 85  	@POST
 86  	@Path("/{cartId}/{tmpId}")
 87  	@Produces(MediaType.APPLICATION_JSON)
 88  	public ShoppingCart set(@PathParam("cartId") String cartId,
 89  							@PathParam("tmpId") String tmpId) throws Exception {
 90  
 91  		ShoppingCart cart = shoppingCartService.getShoppingCart(cartId);
 92  		ShoppingCart tmpCart = shoppingCartService.getShoppingCart(tmpId);
 93  
 94  		if (tmpCart != null) {
 95  			cart.resetShoppingCartItemList();
 96  			cart.setShoppingCartItemList(tmpCart.getShoppingCartItemList());
 97  		}
 98  
 99  		try {
100  			shoppingCartService.priceShoppingCart(cart);
101  			cart.setShoppingCartItemList(dedupeCartItems(cart.getShoppingCartItemList()));
102  		} catch (Exception ex) {
103  			throw ex;
104  		}
105  
106  		return cart;
107  	}
108  
109  	@DELETE
110  	@Path("/{cartId}/{itemId}/{quantity}")
111  	@Produces(MediaType.APPLICATION_JSON)
112  	public ShoppingCart delete(@PathParam("cartId") String cartId,
113  							   @PathParam("itemId") String itemId,
114  							   @PathParam("quantity") int quantity) throws Exception {
```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/rest/CartEndpoint.java
      * Replace the `javax.ws` import statement with `jakarta.ws`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.rest;
  2  
  3  import java.io.Serializable;
  4  import java.util.ArrayList;
  5  import java.util.HashMap;
  6  import java.util.List;
  7  import java.util.Map;
  8  
  9  import javax.enterprise.context.SessionScoped;
 10  import javax.inject.Inject;
 11  import javax.jms.JMSDestinationDefinition;
 12  import javax.jms.JMSDestinationDefinitions;
 13  import javax.ws.rs.DELETE;
 14  import javax.ws.rs.GET;
 15  import javax.ws.rs.POST;
 16  import javax.ws.rs.Path;
 17  import javax.ws.rs.PathParam;
 18  import javax.ws.rs.Produces;
 19  import javax.ws.rs.core.MediaType;
 20  
 21  import com.redhat.coolstore.model.Product;
 22  import com.redhat.coolstore.model.ShoppingCart;
 23  import com.redhat.coolstore.model.ShoppingCartItem;
 24  import com.redhat.coolstore.service.ShoppingCartService;
 25  
 26  @SessionScoped
 27  @Path("/cart")
 28  @JMSDestinationDefinitions(
 29  	value = {
 30  		@JMSDestinationDefinition(
 31  			name = "java:/jms/queue/orders",
 32  			interfaceName = "javax.jms.Queue",
 33  			destinationName = "ordersQueue"
 34  		)
 35  	}
 36  )
 37  public class CartEndpoint implements Serializable {
 38  
 39  	private static final long serialVersionUID = -7227732980791688773L;
 40  
 41  	@Inject
 42  	private ShoppingCartService shoppingCartService;
 43  
 44  	@GET
 45  	@Path("/{cartId}")
 46  	@Produces(MediaType.APPLICATION_JSON)
 47  	public ShoppingCart getCart(@PathParam("cartId") String cartId) {
 48  		return shoppingCartService.getShoppingCart(cartId);
 49  	}
 50  
 51  	@POST
 52  	@Path("/checkout/{cartId}")
 53  	@Produces(MediaType.APPLICATION_JSON)
 54  	public ShoppingCart checkout(@PathParam("cartId") String cartId) {
 55  		return shoppingCartService.checkOutShoppingCart(cartId);
 56  	}
 57  
 58  	@POST
 59  	@Path("/{cartId}/{itemId}/{quantity}")
 60  	@Produces(MediaType.APPLICATION_JSON)
 61  	public ShoppingCart add(@PathParam("cartId") String cartId,
 62  							@PathParam("itemId") String itemId,
 63  							@PathParam("quantity") int quantity) throws Exception {
 64  		ShoppingCart cart = shoppingCartService.getShoppingCart(cartId);
 65  
 66  		Product product = shoppingCartService.getProduct(itemId);
 67  
 68  		ShoppingCartItem sci = new ShoppingCartItem();
 69  		sci.setProduct(product);
 70  		sci.setQuantity(quantity);
 71  		sci.setPrice(product.getPrice());
 72  		cart.addShoppingCartItem(sci);
 73  
 74  		try {
 75  			shoppingCartService.priceShoppingCart(cart);
 76  			cart.setShoppingCartItemList(dedupeCartItems(cart.getShoppingCartItemList()));
 77  		} catch (Exception ex) {
 78  			cart.removeShoppingCartItem(sci);
 79  			throw ex;
 80  		}
 81  
 82  		return cart;
 83  	}
 84  
 85  	@POST
 86  	@Path("/{cartId}/{tmpId}")
 87  	@Produces(MediaType.APPLICATION_JSON)
 88  	public ShoppingCart set(@PathParam("cartId") String cartId,
 89  							@PathParam("tmpId") String tmpId) throws Exception {
 90  
 91  		ShoppingCart cart = shoppingCartService.getShoppingCart(cartId);
 92  		ShoppingCart tmpCart = shoppingCartService.getShoppingCart(tmpId);
 93  
 94  		if (tmpCart != null) {
 95  			cart.resetShoppingCartItemList();
 96  			cart.setShoppingCartItemList(tmpCart.getShoppingCartItemList());
 97  		}
 98  
 99  		try {
100  			shoppingCartService.priceShoppingCart(cart);
101  			cart.setShoppingCartItemList(dedupeCartItems(cart.getShoppingCartItemList()));
102  		} catch (Exception ex) {
103  			throw ex;
104  		}
105  
106  		return cart;
107  	}
108  
109  	@DELETE
110  	@Path("/{cartId}/{itemId}/{quantity}")
111  	@Produces(MediaType.APPLICATION_JSON)
112  	public ShoppingCart delete(@PathParam("cartId") String cartId,
113  							   @PathParam("itemId") String itemId,
114  							   @PathParam("quantity") int quantity) throws Exception {
115  
116  		List<ShoppingCartItem> toRemoveList = new ArrayList<>();
```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/rest/OrderEndpoint.java
      * Replace the `javax.enterprise` import statement with `jakarta.enterprise`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.rest;
  2  
  3  import java.io.Serializable;
  4  import java.util.List;
  5  
  6  import javax.enterprise.context.RequestScoped;
  7  import javax.inject.Inject;
  8  import javax.ws.rs.Consumes;
  9  import javax.ws.rs.GET;
 10  import javax.ws.rs.Path;
 11  import javax.ws.rs.PathParam;
 12  import javax.ws.rs.Produces;
 13  import javax.ws.rs.core.MediaType;
 14  
 15  import com.redhat.coolstore.model.Order;
 16  import com.redhat.coolstore.service.OrderService;
 17  
 18  @RequestScoped
 19  @Path("/orders")
 20  @Consumes(MediaType.APPLICATION_JSON)
 21  @Produces(MediaType.APPLICATION_JSON)
 22  public class OrderEndpoint implements Serializable {
 23  
 24      private static final long serialVersionUID = -7227732980791688774L;
 25  
 26      @Inject
 27      private OrderService os;
 28  
 29  
 30      @GET
 31      @Path("/")
 32      public List<Order> listAll() {
 33          return os.getOrders();
 34      }
 35  
 36      @GET
 37      @Path("/{orderId}")
 38      public Order getOrder(@PathParam("orderId") long orderId) {
 39          return os.getOrderById(orderId);
 40      }
 41  
 42  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/rest/OrderEndpoint.java
      * Replace the `javax.ws` import statement with `jakarta.ws`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.rest;
  2  
  3  import java.io.Serializable;
  4  import java.util.List;
  5  
  6  import javax.enterprise.context.RequestScoped;
  7  import javax.inject.Inject;
  8  import javax.ws.rs.Consumes;
  9  import javax.ws.rs.GET;
 10  import javax.ws.rs.Path;
 11  import javax.ws.rs.PathParam;
 12  import javax.ws.rs.Produces;
 13  import javax.ws.rs.core.MediaType;
 14  
 15  import com.redhat.coolstore.model.Order;
 16  import com.redhat.coolstore.service.OrderService;
 17  
 18  @RequestScoped
 19  @Path("/orders")
 20  @Consumes(MediaType.APPLICATION_JSON)
 21  @Produces(MediaType.APPLICATION_JSON)
 22  public class OrderEndpoint implements Serializable {
 23  
 24      private static final long serialVersionUID = -7227732980791688774L;
 25  
 26      @Inject
 27      private OrderService os;
 28  
 29  
 30      @GET
 31      @Path("/")
 32      public List<Order> listAll() {
 33          return os.getOrders();
 34      }
 35  
 36      @GET
 37      @Path("/{orderId}")
 38      public Order getOrder(@PathParam("orderId") long orderId) {
 39          return os.getOrderById(orderId);
 40      }
 41  
 42  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/rest/OrderEndpoint.java
      * Replace the `javax.inject` import statement with `jakarta.inject`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.rest;
  2  
  3  import java.io.Serializable;
  4  import java.util.List;
  5  
  6  import javax.enterprise.context.RequestScoped;
  7  import javax.inject.Inject;
  8  import javax.ws.rs.Consumes;
  9  import javax.ws.rs.GET;
 10  import javax.ws.rs.Path;
 11  import javax.ws.rs.PathParam;
 12  import javax.ws.rs.Produces;
 13  import javax.ws.rs.core.MediaType;
 14  
 15  import com.redhat.coolstore.model.Order;
 16  import com.redhat.coolstore.service.OrderService;
 17  
 18  @RequestScoped
 19  @Path("/orders")
 20  @Consumes(MediaType.APPLICATION_JSON)
 21  @Produces(MediaType.APPLICATION_JSON)
 22  public class OrderEndpoint implements Serializable {
 23  
 24      private static final long serialVersionUID = -7227732980791688774L;
 25  
 26      @Inject
 27      private OrderService os;
 28  
 29  
 30      @GET
 31      @Path("/")
 32      public List<Order> listAll() {
 33          return os.getOrders();
 34      }
 35  
 36      @GET
 37      @Path("/{orderId}")
 38      public Order getOrder(@PathParam("orderId") long orderId) {
 39          return os.getOrderById(orderId);
 40      }
 41  
 42  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/rest/OrderEndpoint.java
      * Replace the `javax.ws` import statement with `jakarta.ws`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.rest;
  2  
  3  import java.io.Serializable;
  4  import java.util.List;
  5  
  6  import javax.enterprise.context.RequestScoped;
  7  import javax.inject.Inject;
  8  import javax.ws.rs.Consumes;
  9  import javax.ws.rs.GET;
 10  import javax.ws.rs.Path;
 11  import javax.ws.rs.PathParam;
 12  import javax.ws.rs.Produces;
 13  import javax.ws.rs.core.MediaType;
 14  
 15  import com.redhat.coolstore.model.Order;
 16  import com.redhat.coolstore.service.OrderService;
 17  
 18  @RequestScoped
 19  @Path("/orders")
 20  @Consumes(MediaType.APPLICATION_JSON)
 21  @Produces(MediaType.APPLICATION_JSON)
 22  public class OrderEndpoint implements Serializable {
 23  
 24      private static final long serialVersionUID = -7227732980791688774L;
 25  
 26      @Inject
 27      private OrderService os;
 28  
 29  
 30      @GET
 31      @Path("/")
 32      public List<Order> listAll() {
 33          return os.getOrders();
 34      }
 35  
 36      @GET
 37      @Path("/{orderId}")
 38      public Order getOrder(@PathParam("orderId") long orderId) {
 39          return os.getOrderById(orderId);
 40      }
 41  
 42  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/rest/OrderEndpoint.java
      * Replace the `javax.ws` import statement with `jakarta.ws`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.rest;
  2  
  3  import java.io.Serializable;
  4  import java.util.List;
  5  
  6  import javax.enterprise.context.RequestScoped;
  7  import javax.inject.Inject;
  8  import javax.ws.rs.Consumes;
  9  import javax.ws.rs.GET;
 10  import javax.ws.rs.Path;
 11  import javax.ws.rs.PathParam;
 12  import javax.ws.rs.Produces;
 13  import javax.ws.rs.core.MediaType;
 14  
 15  import com.redhat.coolstore.model.Order;
 16  import com.redhat.coolstore.service.OrderService;
 17  
 18  @RequestScoped
 19  @Path("/orders")
 20  @Consumes(MediaType.APPLICATION_JSON)
 21  @Produces(MediaType.APPLICATION_JSON)
 22  public class OrderEndpoint implements Serializable {
 23  
 24      private static final long serialVersionUID = -7227732980791688774L;
 25  
 26      @Inject
 27      private OrderService os;
 28  
 29  
 30      @GET
 31      @Path("/")
 32      public List<Order> listAll() {
 33          return os.getOrders();
 34      }
 35  
 36      @GET
 37      @Path("/{orderId}")
 38      public Order getOrder(@PathParam("orderId") long orderId) {
 39          return os.getOrderById(orderId);
 40      }
 41  
 42  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/rest/OrderEndpoint.java
      * Replace the `javax.ws` import statement with `jakarta.ws`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.rest;
  2  
  3  import java.io.Serializable;
  4  import java.util.List;
  5  
  6  import javax.enterprise.context.RequestScoped;
  7  import javax.inject.Inject;
  8  import javax.ws.rs.Consumes;
  9  import javax.ws.rs.GET;
 10  import javax.ws.rs.Path;
 11  import javax.ws.rs.PathParam;
 12  import javax.ws.rs.Produces;
 13  import javax.ws.rs.core.MediaType;
 14  
 15  import com.redhat.coolstore.model.Order;
 16  import com.redhat.coolstore.service.OrderService;
 17  
 18  @RequestScoped
 19  @Path("/orders")
 20  @Consumes(MediaType.APPLICATION_JSON)
 21  @Produces(MediaType.APPLICATION_JSON)
 22  public class OrderEndpoint implements Serializable {
 23  
 24      private static final long serialVersionUID = -7227732980791688774L;
 25  
 26      @Inject
 27      private OrderService os;
 28  
 29  
 30      @GET
 31      @Path("/")
 32      public List<Order> listAll() {
 33          return os.getOrders();
 34      }
 35  
 36      @GET
 37      @Path("/{orderId}")
 38      public Order getOrder(@PathParam("orderId") long orderId) {
 39          return os.getOrderById(orderId);
 40      }
 41  
 42  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/rest/OrderEndpoint.java
      * Replace the `javax.ws` import statement with `jakarta.ws`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.rest;
  2  
  3  import java.io.Serializable;
  4  import java.util.List;
  5  
  6  import javax.enterprise.context.RequestScoped;
  7  import javax.inject.Inject;
  8  import javax.ws.rs.Consumes;
  9  import javax.ws.rs.GET;
 10  import javax.ws.rs.Path;
 11  import javax.ws.rs.PathParam;
 12  import javax.ws.rs.Produces;
 13  import javax.ws.rs.core.MediaType;
 14  
 15  import com.redhat.coolstore.model.Order;
 16  import com.redhat.coolstore.service.OrderService;
 17  
 18  @RequestScoped
 19  @Path("/orders")
 20  @Consumes(MediaType.APPLICATION_JSON)
 21  @Produces(MediaType.APPLICATION_JSON)
 22  public class OrderEndpoint implements Serializable {
 23  
 24      private static final long serialVersionUID = -7227732980791688774L;
 25  
 26      @Inject
 27      private OrderService os;
 28  
 29  
 30      @GET
 31      @Path("/")
 32      public List<Order> listAll() {
 33          return os.getOrders();
 34      }
 35  
 36      @GET
 37      @Path("/{orderId}")
 38      public Order getOrder(@PathParam("orderId") long orderId) {
 39          return os.getOrderById(orderId);
 40      }
 41  
 42  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/rest/OrderEndpoint.java
      * Replace the `javax.ws` import statement with `jakarta.ws`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.rest;
  2  
  3  import java.io.Serializable;
  4  import java.util.List;
  5  
  6  import javax.enterprise.context.RequestScoped;
  7  import javax.inject.Inject;
  8  import javax.ws.rs.Consumes;
  9  import javax.ws.rs.GET;
 10  import javax.ws.rs.Path;
 11  import javax.ws.rs.PathParam;
 12  import javax.ws.rs.Produces;
 13  import javax.ws.rs.core.MediaType;
 14  
 15  import com.redhat.coolstore.model.Order;
 16  import com.redhat.coolstore.service.OrderService;
 17  
 18  @RequestScoped
 19  @Path("/orders")
 20  @Consumes(MediaType.APPLICATION_JSON)
 21  @Produces(MediaType.APPLICATION_JSON)
 22  public class OrderEndpoint implements Serializable {
 23  
 24      private static final long serialVersionUID = -7227732980791688774L;
 25  
 26      @Inject
 27      private OrderService os;
 28  
 29  
 30      @GET
 31      @Path("/")
 32      public List<Order> listAll() {
 33          return os.getOrders();
 34      }
 35  
 36      @GET
 37      @Path("/{orderId}")
 38      public Order getOrder(@PathParam("orderId") long orderId) {
 39          return os.getOrderById(orderId);
 40      }
 41  
 42  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/rest/ProductEndpoint.java
      * Replace the `javax.enterprise` import statement with `jakarta.enterprise`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.rest;
  2  
  3  import java.io.Serializable;
  4  import java.util.List;
  5  
  6  import javax.enterprise.context.RequestScoped;
  7  import javax.inject.Inject;
  8  import javax.ws.rs.*;
  9  import javax.ws.rs.core.MediaType;
 10  
 11  import com.redhat.coolstore.model.Product;
 12  import com.redhat.coolstore.service.ProductService;
 13  
 14  @RequestScoped
 15  @Path("/products")
 16  @Consumes(MediaType.APPLICATION_JSON)
 17  @Produces(MediaType.APPLICATION_JSON)
 18  public class ProductEndpoint implements Serializable {
 19  
 20      /**
 21       *
 22       */
 23      private static final long serialVersionUID = -7227732980791688773L;
 24  
 25      @Inject
 26      private ProductService pm;
 27  
 28  
 29      @GET
 30      @Path("/")
 31      public List<Product> listAll() {
 32          return pm.getProducts();
 33      }
 34  
 35      @GET
 36      @Path("/{itemId}")
 37      public Product getProduct(@PathParam("itemId") String itemId) {
 38          return pm.getProductByItemId(itemId);
 39      }
 40  
 41  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/rest/ProductEndpoint.java
      * Replace the `javax.ws` import statement with `jakarta.ws`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.rest;
  2  
  3  import java.io.Serializable;
  4  import java.util.List;
  5  
  6  import javax.enterprise.context.RequestScoped;
  7  import javax.inject.Inject;
  8  import javax.ws.rs.*;
  9  import javax.ws.rs.core.MediaType;
 10  
 11  import com.redhat.coolstore.model.Product;
 12  import com.redhat.coolstore.service.ProductService;
 13  
 14  @RequestScoped
 15  @Path("/products")
 16  @Consumes(MediaType.APPLICATION_JSON)
 17  @Produces(MediaType.APPLICATION_JSON)
 18  public class ProductEndpoint implements Serializable {
 19  
 20      /**
 21       *
 22       */
 23      private static final long serialVersionUID = -7227732980791688773L;
 24  
 25      @Inject
 26      private ProductService pm;
 27  
 28  
 29      @GET
 30      @Path("/")
 31      public List<Product> listAll() {
 32          return pm.getProducts();
 33      }
 34  
 35      @GET
 36      @Path("/{itemId}")
 37      public Product getProduct(@PathParam("itemId") String itemId) {
 38          return pm.getProductByItemId(itemId);
 39      }
 40  
 41  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/rest/ProductEndpoint.java
      * Replace the `javax.inject` import statement with `jakarta.inject`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.rest;
  2  
  3  import java.io.Serializable;
  4  import java.util.List;
  5  
  6  import javax.enterprise.context.RequestScoped;
  7  import javax.inject.Inject;
  8  import javax.ws.rs.*;
  9  import javax.ws.rs.core.MediaType;
 10  
 11  import com.redhat.coolstore.model.Product;
 12  import com.redhat.coolstore.service.ProductService;
 13  
 14  @RequestScoped
 15  @Path("/products")
 16  @Consumes(MediaType.APPLICATION_JSON)
 17  @Produces(MediaType.APPLICATION_JSON)
 18  public class ProductEndpoint implements Serializable {
 19  
 20      /**
 21       *
 22       */
 23      private static final long serialVersionUID = -7227732980791688773L;
 24  
 25      @Inject
 26      private ProductService pm;
 27  
 28  
 29      @GET
 30      @Path("/")
 31      public List<Product> listAll() {
 32          return pm.getProducts();
 33      }
 34  
 35      @GET
 36      @Path("/{itemId}")
 37      public Product getProduct(@PathParam("itemId") String itemId) {
 38          return pm.getProductByItemId(itemId);
 39      }
 40  
 41  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/rest/RestApplication.java
      * Replace the `javax.ws` import statement with `jakarta.ws`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.rest;
  2  
  3  import javax.ws.rs.ApplicationPath;
  4  import javax.ws.rs.core.Application;
  5  
  6  
  7  @ApplicationPath("/services")
  8  public class RestApplication extends Application {
  9  
 10  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/rest/RestApplication.java
      * Replace the `javax.ws` import statement with `jakarta.ws`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.rest;
  2  
  3  import javax.ws.rs.ApplicationPath;
  4  import javax.ws.rs.core.Application;
  5  
  6  
  7  @ApplicationPath("/services")
  8  public class RestApplication extends Application {
  9  
 10  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/service/CatalogService.java
      * Replace the `javax.persistence` import statement with `jakarta.persistence`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.service;
  2  
  3  import java.util.List;
  4  import java.util.logging.Logger;
  5  
  6  import javax.inject.Inject;
  7  
  8  import javax.persistence.criteria.CriteriaBuilder;
  9  import javax.persistence.criteria.CriteriaQuery;
 10  import javax.persistence.criteria.Root;
 11  
 12  import javax.ejb.Stateless;
 13  import javax.persistence.EntityManager;
 14  import javax.persistence.PersistenceContext;
 15  
 16  import com.redhat.coolstore.model.*;
 17  
 18  @Stateless
 19  public class CatalogService {
 20  
 21      @Inject
 22      Logger log;
 23  
 24      @PersistenceContext
 25      private EntityManager em;
 26  
 27      public CatalogService() {
 28      }
 29  
 30      public List<CatalogItemEntity> getCatalogItems() {
 31          CriteriaBuilder cb = em.getCriteriaBuilder();
 32          CriteriaQuery<CatalogItemEntity> criteria = cb.createQuery(CatalogItemEntity.class);
 33          Root<CatalogItemEntity> member = criteria.from(CatalogItemEntity.class);
 34          criteria.select(member);
 35          return em.createQuery(criteria).getResultList();
 36      }
 37  
 38      public CatalogItemEntity getCatalogItemById(String itemId) {
 39          return em.find(CatalogItemEntity.class, itemId);
 40      }
 41  
 42      public void updateInventoryItems(String itemId, int deducts) {
 43          InventoryEntity inventoryEntity = getCatalogItemById(itemId).getInventory();
 44          int currentQuantity = inventoryEntity.getQuantity();
 45          inventoryEntity.setQuantity(currentQuantity-deducts);
 46          em.merge(inventoryEntity);
 47      }
 48  
 49  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/service/CatalogService.java
      * Replace the `javax.ejb` import statement with `jakarta.ejb`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.service;
  2  
  3  import java.util.List;
  4  import java.util.logging.Logger;
  5  
  6  import javax.inject.Inject;
  7  
  8  import javax.persistence.criteria.CriteriaBuilder;
  9  import javax.persistence.criteria.CriteriaQuery;
 10  import javax.persistence.criteria.Root;
 11  
 12  import javax.ejb.Stateless;
 13  import javax.persistence.EntityManager;
 14  import javax.persistence.PersistenceContext;
 15  
 16  import com.redhat.coolstore.model.*;
 17  
 18  @Stateless
 19  public class CatalogService {
 20  
 21      @Inject
 22      Logger log;
 23  
 24      @PersistenceContext
 25      private EntityManager em;
 26  
 27      public CatalogService() {
 28      }
 29  
 30      public List<CatalogItemEntity> getCatalogItems() {
 31          CriteriaBuilder cb = em.getCriteriaBuilder();
 32          CriteriaQuery<CatalogItemEntity> criteria = cb.createQuery(CatalogItemEntity.class);
 33          Root<CatalogItemEntity> member = criteria.from(CatalogItemEntity.class);
 34          criteria.select(member);
 35          return em.createQuery(criteria).getResultList();
 36      }
 37  
 38      public CatalogItemEntity getCatalogItemById(String itemId) {
 39          return em.find(CatalogItemEntity.class, itemId);
 40      }
 41  
 42      public void updateInventoryItems(String itemId, int deducts) {
 43          InventoryEntity inventoryEntity = getCatalogItemById(itemId).getInventory();
 44          int currentQuantity = inventoryEntity.getQuantity();
 45          inventoryEntity.setQuantity(currentQuantity-deducts);
 46          em.merge(inventoryEntity);
 47      }
 48  
 49  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/service/CatalogService.java
      * Replace the `javax.persistence` import statement with `jakarta.persistence`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.service;
  2  
  3  import java.util.List;
  4  import java.util.logging.Logger;
  5  
  6  import javax.inject.Inject;
  7  
  8  import javax.persistence.criteria.CriteriaBuilder;
  9  import javax.persistence.criteria.CriteriaQuery;
 10  import javax.persistence.criteria.Root;
 11  
 12  import javax.ejb.Stateless;
 13  import javax.persistence.EntityManager;
 14  import javax.persistence.PersistenceContext;
 15  
 16  import com.redhat.coolstore.model.*;
 17  
 18  @Stateless
 19  public class CatalogService {
 20  
 21      @Inject
 22      Logger log;
 23  
 24      @PersistenceContext
 25      private EntityManager em;
 26  
 27      public CatalogService() {
 28      }
 29  
 30      public List<CatalogItemEntity> getCatalogItems() {
 31          CriteriaBuilder cb = em.getCriteriaBuilder();
 32          CriteriaQuery<CatalogItemEntity> criteria = cb.createQuery(CatalogItemEntity.class);
 33          Root<CatalogItemEntity> member = criteria.from(CatalogItemEntity.class);
 34          criteria.select(member);
 35          return em.createQuery(criteria).getResultList();
 36      }
 37  
 38      public CatalogItemEntity getCatalogItemById(String itemId) {
 39          return em.find(CatalogItemEntity.class, itemId);
 40      }
 41  
 42      public void updateInventoryItems(String itemId, int deducts) {
 43          InventoryEntity inventoryEntity = getCatalogItemById(itemId).getInventory();
 44          int currentQuantity = inventoryEntity.getQuantity();
 45          inventoryEntity.setQuantity(currentQuantity-deducts);
 46          em.merge(inventoryEntity);
 47      }
 48  
 49  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/service/CatalogService.java
      * Replace the `javax.persistence` import statement with `jakarta.persistence`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.service;
  2  
  3  import java.util.List;
  4  import java.util.logging.Logger;
  5  
  6  import javax.inject.Inject;
  7  
  8  import javax.persistence.criteria.CriteriaBuilder;
  9  import javax.persistence.criteria.CriteriaQuery;
 10  import javax.persistence.criteria.Root;
 11  
 12  import javax.ejb.Stateless;
 13  import javax.persistence.EntityManager;
 14  import javax.persistence.PersistenceContext;
 15  
 16  import com.redhat.coolstore.model.*;
 17  
 18  @Stateless
 19  public class CatalogService {
 20  
 21      @Inject
 22      Logger log;
 23  
 24      @PersistenceContext
 25      private EntityManager em;
 26  
 27      public CatalogService() {
 28      }
 29  
 30      public List<CatalogItemEntity> getCatalogItems() {
 31          CriteriaBuilder cb = em.getCriteriaBuilder();
 32          CriteriaQuery<CatalogItemEntity> criteria = cb.createQuery(CatalogItemEntity.class);
 33          Root<CatalogItemEntity> member = criteria.from(CatalogItemEntity.class);
 34          criteria.select(member);
 35          return em.createQuery(criteria).getResultList();
 36      }
 37  
 38      public CatalogItemEntity getCatalogItemById(String itemId) {
 39          return em.find(CatalogItemEntity.class, itemId);
 40      }
 41  
 42      public void updateInventoryItems(String itemId, int deducts) {
 43          InventoryEntity inventoryEntity = getCatalogItemById(itemId).getInventory();
 44          int currentQuantity = inventoryEntity.getQuantity();
 45          inventoryEntity.setQuantity(currentQuantity-deducts);
 46          em.merge(inventoryEntity);
 47      }
 48  
 49  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/service/CatalogService.java
      * Replace the `javax.inject` import statement with `jakarta.inject`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.service;
  2  
  3  import java.util.List;
  4  import java.util.logging.Logger;
  5  
  6  import javax.inject.Inject;
  7  
  8  import javax.persistence.criteria.CriteriaBuilder;
  9  import javax.persistence.criteria.CriteriaQuery;
 10  import javax.persistence.criteria.Root;
 11  
 12  import javax.ejb.Stateless;
 13  import javax.persistence.EntityManager;
 14  import javax.persistence.PersistenceContext;
 15  
 16  import com.redhat.coolstore.model.*;
 17  
 18  @Stateless
 19  public class CatalogService {
 20  
 21      @Inject
 22      Logger log;
 23  
 24      @PersistenceContext
 25      private EntityManager em;
 26  
 27      public CatalogService() {
 28      }
 29  
 30      public List<CatalogItemEntity> getCatalogItems() {
 31          CriteriaBuilder cb = em.getCriteriaBuilder();
 32          CriteriaQuery<CatalogItemEntity> criteria = cb.createQuery(CatalogItemEntity.class);
 33          Root<CatalogItemEntity> member = criteria.from(CatalogItemEntity.class);
 34          criteria.select(member);
 35          return em.createQuery(criteria).getResultList();
 36      }
 37  
 38      public CatalogItemEntity getCatalogItemById(String itemId) {
 39          return em.find(CatalogItemEntity.class, itemId);
 40      }
 41  
 42      public void updateInventoryItems(String itemId, int deducts) {
 43          InventoryEntity inventoryEntity = getCatalogItemById(itemId).getInventory();
 44          int currentQuantity = inventoryEntity.getQuantity();
 45          inventoryEntity.setQuantity(currentQuantity-deducts);
 46          em.merge(inventoryEntity);
 47      }
 48  
 49  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/service/CatalogService.java
      * Replace the `javax.persistence` import statement with `jakarta.persistence`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.service;
  2  
  3  import java.util.List;
  4  import java.util.logging.Logger;
  5  
  6  import javax.inject.Inject;
  7  
  8  import javax.persistence.criteria.CriteriaBuilder;
  9  import javax.persistence.criteria.CriteriaQuery;
 10  import javax.persistence.criteria.Root;
 11  
 12  import javax.ejb.Stateless;
 13  import javax.persistence.EntityManager;
 14  import javax.persistence.PersistenceContext;
 15  
 16  import com.redhat.coolstore.model.*;
 17  
 18  @Stateless
 19  public class CatalogService {
 20  
 21      @Inject
 22      Logger log;
 23  
 24      @PersistenceContext
 25      private EntityManager em;
 26  
 27      public CatalogService() {
 28      }
 29  
 30      public List<CatalogItemEntity> getCatalogItems() {
 31          CriteriaBuilder cb = em.getCriteriaBuilder();
 32          CriteriaQuery<CatalogItemEntity> criteria = cb.createQuery(CatalogItemEntity.class);
 33          Root<CatalogItemEntity> member = criteria.from(CatalogItemEntity.class);
 34          criteria.select(member);
 35          return em.createQuery(criteria).getResultList();
 36      }
 37  
 38      public CatalogItemEntity getCatalogItemById(String itemId) {
 39          return em.find(CatalogItemEntity.class, itemId);
 40      }
 41  
 42      public void updateInventoryItems(String itemId, int deducts) {
 43          InventoryEntity inventoryEntity = getCatalogItemById(itemId).getInventory();
 44          int currentQuantity = inventoryEntity.getQuantity();
 45          inventoryEntity.setQuantity(currentQuantity-deducts);
 46          em.merge(inventoryEntity);
 47      }
 48  
 49  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/service/CatalogService.java
      * Replace the `javax.persistence` import statement with `jakarta.persistence`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.service;
  2  
  3  import java.util.List;
  4  import java.util.logging.Logger;
  5  
  6  import javax.inject.Inject;
  7  
  8  import javax.persistence.criteria.CriteriaBuilder;
  9  import javax.persistence.criteria.CriteriaQuery;
 10  import javax.persistence.criteria.Root;
 11  
 12  import javax.ejb.Stateless;
 13  import javax.persistence.EntityManager;
 14  import javax.persistence.PersistenceContext;
 15  
 16  import com.redhat.coolstore.model.*;
 17  
 18  @Stateless
 19  public class CatalogService {
 20  
 21      @Inject
 22      Logger log;
 23  
 24      @PersistenceContext
 25      private EntityManager em;
 26  
 27      public CatalogService() {
 28      }
 29  
 30      public List<CatalogItemEntity> getCatalogItems() {
 31          CriteriaBuilder cb = em.getCriteriaBuilder();
 32          CriteriaQuery<CatalogItemEntity> criteria = cb.createQuery(CatalogItemEntity.class);
 33          Root<CatalogItemEntity> member = criteria.from(CatalogItemEntity.class);
 34          criteria.select(member);
 35          return em.createQuery(criteria).getResultList();
 36      }
 37  
 38      public CatalogItemEntity getCatalogItemById(String itemId) {
 39          return em.find(CatalogItemEntity.class, itemId);
 40      }
 41  
 42      public void updateInventoryItems(String itemId, int deducts) {
 43          InventoryEntity inventoryEntity = getCatalogItemById(itemId).getInventory();
 44          int currentQuantity = inventoryEntity.getQuantity();
 45          inventoryEntity.setQuantity(currentQuantity-deducts);
 46          em.merge(inventoryEntity);
 47      }
 48  
 49  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/service/InventoryNotificationMDB.java
      * Replace the `javax.inject` import statement with `jakarta.inject`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.service;
  2  
  3  import com.redhat.coolstore.model.Order;
  4  import com.redhat.coolstore.utils.Transformers;
  5  
  6  import javax.inject.Inject;
  7  import javax.jms.*;
  8  import javax.naming.Context;
  9  import javax.naming.InitialContext;
 10  import javax.naming.NamingException;
 11  import javax.rmi.PortableRemoteObject;
 12  import java.util.Hashtable;
 13  import java.util.logging.Logger;
 14  
 15  public class InventoryNotificationMDB implements MessageListener {
 16  
 17      private static final int LOW_THRESHOLD = 50;
 18  
 19      @Inject
 20      private CatalogService catalogService;
 21  
 22      @Inject
 23      private Logger log;
 24  
 25      private final static String JNDI_FACTORY = "weblogic.jndi.WLInitialContextFactory";
 26      private final static String JMS_FACTORY = "TCF";
 27      private final static String TOPIC = "topic/orders";
 28      private TopicConnection tcon;
 29      private TopicSession tsession;
 30      private TopicSubscriber tsubscriber;
 31  
 32      public void onMessage(Message rcvMessage) {
 33          TextMessage msg;
 34          {
 35              try {
 36                  System.out.println("received message inventory");
 37                  if (rcvMessage instanceof TextMessage) {
 38                      msg = (TextMessage) rcvMessage;
 39                      String orderStr = msg.getBody(String.class);
 40                      Order order = Transformers.jsonToOrder(orderStr);
 41                      order.getItemList().forEach(orderItem -> {
 42                          int old_quantity = catalogService.getCatalogItemById(orderItem.getProductId()).getInventory().getQuantity();
 43                          int new_quantity = old_quantity - orderItem.getQuantity();
 44                          if (new_quantity < LOW_THRESHOLD) {
 45                              System.out.println("Inventory for item " + orderItem.getProductId() + " is below threshold (" + LOW_THRESHOLD + "), contact supplier!");
 46                          } else {
 47                              orderItem.setQuantity(new_quantity);
 48                          }
 49                      });
 50                  }
 51  
 52  
 53              } catch (JMSException jmse) {
 54                  System.err.println("An exception occurred: " + jmse.getMessage());
 55              }
 56          }
 57      }
 58  
 59      public void init() throws NamingException, JMSException {
 60          Context ctx = getInitialContext();
 61          TopicConnectionFactory tconFactory = (TopicConnectionFactory) PortableRemoteObject.narrow(ctx.lookup(JMS_FACTORY), TopicConnectionFactory.class);
 62          tcon = tconFactory.createTopicConnection();
 63          tsession = tcon.createTopicSession(false, Session.AUTO_ACKNOWLEDGE);
 64          Topic topic = (Topic) PortableRemoteObject.narrow(ctx.lookup(TOPIC), Topic.class);
 65          tsubscriber = tsession.createSubscriber(topic);
 66          tsubscriber.setMessageListener(this);
 67          tcon.start();
 68      }
 69  
 70      public void close() throws JMSException {
 71          tsubscriber.close();
 72          tsession.close();
 73          tcon.close();
 74      }
 75  
 76      private static InitialContext getInitialContext() throws NamingException {
 77          Hashtable<String, String> env = new Hashtable<>();
 78          env.put(Context.INITIAL_CONTEXT_FACTORY, JNDI_FACTORY);
 79          env.put(Context.PROVIDER_URL, "t3://localhost:7001");
 80          env.put("weblogic.jndi.createIntermediateContexts", "true");
 81          return new InitialContext(env);
 82      }
 83  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/service/OrderService.java
      * Replace the `javax.ejb` import statement with `jakarta.ejb`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.service;
  2  
  3  import com.redhat.coolstore.model.Order;
  4  import java.util.List;
  5  import javax.ejb.Stateless;
  6  import javax.persistence.EntityManager;
  7  import javax.persistence.PersistenceContext;
  8  import javax.persistence.criteria.CriteriaBuilder;
  9  import javax.persistence.criteria.CriteriaQuery;
 10  import javax.persistence.criteria.Root;
 11  
 12  @Stateless
 13  public class OrderService {
 14  
 15    @PersistenceContext
 16    private EntityManager em;
 17  
 18    public void save(Order order) {
 19      em.persist(order);
 20    }
 21  
 22    public List<Order> getOrders() {
 23      CriteriaBuilder cb = em.getCriteriaBuilder();
 24      CriteriaQuery<Order> criteria = cb.createQuery(Order.class);
 25      Root<Order> member = criteria.from(Order.class);
 26      criteria.select(member);
 27      return em.createQuery(criteria).getResultList();
 28    }
 29  
 30    public Order getOrderById(long id) {
 31      return em.find(Order.class, id);
 32    }
 33  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/service/OrderService.java
      * Replace the `javax.persistence` import statement with `jakarta.persistence`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.service;
  2  
  3  import com.redhat.coolstore.model.Order;
  4  import java.util.List;
  5  import javax.ejb.Stateless;
  6  import javax.persistence.EntityManager;
  7  import javax.persistence.PersistenceContext;
  8  import javax.persistence.criteria.CriteriaBuilder;
  9  import javax.persistence.criteria.CriteriaQuery;
 10  import javax.persistence.criteria.Root;
 11  
 12  @Stateless
 13  public class OrderService {
 14  
 15    @PersistenceContext
 16    private EntityManager em;
 17  
 18    public void save(Order order) {
 19      em.persist(order);
 20    }
 21  
 22    public List<Order> getOrders() {
 23      CriteriaBuilder cb = em.getCriteriaBuilder();
 24      CriteriaQuery<Order> criteria = cb.createQuery(Order.class);
 25      Root<Order> member = criteria.from(Order.class);
 26      criteria.select(member);
 27      return em.createQuery(criteria).getResultList();
 28    }
 29  
 30    public Order getOrderById(long id) {
 31      return em.find(Order.class, id);
 32    }
 33  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/service/OrderService.java
      * Replace the `javax.persistence` import statement with `jakarta.persistence`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.service;
  2  
  3  import com.redhat.coolstore.model.Order;
  4  import java.util.List;
  5  import javax.ejb.Stateless;
  6  import javax.persistence.EntityManager;
  7  import javax.persistence.PersistenceContext;
  8  import javax.persistence.criteria.CriteriaBuilder;
  9  import javax.persistence.criteria.CriteriaQuery;
 10  import javax.persistence.criteria.Root;
 11  
 12  @Stateless
 13  public class OrderService {
 14  
 15    @PersistenceContext
 16    private EntityManager em;
 17  
 18    public void save(Order order) {
 19      em.persist(order);
 20    }
 21  
 22    public List<Order> getOrders() {
 23      CriteriaBuilder cb = em.getCriteriaBuilder();
 24      CriteriaQuery<Order> criteria = cb.createQuery(Order.class);
 25      Root<Order> member = criteria.from(Order.class);
 26      criteria.select(member);
 27      return em.createQuery(criteria).getResultList();
 28    }
 29  
 30    public Order getOrderById(long id) {
 31      return em.find(Order.class, id);
 32    }
 33  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/service/OrderService.java
      * Replace the `javax.persistence` import statement with `jakarta.persistence`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.service;
  2  
  3  import com.redhat.coolstore.model.Order;
  4  import java.util.List;
  5  import javax.ejb.Stateless;
  6  import javax.persistence.EntityManager;
  7  import javax.persistence.PersistenceContext;
  8  import javax.persistence.criteria.CriteriaBuilder;
  9  import javax.persistence.criteria.CriteriaQuery;
 10  import javax.persistence.criteria.Root;
 11  
 12  @Stateless
 13  public class OrderService {
 14  
 15    @PersistenceContext
 16    private EntityManager em;
 17  
 18    public void save(Order order) {
 19      em.persist(order);
 20    }
 21  
 22    public List<Order> getOrders() {
 23      CriteriaBuilder cb = em.getCriteriaBuilder();
 24      CriteriaQuery<Order> criteria = cb.createQuery(Order.class);
 25      Root<Order> member = criteria.from(Order.class);
 26      criteria.select(member);
 27      return em.createQuery(criteria).getResultList();
 28    }
 29  
 30    public Order getOrderById(long id) {
 31      return em.find(Order.class, id);
 32    }
 33  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/service/OrderService.java
      * Replace the `javax.persistence` import statement with `jakarta.persistence`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.service;
  2  
  3  import com.redhat.coolstore.model.Order;
  4  import java.util.List;
  5  import javax.ejb.Stateless;
  6  import javax.persistence.EntityManager;
  7  import javax.persistence.PersistenceContext;
  8  import javax.persistence.criteria.CriteriaBuilder;
  9  import javax.persistence.criteria.CriteriaQuery;
 10  import javax.persistence.criteria.Root;
 11  
 12  @Stateless
 13  public class OrderService {
 14  
 15    @PersistenceContext
 16    private EntityManager em;
 17  
 18    public void save(Order order) {
 19      em.persist(order);
 20    }
 21  
 22    public List<Order> getOrders() {
 23      CriteriaBuilder cb = em.getCriteriaBuilder();
 24      CriteriaQuery<Order> criteria = cb.createQuery(Order.class);
 25      Root<Order> member = criteria.from(Order.class);
 26      criteria.select(member);
 27      return em.createQuery(criteria).getResultList();
 28    }
 29  
 30    public Order getOrderById(long id) {
 31      return em.find(Order.class, id);
 32    }
 33  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/service/OrderService.java
      * Replace the `javax.persistence` import statement with `jakarta.persistence`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.service;
  2  
  3  import com.redhat.coolstore.model.Order;
  4  import java.util.List;
  5  import javax.ejb.Stateless;
  6  import javax.persistence.EntityManager;
  7  import javax.persistence.PersistenceContext;
  8  import javax.persistence.criteria.CriteriaBuilder;
  9  import javax.persistence.criteria.CriteriaQuery;
 10  import javax.persistence.criteria.Root;
 11  
 12  @Stateless
 13  public class OrderService {
 14  
 15    @PersistenceContext
 16    private EntityManager em;
 17  
 18    public void save(Order order) {
 19      em.persist(order);
 20    }
 21  
 22    public List<Order> getOrders() {
 23      CriteriaBuilder cb = em.getCriteriaBuilder();
 24      CriteriaQuery<Order> criteria = cb.createQuery(Order.class);
 25      Root<Order> member = criteria.from(Order.class);
 26      criteria.select(member);
 27      return em.createQuery(criteria).getResultList();
 28    }
 29  
 30    public Order getOrderById(long id) {
 31      return em.find(Order.class, id);
 32    }
 33  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/service/OrderServiceMDB.java
      * Replace the `javax.inject` import statement with `jakarta.inject`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.service;
  2  
  3  import javax.ejb.ActivationConfigProperty;
  4  import javax.ejb.MessageDriven;
  5  import javax.inject.Inject;
  6  import javax.jms.JMSException;
  7  import javax.jms.Message;
  8  import javax.jms.MessageListener;
  9  import javax.jms.TextMessage;
 10  
 11  import com.redhat.coolstore.model.Order;
 12  import com.redhat.coolstore.utils.Transformers;
 13  import weblogic.i18n.logging.NonCatalogLogger;
 14  
 15  @MessageDriven(name = "OrderServiceMDB", activationConfig = {
 16  	@ActivationConfigProperty(propertyName = "destinationLookup", propertyValue = "topic/orders"),
 17  	@ActivationConfigProperty(propertyName = "destinationType", propertyValue = "javax.jms.Topic"),
 18  	@ActivationConfigProperty(propertyName = "acknowledgeMode", propertyValue = "Auto-acknowledge")})
 19  public class OrderServiceMDB implements MessageListener { 
 20  
 21  	@Inject
 22  	OrderService orderService;
 23  
 24  	@Inject
 25  	CatalogService catalogService;
 26  
 27  	private NonCatalogLogger log = new NonCatalogLogger(OrderServiceMDB.class.getName());
 28  
 29  	@Override
 30  	public void onMessage(Message rcvMessage) {
 31  		System.out.println("\nMessage recd !");
 32  		TextMessage msg = null;
 33  		try {
 34  				if (rcvMessage instanceof TextMessage) {
 35  						msg = (TextMessage) rcvMessage;
 36  						String orderStr = msg.getBody(String.class);
 37  						System.out.println("Received order: " + orderStr);
 38  						Order order = Transformers.jsonToOrder(orderStr);
 39  						System.out.println("Order object is " + order);
 40  						orderService.save(order);
 41  						order.getItemList().forEach(orderItem -> {
 42  							catalogService.updateInventoryItems(orderItem.getProductId(), orderItem.getQuantity());
 43  						});
 44  				}
 45  		} catch (JMSException e) {
 46  			throw new RuntimeException(e);
 47  		}
 48  	}
 49  
 50  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/service/OrderServiceMDB.java
      * Replace the `javax.jms` import statement with `jakarta.jms`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.service;
  2  
  3  import javax.ejb.ActivationConfigProperty;
  4  import javax.ejb.MessageDriven;
  5  import javax.inject.Inject;
  6  import javax.jms.JMSException;
  7  import javax.jms.Message;
  8  import javax.jms.MessageListener;
  9  import javax.jms.TextMessage;
 10  
 11  import com.redhat.coolstore.model.Order;
 12  import com.redhat.coolstore.utils.Transformers;
 13  import weblogic.i18n.logging.NonCatalogLogger;
 14  
 15  @MessageDriven(name = "OrderServiceMDB", activationConfig = {
 16  	@ActivationConfigProperty(propertyName = "destinationLookup", propertyValue = "topic/orders"),
 17  	@ActivationConfigProperty(propertyName = "destinationType", propertyValue = "javax.jms.Topic"),
 18  	@ActivationConfigProperty(propertyName = "acknowledgeMode", propertyValue = "Auto-acknowledge")})
 19  public class OrderServiceMDB implements MessageListener { 
 20  
 21  	@Inject
 22  	OrderService orderService;
 23  
 24  	@Inject
 25  	CatalogService catalogService;
 26  
 27  	private NonCatalogLogger log = new NonCatalogLogger(OrderServiceMDB.class.getName());
 28  
 29  	@Override
 30  	public void onMessage(Message rcvMessage) {
 31  		System.out.println("\nMessage recd !");
 32  		TextMessage msg = null;
 33  		try {
 34  				if (rcvMessage instanceof TextMessage) {
 35  						msg = (TextMessage) rcvMessage;
 36  						String orderStr = msg.getBody(String.class);
 37  						System.out.println("Received order: " + orderStr);
 38  						Order order = Transformers.jsonToOrder(orderStr);
 39  						System.out.println("Order object is " + order);
 40  						orderService.save(order);
 41  						order.getItemList().forEach(orderItem -> {
 42  							catalogService.updateInventoryItems(orderItem.getProductId(), orderItem.getQuantity());
 43  						});
 44  				}
 45  		} catch (JMSException e) {
 46  			throw new RuntimeException(e);
 47  		}
 48  	}
 49  
 50  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/service/OrderServiceMDB.java
      * Replace the `javax.jms` import statement with `jakarta.jms`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.service;
  2  
  3  import javax.ejb.ActivationConfigProperty;
  4  import javax.ejb.MessageDriven;
  5  import javax.inject.Inject;
  6  import javax.jms.JMSException;
  7  import javax.jms.Message;
  8  import javax.jms.MessageListener;
  9  import javax.jms.TextMessage;
 10  
 11  import com.redhat.coolstore.model.Order;
 12  import com.redhat.coolstore.utils.Transformers;
 13  import weblogic.i18n.logging.NonCatalogLogger;
 14  
 15  @MessageDriven(name = "OrderServiceMDB", activationConfig = {
 16  	@ActivationConfigProperty(propertyName = "destinationLookup", propertyValue = "topic/orders"),
 17  	@ActivationConfigProperty(propertyName = "destinationType", propertyValue = "javax.jms.Topic"),
 18  	@ActivationConfigProperty(propertyName = "acknowledgeMode", propertyValue = "Auto-acknowledge")})
 19  public class OrderServiceMDB implements MessageListener { 
 20  
 21  	@Inject
 22  	OrderService orderService;
 23  
 24  	@Inject
 25  	CatalogService catalogService;
 26  
 27  	private NonCatalogLogger log = new NonCatalogLogger(OrderServiceMDB.class.getName());
 28  
 29  	@Override
 30  	public void onMessage(Message rcvMessage) {
 31  		System.out.println("\nMessage recd !");
 32  		TextMessage msg = null;
 33  		try {
 34  				if (rcvMessage instanceof TextMessage) {
 35  						msg = (TextMessage) rcvMessage;
 36  						String orderStr = msg.getBody(String.class);
 37  						System.out.println("Received order: " + orderStr);
 38  						Order order = Transformers.jsonToOrder(orderStr);
 39  						System.out.println("Order object is " + order);
 40  						orderService.save(order);
 41  						order.getItemList().forEach(orderItem -> {
 42  							catalogService.updateInventoryItems(orderItem.getProductId(), orderItem.getQuantity());
 43  						});
 44  				}
 45  		} catch (JMSException e) {
 46  			throw new RuntimeException(e);
 47  		}
 48  	}
 49  
 50  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/service/OrderServiceMDB.java
      * Replace the `javax.ejb` import statement with `jakarta.ejb`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.service;
  2  
  3  import javax.ejb.ActivationConfigProperty;
  4  import javax.ejb.MessageDriven;
  5  import javax.inject.Inject;
  6  import javax.jms.JMSException;
  7  import javax.jms.Message;
  8  import javax.jms.MessageListener;
  9  import javax.jms.TextMessage;
 10  
 11  import com.redhat.coolstore.model.Order;
 12  import com.redhat.coolstore.utils.Transformers;
 13  import weblogic.i18n.logging.NonCatalogLogger;
 14  
 15  @MessageDriven(name = "OrderServiceMDB", activationConfig = {
 16  	@ActivationConfigProperty(propertyName = "destinationLookup", propertyValue = "topic/orders"),
 17  	@ActivationConfigProperty(propertyName = "destinationType", propertyValue = "javax.jms.Topic"),
 18  	@ActivationConfigProperty(propertyName = "acknowledgeMode", propertyValue = "Auto-acknowledge")})
 19  public class OrderServiceMDB implements MessageListener { 
 20  
 21  	@Inject
 22  	OrderService orderService;
 23  
 24  	@Inject
 25  	CatalogService catalogService;
 26  
 27  	private NonCatalogLogger log = new NonCatalogLogger(OrderServiceMDB.class.getName());
 28  
 29  	@Override
 30  	public void onMessage(Message rcvMessage) {
 31  		System.out.println("\nMessage recd !");
 32  		TextMessage msg = null;
 33  		try {
 34  				if (rcvMessage instanceof TextMessage) {
 35  						msg = (TextMessage) rcvMessage;
 36  						String orderStr = msg.getBody(String.class);
 37  						System.out.println("Received order: " + orderStr);
 38  						Order order = Transformers.jsonToOrder(orderStr);
 39  						System.out.println("Order object is " + order);
 40  						orderService.save(order);
 41  						order.getItemList().forEach(orderItem -> {
 42  							catalogService.updateInventoryItems(orderItem.getProductId(), orderItem.getQuantity());
 43  						});
 44  				}
 45  		} catch (JMSException e) {
 46  			throw new RuntimeException(e);
 47  		}
 48  	}
 49  
 50  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/service/OrderServiceMDB.java
      * Replace the `javax.jms` import statement with `jakarta.jms`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.service;
  2  
  3  import javax.ejb.ActivationConfigProperty;
  4  import javax.ejb.MessageDriven;
  5  import javax.inject.Inject;
  6  import javax.jms.JMSException;
  7  import javax.jms.Message;
  8  import javax.jms.MessageListener;
  9  import javax.jms.TextMessage;
 10  
 11  import com.redhat.coolstore.model.Order;
 12  import com.redhat.coolstore.utils.Transformers;
 13  import weblogic.i18n.logging.NonCatalogLogger;
 14  
 15  @MessageDriven(name = "OrderServiceMDB", activationConfig = {
 16  	@ActivationConfigProperty(propertyName = "destinationLookup", propertyValue = "topic/orders"),
 17  	@ActivationConfigProperty(propertyName = "destinationType", propertyValue = "javax.jms.Topic"),
 18  	@ActivationConfigProperty(propertyName = "acknowledgeMode", propertyValue = "Auto-acknowledge")})
 19  public class OrderServiceMDB implements MessageListener { 
 20  
 21  	@Inject
 22  	OrderService orderService;
 23  
 24  	@Inject
 25  	CatalogService catalogService;
 26  
 27  	private NonCatalogLogger log = new NonCatalogLogger(OrderServiceMDB.class.getName());
 28  
 29  	@Override
 30  	public void onMessage(Message rcvMessage) {
 31  		System.out.println("\nMessage recd !");
 32  		TextMessage msg = null;
 33  		try {
 34  				if (rcvMessage instanceof TextMessage) {
 35  						msg = (TextMessage) rcvMessage;
 36  						String orderStr = msg.getBody(String.class);
 37  						System.out.println("Received order: " + orderStr);
 38  						Order order = Transformers.jsonToOrder(orderStr);
 39  						System.out.println("Order object is " + order);
 40  						orderService.save(order);
 41  						order.getItemList().forEach(orderItem -> {
 42  							catalogService.updateInventoryItems(orderItem.getProductId(), orderItem.getQuantity());
 43  						});
 44  				}
 45  		} catch (JMSException e) {
 46  			throw new RuntimeException(e);
 47  		}
 48  	}
 49  
 50  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/service/OrderServiceMDB.java
      * Replace the `javax.ejb` import statement with `jakarta.ejb`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.service;
  2  
  3  import javax.ejb.ActivationConfigProperty;
  4  import javax.ejb.MessageDriven;
  5  import javax.inject.Inject;
  6  import javax.jms.JMSException;
  7  import javax.jms.Message;
  8  import javax.jms.MessageListener;
  9  import javax.jms.TextMessage;
 10  
 11  import com.redhat.coolstore.model.Order;
 12  import com.redhat.coolstore.utils.Transformers;
 13  import weblogic.i18n.logging.NonCatalogLogger;
 14  
 15  @MessageDriven(name = "OrderServiceMDB", activationConfig = {
 16  	@ActivationConfigProperty(propertyName = "destinationLookup", propertyValue = "topic/orders"),
 17  	@ActivationConfigProperty(propertyName = "destinationType", propertyValue = "javax.jms.Topic"),
 18  	@ActivationConfigProperty(propertyName = "acknowledgeMode", propertyValue = "Auto-acknowledge")})
 19  public class OrderServiceMDB implements MessageListener { 
 20  
 21  	@Inject
 22  	OrderService orderService;
 23  
 24  	@Inject
 25  	CatalogService catalogService;
 26  
 27  	private NonCatalogLogger log = new NonCatalogLogger(OrderServiceMDB.class.getName());
 28  
 29  	@Override
 30  	public void onMessage(Message rcvMessage) {
 31  		System.out.println("\nMessage recd !");
 32  		TextMessage msg = null;
 33  		try {
 34  				if (rcvMessage instanceof TextMessage) {
 35  						msg = (TextMessage) rcvMessage;
 36  						String orderStr = msg.getBody(String.class);
 37  						System.out.println("Received order: " + orderStr);
 38  						Order order = Transformers.jsonToOrder(orderStr);
 39  						System.out.println("Order object is " + order);
 40  						orderService.save(order);
 41  						order.getItemList().forEach(orderItem -> {
 42  							catalogService.updateInventoryItems(orderItem.getProductId(), orderItem.getQuantity());
 43  						});
 44  				}
 45  		} catch (JMSException e) {
 46  			throw new RuntimeException(e);
 47  		}
 48  	}
 49  
 50  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/service/OrderServiceMDB.java
      * Replace the `javax.jms` import statement with `jakarta.jms`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.service;
  2  
  3  import javax.ejb.ActivationConfigProperty;
  4  import javax.ejb.MessageDriven;
  5  import javax.inject.Inject;
  6  import javax.jms.JMSException;
  7  import javax.jms.Message;
  8  import javax.jms.MessageListener;
  9  import javax.jms.TextMessage;
 10  
 11  import com.redhat.coolstore.model.Order;
 12  import com.redhat.coolstore.utils.Transformers;
 13  import weblogic.i18n.logging.NonCatalogLogger;
 14  
 15  @MessageDriven(name = "OrderServiceMDB", activationConfig = {
 16  	@ActivationConfigProperty(propertyName = "destinationLookup", propertyValue = "topic/orders"),
 17  	@ActivationConfigProperty(propertyName = "destinationType", propertyValue = "javax.jms.Topic"),
 18  	@ActivationConfigProperty(propertyName = "acknowledgeMode", propertyValue = "Auto-acknowledge")})
 19  public class OrderServiceMDB implements MessageListener { 
 20  
 21  	@Inject
 22  	OrderService orderService;
 23  
 24  	@Inject
 25  	CatalogService catalogService;
 26  
 27  	private NonCatalogLogger log = new NonCatalogLogger(OrderServiceMDB.class.getName());
 28  
 29  	@Override
 30  	public void onMessage(Message rcvMessage) {
 31  		System.out.println("\nMessage recd !");
 32  		TextMessage msg = null;
 33  		try {
 34  				if (rcvMessage instanceof TextMessage) {
 35  						msg = (TextMessage) rcvMessage;
 36  						String orderStr = msg.getBody(String.class);
 37  						System.out.println("Received order: " + orderStr);
 38  						Order order = Transformers.jsonToOrder(orderStr);
 39  						System.out.println("Order object is " + order);
 40  						orderService.save(order);
 41  						order.getItemList().forEach(orderItem -> {
 42  							catalogService.updateInventoryItems(orderItem.getProductId(), orderItem.getQuantity());
 43  						});
 44  				}
 45  		} catch (JMSException e) {
 46  			throw new RuntimeException(e);
 47  		}
 48  	}
 49  
 50  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/service/ProductService.java
      * Replace the `javax.ejb` import statement with `jakarta.ejb`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.service;
  2  
  3  import com.redhat.coolstore.model.CatalogItemEntity;
  4  import com.redhat.coolstore.model.Product;
  5  import com.redhat.coolstore.utils.Transformers;
  6  
  7  import javax.ejb.Stateless;
  8  import javax.inject.Inject;
  9  import java.util.List;
 10  import java.util.stream.Collectors;
 11  
 12  import static com.redhat.coolstore.utils.Transformers.toProduct;
 13  
 14  @Stateless
 15  public class ProductService {
 16  
 17      @Inject
 18      CatalogService cm;
 19  
 20      public ProductService() {
 21      }
 22  
 23      public List<Product> getProducts() {
 24          return cm.getCatalogItems().stream().map(entity -> toProduct(entity)).collect(Collectors.toList());
 25      }
 26  
 27      public Product getProductByItemId(String itemId) {
 28          CatalogItemEntity entity = cm.getCatalogItemById(itemId);
 29          if (entity == null)
 30              return null;
 31  
 32          // Return the entity
 33          return Transformers.toProduct(entity);
 34      }
 35  
 36  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/service/ProductService.java
      * Replace the `javax.inject` import statement with `jakarta.inject`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.service;
  2  
  3  import com.redhat.coolstore.model.CatalogItemEntity;
  4  import com.redhat.coolstore.model.Product;
  5  import com.redhat.coolstore.utils.Transformers;
  6  
  7  import javax.ejb.Stateless;
  8  import javax.inject.Inject;
  9  import java.util.List;
 10  import java.util.stream.Collectors;
 11  
 12  import static com.redhat.coolstore.utils.Transformers.toProduct;
 13  
 14  @Stateless
 15  public class ProductService {
 16  
 17      @Inject
 18      CatalogService cm;
 19  
 20      public ProductService() {
 21      }
 22  
 23      public List<Product> getProducts() {
 24          return cm.getCatalogItems().stream().map(entity -> toProduct(entity)).collect(Collectors.toList());
 25      }
 26  
 27      public Product getProductByItemId(String itemId) {
 28          CatalogItemEntity entity = cm.getCatalogItemById(itemId);
 29          if (entity == null)
 30              return null;
 31  
 32          // Return the entity
 33          return Transformers.toProduct(entity);
 34      }
 35  
 36  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/service/PromoService.java
      * Replace the `javax.enterprise` import statement with `jakarta.enterprise`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.service;
  2  
  3  import java.io.Serializable;
  4  import java.util.HashMap;
  5  import java.util.HashSet;
  6  import java.util.Map;
  7  import java.util.Set;
  8  
  9  import javax.enterprise.context.ApplicationScoped;
 10  
 11  import com.redhat.coolstore.model.Promotion;
 12  import com.redhat.coolstore.model.ShoppingCart;
 13  import com.redhat.coolstore.model.ShoppingCartItem;
 14  
 15  @ApplicationScoped
 16  public class PromoService implements Serializable {
 17  
 18      private static final long serialVersionUID = 2088590587856645568L;
 19  
 20      private String name = null;
 21  
 22      private Set<Promotion> promotionSet = null;
 23  
 24      public PromoService() {
 25  
 26          promotionSet = new HashSet<>();
 27  
 28          promotionSet.add(new Promotion("329299", .25));
 29  
 30      }
 31  
 32      public void applyCartItemPromotions(ShoppingCart shoppingCart) {
 33  
 34          if (shoppingCart != null && shoppingCart.getShoppingCartItemList().size() > 0) {
 35  
 36              Map<String, Promotion> promoMap = new HashMap<String, Promotion>();
 37  
 38              for (Promotion promo : getPromotions()) {
 39  
 40                  promoMap.put(promo.getItemId(), promo);
 41  
 42              }
 43  
 44              for (ShoppingCartItem sci : shoppingCart.getShoppingCartItemList()) {
 45  
 46                  String productId = sci.getProduct().getItemId();
 47  
 48                  Promotion promo = promoMap.get(productId);
 49  
 50                  if (promo != null) {
 51  
 52                      sci.setPromoSavings(sci.getProduct().getPrice() * promo.getPercentOff() * -1);
 53                      sci.setPrice(sci.getProduct().getPrice() * (1 - promo.getPercentOff()));
 54  
 55                  }
 56  
 57              }
 58  
 59          }
 60  
 61      }
 62  
 63      public void applyShippingPromotions(ShoppingCart shoppingCart) {
 64  
 65          if (shoppingCart != null) {
 66  
 67              //PROMO: if cart total is greater than 75, free shipping
 68              if (shoppingCart.getCartItemTotal() >= 75) {
 69  
 70                  shoppingCart.setShippingPromoSavings(shoppingCart.getShippingTotal() * -1);
 71                  shoppingCart.setShippingTotal(0);
 72  
 73              }
 74  
 75          }
 76  
 77      }
 78  
 79      public Set<Promotion> getPromotions() {
 80  
 81          if (promotionSet == null) {
 82  
 83              promotionSet = new HashSet<>();
 84  
 85          }
 86  
 87          return new HashSet<>(promotionSet);
 88  
 89      }
 90  
 91      public void setPromotions(Set<Promotion> promotionSet) {
 92  
 93          if (promotionSet != null) {
 94  
 95              this.promotionSet = new HashSet<>(promotionSet);
 96  
 97          } else {
 98  
 99              this.promotionSet = new HashSet<>();
100  
101          }
102  
103      }
104  
105      @Override
106      public String toString() {
107          return "PromoService [name=" + name + ", promotionSet=" + promotionSet + "]";
108      }
109  
```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/service/ShippingService.java
      * Replace the `javax.ejb` import statement with `jakarta.ejb`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.service;
  2  
  3  import javax.ejb.Stateless;
  4  
  5  import com.redhat.coolstore.model.ShoppingCart;
  6  
  7  @Stateless
  8  public class ShippingService {
  9  
 10      public void calculateShipping(ShoppingCart sc) {
 11  
 12          if (sc != null) {
 13  
 14              if (sc.getCartItemTotal() >= 0 && sc.getCartItemTotal() < 25) {
 15  
 16                  sc.setShippingTotal(2.99);
 17  
 18              } else if (sc.getCartItemTotal() >= 25 && sc.getCartItemTotal() < 50) {
 19  
 20                  sc.setShippingTotal(4.99);
 21  
 22              } else if (sc.getCartItemTotal() >= 50 && sc.getCartItemTotal() < 75) {
 23  
 24                  sc.setShippingTotal(6.99);
 25  
 26              } else if (sc.getCartItemTotal() >= 75 && sc.getCartItemTotal() < 100) {
 27  
 28                  sc.setShippingTotal(8.99);
 29  
 30              } else if (sc.getCartItemTotal() >= 100 && sc.getCartItemTotal() < 10000) {
 31  
 32                  sc.setShippingTotal(10.99);
 33  
 34              }
 35  
 36          }
 37  
 38      }
 39  
 40  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/service/ShoppingCartOrderProcessor.java
      * Replace the `javax.jms` import statement with `jakarta.jms`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.service;
  2  
  3  import java.util.logging.Logger;
  4  import javax.ejb.Stateless;
  5  import javax.annotation.Resource;
  6  import javax.inject.Inject;
  7  import javax.jms.JMSContext;
  8  import javax.jms.Topic;
  9  
 10  import com.redhat.coolstore.model.ShoppingCart;
 11  import com.redhat.coolstore.utils.Transformers;
 12  
 13  @Stateless
 14  public class ShoppingCartOrderProcessor  {
 15  
 16      @Inject
 17      Logger log;
 18  
 19  
 20      @Inject
 21      private transient JMSContext context;
 22  
 23      @Resource(lookup = "java:/topic/orders")
 24      private Topic ordersTopic;
 25  
 26      
 27    
 28      public void  process(ShoppingCart cart) {
 29          log.info("Sending order from processor: ");
 30          context.createProducer().send(ordersTopic, Transformers.shoppingCartToJson(cart));
 31      }
 32  
 33  
 34  
 35  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/service/ShoppingCartOrderProcessor.java
      * Replace the `javax.annotation` import statement with `jakarta.annotation`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.service;
  2  
  3  import java.util.logging.Logger;
  4  import javax.ejb.Stateless;
  5  import javax.annotation.Resource;
  6  import javax.inject.Inject;
  7  import javax.jms.JMSContext;
  8  import javax.jms.Topic;
  9  
 10  import com.redhat.coolstore.model.ShoppingCart;
 11  import com.redhat.coolstore.utils.Transformers;
 12  
 13  @Stateless
 14  public class ShoppingCartOrderProcessor  {
 15  
 16      @Inject
 17      Logger log;
 18  
 19  
 20      @Inject
 21      private transient JMSContext context;
 22  
 23      @Resource(lookup = "java:/topic/orders")
 24      private Topic ordersTopic;
 25  
 26      
 27    
 28      public void  process(ShoppingCart cart) {
 29          log.info("Sending order from processor: ");
 30          context.createProducer().send(ordersTopic, Transformers.shoppingCartToJson(cart));
 31      }
 32  
 33  
 34  
 35  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/service/ShoppingCartOrderProcessor.java
      * Replace the `javax.ejb` import statement with `jakarta.ejb`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.service;
  2  
  3  import java.util.logging.Logger;
  4  import javax.ejb.Stateless;
  5  import javax.annotation.Resource;
  6  import javax.inject.Inject;
  7  import javax.jms.JMSContext;
  8  import javax.jms.Topic;
  9  
 10  import com.redhat.coolstore.model.ShoppingCart;
 11  import com.redhat.coolstore.utils.Transformers;
 12  
 13  @Stateless
 14  public class ShoppingCartOrderProcessor  {
 15  
 16      @Inject
 17      Logger log;
 18  
 19  
 20      @Inject
 21      private transient JMSContext context;
 22  
 23      @Resource(lookup = "java:/topic/orders")
 24      private Topic ordersTopic;
 25  
 26      
 27    
 28      public void  process(ShoppingCart cart) {
 29          log.info("Sending order from processor: ");
 30          context.createProducer().send(ordersTopic, Transformers.shoppingCartToJson(cart));
 31      }
 32  
 33  
 34  
 35  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/service/ShoppingCartOrderProcessor.java
      * Replace the `javax.inject` import statement with `jakarta.inject`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.service;
  2  
  3  import java.util.logging.Logger;
  4  import javax.ejb.Stateless;
  5  import javax.annotation.Resource;
  6  import javax.inject.Inject;
  7  import javax.jms.JMSContext;
  8  import javax.jms.Topic;
  9  
 10  import com.redhat.coolstore.model.ShoppingCart;
 11  import com.redhat.coolstore.utils.Transformers;
 12  
 13  @Stateless
 14  public class ShoppingCartOrderProcessor  {
 15  
 16      @Inject
 17      Logger log;
 18  
 19  
 20      @Inject
 21      private transient JMSContext context;
 22  
 23      @Resource(lookup = "java:/topic/orders")
 24      private Topic ordersTopic;
 25  
 26      
 27    
 28      public void  process(ShoppingCart cart) {
 29          log.info("Sending order from processor: ");
 30          context.createProducer().send(ordersTopic, Transformers.shoppingCartToJson(cart));
 31      }
 32  
 33  
 34  
 35  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/service/ShoppingCartOrderProcessor.java
      * Replace the `javax.jms` import statement with `jakarta.jms`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.service;
  2  
  3  import java.util.logging.Logger;
  4  import javax.ejb.Stateless;
  5  import javax.annotation.Resource;
  6  import javax.inject.Inject;
  7  import javax.jms.JMSContext;
  8  import javax.jms.Topic;
  9  
 10  import com.redhat.coolstore.model.ShoppingCart;
 11  import com.redhat.coolstore.utils.Transformers;
 12  
 13  @Stateless
 14  public class ShoppingCartOrderProcessor  {
 15  
 16      @Inject
 17      Logger log;
 18  
 19  
 20      @Inject
 21      private transient JMSContext context;
 22  
 23      @Resource(lookup = "java:/topic/orders")
 24      private Topic ordersTopic;
 25  
 26      
 27    
 28      public void  process(ShoppingCart cart) {
 29          log.info("Sending order from processor: ");
 30          context.createProducer().send(ordersTopic, Transformers.shoppingCartToJson(cart));
 31      }
 32  
 33  
 34  
 35  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/service/ShoppingCartService.java
      * Replace the `javax.inject` import statement with `jakarta.inject`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.service;
  2  
  3  import java.util.logging.Logger;
  4  
  5  import javax.ejb.Stateful;
  6  import javax.inject.Inject;
  7  
  8  
  9  import com.redhat.coolstore.model.Product;
 10  import com.redhat.coolstore.model.ShoppingCart;
 11  import com.redhat.coolstore.model.ShoppingCartItem;
 12  
 13  @Stateful
 14  public class ShoppingCartService  {
 15  
 16      @Inject
 17      Logger log;
 18  
 19      @Inject
 20      ProductService productServices;
 21  
 22      @Inject
 23      ShippingService ss;
 24  
 25      @Inject
 26      PromoService ps;
 27  
 28  
 29      @Inject
 30      ShoppingCartOrderProcessor shoppingCartOrderProcessor;
 31  
 32      private ShoppingCart cart  = new ShoppingCart(); //Each user can have multiple shopping carts (tabbed browsing)
 33  
 34     
 35  
 36      public ShoppingCartService() {
 37      }
 38  
 39      public ShoppingCart getShoppingCart(String cartId) {
 40          return cart;
 41      }
 42  
 43      public ShoppingCart checkOutShoppingCart(String cartId) {
 44          ShoppingCart cart = this.getShoppingCart(cartId);
 45        
 46          log.info("Sending  order: ");
 47          shoppingCartOrderProcessor.process(cart);
 48     
 49          cart.resetShoppingCartItemList();
 50          priceShoppingCart(cart);
 51          return cart;
 52      }
 53  
 54      public void priceShoppingCart(ShoppingCart sc) {
 55  
 56          if (sc != null) {
 57  
 58              initShoppingCartForPricing(sc);
 59  
 60              if (sc.getShoppingCartItemList() != null && sc.getShoppingCartItemList().size() > 0) {
 61  
 62                  ps.applyCartItemPromotions(sc);
 63  
 64                  for (ShoppingCartItem sci : sc.getShoppingCartItemList()) {
 65  
 66                      sc.setCartItemPromoSavings(
 67                              sc.getCartItemPromoSavings() + sci.getPromoSavings() * sci.getQuantity());
 68                      sc.setCartItemTotal(sc.getCartItemTotal() + sci.getPrice() * sci.getQuantity());
 69  
 70                  }
 71  
 72                  ss.calculateShipping(sc);
 73  
 74              }
 75  
 76              ps.applyShippingPromotions(sc);
 77  
 78              sc.setCartTotal(sc.getCartItemTotal() + sc.getShippingTotal());
 79  
 80          }
 81  
 82      }
 83  
 84      private void initShoppingCartForPricing(ShoppingCart sc) {
 85  
 86          sc.setCartItemTotal(0);
 87          sc.setCartItemPromoSavings(0);
 88          sc.setShippingTotal(0);
 89          sc.setShippingPromoSavings(0);
 90          sc.setCartTotal(0);
 91  
 92          for (ShoppingCartItem sci : sc.getShoppingCartItemList()) {
 93              Product p = getProduct(sci.getProduct().getItemId());
 94              //if product exist
 95              if (p != null) {
 96                  sci.setProduct(p);
 97                  sci.setPrice(p.getPrice());
 98              }
 99  
100              sci.setPromoSavings(0);
101          }
102  
103      }
104  
105      public Product getProduct(String itemId) {
106          return productServices.getProductByItemId(itemId);
```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/service/ShoppingCartService.java
      * Replace the `javax.ejb` import statement with `jakarta.ejb`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.service;
  2  
  3  import java.util.logging.Logger;
  4  
  5  import javax.ejb.Stateful;
  6  import javax.inject.Inject;
  7  
  8  
  9  import com.redhat.coolstore.model.Product;
 10  import com.redhat.coolstore.model.ShoppingCart;
 11  import com.redhat.coolstore.model.ShoppingCartItem;
 12  
 13  @Stateful
 14  public class ShoppingCartService  {
 15  
 16      @Inject
 17      Logger log;
 18  
 19      @Inject
 20      ProductService productServices;
 21  
 22      @Inject
 23      ShippingService ss;
 24  
 25      @Inject
 26      PromoService ps;
 27  
 28  
 29      @Inject
 30      ShoppingCartOrderProcessor shoppingCartOrderProcessor;
 31  
 32      private ShoppingCart cart  = new ShoppingCart(); //Each user can have multiple shopping carts (tabbed browsing)
 33  
 34     
 35  
 36      public ShoppingCartService() {
 37      }
 38  
 39      public ShoppingCart getShoppingCart(String cartId) {
 40          return cart;
 41      }
 42  
 43      public ShoppingCart checkOutShoppingCart(String cartId) {
 44          ShoppingCart cart = this.getShoppingCart(cartId);
 45        
 46          log.info("Sending  order: ");
 47          shoppingCartOrderProcessor.process(cart);
 48     
 49          cart.resetShoppingCartItemList();
 50          priceShoppingCart(cart);
 51          return cart;
 52      }
 53  
 54      public void priceShoppingCart(ShoppingCart sc) {
 55  
 56          if (sc != null) {
 57  
 58              initShoppingCartForPricing(sc);
 59  
 60              if (sc.getShoppingCartItemList() != null && sc.getShoppingCartItemList().size() > 0) {
 61  
 62                  ps.applyCartItemPromotions(sc);
 63  
 64                  for (ShoppingCartItem sci : sc.getShoppingCartItemList()) {
 65  
 66                      sc.setCartItemPromoSavings(
 67                              sc.getCartItemPromoSavings() + sci.getPromoSavings() * sci.getQuantity());
 68                      sc.setCartItemTotal(sc.getCartItemTotal() + sci.getPrice() * sci.getQuantity());
 69  
 70                  }
 71  
 72                  ss.calculateShipping(sc);
 73  
 74              }
 75  
 76              ps.applyShippingPromotions(sc);
 77  
 78              sc.setCartTotal(sc.getCartItemTotal() + sc.getShippingTotal());
 79  
 80          }
 81  
 82      }
 83  
 84      private void initShoppingCartForPricing(ShoppingCart sc) {
 85  
 86          sc.setCartItemTotal(0);
 87          sc.setCartItemPromoSavings(0);
 88          sc.setShippingTotal(0);
 89          sc.setShippingPromoSavings(0);
 90          sc.setCartTotal(0);
 91  
 92          for (ShoppingCartItem sci : sc.getShoppingCartItemList()) {
 93              Product p = getProduct(sci.getProduct().getItemId());
 94              //if product exist
 95              if (p != null) {
 96                  sci.setProduct(p);
 97                  sci.setPrice(p.getPrice());
 98              }
 99  
100              sci.setPromoSavings(0);
101          }
102  
103      }
104  
105      public Product getProduct(String itemId) {
```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/utils/DataBaseMigrationStartup.java
      * Replace the `javax.ejb` import statement with `jakarta.ejb`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.utils;
  2  
  3  import org.flywaydb.core.Flyway;
  4  import org.flywaydb.core.api.FlywayException;
  5  
  6  import javax.annotation.PostConstruct;
  7  import javax.annotation.Resource;
  8  import javax.ejb.Singleton;
  9  import javax.ejb.Startup;
 10  import javax.ejb.TransactionManagement;
 11  import javax.ejb.TransactionManagementType;
 12  import javax.inject.Inject;
 13  import javax.sql.DataSource;
 14  import java.util.logging.Level;
 15  import java.util.logging.Logger;
 16  
 17  /**
 18   * Created by tqvarnst on 2017-04-04.
 19   */
 20  @Singleton
 21  @Startup
 22  @TransactionManagement(TransactionManagementType.BEAN)
 23  public class DataBaseMigrationStartup {
 24  
 25      @Inject
 26      Logger logger;
 27  
 28      @Resource(mappedName = "java:jboss/datasources/CoolstoreDS")
 29      DataSource dataSource;
 30  
 31      @PostConstruct
 32      private void startup() {
 33  
 34  
 35          try {
 36              logger.info("Initializing/migrating the database using FlyWay");
 37              Flyway flyway = new Flyway();
 38              flyway.setDataSource(dataSource);
 39              flyway.baseline();
 40              // Start the db.migration
 41              flyway.migrate();
 42          } catch (FlywayException e) {
 43              if(logger !=null)
 44                  logger.log(Level.SEVERE,"FAILED TO INITIALIZE THE DATABASE: " + e.getMessage(),e);
 45              else
 46                  System.out.println("FAILED TO INITIALIZE THE DATABASE: " + e.getMessage() + " and injection of logger doesn't work");
 47  
 48          }
 49      }
 50  
 51  
 52  
 53  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/utils/DataBaseMigrationStartup.java
      * Replace the `javax.inject` import statement with `jakarta.inject`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.utils;
  2  
  3  import org.flywaydb.core.Flyway;
  4  import org.flywaydb.core.api.FlywayException;
  5  
  6  import javax.annotation.PostConstruct;
  7  import javax.annotation.Resource;
  8  import javax.ejb.Singleton;
  9  import javax.ejb.Startup;
 10  import javax.ejb.TransactionManagement;
 11  import javax.ejb.TransactionManagementType;
 12  import javax.inject.Inject;
 13  import javax.sql.DataSource;
 14  import java.util.logging.Level;
 15  import java.util.logging.Logger;
 16  
 17  /**
 18   * Created by tqvarnst on 2017-04-04.
 19   */
 20  @Singleton
 21  @Startup
 22  @TransactionManagement(TransactionManagementType.BEAN)
 23  public class DataBaseMigrationStartup {
 24  
 25      @Inject
 26      Logger logger;
 27  
 28      @Resource(mappedName = "java:jboss/datasources/CoolstoreDS")
 29      DataSource dataSource;
 30  
 31      @PostConstruct
 32      private void startup() {
 33  
 34  
 35          try {
 36              logger.info("Initializing/migrating the database using FlyWay");
 37              Flyway flyway = new Flyway();
 38              flyway.setDataSource(dataSource);
 39              flyway.baseline();
 40              // Start the db.migration
 41              flyway.migrate();
 42          } catch (FlywayException e) {
 43              if(logger !=null)
 44                  logger.log(Level.SEVERE,"FAILED TO INITIALIZE THE DATABASE: " + e.getMessage(),e);
 45              else
 46                  System.out.println("FAILED TO INITIALIZE THE DATABASE: " + e.getMessage() + " and injection of logger doesn't work");
 47  
 48          }
 49      }
 50  
 51  
 52  
 53  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/utils/DataBaseMigrationStartup.java
      * Replace the `javax.ejb` import statement with `jakarta.ejb`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.utils;
  2  
  3  import org.flywaydb.core.Flyway;
  4  import org.flywaydb.core.api.FlywayException;
  5  
  6  import javax.annotation.PostConstruct;
  7  import javax.annotation.Resource;
  8  import javax.ejb.Singleton;
  9  import javax.ejb.Startup;
 10  import javax.ejb.TransactionManagement;
 11  import javax.ejb.TransactionManagementType;
 12  import javax.inject.Inject;
 13  import javax.sql.DataSource;
 14  import java.util.logging.Level;
 15  import java.util.logging.Logger;
 16  
 17  /**
 18   * Created by tqvarnst on 2017-04-04.
 19   */
 20  @Singleton
 21  @Startup
 22  @TransactionManagement(TransactionManagementType.BEAN)
 23  public class DataBaseMigrationStartup {
 24  
 25      @Inject
 26      Logger logger;
 27  
 28      @Resource(mappedName = "java:jboss/datasources/CoolstoreDS")
 29      DataSource dataSource;
 30  
 31      @PostConstruct
 32      private void startup() {
 33  
 34  
 35          try {
 36              logger.info("Initializing/migrating the database using FlyWay");
 37              Flyway flyway = new Flyway();
 38              flyway.setDataSource(dataSource);
 39              flyway.baseline();
 40              // Start the db.migration
 41              flyway.migrate();
 42          } catch (FlywayException e) {
 43              if(logger !=null)
 44                  logger.log(Level.SEVERE,"FAILED TO INITIALIZE THE DATABASE: " + e.getMessage(),e);
 45              else
 46                  System.out.println("FAILED TO INITIALIZE THE DATABASE: " + e.getMessage() + " and injection of logger doesn't work");
 47  
 48          }
 49      }
 50  
 51  
 52  
 53  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/utils/DataBaseMigrationStartup.java
      * Replace the `javax.ejb` import statement with `jakarta.ejb`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.utils;
  2  
  3  import org.flywaydb.core.Flyway;
  4  import org.flywaydb.core.api.FlywayException;
  5  
  6  import javax.annotation.PostConstruct;
  7  import javax.annotation.Resource;
  8  import javax.ejb.Singleton;
  9  import javax.ejb.Startup;
 10  import javax.ejb.TransactionManagement;
 11  import javax.ejb.TransactionManagementType;
 12  import javax.inject.Inject;
 13  import javax.sql.DataSource;
 14  import java.util.logging.Level;
 15  import java.util.logging.Logger;
 16  
 17  /**
 18   * Created by tqvarnst on 2017-04-04.
 19   */
 20  @Singleton
 21  @Startup
 22  @TransactionManagement(TransactionManagementType.BEAN)
 23  public class DataBaseMigrationStartup {
 24  
 25      @Inject
 26      Logger logger;
 27  
 28      @Resource(mappedName = "java:jboss/datasources/CoolstoreDS")
 29      DataSource dataSource;
 30  
 31      @PostConstruct
 32      private void startup() {
 33  
 34  
 35          try {
 36              logger.info("Initializing/migrating the database using FlyWay");
 37              Flyway flyway = new Flyway();
 38              flyway.setDataSource(dataSource);
 39              flyway.baseline();
 40              // Start the db.migration
 41              flyway.migrate();
 42          } catch (FlywayException e) {
 43              if(logger !=null)
 44                  logger.log(Level.SEVERE,"FAILED TO INITIALIZE THE DATABASE: " + e.getMessage(),e);
 45              else
 46                  System.out.println("FAILED TO INITIALIZE THE DATABASE: " + e.getMessage() + " and injection of logger doesn't work");
 47  
 48          }
 49      }
 50  
 51  
 52  
 53  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/utils/DataBaseMigrationStartup.java
      * Replace the `javax.annotation` import statement with `jakarta.annotation`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.utils;
  2  
  3  import org.flywaydb.core.Flyway;
  4  import org.flywaydb.core.api.FlywayException;
  5  
  6  import javax.annotation.PostConstruct;
  7  import javax.annotation.Resource;
  8  import javax.ejb.Singleton;
  9  import javax.ejb.Startup;
 10  import javax.ejb.TransactionManagement;
 11  import javax.ejb.TransactionManagementType;
 12  import javax.inject.Inject;
 13  import javax.sql.DataSource;
 14  import java.util.logging.Level;
 15  import java.util.logging.Logger;
 16  
 17  /**
 18   * Created by tqvarnst on 2017-04-04.
 19   */
 20  @Singleton
 21  @Startup
 22  @TransactionManagement(TransactionManagementType.BEAN)
 23  public class DataBaseMigrationStartup {
 24  
 25      @Inject
 26      Logger logger;
 27  
 28      @Resource(mappedName = "java:jboss/datasources/CoolstoreDS")
 29      DataSource dataSource;
 30  
 31      @PostConstruct
 32      private void startup() {
 33  
 34  
 35          try {
 36              logger.info("Initializing/migrating the database using FlyWay");
 37              Flyway flyway = new Flyway();
 38              flyway.setDataSource(dataSource);
 39              flyway.baseline();
 40              // Start the db.migration
 41              flyway.migrate();
 42          } catch (FlywayException e) {
 43              if(logger !=null)
 44                  logger.log(Level.SEVERE,"FAILED TO INITIALIZE THE DATABASE: " + e.getMessage(),e);
 45              else
 46                  System.out.println("FAILED TO INITIALIZE THE DATABASE: " + e.getMessage() + " and injection of logger doesn't work");
 47  
 48          }
 49      }
 50  
 51  
 52  
 53  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/utils/DataBaseMigrationStartup.java
      * Replace the `javax.ejb` import statement with `jakarta.ejb`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.utils;
  2  
  3  import org.flywaydb.core.Flyway;
  4  import org.flywaydb.core.api.FlywayException;
  5  
  6  import javax.annotation.PostConstruct;
  7  import javax.annotation.Resource;
  8  import javax.ejb.Singleton;
  9  import javax.ejb.Startup;
 10  import javax.ejb.TransactionManagement;
 11  import javax.ejb.TransactionManagementType;
 12  import javax.inject.Inject;
 13  import javax.sql.DataSource;
 14  import java.util.logging.Level;
 15  import java.util.logging.Logger;
 16  
 17  /**
 18   * Created by tqvarnst on 2017-04-04.
 19   */
 20  @Singleton
 21  @Startup
 22  @TransactionManagement(TransactionManagementType.BEAN)
 23  public class DataBaseMigrationStartup {
 24  
 25      @Inject
 26      Logger logger;
 27  
 28      @Resource(mappedName = "java:jboss/datasources/CoolstoreDS")
 29      DataSource dataSource;
 30  
 31      @PostConstruct
 32      private void startup() {
 33  
 34  
 35          try {
 36              logger.info("Initializing/migrating the database using FlyWay");
 37              Flyway flyway = new Flyway();
 38              flyway.setDataSource(dataSource);
 39              flyway.baseline();
 40              // Start the db.migration
 41              flyway.migrate();
 42          } catch (FlywayException e) {
 43              if(logger !=null)
 44                  logger.log(Level.SEVERE,"FAILED TO INITIALIZE THE DATABASE: " + e.getMessage(),e);
 45              else
 46                  System.out.println("FAILED TO INITIALIZE THE DATABASE: " + e.getMessage() + " and injection of logger doesn't work");
 47  
 48          }
 49      }
 50  
 51  
 52  
 53  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/utils/DataBaseMigrationStartup.java
      * Replace the `javax.annotation` import statement with `jakarta.annotation`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.utils;
  2  
  3  import org.flywaydb.core.Flyway;
  4  import org.flywaydb.core.api.FlywayException;
  5  
  6  import javax.annotation.PostConstruct;
  7  import javax.annotation.Resource;
  8  import javax.ejb.Singleton;
  9  import javax.ejb.Startup;
 10  import javax.ejb.TransactionManagement;
 11  import javax.ejb.TransactionManagementType;
 12  import javax.inject.Inject;
 13  import javax.sql.DataSource;
 14  import java.util.logging.Level;
 15  import java.util.logging.Logger;
 16  
 17  /**
 18   * Created by tqvarnst on 2017-04-04.
 19   */
 20  @Singleton
 21  @Startup
 22  @TransactionManagement(TransactionManagementType.BEAN)
 23  public class DataBaseMigrationStartup {
 24  
 25      @Inject
 26      Logger logger;
 27  
 28      @Resource(mappedName = "java:jboss/datasources/CoolstoreDS")
 29      DataSource dataSource;
 30  
 31      @PostConstruct
 32      private void startup() {
 33  
 34  
 35          try {
 36              logger.info("Initializing/migrating the database using FlyWay");
 37              Flyway flyway = new Flyway();
 38              flyway.setDataSource(dataSource);
 39              flyway.baseline();
 40              // Start the db.migration
 41              flyway.migrate();
 42          } catch (FlywayException e) {
 43              if(logger !=null)
 44                  logger.log(Level.SEVERE,"FAILED TO INITIALIZE THE DATABASE: " + e.getMessage(),e);
 45              else
 46                  System.out.println("FAILED TO INITIALIZE THE DATABASE: " + e.getMessage() + " and injection of logger doesn't work");
 47  
 48          }
 49      }
 50  
 51  
 52  
 53  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/utils/Producers.java
      * Replace the `javax.enterprise` import statement with `jakarta.enterprise`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.utils;
  2  
  3  import javax.enterprise.inject.Produces;
  4  import javax.enterprise.inject.spi.InjectionPoint;
  5  import java.util.logging.Logger;
  6  
  7  
  8  public class Producers {
  9  
 10      Logger log = Logger.getLogger(Producers.class.getName());
 11  
 12      @Produces
 13      public Logger produceLog(InjectionPoint injectionPoint) {
 14          return Logger.getLogger(injectionPoint.getMember().getDeclaringClass().getName());
 15      }
 16  
 17  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/utils/Producers.java
      * Replace the `javax.enterprise` import statement with `jakarta.enterprise`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.utils;
  2  
  3  import javax.enterprise.inject.Produces;
  4  import javax.enterprise.inject.spi.InjectionPoint;
  5  import java.util.logging.Logger;
  6  
  7  
  8  public class Producers {
  9  
 10      Logger log = Logger.getLogger(Producers.class.getName());
 11  
 12      @Produces
 13      public Logger produceLog(InjectionPoint injectionPoint) {
 14          return Logger.getLogger(injectionPoint.getMember().getDeclaringClass().getName());
 15      }
 16  
 17  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/utils/StartupListener.java
      * Replace the `javax.inject` import statement with `jakarta.inject`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.utils;
  2  
  3  import weblogic.application.ApplicationLifecycleEvent;
  4  import weblogic.application.ApplicationLifecycleListener;
  5  
  6  import javax.inject.Inject;
  7  import java.util.logging.Logger;
  8  
  9  public class StartupListener extends ApplicationLifecycleListener {
 10  
 11      @Inject
 12      Logger log;
 13  
 14      @Override
 15      public void postStart(ApplicationLifecycleEvent evt) {
 16          log.info("AppListener(postStart)");
 17      }
 18  
 19      @Override
 20      public void preStop(ApplicationLifecycleEvent evt) {
 21          log.info("AppListener(preStop)");
 22      }
 23  
 24  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/utils/Transformers.java
      * Replace the `javax.json` import statement with `jakarta.json`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.utils;
  2  
  3  import com.redhat.coolstore.model.CatalogItemEntity;
  4  import com.redhat.coolstore.model.Order;
  5  import com.redhat.coolstore.model.OrderItem;
  6  import com.redhat.coolstore.model.Product;
  7  import com.redhat.coolstore.model.ProductImpl;
  8  import com.redhat.coolstore.model.ShoppingCart;
  9  import java.io.StringReader;
 10  import java.io.StringWriter;
 11  import java.util.ArrayList;
 12  import java.util.List;
 13  import javax.json.Json;
 14  import javax.json.JsonArray;
 15  import javax.json.JsonArrayBuilder;
 16  import javax.json.JsonObject;
 17  import javax.json.JsonReader;
 18  import javax.json.JsonWriter;
 19  
 20  import java.util.concurrent.ThreadLocalRandom;
 21  import java.util.logging.Logger;
 22  
 23  /**
 24   * Created by tqvarnst on 2017-03-30.
 25   */
 26  public class Transformers {
 27  
 28      private static final String[] RANDOM_NAMES = {"Sven Karlsson","Johan Andersson","Karl Svensson","Anders Johansson","Stefan Olson","Martin Ericsson"};
 29      private static final String[] RANDOM_EMAILS = {"sven@gmail.com","johan@gmail.com","karl@gmail.com","anders@gmail.com","stefan@gmail.com","martin@gmail.com"};
 30  
 31      private static Logger log = Logger.getLogger(Transformers.class.getName());
 32  
 33      public static Product toProduct(CatalogItemEntity entity) {
 34          ProductImpl prod = new ProductImpl();
 35          prod.setItemId(entity.getItemId());
 36          prod.setName(entity.getName());
 37          prod.setDesc(entity.getDesc());
 38          prod.setPrice(entity.getPrice());
 39          if (entity.getInventory() != null) {
 40              prod.setLocation(entity.getInventory().getLocation());
 41              prod.setLink(entity.getInventory().getLink());
 42              prod.setQuantity(entity.getInventory().getQuantity());
 43          } else {
 44              log.warning("Inventory for " + entity.getName() + "[" + entity.getItemId()+ "] unknown and missing");
 45          }
 46          return prod;
 47      }
 48  
 49      public static String shoppingCartToJson(ShoppingCart cart) {
 50          JsonArrayBuilder cartItems = Json.createArrayBuilder();
 51          cart.getShoppingCartItemList().forEach(item -> {
 52              cartItems.add(Json.createObjectBuilder()
 53                  .add("productSku",item.getProduct().getItemId())
 54                  .add("quantity",item.getQuantity())
 55              );
 56          });
 57  
 58          int randomNameAndEmailIndex = ThreadLocalRandom.current().nextInt(RANDOM_NAMES.length);
 59  
 60          JsonObject jsonObject = Json.createObjectBuilder()
 61              .add("orderValue", Double.valueOf(cart.getCartTotal()))
 62              .add("customerName",RANDOM_NAMES[randomNameAndEmailIndex])
 63              .add("customerEmail",RANDOM_EMAILS[randomNameAndEmailIndex])
 64              .add("retailPrice", cart.getShoppingCartItemList().stream().mapToDouble(i -> i.getQuantity()*i.getPrice()).sum())
 65              .add("discount", Double.valueOf(cart.getCartItemPromoSavings()))
 66              .add("shippingFee", Double.valueOf(cart.getShippingTotal()))
 67              .add("shippingDiscount", Double.valueOf(cart.getShippingPromoSavings()))
 68              .add("items",cartItems) 
 69              .build();
 70          StringWriter w = new StringWriter();
 71          try (JsonWriter writer = Json.createWriter(w)) {
 72              writer.write(jsonObject);
 73          }
 74          return w.toString();
 75      }
 76  
 77      public static Order jsonToOrder(String json) {
 78          JsonReader jsonReader = Json.createReader(new StringReader(json));
 79          JsonObject rootObject = jsonReader.readObject();
 80          Order order = new Order();
 81          order.setCustomerName(rootObject.getString("customerName"));
 82          order.setCustomerEmail(rootObject.getString("customerEmail"));
 83          order.setOrderValue(rootObject.getJsonNumber("orderValue").doubleValue());
 84          order.setRetailPrice(rootObject.getJsonNumber("retailPrice").doubleValue());
 85          order.setDiscount(rootObject.getJsonNumber("discount").doubleValue());
 86          order.setShippingFee(rootObject.getJsonNumber("shippingFee").doubleValue());
 87          order.setShippingDiscount(rootObject.getJsonNumber("shippingDiscount").doubleValue());
 88          JsonArray jsonItems = rootObject.getJsonArray("items");
 89          List<OrderItem> items = new ArrayList<OrderItem>(jsonItems.size());
 90          for (JsonObject jsonItem : jsonItems.getValuesAs(JsonObject.class)) {
 91              OrderItem oi = new OrderItem();
 92              oi.setProductId(jsonItem.getString("productSku"));
 93              oi.setQuantity(jsonItem.getInt("quantity"));
 94              items.add(oi);
 95          }
 96          order.setItemList(items); 
 97          return order;
 98      }
 99  
100  
101  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/utils/Transformers.java
      * Replace the `javax.json` import statement with `jakarta.json`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.utils;
  2  
  3  import com.redhat.coolstore.model.CatalogItemEntity;
  4  import com.redhat.coolstore.model.Order;
  5  import com.redhat.coolstore.model.OrderItem;
  6  import com.redhat.coolstore.model.Product;
  7  import com.redhat.coolstore.model.ProductImpl;
  8  import com.redhat.coolstore.model.ShoppingCart;
  9  import java.io.StringReader;
 10  import java.io.StringWriter;
 11  import java.util.ArrayList;
 12  import java.util.List;
 13  import javax.json.Json;
 14  import javax.json.JsonArray;
 15  import javax.json.JsonArrayBuilder;
 16  import javax.json.JsonObject;
 17  import javax.json.JsonReader;
 18  import javax.json.JsonWriter;
 19  
 20  import java.util.concurrent.ThreadLocalRandom;
 21  import java.util.logging.Logger;
 22  
 23  /**
 24   * Created by tqvarnst on 2017-03-30.
 25   */
 26  public class Transformers {
 27  
 28      private static final String[] RANDOM_NAMES = {"Sven Karlsson","Johan Andersson","Karl Svensson","Anders Johansson","Stefan Olson","Martin Ericsson"};
 29      private static final String[] RANDOM_EMAILS = {"sven@gmail.com","johan@gmail.com","karl@gmail.com","anders@gmail.com","stefan@gmail.com","martin@gmail.com"};
 30  
 31      private static Logger log = Logger.getLogger(Transformers.class.getName());
 32  
 33      public static Product toProduct(CatalogItemEntity entity) {
 34          ProductImpl prod = new ProductImpl();
 35          prod.setItemId(entity.getItemId());
 36          prod.setName(entity.getName());
 37          prod.setDesc(entity.getDesc());
 38          prod.setPrice(entity.getPrice());
 39          if (entity.getInventory() != null) {
 40              prod.setLocation(entity.getInventory().getLocation());
 41              prod.setLink(entity.getInventory().getLink());
 42              prod.setQuantity(entity.getInventory().getQuantity());
 43          } else {
 44              log.warning("Inventory for " + entity.getName() + "[" + entity.getItemId()+ "] unknown and missing");
 45          }
 46          return prod;
 47      }
 48  
 49      public static String shoppingCartToJson(ShoppingCart cart) {
 50          JsonArrayBuilder cartItems = Json.createArrayBuilder();
 51          cart.getShoppingCartItemList().forEach(item -> {
 52              cartItems.add(Json.createObjectBuilder()
 53                  .add("productSku",item.getProduct().getItemId())
 54                  .add("quantity",item.getQuantity())
 55              );
 56          });
 57  
 58          int randomNameAndEmailIndex = ThreadLocalRandom.current().nextInt(RANDOM_NAMES.length);
 59  
 60          JsonObject jsonObject = Json.createObjectBuilder()
 61              .add("orderValue", Double.valueOf(cart.getCartTotal()))
 62              .add("customerName",RANDOM_NAMES[randomNameAndEmailIndex])
 63              .add("customerEmail",RANDOM_EMAILS[randomNameAndEmailIndex])
 64              .add("retailPrice", cart.getShoppingCartItemList().stream().mapToDouble(i -> i.getQuantity()*i.getPrice()).sum())
 65              .add("discount", Double.valueOf(cart.getCartItemPromoSavings()))
 66              .add("shippingFee", Double.valueOf(cart.getShippingTotal()))
 67              .add("shippingDiscount", Double.valueOf(cart.getShippingPromoSavings()))
 68              .add("items",cartItems) 
 69              .build();
 70          StringWriter w = new StringWriter();
 71          try (JsonWriter writer = Json.createWriter(w)) {
 72              writer.write(jsonObject);
 73          }
 74          return w.toString();
 75      }
 76  
 77      public static Order jsonToOrder(String json) {
 78          JsonReader jsonReader = Json.createReader(new StringReader(json));
 79          JsonObject rootObject = jsonReader.readObject();
 80          Order order = new Order();
 81          order.setCustomerName(rootObject.getString("customerName"));
 82          order.setCustomerEmail(rootObject.getString("customerEmail"));
 83          order.setOrderValue(rootObject.getJsonNumber("orderValue").doubleValue());
 84          order.setRetailPrice(rootObject.getJsonNumber("retailPrice").doubleValue());
 85          order.setDiscount(rootObject.getJsonNumber("discount").doubleValue());
 86          order.setShippingFee(rootObject.getJsonNumber("shippingFee").doubleValue());
 87          order.setShippingDiscount(rootObject.getJsonNumber("shippingDiscount").doubleValue());
 88          JsonArray jsonItems = rootObject.getJsonArray("items");
 89          List<OrderItem> items = new ArrayList<OrderItem>(jsonItems.size());
 90          for (JsonObject jsonItem : jsonItems.getValuesAs(JsonObject.class)) {
 91              OrderItem oi = new OrderItem();
 92              oi.setProductId(jsonItem.getString("productSku"));
 93              oi.setQuantity(jsonItem.getInt("quantity"));
 94              items.add(oi);
 95          }
 96          order.setItemList(items); 
 97          return order;
 98      }
 99  
100  
101  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/utils/Transformers.java
      * Replace the `javax.json` import statement with `jakarta.json`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.utils;
  2  
  3  import com.redhat.coolstore.model.CatalogItemEntity;
  4  import com.redhat.coolstore.model.Order;
  5  import com.redhat.coolstore.model.OrderItem;
  6  import com.redhat.coolstore.model.Product;
  7  import com.redhat.coolstore.model.ProductImpl;
  8  import com.redhat.coolstore.model.ShoppingCart;
  9  import java.io.StringReader;
 10  import java.io.StringWriter;
 11  import java.util.ArrayList;
 12  import java.util.List;
 13  import javax.json.Json;
 14  import javax.json.JsonArray;
 15  import javax.json.JsonArrayBuilder;
 16  import javax.json.JsonObject;
 17  import javax.json.JsonReader;
 18  import javax.json.JsonWriter;
 19  
 20  import java.util.concurrent.ThreadLocalRandom;
 21  import java.util.logging.Logger;
 22  
 23  /**
 24   * Created by tqvarnst on 2017-03-30.
 25   */
 26  public class Transformers {
 27  
 28      private static final String[] RANDOM_NAMES = {"Sven Karlsson","Johan Andersson","Karl Svensson","Anders Johansson","Stefan Olson","Martin Ericsson"};
 29      private static final String[] RANDOM_EMAILS = {"sven@gmail.com","johan@gmail.com","karl@gmail.com","anders@gmail.com","stefan@gmail.com","martin@gmail.com"};
 30  
 31      private static Logger log = Logger.getLogger(Transformers.class.getName());
 32  
 33      public static Product toProduct(CatalogItemEntity entity) {
 34          ProductImpl prod = new ProductImpl();
 35          prod.setItemId(entity.getItemId());
 36          prod.setName(entity.getName());
 37          prod.setDesc(entity.getDesc());
 38          prod.setPrice(entity.getPrice());
 39          if (entity.getInventory() != null) {
 40              prod.setLocation(entity.getInventory().getLocation());
 41              prod.setLink(entity.getInventory().getLink());
 42              prod.setQuantity(entity.getInventory().getQuantity());
 43          } else {
 44              log.warning("Inventory for " + entity.getName() + "[" + entity.getItemId()+ "] unknown and missing");
 45          }
 46          return prod;
 47      }
 48  
 49      public static String shoppingCartToJson(ShoppingCart cart) {
 50          JsonArrayBuilder cartItems = Json.createArrayBuilder();
 51          cart.getShoppingCartItemList().forEach(item -> {
 52              cartItems.add(Json.createObjectBuilder()
 53                  .add("productSku",item.getProduct().getItemId())
 54                  .add("quantity",item.getQuantity())
 55              );
 56          });
 57  
 58          int randomNameAndEmailIndex = ThreadLocalRandom.current().nextInt(RANDOM_NAMES.length);
 59  
 60          JsonObject jsonObject = Json.createObjectBuilder()
 61              .add("orderValue", Double.valueOf(cart.getCartTotal()))
 62              .add("customerName",RANDOM_NAMES[randomNameAndEmailIndex])
 63              .add("customerEmail",RANDOM_EMAILS[randomNameAndEmailIndex])
 64              .add("retailPrice", cart.getShoppingCartItemList().stream().mapToDouble(i -> i.getQuantity()*i.getPrice()).sum())
 65              .add("discount", Double.valueOf(cart.getCartItemPromoSavings()))
 66              .add("shippingFee", Double.valueOf(cart.getShippingTotal()))
 67              .add("shippingDiscount", Double.valueOf(cart.getShippingPromoSavings()))
 68              .add("items",cartItems) 
 69              .build();
 70          StringWriter w = new StringWriter();
 71          try (JsonWriter writer = Json.createWriter(w)) {
 72              writer.write(jsonObject);
 73          }
 74          return w.toString();
 75      }
 76  
 77      public static Order jsonToOrder(String json) {
 78          JsonReader jsonReader = Json.createReader(new StringReader(json));
 79          JsonObject rootObject = jsonReader.readObject();
 80          Order order = new Order();
 81          order.setCustomerName(rootObject.getString("customerName"));
 82          order.setCustomerEmail(rootObject.getString("customerEmail"));
 83          order.setOrderValue(rootObject.getJsonNumber("orderValue").doubleValue());
 84          order.setRetailPrice(rootObject.getJsonNumber("retailPrice").doubleValue());
 85          order.setDiscount(rootObject.getJsonNumber("discount").doubleValue());
 86          order.setShippingFee(rootObject.getJsonNumber("shippingFee").doubleValue());
 87          order.setShippingDiscount(rootObject.getJsonNumber("shippingDiscount").doubleValue());
 88          JsonArray jsonItems = rootObject.getJsonArray("items");
 89          List<OrderItem> items = new ArrayList<OrderItem>(jsonItems.size());
 90          for (JsonObject jsonItem : jsonItems.getValuesAs(JsonObject.class)) {
 91              OrderItem oi = new OrderItem();
 92              oi.setProductId(jsonItem.getString("productSku"));
 93              oi.setQuantity(jsonItem.getInt("quantity"));
 94              items.add(oi);
 95          }
 96          order.setItemList(items); 
 97          return order;
 98      }
 99  
100  
101  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/utils/Transformers.java
      * Replace the `javax.json` import statement with `jakarta.json`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.utils;
  2  
  3  import com.redhat.coolstore.model.CatalogItemEntity;
  4  import com.redhat.coolstore.model.Order;
  5  import com.redhat.coolstore.model.OrderItem;
  6  import com.redhat.coolstore.model.Product;
  7  import com.redhat.coolstore.model.ProductImpl;
  8  import com.redhat.coolstore.model.ShoppingCart;
  9  import java.io.StringReader;
 10  import java.io.StringWriter;
 11  import java.util.ArrayList;
 12  import java.util.List;
 13  import javax.json.Json;
 14  import javax.json.JsonArray;
 15  import javax.json.JsonArrayBuilder;
 16  import javax.json.JsonObject;
 17  import javax.json.JsonReader;
 18  import javax.json.JsonWriter;
 19  
 20  import java.util.concurrent.ThreadLocalRandom;
 21  import java.util.logging.Logger;
 22  
 23  /**
 24   * Created by tqvarnst on 2017-03-30.
 25   */
 26  public class Transformers {
 27  
 28      private static final String[] RANDOM_NAMES = {"Sven Karlsson","Johan Andersson","Karl Svensson","Anders Johansson","Stefan Olson","Martin Ericsson"};
 29      private static final String[] RANDOM_EMAILS = {"sven@gmail.com","johan@gmail.com","karl@gmail.com","anders@gmail.com","stefan@gmail.com","martin@gmail.com"};
 30  
 31      private static Logger log = Logger.getLogger(Transformers.class.getName());
 32  
 33      public static Product toProduct(CatalogItemEntity entity) {
 34          ProductImpl prod = new ProductImpl();
 35          prod.setItemId(entity.getItemId());
 36          prod.setName(entity.getName());
 37          prod.setDesc(entity.getDesc());
 38          prod.setPrice(entity.getPrice());
 39          if (entity.getInventory() != null) {
 40              prod.setLocation(entity.getInventory().getLocation());
 41              prod.setLink(entity.getInventory().getLink());
 42              prod.setQuantity(entity.getInventory().getQuantity());
 43          } else {
 44              log.warning("Inventory for " + entity.getName() + "[" + entity.getItemId()+ "] unknown and missing");
 45          }
 46          return prod;
 47      }
 48  
 49      public static String shoppingCartToJson(ShoppingCart cart) {
 50          JsonArrayBuilder cartItems = Json.createArrayBuilder();
 51          cart.getShoppingCartItemList().forEach(item -> {
 52              cartItems.add(Json.createObjectBuilder()
 53                  .add("productSku",item.getProduct().getItemId())
 54                  .add("quantity",item.getQuantity())
 55              );
 56          });
 57  
 58          int randomNameAndEmailIndex = ThreadLocalRandom.current().nextInt(RANDOM_NAMES.length);
 59  
 60          JsonObject jsonObject = Json.createObjectBuilder()
 61              .add("orderValue", Double.valueOf(cart.getCartTotal()))
 62              .add("customerName",RANDOM_NAMES[randomNameAndEmailIndex])
 63              .add("customerEmail",RANDOM_EMAILS[randomNameAndEmailIndex])
 64              .add("retailPrice", cart.getShoppingCartItemList().stream().mapToDouble(i -> i.getQuantity()*i.getPrice()).sum())
 65              .add("discount", Double.valueOf(cart.getCartItemPromoSavings()))
 66              .add("shippingFee", Double.valueOf(cart.getShippingTotal()))
 67              .add("shippingDiscount", Double.valueOf(cart.getShippingPromoSavings()))
 68              .add("items",cartItems) 
 69              .build();
 70          StringWriter w = new StringWriter();
 71          try (JsonWriter writer = Json.createWriter(w)) {
 72              writer.write(jsonObject);
 73          }
 74          return w.toString();
 75      }
 76  
 77      public static Order jsonToOrder(String json) {
 78          JsonReader jsonReader = Json.createReader(new StringReader(json));
 79          JsonObject rootObject = jsonReader.readObject();
 80          Order order = new Order();
 81          order.setCustomerName(rootObject.getString("customerName"));
 82          order.setCustomerEmail(rootObject.getString("customerEmail"));
 83          order.setOrderValue(rootObject.getJsonNumber("orderValue").doubleValue());
 84          order.setRetailPrice(rootObject.getJsonNumber("retailPrice").doubleValue());
 85          order.setDiscount(rootObject.getJsonNumber("discount").doubleValue());
 86          order.setShippingFee(rootObject.getJsonNumber("shippingFee").doubleValue());
 87          order.setShippingDiscount(rootObject.getJsonNumber("shippingDiscount").doubleValue());
 88          JsonArray jsonItems = rootObject.getJsonArray("items");
 89          List<OrderItem> items = new ArrayList<OrderItem>(jsonItems.size());
 90          for (JsonObject jsonItem : jsonItems.getValuesAs(JsonObject.class)) {
 91              OrderItem oi = new OrderItem();
 92              oi.setProductId(jsonItem.getString("productSku"));
 93              oi.setQuantity(jsonItem.getInt("quantity"));
 94              items.add(oi);
 95          }
 96          order.setItemList(items); 
 97          return order;
 98      }
 99  
100  
101  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/utils/Transformers.java
      * Replace the `javax.json` import statement with `jakarta.json`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.utils;
  2  
  3  import com.redhat.coolstore.model.CatalogItemEntity;
  4  import com.redhat.coolstore.model.Order;
  5  import com.redhat.coolstore.model.OrderItem;
  6  import com.redhat.coolstore.model.Product;
  7  import com.redhat.coolstore.model.ProductImpl;
  8  import com.redhat.coolstore.model.ShoppingCart;
  9  import java.io.StringReader;
 10  import java.io.StringWriter;
 11  import java.util.ArrayList;
 12  import java.util.List;
 13  import javax.json.Json;
 14  import javax.json.JsonArray;
 15  import javax.json.JsonArrayBuilder;
 16  import javax.json.JsonObject;
 17  import javax.json.JsonReader;
 18  import javax.json.JsonWriter;
 19  
 20  import java.util.concurrent.ThreadLocalRandom;
 21  import java.util.logging.Logger;
 22  
 23  /**
 24   * Created by tqvarnst on 2017-03-30.
 25   */
 26  public class Transformers {
 27  
 28      private static final String[] RANDOM_NAMES = {"Sven Karlsson","Johan Andersson","Karl Svensson","Anders Johansson","Stefan Olson","Martin Ericsson"};
 29      private static final String[] RANDOM_EMAILS = {"sven@gmail.com","johan@gmail.com","karl@gmail.com","anders@gmail.com","stefan@gmail.com","martin@gmail.com"};
 30  
 31      private static Logger log = Logger.getLogger(Transformers.class.getName());
 32  
 33      public static Product toProduct(CatalogItemEntity entity) {
 34          ProductImpl prod = new ProductImpl();
 35          prod.setItemId(entity.getItemId());
 36          prod.setName(entity.getName());
 37          prod.setDesc(entity.getDesc());
 38          prod.setPrice(entity.getPrice());
 39          if (entity.getInventory() != null) {
 40              prod.setLocation(entity.getInventory().getLocation());
 41              prod.setLink(entity.getInventory().getLink());
 42              prod.setQuantity(entity.getInventory().getQuantity());
 43          } else {
 44              log.warning("Inventory for " + entity.getName() + "[" + entity.getItemId()+ "] unknown and missing");
 45          }
 46          return prod;
 47      }
 48  
 49      public static String shoppingCartToJson(ShoppingCart cart) {
 50          JsonArrayBuilder cartItems = Json.createArrayBuilder();
 51          cart.getShoppingCartItemList().forEach(item -> {
 52              cartItems.add(Json.createObjectBuilder()
 53                  .add("productSku",item.getProduct().getItemId())
 54                  .add("quantity",item.getQuantity())
 55              );
 56          });
 57  
 58          int randomNameAndEmailIndex = ThreadLocalRandom.current().nextInt(RANDOM_NAMES.length);
 59  
 60          JsonObject jsonObject = Json.createObjectBuilder()
 61              .add("orderValue", Double.valueOf(cart.getCartTotal()))
 62              .add("customerName",RANDOM_NAMES[randomNameAndEmailIndex])
 63              .add("customerEmail",RANDOM_EMAILS[randomNameAndEmailIndex])
 64              .add("retailPrice", cart.getShoppingCartItemList().stream().mapToDouble(i -> i.getQuantity()*i.getPrice()).sum())
 65              .add("discount", Double.valueOf(cart.getCartItemPromoSavings()))
 66              .add("shippingFee", Double.valueOf(cart.getShippingTotal()))
 67              .add("shippingDiscount", Double.valueOf(cart.getShippingPromoSavings()))
 68              .add("items",cartItems) 
 69              .build();
 70          StringWriter w = new StringWriter();
 71          try (JsonWriter writer = Json.createWriter(w)) {
 72              writer.write(jsonObject);
 73          }
 74          return w.toString();
 75      }
 76  
 77      public static Order jsonToOrder(String json) {
 78          JsonReader jsonReader = Json.createReader(new StringReader(json));
 79          JsonObject rootObject = jsonReader.readObject();
 80          Order order = new Order();
 81          order.setCustomerName(rootObject.getString("customerName"));
 82          order.setCustomerEmail(rootObject.getString("customerEmail"));
 83          order.setOrderValue(rootObject.getJsonNumber("orderValue").doubleValue());
 84          order.setRetailPrice(rootObject.getJsonNumber("retailPrice").doubleValue());
 85          order.setDiscount(rootObject.getJsonNumber("discount").doubleValue());
 86          order.setShippingFee(rootObject.getJsonNumber("shippingFee").doubleValue());
 87          order.setShippingDiscount(rootObject.getJsonNumber("shippingDiscount").doubleValue());
 88          JsonArray jsonItems = rootObject.getJsonArray("items");
 89          List<OrderItem> items = new ArrayList<OrderItem>(jsonItems.size());
 90          for (JsonObject jsonItem : jsonItems.getValuesAs(JsonObject.class)) {
 91              OrderItem oi = new OrderItem();
 92              oi.setProductId(jsonItem.getString("productSku"));
 93              oi.setQuantity(jsonItem.getInt("quantity"));
 94              items.add(oi);
 95          }
 96          order.setItemList(items); 
 97          return order;
 98      }
 99  
100  
101  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/utils/Transformers.java
      * Replace the `javax.json` import statement with `jakarta.json`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.utils;
  2  
  3  import com.redhat.coolstore.model.CatalogItemEntity;
  4  import com.redhat.coolstore.model.Order;
  5  import com.redhat.coolstore.model.OrderItem;
  6  import com.redhat.coolstore.model.Product;
  7  import com.redhat.coolstore.model.ProductImpl;
  8  import com.redhat.coolstore.model.ShoppingCart;
  9  import java.io.StringReader;
 10  import java.io.StringWriter;
 11  import java.util.ArrayList;
 12  import java.util.List;
 13  import javax.json.Json;
 14  import javax.json.JsonArray;
 15  import javax.json.JsonArrayBuilder;
 16  import javax.json.JsonObject;
 17  import javax.json.JsonReader;
 18  import javax.json.JsonWriter;
 19  
 20  import java.util.concurrent.ThreadLocalRandom;
 21  import java.util.logging.Logger;
 22  
 23  /**
 24   * Created by tqvarnst on 2017-03-30.
 25   */
 26  public class Transformers {
 27  
 28      private static final String[] RANDOM_NAMES = {"Sven Karlsson","Johan Andersson","Karl Svensson","Anders Johansson","Stefan Olson","Martin Ericsson"};
 29      private static final String[] RANDOM_EMAILS = {"sven@gmail.com","johan@gmail.com","karl@gmail.com","anders@gmail.com","stefan@gmail.com","martin@gmail.com"};
 30  
 31      private static Logger log = Logger.getLogger(Transformers.class.getName());
 32  
 33      public static Product toProduct(CatalogItemEntity entity) {
 34          ProductImpl prod = new ProductImpl();
 35          prod.setItemId(entity.getItemId());
 36          prod.setName(entity.getName());
 37          prod.setDesc(entity.getDesc());
 38          prod.setPrice(entity.getPrice());
 39          if (entity.getInventory() != null) {
 40              prod.setLocation(entity.getInventory().getLocation());
 41              prod.setLink(entity.getInventory().getLink());
 42              prod.setQuantity(entity.getInventory().getQuantity());
 43          } else {
 44              log.warning("Inventory for " + entity.getName() + "[" + entity.getItemId()+ "] unknown and missing");
 45          }
 46          return prod;
 47      }
 48  
 49      public static String shoppingCartToJson(ShoppingCart cart) {
 50          JsonArrayBuilder cartItems = Json.createArrayBuilder();
 51          cart.getShoppingCartItemList().forEach(item -> {
 52              cartItems.add(Json.createObjectBuilder()
 53                  .add("productSku",item.getProduct().getItemId())
 54                  .add("quantity",item.getQuantity())
 55              );
 56          });
 57  
 58          int randomNameAndEmailIndex = ThreadLocalRandom.current().nextInt(RANDOM_NAMES.length);
 59  
 60          JsonObject jsonObject = Json.createObjectBuilder()
 61              .add("orderValue", Double.valueOf(cart.getCartTotal()))
 62              .add("customerName",RANDOM_NAMES[randomNameAndEmailIndex])
 63              .add("customerEmail",RANDOM_EMAILS[randomNameAndEmailIndex])
 64              .add("retailPrice", cart.getShoppingCartItemList().stream().mapToDouble(i -> i.getQuantity()*i.getPrice()).sum())
 65              .add("discount", Double.valueOf(cart.getCartItemPromoSavings()))
 66              .add("shippingFee", Double.valueOf(cart.getShippingTotal()))
 67              .add("shippingDiscount", Double.valueOf(cart.getShippingPromoSavings()))
 68              .add("items",cartItems) 
 69              .build();
 70          StringWriter w = new StringWriter();
 71          try (JsonWriter writer = Json.createWriter(w)) {
 72              writer.write(jsonObject);
 73          }
 74          return w.toString();
 75      }
 76  
 77      public static Order jsonToOrder(String json) {
 78          JsonReader jsonReader = Json.createReader(new StringReader(json));
 79          JsonObject rootObject = jsonReader.readObject();
 80          Order order = new Order();
 81          order.setCustomerName(rootObject.getString("customerName"));
 82          order.setCustomerEmail(rootObject.getString("customerEmail"));
 83          order.setOrderValue(rootObject.getJsonNumber("orderValue").doubleValue());
 84          order.setRetailPrice(rootObject.getJsonNumber("retailPrice").doubleValue());
 85          order.setDiscount(rootObject.getJsonNumber("discount").doubleValue());
 86          order.setShippingFee(rootObject.getJsonNumber("shippingFee").doubleValue());
 87          order.setShippingDiscount(rootObject.getJsonNumber("shippingDiscount").doubleValue());
 88          JsonArray jsonItems = rootObject.getJsonArray("items");
 89          List<OrderItem> items = new ArrayList<OrderItem>(jsonItems.size());
 90          for (JsonObject jsonItem : jsonItems.getValuesAs(JsonObject.class)) {
 91              OrderItem oi = new OrderItem();
 92              oi.setProductId(jsonItem.getString("productSku"));
 93              oi.setQuantity(jsonItem.getInt("quantity"));
 94              items.add(oi);
 95          }
 96          order.setItemList(items); 
 97          return order;
 98      }
 99  
100  
101  }

```
### #12 - javax-to-jakarta-properties-00001
* Category: mandatory
* Effort: 1
* Description: Rename properties prefixed by javax with jakarta 
Rename properties prefixed by `javax` with `jakarta`
* Labels: konveyor.io/target=jakarta-ee9+, konveyor.io/target=jakarta-ee, konveyor.io/target=eap8, konveyor.io/target=eap, konveyor.io/source
* Links
  * Jakarta EE: https://jakarta.ee/
* Incidents
  * file:///opt/input/source/target/classes/META-INF/persistence.xml
      * Rename properties prefixed by `javax` with `jakarta`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <persistence version="2.1"
  3               xmlns="http://xmlns.jcp.org/xml/ns/persistence" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  4               xsi:schemaLocation="
  5          http://xmlns.jcp.org/xml/ns/persistence
  6          http://xmlns.jcp.org/xml/ns/persistence/persistence_2_1.xsd">
  7      <persistence-unit name="primary">
  8          <jta-data-source>java:jboss/datasources/CoolstoreDS</jta-data-source>
  9          <properties>
 10              <property name="javax.persistence.schema-generation.database.action" value="none"/>
 11              <property name="hibernate.show_sql" value="false" />
 12          </properties>
 13      </persistence-unit>
 14  </persistence>

```
  * file:///opt/input/source/src/main/resources/META-INF/persistence.xml
      * Rename properties prefixed by `javax` with `jakarta`
      * Code Snippet:
```java
  1  <?xml version="1.0" encoding="UTF-8"?>
  2  <persistence version="2.1"
  3               xmlns="http://xmlns.jcp.org/xml/ns/persistence" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  4               xsi:schemaLocation="
  5          http://xmlns.jcp.org/xml/ns/persistence
  6          http://xmlns.jcp.org/xml/ns/persistence/persistence_2_1.xsd">
  7      <persistence-unit name="primary">
  8          <jta-data-source>java:jboss/datasources/CoolstoreDS</jta-data-source>
  9          <properties>
 10              <property name="javax.persistence.schema-generation.database.action" value="none"/>
 11              <property name="hibernate.show_sql" value="false" />
 12          </properties>
 13      </persistence-unit>
 14  </persistence>

```
