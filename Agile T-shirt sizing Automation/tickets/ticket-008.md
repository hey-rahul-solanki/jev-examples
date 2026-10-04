# Build real-time customer order tracking

## Description

Customers should be able to see the current status of their order and see status changes without refreshing the page.

## Requirements

- Status should update without manual refresh.
 - Support confirmed, processing, packed, shipped, out for delivery and delivered.
- Customers must not be able to vew another customer's order.
- Status history should be retained for audit purposes.
 - The solution should support at least 50,000 concurrent tracking sessions.

## Technical notes

The current system is request/response based. We don't have an existing WebSocket or SSE infrastructure. Some delivery partners provide webhooks while others only support polling. The team needs to decide the real-time architecture.
