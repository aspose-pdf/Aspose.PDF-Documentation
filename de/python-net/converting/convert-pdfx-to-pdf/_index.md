---
title: PDF/A und PDF/UA nach PDF in Python konvertieren
linktitle: PDF/A und PDF/UA nach PDF konvertieren
type: docs
weight: 120
url: /de/python-net/convert-pdf_x-to-pdf/
lastmod: "2026-05-18"
description: Erfahren Sie, wie Sie die PDF/A- und PDF/UA-Konformität aus PDF-Dateien in Python mit Aspose.PDF for Python via .NET entfernen und sie als Standard-PDF-Dokumente speichern.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Wie man PDF/A und PDF/UA in ein Standard-PDF in Python konvertiert
Abstract: Dieser Artikel erklärt, wie Sie die PDF/A- und PDF/UA-Konformität aus standardbasierten PDF-Dokumenten mit Aspose.PDF for Python via .NET entfernen. Er behandelt Szenarien, in denen Sie ein Standard-PDF anstelle einer archivierungs- oder barrierefreiheitsbeschränkten Datei benötigen, und zeigt, wie das Ergebnis nach dem Entfernen von Konformitäts-Metadaten und Einschränkungen gespeichert wird.
---

Verwenden Sie diese Seite, wenn Sie ein standardbasiertes PDF, wie PDF/A oder PDF/UA, wieder in ein reguläres PDF-Dokument für nachgelagerte Bearbeitung, Verarbeitung oder Weiterverteilung konvertieren müssen.

Standardkonforme PDFs sind für Archivierungs-, Druck- und Barrierefreiheits‑Workflows hilfreich, aber in einigen Fällen müssen Sie diese Konformität entfernen, bevor Sie die Datei in andere Systeme oder Pipelines integrieren. Aspose.PDF for Python via .NET ermöglicht dies programmgesteuert und anschließend das Speichern des Ergebnisses als Standard‑PDF‑Datei.

## PDF/A in PDF konvertieren

Dieses Beispiel entfernt PDF/A‑Konformitätsmetadaten und -Beschränkungen aus einer PDF, sodass das Dokument erneut als reguläre PDF‑Datei gespeichert werden kann.

1. Laden Sie das PDF-Dokument mit 'ap.Document'.
1. Rufen Sie 'remove_pdfa_compliance()' auf, um alle PDF/A‑bezogenen Konformitätseinstellungen und Metadaten zu entfernen.
1. Speichern Sie die resultierende PDF an dem Ausgabepfad.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDFA_to_PDF(infile, outfile):
    document = ap.Document(infile)
    document.remove_pdfa_compliance()
    document.save(outfile)
```

## Entfernen der PDF/UA-Konformität

Dieses Beispiel zeigt, wie die PDF/UA-bezogene Konformität entfernt wird, damit das Dokument als Standard-PDF für Workflows ohne spezifische Barrierefreiheit gespeichert werden kann.

1. Laden Sie das PDF-Dokument mit 'ap.Document()'.
1. Rufen Sie 'document.remove_pdfa_compliance()' auf, um alle PDF/A-Beschränkungen oder Konformitätseinstellungen zu entfernen.
1. Speichern Sie das modifizierte PDF unter 'path_outfile'.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDFUA_to_PDF(infile, outfile):
    document = ap.Document(infile)
    document.remove_pdf_ua_compliance()
    document.save(outfile)
```

## Wann man diesen Workflow verwendet

- Entfernen Sie die Compliance‑Einstellungen, bevor Sie ein Dokument in eine Toolchain senden, die keine PDF/A‑ oder PDF/UA‑Beschränkungen erfordert.
- Vereinfachen Sie die nachgelagerte Dokumentenverarbeitung, wenn Archivierungs‑ oder Barrierefreiheits‑Metadaten nicht mehr benötigt werden.
- Normalisieren Sie Eingabe‑PDFs, bevor Sie sie in andere Formate exportieren.

## Verwandte Konvertierungen

- [PDF in PDF/A, PDF/E und PDF/X konvertieren](/pdf/de/python-net/convert-pdf-to-pdf_x/) Falls Sie den umgekehrten Workflow benötigen und standardskonforme PDFs erstellen möchten.
- [PDF in Word konvertieren](/pdf/de/python-net/convert-pdf-to-word/) für editierbare Dokumentausgabe nach dem Entfernen von Compliance-Beschränkungen.
- [PDF in HTML konvertieren](/pdf/de/python-net/convert-pdf-to-html/) für browserfreundliche Ausgabe aus Standard-PDF-Dateien.
