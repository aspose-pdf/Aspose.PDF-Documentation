---
title: Ajouter du texte au PDF
linktitle: Ajouter du texte au PDF
type: docs
weight: 10
url: /fr/python-net/add-text-to-pdf-file/
description: Cet article décrit divers aspects du travail avec le texte dans Aspose.PDF. Apprenez comment ajouter du texte au PDF, ajouter des fragments HTML ou utiliser des polices OTF personnalisées.
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter du texte dans un PDF avec Python
Abstract: Cet article fournit un guide complet sur la manipulation de documents PDF à l'aide de la bibliothèque Aspose.PDF en Python. Il couvre diverses techniques d'ajout et de mise en forme du texte, y compris la définition des propriétés du texte telles que la taille de police, le type, la couleur et le positionnement.
---

Ce guide explique comment ajouter du texte aux documents PDF en utilisant Aspose.PDF for Python via .NET. Vous apprendrez les techniques fondamentales d’insertion de texte — de la mise en place d’un simple fragment de texte à une position spécifique, à son style (police, taille, couleur, style), la gestion des langues de droite à gauche (RTL), l’intégration d’hyperliens, et le travail avec les mises en page de paragraphes, les listes et les effets de transparence. L’article couvre également des scénarios avancés tels que l’utilisation de fragments HTML ou LaTeX, les polices personnalisées et les options de mise en forme du texte comme l’interlignage et l’espacement des caractères.

Que vous créiez des annotations simples ou des mises en page typographiques riches, cette ressource vous fournit les éléments de base essentiels pour travailler avec le texte dans les PDF à l’aide d’Aspose.PDF.

## Insertion de texte de base

Aspose.PDF for Python via .NET fournit une API puissante et flexible pour gérer le texte à l'intérieur des fichiers PDF.
Que vous ayez besoin d'étiquettes statiques simples, de contenu richement formaté, de texte multilingue ou d'hyperliens interactifs, la boîte à outils vous permet de tout faire avec un code Python concis.

### Ajouter du texte – Cas simple

Aspose.PDF for Python via .NET montre comment ajouter un fragment de texte simple à une position spécifique sur une page. Vous apprendrez à créer un nouveau document PDF, ajouter une page, insérer du texte à des coordonnées données et enregistrer le fichier résultant.

1. Créez un nouvel objet [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Utilisez `document.pages.add()` pour créer une nouvelle [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) vierge.
1. Créez un [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) avec le contenu texte.
1. Définissez la position du texte à l'aide de la classe [`Position`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/position/). Si vous spécifiez `Position`, le texte sera placé dans votre document de gauche à droite et décalé vers le bas.
1. Personnalisez l'apparence du texte. Vous pouvez définir la taille de police, la couleur, le style de police, et plus via le [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/).
1. Ajoutez le `TextFragment` à la collection de paragraphes de la page avec `page.paragraphs.add(text_fragment)`.
1. Enregistrez le document.

Le fragment de code suivant vous montre comment ajouter du texte dans un fichier PDF existant :

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_simple_case(outfile):
    """
    Add simple text to a PDF document.
    Creates a new PDF document with a single page and adds a text fragment
    "Hello, Aspose!" at position (100, 600) on the page.
    Args:
        outfile (str): The file path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file.
    Example:
        >>> add_text_simple_case("output.pdf")
        # Creates a PDF file named "output.pdf" with "Hello, Aspose!" text
    """

    # Create a new document
    document = ap.Document()
    page = document.pages.add()

    # Add a text fragment at a specific position
    text_fragment = ap.text.TextFragment("Hello, Aspose!")
    text_fragment.position = ap.text.Position(100, 600)

    page.paragraphs.add(text_fragment)
    document.save(outfile)
```

Cet exemple de code utilise un TextFragment. Mais vous pouvez également ajouter du texte à une page PDF en utilisant un TextParagraph. Explorons la différence.
Le **[TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/)** est une seule unité de texte. TextFragment représente une unité unique de texte — essentiellement une chaîne de texte qui peut être placée, stylisée et positionnée indépendamment. Il est idéal lorsque vous devez ajouter de petites quantités de texte simples.

Le **[TextParagraph](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/)** est un groupe de TextFragments. Il peut ajouter plusieurs lignes de texte. TextParagraph est un conteneur ou une collection d'un ou plusieurs objets TextFragment. Il est idéal lorsque vous devez regrouper plusieurs fragments — par exemple, pour créer un bloc de texte avec plusieurs lignes, mots ou éléments formatés.
Un TextParagraph gère également l'alignement du texte, l'interligne et la mise en page automatique sur la page. L'utilisation de la ligne rouge n'est possible qu'avec TextParagraph.

Pour plus d'informations sur le travail avec le texte, veuillez consulter les sections de documentation [Mise en forme du texte dans PDF](/pdf/python-net/text-formatting-inside-pdf/) et [Extraire du texte du PDF avec Python](/pdf/python-net/extract-text-from-pdf/).

### Ajouter du texte en utilisant TextParagraph

Aspose.PDF for Python via .NET peut ajouter un paragraphe de texte en utilisant [`TextBuilder`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textbuilder/) et [`TextParagraph`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/) avec des options d'habillage.

1. Créez un nouveau [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) et une [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) vierge en utilisant `document.pages.add()`.
1. Lisez le texte à partir d'un fichier ou utilisez le texte par défaut.
1. Créez un [`TextBuilder`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textbuilder/) pour ajouter du contenu au niveau du paragraphe avec contrôle de la mise en page et de l'habillage.
1. Créez un [`TextParagraph`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/) et définissez le mode d'habillage (l'exemple utilise `DISCRETIONARY_HYPHENATION`).
1. Créez un [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/), appliquez des styles et ajoutez le fragment au paragraphe.
1. Ajoutez le paragraphe à la page en utilisant le `TextBuilder`.
1. Enregistrez le document.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_paragraph(outfile):
    """
    Add formatted text paragraph with indentation and wrapping to a PDF document.

    Creates a PDF document with a text paragraph that demonstrates advanced text
    formatting including first line indentation, text wrapping with discretionary
    hyphenation, and loading text content from an external file.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Attempts to load text from "lorem.txt" file in DATA_DIR
        - Falls back to default message if file doesn't exist
        - Uses Times New Roman font at 12pt size
        - First line indent: 20 points
        - Rectangle bounds: (80, 800, 400, 200)
        - Text wrapping: DISCRETIONARY_HYPHENATION mode for better line breaks

    Example:
        >>> add_text_paragraph("paragraph_text.pdf")
        # Creates a PDF with formatted paragraph text
    """
    document = ap.Document()
    page = document.pages.add()

    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    if os.path.exists(lorem_path):
        with open(lorem_path, "r", encoding="utf-8") as file:
            text = file.read()
    else:
        text = "Lorem ipsum sample text not found."

    builder = ap.text.TextBuilder(page)
    paragraph = ap.text.TextParagraph()
    paragraph.first_line_indent = 20
    paragraph.rectangle = ap.Rectangle(80, 800, 400, 200, True)
    # paragraph.formatting_options.wrap_mode = TextFormattingOptions.WordWrapMode.BY_WORDS
    paragraph.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.DISCRETIONARY_HYPHENATION
    )

    fragment = ap.text.TextFragment(text)
    fragment.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    fragment.text_state.font_size = 12

    paragraph.append_line(fragment)
    builder.append_paragraph(paragraph)

    document.save(outfile)
```

![Ajouter du texte en utilisant TextParagraph](text_paragraph.png)

### Ajouter des paragraphes avec des retraits dans le PDF

Le fragment de code suivant montre comment créer un nouveau document PDF et ajouter deux paragraphes de texte avec différents styles d'indentation :

- Le premier paragraphe montre un retrait de première ligne (seule la première ligne est indentée).

- Le deuxième paragraphe montre un retrait des lignes suivantes (toutes les lignes après la première sont indentées).

Il utilise les classes 'TextParagraph', 'TextBuilder' et 'TextFragment' d'Aspose.PDF pour contrôler précisément la mise en page et le formatage.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_paragraphs_indents(output_file_name):
    """Add text with indents to a PDF document.
    Creates a PDF document with two text paragraphs demonstrating different
    indent styles. The first paragraph uses first line indent, while the
    second paragraph uses subsequent lines indent. Text content is loaded
    from a lorem.txt file if available, otherwise uses a fallback message.
    Args:
        output_file_name (str): The file path where the PDF document will be saved.
    Returns:
        None: The function saves the PDF document to the specified output file.
    Note:
        - Uses Times New Roman font at 12pt size
        - Text wrapping is set to wrap by words
        - First paragraph: 20pt first line indent, positioned at (80, 800, 300, 50)
        - Second paragraph: 20pt subsequent lines indent, positioned at (320, 800, 500, 50)
    """

    document = ap.Document()
    page = document.pages.add()

    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    if os.path.exists(lorem_path):
        with open(lorem_path, "r", encoding="utf-8") as file:
            text = file.read()
    else:
        text = "Lorem ipsum sample text not found."

    fragment = ap.text.TextFragment(text)
    fragment.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    fragment.text_state.font_size = 12

    builder = ap.text.TextBuilder(page)
    paragraph1 = ap.text.TextParagraph()
    paragraph1.first_line_indent = 20
    paragraph1.rectangle = ap.Rectangle(80, 800, 300, 50, True)
    paragraph1.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )

    paragraph1.append_line(fragment)
    builder.append_paragraph(paragraph1)

    paragraph2 = ap.text.TextParagraph()
    paragraph2.subsequent_lines_indent = 20
    paragraph2.rectangle = ap.Rectangle(320, 800, 500, 50, True)
    paragraph2.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )

    paragraph2.append_line(fragment)
    builder.append_paragraph(paragraph2)
    document.save(output_file_name)
