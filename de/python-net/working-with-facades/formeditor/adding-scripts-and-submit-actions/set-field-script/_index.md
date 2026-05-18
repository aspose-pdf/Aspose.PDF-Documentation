---
title: Feldskript festlegen
type: docs
weight: 30
url: /de/python-net/set-field-script/
description: Dieses Code‑Snippet zeigt, wie man einer Formularfeld in einem PDF‑Dokument mit Aspose.PDF for Python eine JavaScript‑Aktion zuweist.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: JavaScript‑Aktionen für PDF‑Formularfelder mit Python festlegen
Abstract: Dieser Artikel erklärt, wie man ein PDF‑Dokument öffnet, einem Formularfeld JavaScript‑Code zuweist, das Skript mit der FormEditor‑Klasse aktualisiert und die geänderte Datei speichert. Das Beispiel zeigt, wie vorhandene Skripte überschrieben werden können, um das Verhalten von Formularfeldern zu ändern.
---

Interaktive PDF‑Formulare nutzen häufig JavaScript, um Aufgaben wie das Anzeigen von Warnungen, die Validierung von Eingaben oder das Auslösen dynamischen Formularverhaltens auszuführen. Mit Aspose.PDF for Python können Entwickler diese Skripte programmgesteuert verwalten.

Das Beispiel fügt dem Feld zunächst eine JavaScript‑Aktion hinzu und ersetzt sie anschließend mit einem anderen Skript mittels der 'set_field_script'-Methode. Dieser Ansatz ermöglicht es Entwicklern, das interaktive Verhalten von PDF‑Formularelementen wie Schaltflächen oder Eingabefeldern zu steuern oder zu aktualisieren.

Das in diesem Beispiel verwendete Formularfeld heißt 'Script_Demo_Button' und stellt typischerweise eine Schaltfläche dar, die das zugewiesene Skript ausführt, wenn sie ausgelöst wird.

Verwenden des [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) Klasse aus dem [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) Modul, Entwickler können programmatisch JavaScript-Aktionen verwalten, die mit Formularfeldern verknüpft sind:

1. Öffnen Sie ein vorhandenes PDF-Formulardokument.
1. Fügen Sie einem Formularfeld eine JavaScript-Aktion hinzu.
1. Setzen (ersetzen) Sie die JavaScript-Aktion durch ein neues Skript.
1. Speichern Sie das modifizierte PDF‑Dokument.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_field_script(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Add JavaScript action to the field
    form_editor.add_field_script(
        "Script_Demo_Button", "app.alert('Script 1 has been executed');"
    )

    # Set JavaScript action for the field
    form_editor.set_field_script(
        "Script_Demo_Button", "app.alert('Script 2 has been executed');"
    )

    # Save output PDF file
    form_editor.save(output_file_name)
```
