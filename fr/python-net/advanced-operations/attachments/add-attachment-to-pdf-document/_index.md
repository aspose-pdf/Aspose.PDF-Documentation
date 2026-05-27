---
title: Ajouter des pièces jointes à un PDF en Python
linktitle: Ajouter une pièce jointe à un document PDF
type: docs
weight: 10
url: /fr/python-net/add-attachment-to-pdf-document/
description: Apprenez comment ajouter des pièces jointes à des documents PDF en Python en utilisant Aspose.PDF for Python via .NET.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment ajouter des pièces jointes à un PDF avec Python
Abstract: Cet article fournit un guide étape par étape sur la façon d’ajouter des pièces jointes à un fichier PDF en utilisant Python et la bibliothèque Aspose.PDF. Il détaille le processus de configuration d’un nouveau projet Python, d’importation du package Aspose.PDF nécessaire, et de création d’un objet `Document`. L’article explique comment créer un objet `FileSpecification` avec le fichier souhaité et sa description, et comment ajouter cet objet à la `EmbeddedFileCollection` du document PDF en utilisant la méthode `add`. La `EmbeddedFileCollection` contient toutes les pièces jointes du PDF. Un extrait de code est inclus pour démontrer le processus d’ouverture d’un document, de configuration d’un fichier à attacher, de son ajout à la collection de pièces jointes du document, et d’enregistrement du PDF mis à jour.
---

Les pièces jointes peuvent contenir une grande variété d’informations et peuvent être de différents types de fichiers. Cet article explique comment ajouter une pièce jointe à un fichier PDF.

Utilisez les pièces jointes PDF intégrées lorsque vous devez regrouper des fichiers source de support, des feuilles de calcul, des images ou des documents associés avec le PDF principal.

1. Créez un nouveau projet Python.
1. Importez le package Aspose.PDF
1. Créer un [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objet.
1. Créer un [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) objet contenant le fichier que vous ajoutez, et la description du fichier.
1. Ajouter le [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) objet à le [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) de l'objet [EmbeddedFileCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) collection, avec la collection [add](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/#methods) méthode.

Le [EmbeddedFileCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) La collection contient toutes les pièces jointes du fichier PDF. Le fragment de code suivant vous montre comment ajouter une pièce jointe dans un document PDF.

```python
from os import path
import aspose.pdf as ap

def add_attachments(infile, attachment_path, outfile):
    with ap.Document(infile) as document:
        file_spec = ap.FileSpecification(attachment_path, "Sample text file")
        document.embedded_files.add(path.basename(attachment_path), file_spec)
        document.save(outfile)
```

## Sujets liés aux pièces jointes

- [Travailler avec les pièces jointes PDF en Python](/pdf/fr/python-net/attachments/)
- [Supprimer les pièces jointes d'un PDF en Python](/pdf/fr/python-net/removing-attachment-from-an-existing-pdf/)
- [Créer et gérer des portefeuilles PDF en Python](/pdf/fr/python-net/portfolio/)

