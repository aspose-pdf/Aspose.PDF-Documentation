---
title: ما الجديد
linktitle: ما الجديد
type: docs
weight: 10
url: /ar/python-net/whatsnew/
description: في هذه الصفحة يتم تقديم الميزات الجديدة الأكثر شيوعًا في Aspose.PDF لـ Python عبر .NET التي تم تقديمها في الإصدارات الأخيرة.
sitemap:
    changefreq: "monthly"
    priority: 0.8
lastmod: "2021-12-24"
---

## ما الجديد في Aspose.PDF 23.12

من Aspose.PDF 23.12، تمت إضافة دعم لميزات التحويل الجديدة:

- تنفيذ تحويل PDF إلى Markdown

```python

    import aspose.pdf as ap

    input_pdf_path = DIR_INPUT + "input.pdf"
    markdown_output_file_path = DIR_OUTPUT + "output_md_file.md"

    doc = ap.Document(input_pdf_path)
    save_options = ap.pdftomarkdown.MarkdownSaveOptions()
    save_options.resources_directory_name = "images"
    doc.save(markdown_output_file_path, save_options)
```

- تنفيذ تحويل OFD إلى PDF

```python

    import aspose.pdf as ap

    input_path = DIR_INPUT + "input.ofd"
    output_path = DIR_OUTPUT + "output.pdf"
    document = ap.Document(input_path, ap.OfdLoadOptions())
    document.save(output_path)
```


دعم بايثون 3.6 قد تم إيقافه.

## ما الجديد في Aspose.PDF 23.11

منذ 23.11 أصبح من الممكن إزالة النص المخفي. يمكن استخدام جزء الشفرة التالي:

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    text_absorber = ap.text.TextFragmentAbsorber()
    # يمكن استخدام هذا الخيار لمنع تحرك أجزاء النص الأخرى بعد استبدال النص المخفي.
    text_absorber.text_replace_options = ap.text.TextReplaceOptions(ap.text.TextReplaceOptions.ReplaceAdjustment.NONE)
    document.pages.accept(text_absorber)

    for fragment in text_absorber.text_fragments:
        if fragment.text_state.invisible:
            fragment.text = ''

    document.save(output_file)
```    

## ما الجديد في Aspose.PDF 23.8

منذ الإصدار 23.8 يدعم إضافة اكتشاف التحديثات التزايدية.

تمت إضافة وظيفة لاكتشاف التحديثات التزايدية في مستند PDF.
 هذه الدالة تعيد 'true' إذا تم حفظ المستند بتحديثات تدريجية؛ خلاف ذلك، تعيد 'false'.

```python

    import aspose.pdf as ap

    doc = ap.Document(file_path)
    updated = doc.has_incremental_update()
    print(updated)
```

أيضًا، يدعم الإصدار 23.8 الطرق للعمل مع حقول مربعات الاختيار المتداخلة. العديد من نماذج PDF القابلة للتعبئة تحتوي على حقول مربعات اختيار تعمل كمجموعات راديو:

- إنشاء حقل مربع اختيار متعدد القيم:

```python

    import aspose.pdf as ap

    document = ap.Document()
    page = document.pages.add()
    checkbox = ap.forms.CheckboxField(page, ap.Rectangle(50, 50, 70, 70, True))
    # تعيين قيمة خيار مجموعة مربعات الاختيار الأول
    checkbox.export_value = "option 1"
    # إضافة خيار جديد مباشرة تحت الخيارات الموجودة
    checkbox.add_option("option 2")
    # إضافة خيار جديد في المستطيل المعطى
    checkbox.add_option("option 3", ap.Rectangle(100, 100, 120, 120, True))
    document.form.add(checkbox)
    # تحديد مربع الاختيار المضاف
    checkbox.value = "option 2"
    document.save(DIR_OUTPUT + "checkbox_group.pdf")
```

- الحصول على وتعيين قيمة مربع اختيار متعدد القيم:

```python

    import aspose.pdf as ap

    doc = ap.Document("example.pdf")
    form = doc.form
    checkbox = cast(ap.forms.CheckboxField, form.fields[0])

    # يمكن استرجاع القيم المسموح بها من مجموعة AllowedStates
    # تعيين قيمة مربع الاختيار باستخدام خاصية Value
    checkbox.value = checkbox.allowed_states[0]
    checkbox_value = checkbox.value  # القيمة المعينة سابقًا، مثل "الخيار 1"
    # يجب أن تكون القيمة أي عنصر من عناصر AllowedStates
    checkbox.value = "الخيار 2"
    checkbox_value = checkbox.value  # الخيار 2
    # إلغاء تحديد المربعات إما بتعيين القيمة إلى "Off" أو بتعيين Checked إلى false
    checkbox.value = "Off"
    # أو، بدلاً من ذلك:
    # checkbox.checked = False
    checkbox_value = checkbox.value  # Off
