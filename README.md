# Awesome Agent Ops

_Русская версия: [README.ru.md](README.ru.md)_

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Entries](https://img.shields.io/badge/entries-27-blue)
[![Catalog checks](https://github.com/ipanalytics/Awesome-Agent-Ops/actions/workflows/catalog-checks.yml/badge.svg)](.github/workflows/catalog-checks.yml)

<p align="center">
  <img src="./site/banner.svg" alt="Awesome Agent Ops" width="100%">
</p>

A curated list of what it actually takes to **run a personal AI agent (Hermes Agent, Claude Code, any scheduled LLM agent) in production** — not
prompt tricks, but the boring layer: schedules, context budgets, secrets, sandboxes, delivery,
and the failure modes nobody warns you about.

Everything here is written from an agent that has been running unattended since mid-2026 on one
small server: cron jobs that fire at 03:10, a Telegram front end, health data, mail, and
GitHub. The practice notes link to a series of 34 modules where each one is written out in
full: [Hermes-Agent-Ops](https://github.com/ipanalytics/Hermes-Agent-Ops).

## Contents

1. [Start with the failure modes](#1-start-with-the-failure-modes)
2. [Scheduled work](#2-scheduled-work)
3. [Context and cost](#3-context-and-cost)
4. [Isolation and secrets](#4-isolation-and-secrets)
5. [Delivery and attention](#5-delivery-and-attention)
6. [Memory that does not rot](#6-memory-that-does-not-rot)
7. [Watching the machine, not just the model](#7-watching-the-machine-not-just-the-model)

## 1. Start with the failure modes

- **[The job that ran and said nothing](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/28-digest-delivery-health)** — a cron that fails silently is worse than one that crashes. Deliverability is a metric, not a hope.
  *(delivery, cron)*

- **[The job that stopped existing](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/30-schedule-audit)** — schedules drift: a one-shot that never re-armed, a job paused "for a day" in March. Audit the
  schedule itself, not the output. *(cron, publishing)*

- **[The report nobody read](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/12-topic-routing)** — a digest delivered into the wrong channel is the same as not delivered. Route by kind, not by
  habit. *(delivery, routing)*

- **[The context that quietly shrank](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/31-compaction-effect-check)** — compaction is invisible until it drops the one detail you needed. Measure what compaction costs
  before you trust it. *(context)*

## 2. Scheduled work

- **[A cron for the crons](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/05-cron-of-crons)** — one job whose only purpose is to notice that another job did not run. *(cron, observability)*

- **[Fresh-prompt linting](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/07-fresh-prompt-linter)** — prompts rot faster than code: they reference jobs, files and names that no longer exist. *(cron,
  evals)*

- **[From LLM job to script](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/24-llm-to-script)** — the best cron is a collector script plus a small model call at the end, not an agent loop. *(cron,
  cost)*

- **[Task evals and autopsy](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/20-task-evals-and-autopsy)** — when a job fails, reconstruct what it saw instead of re-running it and guessing. *(evals)*

## 3. Context and cost

- **[Cost governance](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/19-cost-governance)** — a hard budget with a graceful downgrade beats a surprise invoice. *(cost)*

- **[The cost dashboard](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/10-cost-dashboard)** — per-job, per-model spend, so "the agent got expensive" becomes a number with a cause. *(cost,
  observability)*

- **[The thinking layer](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/29-thinking-layer-cost)** — pay for reasoning where the decision is, not where the text is. *(cost, routing)*

- **[Compaction that never summarises](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/31-compaction-effect-check)** — the alternative to summarising: delete what is stale, keep the rest verbatim. *(context, cost)*

## 4. Isolation and secrets

- **[Tool guardrails](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/15-agent-tool-guardrails)** — an allow-list per tool, plus a hook that refuses the destructive shape before it runs.
  *(isolation, secrets)*

- **[A sandbox without root](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/04-role-profiles)** — proot, one writable tree, and a home directory that is not mounted at all. *(isolation)*

- **[Wallet guard](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/01-agent-wallet-guard)** — spend limits and a kill switch that does not depend on the agent's own judgement. *(secrets,
  isolation)*

- **[Publishing an agent's work safely](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/03-agent-ops-playbook)** — the denylist that runs before `git push`, because "I will remember to check" is not a control.
  *(publishing, secrets)*

## 5. Delivery and attention

- **[Voice that lands as voice](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/13-voice-input-hypotheses)** — an audio reply has to arrive as a voice note, at a pace a human can stand, or it may as well be
  text. *(voice, delivery)*

- **[Delivery obligations](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/28-digest-delivery-health)** — keep a record of what must be delivered and when, and check it; do not infer it from logs.
  *(delivery)*

- **[Topic routing](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/12-topic-routing)** — one chat, many topics: status goes to the log, decisions go to the human, alerts go where they
  will be seen. *(routing, delivery)*

- **[Quiet hours and cadence](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/03-agent-ops-playbook)** — a digest that arrives when nobody reads it trains the human to ignore digests. *(delivery)*

## 6. Memory that does not rot

- **[Memory in topics](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/09-ops-as-data)** — a small always-loaded core plus one file per subject, read on demand. *(memory)*

- **[Session housekeeping](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/08-session-housekeeping)** — sessions are a log, not a filing cabinet; name, archive, prune. *(memory, context)*

- **[Skill library janitor](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/34-skill-library-janitor)** — skills accumulate, contradict each other, and describe tools that were renamed last month.
  *(memory, evals)*

- **[Blind-spot audit](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/21-blind-spot-audit)** — ask what the agent is *not* looking at; the answer is usually more useful than a summary. *(evals,
  observability)*

## 7. Watching the machine, not just the model

- **[Gateway supervisor](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/02-agent-gateway-supervisor)** — the process that talks to the chat platform is the single point of failure. *(observability,
  isolation)*

- **[Harness probes](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/18-harness-probes)** — synthetic checks that prove the whole path works: model, tool, transport, permission.
  *(observability, evals)*

- **[Ops as data](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/09-ops-as-data)** — every job writes a row; the dashboard is a query, not a memory. *(observability, datasets)*

## What this list is not

- Not prompt engineering. Different problem, different list.
- Not a framework. Most of these are a cron entry, a script and a JSON file.
- Not finished. Every item here was added because something broke.

## Contributing

Corrections and additions are welcome — especially *failure modes*, with the symptom, the cause,
and the fix. One line per item, real link, no marketing.

## License

MIT for the list and for the linked modules unless a module says otherwise.
