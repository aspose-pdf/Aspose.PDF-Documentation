---
title: إدارة التوقيع
linktitle: إدارة التوقيع
type: docs
weight: 80
url: /ar/python-net/signature-management/
description: تعرف على كيفية إزالة التوقيعات الرقمية من مستندات PDF وتنظيف حقول التوقيع اختياريًا باستخدام PDFfileSignature في Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إزالة توقيعات PDF وتنظيف حقول التوقيع في Python
Abstract: تشرح هذه المقالة كيفية إدارة التوقيعات الرقمية الموجودة في مستندات PDF باستخدام Aspose.PDF لـ Python عبر .NET. يوضح كيفية إزالة توقيع من PDF وكيفية إزالة التوقيع مع حقل التوقيع المرتبط به.
---

يوفر Aspose.PDF لبيثون عبر .NET [توقيع ملف PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) واجهة للعمل مع التوقيعات الرقمية الموجودة في مستندات PDF. بالإضافة إلى قراءة التوقيعات والتحقق من صحتها، يمكنك أيضًا إزالتها عندما يتطلب سير العمل تحديث المحتوى الموقّع أو مسح حقل التوقيع.

يوضح هذا المثال مهمتين شائعتين لإدارة التوقيع:

1. قم بإزالة توقيع من وثيقة PDF.
1. قم بإزالة التوقيع وتنظيف حقل التوقيع المرتبط.

## إزالة توقيع من PDF

استخدم `remove_signature()` عندما تريد حذف التوقيع المحدد من المستند مع الحفاظ على بنية حقل التوقيع الأساسية في مكانها. يفتح المثال ملف PDF الموقّع، ويحل اسم التوقيع، ويزيله، ويحفظ ملف الإخراج المحدث.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def remove_signature_from_pdf(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        pdf_signature.remove_signature(sign_name)
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```

## قم بإزالة التوقيع وتنظيف الحقل

استخدم التحميل الزائد مع الإضافات `True` ضع علامة عندما تريد إزالة التوقيع وكذلك تنظيف حقل التوقيع ذي الصلة. يكون هذا مفيدًا عندما لا يجب أن يظل الحقل في المستند بعد حذف التوقيع.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def remove_signature_with_field_cleanup(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        pdf_signature.remove_signature(sign_name, True)
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```
