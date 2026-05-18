---
title: Spezifische Felder flachlegen
type: docs
weight: 20
url: /de/python-net/flatten-specific-fields/
description: Dieser Abschnitt zeigt, wie PDF-Formularfelder mit Aspose.PDF for Python via .NET verwaltet und geändert werden können. Er umfasst praktische Beispiele für das Flachlegen bestimmter Felder, das Flachlegen aller Formularfelder und das programmgesteuerte Umbenennen vorhandener Felder.
lastmod: "2026-05-18"
---

Die Verwaltung von Formularfeldern ist ein wichtiger Bestandteil von PDF-Verarbeitungsabläufen. Das Flachlegen von Feldern entfernt die Interaktivität, indem Formular-Elemente in regulären Seiteninhalt umgewandelt werden, während das Umbenennen von Feldern hilft, Namenskonventionen zu standardisieren und die Datenverarbeitung zu erleichtern.

1. Initialisieren Sie pdf_facades.Form(), um auf PDF-Formularfelder zuzugreifen und diese zu verwalten.
1. Verwenden Sie 'bind_pdf()', um das Eingabedokument anzuhängen.
1. Geben Sie Feldnamen an und rufen Sie 'flatten_field()' auf, um ausgewählte Felder in statischen Inhalt zu konvertieren.
1. Rufen Sie 'flatten_all_fields()' auf, um die Interaktivität aller Formularfelder zu entfernen.
1. Definieren Sie alte und neue Feldnamen und wenden Sie 'rename_field()' an.
1. Speichere das aktualisierte PDF.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Flatten specific fields
def flatten_specific_fields(infile, outfile):
    """Flatten specific fields in a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Flatten specific fields by their names
    fields_to_flatten = ["First Name", "Last Name"]
    for field_name in fields_to_flatten:
        pdf_form.flatten_field(field_name)

    # Save updated PDF
    pdf_form.save(outfile)
```
