---
title: Faire pivoter le texte PDF en Python
linktitle: Faire pivoter le texte à l'intérieur du PDF
type: docs
weight: 50
url: /fr/python-net/rotate-text-inside-pdf/
description: Apprenez comment faire pivoter les fragments de texte et les paragraphes à l'intérieur des documents PDF en Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Faire pivoter les fragments de texte et les paragraphes dans les documents PDF avec Python
Abstract: Cet article explique comment faire pivoter du texte dans des documents PDF en utilisant Aspose.PDF for Python via .NET. Il montre comment définir la propriété `rotation` sur `TextFragment`, créer du contenu pivoté avec `TextBuilder` et `TextParagraph`, et ajouter du texte pivoté directement aux paragraphes de la page pour différents scénarios de mise en page.
---

Faire pivoter les fragments de texte dans un document PDF à l'aide d'Aspose.PDF for Python via .NET. Cette page montre comment contrôler la position et la rotation du texte en utilisant `TextFragment`, `TextState`, et `TextBuilder`. En ajustant les angles de rotation, vous pouvez créer des mises en page telles que des en-têtes diagonaux, des étiquettes verticales et des annotations rotatives.

## Faire pivoter des fragments de texte à l’aide de TextBuilder dans un PDF

Crée un fichier PDF nommé `rotated_fragments.pdf` contenant trois fragments de texte alignés horizontalement :

- Le premier texte n'est pas tourné
- Le deuxième est tourné de 45°
- Le troisième est tourné de 90°

1. Créer un nouveau document PDF.
1. Insérez une nouvelle page pour accueillir le texte tourné.
1. Créez le premier fragment de texte (sans rotation).
1. Créez le deuxième fragment de texte (rotation de 45°).
1. Créez le troisième fragment de texte (rotation de 90°).
1. Ajouter des fragments de texte en utilisant `TextBuilder`.
1. Enregistrez le document.

```python
import aspose.pdf as ap

def rotate_text_inside_pdf_1(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("main text")
        text_fragment_1.position = ap.text.Position(100, 600)
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Create rotated text fragment
        text_fragment_2 = ap.text.TextFragment("rotated text")
        text_fragment_2.position = ap.text.Position(200, 600)
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        text_fragment_2.text_state.rotation = 45
        # Create rotated text fragment
        text_fragment_3 = ap.text.TextFragment("rotated text")
        text_fragment_3.position = ap.text.Position(300, 600)
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
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

## Faire pivoter des TextFragment individuels à l'intérieur d'un paragraphe dans le PDF

Faire pivoter des fragments de texte individuels au sein d'un paragraphe. Cela montre comment créer un paragraphe multi‑lignes (TextParagraph) contenant plusieurs fragments (TextFragment), chacun avec son propre angle de rotation. Cette technique est utile pour créer des documents visuellement riches qui combinent du texte orienté horizontalement et en diagonale — par exemple, des en‑têtes stylisées, des diagrammes ou des libellés annotés.

Crée un PDF nommé `rotated_paragraph_fragments.pdf` contenant un paragraphe avec trois lignes de texte, chaque ligne étant pivotée différemment :

- la première ligne est pivotée à 45°
- la deuxième ligne reste horizontale (0°)
- la troisième ligne est tournée de -45°

1. Créer un nouveau document PDF.
1. Ajoutez une page blanche où le texte tourné apparaîtra.
1. Créer un `TextParagraph`.
1. Créez et configurez le premier fragment de texte (rotation de +45°).
1. Créez le deuxième fragment de texte (sans rotation).
1. Créez le troisième fragment de texte (-45° rotation).
1. Ajoutez les fragments de texte au paragraphe.
1. Ajouter le paragraphe à la page en utilisant `TextBuilder`.
1. Enregistrez le document.

```python
import aspose.pdf as ap

def rotate_text_inside_pdf_2(outfile):
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
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Set rotation
        text_fragment_1.text_state.rotation = 45
        # Create text fragment
        text_fragment_2 = ap.text.TextFragment("main text")
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Create text fragment
        text_fragment_3 = ap.text.TextFragment("another rotated text")
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
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

## Faire pivoter le texte à l'aide des paragraphes de page dans le PDF

