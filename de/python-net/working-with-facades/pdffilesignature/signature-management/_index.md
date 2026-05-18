---
title: Signaturverwaltung
type: docs
weight: 80
url: /de/python-net/signature-management/
description: Erfahren Sie, wie Sie digitale Signaturen aus PDF-Dokumenten entfernen und optional Signaturfelder mit PdfFileSignature in Python bereinigen.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Entfernen von PDF-Signaturen und Bereinigen von Signaturfeldern in Python
Abstract: Dieser Artikel erklärt, wie man vorhandene digitale Signaturen in PDF-Dokumenten mit Aspose.PDF for Python via .NET verwaltet. Er zeigt, wie man eine Signatur aus einem PDF entfernt und wie man eine Signatur zusammen mit dem zugehörigen Signaturfeld entfernt.
---

Aspose.PDF for Python via .NET stellt die [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) Fassade für die Arbeit mit vorhandenen digitalen Signaturen in PDF-Dokumenten. Zusätzlich zum Lesen und Validieren von Signaturen können Sie diese auch entfernen, wenn ein Workflow die Aktualisierung des signierten Inhalts oder das Löschen des Signaturfeldes erfordert.

Dieses Beispiel demonstriert zwei gängige Aufgaben der Signaturverwaltung:

1. Eine Signatur aus einem PDF-Dokument entfernen.
1. Eine Signatur entfernen und das zugehörige Signaturfeld bereinigen.

## Eine Signatur aus einem PDF entfernen

Verwenden `remove_signature()` wenn Sie die ausgewählte Signatur aus dem Dokument löschen möchten, während die zugrunde liegende Signaturfeldstruktur erhalten bleibt. Das Beispiel öffnet das signierte PDF, ermittelt den Signaturnamen, entfernt sie und speichert die aktualisierte Ausgabedatei.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def remove_signature_from_pdf(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        pdf_signature.remove_signature(sign_name)
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```

## Eine Signatur entfernen und das Feld bereinigen

Verwenden Sie die Überladung mit dem zusätzlichen `True` Markieren Sie, wenn Sie die Signatur entfernen und gleichzeitig das zugehörige Signaturfeld bereinigen möchten. Dies ist nützlich, wenn das Feld nach dem Löschen der Signatur nicht im Dokument verbleiben soll.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def remove_signature_with_field_cleanup(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        pdf_signature.remove_signature(sign_name, True)
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```
