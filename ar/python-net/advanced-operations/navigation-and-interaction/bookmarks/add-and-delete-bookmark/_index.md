---
title: إضافة وحذف إشارات مرجعية باستخدام بايثون
linktitle: إضافة وحذف إشارات مرجعية
type: docs
weight: 10
url: /ar/python-net/add-and-delete-bookmark/
description: يمكنك إضافة إشارة مرجعية إلى مستند PDF باستخدام بايثون. من الممكن حذف جميع الإشارات المرجعية أو إشارة مرجعية معينة من مستند PDF.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية إضافة وإزالة الإشارات المرجعية باستخدام بايثون
Abstract: توفر هذه المقالة تعليمات شاملة حول إدارة الإشارات المرجعية في مستندات PDF باستخدام مكتبة Aspose.PDF للبايثون. توضح عمليات إضافة وتعديل وحذف الإشارات المرجعية داخل ملف PDF. تبدأ المقالة بدليل لإضافة إشارة مرجعية عن طريق إنشاء كائن `OutlineItemCollection` وإضافته إلى `OutlineCollection` الخاص بالمستند. تتضمن أمثلة شفرة توضح إنشاء وإضافة كل من الإشارات المرجعية الأصلية والفرعية، مبرزة العلاقة الهرمية. بالإضافة إلى ذلك، تغطي المقالة طرق حذف جميع الإشارات المرجعية أو إشارة مرجعية معينة حسب العنوان. يحتوي كل قسم على مقتطفات شفرة بايثون لتوضيح العمليات، مما يضمن تمكّن القرّاء من تنفيذ الوظائف الموصوفة بسهولة في مهام تعديل ملفات PDF.
---

## إضافة إشارة مرجعية إلى مستند PDF

تُحفظ الإشارات المرجعية في مجموعة [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) الخاصة بكائن Document، والتي بدورها في مجموعة [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/).

لإضافة إشارة مرجعية إلى ملف PDF:

1. افتح مستند PDF باستخدام كائن [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. أنشئ إشارة مرجعية وحدد خصائصها.
1. أضف مجموعة [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) إلى مجموعة Outlines.

يوضح المقتطف البرمجي التالي كيفية إضافة إشارة مرجعية في مستند PDF.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Create a bookmark object
    outline = ap.OutlineItemCollection(document.outlines)
    outline.title = "Test Bookmark"
    outline.italic = True
    outline.bold = True
    # Set the destination page number
    outline.action = ap.annotations.GoToAction(document.pages[1])
    # Add bookmark in the document's outline collection.
    document.outlines.append(outline)

    # Save output
    document.save(output_pdf)
```

## إضافة إشارة مرجعية فرعية إلى مستند PDF

يمكن تجميع الإشارات المرجعية، مما يدل على علاقة هرمية بين الإشارات الأصلية والفرعية. توضح هذه المقالة كيفية إضافة إشارة مرجعية فرعية، أي إشارة مرجعية من المستوى الثاني، إلى ملف PDF.

لإضافة إشارة مرجعية فرعية إلى ملف PDF، أضف أولاً إشارة مرجعية أصلية:

1. افتح مستندًا.
1. أضف إشارة مرجعية إلى [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/)، مع تحديد خصائصها.
1. أضف مجموعة OutlineItemCollection إلى مجموعة [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) الخاصة بكائن Document.

يتم إنشاء الإشارة المرجعية الفرعية بنفس طريقة الإشارة الأصلية المذكورة أعلاه، لكنها تُضاف إلى مجموعة Outlines الخاصة بالإشارة الأصلية.

تُظهر مقتطفات الشفرة التالية كيفية إضافة إشارة مرجعية فرعية إلى مستند PDF.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Create a parent bookmark object
    outline = ap.OutlineItemCollection(document.outlines)
    outline.title = "Parent Outline"
    outline.italic = True
    outline.bold = True

    # Create a child bookmark object
    childOutline = ap.OutlineItemCollection(document.outlines)
    childOutline.title = "Child Outline"
    childOutline.italic = True
    childOutline.bold = True

    # Add child bookmark in parent bookmark's collection
    outline.append(childOutline)
    # Add parent bookmark in the document's outline collection.
    document.outlines.append(outline)

    # Save output
    document.save(output_pdf)
```

## حذف جميع الإشارات المرجعية من مستند PDF

تُحفظ جميع الإشارات المرجعية في ملف PDF ضمن مجموعة [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/). توضح هذه المقالة كيفية حذف جميع الإشارات المرجعية من ملف PDF.

لحذف جميع الإشارات المرجعية من ملف PDF:

1. استدعِ طريقة Delete الخاصة بمجموعة [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/).
1. احفظ الملف المعدل باستخدام طريقة [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) لكائن [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

تُظهر مقتطفات الشفرة التالية كيفية حذف جميع الإشارات المرجعية من مستند PDF.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Delete all bookmarks
    document.outlines.delete()

    # Save updated file
    document.save(output_pdf)

```

## حذف إشارة مرجعية معينة من مستند PDF

لحذف إشارة مرجعية معينة من ملف PDF:

1. مرّر عنوان الإشارة المرجعية كمعامل إلى طريقة Delete الخاصة بمجموعة [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/).
1. ثم احفظ الملف المحدّث باستخدام طريقة Save لكائن Document.

توفر فئة [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) مجموعة [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/). تزيل طريقة [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/#methods) أي إشارة مرجعية بالعنوان الممرّر إلى الطريقة.

تُظهر مقتطفات الشفرة التالية كيفية حذف إشارة مرجعية معينة من مستند PDF.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Delete particular outline by Title
    document.outlines.delete("Child Outline")

    # Save updated file
    document.save(output_pdf)
```


