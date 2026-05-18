---
title: Formulare in PDF mit Python posten
linktitle: Formulare posten
type: docs
weight: 75
url: /de/python-net/posting-form/
description: Fügen Sie Submit‑Schaltflächen und Submit‑Aktionen zu PDF AcroForms hinzu, indem Sie Aspose.PDF for Python via .NET verwenden.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: So fügen Sie Submit‑Schaltflächen und Formular‑Einreichungsaktionen zu einem PDF mit Python hinzu.
Abstract: Dieser Artikel zeigt zwei Ansätze, um Submit‑Funktionalität zu PDF‑Formularen hinzuzufügen, indem Sie Aspose.PDF for Python via .NET verwenden. Sie können über FormEditor einen vordefinierten Submit‑Button hinzufügen oder ein benutzerdefiniertes Schaltflächenfeld mit SubmitFormAction für erweiterte Kontrolle erstellen. Diese Muster helfen, PDF‑Formulare in serverseitige Formularverarbeitungs‑Endpunkte zu integrieren.
---

## Submit‑Button mit FormEditor hinzufügen

Das folgende Code‑Snippet demonstriert, wie man mit der FormEditor‑Klasse in Aspose.PDF für Python via .NET einen Submit‑Button zu einem PDF‑Formular hinzufügt. Der Button ist konfiguriert, um beim Klicken Formulardaten an eine angegebene URL zu senden.

1. Erstelle ein `FormEditor` Objekt.
1. Füge einen Submit‑Button zur Zielseite hinzu.
1. Setze die Übermittlungs‑URL und die Button‑Koordinaten.
1. Speichere das aktualisierte PDF.

```python
import aspose.pdf as ap

def add_submit_button(input_file_name, output_file_name):
    editor = ap.facades.FormEditor(input_file_name, output_file_name)
    editor.add_submit_btn(
        "submitbutton", 1, "Submit", "http://localhost/testing/show", 100, 450, 150, 475
    )
    editor.save()
```

## Benutzerdefinierte Absendeaktion hinzufügen

Das folgende Code‑Snippet erklärt, wie man in einem PDF‑Formular mit Aspose.PDF for Python via .NET eine benutzerdefinierte Submit‑Schaltfläche erstellt. Die Schaltfläche ist so konfiguriert, dass sie beim Klicken Formulardaten an eine angegebene URL sendet.

1. Öffnen Sie das PDF mit ap.Document().
1. Erstellen Sie eine Submit‑Aktion.
1. Setzen Sie die Ziel-URL und die Übermittlungsflags.
1. Erstellen Sie ein Schaltflächenfeld und binden Sie dessen Klickaktion.
1. Fügen Sie die Schaltfläche dem Formular hinzu.
1. Speichere das aktualisierte PDF.

```python
import aspose.pdf as ap

def add_submit_action(input_file_name, output_file_name):
    document = ap.Document(input_file_name)

    submit_action = ap.annotations.SubmitFormAction()
    submit_action.url = ap.FileSpecification("http://localhost:3000/submit")
    submit_action.flags = (
        ap.annotations.SubmitFormAction.EXPORT_FORMAT
        | ap.annotations.SubmitFormAction.SUBMIT_COORDINATES
    )

    rect = ap.Rectangle(10, 10, 100, 40)
    submit_button = ap.forms.ButtonField(document.pages[1], rect)
    submit_button.partial_name = "SubmitButton"
    submit_button.value = "Submit"
    submit_button.actions.on_release_mouse_btn = submit_action

    document.form.add(submit_button, 1)
    document.save(output_file_name)
```

## Verwandte Themen

- [AcroForm erstellen](/pdf/de/python-net/create-form/)
- [AcroForm ausfüllen](/pdf/de/python-net/fill-form/)
- [AcroForm ändern](/pdf/de/python-net/modifying-form/)
- [Formulardaten importieren und exportieren](/pdf/de/python-net/import-export-form-data/)