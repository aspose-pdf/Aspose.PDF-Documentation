---
title: Supprimer les pièces jointes d'un PDF en Python
linktitle: Suppression d’une pièce jointe d’un PDF existant
type: docs
weight: 30
url: /fr/python-net/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF peut supprimer les pièces jointes de vos documents PDF. Utilisez l’API PDF Python pour supprimer les pièces jointes dans les fichiers PDF à l’aide de la bibliothèque Aspose.PDF for Python via .NET.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment supprimer les pièces jointes d’un PDF avec Python
Abstract: Cet article explique comment supprimer les pièces jointes des fichiers PDF à l’aide d’Aspose.PDF for Python. Les pièces jointes d’un document PDF sont stockées dans la collection `EmbeddedFiles` de l’objet `Document`. Pour supprimer toutes les pièces jointes d’un PDF, vous pouvez appeler la méthode `delete()` sur la collection `EmbeddedFiles`, puis enregistrer le document mis à jour en utilisant la méthode `save()` de l’objet `Document`. Un extrait de code est fourni pour démontrer ce processus, montrant les étapes d’ouverture d’un document, de suppression de ses pièces jointes et d’enregistrement du fichier modifié.
---

Aspose.PDF for Python peut supprimer les pièces jointes des fichiers PDF. Les pièces jointes d’un document PDF sont contenues dans l’objet Document. [EmbeddedFiles](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) collection.

Ce flux de travail est utile lorsque vous devez nettoyer les fichiers incorporés obsolètes, réduire la taille du package ou préparer un PDF pour redistribution sans les documents source joints.

Pour supprimer toutes les pièces jointes associées à un fichier PDF :

1. Appelez le [EmbeddedFiles](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) collection’s [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/#methods) méthode.
1. Enregistrez le fichier mis à jour en utilisant le [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) de l'objet [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) méthode.

Le fragment de code suivant montre comment supprimer les pièces jointes d'un document PDF.

```python

import aspose.pdf as ap

def remove_attachment(infile, outfile):
    # Open PDF document
    with ap.Document(infile) as document:
        document.embedded_files.delete()
        document.save(outfile)
```

## Supprimer une pièce jointe spécifique par son nom

Si vous devez supprimer une seule pièce jointe et conserver les autres, utilisez le [delete_by_key()](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/delete_by_key/) méthode et transmettez le nom de la pièce jointe.

Pour supprimer une pièce jointe spécifique :

1. Ouvrez le fichier PDF source.
1. Appel `document.embedded_files.delete_by_key(attachment_name)`.
1. Enregistrez le fichier PDF mis à jour.

Le fragment de code suivant supprime une pièce jointe par son nom.

```python

import aspose.pdf as ap

def remove_attachment(infile, attachment_name, outfile):
    # Open PDF document
    with ap.Document(infile) as document:
        document.embedded_files.delete_by_key(attachment_name)
        document.save(outfile)
```

## Sujets liés aux pièces jointes

- [Travailler avec les pièces jointes PDF en Python](/pdf/fr/python-net/attachments/)
- [Ajouter des pièces jointes au PDF en Python](/pdf/fr/python-net/add-attachment-to-pdf-document/)
- [Créer et gérer des portefeuilles PDF en Python](/pdf/fr/python-net/portfolio/)

