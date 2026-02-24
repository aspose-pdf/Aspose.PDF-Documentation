---
title: Comparer des documents PDF
linktitle: Comparer PDF
type: docs
weight: 130
url: /fr/python-net/compare-pdf-documents/
description: Il est possible de comparer le contenu de documents PDF avec des marques d'annotation et une sortie côte à côte.
lastmod: "2025-05-12"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 
Abstract: 
---

## Manières de comparer des documents PDF

Lorsqu'on travaille avec des documents PDF, il arrive parfois de devoir comparer le contenu de deux documents afin d'identifier les différences. La bibliothèque Aspose.PDF pour Python via .NET fournit un ensemble d'outils puissants à cet effet. Dans cet article, nous explorerons comment comparer des documents PDF en utilisant quelques extraits de code simples.

La fonctionnalité de comparaison d'Aspose.PDF vous permet de comparer deux documents PDF page par page. Vous pouvez choisir de comparer soit des pages spécifiques, soit des documents entiers. Le document de comparaison résultant met en évidence les différences, facilitant l'identification des changements entre les deux fichiers.

Voici une liste des différentes manières de comparer des documents PDF en utilisant la bibliothèque Aspose.PDF pour Python via .NET :

1. **Comparaison de pages spécifiques** - Comparez les premières pages de deux documents PDF.
1. **Comparaison de documents entiers** - Comparez le contenu complet de deux documents PDF.
1. **Comparer les documents PDF graphiquement** :

- Comparez le PDF avec la méthode 'comparer.get_difference' - images individuelles où les changements sont marqués.
- Comparez le PDF avec la méthode 'comparer.compare_documents_to_pdf' - document PDF avec des images où les changements sont marqués.

## Comparaison de pages spécifiques

Le premier extrait de code montre comment comparer les premières pages de deux documents PDF en utilisant la classe SideBySidePdfComparer.

1. Initialisation du document.
1. Créez une fonction pour effectuer la comparaison.
1. Processus de comparaison :

- document1.pages[1] et document2.pages[1] : - ils spécifient la première page de chaque document pour la comparaison. Notez que l'indexation des pages commence à 1 dans Aspose.PDF.
- SideBySideComparisonOptions - cette classe permet de personnaliser le comportement de comparaison.
- additional_change_marks = True - active l'affichage de marqueurs de changement supplémentaires, mettant en évidence les différences qui pourraient être présentes sur d'autres pages, même si elles ne sont pas sur la page actuelle comparée.
- comparison_mode = ComparisonMode.IgnoreSpaces - définit le mode de comparaison pour ignorer les espaces dans le texte, en se concentrant uniquement sur les changements à l'intérieur des mots.

1. Le résultat de la comparaison est enregistré sous forme d'un nouveau fichier PDF nommé ComparingSpecificPages_out.pdf dans le répertoire data_dir spécifié.

```python

    import aspose.pdf as ap
    from aspose.pdf.comparison import SideBySidePdfComparer, SideBySideComparisonOptions, ComparisonMode

    def comparing_specific_pages():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf_documentcompare()

        # Open PDF documents
        document1 = ap.Document(data_dir + "ComparingSpecificPages1.pdf")
        document2 = ap.Document(data_dir + "ComparingSpecificPages2.pdf")

        # Compare
        options = SideBySideComparisonOptions()
        options.additional_change_marks = True
        options.comparison_mode = ComparisonMode.IgnoreSpaces

        # Perform comparison and save the result
        SideBySidePdfComparer.compare(document1.pages[1], document2.pages[1], data_dir + "ComparingSpecificPages_out.pdf", options)
```

## Comparaison de documents entiers

Le second extrait de code élargit le champ pour comparer le contenu complet de deux documents PDF.

```python

    import aspose.pdf as ap
    from aspose.pdf.comparison import SideBySidePdfComparer, SideBySideComparisonOptions, ComparisonMode

    def comparing_entire_documents():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf_documentcompare()

        # Open PDF documents
        document1 = ap.Document(data_dir + "ComparingEntireDocuments1.pdf")
        document2 = ap.Document(data_dir + "ComparingEntireDocuments2.pdf")

        # Compare
        options = SideBySideComparisonOptions()
        options.additional_change_marks = True
        options.comparison_mode = ComparisonMode.IgnoreSpaces

        # Perform comparison and save the result
        SideBySidePdfComparer.compare(document1, document2, data_dir + "ComparingEntireDocuments_out.pdf", options)
```

Le code fourni démontre la comparaison de deux documents PDF en utilisant Aspose.PDF pour Python via .NET. Il utilise la classe SideBySidePdfComparer pour effectuer une comparaison page par page, générant un nouveau PDF qui affiche les différences côte à côte. La comparaison est configurée avec SideBySideComparisonOptions, où additional_change_marks est fixé à True pour mettre en évidence les changements non seulement sur la page actuelle mais aussi sur d'autres pages, et où comparison_mode est réglé sur IgnoreSpaces afin de se concentrer sur les différences de contenu significatives en ignorant les variations d'espaces blancs.

## Comparer en utilisant GraphicalPdfComparer

