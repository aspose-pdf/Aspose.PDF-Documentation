---
title: Rechercher et extraire du texte des pages PDF
linktitle: Rechercher et extraire du texte
type: docs
weight: 60
url: /fr/python-net/search-and-get-text-from-pdf/
description: Apprenez comment rechercher et extraire du texte à partir de documents PDF en Python en utilisant Aspose.PDF pour l'analyse de documents.
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment rechercher et extraire du texte des pages d'un PDF
Abstract: L'article fournit une exploration approfondie des capacités d'extraction et de manipulation de texte dans les documents PDF en utilisant la bibliothèque Aspose.PDF for Python via .NET. Il présente la classe TextFragmentAbsorber, qui permet aux développeurs de rechercher dans tout le document ou dans des pages spécifiques des phrases désignées ou des motifs d'expressions régulières. La page décrit divers scénarios pratiques—tels que la récupération du contenu texte, la détermination de sa position (y compris les coordonnées et les valeurs d'indentation), et l'extraction des propriétés de police comme le nom, la taille, le statut d'incorporation et la couleur—à partir des fragments de texte correspondants. Des exemples de code détaillés montrent le processus étape par étape, facilitant l'intégration des capacités de recherche de texte dans les applications des développeurs.
---

## Recherche de texte à partir du PDF

Recherchez et extrayez du texte d'une zone rectangulaire définie dans un document PDF en utilisant la classe TextAbsorber. Elle utilise le mode de formatage texte pur pour une sortie de texte propre et non formatée, ce qui la rend idéale pour extraire le contenu de régions structurées comme les en-têtes, pieds de page ou zones de tableau. En combinant TextExtractionOptions et TextSearchOptions avec des contraintes rectangulaires, cet exemple vous offre un contrôle précis sur le lieu et la manière dont le texte est extrait du document.

1. Chargez le fichier PDF en utilisant 'ap.Document'.
1. Configurez les options d'extraction de texte.
1. Définissez la zone de recherche avec des contraintes rectangulaires.
1. Créez et configurez TextAbsorber.
1. Traitez toutes les pages du document.
1. Récupérez et affichez le texte extrait.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_absorber_search(input_file_path):
    """
    Search and extract text from PDF using TextAbsorber with area constraints.

    Demonstrates basic text extraction from a PDF document using TextAbsorber
    with pure text formatting mode and rectangular boundary constraints.
    Extracts text from all pages within the specified rectangular area.

    Args:
        input_file_path (str): Path to the input PDF file to search.

    Returns:
        None: Prints extracted text to console.

    Note:
        - Uses PURE text formatting mode for clean text extraction
        - Constrains search to rectangle (0, 0, 842, 250)
        - Processes all pages in the document
        - TextAbsorber provides high-level text extraction capabilities
        - Good for extracting text content without detailed positioning

    Example:
        >>> text_absorber_search("document.pdf")
        # Prints all text found in the specified rectangular area across all pages
    """
    # Open PDF document
    document = ap.Document(input_file_path)

    text_extraction_options = ap.text.TextExtractionOptions(
        ap.text.TextExtractionOptions.TextFormattingMode.PURE
    )
    text_search_options = ap.text.TextSearchOptions(ap.Rectangle(0, 0, 842, 250, True))

    absorber = ap.text.TextAbsorber(text_extraction_options, text_search_options)

    # Process all pages
    document.pages.accept(absorber)

    print(f"Text fragments found: {absorber.text}")
