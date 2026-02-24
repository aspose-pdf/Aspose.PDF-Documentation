---
title: Mise en forme du texte dans un PDF avec Python
linktitle: Mise en forme du texte dans un PDF
type: docs
weight: 70
url: /fr/python-net/text-formatting-inside-pdf/
description: Explorez les options de mise en forme du texte dans les fichiers PDF en Python en utilisant Aspose.PDF pour une stylisation personnalisée des documents.
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment modifier le texte dans un PDF avec Python
Abstract: Cet article fournit un guide complet sur diverses techniques de mise en forme du texte dans les documents PDF à l'aide d'Aspose.PDF pour Python via .NET. Il couvre un éventail de fonctionnalités, notamment l'ajout d'indentation de ligne, la création de bordures de texte, le soulignement du texte et l'ajout de texte barré, entre autres.
---

## Espacement des lignes et des caractères

### Utilisation de l'espacement des lignes

#### Comment formater le texte avec un espacement de ligne personnalisé en Python - Cas simple

Aspose.PDF pour Python illustre une approche simple pour contrôler la mise en page du texte et la lisibilité grâce aux ajustements d'espacement des lignes.

Notre extrait de code montre comment contrôler l'espacement des lignes dans un document PDF. Il lit le texte d'un fichier (ou utilise un message de secours), applique une taille de police et un espacement de ligne personnalisés, et ajoute le texte formaté à une nouvelle page d'un PDF.

1. Créez un nouveau document PDF.
1. Chargez le texte source.
1. Initialise un objet TextFragment et lui assigne le texte chargé.
1. Définissez les propriétés de police et d'espacement pour le texte. Ces valeurs déterminent la densité des lignes de texte :
- Taille de police : 12 points
- Espacement des lignes : 16 points
1. Insérez le fragment de texte formaté dans la collection de paragraphes de la page.
1. Enregistrez le document.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def specify_line_spacing_simple_case(outfile):
    """
    Specify custom line spacing for text in a PDF document.

    Creates a PDF document with text that has custom line spacing applied.
    Loads text content from an external file and applies 16-point line spacing
    to improve readability and text layout.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Attempts to load text from "lorem.txt" file in DATA_DIR
        - Falls back to default message if file doesn't exist
        - Font size: 12 points
        - Line spacing: 16 points (increased from default for better readability)
        - Demonstrates basic line spacing control in PDF text formatting

    Example:
        >>> specify_line_spacing_simple_case("line_spacing.pdf")
        # Creates a PDF with custom 16-point line spacing
    """

    document = ap.Document()
    page = document.pages.add()

    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    text = (
        open(lorem_path, "r", encoding="utf-8").read()
        if os.path.exists(lorem_path)
        else "Lorem ipsum text not found."
    )

    text_fragment = ap.text.TextFragment(text)
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.line_spacing = 16
    page.paragraphs.add(text_fragment)

    document.save(outfile)
```

#### Comment formater le texte avec un espacement de ligne personnalisé en Python - Cas spécifique

Vérifions comment appliquer différents modes d'espacement des lignes dans un document PDF en utilisant une police TrueType (TTF) personnalisée.
Il charge le texte depuis un fichier, intègre une police spécifique, et rend le même texte deux fois sur une page PDF—chaque fois en utilisant un mode d'espacement des lignes différent :

- mode FONT_SIZE : L'espacement des lignes est égal à la taille de la police.
- mode FULL_SIZE : L'espacement des lignes prend en compte la hauteur totale de la police, incluant les ascendantes et les descendantes.

L'exemple montre comment le comportement de l'espacement des lignes peut varier selon le mode sélectionné.

1. Créez un nouveau document PDF.
1. Spécifiez les chemins pour le fichier de police personnalisé et le fichier source du texte.
1. Chargez le contenu du texte.
1. Ouvrez la police personnalisée.
1. Créez et configurez le premier TextFragment (mode FONT_SIZE). Définissez line_spacing sur 'TextFormattingOptions.LineSpacingMode.FONT_SIZE', ce qui signifie que l'espacement des lignes est égal à la taille de la police.
1. Créez et configurez le deuxième TextFragment (mode FULL_SIZE). Définissez line_spacing sur 'TextFormattingOptions.LineSpacingMode.FULL_SIZE', qui utilise la hauteur totale de la police.
1. Ajoutez les deux fragments de texte à la même page PDF.
1. Enregistrez le document final à l'emplacement de sortie spécifié.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def specify_line_spacing_specific_case(outfile):
    """
    Create a PDF document demonstrating different line spacing modes with custom font.
    This function creates a PDF with two text fragments using the same custom TTF font
    but different line spacing modes to demonstrate the visual differences between
    FONT_SIZE and FULL_SIZE line spacing options.
    Args:
        outfile (str): Path where the output PDF file will be saved.
    Notes:
        - Requires 'HPSimplified.ttf' font file in DATA_DIR
        - Requires 'lorem.txt' text file in DATA_DIR for content
        - Falls back to default text if lorem.txt is not found
        - First fragment uses FONT_SIZE line spacing mode
        - Second fragment uses FULL_SIZE line spacing mode
    Dependencies:
        - aspose.pdf (ap) library
        - os module for file path operations
        - DATA_DIR constant must be defined
    """

    document = ap.Document()
    page = document.pages.add()

    font_file = os.path.join(DATA_DIR, "HPSimplified.ttf")
    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    text = (
        open(lorem_path, "r", encoding="utf-8").read()
        if os.path.exists(lorem_path)
        else "Lorem ipsum text not found."
    )

    with open(font_file, "rb") as font_stream:
        font = ap.text.FontRepository.open_font(font_stream, ap.text.FontTypes.TTF)

        fragment1 = ap.text.TextFragment(text)
        fragment1.text_state.font = font
        fragment1.text_state.formatting_options = ap.text.TextFormattingOptions()
        fragment1.text_state.formatting_options.line_spacing = (
            ap.text.TextFormattingOptions.LineSpacingMode.FONT_SIZE
        )
        page.paragraphs.add(fragment1)

        fragment2 = ap.text.TextFragment(text)
        fragment2.text_state.font = font
        fragment2.text_state.formatting_options = ap.text.TextFormattingOptions()
        fragment2.text_state.formatting_options.line_spacing = (
            ap.text.TextFormattingOptions.LineSpacingMode.FULL_SIZE
        )
        page.paragraphs.add(fragment2)

    document.save(outfile)
```

