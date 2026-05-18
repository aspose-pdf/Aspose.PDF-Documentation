---
title: PDF-Dateien in Python zusammenführen
linktitle: PDF-Dateien zusammenführen
type: docs
weight: 50
url: /de/python-net/merge-pdf/
description: Erfahren Sie, wie Sie mehrere PDF‑Dateien in einem einzigen Dokument mit Python zusammenführen.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF‑Seiten mit Python kombinieren
Abstract: Dieser Artikel behandelt das häufige Bedürfnis, mehrere PDF-Dateien zu einem einzigen Dokument zusammenzuführen, ein Vorgang, der für die Organisation und Optimierung von Speicherung und Freigabe von PDF-Inhalten wertvoll ist. Er untersucht die Verwendung von Aspose.PDF for Python via .NET, um PDF-Dateien effizient zu kombinieren, und weist darauf hin, dass das Zusammenführen von PDFs in Python ohne Drittanbieterbibliotheken eine Herausforderung darstellen kann. Der Artikel bietet eine Schritt-für-Schritt-Anleitung zum Verketten von PDF-Dateien - Erstellung eines neuen Dokuments, Zusammenführen der Dateien und Speichern des zusammengeführten Dokuments. Ein Code‑Snippet demonstriert die Implementierung mit Aspose.PDF und hebt die Fähigkeit der Bibliothek hervor, den Zusammenführungsprozess zu vereinfachen. Zusätzlich wird der Aspose.PDF Merger vorgestellt, ein Online‑Tool zum Zusammenführen von PDFs, das es Benutzern ermöglicht, die Funktionalität in einer webbasierten Umgebung zu erkunden.
---

## PDF-Dateien mit Python und DOM zusammenführen

Um zwei PDF-Dateien zu verketten:

1. Ein neues Dokument erstellen.
1. PDF-Dateien zusammenführen
1. Speichern Sie das zusammengeführte Dokument

Mehrere PDF-Dokumente zu einer einzigen Datei kombinieren:

```python
import sys
import aspose.pdf as ap
from os import path

def merge_two_documents(infile1, infile2, outfile):
    document1 = ap.Document(infile1)
    document2 = ap.Document(infile2)
    document1.pages.add(document2.pages)
    document1.save(outfile)
```

## Live‑Beispiel

[Aspose.PDF-Merger](https://products.aspose.app/pdf/merger) ist eine kostenlose Online-Webanwendung, die es ermöglicht, zu untersuchen, wie die Präsentationszusammenführungsfunktion funktioniert.

[![Aspose.PDF-Merger](merger.png)](https://products.aspose.app/pdf/merger)

