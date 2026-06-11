---
title: قم بتوقيع مستندات PDF من بطاقة ذكية في Python
linktitle: توقيع PDF باستخدام البطاقة الذكية
type: docs
weight: 30
url: /ar/python-net/sign-pdf-document-from-smart-card/
description: تعرف على كيفية توقيع مستندات PDF باستخدام البطاقات الذكية والشهادات الخارجية في Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بتوقيع مستندات PDF من بطاقة ذكية باستخدام Python
Abstract: يشرح هذا الدليل كيفية توقيع مستندات PDF رقميًا باستخدام بطاقة ذكية باستخدام Aspose.PDF لـ Python عبر .NET. يوضح كيفية الوصول إلى الشهادات المخزنة على الأجهزة (مثل رموز USB أو البطاقات الذكية) من خلال Windows Certificate Store وتطبيقها لتوقيع ملفات PDF. تتضمن الوثائق أمثلة التعليمات البرمجية التي توضح كيفية تحديد موقع الشهادة المناسبة وتكوين خصائص التوقيع وتضمين التوقيع الرقمي في PDF. يتيح ذلك تسجيل الدخول الآمن والمدعوم بالأجهزة وفقًا لمعايير التوقيع الرقمي، وهو مناسب للمؤسسات ذات الثقة العالية وسير العمل القانوني.
---

يوفر Aspose.PDF إمكانات قوية لدمج مكونات التوقيع المرئي والتشفيري، مما يضمن كلاً من الأصالة والعرض الاحترافي في مستندات PDF الموقعة رقميًا.

استخدم سير العمل هذا عندما تعتمد عملية التوقيع على الشهادات المخزنة في الأجهزة المدعومة بالأجهزة مثل البطاقات الذكية أو رموز USB أو مخازن الشهادات المُدارة.

## قم بالتوقيع باستخدام البطاقة الذكية باستخدام حقل التوقيع

يوضح هذا المثال كيفية التوقيع رقميًا على مستند PDF باستخدام شهادة خارجية باستخدام Aspose.PDF لـ Python وتطبيق صورة مظهر توقيع مخصص:

1. فتح مستند PDF.
1. إنشاء كائن PDFfileSignature وربطه بالمستند.
1. استرداد شهادة رقمية محلية باستخدام طريقة مخصصة `get_local_certificate()`.
1. إعداد توقيع خارجي استنادًا إلى الشهادة المحددة.
1. تطبيق صورة مظهر التوقيع المخصص (على سبيل المثال، شعار الشركة أو التوقيع المكتوب بخط اليد).
1. التوقيع الرقمي على الصفحة الأولى من المستند باستخدام بيانات التعريف المحددة (السبب، جهة الاتصال، الموقع).
1. حفظ المستند الموقّع إلى ملف إخراج جديد.

تُعد هذه الطريقة مثالية للحالات التي يجب فيها تطبيق التوقيعات برمجيًا باستخدام الشهادات الخارجية - مثل الرموز المميزة للأجهزة أو مخازن الشهادات أو الموفرين الموثوق بهم - وتقديمها بتخطيط مرئي مخصص.

فيما يلي مقتطفات الشفرة لتوقيع مستند PDF من بطاقة ذكية:

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def sign_with_smart_card(infile: str, outfile: str, pngfile: str) -> None:
    """Sign a PDF document using a smart-card certificate."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature() as pdf_signature:
            pdf_signature.bind_pdf(document)
            external_signature = ap.forms.ExternalSignature(get_local_certificate())
            pdf_signature.signature_appearance = pngfile
            pdf_signature.sign(
                1,
                "Reason",
                "Contact",
                "Location",
                True,
                drawing.Rectangle(100, 100, 200, 200),
                external_signature,
            )
            pdf_signature.save(outfile)
```

## تحقق من التوقيعات الرقمية

يوضح مقتطف الشفرة هذا كيفية التحقق من التوقيعات الرقمية في مستند PDF باستخدام Aspose.PDF لـ Python:

1. فتح ملف PDF.
1. إنشاء «كائن PDFfileSignature» وربطه بالمستند.
1. استرداد قائمة بجميع أسماء حقول التوقيع باستخدام 'get_signature_names () '.
1. تكرار كل توقيع والتحقق من صلاحيته باستخدام 'verify_signature () '.
1. رفع الاستثناء في حالة فشل التحقق من أي توقيع.

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def verify_external_signature(infile: str) -> None:
    """Verify an external signature in a PDF document."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as pdf_signature:
            for signature_name in pdf_signature.get_signature_names(True):
                if not pdf_signature.verify_signature(signature_name):
                    raise Exception("Not verified")
```

## قم بالتوقيع باستخدام شهادة خارجية

يوضح مقتطف الشفرة هذا كيفية إضافة حقل توقيع رقمي وتوقيعه في مستند PDF باستخدام Aspose.PDF لـ Python مع شهادة خارجية:

1. فتح ملف PDF كتدفق ثنائي.
1. إنشاء SignatureField ووضعه على الصفحة الأولى من المستند في موضع محدد.
1. استرداد شهادة رقمية محلية باستخدام طريقة مخصصة `get_local_certificate()`.
1. إعداد توقيع خارجي باستخدام بيانات التعريف مثل السلطة والسبب ومعلومات الاتصال.
1. تعيين اسم حقل فريد لحقل التوقيع (partial_name = «sig1").
1. إضافة حقل التوقيع إلى حقول النموذج في PDF.
1. توقيع الحقل بالشهادة الخارجية.
1. حفظ المستند الموقّع إلى ملف إخراج.

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def get_signature_info_using_signature_field(infile: str, outfile: str) -> None:
    """Create a signature field and sign it with an external certificate."""
    with open(infile, "rb+") as file_stream:
        document = ap.Document(file_stream)
        signature_field = ap.forms.SignatureField(
            document.pages[1],
            ap.Rectangle(100, 400, 10, 10, True),
        )
        selected_certificate = get_local_certificate()
        external_signature = ap.forms.ExternalSignature(selected_certificate)
        external_signature.authority = "Me"
        external_signature.reason = "Reason"
        external_signature.contact_info = "Contact"
        signature_field.partial_name = "sig1"
        document.form.add(signature_field, 1)
        signature_field.sign(external_signature)
        document.save(outfile)
```

## موضوعات الأمان ذات الصلة

- [تأمين وتوقيع ملفات PDF في Python](/pdf/ar/python-net/securing-and-signing/)
- [قم بتوقيع ملفات PDF رقميًا في Python](/pdf/ar/python-net/digitally-sign-pdf-file/)
- [استخراج معلومات التوقيع من PDF في Python](/pdf/ar/python-net/extract-image-and-signature-information/)
- [تشفير وفك تشفير ملفات PDF في Python](/pdf/ar/python-net/set-privileges-encrypt-and-decrypt-pdf-file/)

