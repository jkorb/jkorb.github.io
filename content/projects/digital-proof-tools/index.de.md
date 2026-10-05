---
title: "Digital Proof Tools for Philosophical Logic"
subtitle: "Formalisierung der Inhaltsgleichheit in der [Wahrmachersemantik](https://truthmakersemantics.github.io/) mit [Lean 4](https://lean-lang.org/), von Menschen verfassten [Beweisplänen](https://github.com/PatrickMassot/leanblueprint) und KI-gestützter Beweisentwicklung."
description: "Ein von NWO gefördertes Projekt zur Formalisierung bilateraler Äquivalenz in der Wahrmachersemantik und zur Bewertung KI-gestützter Beweisentwicklung in Lean."
date: 2026-07-24
publishDate: 2026-09-01T00:00:00+02:00
draft: false
layout: "lean"
funder: "NWO Open Competition – XS"
funder_url: "https://www.nwo.nl/en/calls/ssh-open-competition-xs-2026-round-2"
project_period: "12 Monate"
milestones:
  - title: "Forschungsstrategie und Beweisplan"
    status: "planned"
    description: "Ein Strategie-Repository pflegen, das einen mit [`leanblueprint`](https://github.com/PatrickMassot/leanblueprint) erstellten Beweisplan mit expliziten Abhängigkeiten, von Menschen verfasste Beweisskizzen, Skills für KI-Agenten und Aufzeichnungen zum KI-gestützten Formalisierungsprozess enthält."
  - title: "Lean-Bibliothek für Wahrmachersemantik"
    status: "planned"
    description: "Die zentralen Definitionen und Ergebnisse zu Wahrmacherinhalten, Gegenstandsbereichen und thematischem Bezug in [Lean 4](https://lean-lang.org/) formalisieren, soweit möglich auf [Mathlib](https://mathlib.org/) aufbauen und die Bibliothek in einem öffentlichen [GitHub](https://github.com/)-Repository bereitstellen."
  - title: "Digitale Beweisobjekte"
    status: "planned"
    description: "[Vom Lean-Kernel geprüfte Dateien](https://lean-lang.org/doc/reference/latest/ValidatingProofs/), abgeschlossene Knoten im Beweisplan und die zugehörige Dokumentation der Beweisentwicklung für das Charakterisierungsproblem erstellen."
  - title: "Publikationen und Ergebnisvermittlung"
    status: "planned"
    description: "Die logischen Ergebnisse und die methodologische Bewertung der KI-gestützten Beweisentwicklung in Fachartikeln und Konferenzvorträgen vorstellen."
collaborators:
  - name: "Mark Jago"
    url: "https://www.markjago.net/"
---

Digital Proof Tools for Philosophical Logic ist ein zwölfmonatiges Projekt, das untersucht, ob in der Mathematik entwickelte digitale Beweismethoden substanzielle Forschung in der philosophischen Logik unterstützen können.

Die technische Fallstudie ist das offene Problem der Charakterisierung bilateraler Äquivalenz (d. h. der Gleichheit von Wahrmachern und Falschmachern in allen Modellen) in der [Wahrmachersemantik](https://truthmakersemantics.github.io/). Das Projekt wird den relevanten semantischen Rahmen in [Lean](https://lean-lang.org/) formalisieren, die Beweissuche anhand eines von Menschen verfassten [Beweisplans](https://github.com/PatrickMassot/leanblueprint) mit expliziten Abhängigkeiten steuern und Programmieragenten bewerten, indem ihre Ergebnisse sowohl mit [Leans Kernel](https://lean-lang.org/doc/reference/latest/ValidatingProofs/) als auch anhand der vorgesehenen mathematischen Strategie überprüft werden. Ziel ist ein reproduzierbarer Arbeitsablauf, der philosophische Argumente, formale Aussagen, Beweissuche und verifizierte Beweisobjekte verbindet.
