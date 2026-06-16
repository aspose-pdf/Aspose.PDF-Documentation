---
title: إدارة حقوق الاستخدام
linktitle: إدارة حقوق الاستخدام
type: docs
weight: 100
url: /ar/python-net/usage-rights-management/
description: تعرف على كيفية اكتشاف حقوق الاستخدام وإزالتها من مستندات PDF باستخدام PDFFileSignature في Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إزالة حقوق استخدام PDF في Python
Abstract: توضح هذه المقالة كيفية فحص حقوق الاستخدام وإزالتها من مستندات PDF باستخدام Aspose.PDF لـ Python عبر .NET. يوضح كيفية التحقق مما إذا كان PDF يحتوي على حقوق الاستخدام وكيفية حفظ إصدار جديد من المستند بعد إزالة هذه الحقوق.
---

يوفر Aspose.PDF لبيثون عبر .NET [توقيع ملف PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) واجهة للعمل مع ملفات PDF الموقعة وإعدادات حقوق الاستخدام ذات الصلة. في بعض عمليات سير العمل، قد تحتاج إلى فحص ما إذا كان المستند يحتوي على حقوق الاستخدام وإزالتها قبل حفظ إصدار محدث من الملف.

يوضح هذا المثال إحدى مهام إدارة حقوق الاستخدام الشائعة:

1. تحقق مما إذا كان PDF يحتوي على حقوق الاستخدام.
1. قم بإزالة حقوق الاستخدام من المستند.
1. احفظ ملف PDF المحدث.

## تحقق مما إذا كان PDF يحتوي على حقوق الاستخدام

قبل إزالة حقوق الاستخدام، يتحقق المثال من الحالة الحالية للمستند عن طريق الاتصال `contains_usage_rights()`. يتيح لك ذلك تأكيد ما إذا كانت حقوق الاستخدام موجودة قبل إجراء التغييرات.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def check_usage_rights(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        had_usage_rights = pdf_signature.contains_usage_rights()
        print(f"PDF contains usage rights: {had_usage_rights}")
    finally:
        pdf_signature.close()
```

## قم بإزالة حقوق الاستخدام من PDF

استخدم `remove_usage_rights()` عندما لا يجب أن يحتفظ المستند بإعدادات حقوق الاستخدام الحالية. يتحقق المثال من الحالة الأولية ويزيل الحقوق ويحفظ PDF المحدث إلى ملف جديد.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def remove_usage_rights(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        had_usage_rights = pdf_signature.contains_usage_rights()
        print(f"PDF contains usage rights before removal: {had_usage_rights}")
        pdf_signature.remove_usage_rights()
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```
