---
title: تحويل PDF إلى PowerPoint في بايثون
linktitle: تحويل PDF إلى PowerPoint
type: docs
weight: 30
url: /python-net/convert-pdf-to-powerpoint/
description: يسمح Aspose.PDF لك بتحويل PDF إلى تنسيق PPT (PowerPoint) باستخدام بايثون. هناك إمكانية لتحويل PDF إلى PPTX بالشرائح كصور.
lastmod: "2022-12-23"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## نظرة عامة

هل من الممكن تحويل ملف PDF إلى PowerPoint؟ نعم، يمكنك ذلك! وهو سهل!
توضح هذه المقالة كيفية **تحويل PDF إلى PowerPoint باستخدام بايثون**. تغطي هذه المواضيع.

_التنسيق_: **PPTX**
- [Python PDF إلى PPTX](#python-pdf-to-pptx)
- [Python تحويل PDF إلى PPTX](#python-pdf-to-pptx)
- [Python كيفية تحويل ملف PDF إلى PPTX](#python-pdf-to-pptx)

_التنسيق_: **PowerPoint**
- [Python PDF إلى PowerPoint](#python-pdf-to-powerpoint)
- [Python تحويل PDF إلى PowerPoint](#python-pdf-to-powerpoint)
- [Python كيفية تحويل ملف PDF إلى PowerPoint](#python-pdf-to-powerpoint)


## تحويل بايثون PDF إلى PowerPoint وPPTX

**Aspose.PDF for Python via .NET** يتيح لك تتبع تقدم تحويل PDF إلى PPTX.

لدينا واجهة برمجة تطبيقات تسمى Aspose.Slides والتي تقدم ميزة إنشاء وكذلك معالجة عروض PPT/PPTX. توفر هذه الواجهة أيضًا ميزة تحويل ملفات PPT/PPTX إلى تنسيق PDF. أثناء هذا التحويل، يتم تحويل الصفحات الفردية لملف PDF إلى شرائح منفصلة في ملف PPTX.

خلال تحويل PDF إلى <abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr>، يتم عرض النص كـ Text حيث يمكنك تحديده/تحديثه. يرجى ملاحظة أنه من أجل تحويل ملفات PDF إلى تنسيق PPTX، توفر Aspose.PDF فئة تسمى [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/). يتم تمرير كائن من فئة PptxSaveOptions كحجة ثانية إلى [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods). يوضح مقتطف الكود التالي عملية تحويل ملفات PDF إلى تنسيق PPTX.

## تحويل بسيط من PDF إلى PowerPoint باستخدام Python و Aspose.PDF for Python

من أجل تحويل PDF إلى PPTX، توصي Aspose.PDF for Python باستخدام خطوات الكود التالية.

<a name="csharp-pdf-to-powerpoint"><strong>الخطوات: تحويل PDF إلى PowerPoint في Python</strong></a> | <a name="csharp-pdf-to-pptx"><strong>الخطوات: تحويل PDF إلى PPTX في Python</strong></a>

1. إنشاء مثيل من فئة [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)
2. إنشاء مثيل من فئة [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/)
3. استخدام طريقة **Save** لكائن **Document** لحفظ PDF كـ PPTX

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_pptx.pptx"
    # فتح مستند PDF
    document = ap.Document(input_pdf)
    # إنشاء مثيل PptxSaveOptions
    save_option = ap.PptxSaveOptions()
    # حفظ الملف بتنسيق MS PowerPoint
    document.save(output_pdf, save_option)
```

## تحويل PDF إلى PPTX مع الشرائح كصور


{{% alert color="success" %}}
**حاول تحويل PDF إلى PowerPoint عبر الإنترنت**

يقدم لك Aspose.PDF for Python تطبيقًا مجانيًا عبر الإنترنت ["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![Aspose.PDF تحويل PDF إلى PPTX باستخدام تطبيق مجاني](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

في حال احتجت إلى تحويل مستند PDF قابل للبحث إلى PPTX كصور بدلاً من نص قابل للتحديد، يوفر Aspose.PDF هذه الميزة من خلال فئة [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/). لتحقيق ذلك، قم بتعيين خاصية [slides_as_images](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/#properties) لفئة [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) إلى 'true' كما هو موضح في نموذج الكود التالي.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf =  DIR_OUTPUT + "convert_pdf_to_pptx_with_slides_as_images.pptx"
    # افتح مستند PDF
    document = ap.Document(input_pdf)
    # إنشاء مثيل PptxSaveOptions
    save_option = ap.PptxSaveOptions()
    save_option.slides_as_images = True
    # احفظ الملف بتنسيق MS PowerPoint
    document.save(output_pdf, save_option)
```


## انظر أيضا

تغطي هذه المقالة أيضًا هذه المواضيع. الأكواد هي نفسها كما في الأعلى.

_التنسيق_: **PowerPoint**
- [كود تحويل PDF إلى PowerPoint باستخدام بايثون](#python-pdf-to-powerpoint)
- [API لتحويل PDF إلى PowerPoint باستخدام بايثون](#python-pdf-to-powerpoint)
- [التحويل البرمجي من PDF إلى PowerPoint باستخدام بايثون](#python-pdf-to-powerpoint)
- [مكتبة بايثون لتحويل PDF إلى PowerPoint](#python-pdf-to-powerpoint)
- [حفظ PDF كملف PowerPoint باستخدام بايثون](#python-pdf-to-powerpoint)
- [إنشاء PowerPoint من PDF باستخدام بايثون](#python-pdf-to-powerpoint)
- [إنشاء PowerPoint من PDF باستخدام بايثون](#python-pdf-to-powerpoint)
- [محول PDF إلى PowerPoint باستخدام بايثون](#python-pdf-to-powerpoint)

_التنسيق_: **PPTX**
- [كود تحويل PDF إلى PPTX باستخدام بايثون](#python-pdf-to-pptx)
- [API لتحويل PDF إلى PPTX باستخدام بايثون](#python-pdf-to-pptx)
- [التحويل البرمجي من PDF إلى PPTX باستخدام بايثون](#python-pdf-to-pptx)
- [مكتبة بايثون لتحويل PDF إلى PPTX](#python-pdf-to-pptx)
- [حفظ PDF كملف PPTX باستخدام بايثون](#python-pdf-to-pptx)
- [إنشاء PPTX من PDF باستخدام بايثون](#python-pdf-to-pptx)
- [إنشاء PPTX من PDF باستخدام بايثون](#python-pdf-to-pptx)
- [محول PDF إلى PPTX باستخدام بايثون](#python-pdf-to-pptx)