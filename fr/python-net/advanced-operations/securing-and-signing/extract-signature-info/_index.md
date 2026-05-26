---
title: Extraire les informations de signature du PDF en Python
linktitle: Extraire les détails de la signature
type: docs
weight: 20
url: /fr/python-net/extract-image-and-signature-information/
description: Apprenez comment extraire les images de signature, les certificats et les détails de signature numérique des fichiers PDF avec Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extrayez les images de signature et les détails des certificats des PDF avec Python
Abstract: Cet article explique comment extraire les informations d'image et de signature numérique des documents PDF à l'aide d'Aspose.PDF for Python. Apprenez comment récupérer les images de signature, extraire les données du certificat, inspecter les algorithmes de signature et détecter les signatures compromises dans les fichiers PDF signés.
---

## Extraire l'image d'un champ de signature

Aspose.PDF for Python via .NET vous permet de récupérer l'image visuelle intégrée dans un [SignatureField](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/). Ceci est utile lorsque vous devez afficher ou archiver l'apparence de la signature sans rendre le PDF complet.

L'exemple ci-dessous parcourt tous les champs de formulaire, et trouve chacun d'eux. `SignatureField`, et enregistre son image sous forme de fichier JPEG:

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

## Lire les détails de l'algorithme de signature

Utiliser `PdfFileSignature.get_signatures_info()` lire les métadonnées cryptographiques pour chaque signature d'un document — y compris l'algorithme de hachage, le type d'algorithme, la norme cryptographique et le nom de la signature :

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

## Extraire un certificat numérique d'un champ de signature

Utilisez le [extract_certificate()](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/#methods) méthode sur un `SignatureField` pour récupérer le certificat intégré sous forme de flux d'octets et l'enregistrer sur le disque pour une validation externe :

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

## Extraire les certificats en utilisant la façade PdfFileSignature

`PdfFileSignature.try_extract_certificate()` fournit une méthode alternative pour récupérer les certificats par nom de signature. L'exemple suivant parcourt tous les noms de signature et tente l'extraction pour chacun :

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

## Vérifier les signatures numériques externes

Pour confirmer qu'un document n'a pas été modifié après la signature, vérifiez chaque signature externe en utilisant `PdfFileSignature.verify_signature()`. L'exemple ci-dessous lève une exception pour toute signature qui échoue à la vérification :

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

## Détecter les signatures compromises

`SignaturesCompromiseDetector` vérifie si des signatures numériques dans un document ont été invalidées par des modifications ultérieures. Utilisez ceci dans les flux de travail juridiques, financiers ou de conformité où l’intégrité du document doit être garantie.

L'exemple ci-dessous vérifie les signatures compromises et rapporte leurs noms ainsi que la couverture globale des signatures du document :

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

## Sujets de sécurité associés

- [Sécurisez et signez les fichiers PDF en Python](/pdf/fr/python-net/securing-and-signing/)
- [Signer numériquement des fichiers PDF en Python](/pdf/fr/python-net/digitally-sign-pdf-file/)
- [Signer des documents PDF à partir d'une carte à puce en Python](/pdf/fr/python-net/sign-pdf-document-from-smart-card/)
- [Chiffrer et déchiffrer des fichiers PDF en Python](/pdf/fr/python-net/set-privileges-encrypt-and-decrypt-pdf-file/)
