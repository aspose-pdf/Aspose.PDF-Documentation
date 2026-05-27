---
title: Rechercher et extraire le texte PDF en Python
linktitle: Rechercher et obtenir le texte
type: docs
weight: 60
url: /fr/python-net/search-and-get-text-from-pdf/
description: Apprenez à rechercher, inspecter et extraire du texte à partir de documents PDF en Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Recherchez du texte PDF et inspectez les fragments extraits en Python
Abstract: Cet article explique comment rechercher et extraire du texte à partir de documents PDF à l'aide d'Aspose.PDF for Python via .NET. Il couvre `TextAbsorber` et `TextFragmentAbsorber`, y compris l'extraction basée sur des régions, les recherches spécifiques à une page, la correspondance de phrases et l'inspection de la position du texte ainsi que des propriétés de police.
---

## Rechercher du texte dans le PDF

Rechercher et extraire le texte d'une zone rectangulaire définie dans un document PDF en utilisant le `TextAbsorber` classe. Il utilise le mode de formatage texte pur pour une sortie propre et non formatée, ce qui est utile pour extraire le contenu de régions structurées telles que les en-têtes, pieds de page ou zones de tableau. En combinant `TextExtractionOptions` et `TextSearchOptions` Avec des contraintes rectangulaires, vous pouvez contrôler où et comment le texte est extrait.

Utilisez cette page lorsque vous devez auditer le contenu texte du PDF, extraire le texte pour l'analyse ou inspecter les positions et le formatage des fragments de texte correspondants.

1. Chargez le fichier PDF en utilisant 'ap.Document'.
1. Configurer les options d'extraction de texte.
1. Définir la zone de recherche avec des contraintes de rectangle.
1. Créer et configurer TextAbsorber.
1. Traiter toutes les pages du document.
1. Récupérer et afficher le texte extrait.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_absorber_search(input_file_path):
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

## Rechercher du texte d'une page PDF spécifique

Rechercher et extraire du texte d'une page et d'une zone spécifiques dans un PDF en utilisant TextAbsorber d'Aspose.PDF. Il cible la page 2 du document et n'extrait que le texte trouvé à l'intérieur d'une zone rectangulaire définie.
En combinant TextExtractionOptions (pour le contrôle du formatage) et TextSearchOptions (pour la limitation de zone), vous pouvez effectuer une extraction de texte précise et spécifique à chaque page de manière efficace.

1. Charger le Document PDF.
1. Configurer les options d'extraction de texte.
1. Restreindre l'extraction de texte à une zone rectangulaire spécifique sur la page.
1. Créer et configurer TextAbsorber.
1. Traiter une page spécifique.
1. Récupérer et afficher le texte extrait.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_absorber_search_page(input_file_path):
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

## Analyser et extraire les propriétés détaillées des fragments de texte à partir d'un PDF

Contrairement à TextAbsorber, qui extrait le texte brut, TextFragmentAbsorber fournit des informations détaillées et de bas niveau sur chaque fragment de texte — telles que sa position, ses attributs de police, sa couleur et les détails d’intégration.

1. Charger le Document PDF.
1. Initialiser TextFragmentAbsorber.
1. Traiter toutes les pages du document.
1. Itérer à travers les fragments de texte extraits.
1. Imprimer les informations de texte de base.
1. Imprimer les détails de la police et de la mise en forme.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search(input_file_path):
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

## Rechercher une phrase texte spécifique sur une seule page PDF

Recherchez une phrase texte spécifique dans une page d'un document PDF en utilisant TextFragmentAbsorber. Contrairement à la recherche sur l'ensemble du document, cette approche limite la recherche à une seule page, ce qui la rend plus efficace pour confirmer la présence et l'emplacement du texte dans des zones ciblées comme les en-têtes, les pieds de page ou des sections de contenu spécifiques.

