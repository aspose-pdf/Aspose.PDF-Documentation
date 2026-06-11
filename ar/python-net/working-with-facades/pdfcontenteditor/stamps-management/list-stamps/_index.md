---
title: طوابع القوائم
linktitle: طوابع القوائم
type: docs
weight: 70
url: /ar/python-net/list-stamps/
description: يقوم هذا المثال بتحميل ملف PDF واسترداد جميع الطوابع من الصفحة 1 وطباعتها وعرض رسالة إذا لم يتم العثور على طوابع.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بإدراج التعليقات التوضيحية للختم المطاطي في ملف PDF باستخدام PDFContentEditor في Python
Abstract: يوضح هذا المثال كيفية استرداد التعليقات التوضيحية للخواتم المطاطية وإدراجها من مستند PDF باستخدام Aspose.PDF لـ Python عبر واجهة برمجة تطبيقات الواجهات. يوضح كيفية الوصول إلى الطوابع على صفحة معينة وعرض تفاصيلها.
---

عند العمل مع ملفات PDF المشروحة، قد تحتاج إلى فحص الأختام المطاطية الموجودة قبل تعديلها أو إزالتها. تسمح لك طريقة «get_stamps ()» باسترداد جميع الطوابع الموضوعة على صفحة معينة. يمكنك بعد ذلك تكرار النتائج ومعالجتها برمجيًا.

1. قم بإنشاء [محرر محتوى PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) مثال.
1. قم بربط وثيقة PDF المدخلة.
1. استرجع جميع الطوابع من الصفحة 1.
1. قم بالتكرار من خلال مجموعة الطوابع.
1. اطبع كل طابع.
1. اعرض رسالة في حالة عدم وجود طوابع.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def list_stamps(infile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # List all stamps on page 1
    stamps = content_editor.get_stamps(1)

    count = 0
    for stamp in stamps:
        count += 1
        print(f"Stamp {count}: {stamp}")

    if count == 0:
        print("No stamps found")
```
