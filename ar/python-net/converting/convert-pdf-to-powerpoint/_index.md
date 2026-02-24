---
title: تحويل PDF إلى PowerPoint في Python
linktitle: تحويل PDF إلى PowerPoint
type: docs
weight: 30
url: /ar/python-net/convert-pdf-to-powerpoint/
description: تعرف على كيفية تحويل ملفات PDF بسهولة إلى عروض PowerPoint باستخدام Aspose.PDF لـ Python عبر .NET. دليل خطوة بخطوة للتحويل السلس من PDF إلى PPTX.
lastmod: "2025-09-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية تحويل PDF إلى PowerPoint باستخدام Python
Abstract: يوفر هذا المقال دليلًا شاملًا حول تحويل ملفات PDF إلى عروض PowerPoint باستخدام Python، مع التركيز بشكل خاص على تنسيق PPTX. يقدم استخدام Aspose.PDF لـ Python عبر .NET، الذي يسهل عملية التحويل من خلال السماح بتحويل صفحات PDF إلى شرائح فردية في ملف PPTX. يوضح المقال الخطوات اللازمة للتحويل، بما في ذلك إنشاء مثيلات من الفئات Document و PptxSaveOptions واستخدام طريقة Save. بالإضافة إلى ذلك، يسلط الضوء على ميزة تحويل ملفات PDF إلى PPTX مع الشرائح كصور عن طريق تعيين خاصية محددة في PptxSaveOptions. يتم توفير مقتطفات كود لتوضيح عملية التحويل. كما يشير المقال إلى تطبيق онлайн لاختبار ميزة تحويل PDF إلى PPTX، مما يمنح المستخدمين تجربة عملية. علاوة على ذلك، يسرد مجموعة من المواضيع والوظائف ذات الصلة المتاحة في هذا السياق، مؤكدًا على مرونة والنهج البرمجي في التعامل مع تحويل PDF إلى PowerPoint باستخدام Python.
---

## تحويل PDF إلى PowerPoint و PPTX باستخدام Python

**Aspose.PDF for Python via .NET** يتيح لك تتبع تقدم تحويل PDF إلى PPTX.

لدينا واجهة برمجة تطبيقات تسمى Aspose.Slides تقدم ميزة إنشاء وتعديل عروض PPT/PPTX. كما توفر هذه الواجهة ميزة تحويل ملفات <abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr> إلى تنسيق PDF. خلال هذا التحويل، يتم تحويل صفحات ملف PDF الفردية إلى شرائح منفصلة في ملف PPTX.

أثناء تحويل PDF إلى PPTX، يتم عرض النص كـ Text حيث يمكنك تحديده/تحديثه. يرجى ملاحظة أنه لتحويل ملفات PDF إلى تنسيق PPTX، توفر Aspose.PDF فئة تسمى [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/). يتم تمرير كائن من فئة PptxSaveOptions كمعامل ثانٍ إلى الدالة [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods). يوضح مقتطف الكود التالي عملية تحويل ملفات PDF إلى تنسيق PPTX.

## تحويل بسيط من PDF إلى PowerPoint باستخدام Python و Aspose.PDF for Python عبر .NET

لتحويل PDF إلى PPTX، توصي Aspose.PDF for Python باستخدام خطوات الشيفرة التالية.

خطوات: تحويل PDF إلى PowerPoint باستخدام Python

1. إنشاء مثيل من فئة [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. إنشاء مثيل من فئة [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/).
1. استدعاء طريقة [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.PptxSaveOptions()
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

## تحويل PDF إلى PPTX مع الشرائح كصور

{{% alert color="success" %}}
**جرّب تحويل PDF إلى PowerPoint عبر الإنترنت**

تقدم لك Aspose.PDF تطبيقًا مجانيًا عبر الإنترنت ["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx)، حيث يمكنك تجربة الوظيفة وجودتها.


[![تحويل Aspose.PDF من PDF إلى PPTX مع تطبيق مجاني](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

في حال كنت بحاجة إلى تحويل PDF قابل للبحث إلى PPTX كصور بدلاً من النص القابل للتحديد، توفر Aspose.PDF هذه الميزة عبر فئة [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/). لتحقيق ذلك، اضبط الخاصية [slides_as_images](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/#properties) في فئة [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) إلى 'true' كما هو موضح في مثال الشيفرة التالي.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.PptxSaveOptions()
    save_options.slides_as_images = True

    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

## تحويل PDF إلى PPTX مع دقة صورة مخصصة

تحول هذه الطريقة مستند PDF إلى ملف PowerPoint (PPTX) مع ضبط دقة صورة مخصصة (300 DPI) لتحسين الجودة.

1. تحميل PDF إلى كائن 'ap.Document'.
1. إنشاء مثيل من 'PptxSaveOptions'.
1. ضبط خاصية 'image_resolution' إلى 300 DPI للحصول على عرض عالي الجودة.
1. حفظ PDF كملف PPTX باستخدام خيارات الحفظ المحددة.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.PptxSaveOptions()
    save_options.image_resolution = 300

    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

