---
title: Signaturinformationen aus PDF in Python extrahieren
linktitle: Details aus der Signatur extrahieren
type: docs
weight: 20
url: /de/python-net/extract-image-and-signature-information/
description: Erfahren Sie, wie Sie Signaturbilder, Zertifikate und Details digitaler Signaturen aus PDF-Dateien in Python extrahieren.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extrahieren Sie Signaturbilder und Zertifikatdetails aus PDFs in Python
Abstract: In diesem Artikel wird erklärt, wie man Bild- und digitale Signaturinformationen aus PDF-Dokumenten mit Aspose.PDF for Python extrahiert. Erfahren Sie, wie Sie Signaturbilder abrufen, Zertifikatsdaten extrahieren, Signaturalgorithmen untersuchen und kompromittierte Signaturen in signierten PDF-Dateien erkennen.
---

## Bild aus einem Signaturfeld extrahieren

Aspose.PDF for Python via .NET ermöglicht das Abrufen des eingebetteten visuellen Bildes in einem [Signaturfeld](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/). Dies ist nützlich, wenn Sie die Signaturdarstellung anzeigen oder archivieren müssen, ohne das gesamte PDF zu rendern.

Das folgende Beispiel iteriert über alle Formularfelder und findet jedes `SignatureField`, und speichert sein Bild als JPEG-Datei:

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def extract_images_from_signature_field(infile: str, outfile: str) -> None:
    """Extract the image stored in a signature field."""
    with ap.Document(infile) as document:
        for field in document.form:
            if not isinstance(field, ap.forms.SignatureField):
                continue

            image_stream = field.extract_image()
            if image_stream is None:
                continue

            image = drawing.Bitmap.from_stream(image_stream)
            image.save(outfile, drawing.imaging.ImageFormat.jpeg)
```

## Signatur-Algorithmusdetails lesen

Verwenden `PdfFileSignature.get_signatures_info()` um kryptografische Metadaten für jede Signatur in einem Dokument zu lesen — einschließlich des Digest-Algorithmus, des Algorithmustyps, des kryptografischen Standards und des Signaturnamens:

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def get_signatures_info(infile: str) -> None:
    """Print information about all signatures in a PDF document."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            for signature_info in signature.get_signatures_info():
                print(signature_info.DIGEST_HASH_ALGORITHM)
                print(signature_info.ALGORITHM_TYPE)
                print(signature_info.CRYPTOGRAPHIC_STANDARD)
                print(signature_info.signature_name)
```

## Ein digitales Zertifikat aus einem Signaturfeld extrahieren

Verwenden Sie die [extract_certificate](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/#methods) Methode auf ein `SignatureField` um das eingebettete Zertifikat als Bytestrom abzurufen und auf die Festplatte zu speichern, um es extern zu validieren:

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def extract_certificate(infile: str, outfile: str) -> None:
    """Extract a certificate from a signature field and save it to disk."""
    with ap.Document(infile, password="owner") as document:
        for field in document.form:
            if not isinstance(field, ap.forms.SignatureField):
                continue

            certificate_stream = field.extract_certificate()
            if certificate_stream is None:
                continue

            with certificate_stream:
                bytes_data = bytearray(certificate_stream.length)
                certificate_stream.read(bytes_data, 0, len(bytes_data))
                with open(outfile, "wb") as file_stream:
                    file_stream.write(bytes_data)
                return
```

## Zertifikate extrahieren mit der PdfFileSignature-Fassade

`PdfFileSignature.try_extract_certificate()` bietet eine alternative Methode zum Abrufen von Zertifikaten nach Signaturname. Das folgende Beispiel iteriert über alle Signaturnamen und versucht für jeden die Extraktion:

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def extract_certificate_try_extract_certificate_method(infile: str) -> None:
    """Extract certificates with the try_extract_certificate facade method."""
    with ap.Document(infile, password="owner") as document:
        with ap.facades.PdfFileSignature(document) as signature:
            for signature_name in signature.get_signature_names(True):
                certificate = []
                if signature.try_extract_certificate(signature_name, certificate):
                    print("The certificate extraction succeeded")
```

## Externe digitale Signaturen überprüfen

Um zu bestätigen, dass ein Dokument nach der Signatur nicht geändert wurde, prüfen Sie jede externe Signatur mit `PdfFileSignature.verify_signature()`. Das Beispiel unten wirft eine Ausnahme für jede Signatur, die die Verifizierung nicht besteht:

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def verify_external_signature(infile: str) -> None:
    """Verify an external signature in a PDF document."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as pdf_signature:
            for signature_name in pdf_signature.get_signature_names(True):
                if not pdf_signature.verify_signature(signature_name):
                    raise Exception("Not verified")
```

## Kompromittierte Signaturen erkennen

`SignaturesCompromiseDetector` prüft, ob digitale Signaturen in einem Dokument durch nachfolgende Änderungen ungültig geworden sind. Verwenden Sie dies in rechtlichen, finanziellen oder Compliance-Workflows, bei denen die Integrität des Dokuments gewährleistet sein muss.

Das nachstehende Beispiel prüft auf kompromittierte Signaturen und gibt deren Namen zusammen mit der gesamten Signaturabdeckung des Dokuments aus:

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def check(infile: str) -> None:
    """Check whether a PDF contains compromised signatures."""
    with ap.Document(infile) as document:
        detector = ap.SignaturesCompromiseDetector(document)
        result = []

        if detector.check(result):
            print("No signature compromise detected")
            return

        if result[0].has_compromised_signatures:
            print(
                f"Count of compromised signatures: {len(result[0].COMPROMISED_SIGNATURES)}"
            )
            for signature_name in result[0].COMPROMISED_SIGNATURES:
                print(f"Signature name: {signature_name.FULL_NAME}")

        print(result[0].signatures_coverage)
```

## Verwandte Sicherheitsthemen

- [PDF-Dateien in Python sichern und signieren](/pdf/de/python-net/securing-and-signing/)
- [PDF-Dateien in Python digital signieren](/pdf/de/python-net/digitally-sign-pdf-file/)
- [PDF-Dokumente mit einer Smartcard in Python signieren](/pdf/de/python-net/sign-pdf-document-from-smart-card/)
- [PDF-Dateien in Python verschlüsseln und entschlüsseln](/pdf/de/python-net/set-privileges-encrypt-and-decrypt-pdf-file/)
