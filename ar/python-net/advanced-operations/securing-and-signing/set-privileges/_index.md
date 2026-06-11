---
title: تشفير وفك تشفير ملفات PDF في Python
linktitle: تشفير وفك تشفير ملف PDF
type: docs
weight: 70
url: /ar/python-net/set-privileges-encrypt-and-decrypt-pdf-file/
description: تعرف على كيفية تعيين امتيازات PDF وتشفير الملفات وفك تشفير ملفات PDF المحمية وتغيير كلمات المرور في Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تعيين أذونات PDF وإدارة التشفير في Python
Abstract: تشرح صفحة الوثائق هذه كيفية تعيين امتيازات المستند وتطبيق التشفير وفك تشفير ملفات PDF باستخدام Aspose.PDF لـ Python. إنه يوجه المطورين من خلال تكوين كلمات مرور المستخدم والمالك، وتحديد قيود الوصول (مثل الطباعة أو النسخ أو التحرير). توضح أمثلة التعليمات البرمجية كيفية حماية المحتوى الحساس وإدارة أمان PDF بفعالية داخل تطبيقات Python، مما يضمن الوصول الخاضع للرقابة وسرية البيانات.
---

تعد إدارة أمان المستندات أمرًا ضروريًا عند العمل مع المحتوى الحساس أو المهم للأعمال. يوفر Aspose.PDF لـ Python عبر .NET واجهة برمجة تطبيقات قوية لتطبيق التشفير برمجيًا والتحكم في الوصول من خلال الأذونات وفك تشفير ملفات PDF المحمية.

تقدم هذه المقالة لمطوري Python أمثلة عملية لتعيين الامتيازات وتطبيق التشفير وإزالته وتغيير كلمات المرور واكتشاف حالات الحماية - كل ذلك ضمن سير عمل PDF.

يمنح Aspose.PDF لـ Python عبر .NET للمطورين التحكم الكامل في أمان PDF:

**تعيين الامتيازات** - التحكم الدقيق في الوصول باستخدام الأذونات.
**تشفير الملف** - قم بتطبيق تشفير AES أو RC4 بكلمات مرور مخصصة.
**فك تشفير الملف** - إزالة الأمان باستخدام كلمة مرور المالك.
**تغيير كلمات المرور** - قم بتدوير بيانات الاعتماد أو تحديثها دون تغيير المحتوى.
**فحص الأمان** - اكتشاف حالة التشفير أو أنواع كلمات المرور المطلوبة.

استخدم هذه الصفحة عندما تحتاج إلى حماية مستندات PDF بكلمات مرور أو تقييد الطباعة أو النسخ أو تدوير بيانات الاعتماد أو فحص ما إذا كان المستند مشفرًا.

## تعيين الامتيازات على ملف PDF موجود

يمكنك تقييد عمليات محددة أو السماح بها (مثل الطباعة والنسخ وملء النماذج) عن طريق تعيين كلمات مرور المستخدم والمالك إلى جانب امتيازات الوصول.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def set_privileges_on_existing_pdf_file(infile: str, outfile: str) -> None:
    """Set restricted privileges on an existing PDF document."""
    with ap.Document(infile) as document:
        document_privilege = ap.facades.DocumentPrivilege.forbid_all
        document_privilege.allow_screen_readers = True
        document.encrypt(
            "user",
            "owner",
            document_privilege,
            ap.CryptoAlgorithm.AESx128,
            False,
        )
        document.save(outfile)
```

## تشفير ملف PDF باستخدام أنواع التشفير المختلفة والخوارزميات

يضمن تشفير PDF أن المستخدمين الذين لديهم بيانات اعتماد صالحة فقط يمكنهم فتح الملف أو تعديله.

>المصطلحات الرئيسية:

- كلمة مرور المستخدم. مطلوب لفتح المستند.

- كلمة مرور المالك. مطلوب لتغيير الأذونات أو إزالة التشفير.

- حجم المفتاح. استخدم AE_SX128 للحصول على أقصى درجات الأمان في عمليات سير العمل الحديثة.

يوضح لك مقتطف الشفرة التالي كيفية تشفير ملفات PDF.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def encrypt_pdf_file(infile: str, outfile: str) -> None:
    """Encrypt a PDF document with user and owner passwords."""
    with ap.Document(infile) as document:
        document.encrypt(
            "user",
            "owner",
            ap.Permissions.EXTRACT_CONTENT,
            ap.CryptoAlgorithm.AESx128,
        )
        document.save(outfile)
```

## فك تشفير ملف PDF باستخدام كلمة مرور المالك

لإزالة الحماية بكلمة مرور واستعادة الوصول الكامل:

