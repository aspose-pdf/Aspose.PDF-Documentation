---
title: Что нового
linktitle: Что нового
type: docs
weight: 10
url: ru/python-net/whatsnew/
description: На этой странице представлены самые популярные новые функции в Aspose.PDF для Python через .NET, которые были представлены в последних выпусках.
sitemap:
    changefreq: "monthly"
    priority: 0.8
lastmod: "2021-12-24"
---

## Что нового в Aspose.PDF 23.12

С Aspose.PDF 23.12 была добавлена поддержка новых функций конверсии:

- Реализована конвертация PDF в Markdown

```python

    import aspose.pdf as ap

    input_pdf_path = DIR_INPUT + "input.pdf"
    markdown_output_file_path = DIR_OUTPUT + "output_md_file.md"

    doc = ap.Document(input_pdf_path)
    save_options = ap.pdftomarkdown.MarkdownSaveOptions()
    save_options.resources_directory_name = "images"
    doc.save(markdown_output_file_path, save_options)
```

- Реализована конвертация OFD в PDF

```python

    import aspose.pdf as ap

    input_path = DIR_INPUT + "input.ofd"
    output_path = DIR_OUTPUT + "output.pdf"
    document = ap.Document(input_path, ap.OfdLoadOptions())
    document.save(output_path)
```


Поддержка Python 3.6 была прекращена.

## Что нового в Aspose.PDF 23.11

Начиная с версии 23.11, появилась возможность удаления скрытого текста. Для этого можно использовать следующий фрагмент кода:

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    text_absorber = ap.text.TextFragmentAbsorber()
    # Этот параметр можно использовать, чтобы предотвратить перемещение других фрагментов текста после замены скрытого текста.
    text_absorber.text_replace_options = ap.text.TextReplaceOptions(ap.text.TextReplaceOptions.ReplaceAdjustment.NONE)
    document.pages.accept(text_absorber)

    for fragment in text_absorber.text_fragments:
        if fragment.text_state.invisible:
            fragment.text = ''

    document.save(output_file)
```

## Что нового в Aspose.PDF 23.8

Начиная с версии 23.8 поддерживается добавление обнаружения инкрементных обновлений.

Функция для обнаружения инкрементных обновлений в PDF-документе была добавлена.
 Эта функция возвращает 'true', если документ был сохранен с инкрементными обновлениями; в противном случае возвращает 'false'.

```python

    import aspose.pdf as ap

    doc = ap.Document(file_path)
    updated = doc.has_incremental_update()
    print(updated)
```

Кроме того, версия 23.8 поддерживает способы работы с вложенными полями флажков. Многие заполняемые PDF-формы имеют поля флажков, которые действуют как группы переключателей:

- Создание поля флажков с несколькими значениями:

```python

    import aspose.pdf as ap

    document = ap.Document()
    page = document.pages.add()
    checkbox = ap.forms.CheckboxField(page, ap.Rectangle(50, 50, 70, 70, True))
    # Установите значение первой опции группы флажков
    checkbox.export_value = "option 1"
    # Добавьте новую опцию прямо под существующими
    checkbox.add_option("option 2")
    # Добавьте новую опцию в заданный прямоугольник
    checkbox.add_option("option 3", ap.Rectangle(100, 100, 120, 120, True))
    document.form.add(checkbox)
    # Выберите добавленный флажок
    checkbox.value = "option 2"
    document.save(DIR_OUTPUT + "checkbox_group.pdf")
```

- Получить и установить значение флажка с множественным выбором:

```python

    import aspose.pdf as ap

    doc = ap.Document("example.pdf")
    form = doc.form
    checkbox = cast(ap.forms.CheckboxField, form.fields[0])

    # Допустимые значения можно получить из коллекции AllowedStates
    # Установите значение флажка, используя свойство Value
    checkbox.value = checkbox.allowed_states[0]
    checkbox_value = checkbox.value  # ранее установленное значение, например, "option 1"
    # Значение должно быть любым элементом AllowedStates
    checkbox.value = "option 2"
    checkbox_value = checkbox.value  # option 2
    # Снимите выделение с флажков, установив Value в "Off" или установив Checked в false
    checkbox.value = "Off"
    # или, альтернативно:
    # checkbox.checked = False
    checkbox_value = checkbox.value  # Off
