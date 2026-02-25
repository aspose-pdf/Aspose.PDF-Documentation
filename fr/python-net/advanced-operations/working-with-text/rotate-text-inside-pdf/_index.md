---
title: Faire pivoter le texte dans un PDF avec Python
linktitle: Faire pivoter le texte dans PDF
type: docs
weight: 50
url: /fr/python-net/rotate-text-inside-pdf/
description: Découvrez comment faire pivoter le texte à l'intérieur d'un document PDF en Python pour une mise en forme flexible des documents avec Aspose.PDF pour Python.
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment faire pivoter le texte dans un PDF avec Python
Abstract: L'article fournit un guide détaillé sur la façon de faire pivoter le texte à l'intérieur d'un document PDF en utilisant la bibliothèque Aspose.PDF pour Python via .NET. Il décrit l'utilisation de la propriété `Rotation` de la classe `TextFragment` pour réaliser la rotation du texte à différents angles, ce qui est utile dans de nombreux scénarios de génération de documents. Il démontre la création de fragments de texte avec des angles de rotation spécifiés et leur ajout à une page PDF à l'aide d'un `TextBuilder`. Il illustre comment ajouter des fragments de texte tournés à un `TextParagraph` puis ajouter le paragraphe à une page PDF. Il montre comment ajouter directement des fragments de texte tournés à la collection de paragraphes de la page. Explique la rotation d'un paragraphe entier contenant plusieurs fragments de texte.
---

La rotation des fragments de texte dans un document PDF à l'aide d'Aspose.PDF pour Python via .NET. Cela montre comment contrôler avec précision la position et la rotation d'éléments de texte individuels en combinant les classes 'TextFragment', 'TextState' et 'TextBuilder'. En réglant l'angle de rotation pour chaque fragment de texte, vous pouvez créer des mises en page visuellement dynamiques, comme des en-têtes diagonaux, des étiquettes verticales ou des annotations tournées.

## Faire pivoter les fragments de texte à l'aide de TextBuilder dans un PDF

Crée un fichier PDF nommé rotated_fragments.pdf contenant trois fragments de texte alignés horizontalement :

- le premier texte n'est pas tourné
- le deuxième est tourné à 45°
- le troisième est tourné à 90°

1. Créez un nouveau document PDF.
1. Insérez une nouvelle page pour accueillir le texte tourné.
1. Créez le premier fragment de texte – pas de rotation.
1. Créez le deuxième fragment de texte – rotation de 45°.
1. Créez le troisième fragment de texte – rotation de 90°.
1. Ajoutez des fragments de texte à l'aide de TextBuilder.
1. Enregistrez le document.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def rotate_text_inside_pdf_1(outfile):
    """
    Implement text rotation using TextFragment and TextBuilder.

    Demonstrates basic text rotation techniques by creating multiple text
    fragments with different rotation angles. Shows how to position and
    rotate individual text elements using TextBuilder for precise control.

    Args:
        outfile (str): Path where the PDF with rotated text will be saved.

    Returns:
        None: The function creates and saves a PDF file with rotated text fragments.

    Note:
        - Creates three text fragments with 0°, 45°, and 90° rotations
        - Uses Position class for precise text placement
        - Applies TimesNewRoman font with 12pt size
        - TextBuilder provides low-level control over text placement
        - Demonstrates individual fragment rotation capabilities

    Example:
        >>> rotate_text_inside_pdf_1("rotated_fragments.pdf")
        # Creates a PDF with text fragments at different rotation angles
    """

    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("main text")
        text_fragment_1.position = ap.text.Position(100, 600)
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Create rotated text fragment
        text_fragment_2 = ap.text.TextFragment("rotated text")
        text_fragment_2.position = ap.text.Position(200, 600)
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        text_fragment_2.text_state.rotation = 45
        # Create rotated text fragment
        text_fragment_3 = ap.text.TextFragment("rotated text")
        text_fragment_3.position = ap.text.Position(300, 600)
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        text_fragment_3.text_state.rotation = 90
        # create TextBuilder object
        builder = ap.text.TextBuilder(page)
        # Append the text fragment to the PDF page
        builder.append_text(text_fragment_1)
        builder.append_text(text_fragment_2)
        builder.append_text(text_fragment_3)

        # Save the document
        document.save(outfile)
