
/*
 * JBoss, Home of Professional Open Source
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 * http://www.apache.org/licenses/LICENSE-2.0
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package org.jboss.as.quickstarts.mdb;

import io.quarkus.jms.annotation.JmsListener;
import io.quarkus.jms.runtime.JmsMessage;
import org.jboss.logging.Logger;

import javax.enterprise.context.ApplicationScoped;

/**
 * <p>
 * A simple Message Driven Bean that asynchronously receives and processes the messages that are sent to the queue.
 * </p>
 *
 * @author Serge Pagop (spagop@redhat.com)
 */
@ApplicationScoped
public class HelloWorldQueueMDB {

    private static final Logger LOGGER = Logger.getLogger(HelloWorldQueueMDB.class);

    /**
     * @see JmsListener#receiveMessage(JmsMessage)
     */
    @JmsListener(destination = "queue/HELLOWORLDMDBQueue", acknowledgeMode = "AUTO_ACKNOWLEDGE")
    public void receiveMessage(JmsMessage<String> message) {
        String text = message.getBody();
        LOGGER.info("Received Message from queue: " + text);
    }
}
