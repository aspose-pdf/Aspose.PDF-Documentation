---
title: إضافة وحذف إشارات PDF المرجعية في Python
linktitle: إضافة إشارة مرجعية وحذفها
type: docs
weight: 10
url: /ar/python-net/add-and-delete-bookmark/
description: تعرف على كيفية إضافة الإشارات المرجعية وحذفها في مستندات PDF باستخدام Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية إضافة الإشارات المرجعية وإزالتها باستخدام Python
Abstract: توفر هذه المقالة إرشادات شاملة حول إدارة الإشارات المرجعية في مستندات PDF باستخدام مكتبة Aspose.PDF لـ Python. وهي تحدد عمليات إضافة وتعديل وحذف الإشارات المرجعية داخل PDF. تبدأ المقالة بدليل حول إضافة إشارة مرجعية عن طريق إنشاء كائن «OutlineItemCollection» وإلحاقه بـ «مجموعة الخطوط العريضة» الخاصة بالمستند. يتضمن أمثلة التعليمات البرمجية التي توضح إنشاء وإضافة الإشارات المرجعية لكل من الوالدين والطفل، مع إبراز العلاقة الهرمية. بالإضافة إلى ذلك، تتناول المقالة طرق حذف جميع الإشارات المرجعية أو إشارة مرجعية محددة حسب العنوان. يتضمن كل قسم مقتطفات شفرة Python لتوضيح العمليات، مما يضمن للقراء تنفيذ الوظائف الموصوفة بسهولة في مهام معالجة PDF الخاصة بهم.
---

## إضافة إشارة مرجعية إلى وثيقة PDF

يتم الاحتفاظ بالإشارات المرجعية في كائنات المستند [مجموعة عناصر المخطط التفصيلي](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) المجموعة، نفسها في [مجموعة الخطوط العريضة](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) مجموعة.

لإضافة إشارة مرجعية إلى PDF:

1. افتح مستند PDF باستخدام [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) كائن.
1. قم بإنشاء إشارة مرجعية وحدد خصائصها.
1. أضف [مجموعة عناصر المخطط التفصيلي](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) مجموعة إلى مجموعة الخطوط العريضة.

يوضح مقتطف الشفرة التالي كيفية إضافة إشارة مرجعية في مستند PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def add_bookmark(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Create a bookmark object
    pdf_outline = ap.OutlineItemCollection(document.outlines)
    pdf_outline.title = "Test Outline"
    pdf_outline.italic = True
    pdf_outline.bold = True

    # Set the destination page number
    pdf_outline.action = ap.annotations.GoToAction(document.pages[1])

    # Add bookmark to the document's outline collection
    outlines = document.outlines
    outlines.append(pdf_outline)

    # Save PDF document
    document.save(outfile)
```

## إضافة إشارة مرجعية للأطفال إلى مستند PDF

يمكن أن تتداخل الإشارات المرجعية، مما يشير إلى وجود علاقة هرمية مع الإشارات المرجعية للوالدين والأطفال. تشرح هذه المقالة كيفية إضافة إشارة مرجعية فرعية، أي إشارة مرجعية من المستوى الثاني، إلى PDF.

لإضافة إشارة مرجعية فرعية إلى ملف PDF، قم أولاً بإضافة إشارة مرجعية رئيسية:

1. افتح مستندًا.
1. إضافة إشارة مرجعية إلى [مجموعة عناصر المخطط التفصيلي](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/)، وتحديد خصائصها.
1. قم بإضافة مجموعة OutlineItemcollection إلى كائن المستند [مجموعة الخطوط العريضة](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) مجموعة.

يتم إنشاء الإشارة المرجعية الخاصة بالطفل تمامًا مثل الإشارة المرجعية الرئيسية الموضحة أعلاه، ولكن تتم إضافتها إلى مجموعة الخطوط العريضة للعلامة المرجعية الرئيسية

توضح مقتطفات التعليمات البرمجية التالية كيفية إضافة إشارة مرجعية فرعية إلى مستند PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def add_child_bookmark(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Create a parent bookmark object
    pdf_outline = ap.OutlineItemCollection(document.outlines)
    pdf_outline.title = "Parent Outline"
    pdf_outline.italic = True
    pdf_outline.bold = True

    # Create a child bookmark object
    pdf_child_outline = ap.OutlineItemCollection(document.outlines)
    pdf_child_outline.title = "Child Outline"
    pdf_child_outline.italic = True
    pdf_child_outline.bold = True

    # Add child bookmark to parent bookmark's collection
    pdf_outline.append(pdf_child_outline)

    # Add parent bookmark to the document's outline collection
    document.outlines.append(pdf_outline)

    # Save PDF document
    document.save(outfile)
```

## احذف جميع الإشارات المرجعية من مستند PDF

يتم الاحتفاظ بجميع الإشارات المرجعية في ملف PDF في [مجموعة الخطوط العريضة](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) مجموعة. توضح هذه المقالة كيفية حذف جميع الإشارات المرجعية من ملف PDF.

لحذف جميع الإشارات المرجعية من ملف PDF:

1. اتصل بـ [مجموعة الخطوط العريضة](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) طريقة حذف المجموعة.
1. احفظ الملف المعدل باستخدام [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) الكائنات [حفظ ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) طريقة.

توضح مقتطفات التعليمات البرمجية التالية كيفية حذف جميع الإشارات المرجعية من مستند PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def delete_bookmarks(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Delete all bookmarks in the PDF document
    document.outlines.delete()

    # Save PDF document
    document.save(outfile)
```

## حذف إشارة مرجعية معينة من وثيقة PDF

لحذف إشارة مرجعية معينة من ملف PDF:

1. قم بتمرير عنوان الإشارة المرجعية كمعامل إلى [مجموعة الخطوط العريضة](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) طريقة حذف المجموعة.
1. ثم احفظ الملف المحدث باستخدام طريقة حفظ كائن المستند.

ال [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) يوفر «الفصل» [مجموعة الخطوط العريضة](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) مجموعة. ال [حذف ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/#methods) تزيل الطريقة أي إشارة مرجعية مع تمرير العنوان إلى الطريقة.

توضح مقتطفات التعليمات البرمجية التالية كيفية حذف إشارة مرجعية معينة من مستند PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def delete_bookmark(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Delete a specific bookmark by title.
    # Note: If multiple bookmarks have the same title, only the first matching bookmark will be deleted.
    document.outlines.delete("Child Outline")

    # Save PDF document
    document.save(outfile)
```

## موضوعات الإشارات المرجعية ذات الصلة

- [العمل مع إشارات PDF المرجعية في Python](/pdf/ar/python-net/bookmarks/)
- [احصل على إشارات PDF المرجعية وقم بتحديثها وتوسيعها في Python](/pdf/ar/python-net/get-update-and-expand-bookmark/)
- [التنقل والتفاعل في PDF باستخدام Python](/pdf/ar/python-net/navigation-and-interaction/)

