---
title: تحويل PDF إلى تنسيقات صور مختلفة في بايثون
linktitle: تحويل PDF إلى صور
type: docs
weight: 70
url: ar/python-java/convert-pdf-to-images-format/
lastmod: "2023-04-06"
description: يوضح هذا الموضوع كيفية استخدام Aspose.PDF لبايثون لتحويل PDF إلى تنسيقات صور مختلفة مثل TIFF وBMP وEMF وJPEG وPNG وGIF وSVG ببضع سطور من الكود.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## نظرة عامة

تشرح هذه المقالة كيفية تحويل PDF إلى تنسيقات صور مختلفة باستخدام بايثون. يغطي الموضوعات التالية.

_تنسيق الصورة_: **TIFF**
- [تحويل PDF إلى TIFF باستخدام بايثون](#python-pdf-to-tiff)
- [تحويل PDF إلى TIFF باستخدام بايثون](#python-pdf-to-tiff)
- [تحويل صفحات معينة أو مفردة من PDF إلى TIFF باستخدام بايثون](#python-pdf-to-tiff-pages)

_تنسيق الصورة_: **BMP**
- [تحويل PDF إلى BMP باستخدام بايثون](#python-pdf-to-bmp)
- [تحويل PDF إلى BMP باستخدام بايثون](#python-pdf-to-bmp)
- [محول PDF إلى BMP باستخدام بايثون](#python-pdf-to-bmp)

_تنسيق الصورة_: **EMF**
- [تحويل PDF إلى EMF باستخدام بايثون](#python-pdf-to-emf)

- [تحويل PDF إلى EMF باستخدام بايثون](#python-pdf-to-emf)
- [محول PDF إلى EMF باستخدام بايثون](#python-pdf-to-emf)

_تنسيق الصورة_: **JPG**
- [بايثون لتحويل PDF إلى JPG](#python-pdf-to-jpg)
- [بايثون لتحويل PDF إلى JPG](#python-pdf-to-jpg)
- [محول PDF إلى JPG باستخدام بايثون](#python-pdf-to-jpg)

_تنسيق الصورة_: **PNG**
- [بايثون لتحويل PDF إلى PNG](#python-pdf-to-png)
- [بايثون لتحويل PDF إلى PNG](#python-pdf-to-png)
- [محول PDF إلى PNG باستخدام بايثون](#python-pdf-to-png)

_تنسيق الصورة_: **GIF**
- [بايثون لتحويل PDF إلى GIF](#python-pdf-to-gif)
- [بايثون لتحويل PDF إلى GIF](#python-pdf-to-gif)
- [محول PDF إلى GIF باستخدام بايثون](#python-pdf-to-gif)

_تنسيق الصورة_: **SVG**
- [بايثون لتحويل PDF إلى SVG](#python-pdf-to-svg)
- [بايثون لتحويل PDF إلى SVG](#python-pdf-to-svg)
- [محول PDF إلى SVG باستخدام بايثون](#python-pdf-to-svg)

## تحويل PDF إلى صورة باستخدام بايثون

يستخدم **Aspose.PDF for Python** عدة طرق لتحويل PDF إلى صورة.
 بشكل عام، نستخدم نهجين: التحويل باستخدام نهج الجهاز والتحويل باستخدام SaveOption. سيوضح لك هذا القسم كيفية تحويل مستندات PDF إلى تنسيقات الصور مثل BMP وJPEG وGIF وPNG وEMF وTIFF وSVG باستخدام أحد هذه النهجين.

هناك عدة فئات في المكتبة تتيح لك استخدام جهاز افتراضي لتحويل الصور. DocumentDevice موجه لتحويل المستند بأكمله، بينما ImageDevice - لصفحة معينة.

## تحويل PDF باستخدام فئة DocumentDevice

**Aspose.PDF for Python** يجعل من الممكن تحويل صفحات PDF إلى صور TIFF.

تتيح لك فئة [TiffDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/tiffdevice/) (المبنية على DocumentDevice) تحويل صفحات PDF إلى صور TIFF. توفر هذه الفئة طريقة تسمى [`Process`](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/tiffdevice/#methods) التي تتيح لك تحويل جميع الصفحات في ملف PDF إلى صورة TIFF واحدة.

{{% alert color="success" %}}

**جرب تحويل PDF إلى TIFF عبر الإنترنت**
Aspose.PDF لبايثون عبر .NET يقدم لك تطبيق مجاني عبر الإنترنت ["PDF إلى TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff)، حيث يمكنك محاولة التحقيق في الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF من PDF إلى TIFF مع التطبيق المجاني](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### تحويل صفحات PDF إلى صورة TIFF واحدة

Aspose.PDF لبايثون يشرح كيفية تحويل جميع الصفحات في ملف PDF إلى صورة TIFF واحدة:

<a name="csharp-pdf-to-tiff"><strong>الخطوات: تحويل PDF إلى TIFF في بايثون</strong></a>

1. إنشاء كائن من فئة [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/).
2. إنشاء كائنات [TiffSettings](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/tiffsettings/) و[TiffDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/tiffdevice/).

3. استدعاء طريقة [TiffDevice.Process()](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/tiffdevice/#methods) لتحويل مستند PDF إلى TIFF.  
4. لتعيين خصائص ملف الإخراج، استخدم فئة [TiffSettings](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/tiffsettings/).  

يوضح مقطع الشيفرة التالي كيفية تحويل جميع صفحات PDF إلى صورة TIFF واحدة.

```python

from asposepdf import Api, Device

# تهيئة الترخيص
documentName = "testdata/license/Aspose.PDF.PythonviaJava.lic"
licenseObject = Api.License()
licenseObject.setLicense(documentName)

# فتح مستند PDF
DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"
input_pdf = DIR_INPUT + "source.pdf"
output_image = DIR_OUTPUT + "image.tiff"
# فتح مستند PDF
document = Api.Document(input_pdf)
# إنشاء كائن دقة
resolution = Device.Resolution(300)

# إنشاء كائن إعدادات TIFF
tiffSettings = Device.TiffSettings()
tiffSettings._CompressionType = Device.CompressionType.LZW
tiffSettings._ColorDepth = Device.ColorDepth.Default
tiffSettings._Skip_blank_pages = False

# إنشاء جهاز TIFF
tiffDevice = Device.TiffDevice(resolution, tiffSettings)

# تحويل صفحة معينة وحفظ الصورة في التدفق
tiffDevice.process(document, output_image)
```


## تحويل PDF باستخدام فئة ImageDevice

`ImageDevice` هي السلف لـ `BmpDevice` و `JpegDevice` و `GifDevice` و `PngDevice` و `EmfDevice`.

- تتيح لك فئة [BmpDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/bmpdevice/) تحويل صفحات PDF إلى صور <abbr title="ملف صورة نقطية">BMP</abbr>.
- تتيح لك فئة [EmfDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/emfdevice/) تحويل صفحات PDF إلى صور <abbr title="ملف ميتا محسن">EMF</abbr>.
- تتيح لك فئة [JpegDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/jpegdevice/) تحويل صفحات PDF إلى صور JPEG.
- تتيح لك فئة [PngDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/pngdevice/) تحويل صفحات PDF إلى صور <abbr title="رسومات الشبكة المحمولة">PNG</abbr>.

- تتيح لك فئة [GifDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/gifdevice/) تحويل صفحات PDF إلى صور <abbr title="تنسيق تبادل الرسومات">GIF</abbr>.

لنلقِ نظرة على كيفية تحويل صفحة PDF إلى صورة.

توفر فئة [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) طريقة تسمى [Process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/#methods) والتي تتيح لك تحويل صفحة معينة من ملف PDF إلى تنسيق صورة BMP. تمتلك الفئات الأخرى نفس الطريقة. لذا، إذا كنا بحاجة إلى تحويل صفحة PDF إلى صورة، فإننا نقوم فقط بإنشاء مثيل للفئة المطلوبة.

<a name="csharp-pdf-to-bmp"></a>
<a name="csharp-pdf-to-emf"></a>
<a name="csharp-pdf-to-jpg"></a>
<a name="csharp-pdf-to-png"></a>
<a name="csharp-pdf-to-gif"></a>
    
توضح الخطوات التالية والمقتطف البرمجي في بايثون هذه الإمكانية
 
 - [تحويل PDF إلى BMP في بايثون](#python-pdf-to-image)
 - [تحويل PDF إلى EMF في بايثون](#python-pdf-to-image)
 - [تحويل PDF إلى JPG في بايثون](#python-pdf-to-image)
 - [تحويل PDF إلى PNG في بايثون](#python-pdf-to-image)
 - [تحويل PDF إلى GIF في بايثون](#python-pdf-to-image)


<a name="csharp-pdf-to-image"><strong>الخطوات: تحويل PDF إلى صورة (BMP, EMF, JPG, PNG, GIF) في بايثون</strong></a>

1. تحميل ملف PDF باستخدام فئة [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/).
2. إنشاء مثيل من الفئة الفرعية [ImageDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/imagedevice/) مثل:
   * [BmpDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/bmpdevice/) (لتحويل PDF إلى BMP)
   * [EmfDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/emfdevice/) (لتحويل PDF إلى Emf)
   * [JpegDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/jpegdevice/) (لتحويل PDF إلى JPG)
   * [PngDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/pngdevice/) (لتحويل PDF إلى PNG)
   * [GifDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/gifdevice/) (لتحويل PDF إلى GIF)
3. استدعاء طريقة [ImageDevice.Process()](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/imagedevice/#methods) لتنفيذ تحويل PDF إلى صورة.

### تحويل PDF إلى BMP

```python


from asposepdf import Api, Device

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"

input_pdf = DIR_INPUT + "source.pdf"
output_pdf = DIR_OUTPUT + "image"
# افتح مستند PDF
document = Api.Document(input_pdf)

# إنشاء كائن Resolution
resolution = Device.Resolution(300)
device = Device.BmpDevice(resolution)

for i in range(0, document.getPages.size):
    # إنشاء اسم ملف للحفظ
    imageFileName = output_pdf + "_page_" + str(i + 1) + "_out.bmp"
    # تحويل صفحة معينة وحفظ الصورة في الملف
    device.process(document.getPages.getPage(i + 1), outputFileName=imageFileName)
```


### تحويل PDF إلى EMF

```python

from asposepdf import Api, Device

DIR_INPUT = "../../testdata/"
DIR_OUTPUT = "../../testout/"

input_pdf = DIR_INPUT + "source.pdf"
output_pdf = DIR_OUTPUT + "image"
# فتح مستند PDF
document = Api.Document(input_pdf)

# إنشاء كائن Resolution
resolution = Device.Resolution(300)
device = Device.EmfDevice(resolution)

for i in range(0, document.getPages.size):
    # إنشاء اسم الملف للحفظ
    imageFileName = output_pdf + "_page_" + str(i + 1) + "_out.emf"
    # تحويل صفحة معينة وحفظ الصورة في الملف
    device.process(document.getPages.getPage(i + 1), outputFileName=imageFileName)
```  

### تحويل PDF إلى JPEG

```python

from asposepdf import Api, Device

DIR_INPUT = "../../testdata/"
DIR_OUTPUT = "../../testout/"

input_pdf = DIR_INPUT + "source.pdf"
output_pdf = DIR_OUTPUT + "image"
# فتح مستند PDF
document = Api.Document(input_pdf)

# إنشاء كائن Resolution
resolution = Device.Resolution(300)
device = Device.JpegDevice(resolution)

for i in range(0, document.getPages.size):
    # إنشاء اسم الملف للحفظ
    imageFileName = output_pdf + "_page_" + str(i + 1) + "_out.jpeg"
    # تحويل صفحة معينة وحفظ الصورة في الملف
    device.process(document.getPages.getPage(i + 1), outputFileName=imageFileName)
``` 


### تحويل PDF إلى PNG

```python

from asposepdf import Api, Device

DIR_INPUT = "../../testdata/"
DIR_OUTPUT = "../../testout/"

input_pdf = DIR_INPUT + "source.pdf"
output_pdf = DIR_OUTPUT + "image"
# افتح مستند PDF
document = Api.Document(input_pdf)

# إنشاء كائن الدقة
resolution = Device.Resolution(300)
device = Device.PngDevice(resolution)

for i in range(0, document.getPages.size):
    # إنشاء اسم الملف للحفظ
    imageFileName = output_pdf + "_page_" + str(i + 1) + "_out.png"
    # تحويل صفحة معينة وحفظ الصورة في الملف
    device.process(document.getPages.getPage(i + 1), outputFileName=imageFileName)
```

### تحويل PDF إلى GIF

```python

from asposepdf import Api, Device

DIR_INPUT = "../../testdata/"
DIR_OUTPUT = "../../testout/"

input_pdf = DIR_INPUT + "source.pdf"
output_pdf = DIR_OUTPUT + "image"
# افتح مستند PDF
document = Api.Document(input_pdf)

# إنشاء كائن الدقة
resolution = Device.Resolution(300)
device = Device.GifDevice(resolution)

for i in range(0, document.getPages.size):
    # إنشاء اسم الملف للحفظ
    imageFileName = output_pdf + "_page_" + str(i + 1) + "_out.gif"
    # تحويل صفحة معينة وحفظ الصورة في الملف
    device.process(document.getPages.getPage(i + 1), outputFileName=imageFileName)
```


{{% alert color="success" %}}
**حاول تحويل PDF إلى PNG عبر الإنترنت**

كمثال على كيفية عمل تطبيقاتنا المجانية، يرجى الاطلاع على الميزة التالية.

تقدم لك Aspose.PDF for Python تطبيقًا مجانيًا عبر الإنترنت ["PDF to PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![كيفية تحويل PDF إلى PNG باستخدام التطبيق المجاني](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## تحويل PDF باستخدام فئة SaveOptions

يظهر لك هذا الجزء من المقالة كيفية تحويل PDF إلى <abbr title="رسومات متجهة قابلة للتوسع">SVG</abbr> باستخدام Python وفئة SaveOptions.

{{% alert color="success" %}}
**حاول تحويل PDF إلى SVG عبر الإنترنت**

تقدم لك Aspose.PDF for Python عبر .NET تطبيقًا مجانيًا عبر الإنترنت ["PDF to SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![Aspose.PDF تحويل PDF إلى SVG باستخدام التطبيق المجاني](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**رسومات متجهة قابلة للتوسع (SVG)** هي عائلة من المواصفات لصيغة ملفات مبنية على XML للرسومات المتجهة ثنائية الأبعاد، سواء كانت ثابتة أو ديناميكية (تفاعلية أو متحركة). مواصفة SVG هي معيار مفتوح تم تطويره من قبل اتحاد شبكة الويب العالمية (W3C) منذ عام 1999.

يتم تعريف صور SVG وسلوكياتها في ملفات نصية XML. وهذا يعني أنه يمكن البحث عنها، وفهرستها، وبرمجتها، وضغطها إذا لزم الأمر. وكملفات XML، يمكن إنشاء وتحرير صور SVG باستخدام أي محرر نصوص، ولكن غالبًا ما يكون من الأكثر ملاءمة إنشاؤها باستخدام برامج رسم مثل Inkscape.

يدعم Aspose.PDF for Python ميزة تحويل صورة SVG إلى صيغة PDF كما يوفر القدرة على تحويل ملفات PDF إلى صيغة SVG.
  لتحقيق هذا المتطلب، تم إدخال فئة [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) في مساحة الأسماء Aspose.PDF. أنشئ كائنًا من SvgSaveOptions ومرره كمعامل ثانٍ إلى طريقة [Document.Save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

يظهر مقتطف الكود التالي الخطوات اللازمة لتحويل ملف PDF إلى تنسيق SVG باستخدام Python.

<a name="csharp-pdf-to-svg"><strong>الخطوات: تحويل PDF إلى SVG في Python</strong></a>

1. أنشئ كائنًا من فئة [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/).
2. أنشئ كائن [SvgSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/svgsaveoptions/) بالإعدادات المطلوبة.
3. استدعاء طريقة [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) وتمرير كائن [SvgSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/svgsaveoptions/) لتحويل مستند PDF إلى SVG.

### تحويل PDF إلى SVG

```python

from asposepdf import Api

documentName = "testdata/input.pdf"
doc = Api.Document(documentName, None)
documentOutName = "testout/out.svg"
doc.save(documentOutName, Api.SaveFormat.Svg)
```