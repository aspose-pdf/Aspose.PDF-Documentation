---
title: Inneres Feld kopieren
type: docs
weight: 20
url: /de/python-net/copy-inner-field/
description: PDF-Formularfelder mit Python unter Verwendung von Aspose.PDF für Python an eine neue Position kopieren.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF-Formularfelder mit Python an eine neue Position kopieren.
Abstract: Dieses Beispiel zeigt, wie ein vorhandenes Formularfeld mit Aspose.PDF für Python an eine neue Position in einem PDF-Dokument kopiert wird. Der Code öffnet ein PDF, dupliziert ein Feld zu einer angegebenen Seite und Koordinaten und speichert das aktualisierte Dokument.
---

PDF-Formulare erfordern häufig das Duplizieren von Feldern, wobei das ursprüngliche Format und Verhalten beibehalten werden. Mit Aspose.PDF for Python können Entwickler ein vorhandenes Feld programmgesteuert an eine neue Position auf derselben oder einer anderen Seite kopieren.

Dieser Artikel erklärt, wie man ein Feld mit dem Namen ‘First Name’ in ein neues Feld namens ‘First Name Copy’ auf Seite 2 an spezifischen Koordinaten (x=200, y=600) kopiert, wodurch ein PDF mit dem neu positionierten Feld entsteht.

1. Öffnen Sie ein vorhandenes PDF-Formular.
1. Erstellen Sie ein FormEditor-Objekt.
1. Binden Sie das PDF-Dokument an den FormEditor.
1. Kopieren Sie das Feld ‘First Name’ in ein neues Feld ‘First Name Copy’ auf Seite 2 bei den Koordinaten (200, 600).
1. Speichern Sie das aktualisierte Dokument.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def copy_inner_field(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Copies an existing field to a new position specified by both page number and ordinates.
    # A new document will be produced, which contains everything the source document has except for the newly copied field.
    form_editor.copy_inner_field("First Name", "First Name Copy", 2, 200, 600)
    # Save updated document
    form_editor.save(outfile)
```

**Bitte beachten Sie:**

Die 'copy_inner_field'-Methodensignatur sieht folgendermaßen aus:

```python
copy_inner_field(original_field_name, new_field_name, page_number, x, y)
```

- 'original_field_name' – das Feld, das Sie duplizieren möchten.
- 'new_field_name' – der Name des neuen Feldes.
- 'page_number' – die Seite, auf der das neue Feld erscheinen wird.
- x, y – Koordinaten auf dieser Seite.

Der page_number wird erwartet, eine positive ganze Zahl zu sein, die einer existierenden Seite im PDF entspricht (1-basierte Indizierung).

Wenn Sie einen negativen Parameter übergeben, z. B.:

```python
form_editor.copy_inner_field("First Name", "First Name Copy", -1, 200, 600)
```

Das Programm setzt dann die vorherigen Parameter zurück.
