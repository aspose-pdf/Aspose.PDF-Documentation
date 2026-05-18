---
title: Formularfelder umbenennen
type: docs
weight: 30
url: /de/python-net/rename-form-fields/
description: Dieses Beispiel demonstriert, wie Formularfelder in einem PDF‑Dokument mithilfe von Aspose.PDF for Python via .NET umbenannt werden können. Es zeigt, wie ein PDF‑Formular gebunden, vorhandene Feldnamen programmgesteuert aktualisiert und die modifizierte Datei gespeichert wird. Das Umbenennen von Feldern hilft, Formstrukturen zu standardisieren, die Datenzuordnung zu verbessern und die Integration in automatisierte Workflows oder externe Systeme zu vereinfachen.
lastmod: "2026-05-18"
---

Das Umbenennen von Formularfeldern ist nützlich, wenn PDF‑Formulare an interne Namenskonventionen angepasst oder Dokumente für die strukturierte Datenverarbeitung vorbereitet werden sollen. In diesem Beispiel wird das [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) facade aus der [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) Modul wird verwendet, um die Quell‑PDF zu binden und eine Zuordnung anzuwenden, die alte Feldnamen durch neue ersetzt. Nach der Aktualisierung der Feldkennungen wird das Dokument mit den vorgenommenen Änderungen gespeichert.

1. Initialisieren Sie pdf_facades.Form(), um mit PDF‑Formularfeldern zu interagieren.
1. Rufen Sie 'bind_pdf()' auf, um das PDF‑Dokument anzuhängen.
1. Erstellen Sie eine Liste von Tupeln, die alte Feldnamen und deren entsprechende neue Namen enthalten.
1. Iterieren Sie durch die Zuordnung und rufen Sie 'rename_field()' für jeden Eintrag auf.
1. Speichern Sie das aktualisierte Document.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Rename form fields
def rename_form_fields(infile, outfile):
    """Rename form fields in a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Rename form fields by providing a mapping of old names to new names
    field_renaming_map = [("First Name", "NewFirstName"), ("Last Name", "NewLastName")]
    for old_name, new_name in field_renaming_map:
        pdf_form.rename_field(old_name, new_name)

    # Save updated PDF
    pdf_form.save(outfile)
```
