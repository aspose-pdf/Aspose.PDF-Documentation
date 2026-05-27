---
title: Signer des documents PDF à partir d'une carte à puce en Python
linktitle: Signature PDF avec carte à puce
type: docs
weight: 30
url: /fr/python-net/sign-pdf-document-from-smart-card/
description: Apprenez comment signer des documents PDF avec des cartes à puce et des certificats externes en Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Signer des documents PDF à partir d'une carte à puce avec Python
Abstract: Ce guide explique comment signer numériquement des documents PDF à l'aide d'une carte à puce avec Aspose.PDF for Python via .NET. Il montre comment accéder aux certificats stockés sur des périphériques matériels (tels que des jetons USB ou des cartes à puce) via le Windows Certificate Store et les utiliser pour signer des fichiers PDF. La documentation comprend des exemples de code qui montrent comment localiser le certificat approprié, configurer les propriétés de la signature et intégrer la signature numérique dans le PDF. Cela permet une signature sécurisée, prise en charge par le matériel, conforme aux normes de signature numérique, adaptée aux flux de travail d'entreprise et juridiques à haute confiance.
---

Aspose.PDF fournit des capacités robustes pour l'intégration des composants de signature visuelle et cryptographique, garantissant à la fois l'authenticité et une présentation professionnelle dans les documents PDF signés numériquement.

Utilisez ce flux de travail lorsque votre processus de signature dépend de certificats stockés sur des appareils matériels tels que les cartes à puce, les jetons USB ou les magasins de certificats gérés.

## Signer avec une carte à puce en utilisant le champ de signature

Cet exemple montre comment signer numériquement un document PDF à l'aide d'un certificat externe avec Aspose.PDF for Python et appliquer une image d'apparence de signature personnalisée :

1. Ouverture du document PDF.
1. Création d'un objet PdfFileSignature et liaison de celui-ci au document.
1. Récupération d'un certificat numérique local à l'aide d'une méthode personnalisée `get_local_certificate()`.
1. Configuration d'une ExternalSignature basée sur le certificat sélectionné.
1. Appliquer une image personnalisée d'apparence de signature (par ex., un logo d'entreprise ou une signature manuscrite).
1. Signer numériquement la première page du document avec les métadonnées spécifiées (raison, contact, emplacement).
1. Enregistrer le document signé dans un nouveau fichier de sortie.

Cette méthode est idéale pour les cas où les signatures doivent être appliquées de manière programmatique à l'aide de certificats externes—tels que des jetons matériels, des magasins de certificats ou des fournisseurs de confiance—et présentées avec une mise en page visuelle personnalisée.

Voici les extraits de code pour signer un document PDF à partir d'une carte à puce :

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

## Vérifier les signatures numériques

Cet extrait de code montre comment vérifier les signatures numériques dans un document PDF en utilisant Aspose.PDF for Python:

1. Ouverture du fichier PDF.
1. Création d'un 'PdfFileSignature object' et liaison au document.
1. Récupération de la liste de tous les noms de champs de signature en utilisant 'get_signature_names()'.
1. Itération à travers chaque signature et vérification de sa validité avec 'verify_signature()'.
1. Lever une exception si une signature échoue la vérification.

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

## Signer avec un certificat externe

Cet extrait de code montre comment ajouter et signer un champ de signature numérique dans un document PDF en utilisant Aspose.PDF for Python avec un certificat externe :

1. Ouverture du fichier PDF en tant que flux binaire.
1. Création d'un SignatureField et placement sur la première page du document à une position spécifiée.
1. Récupération d'un certificat numérique local à l'aide d'une méthode personnalisée `get_local_certificate()`.
1. Configuration d'un ExternalSignature avec des métadonnées telles que l'autorité, le motif et les coordonnées.
1. Attribuer un nom de champ unique au champ de signature (partial_name = "sig1").
1. Ajouter le champ de signature aux champs de formulaire du PDF.
1. Signer le champ avec le certificat externe.
1. Enregistrer le document signé dans un fichier de sortie.

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

## Sujets de sécurité associés

- [Sécurisez et signez les fichiers PDF en Python](/pdf/fr/python-net/securing-and-signing/)
- [Signer numériquement des fichiers PDF en Python](/pdf/fr/python-net/digitally-sign-pdf-file/)
- [Extraire les informations de signature du PDF en Python](/pdf/fr/python-net/extract-image-and-signature-information/)
- [Chiffrer et déchiffrer des fichiers PDF en Python](/pdf/fr/python-net/set-privileges-encrypt-and-decrypt-pdf-file/)

