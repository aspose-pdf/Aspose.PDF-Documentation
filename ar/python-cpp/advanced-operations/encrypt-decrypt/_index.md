---
title: تشفير وفك تشفير PDF
linktitle: تشفير وفك تشفير ملف PDF
type: docs
weight: 30
url: ar/python-cpp/set-privileges-encrypt-and-decrypt-pdf-file/
description: تشفير وفك تشفير ملف PDF باستخدام بايثون عبر تطبيق C++.
lastmod: "2024-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## تشفير ملف PDF باستخدام أنواع وتشفيرات مختلفة

إحدى الطرق الفعالة لحماية ملفات PDF هي من خلال التشفير. في هذه المقالة، سنستعرض كيفية تشفير مستندات PDF باستخدام بايثون بمساعدة مكتبة Aspose.PDF.

يتضمن تشفير PDF تشفير محتوى مستند PDF باستخدام خوارزميات التشفير لمنع الوصول غير المصرح به. تتطلب ملفات PDF المشفرة كلمة مرور للفتح وقد تحتوي على قيود على الإجراءات مثل الطباعة والنسخ والتحرير.

- **كلمة مرور المستخدم**، إذا تم تعيينها، هي ما تحتاج إلى توفيره لفتح PDF. سيطلب Acrobat/Reader من المستخدم إدخال كلمة مرور المستخدم. إذا لم تكن صحيحة، فلن يفتح المستند.
- **كلمة مرور المالك**، إذا تم تعيينها، تتحكم في الأذونات، مثل الطباعة والتحرير والاستخراج والتعليق، إلخ.
 Acrobat/Reader سيمنع هذه الأشياء بناءً على إعدادات الأذونات. سيتطلب Acrobat هذه الكلمة السرية إذا كنت تريد تعيين/تغيير الأذونات.

يظهر لك مقطع الكود التالي كيفية تشفير ملفات PDF.

1. إنشاء مسار ملف الإدخال والإخراج
1. تحميل مستند PDF باستخدام AsposePDFPythonWrappers
1. تحديد الأذونات للمستند المشفر
1. تحديد خوارزمية التشفير التي سيتم استخدامها
1. تشفير المستند بكلمات المرور للمستخدم والمالك المحددة، والأذونات، وخوارزمية التشفير باستخدام طريقة 'document.encrypt'
1. حفظ المستند المشفر في ملف الإخراج المحدد باستخدام طريقة 'document.save'.

```python

    import AsposePDFPythonWrappers as apw
    import AsposePDFPython as apCore
    import os
    import os.path

    # تعيين مسار الدليل للملفات النموذجية
    dataDir = os.path.join(os.getcwd(), "samples")

    # تعيين مسار ملف الإدخال
    input_file = os.path.join(dataDir, "sample.pdf")

    # تعيين مسار ملف الإخراج
    output_file = os.path.join(dataDir, "results", "sample-enc.pdf")

    # تحميل مستند PDF باستخدام AsposePDFPythonWrappers
    document = apw.Document(inputFile)

    # تحديد الأذونات للمستند المشفر
    permission = apCore.Permissions(apCore.Permissions.ExtractContent | apCore.ModifyContent)

    # تحديد خوارزمية التشفير التي سيتم استخدامها
    cryptoAlgorithm = apCore.CryptoAlgorithm.RC4x128

    # تشفير المستند بكلمات المرور للمستخدم والمالك المحددة، والأذونات، وخوارزمية التشفير
    document.encrypt("user", "owner", permission, cryptoAlgorithm)

    # حفظ المستند المشفر في ملف الإخراج المحدد
    document.save(output_file)
```

## فك تشفير ملف PDF باستخدام كلمة مرور المالك

1. إنشاء مسار ملف الإدخال والإخراج
2. إنشاء مثيل جديد لفئة Document من وحدة AsposePDFPythonWrappers
3. فك تشفير المستند باستخدام طريقة [document_decrypt](https://reference.aspose.com/pdf/python-cpp/core/document_decrypt/)
4. حفظ المستند المفكك التشفير إلى مسار ملف الإخراج باستخدام طريقة save() مع وظيفة [document_save](https://reference.aspose.com/pdf/python-cpp/core/document_save/).

```Python

    import AsposePDFPythonWrappers as apw
    import AsposePDFPython as apCore
    import os
    import os.path

    # تحديد مسار الدليل للملفات النموذجية
    dataDir = os.path.join(os.getcwd(), "samples")

    # تحديد مسار ملف الإدخال
    input_file = os.path.join(dataDir, "sample_enc.pdf")

    # تحديد مسار ملف الإخراج
    output_file = os.path.join(dataDir, "results", "sample-dec.pdf")

    # إنشاء مثيل جديد لفئة Document من وحدة AsposePDFPythonWrappers
    document = apw.Document(input_file, "owner")

    # فك تشفير المستند باستخدام طريقة decrypt()
    document.decrypt()

    # حفظ المستند المفكك التشفير إلى مسار ملف الإخراج باستخدام طريقة save()
    document.save(output_file)
```