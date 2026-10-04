# Integrate third-party address validation

## Description

Add address validation to checkout using the company's selected third-party provider. The address should be validated before the order is submitted.

## Requirements

- Validate shipping address before order submission.
- Show actionable messages for invalid addresses.
- Allow customers to accept a suggested corrected address.
 - third-party failures should not block cout permanently.
- Credentials must be stored securely.
- Add monitoring for validation failures.

## Technical notes

The provider has a sandbox and a rate limit. We have not previously integrated with this provider. The checkout flow is latency-sensitive, and the team is unsure whether the provider supports all of the address formats we allow.
