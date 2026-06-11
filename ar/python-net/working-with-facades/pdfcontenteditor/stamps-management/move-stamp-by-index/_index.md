---
title: نقل الطابع حسب الفهرس
linktitle: نقل الطابع حسب الفهرس
type: docs
weight: 90
url: /ar/python-net/move-stamp-by-index/
description: كيفية إعادة وضع التعليقات التوضيحية للختم المطاطي في ملف PDF باستخدام فهرسها على صفحة باستخدام Aspose.PDF لـ Python
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: انقل الطوابع المطاطية في ملف PDF باستخدام تحديد المواقع المستند إلى الفهرس
Abstract: يوضح هذا المثال كيفية إعادة وضع التعليقات التوضيحية للختم المطاطي في ملف PDF باستخدام فهرسها على صفحة باستخدام Aspose.PDF لـ Python عبر واجهة برمجة تطبيقات الواجهات. ويسلط الضوء على إنشاء طوابع متعددة وإعدادها لعمليات الحركة.
---

في تحرير PDF، قد يكون من الضروري ضبط موضع الطوابع المطاطية الموجودة. يوضح مقتطف الشفرة هذا كيفية:

- أضف طوابع متعددة على نفس الصفحة
- قم بإعدادهم لإعادة التموضع باستخدام الفهرس الخاص بهم
- يمكنك نقل الطابع اختياريًا من خلال تحديد الصفحة والفهرس والإحداثيات الجديدة

يمكن لطريقة «move_stamp (page_number، stamp_index، new_x، new_y)» إعادة وضع الطوابع بدقة.

1. قم بإنشاء [محرر محتوى PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) كائن.
1. قم بربط PDF بالمحرر.
1. أضف طوابع مطاطية متعددة إلى الصفحة.
1. احفظ المستند قبل تنفيذ عمليات الحركة.
1. انقل طابعًا محددًا بواسطة الفهرس الخاص به.
1. احفظ ملف PDF المحدث.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def move_stamp_by_index(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    content_editor.create_rubber_stamp(
        2,
        apd.Rectangle(200, 380, 180, 60),
        "Draft",
        "Draft stamp for ID-based operations",
        apd.Color.orange,
    )

    content_editor.create_rubber_stamp(
        2,
        apd.Rectangle(200, 480, 180, 60),
        "Draft",
        "Draft stamp for ID-based operations",
        apd.Color.orange,
    )
    content_editor.save(outfile)

    # Move first stamp on page 1 by index
    # content_editor.move_stamp(1, 1, 10, 10)
    # Save updated document
    content_editor.save(outfile)
```    
