---
title: Quoi de neuf
linktitle: Quoi de neuf
type: docs
weight: 10
url: /fr/python-net/whatsnew/
description: Cette page présente les nouvelles fonctionnalités les plus populaires dans Aspose.PDF pour Python via .NET qui ont été introduites dans les versions récentes.
sitemap:
    changefreq: "monthly"
    priority: 0.8
lastmod: "2021-12-24"
---

## Quoi de neuf dans Aspose.PDF 23.12

À partir d'Aspose.PDF 23.12, la prise en charge des nouvelles fonctionnalités de conversion a été ajoutée :

- Implémenter la conversion de PDF en Markdown

```python

    import aspose.pdf as ap

    input_pdf_path = DIR_INPUT + "input.pdf"
    markdown_output_file_path = DIR_OUTPUT + "output_md_file.md"

    doc = ap.Document(input_pdf_path)
    save_options = ap.pdftomarkdown.MarkdownSaveOptions()
    save_options.resources_directory_name = "images"
    doc.save(markdown_output_file_path, save_options)
```

- Implémenter la conversion de OFD en PDF

```python

    import aspose.pdf as ap

    input_path = DIR_INPUT + "input.ofd"
    output_path = DIR_OUTPUT + "output.pdf"
    document = ap.Document(input_path, ap.OfdLoadOptions())
    document.save(output_path)
```


Le support pour Python 3.6 a été interrompu.

## Quoi de neuf dans Aspose.PDF 23.11

Depuis la version 23.11, il est possible de supprimer le texte caché. Le code suivant peut être utilisé :

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    text_absorber = ap.text.TextFragmentAbsorber()
    # Cette option peut être utilisée pour empêcher d'autres fragments de texte de se déplacer après le remplacement du texte caché.
    text_absorber.text_replace_options = ap.text.TextReplaceOptions(ap.text.TextReplaceOptions.ReplaceAdjustment.NONE)
    document.pages.accept(text_absorber)

    for fragment in text_absorber.text_fragments:
        if fragment.text_state.invisible:
            fragment.text = ''

    document.save(output_file)
```    

## Quoi de neuf dans Aspose.PDF 23.8

Depuis la version 23.8, le support pour ajouter la détection des mises à jour incrémentielles a été ajouté.

La fonction pour détecter les mises à jour incrémentielles dans un document PDF a été ajoutée.
 Cette fonction renvoie 'true' si un document a été enregistré avec des mises à jour incrémentielles; sinon, elle renvoie 'false'.

```python

    import aspose.pdf as ap

    doc = ap.Document(file_path)
    updated = doc.has_incremental_update()
    print(updated)
```

De plus, 23.8 prend en charge les moyens de travailler avec des champs de case à cocher imbriqués. De nombreux formulaires PDF remplissables ont des champs de case à cocher qui agissent comme des groupes radio:

- Créer un champ de case à cocher à valeurs multiples :

```python

    import aspose.pdf as ap

    document = ap.Document()
    page = document.pages.add()
    checkbox = ap.forms.CheckboxField(page, ap.Rectangle(50, 50, 70, 70, True))
    # Définir la valeur de l'option du premier groupe de cases à cocher
    checkbox.export_value = "option 1"
    # Ajouter une nouvelle option juste en dessous des options existantes
    checkbox.add_option("option 2")
    # Ajouter une nouvelle option au rectangle donné
    checkbox.add_option("option 3", ap.Rectangle(100, 100, 120, 120, True))
    document.form.add(checkbox)
    # Sélectionner la case à cocher ajoutée
    checkbox.value = "option 2"
    document.save(DIR_OUTPUT + "checkbox_group.pdf")
```

- Obtenir et définir la valeur d'une case à cocher à valeurs multiples :

```python

    import aspose.pdf as ap

    doc = ap.Document("example.pdf")
    form = doc.form
    checkbox = cast(ap.forms.CheckboxField, form.fields[0])

    # Les valeurs autorisées peuvent être récupérées à partir de la collection AllowedStates
    # Définir la valeur de la case à cocher en utilisant la propriété Value
    checkbox.value = checkbox.allowed_states[0]
    checkbox_value = checkbox.value  # la valeur précédemment définie, par exemple "option 1"
    # La valeur doit être un élément de AllowedStates
    checkbox.value = "option 2"
    checkbox_value = checkbox.value  # option 2
    # Décochez les cases en définissant soit Value à "Off", soit Checked à false
    checkbox.value = "Off"
    # ou, alternativement :
    # checkbox.checked = False
    checkbox_value = checkbox.value  # Off