```

## Recherche de texte à partir d'une page PDF spécifique

Recherchez et extrayez du texte d'une page et d'une région spécifiques dans un PDF en utilisant TextAbsorber d'Aspose.PDF. Il cible la page 2 du document et extrait uniquement le texte trouvé dans une zone rectangulaire définie.
En combinant TextExtractionOptions (pour le contrôle du formatage) et TextSearchOptions (pour la limitation de zone), vous pouvez effectuer une extraction de texte précise et spécifique à la page de manière efficace.

1. Chargez le document PDF.
1. Configurez les options d'extraction de texte.
1. Limitez l'extraction du texte à une zone rectangulaire spécifique sur la page.
1. Créez et configurez TextAbsorber.
1. Traitez une page spécifique.
1. Récupérez et affichez le texte extrait.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_absorber_search_page(input_file_path):
    """
    Search and extract text from a specific PDF page using TextAbsorber.

    Demonstrates targeted text extraction from a single page (page 2) using
    TextAbsorber with area constraints. Shows how to limit search scope to
    specific pages and rectangular regions.

    Args:
        input_file_path (str): Path to the input PDF file to search.

    Returns:
        None: Prints extracted text from page 2 to console.

    Note:
        - Targets only page 2 of the document (document.pages[2])
        - Uses PURE text formatting mode for clean extraction
        - Constrains search to rectangle (0, 0, 842, 250)
        - Useful for page-specific text extraction
        - More efficient than processing entire document when targeting specific pages

    Example:
        >>> text_absorber_search_page("document.pdf")
        # Prints text found in the specified area on page 2 only
    """
    document = ap.Document(input_file_path)

    text_extraction_options = ap.text.TextExtractionOptions(
        ap.text.TextExtractionOptions.TextFormattingMode.PURE
    )
    text_search_options = ap.text.TextSearchOptions(ap.Rectangle(0, 0, 842, 250, True))

    absorber = ap.text.TextAbsorber(text_extraction_options, text_search_options)

    # Only page 2
    document.pages[2].accept(absorber)

    print(f"Text fragments found: {absorber.text}")

```

## Analyser et extraire les propriétés détaillées des fragments de texte d'un PDF

Contrairement à TextAbsorber, qui extrait du texte brut, TextFragmentAbsorber fournit des informations détaillées et de bas niveau sur chaque fragment de texte — telles que sa position, les attributs de police, la couleur et les détails d'incorporation.

1. Chargez le document PDF.
1. Initialisez TextFragmentAbsorber.
1. Traitez toutes les pages du document.
1. Parcourez les fragments de texte extraits.
1. Affichez les informations de base du texte.
1. Affichez les détails de la police et du formatage.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search(input_file_path):
    """
    Search and analyze all text fragments in a PDF with detailed properties.

    Demonstrates comprehensive text fragment analysis using TextFragmentAbsorber
    to extract all text with detailed positioning, font, and formatting information.
    Provides low-level access to text properties for detailed analysis.

    Args:
        input_file_path (str): Path to the input PDF file to analyze.

    Returns:
        None: Prints detailed text fragment information to console.

    Note:
        - Extracts all text fragments from all pages
        - Provides detailed properties: position, font info, colors, sizes
        - Shows font accessibility, embedding, and subset information
        - Useful for detailed text analysis and formatting inspection
        - TextFragmentAbsorber offers more granular control than TextAbsorber

    Example:
        >>> text_fragment_absorber_search("document.pdf")
        # Prints comprehensive details about every text fragment in the document
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    document.pages.accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
        print("XIndent:", fragment.position.x_indent)
        print("YIndent:", fragment.position.y_indent)
        print("Font - Name:", fragment.text_state.font.font_name)
        print("Font - IsAccessible:", fragment.text_state.font.is_accessible)
        print("Font - IsEmbedded:", fragment.text_state.font.is_embedded)
        print("Font - IsSubset:", fragment.text_state.font.is_subset)
        print("Font Size:", fragment.text_state.font_size)
        print("Foreground Color:", fragment.text_state.foreground_color)
```

## Recherche d'une phrase texte spécifique sur une seule page PDF

Recherchez une phrase texte spécifique dans une page d'un document PDF en utilisant TextFragmentAbsorber. Contrairement à la recherche dans tout le document, cette approche limite la recherche à une seule page, ce qui la rend plus efficace pour confirmer la présence et l'emplacement du texte dans des zones ciblées comme les en-têtes, pieds de page ou sections de contenu spécifiques.

1. Chargez le document PDF.
1. Initialise TextFragmentAbsorber avec la phrase recherchée.
1. Appliquez l'absorbeur à la page spécifique.
1. Parcourez les fragments trouvés.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_page(input_file_path):
    """
    Search for specific text phrase on a particular PDF page.

    Demonstrates targeted text search for a specific phrase ("whale") on
    a single page. Shows how to combine phrase searching with page-specific
    scope for efficient and focused text location.

    Args:
        input_file_path (str): Path to the input PDF file to search.

    Returns:
        None: Prints matching text fragments and their positions to console.

    Note:
        - Searches for the phrase "whale" on page 2 only
        - Returns text fragments with position information
        - More efficient than document-wide search when targeting specific pages
        - Useful for validating content presence in specific document sections
        - Provides exact positioning coordinates for found text

    Example:
        >>> text_fragment_absorber_search_page("document.pdf")
        # Prints all instances of "whale" found on page 2 with their positions
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber("whale")
    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## Recherche séquentielle de texte page par page avec résultats cumulatifs

