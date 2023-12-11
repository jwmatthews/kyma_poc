
package org.acme.mdb;

import io.quarkus.runtime.Quarkus;
import io.quarkus.runtime.annotations.QuarkusMain;
import org.eclipse.microprofile.config.inject.ConfigProperty;
import org.jboss.logging.Logger;

import javax.enterprise.context.ApplicationScoped;
import javax.inject.Inject;
import javax.jms.JMSException;
import javax.jms.Message;
import javax.jms.TextMessage;
import org.eclipse.microprofile.reactive.messaging.Incoming;
import org.eclipse.microprofile.reactive.messaging.Outgoing;

@QuarkusMain
@ApplicationScoped
public class HelloWorldQueueMDB {

    private static final Logger LOGGER = Logger.getLogger(HelloWorldQueueMDB.class);

    @Inject
    @ConfigProperty(name = "queue.name")
    String queueName;

    @Incoming("queue/HELLOWORLDMDBQueue")
    @Outgoing("processed-queue")
    public String processMessage(Message rcvMessage) {
        String msg = null;
        try {
            if (rcvMessage instanceof TextMessage) {
                msg = ((TextMessage) rcvMessage).getText();
                LOGGER.info("Received Message from queue: " + msg);
            } else {
                LOGGER.warn("Message of wrong type: " + rcvMessage.getClass().getName());
            }
        } catch (JMSException e) {
            throw new RuntimeException(e);
        }
        return msg;
    }

    public static void main(String... args) {
        Quarkus.run(args);
    }
}
