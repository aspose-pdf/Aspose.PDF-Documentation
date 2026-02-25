---
title: Ajout d'une pièce jointe à un document PDF avec Python
linktitle: Ajout d'une pièce jointe à un document PDF
type: docs
weight: 10
url: /fr/python-net/add-attachment-to-pdf-document/
description: Cette page décrit comment ajouter une pièce jointe à un fichier PDF avec Aspose.PDF pour Python via la bibliothèque .NET.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment ajouter des pièces jointes à un PDF avec Python
Abstract: Cet article fournit un guide étape par étape sur la façon d’ajouter des pièces jointes à un fichier PDF en utilisant Python et la bibliothèque Aspose.PDF. Il détaille le processus de création d’un nouveau projet Python, d’importation du package Aspose.PDF nécessaire et de création d’un objet `Document`. L’article explique comment créer un objet `FileSpecification` avec le fichier souhaité et sa description, et comment ajouter cet objet à la `EmbeddedFileCollection` du document PDF en utilisant la méthode `add`. La `EmbeddedFileCollection` contient toutes les pièces jointes du PDF. Un extrait de code est inclus pour démontrer le processus d’ouverture d’un document, de configuration d’un fichier à joindre, de son ajout à la collection de pièces jointes du document, et d’enregistrement du PDF mis à jour.
---

Les pièces jointes peuvent contenir une grande variété d’informations et peuvent être de différents types de fichiers. Cet article explique comment ajouter une pièce jointe à un fichier PDF.

1. Créez un nouveau projet Python.
1. Importez le package Aspose.PDF
1. Créez un objet [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) .
1. Créez un objet [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) avec le fichier que vous ajoutez et la description du fichier.
1. Ajoutez l’objet [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) à la collection [EmbeddedFileCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) de l’objet [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), en utilisant la méthode [add](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/#methods).

La collection [EmbeddedFileCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) contient toutes les pièces jointes du fichier PDF. Le fragment de code suivant vous montre comment ajouter une pièce jointe dans un document PDF.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Setup new file to be added as attachment
    fileSpecification = ap.FileSpecification(attachment_file, "Sample text file")

    # Add attachment to document's attachment collection
    document.embedded_files.append(fileSpecification)

    # Save new output
    document.save(output_pdf)
```


