---
title: معالجة مستند PDF في بايثون عبر .NET
linktitle: معالجة مستند PDF
type: docs
weight: 20
url: /ar/python-net/manipulate-pdf-document/
description: تحتوي هذه المقالة على معلومات حول كيفية التحقق من صحة مستند PDF وفقًا لمعيار PDF A باستخدام بايثون، وكيفية العمل مع جدول المحتويات، وكيفية ضبط تاريخ انتهاء صلاحية PDF، وما إلى ذلك.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: دليل لتعديل مستندات PDF باستخدام بايثون
Abstract: توفر هذه المقالة دليلًا شاملًا حول تعديل مستندات PDF باستخدام بايثون، وتحديدًا باستخدام مكتبة Aspose.PDF. تغطي المقالة عدة وظائف، بما في ذلك التحقق من صحة مستندات PDF للامتثال لمعياري PDF/A-1a و PDF/A-1b باستخدام طريقة `validate` في فئة `Document`. كما توضح كيفية إضافة وتخصيص وإدارة جدول المحتويات (TOC) في ملفات PDF، مثل ضبط أنواع مختلفة من TabLeaderTypes، وإخفاء أرقام الصفحات، وتخصيص ترقيم الصفحات ببادئة. بالإضافة إلى ذلك، تشرح المقالة كيفية ضبط تاريخ انتهاء صلاحيّة مستند PDF عن طريق تضمين JavaScript للحد من الوصول، وكيفية تسوية النماذج القابلة للملء في PDF لجعلها غير قابلة للتحرير. كل قسم مصحوب بمقاطع شفرة توضح تنفيذ هذه الميزات باستخدام Aspose.PDF في بايثون.
---

## معالجة مستند PDF في بايثون

## التحقق من صحة مستند PDF وفقًا لمعيار PDF A (A 1A و A 1B)

للتحقق من صحة مستند PDF لتوافق PDF/A-1a أو PDF/A-1b، استخدم فئة [المستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) وطريقة [التحقق](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods). تسمح لك هذه الطريقة بتحديد اسم الملف الذي سيتم حفظ النتيجة فيه ونوع التحقق المطلوب من تعداد PdfFormat: PDF_A_1A أو PDF_A_1B.

يعرض المقتطف البرمجي التالي كيفية التحقق من صحة مستند PDF لتوافق PDF/A-1A.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Validate PDF for PDF/A-1a
    document.validate(output_xml, ap.PdfFormat.PDF_A_1A)
```

يعرض المقتطف البرمجي التالي كيفية التحقق من صحة مستند PDF لتوافق PDF/A-1b.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Validate PDF for PDF/A-1a
    document.validate(output_xml, ap.PdfFormat.PDF_A_1B)
```

## العمل مع جدول المحتويات

### إضافة جدول المحتويات إلى PDF موجود

يشير TOC في PDF إلى "جدول المحتويات". وهو ميزة تتيح للمستخدمين التنقل بسرعة عبر المستند من خلال توفير نظرة عامة على أقسامه وعناوينه.

لإضافة جدول المحتويات إلى ملف PDF موجود، استخدم فئة Heading في مساحة الاسم [aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/). يمكن لمساحة الاسم [aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/) إنشاء ملفات PDF جديدة ومعالجة الملفات الموجودة. لإضافة جدول المحتويات إلى PDF موجود، استخدم مساحة الاسم Aspose.Pdf. يعرض المقتطف البرمجي التالي كيفية إنشاء جدول محتويات داخل ملف PDF موجود باستخدام بايثون عبر .NET.

```python

    import aspose.pdf as ap

    # Load an existing PDF files
    doc = ap.Document(input_pdf)

    # Get access to first page of PDF file
    tocPage = doc.pages.insert(1)

    # Create object to represent TOC information
    tocInfo = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD

    # Set the title for TOC
    tocInfo.title = title
    tocPage.toc_info = tocInfo

    # Create string objects which will be used as TOC elements
    titles = ["First page", "Second page", "Third page", "Fourth page"]
    for i in range(0, 2):
        # Create Heading object
        heading2 = ap.Heading(1)
        segment2 = ap.text.TextSegment()
        heading2.toc_page = tocPage
        heading2.segments.append(segment2)

        # Specify the destination page for heading object
        heading2.destination_page = doc.pages[i + 2]

        # Destination page
        heading2.top = doc.pages[i + 2].rect.height

        # Destination coordinate
        segment2.text = titles[i]

        # Add heading to page containing TOC
        tocPage.paragraphs.add(heading2)

    # Save the updated document
    doc.save(output_pdf)
```