```

- Mettre à jour l'état de la case à cocher lors d'un clic utilisateur :

```python

    import aspose.pdf as ap
    from aspose.pycore import cast

    input_file = DIR_INPUT + "input.pdf"
    document = ap.Document(input_file)
    point = ap.Point(62,462)  # par exemple, les coordonnées d'un clic de souris
    # Option 1 : parcourir les annotations sur la page
    page = document.pages[5]
    for annotation in page.annotations:
        if(annotation.rect.contains(point)):
            widget = cast(ap.annotations.WidgetAnnotation, annotation)
            checkbox = cast(ap.forms.CheckboxField, widget.parent)
            if(annotation.active_state == "Off"):
                checkbox.value = widget.get_checked_state_name()
            else:
                checkbox.value = "Off"
        break
    # Option 2 : parcourir les champs dans l'AcroForm
    for widget in document.form:
        field = cast(ap.forms.Field, widget)
        if(field == None):
            continue
        checkBoxFound = False
        for annotation in field:
            if(annotation.rect.contains(point)):
                checkBoxFound = True
                if(annotation.active_state=="Off"):
                    annotation.parent.value = annotation.get_checked_state_name()
                else:
                    annotation.parent.value = "Off"
            if(checkBoxFound):
                break
```


## Quoi de neuf dans Aspose.PDF 23.7

Depuis la version 23.7, il est possible d'ajouter l'extraction de formes :

```python

    import aspose.pdf as ap

    input1_file = DIR_INPUT + "input_1.pdf"
    input2_file = DIR_INPUT + "input_2.pdf"

    source = ap.Document(input1_file)
    dest = ap.Document(input2_file)

    graphic_absorber = ap.vector.GraphicsAbsorber()
    graphic_absorber.visit(source.pages[1])
    area = ap.Rectangle(90, 250, 300, 400, True)
    dest.pages[1].add_graphics(graphic_absorber.elements, area)
```

Il prend également en charge la capacité de détecter le débordement lors de l'ajout de texte :

```python

    import aspose.pdf as ap

    output_file = DIR_OUTPUT + "output.pdf"
    doc = ap.Document()
    paragraph_content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras nisl tortor, efficitur sed cursus in, lobortis vitae nulla. Quisque rhoncus, felis sed dictum semper, est tellus finibus augue, ut feugiat enim risus eget tortor. Nulla finibus velit nec ante gravida sollicitudin. Morbi sollicitudin vehicula facilisis. Vestibulum ac convallis erat. Ut eget varius sem. Nam varius pharetra lorem, id ullamcorper justo auctor ac. Integer quis erat vitae lacus mollis volutpat eget et eros. Donec a efficitur dolor. Maecenas non dapibus nisi, ut pellentesque elit. Sed pellentesque rhoncus ante, a consectetur ligula viverra vel. Integer eget bibendum ante. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Curabitur elementum, sem a auctor vulputate, ante libero iaculis dolor, vitae facilisis dolor lorem at orci. Sed laoreet dui id nisi accumsan, id posuere diam accumsan."
    fragment = ap.text.TextFragment(paragraph_content)
    rectangle = ap.Rectangle(100, 600, 500, 700, False)
    paragraph = ap.text.TextParagraph()
    paragraph.vertical_alignment = ap.VerticalAlignment.TOP
    paragraph.formatting_options.wrap_mode = ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    paragraph.rectangle = rectangle
    is_fit_rectangle = fragment.text_state.is_fit_rectangle(paragraph_content, rectangle)

    while is_fit_rectangle == False:
        fragment.text_state.font_size -= 0.5
        is_fit_rectangle = fragment.text_state.is_fit_rectangle(paragraph_content, rectangle)

    paragraph.append_line(fragment)
    builder = ap.text.TextBuilder(doc.pages.add())
    builder.append_paragraph(paragraph)
    doc.save(output_file)
```


## Quoi de neuf dans Aspose.PDF 23.6

Prise en charge de la possibilité de définir le titre de la page HTML, Epub :

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "input.pdf"
    output_html = DIR_OUTPUT + "output_title.html"
    options = ap.HtmlSaveOptions()
    options.fixed_layout = True
    options.raster_images_saving_mode = ap.HtmlSaveOptions.RasterImagesSavingModes.AS_EMBEDDED_PARTS_OF_PNG_PAGE_BACKGROUND
    options.parts_embedding_mode = ap.HtmlSaveOptions.PartsEmbeddingModes.EMBED_ALL_INTO_HTML
    options.title = "NOUVELLE PAGE & TITRE"  # <-- ceci ajouté

    document = ap.Document(input_pdf)
    document.save(output_html, options)
```

## Quoi de neuf dans Aspose.PDF 23.5

Depuis la version 23.5, support pour ajouter l'option RedactionAnnotation FontSize. Utilisez l'extrait de code suivant pour résoudre cette tâche :

