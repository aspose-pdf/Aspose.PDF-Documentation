---
title: 有什么新功能
linktitle: 有什么新功能
type: docs
weight: 10
url: /python-net/whatsnew/
description: 本页介绍了Aspose.PDF for Python via .NET在最近发布版本中引入的最受欢迎的新功能。
sitemap:
    changefreq: "monthly"
    priority: 0.8
lastmod: "2021-12-24"
---

## Aspose.PDF 23.12中的新功能

从Aspose.PDF 23.12开始，新增了对以下转换功能的支持：

- 实现PDF到Markdown的转换

```python

    import aspose.pdf as ap

    input_pdf_path = DIR_INPUT + "input.pdf"
    markdown_output_file_path = DIR_OUTPUT + "output_md_file.md"

    doc = ap.Document(input_pdf_path)
    save_options = ap.pdftomarkdown.MarkdownSaveOptions()
    save_options.resources_directory_name = "images"
    doc.save(markdown_output_file_path, save_options)
```

- 实现OFD到PDF的转换

```python

    import aspose.pdf as ap

    input_path = DIR_INPUT + "input.ofd"
    output_path = DIR_OUTPUT + "output.pdf"
    document = ap.Document(input_path, ap.OfdLoadOptions())
    document.save(output_path)
```


Python 3.6 的支持已被终止。

## Aspose.PDF 23.11 中的新功能

从 23.11 版本开始，可以删除隐藏文本。可以使用以下代码片段：

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    text_absorber = ap.text.TextFragmentAbsorber()
    # 此选项可用于防止在替换隐藏文本后其他文本片段移动。
    text_absorber.text_replace_options = ap.text.TextReplaceOptions(ap.text.TextReplaceOptions.ReplaceAdjustment.NONE)
    document.pages.accept(text_absorber)

    for fragment in text_absorber.text_fragments:
        if fragment.text_state.invisible:
            fragment.text = ''

    document.save(output_file)
```    

## Aspose.PDF 23.8 中的新功能

从 23.8 版本开始支持添加增量更新检测。

已添加检测 PDF 文档中增量更新的功能。
 此函数在文档以增量更新保存时返回'true'；否则，返回'false'。

```python

    import aspose.pdf as ap

    doc = ap.Document(file_path)
    updated = doc.has_incremental_update()
    print(updated)
```

此外，23.8支持处理嵌套复选框字段的方法。许多可填写的PDF表单具有作为单选组的复选框字段：

- 创建多值复选框字段：

```python

    import aspose.pdf as ap

    document = ap.Document()
    page = document.pages.add()
    checkbox = ap.forms.CheckboxField(page, ap.Rectangle(50, 50, 70, 70, True))
    # 设置第一个复选框组选项值
    checkbox.export_value = "option 1"
    # 在现有选项下添加新选项
    checkbox.add_option("option 2")
    # 在给定矩形位置添加新选项
    checkbox.add_option("option 3", ap.Rectangle(100, 100, 120, 120, True))
    document.form.add(checkbox)
    # 选择添加的复选框
    checkbox.value = "option 2"
    document.save(DIR_OUTPUT + "checkbox_group.pdf")
```

- 获取和设置多值复选框的值：

```python

    import aspose.pdf as ap

    doc = ap.Document("example.pdf")
    form = doc.form
    checkbox = cast(ap.forms.CheckboxField, form.fields[0])

    # 允许的值可以从 AllowedStates 集合中检索
    # 使用 Value 属性设置复选框的值
    checkbox.value = checkbox.allowed_states[0]
    checkbox_value = checkbox.value  # 之前设置的值，例如 "option 1"
    # 值应为 AllowedStates 的任何元素
    checkbox.value = "option 2"
    checkbox_value = checkbox.value  # option 2
    # 通过将 Value 设置为 "Off" 或将 Checked 设置为 false 来取消选中
    checkbox.value = "Off"
    # 或者，替代方法：
    # checkbox.checked = False
    checkbox_value = checkbox.value  # Off