### ضبط TabLeaderType مختلفة لمستويات جدول المحتويات المختلفة

تتيح Aspose.PDF للبايثون أيضًا ضبط TabLeaderType مختلفة لمستويات جدول المحتويات المختلفة. تحتاج إلى تعيين خاصية [line_dash](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) في فئة [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/).

```python

    import aspose.pdf as ap

    doc = ap.Document()
    tocPage = doc.pages.add()
    toc_info = ap.TocInfo()

    # set LeaderType
    toc_info.line_dash = ap.text.TabLeaderType.SOLID
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 30
    toc_info.title = title

    # Add the list section to the sections collection of the Pdf document
    tocPage.toc_info = toc_info
    # Define the format of the four levels list by setting the left margins
    # and
    # text format settings of each level

    toc_info.format_array_length = 4
    toc_info.format_array[0].margin.left = 0
    toc_info.format_array[0].margin.right = 30
    toc_info.format_array[0].line_dash = ap.text.TabLeaderType.DOT
    toc_info.format_array[0].text_state.font_style = ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    toc_info.format_array[1].margin.left = 10
    toc_info.format_array[1].margin.right = 30
    toc_info.format_array[1].line_dash = 3
    toc_info.format_array[1].text_state.font_size = 10
    toc_info.format_array[2].margin.left = 20
    toc_info.format_array[2].margin.right = 30
    toc_info.format_array[2].text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.format_array[3].line_dash = ap.text.TabLeaderType.SOLID
    toc_info.format_array[3].margin.left = 30
    toc_info.format_array[3].margin.right = 30
    toc_info.format_array[3].text_state.font_style = ap.text.FontStyles.BOLD

    # Create a section in the Pdf document
    page = doc.pages.add()

    # Add four headings in the section
    for Level in range(1, 5):
        heading2 = ap.Heading(Level)
        segment2 = ap.text.TextSegment()
        heading2.segments.append(segment2)
        heading2.is_auto_sequence = True
        heading2.toc_page = tocPage
        segment2.text = "Sample Heading" + str(Level)
        heading2.text_state.font = ap.text.FontRepository.find_font("Arial")

        # Add the heading into Table Of Contents.
        heading2.is_in_list = True
        page.paragraphs.add(heading2)

    # save the Pdf
    doc.save(output_pdf)
```

### إخفاء أرقام الصفحات في جدول المحتويات

في حال عدم رغبتك في عرض أرقام الصفحات مع العناوين في جدول المحتويات، يمكنك تعيين خاصية [is_show_page_numbers](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) في فئة [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) إلى false. يرجى مراجعة المقتطف البرمجي التالي لإخفاء أرقام الصفحات في جدول المحتويات:

```python

    import aspose.pdf as ap

    doc = ap.Document()
    toc_page = doc.pages.add()
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.title = title
    # Add the list section to the sections collection of the Pdf document
    toc_page.toc_info = toc_info
    # Define the format of the four levels list by setting the left margins and
    # text format settings of each level

    toc_info.is_show_page_numbers = False
    toc_info.format_array_length = 4
    toc_info.format_array[0].margin.right = 0
    toc_info.format_array[0].text_state.font_style = ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    toc_info.format_array[1].margin.left = 30
    toc_info.format_array[1].text_state.underline = True
    toc_info.format_array[1].text_state.font_size = 10
    toc_info.format_array[2].text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.format_array[3].text_state.font_style = ap.text.FontStyles.BOLD
    page = doc.pages.add()
    # Add four headings in the section
    for Level in range(1, 5):
        heading2 = ap.Heading(Level)
        segment2 = ap.text.TextSegment()
        heading2.toc_page = toc_page
        heading2.segments.append(segment2)
        heading2.is_auto_sequence = True
        segment2.text = "this is heading of level " + str(Level)
        heading2.is_in_list = True
        page.paragraphs.add(heading2)
    doc.save(output_pdf)

```