```

- Обновить состояние флажка при клике пользователя:

```python

    import aspose.pdf as ap
    from aspose.pycore import cast

    input_file = DIR_INPUT + "input.pdf"
    document = ap.Document(input_file)
    point = ap.Point(62,462)  # например, координаты щелчка мыши
    # Вариант 1: просмотреть аннотации на странице
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
    # Вариант 2: просмотреть поля в AcroForm
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


## Что нового в Aspose.PDF 23.7

Начиная с версии 23.7 поддерживается добавление извлечения формы:

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

Также поддерживается возможность обнаружения переполнения при добавлении текста:

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


## Что нового в Aspose.PDF 23.6

Поддержка возможности установки заголовка страницы HTML, Epub:

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "input.pdf"
    output_html = DIR_OUTPUT + "output_title.html"
    options = ap.HtmlSaveOptions()
    options.fixed_layout = True
    options.raster_images_saving_mode = ap.HtmlSaveOptions.RasterImagesSavingModes.AS_EMBEDDED_PARTS_OF_PNG_PAGE_BACKGROUND
    options.parts_embedding_mode = ap.HtmlSaveOptions.PartsEmbeddingModes.EMBED_ALL_INTO_HTML
    options.title = "NEW PAGE & TITILE"  # <-- это добавлено

    document = ap.Document(input_pdf)
    document.save(output_html, options)
```

## Что нового в Aspose.PDF 23.5

Начиная с версии 23.5 поддерживается добавление опции RedactionAnnotation FontSize. Используйте следующий код для решения этой задачи:

```python

    import aspose.pdf as ap

    doc = ap.Document(DIR_INPUT + "input.pdf")
    # Создание экземпляра RedactionAnnotation для определенного региона страницы
    annot = ap.annotations.RedactionAnnotation(doc.pages[1], ap.Rectangle(367, 756.919982910156, 420, 823.919982910156, True))
    annot.fill_color = ap.Color.black
    annot.border_color = ap.Color.yellow
    annot.color = ap.Color.blue
    # Текст, который будет напечатан на замаскированной аннотации
    annot.overlay_text = "(Неизвестно)"
    annot.text_alignment = ap.HorizontalAlignment.CENTER
    # Повторить текст наложения поверх замаскированной аннотации
    annot.repeat = False
    # Новое свойство здесь!
    annot.font_size = 20
    # Добавление аннотации в коллекцию аннотаций первой страницы
    doc.pages[1].annotations.add(annot, False)
    # Сглаживает аннотацию и скрывает содержимое страницы (т.е. удаляет текст и изображение
    # Под замаскированной аннотацией)
    annot.redact()
    out_file = DIR_OUTPUT + "RedactPage_out.pdf"
    doc.save(out_file)
```


Поддержка Python 3.5 была прекращена. Добавлена поддержка Python 3.11.

## Что нового в Aspose.PDF 23.3

Версия 23.3 представила поддержку добавления разрешения к изображению. Для решения этой задачи можно использовать два метода:

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

Изображение будет размещено с масштабированным разрешением, или вы можете установить свойства FixedWidth или FixedHeight в сочетании с IsApplyResolution.

## Что нового в Aspose.PDF 23.1

Начиная с версии 23.1 поддерживается создание аннотации PrinterMark.

Печатные метки — это графические символы или текст, добавляемые на страницу, чтобы помочь производственному персоналу в идентификации компонентов многопластинчатой задачи и поддержании стабильного вывода во время производства.
 Примеры, часто используемые в полиграфической промышленности, включают:

- Мишени для совмещения пластин
- Серые шкалы и цветные полосы для измерения цветов и плотности чернил
- Метки обрезки, показывающие, где следует обрезать выходной материал

Мы покажем пример опции с цветными полосами для измерения цветов и плотности чернил. Существует базовый абстрактный класс PrinterMarkAnnotation и от него дочерний класс ColorBarAnnotation, который уже реализует эти полосы. Давайте проверим пример:

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
Также поддерживается извлечение векторных изображений. Попробуйте использовать следующий код для обнаружения и извлечения векторной графики:

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "input.pdf"
    output_pdf = DIR_OUTPUT + "output.svg"
    doc = ap.Document(input_pdf)
    doc.pages[1].try_save_vector_graphics(output_pdf)
```