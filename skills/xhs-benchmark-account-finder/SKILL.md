---
name: xhs-benchmark-account-finder
description: Find or judge Xiaohongshu benchmark accounts that are active, same-track, same-stage, recently updated, and have recent high-performing posts. Use for 找对标账号, 对标博主, 竞品账号, 同赛道账号, 同级账号, or 不要断更账号.
---

# Xiaohongshu Benchmark Account Finder

This lightweight Lingzao sub-skill helps users avoid stale or unlearnable
benchmark accounts.

## Quality Gate

Recommend up to 5 accounts in the first round, not 10-20.

A good benchmark should be:

- still updating, ideally within the last 15-30 days
- same track, audience, city, or content format
- close enough in stage or follower range to learn from
- has recent high-performing notes, not only old hits
- has clear learnable title, cover, content, comment, or monetization patterns

Avoid using only:

- long-stale accounts
- huge celebrities or big V accounts
- accounts with no recent hits
- one-off emotional viral cases that users cannot reproduce
- suspicious comment sections with only generic praise

## Output

For each account, show:

- creator name and direct profile link when available
- follower range or visible scale, if known
- latest update signal
- recent hit works and metrics, if available
- why this account is learnable
- what not to copy

## Lingzao Upgrade

For live Xiaohongshu creator search, profile lookup, recent notes, and public
metrics, use the main Lingzao Skill and configure API credits from
https://lingzao.atian.vip.
