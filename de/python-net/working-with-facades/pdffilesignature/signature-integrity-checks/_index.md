---
title: Signatur-Integritätsprüfungen
type: docs
weight: 70
url: /de/python-net/signature-integrity-checks/
description: Erfahren Sie, wie Sie prüfen können, ob eine PDF‑Signatur das gesamte Dokument abdeckt, und die Integrität des signierten Dokuments mithilfe von PdfFileSignature in Python validieren.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Validieren Sie PDF‑Signaturabdeckung und -Integrität in Python
Abstract: Dieser Artikel erklärt, wie die Integrität digitaler Signaturen in signierten PDF‑Dokumenten mit Aspose.PDF for Python via .NET überprüft wird. Er zeigt, wie geprüft werden kann, ob eine Signatur das gesamte Dokument abdeckt, und wie die Integrität des signierten Inhalts validiert wird.
---

Aspose.PDF for Python via .NET stellt die [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) Fassade zur Validierung signierter PDF‑Dokumente. Nachdem eine Datei signiert wurde, können Sie sie verwenden, um zu prüfen, ob die Signatur auf das gesamte Dokument angewendet wird und ob der signierte Inhalt noch gültig ist.

Dieses Beispiel demonstriert zwei gängige Integritätsprüfungen:

1. Prüfen, ob eine Signatur das gesamte Dokument abdeckt.
1. Validieren Sie die Integrität des signierten PDF-Inhalts.

## Prüfen, ob eine Signatur das gesamte Dokument abdeckt

Verwenden `covers_whole_document()` wenn Sie bestätigen müssen, dass die Signatur für das gesamte PDF gilt und nicht nur für einen Teil seines Inhalts. Das Beispiel liest den ersten verfügbaren Signaturnamen und prüft dessen Geltungsbereich.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def check_signature_coverage(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        covers_document = pdf_signature.covers_whole_document(sign_name)
        print(f"Signature '{sign_name}' covers the whole document: {covers_document}")
    finally:
        pdf_signature.close()
```

## Dokumentintegrität prüfen

Verwenden `verify_signed()` um zu bestätigen, dass der signierte Dokumentinhalt nach dem Anbringen der Signatur nicht verändert wurde. Diese Methode hilft zu überprüfen, ob das Dokument für die ausgewählte Signatur weiterhin gültig ist.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def validate_document_integrity(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        is_valid = pdf_signature.verify_signed(sign_name)
        print(f"Document integrity for '{sign_name}' is valid: {is_valid}")
    finally:
        pdf_signature.close()
```

