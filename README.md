<h1 align="center">Shehao Li</h1>

<p align="center">
  <strong>I build AI workflow systems with visible state, typed contracts, and product loops people can actually use.</strong>
</p>

<p align="center">
  UCSD Math-CS | AI products | full-stack systems | workflow automation
</p>

<p align="center">
  <a href="https://github.com/lishehao/RPG_Demo">
    <img src="https://img.shields.io/github/stars/lishehao/RPG_Demo?style=for-the-badge&logo=github&label=RPG_Demo" alt="RPG Demo GitHub stars" />
  </a>
  <a href="https://lishehao.github.io/RPG_Demo/">
    <img src="https://img.shields.io/badge/Demo-Tiny%20Stories-d4a853?style=for-the-badge" alt="Tiny Stories demo" />
  </a>
  <a href="https://github.com/lishehao/auto-load-off-test">
    <img src="https://img.shields.io/badge/Automation-Auto%20Load--Off%20Test-15161c?style=for-the-badge" alt="Auto Load-Off Test" />
  </a>
</p>

---

<p align="center">
  <img src="./assets/rpg-demo-profile-loop.gif" alt="RPG_Demo current product loop showing the home page, portfolio case study, reviewer mode, runtime inspector, advisor channel, and ending compiler" width="100%" />
</p>

| What I care about | Evidence in shipped work |
| --- | --- |
| **AI product loops** | Seed -> compile -> play -> inspect, with user-visible checkpoints instead of one-shot generation. |
| **Reliable workflow systems** | Typed API boundaries, persisted state, replayable outputs, and task handoff surfaces. |
| **Human-centered control** | Interfaces that show what changed, what the AI is using, and where the user can steer. |

---

## What I Build

I build products that make complicated workflows easier to run, inspect, and improve. This page focuses on work that is already shipped or substantially complete:

- **RPG_Demo / Tiny Stories**, a full-stack AI narrative product where a story seed becomes a playable, inspectable runtime.
- **Auto Load-Off Test**, a Python instrumentation workflow that turned repeated AWG/oscilloscope-style validation work into a repeatable desktop tool.

The common thread is simple: I like turning ambiguous product or operations problems into software with clear interfaces, state, logs, and user-visible checkpoints.

---

## Flagship: RPG_Demo / Tiny Stories

**RPG_Demo** is the implementation repo; **Tiny Stories** is the product experience inside it. A user writes a story seed, previews how the system interprets it, publishes it into a library, plays through natural-language turns, and reviews the ending with state, consequences, and transcript evidence still visible.

<p align="center">
  <img src="./assets/rpg-demo-profile-loop-poster.png" alt="RPG_Demo runtime inspector showing state, role, choices, inventory, and ending compiler status" width="100%" />
</p>

| Layer | What it proves |
| --- | --- |
| **Product loop** | Seed -> preview -> publish -> play -> review, with user-visible checkpoints instead of a one-shot generator. |
| **Frontend surface** | React + TypeScript UI for creation, story library, play sessions, replay, and state/review panels. |
| **Backend runtime** | FastAPI + Pydantic contracts, SQLite persistence, auth/session handling, and typed frontend/backend API boundaries. |
| **LLM workflow** | Structured generation, bounded advisor behavior, deterministic scaffolding before model calls, and runtime state carried across turns. |
| **Reviewability** | State, choices, consequences, transcript, and ending output are exposed so the system can be inspected after play. |

**Links:** [Repository](https://github.com/lishehao/RPG_Demo) | [Demo](https://lishehao.github.io/RPG_Demo/) | [Product site](https://rpg.shehao.app)

---

## Auto Load-Off Test

During my instrument-company internship, I built a Python desktop automation tool for repeated lab validation work. It is less flashy than an AI demo, but it shows the part of engineering I care about: making repeated real-world work reliable enough for other people to use.

| Project | What it automated | Evidence |
| --- | --- | --- |
| [**auto-load-off-test**](https://github.com/lishehao/auto-load-off-test) | AWG/oscilloscope-style sweep measurement and calibration workflow with PyVISA/SCPI control, Tkinter UI, structured outputs, and layered architecture. | Reduced test preparation and result organization effort by about **75%**; supported about **5 users**; includes tests for sweep planning, measurement IO, settings, and task flow. |

---

## Selected Projects

| Project | System Type | What I Owned / Built |
| --- | --- | --- |
| [**RPG_Demo**](https://github.com/lishehao/RPG_Demo) | AI narrative product | Full-stack author -> publish -> play loop, LLM runtime contracts, frontend product surface, state/review experience. |
| [**auto-load-off-test**](https://github.com/lishehao/auto-load-off-test) | Instrument automation | Python desktop workflow for AWG/oscilloscope-style validation, SCPI/PyVISA control, exports, and test repeatability. |
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
