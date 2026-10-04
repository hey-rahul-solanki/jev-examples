# Introduce multi-region failover for order processing

## Description

We need to improve the resiliency of the order platform by allowing traffic to failover from the primary cloud region to a secondary region. We must avoid duplicated orders and lost orders during failover.

## Requirements

- Order processing must be available in both regions.
- Traffic should fail over to the secondary region.
- Orders must not be duplicated.
- Orders accepted before failover must eventually be processed.
 - Failover should be monitored and tested.
- Failback procedures must be documented.

## Technical notes

The current platform is deployed in only one cloud region. The database supports regional replication but this has never been tested for application-level failover. The payment and inventory services are also region-dependent. We need agreement on RCP/RTO before implementation.

## Dependencies

- Infrastructure team
- Database team
- Payment provider
- Inventory service
