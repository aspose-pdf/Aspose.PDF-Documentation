---
title: AcroForm ausfüllen - PDF-Formular mit Python ausfüllen
linktitle: AcroForm ausfüllen
type: docs
weight: 20
url: /de/python-net/fill-form/
description: AcroForm-Felder in einem PDF-Dokument ausfüllen, indem Aspose.PDF for Python via .NET verwendet wird.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Wie man ein Formularfeld in einem PDF mit Python ausfüllt
Abstract: Dieser Artikel erklärt, wie man AcroForm-Felder in einem PDF-Dokument mithilfe von Aspose.PDF for Python via .NET ausfüllt. Das Beispiel verwendet die Form-Fassade, ordnet Feldnamen in einem Wörterbuch neuen Werten zu, aktualisiert passende Felder und speichert das Ergebnis‑PDF. Dieser Ansatz ist nützlich für automatisierte Dokumentvervollständigungs‑Workflows und die Massenverarbeitung von Formularen.
---

## Formularfeld in einem PDF-Dokument ausfüllen

Das folgende Beispiel füllt mehrere Felder in einem bestehenden PDF-Formular aus, indem es die [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) Fassade.

Verwenden Sie die folgenden Schritte:

1. Erstelle ein Wörterbuch mit Feldnamen und Werten.
1. Binde das Eingabe-PDF an ein Form-Objekt.
1. Iteriere über die verfügbaren Formularfelder.
1. Fülle Felder, die im Wörterbuch vorhanden sind.
1. Speichere das aktualisierte PDF.

```python
import aspose.pdf as ap

def fill_form(input_file_name, output_file_name):
    new_field_values = {
        "First Name": "Alexander_New",
        "Last Name": "Greenfield_New",
        "City": "Yellowtown_New",
        "Country": "Redland_New",
    }

    form = ap.facades.Form(input_file_name)

    for field_name in form.field_names:
        if field_name in new_field_values:
            form.fill_field(field_name, new_field_values[field_name])

    form.save(output_file_name)
```

## Verwandte Themen

- [AcroForm erstellen](/pdf/de/python-net/create-form/)
- [Extrahiere AcroForm](/pdf/de/python-net/extract-form/)
- [Formulardaten importieren und exportieren](/pdf/de/python-net/import-export-form-data/)