---
title: Formater le texte PDF en Python
linktitle: Mise en forme du texte dans PDF
type: docs
weight: 70
url: /fr/python-net/text-formatting-inside-pdf/
description: Découvrez comment mettre en forme le texte dans des documents PDF en Python à l'aide des espacements, bordures, retraits et options de style.
lastmod: "2026-05-25"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Mettre en forme et styliser le texte dans des fichiers PDF avec Python
Abstract: Cet article explique comment mettre en forme le texte dans des documents PDF avec Aspose.PDF for Python via .NET. Découvrez comment contrôler les espacements, retraits, bordures, soulignements, effets de barré et autres options de style de texte en Python.
---

## Espacement des lignes et des caractères

### Utiliser l'espacement des lignes

#### Comment mettre en forme du texte avec un interligne personnalisé en Python - Cas simple

Aspose.PDF for Python propose une approche directe pour contrôler la mise en page et la lisibilité du texte grâce aux réglages d'interligne.

Notre extrait de code montre comment contrôler l'interligne dans un document PDF. Il lit le texte à partir d'un fichier, ou utilise un message de secours, applique une taille de police et un interligne personnalisés, puis ajoute le texte formaté à une nouvelle page PDF.

1. Créez un nouveau document PDF.
1. Chargez le texte source.
1. Initialisez un objet `TextFragment` et affectez-lui le texte chargé.
1. Définissez les propriétés de police et d'espacement pour le texte. Ces valeurs déterminent si les lignes de texte apparaissent plus serrées ou plus espacées :
    - Taille de police : 12 points
    - Interligne : 16 points
1. Insérez le fragment de texte formaté dans la collection de paragraphes de la page.
1. Enregistrez le document.

```python
import aspose.pdf as ap
import sys
from os import path

def specify_line_spacing_simple_case(outfile):
    document = ap.Document()
    page = document.pages.add()

    lorem_path = path.join(DATA_DIR, "lorem.txt")
    if path.exists(lorem_path):
        with open(lorem_path, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        text = "Lorem ipsum text not found."

    text_fragment = ap.text.TextFragment(text)
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.line_spacing = 16
    page.paragraphs.add(text_fragment)

    document.save(outfile)
```

#### Comment mettre en forme du texte avec un interligne personnalisé en Python - Cas spécifique

Voyons comment appliquer différents modes d'interligne dans un document PDF en utilisant une police TrueType (TTF) personnalisée.
L'exemple charge du texte à partir d'un fichier, incorpore une police spécifique et affiche deux fois le même texte sur une page PDF, chaque fois avec un mode d'interligne différent :

- Mode `FONT_SIZE` : l'interligne est égal à la taille de la police.
- Mode `FULL_SIZE` : l'interligne tient compte de la hauteur complète de la police, y compris les ascendantes et descendantes.

L'exemple montre comment le comportement de l'interligne peut varier selon le mode sélectionné.

1. Créez un nouveau document PDF.
1. Spécifiez les chemins du fichier de police personnalisée et du fichier texte source.
1. Chargez le contenu du texte.
1. Ouvrez la police personnalisée.
1. Créez et configurez le premier `TextFragment` en mode `FONT_SIZE`. Définissez `line_spacing` sur `TextFormattingOptions.LineSpacingMode.FONT_SIZE`, ce qui signifie que l'interligne est égal à la taille de la police.
1. Créez et configurez le second `TextFragment` en mode `FULL_SIZE`. Définissez `line_spacing` sur `TextFormattingOptions.LineSpacingMode.FULL_SIZE`, qui utilise la hauteur complète de la police.
1. Ajoutez les deux fragments de texte à la même page PDF.
1. Enregistrez le document final à l'emplacement de sortie spécifié.

