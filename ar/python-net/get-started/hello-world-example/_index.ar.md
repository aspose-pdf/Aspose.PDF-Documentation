---
title: مثال Hello World باستخدام بايثون
linktitle: مثال Hello World
type: docs
weight: 20
url: /python-net/hello-world-example/
description: يوضح هذا المثال كيفية إنشاء مستند PDF بسيط يحتوي على نص Hello World باستخدام Aspose.PDF لـ Python عبر .NET.
lastmod: "2022-12-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

مثال "Hello World" يظهر أبسط بناء جملة وأبسط برنامج في أي لغة برمجة معينة. يتم تعريف المطورين على بناء جملة لغة البرمجة الأساسية من خلال تعلم كيفية طباعة "Hello World" على شاشة الجهاز. لذلك، سنبدأ تقليديًا تعارفنا مع مكتبتنا من خلالها.

في هذه المقالة، نقوم بإنشاء مستند PDF يحتوي على نص "Hello World!". بعد تثبيت **Aspose.PDF لـ Python عبر .NET** في بيئتك، يمكنك تنفيذ نموذج الكود أدناه لمعرفة كيفية عمل Aspose.PDF API.

يتبع نموذج الكود أدناه هذه الخطوات:

1. إنشاء كائن [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)
1. إضافة [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) إلى كائن الوثيقة
1. إنشاء كائن [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/)
1. إضافة TextFragment إلى مجموعة [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) الخاصة بالصفحة
1. [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) المستند PDF الناتج

الشفرة التالية هي برنامج "Hello World" لعرض كيفية عمل Aspose.PDF لبايثون عبر .NET API.

```python

    import aspose.pdf as ap

    # تهيئة كائن الوثيقة
    document = ap.Document()
    # إضافة صفحة
    page = document.pages.add()
    # تهيئة كائن textfragment
    text_fragment = ap.text.TextFragment("Hello,world!")
    # إضافة جزء النص إلى الصفحة الجديدة
    page.paragraphs.add(text_fragment)
    # حفظ ملف PDF المحدث
    document.save("output.pdf")
```