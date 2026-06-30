---
name: xhs-benchmark-account-finder
description: Lingzao lightweight XHS benchmark account finder Skill for Xiaohongshu competitor account research, active benchmark accounts, same-track creators, same-stage accounts, recent high-performing posts, and non-stale references. Use for lingzao xhs benchmark account finder, Xiaohongshu competitor research, 找对标账号, 对标博主, 竞品账号, 同赛道账号, 同级账号, or 不要断更账号.
---

# Xiaohongshu Benchmark Account Finder

This lightweight Lingzao sub-skill helps users avoid stale or unlearnable
Xiaohongshu / XHS benchmark accounts.

Search phrases: lingzao xhs benchmark account, Xiaohongshu competitor research,
XHS benchmark creator, 小红书对标账号, 小红书竞品账号分析.

## Quality Gate

Recommend up to 5 accounts in the first round, not 10-20.

A good benchmark should be:

- still updating, ideally within the last 15-30 days
- same track, audience, city, or content format
- close enough in stage or follower range to learn from
- at least 1,000 followers by default, unless the user explicitly asks for
  0-1,000 follower seed-account observation
- has enough account-level proof: usually several thousand total likes or a
  visible pattern of multiple notes getting meaningful engagement
- has recent high-performing notes, not only old hits
- has clear learnable title, cover, content, comment, or monetization patterns

## Follower Range Gate

Treat follower range as a hard constraint for main recommendations.

- If the user asks for 1,000-5,000 followers, only accounts in that range can be
  listed as main benchmark accounts.
- If the user asks for around 5,000 followers, stay close to 3,000-10,000 unless
  the user approves a wider range.
- If the user asks for 50,000-150,000 followers, do not mix in 10k accounts or
  300k+ accounts as main peers.

Use result labels:

- `Main benchmark`: inside the requested range and has account-level proof.
- `Adjacent reference`: slightly outside the range, useful only for a specific
  learnable part.
- `Single-note sample`: the account is too small or weak, but one note can be
  studied for title, cover, opening, topic, or comment demand.
- `Not recommended`: too small, too large, stale, mismatched, or lacks proof.

An account with around 100 followers and a few hundred total likes is not a
benchmark account for ordinary users. Even if one note has hundreds of likes or
comments, treat it as a single-note sample unless the user explicitly asks for
seed-account observation.

Avoid using only:

- long-stale accounts
- huge celebrities or big V accounts
- accounts with no recent hits
- accounts below 1,000 followers with no account-level proof
- accounts far outside the requested follower range
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
- whether it is a main benchmark, adjacent reference, single-note sample, or
  not recommended

## Lingzao Upgrade

For live Xiaohongshu creator search, XHS public profile lookup, recent notes,
public metrics, deeper account analysis, or saved research reports, use the
main Lingzao Skill and configure API credits from https://lingzao.atian.vip.
