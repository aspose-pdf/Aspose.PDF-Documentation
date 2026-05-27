---
title: Création d'un PDF complexe
linktitle: Création d'un PDF complexe
type: docs
weight: 30
url: /fr/python-net/complex-pdf-example/
description: Aspose.PDF for Python via .NET vous permet de créer des documents plus complexes contenant des images, des fragments de texte et des tableaux dans un seul document.
lastmod: "2026-05-25"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Créer un PDF complexe avec Python
Abstract: Cet article approfondit le processus de création de PDF de base présenté dans l'exemple "Hello, World" en illustrant comment créer un document PDF plus complexe en utilisant Python et Aspose.PDF. Le document d'exemple est développé pour une société fictive de services de ferries de passagers et comprend une image, deux fragments de texte (un en-tête et un paragraphe), ainsi qu'un tableau. Le processus implique plusieurs étapes – l'instanciation d'un objet `Document` pour créer un PDF vide, l'ajout d'une `Page`, puis l'insertion d'une `Image` dans la page. Un `TextFragment` est créé pour l'en-tête en utilisant la police Arial avec une taille de 24 pt et un alignement centré, qui est ensuite ajouté aux paragraphes de la page. Un second `TextFragment` est ajouté pour la description, utilisant la police Times New Roman à une taille de 14 pt avec un alignement à gauche. Ensuite, un tableau est créé et formaté avec des largeurs de colonne spécifiques, des bordures et des marges. Le tableau comprend une ligne d'en-tête avec des cellules surlignées et plusieurs lignes de données générées par itération
---

Le [Hello World](/pdf/fr/python-net/hello-world-example/) exemple a montré des étapes simples pour créer un document PDF en utilisant Python et Aspose.PDF. Dans cet article, nous examinerons la création d'un document plus complexe avec Aspose.PDF for Python. À titre d'exemple, nous prendrons un document d'une entreprise fictive qui exploite des services de ferries de passagers. Notre document contiendra une image, deux fragments de texte (en-tête et paragraphe) et un tableau.

Si nous créons un document à partir de zéro, nous devons suivre certaines étapes :

1. Instancier un [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objet. Dans cette étape, nous créerons un document PDF vide avec quelques métadonnées mais sans pages.
1. Ajouter un [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) à l'objet document. Ainsi, maintenant notre document aura une page.
1. Ajouter un [Image](https://reference.aspose.com/pdf/python-net/aspose.pdf/image/) à la Page.
1. Créer un [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) pour l'en-tête. Pour l'en-tête, nous utiliserons la police Arial avec une taille de 24 pt et un alignement centré.
1. Ajouter l'en-tête à la page [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties).
1. Créer un [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) pour la description. Pour la description, nous utiliserons la police Arial avec une taille de 24 pt et un alignement centré.
1. Ajouter la description à la page [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties).
1. Créer et styliser le tableau. Définir la largeur des colonnes, les bordures, le remplissage et la police.
1. Ajouter un tableau à la page [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties).
1. Enregistrer un document "Complex.pdf".

```python
from datetime import timedelta
import aspose.pdf as ap


def run_complex(self):

    # Initialize document object
    document = ap.Document()
    # Add page
    page = document.pages.add()

    # Add image
    imageFileName = self.data_dir + "logo.png"
    page.add_image(imageFileName, ap.Rectangle(20, 730, 120, 830, True))

    # Add Header
    header = ap.text.TextFragment("New ferry routes in Fall 2029")
    header.text_state.font = ap.text.FontRepository.find_font("Arial")
    header.text_state.font_size = 24
    header.horizontal_alignment = ap.HorizontalAlignment.CENTER
    header.position = ap.text.Position(130, 720)
    page.paragraphs.add(header)

    # Add description
    descriptionText = "Visitors must buy tickets online and tickets are limited to 5,000 per day. \
    Ferry service is operating at half capacity and on a reduced schedule. Expect lineups."
    description = ap.text.TextFragment(descriptionText)
    description.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    description.text_state.font_size = 14
    description.horizontal_alignment = ap.HorizontalAlignment.LEFT
    page.paragraphs.add(description)

    # Add table
    table = ap.Table()

    table.column_widths = "200"
    table.border = ap.BorderInfo(ap.BorderSide.BOX, 1.0, ap.Color.dark_slate_gray)
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.BOX, 0.5, ap.Color.black)
    table.default_cell_padding = ap.MarginInfo(4.5, 4.5, 4.5, 4.5)
    table.margin.bottom = 10
    table.default_cell_text_state.font = ap.text.FontRepository.find_font("Helvetica")

    headerRow = table.rows.add()
    headerRow.cells.add("Departs City")
    headerRow.cells.add("Departs Island")

    i = 0
    while i < headerRow.cells.count:
        headerRow.cells[i].background_color = ap.Color.gray
        headerRow.cells[
            i
        ].default_cell_text_state.foreground_color = ap.Color.white_smoke
        i += 1

    time = timedelta(hours=6, minutes=0)
    incTime = timedelta(hours=0, minutes=30)

    i = 0
    while i < 10:
        dataRow = table.rows.add()
        dataRow.cells.add(str(time))
        time = time.__add__(incTime)
        dataRow.cells.add(str(time))
        i += 1

    page.paragraphs.add(table)

    document.save(self.data_dir + "Complex.pdf")
```
