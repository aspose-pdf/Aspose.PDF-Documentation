---
title: إنشاء أو إضافة جدول في PDF باستخدام Python
linktitle: إنشاء أو إضافة جدول
type: docs
weight: 10
url: /ar/python-net/add-table-in-existing-pdf-document/
description: Aspose.PDF for Python عبر .NET هي مكتبة تستخدم لإنشاء وقراءة وتحرير جداول PDF. تحقق من الوظائف المتقدمة الأخرى في هذا الموضوع.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "إنشاء أو إضافة جدول في PDF باستخدام Python",
    "alternativeHeadline": "كيفية إضافة جدول في PDF باستخدام Python عبر .NET",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد مستندات PDF",
    "keywords": "pdf, python, إنشاء جدول في pdf, إضافة جدول",
    "wordcount": "302",
    "proficiencyLevel":"مبتدئ",
    "publisher": {
        "@type": "Organization",
        "name": "فريق وثائق Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/python-net/add-table-in-existing-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-table-in-existing-pdf-document/"
    },
    "dateModified": "2023-02-04",
    "description": "Aspose.PDF for Python عبر .NET هي مكتبة تستخدم لإنشاء وقراءة وتحرير جداول PDF. تحقق من الوظائف المتقدمة الأخرى في هذا الموضوع."
}
</script>


## إنشاء جدول باستخدام بايثون

