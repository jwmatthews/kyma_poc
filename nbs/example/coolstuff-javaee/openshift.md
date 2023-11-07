# openshift
## Description
This ruleset detects the Java Mail API, which may be problematic when migrating an application to a cloud environment.
* Source of rules: https://github.com/konveyor/rulesets/tree/main/default/generated/quarkus
* Sample application: https://github.com/deewhyweb/eap-coolstore-monolith
## Violations
Number of Violations: 1
### #0 - session-00000
* Category: mandatory
* Effort: 3
* Description: HTTP session replication (distributable web.xml)
Session replication ensures that client sessions are not disrupted by node failure. Each node in the cluster shares information about ongoing sessions and can take over sessions if another node disappears. In a cloud environment, however, data in the memory of a running container can be wiped out by a restart.. Recommendations. * Review the session replication usage and ensure that it is configured properly.. * Disable HTTP session clustering and accept its implications.. * Re-architect the application so that sessions are stored in a cache backing service or a remote data grid.. A remote data grid has the following benefits:. * The application is more scaleable and elastic.. * The application can survive EAP node failures because a JVM failure does not cause session data loss.. * Session data can be shared by multiple applications.
* Labels: konveyor.io/source=java, konveyor.io/source=java-ee, konveyor.io/target=cloud-readiness, clustering
* Links
  * JBoss EAP: Clustering in Web Applications: https://access.redhat.com/documentation/en-us/red_hat_jboss_enterprise_application_platform/7.3/html/development_guide/clustering_in_web_applications
  * Twelve-Factor App: Processes: https://12factor.net/processes
  * Getting Started with JBoss EAP for OpenShift Container Platform: Clustering: https://access.redhat.com/documentation/en-us/red_hat_jboss_enterprise_application_platform/7.3/html-single/getting_started_with_jboss_eap_for_openshift_container_platform/index#reference_clustering
  * Twelve-Factor App: Backing services: https://12factor.net/backing-services
  * Running Data Grid on OpenShift: https://access.redhat.com/documentation/en-us/red_hat_data_grid/8.0/html-single/running_data_grid_on_openshift/index
  * JBoss EAP:  Externalize HTTP Sessions to Red Hat Data Grid: https://access.redhat.com/documentation/en-us/red_hat_jboss_enterprise_application_platform/7.3/html-single/configuration_guide/index#jdg_externalize_http_sessions
* Incidents
  * file:///opt/input/source/src/main/webapp/WEB-INF/web.xml
      * Session replication ensures that client sessions are not disrupted by node failure. Each node in the cluster shares information about ongoing sessions and can take over sessions if another node disappears. In a cloud environment, however, data in the memory of a running container can be wiped out by a restart.. Recommendations. * Review the session replication usage and ensure that it is configured properly.. * Disable HTTP session clustering and accept its implications.. * Re-architect the application so that sessions are stored in a cache backing service or a remote data grid.. A remote data grid has the following benefits:. * The application is more scaleable and elastic.. * The application can survive EAP node failures because a JVM failure does not cause session data loss.. * Session data can be shared by multiple applications.
