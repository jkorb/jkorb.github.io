---
title: "Digital Proof Tools for Philosophical Logic"
subtitle: "Formalizing same-saying in [truthmaker semantics](https://truthmakersemantics.github.io/) with [Lean 4](https://lean-lang.org/), human-written [proof blueprints](https://github.com/PatrickMassot/leanblueprint), and AI-assisted proof development."
description: "An NWO-funded project formalizing bilateral equivalence in truthmaker semantics and evaluating AI-assisted proof development in Lean."
date: 2026-07-24
publishDate: 2026-09-01T00:00:00+02:00
draft: false
layout: "lean"
funder: "NWO Open Competition – XS"
funder_url: "https://www.nwo.nl/en/calls/ssh-open-competition-xs-2026-round-2"
project_period: "12 months"
milestones:
  - title: "Research strategy and proof blueprint"
    status: "planned"
    description: "Maintain a strategy repository containing a dependency-aware proof blueprint built with [`leanblueprint`](https://github.com/PatrickMassot/leanblueprint), human-written proof plans, agentic skills, and records of the AI-assisted formalization workflow."
  - title: "Lean library for truthmaker semantics"
    status: "planned"
    description: "Formalize the core definitions and results on truthmaker content, subject matter, and aboutness in [Lean 4](https://lean-lang.org/), building on [Mathlib](https://mathlib.org/) where possible, and release the library in a public [GitHub](https://github.com/) repository."
  - title: "Digital proof objects"
    status: "planned"
    description: "Produce [kernel-checked Lean files](https://lean-lang.org/doc/reference/latest/ValidatingProofs/), completed blueprint nodes, and the associated proof-development records for the characterization problem."
  - title: "Papers and dissemination"
    status: "planned"
    description: "Report the logical results and the methodological assessment of AI-assisted proof development in specialist papers and conference presentations."
collaborators:
  - name: "Mark Jago"
    url: "https://www.markjago.net/"
---

Digital Proof Tools for Philosophical Logic is a twelve-month project testing whether digital proof methods developed in mathematics can support substantive research in philosophical logic.

The technical case study is the open problem of characterizing bilateral equivalence (i.e. sameness of truthmakers and falsemakers in all models) in [truthmaker semantics](https://truthmakersemantics.github.io/). The project will formalize the relevant semantic framework in [Lean](https://lean-lang.org/), use a human-authored and dependency-aware [proof blueprint](https://github.com/PatrickMassot/leanblueprint) to guide proof search, and evaluate coding agents by checking their output against both [Lean's kernel](https://lean-lang.org/doc/reference/latest/ValidatingProofs/) and the intended mathematical strategy. The aim is a reproducible workflow connecting philosophical arguments, formal statements, proof search, and verified proof objects.
