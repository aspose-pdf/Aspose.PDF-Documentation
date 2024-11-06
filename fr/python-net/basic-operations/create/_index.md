---
title: Créer un document PDF par programmation
linktitle: Créer PDF
type: docs
weight: 10
url: fr/python-net/create-document/
description: Cette page décrit comment créer un document PDF à partir de zéro avec Aspose.PDF pour Python via la bibliothèque .NET.
---

Pour les développeurs, il existe de nombreux scénarios où il devient nécessaire de générer des fichiers PDF par programmation. Vous pouvez avoir besoin de générer des rapports PDF et d'autres fichiers PDF par programmation dans votre logiciel. Il est plutôt long et inefficace d'écrire votre propre code et vos fonctions à partir de zéro. Pour créer un fichier PDF avec Python, il existe une meilleure solution - **Aspose.PDF pour Python via .NET**.

## Comment créer un fichier PDF avec Python

Pour créer un fichier PDF avec Python, les étapes suivantes peuvent être utilisées.

1. Créez un objet de la classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)

1. Ajoutez un objet [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) à la collection [Pages](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) de l'objet Document
1. Ajoutez [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) à la collection de [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) de la page
1. Enregistrez le document PDF résultant

```python

    import aspose.pdf as ap

    # Initialiser l'objet document
    document = ap.Document()
    # Ajouter une page
    page = document.pages.add()
    # Initialiser l'objet textfragment
    text_fragment = ap.text.TextFragment("Hello,world!")
    # Ajouter le fragment de texte à la nouvelle page
    page.paragraphs.add(text_fragment)
    # Enregistrer le PDF mis à jour
    document.save("output.pdf")
```