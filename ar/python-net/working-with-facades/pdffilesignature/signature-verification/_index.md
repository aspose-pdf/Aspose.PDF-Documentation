---
title: التحقق من التوقيع
linktitle: التحقق من التوقيع
type: docs
weight: 90
url: /ar/python-net/signature-verification/
description: تعرف على كيفية التحقق من التوقيعات الرقمية والتحقق مما إذا كان PDF يحتوي على توقيعات باستخدام PDFfileSignature في Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تحقق من توقيعات PDF في Python
Abstract: توضح هذه المقالة كيفية التحقق من التوقيعات الرقمية في مستندات PDF باستخدام Aspose.PDF لـ Python عبر .NET. يوضح كيفية التحقق من صحة التوقيع الحالي وكيفية التحقق مما إذا كان PDF يحتوي على أي توقيعات.
---

يوفر Aspose.PDF لبيثون عبر .NET [توقيع ملف PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) واجهة للتحقق من مستندات PDF الموقعة. بعد توقيع PDF، يمكنك استخدامه لتأكيد صحة التوقيع واكتشاف ما إذا كان المستند يحتوي على أية إدخالات توقيع.

يوضح هذا المثال مهمتي تحقق شائعتين:

1. تحقق من صحة توقيع PDF الحالي.
1. تحقق مما إذا كان PDF يحتوي على أية توقيعات.

## تحقق من توقيع PDF

استخدم `verify_signature()` عندما تحتاج إلى التحقق من صحة توقيع معين في المستند. يقوم المثال بحل اسم التوقيع الأول المتاح والتحقق مما إذا كان هذا التوقيع صالحًا.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def verify_pdf_signature(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        is_valid = pdf_signature.verify_signature(sign_name)
        print(f"Signature '{sign_name}' is valid: {is_valid}")
    finally:
        pdf_signature.close()
```

## تحقق مما إذا كان PDF يحتوي على توقيعات

استخدم `contains_signature()` عندما تحتاج فقط إلى معرفة ما إذا كان ملف PDF يتضمن أي توقيعات على الإطلاق. يعد هذا مفيدًا كفحص سريع قبل تشغيل منطق التحقق أو الاستخراج الأكثر تفصيلاً.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def check_if_pdf_contains_signatures(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        contains_signatures = pdf_signature.contains_signature()
        print(f"PDF contains signatures: {contains_signatures}")
    finally:
        pdf_signature.close()
```
