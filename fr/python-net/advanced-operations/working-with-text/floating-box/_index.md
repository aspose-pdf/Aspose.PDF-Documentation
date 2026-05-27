---
title: Utilisez FloatingBox pour la mise en page PDF en Python
linktitle: Utilisation de FloatingBox
type: docs
weight: 30
url: /fr/python-net/floating-box/
description: Apprenez à utiliser FloatingBox pour la mise en page du texte, le contenu multi-colonnes et le positionnement précis dans les documents PDF avec Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Créez et positionnez des conteneurs FloatingBox stylisés dans un PDF avec Python.
Abstract: Cet article explique comment utiliser FloatingBox dans Aspose.PDF for Python via .NET. Apprenez comment placer du texte et d'autres contenus dans des conteneurs flottants stylisés, contrôler la mise en page, les bordures, l'alignement et le rognage, et créer des conceptions de pages PDF plus structurées en Python.
---

## Utilisation de base de FloatingBox

Le [`FloatingBox`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/) Une classe est un conteneur pour placer du texte et d'autres contenus sur une page PDF. Elle vous offre un contrôle plus fin sur la mise en page, les bordures et le style par rapport aux paragraphes de texte ordinaires. Si le contenu dépasse la taille de la boîte, le comportement de découpage est contrôlé par les paramètres de la boîte.

Utilisez cette page lorsque vous avez besoin de conteneurs de texte structurés, de mises en page à plusieurs colonnes et d’un positionnement précis dans les documents PDF avec Aspose.PDF for Python via .NET.

1. Créer un nouveau [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Ajouter un [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) au document.
1. Créer un [`FloatingBox`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/).
1. Définir la bordure de la boîte en utilisant [`BorderInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderinfo/) et [`BorderSide`](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderside/).
1. Répétition de la boîte de contrôle avec le [`is_need_repeating`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) propriété.
1. Ajouter du contenu texte en utilisant [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/).
1. Ajouter le `FloatingBox` au [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Enregistrez le document PDF final en utilisant [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python
import aspose.pdf as ap

def create_and_add_floating_box(outfile):
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

Dans l'exemple ci-dessus, le `FloatingBox` est créé avec une largeur de 400 pt et une hauteur de 30 pt.
Le texte dépasse intentionnellement la hauteur disponible, de sorte qu'une partie est rognée.

![Image 1](image01.png)

Le [`is_need_repeating`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) propriété avec une valeur de `False` limite le rendu du texte à une seule page.

Si vous définissez cette propriété sur `True`, le texte se reformate sur les pages suivantes à la même position.

![Image 2](image02.png)

## Fonctionnalités avancées de FloatingBox

### Prise en charge multicolonnes

#### Mise en page à plusieurs colonnes (cas simple)

`FloatingBox` prend en charge la mise en page à plusieurs colonnes. Pour créer une telle mise en page, vous devez définir les valeurs de [`ColumnInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/columninfo/) propriétés.

* `column_widths` est une chaîne qui définit la largeur de chaque colonne en points.
* `column_spacing` est une chaîne qui définit la largeur de l'écart entre les colonnes.
* `column_count` est le nombre de colonnes.

```python
import sys
import aspose.pdf as ap
from os import path

def multi_column_layout(outfile):
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

L'exemple génère des paragraphes d'exemple et les place dans trois colonnes. Le contenu se poursuit sur des pages supplémentaires jusqu'à ce que tous les paragraphes soient rendus.

#### Mise en page à colonnes multiples avec démarrage de colonne forcé

Cet exemple utilise la même configuration multicolonnes, mais force chaque paragraphe ajouté à commencer dans une nouvelle colonne. Pour ce faire, définissez `is_first_paragraph_in_column = True` sur chaque `TextFragment` avant de l'ajouter à `FloatingBox`.

```python
import sys
import aspose.pdf as ap
from os import path

def multi_column_layout_2(outfile):
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

### Support en arrière-plan

Appliquer une couleur d'arrière-plan à un `FloatingBox` dans un document PDF en utilisant Aspose.PDF for Python via .NET.
En attribuant un [`Color`](https://reference.aspose.com/pdf/python-net/aspose.pdf/color/) à `background_color`, vous pouvez mettre en évidence le contenu pour les en-têtes, les encadrés ou les sections stylisées.

Cet extrait de code montre comment créer une zone de texte vert clair avec un contenu d'exemple.

```python
import sys
import aspose.pdf as ap
from os import path

def background_support(outfile):
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

### Prise en charge du positionnement

La position de `FloatingBox` sur la page est contrôlé par `positioning_mode`, `left`, et `top`.
Quand `positioning_mode` est:

* [`ParagraphPositioningMode.DEFAULT`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paragraphpositioningmode/) (par défaut)

L'emplacement dépend des éléments ajoutés précédemment. L'ajout d'un nouveau paragraphe affecte le flux des éléments suivants. Si [`left`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) ou [`top`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) sont non nuls, ils sont également appliqués.

* [`ParagraphPositioningMode.ABSOLUTE`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paragraphpositioningmode/)

L'emplacement est fixé par `left` et `top`; il ne dépend pas des éléments antérieurs et n'affecte pas le déroulement des suivants.

```python
import sys
import aspose.pdf as ap
from os import path

def offset_support(outfile):
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

Aligner `FloatingBox` éléments sur une page PDF en utilisant [`VerticalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/verticalalignment/) et [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) en Aspose.PDF for Python via .NET. Cela vous aide à placer des conteneurs flottants en haut, au centre ou en bas pour les dispositions de page, les blocs d'en-tête/pied de page ou les notes latérales.

1. Créer un nouveau document PDF.
1. Ajoutez une page au document.
1. Ajouter le premier `FloatingBox` avec un alignement en bas à droite.
1. Ajouter le second `FloatingBox` avec un alignement centré à droite.
1. Ajouter le troisième `FloatingBox` avec un alignement en haut à droite.
1. Enregistrez le document.

```python
import sys
import aspose.pdf as ap
from os import path

def align_text_to_float(outfile):
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

## Sujets de texte associés

* [Travailler avec le texte dans le PDF en utilisant Python](/pdf/fr/python-net/working-with-text/)
* [Ajout de texte au PDF](/pdf/fr/python-net/add-text-to-pdf-file/)
* [Formater le texte PDF en Python](/pdf/fr/python-net/text-formatting-inside-pdf/)
* [Ajouter des info-bulles au texte PDF en Python](/pdf/fr/python-net/pdf-tooltip/)
