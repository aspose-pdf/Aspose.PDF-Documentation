---
title: تحويل PDF إلى PowerPoint في بايثون
linktitle: تحويل PDF إلى PowerPoint
type: docs
weight: 30
url: ar/python-java/convert-pdf-to-powerpoint/
description: تتيح لك Aspose.PDF تحويل PDF إلى صيغة PPT (PowerPoint) باستخدام بايثون. هناك إمكانية لتحويل PDF إلى PPTX مع الشرائح كصور.
lastmod: "2023-04-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## نظرة عامة

هل من الممكن تحويل ملف PDF إلى PowerPoint؟ نعم، يمكنك ذلك! وهو سهل!
تشرح هذه المقالة كيفية **تحويل PDF إلى PowerPoint باستخدام بايثون**. وتغطي هذه المواضيع.

_الصيغة_: **PPTX**
- [بايثون PDF إلى PPTX](#python-pdf-to-pptx)
- [بايثون تحويل PDF إلى PPTX](#python-pdf-to-pptx)
- [بايثون كيفية تحويل ملف PDF إلى PPTX](#python-pdf-to-pptx)

_الصيغة_: **PowerPoint**
- [بايثون PDF إلى PowerPoint](#python-pdf-to-powerpoint)
- [بايثون تحويل PDF إلى PowerPoint](#python-pdf-to-powerpoint)
- [بايثون كيفية تحويل ملف PDF إلى PowerPoint](#python-pdf-to-powerpoint)

## تحويل PDF إلى PowerPoint و PPTX باستخدام بايثون

**Aspose.PDF for Python عبر Java** يتيح لك تتبع تقدم تحويل PDF إلى PPTX.

لدينا واجهة برمجة تطبيقات تسمى Aspose.Slides والتي تقدم ميزة إنشاء وكذلك تعديل عروض PPT/PPTX التقديمية. توفر هذه الواجهة أيضًا ميزة تحويل ملفات PPT/PPTX إلى تنسيق PDF. خلال هذا التحويل، يتم تحويل الصفحات الفردية لملف PDF إلى شرائح منفصلة في ملف PPTX.

خلال تحويل PDF إلى <abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr>، يتم عرض النص كنص حيث يمكنك تحديده/تحديثه. يرجى ملاحظة أنه من أجل تحويل ملفات PDF إلى تنسيق PPTX، توفر Aspose.PDF فئة تسمى [`PptxSaveOptions`](https://reference.aspose.com/pdf/java/aspose.pdf/pptxsaveoptions). يتم تمرير كائن من فئة PptxSaveOptions كوسيطة ثانية إلى [`Document.Save(..) method`](https://reference.aspose.com/pdf/java/aspose.pdf/document/methods/save). يظهر مقتطف الشيفرة التالي عملية تحويل ملفات PDF إلى تنسيق PPTX.

## تحويل بسيط من PDF إلى PowerPoint باستخدام Python وAspose.PDF for Python

من أجل تحويل PDF إلى PPTX، تنصح Aspose.PDF for Python باستخدام خطوات الكود التالية.

<a name="csharp-pdf-to-powerpoint"><strong>الخطوات: تحويل PDF إلى PowerPoint في بايثون</strong></a> | <a name="csharp-pdf-to-pptx"><strong>الخطوات: تحويل PDF إلى PPTX في بايثون</strong></a>

1. إنشاء مثيل لفئة [Document](https://reference.aspose.com/pdf/java/aspose.pdf/document)
2. إنشاء مثيل لفئة [PptxSaveOptions](https://reference.aspose.com/pdf/java/aspose.pdf/pptxsaveoptions)
3. استخدم طريقة **Save** لكائن **Document** لحفظ PDF كـ PPTX

```python

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"

input_pdf = DIR_INPUT + "Hello.pdf"
output_pdf = DIR_OUTPUT + "convert_pdf_to_pptx_with_options.pptx"
# افتح مستند PDF
document = Api.Document(input_pdf)

save_options = Api.PptxSaveOptions()
save_options._ImageResolution = 300
save_options._SeparateImages = True
save_options._OptimizeTextBoxes = True

# احفظ الملف بتنسيق مستند MS Word
document.save(output_pdf, save_options)
```


## تحويل PDF إلى PPTX مع الشرائح كصور

{{% alert color="success" %}}
**جرب تحويل PDF إلى PowerPoint عبر الإنترنت**

تقدم Aspose.PDF for Python تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx)، حيث يمكنك تجربة استكشاف الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF من PDF إلى PPTX باستخدام التطبيق المجاني](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

في حال كنت بحاجة إلى تحويل ملف PDF قابل للبحث إلى PPTX كصور بدلاً من نص قابل للتحديد، توفر Aspose.PDF هذه الميزة عبر فئة [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/pptxsaveoptions/). لتحقيق ذلك، قم بتعيين خاصية [SlidesAsImages](https://reference.aspose.com/pdf/python-java/aspose.pdf/pptxsaveoptions/#properties) لفئة [PptxSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/pptxsaveoptions/) إلى 'true' كما هو موضح في نموذج الكود التالي.

```python

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"

input_pdf = DIR_INPUT + "Hello.pdf"
output_pdf = DIR_OUTPUT + "convert_pdf_to_pptx_with_options.pptx"
# افتح مستند PDF
document = Api.Document(input_pdf)

save_options = Api.PptxSaveOptions()
save_options._ImageResolution = 300
save_options._SlidesAsImages = True

# احفظ الملف بصيغة مستند MS Word
document.save(output_pdf, save_options)
```


## انظر أيضا

هذه المقالة تغطي أيضًا هذه المواضيع. الأكواد هي نفسها كما هو مذكور أعلاه.

_التنسيق_: **PowerPoint**  
- [Python PDF to PowerPoint Code](#python-pdf-to-powerpoint)  
- [Python PDF to PowerPoint API](#python-pdf-to-powerpoint)  
- [Python PDF to PowerPoint Programmatically](#python-pdf-to-powerpoint)  
- [Python PDF to PowerPoint Library](#python-pdf-to-powerpoint)  
- [Python Save PDF as PowerPoint](#python-pdf-to-powerpoint)  
- [Python Generate PowerPoint from PDF](#python-pdf-to-powerpoint)  
- [Python Create PowerPoint from PDF](#python-pdf-to-powerpoint)  
- [Python PDF to PowerPoint Converter](#python-pdf-to-powerpoint)  

_التنسيق_: **PPTX**  
- [Python PDF to PPTX Code](#python-pdf-to-pptx)  
- [Python PDF to PPTX API](#python-pdf-to-pptx)  
- [Python PDF to PPTX Programmatically](#python-pdf-to-pptx)  
- [Python PDF to PPTX Library](#python-pdf-to-pptx)  
- [Python Save PDF as PPTX](#python-pdf-to-pptx)  
- [Python Generate PPTX from PDF](#python-pdf-to-pptx)  
- [Python Create PPTX from PDF](#python-pdf-to-pptx)  
- [Python PDF to PPTX Converter](#python-pdf-to-pptx)