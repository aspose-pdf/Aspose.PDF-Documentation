---
title: Signaturinformationen
type: docs
weight: 60
url: /de/python-net/signature-information/
description: Erfahren Sie, wie Sie Signaturnamen, Unterzeichnerdetails, Zeitstempel und Signaturmetadaten aus signierten PDF-Dateien mithilfe von PdfFileSignature in Python lesen können.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Signaturdetails aus PDF-Dokumenten in Python lesen
Abstract: Dieser Artikel erklärt, wie man Signaturmetadaten in signierten PDF-Dokumenten mit Aspose.PDF for Python via .NET untersucht. Er zeigt, wie man Signaturnamen auflistet, Unterzeichnerdetails liest, das Signaturdatum und die -zeit ermittelt und den Grund sowie den Ort der Signatur extrahiert.
---

Aspose.PDF for Python via .NET stellt die [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) Fassade zum Inspizieren digitaler Signaturen in PDF-Dokumenten. Nachdem ein Dokument signiert wurde, können Sie sie verwenden, um die Signaturnamen zu lesen und Metadaten wie den Namen des Unterzeichners, Kontaktinformationen, Signaturzeit, Grund und Ort abzurufen.

Dieses Beispiel demonstriert vier gängige Aufgaben zur Signaturinformationen:

1. Alle Signaturnamen in einem signierten PDF auflisten.
1. Unterzeichnerdetails für eine ausgewählte Signatur lesen.
1. Ermitteln Sie das Signaturdatum und die Uhrzeit.
1. Lesen Sie den Grund und den Ort der Signatur.

## Signaturnamen abrufen

Verwenden Sie diese Methode, wenn ein PDF ein oder mehrere Signaturen enthalten kann und Sie prüfen möchten, welche Signatur‑Einträge verfügbar sind. Das Beispiel öffnet das Dokument und gibt die zurückgegebene Liste aus. `get_sign_names()`.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_signature_names(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        signature_names = list_signature_names(pdf_signature)
        print(f"Signature Names: {signature_names}")
    finally:
        pdf_signature.close()
```

## Signer-Details abrufen

Sobald Sie den Signaturnamen kennen, können Sie signaturbezogene Metadaten abrufen. Dieses Beispiel liest den Signaturnamen und die Kontaktinformationen für die erste verfügbare Signatur im Dokument.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_signer_details(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signer_name = pdf_signature.get_signer_name(sign_name)
        contact_info = pdf_signature.get_contact_info(sign_name)
        print(
            f"Signer Details for '{sign_name}': "
            f"signer_name={signer_name}, contact_info={contact_info}"
        )
    finally:
        pdf_signature.close()
```

## Signaturdatum und -zeit abrufen

Verwenden `get_date_time()` um zu bestimmen, wann eine bestimmte Signatur angewendet wurde. Dies ist nützlich für Audits und zur Anzeige der Signaturhistorie in Dokumenten-Workflows.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_signature_date_and_time(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signature_date = pdf_signature.get_date_time(sign_name)
        print(f"Signature Date and Time for '{sign_name}': {signature_date}")
    finally:
        pdf_signature.close()
```

## Signaturgrund und -ort abrufen

Digitale Signaturen können auch beschreibende Metadaten wie den Signaturgrund und den Ort speichern. Dieses Beispiel ruft beide Werte für die ausgewählte Signatur ab und gibt sie zusammen aus.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_signature_reason_and_location(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signature_reason = pdf_signature.get_reason(sign_name)
        signature_location = pdf_signature.get_location(sign_name)
        print(
            f"Signature Reason and Location for '{sign_name}': "
            f"reason={signature_reason}, location={signature_location}"
        )
    finally:
        pdf_signature.close()
```