![Document PDF affichant du texte avec espacement de ligne personnalisé démontrant un espacement de 16 points entre les lignes pour une meilleure lisibilité et une mise en forme du texte](line_spacing.png)

### Utilisation de l'espacement des caractères

#### Comment contrôler l'espacement des caractères dans le texte PDF en utilisant la classe TextFragment

L'espacement des caractères détermine la distance entre les caractères individuels dans une ligne de texte—utile pour affiner l'apparence du texte ou obtenir des effets typographiques spécifiques.

1. Initialise un nouvel objet Document et ajoute une page vierge pour placer le texte.
1. Définissez le générateur de fragments. Implémente une fonction d'aide make_fragment(spacing) :
- créez un TextFragment avec le texte d'exemple.
- définissez la police.
1. Ajoutez des fragments de texte avec différentes valeurs d'espacement.
1. Enregistrez le Document.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def character_spacing_using_text_fragment(outfile):
    """
    Demonstrate character spacing control using TextFragment objects.

    Creates a PDF document showing different character spacing values applied
    to text fragments. Each line demonstrates progressively increased character
    spacing to illustrate the visual effect on text appearance.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Creates multiple TextFragment objects with varying character spacing
        - Character spacing values: 0, 1, 2, 3, and 4 points
        - Font: Times Roman, 12 points
        - Each fragment is positioned on a new line for comparison
        - Character spacing affects only horizontal letter spacing
        - Higher values create more space between individual characters

    Example:
        >>> character_spacing_using_text_fragment("char_spacing_fragment.pdf")
        # Creates a PDF showing progressive character spacing effects
    """
    document = ap.Document()
    page = document.pages.add()

    def make_fragment(spacing):
        fragment = ap.text.TextFragment("Sample Text with character spacing")
        fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
        fragment.text_state.font_size = 14
        fragment.text_state.character_spacing = spacing
        return fragment

    page.paragraphs.add(make_fragment(2.0))
    page.paragraphs.add(make_fragment(1.0))
    page.paragraphs.add(make_fragment(0.75))

    document.save(outfile)
```

![Document PDF affichant trois lignes de texte identiques « Sample Text » avec un espacement des caractères montrant un espacement de plus en plus serré du haut vers le bas, la première ligne ayant un espacement plus large entre les lettres, la ligne du milieu un espacement moyen, et la ligne du bas l'espacement le plus rapproché, illustrant l'effet visuel de différentes valeurs d'espacement des caractères dans le formatage du texte PDF](character_spacing_simple.png)

#### Comment contrôler l'espacement des caractères dans le texte PDF en utilisant TextParagraph et TextBuilder

Aspose.PDF permet d'appliquer un espacement de caractères personnalisé lors de l'ajout de texte à un document PDF à l'aide d'un TextParagraph et d'un TextBuilder.
Il définit une zone spécifique sur la page, configure le retour à la ligne du texte, et rend un fragment de texte avec un espacement entre les caractères ajusté.

L'utilisation de TextParagraph est idéale lorsque vous avez besoin d'un contrôle précis sur le placement et la mise en page du texte, par exemple lors de la création de blocs de texte structurés ou multi-colonnes.

1. Créez un nouveau document PDF.
1. Initialise une instance de TextBuilder pour la page.
1. Créez et configurez un TextParagraph.
- Définissez le mode de retour à la ligne sur 'TextFormattingOptions.WordWrapMode.BY_WORDS'.
1. Créez un TextFragment avec un espacement de caractères personnalisé.
- Créez un nouveau TextFragment et définissez son texte (p. ex., "Sample Text with character spacing").
- Spécifiez les attributs de police tels qu'Arial et une taille de police de 14 pt.
- Appliquez un espacement de caractères = 2.0, ce qui augmente l'espace entre les caractères.
1. Ajoutez le TextFragment au TextParagraph.
1. Ajoutez le TextParagraph à la page.
1. Enregistrez le document PDF.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def character_spacing_using_text_paragraph(outfile):
    """
    Demonstrate character spacing control using TextParagraph objects.

    Creates a PDF document with text paragraph that has custom character spacing
    applied. Shows how to set character spacing at the paragraph level and
    demonstrates the visual effect on text layout.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses TextParagraph for paragraph-level formatting
        - Character spacing: 2.0 points
        - Font: Times Roman, 12 points
        - Demonstrates paragraph-based character spacing control
        - Character spacing applies to all text within the paragraph
        - Alternative approach to fragment-based character spacing

    Example:
        >>> character_spacing_using_text_paragraph("char_spacing_paragraph.pdf")
        # Creates a PDF with paragraph-level character spacing
    """
    document = ap.Document()
    page = document.pages.add()

    builder = ap.text.TextBuilder(page)
    paragraph = ap.text.TextParagraph()
    paragraph.rectangle = ap.Rectangle(100, 700, 500, 750, True)
    paragraph.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )

    fragment = ap.text.TextFragment("Sample Text with character spacing")
    fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    fragment.text_state.font_size = 14
    fragment.text_state.character_spacing = 2.0

    paragraph.append_line(fragment)
    builder.append_paragraph(paragraph)
    document.save(outfile)
```

## Création de listes

Lors du travail avec des fichiers PDF, vous pouvez avoir besoin d'afficher des informations structurées telles que des listes — qu'elles soient à puces, numérotées ou formatées avec HTML ou LaTeX.
Aspose.PDF pour Python via .NET offre plusieurs méthodes flexibles pour créer et formater des listes directement dans vos documents PDF, vous donnant un contrôle total sur la mise en page, la police et le style.

Cet article montre plusieurs approches pour créer des listes dans les PDFs, allant du formatage en texte brut au rendu avancé HTML et LaTeX. Chaque méthode répond à un cas d'utilisation spécifique — que vous préfériez un contrôle programmatique précis ou un style pratique basé sur le balisage.

À la fin de cet article, vous saurez comment :

- Créer des listes à puces et numérotées personnalisées en utilisant TextParagraph et TextBuilder.

