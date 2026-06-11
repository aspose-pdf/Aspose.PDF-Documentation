---
title: فك تشفير ملف PDF
linktitle: فك تشفير ملف PDF
type: docs
weight: 20
url: /ar/python-net/decrypt-pdf-file/
description: يشرح هذا الدليل كيفية إزالة القيود مثل الطباعة والنسخ والتحرير للوصول الكامل إلى مستند PDF الخاص بك.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إزالة الحماية بكلمة مرور من PDF
Abstract: توضح هذه المقالة كيفية فك تشفير ملف PDF باستخدام كلمة مرور المالك. وهي تغطي عملية إزالة قيود الأمان التي تحد من الإجراءات مثل طباعة المحتوى أو تحريره أو نسخه. من خلال تطبيق كلمة مرور المالك الصحيحة، يمكن للمستخدمين فتح المستند واستعادة السيطرة الكاملة على وظائفه.
---

## فك تشفير PDF باستخدام كلمة مرور المالك

قم بفك تشفير مستند PDF محمي بكلمة مرور باستخدام كلمة مرور المالك باستخدام Aspose.PDF لـ Python عبر .NET. تزيل هذه العملية التشفير وتسمح بالوصول غير المقيد إلى المستند.

1. قم بإنشاء كائن «أمان ملفات PDF».
1. قم بتحميل ملف PDF المشفر باستخدام طريقة «bind_pdf ()».
1. قم بفك تشفير المستند.
1. احفظ ملف PDF الذي تم فك تشفيره.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Decrypt PDF with Owner Password
def decrypt_pdf_with_owner_password(infile, outfile):
    """Decrypt a PDF document using the owner password."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Decrypt the PDF
    file_security.decrypt_file("owner_password")

    # Save decrypted PDF
    file_security.save(outfile)
```

## حاول فك تشفير PDF بدون استثناء

غالبًا ما تكون مستندات PDF محمية بكلمات مرور لتقييد الوصول والاستخدام. للوصول الكامل إلى هذه المستندات أو تعديلها، قد تحتاج إلى إزالة التشفير. قم بفك تشفير مستند PDF آمن باستخدام كلمة مرور المالك لإزالة قيود التشفير والوصول باستخدام Aspose.PDF لـ Python عبر .NET.

1. قم بإنشاء كائن «أمان ملفات PDF».
1. قم بربط ملف PDF المدخل.
1. قم بفك تشفير ملف PDF.
1. احفظ ملف PDF الناتج.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Try Decrypt PDF Without Exception
def try_decrypt_pdf_without_exception(infile, outfile):
    """Attempt to decrypt a PDF without throwing an exception on failure."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Attempt to decrypt the PDF
    result = file_security.try_decrypt_file("owner_password")

    # Save only if decryption was successful
    if result:
        file_security.save(outfile)
    else:
        print("Decryption failed. Check password or document security.")
```
