---
title: Créer un document PDF de manière programmatique
linktitle: Créer un PDF
type: docs
weight: 10
url: /fr/python-net/create-document/
description: Cette page décrit comment créer un document PDF à partir de zéro avec la bibliothèque Aspose.PDF pour Python via .NET.
TechArticle: true
AlternativeHeadline: Générer des fichiers PDF avec Aspose.PDF pour Python
Abstract: Dans le développement logiciel, la génération de fichiers PDF de manière programmatique est une exigence courante, notamment pour la création de rapports et d'autres documents. Écrire du code personnalisé pour cette tâche peut être inefficace et chronophage. À la place, les développeurs peuvent utiliser **Aspose.PDF pour Python via .NET**, une solution robuste pour créer des fichiers PDF en Python. Le processus consiste à créer un objet `Document`, à ajouter un objet `Page` à la collection `Pages` du document, à insérer un `TextFragment` dans la collection `paragraphs` de la page, puis à enregistrer le document. Un extrait de code Python illustratif montre ces étapes, démontrant la facilité avec laquelle les fichiers PDF peuvent être générés à l'aide d'Aspose.PDF.
---

Pour les développeurs, de nombreux scénarios nécessitent de générer des fichiers PDF de manière programmatique. Vous pouvez avoir besoin de générer des rapports PDF et d'autres fichiers PDF de façon programmatique dans votre logiciel. Il est assez long et inefficace d'écrire votre propre code et vos fonctions à partir de zéro. Pour créer un fichier PDF avec Python, il existe une meilleure solution - **Aspose.PDF pour Python via .NET**.

## Comment créer un fichier PDF en utilisant Python

Pour créer un fichier PDF en utilisant Python, les étapes suivantes peuvent être utilisées.

1. Créez un objet de la classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)
1. Ajoutez un objet [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) à la collection [Pages](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) du document
1. Ajoutez un [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) à la collection [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) de la page
1. Enregistrez le document PDF résultant

```python

    import aspose.pdf as ap

    # Initialize document object
    document = ap.Document()
    # Add page
    page = document.pages.add()
    # Initialize textfragment object
    text_fragment = ap.text.TextFragment("Hello,world!")
    # Add text fragment to new page
    page.paragraphs.add(text_fragment)
    # Save updated PDF
    document.save("output.pdf")
```



