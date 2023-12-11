
package org.acme.mdb;

import javax.inject.Inject;
import javax.jms.JMSException;
import javax.jms.Message;
import javax.jms.TextMessage;

import org.eclipse.microprofile.config.inject.ConfigProperty;
import org.jboss.logging.Logger;

import io.quarkus.jms.annotation.JmsListener;
import io.quarkus.runtime.Startup;

/**
 * <p>
 * A simple Message Driven Bean that asynchronously receives and processes the messages that are sent to the queue.
 * </p>
 *
 * @author Serge Pagop (spagop@redhat.com)
 */
@Startup
public class HelloWorldQueueMDB {

    private static final Logger LOGGER = Logger.getLogger(HelloWorldQueueMDB.class);

    @Inject
    @ConfigProperty(name = "queue.name")
    String queueName;

    /**
     * @see MessageListener#onMessage(Message)
     */
    @JmsListener(destination = "${queue.name}")
    public void onMessage(TextMessage msg) {
        try {
            LOGGER.info("Received Message from queue: " + msg.getText());
        } catch (JMSException e) {
            throw new RuntimeException(e);
        }
    }
}