- Utiliser des fragments HTML (HtmlFragment) pour rendre facilement des listes '<ul>' et '<ol>' dans les PDFs.

- Exploiter les fragments LaTeX (TeXFragment) pour le formatage de listes mathématiques ou scientifiques.

- Contrôler le retour à la ligne du texte, les styles de police et le positionnement de la mise en page au sein d'une page.

- Comprendre la différence entre la construction manuelle de listes et les approches basées sur le balisage.

### Créer une liste à puces

Créez une liste à puces personnalisée dans un PDF en utilisant TextParagraph et TextBuilder, sans dépendre du formatage HTML ou LaTeX.
Chaque élément de liste est préfixé d'un caractère puce (•) et ajouté comme un TextFragment séparé.

1. Initialise un objet Document et ajoute une page vierge.
1. Définez une liste Python de chaînes qui seront converties en puces.
1. Créez un TextBuilder et un TextParagraph.
1. Utilisez le 'TextBuilder' pour ajouter le paragraphe configuré à la page.
1. Enregistrez le document PDF.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_bullet_list(outfile):
    """
    Create a PDF document with a bullet list using plain text formatting.
    This function generates a PDF document containing a bullet list with predefined items.
    The list is formatted with bullet points, uses Times New Roman font, and includes
    text wrapping behavior for longer items.
    Args:
        outfile (str): The file path where the PDF document will be saved.
    Returns:
        None: The function saves the document to the specified file path.
    Note:
        The bullet list is positioned within a rectangle at coordinates (80, 200, 400, 800)
        and uses word wrapping mode for text formatting.
    """

    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item in the list",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]

    builder = ap.text.TextBuilder(page)
    paragraph = ap.text.TextParagraph()
    paragraph.rectangle = ap.Rectangle(80, 200, 400, 800, True)
    paragraph.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )

    for item in items:
        fragment = ap.text.TextFragment("• " + item)
        fragment.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
        fragment.text_state.font_size = 12
        paragraph.append_line(fragment)

    builder.append_paragraph(paragraph)
    document.save(outfile)
```

### Créer une liste numérotée

Créez une liste numérotée (ordonnée) personnalisée dans un PDF en utilisant TextParagraph et TextBuilder, sans dépendre du formatage HTML ou LaTeX.
Chaque élément de liste est préfixé de son numéro (p. ex., 1., 2.) et ajouté comme un TextFragment séparé.

1. Initialise un objet Document et ajoute une page vierge.
1. Définez une liste Python de chaînes qui seront converties en éléments de liste numérotés.
1. Créez un TextBuilder et un TextParagraph.
1. Ajoutez chaque élément comme un TextFragment avec son numéro.
1. Utilisez le TextBuilder pour ajouter le paragraphe configuré à la page.
1. Enregistrez le document PDF.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_numbered_list(outfile):
    """
    Create a numbered list in a PDF document using plain text formatting.
    This function generates a PDF document containing a numbered list with predefined
    items. The list is formatted with Times New Roman font and includes text wrapping
    by words within a specified rectangular area on the page.
    Args:
        outfile (str): The file path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified file path but does
              not return any value.
    Note:
        - Uses Aspose.PDF library (imported as 'ap')
        - List items are hardcoded within the function
        - Font: Times New Roman, size 12
        - Text wrapping: BY_WORDS mode
        - Rectangle bounds: (80, 200, 400, 800)
    """

    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item in the list",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]

    builder = ap.text.TextBuilder(page)
    paragraph = ap.text.TextParagraph()
    paragraph.rectangle = ap.Rectangle(80, 200, 400, 800, True)
    paragraph.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )

    for i, item in enumerate(items):
        fragment = ap.text.TextFragment(f"{i + 1}. {item}")
        fragment.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
        fragment.text_state.font_size = 12
        paragraph.append_line(fragment)

    builder.append_paragraph(paragraph)
    document.save(outfile)
```

### Créer une version HTML d'une liste à puces

