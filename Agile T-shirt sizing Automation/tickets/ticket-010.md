# Add audit history for customer profile changes

## Description

Create an audit history for customer profile changes. We need to know when a field was changed, what the previous value was, what the new value is and which user or system made the change.

## Requirements

- Track changes to name, email, phone, address and status.
- Record timestamp, field name, previous value, new value and actor.
- Distinguish user-initiated and system-initiated changes.
 - Audit records should not be modifiable through the application.
- Authorized support users should be able to view the history.

## Technical notes

Customer profile updates currently occur through three different services. One of the services uses direct database updates instead of the central profile API. We need to decide whether auditing should be handled at the application layer, database layer, or both.
