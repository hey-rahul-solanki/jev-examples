# Add retry mechanism for failed payment notifications

## Description

Currently, when a payment notification fails to be delivered, the event is marked as failed and requires manual intervention.

We want to introduce automatic retries so transient failures don't require support intervention.

## Requirements

- Failed notifications should be retried automatically.
- Use exponential backoff.
- A maximum of 5 retries should be made.
- After all retries fail, move the event to a dead-letter queue.
- Customers must not receive duplicate notifications.
- Retry attempts should be visible in logs and monitoring.

## Technical notes

The current implementation uses an asynchronous payment event published to the message queue.
Idempotency already exists for some notification types, but not all.

The team needs to decide whether retry handling should be implemented at the consumer level or through the queue configuration.
