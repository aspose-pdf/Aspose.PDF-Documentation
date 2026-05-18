---
title: AcroForm extrahieren - Formulardaten aus PDF in Python extrahieren
linktitle: Extrahiere AcroForm
type: docs
weight: 30
url: /de/python-net/extract-form/
description: Werte aus AcroForm-Feldern in PDF-Dokumenten extrahieren, indem Aspose.PDF for Python via .NET verwendet wird.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Wie man Form-Daten aus PDF mit Python erhält
Abstract: Dieser Artikel zeigt, wie man Daten aus AcroForm-Feldern in PDF-Dokumenten extrahiert, indem Aspose.PDF for Python via .NET verwendet wird. Das Beispiel iteriert über die Namen der Formularfelder, liest Werte über die Form-Fassade und gibt ein Wörterbuch für die nachgelagerte Verarbeitung zurück. Dieser Workflow ist nützlich für Berichte, Validierung und die Integration mit externen Systemen.
---

## Daten aus Form extrahieren

### Werte aus allen Feldern in einem PDF-Dokument abrufen

Um Werte aus allen Feldern in einem PDF-Dokument zu lesen, iterieren Sie durch die FormField-Namen und rufen jeden Wert aus der [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) Fassade.

Verwenden Sie die folgenden Schritte:

1. Binden Sie das Eingabe-PDF an ein `Form` Objekt.
1. Durchlaufen `field_names`.
1. Lese jeden Wert mit `get_field()`.
1. Werte in einem Wörterbuch speichern.
1. Geben Sie die extrahierten Werte zurück oder verarbeiten Sie sie.

Das folgende Python-Code‑Snippet zeigt diesen Ansatz.

```python
import aspose.pdf as ap


def get_values_from_all_fields(input_file_name):
    form = ap.facades.Form(input_file_name)

    form_values = {}
    for field_name in form.field_names:
        form_values[field_name] = form.get_field(field_name)

    print(form_values)
    return form_values
```

## Verwandte Themen

- [AcroForm erstellen](/pdf/de/python-net/create-form/)
- [AcroForm ausfüllen](/pdf/de/python-net/fill-form/)
- [Formulardaten importieren und exportieren](/pdf/de/python-net/import-export-form-data/)
- [AcroForm ändern](/pdf/de/python-net/modifying-form/)