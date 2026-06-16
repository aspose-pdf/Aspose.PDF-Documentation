---
title: تشفير ملف PDF
linktitle: تشفير ملف PDF
type: docs
weight: 30
url: /ar/python-net/encrypt-pdf-file/
description: قم بتشفير مستند PDF وتكوين الأذونات للتحكم في ما يمكن للمستخدمين القيام به مع الملف.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تشفير PDF والتحكم في إجراءات المستخدم
Abstract: تعرف على كيفية تشفير ملف PDF أثناء تحديد أذونات مستخدم محددة باستخدام Aspose.PDF لـ Python عبر .NET. يوضح هذا الدليل كيفية السماح بالإجراءات أو تقييدها مثل الطباعة والنسخ مع الحفاظ على أمان المستند.
---

## تشفير PDF باستخدام كلمة مرور المستخدم والمالك

يعد تأمين مستندات PDF أمرًا ضروريًا عند مشاركة محتوى حساس أو مقيد. يتيح لك التشفير حماية مستند بكلمات مرور وتحديد الإجراءات التي يُسمح للمستخدمين بتنفيذها. يوضح مقتطف الشفرة هذا كيفية تطبيق كلمات مرور المستخدم والمالك إلى جانب أذونات الوصول لتأمين ملف PDF.

1. قم بإنشاء كائن أمان ملف PDF.
1. قم بربط ملف PDF المدخل.
1. حدد امتيازات المستند.
1. قم بتشفير ملف PDF.
1. احفظ ملف PDF المشفر.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Encrypt PDF with User and Owner Password
def encrypt_pdf_with_user_owner_password(infile, outfile):
    """Encrypt a PDF document using user and owner passwords."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Define document privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True

    # Encrypt the PDF
    file_security.encrypt_file(
        "user_password", "owner_password", privilege, pdf_facades.KeySize.X128
    )

    # Save encrypted PDF
    file_security.save(outfile)
```

## تشفير PDF باستخدام الأذونات

يشرح مقتطف الشفرة التالي كيفية السماح بالإجراءات المحددة مثل الطباعة والنسخ مع تقييد الآخرين.

1. قم بتهيئة [أمان ملفات PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesecurity/) فئة.
1. قم بربط ملف PDF الخاص بالإدخال.
1. قم بتكوين امتيازات المستند.
1. قم باستدعاء طريقة «encrypt_file ()».
1. احفظ ملف PDF المشفر.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Encrypt PDF with Permissions
def encrypt_pdf_with_permissions(infile, outfile):
    """Encrypt a PDF document and configure specific permissions."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Configure privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True
    privilege.allow_copy = True

    # Encrypt the PDF
    file_security.encrypt_file(
        "user_password", "owner_password", privilege, pdf_facades.KeySize.X128
    )

    # Save encrypted PDF
    file_security.save(outfile)
```

## تشفير PDF باستخدام خوارزمية التشفير

لا يحمي تشفير PDF المستندات بكلمات مرور فحسب، بل يسمح لك أيضًا باختيار خوارزمية التشفير والقوة. اختيار الخوارزمية المناسبة يضمن أمانًا أقوى للمستندات الحساسة.

1. قم بإنشاء كائن أمان ملف PDF.
1. قم بربط ملف PDF الخاص بالإدخال.
1. حدد امتيازات المستند.
1. قم بتشفير ملف PDF باستخدام الخوارزمية.
1. احفظ ملف PDF المشفر.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Encrypt PDF with Encryption Algorithm
def encrypt_pdf_with_encryption_algorithm(infile, outfile):
    """Encrypt a PDF document using a specific encryption algorithm."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Define privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True

    # Encrypt the PDF using AES algorithm
    file_security.encrypt_file(
        "user_password",
        "owner_password",
        privilege,
        pdf_facades.KeySize.X256,
        pdf_facades.Algorithm.AES,
    )

    # Save encrypted PDF
    file_security.save(outfile)
```
