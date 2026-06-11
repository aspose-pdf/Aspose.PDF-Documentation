---
title: إضافة ختم مطاطي
linktitle: إضافة ختم مطاطي
type: docs
weight: 10
url: /ar/python-net/add-rubber-stamp/
description: يربط هذا المثال ملف PDF للإدخال، ويضيف ختمًا مطاطيًا أخضر «معتمدًا» إلى الصفحات الأربع الأولى، ويحفظ المستند المعدل.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: أضف تعليقًا توضيحيًا للختم المطاطي إلى ملف PDF باستخدام PDFContentEditor في Python
Abstract: يوضح هذا المثال كيفية إضافة تعليق توضيحي بختم مطاطي إلى مستند PDF باستخدام Aspose.PDF لـ Python عبر واجهة برمجة تطبيقات الواجهات. تسمح لك الطوابع المطاطية بوضع علامات مرئية على الصفحات باستخدام الموافقات أو المراجعات أو الملصقات المخصصة.
---

تُستخدم التعليقات التوضيحية للختم المطاطي بشكل شائع في ملفات PDF للإشارة إلى الموافقة أو حالة المراجعة أو الملاحظات الأخرى. استخدام [محرر محتوى PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)، يمكنك تحديد مستطيل للختم وتعيين نصه وتعليقاته واختيار لون وتطبيقه على صفحات متعددة من المستند.

1. قم بإنشاء مثيل محرر محتوى PDF.
1. قم بربط وثيقة PDF المدخلة.
1. تصفح الصفحات من 1 إلى 4.
1. أضف تعليقًا توضيحيًا بختم مطاطي يحتوي على نص مخصص وتعليقات ولون.
1. احفظ مستند PDF المحدث.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_rubber_stamp(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    for i in range(1, 5):
        content_editor.create_rubber_stamp(
            i,
            apd.Rectangle(120, 450, 180, 60),
            "Approved",
            "Approved by reviewer",
            apd.Color.green,
        )
    # Save updated document
    content_editor.save(outfile)
```
