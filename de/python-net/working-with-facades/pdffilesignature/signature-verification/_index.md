---
title: Signaturprüfung
type: docs
weight: 90
url: /de/python-net/signature-verification/
description: Erfahren Sie, wie Sie digitale Signaturen überprüfen und prüfen, ob ein PDF Signaturen enthält, indem Sie PdfFileSignature in Python verwenden.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF-Signaturen in Python überprüfen
Abstract: Dieser Artikel erklärt, wie digitale Signaturen in PDF-Dokumenten mit Aspose.PDF for Python via .NET überprüft werden. Er zeigt, wie eine vorhandene Signatur validiert wird und wie geprüft wird, ob ein PDF irgendwelche Signaturen enthält.
---

Aspose.PDF for Python via .NET stellt die [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) Facade zur Validierung signierter PDF-Dokumente. Nachdem ein PDF signiert wurde, können Sie es verwenden, um zu bestätigen, dass eine Signatur gültig ist, und um festzustellen, ob das Dokument Signatur‑Einträge enthält.

Dieses Beispiel demonstriert zwei gängige Verifizierungsaufgaben:

1. Überprüfen Sie, ob eine vorhandene PDF-Signatur gültig ist.
1. Überprüfen Sie, ob ein PDF Signaturen enthält.

## PDF-Signatur überprüfen

Verwenden `verify_signature()` Wenn Sie eine bestimmte Signatur im Dokument validieren müssen. Das Beispiel ermittelt den ersten verfügbaren Signaturnamen und prüft, ob diese Signatur gültig ist.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def verify_pdf_signature(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        is_valid = pdf_signature.verify_signature(sign_name)
        print(f"Signature '{sign_name}' is valid: {is_valid}")
    finally:
        pdf_signature.close()
```

## Prüfen, ob ein PDF Signaturen enthält

Verwenden `contains_signature()` wenn Sie nur wissen müssen, ob das PDF überhaupt Unterschriften enthält. Das ist nützlich als schnelle Überprüfung, bevor Sie detailliertere Verifizierungs- oder Extraktionslogik ausführen.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def check_if_pdf_contains_signatures(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        contains_signatures = pdf_signature.contains_signature()
        print(f"PDF contains signatures: {contains_signatures}")
    finally:
        pdf_signature.close()
```
