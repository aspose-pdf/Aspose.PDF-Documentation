---
title: Comparer des documents PDF en Python
linktitle: Comparer PDF
type: docs
weight: 130
url: /fr/python-net/compare-pdf-documents/
description: Apprenez comment comparer des documents PDF en Python en utilisant une sortie de différence côte à côte et graphique avec Aspose.PDF for Python via .NET.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comparer les pages PDF et les documents complets avec une sortie de différence visuelle en Python
Abstract: Cet article explique comment comparer des documents PDF dans Aspose.PDF for Python via .NET. Apprenez comment comparer des pages spécifiques ou des fichiers PDF entiers avec une sortie côte à côte, et comment utiliser des méthodes de comparaison graphiques pour générer des rapports de différences basés sur des images ou sur des PDF.
---

## Méthodes de comparaison de documents PDF

Lorsqu’on travaille avec des documents PDF, il arrive qu’on doive comparer le contenu de deux documents afin d’identifier les différences. La bibliothèque Aspose.PDF for Python via .NET offre un ensemble d’outils puissant à cet effet. Dans cet article, nous explorerons comment comparer des documents PDF en utilisant quelques extraits de code simples.

Utilisez la comparaison côte à côte lorsque vous souhaitez une sortie PDF qui met en évidence les changements de texte et de mise en page entre les pages. Utilisez la comparaison graphique lorsque vous avez besoin d'une détection de différences basée sur l'image pour les flux de travail d'examen visuel, les vérifications de régression ou les rapports de comparaison de PDF.

La fonctionnalité de comparaison dans Aspose.PDF vous permet de comparer deux documents PDF page par page. Vous pouvez choisir de comparer soit des pages spécifiques, soit des documents entiers. Le document de comparaison résultant met en évidence les différences, ce qui facilite l'identification des modifications entre les deux fichiers.

Voici une liste des méthodes possibles pour comparer des documents PDF en utilisant la bibliothèque Aspose.PDF for Python via .NET :

1. **Comparaison de pages spécifiques** - Comparez les premières pages de deux documents PDF.
1. **Comparaison de documents entiers** - Comparez le contenu complet de deux documents PDF.
1. **Comparer les documents PDF graphiquement** :

- Comparez le PDF avec la méthode 'comparer.get_difference' - images individuelles où les modifications sont marquées.
- Comparez le PDF avec la méthode 'comparer.compare_documents_to_pdf' - document PDF avec images où les modifications sont marquées.

## Comparer des pages spécifiques

Le premier extrait de code montre comment comparer les premières pages de deux documents PDF en utilisant la classe SideBySidePdfComparer.

1. Initialisation du document.
1. Créer une fonction pour effectuer la comparaison.
1. Processus de comparaison :

- document1.pages[1] et document2.pages[1] : - ils spécifient la première page de chaque document pour la comparaison. Notez que l’indexation des pages commence à 1 dans Aspose.PDF.
- SideBySideComparisonOptions - cette classe permet de personnaliser le comportement de la comparaison.
- additional_change_marks = True - active l’affichage de marques de changement supplémentaires, mettant en évidence les différences qui pourraient être présentes sur d’autres pages, même si elles ne sont pas sur la page actuelle comparée.
- comparison_mode = ComparisonMode.IgnoreSpaces - définit le mode de comparaison pour ignorer les espaces dans le texte, en se concentrant uniquement sur les changements à l'intérieur des mots.

1. Le résultat de la comparaison est enregistré sous forme d'un nouveau fichier PDF nommé ComparingSpecificPages_out.pdf dans le répertoire data_dir spécifié.

```python
import aspose.pdf as ap
import sys
from os import path

def comparing_specific_pages(infile1, infile2, outfile):
    # Open PDF documents
    document_1 = ap.Document(infile1)
    document_2 = ap.Document(infile2)

    # Compare
    options = ap.comparison.SideBySideComparisonOptions()
    options.additional_change_marks = True
    options.comparison_mode = ap.comparison.ComparisonMode.IGNORE_SPACES

    # Perform comparison and save the result
    ap.comparison.SideBySidePdfComparer.compare(
        document_1.pages[1], document_2.pages[1], outfile, options
    )
```

## Comparer l'intégralité des documents

Le deuxième extrait de code élargit la portée pour comparer l'intégralité du contenu de deux documents PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def comparing_entire_documents(infile1, infile2, outfile):
    # Open PDF documents
    document_1 = ap.Document(infile1)
    document_2 = ap.Document(infile2)

    # Compare
    options = ap.comparison.SideBySideComparisonOptions()
    options.additional_change_marks = True
    options.comparison_mode = ap.comparison.ComparisonMode.IGNORE_SPACES

    # Perform comparison and save the result
    ap.comparison.SideBySidePdfComparer.compare(
        document_1, document_2, outfile, options
    )