```

- تحديث حالة مربع الاختيار عند نقرة المستخدم:

```python

    import aspose.pdf as ap
    from aspose.pycore import cast

    input_file = DIR_INPUT + "input.pdf"
    document = ap.Document(input_file)
    point = ap.Point(62,462)  # على سبيل المثال، إحداثيات نقرة الماوس
    # الخيار 1: البحث من خلال التعليقات التوضيحية على الصفحة
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
    # الخيار 2: البحث من خلال الحقول في AcroForm
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


## ما الجديد في Aspose.PDF 23.7

منذ الإصدار 23.7 يدعم إضافة استخراج الأشكال:

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

كما يدعم القدرة على كشف تجاوز النص عند الإضافة:

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


## ما الجديد في Aspose.PDF 23.6

دعم القدرة على تعيين عنوان صفحة HTML وEpub:

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "input.pdf"
    output_html = DIR_OUTPUT + "output_title.html"
    options = ap.HtmlSaveOptions()
    options.fixed_layout = True
    options.raster_images_saving_mode = ap.HtmlSaveOptions.RasterImagesSavingModes.AS_EMBEDDED_PARTS_OF_PNG_PAGE_BACKGROUND
    options.parts_embedding_mode = ap.HtmlSaveOptions.PartsEmbeddingModes.EMBED_ALL_INTO_HTML
    options.title = "NEW PAGE & TITILE"  # <-- هذا مضاف

    document = ap.Document(input_pdf)
    document.save(output_html, options)
```

## ما الجديد في Aspose.PDF 23.5

منذ الإصدار 23.5 يدعم إضافة خيار حجم الخط RedactionAnnotation. استخدم الكود التالي لحل هذه المهمة:

```python

    import aspose.pdf as ap

    doc = ap.Document(DIR_INPUT + "input.pdf")
    # إنشاء مثيل RedactionAnnotation لمنطقة صفحة محددة
    annot = ap.annotations.RedactionAnnotation(doc.pages[1], ap.Rectangle(367, 756.919982910156, 420, 823.919982910156, True))
    annot.fill_color = ap.Color.black
    annot.border_color = ap.Color.yellow
    annot.color = ap.Color.blue
    # النص الذي سيتم طباعته على تعتيم التعليق
    annot.overlay_text = "(Unknown)"
    annot.text_alignment = ap.HorizontalAlignment.CENTER
    # تكرار النص المضاف فوق التعتيم التعليق
    annot.repeat = False
    # خاصية جديدة هنا!
    annot.font_size = 20
    # إضافة التعليق إلى مجموعة التعليقات في الصفحة الأولى
    doc.pages[1].annotations.add(annot, False)
    # تسطيح التعليق وتعتيم محتويات الصفحة (أي إزالة النص والصورة
    # تحت التعليق المعتم)
    annot.redact()
    out_file = DIR_OUTPUT + "RedactPage_out.pdf"
    doc.save(out_file)
```


دعم Python 3.5 قد تم إيقافه. تم إضافة دعم لـ Python 3.11.

## ما الجديد في Aspose.PDF 23.3

قدمت النسخة 23.3 دعمًا لإضافة دقة للصورة. يمكن استخدام طريقتين لحل هذه المشكلة:

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

سيتم وضع الصورة بدقة مضبوطة أو يمكنك تعيين خصائص FixedWidth أو FixedHeight بالاشتراك مع IsApplyResolution

## ما الجديد في Aspose.PDF 23.1

منذ النسخة 23.1، تم دعم إنشاء توضيح PrinterMark.

علامات الطابعة هي رموز بيانية أو نص يضاف إلى الصفحة لمساعدة موظفي الإنتاج في تحديد مكونات وظيفة متعددة الألواح والحفاظ على إنتاج متسق أثناء الإنتاج.
 أمثلة شائعة الاستخدام في صناعة الطباعة تشمل:

- أهداف التسجيل لمحاذاة الألواح
- تدرجات الرمادي وأشرطة الألوان لقياس الألوان وكثافات الحبر
- علامات القطع التي تظهر مكان قطع وسيط الإخراج

سنوضح مثال الخيار مع أشرطة الألوان لقياس الألوان وكثافات الحبر. هناك فئة مجردة أساسية PrinterMarkAnnotation ومنها فئة فرعية ColorBarAnnotation - التي تنفذ بالفعل هذه الأشرطة. دعونا نتحقق من المثال:

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
أيضًا دعم استخراج الصور المتجهة. حاول استخدام الكود التالي لاكتشاف واستخراج الرسومات المتجهة:

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "input.pdf"
    output_pdf = DIR_OUTPUT + "output.svg"
    doc = ap.Document(input_pdf)
    doc.pages[1].try_save_vector_graphics(output_pdf)
```