---
title: Digitale Signatur hinzufügen oder PDF in Python digital signieren
linktitle: PDF digital signieren
type: docs
weight: 10
url: /de/python-net/digitally-sign-pdf-file/
description: Erfahren Sie, wie Sie PDF‑Dokumente digital signieren, Zeitstempel hinzufügen und Signaturen in Python validieren.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Signieren Sie PDF‑Dateien digital mit Python
Abstract: Dieses Handbuch erklärt, wie PDF-Dokumente mit Aspose.PDF for Python via .NET digital signiert werden. Es beschreibt den Vorgang zum Anwenden von Standard‑ und erweiterten digitalen Signaturen, die Verwendung von Zertifikaten (PFX und PKCS#12) und die Anpassung des Signatur‑Aussehens und -Verhaltens. Die Dokumentation enthält Code‑Beispiele, die zeigen, wie vorhandene PDFs signiert, Zeitstempel hinzugefügt und die Gültigkeit der Signatur überprüft werden. Dadurch können Entwickler die Authentizität, Integrität und Konformität von Dokumenten mit digitalen Signaturstandards in ihren Python‑Anwendungen sicherstellen.
---

## PDF mit digitalen Signaturen signieren

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def sign_document(infile: str, outfile: str, pfxfile: str) -> None:
    """Sign a PDF document with a PKCS#7 certificate."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            pkcs = ap.forms.PKCS7(pfxfile, "12345")
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)
            signature.save(outfile)
```

Eine **PKCS#7 abgetrennte Signatur** fügt einem Dokument eine digitale Signatur hinzu, ohne den Inhalt in den Signaturblock einzubetten.

Verwenden Sie diese Beispiele, wenn Sie zertifikatbasierte Signaturen auf PDF-Dateien anwenden, die Signaturgültigkeit überprüfen oder vertrauenswürdige Zeitstempel zu signierten Dokumenten hinzufügen müssen.

Das nächste Beispiel signiert ein PDF-Dokument mit einer PKCS#7-losgelösten digitalen Signatur und wendet die Signatur auf der ersten Seite in einem angegebenen rechteckigen Bereich an.

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def sign_document_PKCS7_detached(
    infile: str,
    outfile: str,
    pfxfile: str,
    password: str,
) -> None:
    """Sign a PDF document with a detached PKCS#7 certificate."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            pkcs = ap.forms.PKCS7Detached(
                pfxfile,
                password,
                ap.DigestHashAlgorithm.SHA256,
            )
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)
            signature.save(outfile)
```

**Alle digitalen Signaturen in einem PDF-Dokument überprüfen**

1. Erzeugt eine Instanz von PdfFileSignature, die es Ihnen ermöglicht, mit Signaturen in PDF zu interagieren.
1. Eine Liste von Signaturnamen abrufen `get_signature_names(True)`.
1. Überprüft die erste Signatur in der Liste `verify_signature` zur Einhaltung des angegebenen Zertifikats.

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def verify(infile: str) -> None:
    """Verify all digital signatures in a PDF document."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            for signature_name in signature.get_signature_names(True):
                if not signature.verify_signature(signature_name):
                    raise Exception("Not verified")
```

**Eine Signatur mit einer öffentlichen Schlüsselzertifikatsdatei überprüfen**

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def verify_with_public_key_certificate1(certificate: str, infile: str) -> None:
    """Verify a signature with a public key certificate file."""
    with ap.facades.PdfFileSignature(infile) as file_sign:
        signature_names = file_sign.get_signature_names(True)
        with open(certificate, "rb") as file_stream:
            certificate_bytes = file_stream.read()
        print(file_sign.verify_signature(signature_names[0], certificate_bytes))
```

**Überprüfen Sie eine Signatur mit dem aus der Datei extrahierten Zertifikat**

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def verify_with_public_key_certificate_from_signature(infile: str) -> None:
    """Verify a signature with the certificate extracted from the file."""
    with ap.facades.PdfFileSignature(infile) as file_sign:
        signature_names = file_sign.get_signature_names(True)
        certificate = []
        if file_sign.try_extract_certificate(signature_names[0], certificate):
            print(file_sign.verify_signature(signature_names[0], certificate[0]))
        else:
            print(False)
```

