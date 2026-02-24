---
title: Supprimer les images d'un fichier PDF à l'aide de Python
linktitle: Supprimer les images
type: docs
weight: 20
url: /fr/python-net/delete-images-from-pdf-file/
description: Cette section explique comment supprimer des images d'un fichier PDF en utilisant Aspose.PDF pour Python via .NET.
lastmod: "2025-09-27"
TechArticle: true
AlternativeHeadline: Comment supprimer des images d'un PDF avec Python
Abstract: L'article explique les différentes raisons de supprimer des images des fichiers PDF, telles que la protection de la vie privée, la prévention de l'accès non autorisé à des informations sensibles, la réduction de la taille du fichier pour faciliter le partage et le stockage, ainsi que la préparation du document à la compression ou à l'extraction de texte. Il présente **Aspose.PDF for Python via .NET** comme un outil pour accomplir cette tâche. L'article fournit des instructions étape par étape et des extraits de code pour supprimer des images spécifiques ou toutes les images d'un fichier PDF à l'aide d'Aspose.PDF. Le processus consiste à ouvrir un document PDF existant, à supprimer les images individuellement ou en masse, puis à enregistrer le fichier mis à jour. Le code Python fourni montre comment supprimer les images en accédant aux ressources du document et en modifiant les pages souhaitées.
---

Il existe de nombreuses raisons de supprimer toutes les images ou des images spécifiques des PDF.
Parfois, un fichier PDF peut contenir des images importantes qui doivent être supprimées pour protéger la vie privée ou empêcher l'accès non autorisé à certaines informations.

Supprimer les images indésirables ou redondantes peut aider à réduire la taille du fichier, facilitant ainsi le partage ou le stockage des PDF.
Si nécessaire, vous pouvez réduire le nombre de pages en supprimant toutes les images du document.
De plus, la suppression des images du document aidera à préparer le PDF pour la compression ou l'extraction d'informations textuelles.

**Aspose.PDF for Python via .NET** vous aidera dans cette tâche.

## Supprimer les images d'un fichier PDF

Pour supprimer une image d'un fichier PDF :

1. Ouvrez le document PDF existant.
1. Supprimez une image particulière.
1. Enregistrez le fichier PDF mis à jour.

L'extrait de code suivant montre comment supprimer une image d'un fichier PDF.

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)

    document = ap.Document(path_infile)
    document.pages[1].resources.images.delete(1)
    document.save(path_outfile)
```
