---
title: تعيين الامتيازات على ملف PDF موجود
linktitle: تعيين الامتيازات على ملف PDF موجود
type: docs
weight: 40
url: /ar/python-net/set-privileges/
description: قم بتعيين وإدارة امتيازات وثيقة PDF للتحكم في إجراءات المستخدم مثل الطباعة والنسخ والتحرير.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إدارة أذونات PDF وعناصر التحكم في الوصول
Abstract: تعرف على كيفية التحكم في ما يمكن للمستخدمين القيام به باستخدام PDF عن طريق تعيين امتيازات المستند باستخدام Aspose.PDF لـ Python عبر .NET. يغطي هذا الدليل تطبيق الأذونات بكلمات مرور أو بدونها لتقييد الإجراءات مثل الطباعة أو النسخ أو التحرير.
---

## تعيين امتيازات PDF بدون كلمات مرور

تحقق من كيفية تطبيق امتيازات المستند على PDF دون تحديد كلمات مرور المستخدم أو المالك باستخدام Aspose.PDF لـ Python عبر .NET. يوضح مقتطف الشفرة هذا كيفية التحكم في الإجراءات المسموح بها مع الحفاظ على إمكانية الوصول إلى المستند.

1. قم بإنشاء كائن «أمان ملفات PDF».
1. قم بربط ملف PDF المدخل.
1. حدد امتيازات المستند.
1. قم باستدعاء طريقة 'set_privilege () 'دون تمرير كلمات المرور.
1. احفظ ملف PDF المحدث.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Set PDF Privileges Without Passwords
def set_pdf_privileges_without_passwords(infile, outfile):
    """Set PDF privileges without specifying user and owner passwords."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Define privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True

    # Apply privileges (owner password will be generated automatically)
    file_security.set_privilege(privilege)

    # Save updated PDF
    file_security.save(outfile)
```

## تعيين امتيازات PDF باستخدام كلمات مرور المستخدم والمالك

لتأمين مستند PDF بالكامل، تحتاج غالبًا إلى كل من التحكم في الوصول (كلمات المرور) وقيود الاستخدام (الأذونات). من خلال الجمع بين هذه العناصر، يمكنك التأكد من أن المستخدمين المصرح لهم فقط يمكنهم فتح المستند وتنفيذ إجراءات محددة.

باستخدام طريقة set_privilege مع معلمات كلمة المرور، يمكنك:

- قم بحماية المستند بكلمة مرور مستخدم
- حدد كلمة مرور المالك للتحكم الكامل
- تكوين الإجراءات المسموح بها والمقيدة
- فرض سياسات الأمان على مستوى المستند

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Set PDF Privileges with User and Owner Passwords
def set_pdf_privileges_with_passwords(infile, outfile):
    """Set PDF privileges using user and owner passwords."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Define privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True
    privilege.allow_copy = False

    # Apply privileges with passwords
    file_security.set_privilege("user_password", "owner_password", privilege)

    # Save updated PDF
    file_security.save(outfile)
```

## حاول تعيين امتيازات PDF بدون استثناء

يشرح مقتطف الشفرة هذا كيفية التحكم في الوصول وتقييد الإجراءات مثل النسخ مع السماح للآخرين مثل الطباعة.

1. قم بإنشاء كائن «أمان ملفات PDF».
1. قم بتحميل ملف PDF المصدر باستخدام طريقة «bind_pdf ()».
1. حدد امتيازات المستند.
1. قم بتطبيق الامتيازات باستخدام كلمات المرور.
1. احفظ ملف PDF المحدث.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Try Set PDF Privileges Without Exception
def try_set_pdf_privileges_without_exception(infile, outfile):
    """Attempt to set PDF privileges without throwing an exception on failure."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Define privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True

    # Attempt to apply privileges
    result = file_security.try_set_privilege(
        "user_password", "owner_password", privilege
    )

    # Save only if operation succeeded
    if result:
        file_security.save(outfile)
    else:
        print("Setting privileges failed. Check passwords or document state.")
```