**Signaturen mit aktivierter Zertifikatskettenvalidierung überprüfen**

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def verify_signature_with_certificate_check(infile: str) -> None:
    """Verify signatures with certificate-chain validation enabled."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            for signature_name in signature.get_signature_names(True):
                options = ap.security.ValidationOptions()
                options.validation_mode = ap.security.ValidationMode.STRICT
                options.validation_method = ap.security.ValidationMethod.AUTO
                options.check_certificate_chain = True
                options.request_timeout = 20000
                validation_result = []
                verified = signature.verify_signature(
                    signature_name,
                    options,
                    validation_result,
                )
                print(f"Certificate validation result: {validation_result[0].status}")
                print(f"Is verified: {verified}")
```

## Zeitstempel zur digitalen Signatur hinzufügen

### Wie man ein PDF mit Zeitstempel digital signiert

Aspose.PDF for Python unterstützt das digitale Signieren von PDF mit einem Zeitstempeldienst oder Webdienst.

Um diese Anforderung zu erfüllen, die [Zeitstempel-Einstellungen](https://reference.aspose.com/pdf/python-net/aspose.pdf/timestampsettings/) Klasse wurde zum Aspose.PDF-Namespace hinzugefügt. Bitte schauen Sie sich das folgende Code‑Snippet an, das einen Zeitstempel ermittelt und ihn dem PDF-Dokument hinzufügt:

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def sign_with_time_stamp_server(
    infile: str,
    outfile: str,
    pfxfile: str,
    password: str,
) -> None:
    """Sign a PDF document and apply a timestamp from an external server."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            pkcs = ap.forms.PKCS7(pfxfile, password)
            pkcs.timestamp_settings = ap.TimestampSettings(
                "https://freetsa.org/tsr",
                "",
                ap.DigestHashAlgorithm.SHA256,
            )
            rect = drawing.Rectangle(100, 100, 200, 100)
            signature.sign(
                1, "Signature Reason", "Contact", "Location", True, rect, pkcs
            )
            signature.save(outfile)
```

## Signieren von PDF-Dokumenten mit ECDSA

Das Signieren von PDF-Dokumenten mit ECDSA (Elliptic Curve Digital Signature Algorithm) beinhaltet die Verwendung von elliptischer Kurven‑Kryptografie zur Erstellung digitaler Signaturen.

Das obige Code‑Snippet zeigt, wie man eine PKCS#7‑detached digitale Signatur auf ein PDF‑Dokument mit Aspose.PDF für Python anwendet. Durch das Laden des Dokuments, das Konfigurieren des Signatur‑Auftritts und der Sicherheitseinstellungen und das Speichern des Ergebnisses demonstriert dieses Beispiel einen vollständigen, zuverlässigen Workflow zum digitalen Signieren von PDF‑Dateien.

Diese Methode stellt die Authentizität und Integrität des Dokuments sicher, indem sie eine sichere, prüfbare Signatur auf der ersten Seite einbettet. Die Verwendung von SHA-256 als Digest-Algorithmus entspricht modernen kryptografischen Standards, während die Möglichkeit, die Platzierung der Signatur zu steuern, Flexibilität für sichtbare Genehmigungsmarkierungen bietet.

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def sign_ecdsa(infile: str, outfile: str, pfxfile: str, password: str) -> None:
    """Sign a PDF document with an ECDSA signature."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            pkcs = ap.forms.PKCS7Detached(
                pfxfile,
                password,
                ap.DigestHashAlgorithm.SHA256,
            )
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)
            signature.save(outfile)
```

**ECDSA-Signaturen in einem PDF-Dokument überprüfen**

```python
def verify_ecdsa(infile: str) -> None:
    """Verify ECDSA signatures in a PDF document."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            if not signature.contains_signature():
                raise Exception("Not contains signature")

            for signature_name in signature.get_signature_names(True):
                if not signature.verify_signature(signature_name):
                    raise Exception("Not verified")
```

## Verwandte Sicherheitsthemen

- [PDF-Dateien in Python sichern und signieren](/pdf/de/python-net/securing-and-signing/)
- [Extrahiere Bild- und Signaturinformationen in Python](/pdf/de/python-net/extract-image-and-signature-information/)
- [PDF-Dokumente mit einer Smartcard in Python signieren](/pdf/de/python-net/sign-pdf-document-from-smart-card/)
- [PDF-Dateien in Python verschlüsseln und entschlüsseln](/pdf/de/python-net/set-privileges-encrypt-and-decrypt-pdf-file/)