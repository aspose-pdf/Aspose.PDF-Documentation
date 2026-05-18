---
title: Arbeiten mit XFA-Formularen
linktitle: XFA-Formulare
type: docs
weight: 20
url: /de/python-net/xfa-forms/
description: Aspose.PDF for Python via .NET API ermöglicht es Ihnen, mit XFA- und XFA-Acroform-Feldern in einem PDF-Dokument zu arbeiten.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## XFA-zu-Acroform konvertieren

{{% alert color="primary" %}}

Online ausprobieren
Sie können die Qualität der Aspose.PDF-Konvertierung überprüfen und die Ergebnisse online unter diesem Link ansehen: [products.aspose.app/pdf/xfa/acroform](https://products.aspose.app/pdf/xfa/acroform)

{{% /alert %}}

Der folgende Codeabschnitt zeigt, wie man ein dynamisches XFA (XML Forms Architecture)-Formular in ein Standard-AcroForm konvertiert.

**Schlüsselschritte umfassen:**

1. Laden des Eingabe-PDF-Dokuments.
1. Formtyp wird auf STANDARD geändert.
1. Speichern der konvertierten PDF in einer neuen Datei.

Diese Konvertierung ermöglicht bessere Kompatibilität und ein konsistentes Formularhandling über verschiedene PDF-Reader und Anwendungen hinweg.

```python
import aspose.pdf as ap
import sys
from os import path

def convert_dynamic_xfa_to_acroform(infile: str, outfile: str):
    """Convert dynamic XFA form to standard AcroForm."""
    with ap.Document(infile) as document:
        document.form.type = ap.forms.FormType.STANDARD
        document.save(outfile)
```

## Verwendung von IgnoreNeedsRendering

Dieses Beispiel demonstriert, wie ein dynamisches XFA-Formular in ein Standard‑AcroForm konvertiert wird, wobei Aspose.PDF für Python verwendet wird. Der Code prüft, ob das Eingabe‑PDF ein XFA‑Formular enthält, und überschreibt die Darstellung, falls erforderlich. Anschließend wird der Formulartyp auf STANDARD gesetzt und das aktualisierte PDF gespeichert.

```python
import aspose.pdf as ap
import sys
from os import path

def convert_xfa_form_with_ignore_needs_rendering(infile: str, outfile: str):
    """Convert XFA form ignoring needs rendering flag."""
    with ap.Document(infile) as document:
        if not document.form.needs_rendering and document.form.has_xfa:
            document.form.ignore_needs_rendering = True
        document.form.type = ap.forms.FormType.STANDARD
        document.save(outfile)
```
