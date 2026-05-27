---
title: Extraire les polices du PDF via Python
linktitle: Extraire les polices du PDF
type: docs
weight: 30
url: /fr/python-net/extract-fonts-from-pdf/
description: Utilisez la bibliothèque Aspose.PDF for Python pour extraire toutes les polices intégrées de votre document PDF.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment extraire les polices du PDF en utilisant Python
Abstract: Cet article explique comment examiner les polices utilisées dans un document PDF avec Aspose.PDF for Python. Il montre comment ouvrir un PDF avec la classe Document, appeler font_utilities.get_all_fonts() pour récupérer les objets de police disponibles, et parcourir les résultats afin de lire les noms des polices pour l'analyse, l'audit ou les flux de travail de traitement de documents.
---

Utiliser [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) pour ouvrir le PDF et appeler `font_utilities.get_all_fonts()` pour récupérer tout disponible [Font](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/font/) objets référencés par le document. Ceci est utile lors de l'audit des polices intégrées, de la vérification de la disponibilité des polices avant la conversion, ou de l'analyse des ressources du document.

1. Ouvrez le PDF source en tant que `Document`.
1. Appeler `document.font_utilities.get_all_fonts()` pour obtenir la collection de polices.
1. Parcourir les éléments retournés `Font` objets.
1. Lire et imprimer chaque `font.font_name` valeur.

```python

    import aspose.pdf as apdf
    from os import path

    path_infile = path.join(self.dataDir, infile)

    # Open PDF document
    document = apdf.Document(path_infile)

    fonts = document.font_utilities.get_all_fonts()
    for font in fonts:
        print(font.font_name)
```
