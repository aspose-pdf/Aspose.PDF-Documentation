---
title: Utilisation de FloatingBox pour la génération de texte avec Python
linktitle: Utilisation de FloatingBox
type: docs
weight: 30
url: /fr/python-net/floating-box/
description: Cette page explique comment formater le texte à l'intérieur d'une boîte flottante.
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: L'outil FloatingBox pour la génération de texte
Abstract: Cet article fournit un guide complet sur l'utilisation de l'outil FloatingBox dans Aspose.PDF pour Python, qui permet aux développeurs de placer du texte et d'autres contenus dans des conteneurs mobiles et stylisés sur les pages PDF. Il couvre à la fois les utilisations de base et avancées, démontrant comment créer des boîtes flottantes, appliquer des bordures et des couleurs d'arrière-plan, contrôler les mises en page à plusieurs colonnes, gérer le positionnement des paragraphes et aligner les boîtes verticalement et horizontalement. L'article met également en avant des fonctionnalités clés telles que la découpe du texte, la répétition du contenu sur plusieurs pages, le positionnement absolu et un contrôle amélioré de la mise en page, permettant une personnalisation précise du contenu PDF. Grâce à des exemples de code pratiques, les lecteurs apprennent à créer des PDF visuellement attrayants et bien structurés qui exploitent pleinement les capacités du conteneur FloatingBox.
---

## Bases de l'utilisation de l'outil FloatingBox

L'outil [`FloatingBox`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/) est un conteneur spécialisé pour placer du texte et d'autres contenus sur une page PDF. Sa principale fonctionnalité est la découpe du texte lorsque le contenu dépasse les limites de la boîte. Créez et ajoutez un `FloatingBox` à un [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) à l'aide d'Aspose.PDF pour Python. Un `FloatingBox` agit comme un conteneur de texte mobile, offrant un meilleur contrôle sur le positionnement de la mise en page, les bordures et le style par rapport aux paragraphes de texte classiques.

