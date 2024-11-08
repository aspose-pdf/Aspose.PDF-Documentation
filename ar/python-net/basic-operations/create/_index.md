---
title: إنشاء مستند PDF برمجياً
linktitle: إنشاء PDF
type: docs
weight: 10
url: /ar/python-net/create-document/
description: تصف هذه الصفحة كيفية إنشاء مستند PDF من الصفر باستخدام Aspose.PDF for Python عبر مكتبة .NET.
---

بالنسبة للمطورين، هناك العديد من السيناريوهات حيث يصبح من الضروري توليد ملفات PDF برمجياً. قد تحتاج إلى توليد تقارير PDF وملفات PDF أخرى برمجياً في برنامجك. إنه طويل وغير فعال إلى حد ما كتابة التعليمات البرمجية والوظائف الخاصة بك من الصفر. لإنشاء ملف PDF باستخدام Python، هناك حل أفضل - **Aspose.PDF for Python عبر .NET**.

## كيفية إنشاء ملف PDF باستخدام Python

لإنشاء ملف PDF باستخدام Python، يمكن استخدام الخطوات التالية.

1. إنشاء كائن من فئة [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)

1. أضف كائن [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) إلى مجموعة [Pages](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) لكائن الوثيقة
1. أضف [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) إلى مجموعة [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) في الصفحة
1. احفظ مستند PDF الناتج

```python

    import aspose.pdf as ap

    # تهيئة كائن الوثيقة
    document = ap.Document()
    # أضف صفحة
    page = document.pages.add()
    # تهيئة كائن textfragment
    text_fragment = ap.text.TextFragment("Hello,world!")
    # أضف جزء النص للصفحة الجديدة
    page.paragraphs.add(text_fragment)
    # احفظ ملف PDF المحدّث
    document.save("output.pdf")
```