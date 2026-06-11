---
title: قم بإنشاء ختم مطاطي مع تيار المظهر
linktitle: قم بإنشاء ختم مطاطي مع تيار المظهر
type: docs
weight: 30
url: /ar/python-net/create-rubber-stamp-with-appearance-stream/
description: يقوم هذا المثال بتحميل ملف PDF وإنشاء ختم مطاطي على الصفحة 1 باستخدام ملف صورة لمظهره وحفظ المستند المعدل. ✨
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بإنشاء ختم مطاطي بمظهر مخصص للصورة باستخدام PDFContentEditor في Python
Abstract: يوضح هذا المثال كيفية إنشاء تعليق توضيحي لختم مطاطي بمظهر صورة مخصص في ملف PDF باستخدام Aspose.PDF لـ Python عبر واجهة برمجة تطبيقات الواجهات. يتيح لك هذا الأسلوب تطبيق الطوابع ذات العلامات التجارية أو الغنية بصريًا مثل الشعارات أو الأختام أو التوقيعات.
---

يمكن تخصيص التعليقات التوضيحية للختم المطاطي باستخدام ملف صورة خارجي. بدلاً من الاعتماد فقط على الطوابع النصية، يمكنك تحديد المظهر المرئي (على سبيل المثال، شعار الشركة أو شارة الموافقة) ووضعه على الصفحة.

1. قم بإنشاء [محرر محتوى PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) مثال.
1. قم بربط وثيقة PDF المدخلة.
1. حدد مستطيلًا لموقع الختم.
1. استخدم ملف صورة كمظهر الختم.
1. قم بتطبيق إعدادات النص واللون.
1. احفظ مستند PDF المحدث.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_rubber_stamp_with_appearance_file(infile, image_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Create rubber stamp using appearance_file overload (image path)
    content_editor.create_rubber_stamp(
        1,
        apd.Rectangle(100, 400, 200, 60),
        "Stamp with custom appearance",
        apd.Color.dark_green,
        image_file,
    )
    # Save updated document
    content_editor.save(outfile)
```    
