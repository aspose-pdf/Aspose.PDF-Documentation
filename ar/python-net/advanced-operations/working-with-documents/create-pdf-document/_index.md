---
title: إنشاء ملفات PDF في بايثون
linktitle: إنشاء مستند PDF
type: docs
weight: 10
url: /ar/python-net/create-pdf-document/
description: تعرف على كيفية إنشاء ملفات PDF وإنشاء ملفات PDF قابلة للبحث في Python باستخدام Aspose.PDF لـ Python عبر .NET.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إنشاء ملف PDF باستخدام بايثون
Abstract: Aspose.PDF لـ Python عبر .NET هي واجهة برمجة تطبيقات متعددة الاستخدامات مصممة للمطورين لمعالجة ملفات PDF داخل تطبيقات Python التي تستهدف إطار عمل .NET. إنه يمكّن المستخدمين من إنشاء مستندات PDF وتحميلها وتعديلها وتحويلها دون عناء. توفر هذه المقالة دليلًا خطوة بخطوة لإنشاء ملف PDF بسيط باستخدام Aspose.PDF. تتضمن العملية تهيئة كائن «المستند»، وإضافة «صفحة» إلى المستند، وإدراج «TextFragment» في فقرات الصفحة، وحفظ الملف كملف PDF. يوضح مقتطف شفرة Python المضمن هذه الخطوات من خلال إنشاء مستند PDF يحتوي على النص «Hello World!». تعمل واجهة برمجة التطبيقات هذه على تبسيط معالجة PDF بأقل قدر من التعليمات البرمجية، مما يعزز الإنتاجية للمطورين الذين يعملون مع ملفات PDF في بيئات .NET.
---

**Aspose.pdf لـ Python عبر .NET** عبارة عن واجهة برمجة تطبيقات لمعالجة ملفات PDF تسمح للمطورين بإنشاء ملفات PDF وتحميلها وتعديلها وتحويلها مباشرة من Python لتطبيقات .NET ببضعة أسطر من التعليمات البرمجية.

استخدم هذه الأمثلة عندما تحتاج إلى إنشاء ملفات PDF جديدة من البداية أو تحويل إخراج OCR إلى مستندات PDF قابلة للبحث في Python.

## كيفية إنشاء ملف PDF بسيط

لإنشاء ملف PDF باستخدام Python عبر .NET مع Aspose.PDF، يمكنك اتباع الخطوات التالية:

1. قم بإنشاء كائن من [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) صنف
1. إضافة [صفحة](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) الاعتراض على [صفحات](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) مجموعة من كائن المستند
1. أضِف [جزء من النص](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) إلى [فقرات](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) مجموعة من الصفحة
1. احفظ مستند PDF الناتج

```python
import sys
from os import path
import aspose.pdf as ap

def create_new_document(output_pdf):
    """Create a simple PDF with a single “Hello World!” page."""
    document = ap.Document()
    page = document.pages.add()
    page.paragraphs.add(ap.text.TextFragment("Hello World!"))
    document.save(output_pdf)
```

## كيفية إنشاء مستند PDF قابل للبحث

يسمح Aspose.PDF لـ Python عبر .NET بإنشاء مستندات PDF الموجودة ومعالجتها. عند إضافة عناصر نصية إلى ملف PDF، يكون ملف PDF الناتج قابلاً للبحث. ومع ذلك، عند تحويل صورة تحتوي على نص إلى ملف PDF، لا يمكن البحث عن محتويات PDF الناتجة. وكحل بديل، يمكننا تطبيق OCR على الملف الناتج بحيث يصبح قابلاً للبحث.

فيما يلي الكود الكامل لإنجاز هذا المطلب:

1. قم بتحميل ملف PDF باستخدام «AP.document».
1. قم بتكوين دقة العرض.
1. استخدم «PNGdevice.process» لتحويل صفحة PDF المحددة إلى صورة.
1. قم بتشغيل OCR على الصورة التي تم إنشاؤها.
1. قم بإنشاء ملف PDF جديد من إخراج OCR.
1. احفظ ملف PDF القابل للبحث.

```python
import aspose.pdf as ap
import io

# Requires: pip install pytesseract
# Also ensure the Tesseract OCR engine is installed and available on your system PATH.
import pytesseract
from pathlib import Path


# Path to the source PDF
input_pdf_path = "input.pdf"
# Path for the temporary image
temp_image_path = "temp_image.png"
# Path for the searchable PDF
output_pdf_path = "output_searchable.pdf"
page_number = 1
image_stream = io.FileIO(temp_image_path, "w")
try:
    document = ap.Document(input_pdf_path)
    resolution = ap.devices.Resolution(300)
    png_device = ap.devices.PngDevice(resolution)
    png_device.process(document.pages[page_number], image_stream)
    image_stream.close()
    pdf = pytesseract.image_to_pdf_or_hocr(temp_image_path, extension="pdf")
    document = ap.Document(io.BytesIO(pdf))
    document.save(output_pdf_path)
finally:
    image_file = Path(temp_image_path)
    image_file.unlink(missing_ok=True)
```

## موضوعات المستندات ذات الصلة

- [العمل مع مستندات PDF في بايثون](/pdf/ar/python-net/working-with-documents/)
- [تنسيق مستندات PDF في بايثون](/pdf/ar/python-net/formatting-pdf-document/)
- [معالجة مستندات PDF في Python](/pdf/ar/python-net/manipulate-pdf-document/)
- [تحسين ملفات PDF في بايثون](/pdf/ar/python-net/optimize-pdf/)

