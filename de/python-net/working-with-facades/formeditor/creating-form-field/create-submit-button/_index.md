---
title: Submit-Schaltfläche erstellen
type: docs
weight: 50
url: /de/python-net/create-submit-button/
description: Erfahren Sie, wie Sie programmgesteuert mit Aspose.PDF für Python eine Submit-Schaltfläche zu einem PDF-Dokument hinzufügen. Dieses Tutorial demonstriert, wie man eine Schaltfläche erstellt, die Formulardaten an eine angegebene URL sendet und das aktualisierte PDF speichert.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Erstellen Sie eine Submit-Schaltfläche in einem PDF mit Aspose.PDF für Python
Abstract: Submit-Schaltflächen in PDF-Formularen ermöglichen es Benutzern, Formulardaten direkt an einen Server oder Endpunkt zu senden. In diesem Leitfaden lernen Sie, wie Sie ein Submit-Schaltflächenfeld zu einem PDF mithilfe der FormEditor‑Klasse in Aspose.PDF für Python hinzufügen. Das Beispiel zeigt, wie man den Namen, die Beschriftung, die Ziel‑URL und die Position der Schaltfläche konfiguriert und anschließend das aktualisierte PDF-Dokument speichert.
---

Interaktive PDF-Formulare erfordern häufig, dass Benutzer ihre Eingaben zur Verarbeitung übermitteln, z. B. das Senden von Umfrageergebnissen, Antragsformularen oder Feedback‑Daten. Ein Submit‑Schaltflächenfeld bietet diese Funktionalität, indem es die Schaltfläche mit einem Web‑Endpunkt verknüpft.

Der [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) class ermöglicht das Hinzufügen von Schaltflächen, Kontrollkästchen, Optionsschaltern, Textfeldern und anderen Formularsteuerelementen.

1. Laden Sie ein vorhandenes PDF-Dokument.
1. Füge ein Submit-Button-Feld zu einer bestimmten Seite hinzu.
1. Setze die Beschriftung des Buttons und die Ziel-URL für die Übermittlung.
1. Speichere das aktualisierte PDF mit dem neuen Button.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_submit_button(infile, outfile):
    """Create Submit Button in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add Submit Button to PDF form
    pdf_form_editor.add_submit_btn(
        "submitbtn1",
        1,
        "Submit Button",
        "http://example.com/submit",
        100,
        450,
        200,
        470,
    )

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```
