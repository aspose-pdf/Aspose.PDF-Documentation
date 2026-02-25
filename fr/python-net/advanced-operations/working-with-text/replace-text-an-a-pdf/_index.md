---
title: Remplacer du texte dans un PDF via Python
linktitle: Remplacer du texte dans le PDF
type: docs
weight: 40
url: /fr/python-net/replace-text-in-pdf/
description: En savoir plus sur les différentes manières de remplacer et de supprimer du texte avec la bibliothèque Aspose.PDF pour Python via .NET.
lastmod: "2025-10-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
aliases: 
    - /python-net/replace-text-in-a-pdf-document/
TechArticle: true
AlternativeHeadline: Comment remplacer du texte dans un PDF en utilisant Python
Abstract: L'article fournit un guide complet sur diverses techniques de manipulation de texte au sein des documents PDF à l'aide d'Aspose.PDF pour Python via .NET. Il couvre plusieurs stratégies de remplacement de texte, notamment le remplacement du texte sur toutes les pages, dans des régions spécifiques de la page et l'utilisation d'expressions régulières. L'article explique également comment remplacer les polices dans les PDF, en veillant à ce que les polices inutilisées soient supprimées, et comment gérer le remplacement de texte afin de réarranger automatiquement le contenu des pages. De plus, il explore le rendu de symboles remplaçables lors de la création de PDF, y compris leur utilisation dans les zones d'en-tête/pied de page, pour améliorer la personnalisation du document. Enfin, il détaille les méthodes permettant de supprimer tout le texte d'un document PDF, optimisant les opérations pour les scénarios où une suppression complète du texte est nécessaire. Chaque section est accompagnée d'extraits de code en Python et dans d'autres langages supportés afin de démontrer une mise en œuvre pratique.
---

Ces exemples démontrent comment **modifier ou supprimer du texte dans un PDF existant**.

## Remplacer le texte existant

### Remplacer le texte dans toutes les pages du document PDF

{{% alert color="primary" %}}

