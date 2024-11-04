---
title: Qué hay de nuevo
linktitle: Qué hay de nuevo
type: docs
weight: 10
url: /python-net/whatsnew/
description: En esta página se presentan las características nuevas más populares en Aspose.PDF para Python a través de .NET que se han introducido en lanzamientos recientes.
sitemap:
    changefreq: "monthly"
    priority: 0.8
lastmod: "2021-12-24"
---

## Qué hay de nuevo en Aspose.PDF 23.12

A partir de Aspose.PDF 23.12, se agregó soporte a las nuevas características de conversión:

- Implementar conversión de PDF a Markdown

```python

    import aspose.pdf as ap

    input_pdf_path = DIR_INPUT + "input.pdf"
    markdown_output_file_path = DIR_OUTPUT + "output_md_file.md"

    doc = ap.Document(input_pdf_path)
    save_options = ap.pdftomarkdown.MarkdownSaveOptions()
    save_options.resources_directory_name = "images"
    doc.save(markdown_output_file_path, save_options)
```

- Implementar conversión de OFD a PDF

```python

    import aspose.pdf as ap

    input_path = DIR_INPUT + "input.ofd"
    output_path = DIR_OUTPUT + "output.pdf"
    document = ap.Document(input_path, ap.OfdLoadOptions())
    document.save(output_path)
```


El soporte para Python 3.6 ha sido descontinuado.

## Novedades en Aspose.PDF 23.11

Desde la versión 23.11 es posible eliminar el texto oculto. Se puede usar el siguiente fragmento de código:

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    text_absorber = ap.text.TextFragmentAbsorber()
    # Esta opción se puede usar para evitar que otros fragmentos de texto se muevan después de la sustitución del texto oculto.
    text_absorber.text_replace_options = ap.text.TextReplaceOptions(ap.text.TextReplaceOptions.ReplaceAdjustment.NONE)
    document.pages.accept(text_absorber)

    for fragment in text_absorber.text_fragments:
        if fragment.text_state.invisible:
            fragment.text = ''

    document.save(output_file)
```    

## Novedades en Aspose.PDF 23.8

Desde la versión 23.8 se admite añadir la detección de Actualizaciones Incrementales.

Se ha añadido la función para detectar Actualizaciones Incrementales en un documento PDF.
 Esta función devuelve 'true' si un documento fue guardado con actualizaciones incrementales; de lo contrario, devuelve 'false'.

```python

    import aspose.pdf as ap

    doc = ap.Document(file_path)
    updated = doc.has_incremental_update()
    print(updated)
```

Además, la versión 23.8 admite formas de trabajar con campos de casillas de verificación anidadas. Muchos formularios PDF rellenables tienen campos de casillas de verificación que actúan como grupos de radio:

- Crear campo de casilla de verificación de múltiples valores:

```python

    import aspose.pdf as ap

    document = ap.Document()
    page = document.pages.add()
    checkbox = ap.forms.CheckboxField(page, ap.Rectangle(50, 50, 70, 70, True))
    # Establecer el valor de la primera opción del grupo de casillas
    checkbox.export_value = "option 1"
    # Añadir nueva opción justo debajo de las existentes
    checkbox.add_option("option 2")
    # Añadir nueva opción en el rectángulo dado
    checkbox.add_option("option 3", ap.Rectangle(100, 100, 120, 120, True))
    document.form.add(checkbox)
    # Seleccionar la casilla añadida
    checkbox.value = "option 2"
    document.save(DIR_OUTPUT + "checkbox_group.pdf")
```

- Obtener y establecer el valor de un checkbox de múltiples valores:

```python

    import aspose.pdf as ap

    doc = ap.Document("example.pdf")
    form = doc.form
    checkbox = cast(ap.forms.CheckboxField, form.fields[0])

    # Los valores permitidos pueden ser recuperados de la colección AllowedStates
    # Establecer el valor del checkbox usando la propiedad Value
    checkbox.value = checkbox.allowed_states[0]
    checkbox_value = checkbox.value  # el valor previamente establecido, por ejemplo, "opción 1"
    # El valor debe ser cualquier elemento de AllowedStates
    checkbox.value = "opción 2"
    checkbox_value = checkbox.value  # opción 2
    # Desmarcar las cajas estableciendo Value en "Off" o estableciendo Checked en falso
    checkbox.value = "Off"
    # o, alternativamente:
    # checkbox.checked = False
    checkbox_value = checkbox.value  # Off
