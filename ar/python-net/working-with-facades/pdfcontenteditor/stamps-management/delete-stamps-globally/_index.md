---
title: حذف الطوابع عالميًا
linktitle: حذف الطوابع عالميًا
type: docs
weight: 60
url: /ar/python-net/delete-stamps-globally/
description: يوضح هذا المثال كيفية حذف التعليقات التوضيحية للختم المطاطي عالميًا عبر جميع الصفحات في ملف PDF باستخدام Aspose.PDF لـ Python عبر واجهة برمجة تطبيقات الواجهات. يوضح كيفية إزالة الطوابع حسب المعرف دون تحديد صفحات فردية.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: احذف الطوابع المطاطية عالميًا في ملف PDF باستخدام PDFContentEditor في Python
Abstract: يوضح هذا المثال كيفية حذف التعليقات التوضيحية للختم المطاطي عالميًا عبر جميع الصفحات في ملف PDF باستخدام Aspose.PDF لـ Python عبر واجهة برمجة تطبيقات الواجهات. يوضح كيفية إزالة الطوابع حسب المعرف دون تحديد صفحات فردية.
---

عند العمل مع صفحات متعددة، قد تحتاج إلى إزالة طوابع معينة في المستند بأكمله. تسمح لك أساليب 'delete_stamp_by_id () 'و 'delete_stamp_by_ids ()' بحذف الطوابع عالميًا من خلال معرفاتها، مما يلغي الحاجة إلى التكرار من خلال كل صفحة يدويًا.

1. قم بإنشاء [محرر محتوى PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) مثال.
1. قم بربط وثيقة PDF المدخلة.
1. أضف أختام مطاطية إلى صفحات متعددة.
1. احذف الطوابع عالميًا باستخدام معرفاتها.
1. احفظ مستند PDF المحدث.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def delete_stamps_globally(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    # Add stamps across multiple pages so global deletion is meaningful
    for page in range(1, 5):
        content_editor.create_rubber_stamp(
            page,
            apd.Rectangle(120, 500, 180, 60),
            "Draft",
            "Stamp for global deletion",
            apd.Color.gray,
        )

    # delete_stamp_by_id without page number removes stamp ID from all pages
    content_editor.delete_stamp_by_id(1)
    # delete_stamp_by_ids without page number removes a list of IDs from all pages
    content_editor.delete_stamp_by_ids([2, 3])

    # Save updated document
    content_editor.save(outfile)
```