Vous pouvez essayer de rechercher et remplacer le texte dans le document en utilisant Aspose.PDF et obtenir les résultats en ligne à ce [lien](https://products.aspose.app/pdf/redaction)

{{% /alert %}}

Le remplacement de texte est une exigence courante lors de la mise à jour ou de la correction de contenu dans des documents PDF existants — par exemple, changer les noms de produits, corriger des fautes de frappe ou mettre à jour la terminologie sur plusieurs pages.

Aspose.PDF pour Python via .NET offre une méthode puissante et efficace pour rechercher et remplacer du texte de façon programmatique via la classe [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/).

Cet exemple montre comment trouver toutes les occurrences d'une phrase spécifique (dans ce cas, "Black cat") et les remplacer par une nouvelle phrase ("White dog") dans l'ensemble d'un document PDF.

1. Spécifier les phrases de recherche et de remplacement. Définissez le texte que vous souhaitez rechercher et le texte par lequel il doit être remplacé.
1. Charger le document PDF.
1. Créer un absorbeur de texte. Un TextFragmentAbsorber est initialisé avec la phrase de recherche. Il parcourt le document à la recherche de toutes les instances de la phrase donnée.
1. Appliquer l'absorbeur à toutes les pages. Cela parcourt toutes les pages et collecte les fragments de texte correspondant à la phrase.
1. Remplacer chaque fragment trouvé. Chaque occurrence de "Black cat" doit être changée en "White dog".
1. Enregistrer le PDF mis à jour.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_on_all_pages(infile, outfile):
    """
    Replace text on all pages of a PDF document.

    Searches for a specific text phrase throughout all pages of a PDF document
    and replaces all occurrences with a new phrase. This function demonstrates
    global text replacement using TextFragmentAbsorber.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Replaces "Black cat" with "White dog" as demonstration
        - Searches across all pages in the document
        - Preserves original formatting and layout
        - Uses TextFragmentAbsorber for efficient text search

    Example:
        >>> replace_text_on_all_pages("input.pdf", "output.pdf")
        # Replaces all instances of "Black cat" with "White dog"
    """
    search_phrase = "Black cat"
    replace_phrase = "White dog"

    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(search_phrase)
        document.pages.accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = replace_phrase

        document.save(outfile)
```

### Remplacer le texte dans une région de page particulière

Parfois, vous pouvez avoir besoin de remplacer le texte uniquement dans une zone spécifique d'une page PDF plutôt que de rechercher dans l'ensemble du document — par exemple, mettre à jour un en-tête, un pied de page ou une cellule de tableau à une position connue.

La bibliothèque Aspose.PDF pour Python via .NET permet cette fonctionnalité en utilisant le [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) conjointement avec la recherche de texte basée sur les régions.

Cet exemple montre comment trouver et remplacer toutes les occurrences d'une phrase cible dans une région rectangulaire définie sur une page spécifique.

1. Spécifier les phrases de recherche et de remplacement.
1. Charger le document PDF.
1. Créer un absorbeur de texte pour la recherche. Initialise un TextFragmentAbsorber afin de trouver le texte souhaité.
1. Restreindre la zone de recherche. Le rectangle spécifie les limites des coordonnées x et y sur la page.
1. Appliquer l'absorbeur à une page spécifique. Cela effectue la recherche et collecte les fragments de texte correspondants dans la zone spécifiée.
1. Remplacer le texte trouvé. Chaque occurrence de 'doc' dans la région définie devient 'DOC'.
1. Enregistrer le PDF mis à jour.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_in_particular_page_region(infile, outfile):
    """
    Replace text in a particular region of a page.

    Performs targeted text replacement within a specific rectangular region
    on the first page of a PDF document. This allows for precise control
    over which text gets replaced based on its location.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Replaces "doc" with "DOC" within the specified region
        - Only affects text within coordinates (300, 442, 500, 742)
        - Uses limit_to_page_bounds for precise region control
        - Only processes the first page (pages[1])

    Example:
        >>> replace_text_in_particular_page_region("input.pdf", "output.pdf")
        # Replaces "doc" with "DOC" only in the specified rectangular area
    """
    search_phrase = "doc"
    replace_phrase = "DOC"

    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(search_phrase)
        absorber.text_search_options.limit_to_page_bounds = True
        absorber.text_search_options.rectangle = ap.Rectangle(300, 442, 500, 742, True)
        document.pages[1].accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = replace_phrase

        document.save(outfile)
```

### Redimensionner et déplacer le texte sans changer la taille de la police

Lors du remplacement de texte dans un PDF, il arrive parfois que vous souhaitiez ajuster ou repositionner le nouveau texte dans une zone spécifique sans modifier la taille de la police.
Aspose.PDF pour Python via .NET propose des options pour ajuster la mise en page et l'espacement du texte tout en conservant la taille de police d'origine.

1. Charger le document PDF.
1. Collecter tous les fragments de texte sur la page en utilisant un 'TextFragmentAbsorber'.
1. Sélectionner le fragment à modifier.
1. Déplacer et redimensionner le rectangle du texte.
1. Ajuster l'espacement du texte. Activer l'ajustement de l'espacement pour faire tenir le texte dans le rectangle modifié.
1. Remplacer le texte du fragment.
1. Enregistrer le PDF mis à jour.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_and_resize_and_shift_without_changing_font_size(infile, outfile):
    """
    Resize and shift text without changing the font size.

    Demonstrates how to replace text content while adjusting its position
    and width within a modified rectangular area. The font size remains
    unchanged, but spacing is adjusted to fit the new content.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Targets the second text fragment on the first page
        - Narrows the text rectangle by 50 units on each side
        - Duplicates the original text content
        - Uses ADJUST_SPACE_WIDTH for proper spacing
        - Maintains original font size and style

    Example:
        >>> replace_text_and_resize_and_shift_without_changing_font_size("input.pdf", "output.pdf")
        # Duplicates text in a narrower space with adjusted spacing
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        rect = fragment.rectangle
        rect.llx += 50
        rect.urx -= 50
        fragment.replace_options.rectangle = rect
        fragment.replace_options.replace_adjustment_action = (
             ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### Redimensionner et déplacer un paragraphe dans un PDF

Lorsque vous travaillez avec des PDF, il arrive parfois de devoir remplacer ou développer un paragraphe tout en conservant son alignement visuel avec la mise en page. Aspose.PDF vous permet de redimensionner le rectangle englobant du paragraphe et d’ajuster l’espacement pour adapter le nouveau texte, le tout sans modifier la taille de la police.

1. Charger le document PDF.
1. Utiliser 'TextFragmentAbsorber' pour collecter tous les fragments de texte sur la page.
1. Sélectionner le fragment à modifier.
1. Redimensionner et déplacer le paragraphe. Utilisez la boîte média de la page pour déterminer les limites et ajuster le rectangle.
1. Ajuster l’espacement. Cela modifie l’espacement entre les mots/lettres au lieu de changer la taille de la police.
1. Remplacer le texte du fragment.
1. Enregistrer le PDF modifié.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_and_resize_and_shift_paragraph(infile, outfile):
    """
    Resize and shift a paragraph in the document.

    Demonstrates paragraph-level text replacement with automatic resizing
    to fit within the page's media box boundaries. Adjusts the text area
    to provide margins while duplicating content.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses page media box as base rectangle
        - Adds 20-unit margins on left, right, and top
        - Targets the second text fragment on the first page
        - Duplicates original text content
        - Automatically adjusts space width for proper fit

    Example:
        >>> replace_text_and_resize_and_shift_paragraph("input.pdf", "output.pdf")
        # Resizes paragraph to fit within page margins with duplicated text
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        rect = document.pages[1].media_box
        rect.llx += 20
        rect.urx -= 20
        rect.ury -= 20
        fragment.replace_options.rectangle = rect
        fragment.replace_options.replace_adjustment_action = (
             ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### Remplacer le texte et agrandir automatiquement la police pour remplir la zone cible

Remplacez du texte dans un PDF tout en redimensionnant et en agrandissant automatiquement la police pour remplir une zone rectangulaire spécifique. En utilisant la bibliothèque Aspose.PDF pour Python via .NET, le code ajuste dynamiquement la taille de la police et l’espacement afin que le nouveau contenu texte s’adapte parfaitement à une boîte englobante définie — sans calculs manuels de police.

1. Charger le PDF.
1. Capturer les fragments de texte.
1. Sélectionner un fragment spécifique.
1. Définir le rectangle cible.
1. Activer les options d’ajustement du texte.
1. Remplacer le texte.
1. Enregistrer le document.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_and_resize_and_expand_font(infile, outfile):
    """
    Resize and expand font to fill target area.

    Demonstrates automatic font scaling to fill a specified rectangular area.
    The font size is dynamically adjusted to make the text content fit
    perfectly within the defined target rectangle.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Defines target rectangle at coordinates (100, 300, 512, 692)
        - Uses SCALE_TO_FILL for automatic font size adjustment
        - Duplicates original text content
        - Adjusts space width for optimal text distribution
        - Font size scales up or down to fill the entire rectangle

    Example:
        >>> replace_text_and_resize_and_expand_font("input.pdf", "output.pdf")
        # Scales font to completely fill the specified rectangular area
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        fragment.replace_options.rectangle = ap.Rectangle(100, 300, 512, 692, True)
        fragment.replace_options.replace_adjustment_action = (
             ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.replace_options.font_size_adjustment_action = (
            ap.text.TextReplaceOptions.FontSizeAdjustment.SCALE_TO_FILL
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)

```

### Remplacer le texte et l’ajuster dans un rectangle

Remplacez du texte dans un document PDF tout en veillant à ce que le nouveau contenu s’insère dans la zone rectangulaire du texte original en réduisant automatiquement la taille de la police si nécessaire.

En utilisant la bibliothèque Aspose.PDF pour Python via .NET, cette fonction ajuste dynamiquement la mise en page du texte et la taille de la police, préservant la structure du document tout en évitant le débordement.

1. Créer un objet TextFragmentAbsorber pour extraire tous les fragments de texte de la première page.
1. Accéder à un fragment de texte spécifique.
1. Définir la zone de remplacement.
1. Configurer les options d’ajustement du texte. Définissez deux options de remplacement clés :
- Ajustement de la taille de la police – 'SHRINK_TO_FIT' réduit automatiquement la taille de la police si le nouveau texte est trop long.
- Ajustement de l’espacement – 'ADJUST_SPACE_WIDTH' maintient l’espacement proportionnel.
1. Remplacer le texte.
1. Enregistrer le PDF modifié.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_and_fit_text_into_rectangle(infile, outfile):
    """
    Fit text into a rectangle by adjusting font size.

    Demonstrates how to ensure text content fits within its original
    rectangle by automatically shrinking the font size when the new
    content is longer than the original.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses original text fragment rectangle as target area
        - Employs SHRINK_TO_FIT to reduce font size if needed
        - Duplicates original text content (making it longer)
        - Adjusts space width for proper text distribution
        - Prevents text overflow by automatic font scaling

    Example:
        >>> replace_text_and_fit_text_into_rectangle("input.pdf", "output.pdf")
        # Shrinks font size to fit doubled text content in original space
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        fragment.replace_options.rectangle = fragment.rectangle
        fragment.replace_options.font_size_adjustment_action = (
            ap.text.TextReplaceOptions.FontSizeAdjustment.SHRINK_TO_FIT
        )
        fragment.replace_options.replace_adjustment_action = (
            ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH

        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### Remplacer automatiquement le texte de l’espace réservé et réorganiser la mise en page du PDF

Remplacez le texte d’espace réservé dans un PDF (par exemple, des modèles ou des formulaires) par des données réelles telles que des noms ou des informations d’entreprise.
Il ajuste automatiquement la mise en page pour accueillir le nouveau texte tout en appliquant un formatage personnalisé (police, couleur, taille).

1. Importer et charger le PDF.
1. Créer un absorbeur de texte pour l’espace réservé.
1. Appliquer l’absorbeur à toutes les pages.
1. Parcourir les fragments de texte trouvés.
1. Appliquer un formatage de texte personnalisé.
1. Enregistrer le document mis à jour.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def automatically_rearrange_page_contents(input_file, output_file):
    """
    Replace placeholder text in PDF with actual content.

    Demonstrates how to replace long placeholder text with actual content
    and automatically rearrange page layout. Shows dynamic content replacement
    with custom formatting applied to the new text.

    Args:
        input_file (str): Path to the input PDF file containing placeholders.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Searches for "[Long_placeholder_Long_placeholder]" placeholders
        - Replaces with either "John Smith" or extended version with studio info
        - Applies Calibri font, size 12, navy blue color
        - Automatically adjusts page layout to accommodate content changes
        - Demonstrates real-world template filling scenarios

    Example:
        >>> automatically_rearrange_page_contents("template.pdf", "filled.pdf")
        # Replaces placeholders with formatted actual content
    """
    document = ap.Document(input_file)

    absorber = ap.text.TextFragmentAbsorber("[Long_placeholder_Long_placeholder]")
    document.pages.accept(absorber)

    for text_fragment in absorber.text_fragments:
        # text_fragment.text = "John Smith"
        text_fragment.text = "John Smith, South Development Studio"
        text_fragment.text_state.font = ap.text.FontRepository.find_font("Calibri")
        text_fragment.text_state.font_size = 12
        text_fragment.text_state.foreground_color = ap.Color.navy

    # Save PDF document
    document.save(output_file)
```

### Remplacer le texte basé sur une expression régulière

Lorsque vous travaillez avec des documents PDF, il peut être nécessaire de remplacer du texte qui suit un motif plutôt qu’une phrase précise — par exemple, des numéros de téléphone, des codes ou des formats de type date.

Aspose.PDF pour Python via .NET vous permet d’effectuer ces remplacements en utilisant des expressions régulières (regex) avec la classe TextFragmentAbsorber.

Cet exemple montre comment trouver des motifs de texte (dans ce cas, tout texte correspondant au format ####-####, comme 1234-5678) et les remplacer par une chaîne formatée 'ABC1-2XZY'. Il montre également comment personnaliser la police, la couleur et la taille du texte remplacé.

Le fragment de code suivant vous montre comment remplacer du texte basé sur une expression régulière.

1. Charger le document PDF.
1. Créer un absorbeur de texte basé sur une expression régulière. Initialise le TextFragmentAbsorber avec un motif d’expression régulière.
1. Activer le mode d’expression régulière. Le paramètre 'True' active le mode de recherche d’expression régulière.
1. Appliquer l’absorbeur à une page. Cela analyse la page pour tous les fragments de texte correspondant au motif regex défini.
1. Remplacer chaque correspondance par du nouveau texte et appliquer un style personnalisé.
1. Enregistrer le document modifié.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_based_on_regex(infile, outfile):
    """
    Replace text based on a regular expression pattern.

    Demonstrates pattern-based text replacement using regular expressions
    to find and replace text that matches specific formats. Also shows
    how to apply formatting changes to the replaced text.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses regex pattern r"\\d{4}-\\d{4}" to find 4-digit-4-digit patterns
        - Replaces matched patterns with "ABC1-2XZY"
        - Applies custom formatting: Verdana font, size 12, blue text
        - Sets light green background color for replaced text
        - Enables regex mode with TextSearchOptions(True)

    Example:
        >>> replace_text_based_on_regex("input.pdf", "output.pdf")
        # Replaces patterns like "1234-5678" with formatted "ABC1-2XZY"
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(r"\d{4}-\d{4}")
        absorber.text_search_options = ap.text.TextSearchOptions(True)
        document.pages[1].accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = "ABC1-2XZY"
            fragment.text_state.font = ap.text.FontRepository.find_font("Verdana")
            fragment.text_state.font_size = 12
            fragment.text_state.foreground_color = ap.Color.blue
            fragment.text_state.background_color = ap.Color.light_green

        document.save(outfile)
```

## Remplacer les polices ou supprimer les polices inutilisées

### Remplacer les polices dans un fichier PDF existant

Il arrive que vous deviez standardiser ou mettre à jour les polices d’un PDF — par exemple, remplacer une police obsolète ou propriétaire par une police plus accessible. La bibliothèque Aspose.PDF pour Python via .NET vous permet de détecter et remplacer les polices de manière programmatique, garantissant une typographie cohérente et une compatibilité du document.

Cet exemple montre comment remplacer toutes les instances d’une police spécifique (p. ex., 'Arial-BoldMT') par une autre police (p. ex., 'Verdana') dans l’ensemble d’un document PDF.

L’extrait de code suivant montre comment remplacer la police dans un document PDF :

1. Ouvrir le document PDF.
1. Initialiser un TextFragmentAbsorber.
1. Utiliser l’Absorber pour extraire les fragments de texte de chaque page du document.
1. Identifier et remplacer les polices. Le script vérifie si la police actuelle d’un fragment est 'Arial-BoldMT'. Si c’est le cas, il la remplace par la police 'Verdana' en utilisant la méthode FontRepository.find_font().
1. Enregistrer le document modifié.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_fonts(infile, outfile):
    """
    Replace specific fonts in a PDF document.

    Demonstrates how to find and replace specific fonts throughout a PDF
    document. Searches for text using a particular font and changes it
    to a different font while preserving the text content.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Searches for text using "Arial-BoldMT" font
        - Replaces font with "Verdana" while keeping text content
        - Processes all text fragments across all pages
        - Maintains original text size and formatting properties
        - Useful for font standardization across documents

    Example:
        >>> replace_fonts("input.pdf", "output.pdf")
        # Changes all Arial-BoldMT text to use Verdana font instead
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        document.pages.accept(absorber)

        for fragment in absorber.text_fragments:
            if fragment.text_state.font.font_name == "Arial-BoldMT":
                fragment.text_state.font = ap.text.FontRepository.find_font("Verdana")

        document.save(outfile)
```

### Supprimer les polices inutilisées

Avec le temps, les documents PDF peuvent accumuler des polices inutilisées ou incorporées qui augmentent la taille du fichier et ralentissent le traitement. Ces polices inutilisées restent souvent présentes même après des modifications ou remplacements de texte, notamment lors de la manipulation de PDF volumineux ou complexes.

La bibliothèque Aspose.PDF pour Python via .NET offre un moyen efficace de supprimer ces polices redondantes à l’aide de la classe TextEditOptions. Cela optimise non seulement votre document, mais garantit également qu’il n’utilise que les polices réellement appliquées au texte visible.

La méthode 'remove_unused_fonts()' est une façon simple mais puissante d’optimiser les fichiers PDF en supprimant les données de police redondantes.

Cet exemple montre comment :

- Analyser un PDF à la recherche de polices inutilisées.
- Les supprimer en toute sécurité.
- Réassigner les fragments de texte actifs à une police cohérente (p. ex., Times New Roman).

1. Ouvrir le document PDF.
1. Configurer les options de modification de texte. Cela indique au moteur d’éliminer les polices incorporées qui ne sont pas utilisées dans le texte visible.
1. Créer un TextFragmentAbsorber avec des options. Un TextFragmentAbsorber extrait les fragments de texte du document pour les éditer.
1. Réassigner une police standard. Une fois que l’absorber a collecté tous les fragments, parcourez-les et appliquez une police cohérente.
1. Enregistrer le PDF nettoyé.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def remove_unused_fonts(input_file, output_file):
    """
    Remove unused fonts from a PDF document.

    Optimizes PDF file size by removing fonts that are embedded but not
    actually used in the document. Also demonstrates how to standardize
    all text to use a specific font family.

    Args:
        input_file (str): Path to the input PDF file to optimize.
        output_file (str): Path where the optimized PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses REMOVE_UNUSED_FONTS option for optimization
        - Changes all text to use TimesNewRoman font
        - Processes all text fragments across the document
        - Reduces file size by eliminating unnecessary font data
        - Useful for PDF optimization and standardization

    Example:
        >>> remove_unused_fonts("input.pdf", "optimized.pdf")
        # Removes unused fonts and standardizes text to TimesNewRoman
    """

    # Open PDF document
    document = ap.Document(input_file)

    # Initialize text edit options to remove unused fonts
    options = ap.text.TextEditOptions(ap.text.TextEditOptions.FontReplace.REMOVE_UNUSED_FONTS)

    # Create a TextFragmentAbsorber with the specified options
    absorber = ap.text.TextFragmentAbsorber(options)
    document.pages.accept(absorber)

    # Iterate through all TextFragments
    for text_fragment in absorber.text_fragments:
        text_fragment.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")

    # Save the updated PDF document
    document.save(output_file)
```

## Supprimer tout le texte

### Supprimer le texte d’un PDF

Supprimer tout le contenu texte d’un fichier PDF tout en conservant les images, les formes et la structure de la mise en page.
En utilisant TextFragmentAbsorber, le code parcourt efficacement l’ensemble du document et supprime chaque fragment de texte trouvé sur chaque page.

1. Charger le document PDF.
1. Un objet TextFragmentAbsorber est créé pour détecter et gérer les fragments de texte dans le PDF.
1. Supprimer tout le contenu texte. La méthode 'absorber.remove_all_text()' supprime chaque élément texte du document chargé, laissant les composants non textuels intacts.
1. Enregistrer le document mis à jour.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def remove_all_text_using_absorber1(infile, outfile):
    """
    Remove all text from a PDF using TextFragmentAbsorber.

    Demonstrates complete text removal from an entire PDF document,
    leaving only non-text elements like images, shapes, and layout
    structures intact.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the text-free PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Removes all text content from the entire document
        - Preserves images, graphics, and page structure
        - Uses document-level text removal for complete cleanup
        - Useful for creating templates or removing sensitive text
        - Maintains page layout and non-text elements

    Example:
        >>> remove_all_text_using_absorber1("input.pdf", "no_text.pdf")
        # Creates a PDF with all text removed but graphics preserved
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(document)
        document.save(outfile)
```

### Supprimer tout le texte d’une page spécifique

Supprimer tout le texte d’une seule page d’un document PDF à l’aide de la classe TextFragmentAbsorber d’Aspose.PDF.
Contrairement à la suppression à l’échelle du document, cette méthode réalise un nettoyage du texte au niveau de la page, supprimant le texte uniquement de la page choisie tout en laissant les autres pages intactes.

1. Charger le fichier PDF.
1. Créer une instance de TextFragmentAbsorber.
1. Supprimer tout le texte de la première page.
1. Enregistrer le PDF modifié.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def remove_all_text_using_absorber2(infile, outfile):
    """
    Remove all text from page using TextFragmentAbsorber.

    Demonstrates text removal from a specific page while leaving text
    on other pages intact. Useful for selective text cleanup or
    creating mixed-content documents.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Removes text only from the first page (pages[1])
        - Preserves text content on all other pages
        - Maintains page structure and non-text elements
        - Useful for page-specific text removal operations
        - Images and graphics on the target page remain intact

    Example:
        >>> remove_all_text_using_absorber2("input.pdf", "first_page_clean.pdf")
        # Removes all text from first page only
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(document.pages[1])
        document.save(outfile)
```

### Supprimer tout le texte d’une zone particulière sur la page d’un PDF

Supprimer tout le texte d’une région rectangulaire spécifique sur une page à l’aide du TextFragmentAbsorber d’Aspose.PDF.
Au lieu de nettoyer une page entière, cette méthode effectue une suppression ciblée du texte, permettant un contrôle précis de la partie de la page concernée.

1. Charger le document PDF.
1. Créer un TextFragmentAbsorber.
1. Définir la zone cible (rectangle).
1. Supprimer le texte de la région spécifiée.
1. Préserver le reste du document.
1. Enregistrer le PDF modifié.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def remove_all_text_using_absorber3(infile, outfile):
    """
    Remove all text from particular area on PDF page using TextFragmentAbsorber.

    Demonstrates precise text removal from a specific rectangular region
    on a page. Allows for surgical text removal while preserving text
    outside the target area.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Removes text only within rectangle (10, 200, 120, 600)
        - Targets the first page only (pages[1])
        - Preserves text outside the specified rectangle
        - Maintains all non-text elements in the region
        - Useful for removing watermarks, headers, or specific sections

    Example:
        >>> remove_all_text_using_absorber3("input.pdf", "region_clean.pdf")
        # Removes text only from the specified rectangular area
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(document.pages[1], ap.Rectangle(10, 200, 120, 600))
        document.save(outfile)
```

### Supprimer tout le texte caché d’un document PDF

Supprimer tout le texte d’une région rectangulaire spécifique sur une page à l’aide du TextFragmentAbsorber d’Aspose.PDF.
Au lieu de nettoyer une page entière, cette méthode effectue une suppression ciblée du texte, permettant un contrôle précis de la partie de la page concernée.

1. Charger le document PDF.
1. Créez un TextFragmentAbsorber.
1. Définissez la zone cible (Rectangle).
1. Supprimez le texte de la région spécifiée.
1. Conservez le reste du document.
1. Enregistrez le PDF modifié.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def remove_hidden_text(infile, outfile):
    """
    Remove all hidden (invisible) text from a PDF document.

    Identifies and removes text that has been marked as invisible while
    preserving all visible text content. Useful for cleaning documents
    that may contain hidden tracking text or metadata.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the cleaned PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Detects text fragments with invisible text state
        - Replaces hidden text with empty strings
        - Uses NONE replacement adjustment to prevent layout shifts
        - Preserves all visible text and document structure
        - Useful for privacy and security document cleanup

    Example:
        >>> remove_hidden_text("input.pdf", "no_hidden_text.pdf")
        # Removes all invisible text while keeping visible content intact
    """
    # Open PDF document
    with ap.Document(infile) as document:
        text_absorber = ap.text.TextFragmentAbsorber()
        # This option can be used to prevent other text fragments from moving after hidden text replacement
        text_absorber.text_replace_options = ap.text.TextReplaceOptions(ap.text.TextReplaceOptions.ReplaceAdjustment.NONE)
        document.pages.accept(text_absorber)
        # Remove hidden text
        for fragment in text_absorber.text_fragments:
            if fragment.text_state.invisible:
                fragment.text = ""
        # Save PDF document
        document.save(outfile)
```