```

## Faire pivoter des fragments de texte individuels à l'intérieur d'un paragraphe dans un PDF

Faire pivoter des fragments de texte individuels au sein d'un paragraphe. Cela montre comment construire un paragraphe multi-lignes (TextParagraph) contenant plusieurs fragments (TextFragment), chacun avec son propre angle de rotation. Cette technique est utile pour créer des documents visuellement riches qui combinent du texte orienté horizontalement et en diagonale — par exemple, des en-têtes stylisés, des diagrammes ou des légendes annotées.

Crée un PDF nommé rotated_paragraph_fragments.pdf contenant un paragraphe avec trois lignes de texte, chaque ligne étant tournée différemment :

- la première ligne est tournée à 45°
- la deuxième ligne reste horizontale (0°)
- la troisième ligne est tournée à -45°

1. Créez un nouveau document PDF.
1. Ajoutez une page vierge où le texte tourné apparaîtra.
1. Créez un TextParagraph.
1. Créez et configurez le premier fragment de texte – rotation de 45°.
1. Créez le deuxième fragment de texte – aucune rotation.
1. Créez le troisième fragment de texte – rotation de 45°.
1. Ajoutez les fragments de texte au paragraphe.
1. Ajoutez le paragraphe à la page en utilisant TextBuilder.
1. Enregistrez le document.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def rotate_text_inside_pdf_2(outfile):
    """
    Implement text rotation using TextParagraph and TextBuilder with rotated fragments.

    Demonstrates how to create multi-line paragraphs containing individually
    rotated text fragments. Shows the combination of paragraph structure
    with fragment-level rotation control.

    Args:
        outfile (str): Path where the PDF with rotated paragraph fragments will be saved.

    Returns:
        None: The function creates and saves a PDF file with a paragraph containing rotated fragments.

    Note:
        - Creates a TextParagraph containing multiple text fragments
        - Individual fragments have different rotations: 45°, 0°, and -45°
        - Uses append_line to structure fragments within the paragraph
        - Demonstrates mixed rotation within a single paragraph
        - TextBuilder handles paragraph-level placement and rendering

    Example:
        >>> rotate_text_inside_pdf_2("rotated_paragraph_fragments.pdf")
        # Creates a PDF with a paragraph containing individually rotated text fragments
    """

    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        paragraph = ap.text.TextParagraph()
        paragraph.position = ap.text.Position(200, 600)
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Set rotation
        text_fragment_1.text_state.rotation = 45
        # Create text fragment
        text_fragment_2 = ap.text.TextFragment("main text")
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Create text fragment
        text_fragment_3 = ap.text.TextFragment("another rotated text")
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Set rotation
        text_fragment_3.text_state.rotation = -45
        # Append the text fragments to the paragraph
        paragraph.append_line(text_fragment_1)
        paragraph.append_line(text_fragment_2)
        paragraph.append_line(text_fragment_3)
        # Create TextBuilder object
        text_builder = ap.text.TextBuilder(page)
        # Append the text paragraph to the PDF page
        text_builder.append_paragraph(paragraph)

        # Save the document
        document.save(outfile)
```

## Faire pivoter le texte en utilisant les paragraphes de page dans un PDF

Méthode simplifiée pour faire pivoter le texte à l'intérieur d'un PDF en utilisant Aspose.PDF pour Python via .NET.
Contrairement aux approches de bas niveau avec TextBuilder ou TextParagraph, cette méthode ajoute les fragments de texte tournés directement à la collection de paragraphes de la page (page.paragraphs). Elle est idéale pour les cas où vous avez besoin d'une rotation de texte basique mais ne requérez pas de positionnement précis ou de structuration de paragraphes. Cette approche simplifie la création de mise en page, gérant automatiquement le placement du texte sur la page tout en permettant le contrôle de la rotation individuelle du texte.

Génère un fichier nommé 'simple_rotated_text.pdf' contenant :

- un fragment de texte horizontal principal avec rotation 0°
- fragment tourné à 315°
- fragment tourné à 270°

1. Initialisez un nouveau document PDF.
1. Créez une page où le texte tourné sera placé.
1. Créez le premier fragment de texte - aucune rotation.
1. Créez le deuxième fragment de texte - rotation de 315°.
1. Créez le troisième fragment de texte - rotation de 270°.
1. Ajoutez des fragments de texte directement aux paragraphes de la page.
1. Enregistrez le document PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def rotate_text_inside_pdf_3(outfile):
    """
    Implement text rotation using TextFragment and Page.Paragraphs.

    Demonstrates a simplified approach to text rotation by adding rotated
    text fragments directly to the page's paragraph collection. Shows
    high-level text placement without TextBuilder complexity.

    Args:
        outfile (str): Path where the PDF with rotated text will be saved.

    Returns:
        None: The function creates and saves a PDF file with rotated text using page paragraphs.

    Note:
        - Uses Page.Paragraphs for direct text fragment addition
        - Creates fragments with 0°, 315°, and 270° rotations
        - Simpler approach compared to TextBuilder method
        - Demonstrates automatic layout with rotated text elements
        - Good for basic rotation without precise positioning needs

    Example:
        >>> rotate_text_inside_pdf_3("simple_rotated_text.pdf")
        # Creates a PDF with rotated text using the simplified page paragraphs approach
    """

    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("main text")
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Create text fragment
        text_fragment_2 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Set rotation
        text_fragment_2.text_state.rotation = 315
        # Create text fragment
        text_fragment_3 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Set rotation
        text_fragment_3.text_state.rotation = 270
        page.paragraphs.add(text_fragment_1)
        page.paragraphs.add(text_fragment_2)
        page.paragraphs.add(text_fragment_3)

        # Save the document
        document.save(outfile)
