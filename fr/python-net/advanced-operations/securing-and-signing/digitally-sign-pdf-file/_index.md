---
title: Ajouter une signature numérique ou signer numériquement un PDF en Python
linktitle: Signer numériquement le PDF
type: docs
weight: 10
url: /fr/python-net/digitally-sign-pdf-file/
description: Apprenez à signer numériquement des documents PDF, ajouter des horodatages et valider les signatures en Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Signez numériquement des fichiers PDF avec Python
Abstract: Ce guide explique comment signer numériquement des documents PDF à l'aide d'Aspose.PDF for Python via .NET. Il détaille le processus d'application de signatures numériques standard et avancées, en utilisant des certificats (PFX et PKCS#12), et la personnalisation de l'apparence et du comportement de la signature. La documentation comprend des exemples de code qui démontrent comment signer des PDF existants, ajouter des horodatages et vérifier la validité de la signature. Cela permet aux développeurs d'assurer l'authenticité, l'intégrité et la conformité des documents aux normes de signature numérique dans leurs applications Python.
---

## Signer le PDF avec des signatures numériques

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

Une **signature détachée PKCS#7** ajoute une signature numérique à un document sans intégrer le contenu dans le bloc de signature.

Utilisez ces exemples lorsque vous devez appliquer des signatures basées sur des certificats aux fichiers PDF, vérifier la validité des signatures ou ajouter des horodatages de confiance aux documents signés.

L'exemple suivant signe un document PDF en utilisant une signature numérique détachée PKCS#7, appliquant la signature à la première page dans une zone rectangulaire spécifiée.

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

**Vérifier toutes les signatures numériques dans un document PDF**

1. Crée une instance de PdfFileSignature qui vous permet d'interagir avec les signatures dans le PDF.
1. Obtenez une liste des noms de signature `get_signature_names(True)`.
1. Vérifie la première signature de la liste `verify_signature` pour se conformer au certificat spécifié.

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

**Vérifier une signature avec un fichier de certificat de clé publique**

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

**Vérifier une signature avec le certificat extrait du fichier**

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

**Vérifier les signatures avec la validation de la chaîne de certificats activée**

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

## Ajouter un horodatage à la signature numérique

### Comment signer numériquement un PDF avec horodatage

Aspose.PDF for Python prend en charge la signature numérique du PDF avec un serveur d'horodatage ou un service Web.

Afin d’accomplir cette exigence, le [TimestampSettings](https://reference.aspose.com/pdf/python-net/aspose.pdf/timestampsettings/) Une classe a été ajoutée à l'espace de noms Aspose.PDF. Veuillez consulter le fragment de code suivant qui récupère l'horodatage et l'ajoute au document PDF :

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

## Signer des documents PDF en utilisant ECDSA

Signer des documents PDF en utilisant ECDSA (Elliptic Curve Digital Signature Algorithm) implique d'utiliser la cryptographie à courbes elliptiques pour générer des signatures numériques.

L'extrait de code ci‑dessus illustre comment appliquer une signature numérique détachée PKCS#7 à un document PDF en utilisant Aspose.PDF for Python. En chargeant le document, en configurant l'apparence de la signature et les paramètres de sécurité, puis en enregistrant le résultat, cet exemple démontre un flux de travail complet et fiable pour signer numériquement des fichiers PDF.

Cette méthode garantit l'authenticité et l'intégrité du document en incorporant une signature sécurisée et vérifiable sur la première page. L'utilisation de SHA-256 comme algorithme de hachage répond aux normes cryptographiques modernes, tandis que la possibilité de contrôler le placement de la signature offre une flexibilité pour les marques d'approbation visibles.

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

**Vérifier les signatures ECDSA dans un document PDF**

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

## Sujets de sécurité associés

- [Sécurisez et signez les fichiers PDF en Python](/pdf/fr/python-net/securing-and-signing/)
- [Extraire les informations d'image et de signature en Python](/pdf/fr/python-net/extract-image-and-signature-information/)
- [Signer des documents PDF à partir d'une carte à puce en Python](/pdf/fr/python-net/sign-pdf-document-from-smart-card/)
- [Chiffrer et déchiffrer des fichiers PDF en Python](/pdf/fr/python-net/set-privileges-encrypt-and-decrypt-pdf-file/)