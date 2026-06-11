---
title: احصل على إشارات PDF المرجعية وقم بتحديثها وتوسيعها في Python
linktitle: احصل على إشارة مرجعية وقم بتحديثها وتوسيعها
type: docs
weight: 20
url: /ar/python-net/get-update-and-expand-bookmark/
description: تعرف على كيفية استرداد الإشارات المرجعية وتحديثها وتوسيعها في مستندات PDF باستخدام Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية استخدام الإشارات المرجعية في PDF باستخدام Python
Abstract: توفر هذه المقالة دليلًا شاملاً حول إدارة الإشارات المرجعية داخل مستند PDF باستخدام مكتبة Aspose.PDF في Python. يبدأ بشرح كيفية استرداد الإشارات المرجعية من ملف PDF من خلال «OutlineCollection»، الذي يحتوي على جميع الإشارات المرجعية، وتفاصيل الوصول إلى سمات الإشارات المرجعية عبر «OutlineItemCollection». ثم تصف المقالة عملية تحديد رقم الصفحة المرتبط بإشارة مرجعية باستخدام `PDFBookMarketEditor`. كما يشرح كيفية التعامل مع هياكل الإشارات المرجعية الهرمية عن طريق استرداد الإشارات المرجعية الفرعية داخل كل `outlineItemCollection`. كما يغطي تحديث خصائص الإشارات المرجعية، ويوضح كيفية تعديل سمات الإشارات المرجعية وحفظ التغييرات في PDF. أخيرًا، تتناول المقالة متطلبات توسيع الإشارات المرجعية عند عرض مستند، مع توضيح كيفية تعيين حالة الفتح لكل إشارة مرجعية لضمان توسيعها افتراضيًا. ترافق مقتطفات التعليمات البرمجية كل قسم، وتقدم أمثلة عملية لتنفيذ هذه الوظائف.
---

## احصل على الإشارات المرجعية

ال [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) الكائنات [مجموعة الخطوط العريضة](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) تحتوي المجموعة على جميع الإشارات المرجعية لملف PDF. تشرح هذه المقالة كيفية الحصول على إشارات مرجعية من ملف PDF، وكيفية الحصول على الصفحة التي توجد بها إشارة مرجعية معينة.

للحصول على الإشارات المرجعية، قم بالتمرير عبر [مجموعة الخطوط العريضة](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) المجموعة واحصل على كل إشارة مرجعية في مجموعة OutlineItemCollection. ال [مجموعة عناصر المخطط التفصيلي](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) يوفر الوصول إلى جميع سمات الإشارة المرجعية. يوضح لك مقتطف الشفرة التالي كيفية الحصول على إشارات مرجعية من ملف PDF.

```python
from os import path
import sys
import aspose.pdf as ap

def get_bookmarks(input_pdf):
    document = ap.Document(input_pdf)
    for i in range(len(document.outlines)):
        outline_item = document.outlines[i + 1]
        print(outline_item.title)
        print(outline_item.italic)
        print(outline_item.bold)
        print(outline_item.color)
```

## الحصول على رقم صفحة إشارة مرجعية

بمجرد إضافة إشارة مرجعية، يمكنك معرفة الصفحة الموجودة عليها من خلال الحصول على رقم صفحة الوجهة المرتبط بكائن Bookmark.

```python
from os import path
import sys
import aspose.pdf as ap

def get_bookmark_page_number(input_pdf):
    # Create PdfBookmarkEditor
    bookmark_editor = ap.facades.PdfBookmarkEditor()
    # Open PDF file
    bookmark_editor.bind_pdf(input_pdf)
    # Extract bookmarks
    bookmarks = bookmark_editor.extract_bookmarks()
    for bookmark in bookmarks:
        str_level_separator = ""
        for i in range(bookmark.level):
            str_level_separator += "----"

        print(str_level_separator, "Title:", bookmark.title)
        print(str_level_separator, "Page Number:", bookmark.page_number)
        print(str_level_separator, "Page Action:", bookmark.action)
```

## احصل على إشارات مرجعية للأطفال من مستند PDF

يمكن تنظيم الإشارات المرجعية في هيكل هرمي مع الآباء والأطفال. للحصول على جميع الإشارات المرجعية، قم بتكرار مجموعات الخطوط العريضة لكائن المستند. ومع ذلك، للحصول على إشارات مرجعية للأطفال أيضًا، قم أيضًا بتكرار جميع الإشارات المرجعية في كل منها [مجموعة عناصر المخطط التفصيلي](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) تم الحصول على الكائن في الحلقة الأولى. توضح مقتطفات التعليمات البرمجية التالية كيفية الحصول على إشارات مرجعية للأطفال من مستند PDF.

```python
from os import path
import sys
import aspose.pdf as ap

def get_child_bookmarks(input_pdf):
    document = ap.Document(input_pdf)
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
                child_outline_item = outline_item[j + 1]
                print(child_outline_item.title)
                print(child_outline_item.italic)
                print(child_outline_item.bold)
                print(child_outline_item.color)
```

## تحديث الإشارات المرجعية في وثيقة PDF

لتحديث إشارة مرجعية في ملف PDF، أولاً، احصل على إشارة مرجعية معينة من مجموعة OutlineCollection الخاصة بكائن المستند عن طريق تحديد فهرس الإشارة المرجعية. بمجرد استرداد الإشارة المرجعية إلى [مجموعة عناصر المخطط التفصيلي](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) الكائن، يمكنك تحديث خصائصه ثم حفظ ملف PDF المحدث باستخدام طريقة الحفظ. توضح مقتطفات التعليمات البرمجية التالية كيفية تحديث الإشارات المرجعية في مستند PDF.

```python
from os import path
import sys
import aspose.pdf as ap

def update_bookmarks(input_pdf, output_pdf):
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

## الإشارات المرجعية الموسعة عند عرض المستند

يتم الاحتفاظ بالإشارات المرجعية في كائنات المستند [مجموعة عناصر المخطط التفصيلي](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) المجموعة، نفسها في [مجموعة الخطوط العريضة](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) مجموعة. ومع ذلك، قد يكون لدينا شرط لتوسيع جميع الإشارات المرجعية عند عرض ملف PDF.

من أجل تحقيق هذا المطلب، يمكننا تعيين حالة الفتح لكل عنصر مخطط/إشارة مرجعية على أنه مفتوح. يوضح لك مقتطف الشفرة التالي كيفية تعيين حالة الفتح لكل إشارة مرجعية كما تم توسيعها في مستند PDF.

```python
from os import path
import sys
import aspose.pdf as ap

def expanded_bookmarks(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    document.page_mode = ap.PageMode.USE_OUTLINES
    for i in range(len(document.outlines)):
        item = document.outlines[i + 1]
        item.open = True
    document.save(output_pdf)
```

## موضوعات الإشارات المرجعية ذات الصلة

- [العمل مع إشارات PDF المرجعية في Python](/pdf/ar/python-net/bookmarks/)
- [إضافة وحذف إشارات PDF المرجعية في Python](/pdf/ar/python-net/add-and-delete-bookmark/)
- [التنقل والتفاعل في PDF باستخدام Python](/pdf/ar/python-net/navigation-and-interaction/)

