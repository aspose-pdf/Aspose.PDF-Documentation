---
title: Signaturextraktion
type: docs
weight: 50
url: /de/python-net/signature-extraction/
description: Erfahren Sie, wie Sie ein Signaturbild und das Signaturzertifikat aus einem signierten PDF mithilfe von PdfFileSignature in Python extrahieren.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Signaturbild und Zertifikat aus PDF in Python extrahieren
Abstract: Dieser Artikel erklärt, wie man signaturbezogene Daten aus signierten PDF-Dokumenten mit Aspose.PDF for Python via .NET extrahiert. Er zeigt, wie man die erste verfügbare Signatur liest, ihr Bild exportiert und den zugehörigen Zertifikat-Stream in eine Ausgabedatei speichert.
---

Aspose.PDF for Python via .NET stellt die [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) Fassade zum Inspektieren und Extrahieren von Daten aus signierten PDF-Dokumenten. Nachdem ein PDF signiert wurde, können Sie es verwenden, um Signaturressourcen wie das visuelle Signaturbild und das mit der Signatur verbundene Zertifikat zu exportieren.

Dieses Beispiel demonstriert zwei gängige Extraktionsaufgaben:

1. Extrahieren Sie das visuelle Bild, das mit einer Signatur verknüpft ist.
1. Extrahieren Sie das Signaturzertifikat aus einem signierten PDF.

## Extrahieren Sie ein Signaturbild

Verwenden Sie diese Methode, wenn das PDF eine sichtbare Signatur enthält und Sie deren Bilddaten exportieren möchten. Das Beispiel öffnet das signierte Dokument, holt den zuerst verfügbaren Signaturnamen, extrahiert den Bild-Stream und schreibt ihn in eine Datei.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def extract_signature_image(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signature_image = pdf_signature.extract_image(sign_name)
        write_stream_data(signature_image, outfile)
    finally:
        pdf_signature.close()
```

## Ein Signaturzertifikat extrahieren

Verwenden `extract_certificate()` wenn Sie die Zertifikatsdaten benötigen, die an einer Signatur angehängt sind. Dies ist nützlich für Inspektion, Validierungs-Workflows oder das separate Speichern des Unterzeichnerzertifikats vom PDF-Dokument.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def extract_signature_certificate(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signature_certificate = pdf_signature.extract_certificate(sign_name)
        write_stream_data(signature_certificate, outfile)
    finally:
        pdf_signature.close()
```

