---
title: إحضار، تحديث وتوسيع علامة مرجعية باستخدام بايثون
linktitle: إحضار، تحديث وتوسيع علامة مرجعية
type: docs
weight: 20
url: /ar/python-net/get-update-and-expand-bookmark/
description: يصف هذا المقال كيفية استخدام العلامات المرجعية في ملف PDF باستخدام مكتبة Aspose.PDF للبايثون الخاصة بنا.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية استخدام العلامات المرجعية في PDF باستخدام بايثون
Abstract: يوفر هذا المقال دليلًا شاملاً لإدارة العلامات المرجعية داخل مستند PDF باستخدام مكتبة Aspose.PDF في بايثون. يبدأ بشرح كيفية استرجاع العلامات المرجعية من ملف PDF عبر `OutlineCollection`، التي تحتوي على جميع العلامات المرجعية، ويُفصل طريقة الوصول إلى خصائص العلامة المرجعية عبر `OutlineItemCollection`. ثم يصف المقال عملية تحديد رقم الصفحة المرتبط بالعلامة المرجعية باستخدام `PdfBookmarkEditor`. كما يوضح كيفية التعامل مع هياكل العلامات المرجعية الهرمية عن طريق استرجاع العلامات المرجعية الفرعية داخل كل `OutlineItemCollection`. يغطي أيضًا تحديث خصائص العلامة المرجعية، موضحًا كيفية تعديل خصائصها وحفظ التغييرات إلى ملف PDF. أخيرًا، يتناول المقال الحاجة لتوسيع العلامات المرجعية عند عرض المستند، موضحًا كيفية تعيين حالة الفتح لكل علامة مرجعية لضمان توسعتها افتراضيًا. تصاحب كل قسم مقاطع شفرة برمجية تُقدم أمثلة عملية لتطبيق هذه الوظائف.
---

## الحصول على العلامات المرجعية

تحتوي مجموعة [المستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) كائن [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) على جميع علامات مرجعية ملف PDF. يشرح هذا المقال كيفية الحصول على العلامات المرجعية من ملف PDF، وكيفية معرفة الصفحة التي توجد عليها علامة مرجعية معينة.

للحصول على العلامات المرجعية، قم بالتكرار عبر مجموعة [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) واحصل على كل علامة مرجعية في OutlineItemCollection. توفر [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) الوصول إلى جميع خصائص العلامة المرجعية. يوضح مقطع الشفرة التالي كيفية الحصول على العلامات المرجعية من ملف PDF.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Loop through all the bookmarks
    for i in range(len(document.outlines)):
        outline_item = document.outlines[i + 1]
        print(outline_item.title)
        print(outline_item.italic)
        print(outline_item.bold)
        print(outline_item.color)
```

## الحصول على رقم صفحة العلامة المرجعية

بعد إضافة علامة مرجعية، يمكنك معرفة الصفحة التي توجد عليها عن طريق الحصول على رقم الصفحة (PageNumber) المرتبط بالهدف في كائن العلامة المرجعية.

```python

    import aspose.pdf as ap

    # Create PdfBookmarkEditor
    bookmarkEditor = ap.facades.PdfBookmarkEditor()
    # Open PDF file
    bookmarkEditor.bind_pdf(input_pdf)
    # Extract bookmarks
    bookmarks = bookmarkEditor.extract_bookmarks()
    for bookmark in bookmarks:
        str_level_seprator = ""
        for i in range(bookmark.level):
            str_level_seprator += "----"

        print(str_level_seprator, "Title:", bookmark.title)
        print(str_level_seprator, "Page Number:", bookmark.page_number)
        print(str_level_seprator, "Page Action:", bookmark.action)
```

## الحصول على العلامات المرجعية الفرعية من مستند PDF

يمكن تنظيم العلامات المرجعية في هيكل هرمي، مع الأبواب والأبناء. للحصول على جميع العلامات المرجعية، قم بالتكرار عبر مجموعات Outlines لكائن المستند. ومع ذلك، للحصول على العلامات المرجعية الفرعية أيضًا، قم بالتكرار عبر جميع العلامات المرجعية في كل كائن [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) الذي تم الحصول عليه في الحلقة الأولى. يوضح مقاطع الشفرة التالية كيفية الحصول على العلامات المرجعية الفرعية من مستند PDF.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Loop through all the bookmarks
    for i in range(len(document.outlines)):
        outline_item = document.outlines[i + 1]
        print(outline_item.title)
        print(outline_item.italic)
        print(outline_item.bold)
        print(outline_item.color)
        count = len(outline_item)
        if count > 0:
            print("Child Bookmarks")
            # There are child bookmarks then loop through that as well
            for j in range(len(outline_item)):
                child_outline_item = outline_item[i + 1]
                print(child_outline_item.title)
                print(child_outline_item.italic)
                print(child_outline_item.bold)
                print(child_outline_item.color)
```

## تحديث العلامات المرجعية في مستند PDF

لتحديث علامة مرجعية في ملف PDF، أولاً احصل على العلامة المرجعية المحددة من مجموعة OutlineColletion لكائن المستند عن طريق تحديد فهرس العلامة. بمجرد استرجاع العلامة المرجعية إلى كائن [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/)، يمكنك تحديث خصائصها ثم حفظ ملف PDF المحدث باستخدام طريقة Save. يوضح مقاطع الشفرة التالية كيفية تحديث العلامات المرجعية في مستند PDF.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Get a bookmark object
    outline = document.outlines[1]

    # Get child bookmark object
    child_outline = outline[1]
    child_outline.title = "Updated Outline"
    child_outline.italic = True
    child_outline.bold = True

    # Save output
    document.save(output_pdf)
```

## توسيع العلامات المرجعية عند عرض المستند

تُخزن العلامات المرجعية في مجموعة [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) لكائن المستند، والتي هي بدورها في مجموعة [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/). ومع ذلك، قد تكون لدينا حاجة لجعل جميع العلامات المرجعية موسعة عند عرض ملف PDF.

لتحقيق هذا المتطلب، يمكننا تعيين حالة الفتح لكل عنصر مخطط/علامة مرجعية كـ Open. يوضح مقطع الشفرة التالي كيفية تعيين حالة الفتح لكل علامة مرجعية لتكون موسعة في مستند PDF.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Set page view mode i.e. show thumbnails, full-screen, show attachment panel
    document.page_mode = ap.PageMode.USE_OUTLINES
    # Traverse through each Ouline item in outlines collection of PDF file
    for i in range(len(document.outlines)):
        item = document.outlines[i + 1]
        # Set open status for outline item
        item.open = True

    # Save output
    document.save(output_pdf)
```