```python
import aspose.pdf as ap
import sys
from os import path

def specify_line_spacing_specific_case(outfile):
    document = ap.Document()
    page = document.pages.add()

    font_file = path.join(DATA_DIR, "HPSimplified.ttf")
    lorem_path = path.join(DATA_DIR, "lorem.txt")
    if path.exists(lorem_path):
        with open(lorem_path, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        text = "Lorem ipsum text not found."

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

![Document PDF affichant du texte avec un interligne personnalisé de 16 points pour améliorer la lisibilité et la mise en page du texte](line_spacing.png)

### Utiliser l'espacement des caractères

#### Comment contrôler l'espacement des caractères dans du texte PDF avec la classe TextFragment

L'espacement des caractères détermine la distance entre chaque caractère d'une ligne de texte. C'est utile pour ajuster finement l'apparence du texte ou obtenir des effets typographiques spécifiques.

1. Initialisez un nouvel objet `Document` et ajoutez une page vide pour y placer le texte.
1. Définissez un générateur de fragments. Implémentez une fonction utilitaire `make_fragment(spacing)` :
    - créez un `TextFragment` avec le texte d'exemple ;
    - définissez la police.
1. Ajoutez des fragments de texte avec différentes valeurs d'espacement.
1. Enregistrez le `Document`.

```python
import aspose.pdf as ap
import sys
from os import path

def character_spacing_using_text_fragment(outfile):
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

