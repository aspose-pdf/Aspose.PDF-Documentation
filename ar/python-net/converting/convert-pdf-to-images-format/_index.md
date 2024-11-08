---
title: تحويل PDF إلى تنسيقات صور مختلفة في بايثون
linktitle: تحويل PDF إلى صور
type: docs
weight: 70
url: /ar/python-net/convert-pdf-to-images-format/
lastmod: "2022-12-23"
description: يوضّح هذا الموضوع كيفية استخدام Aspose.PDF لبايثون لتحويل PDF إلى تنسيقات صور مختلفة مثل TIFF وBMP وEMF وJPEG وPNG وGIF وSVG ببضع سطور من التعليمات البرمجية.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## نظرة عامة

توضح هذه المقالة كيفية تحويل PDF إلى تنسيقات صور مختلفة باستخدام بايثون. وهي تغطي الموضوعات التالية.

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
- [Python PDF to EMF Converter](#python-pdf-to-emf)

_تنسيق الصورة_: **JPG**
- [Python PDF إلى JPG](#python-pdf-to-jpg)
- [Python تحويل PDF إلى JPG](#python-pdf-to-jpg)
- [Python محول PDF إلى JPG](#python-pdf-to-jpg)

_تنسيق الصورة_: **PNG**
- [Python PDF إلى PNG](#python-pdf-to-png)
- [Python تحويل PDF إلى PNG](#python-pdf-to-png)
- [Python محول PDF إلى PNG](#python-pdf-to-png)

_تنسيق الصورة_: **GIF**
- [Python PDF إلى GIF](#python-pdf-to-gif)
- [Python تحويل PDF إلى GIF](#python-pdf-to-gif)
- [Python محول PDF إلى GIF](#python-pdf-to-gif)

_تنسيق الصورة_: **SVG**
- [Python PDF إلى SVG](#python-pdf-to-svg)
- [Python تحويل PDF إلى SVG](#python-pdf-to-svg)
- [Python محول PDF إلى SVG](#python-pdf-to-svg)

## تحويل PDF إلى صورة باستخدام Python

يستخدم **Aspose.PDF for Python** عدة طرق لتحويل PDF إلى صورة.
 بشكل عام، نستخدم نهجين: التحويل باستخدام نهج الجهاز والتحويل باستخدام SaveOption. ستوضح لك هذه القسم كيفية تحويل مستندات PDF إلى تنسيقات الصور مثل BMP وJPEG وGIF وPNG وEMF وTIFF وSVG باستخدام أحد هذه النهج.

هناك عدة فئات في المكتبة تتيح لك استخدام جهاز افتراضي لتحويل الصور. DocumentDevice موجه لتحويل المستند بالكامل، ولكن ImageDevice - لصفحة معينة.

## تحويل PDF باستخدام فئة DocumentDevice

**Aspose.PDF for Python** يجعل من الممكن تحويل صفحات PDF إلى صور TIFF.

تتيح لك فئة [TiffDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/) (المبنية على DocumentDevice) تحويل صفحات PDF إلى صور TIFF. توفر هذه الفئة طريقة تسمى [process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/#methods) والتي تتيح لك تحويل جميع الصفحات في ملف PDF إلى صورة TIFF واحدة.

{{% alert color="success" %}}

**حاول تحويل PDF إلى TIFF عبر الإنترنت**
Aspose.PDF لـ Python عبر .NET يقدم لك تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF من PDF إلى TIFF مع تطبيق مجاني](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### تحويل صفحات PDF إلى صورة TIFF واحدة

Aspose.PDF لـ Python يشرح كيفية تحويل جميع الصفحات في ملف PDF إلى صورة TIFF واحدة:

<a name="csharp-pdf-to-tiff"><strong>الخطوات: تحويل PDF إلى TIFF في Python</strong></a>

1. إنشاء كائن من فئة [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
2. إنشاء كائنات [TiffSettings](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffsettings/) و[TiffDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/)

3. قم باستدعاء [process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/#methods) لتحويل مستند PDF إلى TIFF.
4. لتعيين خصائص ملف الإخراج، استخدم فئة [TiffSettings](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffsettings/).

يظهر مقطع الشيفرة التالي كيفية تحويل جميع صفحات PDF إلى صورة TIFF واحدة.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_tiff.tiff"
    # افتح مستند PDF
    document = ap.Document(input_pdf)

    # إنشاء كائن Resolution
    resolution = ap.devices.Resolution(300)

    # إنشاء كائن TiffSettings
    tiffSettings = ap.devices.TiffSettings()
    tiffSettings.compression = ap.devices.CompressionType.LZW
    tiffSettings.depth = ap.devices.ColorDepth.DEFAULT
    tiffSettings.skip_blank_pages = False

    # إنشاء جهاز TIFF
    tiffDevice = ap.devices.TiffDevice(resolution, tiffSettings)

    # تحويل صفحة معينة وحفظ الصورة إلى التدفق
    tiffDevice.process(document, output_pdf)
```


## تحويل PDF باستخدام فئة ImageDevice

`ImageDevice` هو السلف لـ `BmpDevice`، `JpegDevice`، `GifDevice`، `PngDevice` و `EmfDevice`.

- تتيح لك فئة [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) تحويل صفحات PDF إلى صور <abbr title="Bitmap Image File">BMP</abbr>.
- تتيح لك فئة [EmfDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/emfdevice/) تحويل صفحات PDF إلى صور <abbr title="Enhanced Meta File">EMF</abbr>.
- تتيح لك فئة [JpegDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/jpegdevice/) تحويل صفحات PDF إلى صور JPEG.
- تتيح لك فئة [PngDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/pngdevice/) تحويل صفحات PDF إلى صور <abbr title="Portable Network Graphics">PNG</abbr>.

- تتيح لك فئة [GifDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/gifdevice/) تحويل صفحات PDF إلى صور <abbr title="Graphics Interchange Format">GIF</abbr>.

لنلقِ نظرة على كيفية تحويل صفحة PDF إلى صورة.

توفر فئة [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) طريقة باسم [process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/#methods) التي تتيح لك تحويل صفحة معينة من ملف PDF إلى تنسيق صورة BMP. الفئات الأخرى لديها نفس الطريقة. لذا، إذا كنا بحاجة إلى تحويل صفحة PDF إلى صورة، فنحن نقوم بإنشاء نسخة من الفئة المطلوبة.

الخطوات التالية ومقتطف الكود في بايثون يوضح هذه الإمكانية

- [تحويل PDF إلى BMP في بايثون](#python-pdf-to-image)
- [تحويل PDF إلى EMF في بايثون](#python-pdf-to-image)
- [تحويل PDF إلى JPG في بايثون](#python-pdf-to-image)
- [تحويل PDF إلى PNG في بايثون](#python-pdf-to-image)
- [تحويل PDF إلى GIF في بايثون](#python-pdf-to-image)

<a name="csharp-pdf-to-image"><strong>الخطوات: تحويل PDF إلى صورة (BMP, EMF, JPG, PNG, GIF) في بايثون</strong></a>

1. قم بتحميل ملف PDF باستخدام فئة [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
2. قم بإنشاء مثيل لفئة فرعية من [ImageDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/imagedevice/) مثل:
   * [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) (لتحويل PDF إلى BMP)
   * [EmfDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/emfdevice/) (لتحويل PDF إلى Emf)
   * [JpegDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/jpegdevice/) (لتحويل PDF إلى JPG)
   * [PngDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/pngdevice/) (لتحويل PDF إلى PNG)
   * [GifDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/gifdevice/) (لتحويل PDF إلى GIF)
3. قم باستدعاء طريقة [ImageDevice.Process()](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/imagedevice/#methods) لتنفيذ تحويل PDF إلى صورة.

### تحويل PDF إلى BMP

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "many_pages.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_bmp"
    # فتح مستند PDF
    document = ap.Document(input_pdf)

    # إنشاء كائن Resolution
    resolution = ap.devices.Resolution(300)
    device = ap.devices.BmpDevice(resolution)

    for i in range(0, len(document.pages)):
        # إنشاء ملف للحفظ
        imageStream = io.FileIO(
            output_pdf + "_page_" + str(i + 1) + "_out.bmp", 'x'
        )
        # تحويل صفحة معينة وحفظ الصورة إلى التدفق
        device.process(document.pages[i + 1], imageStream)
        imageStream.close()
```


### تحويل PDF إلى EMF

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_emf"
    # فتح مستند PDF
    document = ap.Document(input_pdf)

    # إنشاء كائن دقة
    resolution = ap.devices.Resolution(300)
    device = ap.devices.EmfDevice(resolution)

    for i in range(0, len(document.pages)):
        # إنشاء ملف للحفظ
        imageStream = io.FileIO(
            output_pdf + "_page_" + str(i + 1) + "_out.emf", 'x'
        )
        # تحويل صفحة معينة وحفظ الصورة إلى التدفق
        device.process(document.pages[i + 1], imageStream)
        imageStream.close()
```  

### تحويل PDF إلى JPEG

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "many_pages.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_jpeg"
    # فتح مستند PDF
    document = ap.Document(input_pdf)

    # إنشاء كائن دقة
    resolution = ap.devices.Resolution(300)
    device = ap.devices.JpegDevice(resolution)

    for i in range(0, len(document.pages)):
        # إنشاء ملف للحفظ
        imageStream = io.FileIO(
            output_pdf + "_page_" + str(i + 1) + "_out.jpeg", "x"
        )
        # تحويل صفحة معينة وحفظ الصورة إلى التدفق
        device.process(document.pages[i + 1], imageStream)
        imageStream.close()  
``` 


### تحويل PDF إلى PNG

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_png"
    # فتح مستند PDF
    document = ap.Document(input_pdf)

    # إنشاء كائن دقة
    resolution = ap.devices.Resolution(300)
    device = ap.devices.PngDevice(resolution)

    for i in range(0, len(document.pages)):
        # إنشاء ملف للحفظ
        imageStream = io.FileIO(
            output_pdf + "_page_" + str(i + 1) + "_out.png", 'x'
        )
        # تحويل صفحة معينة وحفظ الصورة في الدفق
        device.process(document.pages[i + 1], imageStream)
        imageStream.close()
``` 

### تحويل PDF إلى GIF

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "many_pages.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_gif"
    # فتح مستند PDF
    document = ap.Document(input_pdf)

    # إنشاء كائن دقة
    resolution = ap.devices.Resolution(300)

    device = ap.devices.GifDevice(resolution)

    for i in range(0, len(document.pages)):
        # إنشاء ملف للحفظ
        imageStream = io.FileIO(
            output_pdf + "_page_" + str(i + 1) + "_out.gif", 'x'
        )
        # تحويل صفحة معينة وحفظ الصورة في الدفق
        device.process(document.pages[i + 1], imageStream)
        # إغلاق الدفق
        imageStream.close()  
``` 


{{% alert color="success" %}}
**حاول تحويل PDF إلى PNG عبر الإنترنت**

كمثال على كيفية عمل تطبيقاتنا المجانية، يرجى التحقق من الميزة التالية.

Aspose.PDF لـ Python يقدم لك تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![كيفية تحويل PDF إلى PNG باستخدام التطبيق المجاني](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## تحويل PDF باستخدام فئة SaveOptions

يظهر لك هذا الجزء من المقالة كيفية تحويل PDF إلى <abbr title="Scalable Vector Graphics">SVG</abbr> باستخدام Python وفئة SaveOptions.

{{% alert color="success" %}}
**حاول تحويل PDF إلى SVG عبر الإنترنت**

Aspose.PDF لـ Python عبر .NET يقدم لك تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![Aspose.PDF تحويل PDF إلى SVG باستخدام التطبيق المجاني](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**Scalable Vector Graphics (SVG)** هو عائلة من المواصفات الخاصة بتنسيق الملفات المعتمد على XML للرسومات المتجهية ثنائية الأبعاد، سواء كانت ثابتة أو ديناميكية (تفاعلية أو متحركة). إن مواصفة SVG هي معيار مفتوح تم تطويره من قبل اتحاد شبكة الويب العالمية (W3C) منذ عام 1999.

يتم تعريف صور SVG وسلوكياتها في ملفات نصية XML. هذا يعني أنها يمكن أن تُبحث، تُفهرس، تُبرمج، وإذا لزم الأمر، تُضغط. وكملفات XML، يمكن إنشاء صور SVG وتحريرها باستخدام أي محرر نصوص، ولكن غالبًا ما يكون من الأكثر ملاءمة إنشاؤها باستخدام برامج الرسم مثل Inkscape.

يدعم Aspose.PDF for Python ميزة تحويل صور SVG إلى تنسيق PDF كما يقدم القدرة على تحويل ملفات PDF إلى تنسيق SVG.
 لتلبية هذا المتطلب، تم إدخال فئة [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) إلى مساحة الأسماء Aspose.PDF. قم بإنشاء كائن من SvgSaveOptions ومرره كمعامل ثانٍ إلى طريقة [Document.Save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

يوضح المقتطف البرمجي التالي الخطوات لتحويل ملف PDF إلى تنسيق SVG باستخدام بايثون.

<a name="csharp-pdf-to-svg"><strong>الخطوات: تحويل PDF إلى SVG في بايثون</strong></a>

1. قم بإنشاء كائن من فئة [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
2. قم بإنشاء كائن [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) بالإعدادات المطلوبة.
3. استدعاء [Document.Save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) وتمرير كائن [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) لتحويل مستند PDF إلى SVG.

### تحويل PDF إلى SVG

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_svg.svg"
    # فتح مستند PDF
    document = ap.Document(input_pdf)

    # إنشاء كائن من SvgSaveOptions
    saveOptions = ap.SvgSaveOptions()

    # عدم ضغط صورة SVG إلى أرشيف Zip
    saveOptions.compress_output_to_zip_archive = False
    saveOptions.treat_target_file_name_as_directory = True

    # حفظ المخرجات في ملفات SVG
    document.save(output_pdf, saveOptions)
```