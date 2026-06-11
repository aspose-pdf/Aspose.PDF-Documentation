---
title: إدارة الختم حسب المعرف
linktitle: إدارة الختم حسب المعرف
type: docs
weight: 95
url: /ar/python-net/manage-stamp-by-id/
description: كيفية التعامل مع التعليقات التوضيحية للخواتم المطاطية في ملف PDF من خلال معرفاتها الفريدة باستخدام Aspose.PDF لـ Python
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إدارة الطوابع المطاطية حسب المعرف في ملف PDF باستخدام PDFContentEditor في Python
Abstract: يوضح هذا المثال كيفية التعامل مع التعليقات التوضيحية للختم المطاطي في ملف PDF من خلال معرفاتها الفريدة باستخدام Aspose.PDF لـ Python عبر واجهة برمجة تطبيقات الواجهات. يمكنك إخفاء أو إظهار طوابع محددة على صفحات معينة دون التأثير على الطوابع الأخرى.
---

في ملفات PDF ذات الطوابع المطاطية المتعددة، قد يكون من المفيد التحكم في الطوابع الفردية بناءً على المعرف الخاص بها. تسمح أساليب 'hide_stamp_by_id () 'و 'show_stamp_by_id ()' بالتحكم الانتقائي في الرؤية. يوضح هذا المثال كيفية:

- أضف طوابع متعددة بمعرفات فريدة
- إخفاء طابع على صفحة معينة
- عرض طابع على صفحة أخرى

باستخدام العمليات المستندة إلى المعرف، يمكنك تجنب تتبع الطوابع حسب موضع الصفحة أو السمات الأخرى.

1. قم بإنشاء [محرر محتوى PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) مثال.
1. قم بربط وثيقة PDF المدخلة.
1. أضف أختام مطاطية بمعرفات محددة.
1. قم بإخفاء الطوابع وإظهارها بناءً على معرفاتها وأرقام الصفحات.
1. احفظ مستند PDF المحدث.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def manage_stamp_by_id(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    content_editor.create_rubber_stamp(
        1,
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

    # Apply ID-based stamp operations
    content_editor.hide_stamp_by_id(1, 1)
    content_editor.show_stamp_by_id(1, 2)

    # Save updated document
    content_editor.save(outfile)
```
