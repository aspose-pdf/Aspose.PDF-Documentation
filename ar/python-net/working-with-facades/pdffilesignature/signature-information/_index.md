---
title: معلومات التوقيع
linktitle: معلومات التوقيع
type: docs
weight: 60
url: /ar/python-net/signature-information/
description: تعرف على كيفية قراءة أسماء التوقيعات وتفاصيل الموقّع والطوابع الزمنية والبيانات الوصفية للتوقيع من ملفات PDF الموقعة باستخدام PDFfileSignature في Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: اقرأ تفاصيل التوقيع من مستندات PDF في Python
Abstract: تشرح هذه المقالة كيفية فحص البيانات الوصفية للتوقيع في مستندات PDF الموقعة باستخدام Aspose.PDF لـ Python عبر .NET. يوضح كيفية إدراج أسماء التوقيع، وقراءة تفاصيل الموقّع، والحصول على تاريخ التوقيع ووقته، واستخراج سبب التوقيع وموقعه.
---

يوفر Aspose.PDF لبيثون عبر .NET [توقيع ملف PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) واجهة لفحص التوقيعات الرقمية في مستندات PDF. بعد توقيع المستند، يمكنك استخدامه لقراءة أسماء التوقيعات واسترداد البيانات الوصفية مثل اسم الموقّع ومعلومات جهة الاتصال ووقت التوقيع والسبب والموقع.

يوضح هذا المثال أربع مهام شائعة لمعلومات التوقيع:

1. قم بإدراج جميع أسماء التوقيعات في ملف PDF موقّع.
1. اقرأ تفاصيل الموقّع للتوقيع المحدد.
1. احصل على تاريخ التوقيع ووقته.
1. اقرأ سبب التوقيع وموقعه.

## احصل على أسماء التوقيعات

استخدم هذه الطريقة عندما يحتوي PDF على توقيع واحد أو أكثر وتريد فحص إدخالات التوقيع المتاحة. يفتح المثال المستند ويطبع القائمة التي تم إرجاعها بواسطة `get_sign_names()`.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_signature_names(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        signature_names = list_signature_names(pdf_signature)
        print(f"Signature Names: {signature_names}")
    finally:
        pdf_signature.close()
```

## احصل على تفاصيل الموقّع

بمجرد معرفة اسم التوقيع، يمكنك استرداد البيانات الوصفية الخاصة بالموقع. يقرأ هذا المثال اسم الموقّع ومعلومات جهة الاتصال لأول توقيع متاح في المستند.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_signer_details(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signer_name = pdf_signature.get_signer_name(sign_name)
        contact_info = pdf_signature.get_contact_info(sign_name)
        print(
            f"Signer Details for '{sign_name}': "
            f"signer_name={signer_name}, contact_info={contact_info}"
        )
    finally:
        pdf_signature.close()
```

## احصل على تاريخ التوقيع ووقته

استخدم `get_date_time()` لتحديد متى تم تطبيق توقيع معين. يعد هذا مفيدًا للتدقيق ولعرض محفوظات التوقيع في عمليات سير عمل المستند.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_signature_date_and_time(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signature_date = pdf_signature.get_date_time(sign_name)
        print(f"Signature Date and Time for '{sign_name}': {signature_date}")
    finally:
        pdf_signature.close()
```

## احصل على التوقيع والسبب والموقع

يمكن للتوقيعات الرقمية أيضًا تخزين البيانات الوصفية مثل سبب التوقيع والموقع. يسترجع هذا المثال كلا القيمتين للتوقيع المحدد ويطبعهما معًا.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_signature_reason_and_location(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signature_reason = pdf_signature.get_reason(sign_name)
        signature_location = pdf_signature.get_location(sign_name)
        print(
            f"Signature Reason and Location for '{sign_name}': "
            f"reason={signature_reason}, location={signature_location}"
        )
    finally:
        pdf_signature.close()
```

