---
title: تغيير كلمة مرور ملف PDF
linktitle: تغيير كلمة مرور ملف PDF
type: docs
weight: 10
url: /ar/python-net/change-password/
description: قم بتغيير كلمات مرور المستخدم والمالك لمستند PDF آمن باستخدام Aspose.PDF لـ Python عبر .NET.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تحديث كلمات مرور PDF
Abstract: تعرف على كيفية تغيير كلمات مرور المستخدم والمالك في ملف PDF آمن باستخدام Aspose.PDF لـ Python عبر .NET. يوضح هذا المثال كيفية تحديث بيانات اعتماد الوصول بأمان مع الحفاظ على التشفير والأذونات الحالية كما هي.
---

## تغيير كلمة مرور المستخدم والمالك

في كثير من الحالات، قد تحتاج إلى تحديث كلمات مرور PDF المحمي دون تغيير إعداد الأمان الحالي. يمكن أن يكون هذا مفيدًا عند تدوير بيانات الاعتماد أو نقل الملكية أو تحسين أمان المستند.

طريقة «change_password» الخاصة بـ [أمان ملفات PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesecurity/) يتيح لك الفصل:

- قم بتحديث كلمة مرور المستخدم (مطلوب لفتح المستند)
- تحديث كلمة مرور المالك (المستخدمة للتحكم في الأذونات)
- احتفظ بإعدادات التشفير والأذونات الحالية

1. قم بإنشاء كائن «أمان ملفات PDF».
1. قم بربط ملف PDF المدخل.
1. قم بتغيير كلمات المرور باستخدام طريقة «change_password ()».
1. احفظ ملف PDF المحدث.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Change User and Owner Password
def change_user_and_owner_password(infile, outfile):
    """Change user and owner passwords while keeping existing security settings."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Change passwords
    file_security.change_password(
        "owner_password", "new_user_password", "new_owner_password"
    )

    # Save updated PDF
    file_security.save(outfile)
```

## تغيير كلمة المرور وإعادة تعيين الأمان

عند العمل مع مستندات PDF المؤمنة، قد لا يكون مجرد تغيير كلمات المرور كافيًا. قد تحتاج أيضًا إلى ضبط الأذونات، مثل حقوق الطباعة أو النسخ أو التحرير.

تعرف على كيفية تحديث كلمات مرور المستخدم والمالك أثناء إعادة تعيين إعدادات أمان PDF باستخدام Aspose.PDF لـ Python عبر .NET. يوضح هذا المثال كيفية إعادة تعريف أذونات المستند وقوة التشفير إلى جانب بيانات اعتماد الوصول الجديدة.

1. قم بإنشاء كائن «أمان ملفات PDF».
1. قم بربط ملف PDF المدخل.
1. قم بإنشاء كائن «DocumentPrivilege» وقم بتكوين الإجراءات المسموح بها.
1. قم بتغيير كلمات المرور وإعادة تعيين الأمان.
1. احفظ ملف PDF المحدث.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Change Password and Reset Security
def change_password_and_reset_security(infile, outfile):
    """Change passwords and reset document security settings."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Define new privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True

    # Change passwords and reset security
    file_security.change_password(
        "owner_password",
        "new_user_password",
        "new_owner_password",
        privilege,
        pdf_facades.KeySize.X128,
    )

    # Save updated PDF
    file_security.save(outfile)
```

## حاول تغيير كلمة المرور بدون استثناء

في بعض عمليات سير العمل، خاصة في المعالجة المجمعة أو الأنظمة الآلية، من المهم تجنب الاستثناءات التي قد تعطل التنفيذ. بدلاً من إلقاء الأخطاء، قد تفضل عملية آمنة تُبلغ عن النجاح أو الفشل.

طريقة «try_change_password» الخاصة بـ [أمان ملفات PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesecurity/) توفر الفئة هذه الوظيفة من خلال:

1. قم بإنشاء كائن «أمان ملفات PDF».
1. قم بتحميل مستند PDF باستخدام طريقة «bind_pdf ()».
1. حاول تغيير كلمات المرور.
1. تحقق من النتيجة.
1. احفظ ملف PDF المحدث.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Try Change Password Without Exception
def try_change_password_without_exception(infile, outfile):
    """Attempt to change passwords without throwing an exception on failure."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Attempt to change passwords
    result = file_security.try_change_password(
        "owner_password", "new_user_password", "new_owner_password"
    )

    # Save only if operation succeeded
    if result:
        file_security.save(outfile)
    else:
        print("Password change failed. Check owner password or document security.")
```