1. Créez un nouveau [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Ajoutez une [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) au document.
1. Créez un [`FloatingBox`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/).
1. Définissez la bordure de la boîte en utilisant [`BorderInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderinfo/) et [`BorderSide`](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderside/).
1. Contrôlez la répétition de la boîte avec la propriété [`is_need_repeating`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties).
1. Ajoutez du contenu texte en utilisant [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/).
1. Ajoutez le `FloatingBox` à la [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Enregistrez le document PDF final en utilisant [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

import math
import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def create_and_add_floating_box(outfile):
    """
    Create and add a basic floating box to a PDF document.

    Demonstrates the fundamental usage of FloatingBox to create a bordered
    text container with Lorem ipsum content. Shows basic box creation,
    styling, and text content addition.

    Args:
        outfile (str): Path where the PDF with floating box will be saved.

    Returns:
        None: The function creates and saves a PDF file with a floating box.

    Note:
        - Creates a FloatingBox with dimensions 400x30
        - Applies dark green border with 1.5 width
        - Sets is_need_repeating to False for single occurrence
        - Contains Lorem ipsum text fragment
        - Demonstrates basic floating box functionality

    Example:
        >>> create_and_add_floating_box("basic_floating_box.pdf")
        # Creates a PDF with a simple bordered floating text box
    """

    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()
        # Create and fill box
        box = ap.FloatingBox(400, 30)
        box.border = ap.BorderInfo(ap.BorderSide.ALL, 1.5, ap.Color.dark_green)
        box.is_need_repeating = False
        phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi."
        box.paragraphs.add(ap.text.TextFragment(phrase))
        # Add box
        page.paragraphs.add(box)
        document.save(outfile)
```  

Dans l'exemple ci-dessus, nous créons un FloatingBox avec une largeur de 400 pt et une hauteur de 30 pt.
De plus, dans cet exemple, plus de texte a été créé intentionnellement que ce qui pouvait tenir dans la taille donnée.
En conséquence, le texte a été coupé.

![Image 1](image01.png)

La propriété [`is_need_repeating`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) avec la valeur `False` limite le texte à une seule page.

Si nous définissons cette propriété sur `True`, le texte s'écoulera vers les pages suivantes à la même position.

![Image 2](image02.png)

## Fonctionnalités avancées de FloatingBox

### Support multi-colonnes

#### Mise en page multi-colonnes (cas simple)

`FloatingBox` prend en charge la mise en page multi-colonnes. Pour créer une telle mise en page, vous devez définir les valeurs des propriétés [`ColumnInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/columninfo/).

* `column_widths` est une chaîne avec l'énumération des largeurs en pt.
* `column_spacing` est une chaîne avec la largeur de l'espace entre les colonnes.
* `column_count` est le nombre de colonnes.

```python

import math
import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def multi_column_layout(outfile):
    """
    Create a multi-column layout using FloatingBox.

    Demonstrates advanced layout capabilities by creating a three-column
    text layout within a floating box. Shows dynamic width calculation
    and column spacing configuration.

    Args:
        outfile (str): Path where the PDF with multi-column layout will be saved.

    Returns:
        None: The function creates and saves a PDF file with multi-column text.

    Note:
        - Creates 3 equal-width columns with 10-unit spacing
        - Calculates column width based on page margins and spacing
        - Uses is_need_repeating for content continuation across columns
        - Adds multiple Lorem ipsum paragraphs for column demonstration
        - Automatically distributes content across columns

    Example:
        >>> multi_column_layout("multi_column.pdf")
        # Creates a PDF with text arranged in three columns
    """
    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()
        # Set margin settings
        page.page_info.margin = ap.MarginInfo(36, 18, 36, 18)
        column_count = 3
        spacing = 10
        width = (
            page.page_info.width
            - page.page_info.margin.left
            - page.page_info.margin.right
            - (column_count - 1) * spacing
        )
        column_width = width / 3
        # Create FloatingBox
        box = ap.FloatingBox()
        box.is_need_repeating = True
        box.column_info.column_widths = f"{column_width} {column_width} {column_width}"
        box.column_info.column_spacing = f"{spacing}"
        box.column_info.column_count = 3
        phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi."
        paragraphs = [
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
        ]
        for paragraph in paragraphs:
            box.paragraphs.add(ap.text.TextFragment(paragraph))
        # Add a box to a page
        page.paragraphs.add(box)
        # Save PDF document
        document.save(outfile)
```

Nous avons utilisé la bibliothèque supplémentaire LoremNET dans l'exemple ci-dessus et créé 20 paragraphes. Ces paragraphes ont été divisés en trois colonnes et ont rempli les pages suivantes jusqu'à épuisement du texte.

#### Mise en page multi-colonnes avec démarrage de colonne forcé

Nous ferons la même chose avec l'exemple suivant comme le précédent. La différence est que nous avons créé 3 paragraphes. Nous pouvons forcer FloatingBox à rendre chaque paragraphe dans une nouvelle colonne. Pour cela, nous devons définir `is_first_paragraph_in_column` lors de l'ajout de texte à l'objet FloatingBox.

```python

import math
import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def multi_column_layout_2(outfile):
    """
    Create a multi-column layout with paragraph column control.

    Demonstrates advanced multi-column layout with explicit control over
    paragraph positioning within columns. Uses is_first_paragraph_in_column
    to control text flow and column breaks.

    Args:
        outfile (str): Path where the PDF with controlled multi-column layout will be saved.

    Returns:
        None: The function creates and saves a PDF file with controlled column text.

    Note:
        - Creates 3 equal-width columns with 10-unit spacing
        - Uses is_first_paragraph_in_column for explicit column control
        - Calculates column width dynamically based on page dimensions
        - Demonstrates precise paragraph positioning within columns
        - Shows advanced column layout management techniques

    Example:
        >>> multi_column_layout_2("controlled_columns.pdf")
        # Creates a PDF with precisely controlled multi-column text flow
    """

    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()
        # Set margin settings
        page.page_info.margin = ap.MarginInfo(36, 18, 36, 18)
        column_count = 3
        spacing = 10
        width = (
            page.page_info.width
            - page.page_info.margin.left
            - page.page_info.margin.right
            - (column_count - 1) * spacing
        )
        column_width = width / 3
        # Create FloatingBox
        box = ap.FloatingBox()
        box.is_need_repeating = True
        box.column_info.column_widths = f"{column_width} {column_width} {column_width}"
        box.column_info.column_spacing = f"{spacing}"
        box.column_info.column_count = 3
        phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi."
        paragraphs = [
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
        ]
        for paragraph in paragraphs:
            text = ap.text.TextFragment(paragraph)
            text.is_first_paragraph_in_column = True
            box.paragraphs.add(text)
        # Add a box to a page
        page.paragraphs.add(box)
        # Save PDF document
        document.save(outfile)
```

### Support d'arrière-plan

Appliquez une couleur d'arrière-plan à un FloatingBox dans un document PDF en utilisant Aspose.PDF pour Python via .NET.
Un `FloatingBox` est un conteneur pour du texte ou d'autres éléments, et en attribuant un [`Color`](https://reference.aspose.com/pdf/python-net/aspose.pdf/color/) comme couleur d'arrière-plan, vous pouvez faire ressortir visuellement le contenu — utile pour les en-têtes, les surlignages ou les sections stylisées.

Cet extrait de code montre comment créer une boîte de texte vert clair simple avec du contenu d'exemple.

```python

import math
import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def background_support(outfile):
    """
    Demonstrate FloatingBox background color support.

    Shows how to apply background colors to floating boxes to create
    visually distinct text containers. Demonstrates basic styling
    capabilities for enhanced visual presentation.

    Args:
        outfile (str): Path where the PDF with colored background box will be saved.

    Returns:
        None: The function creates and saves a PDF file with a colored floating box.

    Note:
        - Applies light green background color to the floating box
        - Creates a 400x30 box with sample text content
        - Sets is_need_repeating to False for single occurrence
        - Demonstrates visual styling options for floating boxes
        - Shows how background colors enhance text presentation

    Example:
        >>> background_support("colored_background.pdf")
        # Creates a PDF with a light green background floating box
    """

    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()
        # Create and fill box
        box = ap.FloatingBox(400, 30)
        box.background_color = ap.Color.light_green
        box.is_need_repeating = False
        box.paragraphs.add(ap.text.TextFragment("text example"))
        # Add box
        page.paragraphs.add(box)
        # Save PDF document
        document.save(outfile)
```

### Support du positionnement

L'emplacement du FloatingBox sur la page générée est déterminé par les propriétés `positioning_mode`, `left`, `top`.
Lorsque la valeur de `positioning_mode` est

* [`ParagraphPositioningMode.DEFAULT`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paragraphpositioningmode/) (valeur par défaut)

L'emplacement est déterminé par les éléments placés précédemment ; ajouter un élément influence l'emplacement des éléments suivants. Si [`Left`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) ou [`Top`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) sont différents de zéro, ils sont également pris en compte, mais la logique combinée peut ne pas être évidente.

* [`ParagraphPositioningMode.ABSOLUTE`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paragraphpositioningmode/)

L'emplacement est spécifié par les valeurs `Left` et `Top` ; il ne dépend pas des éléments précédents et n'affecte pas l'emplacement des éléments suivants.

```python

import math
import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def offset_support(outfile):
    """
    Demonstrate FloatingBox positioning and offset support.

    Shows how to position floating boxes at specific coordinates using
    absolute positioning mode. Demonstrates integration of floating boxes
    with regular text content and precise layout control.

    Args:
        outfile (str): Path where the PDF with positioned floating box will be saved.

    Returns:
        None: The function creates and saves a PDF file with positioned floating box.

    Note:
        - Uses absolute positioning mode for precise box placement
        - Sets box position to top=45, left=15 coordinates
        - Creates bordered box with dark green border
        - Integrates floating box with regular text paragraphs
        - Demonstrates layered content with mixed positioning

    Example:
        >>> offset_support("positioned_box.pdf")
        # Creates a PDF with a floating box at specific coordinates
    """

    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()
        # Create and fill box
        box = ap.FloatingBox(400, 30)
        box.top = 45
        box.left = 15
        box.positioning_mode = ap.ParagraphPositioningMode.ABSOLUTE
        box.border = ap.BorderInfo(ap.BorderSide.ALL, 1.5, ap.Color.dark_green)
        box.paragraphs.add(ap.text.TextFragment("text example 1"))
        page.paragraphs.add(ap.text.TextFragment("text example 2"))
        # Add the box to the page
        page.paragraphs.add(box)
        page.paragraphs.add(ap.text.TextFragment("text example 3"))
        document.save(outfile)
```

### Aligner les boîtes flottantes avec un alignement vertical et horizontal dans le PDF

Alignez les éléments `FloatingBox` au sein d'une page PDF en utilisant différentes options [`VerticalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/verticalalignment/) et [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) dans Aspose.PDF pour Python via .NET. Cela montre comment contrôler le positionnement de la mise en page (haut, centre, bas, gauche, droite) pour obtenir un alignement visuel précis des conteneurs flottants. Chaque boîte flottante se voit attribuer une position distincte afin de démontrer la flexibilité d'alignement pour la mise en page, le placement des en-têtes/pieds de page ou des annotations latérales.

1. Créez un nouveau document PDF.
1. Ajoutez une page au document.
1. Créez la première FloatingBox (alignement bas‑droite).
1. Créez la deuxième FloatingBox (alignement centre‑droite).
1. Créez la troisième FloatingBox (alignement haut‑droite).
1. Enregistrez le document.

```python

import math
import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def align_text_to_float(outfile):
    """
    Demonstrate text alignment options for FloatingBox elements.

    Shows different vertical and horizontal alignment options for floating
    boxes. Creates multiple boxes with different alignment settings to
    demonstrate positioning flexibility.

    Args:
        outfile (str): Path where the PDF with aligned floating boxes will be saved.

    Returns:
        None: The function creates and saves a PDF file with variously aligned boxes.

    Note:
        - Creates three 100x100 floating boxes with different alignments
        - First box: bottom-right alignment
        - Second box: center-right alignment
        - Third box: top-right alignment
        - All boxes have blue borders for visual distinction
        - Demonstrates comprehensive alignment control options

    Example:
        >>> align_text_to_float("aligned_boxes.pdf")
        # Creates a PDF with floating boxes in different alignment positions
    """
    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()

        # Create float box
        float_box = ap.FloatingBox(100, 100)
        # Set settings to float box
        float_box.vertical_alignment = ap.VerticalAlignment.BOTTOM
        float_box.horizontal_alignment = ap.HorizontalAlignment.RIGHT
        float_box.paragraphs.add(ap.text.TextFragment("FloatingBox_bottom"))
        float_box.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.blue)
        # Add float box
        page.paragraphs.add(float_box)

        # Create float box
        float_box_2 = ap.FloatingBox(100, 100)
        # Set settings to float box
        float_box_2.vertical_alignment = ap.VerticalAlignment.CENTER
        float_box_2.horizontal_alignment = ap.HorizontalAlignment.RIGHT
        float_box_2.paragraphs.add(ap.text.TextFragment("FloatingBox_center"))
        float_box_2.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.blue)
        # Add float box
        page.paragraphs.add(float_box_2)

        # Create float box
        float_box_3 = ap.FloatingBox(100, 100)
        # Set settings to float box
        float_box_3.vertical_alignment = ap.VerticalAlignment.TOP
        float_box_3.horizontal_alignment = ap.HorizontalAlignment.RIGHT
        float_box_3.paragraphs.add(ap.text.TextFragment("FloatingBox_top"))
        float_box_3.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.blue)
        # Add float box
        page.paragraphs.add(float_box_3)

        # Save the document
        document.save(outfile)
```