1. يقوم بتحميل ملف PDF المشفر باستخدام كلمة المرور الصحيحة («كلمة المرور» هي كلمة مرور المستخدم أو المالك).
1. يزيل جميع إعدادات حماية كلمة المرور والتشفير من المستند.
1. يحفظ ملف PDF غير المحمي الآن إلى ملف الإخراج المحدد.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def decrypt_pdf_file(infile: str, outfile: str) -> None:
    """Decrypt a password-protected PDF document."""
    with ap.Document(infile, "password") as document:
        document.decrypt()
        document.save(outfile)
```

## تشفير وفك تشفير ملف PDF باستخدام شهادات المفتاح العام

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def pub_sec_encryption(
    crypto_algorithm,
    pub_cert: str,
    in_pfx: str,
    outfile: str,
) -> None:
    """Demonstrate public-key encryption and decryption."""
    pfx_password = "12345"

    with ap.Document() as document:
        document.info.title = "TestTitle"
        document.info.author = "TestAuthor"
        page = document.pages.add()
        page.paragraphs.add(ap.text.TextFragment("Hello World!"))

        with open(pub_cert, "rb") as file_stream:
            byte_content = file_stream.read()

        document.encrypt(
            ap.Permissions.PRINT_DOCUMENT,
            crypto_algorithm,
            [byte_content],
        )
        document.save(outfile)

    with ap.Document(
        outfile,
        ap.security.CertificateEncryptionOptions(pub_cert, in_pfx, pfx_password),
    ) as document:
        print(document.info.title)
        print(document.info.author)

        text_absorber = ap.text.TextAbsorber()
        document.pages[1].accept(text_absorber)
        print(text_absorber.text)

        document.decrypt()
        document.save(path.join(path.dirname(outfile), "pubsec_decrypted_out.pdf"))
```

## تغيير كلمة مرور ملف PDF

لتحديث بيانات اعتماد الأمان (كلمات مرور المستخدم والمالك) لوثيقة PDF مع الحفاظ على محتواها وهيكلها.

1. يفتح ملف PDF باستخدام كلمة مرور المالك الحالية («المالك»)، والتي تمنح الوصول الكامل بما في ذلك الإذن لتغيير إعدادات الأمان.
1. يستبدل كلمات المرور القديمة بكلمة مرور مستخدم جديدة ('newuser') وكلمة مرور مالك جديدة ('newowner').
1. يحفظ ملف PDF مع إعدادات كلمة المرور المحدثة.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def change_password(infile: str, outfile: str) -> None:
    """Change the passwords of a password-protected PDF document."""
    with ap.Document(infile, "owner") as document:
        document.change_passwords("owner", "newuser", "newowner")
        document.save(outfile)
```

## كيفية - تحديد ما إذا كان ملف PDF المصدر محميًا بكلمة مرور

### تحديد كلمة المرور الصحيحة من Array

في بعض السيناريوهات، قد تحتاج إلى تحديد كلمة المرور الصحيحة من قائمة المرشحين المحتملين من أجل الوصول إلى PDF آمن. يوضح مقتطف الشفرة أدناه كيفية التحقق مما إذا كان ملف PDF محميًا بكلمة مرور ثم محاولة إلغاء قفله من خلال التكرار من خلال قائمة كلمات المرور المحددة مسبقًا باستخدام Aspose.PDF لـ Python عبر .NET.

تتضمن العملية:

1. استخدام PDFfileInfo لاكتشاف ما إذا كان PDF مشفرًا.
1. يحاول فتح ملف PDF مع كل كلمة مرور باستخدام AP.document ().
1. إذا نجحت، فإنها تطبع عدد الصفحات.
1. إذا لم يكن الأمر كذلك، فإنه يكتشف الاستثناء ويبلغ عن كلمة المرور الفاشلة.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def determine_correct_password_from_array(infile: str) -> None:
    """Try a list of passwords until the document opens successfully."""
    with ap.facades.PdfFileInfo() as pdf_file_info:
        pdf_file_info.bind_pdf(infile)
        print(f"File is password protected {pdf_file_info.is_encrypted}")

    passwords = ["test", "test1", "test2", "test3", "sample"]

    for password in passwords:
        try:
            with ap.Document(infile, password) as document:
                if len(document.pages) > 0:
                    print(f"Password = {password} is correct")
                    print(f"Number of pages in document = {len(document.pages)}")
                    break
        except Exception:
            print(f"Password = {password} is not correct")
```

## موضوعات الأمان ذات الصلة

- [تأمين وتوقيع ملفات PDF في Python](/pdf/ar/python-net/securing-and-signing/)
- [قم بتوقيع ملفات PDF رقميًا في Python](/pdf/ar/python-net/digitally-sign-pdf-file/)
- [استخراج معلومات التوقيع من PDF في Python](/pdf/ar/python-net/extract-image-and-signature-information/)
- [قم بتوقيع مستندات PDF من بطاقة ذكية في Python](/pdf/ar/python-net/sign-pdf-document-from-smart-card/)

