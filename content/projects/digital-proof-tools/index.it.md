---
title: "Digital Proof Tools for Philosophical Logic"
subtitle: "Formalizzare l’identità di contenuto nella [semantica dei verificatori](https://truthmakersemantics.github.io/) con [Lean 4](https://lean-lang.org/), [piani di dimostrazione](https://github.com/PatrickMassot/leanblueprint) redatti da persone e sviluppo di dimostrazioni assistito dall’IA."
description: "Un progetto finanziato da NWO che formalizza l’equivalenza bilaterale nella semantica dei verificatori e valuta lo sviluppo di dimostrazioni assistito dall’IA in Lean."
date: 2026-07-24
publishDate: 2026-09-01T00:00:00+02:00
draft: false
layout: "lean"
funder: "NWO Open Competition – XS"
funder_url: "https://www.nwo.nl/en/calls/ssh-open-competition-xs-2026-round-2"
project_period: "12 mesi"
milestones:
  - title: "Strategia di ricerca e piano di dimostrazione"
    status: "planned"
    description: "Mantenere un repository di strategia contenente un piano di dimostrazione creato con [`leanblueprint`](https://github.com/PatrickMassot/leanblueprint) che espliciti le dipendenze, schemi dimostrativi redatti da persone, skill per agenti IA e documentazione del processo di formalizzazione assistito dall’IA."
  - title: "Libreria Lean per la semantica dei verificatori"
    status: "planned"
    description: "Formalizzare in [Lean 4](https://lean-lang.org/) le definizioni e i risultati fondamentali sul contenuto nella semantica dei verificatori, sull’argomento e sulla relazione di pertinenza tematica, utilizzando [Mathlib](https://mathlib.org/) ove possibile, e pubblicare la libreria in un repository [GitHub](https://github.com/) pubblico."
  - title: "Oggetti di dimostrazione digitali"
    status: "planned"
    description: "Produrre [file Lean verificati dal kernel](https://lean-lang.org/doc/reference/latest/ValidatingProofs/), nodi completati del piano di dimostrazione e la relativa documentazione dello sviluppo delle dimostrazioni per il problema di caratterizzazione."
  - title: "Pubblicazioni e divulgazione dei risultati"
    status: "planned"
    description: "Presentare i risultati logici e la valutazione metodologica dello sviluppo di dimostrazioni assistito dall’IA in articoli specialistici e interventi a convegni."
collaborators:
  - name: "Mark Jago"
    url: "https://www.markjago.net/"
---

Digital Proof Tools for Philosophical Logic è un progetto di dodici mesi che verifica se i metodi digitali di dimostrazione sviluppati in matematica possano sostenere la ricerca sostanziale in logica filosofica.

Il caso di studio tecnico è il problema aperto della caratterizzazione dell’equivalenza bilaterale (ossia l’identità dei verificatori e dei falsificatori in tutti i modelli) nella [semantica dei verificatori](https://truthmakersemantics.github.io/). Il progetto formalizzerà il quadro semantico pertinente in [Lean](https://lean-lang.org/), utilizzerà un [piano di dimostrazione](https://github.com/PatrickMassot/leanblueprint) redatto da persone e con dipendenze esplicite per guidare la ricerca delle dimostrazioni, e valuterà gli agenti di programmazione verificandone i risultati sia con [il kernel di Lean](https://lean-lang.org/doc/reference/latest/ValidatingProofs/) sia rispetto alla strategia matematica prevista. L’obiettivo è un processo riproducibile che colleghi argomenti filosofici, enunciati formali, ricerca delle dimostrazioni e oggetti di dimostrazione verificati.