Notre bibliothèque montre comment créer une liste à puces (non ordonnée) dans un document PDF en utilisant des fragments HTML. Elle convertit une liste Python de chaînes en un élément HTML `<ul>` et l'insère dans une page PDF en tant qu'HtmlFragment. L'utilisation de fragments HTML vous permet d'exploiter les fonctionnalités de formatage HTML (comme les listes, le gras, l'italique) directement dans le PDF.

1. Créez un nouveau document PDF et ajoutez une page.
1. Préparez les éléments de la liste.
1. Convertissez la liste en une liste HTML non ordonnée.
- Utilisez la balise `<ul>` pour une liste non ordonnée (à puces).
- Encapsulez chaque élément avec des balises 'li' en utilisant une compréhension de liste.
1. Créez un HtmlFragment. Convertissez la chaîne HTML en un objet HtmlFragment qui peut être ajouté à la page PDF.
1. Insérez le HtmlFragment dans la collection de paragraphes de la page.
1. Enregistrez le document PDF.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_bullet_list_html_version(outfile):
    """
    Create a bulleted list using HTML formatting in a PDF document.

    Generates a PDF with an unordered (bulleted) list created using HTML markup.
    Demonstrates how to use HtmlFragment to embed HTML list structures directly
    into PDF documents with proper formatting and styling.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses HTML <ul> and <li> tags for list structure
        - Items are predefined with sample content
        - HtmlFragment automatically handles HTML rendering
        - Lists maintain proper bullet formatting and indentation
        - Simpler alternative to manual list creation with TextFragments
        - Supports nested lists and HTML styling if needed

    Example:
        >>> create_bullet_list_html_version("bullet_list_html.pdf")
        # Creates a PDF with HTML-formatted bulleted list
    """

    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item in the list",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]
    html_list = "<ul>" + "".join([f"<li>{item}</li>" for item in items]) + "</ul>"
    html_fragment = ap.HtmlFragment(html_list)
    page.paragraphs.add(html_fragment)
    document.save(outfile)
```

![Bulleted list displayed in a PDF document showing four items: First item in the list, Second item with more text to demonstrate wrapping behavior, Third item, and Fourth item. Each item is preceded by a standard bullet point and demonstrates HTML-formatted list rendering within the PDF structure with proper indentation and spacing](bullet_list_html.png)

### Créer une version HTML de liste numérotée

Créez une liste numérotée (ordonnée) dans un document PDF en utilisant des fragments HTML. Elle convertit une liste Python de chaînes en un élément HTML `<ol>` et l’insère dans une page PDF en tant que HtmlFragment.

L’utilisation de fragments HTML vous permet d’intégrer directement dans votre PDF des fonctionnalités de mise en forme basées sur HTML, comme les listes numérotées, le gras, l’italique, etc.

1. Créez un nouveau document PDF et ajoutez une page.
1. Préparez les éléments de la liste.
1. Convertissez la liste en une liste ordonnée HTML.
- Utilisez la balise `<ol>` pour une liste numérotée.
- Enveloppez chaque élément avec des balises `li` à l’aide d’une compréhension de liste.
1. Convertissez la chaîne HTML en un objet HtmlFragment qui peut être ajouté à la page PDF.
1. Insérez le HtmlFragment dans la collection de paragraphes de la page.
1. Enregistrez le document PDF.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_numbered_list_html_version(outfile):
    """
    Create a numbered list using HTML formatting in a PDF document.

    Generates a PDF with an ordered (numbered) list created using HTML markup.
    Demonstrates how to use HtmlFragment to embed HTML ordered list structures
    directly into PDF documents with automatic numbering and formatting.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses HTML <ol> and <li> tags for ordered list structure
        - Items are predefined with sample content
        - HtmlFragment automatically handles HTML rendering and numbering
        - Lists maintain proper numeric formatting and indentation
        - Numbers are automatically generated (1, 2, 3, etc.)
        - Supports nested lists and custom numbering styles if needed

    Example:
        >>> create_numbered_list_html_version("numbered_list_html.pdf")
        # Creates a PDF with HTML-formatted numbered list
    """

    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item in the list",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]
    html_list = "<ol>" + "".join([f"<li>{item}</li>" for item in items]) + "</ol>"
    html_fragment = ap.HtmlFragment(html_list)
    page.paragraphs.add(html_fragment)
    document.save(outfile)
```

![Numbered list displayed in a PDF document showing four automatically numbered items: 1. First item in the list, 2. Second item with more text to demonstrate wrapping behavior, 3. Third item, and 4. Fourth item. The list demonstrates HTML-formatted ordered list rendering within PDF structure with proper numeric sequencing, indentation, and spacing between items](numbered_list_html.png)

### Créer une version LaTeX de liste à puces

Créez une liste à puces (non ordonnée) dans un PDF en utilisant des fragments LaTeX (TeXFragment). Elle convertit une liste Python de chaînes en un environnement LaTeX `itemize` et l’insère dans une page PDF. L’utilisation de fragments LaTeX est idéale lorsque vous souhaitez rendre des formules mathématiques, des symboles ou des listes structurées avec un formatage précis.

1. Créez un nouveau document PDF et ajoutez une page.
1. Définissez une liste Python de chaînes qui deviendront des puces dans l’environnement LaTeX `itemize`.
1. Convertissez la liste en un environnement LaTeX `itemize` :
- Enveloppez les éléments avec \begin{itemize} et \end{itemize}.
- Chaque élément est préfixé par \item à l’aide d’une compréhension de liste.
1. Convertissez la chaîne LaTeX en un objet TeXFragment qui peut être rendu dans le PDF.
1. Ajoutez le fragment LaTeX à la page.
1. Enregistrez le document PDF.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_bullet_list_latex_version(outfile):
    """
    Create a bulleted list using LaTeX formatting in a PDF document.

    Generates a PDF with an unordered list created using LaTeX markup.
    Demonstrates how to use TeXFragment to embed LaTeX itemize environments
    directly into PDF documents with proper mathematical and scientific formatting.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses LaTeX \\begin{itemize} and \\item commands
        - TeXFragment handles LaTeX compilation and rendering
        - Supports mathematical expressions and scientific notation
        - Lists maintain proper bullet formatting and indentation
        - More powerful than HTML for mathematical content
        - Can include LaTeX math modes and special symbols

    Example:
        >>> create_bullet_list_latex_version("bullet_list_latex.pdf")
        # Creates a PDF with LaTeX-formatted bulleted list
    """

    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]
    tex_list = (
        "Lists are easy to create: \\begin{itemize}"
        + "".join([f"\\item {i}" for i in items])
        + "\\end{itemize}"
    )
    tex_fragment = ap.TeXFragment(tex_list)
    page.paragraphs.add(tex_fragment)
    document.save(outfile)
```

![Bulleted list displayed in PDF showing LaTeX-rendered formatting with text Lists are easy to create: followed by four bullet-pointed items: First item, Second item with more text to demonstrate wrapping behavior, Third item, and Fourth item. The list demonstrates professional LaTeX typesetting with proper bullet formatting, consistent spacing, and text wrapping capabilities within a clean PDF document layout](bullet_list_latex.png)

### Créer une version LaTeX de liste numérotée

Créez une liste numérotée (ordonnée) dans un PDF en utilisant des fragments LaTeX (TeXFragment). Elle convertit une liste Python de chaînes en un environnement LaTeX `enumerate` et l’insère dans une page PDF. L’utilisation de fragments LaTeX est idéale lorsque vous désirez un formatage précis, des listes structurées ou des notations mathématiques dans les PDF.

1. Créez un nouveau document PDF et ajoutez une page.
1. Définissez une liste Python de chaînes qui deviendront des éléments numérotés dans l’environnement LaTeX `enumerate`.
1. Convertissez la liste en un environnement LaTeX `enumerate`.
1. Convertissez la chaîne LaTeX en un objet TeXFragment qui peut être rendu dans le PDF.
1. Ajoutez le fragment LaTeX à la page.
1. Enregistrez le document PDF.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_numbered_list_latex_version(outfile):
    """Create a numbered list using LaTeX."""

    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]
    tex_list = (
        "Lists are easy to create: \\begin{enumerate}"
        + "".join([f"\\item {i}" for i in items])
        + "\\end{enumerate}"
    )
    tex_fragment = ap.TeXFragment(tex_list)
    page.paragraphs.add(tex_fragment)
    document.save(outfile)
```

![Numbered list displayed in PDF showing LaTeX-rendered formatting with items 1. First item, 2. Second item with more text to demonstrate wrapping behavior, 3. Third item, and 4. Fourth item, preceded by the text Lists are easy to create](numbered_list_latex.png)

