---
title: استخراج التوقيع
linktitle: استخراج التوقيع
type: docs
weight: 50
url: /ar/python-net/signature-extraction/
description: تعرف على كيفية استخراج صورة التوقيع وشهادة التوقيع من ملف PDF موقّع باستخدام PDFfileSignature في Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: استخراج صورة التوقيع والشهادة من PDF في Python
Abstract: تشرح هذه المقالة كيفية استخراج البيانات المتعلقة بالتوقيع من مستندات PDF الموقعة باستخدام Aspose.PDF لـ Python عبر .NET. ويعرض كيفية قراءة أول توقيع متاح وتصدير صورته وحفظ دفق الشهادة المرتبط إلى ملف الإخراج.
---

يوفر Aspose.PDF لبيثون عبر .NET [توقيع ملف PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) واجهة لفحص واستخراج البيانات من مستندات PDF الموقعة. بعد توقيع PDF، يمكنك استخدامه لتصدير موارد التوقيع مثل صورة التوقيع المرئي والشهادة المرتبطة بالتوقيع.

يوضح هذا المثال مهمتي استخراج شائعتين:

1. استخرج الصورة المرئية المرتبطة بالتوقيع.
1. استخرج شهادة التوقيع من ملف PDF موقّع.

## استخراج صورة توقيع

استخدم هذه الطريقة عندما يحتوي PDF على توقيع مرئي وتريد تصدير بيانات الصورة الخاصة به. يفتح المثال المستند الموقّع، ويحصل على أول اسم توقيع متاح، ويستخرج دفق الصور، ويكتبه إلى ملف.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def extract_signature_image(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signature_image = pdf_signature.extract_image(sign_name)
        write_stream_data(signature_image, outfile)
    finally:
        pdf_signature.close()
```

## استخراج شهادة توقيع

استخدم `extract_certificate()` عندما تحتاج إلى بيانات الشهادة المرفقة بالتوقيع. هذا مفيد للتفتيش أو عمليات سير عمل التحقق أو تخزين شهادة الموقّع بشكل منفصل عن مستند PDF.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def extract_signature_certificate(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signature_certificate = pdf_signature.extract_certificate(sign_name)
        write_stream_data(signature_certificate, outfile)
    finally:
        pdf_signature.close()
```

