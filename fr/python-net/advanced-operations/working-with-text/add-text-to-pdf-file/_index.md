---
title: Ajouter du texte à un PDF en Python
linktitle: Ajouter du texte à un PDF
type: docs
weight: 10
url: /fr/python-net/add-text-to-pdf-file/
description: Apprenez comment ajouter du texte, des fragments HTML, des listes, des liens et des polices personnalisées aux documents PDF en Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajoutez du texte, des liens, du HTML et des polices aux fichiers PDF avec Python
Abstract: Cet article explique comment ajouter et formater du texte dans les documents PDF en utilisant Aspose.PDF for Python via .NET. Il couvre les techniques de base telles que le positionnement du texte, l'application des paramètres de Font et de style, l'insertion de liens et de listes, ainsi que l'utilisation de HTML, LaTeX et de polices personnalisées dans les flux de travail Python.
---

Ce guide explique comment ajouter du texte aux documents PDF en utilisant Aspose.PDF for Python via .NET. Vous apprendrez les techniques essentielles d’insertion de texte — de placer un simple fragment de texte à une position précise, à le styliser (police, taille, couleur, style), à gérer les langues de droite à gauche (RTL), à incorporer des hyperliens, et à travailler avec les mises en page de paragraphes, les listes et les effets de transparence. L’article couvre également des scénarios avancés tels que l’utilisation de fragments HTML ou LaTeX, des polices personnalisées, et les options de mise en forme du texte comme l’interlignage et l’espacement des caractères.

Que vous créiez des annotations simples ou des mises en page typographiques riches, cette ressource vous fournit les blocs de construction fondamentaux pour travailler avec du texte dans les PDF en utilisant Aspose.PDF.

## Insertion de texte basique

Aspose.PDF for Python via .NET fournit une API puissante et flexible pour gérer le texte à l'intérieur des fichiers PDF.
Que vous ayez besoin d'étiquettes statiques simples, de contenu richement formaté, de texte multilingue ou de liens hypertexte interactifs, l'outil vous permet de tout faire avec un code Python concis.

### Ajouter du texte Cas simple

Aspose.PDF for Python via .NET montre comment ajouter un fragment de texte simple à une position spécifique sur une page. Vous apprendrez comment créer un nouveau document PDF, ajouter une page, insérer du texte à des coordonnées données et enregistrer le fichier résultant.

