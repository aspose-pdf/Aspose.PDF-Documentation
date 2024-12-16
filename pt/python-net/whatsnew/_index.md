---
title: O que há de novo
linktitle: O que há de novo
type: docs
weight: 10
url: /pt/python-net/whatsnew/
description: Nesta página são apresentadas as novas funcionalidades mais populares no Aspose.PDF para Python via .NET que foram introduzidas em lançamentos recentes.
sitemap:
    changefreq: "monthly"
    priority: 0.8
lastmod: "2021-12-24"
---

## O que há de novo no Aspose.PDF 23.12

A partir do Aspose.PDF 23.12, foi adicionada a compatibilidade com os novos recursos de conversão:

- Implementar conversão de PDF para Markdown

```python

    import aspose.pdf as ap

    input_pdf_path = DIR_INPUT + "input.pdf"
    markdown_output_file_path = DIR_OUTPUT + "output_md_file.md"

    doc = ap.Document(input_pdf_path)
    save_options = ap.pdftomarkdown.MarkdownSaveOptions()
    save_options.resources_directory_name = "images"
    doc.save(markdown_output_file_path, save_options)
```

- Implementar conversão de OFD para PDF

```python

    import aspose.pdf as ap

    input_path = DIR_INPUT + "input.ofd"
    output_path = DIR_OUTPUT + "output.pdf"
    document = ap.Document(input_path, ap.OfdLoadOptions())
    document.save(output_path)
```


O suporte para Python 3.6 foi descontinuado.

## O que há de novo no Aspose.PDF 23.11

Desde a versão 23.11 é possível remover o texto oculto. O seguinte trecho de código pode ser usado:

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    text_absorber = ap.text.TextFragmentAbsorber()
    # Esta opção pode ser usada para evitar que outros fragmentos de texto se movam após a substituição do texto oculto.
    text_absorber.text_replace_options = ap.text.TextReplaceOptions(ap.text.TextReplaceOptions.ReplaceAdjustment.NONE)
    document.pages.accept(text_absorber)

    for fragment in text_absorber.text_fragments:
        if fragment.text_state.invisible:
            fragment.text = ''

    document.save(output_file)
```

## O que há de novo no Aspose.PDF 23.8

Desde a versão 23.8, há suporte para adicionar detecção de Atualizações Incrementais.

A função para detectar Atualizações Incrementais em um documento PDF foi adicionada.
 Essa função retorna 'true' se um documento foi salvo com atualizações incrementais; caso contrário, retorna 'false'.

```python

    import aspose.pdf as ap

    doc = ap.Document(file_path)
    updated = doc.has_incremental_update()
    print(updated)
```

Além disso, o 23.8 suporta maneiras de trabalhar com campos de caixa de seleção aninhados. Muitos formulários PDF preenchíveis têm campos de caixa de seleção que atuam como grupos de rádio:

- Criar campo de caixa de seleção de múltiplos valores:

```python

    import aspose.pdf as ap

    document = ap.Document()
    page = document.pages.add()
    checkbox = ap.forms.CheckboxField(page, ap.Rectangle(50, 50, 70, 70, True))
    # Definir o valor da primeira opção do grupo de caixa de seleção
    checkbox.export_value = "opção 1"
    # Adicionar nova opção logo abaixo das existentes
    checkbox.add_option("opção 2")
    # Adicionar nova opção no retângulo fornecido
    checkbox.add_option("opção 3", ap.Rectangle(100, 100, 120, 120, True))
    document.form.add(checkbox)
    # Selecionar a caixa de seleção adicionada
    checkbox.value = "opção 2"
    document.save(DIR_OUTPUT + "checkbox_group.pdf")
```

- Obter e definir o valor de uma checkbox de múltiplos valores:

```python

    import aspose.pdf as ap

    doc = ap.Document("example.pdf")
    form = doc.form
    checkbox = cast(ap.forms.CheckboxField, form.fields[0])

    # Os valores permitidos podem ser recuperados da coleção AllowedStates
    # Defina o valor da checkbox usando a propriedade Value
    checkbox.value = checkbox.allowed_states[0]
    checkbox_value = checkbox.value  # o valor definido anteriormente, por exemplo, "option 1"
    # O valor deve ser qualquer elemento de AllowedStates
    checkbox.value = "option 2"
    checkbox_value = checkbox.value  # opção 2
    # Desmarcar caixas definindo Value como "Off" ou definindo Checked como false
    checkbox.value = "Off"
    # ou, alternativamente:
    # checkbox.checked = False
    checkbox_value = checkbox.value  # Off