```

### Ajouter une nouvelle ligne de texte dans le PDF

Aspose.PDF for Python via .NET vous permet d'insérer du texte multiligne dans un document PDF en utilisant les classes TextFragment, TextParagraph et TextBuilder.

1. Créez un nouveau document.
1. Définissez un TextFragment contenant un caractère de nouvelle ligne.
1. Définissez le style du texte.
1. Ajoutez le fragment à un paragraphe.
1. Positionnez le paragraphe.
1. Rendre le paragraphe sur la page.
1. Enregistrez le document.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_new_line(output_file):
    """Add a new line of text to a PDF document."""
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Initialize new TextFragment with text containing required newline markers
    text_fragment = ap.text.TextFragment("Applicant Name: " + os.linesep + " Joe Smoe")

    # Set text fragment properties if necessary
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
    text_fragment.text_state.background_color = ap.Color.light_gray
    text_fragment.text_state.foreground_color = ap.Color.red

    # Create TextParagraph object
    par = ap.text.TextParagraph()

    # Add new TextFragment to paragraph
    par.append_line(text_fragment)

    # Set paragraph position
    par.position = ap.text.Position(100, 600)

    # Create TextBuilder object
    text_builder = ap.text.TextBuilder(page)

    # Add the TextParagraph using TextBuilder
    text_builder.append_paragraph(par)

    # Save PDF document
    document.save(output_file)
```

### Déterminer les sauts de ligne et consigner les notifications dans un PDF

Il montre comment créer un document PDF contenant plusieurs fragments de texte et activer la journalisation des notifications Aspose.PDF pour surveiller les événements de mise en page — tels que les sauts de ligne et le retour à la ligne du texte — pendant le rendu.

1. Créez un nouveau document PDF.
1. Activez la journalisation des notifications.
1. Utilisez document.pages.add() pour créer la première page.
1. Ajoutez plusieurs fragments de texte.
1. Utilisez page.paragraphs.add(text) pour rendre chaque fragment de texte.
1. Enregistrez le document.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def determine_line_break(output_file):
    """Create a PDF document with multiple text fragments and log notifications."""
    # Create PDF document
    document = ap.Document()

    # Enable notification logging
    document.enable_notification_logging = True

    page = document.pages.add()

    for i in range(4):
        text = ap.text.TextFragment(
            "Lorem ipsum \r\ndolor sit amet, consectetur adipiscing elit, "
            "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
            "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris "
            "nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in "
            "reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla "
            "pariatur. Excepteur sint occaecat cupidatat non proident, sunt in "
            "culpa qui officia deserunt mollit anim id est laborum."
        )
        text.text_state.font_size = 20
        page.paragraphs.add(text)

    # Save PDF document
    document.save(output_file)

    notifications = document.pages[1].get_notifications()
    print(notifications)
