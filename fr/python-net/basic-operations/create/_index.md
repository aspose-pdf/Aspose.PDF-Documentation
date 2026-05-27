---
title: Créer un document PDF de façon programmatique
linktitle: Créer un PDF
type: docs
weight: 10
url: /fr/python-net/create-document/
description: Cette page décrit comment créer un document PDF à partir de zéro avec la bibliothèque Aspose.PDF for Python via .NET.
TechArticle: true
AlternativeHeadline: Générer des fichiers PDF avec Aspose.PDF for Python
Abstract: Dans le développement logiciel, la génération de fichiers PDF de manière programmatique est une exigence courante, notamment pour créer des rapports et d’autres documents. Écrire du code personnalisé pour cette tâche peut être inefficace et chronophage. À la place, les développeurs peuvent utiliser **Aspose.PDF for Python via .NET**, une solution robuste pour créer des fichiers PDF en Python. Le processus consiste à créer un objet `Document`, ajouter un objet `Page` à la collection `Pages` du document, insérer un `TextFragment` dans la collection `paragraphs` de la page, puis enregistrer le document. Un extrait de code Python d’exemple montre ces étapes, illustrant la facilité avec laquelle des fichiers PDF peuvent être générés à l’aide d’Aspose.PDF.
---

Pour les développeurs, de nombreux scénarios nécessitent de générer des fichiers PDF de manière programmatique. Vous pouvez avoir besoin de générer des rapports PDF et d'autres fichiers PDF dans votre logiciel. Il est assez long et inefficace d'écrire votre propre code et vos fonctions à partir de zéro. Pour créer un fichier PDF avec Python, il existe une meilleure solution - **Aspose.PDF for Python via .NET**.

## Comment créer un fichier PDF avec Python

Pour créer un fichier PDF avec Python, les étapes suivantes peuvent être utilisées.

1. Créer un objet de [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) class
1. Ajouter un [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) objet à la [Pages](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) collection de l'objet Document
1. Ajouter [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) à [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) collection de la page
1. Enregistrer le document PDF résultant

```python
import aspose.pdf as ap

# Initialize document object
document = ap.Document()
# Add page
page = document.pages.add()
# Add text to new page
page.paragraphs.add(ap.text.TextFragment("Hello World!"))
# Define output file path
output_pdf = "output.pdf"
# Save updated PDF
output_pdf = "output.pdf"
document.save(output_pdf)
```
