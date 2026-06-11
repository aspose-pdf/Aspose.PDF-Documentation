---
title: إضافة توقيع رقمي أو توقيع PDF رقميًا في Python
linktitle: قم بتوقيع PDF رقميًا
type: docs
weight: 10
url: /ar/python-net/digitally-sign-pdf-file/
description: تعرف على كيفية توقيع مستندات PDF رقميًا وإضافة الطوابع الزمنية والتحقق من صحة التوقيعات في Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بتوقيع ملفات PDF رقميًا باستخدام Python
Abstract: يشرح هذا الدليل كيفية توقيع مستندات PDF رقميًا باستخدام Aspose.PDF لـ Python عبر .NET. ويعرض بالتفصيل عملية تطبيق التوقيعات الرقمية القياسية والمتقدمة، واستخدام الشهادات (PFX و PKCS #12)، وتخصيص مظهر التوقيع وسلوكه. تتضمن الوثائق أمثلة التعليمات البرمجية التي توضح كيفية توقيع ملفات PDF الحالية وإضافة الطوابع الزمنية والتحقق من صلاحية التوقيع. يتيح ذلك للمطورين ضمان أصالة المستند وتكامله والامتثال لمعايير التوقيع الرقمي في تطبيقات Python الخاصة بهم.
---

## قم بتوقيع PDF بالتوقيعات الرقمية

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def sign_document(infile: str, outfile: str, pfxfile: str) -> None:
    """Sign a PDF document with a PKCS#7 certificate."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            pkcs = ap.forms.PKCS7(pfxfile, "12345")
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)
            signature.save(outfile)
```

يضيف توقيع**PKCS #7 المنفصل** توقيعًا رقميًا إلى مستند دون تضمين المحتوى في كتلة التوقيع.

استخدم هذه الأمثلة عندما تحتاج إلى تطبيق التوقيعات المستندة إلى الشهادات على ملفات PDF أو التحقق من صحة التوقيع أو إضافة طوابع زمنية موثوقة إلى المستندات الموقعة.

يقوم المثال التالي بتوقيع وثيقة PDF باستخدام توقيع رقمي منفصل PKCS #7، وتطبيق التوقيع على الصفحة الأولى في منطقة مستطيلة محددة.

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def sign_document_PKCS7_detached(
    infile: str,
    outfile: str,
    pfxfile: str,
    password: str,
) -> None:
    """Sign a PDF document with a detached PKCS#7 certificate."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            pkcs = ap.forms.PKCS7Detached(
                pfxfile,
                password,
                ap.DigestHashAlgorithm.SHA256,
            )
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)
            signature.save(outfile)
```

** تحقق من جميع التوقيعات الرقمية في مستند PDF**

1. يقوم بإنشاء مثيل لـ PDFFileSignature يسمح لك بالتفاعل مع التوقيعات في PDF.
1. احصل على قائمة بأسماء التوقيعات `get_signature_names(True)`.
1. يتحقق من التوقيع الأول في القائمة `verify_signature` للامتثال للشهادة المحددة.

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def verify(infile: str) -> None:
    """Verify all digital signatures in a PDF document."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            for signature_name in signature.get_signature_names(True):
                if not signature.verify_signature(signature_name):
                    raise Exception("Not verified")
```

**تحقق من التوقيع باستخدام ملف شهادة المفتاح العامة**

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def verify_with_public_key_certificate1(certificate: str, infile: str) -> None:
    """Verify a signature with a public key certificate file."""
    with ap.facades.PdfFileSignature(infile) as file_sign:
        signature_names = file_sign.get_signature_names(True)
        with open(certificate, "rb") as file_stream:
            certificate_bytes = file_stream.read()
        print(file_sign.verify_signature(signature_names[0], certificate_bytes))
```

** تحقق من التوقيع بالشهادة المستخرجة من الملف**

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def verify_with_public_key_certificate_from_signature(infile: str) -> None:
    """Verify a signature with the certificate extracted from the file."""
    with ap.facades.PdfFileSignature(infile) as file_sign:
        signature_names = file_sign.get_signature_names(True)
        certificate = []
        if file_sign.try_extract_certificate(signature_names[0], certificate):
            print(file_sign.verify_signature(signature_names[0], certificate[0]))
        else:
            print(False)
```

