# Add CSV export to customer search results

## Description

Support agents currently can search for customers but cannot download the results. Add an Export CSV button to the search page.

## Requirements

- Export should respect current filters and sorting.
 - CSV should contain customer ID, name, email, status and created date.
- Support agents should see an Export CSV button only when they have export permission.
- Large exports should not cause the browser to time out.

## Technical notes

The current search API supports filtering and pagination. We expect up to several thousand results for some queries. Availability of a streaming export may need to be checked.
