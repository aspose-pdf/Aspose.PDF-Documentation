---
title: Comment créer un PDF avec Python
linktitle: Créer un document PDF
type: docs
weight: 10
url: /fr/python-net/create-pdf-document/
description: Créer et formater le document PDF avec Aspose.PDF for Python via .NET.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Créer un fichier PDF avec Python
Abstract: Aspose.PDF for Python via .NET est une API polyvalente conçue pour les développeurs afin de manipuler des fichiers PDF au sein d'applications Python ciblant le framework .NET. Elle permet aux utilisateurs de créer, charger, modifier et convertir des documents PDF facilement. Cet article fournit un guide étape par étape pour créer un fichier PDF simple à l'aide d'Aspose.PDF. Le processus consiste à initialiser un objet `Document`, ajouter une `Page` au document, insérer un `TextFragment` dans les paragraphes de la page, puis enregistrer le fichier au format PDF. L'extrait de code Python inclus montre ces étapes en créant un document PDF contenant le texte "Hello World!". Cette API simplifie la gestion des PDF avec peu de code, améliorant la productivité des développeurs travaillant avec les PDF dans les environnements .NET.
---

**Aspose.PDF for Python via .NET** est une API de manipulation PDF qui permet aux développeurs de créer, charger, modifier et convertir des fichiers PDF directement depuis Python pour les applications .NET avec seulement quelques lignes de code.

## Comment créer un fichier PDF simple

Pour créer un PDF en utilisant Python via .NET avec Aspose.PDF, vous pouvez suivre ces étapes :

1. Créez un objet de la classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)
1. Ajoutez un objet [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) à la collection [pages](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) de l'objet Document
1. Ajoutez un [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) à la collection [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) de la page
1. Enregistrez le document PDF résultant

```python

    import aspose.pdf as ap

    # Initialize document object
    document = ap.Document()
    # Add page
    page = document.pages.add()
    # Add text to new page
    page.paragraphs.add(ap.text.TextFragment("Hello World!"))
    # Save updated PDF
    document.save(output_pdf)
```


