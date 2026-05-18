---
title: Verwaltung von Nutzungsrechten
type: docs
weight: 100
url: /de/python-net/usage-rights-management/
description: Erfahren Sie, wie Sie Nutzungsrechte in PDF-Dokumenten mit PdfFileSignature in Python erkennen und entfernen.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Entfernen von PDF-Nutzungsrechten in Python
Abstract: Dieser Artikel erklärt, wie man mit Aspose.PDF for Python via .NET Nutzungsrechte in PDF-Dokumenten prüft und entfernt. Er zeigt, wie man überprüft, ob ein PDF Nutzungsrechte enthält, und wie man nach deren Entfernung eine neue Version des Dokuments speichert.
---

Aspose.PDF for Python via .NET stellt die [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) Fassade für die Arbeit mit signierten PDFs und zugehörigen Nutzungsrechte-Einstellungen. In einigen Workflows müssen Sie möglicherweise prüfen, ob ein Dokument Nutzungsrechte enthält, und diese entfernen, bevor Sie eine aktualisierte Version der Datei speichern.

Dieses Beispiel demonstriert eine häufige Aufgabe im Umgang mit Nutzungsrechten:

1. Prüfen, ob ein PDF Nutzungsrechte enthält.
1. Entfernen Sie die Nutzungsrechte aus dem Dokument.
1. Speichern Sie die aktualisierte PDF-Datei.

## Prüfen, ob das PDF Nutzungsrechte enthält

Bevor die Nutzungsrechte entfernt werden, prüft das Beispiel den aktuellen Zustand des Dokuments, indem es aufruft `contains_usage_rights()`. Dies ermöglicht es Ihnen, zu bestätigen, ob Nutzungsrechte vorhanden sind, bevor Änderungen vorgenommen werden.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def check_usage_rights(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        had_usage_rights = pdf_signature.contains_usage_rights()
        print(f"PDF contains usage rights: {had_usage_rights}")
    finally:
        pdf_signature.close()
```

## Nutzungsrechte aus dem PDF entfernen

Verwenden `remove_usage_rights()` wenn das Dokument seine bestehenden Nutzungsrechte-Einstellungen nicht mehr beibehalten soll. Das Beispiel prüft den Ausgangszustand, entfernt die Rechte und speichert das aktualisierte PDF in einer neuen Datei.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def remove_usage_rights(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        had_usage_rights = pdf_signature.contains_usage_rights()
        print(f"PDF contains usage rights before removal: {had_usage_rights}")
        pdf_signature.remove_usage_rights()
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```