```

### Mesurer dynamiquement la largeur du texte dans un PDF

Mesurez dynamiquement la largeur des caractères et des chaînes dans une police spécifique en utilisant Aspose.PDF pour Python via .NET. Il utilise les méthodes 'Font.measure_string()' et 'TextState.measure_string()' pour vérifier que les largeurs de chaîne mesurées sont cohérentes et précises.

1. Utilisez 'FontRepository.find_font()' pour récupérer l'objet police Arial depuis le dépôt.
1. Créez un objet TextState pour gérer les propriétés de police.
1. Mesurez les caractères individuels.
1. Comparez les résultats des deux méthodes pour tous les caractères entre 'A' et 'z'.
1. Assurez-vous que les deux approches de mesure donnent les mêmes résultats.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_text_width_dynamically(output_file):

    font = ap.text.FontRepository.find_font("Arial")
    ts = ap.text.TextState()
    ts.font = font
    ts.font_size = 14

    if math.fabs(font.measure_string("A", 14) - 9.337) > 0.001:
        print("Unexpected font string measure!")

    if math.fabs(ts.measure_string("z") - 7.0) > 0.001:
        print("Unexpected font string measure!")

    c_code = ord("A")
    while c_code <= ord("z"):
        c = chr(c_code)

        fn_measure = font.measure_string(str(c), 14)
        ts_measure = ts.measure_string(str(c))

        if math.fabs(fn_measure - ts_measure) > 0.001:
            print("Font and state string measuring doesn't match!")

        c_code += 1
```

### Ajouter du texte avec des hyperliens

Ajoutez des hyperliens cliquables au texte dans un PDF en utilisant Aspose.PDF pour Python via .NET. Notre bibliothèque montre comment ajouter plusieurs segments de texte au sein d'un seul TextFragment et appliquer un hyperlien à un segment spécifique, et styliser les segments de texte individuellement (par ex., couleur, police italique).

1. Créez un nouveau document et une page en utilisant 'Document()', et 'document.pages.add()' pour ajouter une page vierge.
1. Créez un TextFragment.
1. Ajoutez plusieurs objets TextSegment. Chaque segment peut avoir son propre contenu et style. Par exemple du texte simple ou du texte hyperlié.
1. Appliquez un hyperlien à un segment. Créez un objet WebHyperlink avec l'URL souhaitée.
1. Stylisez le segment. Personnalisez la couleur, le style de police, la taille, etc., en utilisant text_state.
1. Ajoutez le fragment à la page en utilisant 'page.paragraphs.add()'.
1. Enregistrez le PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_with_hyperlink(outfile):
    """
    Add text with embedded hyperlinks to a PDF document.

    Creates a PDF document with a text fragment containing multiple segments,
    including one with a hyperlink to Aspose. Demonstrates how to create
    clickable links within PDF text content with different formatting.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Creates 4 text segments within a single text fragment
        - One segment contains a hyperlink to "https://products.aspose.com/pdf"
        - Hyperlinked text is styled in blue italic font
        - Other segments are regular text without links

    Example:
        >>> add_text_with_hyperlink("hyperlink_text.pdf")
        # Creates a PDF with clickable Aspose link in the text
    """

    document = ap.Document()
    page = document.pages.add()

    fragment = ap.text.TextFragment(
        "Sample Text Fragment"
    )

    segment = ap.text.TextSegment(" ... Text Segment 1...")
    fragment.segments.append(segment)

    segment = ap.text.TextSegment("Link to Aspose")
    fragment.segments.append(segment)
    segment.hyperlink = ap.WebHyperlink("https://products.aspose.com/pdf")
    segment.text_state.foreground_color = ap.Color.blue
    segment.text_state.font_style = ap.text.FontStyles.ITALIC

    segment = ap.text.TextSegment("TextSegment without hyperlink")
    fragment.segments.append(segment)

    page.paragraphs.add(fragment)
    document.save(outfile)
```

![Fragment de texte affiché dans un PDF montrant un contenu mixte avec Sample Text Fragment suivi de Text Segment 1, puis un texte hyperlié bleu lisant Link to Aspose (liant à https://products.aspose.com/pdf), et se terminant par TextSegment sans hyperlien en formatage de texte noir régulier](hyperlink_text.png)

### Ajouter du texte de droite à gauche (RTL) à un document PDF

RTL (de droite à gauche) est une propriété qui indique la direction d'écriture du texte, où le texte est écrit de droite à gauche.
Aspose.PDF pour Python via .NET. montre comment ajouter du texte de droite à gauche (RTL), tel que l'arabe ou l'hébreu, à un document PDF.

1. Créez un nouveau document et une page en utilisant 'Document()', et 'document.pages.add()' pour ajouter une page vierge.
1. Créez un TextFragment avec du contenu RTL. Insérez votre texte en arabe, hébreu ou autre langue RTL comme contenu du fragment.
Définissez la police et le style. Choisissez une police qui prend en charge l'écriture RTL (par ex., Tahoma, Arial Unicode MS). Réglez font_size et foreground_color selon les besoins.
1. Définissez l'alignement horizontal à droite en utilisant 'text_fragment.horizontal_alignment'.
1. Ajoutez le fragment de texte à la page.
1. Enregistrez le document PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_with_rtl_text(outfile):
    """
    Add right-to-left (RTL) text to a PDF document.

    Creates a PDF document with Arabic text that demonstrates right-to-left text
    rendering and alignment. The text uses the Tahoma font which supports Arabic
    characters and is aligned to the right side of the page.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses Tahoma font at 14pt size for proper Arabic character support
        - Text color is set to blue
        - Horizontal alignment is set to RIGHT for proper RTL display
        - The Arabic text describes Nasreddin Hodja, a folklore character

    Example:
        >>> add_text_with_rtl_text("arabic_text.pdf")
        # Creates a PDF with right-to-left Arabic text
    """

    document = ap.Document()
    page = document.pages.add()
    # Styled text fragment
    text_fragment = ap.text.TextFragment(
        "يعتبر خوجا نصر الدين شخصية فولكلورية من الشرق الإسلامي وبعض شعوب البحر الأبيض المتوسط ​​والبلقان، وهو بطل القصص والحكايات القصيرة الفكاهية والساخرة، وأحيانًا الحكايات اليومية."
    )
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Tahoma")
    text_fragment.text_state.font_size = 14
    text_fragment.text_state.foreground_color = ap.Color.blue
    text_fragment.horizontal_alignment = ap.HorizontalAlignment.RIGHT

    page.paragraphs.add(text_fragment)
    document.save(outfile)
```

