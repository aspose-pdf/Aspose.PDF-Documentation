---
title: Ajout d'en-tête et de pied de page à un PDF avec Python
linktitle: Ajout d'en-tête et de pied de page au PDF
type: docs
weight: 50
url: /fr/python-net/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF pour Python via .NET vous permet d'ajouter des en-têtes et des pieds de page à votre fichier PDF à l'aide de la classe TextStamp.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment ajouter un en-tête et un pied de page à un PDF avec Python
Abstract: Cet article fournit un guide complet sur l'utilisation de **Aspose.PDF pour Python via .NET** pour ajouter des en-têtes et des pieds de page aux fichiers PDF, avec la possibilité d'incorporer du texte ou des images. Il commence par détailler l'utilisation de la classe `TextStamp` pour insérer du texte dans l'en-tête d'un document PDF. Des propriétés clés telles que la taille de police, le style et la couleur sont réglables, et la méthode pour ajouter du texte à l'en-tête est illustrée avec un extrait de code Python. L'article explique de même comment ajouter du texte au pied de page, en suivant les mêmes étapes procédurales. Pour ajouter des images, la classe `ImageStamp` est utilisée, et le processus est décrit pour les en-têtes et les pieds de page, également illustré par des exemples de code Python. De plus, l'article aborde l'ajout de plusieurs en-têtes dans un même fichier PDF. Cela comprend la création de plusieurs objets `TextStamp`, chacun avec un formatage distinct, et leur application à différentes pages. L'explication est complétée par un extrait de code détaillé démontrant cette fonctionnalité.
---

Cette page fournit un aperçu concis de l'ajout d'en-têtes et de pieds de page aux documents PDF à l'aide d'Aspose.PDF pour Python via .NET, couvrant les approches basées sur le texte, le HTML, LaTeX, l'image et le tableau ainsi que la numérotation dynamique des pages et les multiples en-têtes par page ; elle explique comment créer et styliser les objets [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) (en utilisant [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/), [`HtmlFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlfragment/), [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/), [`Image`](https://reference.aspose.com/pdf/python-net/aspose.pdf/image/), [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/), etc.), ajuster [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) et [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/) pour un placement précis, et attacher les résultats aux pages avec des exemples de code Python pratiques.

**Aspose.PDF pour Python via .NET** vous permet d'ajouter des en-têtes et des pieds de page à votre [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) existant. Vous pouvez ajouter des images ou du texte à un document PDF. Essayez également d'ajouter différents en-têtes dans un même fichier PDF avec Python.

## Ajout d'en-têtes et de pieds de page sous forme de fragments de texte

Ajoutez des en-têtes et des pieds de page texte simples à toutes les pages d'un PDF. Il crée des objets [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) , insère des éléments [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/) dans ceux‑ci, définit [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) pour un positionnement correct, et les attache à chaque page du document. Le résultat est un PDF où chaque page affiche un texte d'en‑tête et de pied de page cohérent.

Le fragment de code suivant montre comment ajouter des en‑têtes et des pieds de page sous forme de fragments de texte dans un PDF en utilisant Python :

1. Créez des fragments de texte pour l'en‑tête et le pied de page.
1. Créez des objets HeaderFooter et ajoutez les fragments de texte à ceux‑ci.
1. Définissez les paramètres de marge pour contrôler le placement de l'en‑tête et du pied de page.
1. Chargez le document PDF à partir du fichier d'entrée.
1. Parcourez toutes les pages du document.
1. Assignez l'en‑tête et le pied de page à chaque page.
1. Enregistrez le PDF modifié dans le fichier de sortie.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_header_and_footer_as_text(input_file, output_file):
    """
    Add simple text headers and footers to all pages of a PDF document.

    Creates basic text-based headers and footers that appear on every page
    of the PDF document. Headers show "header" text and footers show "footer" text.

    Args:
        input_file (str): Path to the input PDF file.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Adds identical headers and footers to all pages
        - Sets margins of 50 units left and 20 units top
        - Uses simple TextFragment elements for content
        - Headers and footers are created separately for each page

    Example:
        >>> add_header_and_footer_as_text("input.pdf", "output.pdf")
        # Adds text headers and footers to all pages
    """
    # Create header text
    header_text = ap.text.TextFragment("Demo header")
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_text)

    # Create footer text
    footer_text = ap.text.TextFragment("Demo footer")

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_text)

    # Set header margin
    margin = ap.MarginInfo()
    margin.left = 50
    margin.top = 20
    header.margin = margin

    # Set footer margin
    footer.margin = margin

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