Recherchez du texte de manière incrémentale à travers plusieurs pages d'un document PDF en utilisant TextFragmentAbsorber d'Aspose.PDF.
Contrairement à une recherche sur une seule page ou sur l'ensemble du document, cette méthode vous permet de traiter les pages séquentiellement, de collecter les résultats progressivement et d'analyser les fragments de texte avec un contexte spécifique à chaque page. Cette approche est idéale pour les documents volumineux ou les flux de traitement progressifs.

1. Chargez le document PDF.
1. Initialise TextFragmentAbsorber et définissez la phrase de recherche.
1. Traitez la première page. Recherchez uniquement la page 1. Affiche le texte, le numéro de page et la position. Fournit des résultats isolés propres à chaque page pour plus de clarté.
1. Traitez la page suivante séquentiellement. Passez à la page 2 et continuez éventuellement à travers le reste du document. Le 'absorber.visit()' garantit l'accumulation des résultats de toutes les pages visitées. Affiche les résultats de recherche cumulés, montrant à la fois le texte et l'emplacement.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_sequential_search(input_file_path):
    """
    Demonstrate sequential page-by-page text search with cumulative results.

    Shows how to perform incremental text searches across multiple pages,
    accumulating results from each page. Demonstrates both individual page
    processing and document-wide search continuation.

    Args:
        input_file_path (str): Path to the input PDF file to search.

    Returns:
        None: Prints text fragments from sequential page searches to console.

    Note:
        - Searches for "whale" on page 1, then continues to page 2
        - Uses absorber.visit(document) to process remaining pages
        - Demonstrates incremental search accumulation
        - Shows page numbers for found fragments
        - Useful for progressive document processing and result accumulation

    Example:
        >>> text_fragment_absorber_sequential_search("document.pdf")
        # Prints "whale" instances from page 1, then from all remaining pages
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    absorber.phrase = "whale"

    # First page
    document.pages[1].accept(absorber)
    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Page:", fragment.page.number)
        print("Position:", fragment.position)

    print("--")

    # Continue to next page
    document.pages[2].accept(absorber)
    absorber.visit(document)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Page:", fragment.page.number)
        print("Position:", fragment.position)
```

## Recherche de phrase ciblée dans une zone rectangulaire

Recherchez une phrase spécifique dans un PDF tout en limitant la recherche à une zone rectangulaire précise sur une seule page.
En combinant la recherche de phrase avec des contraintes spatiales, vous pouvez localiser le contenu avec précision dans des zones désignées sans analyser toute la page ou le document. Cela est particulièrement utile pour les formulaires, en-têtes, pieds de page ou rapports structurés où le contenu apparaît à des emplacements prévisibles.

1. Chargez le document PDF.
1. Initialise TextFragmentAbsorber avec la phrase et les contraintes rectangulaires
1. Appliquez l'absorbeur à la page 2. Restreint le traitement à la page 2, réduisant les calculs inutiles. Garantit que la recherche est spécifique à la page.
1. Parcourez les fragments trouvés et affichez-les

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_phrase(input_file_path):
    """
    Search for specific phrase within a rectangular area constraint.

    Demonstrates targeted phrase searching with both text matching and
    spatial constraints. Combines phrase search with rectangular boundary
    limitations for precise content location.

    Args:
        input_file_path (str): Path to the input PDF file to search.

    Returns:
        None: Prints matching text fragments and positions to console.

    Note:
        - Searches for "elephant" phrase on page 2
        - Constrains search to rectangle (0, 0, 842, 250)
        - Combines text matching with spatial filtering
        - Useful for finding content in specific document regions
        - More precise than page-wide or document-wide searches

    Example:
        >>> text_fragment_absorber_search_phrase("document.pdf")
        # Prints "elephant" instances found within the specified rectangular area on page 2
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber(
        "elephant", ap.text.TextSearchOptions(ap.Rectangle(0, 0, 842, 250, True))
    )

    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## Recherche de motifs de texte dans un PDF à l'aide d'expressions régulières