### تخصيص أرقام الصفحات أثناء إضافة جدول المحتويات

من الشائع تخصيص ترقيم الصفحات في جدول المحتويات أثناء إضافته إلى مستند PDF. على سبيل المثال، قد نحتاج إلى إضافة بادئة قبل رقم الصفحة مثل P1، P2، P3 وما إلى ذلك. في هذه الحالة، توفر Aspose.PDF للبايثون خاصية [page_numbers_prefix](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) في فئة [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) التي يمكن استخدامها لتخصيص أرقام الصفحات كما هو موضح في عينة الشفرة التالية.

```python

    import aspose.pdf as ap

    # Load an existing PDF files
    doc = ap.Document(input_pdf)
    # Get access to first page of PDF file
    toc_page = doc.pages.insert(1)
    # Create object to represent TOC information
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    # Set the title for TOC
    toc_info.title = title
    toc_info.page_numbers_prefix = "P"
    toc_page.toc_info = toc_info
    for i in range(len(doc.pages)):
        # Create Heading object
        heading2 = ap.Heading(1)
        segment2 = ap.text.TextSegment()
        heading2.toc_page = toc_page
        heading2.segments.append(segment2)
        # Specify the destination page for heading object
        heading2.destination_page = doc.pages[i + 1]
        # Destination page
        heading2.top = doc.pages[i + 1].rect.height
        # Destination coordinate
        segment2.text = "Page " + str(i)
        # Add heading to page containing TOC
        toc_page.paragraphs.add(heading2)

    # Save the updated document
    doc.save(output_pdf)

```

## كيفية ضبط تاريخ انتهاء صلاحية PDF

نُطبّق صلاحيات الوصول على ملفات PDF بحيث يمكن لمجموعة معينة من المستخدمين الوصول إلى ميزات/كائنات محددة في مستندات PDF. لتقييد الوصول إلى ملف PDF، عادةً ما نُطبق تشفيرًا وقد نحتاج إلى ضبط تاريخ انتهاء صلاحية ملف PDF، بحيث يتلقى المستخدم الذي يفتح/يعرض المستند تنبيهًا صالحًا بشأن انتهاء صلاحية ملف PDF.

```python

    import aspose.pdf as ap

    # Instantiate Document object
    doc = ap.Document()
    # Add page to pages collection of PDF file
    doc.pages.add()
    # Add text fragment to paragraphs collection of page object
    doc.pages[1].paragraphs.add(ap.text.TextFragment("Hello World..."))
    # Create JavaScript object to set PDF expiry date
    javaScript = ap.annotations.JavascriptAction(
        "var year=2017;"
        + "var month=5;"
        + "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());"
        + "expiry = new Date(year, month);"
        + "if (today.getTime() > expiry.getTime())"
        + "app.alert('The file is expired. You need a new one.');"
    )
    # Set JavaScript as PDF open action
    doc.open_action = javaScript

    # Save PDF Document
    doc.save(output_pdf)
```

## تسوية PDF القابل للملء في بايثون

غالبًا ما تتضمن مستندات PDF نماذجًا ذات عناصر تفاعلية قابلة للملء مثل أزرار الاختيار، مربعات الفحص، مربعات النص، القوائم، إلخ. لجعلها غير قابلة للتحرير لأغراض تطبيقية مختلفة، نحتاج إلى تسوية ملف PDF.
توفر Aspose.PDF دالة لتسوية ملف PDF الخاص بك في بايثون ببضع أسطر من الشيفرة فقط:

```python

    import aspose.pdf as ap

    # Load source PDF form
    doc = ap.Document(input_pdf)

    # Flatten Flatten Fillable PDF
    if len(doc.form.fields) > 0:
        for item in doc.form.fields:
            item.flatten()

    # Save the updated document
    doc.save(output_pdf)
```


