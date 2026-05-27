---
title: Signer des documents PDF
type: docs
weight: 10
url: /fr/python-net/pdf-signing/
description: Apprenez comment signer des documents PDF en Python en utilisant PdfFileSignature avec des signatures numériques basées sur certificat, nommées et visibles.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Signer des documents PDF avec des signatures numériques en Python
Abstract: Cet article montre comment signer des documents PDF avec Aspose.PDF for Python via .NET en utilisant la façade PdfFileSignature. Il couvre la configuration du certificat, la signature avec des paramètres de base, la signature avec un objet PKCS7, l'attribution d'un nom de signature et l'application d'une apparence de signature visible.
---

Aspose.PDF for Python via .NET fournit le [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) façade pour appliquer des signatures numériques à des documents PDF existants. En utilisant un fichier de certificat, vous pouvez signer un document par programmation, placer la signature sur une page, attribuer des métadonnées de signature et personnaliser la façon dont la signature est affichée.

Cet article présente plusieurs flux de travail de signature courants :

1. Créer et lier un `PdfFileSignature` objet au PDF d'entrée.
1. Configurez le certificat de signature.
1. Appliquez une signature numérique à la page cible.
1. Attribuez éventuellement un nom de signature et une apparence visible.
1. Enregistrez le PDF signé.

## Préparer des aides de signature réutilisables

Avant d'appliquer une signature numérique à un PDF, il est utile de mettre en place un petit groupe de fonctions d'aide réutilisables. Ces aides initialisent le gestionnaire de signature, définissent la zone de signature visible, configurent le certificat et créent des objets de signature PKCS#7 réutilisables afin que les exemples de signature ci-dessous restent autonomes et plus faciles à suivre.

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

## Signer un PDF avec des paramètres de certificat de base

Cette approche configure le certificat directement sur le `PdfFileSignature` objet. Il est utile lorsque vous souhaitez un flux de signature simple avec des métadonnées de signature standard et aucune gestion séparée des objets de signature.

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

## Signer un PDF avec un objet PKCS7

Utilisez un `PKCS7` objet lorsque vous devez préparer la signature d'abord, puis la transmettre à l'appel de signature. Ce modèle vous donne plus de contrôle sur les paramètres de signature et constitue une bonne base pour des flux de travail plus avancés.

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

## Signer un PDF avec une signature nommée

Si votre flux de travail de document dépend d'un nom de champ de signature prédéfini, transmettez ce nom à `sign()`. Cela facilite la référence à la signature ultérieurement pour la validation, le traitement ou l'intégration à un flux de travail d'approbation.

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

## Appliquer une signature visible

Vous pouvez rendre la signature visible sur la page PDF en assignant une apparence personnalisée à la `PKCS7` objet. Ceci est utile lorsque le document de sortie doit afficher les détails d'approbation tels que la raison, le lieu et les coordonnées aux utilisateurs finaux.

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
