---
title: PDF-Zertifizierung
type: docs
weight: 30
url: /de/python-net/pdf-certification/
description: Erfahren Sie, wie Sie PDF-Dokumente in Python mit PdfFileSignature und DocMDPSignature und unterschiedlichen Berechtigungen für Dokumentenänderungen zertifizieren.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF-Dokumente mit DocMDP-Berechtigungen in Python zertifizieren
Abstract: Dieser Artikel erklärt, wie man PDF-Dokumente mit Aspose.PDF for Python via .NET unter Verwendung des PdfFileSignature-Facade zertifiziert. Er zeigt, wie man eine DocMDPSignature erstellt, eine Zertifizierung mit Berechtigungen zum Ausfüllen von Formularen anwendet und ein Dokument mit einem Zertifizierungsgrad „keine Änderungen“ sperrt.
---

Aspose.PDF for Python via .NET ermöglicht es Ihnen, PDF-Dokumente zu zertifizieren, indem Sie eine dokumentenbezogene Signatur mit [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/). Zertifizierung unterscheidet sich von einer Standard‑Genehmigungsunterschrift, weil sie festlegt, welche Änderungen, falls überhaupt, nach der Zertifizierung des Dokuments zulässig sind.

Dieser Artikel demonstriert zwei gängige Zertifizierungs‑Workflows:

1. Ein PDF zertifizieren und das Ausfüllen von Formularen nach der Zertifizierung zulassen.
1. Ein PDF zertifizieren und weitere Änderungen verhindern.

## Ein PDF für das Ausfüllen von Formularen zertifizieren

Verwenden Sie diesen Ansatz, wenn das Dokument zertifiziert bleiben soll, aber Benutzer dennoch interaktive Formulare ausfüllen oder die Datei weiter signieren müssen. Der `FILLING_IN_FORMS` Berechtigungsstufe erlaubt diese kontrollierten Änderungen, während die Zertifizierung gültig bleibt.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def certify_pdf_with_mdp_signature(infile, outfile, certificate_path):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        doc_mdp_signature = create_doc_mdp_signature(
            certificate_path,
            ap.forms.DocMDPAccessPermissions.FILLING_IN_FORMS,
            reason="Certified for form filling and signing",
        )
        pdf_signature.certify(
            1,
            "Certified for form filling and signing",
            "security@example.com",
            "New York, USA",
            True,
            create_signature_rectangle(),
            doc_mdp_signature,
        )
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```

## Zertifizierung auf Dokumentebene anwenden, ohne Änderungen zu erlauben

Verwenden Sie diesen Modus, wenn das zertifizierte Dokument nach der Zertifizierung unverändert bleiben muss. Der `NO_CHANGES` Die Berechtigungsstufe ist geeignet für fertiggestellte PDFs, bei denen jede nachträgliche Änderung den Zertifizierungsstatus ungültig machen sollte.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def apply_document_level_certification(infile, outfile, certificate_path):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        doc_mdp_signature = create_doc_mdp_signature(
            certificate_path,
            ap.forms.DocMDPAccessPermissions.NO_CHANGES,
            reason="Certified with no further changes allowed",
        )
        pdf_signature.certify(
            1,
            "Certified with no further changes allowed",
            "security@example.com",
            "New York, USA",
            True,
            create_signature_rectangle(),
            doc_mdp_signature,
        )
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```