Recherchez des motifs de texte dans un PDF en utilisant des expressions régulières. En activant le mode regex dans TextFragmentAbsorber, vous pouvez localiser des motifs complexes tels que des nombres, des dates, des prix, des coordonnées ou des formats de texte personnalisés. La fonction limite la recherche à une page spécifique, ce qui la rend efficace pour l'extraction ciblée de données structurées.

1. Chargez le document PDF.
1. Initialise TextFragmentAbsorber avec le motif regex.
1. Appliquez l'absorbeur à la page 2. Limite la recherche à la page 2 pour plus d'efficacité et de précision. Seul le texte de cette page est analysé.
1. Parcourez les fragments trouvés. Affiche les fragments de texte correspondants et leurs coordonnées. Fournit des informations de localisation précises pour les motifs extraits.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_regex(input_file_path):
    """
    Search for text patterns using regular expressions.

    Demonstrates advanced text searching using regular expression patterns
    to find complex text structures like numbers, dates, or custom formats.
    Shows how to enable regex mode in TextFragmentAbsorber.

    Args:
        input_file_path (str): Path to the input PDF file to search.

    Returns:
        None: Prints matching text fragments and positions to console.

    Note:
        - Uses regex pattern r"\\d+\\.\\d+" to find decimal numbers
        - Enables regex mode with is_regular_expression_used=True
        - Searches on page 2 only
        - Powerful for finding formatted data like prices, coordinates, dates
        - Regular expressions provide flexible pattern matching capabilities

    Example:
        >>> text_fragment_absorber_search_regex("document.pdf")
        # Prints all decimal numbers (e.g., "12.34", "0.99") found on page 2
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber(r"\d+\.\d+", ap.text.TextSearchOptions(is_regular_expression_used=True))

    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## Convertir les correspondances de texte en hyperliens dans un PDF à l'aide de TextFragmentAbsorber

Recherchez des phrases de texte spécifiques dans un PDF et convertissez-les en hyperliens cliquables. En utilisant TextFragmentAbsorber avec des motifs regex, il localise les mots cibles et applique un style visuel (couleur et soulignement) ainsi que des liens interactifs.

1. Chargez le document PDF.
1. Initialise TextFragmentAbsorber avec le motif regex.
1. Appliquez l'absorbeur à la page 1.
1. Appliquez le style et ajoutez des hyperliens aux correspondances.
1. Enregistrez le PDF modifié.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_and_add_hyperlink(input_file_path):
    """
    Search for text and convert matches to hyperlinks with styling.

    Demonstrates advanced text processing by finding specific words and
    converting them into clickable hyperlinks with visual styling. Shows
    how to combine text search with document modification.

    Args:
        input_file_path (str): Path to the input PDF file to process.

    Returns:
        None: Saves modified PDF with hyperlinks to output file.

    Note:
        - Searches for "whale|elephant" using regex pattern on page 1
        - Converts found text to Wikipedia hyperlinks
        - Applies blue color and underline styling to hyperlinks
        - Creates new output file with "_out.pdf" suffix
        - Demonstrates practical text enhancement and interactivity
        - Combines search, styling, and hyperlinking in one operation

    Example:
        >>> text_fragment_absorber_search_and_add_hyperlink("document_in.pdf")
        # Creates "document_out.pdf" with "whale" and "elephant" as clickable Wikipedia links
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber("whale|elephant")
    absorber.text_search_options = ap.text.TextSearchOptions(True)

    absorber.visit(document.pages[1])

    for fragment in absorber.text_fragments:
        fragment.text_state.foreground_color = ap.Color.blue
        fragment.text_state.underline = True
        fragment.hyperlink = ap.WebHyperlink(
            f"https://en.wikipedia.org/wiki/{fragment.text}"
        )

    output = input_file_path.replace("in.pdf", "out.pdf")
    document.save(output)