![Document PDF affichant trois lignes de texte identique avec des espacements de caractères différents afin d'illustrer l'effet visuel des variations d'espacement dans le texte PDF](character_spacing_simple.png)

#### Comment contrôler l'espacement des caractères dans du texte PDF avec TextParagraph et TextBuilder

Aspose.PDF permet d'appliquer un espacement personnalisé entre les caractères lors de l'ajout de texte à un document PDF à l'aide de `TextParagraph` et `TextBuilder`.
L'exemple définit une zone spécifique sur la page, configure le retour à la ligne et affiche un fragment de texte avec un espacement ajusté entre les caractères.

L'utilisation de `TextParagraph` est idéale lorsque vous avez besoin d'un contrôle précis sur le placement et la mise en page du texte, par exemple pour créer des blocs de texte structurés ou multicolonnes.

1. Créez un nouveau document PDF.
1. Initialisez une instance de `TextBuilder` pour la page.
1. Créez et configurez un `TextParagraph`.
    - Définissez le mode de retour à la ligne sur `TextFormattingOptions.WordWrapMode.BY_WORDS`.
1. Créez un `TextFragment` avec un espacement personnalisé entre les caractères.
    - Créez un nouveau `TextFragment` et définissez son texte, par exemple `"Sample Text with character spacing"`.
    - Spécifiez les attributs de police tels qu'Arial et une taille de 14 pt.
    - Appliquez `character_spacing = 2.0`, ce qui augmente l'espace entre les caractères.
1. Ajoutez le `TextFragment` au `TextParagraph`.
1. Ajoutez le `TextParagraph` à la page.
1. Enregistrez le document PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def character_spacing_using_text_paragraph(outfile):
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

## Créer des listes

Lorsque vous travaillez avec des fichiers PDF, vous pouvez avoir besoin d'afficher des informations structurées sous forme de listes, qu'elles soient à puces, numérotées ou formatées en HTML ou en LaTeX.
Aspose.PDF for Python via .NET propose plusieurs façons flexibles de créer et de formater des listes directement dans vos documents PDF, avec un contrôle total sur la mise en page, la police et le style.

Cet article présente plusieurs approches pour créer des listes dans des PDF, de la simple mise en forme de texte jusqu'au rendu avancé en HTML et en LaTeX. Chaque méthode répond à un cas d'usage particulier, que vous préfériez un contrôle programmatique précis ou une mise en forme pratique basée sur le balisage.

À la fin de cet article, vous saurez comment :

- créer des listes à puces et des listes numérotées personnalisées avec `TextParagraph` et `TextBuilder` ;
- utiliser des fragments HTML (`HtmlFragment`) pour afficher facilement des listes `<ul>` et `<ol>` dans des PDF ;
- tirer parti de fragments LaTeX (`TeXFragment`) pour la mise en forme de listes mathématiques ou scientifiques ;
- contrôler le retour à la ligne, les styles de police et le positionnement de la mise en page dans une page ;
- comprendre la différence entre la construction manuelle de listes et les approches pilotées par balisage.

### Créer une liste numérotée

```python
import aspose.pdf as ap
import sys
from os import path

def create_bullet_list(outfile):
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
        fragment = ap.text.TextFragment("вЂў " + item)
        fragment.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
        fragment.text_state.font_size = 12
        paragraph.append_line(fragment)

    builder.append_paragraph(paragraph)
    document.save(outfile)
```

### Créer une liste à puces

```python
import aspose.pdf as ap
import sys
from os import path

def create_numbered_list(outfile):
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

### Créer une liste numérotée en version HTML

Créez une liste numérotée dans un document PDF à l'aide de fragments HTML. L'exemple convertit une liste Python de chaînes en un élément HTML `<ol>` et l'insère dans une page PDF en tant que `HtmlFragment`.

L'utilisation de fragments HTML vous permet d'incorporer directement dans le PDF des fonctionnalités de mise en forme basées sur HTML, comme des listes numérotées, du texte en gras, en italique, etc.

1. Créez un nouveau document PDF et ajoutez une page.
1. Préparez les éléments de la liste.
1. Convertissez la liste en liste HTML ordonnée.
    - Utilisez la balise `<ol>` pour une liste numérotée.
    - Entourez chaque élément de balises `li` à l'aide d'une compréhension de liste.
1. Convertissez la chaîne HTML en objet `HtmlFragment` pouvant être ajouté à la page PDF.
1. Insérez le `HtmlFragment` dans la collection de paragraphes de la page.
1. Enregistrez le document PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def create_numbered_list_html_version(outfile):
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

![Liste numérotée affichée dans un document PDF avec quatre éléments numérotés automatiquement et un espacement correct entre les éléments](numbered_list_html.png)

### Créer une liste à puces en version HTML

Notre bibliothèque montre comment créer une liste à puces dans un document PDF à l'aide de fragments HTML. L'exemple convertit une liste Python de chaînes en élément HTML `<ul>` et l'insère dans une page PDF sous forme de `HtmlFragment`. Les fragments HTML permettent d'utiliser directement dans le PDF des fonctionnalités de mise en forme HTML comme les listes, le gras et l'italique.

1. Créez un nouveau document PDF et ajoutez une page.
1. Préparez les éléments de la liste.
1. Convertissez la liste en liste HTML non ordonnée.
    - Utilisez la balise `<ul>` pour une liste à puces.
    - Entourez chaque élément de balises `li` à l'aide d'une compréhension de liste.
1. Créez un `HtmlFragment`. Convertissez la chaîne HTML en objet `HtmlFragment` pouvant être ajouté à la page PDF.
1. Insérez le `HtmlFragment` dans la collection de paragraphes de la page.
1. Enregistrez le document PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def create_bullet_list_html_version(outfile):
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

![Liste à puces affichée dans un document PDF avec une indentation et un espacement corrects entre les éléments](bullet_list_html.png)

### Créer une liste à puces en version LaTeX

Créez une liste à puces dans un PDF à l'aide de fragments LaTeX (`TeXFragment`). L'exemple convertit une liste Python de chaînes en environnement LaTeX `itemize` puis l'insère dans une page PDF. Les fragments LaTeX sont idéaux lorsque vous souhaitez afficher des formules mathématiques, des symboles ou des listes structurées avec une mise en forme précise.

1. Créez un nouveau document PDF et ajoutez une page.
1. Définissez une liste Python de chaînes qui deviendront des puces dans l'environnement LaTeX `itemize`.
1. Convertissez la liste en environnement LaTeX `itemize` :
    - Entourez les éléments avec `\begin{itemize}` et `\end{itemize}`.
    - Préfixez chaque élément avec `\item` à l'aide d'une compréhension de liste.
1. Convertissez la chaîne LaTeX en objet `TeXFragment` pouvant être rendu dans le PDF.
1. Ajoutez le fragment LaTeX à la page.
1. Enregistrez le document PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def create_bullet_list_latex_version(outfile):
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

![Liste à puces affichée dans un PDF avec une mise en forme LaTeX et un espacement cohérent](bullet_list_latex.png)

### Créer une liste numérotée en version LaTeX

Créez une liste numérotée dans un PDF à l'aide de fragments LaTeX (`TeXFragment`). L'exemple convertit une liste Python de chaînes en environnement LaTeX `enumerate` puis l'insère dans une page PDF. Les fragments LaTeX sont idéaux lorsque vous souhaitez une mise en forme précise, des listes structurées ou une notation mathématique dans des PDF.

1. Créez un nouveau document PDF et ajoutez une page.
1. Définissez une liste Python de chaînes qui deviendront des éléments numérotés dans l'environnement LaTeX `enumerate`.
1. Convertissez la liste en environnement LaTeX `enumerate`.
1. Convertissez la chaîne LaTeX en objet `TeXFragment` pouvant être rendu dans le PDF.
1. Ajoutez le fragment LaTeX à la page.
1. Enregistrez le document PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def create_numbered_list_latex_version(outfile):
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

![Liste numérotée affichée dans un PDF avec une mise en forme LaTeX](numbered_list_latex.png)

## Notes de bas de page et notes de fin

### Ajouter des notes de bas de page

Les notes de bas de page servent à référencer des annotations dans le corps d'un document en plaçant des numéros en exposant à côté du texte concerné. Ces numéros correspondent à des notes détaillées généralement indentées et placées en bas de la même page, afin d'apporter un contexte supplémentaire, des citations ou des commentaires.

Ajoutez une note de bas de page à un fragment de texte dans un document PDF avec Aspose.PDF for Python via .NET. Les notes de bas de page sont utiles pour fournir des informations complémentaires, des citations ou des clarifications sans surcharger le contenu principal. Cette méthode garantit une intégration visuelle et structurelle des notes dans la mise en page PDF.

1. Créez un nouveau document.
1. Créez un `TextFragment` contenant le contenu principal.
1. Ajoutez du texte inline. Créez un autre `TextFragment` qui continue dans le même paragraphe.
1. Enregistrez le document.

```python
import aspose.pdf as ap
import sys
from os import path

def add_footnote(outfile):
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

### Ajouter une note de bas de page avec une mise en forme personnalisée dans le PDF

1. Initialisez un nouveau document PDF et ajoutez une page vide.
1. Créez le fragment de texte principal.
1. Créez et stylisez la note de bas de page avec police, taille, couleur et style.
1. Insérez dans la page le fragment de texte stylisé avec la note de bas de page.
1. Ajoutez un autre fragment de texte sans note de bas de page.
1. Enregistrez le document.

```python
import aspose.pdf as ap
import sys
from os import path

def add_footnote_custom_text_style(outfile):
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

Ajoutez des notes de bas de page à des fragments de texte dans un document PDF avec Aspose.PDF for Python via .NET, avec la possibilité de personnaliser le symbole du marqueur de note.

1. Créez le document PDF et la page.
1. Ajoutez le premier fragment de texte avec un symbole de note de bas de page personnalisé.
1. Ajoutez un autre fragment de texte qui poursuit le paragraphe sans note.
1. Ajoutez un second fragment de texte avec la note de bas de page par défaut.
1. Enregistrez le document.

```python
import aspose.pdf as ap
import sys
from os import path

def add_footnote_custom_text(outfile):
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

Personnalisez l'apparence visuelle des lignes de note de bas de page dans un document PDF avec la bibliothèque Python. La personnalisation de ces lignes améliore la lisibilité visuelle et permet une cohérence stylistique dans des documents tels que des rapports, des articles académiques ou des publications annotées.

1. Créez un nouveau document PDF et ajoutez une page.
1. Définissez un style de ligne personnalisé pour les connecteurs de notes de bas de page, avec couleur, largeur et motif de tirets.
1. Ajoutez plusieurs fragments de texte avec des notes de bas de page.
1. Enregistrez le document final.

```python
import aspose.pdf as ap
import sys
from os import path

def add_footnote_with_custom_line_style(outfile):
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

Comment enrichir des notes de bas de page dans un document PDF en intégrant des images, du texte stylisé et des tableaux avec Aspose.PDF for Python via .NET ?

1. Créez un nouveau document PDF et ajoutez une page.
1. Ajoutez un fragment de texte avec une note de bas de page attachée.
1. Intégrez une image, du texte stylisé et un tableau dans la note de bas de page.
1. Enregistrez le document.

```python
import aspose.pdf as ap
import sys
from os import path

def add_footnote_with_image_and_table(outfile):
    document = ap.Document()
    page = document.pages.add()

    text = ap.text.TextFragment("This is a sample text with a footnote.")
    page.paragraphs.add(text)

    note = ap.Note()

    # Add image
    image_note = ap.Image()
    image_note.file = path.join(DATA_DIR, "logo.jpg")
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

### Ajouter des notes de fin à des documents PDF

Une note de fin est un type de citation qui dirige le lecteur vers une section située à la fin du document, où il peut trouver la référence complète d'une citation, d'une idée reformulée ou d'un contenu résumé. Lorsqu'on utilise des notes de fin, un numéro en exposant est placé juste après le contenu référencé afin de renvoyer à la note correspondante à la fin du document.

Cet extrait de code montre comment ajouter une note de fin à un fragment de texte dans un document PDF. Contrairement aux notes de bas de page, qui apparaissent près du texte référencé, les notes de fin sont généralement placées à la fin d'un document ou d'une section. Cette méthode simule également un document plus long pour illustrer le comportement des notes de fin dans un contenu étendu.

1. Créez le document PDF et la page.
1. Ajoutez un fragment de texte avec une note de fin.
1. Chargez du contenu texte externe.
1. Simulez un document long. Ajoutez plusieurs fois le texte chargé afin de représenter un document plus long.
1. Enregistrez le document.

```python
import aspose.pdf as ap
import sys
from os import path

def add_endnote(outfile):
    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with an endnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.end_note = ap.Note("This is the EndNote content.")
    page.paragraphs.add(text_fragment)

    lorem_path = path.join(DATA_DIR, "lorem.txt")
    if path.exists(lorem_path):
        with open(lorem_path, encoding="utf-8") as f:
            text_content = f.read()
    else:
        text_content = "Lorem ipsum sample text not found."

    # Simulate long text
    for _ in range(5):
        tf = ap.text.TextFragment(text_content)
        tf.text_state.font = ap.text.FontRepository.find_font("Arial")
        tf.text_state.font_size = 14
        page.paragraphs.add(tf)

    document.save(outfile)
```

### Ajouter des notes de fin avec un texte de marqueur personnalisé dans le PDF

Ajoutez une note de fin à un fragment de texte dans un document PDF, avec un symbole de marqueur personnalisé, par exemple `"***"`. Les notes de fin sont généralement placées à la fin d'un document ou d'une section et permettent d'ajouter du contexte, des citations ou des commentaires.

1. Créez le document PDF et la page.
1. Ajoutez un fragment de texte stylisé avec une note de fin.
1. Personnalisez le texte du marqueur de la note de fin.
1. Chargez un contenu externe à partir d'un fichier `.txt`.
1. Simulez un contenu long afin d'illustrer le placement des notes de fin.
1. Enregistrez le document PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def add_endnote_custom_text(outfile):
    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with an endnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.end_note = ap.Note("This is the EndNote content.")
    text_fragment.end_note.text = "***"
    page.paragraphs.add(text_fragment)

    lorem_path = path.join(DATA_DIR, "lorem.txt")
    if path.exists(lorem_path):
        with open(lorem_path, encoding="utf-8") as f:
            text_content = f.read()
    else:
        text_content = "Lorem ipsum sample text not found."

    # Simulate long text
    for _ in range(5):
        tf = ap.text.TextFragment(text_content)
        tf.text_state.font = ap.text.FontRepository.find_font("Arial")
        tf.text_state.font_size = 14
        page.paragraphs.add(tf)

    document.save(outfile)
```

## Contrôle de la mise en page et des pages

### Forcer une table à commencer sur une nouvelle page dans le PDF

Ajoutez un contenu spécifique qui doit commencer sur une nouvelle page dans un document PDF avec Aspose.PDF for Python via .NET.
En définissant la propriété `is_in_new_page`, vous pouvez contrôler précisément la structure et la mise en page des pages afin que certaines sections, telles que des tableaux, des rapports ou des résumés, commencent toujours sur une page vierge. C'est idéal pour la mise en forme de documents, les rapports prêts à imprimer ou la génération de sorties bien organisées.

1. Créez et configurez un tableau.
1. Ajoutez des données au tableau.
1. Forcez une nouvelle page pour le tableau. Cela garantit que le tableau commence en haut d'une nouvelle page, même s'il y a déjà du contenu sur la page en cours.
1. Ajoutez le tableau à la page. Utilisez `page.paragraphs.add()` pour inclure le tableau dans la mise en page PDF.
1. Enregistrez le document.

```python
import aspose.pdf as ap
import sys
from os import path

def force_new_page(output_file_name):
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

### Utiliser la propriété de paragraphe inline dans un PDF

Notre bibliothèque vous permet d'utiliser la propriété `is_in_line_paragraph` pour contrôler le flux inline entre le texte et les images dans un PDF.
Normalement, lorsque vous ajoutez de nouveaux éléments, comme des fragments de texte ou des images, chacun commence sur une nouvelle ligne ou dans un nouveau paragraphe.
En définissant `is_in_line_paragraph = True`, vous pouvez faire apparaître les éléments sur la même ligne ou dans le même paragraphe, ce qui permet de créer des mises en page inline fluides, idéales pour combiner du texte et des images comme des logos, des icônes ou des symboles dans une phrase.

Le premier fragment de texte, l'image et le second fragment de texte apparaissent sur la même ligne et forment un paragraphe inline continu.
Le troisième fragment de texte commence un nouveau paragraphe, ce qui illustre le comportement par défaut du retour à la ligne.

1. Créez un nouveau document PDF.
1. Ajoutez le premier fragment de texte.
1. Insérez une image inline.
1. Ajoutez davantage de texte inline.
1. Ajoutez un nouveau paragraphe.
1. Enregistrez le PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def using_inline_paragraph_property(output_file_name):
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
    image.file = path.join(DATA_DIR, "logo.jpg")
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

### Créer un PDF multicolonne

Créez une mise en page multicolonne de type journal dans un PDF avec Aspose.PDF for Python via .NET.
Cet exemple montre comment combiner du texte, de la mise en forme HTML et des graphiques dans une `FloatingBox`, afin d'obtenir un contrôle avancé de la mise en page comparable à celui d'un magazine ou d'une newsletter à colonnes.

1. Initialisez le document PDF.
1. Ajoutez une ligne de séparation horizontale en haut.
1. Ajoutez un titre HTML stylisé.
1. Créez la `FloatingBox` pour contrôler la mise en page.
1. Configurez la mise en page multicolonne.
1. Ajoutez les informations sur l'auteur.
1. Dessinez une autre ligne horizontale interne.
1. Ajoutez le texte de l'article.
1. Enregistrez le PDF final.

```python
import aspose.pdf as ap
import sys
from os import path

def create_multi_column_pdf(output_file_name):
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
    lorem_path = path.join(DATA_DIR, "lorem.txt")
    if path.exists(lorem_path):
        with open(lorem_path, "r", encoding="utf-8") as f:
            lorem_text = f.read()
    else:
        lorem_text = "Lorem ipsum text not found."
    text2 = ap.text.TextFragment(lorem_text * 5)
    box.paragraphs.add(text2)

    page.paragraphs.add(box)

    # Save PDF
    document.save(output_file_name)
```

### Tabulations personnalisées pour l'alignement du texte dans le PDF

Créez une mise en page de texte semblable à un tableau dans un PDF à l'aide de tabulations personnalisées, sans utiliser de structure de tableau.
En définissant les positions, les alignements et les styles de remplissage des tabulations, vous pouvez aligner le texte avec précision entre les colonnes. C'est utile pour les factures, les rapports ou les données textuelles structurées.

1. Créez un nouveau document PDF.
1. Définissez des tabulations personnalisées.
1. Utilisez les marqueurs `#$TAB` dans le texte.
1. Ajoutez le texte au PDF.
1. Enregistrez le PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def custom_tab_stops(output_file_name):
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

### Rubriques liées au texte

- [Travailler avec du texte dans un PDF avec Python](/pdf/python-net/working-with-text/)
- [Ajouter du texte à un PDF](/pdf/python-net/add-text-to-pdf-file/)
- [Faire pivoter du texte dans un PDF avec Python](/pdf/python-net/rotate-text-inside-pdf/)
- [Remplacer du texte dans un PDF avec Python](/pdf/python-net/replace-text-in-pdf/)
