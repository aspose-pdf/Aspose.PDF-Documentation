---
title: حفظ مستند PDF برمجيًا
linktitle: حفظ PDF
type: docs
weight: 30
url: /ar/python-net/save-pdf-document/
description: تعلم كيفية حفظ ملف PDF في Aspose.PDF لـ Python عبر مكتبة .NET. حفظ مستند PDF في نظام الملفات، إلى دفق، وفي تطبيقات الويب.
lastmod: "2022-12-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## حفظ مستند PDF في نظام الملفات

يمكنك حفظ مستند PDF الذي تم إنشاؤه أو التلاعب به إلى نظام الملفات باستخدام طريقة [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) من فئة [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    # إجراء بعض التلاعبات، مثل إضافة صفحة فارغة جديدة
    document.pages.add()
    document.save(output_pdf)
```

## حفظ مستند PDF إلى دفق

يمكنك أيضًا حفظ مستند PDF الذي تم إنشاؤه أو التلاعب به إلى دفق باستخدام التحميل الزائد لطرق `Save`.

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    # إجراء بعض التلاعبات، مثل إضافة صفحة فارغة جديدة
    document.pages.add()
    document.save(io.FileIO(output_pdf, 'w'))
```


## حفظ بصيغة PDF/A أو PDF/X

PDF/A هو إصدار موحد من قبل ISO لصيغة المستندات المحمولة (PDF) للاستخدام في الأرشفة والحفظ طويل الأمد للمستندات الإلكترونية. يختلف PDF/A عن PDF في أنه يحظر الميزات غير المناسبة للأرشفة طويلة الأمد، مثل ربط الخطوط (على عكس تضمين الخطوط) والتشفير. تشمل متطلبات ISO لمشاهدات PDF/A إرشادات إدارة الألوان، ودعم الخطوط المدمجة، وواجهة مستخدم لقراءة التعليقات التوضيحية المدمجة.

PDF/X هو مجموعة فرعية من معيار PDF ISO. الغرض من PDF/X هو تسهيل تبادل الرسومات، ولهذا السبب يحتوي على سلسلة من المتطلبات المتعلقة بالطباعة التي لا تنطبق على ملفات PDF القياسية.

في كلا الحالتين، يتم استخدام طريقة [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) لتخزين المستندات، بينما يجب إعداد المستندات باستخدام طريقة [convert](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    document.pages.add()
    document.convert(output_log, ap.PdfFormat.PDF_X_3, ap.ConvertErrorAction.DELETE)
    document.save(output_pdf)
```