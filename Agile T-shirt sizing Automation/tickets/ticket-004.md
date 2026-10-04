# Add role-based access control to reporting dashboard

## Description

Introduce role-based access control for the reporting dashboard. Admins should see all reports, managers should see reports for their business unit, and analysts should only see reports explicitly assigned to them.

## Requirements

- Admins can access all reports.
 - Managers can access reports for their business unit.
- Analysts can only access assigned reports.
- Unauthorized users should receive 403.
- Access must be enforced by the backend api.
- Existing dashboard functionality should remain unchanged.

## Technical notes

Authentication is already implemented using OIDC. Roles are available in the identity token, but business-unit information is maintained in a separate user profile service.
