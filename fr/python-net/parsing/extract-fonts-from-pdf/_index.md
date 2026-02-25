---
title: Extraire les polices d'un PDF via Python
linktitle: Extraire les polices d'un PDF
type: docs
weight: 30
url: /fr/python-net/extract-fonts-from-pdf/
description: Utilisez la bibliothèque Aspose.PDF pour Python afin d'extraire toutes les polices incorporées de votre document PDF.
lastmod: "2025-03-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment extraire les polices d'un PDF en utilisant Python
Abstract: Cet article fournit des instructions sur l'extraction de toutes les polices d'un document PDF à l'aide d'une méthode spécifique de la bibliothèque Aspose.PDF. Il présente la méthode `font_utilities.get_all_fonts()` disponible dans la classe `Document`, qui facilite la récupération des informations de police. L'article inclut un extrait de code Python démontrant le processus, qui consiste à importer les modules nécessaires, ouvrir le document PDF et parcourir les polices pour afficher le nom de chaque police. Cette approche est utile aux développeurs qui doivent analyser ou manipuler les données de police dans les fichiers PDF.
---

Si vous souhaitez récupérer toutes les polices d'un document PDF, vous pouvez utiliser la méthode 'font_utilities.get_all_fonts()' fournie dans la classe Document. Veuillez consulter l'extrait de code suivant afin d'obtenir toutes les polices d'un document PDF existant :

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)

    # Open PDF document
    document = apdf.Document(path_infile)

    fonts = document.font_utilities.get_all_fonts()
    for font in fonts:
        print(font.font_name)
```

