---
title: Alle Felder abflachen
type: docs
weight: 10
url: /de/python-net/flatten-all-fields/
description: Dieses Beispiel zeigt, wie man alle Formularfelder in einem PDF mit Aspose.PDF for Python via .NET abflacht. Es demonstriert, wie man ein PDF-Dokument bindet, jedes interaktive Formularelement in statischen Seiteninhalt umwandelt und die fertiggestellte Datei speichert.
lastmod: "2026-05-18"
---

Das Abflachen entfernt die Interaktivität aus PDF-Formularen, indem Feldwerte direkt in das Dokumentlayout integriert werden. In diesem Beispiel wird das [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) Facade von [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) wird verwendet, um das Quell-PDF zu binden und die Methode flatten_all_fields() anzuwenden, die alle Felder in nicht editierbaren Inhalt umwandelt.

1. Initialisieren Sie pdf_facades.Form(), um mit PDF‑Formularfeldern zu interagieren.
1. Rufen Sie 'bind_pdf()' auf, um das Quell-Dokument anzuhängen.
1. Rufen Sie 'flatten_all_fields()' auf, um alle interaktiven Felder in statischen Inhalt zu konvertieren.
1. Speichern Sie das aktualisierte Document.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Flatten all fields
def flatten_all_fields(infile, outfile):
    """Flatten all fields in a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Flatten all fields in the PDF document
    pdf_form.flatten_all_fields()

    # Save updated PDF
    pdf_form.save(outfile)
```