## Notes de bas de page et notes de fin

### Ajouter des notes de bas de page

Les notes de bas de page sont utilisées pour référencer des remarques dans le corps d’un document en plaçant des numéros en exposant consécutifs à côté du texte pertinent. Ces numéros correspondent à des notes détaillées qui sont généralement indentées et positionnées en bas de la même page, fournissant un contexte supplémentaire, des citations ou des commentaires.

Ajoutez une note de bas de page à un fragment de texte dans un document PDF en utilisant Aspose.PDF for Python via .NET. Les notes de bas de page sont utiles pour fournir des informations supplémentaires, des citations ou des clarifications sans encombrer le contenu principal. Cette méthode garantit que les notes de bas de page sont intégrées visuellement et structurellement dans la mise en page du PDF.

1. Créez un nouveau document.
1. Créez un TextFragment avec le contenu principal.
1. Ajoutez du texte en ligne. Créez un autre TextFragment qui continue dans le même paragraphe.
1. Enregistrez le document.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_footnote(outfile):
    """Add footnote to a PDF document."""

    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with a footnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.foot_note = ap.Note("This is the footnote content.")
    page.paragraphs.add(text_fragment)

    inline_text = ap.text.TextFragment(
        " This is another text after footnote in the same paragraph."
    )
    inline_text.is_in_line_paragraph = True
    inline_text.text_state.font = ap.text.FontRepository.find_font("Arial")
    inline_text.text_state.font_size = 14
    page.paragraphs.add(inline_text)

    document.save(outfile)
```

### Ajouter une note de bas de page avec style personnalisé dans le PDF

1. Initialise un nouveau document PDF et ajoute une page blanche.
1. Créez le fragment de texte principal.
1. Créez et stylisez la note de bas de page (police, taille, couleur, style).
1. Insérez le fragment de texte stylisé avec la note de bas de page dans la page.
1. Ajoutez un autre fragment de texte sans note de bas de page.
1. Enregistrer le document.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_footnote_custom_text_style(outfile):
    """Add footnote with custom text style."""

    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with a footnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14

    note = ap.Note("This is the footnote content with custom text style.")
    note.text_state = ap.text.TextState()
    note.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    note.text_state.font_size = 10
    note.text_state.foreground_color = ap.Color.red
    note.text_state.font_style = ap.text.FontStyles.ITALIC
    text_fragment.foot_note = note

    page.paragraphs.add(text_fragment)

    another_text = ap.text.TextFragment(" This is another text without footnote.")
    another_text.text_state.font = ap.text.FontRepository.find_font("Arial")
    another_text.text_state.font_size = 14
    page.paragraphs.add(another_text)

    document.save(outfile)
```

### Ajouter des notes de bas de page avec des symboles personnalisés dans le PDF

Ajouter des notes de bas de page aux fragments de texte dans un document PDF en utilisant Aspose.PDF pour Python via .NET, avec la possibilité de personnaliser le symbole du marqueur de note de bas de page.

