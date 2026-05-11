<h1 align="center">Shehao Li</h1>

<p align="center">
  <strong>AI product builder turning messy workflows into inspectable software.</strong>
</p>

<p align="center">
  UCSD Math-CS | full-stack AI products | workflow automation | product-quality demos
</p>

<p align="center">
  <a href="https://github.com/lishehao/RPG_Demo">
    <img src="https://img.shields.io/github/stars/lishehao/RPG_Demo?style=for-the-badge&logo=github&label=RPG_Demo" alt="RPG Demo GitHub stars" />
  </a>
  <a href="https://lishehao.github.io/RPG_Demo/">
    <img src="https://img.shields.io/badge/Demo-Tiny%20Stories-d4a853?style=for-the-badge" alt="Tiny Stories demo" />
  </a>
  <a href="https://github.com/lishehao/auto-load-off-test">
    <img src="https://img.shields.io/badge/Automation-Saiwei%20Systems-15161c?style=for-the-badge" alt="Saiwei automation systems" />
  </a>
</p>

---

## What I Build

I build products that make complicated workflows easier to run, inspect, and improve. Right now, this page focuses on work that is already shipped or substantially complete:

- **RPG_Demo / Tiny Stories**, a full-stack AI storytelling product with a visible authoring and play loop.
- **Saiwei automation systems**, a set of Python tools that turned instrument testing, email operations, and issue tracking into repeatable workflows.

The common thread is simple: I like turning ambiguous product or operations problems into software with clear interfaces, state, logs, and user-visible checkpoints.

---

## Flagship: RPG_Demo / Tiny Stories

Tiny Stories is a full-stack AI narrative product shaped like a playable workflow. A user writes a short story seed, previews how the AI interpreted it, compiles it into a runtime, publishes it into a library, and plays through natural-language turns.

<p align="center">
  <img src="./assets/tiny-stories-product-loop.gif" alt="Tiny Stories product loop: seed, preview, compile, play, and inspect state changes" width="100%" />
</p>

| Layer | What it proves |
| --- | --- |
| **Product loop** | Seed -> preview -> author job -> publish -> play -> ending, with user-visible checkpoints instead of a one-shot generator. |
| **Frontend surface** | React + TypeScript UI for creation, story library, play sessions, replay, and state/review panels. |
| **Backend runtime** | FastAPI + Pydantic contracts, SQLite persistence, auth/session handling, and typed frontend/backend API boundaries. |
| **LLM workflow** | Structured generation, bounded advisor behavior, deterministic scaffolding before model calls, and runtime state carried across turns. |
| **Reviewability** | State, choices, consequences, transcript, and ending output are exposed so the system can be inspected after play. |

**Links:** [Repository](https://github.com/lishehao/RPG_Demo) | [Demo](https://lishehao.github.io/RPG_Demo/) | [Product site](https://rpg.shehao.app)

---

## Saiwei Automation Systems

During my instrument-company internship, I built internal automation tools for lab validation and operational handoff. These projects are less flashy than an AI demo, but they show the part of engineering I care about: making repeated real-world work reliable enough for other people to use.

| Project | What it automated | Evidence |
| --- | --- | --- |
| [**auto-load-off-test**](https://github.com/lishehao/auto-load-off-test) | AWG/oscilloscope-style sweep measurement and calibration workflow with PyVISA/SCPI control, Tkinter UI, structured outputs, and layered architecture. | Reduced test preparation and result organization effort by about **75%**; supported about **5 users**; includes tests for sweep planning, measurement IO, settings, and task flow. |
| [**mail-to-dingtalk-todo**](https://github.com/lishehao/mail-to-dingtalk-todo) | IMAP email parsing -> structured business fields -> DingTalk To-Do creation -> idempotent processed-message state. | Handled about **200 emails/day** for about **10 users** in a restart-safe workflow. |
| [**github-issues-to-dingtalk**](https://github.com/lishehao/github-issues-to-dingtalk) | GitHub issue activity -> incremental sync -> digest-style DingTalk summaries for responsible owners. | Summarized **1000+ issues/day**, covered about **50 owners**, and stayed in production-style use for around **six months**. |

---

## Selected Projects

| Project | System Type | What I Owned / Built |
| --- | --- | --- |
| [**RPG_Demo**](https://github.com/lishehao/RPG_Demo) | AI narrative product | Full-stack author -> publish -> play loop, LLM runtime contracts, frontend product surface, state/review experience. |
| [**auto-load-off-test**](https://github.com/lishehao/auto-load-off-test) | Instrument automation | Python desktop workflow for AWG/oscilloscope-style validation, SCPI/PyVISA control, exports, and test repeatability. |
| [**mail-to-dingtalk-todo**](https://github.com/lishehao/mail-to-dingtalk-todo) | Operations automation | IMAP parsing, structured task extraction, DingTalk task creation, idempotency, and internal workflow handoff. |
| [**github-issues-to-dingtalk**](https://github.com/lishehao/github-issues-to-dingtalk) | DevOps workflow automation | Incremental issue sync, digest-style notification, owner handoff, and DingTalk integration. |
| [**ScholarPath**](https://github.com/lishehao/ScholarPath) | AI advising and decision system | Guided intake, recommendation surfaces, semantic retrieval, and application-decision workflow logic. |

---

## Working Thesis

AI is making simple implementation cheaper. That makes product judgment and surrounding workflow design more important:

- What user problem is worth automating?
- What state should the product remember?
- What is the model allowed to change?
- How do users inspect, undo, replay, and trust the result?
- How does the team know whether the workflow got better?

That is the space I like building in: **product judgment + full-stack implementation + reliable workflow design**.

---

## Stack

<p>
  <img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/TypeScript-React-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript and React" />
  <img src="https://img.shields.io/badge/FastAPI-runtime-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/badge/Pydantic-contracts-E92063?style=flat-square" alt="Pydantic" />
  <img src="https://img.shields.io/badge/SQLite-state-003B57?style=flat-square&logo=sqlite&logoColor=white" alt="SQLite" />
  <img src="https://img.shields.io/badge/PyVISA-SCPI-5b5f97?style=flat-square" alt="PyVISA and SCPI" />
  <img src="https://img.shields.io/badge/LLM%20Workflows-state%20%2B%20eval-d4a853?style=flat-square" alt="LLM workflows" />
  <img src="https://img.shields.io/badge/Product%20Surfaces-demo%20%2B%20review-15161c?style=flat-square" alt="Product surfaces" />
</p>

---

## Current Focus

I am currently building portfolio-ready systems that combine:

- **AI product surfaces** users can try,
- **typed backend contracts** reviewers can inspect,
- **automation workflows** that reduce repeated manual work,
- **evidence and logs** showing what happened and why.

I am also exploring newer agent-product work through an ongoing internship, but I keep this profile centered on completed projects until those results are mature enough to stand on their own.
