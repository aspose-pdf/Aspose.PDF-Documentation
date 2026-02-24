---
title: Travailler avec les métadonnées de fichiers PDF en Python
linktitle: Métadonnées de fichiers PDF
type: docs
weight: 200
url: /fr/python-net/pdf-file-metadata/
description: Découvrez comment extraire et gérer les métadonnées PDF, telles que l'auteur et le titre, en Python avec Aspose.PDF.
lastmod: "2025-05-12"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Obtenir et définir les métadonnées dans un PDF avec Python
Abstract: L'article fournit un guide complet sur la manipulation des métadonnées PDF à l'aide d'Aspose.PDF pour Python via .NET. Il décrit les méthodes d'extraction et de définition des propriétés de métadonnées, y compris l'auteur, la date de création, les mots‑clés et plus encore, qui sont essentielles pour le catalogage des documents, l'optimisation de la recherche ou la validation. Les extraits de code montrent comment récupérer les métadonnées d'un PDF en utilisant la classe `Document` et la propriété `info`, définir de nouvelles métadonnées avec l'objet `DocumentInfo`, et enregistrer les modifications. De plus, il montre comment mettre à jour programmatiquement les métadonnées XMP, ce qui améliore l'organisation et la recherche des documents. L'article explique également comment insérer des métadonnées avec un préfixe personnalisé en enregistrant un URI d'espace de noms. Ces fonctionnalités sont essentielles pour les développeurs qui souhaitent gérer efficacement les informations des documents PDF au sein d'applications.
---

## Obtenir les informations du fichier PDF

Cet extrait de code montre comment extraire les métadonnées d'un document PDF à l'aide d'Aspose.PDF pour Python via .NET. En accédant à la propriété info de l'objet Document, il récupère les informations clés telles que l'auteur, la date de création, les mots‑clés, la date de modification, le sujet et le titre. Cette fonctionnalité est essentielle pour les applications qui nécessitent le catalogage des documents, l'optimisation de la recherche ou la validation des propriétés des documents.

1. Ouvrez le fichier PDF en utilisant la classe Document
1. Récupérez les métadonnées du document via la propriété info
1. Affichez les informations de métadonnées. Imprimez les champs de métadonnées souhaités

```python

    import aspose.pdf as ap

    def get_pdf_file_information():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf()

        # Open PDF document
        document = ap.Document(data_dir + "GetFileInfo.pdf")

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

Aspose.PDF pour Python via .NET vous permet de définir des informations spécifiques à un fichier PDF, telles que l'auteur, la date de création, le sujet et le titre. Pour définir ces informations :

1. Ouvrez le fichier PDF en utilisant la classe Document.
1. Créez un objet [DocumentInfo]() et définissez les propriétés de métadonnées souhaitées.
1. Enregistrez les modifications dans un nouveau fichier PDF en utilisant la méthode save.

L'extrait de code suivant vous montre comment définir les informations d'un fichier PDF.

```python

    import aspose.pdf as ap
    import datetime

    def set_file_information():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf_workingdocuments()

        # Open PDF document
        document = ap.Document(data_dir + "SetFileInfo.pdf")

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
        document.save(data_dir + "SetFileInfo_out.pdf")
```

## Définir les métadonnées XMP dans un fichier PDF

Cet extrait de code montre comment définir ou mettre à jour programmatiquement les métadonnées XMP dans un document PDF à l'aide d'Aspose.PDF pour Python via .NET. En modifiant des propriétés telles que xmp:CreateDate, xmp:Nickname et des champs définis sur mesure, vous pouvez intégrer des métadonnées standardisées dans vos fichiers PDF. Cette approche est particulièrement utile pour améliorer l'organisation des documents, faciliter la recherche et intégrer des informations essentielles directement dans le fichier.

Aspose.PDF vous permet de définir des métadonnées dans un fichier PDF. Pour définir des métadonnées :

1. Ouvrez le fichier PDF en utilisant la classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Modifiez les métadonnées XMP en affectant des valeurs à des clés spécifiques.
1. Enregistrez le document PDF mis à jour.

L'extrait de code suivant vous montre comment définir des métadonnées dans un fichier PDF.

```python

    import aspose.pdf as ap
    import datetime

    def set_xmp_metadata():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf()

        # Open PDF document
        document = ap.Document(data_dir + "SetXMPMetadata.pdf")

        # Set XMP metadata properties
        document.metadata["xmp:CreateDate"] = datetime.datetime.now().isoformat()
        document.metadata["xmp:Nickname"] = "Nickname"
        document.metadata["xmp:CustomProperty"] = "Custom Value"

        # Save the updated PDF document
        document.save(data_dir + "SetXMPMetadata_out.pdf")
```

## Insérer des métadonnées avec un préfixe

Certains développeurs doivent créer un nouvel espace de noms de métadonnées avec un préfixe. L'extrait de code suivant montre comment insérer des métadonnées avec un préfixe.

```python

    import aspose.pdf as ap
    import datetime

    def set_prefix_metadata():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf()

        # Open PDF document
        document = ap.Document(data_dir + "SetXMPMetadata.pdf")

        # Register a namespace URI for the 'xmp' prefix
        document.metadata.register_namespace_uri("xmp", "http://ns.adobe.com/xap/1.0/")

        # Set the metadata property using the registered prefix
        document.metadata["xmp:ModifyDate"] = datetime.datetime.now().isoformat()  # ISO 8601 format

        # Save the updated PDF document
        document.save(data_dir + "SetPrefixMetadata_out.pdf")
```