1. Créer un document PDF et une page.
1. Ajouter le premier fragment de texte avec un symbole de note de bas de page personnalisé.
1. Ajouter un autre fragment de texte qui continue le paragraphe sans note de bas de page.
1. Ajouter le deuxième fragment de texte avec une note de bas de page par défaut.
1. Enregistrer le document.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_footnote_custom_text(outfile):
    """
    Add footnote with custom text marker to a PDF document.
    Creates a PDF document with text fragments that include footnotes with custom
    styling. The function demonstrates how to add footnotes with custom text markers
    and standard footnotes to different text fragments within the same document.
    Args:
        outfile (str): The output file path where the PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file.
    Example:
        add_footnote_custom_text("output_with_footnotes.pdf")
    Note:
        The document will contain:
        - Text with a custom footnote marker ("*")
        - Text without footnotes
        - Text with a standard footnote
    """

    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with a footnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14

    note = ap.Note("This is the footnote content with custom text style.")
    note.text = "*"
    text_fragment.foot_note = note
    page.paragraphs.add(text_fragment)

    another_text = ap.text.TextFragment(" This is another text without footnote.")
    another_text.text_state.font = ap.text.FontRepository.find_font("Arial")
    another_text.text_state.font_size = 14
    page.paragraphs.add(another_text)

    text_fragment = ap.text.TextFragment("This is a sample text with a footnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.foot_note = ap.Note("This is the footnote content.")
    page.paragraphs.add(text_fragment)

    document.save(outfile)
```

### Ajouter des notes de bas de page avec un style de ligne personnalisé dans le PDF

Personnaliser l'apparence visuelle des lignes de notes de bas de page dans un document PDF avec la bibliothèque Python. La personnalisation des lignes de notes de bas de page améliore la clarté visuelle et permet une cohérence stylistique dans des documents tels que des rapports, des articles académiques et des publications annotées.

1. Créer un nouveau document PDF et ajouter une page.
1. Définir un style de ligne personnalisé pour les connecteurs de notes de bas de page (couleur, épaisseur et motif de tirets).
1. Ajouter plusieurs fragments de texte avec des notes de bas de page.
1. Enregistrer le document final.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_footnote_with_custom_line_style(outfile):
    """
    Add footnotes with custom line style to a PDF document.
    Creates a PDF document with text fragments that have footnotes and applies
    a custom line style for the footnote separator line. The custom style includes
    red color, increased line width, and dashed pattern.
    Args:
        outfile (str): Path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file.
    Example:
        >>> add_footnote_with_custom_line_style("output.pdf")
        # Creates a PDF with footnoted text and custom separator line styling
    """

    document = ap.Document()
    page = document.pages.add()

    # Define custom line style
    graph_info = ap.GraphInfo()
    graph_info.line_width = 2
    graph_info.color = ap.Color.red
    graph_info.dash_array = [3]
    graph_info.dash_phase = 1
    page.note_line_style = graph_info

    # First text fragment with footnote
    text1 = ap.text.TextFragment("This is a sample text with a footnote.")
    text1.foot_note = ap.Note("foot note for text 1")
    page.paragraphs.add(text1)

    # Second text fragment with footnote
    text2 = ap.text.TextFragment("This is yet another sample text with a footnote.")
    text2.foot_note = ap.Note("foot note for text 2")
    page.paragraphs.add(text2)

    document.save(outfile)
```

### Ajouter des notes de bas de page avec image et tableau dans le PDF

Comment enrichir les notes de bas de page dans un document PDF en incorporant des images, du texte stylisé et des tableaux à l'aide d'Aspose.PDF pour Python via .NET ?

1. Créer un nouveau document PDF et ajouter une page.
1. Ajouter un fragment de texte avec une note de bas de page attachée.
1. Intégrer une image, du texte stylisé et un tableau à l'intérieur de la note de bas de page.
1. Enregistrer le document.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_footnote_with_image_and_table(outfile):
    """
    Add a footnote containing an image and table to a PDF document.
    Creates a new PDF document with sample text that includes a footnote. The footnote
    contains three elements: an image (logo.jpg), descriptive text, and a simple table
    with two cells. The image is resized to 20x20 pixels and the footnote text uses
    a 20pt font size.
    Args:
        outfile (str): The file path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file.
    Note:
        - Requires the logo.jpg file to be present in the DATA_DIR directory
        - Uses the Aspose.PDF library (imported as 'ap')
        - The footnote is attached to the main text fragment on the page
    """

    document = ap.Document()
    page = document.pages.add()

    text = ap.text.TextFragment("This is a sample text with a footnote.")
    page.paragraphs.add(text)

    note = ap.Note()

    # Add image
    image_note = ap.Image()
    image_note.file = os.path.join(DATA_DIR, "logo.jpg")
    image_note.fix_height = 20
    image_note.fix_width = 20
    note.paragraphs.add(image_note)

    # Add text
    text_note = ap.text.TextFragment("This is the footnote content.")
    text_note.text_state.font_size = 20
    text_note.is_in_line_paragraph = True
    note.paragraphs.add(text_note)

    # Add table
    table = ap.Table()
    table.rows.add().cells.add("Cell 1,1")
    table.rows.add().cells.add("Cell 1,2")
    note.paragraphs.add(table)

    text.foot_note = note

    document.save(outfile)
```

### Ajouter des notes de fin aux documents PDF

Une note de fin est un type de citation qui dirige les lecteurs vers une section désignée à la fin d'un document, où ils peuvent trouver la référence complète d'une citation, d'une idée paraphrasée ou d'un contenu résumé. Lorsqu'on utilise des notes de fin, un chiffre en exposant est placé immédiatement après le matériel référencé, guidant le lecteur vers la note correspondante à la fin du texte.

Cet extrait de code montre comment ajouter une note de fin à un fragment de texte dans un document PDF. Contrairement aux notes de bas de page, qui apparaissent près du texte référencé, les notes de fin sont généralement placées à la fin d'un document ou d'une section. Cette méthode simule également un document plus long pour illustrer le comportement des notes de fin dans un contenu étendu.

1. Créer un document PDF et une page.
1. Ajouter un fragment de texte avec une note de fin.
1. Charger le contenu texte externe.
1. Simuler un document long. Ajouter le texte chargé plusieurs fois pour simuler un document plus long.
1. Enregistrer le document.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_endnote(outfile):
    """Add endnote to a PDF document.
    Creates a new PDF document with a text fragment containing an endnote,
    followed by additional lorem ipsum content to simulate a longer document.
    The endnote is attached to the first text fragment and will be displayed
    according to the PDF viewer's endnote handling.
    Args:
        outfile (str): The file path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file path.
    Note:
        This function requires the aspose-pdf library and assumes the existence
        of a DATA_DIR variable pointing to a directory containing 'lorem.txt'.
        If the lorem.txt file is not found, fallback text will be used.
    """

    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with an endnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.end_note = ap.Note("This is the EndNote content.")
    page.paragraphs.add(text_fragment)

    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    text_content = (
        open(lorem_path, encoding="utf-8").read()
        if os.path.exists(lorem_path)
        else "Lorem ipsum sample text not found."
    )

    # Simulate long text
    for _ in range(5):
        tf = ap.text.TextFragment(text_content)
        tf.text_state.font = ap.text.FontRepository.find_font("Arial")
        tf.text_state.font_size = 14
        page.paragraphs.add(tf)

    document.save(outfile)
```

### Ajouter des notes de fin avec un texte de marqueur personnalisé dans le PDF

Ajouter une note de fin à un fragment de texte dans un document PDF, avec un symbole de marqueur personnalisé (par ex., "***"). Les notes de fin sont généralement placées à la fin d'un document ou d'une section et sont utiles pour fournir un contexte supplémentaire, des citations ou des commentaires.

1. Créer un document PDF et une page.
1. Ajouter un fragment de texte stylisé avec une note de fin.
1. Personnaliser le texte du marqueur de note de fin.
1. Charger le contenu externe depuis un fichier .txt.
1. Simuler un contenu long pour illustrer le placement de la note de fin.
1. Enregistrer le document PDF.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_endnote_custom_text(outfile):
    """
    Add endnote with custom text marker to a PDF document.
    Creates a PDF document with a text fragment that contains an endnote with
    a custom marker ("***"). The document is populated with sample text content
    from a lorem.txt file, repeated multiple times to simulate a longer document.
    Args:
        outfile (str): Path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file path.
    Note:
        - Requires lorem.txt file in DATA_DIR for sample content
        - Falls back to default text if lorem.txt is not found
        - Uses Arial font with 14pt size for all text elements
        - The endnote marker is set to "***" instead of default numbering
    """

    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with an endnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.end_note = ap.Note("This is the EndNote content.")
    text_fragment.end_note.text = "***"
    page.paragraphs.add(text_fragment)

    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    text_content = (
        open(lorem_path, encoding="utf-8").read()
        if os.path.exists(lorem_path)
        else "Lorem ipsum sample text not found."
    )

    # Simulate long text
    for _ in range(5):
        tf = ap.text.TextFragment(text_content)
        tf.text_state.font = ap.text.FontRepository.find_font("Arial")
        tf.text_state.font_size = 14
        page.paragraphs.add(tf)

    document.save(outfile)
```

## Mise en page et contrôle des pages

### Forcer un tableau à commencer sur une nouvelle page dans le PDF

Ajouter un contenu spécifique pour commencer sur une nouvelle page dans un document PDF en utilisant Aspose.PDF pour Python via .NET.
En définissant la propriété 'is_in_new_page', vous pouvez contrôler avec précision la mise en page et la structure des pages, en veillant à ce que des sections particulières (telles que des tableaux, des rapports ou des résumés) commencent toujours sur une page vierge — idéal pour le formatage de documents, les rapports prêts à imprimer ou la génération de sorties organisées.

1. Créer et configurer un tableau.
1. Ajouter des données au tableau.
1. Forcer une nouvelle page pour le tableau. Cela garantit que le tableau commence en haut d'une nouvelle page, même s'il y a du contenu existant sur la page actuelle.
1. Ajouter le tableau à la page. Utilisez 'page.paragraphs.add()' pour inclure le tableau dans la mise en page du PDF.
1. Enregistrer le document.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def force_new_page(output_file_name):
    """
    Create a PDF document demonstrating forced page breaks with tables.

    Creates a PDF document with a table that is forced to start on a new page
    using the is_in_new_page property. This is useful for controlling page layout
    and ensuring specific content starts on fresh pages.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Creates a 3-column table with 5 rows of sample data
        - Table uses uniform column widths of 150 units each
        - All cells have borders for clear visual separation
        - is_in_new_page=True forces the table to start on a new page
        - Useful for reports, documents with sections, or content organization

    Example:
        >>> force_new_page("new_page_table.pdf")
        # Creates a PDF with a table that starts on a new page
    """
    # Create new PDF document
    document = ap.Document()
    page = document.pages.add()

    # Create a table
    table = ap.Table()
    table.column_widths = "150 150 150"
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL)

    # Add rows with sample data
    for i in range(5):
        row = table.rows.add()
        row.cells.add(f"Row {i + 1} - Col 1")
        row.cells.add(f"Row {i + 1} - Col 2")
        row.cells.add(f"Row {i + 1} - Col 3")

    # --- Key part: force table to start on a new PDF page ---
    table.is_in_new_page = True

    # Add table to page
    page.paragraphs.add(table)

    # Save the PDF
    document.save(output_file_name)
```

### Utiliser la propriété de paragraphe en ligne dans un PDF

Notre bibliothèque vous permet d'utiliser la propriété 'is_in_line_paragraph' pour contrôler le flux en ligne entre le texte et les images au sein d'un PDF.
Normalement, lorsque vous ajoutez de nouveaux éléments (comme des fragments de texte ou des images), chacun commence sur une nouvelle ligne ou un nouveau paragraphe.
En réglant 'is_in_line_paragraph = True', vous pouvez faire apparaître les éléments sur la même ligne ou au sein du même paragraphe, créant des mises en page en ligne fluides — parfait pour combiner texte et images en ligne, comme l'ajout de logos, d'icônes ou de symboles au sein de phrases.

Le premier fragment de texte, l'image et le deuxième fragment de texte apparaissent sur la même ligne, formant un paragraphe en ligne continu.
Le troisième fragment de texte commence un nouveau paragraphe, démontrant le comportement de retour à la ligne par défaut.

1. Créez un nouveau document PDF.
1. Ajoutez le premier fragment de texte.
1. Insérez une image en ligne.
1. Ajoutez plus de texte en ligne.
1. Ajoutez un nouveau paragraphe.
1. Enregistrez le PDF.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def using_inline_paragraph_property(output_file_name):
    """
    Demonstrate inline paragraph behavior in PDF document layout.

    Creates a PDF document showing how the is_in_line_paragraph property affects
    the flow of text and images. Elements with this property continue the flow
    of the previous paragraph instead of starting a new one.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - First text fragment starts a new paragraph
        - Image with is_in_line_paragraph=True continues the same line
        - Second text fragment also continues the same paragraph line
        - Third text fragment starts a new paragraph (default behavior)
        - Demonstrates inline flow control for mixed content (text + images)
        - Image is resized to 30x30 pixels and flows inline with text

    Example:
        >>> using_inline_paragraph_property("inline_paragraph.pdf")
        # Creates a PDF demonstrating inline paragraph flow
    """
    # Create a PDF document
    document = ap.Document()
    page = document.pages.add()

    # --- First text fragment (normal paragraph) ---
    fragment1 = ap.text.TextFragment("This is the first part of the paragraph. ")
    fragment1.text_state.font = ap.text.FontRepository.find_font("Arial")
    fragment1.text_state.font_size = 14
    page.paragraphs.add(fragment1)

    # --- Inline image (continues same paragraph flow) ---
    image = ap.Image()
    image.is_in_line_paragraph = True  # Makes image inline with previous paragraph
    image.file = os.path.join(DATA_DIR, "logo.jpg")
    image.fix_height = 30
    image.fix_width = 30
    page.paragraphs.add(image)

    # --- Second inline text fragment (keeps same paragraph flow) ---
    fragment2 = ap.text.TextFragment("This is the second part of the same paragraph.")
    fragment2.is_in_line_paragraph = True
    fragment2.text_state.font = ap.text.FontRepository.find_font("Arial")
    fragment2.text_state.font_size = 14
    page.paragraphs.add(fragment2)

    # --- Third fragment (starts new paragraph automatically) ---
    fragment3 = ap.text.TextFragment("This is a new paragraph.")
    fragment3.text_state.font = ap.text.FontRepository.find_font("Arial")
    fragment3.text_state.font_size = 14
    page.paragraphs.add(fragment3)

    # Save PDF
    document.save(output_file_name)
```

### Créer un PDF à plusieurs colonnes

Créez une mise en page de type journal à plusieurs colonnes dans un PDF en utilisant Aspose.PDF pour Python via .NET.
Il montre comment combiner texte, formatage HTML et graphiques dans un FloatingBox, permettant un contrôle avancé de la mise en page similaire aux conceptions de magazines ou newsletters à colonnes multiples.

1. Initialise le document PDF.
1. Ajoutez une ligne de séparation horizontale en haut.
1. Ajoutez un titre HTML stylisé.
1. Créez le FloatingBox pour le contrôle de la mise en page.
1. Configurez la mise en page à colonnes multiples.
1. Ajoutez les informations de l'auteur.
1. Dessinez une autre ligne horizontale interne.
1. Ajoutez le texte de l'article.
1. Enregistrez le PDF final.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_multi_column_pdf(output_file_name):
    """
    Create a PDF document with multi-column layout using FloatingBox.

    Creates a professional-looking PDF with a multi-column newspaper-style layout.
    Demonstrates advanced layout techniques including floating boxes, column
    configuration, and mixed content with graphics and text.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Document margins: 40 points left and right
        - Top horizontal line for visual separation
        - HTML-formatted heading with custom styling
        - FloatingBox with 2-column layout (105 units wide each)
        - Column spacing: 5 units between columns
        - Includes author attribution with italic styling
        - Internal horizontal line within the floating box
        - Long text content automatically flows between columns
        - Demonstrates professional document layout techniques

    Example:
        >>> create_multi_column_pdf("multi_column_layout.pdf")
        # Creates a PDF with newspaper-style multi-column layout
    """
    # Create PDF document
    document = ap.Document()

    # Set margins
    document.page_info.margin.left = 40
    document.page_info.margin.right = 40

    page = document.pages.add()

    #
    # Draw horizontal line at the top
    #
    graph1 = ap.drawing.Graph(500.0, 2.0)
    page.paragraphs.add(graph1)

    pos_arr = [1.0, 2.0, 500.0, 2.0]
    line1 = ap.drawing.Line(pos_arr)
    graph1.shapes.add(line1)

    #
    # Add HTML heading text
    #
    html = "<span style=\"font-family: 'Times New Roman'; font-size: 18px;\"><strong>How to Steer Clear of money scams</strong></span>"
    heading_text = ap.HtmlFragment(html)
    page.paragraphs.add(heading_text)

    #
    # Floating box: enables multi-column layout
    #
    box = ap.FloatingBox()

    box.column_info.column_count = 2  # Two columns
    box.column_info.column_spacing = "5"  # Space between columns
    box.column_info.column_widths = "105 105"  # Width of each column

    #
    # Add title text to the FloatingBox
    #
    text1 = ap.text.TextFragment("By A Googler (The Official Google Blog)")
    text1.text_state.font_size = 8
    text1.text_state.line_spacing = 2
    box.paragraphs.add(text1)

    text1.text_state.font_size = 10
    text1.text_state.font_style = ap.text.FontStyles.ITALIC

    #
    # Add another horizontal line inside the box
    #
    graph2 = ap.drawing.Graph(50.0, 10.0)

    pos_arr2 = [1.0, 10.0, 100.0, 10.0]
    line2 = ap.drawing.Line(pos_arr2)
    graph2.shapes.add(line2)

    box.paragraphs.add(graph2)

    #
    # Add long text content
    #
    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    lorem_text = (
        open(lorem_path, "r", encoding="utf-8").read()
        if os.path.exists(lorem_path)
        else "Lorem ipsum text not found."
    )
    text2 = ap.text.TextFragment(lorem_text * 5)
    box.paragraphs.add(text2)

    page.paragraphs.add(box)

    # Save PDF
    document.save(output_file_name)
```

### Arrêts de tabulation personnalisés pour l'alignement du texte dans le PDF

Créez une mise en page de texte similaire à un tableau dans un PDF en utilisant des arrêts de tabulation personnalisés — sans vous appuyer sur des structures de tableau.
En définissant les positions des arrêts de tabulation, les alignements et les styles de leader, vous pouvez aligner le texte précisément à travers les colonnes. Cela est utile pour les factures, les rapports ou les données textuelles structurées.

1. Créez un nouveau document PDF.
1. Définissez des arrêts de tabulation personnalisés.
1. Utilisez les espaces réservés #$TAB dans le texte.
1. Ajoutez du texte au PDF.
1. Enregistrez le PDF.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def custom_tab_stops(output_file_name):
    """
    Create a PDF document demonstrating custom tab stops for table-like formatting.

    Creates a PDF document that uses custom tab stops to format text in a table-like
    structure without using actual table elements. This demonstrates advanced text
    formatting with precise positioning and leader styles.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Tab stop 1: Position 100, right-aligned, solid leader line
        - Tab stop 2: Position 200, center-aligned, dashed leader line
        - Tab stop 3: Position 300, left-aligned, dotted leader line
        - Uses #$TAB placeholder for tab positions in text
        - Creates table-like structure with headers and data rows
        - Demonstrates mixing TextFragment and TextSegment approaches
        - Leader lines provide visual guides between columns
        - Alternative to HTML tables for precise text positioning

    Example:
        >>> custom_tab_stops("custom_tabs.pdf")
        # Creates a PDF with custom tab stop formatting
    """
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Define tab stops
    tab_stops = ap.text.TabStops()

    tab_stop1 = tab_stops.add(100)
    tab_stop1.alignment_type = ap.text.TabAlignmentType.RIGHT
    tab_stop1.leader_type = ap.text.TabLeaderType.SOLID

    tab_stop2 = tab_stops.add(200)
    tab_stop2.alignment_type = ap.text.TabAlignmentType.CENTER
    tab_stop2.leader_type = ap.text.TabLeaderType.DASH

    tab_stop3 = tab_stops.add(300)
    tab_stop3.alignment_type = ap.text.TabAlignmentType.LEFT
    tab_stop3.leader_type = ap.text.TabLeaderType.DOT

    # Create TextFragments with tab placeholders
    header = ap.text.TextFragment(
        "This is an example of forming table with TAB stops", tab_stops
    )
    text0 = ap.text.TextFragment("#$TABHead1 #$TABHead2 #$TABHead3", tab_stops)
    text1 = ap.text.TextFragment("#$TABdata11 #$TABdata12 #$TABdata13", tab_stops)

    text2 = ap.text.TextFragment("#$TABdata21 ", tab_stops)
    text2.segments.append(ap.text.TextSegment("#$TAB"))
    text2.segments.append(ap.text.TextSegment("data22 "))
    text2.segments.append(ap.text.TextSegment("#$TAB"))
    text2.segments.append(ap.text.TextSegment("data23"))

    # Add text fragments to page
    page.paragraphs.add(header)
    page.paragraphs.add(text0)
    page.paragraphs.add(text1)
    page.paragraphs.add(text2)

    # Save PDF document
    document.save(output_file_name)
```
