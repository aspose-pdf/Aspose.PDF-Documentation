---
title: إنشاء ختم مطاطي مع ملف المظهر
linktitle: إنشاء ختم مطاطي مع ملف المظهر
type: docs
weight: 20
url: /ar/python-net/create-rubber-stamp-with-appearance-file/
description: يقوم المثال بربط ملف PDF للإدخال، وإنشاء ختم مطاطي على الصفحة 1 باستخدام ملف صورة كمظهر الختم، وحفظ ملف PDF المحدث.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بإنشاء ختم مطاطي بمظهر مخصص في ملف PDF باستخدام PDFContentEditor
Abstract: يوضح هذا المثال كيفية إضافة تعليق توضيحي لختم مطاطي بمظهر مخصص (صورة) إلى مستند PDF باستخدام Aspose.PDF لـ Python عبر واجهة برمجة تطبيقات الواجهات. تسمح لك الطوابع المخصصة بتضمين الشعارات أو التوقيعات أو المرئيات ذات العلامات التجارية كجزء من الطابع.
---

يمكن تخصيص التعليقات التوضيحية للختم المطاطي ليس فقط بالنص ولكن أيضًا باستخدام ملف صورة كمظهر لها. هذا الأسلوب مفيد لإضافة شعارات الشركة أو طوابع التوقيع أو أي مؤشر مرئي إلى صفحات PDF الخاصة بك.

1. قم بإنشاء [محرر محتوى PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) مثال.
1. قم بربط وثيقة PDF المدخلة.
1. حدد مستطيلًا للختم.
1. استخدم ملف صورة مخصص لتحديد مظهر الختم المطاطي.
1. قم بتعيين نص ولون الطابع.
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
