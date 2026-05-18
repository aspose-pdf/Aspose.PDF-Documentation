---
title: PDF-Dokumente signieren
type: docs
weight: 10
url: /de/python-net/pdf-signing/
description: Erfahren Sie, wie Sie PDF-Dokumente in Python mit PdfFileSignature unter Verwendung von zertifikatsbasierten, benannten und sichtbaren digitalen Signaturen signieren.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF-Dokumente mit digitalen Signaturen in Python signieren
Abstract: Dieser Artikel zeigt, wie man PDF-Dokumente mit Aspose.PDF for Python via .NET unter Verwendung der PdfFileSignature‑Fassade signiert. Er behandelt die Zertifikatskonfiguration, das Signieren mit Grundparametern, das Signieren mit einem PKCS7‑Objekt, das Zuweisen eines Signaturnamens und das Anwenden einer sichtbaren Signaturdarstellung.
---

Aspose.PDF for Python via .NET stellt die [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) Fassade zum Anwenden digitaler Signaturen auf vorhandene PDF-Dokumente. Mit einer Zertifikatsdatei können Sie ein Dokument programmgesteuert signieren, die Signatur auf einer Seite platzieren, Signatur-Metadaten zuweisen und anpassen, wie die Signatur angezeigt wird.

Dieser Artikel demonstriert mehrere gängige Signatur‑Workflows:

1. Erstellen und binden Sie ein `PdfFileSignature` Objekt zur Eingabe-PDF.
1. Konfigurieren Sie das Signaturzertifikat.
1. Wenden Sie eine digitale Signatur auf die Zielseite an.
1. Weisen Sie optional einen Signaturnamen und ein sichtbares Erscheinungsbild zu.
1. Speichern Sie das signierte PDF.

## Wiederverwendbare Signaturhilfsfunktionen vorbereiten

Bevor Sie eine digitale Signatur auf ein PDF anwenden, ist es sinnvoll, eine kleine Gruppe wiederverwendbarer Hilfsfunktionen einzurichten. Diese Helfer initialisieren den Signatur-Handler, definieren den sichtbaren Signaturbereich, konfigurieren das Zertifikat und erstellen wiederverwendbare PKCS#7‑Signaturobjekte, sodass die untenstehenden Signaturbeispiele eigenständig bleiben und leichter nachzuvollziehen sind.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd


DEFAULT_CERTIFICATE_PASSWORD = "Aspose2021"
DEFAULT_SIGNATURE_NAME = "Signature1"


def create_pdf_file_signature(infile):
    pdf_signature = pdf_facades.PdfFileSignature()
    pdf_signature.bind_pdf(infile)
    return pdf_signature


def create_signature_rectangle():
    return apd.Rectangle(10, 10, 200, 60)


def configure_signature_certificate(
    pdf_signature, certificate_path, certificate_password=DEFAULT_CERTIFICATE_PASSWORD
):
    pdf_signature.set_certificate(certificate_path, certificate_password)


def create_pkcs7_signature(
    certificate_path, certificate_password=DEFAULT_CERTIFICATE_PASSWORD
):
    signature = ap.forms.PKCS7(certificate_path, certificate_password)
    signature.reason = "Document approval"
    signature.contact_info = "qa@example.com"
    signature.location = "New York, USA"
    signature.authority = "Aspose.PDF Example"
    return signature


def create_custom_signature_appearance():
    appearance = ap.forms.SignatureCustomAppearance()
    appearance.font_family_name = "Arial"
    appearance.font_size = 10
    appearance.show_contact_info = True
    appearance.show_location = True
    appearance.show_reason = True
    return appearance
```

## Signieren Sie ein PDF mit grundlegenden Zertifikatsparametern

Dieser Ansatz konfiguriert das Zertifikat direkt auf dem `PdfFileSignature` Objekt. Es ist nützlich, wenn Sie einen unkomplizierten Signaturablauf mit Standard‑Signatur‑Metadaten und keiner separaten Signaturobjektverwaltung wünschen.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def sign_pdf_with_basic_parameters(infile, outfile, certificate_path):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        configure_signature_certificate(pdf_signature, certificate_path)
        pdf_signature.sign(
            1,
            "Document approval",
            "qa@example.com",
            "New York, USA",
            False,
            create_signature_rectangle(),
        )
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```

## Ein PDF mit einem PKCS7-Objekt signieren

Verwenden Sie ein `PKCS7` Objekt, wenn Sie die Signatur zuerst vorbereiten und dann in den Signaturaufruf übergeben müssen. Dieses Muster gibt Ihnen mehr Kontrolle über die Signatur‑Einstellungen und bildet eine gute Grundlage für fortgeschrittene Workflows.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def sign_pdf_with_certificate_object(infile, outfile, certificate_path):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        signature = create_pkcs7_signature(certificate_path)
        pdf_signature.sign(1, False, create_signature_rectangle(), signature)
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```

## Signieren Sie ein PDF mit einer benannten Signatur

Wenn Ihr Dokumenten-Workflow auf einem vordefinierten Signaturfeldnamen beruht, übergeben Sie diesen Namen an `sign()`. Dies erleichtert das spätere Nachschlagen der Signatur für Validierung, Verarbeitung oder Integration in einen Genehmigungs‑Workflow.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def sign_pdf_with_named_signature(infile, outfile, certificate_path):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        signature = create_pkcs7_signature(certificate_path)
        signature.reason = "Approved by signing workflow"
        pdf_signature.sign(
            1,
            DEFAULT_SIGNATURE_NAME,
            "Approved by signing workflow",
            "qa@example.com",
            "New York, USA",
            True,
            create_signature_rectangle(),
            signature,
        )
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```

## Sichtbare Signatur anwenden

Sie können die Signatur auf der PDF-Seite sichtbar machen, indem Sie ihr ein benutzerdefiniertes Aussehen zuweisen. `PKCS7` object. Dies ist nützlich, wenn das Ausgabedokument Genehmigungsdetails wie den Grund, den Standort und die Kontaktinformationen für Endbenutzer anzeigen soll.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def apply_visible_signature(infile, outfile, certificate_path):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        signature = create_pkcs7_signature(certificate_path)
        signature.reason = "Visible approval signature"
        signature.custom_appearance = create_custom_signature_appearance()
        pdf_signature.sign(
            1,
            "Visible approval signature",
            "qa@example.com",
            "New York, USA",
            True,
            create_signature_rectangle(),
            signature,
        )
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```
