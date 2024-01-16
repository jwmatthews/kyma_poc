# cloud-readiness
## Description
This ruleset detects logging configurations that may be problematic when migrating an application to a cloud environment.
* Source of rules: https://github.com/konveyor/rulesets/tree/main/default/generated
## Violations
Number of Violations: 1
### #0 - local-storage-00001
* Category: mandatory
* Effort: 1
* Description: File system - Java IO
* Labels: konveyor.io/source, konveyor.io/target=cloud-readiness, storage
* Links
  * OpenShift Container Platform: Input secrets and ConfigMaps: https://docs.openshift.com/container-platform/4.5/builds/creating-build-inputs.html#builds-input-secrets-configmaps_creating-build-inputs
  * OpenShift Container Platform: Understanding cluster logging: https://docs.openshift.com/container-platform/4.5/logging/cluster-logging.html
  * OpenShift Container Platform: Understanding persistent storage: https://docs.openshift.com/container-platform/4.5/storage/understanding-persistent-storage.html
  * Twelve-Factor App: Backing services: https://12factor.net/backing-services
  * Twelve-Factor App: Config: https://12factor.net/config
  * Twelve-Factor App: Logs: https://12factor.net/logs
* Incidents
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/tasksJsf/Resources.java
      * Line Number: 56
      * Message: 'An application running inside a container could lose access to a file in local storage.

 Recommendations

 The following recommendations depend on the function of the file in local storage:

 * Logging: Log to standard output and use a centralized log collector to analyze the logs.
 * Caching: Use a cache backing service.
 * Configuration: Store configuration settings in environment variables so that they can be updated without code changes.
 * Data storage: Use a database backing service for relational data or use a persistent data storage system.
 * Temporary data storage: Use the file system of a running container as a brief, single-transaction cache.'
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
      * Line Number: 62
      * Message: 'An application running inside a container could lose access to a file in local storage.

 Recommendations

 The following recommendations depend on the function of the file in local storage:

 * Logging: Log to standard output and use a centralized log collector to analyze the logs.
 * Caching: Use a cache backing service.
 * Configuration: Store configuration settings in environment variables so that they can be updated without code changes.
 * Data storage: Use a database backing service for relational data or use a persistent data storage system.
 * Temporary data storage: Use the file system of a running container as a brief, single-transaction cache.'
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
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/tasksJsf/TaskController.java
      * Line Number: 72
      * Message: 'An application running inside a container could lose access to a file in local storage.

 Recommendations

 The following recommendations depend on the function of the file in local storage:

 * Logging: Log to standard output and use a centralized log collector to analyze the logs.
 * Caching: Use a cache backing service.
 * Configuration: Store configuration settings in environment variables so that they can be updated without code changes.
 * Data storage: Use a database backing service for relational data or use a persistent data storage system.
 * Temporary data storage: Use the file system of a running container as a brief, single-transaction cache.'
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
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/tasksJsf/TaskDaoImpl.java
      * Line Number: 52
      * Message: 'An application running inside a container could lose access to a file in local storage.

 Recommendations

 The following recommendations depend on the function of the file in local storage:

 * Logging: Log to standard output and use a centralized log collector to analyze the logs.
 * Caching: Use a cache backing service.
 * Configuration: Store configuration settings in environment variables so that they can be updated without code changes.
 * Data storage: Use a database backing service for relational data or use a persistent data storage system.
 * Temporary data storage: Use the file system of a running container as a brief, single-transaction cache.'
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
      * Line Number: 60
      * Message: 'An application running inside a container could lose access to a file in local storage.

 Recommendations

 The following recommendations depend on the function of the file in local storage:

 * Logging: Log to standard output and use a centralized log collector to analyze the logs.
 * Caching: Use a cache backing service.
 * Configuration: Store configuration settings in environment variables so that they can be updated without code changes.
 * Data storage: Use a database backing service for relational data or use a persistent data storage system.
 * Temporary data storage: Use the file system of a running container as a brief, single-transaction cache.'
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
      * Line Number: 67
      * Message: 'An application running inside a container could lose access to a file in local storage.

 Recommendations

 The following recommendations depend on the function of the file in local storage:

 * Logging: Log to standard output and use a centralized log collector to analyze the logs.
 * Caching: Use a cache backing service.
 * Configuration: Store configuration settings in environment variables so that they can be updated without code changes.
 * Data storage: Use a database backing service for relational data or use a persistent data storage system.
 * Temporary data storage: Use the file system of a running container as a brief, single-transaction cache.'
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
  * file:///tmp/source-code/src/main/java/org/jboss/as/quickstarts/tasksJsf/UserDaoImpl.java
      * Line Number: 40
      * Message: 'An application running inside a container could lose access to a file in local storage.

 Recommendations

 The following recommendations depend on the function of the file in local storage:

 * Logging: Log to standard output and use a centralized log collector to analyze the logs.
 * Caching: Use a cache backing service.
 * Configuration: Store configuration settings in environment variables so that they can be updated without code changes.
 * Data storage: Use a database backing service for relational data or use a persistent data storage system.
 * Temporary data storage: Use the file system of a running container as a brief, single-transaction cache.'
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
  * file:///tmp/source-code/src/test/java/org/jboss/as/quickstarts/tasksJsf/DefaultDeployment.java
      * Line Number: 38
      * Message: 'An application running inside a container could lose access to a file in local storage.

 Recommendations

 The following recommendations depend on the function of the file in local storage:

 * Logging: Log to standard output and use a centralized log collector to analyze the logs.
 * Caching: Use a cache backing service.
 * Configuration: Store configuration settings in environment variables so that they can be updated without code changes.
 * Data storage: Use a database backing service for relational data or use a persistent data storage system.
 * Temporary data storage: Use the file system of a running container as a brief, single-transaction cache.'
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
 19  import java.io.File;
 20  
 21  import org.jboss.shrinkwrap.api.ShrinkWrap;
 22  import org.jboss.shrinkwrap.api.spec.WebArchive;
 23  
 24  /**
 25   * Enables prepare project-specific {@link WebArchive} for deployment.
 26   *
 27   * @author Lukas Fryc
 28   *
 29   */
 30  public class DefaultDeployment {
 31  
 32      private static final String WEBAPP_SRC = "src/main/webapp";
 33      private static final String TEST_WEBAPP_SRC = "src/test/webapp";
 34  
 35      private WebArchive webArchive;
 36  
 37      public DefaultDeployment() {
 38          this(false);
 39      }
 40  
 41      public DefaultDeployment(boolean useAlternative) {
 42          if (useAlternative) {
 43              webArchive = ShrinkWrap.create(WebArchive.class, "test.war").addAsWebInfResource(
 44                  new File(TEST_WEBAPP_SRC, "WEB-INF/beans.xml"));
 45          } else {
 46              webArchive = ShrinkWrap.create(WebArchive.class, "test.war").addAsWebInfResource(
 47                  new File(WEBAPP_SRC, "WEB-INF/beans.xml"));
 48          }
 49      }
 50  
 51      public DefaultDeployment withPersistence() {
 52          webArchive = webArchive.addAsResource("META-INF/test-persistence.xml", "META-INF/persistence.xml").addAsWebInfResource(
 53              "test-ds.xml", "test-ds.xml");
 54          return this;
 55      }
 56  
 57      public DefaultDeployment withImportedData() {
 58          webArchive = webArchive.addAsResource("import.sql");
 59          return this;
 60      }
 61  
 62      public DefaultDeployment withFaces() {
 63          webArchive = webArchive.addAsWebInfResource(new File(WEBAPP_SRC, "WEB-INF/faces-config.xml"));
 64          return this;
 65      }
 66  
 67      public WebArchive getArchive() {
 68          return webArchive;
 69      }
 70  }