**تحقق من التوقيعات مع تمكين التحقق من سلسلة الشهادة**

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def verify_signature_with_certificate_check(infile: str) -> None:
    """Verify signatures with certificate-chain validation enabled."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            for signature_name in signature.get_signature_names(True):
                options = ap.security.ValidationOptions()
                options.validation_mode = ap.security.ValidationMode.STRICT
                options.validation_method = ap.security.ValidationMethod.AUTO
                options.check_certificate_chain = True
                options.request_timeout = 20000
                validation_result = []
                verified = signature.verify_signature(
                    signature_name,
                    options,
                    validation_result,
                )
                print(f"Certificate validation result: {validation_result[0].status}")
                print(f"Is verified: {verified}")
```

## إضافة طابع زمني إلى التوقيع الرقمي

### كيفية التوقيع رقميًا على ملف PDF باستخدام الطابع الزمني

يدعم Aspose.PDF لـ Python توقيع PDF رقميًا باستخدام خادم الطابع الزمني أو خدمة الويب.

من أجل تحقيق هذا المطلب، فإن [إعدادات الطابع الزمني](https://reference.aspose.com/pdf/python-net/aspose.pdf/timestampsettings/) تمت إضافة الفئة إلى مساحة اسم Aspose.PDF. يرجى إلقاء نظرة على مقتطف الشفرة التالي الذي يحصل على الطابع الزمني ويضيفه إلى مستند PDF:

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def sign_with_time_stamp_server(
    infile: str,
    outfile: str,
    pfxfile: str,
    password: str,
) -> None:
    """Sign a PDF document and apply a timestamp from an external server."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            pkcs = ap.forms.PKCS7(pfxfile, password)
            pkcs.timestamp_settings = ap.TimestampSettings(
                "https://freetsa.org/tsr",
                "",
                ap.DigestHashAlgorithm.SHA256,
            )
            rect = drawing.Rectangle(100, 100, 200, 100)
            signature.sign(
                1, "Signature Reason", "Contact", "Location", True, rect, pkcs
            )
            signature.save(outfile)
```

## توقيع مستندات PDF باستخدام ECDSA

يتضمن توقيع مستندات PDF باستخدام ECDSA (خوارزمية التوقيع الرقمي للمنحنى البيضاوي) استخدام تشفير المنحنى البيضاوي لإنشاء توقيعات رقمية.

يوضح مقتطف الشفرة أعلاه كيفية تطبيق توقيع رقمي منفصل PKCS #7 على مستند PDF باستخدام Aspose.PDF لـ Python. من خلال تحميل المستند وتكوين مظهر التوقيع وإعدادات الأمان وحفظ النتيجة، يوضح هذا المثال سير عمل كامل وموثوق للتوقيع الرقمي لملفات PDF.

تضمن هذه الطريقة أصالة المستند وتكامله من خلال تضمين توقيع آمن يمكن التحقق منه في الصفحة الأولى. يفي استخدام SHA-256 كخوارزمية الملخص بمعايير التشفير الحديثة، بينما توفر القدرة على التحكم في موضع التوقيع المرونة لعلامات الموافقة المرئية.

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def sign_ecdsa(infile: str, outfile: str, pfxfile: str, password: str) -> None:
    """Sign a PDF document with an ECDSA signature."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            pkcs = ap.forms.PKCS7Detached(
                pfxfile,
                password,
                ap.DigestHashAlgorithm.SHA256,
            )
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)
            signature.save(outfile)
```

** تحقق من توقيعات ECDSA في مستند PDF**

```python
def verify_ecdsa(infile: str) -> None:
    """Verify ECDSA signatures in a PDF document."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            if not signature.contains_signature():
                raise Exception("Not contains signature")

            for signature_name in signature.get_signature_names(True):
                if not signature.verify_signature(signature_name):
                    raise Exception("Not verified")
```

## موضوعات الأمان ذات الصلة

- [تأمين وتوقيع ملفات PDF في Python](/pdf/ar/python-net/securing-and-signing/)
- [استخراج معلومات الصورة والتوقيع في Python](/pdf/ar/python-net/extract-image-and-signature-information/)
- [قم بتوقيع مستندات PDF من بطاقة ذكية في Python](/pdf/ar/python-net/sign-pdf-document-from-smart-card/)
- [تشفير وفك تشفير ملفات PDF في Python](/pdf/ar/python-net/set-privileges-encrypt-and-decrypt-pdf-file/)