![Texte de droite à gauche](rtl_text.png)

## Stylisation du texte

### Ajouter du texte avec un style de police

Il s'agit d'un exemple plus avancé qui montre la stylisation du texte, la personnalisation des polices et le texte à format mixte (en utilisant des segments de texte en indice). Aspose.PDF explique comment appliquer des propriétés de police telles que la famille, la taille, la couleur, le gras, l'italique et le soulignement à un fragment de texte.
De plus, cet extrait de code montre comment utiliser plusieurs segments de texte au sein d'un même fragment pour créer des expressions textuelles complexes — par exemple, inclure des caractères en indice ou en exposant, souvent requis dans les formules ou les notations scientifiques.

1. Créez un nouveau document et une page en utilisant 'Document()', et 'document.pages.add()' pour ajouter une page vierge.
1. Créez un TextFragment pour du texte simplement stylisé.
1. Définissez le contenu du texte.
1. Définissez la position en utilisant les coordonnées Position(x, y).
1. Appliquer le style via la propriété 'text_state' - police, font_size, foreground_color, font_style, soulignement.
1. Créer une expression complexe avec plusieurs objets TextSegment. Chaque TextSegment représente une portion de texte qui peut avoir son propre style. Cela vous permet de construire des expressions, telles que des formules mathématiques ou chimiques.
1. Définir plusieurs objets TextState. Un pour le texte principal (text_state_letters). Un autre pour le texte en indice ou exposant (text_state_index).
1. Combiner les segments de texte. Ajouter chaque segment à un 'TextFragment' en utilisant 'segments.append()'.
1. Ajouter les deux objets texte à la page. Utiliser 'page.paragraphs.add()' pour les placer dans le document.
1. Enregistrer le document final.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_with_font_styling(outfile):
    """
    Add styled text fragments to a PDF document.
    Creates a new PDF document with a single page and adds a styled text fragment
    "Hello, Aspose!" at position (100, 600) and a formula with styled segments at position (100, 500).
    Args:
        outfile (str): The file path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file.
    Example:
        >>> add_text_with_font_styling("styled_text.pdf")
        # Creates a PDF file named "styled_text.pdf" with styled text and a formula
    """

    document = ap.Document()
    page = document.pages.add()

    # Initialize an empty TextFragment to build a formula using segments
    formula = ap.text.TextFragment()
    text_fragment = ap.text.TextFragment("Hello, Aspose!")
    text_fragment.position = ap.text.Position(100, 600)
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.text_state.foreground_color = ap.Color.blue
    text_fragment.text_state.font_style = (
        ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    )
    text_fragment.text_state.underline = True
    text_fragment.horizontal_alignment = ap.HorizontalAlignment.LEFT

    text_state_letters = ap.text.TextState()
    text_state_letters.font = ap.text.FontRepository.find_font("Arial")
    text_state_letters.font_size = 14
    text_state_letters.foreground_color = ap.Color.blue
    text_state_letters.font_style = ap.text.FontStyles.BOLD

    text_state_index = ap.text.TextState()
    text_state_index.font = ap.text.FontRepository.find_font("Arial")
    text_state_index.font_size = 14
    text_state_index.foreground_color = ap.Color.dark_red
    # text_state_index.superscript = True
    text_state_index.subscript = True

    position = ap.text.Position(100, 500)

    # Helper function to add segments
    def add_segment(text, state):
        seg = ap.text.TextSegment(text)
        seg.text_state = state
        seg.position = position
        formula.segments.append(seg)

    add_segment("S = a", text_state_letters)
    add_segment("2n", text_state_index)
    add_segment(" + a", text_state_letters)
    add_segment("2n+1", text_state_index)
    add_segment(" + a", text_state_letters)
    add_segment("2n+2", text_state_index)
    formula.horizontal_alignment = ap.HorizontalAlignment.LEFT

    page.paragraphs.add(text_fragment)
    page.paragraphs.add(formula)
    document.save(outfile)
