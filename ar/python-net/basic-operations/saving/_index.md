---
title: حفظ مستند PDF برمجياً
linktitle: حفظ PDF
type: docs
weight: 30
url: /ar/python-net/save-pdf-document/
description: تعلم كيفية حفظ ملف PDF في Python باستخدام مكتبة Aspose.PDF للـ Python عبر .NET. احفظ مستند PDF إلى نظام الملفات، إلى تدفق، وفي تطبيقات الويب.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: حفظ مستندات PDF باستخدام مكتبة Aspose.PDF في Python
Abstract: يوفر المقال إرشادات حول حفظ مستندات PDF باستخدام مكتبة Aspose.PDF في Python. يوضح ثلاث طرق أساسية لحفظ ملفات PDF - إلى نظام الملفات، إلى تدفق، وفي صيغ محددة مثل PDF/A أو PDF/X. طريقة `save()` في فئة `Document` هي المحور الأساسي لهذه العمليات. لحفظ PDF إلى نظام الملفات، يمكن إنشاء مستند أو تعديلّه، مثل إضافة صفحة جديدة، ثم حفظه مباشرةً إلى مسار. لحفظه إلى تدفق، تسمح التحميلات الزائدة (overloads) لطريقة `Save` بكتابة المستند إلى كائن تدفق. بالإضافة إلى ذلك، يشرح المقال كيفية حفظ المستندات بصيغ PDF/A أو PDF/X، وهي معايير للأرشفة طويلة الأمد وتبادل الرسومات على التوالي. تتطلب هذه العملية إعداد المستند باستخدام طريقة `convert` قبل حفظه. توضح مقتطفات كود Python المقدمة كل نهج، موضحةً التطبيق العملي لهذه الطرق.
---

## حفظ مستند PDF إلى نظام الملفات

يمكنك حفظ مستند PDF المُنشأ أو المُعدل إلى نظام الملفات باستخدام طريقة [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) لفئة [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    # make some manipation, i.g add new empty page
    document.pages.add()
    document.save(output_pdf)
```

## حفظ مستند PDF إلى تدفق

يمكنك أيضًا حفظ مستند PDF المُنشأ أو المُعدل إلى تدفق باستخدام التحميلات الزائدة (overloads) لطرق `Save`.

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    # make some manipation, i.g add new empty page
    document.pages.add()
    document.save(io.FileIO(output_pdf, 'w'))
```

## حفظ صيغة PDF/A أو PDF/X

PDF/A هو نسخة موحدة وفقًا لمواصفات ISO من تنسيق المستندات المحمولة (PDF) للمستخدم في الأرشفة والحفظ الطويل الأمد للمستندات الإلكترونية.
يختلف PDF/A عن PDF بأنه يمنع الخصائص غير المناسبة للأرشفة طويلة الأمد، مثل ربط الخطوط (بدلاً من تضمين الخطوط) والتشفير. تشمل متطلبات ISO لمشغلات PDF/A إرشادات إدارة الألوان، دعم الخطوط المضمنة، وواجهة مستخدم لقراءة التعليقات المضمنة.

PDF/X هو مجموعة فرعية من معيار ISO الخاص بـ PDF. الهدف من PDF/X هو تسهيل تبادل الرسومات، وبالتالي يحتوي على مجموعة من المتطلبات المتعلقة بالطباعة التي لا تنطبق على ملفات PDF العادية.

في الحالتين، تُستخدم طريقة [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) لتخزين المستندات، بينما يجب إعداد المستندات باستخدام طريقة [convert](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    document.pages.add()
    document.convert(output_log, ap.PdfFormat.PDF_X_3, ap.ConvertErrorAction.DELETE)
    document.save(output_pdf)
```

