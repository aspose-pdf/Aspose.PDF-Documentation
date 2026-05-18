---
title: Felddarstellung abrufen
type: docs
weight: 20
url: /de/python-net/get-field-appearance/
description: Dieser Artikel erklärt, wie man ein PDF öffnet, ein Formularfeld zugreift, dessen Anzeigeeinstellungen abruft und sie anzeigt. Das Beispiel zeigt das Abrufen der Darstellung eines Feldes mit dem Namen "Last Name".
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF-Formularfelddarstellung mit Python abrufen
Abstract: Dieses Beispiel demonstriert, wie man die visuellen Darstellungseigenschaften eines Formularfelds in einem PDF-Dokument mit Aspose.PDF for Python abruft. Der Code öffnet ein vorhandenes PDF, greift auf ein bestimmtes Formularfeld zu und gibt dessen Darstellungsdetails aus, einschließlich Hintergrundfarbe, Textfarbe, Rahmenfarbe und Ausrichtung.
---

Formularfelder in PDF-Dokumenten haben visuelle Eigenschaften wie Hintergrundfarbe, Textfarbe, Rahmenfarbe und Ausrichtung. Mit Aspose.PDF for Python können Entwickler diese Anzeigeeinstellungen programmgesteuert prüfen, indem sie das [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) Klasse.

1. Öffnen Sie ein vorhandenes PDF-Dokument.
1. Erstellen Sie ein FormEditor-Objekt.
1. Rufen Sie die Erscheinungsinformationen eines bestimmten Feldes ab.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_field_appearance(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Get field appearance
    appearance = form_editor.get_field_appearance("Last Name")
    print("Field Appearance: " + str(appearance))
```