```

![Fragment de texte affiché avec une police Arial italique bleue contenant le texte Hello, Aspose! suivi d’une formule mathématique montrant S = a subscript 2n + a subscript 2n+1 + a subscript 2n+2 avec texte principal bleu et formatage d’indice rouge](styled_text.png)

## Ajouter du texte transparent

Ajouter des formes semi-transparentes et du texte à un document PDF à l’aide d’Aspose.PDF pour Python.
Il crée un rectangle coloré avec une opacité partielle et superpose un TextFragment avec une couleur de premier plan transparente.

1. Initialiser un objet Document et ajouter une page vierge pour le dessin du contenu.
1. Utiliser 'ap.drawing.Graph' pour créer une toile qui vous permet de dessiner des formes.
1. Ajouter un rectangle avec un remplissage semi-transparent.
1. Empêcher le déplacement de la position du canvas.
1. Ajouter le canvas à la page. Insérer les formes graphiques dans la collection de paragraphes de la page.
1. Créer un fragment de texte transparent.
1. Insérer le fragment de texte dans la collection de paragraphes de la page.
1. Enregistrer le document PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_transparent(outfile):
    """
    Add transparent text over a semi-transparent background to a PDF document.

    Creates a PDF document with a semi-transparent filled rectangle as background
    and transparent green text overlaid on top. This demonstrates how to create
    transparency effects in PDF documents using ARGB color values.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Background rectangle: 128 alpha, light purple color (0xC5, 0xB5, 0xFF)
        - Text transparency: 30 alpha, green color (0, 255, 0)
        - The canvas is set to not change position to prevent layout shifts

    Example:
        >>> add_text_transparent("transparent_output.pdf")
        # Creates a PDF with transparent text effects
    """

    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Create Graph object
    canvas = ap.drawing.Graph(100.0, 400.0)

    # Create rectangle with semi-transparent fill
    rect = ap.drawing.Rectangle(100, 100, 400, 400)
    rect.graph_info.fill_color = ap.Color.from_argb(128, 0xC5, 0xB5, 0xFF)
    canvas.shapes.add(rect)

    # Prevent position shift
    canvas.is_change_position = False
    page.paragraphs.add(canvas)

    # Create transparent text
    text = ap.text.TextFragment(
        "This is the transparent text. "
        "This is the transparent text. "
        "This is the transparent text."
    )
    text.text_state.foreground_color = ap.Color.from_argb(30, 0, 255, 0)
    page.paragraphs.add(text)

    document.save(outfile)
```

### Ajouter du texte invisible au PDF

Cet exemple montre comment créer un document PDF contenant à la fois du texte visible et du texte invisible. Le texte invisible reste partie de la structure du document mais est caché de la vue, ce qui le rend utile pour incorporer des métadonnées, des balises d'accessibilité ou du contenu recherchable sans affecter la mise en page.

1. Créer un document PDF et une page.
1. Créer un fragment de texte avec du contenu visible répété.
1. Ajouter un deuxième fragment de texte et le marquer comme invisible.
1. Enregistrer le document.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_invisible(outfile):
    """
    Creates a PDF document with both visible and invisible text.
    This function generates a PDF file containing two text fragments:
    one visible text that will be displayed normally, and one invisible
    text that will be hidden from view but still present in the document.
    Args:
        outfile (str): The file path where the PDF document will be saved.
    Returns:
        None: The function saves the PDF to the specified file path.
    Example:
        add_text_invisible("output.pdf")
    """

    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Add visible text
    text1 = ap.text.TextFragment(
        "This is the visible text. "
        "This is the visible text. "
        "This is the visible text."
    )
    page.paragraphs.add(text1)

    # Create transparent text
    text2 = ap.text.TextFragment(
        "This is the invisible text. "
        "This is the invisible text. "
        "This is the invisible text."
    )
    text2.text_state.invisible = True
    page.paragraphs.add(text2)

    document.save(outfile)
```

### Ajouter du texte avec un style de bordure dans le PDF

La bibliothèque Aspose.PDF montre comment créer un document PDF contenant un fragment de texte stylisé avec une bordure visible. La méthode applique des couleurs d'arrière-plan et de premier plan, des paramètres de police, et un trait (bordure) autour du rectangle du texte pour renforcer l'accent visuel.

1. Créer un document PDF et une page.
1. Créer et positionner le fragment de texte. Ajouter un fragment de texte avec le message et définir sa position.
1. Appliquer le style du texte. Définir la police à Times New Roman, taille 12. Appliquer un arrière-plan gris clair et une couleur de premier plan (texte) rouge.
1. Configurer le style de la bordure.
1. Ajouter du texte à la page. Utiliser TextBuilder pour ajouter le texte stylisé à la page.
1. Enregistrer le document.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_border(output_file_name):
    """
    Add text with border styling to a PDF document.

    Creates a PDF document with a text fragment that has border styling applied.
    The text includes background color, foreground color, and a configurable
    border (stroke) around the text rectangle.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Text: "This is sample text with border."
        - Font: Times New Roman, 12pt
        - Background: Light gray
        - Foreground: Red text
        - Border: Dark red stroke around text rectangle
        - Position: (10, 700)
        - Border is only visible when draw_text_rectangle_border is True

    Example:
        >>> add_text_border("bordered_text.pdf")
        # Creates a PDF with bordered text styling
    """
    # Create PDF document
    document = ap.Document()
    # Get particular page
    page = document.pages.add()
    # Create text fragment
    text_fragment = ap.text.TextFragment("This is sample text with border.")
    text_fragment.position = ap.text.Position(10, 700)

    # Set text properties
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.background_color = ap.Color.light_gray
    text_fragment.text_state.foreground_color = ap.Color.red
    # Set StrokingColor property for drawing border (stroking) around text rectangle.
    # Note: This only affects the border if draw_text_rectangle_border is set to True.
    text_fragment.text_state.stroking_color = ap.Color.dark_red
    # Enable drawing of the text rectangle border
    text_fragment.text_state.draw_text_rectangle_border = True

    text_builder = ap.text.TextBuilder(page)
    text_builder.append_text(text_fragment)

    # Save PDF document
    document.save(output_file_name)
```

### Ajouter du texte barré à un PDF

Ajouter un format de texte barré (strikethrough) à un fragment de texte dans un document PDF. Le texte barré est utile pour indiquer des suppressions, des révisions ou un accent dans les documents annotés.

1. Créer un nouveau document et une page en utilisant 'Document()', et 'document.pages.add()' pour ajouter une page vierge.
1. Créer et styliser le fragment de texte.
1. Appliquer la couleur et le format barré. Définir l'arrière-plan en gris clair, la couleur du texte en rouge, et activer le barré.
1. Positionner le texte.
1. Utiliser 'TextBuilder' pour ajouter le texte stylisé à la page.
1. Enregistrer le document.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_strikeout_text(output_file_name):
    """
    Add text with strikeout (strikethrough) formatting to a PDF document.

    Creates a PDF document with a text fragment that has strikeout formatting applied.
    The text appears with a line through it, along with additional styling including
    background color, foreground color, and bold font style.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Text: "This is sample strikeout text."
        - Font: Times New Roman, 12pt, Bold
        - Background: Light gray
        - Foreground: Red text
        - Strikeout: Enabled (line through text)
        - Position: (100, 600)

    Example:
        >>> add_strikeout_text("strikeout_text.pdf")
        # Creates a PDF with strikethrough text formatting
    """
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Create text fragment
    text_fragment = ap.text.TextFragment("This is sample strikeout text.")
    # Set text properties
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
    text_fragment.text_state.background_color = ap.Color.light_gray
    text_fragment.text_state.foreground_color = ap.Color.red
    text_fragment.text_state.strike_out = True
    text_fragment.text_state.font_style = ap.text.FontStyles.BOLD
    text_fragment.position = ap.text.Position(100, 600)

    # Create TextBuilder object
    text_builder = ap.text.TextBuilder(page)
    text_builder.append_text(text_fragment)

    # Save PDF document
    document.save(output_file_name)
