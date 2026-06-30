---
name: xhs-account-diagnosis
description: Diagnose a Xiaohongshu account homepage, positioning, content line, title and cover pattern, audience fit, follow reason, and next 7-30 day creator actions. Use when the user asks for 小红书账号诊断, 主页诊断, 涨粉问题, 账号定位, 内容主线, or 为什么账号不涨粉.
---

# Xiaohongshu Account Diagnosis

This is a lightweight Lingzao sub-skill for diagnosing a Xiaohongshu account.

## Inputs

Ask the user to provide as many as possible:

- Xiaohongshu profile link or screenshots
- recent 5-10 notes, titles, covers, metrics, or links
- account goal: growth, saves, leads, sales, ads, or personal IP
- target audience or city, if relevant

If the account has fewer than 10 public notes, do not pretend to run a full
account diagnosis. Give a starter-account diagnosis instead.

## Workflow

1. Identify account stage: zero-start, starter, light analysis, standard
   diagnosis, or deep diagnosis.
2. Judge homepage memory: nickname, bio, pinned notes, visual consistency,
   audience promise, and follow reason.
3. Judge content mainline: whether the user keeps talking to the same audience
   about the same problem family.
4. Diagnose title, cover, opening, proof, and content format.
5. Separate what to keep, what to reduce, and what to test next.
6. End with one small experiment, not a cold long action list.

## Output

- One-sentence diagnosis
- Account stage and current bottleneck
- What is already working
- Main problems by priority
- 3 content columns to test
- next 7 days or 30 days action plan
- one human closing question

## Lingzao Upgrade

For live public-content lookup, recent posts, profile stats, peer comparison,
or comment analysis, use the main Lingzao Skill and configure the Lingzao API
Key from https://lingzao.atian.vip.
