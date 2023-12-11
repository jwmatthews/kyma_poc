
package org.jboss.as.quickstarts.mdb;

import org.eclipse.microprofile.reactive.messaging.Incoming;
import org.jboss.logging.Logger;

import javax.enterprise.context.ApplicationScoped;
import javax.jms.JMSException;
import javax.jms.TextMessage;

@ApplicationScoped
public class HelloWorldQueueMDB {

    private static final Logger LOGGER = Logger.getLogger(HelloWorldQueueMDB.class);

    @Incoming("helloworld-queue")
    public void onMessage(TextMessage rcvMessage) {
        try {
            LOGGER.info("Received Message from queue: " + rcvMessage.getText());
        } catch (JMSException e) {
            throw new RuntimeException(e);
        }
    }
}