```

## Rechercher et identifier le texte stylisé dans un PDF à l'aide de TextFragmentAbsorber

Recherchez des fragments de texte dans un PDF en fonction de leurs propriétés de formatage plutôt que de leur contenu. Avec TextFragmentAbsorber, il identifie le texte avec des styles spécifiques, comme le texte en gras.

1. Chargez le document PDF.
1. Initialise TextFragmentAbsorber.
1. Appliquez l'absorbeur à la page 1.
1. Inspectez les fragments de texte en fonction du formatage. Vérifie le style de police pour le format gras.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_styled_text(input_file_path):
    """
    Search and identify text based on formatting properties.

    Demonstrates how to find text fragments based on their formatting
    characteristics rather than content. Shows detection of bold text
    and invisible text within the document.

    Args:
        input_file_path (str): Path to the input PDF file to analyze.

    Returns:
        None: Prints formatted text findings to console.

    Note:
        - Searches all text fragments on page 1
        - Identifies text with FontStyles.BOLD formatting
        - Detects invisible/hidden text using text_state.invisible
        - Useful for formatting analysis and hidden content detection
        - Demonstrates text property-based filtering capabilities

    Example:
        >>> text_fragment_absorber_search_styled_text("document.pdf")
        # Prints all bold text and any hidden/invisible text found on page 1
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    absorber.text_search_options = ap.text.TextSearchOptions(True)

    absorber.visit(document.pages[1])

    for fragment in absorber.text_fragments:
        if fragment.text_state.font_style == ap.text.FontStyles.BOLD:
            print(f"Bold: {fragment.text}")
```

Détecte le texte caché ou invisible dans un document PDF en analysant les propriétés de formatage du texte :