1. Charger le Document PDF.
1. Initialiser TextFragmentAbsorber avec la phrase de recherche.
1. Appliquer Absorber à une page spécifique.
1. Itérer sur les fragments trouvés.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_page(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber("whale")
    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## Recherche séquentielle de texte page par page avec résultats cumulatifs

Recherchez du texte de façon incrémentielle sur plusieurs pages d'un document PDF à l'aide de TextFragmentAbsorber d'Aspose.PDF.
Contrairement à une recherche à page unique ou sur l'ensemble du document, cette approche vous permet de traiter les pages séquentiellement, de collecter les résultats de manière progressive et d'analyser les fragments de texte avec un contexte spécifique à chaque page. Cette méthode est idéale pour les documents volumineux ou les flux de travail de traitement progressif.

1. Charger le Document PDF.
1. Initialiser TextFragmentAbsorber et définir la phrase de recherche.
1. Traiter la première page. Rechercher uniquement la page 1. Imprimer le texte, le numéro de page et la position. Fournir des résultats isolés spécifiques à la page pour plus de clarté.
1. Traiter la page suivante séquentiellement. Passer à la page 2 et éventuellement continuer à travers le reste du document. La fonction 'absorber.visit()' assure l'accumulation des résultats de toutes les pages visitées. Imprime les résultats de recherche cumulatifs, montrant à la fois le texte et la localisation.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_sequential_search(input_file_path):
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

## Recherche ciblée de phrase dans une zone rectangulaire

Rechercher une phrase spécifique dans un PDF tout en limitant la recherche à une zone rectangulaire précise sur une seule page.
En combinant la recherche de phrases avec des contraintes spatiales, vous pouvez localiser le contenu avec précision dans des régions désignées sans scanner l'intégralité de la page ou du document. Cela est particulièrement utile pour les formulaires, en-têtes, pieds de page ou rapports structurés où le contenu apparaît à des emplacements prévisibles.

1. Charger le Document PDF.
1. Initialiser TextFragmentAbsorber avec Phrase et contraintes rectangulaires
1. Appliquer l'Absorber à la page 2. Restreint le traitement à la page 2, réduisant les calculs inutiles. Assure que la recherche est spécifique à la page.
1. Parcourir les fragments trouvés et les imprimer

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_phrase(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber(
        "elephant", ap.text.TextSearchOptions(ap.Rectangle(0, 0, 842, 250, True))
    )

    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## Recherche de motifs de texte dans le PDF à l'aide d'expressions régulières

Recherchez des motifs de texte dans un PDF à l'aide d'expressions régulières. En activant le mode regex dans TextFragmentAbsorber, vous pouvez localiser des motifs complexes tels que des nombres, des dates, des prix, des coordonnées ou des formats de texte personnalisés. La fonction limite la recherche à une page spécifique, ce qui la rend efficace pour l'extraction ciblée de données structurées.

1. Charger le Document PDF.
1. Initialiser TextFragmentAbsorber avec un motif Regex.
1. Appliquer l'Absorber à la Page 2. Limite la recherche à la page 2 pour plus d'efficacité et de précision. Seul le texte de cette page est analysé.
1. Itérer à travers les fragments trouvés. Imprime les fragments de texte correspondants et leurs coordonnées. Fournit des informations de localisation précises pour les motifs extraits.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_regex(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber(
        r"\d+\.\d+", ap.text.TextSearchOptions(is_regular_expression_used=True)
    )

    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## Convertir les correspondances de texte en hyperliens dans un PDF en utilisant TextFragmentAbsorber

Recherchez des expressions textuelles spécifiques dans un PDF et convertissez‑les en hyperliens cliquables. En utilisant TextFragmentAbsorber avec des modèles regex, il localise les mots cibles et applique un style visuel (couleur et soulignement) ainsi que des liens interactifs.

1. Charger le Document PDF.
1. Initialiser TextFragmentAbsorber avec un motif Regex.
1. Appliquer Absorber à la page 1.
1. Styliser et ajouter des hyperliens aux correspondances.
1. Enregistrer le PDF modifié.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_and_add_hyperlink(input_file_path):
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

## Rechercher et identifier le texte stylisé dans le PDF à l'aide de TextFragmentAbsorber

Recherchez des fragments de texte dans un PDF en fonction de leurs propriétés de formatage plutôt qu'en fonction de leur contenu. En utilisant TextFragmentAbsorber, il identifie le texte avec des styles spécifiques, comme le texte en gras.

1. Charger le Document PDF.
1. Initialiser TextFragmentAbsorber.
1. Appliquer Absorber à la page 1.
1. Inspecter les fragments de texte en fonction du formatage. Vérifie le style de police pour le format gras.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_styled_text(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    absorber.text_search_options = ap.text.TextSearchOptions(True)

    absorber.visit(document.pages[1])

    for fragment in absorber.text_fragments:
        if fragment.text_state.font_style == ap.text.FontStyles.BOLD:
            print(f"Bold: {fragment.text}")
        if fragment.text_state.invisible:
            print(f"Invisible: {fragment.text}")
```

## Mise en surbrillance visuelle du texte dans les pages PDF

Cette fonction combine la reconnaissance de texte et le rendu en un seul flux de travail. Elle ne se contente pas d'extraire le texte, mais le visualise également en mettant en évidence les fragments, les segments et les caractères avec des rectangles colorés sur les images PNG de chaque page.

Notre exemple effectue une visualisation avancée du texte sur un PDF en :

- recherche de tous les fragments de texte visibles en utilisant des expressions régulières
- rendu de chaque page PDF en image PNG haute résolution
- dessiner des rectangles colorés autour des fragments de texte, des segments de texte et des caractères individuels

1. Définir la résolution de l'image de sortie. Chaque page PDF est convertie en une image PNG à 150 DPI.
1. Ouvrez le PDF et initialisez Text Absorber.
1. Traiter chaque page. Appliquer l'absorbeur à chaque page. Collecter tous les fragments de texte détectés et leurs positions géométriques.
1. Convertir la page en flux PNG.
1. Préparer l'objet graphique pour le dessin.
1. Appliquer la transformation de coordonnées. Convertir les coordonnées PDF en pixels d'image.
1. Dessiner des rectangles pour les éléments de texte.
1. Enregistrez le résultat.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_and_highlight(infile):
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

## Sujets de texte associés

- [Travailler avec du texte dans le PDF en utilisant Python](/pdf/fr/python-net/working-with-text/)
- [Remplacer le texte dans le PDF via Python](/pdf/fr/python-net/replace-text-in-pdf/)
- [Ajouter des infobulles au texte du PDF en Python](/pdf/fr/python-net/pdf-tooltip/)
- [Ajout de texte au PDF](/pdf/fr/python-net/add-text-to-pdf-file/)