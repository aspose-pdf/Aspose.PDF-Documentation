---
title: فئة توقيع ملف PDF
linktitle: فئة توقيع ملف PDF
type: docs
weight: 60
url: /ar/python-net/pdffilesignature-class/
description: استكشف كيفية إضافة التوقيعات الرقمية والتحقق منها وإزالتها من مستندات PDF في Python باستخدام فئة PDFfileSignature مع Aspose.PDF.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

- [توقيع PDF](/pdf/ar/python-net/pdf-signing/)
- [شهادة PDF](/pdf/ar/python-net/pdf-certification/)
- [إدارة التوقيع](/pdf/ar/python-net/signature-management/)
- [التحقق من التوقيع](/pdf/ar/python-net/signature-verification/)
- [معلومات التوقيع](/pdf/ar/python-net/signature-information/)
- [عمليات التحقق من سلامة التوقيع](/pdf/ar/python-net/signature-integrity-checks/)
- [المراجعة والأذونات](/pdf/ar/python-net/revision-permissions/)
- [استخراج التوقيع](/pdf/ar/python-net/signature-extraction/)
- [إدارة حقوق الاستخدام](/pdf/ar/python-net/usage-rights-management/)

## إعداد مساعدي التوقيع الرقمي بصيغة PDF

قبل تطبيق التوقيع الرقمي على PDF، من الأفضل إعداد مجموعة من الوظائف المساعدة القابلة لإعادة الاستخدام. تتضمن هذه الوظائف المهام الشائعة - مثل تهيئة معالج التوقيع، وتحديد الموضع المرئي للتوقيع، وتكوين التوقيع المستند إلى الشهادة - بحيث يظل منطق التوقيع الرئيسي نظيفًا ومتسقًا وسهل الصيانة.

### ما يحققه هذا الإعداد

تقوم هذه الطبقة المساعدة بإعداد كل ما يلزم لسير عمل التوقيع السلس:

- يقوم بتهيئة كائن PDFfileSignature ويربطه بمستند
- يحدد المكان الذي سيظهر فيه التوقيع على الصفحة
- يقوم بتحميل وتطبيق شهادة التوقيع
- يقوم بإنشاء كائن توقيع PKCS #7 قابل لإعادة الاستخدام مع البيانات الوصفية
- يقوم بتخصيص كيفية ظهور التوقيع بشكل مرئي

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