```

## Effets de couleur avancés

### Appliquer un dégradé axial au texte dans un PDF

Aspose.PDF for Python via .NET démontre comment appliquer un effet de dégradé linéaire au texte dans un document PDF. Le dégradé axial passe en douceur du rouge au bleu sur l’ensemble du texte, créant un titre visuellement saisissant. Cette technique est idéale pour les titres stylisés, le branding ou les éléments décoratifs dans les mises en page de documents PDF.

1. Initialiser un nouveau document et ajouter une page vierge.
1. Créer et styliser le fragment de texte. Ajouter le titre, définir la position, la police et la taille.
1. Appliquer un dégradé axial avec 'GradientAxialShading'. Définir la couleur de premier plan en utilisant GradientAxialShading du rouge au bleu.
1. Ajouter le style de soulignement.
1. Insérer le fragment de texte stylisé dans la page.
1. Enregistrer le document.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def apply_gradient_axial_shading_to_text(output_file_name):
    """
    Apply axial gradient shading to text in a PDF document.

    Creates a PDF document with large title text that has an axial (linear) gradient
    effect applied. The gradient transitions from red to blue in a linear fashion
    across the text. This demonstrates advanced text styling with gradient effects.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Text: "PDF TITLE"
        - Font: Arial Bold, 36pt
        - Position: (100, 600)
        - Gradient: Linear gradient from red to blue
        - Additional styling: Underlined text
        - Uses GradientAxialShading for linear gradient effect

    Example:
        >>> apply_gradient_axial_shading_to_text("gradient_axial.pdf")
        # Creates a PDF with linear gradient text effect
    """
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("PDF TITLE")
    text_fragment.position = ap.text.Position(100, 600)
    text_fragment.text_state.font_size = 36
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial Bold")

    text_fragment.text_state.foreground_color = ap.Color()
    text_fragment.text_state.foreground_color.pattern_color_space = (
        ap.drawing.GradientAxialShading(ap.Color.red, ap.Color.blue)
    )
    text_fragment.text_state.underline = True

    page.paragraphs.add(text_fragment)
    document.save(output_file_name)
```

### Appliquer un dégradé radial au texte dans un PDF

Un dégradé radial crée une transition de couleur circulaire qui rayonne depuis le centre du texte, offrant une option de style visuellement dynamique pour les titres, en-têtes ou éléments décoratifs.

1. Initialisez un nouveau document et ajoutez une page vierge.
1. Créez et stylisez un fragment de texte. Ajoutez le titre, définissez la position, la police et la taille.
1. Appliquez un dégradé radial avec 'GradientRadialShading'. Définissez la couleur de premier plan en utilisant GradientRadialShading du rouge au bleu.
1. Ajoutez le style souligné.
1. Insérez le fragment de texte stylisé dans la page.
1. Enregistrez le document.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def apply_gradient_radial_shading_to_text(output_file_name):
    """
    Apply radial gradient shading to text in a PDF document.

    Creates a PDF document with large title text that has a radial (circular) gradient
    effect applied. The gradient radiates from the center outward, transitioning from
    red to blue. This demonstrates advanced text styling with radial gradient effects.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Text: "PDF TITLE"
        - Font: Arial Bold, 36pt
        - Position: (100, 600)
        - Gradient: Radial gradient from red to blue
        - Additional styling: Underlined text
        - Uses GradientRadialShading for circular gradient effect

    Example:
        >>> apply_gradient_radial_shading_to_text("gradient_radial.pdf")
        # Creates a PDF with radial gradient text effect
    """
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("PDF TITLE")
    text_fragment.position = ap.text.Position(100, 600)
    text_fragment.text_state.font_size = 36
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial Bold")

    # Apply radial gradient shading (red to blue)
    text_fragment.text_state.foreground_color = ap.Color()
    text_fragment.text_state.foreground_color.pattern_color_space = (
        ap.drawing.GradientRadialShading(ap.Color.red, ap.Color.blue)
    )
    text_fragment.text_state.underline = True

    page.paragraphs.add(text_fragment)
    document.save(output_file_name)
```

![Appliquer le dégradé radial](gradient_radial_shading.png)

## Fragments HTML et LaTeX

### Ajouter du texte HTML à un document PDF

La bibliothèque Aspose.PDF for Python via .NET vous permet d’insérer du contenu formaté en HTML dans un document PDF en utilisant la classe HtmlFragment. En utilisant les balises HTML, vous pouvez rendre du texte stylisé, structuré ou semblable à une formule directement dans un PDF.

1. Créez un nouveau document et une page en utilisant 'Document()', et 'document.pages.add()' pour ajouter une page vierge.
1. Créez une instance de la classe HtmlFragment et passez votre chaîne HTML comme paramètre.
1. Ajoutez le fragment à la page en utilisant 'page.paragraphs.add()' pour insérer le contenu HTML.
1. Enregistrez le PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_html_fragment(outfile):
    """
    Add HTML fragment with mathematical notation to a PDF document.

    Creates a PDF document containing an HTML fragment that displays mathematical
    notation using HTML tags including subscript and superscript elements.
    This demonstrates how to embed formatted HTML content directly into PDF.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses HTML <pre> tags to preserve formatting
        - Includes <sub> for subscript (2n) and <sup> for superscript (2)
        - Formula displayed: S=a₂ₙ+a²
        - HTML is rendered as formatted content within the PDF

    Example:
        >>> add_text_html_fragment("html_math.pdf")
        # Creates a PDF with HTML mathematical notation
    """

    # Create a new document
    document = ap.Document()
    page = document.pages.add()

    # Add a text fragment at a specific position
    text_fragment = ap.HtmlFragment("<pre>S=a<sub>2n</sub>+a<sup>2</sup><pre>")

    page.paragraphs.add(text_fragment)
    document.save(outfile)
```

