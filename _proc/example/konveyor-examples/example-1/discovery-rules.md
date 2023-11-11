# discovery-rules
## Description

* Source of rules: https://github.com/konveyor/rulesets/tree/main/default/generated
* Sample application: https://github.com/deewhyweb/eap-coolstore-monolith
## Violations
Number of Violations: 1
### #0 - hardcoded-ip-address
* Category: mandatory
* Effort: 1
* Description: Hardcoded IP Address
When migrating environments, hard-coded IP addresses may need to be modified or eliminated.
* Labels: konveyor.io/target=cloud-readiness, discovery
* Incidents
  * file:///opt/input/source/target/classes/persistence.properties
      * When migrating environments, hard-coded IP addresses may need to be modified or eliminated.
      * Code Snippet:
```java
  1  jdbc.driverClassName=oracle.jdbc.driver.OracleDriver
  2  jdbc.url=jdbc:oracle:thin:@169.60.225.216:1521/XEPDB1
  3  jdbc.user=customers
  4  jdbc.password=customers
  5  hibernate.hbm2ddl.auto=create-drop
  6  hibernate.dialect=org.hibernate.dialect.OracleDialect

```
  * file:///opt/input/source/src/main/resources/persistence.properties
      * When migrating environments, hard-coded IP addresses may need to be modified or eliminated.
      * Code Snippet:
```java
  1  jdbc.driverClassName=oracle.jdbc.driver.OracleDriver
  2  jdbc.url=jdbc:oracle:thin:@169.60.225.216:1521/XEPDB1
  3  jdbc.user=customers
  4  jdbc.password=customers
  5  hibernate.hbm2ddl.auto=create-drop
  6  hibernate.dialect=org.hibernate.dialect.OracleDialect

```