```
  * file:///tmp/source-code/src/test/java/org/jboss/as/quickstarts/tasksJsf/ResourcesIT.java
      * Line Number: 47
      * Message: 'An application running inside a container could lose access to a file in local storage.

 Recommendations

 The following recommendations depend on the function of the file in local storage:

 * Logging: Log to standard output and use a centralized log collector to analyze the logs.
 * Caching: Use a cache backing service.
 * Configuration: Store configuration settings in environment variables so that they can be updated without code changes.
 * Data storage: Use a database backing service for relational data or use a persistent data storage system.
 * Temporary data storage: Use the file system of a running container as a brief, single-transaction cache.'
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
      * Line Number: 61
      * Message: 'An application running inside a container could lose access to a file in local storage.

 Recommendations

 The following recommendations depend on the function of the file in local storage:

 * Logging: Log to standard output and use a centralized log collector to analyze the logs.
 * Caching: Use a cache backing service.
 * Configuration: Store configuration settings in environment variables so that they can be updated without code changes.
 * Data storage: Use a database backing service for relational data or use a persistent data storage system.
 * Temporary data storage: Use the file system of a running container as a brief, single-transaction cache.'
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
      * Line Number: 67
      * Message: 'An application running inside a container could lose access to a file in local storage.

 Recommendations

 The following recommendations depend on the function of the file in local storage:

 * Logging: Log to standard output and use a centralized log collector to analyze the logs.
 * Caching: Use a cache backing service.
 * Configuration: Store configuration settings in environment variables so that they can be updated without code changes.
 * Data storage: Use a database backing service for relational data or use a persistent data storage system.
 * Temporary data storage: Use the file system of a running container as a brief, single-transaction cache.'
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
      * Line Number: 73
      * Message: 'An application running inside a container could lose access to a file in local storage.

 Recommendations

 The following recommendations depend on the function of the file in local storage:

 * Logging: Log to standard output and use a centralized log collector to analyze the logs.
 * Caching: Use a cache backing service.
 * Configuration: Store configuration settings in environment variables so that they can be updated without code changes.
 * Data storage: Use a database backing service for relational data or use a persistent data storage system.
 * Temporary data storage: Use the file system of a running container as a brief, single-transaction cache.'
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
      * Line Number: 73
      * Message: 'An application running inside a container could lose access to a file in local storage.

 Recommendations

 The following recommendations depend on the function of the file in local storage:

 * Logging: Log to standard output and use a centralized log collector to analyze the logs.
 * Caching: Use a cache backing service.
 * Configuration: Store configuration settings in environment variables so that they can be updated without code changes.
 * Data storage: Use a database backing service for relational data or use a persistent data storage system.
 * Temporary data storage: Use the file system of a running container as a brief, single-transaction cache.'
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
126  
127          // when
128          taskDao.deleteTask(task);
129  
130          // then
131          assertEquals(1, taskDao.getAll(detachedUser).size());
132      }
133  }

```
  * file:///tmp/source-code/src/test/java/org/jboss/as/quickstarts/tasksJsf/TaskListBeanIT.java
      * Line Number: 40
      * Message: 'An application running inside a container could lose access to a file in local storage.

 Recommendations

 The following recommendations depend on the function of the file in local storage:

 * Logging: Log to standard output and use a centralized log collector to analyze the logs.
 * Caching: Use a cache backing service.
 * Configuration: Store configuration settings in environment variables so that they can be updated without code changes.
 * Data storage: Use a database backing service for relational data or use a persistent data storage system.
 * Temporary data storage: Use the file system of a running container as a brief, single-transaction cache.'
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
