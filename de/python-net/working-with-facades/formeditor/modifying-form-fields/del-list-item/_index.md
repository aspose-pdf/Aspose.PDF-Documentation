---
title: Listenelement löschen
type: docs
weight: 40
url: /de/python-net/del-list-item/
description:
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Entfernen von Elementen aus PDF-Listbox-Feldern mit Python
Abstract: Dieses Beispiel zeigt, wie man ein Element aus einem Listbox-Formularfeld in einem PDF‑Dokument mit Aspose.PDF für Python entfernt. Der Code öffnet ein vorhandenes PDF, löscht ein bestimmtes Element aus einem Listbox‑Feld und speichert das aktualisierte Dokument.
---

Listbox‑Felder in PDFs ermöglichen es Benutzern, eine oder mehrere vordefinierte Optionen auszuwählen. Mit Aspose.PDF für Python können Entwickler programmgesteuert Elemente aus diesen Feldern entfernen.

Dieser Artikel erklärt, wie man das Element ‘UK’ aus einem Listbox‑Feld mit dem Namen ‘Country’ löscht, sodass das Feld nur die gewünschten Optionen enthält.

Der [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) Die Klasse bietet die Methode ‘del_list_item’, um ein bestimmtes Element aus einem Listbox‑Feld zu entfernen.

1. Öffnen Sie ein vorhandenes PDF-Formular.
1. Erstellen Sie ein FormEditor-Objekt.
1. Binden Sie das PDF-Dokument an den FormEditor.
1. Löschen Sie das "UK"-Element aus dem "Country"-Listbox-Feld.
1. Speichern Sie das aktualisierte Dokument.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def del_list_item(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Delete list item from list box field
    form_editor.del_list_item("Country", "UK")
    # Save updated document
    form_editor.save(outfile)
```