```

## Faire pivoter des paragraphes entiers dans un PDF

Notre bibliothèque montre une rotation avancée du texte au niveau du paragraphe dans un PDF. Contrairement à la rotation au niveau des fragments (où chaque morceau de texte est tourné individuellement), cette méthode fait pivoter des paragraphes entiers comme des blocs unifiés à différents angles.
Chaque paragraphe contient plusieurs fragments de texte stylisés, et le paragraphe complet est pivoté à des angles spécifiques — permettant des transformations de mise en page complexes et cohérentes.
Ceci est idéal pour les mises en page artistiques, les filigranes ou les PDF très design où des sections de texte entières doivent être orientées dans diverses directions.

Crée le fichier 'rotated_paragraphs.pdf', contenant quatre paragraphes entièrement stylisés et pivotés :

- chacun pivoté à un angle unique (45°, 135°, 225° et 315°)
- chaque paragraphe a trois lignes de texte avec des arrière-plans colorés, du soulignement et un style cohérent

1. Créez un nouveau document PDF.
1. Ajoutez une page vierge pour contenir les paragraphes pivotés.
1. Itérez pour créer plusieurs paragraphes.
1. Créez et positionnez le paragraphe.
1. Créez des fragments de texte avec mise en forme.
1. Appliquez la mise en forme du texte.
1. Ajoutez les fragments de texte au paragraphe.
1. Ajoutez le paragraphe à la page en utilisant TextBuilder.
1. Répétez pour les quatre rotations.
1. Enregistrez le document PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def rotate_text_inside_pdf_4(outfile):
    """
    Implement whole paragraph rotation using TextParagraph and TextBuilder.

    Demonstrates advanced text rotation by rotating entire paragraphs at
    different angles. Creates multiple styled paragraphs with comprehensive
    formatting and rotates each paragraph as a complete unit.

    Args:
        outfile (str): Path where the PDF with rotated paragraphs will be saved.

    Returns:
        None: The function creates and saves a PDF file with fully rotated paragraphs.

    Note:
        - Creates 4 paragraphs rotated at 45°, 135°, 225°, and 315°
        - Each paragraph contains multiple formatted text fragments
        - Applies comprehensive styling: colors, backgrounds, underlines
        - Demonstrates paragraph-level rotation vs. fragment-level rotation
        - Shows complex multi-line content with consistent rotation
        - Uses loop to create systematic rotation pattern

    Example:
        >>> rotate_text_inside_pdf_4("rotated_paragraphs.pdf")
        # Creates a PDF with complete paragraphs rotated at different angles
    """

    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        for i in range(4):
            paragraph = ap.text.TextParagraph()
            paragraph.position = ap.text.Position(200, 600)
            # Specify rotation
            paragraph.rotation = i * 90 + 45
            # Create text fragment
            text_fragment_1 = ap.text.TextFragment("Paragraph Text")
            # Create text fragment
            text_fragment_1.text_state.font_size = 12
            text_fragment_1.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
            text_fragment_1.text_state.background_color = ap.Color.light_gray
            text_fragment_1.text_state.foreground_color = ap.Color.blue
            # Create text fragment
            text_fragment_2 = ap.text.TextFragment("Second line of text")
            # Set text properties
            text_fragment_2.text_state.font_size = 12
            text_fragment_2.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
            text_fragment_2.text_state.background_color = ap.Color.light_gray
            text_fragment_2.text_state.foreground_color = ap.Color.blue
            # Create text fragment
            text_fragment_3 = ap.text.TextFragment("And some more text...")
            # Set text properties
            text_fragment_3.text_state.font_size = 12
            text_fragment_3.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
            text_fragment_3.text_state.background_color = ap.Color.light_gray
            text_fragment_3.text_state.foreground_color = ap.Color.blue
            text_fragment_3.text_state.underline = True
            paragraph.append_line(text_fragment_1)
            paragraph.append_line(text_fragment_2)
            paragraph.append_line(text_fragment_3)
            # Create TextBuilder object
            builder = ap.text.TextBuilder(page)
            # Append the text fragment to the PDF page
            builder.append_paragraph(paragraph)

        # Save the document
        document.save(outfile)
```
