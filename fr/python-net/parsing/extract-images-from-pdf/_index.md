---
title: Extraire des images d'un PDF à l'aide de Python
linktitle: Extraire des images du PDF
type: docs
weight: 20
url: /fr/python-net/extract-images-from-the-pdf-file/
description: Comment extraire une partie de l'image d'un PDF à l'aide d'Aspose.PDF pour Python
lastmod: "2023-03-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment extraire des images d'un PDF via Python
Abstract: Cet article propose un guide concis sur l'extraction d'images intégrées d'un document PDF à l'aide de Python. Le processus comprend trois étapes principales charger le document PDF, accéder à la ressource d'image et enregistrer l'image dans un fichier. L'extrait de code utilise la bibliothèque Aspose.PDF pour faciliter ces opérations. Tout d'abord, le document PDF est chargé depuis un chemin spécifié, et l'image souhaitée est récupérée parmi les ressources de la première page. Enfin, l'image est enregistrée dans un fichier de sortie spécifié à l'aide d'une opération d'E/S de fichier, permettant une analyse, une modification ou une réutilisation ultérieure dans d'autres documents.
---

Ce fragment de code extrait les images intégrées d'un document PDF pour une analyse, une modification ou une réutilisation séparées dans d'autres documents :

1. Charger le document PDF
1. Accéder à la ressource d'image
1. Enregistrer l'image dans un fichier

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    document = apdf.Document(path_infile)
    xImage = document.pages[1].resources.images[1]
    with FileIO(path_outfile, "w") as output_image:
        xImage.save(output_image)
```