Cette section présente une méthode simplifiée pour faire pivoter du texte dans un PDF à l'aide d'Aspose.PDF for Python via .NET.
Contrairement aux approches de bas niveau avec `TextBuilder` ou `TextParagraph`, cette méthode ajoute des fragments de texte tournés directement à la collection de paragraphes de la page (`page.paragraphs`). Il est idéal lorsque vous avez besoin d'une rotation de texte basique mais que vous ne nécessitez pas de positionnement précis ou de structuration de paragraphe.

Génère un fichier nommé `simple_rotated_text.pdf` contenant :

- un fragment de texte principal horizontal avec une rotation de 0°
- fragment tourné de 315°
- fragment tourné à 270°

1. Initialisez un nouveau document PDF.
1. Créez une page où le texte pivoté sera placé.
1. Créez le premier fragment de texte (sans rotation).
1. Créez le deuxième fragment de texte (rotation de 315°).
1. Créer le troisième fragment de texte (rotation de 270°).
1. Ajoutez des fragments de texte directement aux paragraphes de la page.
1. Enregistrez le document PDF.

```python
import aspose.pdf as ap

def rotate_text_inside_pdf_3(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("main text")
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Create text fragment
        text_fragment_2 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Set rotation
        text_fragment_2.text_state.rotation = 315
        # Create text fragment
        text_fragment_3 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Set rotation
        text_fragment_3.text_state.rotation = 270
        page.paragraphs.add(text_fragment_1)
        page.paragraphs.add(text_fragment_2)
        page.paragraphs.add(text_fragment_3)

        # Save the document
        document.save(outfile)
```

## Faire pivoter les paragraphes entiers dans un PDF

Cet exemple démontre la rotation avancée du texte au niveau du paragraphe dans un PDF. Contrairement à la rotation au niveau du fragment (où chaque morceau de texte est pivoté individuellement), cette méthode fait pivoter des paragraphes entiers comme des blocs unifiés sous différents angles.
Chaque paragraphe contient plusieurs fragments de texte stylisés, et le paragraphe complet est tourné à des angles spécifiques — permettant des transformations de mise en page complexes et cohérentes.
Ceci est idéal pour les mises en page artistiques, les filigranes ou les PDF fortement axés sur le design où des sections entières de texte doivent être orientées dans différentes directions.

Crée `rotated_paragraphs.pdf`, contenant quatre paragraphes entièrement stylisés et pivotés :

- chacun tourné à un angle unique (45°, 135°, 225° et 315°)
- chaque paragraphe comporte trois lignes de texte avec des arrière-plans colorés, du soulignement et une mise en forme cohérente

1. Créer un nouveau document PDF.
1. Ajoutez une page vierge pour contenir les paragraphes tournés.
1. Itérer pour créer plusieurs paragraphes.
1. Créer et positionner le paragraphe.
1. Créer des fragments de texte avec mise en forme.
1. Appliquer le formatage du texte.
1. Ajouter des fragments de texte au paragraphe.
1. Ajoutez le paragraphe à la page en utilisant `TextBuilder`.
1. Répétez pour les quatre rotations.
1. Enregistrez le document PDF.

```python
import aspose.pdf as ap

def rotate_text_inside_pdf_4(outfile):
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
            text_fragment_1.text_state.font = ap.text.FontRepository.find_font(
                "TimesNewRoman"
            )
            text_fragment_1.text_state.background_color = ap.Color.light_gray
            text_fragment_1.text_state.foreground_color = ap.Color.blue
            # Create text fragment
            text_fragment_2 = ap.text.TextFragment("Second line of text")
            # Set text properties
            text_fragment_2.text_state.font_size = 12
            text_fragment_2.text_state.font = ap.text.FontRepository.find_font(
                "TimesNewRoman"
            )
            text_fragment_2.text_state.background_color = ap.Color.light_gray
            text_fragment_2.text_state.foreground_color = ap.Color.blue
            # Create text fragment
            text_fragment_3 = ap.text.TextFragment("And some more text...")
            # Set text properties
            text_fragment_3.text_state.font_size = 12
            text_fragment_3.text_state.font = ap.text.FontRepository.find_font(
                "TimesNewRoman"
            )
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

## Sujets de texte liés

- [Travailler avec du texte dans le PDF en utilisant Python](/pdf/fr/python-net/working-with-text/)
- [Ajout de texte au PDF](/pdf/fr/python-net/add-text-to-pdf-file/)
- [Formater le texte PDF en Python](/pdf/fr/python-net/text-formatting-inside-pdf/)
- [Remplacer le texte dans le PDF avec Python](/pdf/fr/python-net/replace-text-in-pdf/)