Cette méthode est utile pour ajouter des titres cohérents, des indicateurs de page ou des mentions légales en haut et en bas de chaque page. Vous pouvez également l'étendre pour inclure des images ou du contenu dynamique, comme les numéros de page.

## Ajout d'en‑têtes et de pieds de page pour la numérotation des pages

Ajoutez une numérotation automatique des pages aux en‑têtes et pieds de page d'un document PDF à l'aide d'Aspose.PDF pour Python. En utilisant les variables intégrées $p (numéro de page actuel) et $P (nombre total de pages), le script insère dynamiquement la numérotation sur chaque page. Les en‑têtes affichent le format « Page X sur Y », tandis que les pieds de page montrent « Page X / Y ». Le [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) assure un placement correct sur chaque page.

1. Créez un TextFragment pour l'en‑tête en utilisant "Page $p from $P" pour afficher la page actuelle et le total.
1. Créez un objet HeaderFooter et ajoutez le texte d'en‑tête à celui‑ci.
1. Créez un TextFragment pour le pied de page en utilisant "Page $p / $P" comme style de numérotation alternatif.
1. Créez un objet Footer et ajoutez le texte du pied de page.
1. Définissez les paramètres de marge (gauche = 50, haut = 20) et appliquez‑les à la fois à l'en‑tête et au pied de page.
1. Ouvrez le document PDF à partir du fichier d'entrée.
1. Parcourez toutes les pages et assignez l'en‑tête et le pied de page à chaque page.
1. Enregistrez le PDF mis à jour dans le chemin de sortie.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def using_header_and_footer_for_page_numbering(input_file, output_file):
    """
    Add page numbering headers and footers to all pages of a PDF document.

    Creates headers and footers with dynamic page numbering using special variables.
    The $p variable represents the current page number and $P represents the total
    number of pages in the document.

    Args:
        input_file (str): Path to the input PDF file.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses $p for current page number and $P for total pages
        - Header shows "Page X from Y" format
        - Footer shows "Page X / Y" format
        - Variables are automatically replaced by Aspose.PDF
        - Sets margins of 50 units left and 20 units top
        - Page numbering updates dynamically for each page

    Example:
        >>> using_header_and_footer_for_page_numbering("input.pdf", "output.pdf")
        # Adds page numbering headers and footers to all pages
    """
    # Create header text
    header_text = ap.text.TextFragment("Page $p from $P")
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_text)

    # Create footer text
    footer_text = ap.text.TextFragment("Page $p / $P")

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_text)

    # Create margins
    margin = ap.MarginInfo()
    margin.left = 50
    margin.top = 20

    # Set header margin
    header.margin = margin
    # Set footer margin
    footer.margin = margin

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## Ajout d'en‑têtes et de pieds de page sous forme de fragments HTML

Appliquez des en‑têtes et pieds de page au format HTML à chaque page d'un document PDF en utilisant Aspose.PDF pour Python. En utilisant [`HtmlFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlfragment/), le script permet un style de texte riche — tel que gras et italique — d’apparaître dans l'en‑tête et le pied de page. Le [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) est appliqué pour un placement correct, et les mêmes éléments formatés sont attachés à chaque page du document.

Le fragment de code suivant montre comment ajouter des en‑têtes et pieds de page sous forme de fragments HTML à un PDF en utilisant Python :

1. Créez un extrait d'en‑tête HTML en utilisant HtmlFragment — incluant du texte stylisé tel que '<strong>' pour le gras.
1. Créez un objet HeaderFooter et ajoutez l'en‑tête HTML à celui‑ci.
1. Créez un extrait de pied de page HTML en utilisant '<i>' pour le style italique.
1. Créez un objet Footer et ajoutez le HTML du pied de page.
1. Configurez les marges (gauche = 50, haut = 20) et attribuez‑les à la fois à l'en‑tête et au pied de page.
1. Chargez le document PDF en utilisant 'ap.Document()'.
1. Parcourez toutes les pages et assignez l'en‑tête et le pied de page à chacune d'elles.
1. Enregistrez le PDF modifié dans le chemin de sortie spécifié.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_header_and_footer_as_html(input_file, output_file):
    """
    Add HTML-formatted headers and footers to all pages of a PDF document.

    Creates rich HTML-based headers and footers with formatting like bold
    and italic text. Demonstrates how to use HtmlFragment for styled content.

    Args:
        input_file (str): Path to the input PDF file.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses HtmlFragment for rich text formatting
        - Header includes HTML with <strong> tag for bold text
        - Footer includes HTML with <i> tag for italic text
        - Sets margins of 50 units left and 20 units top
        - HTML tags are rendered properly in the PDF

    Example:
        >>> add_header_and_footer_as_html("input.pdf", "output.pdf")
        # Adds HTML-formatted headers and footers to all pages
    """
    # Create header HTML
    header_html = ap.HtmlFragment("This is an HTML <strong>Header</strong>")
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_html)

    # Create footer HTML
    footer_html = ap.HtmlFragment("Powered by <i>Aspose.PDF</i>")

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_html)

    # Set header margin
    margin = ap.MarginInfo()
    margin.left = 50
    margin.top = 20
    header.margin = margin

    # Set footer margin
    footer.margin = margin

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

