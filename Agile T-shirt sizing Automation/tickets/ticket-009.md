# Add Slack notifications for critical production alerts

## Description

Send critical production monitoring alerts to the engineering team's Slack channel so incidents can be identified more quickly.

## Requirements

- Only critical alerts should be sent to Slack.
- Messages should contain service, severity, timestamp and a link to the monitoring dashboard.
- Duplicate alerts should be suppressed.
 - Slack failure should not affect the monitoring platform.

## Technical notes

The monitoring platform already supports outbound webhooks, but the team has not integrated it with Slack before. It is unclear whether the existing webhook can handle the required formatting and duplicate suppression.