الجداول مهمة عند العمل مع مستندات PDF. توفر ميزات رائعة لعرض المعلومات بطريقة منظمة. تحتوي مساحة الأسماء Aspose.PDF على فئات باسم [Table](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/)، و[Cell](https://reference.aspose.com/pdf/python-net/aspose.pdf/cell/)، و[Row](https://reference.aspose.com/pdf/python-net/aspose.pdf/row/) التي توفر وظائف لإنشاء الجداول عند إنشاء مستندات PDF من الصفر.

يمكن إنشاء جدول عن طريق إنشاء كائن من فئة Table.

```python

    table = ap.Table()
```

### إضافة جدول إلى مستند PDF موجود

لإضافة جدول إلى ملف PDF موجود باستخدام Aspose.PDF لبايثون عبر .NET، اتبع الخطوات التالية:

1. قم بتحميل الملف المصدر.
2. قم بتهيئة جدول واضبط أعمدته وصفوفه.
3. اضبط إعدادات الجدول (لقد قمنا بتعيين الحدود).
4. قم بملء الجدول.
5. أضف الجدول إلى الصفحة.
6. احفظ الملف.

توضح مقتطفات الشيفرة التالية كيفية إضافة نص في ملف PDF موجود.

```python

    import aspose.pdf as ap

    # تحميل مستند PDF المصدر
    doc = ap.Document(input_file)
    # تهيئة مثيل جديد من الجدول
    table = ap.Table()
    # تعيين لون حدود الجدول كرمادي فاتح
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 5, ap.Color.from_rgb(apd.Color.light_gray))
    # تعيين الحدود لخلايا الجدول
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 5, ap.Color.from_rgb(apd.Color.light_gray))
    # إنشاء حلقة لإضافة 10 صفوف
    for row_count in range(0, 10):
        # إضافة صف إلى الجدول
        row = table.rows.add()
        # إضافة خلايا الجدول
        row.cells.add("عمود (" + str(row_count) + ", 1)")
        row.cells.add("عمود (" + str(row_count) + ", 2)")
        row.cells.add("عمود (" + str(row_count) + ", 3)")
    # إضافة كائن الجدول إلى الصفحة الأولى من المستند المدخل
    doc.pages[1].paragraphs.add(table)
    # حفظ المستند المحدث الذي يحتوي على كائن الجدول
    doc.save(output_file)
```

### دمج الأعمدة والصفوف في الجداول

يوفر Aspose.PDF لـ Python عبر .NET خاصية [col_span](https://reference.aspose.com/pdf/python-net/aspose.pdf/cell/#properties) لدمج الأعمدة في الجدول وخاصية [row_span](https://reference.aspose.com/pdf/python-net/aspose.pdf/cell/#properties) لدمج الصفوف.

نحن نستخدم خاصية `col_span` أو `row_span` على كائن `Cell` الذي ينشئ خلية الجدول. بعد تطبيق الخصائص المطلوبة، يمكن إضافة الخلية التي تم إنشاؤها إلى الجدول.

```python

    import aspose.pdf as ap

    # تهيئة كائن المستند عن طريق استدعاء المُنشئ الفارغ
    pdf_document = ap.Document()
    pdf_document.pages.add()
    # تهيئة مثيل جديد من الجدول
    table = ap.Table()
    # تعيين لون حدود الجدول كرمادي فاتح
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.black)
    # تعيين الحدود لخلايا الجدول
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.black)
    # إضافة الصف الأول إلى الجدول
    row1 = table.rows.add()
    for cellCount in range(1, 5):
        # إضافة خلايا الجدول
        row1.cells.add("اختبار 1" + str(cellCount))

    # إضافة الصف الثاني إلى الجدول
    row2 = table.rows.add()
    row2.cells.add("اختبار 2 1")
    cell = row2.cells.add("اختبار 2 2")
    cell.col_span = 2
    row2.cells.add("اختبار 2 4")

    # إضافة الصف الثالث إلى الجدول
    row3 = table.rows.add()
    row3.cells.add("اختبار 3 1")
    row3.cells.add("اختبار 3 2")
    row3.cells.add("اختبار 3 3")
    row3.cells.add("اختبار 3 4")

    # إضافة الصف الرابع إلى الجدول
    row4 = table.rows.add()
    row4.cells.add("اختبار 4 1")
    cell = row4.cells.add("اختبار 4 2")
    cell.row_span = 2
    row4.cells.add("اختبار 4 3")
    row4.cells.add("اختبار 4 4")

    # إضافة الصف الخامس إلى الجدول
    row5 = table.rows.add()
    row5.cells.add("اختبار 5 1")
    row5.cells.add("اختبار 5 3")
    row5.cells.add("اختبار 5 4")

    # إضافة كائن الجدول إلى الصفحة الأولى من المستند المدخل
    pdf_document.pages[1].paragraphs.add(table)
    # حفظ المستند المحدث الذي يحتوي على كائن الجدول
    pdf_document.save(output_file)
```


نتيجة تنفيذ الكود أدناه هي الجدول الموضح في الصورة التالية:

![عرض توضيحي لـ ColSpan وRowSpan](colspan_rowspan.png)

## العمل مع الحدود والهوامش والتعبئة

يرجى ملاحظة أنه يدعم أيضًا ميزة تعيين نمط الحدود والهوامش والتعبئة للخلايا في الجداول. قبل الدخول في تفاصيل تقنية أكثر، من المهم فهم مفاهيم الحدود والهوامش والتعبئة التي تُعرض أدناه في مخطط:

![الحدود والهوامش والتعبئة](set-border-style-margins-and-padding-of-table_1.png)

في الشكل أعلاه، يمكنك أن ترى أن حدود الجدول والصف والخلايا تتداخل. باستخدام Aspose.PDF، يمكن أن يكون للجدول هوامش وللخلايا تعبئة. لتعيين هوامش الخلايا، علينا تعيين تعبئة الخلايا.

### الحدود

لتعيين حدود كائنات [الجدول](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/)، [الصف](https://reference.aspose.com/pdf/python-net/aspose.pdf/row/) و[الخلايا](https://reference.aspose.com/pdf/python-net/aspose.pdf/cell/)، استخدم خصائص Table.border وRow.border وCell.border.
 يمكن أيضًا تعيين حدود الخلايا باستخدام خاصية [Table](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) أو فئة Row [default_cell_border](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties). جميع الخصائص المتعلقة بالحدود التي نوقشت أعلاه تُعين إلى مثيل لفئة Row، التي يتم إنشاؤها عن طريق استدعاء المنشئ الخاص بها. تحتوي فئة Row على العديد من التحميلات الزائدة التي تأخذ تقريبًا جميع المعلمات المطلوبة لتخصيص الحدود.

### الهوامش أو الحشو

يمكن إدارة حشو الخلايا باستخدام خاصية [default_cell_padding](https://reference.aspose.com/pdf/python-net/aspose.pdf/row/#properties) لفئة Table. جميع الخصائص المتعلقة بالحشو تُعين إلى مثيل لفئة [MarginInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) التي تأخذ معلومات عن معلمات `left`، `right`، `top`، و`bottom` لإنشاء هوامش مخصصة.
في المثال التالي، تم تعيين عرض حد الخلية إلى 0.1 نقطة، وتم تعيين عرض حد الجدول إلى 1 نقطة وتم تعيين حشوة الخلية إلى 5 نقاط.

![الهامش والحد في جدول PDF](margin-border.png)

```python

    import aspose.pdf as ap

    # إنشاء كائن Document عن طريق استدعاء المُنشئ الفارغ
    doc = ap.Document()
    page = doc.pages.add()
    # إنشاء كائن جدول
    tab1 = ap.Table()
    # إضافة الجدول في مجموعة الفقرات للقسم المطلوب
    page.paragraphs.add(tab1)
    # تعيين عرض الأعمدة في الجدول
    tab1.column_widths = "50 50 50"
    # تعيين حد الخلية الافتراضي باستخدام كائن BorderInfo
    tab1.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.1)
    # تعيين حد الجدول باستخدام كائن BorderInfo مخصص آخر
    tab1.border = ap.BorderInfo(ap.BorderSide.ALL, 1)
    # إنشاء كائن MarginInfo وتعيين هوامشه اليسار والأسفل واليمين والأعلى
    margin = ap.MarginInfo()
    margin.top = 5
    margin.left = 5
    margin.right = 5
    margin.bottom = 5
    # تعيين حشوة الخلية الافتراضية إلى كائن MarginInfo
    tab1.default_cell_padding = margin
    # إنشاء صفوف في الجدول ثم خلايا في الصفوف
    row1 = tab1.rows.add()
    row1.cells.add("col1")
    row1.cells.add("col2")
    row1.cells.add()
    my_text = ap.text.TextFragment("col3 with large text string")
    # Row1.Cells.Add("col3 with large text string to be placed inside cell")
    row1.cells[2].paragraphs.add(my_text)
    row1.cells[2].is_word_wrapped = False
    row2 = tab1.rows.add()
    row2.cells.add("item1")
    row2.cells.add("item2")
    row2.cells.add("item3")
    # حفظ ملف Pdf
    doc.save(output_file)
```


لإنشاء جدول بزوايا مستديرة، استخدم قيمة [BorderInfo class](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderinfo/) [rounded_border_radius](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderinfo/#properties) واضبط نمط زوايا الجدول ليكون مستديرًا.

```python
    
    import aspose.pdf as ap
    
    tab1 = ap.Table()
    graph = ap.GraphInfo()
    graph.color = ap.Color.red
    # إنشاء كائن BorderInfo فارغ
    b_info = ap.BorderInfo(ap.BorderSide.ALL, graph)
    # ضبط الحدود لتكون مستديرة حيث نصف قطر الدائرة هو 15
    b_info.rounded_border_radius = 15
    # ضبط نمط زوايا الجدول ليكون مستديرًا
    tab1.corner_style = ap.BorderCornerStyle.ROUND
    # ضبط معلومات حدود الجدول
    tab1.border = b_info
```

## تطبيق إعدادات AutoFit مختلفة على جدول

عند تصميم جدول باستخدام أداة مرئية مثل مايكروسوفت وورد، ستستخدم بشكل متكرر إحدى ميزات AutoFit لضبط حجم الجدول بشكل ملائم إلى العرض المطلوب.
 على سبيل المثال، يمكنك استخدام الخيار "AUTO_FIT_TO_WINDOW" لمطابقة عرض الجدول مع الصفحة أو AUTO_FIT_TO_CONTENT. بشكل افتراضي، عند استخدام Aspose.Pdf لإنشاء جدول جديد، فإنه يستخدم [column_adjustment](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties) مع قيمة "مخصص". في مقتطف الشفرة التالي، نقوم بتعيين معلمات الكائن [MarginInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) وكائنات [BorderInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderinfo/) في الجدول. اختبر المثال وقيم النتيجة.


```python

    import aspose.pdf as ap

    # إنشاء كائن Pdf باستدعاء منشئه الفارغ
    doc = ap.Document()
    # إنشاء القسم في كائن Pdf
    sec1 = doc.pages.add()
    # إنشاء كائن جدول
    tab1 = ap.Table()
    # إضافة الجدول في مجموعة الفقرات للقسم المطلوب
    sec1.paragraphs.add(tab1)
    # تعيين عرض الأعمدة للجدول
    tab1.column_widths = "50 50 50"
    tab1.column_adjustment = ap.ColumnAdjustment.AUTO_FIT_TO_WINDOW
    # تعيين الحدود الافتراضية للخلية باستخدام كائن BorderInfo
    tab1.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.1)
    # تعيين حدود الجدول باستخدام كائن BorderInfo مخصص آخر
    tab1.border = ap.BorderInfo(ap.BorderSide.ALL, 1)
    # إنشاء كائن MarginInfo وتعيين هوامشه اليسرى والسفلية واليمنى والعلوية
    margin = ap.MarginInfo()
    margin.top = 5
    margin.left = 5
    margin.right = 5
    margin.bottom = 5
    # تعيين الحشو الافتراضي للخلية إلى كائن MarginInfo
    tab1.default_cell_padding = margin
    # إنشاء صفوف في الجدول ثم خلايا في الصفوف
    row1 = tab1.rows.add()
    row1.cells.add("col1")
    row1.cells.add("col2")
    row1.cells.add("col3")
    row2 = tab1.rows.add()
    row2.cells.add("item1")
    row2.cells.add("item2")
    row2.cells.add("item3")
    # حفظ المستند المحدّث الذي يحتوي على كائن الجدول
    doc.save(output_file)
```

### الحصول على عرض الجدول

في بعض الأحيان، من المطلوب الحصول على عرض الجدول ديناميكيًا. تحتوي فئة Aspose.PDF.Table على طريقة [get_width()](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#methods) لهذا الغرض. على سبيل المثال، لم تقم بتعيين عرض أعمدة الجدول بشكل صريح وقمت بتعيين [column_adjustment](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties) إلى 'AUTO_FIT_TO_CONTENT'. في هذه الحالة يمكنك الحصول على عرض الجدول كما يلي.

```python

    import aspose.pdf as ap

    # إنشاء مستند جديد
    doc = ap.Document()
    # إضافة صفحة في المستند
    page = doc.pages.add()
    # تهيئة جدول جديد
    table = ap.Table()
    table.column_adjustment = ap.ColumnAdjustment.AUTO_FIT_TO_CONTENT
    # إضافة صف في الجدول
    row = table.rows.add()
    # إضافة خلية في الجدول
    cell = row.cells.add("Cell 1 text")
    cell = row.cells.add("Cell 2 text")
    # الحصول على عرض الجدول
    print(table.get_width())
```

## إضافة صورة SVG إلى خلية الجدول

يوفر Aspose.PDF لـ Python عبر .NET القدرة على إدراج خلايا الجدول في ملف PDF.
 عند إنشاء جدول، يمكنك تضمين النصوص والصور داخل هذه الخلايا. بالإضافة إلى ذلك، توفر واجهة برمجة التطبيقات الوظيفة لتحويل ملفات SVG إلى تنسيق PDF. من خلال الاستفادة من هذه الوظائف معًا، يمكنك تحميل صورة SVG ووضعها داخل خلية جدول.

يعرض المقتطف التالي من الشيفرة عملية إنشاء كائن جدول وتضمين صورة SVG داخل إحدى خلاياه.

```python

    import aspose.pdf as ap

    # إنشاء كائن مستند
    doc = ap.Document()
    # إنشاء مثيل صورة
    img = ap.Image()
    # ضبط نوع الصورة كـ SVG
    img.file_type = ap.ImageFileType.SVG
    # المسار إلى الملف المصدر
    img.file = DIR_INPUT_TABLE + "SVGToPDF.svg"
    # ضبط العرض لمثيل الصورة
    img.fix_width = 50
    # ضبط الارتفاع لمثيل الصورة
    img.fix_height = 50
    # إنشاء مثيل جدول
    table = ap.Table()
    # ضبط العرض لخلايا الجدول
    table.column_widths = "100 100"
    # إنشاء كائن صف وإضافته إلى مثيل الجدول
    row = table.rows.add()
    # إنشاء كائن خلية وإضافته إلى مثيل الصف
    cell = row.cells.add()
    # إضافة نص إلى مجموعة الفقرات لكائن الخلية
    cell.paragraphs.add(ap.text.TextFragment("الخليّة الأولى"))
    # إضافة خلية أخرى إلى كائن الصف
    cell = row.cells.add()
    # إضافة صورة SVG إلى مجموعة الفقرات لمثيل الخلية المضاف حديثًا
    cell.paragraphs.add(img)
    # إنشاء كائن صفحة وإضافته إلى مجموعة الصفحات لمثيل المستند
    page = doc.pages.add()
    # إضافة الجدول إلى مجموعة الفقرات لكائن الصفحة
    page.paragraphs.add(table)
    # حفظ ملف PDF
    doc.save(output_file)
```

## إدراج فاصل صفحات بين صفوف الجدول

افتراضيًا، عندما تقوم بإنشاء جدول داخل ملف PDF، سيمتد الجدول عبر صفحات متعددة إذا تجاوز الحد السفلي للجدول. ومع ذلك، هناك حالات نحتاج فيها إلى فرض فواصل صفحات بعد إضافة عدد معين من الصفوف إلى الجدول. يوضح المقتطف التالي من الكود عملية إدراج فاصل صفحات عندما يتم تضمين 10 صفوف في الجدول.

```python

    import aspose.pdf as ap

    # إنشاء مثيل لوثيقة
    doc = ap.Document()
    # إضافة صفحة إلى مجموعة صفحات ملف PDF
    doc.pages.add()
    # إنشاء مثيل للجدول
    tab = ap.Table()
    # تعيين نمط الحدود للجدول
    tab.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)
    # تعيين نمط الحدود الافتراضي للجدول بلون الحدود أحمر
    tab.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)
    # تحديد عرض أعمدة الجدول
    tab.column_widths = "100 100"
    # إنشاء حلقة لإضافة 200 صف للجدول
    for counter in range(0, 201):
        row = ap.Row()
        tab.rows.add(row)
        cell1 = ap.Cell()
        cell1.paragraphs.add(ap.text.TextFragment("Cell " + str(counter) + ", 0"))
        row.cells.add(cell1)
        cell2 = ap.Cell()
        cell2.paragraphs.add(ap.text.TextFragment("Cell " + str(counter) + ", 1"))
        row.cells.add(cell2)
        # عندما يتم إضافة 10 صفوف، يتم عرض صف جديد في صفحة جديدة
        if counter % 10 == 0 and counter != 0:
            row.is_in_new_page = True
    # إضافة الجدول إلى مجموعة الفقرات في ملف PDF
    doc.pages[1].paragraphs.add(tab)
    # حفظ وثيقة PDF
    doc.save(output_file)
```


## عرض جدول في صفحة جديدة

افتراضيًا، يتم إضافة الفقرات إلى مجموعة الفقرات الخاصة بكائن الصفحة. ومع ذلك، من الممكن عرض جدول في صفحة جديدة بدلاً من مباشرة بعد الكائن الفقري المضاف سابقًا في الصفحة.

### مثال: كيفية عرض جدول في صفحة جديدة باستخدام بايثون

لعرض جدول في صفحة جديدة، استخدم الخاصية [is_in_new_page](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties) في فئة [BaseParagraph](https://reference.aspose.com/pdf/python-net/aspose.pdf/baseparagraph/). يظهر مقتطف الشيفرة التالي كيفية ذلك.

```python

    import aspose.pdf as ap

    doc = ap.Document()
    page_info = doc.page_info
    margin_info = page_info.margin

    margin_info.left = 37
    margin_info.right = 37
    margin_info.top = 37
    margin_info.bottom = 37

    page_info.is_landscape = True

    table = ap.Table()
    table.column_widths = "50 100"
    # تمت إضافة الصفحة.
    cur_page = doc.pages.add()
    for i in range(1, 121):
        row = table.rows.add()
        row.fixed_row_height = 15
        cell1 = row.cells.add()
        cell1.paragraphs.add(ap.text.TextFragment("Content 1"))
        cell2 = row.cells.add()
        cell2.paragraphs.add(ap.text.TextFragment("HHHHH"))
    paragraphs = cur_page.paragraphs
    paragraphs.add(table)

    table1 = ap.Table()
    table1.column_widths = "100 100"
    for i in range(1, 11):
        row = table1.rows.add()
        cell1 = row.cells.add()
        cell1.paragraphs.add(ap.text.TextFragment("LAAAAAAA"))
        cell2 = row.cells.add()
        cell2.paragraphs.add(ap.text.TextFragment("LAAGGGGGG"))
    table1.is_in_new_page = True
    # أريد الاحتفاظ بالجدول 1 للصفحة التالية من فضلك...
    paragraphs.add(table1)
    doc.save(output_file)
```


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python via .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "مكتبة معالجة PDF لـ Python عبر .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/example.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>