```python

    import aspose.pdf as ap

    doc = ap.Document(DIR_INPUT + "input.pdf")
    # Créer une instance de RedactionAnnotation pour une région spécifique de la page
    annot = ap.annotations.RedactionAnnotation(doc.pages[1], ap.Rectangle(367, 756.919982910156, 420, 823.919982910156, True))
    annot.fill_color = ap.Color.black
    annot.border_color = ap.Color.yellow
    annot.color = ap.Color.blue
    # Texte à imprimer sur l'annotation de rédaction
    annot.overlay_text = "(Inconnu)"
    annot.text_alignment = ap.HorizontalAlignment.CENTER
    # Répéter le texte de superposition sur l'annotation de rédaction
    annot.repeat = False
    # Nouvelle propriété ici !
    annot.font_size = 20
    # Ajouter l'annotation à la collection d'annotations de la première page
    doc.pages[1].annotations.add(annot, False)
    # Aplatit l'annotation et rédige le contenu de la page (c'est-à-dire supprime le texte et l'image
    # sous l'annotation rédigée)
    annot.redact()
    out_file = DIR_OUTPUT + "RedactPage_out.pdf"
    doc.save(out_file)
```


Le support pour Python 3.5 a été interrompu. Le support pour Python 3.11 a été ajouté.

## Quoi de neuf dans Aspose.PDF 23.3

La version 23.3 a introduit la prise en charge de l'ajout d'une résolution à une image. Deux méthodes peuvent être utilisées pour résoudre ce problème :

```python

    import aspose.pdf as ap

    input_file = DIR_INPUT + "input.jpg"
    table = ap.Table()
    table.column_widths = "600"
    image = ap.Image()
    image.is_apply_resolution = True
    image.file = input_file
    for i in range(0, 2):
        row = table.rows.add()
        cell = row.cells.add()
        cell.paragraphs.add(image)

    page.paragraphs.add(table)
```

L'image sera placée avec une résolution mise à l'échelle ou vous pouvez définir les propriétés FixedWidth ou FixedHeight en combinaison avec IsApplyResolution

## Quoi de neuf dans Aspose.PDF 23.1

Depuis la version 23.1, il est possible de créer une annotation PrinterMark.

Les marques d'imprimante sont des symboles graphiques ou du texte ajoutés à une page pour aider le personnel de production à identifier les composants d'un travail à plaques multiples et à maintenir une sortie cohérente pendant la production.
 Exemples couramment utilisés dans l'industrie de l'impression incluent :

- Cibles d'enregistrement pour aligner les plaques
- Rampes de gris et barres de couleur pour mesurer les couleurs et les densités d'encre
- Marques de coupe indiquant où le support de sortie doit être coupé

Nous allons montrer l'exemple de l'option avec des barres de couleur pour mesurer les couleurs et les densités d'encre. Il y a une classe abstraite de base PrinterMarkAnnotation et de celle-ci un enfant ColorBarAnnotation - qui implémente déjà ces bandes. Vérifions l'exemple :

```python

    import aspose.pdf as ap

    out_file = DIR_OUTPUT  + "ColorBarTest.pdf"
    doc = ap.Document()
    page = doc.pages.add()
    page.trim_box = ap.Rectangle(20, 20, 580, 820, True)
    add_annotations(page)
    doc.save(out_file)


def add_annotations(page: ap.Page):
    rect_black = ap.Rectangle(100, 300, 300, 320, True)
    rect_cyan = ap.Rectangle(200, 600, 260, 690, True)
    rect_magenta = ap.Rectangle(10, 650, 140, 670, True)
    color_bar_black = ap.annotations.ColorBarAnnotation(page, rect_black, ap.annotations.ColorsOfCMYK.BLACK)
    color_bar_cyan = ap.annotations.ColorBarAnnotation(page, rect_cyan, ap.annotations.ColorsOfCMYK.CYAN)
    color_ba_magenta = ap.annotations.ColorBarAnnotation(page, rect_magenta, ap.annotations.ColorsOfCMYK.BLACK)
    color_ba_magenta.color_of_cmyk = ap.annotations.ColorsOfCMYK.MAGENTA
    color_bar_yellow = ap.annotations.ColorBarAnnotation(page, ap.Rectangle(400, 250, 450, 700, True), ap.annotations.ColorsOfCMYK.YELLOW)
    page.annotations.add(color_bar_black, False)
    page.annotations.add(color_bar_cyan, False)
    page.annotations.add(color_ba_magenta, False)
    page.annotations.add(color_bar_yellow, False)
```
Also supporte l'extraction des images vectorielles. Essayez d'utiliser le code suivant pour détecter et extraire des graphiques vectoriels :

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "input.pdf"
    output_pdf = DIR_OUTPUT + "output.svg"
    doc = ap.Document(input_pdf)
    doc.pages[1].try_save_vector_graphics(output_pdf)
```