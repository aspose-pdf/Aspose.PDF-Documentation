---
title: نقل الطابع حسب الهوية
linktitle: نقل الطابع حسب الهوية
type: docs
weight: 80
url: /ar/python-net/move-stamp-by-id-example/
description: في هذا المثال، تتم إضافة ختم مطاطي إلى الصفحة 1 ثم نقله إلى موضع جديد باستخدام المعرف الخاص به قبل حفظ المستند المحدث.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: انقل ختمًا مطاطيًا حسب المعرف في ملف PDF باستخدام PDFContentEditor في Python
Abstract: يوضح هذا المثال كيفية إعادة وضع تعليق توضيحي لختم مطاطي موجود في ملف PDF باستخدام Aspose.PDF لـ Python عبر واجهة برمجة تطبيقات الواجهات. يوضح كيفية إنشاء طابع ثم نقله برمجيًا باستخدام معرفه.
---

بعد إضافة تعليق توضيحي بختم مطاطي إلى PDF، قد تحتاج إلى ضبط موضعه. تسمح لك طريقة 'move_stamp_by_id () 'بنقل الطابع بناءً على معرفه، دون إعادة إنشائه. هذا مفيد في عمليات سير العمل الآلية حيث يجب تعديل موضع الطوابع ديناميكيًا.

1. قم بإنشاء [محرر محتوى PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) مثال.
1. قم بربط وثيقة PDF المدخلة.
1. أضف تعليقًا توضيحيًا بختم مطاطي.
1. انقل الطابع باستخدام المعرف الخاص به.
1. احفظ مستند PDF المحدث.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def move_stamp_by_id_example(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    content_editor.create_rubber_stamp(
        1,
        apd.Rectangle(300, 420, 180, 60),
        "Approved",
        "Move this stamp by ID",
        apd.Color.green,
    )

    # Move stamp by ID overload
    content_editor.move_stamp_by_id(1, 1, 240, 360)

    # Save updated document
    content_editor.save(outfile)
```    