```

- Atualizar o estado da checkbox ao clicar do usuário:

```python

    import aspose.pdf as ap
    from aspose.pycore import cast

    input_file = DIR_INPUT + "input.pdf"
    document = ap.Document(input_file)
    point = ap.Point(62,462)  # por exemplo, as coordenadas de um clique do mouse
    # Opção 1: percorrer as anotações na página
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
    # Opção 2: percorrer os campos no AcroForm
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


## O que há de novo no Aspose.PDF 23.7

Desde a versão 23.7, há suporte para adicionar a extração de formas:

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

Também suporta a capacidade de detectar Overflow ao adicionar texto:

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


## O que há de novo no Aspose.PDF 23.6

Suporte à capacidade de definir o título da página HTML, Epub:

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "input.pdf"
    output_html = DIR_OUTPUT + "output_title.html"
    options = ap.HtmlSaveOptions()
    options.fixed_layout = True
    options.raster_images_saving_mode = ap.HtmlSaveOptions.RasterImagesSavingModes.AS_EMBEDDED_PARTS_OF_PNG_PAGE_BACKGROUND
    options.parts_embedding_mode = ap.HtmlSaveOptions.PartsEmbeddingModes.EMBED_ALL_INTO_HTML
    options.title = "NOVA PÁGINA & TÍTULO"  # <-- isto foi adicionado

    document = ap.Document(input_pdf)
    document.save(output_html, options)
```

## O que há de novo no Aspose.PDF 23.5

Desde a versão 23.5, há suporte para adicionar a opção FontSize em RedactionAnnotation. Use o próximo trecho de código para resolver esta tarefa:

```python

    import aspose.pdf as ap

    doc = ap.Document(DIR_INPUT + "input.pdf")
    # Cria uma instância de RedactionAnnotation para uma região específica da página
    annot = ap.annotations.RedactionAnnotation(doc.pages[1], ap.Rectangle(367, 756.919982910156, 420, 823.919982910156, True))
    annot.fill_color = ap.Color.black
    annot.border_color = ap.Color.yellow
    annot.color = ap.Color.blue
    # Texto a ser impresso na anotação de redação
    annot.overlay_text = "(Desconhecido)"
    annot.text_alignment = ap.HorizontalAlignment.CENTER
    # Repetir texto de sobreposição sobre a anotação de redação
    annot.repeat = False
    # Nova propriedade aqui!
    annot.font_size = 20
    # Adicionar anotação à coleção de anotações da primeira página
    doc.pages[1].annotations.add(annot, False)
    # Achata a anotação e redige o conteúdo da página (ou seja, remove texto e imagem
    # Sob a anotação redigida)
    annot.redact()
    out_file = DIR_OUTPUT + "RedactPage_out.pdf"
    doc.save(out_file)
```


Suporte para Python 3.5 foi descontinuado. Suporte para Python 3.11 foi adicionado.

## O que há de novo no Aspose.PDF 23.3

A versão 23.3 introduziu suporte para adicionar uma resolução a uma imagem. Dois métodos podem ser usados para resolver este problema:

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

A imagem será colocada com resolução escalada ou você pode definir as propriedades FixedWidth ou FixedHeight em combinação com IsApplyResolution.

## O que há de novo no Aspose.PDF 23.1

Desde a versão 23.1, há suporte para criação de anotação PrinterMark.

As marcas de impressora são símbolos gráficos ou texto adicionados a uma página para ajudar o pessoal de produção a identificar componentes de um trabalho de múltiplas chapas e manter uma saída consistente durante a produção.
 Exemplos comumente usados na indústria gráfica incluem:

- Alvos de registro para alinhar chapas
- Rampas de cinza e barras de cores para medir cores e densidades de tinta
- Marcas de corte mostrando onde o meio de saída deve ser cortado

Mostraremos o exemplo da opção com barras de cores para medir cores e densidades de tinta. Existe uma classe abstrata básica PrinterMarkAnnotation e dela deriva ColorBarAnnotation - que já implementa essas listras. Vamos verificar o exemplo:

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
Also suporte a extração de imagens vetoriais. Tente usar o seguinte código para detectar e extrair gráficos vetoriais:

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "input.pdf"
    output_pdf = DIR_OUTPUT + "output.svg"
    doc = ap.Document(input_pdf)
    doc.pages[1].try_save_vector_graphics(output_pdf)
```