1. Créer un nouveau [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objet.
1. Utiliser `document.pages.add()` créer un nouveau vierge [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Créer un [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) avec le contenu du texte.
1. Définissez la position du texte en utilisant le [`Position`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/position/) classe. Si vous spécifiez `Position`, le texte sera situé dans votre document de gauche à droite et décalé vers le bas.
1. Personnalisez l'apparence du texte. Vous pouvez définir la taille de la police, la couleur, le style de police, et plus encore via le [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/).
1. Ajouter le `TextFragment` à la collection de paragraphes de la page avec `page.paragraphs.add(text_fragment)`.
1. Enregistrez le document.

Le fragment de code suivant vous montre comment ajouter du texte dans un fichier PDF existant :

```python
import math
import sys
import os
import aspose.pdf as ap

# region Basic text insertion
def add_text_simple_case(output_file_name):
    # Create a new document
    document = ap.Document()
    page = document.pages.add()

    # Add a text fragment at a specific position
    text_fragment = ap.text.TextFragment("Hello, Aspose!")
    text_fragment.position = ap.text.Position(100, 600)

    page.paragraphs.add(text_fragment)
    document.save(output_file_name)
```

Cet exemple de code utilise un TextFragment. Vous pouvez également ajouter du texte à une page PDF en utilisant un TextParagraph.
Le **[TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/)** est un morceau unique de texte. Il représente une chaîne de texte qui peut être placée, stylisée et positionnée indépendamment. C’est idéal lorsque vous devez ajouter un petit contenu textuel simple.

Le **[TextParagraph](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/)** est un groupe de TextFragments. Il peut ajouter plusieurs lignes de texte. TextParagraph est un conteneur ou une collection d’un ou plusieurs objets TextFragment. C’est idéal lorsque vous devez regrouper plusieurs fragments — par exemple, pour créer un bloc de texte contenant plusieurs lignes, mots ou éléments formatés.
Un TextParagraph gère également l'alignement du texte, l'espacement des lignes et la mise en page automatique sur la page. L'utilisation de la ligne rouge n'est possible qu'avec TextParagraph.

Pour plus d'informations sur le travail avec le texte, voir [Formatage du texte dans le PDF](/pdf/fr/python-net/text-formatting-inside-pdf/) et [Rechercher et extraire le texte du PDF](/pdf/fr/python-net/search-and-get-text-from-pdf/).

### Ajouter du texte à l'aide de TextParagraph

Aspose.PDF for Python via .NET peut ajouter un paragraphe de texte en utilisant [`TextBuilder`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textbuilder/) et [`TextParagraph`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/) avec des options d'enroulement.

1. Créer un nouveau [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) et un blanc [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) en utilisant `document.pages.add()`.
1. Lire le texte à partir d'un fichier ou utiliser le texte par défaut.
1. Créer un [`TextBuilder`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textbuilder/) pour ajouter du contenu au niveau du paragraphe avec contrôle de la mise en page et de l'habillage.
1. Créer un [`TextParagraph`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/) et définir le mode d'ajustement (l'exemple utilise `DISCRETIONARY_HYPHENATION`).
1. Créer un [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/), appliquez les styles, et ajoutez le fragment au paragraphe.
1. Ajoutez le paragraphe à la page en utilisant le `TextBuilder`.
1. Enregistrez le document.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_paragraph(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    lorem_path = LOREM_PATH
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

    document.save(output_file_name)
```

![Ajouter du texte à l'aide de TextParagraph](text_paragraph.png)

### Ajouter des paragraphes avec des retraits dans le PDF

Le fragment de code suivant montre comment créer un nouveau document PDF et ajouter deux paragraphes de texte avec différents styles d'indentation :

- Le premier paragraphe illustre un retrait de première ligne (seule la première ligne est en retrait).

- Le deuxième paragraphe montre une indentation des lignes suivantes (toutes les lignes après la première sont indentées).

Il utilise les classes 'TextParagraph', 'TextBuilder' et 'TextFragment' d'Aspose.PDF pour contrôler précisément la mise en page et le formatage.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_paragraphs_indents(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    lorem_path = LOREM_PATH
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

Aspose.PDF for Python via .NET vous permet d'insérer du texte multilignes dans un document PDF en utilisant les classes TextFragment, TextParagraph et TextBuilder.

1. Créer un nouveau document.
1. Définir un TextFragment contenant un caractère de saut de ligne.
1. Définir le style du texte.
1. Ajoutez le fragment à un paragraphe.
1. Positionnez le paragraphe.
1. Rendre le paragraphe sur la page.
1. Enregistrez le document.

```python
import math
import sys
import os
import aspose.pdf as ap

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

Il montre comment créer un document PDF contenant plusieurs fragments de texte et activer la journalisation des notifications Aspose.PDF pour surveiller les événements de mise en page — tels que les sauts de ligne et le retour à la ligne du texte — lors du rendu.

1. Créer un nouveau document PDF.
1. Activer la journalisation des notifications.
1. Utilisez document.pages.add() pour créer la première page.
1. Ajouter plusieurs fragments de texte.
1. Utilisez page.paragraphs.add(text) pour rendre chaque fragment de texte.
1. Enregistrez le document.

```python
import math
import sys
import os
import aspose.pdf as ap

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

### Mesurer dynamiquement la largeur du texte dans le PDF

Mesurer dynamiquement la largeur des caractères et des chaînes dans une police spécifique en utilisant Aspose.PDF for Python via .NET. Il utilise les méthodes 'Font.measure_string()' et 'TextState.measure_string()' pour vérifier que les largeurs des chaînes mesurées sont cohérentes et précises.

1. Utilisez 'FontRepository.find_font()' pour récupérer l'objet de police Arial depuis le référentiel.
1. Créez un objet TextState pour gérer les propriétés de police.
1. Mesurer les caractères individuels.
1. Comparez les résultats des deux méthodes pour tous les caractères compris entre 'A' et 'z'.
1. Assurez-vous que les deux approches de mesure donnent les mêmes résultats.

```python
import math
import sys
import os
import aspose.pdf as ap

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

Ajoutez des hyperliens cliquables au texte d'un PDF en utilisant Aspose.PDF for Python via .NET. Notre bibliothèque montre comment ajouter plusieurs segments de texte dans un seul TextFragment et appliquer un hyperlien à un segment spécifique, ainsi que styliser les segments de texte individuellement (par exemple, couleur, police italique).

1. Créez un nouveau document et une page en utilisant 'Document()', et 'document.pages.add()' pour ajouter une page vierge.
1. Créer un TextFragment.
1. Ajoutez plusieurs objets TextSegment. Chaque segment peut avoir son propre contenu et style. Par exemple du texte simple ou du texte hyperlien.
1. Appliquez un hyperlien à un segment. Créez un objet WebHyperlink avec l'URL souhaitée.
1. Stylisez le segment. Personnalisez la couleur, le style de police, la taille, etc., en utilisant text_state.
1. Ajoutez le fragment à la page en utilisant \u0027page.paragraphs.add()\u0027.
1. Enregistrez le PDF.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_with_hyperlink(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    fragment = ap.text.TextFragment("Sample Text Fragment")

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
    document.save(output_file_name)
```

![Fragment de texte affiché dans un PDF montrant un contenu mixte avec Sample Text Fragment suivi de Text Segment 1, puis un texte hyperlié bleu indiquant Link to Aspose (liant à https://products.aspose.com/pdf), et se terminant par TextSegment sans lien hypertexte dans une mise en forme de texte noir standard](hyperlink_text.png)

### Ajouter du texte de droite à gauche (RTL) au document PDF

RTL (de droite à gauche) est une propriété qui indique la direction de l'écriture du texte, où le texte est écrit de droite à gauche.
Aspose.PDF for Python via .NET. démontre comment ajouter du texte de droite à gauche (RTL), tel que l'arabe ou l'hébreu, à un document PDF.

1. Créez un nouveau document et une page en utilisant 'Document()', et 'document.pages.add()' pour ajouter une page vierge.
1. Créez un TextFragment avec du contenu RTL. Insérez votre texte en arabe, hébreu ou autre langue RTL comme contenu du fragment.
Définir la police et le style. Choisissez une police qui prend en charge le script RTL (par exemple, Tahoma, Arial Unicode MS). Définissez font_size et foreground_color selon les besoins.
1. Définissez l'alignement horizontal sur la droite en utilisant 'text_fragment.horizontal_alignment'.
1. Ajoutez le TextFragment à la page.
1. Enregistrez le document PDF.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_with_rtl_text(output_file_name):
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
    document.save(output_file_name)
```

![Texte de droite à gauche](rtl_text.png)

## Mise en forme du texte

### Ajouter du texte avec le style de police

Ceci est un exemple plus avancé qui démontre le style du texte, la personnalisation des polices, et le texte à format mixte (utilisant des segments de texte en indice). Aspose.PDF explique comment appliquer les propriétés de police telles que la famille de police, la taille, la couleur, le gras, l'italique et le soulignement à un fragment de texte.
De plus, cet extrait de code montre comment utiliser plusieurs segments de texte au sein d'un même fragment pour créer des expressions textuelles complexes — par exemple, en incluant des caractères en indice ou en exposant, souvent nécessaires dans les formules ou les notations scientifiques.

1. Créez un nouveau document et une page en utilisant 'Document()', et 'document.pages.add()' pour ajouter une page vierge.
1. Créer un TextFragment pour du texte simple stylisé.
1. Définir le contenu texte.
1. Définir la position en utilisant les coordonnées Position(x, y).
1. Appliquer le style via la propriété "text_state" - font, font_size, foreground_color, font_style, underline.
1. Créez une expression complexe avec plusieurs objets TextSegment. Chaque TextSegment représente une portion de texte pouvant avoir son propre style. Cela vous permet de construire des expressions, comme des formules mathématiques ou chimiques.
1. Définissez plusieurs objets TextState. Un pour le texte principal (text_state_letters). Un autre pour le texte en indice ou exposant (text_state_index).
1. Combinez les segments de texte. Ajoutez chaque segment à un 'TextFragment' en utilisant 'segments.append()'.
1. Ajoutez les deux objets texte à la page. Utilisez 'page.paragraphs.add()' pour les placer dans le document.
1. Enregistrez le document final.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_with_font_styling(output_file_name):
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
    document.save(output_file_name)
```

![Fragment de texte affiché avec une police Arial italique en bleu contenant le texte Hello, Aspose! suivi d’une formule mathématique affichant S = a indice 2n + a indice 2n+1 + a indice 2n+2 avec le texte principal en bleu et la mise en forme des indices en rouge](styled_text.png)

## Ajouter du texte transparent

Ajoutez des formes semi-transparentes et du texte à un document PDF à l'aide d'Aspose.PDF pour Python.
Il crée un rectangle coloré avec une opacité partielle et superpose un TextFragment avec une couleur de premier plan transparente.

1. Initialisez un objet Document et ajoutez une page vierge pour dessiner du contenu.
1. Utilisez 'ap.drawing.Graph' pour créer un canevas qui vous permet de dessiner des formes.
1. Ajoutez un rectangle avec un remplissage semi-transparent.
1. Empêcher le décalage de la position du canvas.
1. Ajoutez le canvas à la page. Insérez les formes graphiques dans la collection de paragraphes de la page.
1. Créer un fragment de texte transparent.
1. Insérez le TextFragment dans la collection de paragraphes de la Page.
1. Enregistrez le document PDF.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_transparent(output_file_name):
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

    document.save(output_file_name)
```

### Ajouter du texte invisible au PDF

Cet exemple montre comment créer un document PDF contenant du texte à la fois visible et invisible. Le texte invisible fait partie de la structure du document mais il est caché à la vue, ce qui le rend utile pour intégrer des métadonnées, des balises d'accessibilité ou du contenu recherchable sans affecter la mise en page.

1. Créer un Document PDF et une Page.
1. Créer un fragment de texte avec du contenu visible répété.
1. Ajoutez un deuxième fragment de texte et marquez-le comme invisible.
1. Enregistrez le Document.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_invisible(output_file_name):
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Add visible text
    text1 = ap.text.TextFragment(
        "This is the visible text. This is the visible text. This is the visible text."
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

    document.save(output_file_name)
```

### Ajouter du texte avec un style de bordure dans le PDF

La bibliothèque Aspose.PDF montre comment créer un document PDF contenant un fragment de texte stylisé avec une bordure visible. La méthode applique des couleurs d'arrière-plan et de premier plan, les paramètres de police, et un trait (bordure) autour du rectangle du texte pour renforcer l'accent visuel.

1. Créer un Document PDF et une Page.
1. Créer et positionner un fragment de texte. Ajouter un fragment de texte avec le message et définir sa position.
1. Appliquer le style de texte. Définir la police sur Times New Roman, taille 12. Appliquer un arrière-plan gris clair et une couleur de premier plan (texte) rouge.
1. Configurer le style de bordure.
1. Ajouter du texte à la page. Utilisez TextBuilder pour ajouter le texte stylisé à la page.
1. Enregistrez le Document.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_border(output_file_name):
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

Ajouter une mise en forme barrée (strikethrough) à un fragment de texte dans un document PDF. Le texte barré est utile pour indiquer des suppressions, des révisions ou des mises en évidence dans des documents annotés.

1. Créez un nouveau document et une page en utilisant 'Document()', et 'document.pages.add()' pour ajouter une page vierge.
1. Créer et styliser le fragment de texte.
1. Appliquer le formatage Couleur et Barré. Définir l'arrière-plan en gris clair, la couleur du texte en rouge, et activer le barré.
1. Positionner le texte.
1. Utilisez 'TextBuilder' pour ajouter le texte stylisé à la page.
1. Enregistrez le Document.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_strikeout_text(output_file_name):
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

Aspose.PDF for Python via .NET montre comment appliquer un effet de dégradé linéaire au texte d'un document PDF. Le dégradé axial passe en douceur du rouge au bleu sur l'ensemble du texte, créant un en-tête visuellement saisissant. Cette technique est idéale pour les titres stylisés, le branding ou les éléments décoratifs dans les mises en page de documents PDF.

1. Initialisez un nouveau document et ajoutez une page vierge.
1. Créer et styliser le fragment de texte. Ajouter le titre, définir la position, la police et la taille.
1. Appliquer un dégradé axial avec 'GradientAxialShading'. Définir la couleur de premier plan en utilisant GradientAxialShading du rouge au bleu.
1. Ajouter le style souligné.
1. Insérez le fragment de texte stylisé dans la page.
1. Enregistrez le Document.

```python
import math
import sys
import os
import aspose.pdf as ap

def apply_gradient_axial_shading_to_text(output_file_name):
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

Un dégradé radial crée une transition de couleur circulaire qui rayonne depuis le centre du texte, offrant une option de style visuellement dynamique pour les titres, les en-têtes ou les éléments décoratifs.

1. Initialisez un nouveau document et ajoutez une page vierge.
1. Créer et styliser le fragment de texte. Ajouter le titre, définir la position, la police et la taille.
1. Appliquer un dégradé radial avec 'GradientRadialShading'. Définir la couleur de premier plan en utilisant GradientRadialShading du rouge au bleu.
1. Ajouter le style souligné.
1. Insérez le fragment de texte stylisé dans la page.
1. Enregistrez le Document.

```python
import math
import sys
import os
import aspose.pdf as ap

def apply_gradient_radial_shading_to_text(output_file_name):
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

![Appliquer un dégradé radial](gradient_radial_shading.png)

## Fragments HTML et LaTeX

### Ajouter du texte HTML au document PDF

La bibliothèque Aspose.PDF for Python via .NET vous permet d'insérer du contenu au format HTML dans un document PDF en utilisant la classe HtmlFragment. En utilisant les balises HTML, vous pouvez rendre du texte stylisé, structuré ou semblable à une formule directement dans un PDF.

1. Créez un nouveau document et une page en utilisant 'Document()', et 'document.pages.add()' pour ajouter une page vierge.
1. Créez une instance de la classe HtmlFragment et transmettez votre chaîne HTML en tant que paramètre.
1. Ajoutez le fragment à la page en utilisant 'page.paragraphs.add()' pour insérer le contenu HTML.
1. Enregistrez le PDF.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_html_fragment(output_file_name):
    # Create a new document
    document = ap.Document()
    page = document.pages.add()

    # Add a text fragment at a specific position
    text_fragment = ap.HtmlFragment("<pre>S=a<sub>2n</sub>+a<sup>2</sup><pre>")

    page.paragraphs.add(text_fragment)
    document.save(output_file_name)
```

![Ajouter du texte HTML à un Document PDF](html_fragment.png)

### Ajouter un fragment HTML stylisé avec divers formats à un document PDF

Nous pouvons définir un fragment HTML et définir le style du texte directement à l'aide de balises HTML. Intégrer du contenu HTML stylisé dans un document PDF. Cet extrait de code crée un nouveau fichier PDF, ajoute une page, insère un fragment HTML avec divers éléments de mise en forme (titres, paragraphes, liens et styles en ligne), puis enregistre le résultat dans le chemin spécifié.

1. Initialise un nouvel objet Document pour représenter le PDF.
1. Ajoute une page blanche au document où le contenu HTML sera placé.
1. Préparer le contenu HTML. La chaîne HTML contient un titre h1, un paragraphe de couleur verte avec du texte en gras, en italique et souligné, ainsi qu'un hyperlien vers un site web avec une taille de police augmentée.
1. Créer un fragment HTML. Enveloppez la chaîne HTML dans un objet HtmlFragment.
1. Insérer du HTML dans la Page. Ajoute le fragment HTML à la collection de paragraphes de la page, en rendant le HTML en tant que contenu PDF natif.
1. Enregistrez le Document.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_html_fragment(output_file_name):
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
    document.save(output_file_name)
```

![Ajouter du contenu HTML à un document PDF](html_content.png)

### Ajouter un fragment HTML avec un état de texte remplacé

Comme nous l'avons vu dans l'exemple précédent, il est possible de définir des styles directement dans le code HTML. Cela présente des avantages, mais aussi quelques inconvénients. Supposons que nous travaillions avec le HTML d'un client et que nous voulions uniformiser l'apparence de notre sortie.
Dans ce cas, nous pouvons remplacer le style du client en utilisant notre propre TextState, comme le montre l'exemple suivant.

1. Créez un nouveau document et une page en utilisant 'Document()', et 'document.pages.add()' pour ajouter une page vierge.
1. Préparer le contenu HTML. La chaîne HTML contient un titre h1 avec la police Verdana, un paragraphe de couleur verte avec du texte en gras, italique et souligné, ainsi qu’un hyperlien vers un site web avec une taille de police plus grande.
1. Créer un fragment HTML. Enveloppez la chaîne HTML dans un objet HtmlFragment.
1. Remplacez le formatage du texte. Créez un objet TextState et définissez le Font, le Font Size et le Text Color.
1. Ajoutez le fragment HTML à la collection de paragraphes de la page.
1. Enregistrez le Document.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_html_fragment_override_text_state(output_file_name):
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
    document.save(output_file_name)
```

![Ajouter le texte d’état de substitution du fragment HTML](html_override.png)

### Ajouter du texte LaTeX au document PDF

Ajouter des expressions mathématiques formatées en LaTeX à un document PDF en utilisant la classe TeXFragment dans Aspose.PDF for Python via .NET.
LaTeX est un système de composition puissant largement utilisé pour créer des documents scientifiques et mathématiques. En utilisant TeXFragment, vous pouvez rendre directement la notation et les symboles mathématiques LaTeX à l'intérieur d'une page PDF.

1. Créez un nouveau document et une page en utilisant 'Document()', et 'document.pages.add()' pour ajouter une page vierge.
1. Utilisez la classe TeXFragment pour rendre directement la syntaxe LaTeX.
1. Ajoutez le contenu LaTeX à la mise en page du PDF avec 'page.paragraphs.add()'.
1. Enregistrez le PDF.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_latex_fragment(output_file_name):
    # Create a new document
    document = ap.Document()
    page = document.pages.add()

    # Add a text fragment at a specific position
    text_fragment = ap.TeXFragment(
        "\\underbrace{\\overbrace{a+b}^6 \\cdot \\overbrace{c+d}^7}_\\text{example of text} = 42"
    )

    page.paragraphs.add(text_fragment)
    document.save(output_file_name)
```

![Expression mathématique complexe affichée dans un PDF montrant la formule LaTeX avec une notation overbrace au-dessus de (a+b)⁶, une notation underbrace sous l’ensemble de l’expression (a+b)⁶ · (c+d)⁷, étiquetée comme exemple de texte, et égale à 42. La formule illustre une composition mathématique avancée avec un espacement approprié et un style de parenthèses typique du rendu LaTeX.](latex_fragment.png)

## Polices personnalisées

### Utilisez une Font personnalisée à partir d'un fichier

Cet exemple vous permet d'ajouter du texte à un fichier PDF en utilisant une police OpenType personnalisée dans Aspose.PDF for Python via .NET. Il montre comment créer un nouveau document PDF, positionner le texte avec précision sur la page, et appliquer un formatage personnalisé tel que le type de police, la taille, la couleur et le style italique.

1. Créez un nouveau document PDF et ajoutez une page.
1. Définissez le contenu texte que vous souhaitez ajouter au PDF.
1. Définir la position du texte.
1. Ajoutez le TextFragment à la page.
1. Enregistrez le document PDF.

Cette fonction fonctionne non seulement avec les polices OTF mais aussi avec les polices TTF.

```python
import math
import sys
import os
import aspose.pdf as ap

def use_custom_font_from_file(output_file_name):
    font_path = os.path.join(FONT_DIR, "BriosoPro Italic.otf")
    document = ap.Document()
    page = document.pages.add()

    fragment = ap.text.TextFragment("Hello, Aspose!")
    fragment.position = ap.text.Position(100, 600)
    fragment.text_state.font = ap.text.FontRepository.open_font(font_path)
    fragment.text_state.font_size = 24
    fragment.text_state.foreground_color = ap.Color.blue
    fragment.text_state.font_style = ap.text.FontStyles.ITALIC

    page.paragraphs.add(fragment)
    document.save(output_file_name)
```

![Fragment de texte affiché dans un document PDF montrant Hello, Aspose! rendu en police BriosoPro bleu italique, démontrant l'intégration personnalisée de polices OpenType et les capacités de style dans le formatage du texte PDF.](custom_font.png)

### Utilisez une Font personnalisée depuis un flux

Ce fragment de code montre comment ajouter du texte à un document PDF en utilisant une police OpenType (OTF) personnalisée incorporée avec Aspose.PDF for Python via .NET. Il montre comment ouvrir un fichier de police en tant que flux, l'incorporer dans le PDF pour garantir la disponibilité de la police sur différents systèmes, et appliquer le formatage du texte tel que la taille de la police, la couleur et le style italique. Cette approche est idéale pour créer des PDF visuellement cohérents qui conservent la typographie même lorsqu'ils sont partagés ou visualisés sur des appareils ne disposant pas de la police installée.

1. Charger le fichier Font en tant que flux binaire.
1. Ouvrez et intégrez la police en utilisant 'FontRepository.open_font'.
1. Créez un nouveau document PDF et ajoutez une page.
1. Ajouter un fragment de texte stylisé avec :
    - Police personnalisée intégrée.
    - style italique et couleur bleue.
    - Taille de police spécifique et position.
1. Enregistrez le document final à un chemin de sortie spécifié.

```python
import math
import sys
import os
import aspose.pdf as ap

def use_custom_font_from_stream(output_file_name):
    font_path = os.path.join(FONT_DIR, "BriosoPro Italic.otf")
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
        document.save(output_file_name)
```

L'intégration des polices garantit un rendu cohérent sur toutes les plateformes, ce qui rend cette approche idéale pour le branding, la fidélité du design et le support multilingue.

## Sujets de texte associés

- [Travailler avec le texte dans le PDF en utilisant Python](/pdf/fr/python-net/working-with-text/)
- [Formater le texte PDF en Python](/pdf/fr/python-net/text-formatting-inside-pdf/)
- [Remplacer le texte dans le PDF via Python](/pdf/fr/python-net/replace-text-in-pdf/)
- [Rechercher et extraire le texte PDF en Python](/pdf/fr/python-net/search-and-get-text-from-pdf/)