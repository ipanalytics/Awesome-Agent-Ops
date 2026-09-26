# Awesome Agent Ops

_Русская версия: [README.ru.md](README.ru.md)_

A curated list of what it actually takes to **run a personal AI agent in production** — not
prompt tricks, but the boring layer: schedules, context budgets, secrets, sandboxes, delivery,
and the failure modes nobody warns you about.

Everything here is written from an agent that has been running unattended since mid-2026 on one
small server: cron jobs that fire at 03:10, a Telegram front end, health data, mail, and
GitHub. The practice notes link to a series of 34 modules where each one is written out in
full: [Hermes-Agent-Ops](https://github.com/ipanalytics/Hermes-Agent-Ops).

---

## 1. Start with the failure modes

- **[The job that ran and said nothing](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/28-digest-delivery-health)** —
  a cron that fails silently is worse than one that crashes. Deliverability is a metric, not a hope.
- **[The job that stopped existing](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/30-schedule-audit)** —
  schedules drift: a one-shot that never re-armed, a job paused "for a day" in March. Audit the
  schedule itself, not the output.
- **[The report nobody read](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/12-topic-routing)** —
  a digest delivered into the wrong channel is the same as not delivered. Route by kind, not by habit.
- **[The context that quietly shrank](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/31-compaction-effect-check)** —
  compaction is invisible until it drops the one detail you needed. Measure what compaction costs
  before you trust it.

## 2. Scheduled work

- **[A cron for the crons](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/05-cron-of-crons)** —
  one job whose only purpose is to notice that another job did not run.
- **[Fresh-prompt linting](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/07-fresh-prompt-linter)** —
  prompts rot faster than code: they reference jobs, files and names that no longer exist.
- **[From LLM job to script](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/24-llm-to-script)** —
  the best cron is a collector script plus a small model call at the end, not an agent loop.
- **[Task evals and autopsy](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/20-task-evals-and-autopsy)** —
  when a job fails, reconstruct what it saw instead of re-running it and guessing.

## 3. Context and cost

- **[Cost governance](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/19-cost-governance)** —
  a hard budget with a graceful downgrade beats a surprise invoice.
- **[The cost dashboard](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/10-cost-dashboard)** —
  per-job, per-model spend, so "the agent got expensive" becomes a number with a cause.
- **[The thinking layer](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/29-thinking-layer-cost)** —
  pay for reasoning where the decision is, not where the text is.
- **[Compaction that never summarises](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/31-compaction-effect-check)** —
  the alternative to summarising: delete what is stale, keep the rest verbatim.

## 4. Isolation and secrets

- **[Tool guardrails](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/15-agent-tool-guardrails)** —
  an allow-list per tool, plus a hook that refuses the destructive shape before it runs.
- **[A sandbox without root](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/04-role-profiles)** —
  proot, one writable tree, and a home directory that is simply not mounted.
- **[Wallet guard](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/01-agent-wallet-guard)** —
  spend limits and a kill switch that does not depend on the agent's own judgement.
- **[Publishing an agent's work safely](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/03-agent-ops-playbook)** —
  the denylist that runs before `git push`, because "I will remember to check" is not a control.

## 5. Delivery and attention

- **[Voice that lands as voice](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/13-voice-input-hypotheses)** —
  an audio reply has to arrive as a voice note, at a pace a human can stand, or it may as well be text.
- **[Delivery obligations](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/28-digest-delivery-health)** —
  keep a record of what must be delivered and when, and check it; do not infer it from logs.
- **[Topic routing](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/12-topic-routing)** —
  one chat, many topics: status goes to the log, decisions go to the human, alerts go where they
  will be seen.
- **[Quiet hours and cadence](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/03-agent-ops-playbook)** —
  a digest that arrives when nobody reads it trains the human to ignore digests.

## 6. Memory that does not rot

- **[Memory in topics](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/09-ops-as-data)** —
  a small always-loaded core plus one file per subject, read on demand.
- **[Session housekeeping](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/08-session-housekeeping)** —
  sessions are a log, not a filing cabinet; name, archive, prune.
- **[Skill library janitor](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/34-skill-library-janitor)** —
  skills accumulate, contradict each other, and describe tools that were renamed last month.
- **[Blind-spot audit](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/21-blind-spot-audit)** —
  ask what the agent is *not* looking at; the answer is usually more useful than a summary.

## 7. Watching the machine, not just the model

- **[Gateway supervisor](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/02-agent-gateway-supervisor)** —
  the process that talks to the chat platform is the single point of failure.
- **[Harness probes](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/18-harness-probes)** —
  synthetic checks that prove the whole path works: model, tool, transport, permission.
- **[Ops as data](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/09-ops-as-data)** —
  every job writes a row; the dashboard is a query, not a memory.

## 8. Tools worth knowing

- [**Hermes Agent**](https://hermes-agent.nousresearch.com/docs) — the harness this list is written
  against: profiles, cron, skills, plugins, a terminal tool and a chat front end.
- [**proot**](https://proot-me.github.io/) — userspace isolation without root, which is how the
  terminal tool gets a workspace and nothing else.
- [**edge-tts**](https://github.com/rany2/edge-tts) — a free fallback voice when the paid provider
  is rate-limited at 03:10.
- [**Jev (TypeSafe)**](https://github.com/kerpopule/hermes-jev-skills) — cheap decisions
  (routing, skill selection, compaction) taken by a small fast model instead of the expensive one.
- [**RIPE RIS**](https://ris.ripe.net) — public BGP RIB dumps, the raw material of route-security
  work. [**CAIDA**](https://www.caida.org/catalog/datasets/) for AS relationships,
  [**MaxMind GeoLite2**](https://dev.maxmind.com/geoip/geolite2-free-geolocation-data) for the geo
  layer.
- [**SQLite FTS5**](https://sqlite.org/fts5.html) — full-text search over your own session history,
  which is the only reason an agent's past is usable at all.

## What this list is not

- Not prompt engineering. Different problem, different list.
- Not a framework. Most of these are a cron entry, a script and a JSON file.
- Not finished. Every item here was added because something broke.

## Contributing

Corrections and additions are welcome — especially *failure modes*, with the symptom, the cause,
and the fix. One line per item, real link, no marketing.

## License

MIT for the list and for the linked modules unless a module says otherwise.
