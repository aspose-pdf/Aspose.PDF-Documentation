---
title: Comment ajouter une signature de carte à puce à un PDF
linktitle: Signature PDF avec carte à puce
type: docs
weight: 30
url: /fr/python-net/sign-pdf-document-from-smart-card/
description: Aspose.PDF pour Python via .NET vous permet de signer des documents PDF à partir d'une carte à puce en utilisant le champ de signature.
lastmod: "2025-06-22"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Signer des documents PDF à partir d'une carte à puce avec Python
Abstract: Ce guide explique comment signer numériquement des documents PDF à l'aide d'une carte à puce avec Aspose.PDF pour Python via .NET. Il montre comment accéder aux certificats stockés sur des appareils matériels (tels que des jetons USB ou des cartes à puce) via le magasin de certificats Windows et les utiliser pour signer des fichiers PDF. La documentation comprend des exemples de code montrant comment localiser le certificat approprié, configurer les propriétés de signature et intégrer la signature numérique dans le PDF. Cela permet une signature sécurisée, soutenue par le matériel, conforme aux normes de signature numérique, adaptée aux workflows d'entreprise et juridiques à haut niveau de confiance.
---

Aspose.PDF offre des capacités robustes pour intégrer des composants de signature visuelle et cryptographique, garantissant à la fois l'authenticité et une présentation professionnelle dans les documents PDF signés numériquement.

## Signer avec carte à puce en utilisant le champ de signature

Cet exemple montre comment signer numériquement un document PDF en utilisant un certificat externe avec Aspose.PDF pour Python et appliquer une image d'apparence de signature personnalisée :

1. Ouverture du document PDF.
1. Création d'un objet PdfFileSignature et liaison au document.
1. Récupération d'un certificat numérique local à l'aide d'une méthode personnalisée `get_local_certificate()`.
1. Configuration d'une ExternalSignature basée sur le certificat sélectionné.
1. Application d'une image d'apparence de signature personnalisée (par ex., un logo d'entreprise ou une signature manuscrite).
1. Signature numérique de la première page du document avec les métadonnées spécifiées (raison, contact, localisation).
1. Enregistrement du document signé dans un nouveau fichier de sortie.

Cette méthode est idéale pour les cas où les signatures doivent être appliquées de manière programmatique à l'aide de certificats externes — tels que des jetons matériels, des magasins de certificats ou des fournisseurs de confiance — et présentées avec une mise en page visuelle personnalisée.

Voici les extraits de code pour signer un document PDF à partir d'une carte à puce :

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile
    path_pngfile = self.data_dir + pngfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        with ap.facades.PdfFileSignature() as pdf_signature:
            # Bind PDF document
            pdf_signature.bind_pdf(document)
            selected_certificates = self.get_local_certificate()
            # Set an external signature settings
            external_signature = ap.forms.ExternalSignature(selected_certificates)
            pdf_signature.signature_appearance = path_pngfile
            # Sign the document
            pdf_signature.sign(1, "Reason", "Contact", "Location", True, drawing.Rectangle(100, 100, 200, 200),
                                external_signature)
            # Save PDF document
            pdf_signature.save(path_outfile)
```

## Vérifier les signatures numériques

Cet extrait de code montre comment vérifier les signatures numériques dans un document PDF à l'aide d'Aspose.PDF pour Python :

1. Ouverture du fichier PDF.
1. Création d'un objet 'PdfFileSignature' et liaison au document.
1. Récupération de la liste de tous les noms de champs de signature à l'aide de 'get_signature_names()'.
1. Parcours de chaque signature et vérification de sa validité avec 'verify_signature()'.
1. Levée d'une exception si une signature échoue à la vérification.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile

    # Open PDF document
    with ap.Document(path_infile) as document:
        with ap.facades.PdfFileSignature(document) as pdf_signature:
            signature_names = pdf_signature.get_signature_names(True)
            for index in range(len(signature_names)):
                if not pdf_signature.verify_signature(signature_names[index]):
                    raise Exception("Not verified")
```

## Signer avec un certificat externe

Cet extrait de code montre comment ajouter et signer un champ de signature numérique dans un document PDF en utilisant Aspose.PDF pour Python avec un certificat externe :

1. Ouverture du fichier PDF en tant que flux binaire.
1. Création d'un SignatureField et placement sur la première page du document à une position spécifiée.
1. Récupération d'un certificat numérique local à l'aide d'une méthode personnalisée `get_local_certificate()`.
1. Configuration d'une ExternalSignature avec des métadonnées telles que l'autorité, la raison et les informations de contact.
1. Attribution d'un nom de champ unique au champ de signature (partial_name = "sig1").
1. Ajout du champ de signature aux champs de formulaire du PDF.
1. Signature du champ avec le certificat externe.
1. Enregistrement du document signé dans un fichier de sortie.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open a document stream
    with open(path_infile, "rb+") as file_stream:
        # Open PDF document from stream
        document = ap.Document(file_stream)

        # Create a signature field
        signature_field = ap.forms.SignatureField(document.pages[1], ap.Rectangle(100, 400, 10, 10, True))
        selected_certificate = self.get_local_certificate()

        # Set external signature settings
        external_signature = ap.forms.ExternalSignature(selected_certificate)
        external_signature.authority = "Me"
        external_signature.reason = "Reason"
        external_signature.contact_info = "Contact"

        # Set a name of signature field
        signature_field.partial_name = "sig1"

        # Add the signature field to the document
        document.form.add(signature_field, 1)

        # Sign the document
        signature_field.sign(external_signature)

        # Save PDF document
        document.save(path_outfile)
```


