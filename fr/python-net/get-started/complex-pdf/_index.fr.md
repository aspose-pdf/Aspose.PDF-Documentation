---
title: Création d'un PDF complexe
linktitle: Création d'un PDF complexe
type: docs
weight: 30
url: /python-net/complex-pdf-example/
description: Aspose.PDF pour Python via .NET vous permet de créer des documents plus complexes contenant des images, des fragments de texte et des tableaux dans un seul document.
lastmod: "2022-12-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

L'exemple [Bonjour, le Monde](/pdf/python-net/hello-world-example/) a montré des étapes simples pour créer un document PDF en utilisant Python et Aspose.PDF. Dans cet article, nous allons examiner la création d'un document plus complexe avec Aspose.PDF pour Python. Comme exemple, nous prendrons un document d'une entreprise fictive qui exploite des services de ferry pour passagers. Notre document contiendra une image, deux fragments de texte (en-tête et paragraphe), et un tableau.

Si nous créons un document à partir de zéro, nous devons suivre certaines étapes :

1. Instancier un objet [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). Dans cette étape, nous allons créer un document PDF vide avec des métadonnées mais sans pages.
1. Ajouter une [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) à l'objet document. Ainsi, notre document aura maintenant une page.
1. Ajouter une [Image](https://reference.aspose.com/pdf/python-net/aspose.pdf/image/) à la Page.
1. Créer un [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) pour l'en-tête. Pour l'en-tête, nous utiliserons la police Arial avec une taille de police de 24pt et un alignement centré.
1. Ajouter l'en-tête aux [paragraphes](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) de la page.
1. Créer un [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) pour la description. Pour la description, nous utiliserons la police Arial avec une taille de police de 24pt et un alignement centré.
1. Ajouter la (description) aux Paragraphes de la page.
1. Créer un tableau, ajouter des propriétés au tableau.

1. Ajouter (table) à la page [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties).
1. Enregistrer un document "Complex.pdf".

```python

    import aspose.pdf as ap

    # Initialiser l'objet document
    document = ap.Document()
    # Ajouter une page
    page = document.pages.add()

    # Ajouter une image
    page.add_image(image_file, ap.Rectangle(20, 730, 120, 830, True))

    # Ajouter un en-tête
    header = ap.text.TextFragment("Nouvelles routes de ferry à l'automne 2020")
    header.text_state.font = ap.text.FontRepository.find_font("Arial")
    header.text_state.font_size = 24
    header.horizontal_alignment = ap.HorizontalAlignment.CENTER
    header.position = ap.text.Position(130, 720)
    page.paragraphs.add(header)

    # Ajouter une description
    descriptionText = "Les visiteurs doivent acheter des billets en ligne et les billets sont limités à 5 000 par jour. \
    Le service de ferry fonctionne à moitié capacité et sur un horaire réduit. Attendez-vous à des files d'attente."
    description = ap.text.TextFragment(descriptionText)
    description.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    description.text_state.font_size = 14
    description.horizontal_alignment = ap.HorizontalAlignment.LEFT
    page.paragraphs.add(description)

    # Ajouter un tableau
    table = ap.Table()

    table.column_widths = "200"
    table.border = ap.BorderInfo(ap.BorderSide.BOX, 1.0, ap.Color.dark_slate_gray)
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.BOX, 0.5, ap.Color.black)
    table.default_cell_padding = ap.MarginInfo(4.5, 4.5, 4.5, 4.5)
    table.margin.bottom = 10
    table.default_cell_text_state.font = ap.text.FontRepository.find_font("Helvetica")

    headerRow = table.rows.add()
    headerRow.cells.add("Départs Ville")
    headerRow.cells.add("Départs Île")

    i = 0
    while i < headerRow.cells.count:
        headerRow.cells[i].background_color = ap.Color.gray
        headerRow.cells[i].default_cell_text_state.foreground_color = ap.Color.white_smoke
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

    document.save(output_pdf)
```