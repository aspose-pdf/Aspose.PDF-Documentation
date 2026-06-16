---
title: استخراج معلومات التوقيع من PDF في Python
linktitle: استخراج التفاصيل من التوقيع
type: docs
weight: 20
url: /ar/python-net/extract-image-and-signature-information/
description: تعرف على كيفية استخراج صور التوقيع والشهادات وتفاصيل التوقيع الرقمي من ملفات PDF في Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: استخراج صور التوقيع وتفاصيل الشهادة من ملفات PDF في Python
Abstract: تشرح هذه المقالة كيفية استخراج معلومات الصورة والتوقيع الرقمي من مستندات PDF باستخدام Aspose.PDF لـ Python. تعرف على كيفية استرداد صور التوقيع واستخراج بيانات الشهادة وفحص خوارزميات التوقيع واكتشاف التوقيعات المخترقة في ملفات PDF الموقعة.
---

## استخراج صورة من حقل التوقيع

يتيح لك Aspose.PDF لـ Python عبر .NET استرداد الصورة المرئية المضمنة في ملف [حقل التوقيع](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/). يكون هذا مفيدًا عندما تحتاج إلى عرض مظهر التوقيع أو أرشفته دون عرض ملف PDF الكامل.

يتكرر المثال أدناه في جميع حقول النموذج، ويجد كل منها `SignatureField`، ويحفظ صورته كملف JPEG:

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def extract_images_from_signature_field(infile: str, outfile: str) -> None:
    """Extract the image stored in a signature field."""
    with ap.Document(infile) as document:
        for field in document.form:
            if not isinstance(field, ap.forms.SignatureField):
                continue

            image_stream = field.extract_image()
            if image_stream is None:
                continue

            image = drawing.Bitmap.from_stream(image_stream)
            image.save(outfile, drawing.imaging.ImageFormat.jpeg)
```

## اقرأ تفاصيل خوارزمية التوقيع

استخدم `PdfFileSignature.get_signatures_info()` لقراءة بيانات تعريف التشفير لكل توقيع في مستند - بما في ذلك خوارزمية الملخص ونوع الخوارزمية ومعيار التشفير واسم التوقيع:

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def get_signatures_info(infile: str) -> None:
    """Print information about all signatures in a PDF document."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            for signature_info in signature.get_signatures_info():
                print(signature_info.DIGEST_HASH_ALGORITHM)
                print(signature_info.ALGORITHM_TYPE)
                print(signature_info.CRYPTOGRAPHIC_STANDARD)
                print(signature_info.signature_name)
```

## استخراج شهادة رقمية من حقل التوقيع

استخدم [استخراج الشهادة](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/#methods) طريقة على `SignatureField` لاسترداد الشهادة المضمنة كتدفق بايت وحفظها على القرص للتحقق الخارجي:

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def extract_certificate(infile: str, outfile: str) -> None:
    """Extract a certificate from a signature field and save it to disk."""
    with ap.Document(infile, password="owner") as document:
        for field in document.form:
            if not isinstance(field, ap.forms.SignatureField):
                continue

            certificate_stream = field.extract_certificate()
            if certificate_stream is None:
                continue

            with certificate_stream:
                bytes_data = bytearray(certificate_stream.length)
                certificate_stream.read(bytes_data, 0, len(bytes_data))
                with open(outfile, "wb") as file_stream:
                    file_stream.write(bytes_data)
                return
```

## استخراج الشهادات باستخدام واجهة توقيع ملف PDF

`PdfFileSignature.try_extract_certificate()` يوفر طريقة بديلة لاسترداد الشهادات حسب اسم التوقيع. يتكرر المثال التالي على جميع أسماء التوقيعات ويحاول الاستخراج لكل منها:

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def extract_certificate_try_extract_certificate_method(infile: str) -> None:
    """Extract certificates with the try_extract_certificate facade method."""
    with ap.Document(infile, password="owner") as document:
        with ap.facades.PdfFileSignature(document) as signature:
            for signature_name in signature.get_signature_names(True):
                certificate = []
                if signature.try_extract_certificate(signature_name, certificate):
                    print("The certificate extraction succeeded")
```

## تحقق من التوقيعات الرقمية الخارجية

للتأكد من عدم تعديل المستند بعد التوقيع، تحقق من كل توقيع خارجي باستخدام `PdfFileSignature.verify_signature()`. يعرض المثال أدناه استثناءً لأي توقيع يفشل في التحقق:

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

## كشف التوقيعات المخترقة

`SignaturesCompromiseDetector` يتحقق مما إذا كانت أي توقيعات رقمية في مستند قد تم إبطالها من خلال التغييرات اللاحقة. استخدم هذا في عمليات سير العمل القانونية أو المالية أو الامتثال حيث يجب ضمان سلامة المستندات.

يقوم المثال أدناه بالتحقق من التوقيعات المخترقة والإبلاغ عن أسمائها بالإضافة إلى تغطية التوقيع الشاملة للمستند:

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def check(infile: str) -> None:
    """Check whether a PDF contains compromised signatures."""
    with ap.Document(infile) as document:
        detector = ap.SignaturesCompromiseDetector(document)
        result = []

        if detector.check(result):
            print("No signature compromise detected")
            return

        if result[0].has_compromised_signatures:
            print(
                f"Count of compromised signatures: {len(result[0].COMPROMISED_SIGNATURES)}"
            )
            for signature_name in result[0].COMPROMISED_SIGNATURES:
                print(f"Signature name: {signature_name.FULL_NAME}")

        print(result[0].signatures_coverage)
```

## موضوعات الأمان ذات الصلة

- [تأمين وتوقيع ملفات PDF في Python](/pdf/ar/python-net/securing-and-signing/)
- [قم بتوقيع ملفات PDF رقميًا في Python](/pdf/ar/python-net/digitally-sign-pdf-file/)
- [قم بتوقيع مستندات PDF من بطاقة ذكية في Python](/pdf/ar/python-net/sign-pdf-document-from-smart-card/)
- [تشفير وفك تشفير ملفات PDF في Python](/pdf/ar/python-net/set-privileges-encrypt-and-decrypt-pdf-file/)
