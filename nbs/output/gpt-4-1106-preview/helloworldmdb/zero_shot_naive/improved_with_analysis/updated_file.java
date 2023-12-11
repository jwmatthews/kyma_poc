
package org.jboss.as.quickstarts.mdb;

import org.eclipse.microprofile.reactive.messaging.Incoming;
import javax.enterprise.context.ApplicationScoped;
import org.jboss.logging.Logger;

/**
 * A simple bean that asynchronously receives and processes the messages that are sent to the queue.
 */
@ApplicationScoped
public class HelloWorldQueueMDB {

    private static final Logger LOGGER = Logger.getLogger(HelloWorldQueueMDB.class);

    /**
     * This method is called when a message is received.
     * @param message The text message received
     */
    @Incoming("helloworld-queue")
    public void onMessage(String message) {
        LOGGER.info("Received Message from queue: " + message);
    }
}
