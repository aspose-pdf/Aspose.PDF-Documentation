---
title: Travailler avec les métadonnées de fichiers PDF en Python
linktitle: Métadonnées de fichiers PDF
type: docs
weight: 200
url: /fr/python-net/pdf-file-metadata/
description: Apprenez à extraire, mettre à jour et gérer les métadonnées de fichiers PDF et les propriétés XMP en Python à l'aide d'Aspose.PDF.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Obtenez et définissez les informations du document PDF et les métadonnées XMP en Python
Abstract: Cet article explique comment travailler avec les métadonnées PDF dans Aspose.PDF for Python via .NET. Apprenez à lire les informations du document telles que l'auteur, le titre et les mots‑clés, à mettre à jour les propriétés du fichier, à définir les champs de métadonnées XMP et à enregistrer des préfixes de métadonnées personnalisés pour les fichiers PDF en Python.
---

Utilisez ce guide lorsque vous devez inspecter les propriétés du document, mettre à jour les informations du fichier PDF pour la recherche ou le catalogage, ou gérer les métadonnées XMP de manière programmatique en Python.

## Obtenir les informations du fichier PDF

Cet extrait de code montre comment extraire les métadonnées d'un document PDF à l'aide d'Aspose.PDF for Python via .NET. En accédant à la propriété info du Document, il récupère des informations clés telles que l'auteur, la date de création, les mots‑clés, la date de modification, le sujet et le titre. Cette fonctionnalité est essentielle pour les applications qui nécessitent le catalogage de documents, l'optimisation de la recherche ou la validation des propriétés du document.

1. Ouvrez le fichier PDF en utilisant la classe Document
1. Récupérez les métadonnées du document via la propriété info
1. Affichez les informations de métadonnées. Imprimez les champs de métadonnées souhaités

```python
import aspose.pdf as ap
import datetime
import sys
from os import path

def get_pdf_file_information(infile):
    # Open PDF document
    document = ap.Document(infile)

    # Get document information
    doc_info = document.info

    # Display document information
    print(f"Author: {doc_info.author}")
    print(f"Creation Date: {doc_info.creation_date}")
    print(f"Keywords: {doc_info.keywords}")
    print(f"Modify Date: {doc_info.mod_date}")
    print(f"Subject: {doc_info.subject}")
    print(f"Title: {doc_info.title}")
```

## Définir les informations du fichier PDF

Aspose.PDF for Python via .NET vous permet de définir des informations spécifiques au fichier pour un PDF, des informations telles que l’auteur, la date de création, le sujet et le titre. Pour définir ces informations :

1. Ouvrez le fichier PDF en utilisant la classe Document.
1. Créer un [DocumentInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/documentinfo/) objet et définir les propriétés de métadonnées souhaitées.
1. Enregistrez les modifications dans un nouveau fichier PDF en utilisant la méthode save.

L'extrait de code suivant vous montre comment définir les informations du fichier PDF.

```python
import aspose.pdf as ap
import datetime
import sys
from os import path

def set_file_information(infile, outfile):

    # Open PDF document
    document = ap.Document(infile)

    # Specify document information
    doc_info = ap.DocumentInfo(document)
    doc_info.author = "Aspose"
    doc_info.creation_date = datetime.datetime.now()
    doc_info.keywords = "Aspose.Pdf, DOM, API"
    doc_info.mod_date = datetime.datetime.now()
    doc_info.subject = "PDF Information"
    doc_info.title = "Setting PDF Document Information"
    doc_info.producer = "Custom producer"
    doc_info.creator = "Custom creator"

    # Save PDF document
    document.save(outfile)
```

## Définir les métadonnées XMP dans un fichier PDF

Cet extrait de code montre comment définir ou mettre à jour programmatiquement les métadonnées XMP dans un document PDF à l'aide d'Aspose.PDF for Python via .NET. En modifiant des propriétés telles que xmp:CreateDate, xmp:Nickname et des champs définis sur mesure, vous pouvez intégrer des métadonnées standardisées dans vos fichiers PDF. Cette approche est particulièrement utile pour améliorer l'organisation des documents, faciliter la recherche et intégrer des informations essentielles directement dans le fichier.

Aspose.PDF vous permet de définir des métadonnées dans un fichier PDF. Pour définir des métadonnées :

1. Ouvrez le fichier PDF en utilisant le [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) classe.
1. Modifiez les métadonnées XMP en attribuant des valeurs à des clés spécifiques.
1. Enregistrez le Document PDF mis à jour.

L'extrait de code suivant vous montre comment définir les métadonnées dans un fichier PDF.

```python
import aspose.pdf as ap
import datetime
import sys
from os import path

def set_xmp_metadata(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Set XMP metadata properties
    document.metadata.add("xmp:CreateDate", datetime.datetime.now().isoformat())
    document.metadata.add("xmp:Nickname", "Nickname")
    document.metadata.add("xmp:CustomProperty", "Custom Value")

    # Save the updated PDF document
    document.save(outfile)
```

## Insérer des métadonnées avec un préfixe

Certains développeurs doivent créer un nouvel espace de noms de métadonnées avec un préfixe. L'extrait de code suivant montre comment insérer des métadonnées avec un préfixe.

```python
import aspose.pdf as ap
import datetime
import sys
from os import path

def set_prefix_metadata(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Register a namespace URI for the 'xmp' prefix
    document.metadata.register_namespace_uri("xmp", "http://ns.adobe.com/xap/1.0/")

    # Set the metadata property using the registered prefix
    document.metadata.add(
        "xmp:ModifyDate", datetime.datetime.now().isoformat()
    )  # ISO 8601 format

    # Save the updated PDF document
    document.save(outfile)
```

## Sujets associés

- [Opérations PDF avancées en Python](/pdf/fr/python-net/advanced-operations/)
- [Travailler avec des documents PDF en Python](/pdf/fr/python-net/working-with-documents/)
- [Travailler avec des pièces jointes PDF en Python](/pdf/fr/python-net/attachments/)
- [Comparer des documents PDF en Python](/pdf/fr/python-net/compare-pdf-documents/)
