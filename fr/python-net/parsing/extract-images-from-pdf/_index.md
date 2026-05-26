---
title: Extraire des images du PDF à l'aide de Python
linktitle: Extraire des images du PDF
type: docs
weight: 20
url: /fr/python-net/extract-images-from-the-pdf-file/
description: Apprenez comment extraire des images intégrées des fichiers PDF avec Aspose.PDF for Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment extraire des images du PDF via Python
Abstract: Cet article explique comment extraire des images intégrées d'un document PDF avec Aspose.PDF for Python. Il couvre l'ouverture du PDF source avec la classe Document, l'accès à une image de la collection des ressources de la page, et l'enregistrement de l'XImage extrait vers un fichier externe pour réutilisation, inspection ou traitement en aval.
---

Utiliser [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) pour ouvrir le PDF, puis accéder aux ressources de la page afin de récupérer un [XImage](https://reference.aspose.com/pdf/python-net/aspose.pdf/ximage/) objet et l'enregistrer comme un fichier distinct. Cette approche est utile lorsque vous devez réutiliser des images, inspecter les ressources extraites, ou créer des flux de travail de traitement d'images à partir du contenu PDF.

1. Ouvrez le PDF en tant que `Document`.
1. Accédez à la ressource d'image depuis la page cible.
1. Récupérer le requis `XImage` à partir de la collection d'images de la page.
1. Enregistrez l'image extraite dans un fichier de sortie.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    document = apdf.Document(path_infile)
    xImage = document.pages[1].resources.images[1]
    with FileIO(path_outfile, "w") as output_image:
        xImage.save(output_image)
```
