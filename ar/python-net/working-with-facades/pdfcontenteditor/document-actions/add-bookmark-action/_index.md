---
title: إضافة إجراء إشارة مرجعية
linktitle: إضافة إجراء إشارة مرجعية
type: docs
weight: 10
url: /ar/python-net/add-bookmark-action/
description: يقوم هذا المثال بربط ملف PDF مُدخل، وإنشاء إشارة مرجعية باسم «PDFContentEditor Bookmark» تنتقل إلى الصفحة 1، وتحفظ المستند المحدث.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بإنشاء إشارة مرجعية مع إجراء التنقل في ملف PDF باستخدام Python
Abstract: يوضح هذا المثال كيفية إضافة إشارة مرجعية مع إجراء التنقل إلى مستند PDF باستخدام Aspose.PDF لـ Python عبر واجهة برمجة تطبيقات الواجهات. ويعرض كيفية تكوين نص الإشارة المرجعية والمظهر والإجراء الذي يوجه المستخدمين إلى صفحة معينة.
---

توفر الإشارات المرجعية التنقل السريع داخل مستندات PDF. استخدام [محرر محتوى PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)، يمكنك إنشاء إشارات مرجعية برمجيًا وتعيين إجراءات مثل الانتقال إلى صفحة. يمكنك أيضًا تخصيص مظهر الإشارة المرجعية، بما في ذلك خيارات الألوان والنمط مثل الخط الغامق أو المائل.

1. قم بإنشاء كائن محرر محتوى PDF.
1. قم بربط ملف PDF المدخل.
1. حدد خصائص الإشارات المرجعية.
1. تعيين إجراء إشارة مرجعية.
1. احفظ المستند المحدث.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_bookmark_action(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add a bookmark action to navigate to page 1
    content_editor.create_bookmarks_action(
        "PdfContentEditor Bookmark",
        apd.Color.blue,
        True,
        False,
        "",
        "GoTo",
        "1",
    )
    # Save updated document
    content_editor.save(outfile)
```