![Ajouter du texte HTML à un document PDF](html_fragment.png)

### Ajouter un fragment HTML stylisé avec divers formats à un document PDF

Nous pouvons définir un fragment HTML et appliquer le style du texte directement à l’aide des balises HTML. Intégrez du contenu HTML stylisé dans un document PDF. Cet extrait de code crée un nouveau fichier PDF, ajoute une page, insère un fragment HTML contenant divers éléments de mise en forme (titres, paragraphes, liens et styles en ligne), et enregistre le résultat à l’emplacement spécifié.

1. Initialise un nouvel objet Document pour représenter le PDF.
1. Ajoute une page vierge au document où le contenu HTML sera placé.
1. Préparez le contenu HTML. La chaîne HTML contient un titre h1, un paragraphe vert avec du texte en gras, italique et souligné, ainsi qu’un lien hypertexte vers un site web avec une taille de police augmentée.
1. Créez un fragment HTML. Enveloppez la chaîne HTML dans un objet HtmlFragment.
1. Insérez le HTML dans la page. Ajoute le fragment HTML à la collection de paragraphes de la page, rendant le HTML comme contenu PDF natif.
1. Enregistrez le document.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_html_fragment(outfile):
    """
    Add styled HTML fragment with various formatting to a PDF document.

    Creates a PDF document containing rich HTML content including headings,
    paragraphs with inline formatting, colored text, and hyperlinks.
    Demonstrates comprehensive HTML rendering capabilities in PDF.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Includes HTML heading (h1) with blue color styling
        - Contains paragraph with bold, italic, and underlined text
        - Features green-colored paragraph text
        - Includes styled hyperlink to Aspose website
        - All HTML styling is preserved in the PDF output

    Example:
        >>> add_html_fragment("rich_html.pdf")
        # Creates a PDF with various HTML formatting elements
    """

    document = ap.Document()
    page = document.pages.add()
    html_content = """
        <h1 style='color:blue;'>Hello, Aspose!</h1>
        <p>This is a sample paragraph with <b>bold</b>, <i>italic</i>, and <u>underlined</u> text.</p>
        <p style='color:green;'>This paragraph is green.</p>
        <a href='https://www.aspose.com' style='font-size:16px;'>Visit Aspose</a>
    """
    html_fragment = ap.HtmlFragment(html_content)
    page.paragraphs.add(html_fragment)
    document.save(outfile)
```

![Ajouter du contenu HTML à un document PDF](html_content.png)

### Ajouter un fragment HTML avec un état de texte remplacé

Comme nous l’avons vu dans l’exemple précédent, il est possible de définir les styles directement dans le code HTML. Cela présente des avantages, mais aussi quelques inconvénients. Supposons que nous travaillions avec le HTML d’un client et que nous voulions unifier l’apparence de notre sortie.
Dans ce cas, nous pouvons remplacer le style du client en utilisant notre propre TextState, comme le montre l’exemple suivant.

1. Créez un nouveau document et une page en utilisant 'Document()', et 'document.pages.add()' pour ajouter une page vierge.
1. Préparez le contenu HTML. La chaîne HTML contient un titre h1 avec la police Verdana, un paragraphe vert avec du texte en gras, italique et souligné, ainsi qu’un lien hypertexte vers un site web avec une taille de police plus grande.
1. Créez un fragment HTML. Enveloppez la chaîne HTML dans un objet HtmlFragment.
1. Remplacez le formatage du texte. Créez un objet TextState et définissez la police, la taille de police et la couleur du texte.
1. Ajoutez le fragment HTML à la collection de paragraphes de la page.
1. Enregistrez le document.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_html_fragment_override_text_state(outfile):
    """
    Add HTML fragment with overridden text styling to a PDF document.

    Creates a PDF document with HTML content where the default text styling
    is overridden using TextState properties. This demonstrates how to apply
    global text formatting that supersedes HTML styling for consistent appearance.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - HTML includes heading, paragraphs, and links with original styling
        - TextState override applies: Arial font, 14pt size, red color
        - Override styling takes precedence over HTML inline styles
        - Useful for enforcing consistent document-wide text appearance
        - Original HTML styling is replaced by the TextState properties

    Example:
        >>> add_html_fragment_override_text_state("html_override.pdf")
        # Creates a PDF where HTML styling is overridden with red Arial text
    """

    document = ap.Document()
    page = document.pages.add()
    html_content = """
        <h1 style='color:blue;font-family:Verdana'>Hello, Aspose!</h1>
        <p>This is a sample paragraph with <b>bold</b>, <i>italic</i>, and <u>underlined</u> text.</p>
        <p style='color:green;'>This paragraph is green.</p>
        <a href='https://www.aspose.com' style='font-size:16px;'>Visit Aspose</a>
    """
    html_fragment = ap.HtmlFragment(html_content)
    html_fragment.text_state = ap.text.TextState()
    html_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    html_fragment.text_state.font_size = 14
    html_fragment.text_state.foreground_color = ap.Color.red

    page.paragraphs.add(html_fragment)
    document.save(outfile)
```

![Ajouter un fragment HTML avec état de texte remplacé](html_override.png)

### Ajouter du texte LaTeX à un document PDF

Ajoutez des expressions mathématiques formatées en LaTeX à un document PDF en utilisant la classe TeXFragment dans Aspose.PDF for Python via .NET.
LaTeX est un puissant système de composition largement utilisé pour créer des documents scientifiques et mathématiques. En utilisant TeXFragment, vous pouvez rendre directement la notation mathématique LaTeX et les symboles à l’intérieur d’une page PDF.

