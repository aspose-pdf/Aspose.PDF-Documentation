---
title: Submit-Flag festlegen
type: docs
weight: 50
url: /de/python-net/set-submit-flag/
description: Erfahren Sie, wie Sie programmgesteuert ein Submit-Flag für eine PDF-Formularschaltfläche mit Aspose.PDF für Python festlegen. Dadurch kann die Schaltfläche Formulardaten in einem bestimmten Format, z. B. XFDF, beim Klicken durch einen Benutzer übermitteln.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Submit-Flag für eine PDF-Formularschaltfläche mit Aspose.PDF für Python festlegen
Abstract: PDF-Formulare können so konfiguriert werden, dass Sie Formulardaten in verschiedenen Formaten an einen Server oder Endpunkt übermitteln. Durch das Setzen eines Submit-Flags auf ein Schaltflächenfeld können Entwickler festlegen, wie die Daten gesendet werden. Dieses Tutorial zeigt, wie die Klasse FormEditor verwendet wird, um ein Submit-Flag für eine vorhandene Sende-Schaltfläche in einem PDF-Dokument zu setzen und die aktualisierte Datei zu speichern.
---

PDF-Formulare enthalten häufig Submit‑Buttons, um Benutzereingaben an einen Server zu senden. Das Submit-Flag bestimmt das gesendete Datenformat (z. B. XFDF, FDF, HTML).

1. Ein PDF-Dokument binden.
1. Greifen Sie auf eine vorhandene Senden-Schaltfläche zu.
1. Setzen Sie das Sende-Flag für das gewünschte Format.
1. Speichern Sie das aktualisierte PDF-Dokument.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_submit_flag(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Set submit flag for the form
    form_editor.set_submit_flag("Script_Demo_Button", ap.facades.SubmitFormFlag.XFDF)

    # Save output PDF file
    form_editor.save(output_file_name)
```
