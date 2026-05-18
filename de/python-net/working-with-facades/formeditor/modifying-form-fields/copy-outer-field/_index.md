---
title: Äußeres Feld kopieren
type: docs
weight: 30
url: /de/python-net/copy-outer-field/
description: Dieses Beispiel zeigt, wie man ein Formularfeld von einem PDF-Dokument in ein anderes kopiert, wobei Aspose.PDF for Python verwendet wird.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF-Formularfelder aus einem anderen Dokument mit Python kopieren
Abstract: Dieser Artikel erklärt, wie man ein neues PDF-Dokument erstellt, das Feld "First Name" aus einer Quell-PDF auf Seite 1 bei den Koordinaten (200, 600) kopiert und das aktualisierte Ziel-Dokument speichert.
---

Manchmal erfordern PDF-Formulare die Wiederverwendung von Feldern von einem Dokument in ein anderes. Mit Aspose.PDF for Python können Entwickler programmatisch Formularfelder von einem Quell-PDF zu einem Ziel-PDF kopieren.

Der [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) Die Klasse bietet die Methode 'copy_outer_field', die ein Feld von einem Quelldokument zu einem Zieldokument auf einer angegebenen Seite und bei angegebenen Koordinaten kopiert.

Der Code erstellt ein neues PDF (Ziel), fügt eine Seite hinzu und kopiert dann ein Feld von einem bestehenden PDF (Quelle) zum Zieldokument bei angegebenen Koordinaten.

1. Erstellen Sie ein neues Ziel-PDF-Dokument.
1. Fügen Sie dem Ziel-PDF mindestens eine Seite hinzu.
1. Speichern Sie das leere Ziel-Dokument.
1. Erstellen Sie ein FormEditor-Objekt und binden Sie es an das Ziel-PDF.
1. Kopieren Sie das Feld 'First Name' aus dem Quell-PDF auf Seite 1 bei (200, 600).
1. Speichern Sie das aktualisierte Ziel-PDF.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def copy_outer_field(infile, outfile):
    # Since copy_outer_field() method needs to copy field from source document to target document, we need to create a new document as target document first.
    doc = ap.Document()
    doc.pages.add()
    doc.save(outfile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(outfile)
    # Copies an existing field to a new position specified by both page number and ordinates.
    # A new document will be produced, which contains everything the source document has except for the newly copied field.
    form_editor.copy_outer_field(infile, "First Name", 1, 200, 600)
    # Save updated document
    form_editor.save(outfile)
```

**Bitte beachten Sie:**

Die Methodensignatur 'copy_outer_field' sieht folgendermaßen aus:

```python
copy_outer_field(original_field_name, new_field_name, page_number, x, y)
```

- 'original_field_name' – das Feld, das Sie duplizieren möchten.
- 'new_field_name' – der Name des neuen Feldes.
- 'page_number' – die Seite, auf der das neue Feld erscheinen wird.
- x, y – Koordinaten auf dieser Seite.

Der page_number wird erwartet, eine positive ganze Zahl zu sein, die einer existierenden Seite im PDF entspricht (1-basierte Indizierung).

Wenn Sie einen negativen Parameter übergeben, z. B.:

```python
form_editor.copy_outer_field("First Name", "First Name Copy", 1, -200, 600)
```

Das Programm setzt dann die vorherigen Parameter zurück.