L'utilisation de HtmlFragment permet un formatage riche avec des styles en ligne ou du balisage HTML, offrant plus de flexibilité de conception par rapport au texte brut.

## Ajout d'en‑têtes et de pieds de page sous forme d'images

Ajoutez des en‑têtes et pieds de page basés sur des images à chaque page d'un document PDF en utilisant Aspose.PDF pour Python. Le même fichier image est utilisé pour l'en‑tête et le pied de page sur chaque page. Le [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) positionne les images, et l'image s'ajuste automatiquement pour tenir dans la zone d'en‑tête/pied de page.

L'extrait de code suivant montre comment ajouter des en-têtes et pieds de page sous forme d'images à un PDF en utilisant Python :

1. Chargez l'image dans un objet 'ap.Image' et préparez-la pour une utilisation en tant qu'en-tête.
1. Créez un objet HeaderFooter et attachez-y l'image d'en-tête.
1. Rechargez la même image pour l'utiliser comme pied de page.
1. Créez un objet Footer et ajoutez-y l'image du pied de page.
1. Chargez le document PDF d'entrée en utilisant 'ap.Document()'.
1. Parcourez toutes les pages du document.
1. Appliquez des marges (gauche = 50) pour positionner à la fois l'en-tête et le pied de page.
1. Assignez l'en-tête et le pied de page à chaque page du PDF.
1. Enregistrez le PDF mis à jour dans le fichier de sortie spécifié.

Cette technique est idéale pour marquer les documents avec des logos ou des filigranes dans la zone d'en-tête/pied de page.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_header_and_footer_as_image(input_file, image_file, output_file):
    """
    Add image-based headers and footers to all pages of a PDF document.

    Creates headers and footers using image files. The same image is used
    for both header and footer positioning on each page.

    Args:
        input_file (str): Path to the input PDF file.
        image_file (str): Path to the image file to use for headers and footers.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses the same image file for both header and footer
        - Creates separate Image objects for header and footer
        - Sets margin of 50 units left for positioning
        - Image files should be in supported formats (PNG, JPG, etc.)
        - Images are automatically sized to fit header/footer areas

    Example:
        >>> add_header_and_footer_as_image("input.pdf", "logo.png", "output.pdf")
        # Adds image headers and footers using logo.png
    """

    # Create header image
    header_image = ap.Image()
    header_image.file = image_file
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_image)

    # Create footer image
    footer_image = ap.Image()
    footer_image.file = image_file

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_image)

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Set header margin
            margin = ap.MarginInfo()
            margin.left = 50
            header.margin = margin

            # Set footer margin
            footer.margin = margin

            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## Ajouter des en-têtes et pieds de page sous forme de tableau

Ajoutez des en-têtes et pieds de page structurés, basés sur des tableaux, à toutes les pages d'un document PDF en utilisant Aspose.PDF for Python. Les objets [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) offrent un meilleur contrôle de mise en page, un alignement et un formatage cohérent pour les en-têtes et pieds de page complexes. Le texte de l'en-tête est centré tandis que le texte du pied de page est aligné à gauche, tous deux utilisant la police Arial 12 pt. Les largeurs de colonnes sont calculées dynamiquement en fonction des dimensions de la page afin d'assurer un placement correct.

Cet extrait de code ajoute des en-têtes et pieds de page (en utilisant des tables) à chaque page d'un document PDF avec Aspose.PDF for Python via .NET.

