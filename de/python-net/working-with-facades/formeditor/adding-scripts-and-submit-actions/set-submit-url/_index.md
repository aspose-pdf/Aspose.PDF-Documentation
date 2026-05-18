---
title: Submit-URL festlegen
type: docs
weight: 40
url: /de/python-net/set-submit-url/
description: Dieses Beispiel demonstriert, wie man mit Aspose.PDF für Python eine Submit-Aktion für ein Schaltflächenfeld in einem PDF-Formular konfiguriert.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Eine Submit-URL für eine PDF-Formular-Schaltfläche mit Python festlegen
Abstract: Dieser Artikel erklärt, wie man ein vorhandenes PDF-Formular öffnet, eine Übermittlungs-URL für ein Schaltflächenfeld mithilfe der FormEditor-Klasse definiert, prüft, ob der Vorgang erfolgreich war, und das aktualisierte PDF-Dokument speichert.
---

PDF-Formulare können so gestaltet werden, dass sie ihre Daten an einen Webserver senden, wenn ein Benutzer auf eine Submit-Schaltfläche klickt. Mit Aspose.PDF für Python können Entwickler programmgesteuert eine Submit-Aktion für Formularfelder konfigurieren.
Durch das Festlegen einer Submit-URL kann das Formular die vom Benutzer eingegebenen Daten an einen Server senden, wenn die Schaltfläche geklickt wird. Diese Funktionalität ist nützlich für Workflows, bei denen PDF-Formulare Informationen an Webanwendungen, Datenbanken oder Verarbeitungsdienste übermitteln müssen.

Verwenden des [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) Klasse aus dem [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) Modul, Entwickler können programmgesteuert einer Schaltfläche in einem bestehenden PDF-Formular eine Submit-URL zuweisen.

1. Öffnen Sie ein vorhandenes PDF-Formular.
1. Suchen Sie ein Schaltflächenfeld mit dem Namen Script_Demo_Button.
1. Weisen Sie eine URL zu, an die die Formulardaten gesendet werden.
1. Vergewissern Sie sich, dass die Aktion erfolgreich angewendet wurde.
1. Speichern Sie das aktualisierte PDF-Dokument.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_submit_url(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Set license
    set_license()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Set submit URL for the button
    if not form_editor.set_submit_url(
        "Script_Demo_Button", "http://www.example.com/submit"
    ):
        raise Exception("Failed to set submit URL")

    # Save output PDF file
    form_editor.save(output_file_name)
```
