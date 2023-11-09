# openshift
## Description
This ruleset detects the Java Mail API, which may be problematic when migrating an application to a cloud environment.
* Source of rules: https://github.com/konveyor/rulesets/tree/main/default/generated/quarkus
* Sample application: https://github.com/deewhyweb/eap-coolstore-monolith
## Violations
Number of Violations: 2
### #0 - jni-native-code-00000
* Category: mandatory
* Effort: 7
* Description: Java native libraries (JNI, JNA)
Java native libraries might not run in a cloud or container environment.. Recommendations. * Review the purpose of the native library in your application.. * Check whether the native library is compatible with a cloud environment.. * Reuse or embed the native library or application in a cloud environment, for example, in a JBoss module.. * Replace, remove, or rewrite the native library or application using a cloud-compatible equivalent.
* Labels: konveyor.io/target=cloud-readiness, konveyor.io/source, jni
* Links
  * How to load native libraries and access them via JNI in EAP (with or without a module): https://access.redhat.com/solutions/229443
  * Is it supported to compile the JNI code as 32-bit shared libraries and use it in 64-bit compiled Java code ?: https://access.redhat.com/solutions/1444643
* Incidents
  * file:///root/.m2/repository/io/konveyor/demo/config-utils/1.0.0/io/konveyor/demo/config/ApplicationConfiguration.java
      * Java native libraries might not run in a cloud or container environment.. Recommendations. * Review the purpose of the native library in your application.. * Check whether the native library is compatible with a cloud environment.. * Reuse or embed the native library or application in a cloud environment, for example, in a JBoss module.. * Replace, remove, or rewrite the native library or application using a cloud-compatible equivalent.
      * Code Snippet:
```java
  1  package io.konveyor.demo.config;
  2  
  3  import java.io.FileInputStream;
  4  import java.io.InputStream;
  5  import java.util.Properties;
  6  
  7  public class ApplicationConfiguration {
  8  
  9  	private Properties config;
 10  
 11  	public ApplicationConfiguration() {
 12  		super();
 13  		this.config = loadProperties();
 14  
 15  	}
 16  
 17  	private Properties loadProperties() {
 18  		Properties properties = new Properties();
 19  
 20  		try (InputStream inputStream = new FileInputStream("/opt/config/persistence.properties")) {
 21  
 22  			properties.load(inputStream);
 23  
 24  		} catch (Exception e) {
 25  			System.out.println("Exception: " + e);
 26  		}
 27  
 28  		return properties;
 29  	}
 30  
 31  	public String getProperty (String name) {
 32  		return config.getProperty(name);
 33  	}
 34  
 35  
 36  
 37  }

```
  * file:///root/.m2/repository/io/konveyor/demo/config-utils/1.0.0/io/konveyor/demo/config/ApplicationConfiguration.java
      * Java native libraries might not run in a cloud or container environment.. Recommendations. * Review the purpose of the native library in your application.. * Check whether the native library is compatible with a cloud environment.. * Reuse or embed the native library or application in a cloud environment, for example, in a JBoss module.. * Replace, remove, or rewrite the native library or application using a cloud-compatible equivalent.
      * Code Snippet:
```java
  1  package io.konveyor.demo.config;
  2  
  3  import java.io.FileInputStream;
  4  import java.io.InputStream;
  5  import java.util.Properties;
  6  
  7  public class ApplicationConfiguration {
  8  
  9  	private Properties config;
 10  
 11  	public ApplicationConfiguration() {
 12  		super();
 13  		this.config = loadProperties();
 14  
 15  	}
 16  
 17  	private Properties loadProperties() {
 18  		Properties properties = new Properties();
 19  
 20  		try (InputStream inputStream = new FileInputStream("/opt/config/persistence.properties")) {
 21  
 22  			properties.load(inputStream);
 23  
 24  		} catch (Exception e) {
 25  			System.out.println("Exception: " + e);
 26  		}
 27  
 28  		return properties;
 29  	}
 30  
 31  	public String getProperty (String name) {
 32  		return config.getProperty(name);
 33  	}
 34  
 35  
 36  
 37  }

```
### #1 - local-storage-00001
* Category: mandatory
* Effort: 1
* Description: File system - Java IO
An application running inside a container could lose access to a file in local storage.. Recommendations. The following recommendations depend on the function of the file in local storage:. * Logging: Log to standard output and use a centralized log collector to analyze the logs.. * Caching: Use a cache backing service.. * Configuration: Store configuration settings in environment variables so that they can be updated without code changes.. * Data storage: Use a database backing service for relational data or use a persistent data storage system.. * Temporary data storage: Use the file system of a running container as a brief, single-transaction cache.
* Labels: konveyor.io/target=cloud-readiness, konveyor.io/source, storage
* Links
  * Twelve-Factor App: Logs: https://12factor.net/logs
  * OpenShift Container Platform: Understanding cluster logging: https://docs.openshift.com/container-platform/4.5/logging/cluster-logging.html
  * Twelve-Factor App: Backing services: https://12factor.net/backing-services
  * Twelve-Factor App: Config: https://12factor.net/config
  * OpenShift Container Platform: Input secrets and ConfigMaps: https://docs.openshift.com/container-platform/4.5/builds/creating-build-inputs.html#builds-input-secrets-configmaps_creating-build-inputs
  * OpenShift Container Platform: Understanding persistent storage: https://docs.openshift.com/container-platform/4.5/storage/understanding-persistent-storage.html
* Incidents
  * file:///root/.m2/repository/io/konveyor/demo/config-utils/1.0.0/io/konveyor/demo/config/ApplicationConfiguration.java
      * An application running inside a container could lose access to a file in local storage.. Recommendations. The following recommendations depend on the function of the file in local storage:. * Logging: Log to standard output and use a centralized log collector to analyze the logs.. * Caching: Use a cache backing service.. * Configuration: Store configuration settings in environment variables so that they can be updated without code changes.. * Data storage: Use a database backing service for relational data or use a persistent data storage system.. * Temporary data storage: Use the file system of a running container as a brief, single-transaction cache.
      * Code Snippet:
```java
  1  package io.konveyor.demo.config;
  2  
  3  import java.io.FileInputStream;
  4  import java.io.InputStream;
  5  import java.util.Properties;
  6  
  7  public class ApplicationConfiguration {
  8  
  9  	private Properties config;
 10  
 11  	public ApplicationConfiguration() {
 12  		super();
 13  		this.config = loadProperties();
 14  
 15  	}
 16  
 17  	private Properties loadProperties() {
 18  		Properties properties = new Properties();
 19  
 20  		try (InputStream inputStream = new FileInputStream("/opt/config/persistence.properties")) {
 21  
 22  			properties.load(inputStream);
 23  
 24  		} catch (Exception e) {
 25  			System.out.println("Exception: " + e);
 26  		}
 27  
 28  		return properties;
 29  	}
 30  
 31  	public String getProperty (String name) {
 32  		return config.getProperty(name);
 33  	}
 34  
 35  
 36  
 37  }

```
