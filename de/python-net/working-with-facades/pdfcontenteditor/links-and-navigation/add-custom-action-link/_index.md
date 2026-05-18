---
title: Benutzerdefinierten Aktionslink hinzufügen
type: docs
weight: 20
url: /de/python-net/add-custom-action-link/
description: Dieses Beispiel bindet ein Eingabe‑PDF, fügt auf der ersten Seite einen benutzerdefinierten Aktionslink hinzu und speichert das modifizierte Dokument. Für die Einfachheit wird eine leere Aktionsliste verwendet, aber echte Implementierungen können tatsächliche Aktionen enthalten.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Einen benutzerdefinierten Aktionslink zu einem PDF mit PdfContentEditor in Python hinzufügen
Abstract: Dieses Beispiel zeigt, wie man mit Aspose.PDF for Python via the Facades API einen benutzerdefinierten Aktionslink zu einem PDF‑Dokument hinzufügt. Es zeigt, wie man einen anklickbaren Bereich auf einer Seite erstellt, eine benutzerdefinierte Aktion zuweist und das aktualisierte Dokument speichert.
---

Benutzerdefinierte Aktionslinks ermöglichen es Ihnen, interaktive Bereiche in einem PDF zu definieren, die beim Anklicken bestimmte Aktionen auslösen können, wie das Ausführen von Skripten, das Navigieren zu Seiten oder das Ausführen anwendungsspezifischer Befehle. Using [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), können Sie einen benutzerdefinierten Aktionslink erstellen, indem Sie Seite, Rechteck, Farbe und Aktionen angeben.

1. Erstellen Sie eine PdfContentEditor-Instanz.
1. Binden Sie das Eingabe-PDF-Dokument.
1. Definieren Sie ein Rechteck für den anklickbaren Link.
1. Geben Sie die Seitenzahl und die Linkfarbe an.
1. Weisen Sie benutzerdefinierte Aktionen zu (im Beispiel leer).
1. Speichern Sie das aktualisierte PDF-Dokument.

```python
import aspose.pdf.facades as pdf_facades
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as apd
import aspose.pdf as ap

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_custom_action_link(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add custom action link. Empty action list keeps the sample runnable
    # without requiring additional enum lookups.
    content_editor.create_custom_action_link(
        apd.Rectangle(200, 500, 260, 20),
        1,
        apd.Color.dark_red,
        [],
    )
    # Save updated document
    content_editor.save(outfile)
```
