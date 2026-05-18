---
title: Exportieren nach FDF
type: docs
weight: 10
url: /de/python-net/export-to-fdf/
description: Dieses Beispiel erklärt, wie man PDF-Formularfelddaten in eine FDF (Forms Data Format)-Datei exportiert, indem man Aspose.PDF for Python via .NET verwendet. Es demonstriert, wie man über die Form‑Fassade auf interaktive Formulardaten zugreift, ein Quell‑PDF‑Dokument bindet und die extrahierten Werte in einen FDF‑Stream speichert.
lastmod: "2026-05-18"
---

FDF ist ein leichtgewichtiges Format, das speziell für das Speichern und Übertragen von PDF-Formulardaten entwickelt wurde, ohne das gesamte Dokument einzubetten. In diesem Beispiel, a [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) Objekt wird aus dem [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) Modul, das Entwicklern ermöglicht, mit AcroForm-Feldern zu interagieren und deren Werte zu exportieren.

1. Erstellen Sie eine Instanz von pdf_facades.Form(), um mit PDF-Formularfeldern zu arbeiten.
1. Rufen Sie \u0027bind_pdf()\u0027 auf, um das PDF-Dokument, das das Formular enthält, anzuhängen.
1. Verwenden Sie 'open(')' um einen beschreibbaren Binärstream für die FDF-Datei zu erstellen.
1. Formulardaten exportieren. Rufen Sie 'export_fdf()' auf, um alle Werte der Formularfelder zu extrahieren und zu speichern.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Export Data to FDF
def export_form_data_to_fdf(infile, outfile):
    """Export PDF form data to FDF file."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Create FDF file stream
    with open(outfile, "wb") as fdf_output_stream:
        # Export form data to FDF file
        pdf_form.export_fdf(fdf_output_stream)
```