1. Créez un nouveau document et une page en utilisant 'Document()', et 'document.pages.add()' pour ajouter une page vierge.
1. Utilisez la classe TeXFragment pour rendre directement la syntaxe LaTeX.
1. Ajoutez le contenu LaTeX à la mise en page du PDF avec 'page.paragraphs.add()'.
1. Enregistrez le PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_latex_fragment(outfile):
    """
    Add LaTeX mathematical expression to a PDF document.

    Creates a PDF document containing a complex mathematical expression rendered
    from LaTeX markup. This demonstrates advanced mathematical typesetting
    capabilities using LaTeX syntax within PDF documents.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses LaTeX TeXFragment for mathematical expression rendering
        - Expression includes overbrace and underbrace notation
        - Formula: (a+b)⁶ · (c+d)⁷ with braces and labels = 42
        - LaTeX commands: \\overbrace, \\underbrace, \\text, \\cdot
        - Provides professional mathematical typography

    Example:
        >>> add_text_latex_fragment("latex_math.pdf")
        # Creates a PDF with complex LaTeX mathematical expression
    """

    # Create a new document
    document = ap.Document()
    page = document.pages.add()

    # Add a text fragment at a specific position
    text_fragment = ap.TeXFragment(
        "\\underbrace{\\overbrace{a+b}^6 \\cdot \\overbrace{c+d}^7}_\\text{example of text} = 42"
    )

    page.paragraphs.add(text_fragment)
    document.save(outfile)
```

![Expression mathématique complexe affichée dans un PDF montrant la formule LaTeX avec notation overbrace au-dessus de (a+b)⁶, notation underbrace sous l’ensemble de l’expression (a+b)⁶·(c+d)⁷, étiquetée comme exemple de texte, et égale à 42. La formule démontre une composition mathématique avancée avec un espacement et un style de parenthèses typiques du rendu LaTeX](latex_fragment.png)

## Polices personnalisées

### Utiliser une police personnalisée depuis un fichier

Cet exemple vous permet d’ajouter du texte à un fichier PDF en utilisant une police OpenType personnalisée dans Aspose.PDF for Python via .NET. Il montre comment créer un nouveau document PDF, positionner le texte précisément sur la page, et appliquer un formatage personnalisé tel que le type de police, la taille, la couleur et le style italique.

1. Créez un nouveau document PDF et ajoutez une page.
1. Définissez le contenu texte que vous souhaitez ajouter au PDF.
1. Définissez la position du texte.
1. Ajoutez le TextFragment à la page.
1. Enregistrez le document PDF.

Cette fonction fonctionne non seulement avec les polices OTF mais aussi avec les polices TTF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def use_custom_font_from_file(outfile):
    """
    Creates a PDF document with text using a custom font loaded from a file.
    This function demonstrates how to load a custom OpenType font (.otf) from the file system
    and apply it to text in a PDF document. The text is styled with blue color, italic style,
    and positioned at specific coordinates on the page.
    Args:
        outfile (str): The output file path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file path.
    Note:
        - Requires the "BriosoPro Italic.otf" font file to be present in the DATA_DIR directory
        - Uses Aspose.PDF library for PDF generation and text manipulation
        - The text fragment is positioned at coordinates (100, 600) on the page
        - Font size is set to 24 points with blue foreground color and italic style
    """

    font_path = os.path.join(DATA_DIR, "BriosoPro Italic.otf")
    document = ap.Document()
    page = document.pages.add()

    fragment = ap.text.TextFragment("Hello, Aspose!")
    fragment.position = ap.text.Position(100, 600)
    fragment.text_state.font = ap.text.FontRepository.open_font(font_path)
    fragment.text_state.font_size = 24
    fragment.text_state.foreground_color = ap.Color.blue
    fragment.text_state.font_style = ap.text.FontStyles.ITALIC

    page.paragraphs.add(fragment)
    document.save(outfile)
```

![Fragment de texte affiché dans un document PDF montrant Hello, Aspose! rendu en bleu italique avec la police BriosoPro, démontrant l'intégration de police OpenType personnalisée et les capacités de style dans le formatage du texte PDF](custom_font.png)

### Utiliser une police personnalisée depuis un flux

Cet extrait de code montre comment ajouter du texte à un document PDF en utilisant une police OpenType (OTF) personnalisée intégrée avec Aspose.PDF pour Python via .NET. Il montre comment ouvrir un fichier de police en tant que flux, l'intégrer dans le PDF pour garantir la disponibilité de la police sur différents systèmes, et appliquer une mise en forme du texte telle que la taille de police, la couleur et le style italique. Cette approche est idéale pour créer des PDF visuellement cohérents qui préservent la typographie même lorsqu'ils sont partagés ou visualisés sur des appareils ne disposant pas de la police installée.

1. Chargez le fichier de police sous forme de flux binaire.
1. Ouvrez et intégrez la police en utilisant 'FontRepository.open_font'.
1. Créez un nouveau document PDF et ajoutez une page.
1. Ajoutez un fragment de texte stylisé avec :
- Police personnalisée intégrée.
- Style italique et couleur bleue.
- Taille de police et position spécifiques.
1. Enregistrez le document final dans un chemin de sortie spécifié.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def use_custom_font_from_stream(outfile):
    """Use custom font from stream."""

    font_path = os.path.join(DATA_DIR, "BriosoPro Italic.otf")
    with open(font_path, "rb") as font_stream:
        font = ap.text.FontRepository.open_font(font_stream, ap.text.FontTypes.OTF)
        font.is_embedded = True

        document = ap.Document()
        page = document.pages.add()

        fragment = ap.text.TextFragment("Hello, Aspose!")
        fragment.position = ap.text.Position(100, 600)
        fragment.text_state.font = font
        fragment.text_state.font_size = 14
        fragment.text_state.foreground_color = ap.Color.blue
        fragment.text_state.font_style = ap.text.FontStyles.ITALIC

        page.paragraphs.add(fragment)
        document.save(outfile)
```

L'intégration des polices garantit un rendu cohérent sur toutes les plateformes, ce qui rend cette approche idéale pour le branding, la fidélité du design et le support multilingue.

