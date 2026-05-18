---
title: Feldskript hinzufügen
type: docs
weight: 10
url: /de/python-net/add-field-script/
description: Interaktive PDF-Formulare können JavaScript enthalten, um Aktionen zu automatisieren, wenn Benutzer mit Formularfeldern interagieren. Mit Aspose.PDF for Python können Entwickler Scripts einfach an Formularelemente wie Schaltflächen oder Textfelder anhängen.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: JavaScript-Aktionen zu PDF-Formularfeldern mit Python hinzufügen
Abstract: Dieser Artikel erklärt, wie man ein PDF-Formular öffnet, JavaScript-Code einem bestimmten Formularfeld zuweist, zusätzliche Skriptaktionen anhängt und das aktualisierte Dokument speichert. Das Beispiel verwendet die FormEditor-Klasse aus der Aspose.PDF Facades API, um das Formularverhalten programmgesteuert zu manipulieren.
---

## JavaScript-Aktionen zu PDF-Formularfeldern mit Python hinzufügen

Dieses Code‑Snippet ermöglicht es Ihnen, JavaScript‑Aktionen zu einem bestehenden PDF-Formularfeld mit der Aspose.PDF for Python‑Bibliothek hinzuzufügen. Es öffnet ein PDF‑Dokument, weist einem Formularfeld eine JavaScript‑Aktion zu und fügt ein Skript hinzu, das ausgeführt wird, wenn das Feld ausgelöst wird. Abschließend wird das aktualisierte PDF als neue Datei gespeichert.
Verwenden des [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) Klasse aus dem [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) Modul, Sie können programmgesteuert JavaScript an vorhandene Formularfelder anhängen:

1. Öffnen Sie ein vorhandenes PDF-Formular.
1. Legen Sie eine JavaScript-Aktion für ein bestimmtes Feld fest.
1. Fügen Sie dem selben Feld eine weitere JavaScript‑Aktion hinzu.
1. Speichern Sie das modifizierte PDF‑Dokument.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_field_script(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Set JavaScript action for the field
    form_editor.set_field_script(
        "Script_Demo_Button", "app.alert('Script 1 has been executed');"
    )

    # Add JavaScript action to the field
    form_editor.add_field_script(
        "Script_Demo_Button", "app.alert('Script 2 has been executed');"
    )

    # Save output PDF file
    form_editor.save(output_file_name)
```
