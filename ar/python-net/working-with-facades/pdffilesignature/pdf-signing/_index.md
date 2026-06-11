---
title: توقيع مستندات PDF
linktitle: توقيع مستندات PDF
type: docs
weight: 10
url: /ar/python-net/pdf-signing/
description: تعرف على كيفية توقيع مستندات PDF في Python باستخدام PDFfileSignature مع التوقيعات الرقمية القائمة على الشهادات والمسماة والمرئية.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بتوقيع مستندات PDF باستخدام التوقيعات الرقمية في Python
Abstract: توضح هذه المقالة كيفية توقيع مستندات PDF باستخدام Aspose.PDF لبيثون عبر.NET باستخدام واجهة PDFfileSignature. وهي تغطي تكوين الشهادة والتوقيع باستخدام المعلمات الأساسية والتوقيع باستخدام كائن PKCS7 وتعيين اسم توقيع وتطبيق مظهر توقيع مرئي.
---

يوفر Aspose.PDF لبيثون عبر .NET [توقيع ملف PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) واجهة لتطبيق التوقيعات الرقمية على مستندات PDF الموجودة. باستخدام ملف الشهادة، يمكنك توقيع مستند برمجيًا، ووضع التوقيع على صفحة، وتعيين بيانات تعريف التوقيع، وتخصيص كيفية عرض التوقيع.

توضح هذه المقالة العديد من عمليات سير عمل التوقيع الشائعة:

1. إنشاء ملف وربطه `PdfFileSignature` كائن على ملف PDF المدخل.
1. قم بتكوين شهادة التوقيع.
1. قم بتطبيق توقيع رقمي على الصفحة المستهدفة.
1. قم بتعيين اسم توقيع ومظهر مرئي اختياريًا.
1. احفظ ملف PDF الموقّع.

## قم بإعداد أدوات مساعدة للتوقيع قابلة لإعادة الاستخدام

قبل تطبيق التوقيع الرقمي على PDF، من المفيد إعداد مجموعة صغيرة من الوظائف المساعدة القابلة لإعادة الاستخدام. يقوم هؤلاء المساعدون بتهيئة معالج التوقيع وتحديد منطقة التوقيع المرئية وتكوين الشهادة وإنشاء كائنات توقيع PKCS #7 القابلة لإعادة الاستخدام بحيث تظل أمثلة التوقيع أدناه قائمة بذاتها ويسهل متابعتها.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd


DEFAULT_CERTIFICATE_PASSWORD = "Aspose2021"
DEFAULT_SIGNATURE_NAME = "Signature1"


def create_pdf_file_signature(infile):
    pdf_signature = pdf_facades.PdfFileSignature()
    pdf_signature.bind_pdf(infile)
    return pdf_signature


def create_signature_rectangle():
    return apd.Rectangle(10, 10, 200, 60)


def configure_signature_certificate(
    pdf_signature, certificate_path, certificate_password=DEFAULT_CERTIFICATE_PASSWORD
):
    pdf_signature.set_certificate(certificate_path, certificate_password)


def create_pkcs7_signature(
    certificate_path, certificate_password=DEFAULT_CERTIFICATE_PASSWORD
):
    signature = ap.forms.PKCS7(certificate_path, certificate_password)
    signature.reason = "Document approval"
    signature.contact_info = "qa@example.com"
    signature.location = "New York, USA"
    signature.authority = "Aspose.PDF Example"
    return signature


def create_custom_signature_appearance():
    appearance = ap.forms.SignatureCustomAppearance()
    appearance.font_family_name = "Arial"
    appearance.font_size = 10
    appearance.show_contact_info = True
    appearance.show_location = True
    appearance.show_reason = True
    return appearance
```

## قم بتوقيع ملف PDF باستخدام معايير الشهادة الأساسية

يقوم هذا الأسلوب بتكوين الشهادة مباشرة على `PdfFileSignature` كائن. يكون مفيدًا عندما تريد تدفق توقيع مباشر مع بيانات تعريف التوقيع القياسية وعدم وجود إدارة منفصلة لكائن التوقيع.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def sign_pdf_with_basic_parameters(infile, outfile, certificate_path):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        configure_signature_certificate(pdf_signature, certificate_path)
        pdf_signature.sign(
            1,
            "Document approval",
            "qa@example.com",
            "New York, USA",
            False,
            create_signature_rectangle(),
        )
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```

## قم بتوقيع ملف PDF باستخدام كائن PKCS7

استخدم `PKCS7` الكائن عندما تحتاج إلى إعداد التوقيع أولاً ثم تمريره إلى مكالمة التوقيع. يمنحك هذا النمط مزيدًا من التحكم في إعدادات التوقيع وهو أساس جيد لمزيد من عمليات سير العمل المتقدمة.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def sign_pdf_with_certificate_object(infile, outfile, certificate_path):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        signature = create_pkcs7_signature(certificate_path)
        pdf_signature.sign(1, False, create_signature_rectangle(), signature)
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```

## قم بتوقيع ملف PDF بتوقيع مسمى

إذا كان سير عمل المستند يعتمد على اسم حقل توقيع محدد مسبقًا، فقم بتمرير هذا الاسم إلى `sign()`. هذا يجعل من السهل الرجوع إلى التوقيع لاحقًا للتحقق من الصحة أو المعالجة أو التكامل مع سير عمل الموافقة.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def sign_pdf_with_named_signature(infile, outfile, certificate_path):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        signature = create_pkcs7_signature(certificate_path)
        signature.reason = "Approved by signing workflow"
        pdf_signature.sign(
            1,
            DEFAULT_SIGNATURE_NAME,
            "Approved by signing workflow",
            "qa@example.com",
            "New York, USA",
            True,
            create_signature_rectangle(),
            signature,
        )
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```

## قم بتطبيق توقيع مرئي

يمكنك جعل التوقيع مرئيًا على صفحة PDF عن طريق تعيين مظهر مخصص لـ `PKCS7` كائن. يكون هذا مفيدًا عندما يجب أن يعرض مستند الإخراج تفاصيل الموافقة مثل السبب والموقع ومعلومات الاتصال للمستخدمين النهائيين.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def apply_visible_signature(infile, outfile, certificate_path):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        signature = create_pkcs7_signature(certificate_path)
        signature.reason = "Visible approval signature"
        signature.custom_appearance = create_custom_signature_appearance()
        pdf_signature.sign(
            1,
            "Visible approval signature",
            "qa@example.com",
            "New York, USA",
            True,
            create_signature_rectangle(),
            signature,
        )
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```
