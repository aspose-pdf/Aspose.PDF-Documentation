---
title: تعيين الصلاحيات، تشفير وفك تشفير PDF
linktitle: تشفير وفك تشفير ملف PDF
type: docs
weight: 70
url: /ar/python-net/set-privileges-encrypt-and-decrypt-pdf-file/
description: تشفير ملف PDF باستخدام بايثون عبر أنواع وخوارزميات تشفير مختلفة. كما يمكن فك تشفير ملفات PDF باستخدام كلمة مرور المالك.
lastmod: "2025-06-22"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تشفير أو فك تشفير ملف PDF باستخدام بايثون
Abstract: تشرح صفحة التوثيق هذه كيفية تعيين صلاحيات المستند، تطبيق التشفير، وفك تشفير ملفات PDF باستخدام Aspose.PDF for Python. تُرشد المطورين خلال إعداد كلمات مرور المستخدم والمالك، وتحديد قيود الوصول (مثل الطباعة، النسخ، أو التحرير). تُظهر أمثلة الشيفرة كيفية حماية المحتوى الحساس وإدارة أمان PDF بفعالية ضمن تطبيقات بايثون، لضمان الوصول المتحكم فيه وسرية البيانات.
---

إدارة أمان المستندات أمر أساسي عند التعامل مع محتوى حساس أو حيوي للأعمال. توفر Aspose.PDF for Python عبر .NET واجهة برمجة تطبيقات قوية لتطبيق التشفير برمجياً، التحكم في الوصول عبر الصلاحيات، وفك تشفير ملفات PDF المحمية.

تُرشد هذه المقالة مطوري بايثون من خلال أمثلة عملية لتعيين الصلاحيات، تطبيق وإزالة التشفير، تغيير كلمات المرور، واكتشاف حالات الحماية — كل ذلك ضمن سير عمل PDF.

توفر Aspose.PDF for Python عبر .NET للمطورين تحكمًا كاملاً في أمان PDF:

**تعيين الصلاحيات** - التحكم الدقيق في الوصول باستخدام الصلاحيات.
**تشفير الملف** - تطبيق تشفير AES أو RC4 باستخدام كلمات مرور مخصصة.
**فك تشفير الملف** - إزالة الحماية باستخدام كلمة مرور المالك.
**تغيير كلمات المرور** - تدوير أو تحديث بيانات الاعتماد دون تعديل المحتوى.
**فحص الأمان** - اكتشاف حالة التشفير أو أنواع كلمات المرور المطلوبة.

## تعيين الصلاحيات على ملف PDF موجود

يمكنك تقييد أو السماح بعمليات محددة (مثل الطباعة، النسخ، تعبئة النماذج) عن طريق تعيين كلمات مرور المستخدم والمالك بالإضافة إلى صلاحيات الوصول.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Instantiate Document Privileges object
        # Apply restrictions on all privileges
        document_privilege = ap.facades.DocumentPrivilege.forbid_all
        # Only allow screen reading
        document_privilege.allow_screen_readers = True
        # Encrypt the file with User and Owner password
        # Need to set the password, so that once the user views the file with user password
        # Only screen reading option is enabled
        document.encrypt("user", "owner", document_privilege, ap.CryptoAlgorithm.AE_SX128, False)
        # Save PDF document
        document.save(path_outfile)
```

## تشفير ملف PDF باستخدام أنواع وخوارزميات تشفير مختلفة

يضمن تشفير PDF أن المستخدمين الذين لديهم بيانات اعتماد صالحة فقط يمكنهم فتح أو تعديل الملف.

>المصطلحات الرئيسية:

- كلمة مرور المستخدم. مطلوبة لفتح المستند.

- كلمة مرور المالك. مطلوبة لتغيير الصلاحيات أو إزالة التشفير.

- حجم المفتاح. استخدم AE_SX128 للحصول على أقصى أمان في سير العمل الحديث.

يوضح مقطع الشيفرة التالي كيفية تشفير ملفات PDF.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Encrypt PDF
        document.encrypt("user", "owner", ap.Permissions.EXTRACT_CONTENT, ap.CryptoAlgorithm.AE_SX128)
        # Save PDF document
        document.save(path_outfile)
```

## فك تشفير ملف PDF باستخدام كلمة مرور المالك

لإزالة حماية كلمة المرور واستعادة الوصول الكامل:

1. تحميل ملف PDF المشفر باستخدام كلمة المرور الصحيحة ('password' هي كلمة مرور المستخدم أو المالك).
1. إزالة جميع حماية كلمات المرور وإعدادات التشفير من المستند.
1. حفظ ملف PDF غير المحمي الآن إلى ملف الإخراج المحدد.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document with password
    with ap.Document(path_infile, "password") as document:
        # Decrypt PDF
        document.decrypt()
        # Save PDF document
        document.save(path_outfile)
```

## تغيير كلمة مرور ملف PDF

لتحديث بيانات الاعتماد الأمنية (كلمات مرور المستخدم والمالك) لمستند PDF مع الحفاظ على محتواه وبنيته.

1. فتح ملف PDF باستخدام كلمة مرور المالك الحالية ('owner')، والتي تمنح وصولًا كاملاً بما في ذلك الإذن بتغيير إعدادات الأمان.
1. استبدال كلمات المرور القديمة بكلمة مرور مستخدم جديدة ('newuser') وكلمة مرور مالك جديدة ('newowner').
1. حفظ ملف PDF بإعدادات كلمة المرور المحدثة.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document with password
    with ap.Document(path_infile, "owner") as document:
        # Change password
        document.change_passwords("owner", "newuser", "newowner")
        # Save PDF document
        document.save(path_outfile)
```

## كيفية - تحديد ما إذا كان ملف PDF المصدر محمياً بكلمة مرور

### تحديد كلمة المرور الصحيحة من المصفوفة

في بعض السيناريوهات، قد تحتاج إلى تحديد كلمة المرور الصحيحة من قائمة من المرشحين المحتملين للوصول إلى PDF مؤمن. يوضح مقطع الشيفرة أدناه كيفية التحقق مما إذا كان ملف PDF محمياً بكلمة مرور ثم محاولة فك القفل عن طريق التكرار عبر قائمة مسبقة التعريف من كلمات المرور باستخدام Aspose.PDF for Python عبر .NET.

تشمل العملية:

1. استخدام PdfFileInfo لاكتشاف ما إذا كان PDF مشفراً.
1. محاولة فتح PDF بكل كلمة مرور باستخدام ap.Document().
1. إذا نجح، يطبع عدد الصفحات.
1. إذا لم ينجح، يلتقط الاستثناء ويبلغ عن كلمة المرور الفاشلة.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile

    with ap.facades.PdfFileInfo() as pdf_file_info:
        # Bind PDF document
        pdf_file_info.bind_pdf(path_infile)
        # Determine if the source PDF is encrypted
        print("File is password protected " + str(pdf_file_info.is_encrypted))

        passwords = ["test", "test1", "test2", "test3", "sample"]

        for password_index in range(len(passwords)):
            try:
                with ap.Document(path_infile, passwords[password_index]) as document:
                    if len(document.pages) > 0:
                        print("Number of Pages in document are = " + str(len(document.pages)))
                    password_index = password_index + 1
            except Exception as e:
                print("Password = " + passwords[password_index] + " is not correct")
                password_index = password_index + 1
```