```

Le code fourni montre la comparaison de deux documents PDF à l'aide d'Aspose.PDF for Python via .NET. Il utilise la classe SideBySidePdfComparer pour effectuer une comparaison page par page, en générant un nouveau PDF qui affiche les différences côte à côte. La comparaison est configurée avec SideBySideComparisonOptions, où additional_change_marks est définie sur True afin de mettre en évidence les changements non seulement sur la page actuelle mais aussi sur les autres pages, et comparison_mode est défini sur IgnoreSpaces pour se concentrer sur les différences de contenu significatif en ignorant les variations d'espaces.

## Comparer à l'aide de GraphicalPdfComparer

Lorsque vous collaborez sur des documents, en particulier dans des environnements professionnels, vous vous retrouvez souvent avec plusieurs versions du même fichier.
Le code fourni démontre comment comparer visuellement des pages spécifiques de deux documents PDF en utilisant Aspose.PDF for Python via .NET. En utilisant le `GraphicalPdfComparer` classe, elle met en évidence les différences entre les premières pages des deux PDFs et génère des images correspondantes pour représenter ces différences.

Vous pouvez définir les propriétés de classe suivantes :

- Resolution - résolution en unités DPI pour les images de sortie, ainsi que pour les images générées pendant la comparaison.
- Color - la couleur des marques de modification.
- Seuil - modifiez le seuil en pourcentage. La valeur par défaut est zéro. Définir une valeur autre que zéro vous permet d'ignorer les modifications graphiques qui sont insignifiantes pour vous.

Avec Aspose.PDF for Python via .NET, il est possible de comparer des documents et des pages et de générer le résultat de la comparaison dans un document PDF ou un fichier image.

Le `GraphicalPdfComparer` la classe possède une méthode qui vous permet d'obtenir les différences d'images de page sous une forme adaptée à un traitement ultérieur : `get_difference(document1.pages[1], document2.pages[1])`.

Cette méthode renvoie un objet de `images_difference` type, qui contient une image de la première page comparée et un tableau de différences.

Le `images_difference` l'objet vous permet de générer une image différente et d'obtenir une image de la deuxième page comparée en appliquant un tableau de différences à l'image originale. Pour ce faire, utilisez le `difference_to_image` et `get_destination_image` méthodes.

### Comparer le PDF avec la méthode Get Difference

Le code fourni définit une méthode `get_difference` qui compare deux documents PDF et génère des représentations visuelles des différences entre eux.

Cette méthode compare les premières pages de deux fichiers PDF et génère deux images PNG :

- Une image met en évidence les différences entre les pages en rouge.
- L'autre image est une représentation visuelle de la page PDF de destination (deuxième).

Ce processus peut être utile pour comparer visuellement les changements ou les différences entre deux versions d'un document.

```python
import aspose.pdf as ap
import sys
from os import path

def compare_pdf_with_get_difference_method(infile1, infile2, outfile1, outfile2):
    # Open PDF documents
    document1 = ap.Document(infile1)
    document2 = ap.Document(infile2)

    # Create comparer
    comparer = ap.comparison.GraphicalPdfComparer()

    # Compare specific pages
    images_difference = comparer.get_difference(document1.pages[1], document2.pages[1])

    # Get image showing differences in red over a white background
    diff_img = images_difference.difference_to_image(ap.Color.red, ap.Color.white)
    diff_img.save(outfile1)

    # Get the second image representing the destination page
    dest_img = images_difference.get_destination_image()
    dest_img.save(outfile2)
```

### Comparer le PDF avec la méthode CompareDocumentsToPdf

Le fragment de code fourni utilise le `compare_documents_to_pdf` méthode, qui compare deux documents et génère un rapport PDF des résultats de la comparaison.

```python
import aspose.pdf as ap
import sys
from os import path

def compare_pdf_with_compare_documents_to_pdf_method(infile1, infile2, outfile):
    # Open PDF documents
    document_1 = ap.Document(infile1)
    document_2 = ap.Document(infile2)

    # Create comparer and set options
    pdf_comparer = ap.comparison.GraphicalPdfComparer()
    pdf_comparer.threshold = 3.0
    pdf_comparer.color = ap.Color.blue
    pdf_comparer.resolution = ap.devices.Resolution(300)

    # Compare and output to a PDF file
    pdf_comparer.compare_documents_to_pdf(document_1, document_2, outfile)
```

Cet exemple montre comment effectuer une comparaison graphique de deux documents PDF complets en utilisant Aspose.PDF for Python via .NET. En tirant parti du `GraphicalPdfComparer` classe, il génère un nouveau fichier PDF qui met visuellement en évidence les différences entre les documents.

- La propriété de seuil est définie à 3,0, ce qui signifie que les différences mineures en dessous de ce pourcentage sont ignorées lors de la comparaison, en se concentrant sur les changements plus significatifs.
- Les différences sont marquées en bleu en réglant la propriété color sur ap.Color.blue, ce qui permet une distinction visuelle claire.
- La comparaison est effectuée à une résolution de 300 DPI en réglant la propriété de résolution, garantissant une sortie détaillée et claire.

Le `compare_documents_to_pdf` La méthode compare toutes les pages des deux documents et génère le résultat dans un nouveau fichier PDF, compareDocumentsToPdf_out.pdf, avec les différences mises en évidence visuellement.

## Sujets associés

- [Opérations PDF avancées en Python](/pdf/fr/python-net/advanced-operations/)
- [Travailler avec des documents PDF en Python](/pdf/fr/python-net/working-with-documents/)
- [Travailler avec les pages PDF en Python](/pdf/fr/python-net/working-with-pages/)
- [Travailler avec le texte PDF en Python](/pdf/fr/python-net/working-with-text/)