1. Définissez les styles de texte en utilisant [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/) pour l'en-tête et le pied de page (police, taille, alignement).
1. Créez des objets [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) pour l'en-tête et le pied de page.
1. Construisez le [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) d'en-tête avec une seule ligne et une cellule contenant le texte de l'en-tête.
1. Construisez le [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) de pied de page avec une seule ligne et une cellule contenant le texte du pied de page.
1. Ajoutez les tableaux aux objets [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) correspondants.
1. Définissez le [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) du pied de page pour un positionnement horizontal approprié.
1. Ouvrez le [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) en utilisant les méthodes appropriées.
1. Parcourez toutes les pages et affectez l'en-tête et le pied de page basés sur des tableaux à chaque page.
1. Enregistrez le [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) modifié dans le fichier de sortie.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_header_and_footer_as_table(input_file, output_file):
    """
    Add table-based headers and footers to all pages of a PDF document.

    Creates headers and footers using table structures for better layout
    control and alignment. Demonstrates advanced formatting with text states.

    Args:
        input_file (str): Path to the input PDF file.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses Table objects for structured layout
        - Header table has centered Arial 12pt text
        - Footer table has left-aligned Arial 12pt text
        - Column width calculated based on page width minus margins
        - Provides more precise control over text positioning

    Example:
        >>> add_header_and_footer_as_table("input.pdf", "output.pdf")
        # Adds table-structured headers and footers to all pages
    """
    text_state_header = ap.text.TextState()
    text_state_header.font = ap.text.FontRepository.find_font("Arial")
    text_state_header.font_size = 12
    text_state_header.horizontal_alignment = ap.HorizontalAlignment.CENTER
    text_state_footer = ap.text.TextState()
    text_state_footer.font = ap.text.FontRepository.find_font("Arial")
    text_state_footer.font_size = 12
    text_state_footer.horizontal_alignment = ap.HorizontalAlignment.LEFT
    # Create header
    header = ap.HeaderFooter()
    # Create footer
    footer = ap.HeaderFooter()
    # Create header Table
    table_header = ap.Table()
    table_header.column_widths = str(594 - header.margin.left - header.margin.right)
    header_row = table_header.rows.add()
    header_row.cells.add("This is a Table Header", text_state_header)
    # Create footer Table
    table = ap.Table()
    table.column_widths = str(594 - footer.margin.left - footer.margin.right)
    table.rows.add().cells.add("Powered by Aspose.PDF", text_state_footer)
    header.paragraphs.add(table_header)
    footer.paragraphs.add(table)
    # Set footer margin
    footer.margin.left = 150

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## Ajouter des en-têtes et pieds de page sous forme de LaTeX

Ajoutez des en-têtes et pieds de page contenant du contenu formaté en LaTeX à toutes les pages d'un document PDF en utilisant Aspose.PDF for Python. LaTeX permet de rendre des symboles mathématiques, des dates, des marques de copyright et d'autres mises en forme avancées. L'en-tête inclut une date dynamique, tandis que le pied de page affiche un symbole de copyright ainsi que le numéro de page actuel et le nombre total de pages.

L'extrait de code suivant montre comment utiliser [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) dans les en-têtes et pieds de page d'un PDF en utilisant Aspose.PDF for Python via .NET.

1. Ouvrez le [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) en utilisant les méthodes appropriées.
1. Déterminez le nombre total de pages à utiliser dans les pieds de page dynamiques.
1. Parcourez toutes les pages du document.
1. Créez un objet [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) pour l'en-tête.
1. Créez un [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) pour le texte d'en-tête contenant des commandes LaTeX (par ex., `\\today\\`).
1. Créez un objet [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) pour le pied de page.
1. Créez un [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) pour le texte du pied de page incluant des symboles LaTeX et la numérotation des pages.
1. Ajoutez le [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) à l'objet d'en-tête/pied de page correspondant.
1. Liez l'en-tête et le pied de page à la page actuelle.
1. Enregistrez le [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) modifié dans le fichier de sortie.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_header_and_footer_as_latex(input_file, output_file):
    """
    Add LaTeX-formatted headers and footers to all pages of a PDF document.

    Creates headers and footers using LaTeX markup for mathematical expressions,
    symbols, and advanced formatting. Demonstrates TeXFragment usage.

    Args:
        input_file (str): Path to the input PDF file.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses TeXFragment for LaTeX rendering
        - Header includes LaTeX date command (\\today\\)
        - Footer includes copyright symbol and page numbering
        - LaTeX commands are processed and rendered properly
        - Page count is dynamically calculated and inserted

    Example:
        >>> add_header_and_footer_as_latex("input.pdf", "output.pdf")
        # Adds LaTeX-formatted headers and footers with symbols and page numbers
    """
    # Open PDF document
    with ap.Document(input_file) as document:
        page_count = len(document.pages)
        for i in range(1, page_count + 1):
            # Create header
            header = ap.HeaderFooter()
            h_latex_text = "This is a LaTex Header. \\today\\"
            h_l_text = ap.TeXFragment(h_latex_text, True)
            # Create footer
            footer = ap.HeaderFooter()
            f_latex_text = f"\\copyright\\ 2025 My Company -- Page \\thepage\\ is {page_count}"
            f_l_text = ap.TeXFragment(f_latex_text, True)

            header.paragraphs.add(h_l_text)
            footer.paragraphs.add(f_l_text)
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```
