---
title: تحسين، ضغط أو تقليل حجم PDF في بايثون
linktitle: تحسين PDF
type: docs
weight: 30
url: /ar/python-cpp/optimize-pdf/
description: تحسين ملف PDF، تقليص جميع الصور، تقليل حجم PDF، إزالة تضمين الخطوط، إزالة الكائنات غير المستخدمة باستخدام بايثون.
lastmod: "2023-12-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

قد يحتوي مستند PDF أحيانًا على بيانات إضافية. سيساعد تقليل حجم ملف PDF على تحسين نقل الشبكة والتخزين. هذا مفيد بشكل خاص للنشر على صفحات الويب، المشاركة على الشبكات الاجتماعية، الإرسال عبر البريد الإلكتروني، أو الأرشفة في التخزين. يمكننا استخدام عدة تقنيات لتحسين PDF:

- تحسين محتوى الصفحة للتصفح عبر الإنترنت
- تقليص أو ضغط جميع الصور
- تمكين إعادة استخدام محتوى الصفحة
- دمج التدفقات المكررة
- إزالة تضمين الخطوط
- إزالة الكائنات غير المستخدمة
- إزالة أو تسطيح حقول النماذج
- إزالة أو تسطيح التعليقات التوضيحية

{{% alert color="primary" %}}

يمكن العثور على شرح مفصل لأساليب التحسين في صفحة نظرة عامة على أساليب التحسين.

{{% /alert %}}

## تحسين مستند PDF للويب

يشير التحسين، أو الخطية للويب، إلى عملية جعل ملف PDF مناسبًا لتصفحه عبر الإنترنت باستخدام متصفح ويب. لتحسين ملف للعرض على الويب:

يوضح مقتطف الشيفرة التالي كيفية تحسين مستند PDF للويب.

```python

    import AsposePDFPythonWrappers as ap

    # المسار إلى دليل المستندات.
    dataDir = "..."

    # فتح المستند
    document = ap.Document(dataDir + "OptimizeDocument.pdf")

    # تحسين للويب
    document.optimize()

    dataDir = dataDir + "OptimizeDocument_out.pdf"

    # حفظ المستند الناتج
    document.Save(dataDir)
```