```

- Actualizar el estado del checkbox al hacer clic el usuario:

```python

    import aspose.pdf as ap
    from aspose.pycore import cast

    input_file = DIR_INPUT + "input.pdf"
    document = ap.Document(input_file)
    point = ap.Point(62,462)  # por ejemplo, las coordenadas de un clic del ratón
    # Opción 1: revisar las anotaciones en la página
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
    # Opción 2: revisar los campos en el AcroForm
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


## Qué hay de nuevo en Aspose.PDF 23.7

Desde la versión 23.7 se admite agregar la extracción de formas:

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

También se admite la capacidad de detectar desbordamiento al agregar texto:

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


## Qué hay de nuevo en Aspose.PDF 23.6

Soporte para la capacidad de establecer el título de la página HTML, Epub:

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "input.pdf"
    output_html = DIR_OUTPUT + "output_title.html"
    options = ap.HtmlSaveOptions()
    options.fixed_layout = True
    options.raster_images_saving_mode = ap.HtmlSaveOptions.RasterImagesSavingModes.AS_EMBEDDED_PARTS_OF_PNG_PAGE_BACKGROUND
    options.parts_embedding_mode = ap.HtmlSaveOptions.PartsEmbeddingModes.EMBED_ALL_INTO_HTML
    options.title = "NUEVA PÁGINA Y TÍTULO"  # <-- esto se añadió

    document = ap.Document(input_pdf)
    document.save(output_html, options)
```

## Qué hay de nuevo en Aspose.PDF 23.5

Desde la versión 23.5 se soporta añadir la opción RedactionAnnotation FontSize. Use el siguiente fragmento de código para resolver esta tarea:

```python

    import aspose.pdf as ap

    doc = ap.Document(DIR_INPUT + "input.pdf")
    # Crear instancia de RedactionAnnotation para una región específica de la página
    annot = ap.annotations.RedactionAnnotation(doc.pages[1], ap.Rectangle(367, 756.919982910156, 420, 823.919982910156, True))
    annot.fill_color = ap.Color.black
    annot.border_color = ap.Color.yellow
    annot.color = ap.Color.blue
    # Texto a imprimir en la anotación de redacción
    annot.overlay_text = "(Desconocido)"
    annot.text_alignment = ap.HorizontalAlignment.CENTER
    # Repetir texto de superposición sobre la anotación de redacción
    annot.repeat = False
    # ¡Nueva propiedad aquí!
    annot.font_size = 20
    # Añadir anotación a la colección de anotaciones de la primera página
    doc.pages[1].annotations.add(annot, False)
    # Aplana la anotación y redacta el contenido de la página (es decir, elimina texto e imagen
    # Bajo la anotación redactada)
    annot.redact()
    out_file = DIR_OUTPUT + "RedactPage_out.pdf"
    doc.save(out_file)
```


El soporte para Python 3.5 ha sido descontinuado. Se ha agregado soporte para Python 3.11.

## Qué hay de nuevo en Aspose.PDF 23.3

La versión 23.3 introdujo soporte para agregar una resolución a una imagen. Se pueden usar dos métodos para resolver este problema:

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

La imagen se colocará con resolución escalada o puede establecer propiedades de AnchoFijo o AltoFijo en combinación con IsApplyResolution

## Qué hay de nuevo en Aspose.PDF 23.1

Desde la versión 23.1 se admite la creación de anotaciones PrinterMark.

Las marcas de impresora son símbolos gráficos o texto añadidos a una página para ayudar al personal de producción a identificar componentes de un trabajo de múltiples placas y mantener una salida consistente durante la producción.
 Ejemplos comúnmente utilizados en la industria de la impresión incluyen:

- Objetivos de registro para alinear placas
- Rampas grises y barras de color para medir colores y densidades de tinta
- Marcas de corte que muestran dónde se debe recortar el medio de salida

Mostraremos el ejemplo de la opción con barras de color para medir colores y densidades de tinta. Hay una clase abstracta básica PrinterMarkAnnotation y de ella una clase hija ColorBarAnnotation, que ya implementa estas franjas. Vamos a ver el ejemplo:

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
También se admite la extracción de imágenes vectoriales. Intenta usar el siguiente código para detectar y extraer gráficos vectoriales:

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "input.pdf"
    output_pdf = DIR_OUTPUT + "output.svg"
    doc = ap.Document(input_pdf)
    doc.pages[1].try_save_vector_graphics(output_pdf)
```