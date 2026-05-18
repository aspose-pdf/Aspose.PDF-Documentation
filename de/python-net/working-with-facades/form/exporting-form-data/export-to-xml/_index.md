---
title: Export nach XML
type: docs
weight: 40
url: /de/python-net/export-to-xml/
description: Dieses Beispiel zeigt, wie PDF-Formulardaten mithilfe von Aspose.PDF for Python via .NET in eine XML‑Datei exportiert werden. Es demonstriert, wie ein PDF‑Dokument geladen, über das Form facade auf seine Formularfelder zugegriffen und die extrahierten Daten mithilfe der Form Class als strukturiertes XML gespeichert werden.
lastmod: "2026-05-18"
---

Der Export von Formulardaten ermöglicht es Entwicklern, Informationen, die in PDF AcroForms gespeichert sind, erneut zu verwenden, ohne Feldwerte manuell kopieren zu müssen. In diesem Beispiel wird ein [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) Objekt wird aus aspose.pdf erstellt. Im facades‑Modul wird das Quell‑PDF daran gebunden, und die Formulardaten werden in einen XML‑Stream geschrieben.

1. Erstellen Sie ein Form‑Objekt. Initialisieren Sie pdf_facades.Form(), um auf Formularfelder zuzugreifen und diese zu verwalten.
1. Verwenden Sie 'bind_pdf()', um das Quell‑PDF‑Dokument an die Form‑Instanz anzuhängen.
1. Erstellen Sie einen beschreibbaren Dateistream mit 'FileIO()'.
1. Rufen Sie 'export_xml()' auf, um alle Formularfeldwerte zu extrahieren und in die XML-Datei zu schreiben.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Export Data to XML
def export_pdf_form_data_to_xml(infile, datafile):
    """Export PDF form data to XML file."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Open XML file as stream
    with FileIO(datafile, "w") as xml_output_stream:
        # Export data from PDF form fields to XML
        pdf_form.export_xml(xml_output_stream)
```