1. Chargez le document PDF.
1. Initialise TextFragmentAbsorber.
1. Appliquez l'absorbeur à la page 1.
1. Inspectez les fragments de texte en fonction du formatage. Vérifiez 'fragment.text_state.invisible' pour le texte caché.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_styled_text(input_file_path):
    """
    Search and identify text based on formatting properties.

    Demonstrates how to find text fragments based on their formatting
    characteristics rather than content. Shows detection of bold text
    and invisible text within the document.

    Args:
        input_file_path (str): Path to the input PDF file to analyze.

    Returns:
        None: Prints formatted text findings to console.

    Note:
        - Searches all text fragments on page 1
        - Identifies text with FontStyles.BOLD formatting
        - Detects invisible/hidden text using text_state.invisible
        - Useful for formatting analysis and hidden content detection
        - Demonstrates text property-based filtering capabilities

    Example:
        >>> text_fragment_absorber_search_styled_text("document.pdf")
        # Prints all bold text and any hidden/invisible text found on page 1
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    absorber.text_search_options = ap.text.TextSearchOptions(True)

    absorber.visit(document.pages[1])

    for fragment in absorber.text_fragments:
        if fragment.text_state.invisible:
            print(f"Invisible: {fragment.text}")
```

## Mise en évidence visuelle du texte dans les pages PDF

Cette fonction combine la reconnaissance de texte et le rendu en un seul flux de travail. Elle n'extrait pas seulement le texte mais le visualise également en mettant en évidence les fragments, segments et caractères dans des rectangles colorés sur les images PNG de chaque page.

Notre exemple réalise une visualisation avancée du texte sur un PDF en :

- recherchant tous les fragments de texte visibles à l'aide d'expressions régulières
- rendant chaque page PDF en une image PNG haute résolution
- dessinant des rectangles colorés autour des fragments de texte, des segments de texte et des caractères individuels

1. Définissez la résolution de l'image de sortie. Chaque page PDF est convertie en une image PNG de 150 DPI.
1. Ouvrez le PDF et initialisez le Text Absorber.
1. Traitez chaque page. Appliquez l'absorbeur à chaque page. Collectez tous les fragments de texte détectés et leurs positions géométriques.
1. Convertissez la page en flux PNG.
1. Préparez l'objet graphique pour le dessin.
1. Appliquez la transformation de coordonnées. Convertissez les coordonnées PDF en pixels d'image.
1. Dessinez des rectangles pour les éléments de texte.
1. Enregistrez le résultat.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_and_highlight(infile):
    """
    Search text and create visual highlighting with PNG output.

    Advanced function that combines text search with visual highlighting.
    Converts PDF pages to PNG images and draws colored rectangles around
    found text fragments, segments, and individual characters.

    Args:
        infile (str): Path to the input PDF file to process.

    Returns:
        None: Saves highlighted PNG images for each page.

    Note:
        - Uses regex pattern r"[\\S]+" to find all non-whitespace sequences
        - Converts each page to 150 DPI PNG image using PngDevice
        - Draws yellow rectangles around text fragments
        - Draws green rectangles around text segments
        - Draws black rectangles around individual characters
        - Creates detailed visual analysis of text structure
        - Output files named with page numbers: "filename1_out.png", etc.
        - Complex coordinate transformation for proper overlay positioning

    Example:
        >>> text_fragment_absorber_search_and_highlight("document_in.pdf")
        # Creates PNG files with visual highlighting of all text elements
    """
    resolution = 150
    png_device = ap.devices.PngDevice(ap.devices.Resolution(resolution, resolution))

    # Open PDF document
    document = ap.Document(infile)
    absorber = ap.text.TextFragmentAbsorber(r"[\S]+")
    absorber.text_search_options.is_regular_expression_used = True

    for page in document.pages:
        page.accept(absorber)
        stream = io.BytesIO()
        png_device.process(page, stream)
        with drawing.Bitmap.from_stream(stream) as bmp:
            with drawing.Graphics.from_image(bmp) as gr:
                scale = resolution / 72
                gr.transform = drawing.drawing2d.Matrix(
                    float(scale),
                    float(0),
                    float(0),
                    float(-scale),
                    float(0),
                    float(bmp.height),
                )
                text_fragment_collection = absorber.text_fragments
                # Loop through the fragments
                for text_fragment in text_fragment_collection:
                    gr.draw_rectangle(
                        drawing.Pens.yellow,
                        float(text_fragment.position.x_indent),
                        float(text_fragment.position.y_indent),
                        float(text_fragment.rectangle.width),
                        float(text_fragment.rectangle.height),
                    )
                    for seg_num in range(1, len(text_fragment.segments) + 1):
                        segment = text_fragment.segments[seg_num]
                        for char_num in range(1, len(segment.characters) + 1):
                            character_info = segment.characters[char_num]
                            rect = page.get_page_rect(True)
                            print(
                                f"TextFragment = {text_fragment.text}"
                                + f" Page URY = {rect.ury}"
                                + f" TextFragment URY = {text_fragment.rectangle.ury}"
                            )
                            gr.draw_rectangle(
                                drawing.Pens.black,
                                float(character_info.rectangle.llx),
                                float(character_info.rectangle.lly),
                                float(character_info.rectangle.width),
                                float(character_info.rectangle.height),
                            )
                        gr.draw_rectangle(
                            drawing.Pens.green,
                            float(segment.rectangle.llx),
                            float(segment.rectangle.lly),
                            float(segment.rectangle.width),
                            float(segment.rectangle.height),
                        )

                # Save result
                bmp.save(
                    infile.replace("_in.pdf", str(page.number) + "_out.png"),
                    drawing.imaging.ImageFormat.png,
                )
```
