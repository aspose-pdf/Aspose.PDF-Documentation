---
title: Suppression d'une pièce jointe d'un PDF avec Python
linktitle: Suppression d'une pièce jointe d'un PDF existant
type: docs
weight: 30
url: /fr/python-net/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF peut supprimer les pièces jointes de vos documents PDF. Utilisez l'API PDF Python pour supprimer les pièces jointes des fichiers PDF en utilisant Aspose.PDF pour Python via la bibliothèque .NET.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment supprimer les pièces jointes d'un PDF avec Python
Abstract: Cet article explique comment supprimer les pièces jointes des fichiers PDF en utilisant Aspose.PDF pour Python. Les pièces jointes d'un document PDF sont stockées dans la collection `EmbeddedFiles` de l'objet `Document`. Pour supprimer toutes les pièces jointes d'un PDF, vous pouvez appeler la méthode `delete()` sur la collection `EmbeddedFiles`, puis enregistrer le document mis à jour en utilisant la méthode `save()` de l'objet `Document`. Un extrait de code est fourni pour démontrer ce processus, illustrant les étapes d'ouverture d'un document, de suppression de ses pièces jointes et d'enregistrement du fichier modifié.
---

Aspose.PDF pour Python peut supprimer les pièces jointes des fichiers PDF. Les pièces jointes d'un document PDF sont stockées dans la collection [EmbeddedFiles](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) de l'objet Document.

Pour supprimer toutes les pièces jointes associées à un fichier PDF :

1. Appelez la méthode [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/#methods) de la collection [EmbeddedFiles](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/).
1. Enregistrez le fichier mis à jour en utilisant la méthode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) de l'objet [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

L'extrait de code suivant montre comment supprimer les pièces jointes d'un document PDF.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Delete all attachments
    document.embedded_files.delete()

    # Save updated file
    document.save(output_pdf)
```