```

- 用户点击时更新复选框状态：

```python

    import aspose.pdf as ap
    from aspose.pycore import cast

    input_file = DIR_INPUT + "input.pdf"
    document = ap.Document(input_file)
    point = ap.Point(62,462)  # 例如，鼠标点击的坐标
    # 选项 1：查看页面上的注释
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
    # 选项 2：查看 AcroForm 中的字段
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


## Aspose.PDF 23.7 中的新功能

由于23.7版本支持添加形状提取：

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

还支持在添加文本时检测溢出的功能：

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


## Aspose.PDF 23.6 的新功能

支持设置 HTML 和 Epub 页面标题的功能：

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "input.pdf"
    output_html = DIR_OUTPUT + "output_title.html"
    options = ap.HtmlSaveOptions()
    options.fixed_layout = True
    options.raster_images_saving_mode = ap.HtmlSaveOptions.RasterImagesSavingModes.AS_EMBEDDED_PARTS_OF_PNG_PAGE_BACKGROUND
    options.parts_embedding_mode = ap.HtmlSaveOptions.PartsEmbeddingModes.EMBED_ALL_INTO_HTML
    options.title = "NEW PAGE & TITILE"  # <-- 这是新增的

    document = ap.Document(input_pdf)
    document.save(output_html, options)
```

## Aspose.PDF 23.5 的新功能

自 23.5 版本起，支持添加 RedactionAnnotation 字体大小选项。使用下面的代码片段来解决此任务：

```python

    import aspose.pdf as ap

    doc = ap.Document(DIR_INPUT + "input.pdf")
    # 为特定页面区域创建 RedactionAnnotation 实例
    annot = ap.annotations.RedactionAnnotation(doc.pages[1], ap.Rectangle(367, 756.919982910156, 420, 823.919982910156, True))
    annot.fill_color = ap.Color.black
    annot.border_color = ap.Color.yellow
    annot.color = ap.Color.blue
    # 要在修订注释上打印的文本
    annot.overlay_text = "(Unknown)"
    annot.text_alignment = ap.HorizontalAlignment.CENTER
    # 在修订注释上重复覆盖文本
    annot.repeat = False
    # 这里是新的属性！
    annot.font_size = 20
    # 将注释添加到第一页的注释集合中
    doc.pages[1].annotations.add(annot, False)
    # 扁平化注释并修订页面内容（即删除修订注释下方的文本和图像）
    annot.redact()
    out_file = DIR_OUTPUT + "RedactPage_out.pdf"
    doc.save(out_file)
```


对Python 3.5的支持已被终止。对Python 3.11的支持已被添加。

## Aspose.PDF 23.3中的新功能

版本23.3引入了为图像添加分辨率的支持。可以使用两种方法来解决此问题：

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

图像将以缩放分辨率放置，或者您可以结合使用FixedWidth或FixedHeight属性与IsApplyResolution

## Aspose.PDF 23.1中的新功能

自23.1版本起支持创建PrinterMark注释。

打印标记是添加到页面的图形符号或文本，以帮助生产人员识别多板作业的组件并在生产过程中保持一致的输出。
 常用于印刷行业的示例包括：

- 对齐版材的套准标记
- 用于测量颜色和墨水密度的灰阶和颜色条
- 显示输出介质修剪位置的切割标记

我们将展示一个带有颜色条选项的示例，用于测量颜色和墨水密度。这里有一个基本的抽象类 PrinterMarkAnnotation，从它派生出了子类 ColorBarAnnotation - 它已经实现了这些条纹。让我们检查这个示例：

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
还支持矢量图像提取。尝试使用以下代码来检测和提取矢量图形：

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "input.pdf"
    output_pdf = DIR_OUTPUT + "output.svg"
    doc = ap.Document(input_pdf)
    doc.pages[1].try_save_vector_graphics(output_pdf)
```