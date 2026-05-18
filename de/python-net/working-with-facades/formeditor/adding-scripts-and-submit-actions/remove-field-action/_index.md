---
title: Feldaktion entfernen
type: docs
weight: 20
url: /de/python-net/remove-field-action/
description: Das Entfernen von JavaScript aus Formularfeldern kann nützlich sein, wenn interaktive PDF-Formulare geändert, zuvor zugewiesene Aktionen deaktiviert oder Dokumente bereinigt werden, die unnötige Skripte enthalten.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: JavaScript-Aktionen aus PDF-Formularfeldern mit Python entfernen
Abstract: Mit Aspose.PDF for Python können Entwickler programmgesteuert JavaScript-Aktionen, die Formularfeldern zugeordnet sind, entfernen. Dieser Artikel erklärt, wie ein vorhandenes PDF-Formular geöffnet, das mit einem bestimmten Feld verknüpfte Skript mithilfe der FormEditor-Klasse entfernt, der Vorgang verifiziert und das modifizierte Dokument gespeichert wird.
---

PDF-Formulare enthalten häufig JavaScript-Aktionen, die ausgeführt werden, wenn Benutzer mit Formularelementen wie Schaltflächen oder Eingabefeldern interagieren. In einigen Fällen müssen diese Skripte entfernt werden, um das Formulargebaren zu vereinfachen, die Sicherheit zu erhöhen oder die Formularlogik zu aktualisieren. Entfernen Sie eine JavaScript-Aktion aus einem Formularfeld in einem PDF-Dokument mithilfe von Aspose.PDF for Python. Der Code öffnet ein vorhandenes PDF-Formular, findet ein bestimmtes Feld, entfernt die zugehörige JavaScript-Aktion und speichert das aktualisierte Dokument als neue PDF-Datei.

Verwenden des [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) Klasse aus dem [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/), Sie können JavaScript-Aktionen aus bestimmten Feldern in einem vorhandenen PDF-Formular entfernen:

1. Öffnen Sie ein vorhandenes PDF-Formular.
1. Suchen Sie ein Formularfeld mit dem Namen 'Script_Demo_Button'.
1. Entfernen Sie die mit diesem Feld verbundene JavaScript-Aktion.
1. Überprüfen Sie, ob das Entfernen erfolgreich war.
1. Speichern Sie das aktualisierte PDF-Dokument.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def remove_field_script(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Remove JavaScript action from the field
    if not form_editor.remove_field_action("Script_Demo_Button"):
        raise Exception("Failed to remove field script")

    # Save output PDF file
    form_editor.save(output_file_name)
```