Lors de la collaboration sur des documents, surtout en milieu professionnel, vous vous retrouvez souvent avec plusieurs versions du même fichier.
Le code fourni montre comment comparer visuellement des pages spécifiques de deux documents PDF en utilisant Aspose.PDF pour Python via .NET. En utilisant la classe `GraphicalPdfComparer`, il met en évidence les différences entre les premières pages des deux PDF et génère des images correspondantes pour représenter ces différences.

Vous pouvez définir les propriétés de classe suivantes :

- Resolution - résolution en unités DPI pour les images de sortie, ainsi que pour les images générées lors de la comparaison.
- Color - la couleur des marques de changement.
- Threshold - seuil de changement en pourcentage. La valeur par défaut est zéro. Définir une valeur différente de zéro vous permet d'ignorer les changements graphiques qui ne sont pas significatifs pour vous.

Avec Aspose.PDF pour Python via .NET, il est possible de comparer des documents et des pages et de produire le résultat de la comparaison dans un document PDF ou un fichier image.

La classe `GraphicalPdfComparer` possède une méthode qui vous permet d'obtenir les différences d'images de page sous une forme adaptée à un traitement ultérieur : `get_difference(document1.pages[1], document2.pages[1])`.

Cette méthode renvoie un objet du type `images_difference`, qui contient une image de la première page comparée et un tableau de différences.

L'objet `images_difference` vous permet de générer une image différente et d'obtenir une image de la deuxième page comparée en appliquant un tableau de différences à l'image originale. Pour cela, utilisez les méthodes `difference_to_image` et `get_destination_image`.

### Comparer le PDF avec la méthode Get Difference

Le code fourni définit une méthode `get_difference` qui compare deux documents PDF et génère des représentations visuelles des différences entre eux.

Cette méthode compare les premières pages de deux fichiers PDF et génère deux images PNG :

- Une image met en évidence les différences entre les pages en rouge.
- L'autre image est une représentation visuelle de la page PDF de destination (deuxième).

Ce processus peut être utile pour comparer visuellement les changements ou les différences entre deux versions d'un document.

```python

    import aspose.pdf as ap
    from aspose.pdf.comparison import GraphicalPdfComparer

    def compare_pdf_with_get_difference_method():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf_documentcompare()

        # Open PDF documents
        document1 = ap.Document(data_dir + "ComparePDFWithGetDifferenceMethod1.pdf")
        document2 = ap.Document(data_dir + "ComparePDFWithGetDifferenceMethod2.pdf")

        # Create comparer
        comparer = GraphicalPdfComparer()

        # Compare specific pages
        images_difference = comparer.get_difference(document1.pages[1], document2.pages[1])

        # Get image showing differences in red over a white background
        diff_img = images_difference.difference_to_image(ap.Color.red, ap.Color.white)
        diff_img.save(data_dir + "ComparePDFWithGetDifferenceMethodDiffPngFilePath_out.png")

        # Get the second image representing the destination page
        dest_img = images_difference.get_destination_image()
        dest_img.save(data_dir + "ComparePDFWithGetDifferenceMethodDestPngFilePath_out.png")
```

### Comparer le PDF avec la méthode CompareDocumentsToPdf

L'extrait de code fourni utilise la méthode `compare_documents_to_pdf`, qui compare deux documents et génère un rapport PDF des résultats de la comparaison.

```python

    import aspose.pdf as ap
    from aspose.pdf.comparison import GraphicalPdfComparer
    from aspose.pdf.devices import Resolution

    def compare_pdf_with_compare_documents_to_pdf_method():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf_documentcompare()

        # Open PDF documents
        document1 = ap.Document(data_dir + "ComparePDFWithCompareDocumentsToPdfMethod1.pdf")
        document2 = ap.Document(data_dir + "ComparePDFWithCompareDocumentsToPdfMethod2.pdf")

        # Create comparer and set options
        comparer = GraphicalPdfComparer()
        comparer.threshold = 3.0
        comparer.color = ap.Color.blue
        comparer.resolution = Resolution(300)

        # Compare and output to a PDF file
        comparer.compare_documents_to_pdf(document1, document2, data_dir + "compareDocumentsToPdf_out.pdf")
```

Cet exemple montre comment effectuer une comparaison graphique de deux documents PDF complets en utilisant Aspose.PDF pour Python via .NET. En exploitant la classe `GraphicalPdfComparer`, il génère un nouveau fichier PDF qui met visuellement en évidence les différences entre les documents.

- La propriété seuil est définie à 3.0, ce qui signifie que les petites différences en dessous de ce pourcentage sont ignorées lors de la comparaison, en se concentrant sur les changements plus significatifs.
- Les différences sont marquées en bleu en définissant la propriété couleur sur ap.Color.blue, permettant une distinction visuelle claire.
- La comparaison est effectuée à une résolution de 300 DPI en définissant la propriété résolution, garantissant une sortie détaillée et claire.

La méthode `compare_documents_to_pdf` compare toutes les pages des deux documents et envoie le résultat vers un nouveau fichier PDF, compareDocumentsToPdf_out.pdf, avec les différences mises en évidence visuellement.

