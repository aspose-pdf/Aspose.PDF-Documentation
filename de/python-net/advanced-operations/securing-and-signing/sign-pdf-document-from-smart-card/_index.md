---
title: PDF-Dokumente von einer Smart Card in Python signieren
linktitle: PDF-Signatur mit Smart Card
type: docs
weight: 30
url: /de/python-net/sign-pdf-document-from-smart-card/
description: Erfahren Sie, wie Sie PDF-Dokumente mit Smart Cards und externen Zertifikaten in Python signieren.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF-Dokumente von einer Smart Card mit Python signieren
Abstract: Dieser Leitfaden erklärt, wie man PDF‑Dokumente mit einer Smartcard mithilfe von Aspose.PDF for Python via .NET digital signiert. Er demonstriert, wie man über den Windows‑Zertifikatspeicher auf in Hardwaregeräten (wie USB‑Token oder Smartcards) gespeicherte Zertifikate zugreift und sie zum Signieren von PDF‑Dateien verwendet. Die Dokumentation beinhaltet Codebeispiele, die zeigen, wie das passende Zertifikat gefunden, Signatureigenschaften konfiguriert und die digitale Signatur in das PDF eingebettet wird. Das ermöglicht sichere, hardwaregestützte Signaturen in Übereinstimmung mit Standards für digitale Signaturen, geeignet für hochtrustige Unternehmens‑ und Rechtsabläufe.
---

Aspose.PDF bietet robuste Funktionen zur Integration visueller und kryptografischer Signaturkomponenten und gewährleistet sowohl Authentizität als auch eine professionelle Darstellung in digital signierten PDF-Dokumenten.

Verwenden Sie diesen Workflow, wenn Ihr Signaturprozess von Zertifikaten abhängt, die in hardwaregestützten Geräten wie Smartcards, USB-Token oder verwalteten Zertifikatspeichern gespeichert sind.

## Signieren mit Smart Card über Signaturfeld

Dieses Beispiel zeigt, wie man ein PDF-Dokument mithilfe eines externen Zertifikats mit Aspose.PDF for Python digital signiert und ein benutzerdefiniertes Signatur‑Design‑Bild anwendet:

1. Öffnen des PDF-Dokuments.
1. Erstellen eines PdfFileSignature-Objekts und Binden an das Dokument.
1. Abrufen eines lokalen digitalen Zertifikats mit einer benutzerdefinierten Methode `get_local_certificate()`.
1. Einrichten einer ExternalSignature basierend auf dem ausgewählten Zertifikat.
1. Anwenden eines benutzerdefinierten Signatur‑Anzeige‑Bildes (z. B. ein Firmenlogo oder eine handschriftliche Signatur).
1. Digitales Signieren der ersten Seite des Dokuments mit angegebenen Metadaten (Grund, Kontakt, Ort).
1. Speichern des signierten Dokuments in einer neuen Ausgabedatei.

Diese Methode ist ideal für Fälle, in denen Signaturen programmgesteuert mit externen Zertifikaten angewendet werden müssen – zum Beispiel Hardware‑Token, Zertifikatspeicher oder vertrauenswürdige Anbieter – und mit einem personalisierten visuellen Layout präsentiert werden.

Nachfolgend sind die Code‑Snippets zum Signieren eines PDF‑Dokuments von einer Smartcard:

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def sign_with_smart_card(infile: str, outfile: str, pngfile: str) -> None:
    """Sign a PDF document using a smart-card certificate."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature() as pdf_signature:
            pdf_signature.bind_pdf(document)
            external_signature = ap.forms.ExternalSignature(get_local_certificate())
            pdf_signature.signature_appearance = pngfile
            pdf_signature.sign(
                1,
                "Reason",
                "Contact",
                "Location",
                True,
                drawing.Rectangle(100, 100, 200, 200),
                external_signature,
            )
            pdf_signature.save(outfile)
```

## Digitale Signaturen überprüfen

Dieses Code‑Snippet demonstriert, wie digitale Signaturen in einem PDF‑Dokument mit Aspose.PDF for Python überprüft werden:

1. Öffnen der PDF-Datei.
1. Erstellen eines 'PdfFileSignature-Objekts' und Bindung an das Dokument.
1. Abrufen der Liste aller Signaturfeldnamen mit 'get_signature_names()'.
1. Durchlaufen jeder Signatur und Überprüfen ihrer Gültigkeit mit 'verify_signature()'.
1. Eine Ausnahme auslösen, wenn irgendeine Signatur die Verifizierung nicht besteht.

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

## Mit externem Zertifikat signieren

Dieses Code‑Snippet demonstriert, wie man ein digitales Signaturfeld zu einem PDF‑Dokument hinzufügt und signiert, wobei Aspose.PDF for Python mit einem externen Zertifikat verwendet wird:

1. Öffnen der PDF‑Datei als Binär‑Stream.
1. Erstellen eines SignatureField und dessen Platzierung auf der ersten Seite des Dokuments an einer angegebenen Position.
1. Abrufen eines lokalen digitalen Zertifikats mit einer benutzerdefinierten Methode `get_local_certificate()`.
1. Einrichten einer ExternalSignature mit Metadaten wie Autorität, Grund und Kontaktinformationen.
1. Zuweisen eines eindeutigen Feldnamens zum Signaturfeld (partial_name = "sig1").
1. Hinzufügen des Signaturfelds zu den Formularfeldern des PDFs.
1. Signieren des Feldes mit dem externen Zertifikat.
1. Speichern des signierten Dokuments in einer Ausgabedatei.

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def get_signature_info_using_signature_field(infile: str, outfile: str) -> None:
    """Create a signature field and sign it with an external certificate."""
    with open(infile, "rb+") as file_stream:
        document = ap.Document(file_stream)
        signature_field = ap.forms.SignatureField(
            document.pages[1],
            ap.Rectangle(100, 400, 10, 10, True),
        )
        selected_certificate = get_local_certificate()
        external_signature = ap.forms.ExternalSignature(selected_certificate)
        external_signature.authority = "Me"
        external_signature.reason = "Reason"
        external_signature.contact_info = "Contact"
        signature_field.partial_name = "sig1"
        document.form.add(signature_field, 1)
        signature_field.sign(external_signature)
        document.save(outfile)
```

## Verwandte Sicherheitsthemen

- [PDF-Dateien in Python sichern und signieren](/pdf/de/python-net/securing-and-signing/)
- [PDF-Dateien in Python digital signieren](/pdf/de/python-net/digitally-sign-pdf-file/)
- [Extrahiere Signaturinformationen aus PDF in Python](/pdf/de/python-net/extract-image-and-signature-information/)
- [PDF-Dateien in Python verschlüsseln und entschlüsseln](/pdf/de/python-net/set-privileges-encrypt-and-decrypt-pdf-file/)

