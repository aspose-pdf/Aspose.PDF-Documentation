---
title: حماية ملفات PDF في بايثون
linktitle: تشفير وفك تشفير ملف PDF
type: docs
weight: 70
url: /ar/python-net/protect-pdf-file/
description: تعرف على كيفية تشفير الملفات وفك تشفير ملفات PDF المحمية وتغيير كلمات المرور في Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تعيين أذونات PDF وإدارة التشفير في Python
Abstract: تشرح هذه الصفحة كيفية تعيين امتيازات المستند وتطبيق التشفير وفك تشفير ملفات PDF وتغيير كلمات المرور باستخدام Aspose.PDF لـ Python عبر .NET. ويغطي تكوين كلمات مرور المستخدم والمالك، وتحديد قيود الوصول (مثل الطباعة والنسخ والتحرير)، وإدارة أمان PDF في تطبيقات Python.
---

## تشفير PDF بكلمة مرور وأذونات

استخدم Aspose.PDF لـ Python عبر .NET لتأمين مستند PDF بالتشفير المستند إلى كلمة المرور والأذونات المقيدة.

1. قم بتحميل وثيقة PDF.
1. قم بإنشاء `DocumentPrivilege` كائن الأذونات.
1. قم بتمكين الأذونات المطلوبة.
1. قم بتعيين كلمات مرور المستخدم والمالك.
1. اختر خوارزمية التشفير.
1. قم بتطبيق التشفير على المستند.
1. احفظ ملف PDF المشفر.

```python
import aspose.pdf as ap

def encrypt_password(infile, outfile):
    """
    Encrypt PDF with password and permissions.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Returns:
        None

    Example:
        encrypt_password("sample.pdf", "sample_protected.pdf")

    Note:
        Uses AES 128-bit encryption. Allows screen readers, forbids all other operations.
        User password: "userpassword", Owner password: "ownerpassword".
    """
    document = ap.Document(infile)
    document_privilege = ap.facades.DocumentPrivilege.forbid_all
    document_privilege.allow_screen_readers = True

    document.encrypt(
        "userpassword",
        "ownerpassword",
        document_privilege,
        ap.CryptoAlgorithm.AESx128,
        False,
    )
    document.save(outfile)
```

## تشفير PDF بالأذونات الكاملة

قم بتشفير مستند PDF مع السماح بأذونات الوصول الكامل باستخدام Aspose.PDF لـ Python عبر .NET. يستخدم هذا المثال تشفير RC4 128 بت للتوافق مع برامج عرض PDF القديمة.

1. قم بتحميل وثيقة PDF.
1. حدد كلمات مرور المستخدم والمالك.
1. قم بتعيين أذونات الوصول الكامل.
1. اختر خوارزمية التشفير.
1. اتصل `encrypt()` باستخدام كلمات المرور والأذونات والخوارزمية.
1. احفظ ملف PDF المشفر.

```python
import aspose.pdf as ap

def encrypt_pdf_file(infile, outfile):
    """
    Encrypt PDF with full permissions.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Returns:
        None

    Example:
        encrypt_pdf_file("sample.pdf", "sample_protected.pdf")

    Note:
        Uses RC4 128-bit encryption with allow_all privileges.
    """
    document = ap.Document(infile)
    document.encrypt(
        "userpassword",
        "ownerpassword",
        ap.facades.DocumentPrivilege.allow_all,
        ap.CryptoAlgorithm.RC4x128,
        False,
    )
    document.save(outfile)
```

## فك تشفير ملف PDF باستخدام كلمة مرور المالك

لإزالة الحماية بكلمة مرور واستعادة الوصول الكامل:

1. قم بتحميل ملف PDF المشفر باستخدام كلمة المرور الصحيحة (المستخدم أو المالك).
1. قم بإزالة جميع إعدادات حماية كلمة المرور والتشفير من المستند.
1. احفظ ملف PDF غير المحمي الآن في ملف الإخراج المحدد.

```python
import aspose.pdf as ap

def decrypt_pdf_file(infile, outfile):
    """
    Decrypt password-protected PDF.

    Args:
        infile (str): Input encrypted PDF filename
        outfile (str): Output decrypted PDF filename

    Returns:
        None

    Example:
        decrypt_pdf_file("sample_protected.pdf", "sample_unprotected.pdf")

    Note:
        Requires user password to open document.
    """
    document = ap.Document(infile, "userpassword")
    document.decrypt()
    document.save(outfile)
```

## تغيير كلمة مرور ملف PDF

قم بتحديث بيانات اعتماد الأمان (كلمات مرور المستخدم والمالك) لوثيقة PDF مع الحفاظ على محتواها وهيكلها.

1. افتح ملف PDF باستخدام كلمة مرور المالك الحالية، والتي توفر الوصول الكامل إلى إعدادات الأمان.
1. استبدل كلمات المرور القديمة بكلمة مرور مستخدم جديدة وكلمة مرور مالك جديدة.
1. احفظ ملف PDF مع إعدادات كلمة المرور المحدثة.

```python
import aspose.pdf as ap

def change_password(infile, outfile):
    """
    Change user and owner passwords.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Returns:
        None

    Example:
        change_password("sample_protected.pdf", "sample_changepassword.pdf")

    Note:
        Changes from ownerpassword to newuser/newowner.
    """
    document = ap.Document(infile, "ownerpassword")
    document.change_passwords("ownerpassword", "newuser", "newowner")
    document.save(outfile)

```

## تحديد كلمة المرور الصحيحة من Array

في بعض السيناريوهات، قد تحتاج إلى تحديد كلمة المرور الصحيحة من قائمة المرشحين المحتملين للوصول إلى PDF آمن. يتحقق المقتطف أدناه مما إذا كان ملف PDF مشفرًا ثم يحاول فتحه من خلال التكرار من خلال قائمة كلمات المرور المحددة مسبقًا.

تتضمن العملية:

1. استخدم `PdfFileInfo` لاكتشاف ما إذا كان ملف PDF مشفرًا.
1. افتح ملف PDF مع كل كلمة مرور باستخدام `ap.Document()`.
1. إذا نجحت، فإنها تطبع عدد الصفحات.
1. إذا لم يكن الأمر كذلك، فإنه يكتشف الاستثناء ويبلغ عن كلمة المرور الفاشلة.

```python
import aspose.pdf as ap

def determine_correct_password_from_list(infile):
    """
    Test multiple passwords to find correct one.

    Args:
        infile (str): Input encrypted PDF filename

    Returns:
        None

    Example:
        determine_correct_password_from_list("sample_protected.pdf")

    Note:
        Tries passwords: test, test1, test2, test3, userpassword.
        Prints page count if password is correct.
    """
    info = ap.facades.PdfFileInfo(infile)
    print(f"File is password protected {info.is_encrypted}")

    passwords = "test", "test1", "test2", "test3", "userpassword"

    for password in passwords:
        try:
            document = ap.Document(infile, password)
            count = len(document.pages)
            if count > 0:
                print(f"Number of Page in document are = {count}")
        except RuntimeError as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
```
