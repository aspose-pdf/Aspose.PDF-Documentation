---
title: إنشاء مستند PDF برمجيًا
linktitle: إنشاء PDF
type: docs
weight: 10
url: /ar/python-net/create-document/
description: تصف هذه الصفحة كيفية إنشاء مستند PDF من الصفر باستخدام مكتبة Aspose.PDF للبايثون عبر .NET.
TechArticle: true
AlternativeHeadline: إنشاء ملفات PDF باستخدام Aspose.PDF للبايثون
Abstract: في تطوير البرمجيات، يُعد إنشاء ملفات PDF برمجيًا مطلبًا شائعًا، خاصةً لإنشاء التقارير وغيرها من المستندات. كتابة كود مخصص لهذه المهمة قد تكون غير فعّالة وتستغرق وقتًا طويلاً. بدلاً من ذلك، يمكن للمطورين الاستفادة من **Aspose.PDF للبايثون عبر .NET**، وهو حل قوي لإنشاء ملفات PDF باستخدام بايثون. يتضمن العملية إنشاء كائن `Document`، وإضافة كائن `Page` إلى مجموعة `Pages` في المستند، وإدراج `TextFragment` في مجموعة `paragraphs` للصفحة، ثم حفظ المستند. يوضح مقتطف كود بايثون نمطياً هذه الخطوات، مظهرًا السهولة التي يمكن بها توليد ملفات PDF باستخدام Aspose.PDF.
---

بالنسبة للمطورين، هناك العديد من السيناريوهات التي يصبح فيها من الضروري إنشاء ملفات PDF برمجيًا. قد تحتاج إلى إنشاء تقارير PDF وغيرها من ملفات PDF في برنامجك برمجيًا. إن كتابة الكود والوظائف الخاصة بك من الصفر يستغرق وقتًا طويلاً وغير فعال. لإنشاء ملف PDF باستخدام بايثون، هناك حل أفضل - **Aspose.PDF للبايثون عبر .NET**.

## كيفية إنشاء ملف PDF باستخدام بايثون

لإنشاء ملف PDF باستخدام بايثون، يمكن استخدام الخطوات التالية.

1. إنشاء كائن من فئة [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) class
1. إضافة كائن [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) إلى مجموعة [Pages](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) لكائن Document
1. إضافة [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) إلى مجموعة [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) للصفحة
1. حفظ مستند PDF الناتج

```python

    import aspose.pdf as ap

    # Initialize document object
    document = ap.Document()
    # Add page
    page = document.pages.add()
    # Initialize textfragment object
    text_fragment = ap.text.TextFragment("Hello,world!")
    # Add text fragment to new page
    page.paragraphs.add(text_fragment)
    # Save updated PDF
    document.save("output.pdf")
```



