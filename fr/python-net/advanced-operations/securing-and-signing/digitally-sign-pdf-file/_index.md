---
title: Ajouter une signature numérique ou signer numériquement un PDF en Python
linktitle: Signer numériquement le PDF
type: docs
weight: 10
url: /fr/python-net/digitally-sign-pdf-file/
description: Signer numériquement des documents PDF, vérifier ou valider les PDF signés numériquement à l'aide de Python.
lastmod: "2025-06-07"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Signer numériquement des fichiers PDF avec Python
Abstract: Ce guide explique comment signer numériquement des documents PDF à l'aide d'Aspose.PDF pour Python via .NET. Il détaille le processus d'application de signatures numériques standards et avancées, l'utilisation de certificats (PFX et PKCS#12) et la personnalisation de l'apparence et du comportement de la signature. La documentation comprend des exemples de code qui démontrent comment signer des PDF existants, ajouter des horodatages et vérifier la validité de la signature. Cela permet aux développeurs d'assurer l'authenticité, l'intégrité et la conformité des documents aux normes de signature numérique dans leurs applications Python.
---

## Signer un PDF avec des signatures numériques

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing

    ppath_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile
    path_pfxfile = self.data_dir + pfxfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Instantiate PdfFileSignature object
        with ap.facades.PdfFileSignature(document) as signature:
            # Create PKCS#7 object for sign
            pkcs = ap.forms.PKCS7(path_pfxfile, "12345")
            # Sign PDF file
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)
            #  Save PDF document
            signature.save(path_outfile)
```

Une **signature détachée PKCS#7** ajoute une signature numérique à un document sans incorporer le contenu dans le bloc de signature.

L'exemple suivant signe un document PDF en utilisant une signature numérique détachée PKCS#7, en appliquant la signature à la première page dans une zone rectangulaire spécifiée.

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile
    path_pfxfile = self.data_dir + pfxfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Instantiate PdfFileSignature object using the opened document
        with ap.facades.PdfFileSignature(document) as signature:
            # Create PKCS#7 detached object for sign
            pkcs = ap.forms.PKCS7Detached(path_pfxfile, password, ap.DigestHashAlgorithm.SHA256)
            # Sign PDF file
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)
            #  Save PDF document
            signature.save(path_outfile)
```

Cet extrait de code Python vérifie une signature numérique dans un fichier PDF en utilisant la méthode 'file_sign.verify_signature()'.

1. Crée une instance de PdfFileSignature qui vous permet d'interagir avec les signatures dans le PDF.
1. Obtient une liste des noms de signature `get_signature_names(True)`.
1. Vérifie la première signature de la liste `verify_signature` pour la conformité avec le certificat spécifié.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile

    # Create an instance of PdfFileSignature for working with signatures in the document
    with ap.facades.PdfFileSignature(path_infile) as file_sign:
        # Get a list of signatures
        signature_names = file_sign.get_signature_names(True)
        # Verify the signature with the given name.
        return file_sign.verify_signature(signature_names[0], certificate)
```

## Ajouter un horodatage à la signature numérique

### Comment signer numériquement un PDF avec un horodatage

Aspose.PDF pour Python prend en charge la signature numérique du PDF avec un serveur d'horodatage ou un service Web.

Pour répondre à cette exigence, la classe [TimestampSettings](https://reference.aspose.com/pdf/python-net/aspose.pdf/timestampsettings/) a été ajoutée à l'espace de noms Aspose.PDF. Veuillez consulter l'extrait de code suivant qui obtient l'horodatage et l'ajoute au document PDF :

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile
    path_pfxfile = self.data_dir + pfxfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create an instance of PdfFileSignature for working with signatures in the document
        with ap.facades.PdfFileSignature(document) as signature:
            pkcs = ap.forms.PKCS7(path_pfxfile, password)
            # Create TimestampSettings settings
            timestamp_settings = ap.TimestampSettings("https://freetsa.org/tsr",
                                                                "", ap.DigestHashAlgorithm.SHA256)  # User/Password can be omitted
            pkcs.timestamp_settings = timestamp_settings
            rect = drawing.Rectangle(100, 100, 200, 100)  # Creating a rectangle for the signature
            # Create any of the three signature types
            signature.sign(1, "Signature Reason", "Contact", "Location", True, rect, pkcs)
            # Save PDF document
                signature.save(path_outfile)
```

## Signer des documents PDF en utilisant ECDSA

Signer des documents PDF en utilisant ECDSA (Elliptic Curve Digital Signature Algorithm) implique l'utilisation de la cryptographie à courbe elliptique pour générer des signatures numériques.

L'extrait de code ci-dessus illustre comment appliquer une signature numérique détachée PKCS#7 à un document PDF à l'aide d'Aspose.PDF pour Python. En chargeant le document, en configurant l'apparence de la signature et les paramètres de sécurité, puis en enregistrant le résultat, cet exemple démontre un flux de travail complet et fiable pour signer numériquement des fichiers PDF.

Cette méthode garantit l'authenticité et l'intégrité du document en intégrant une signature sécurisée et vérifiable sur la première page. L'utilisation de SHA-256 comme algorithme de hachage répond aux standards cryptographiques modernes, tandis que la capacité à contrôler le placement de la signature offre une flexibilité pour les marques d'approbation visibles.

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile
    path_pfxfile = self.data_dir + pfxfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create an instance of PdfFileSignature to sign the document
        with ap.facades.PdfFileSignature(document) as signature:
            # Create a PKCS7Detached object using the provided certificate and password
            pkcs = ap.forms.PKCS7Detached(path_pfxfile, password, ap.DigestHashAlgorithm.SHA256)

            # Sign the first page of the document, setting the signature's appearance at the specified location
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)

            # Save PDF document
            signature.save(path_outfile)
```
