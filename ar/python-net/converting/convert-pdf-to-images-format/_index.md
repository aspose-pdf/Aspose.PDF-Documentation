---
title: تحويل PDF إلى تنسيقات الصور في Python
linktitle: تحويل PDF إلى صور
type: docs
weight: 70
url: /ar/python-net/convert-pdf-to-images-format/
lastmod: "2026-06-11"
description: تعرف على كيفية عرض صفحات PDF كملفات TIFF و BMP و EMF و JPEG و PNG و GIF و SVG في بايثون باستخدام Aspose.PDF لبيثون عبر .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: تحويل صفحات PDF إلى ملفات TIFF وPNG وJPEG وGIF وBMP وEMF وSVG بلغة بايثون
Abstract: توضح هذه المقالة كيفية تحويل ملفات PDF إلى تنسيقات الصور الشائعة باستخدام Aspose.PDF لـ Python عبر .NET. ويغطي تصدير TIFF على مستوى المستند باستخدام «TIFFDevice»، وإنشاء الصور النقطية لكل صفحة باستخدام الفئات الفرعية «ImageDevice» مثل «BMPDevice» و «JPEGDevice» و «PNGDevice» و «GIFDevice» و «EMFDevice»، وتصدير المتجهات إلى SVG باستخدام «SVGsaveOptions». يتضمن كل قسم الخطوات الأساسية وأمثلة Python اللازمة لحفظ محتوى PDF كإخراج للصورة.
---

## بايثون: تحويل PDF إلى صورة

**Aspose.pdf لبايثون عبر .NET** يدعم عدة طرق لتحويل محتوى PDF إلى صور. من الناحية العملية، تستخدم معظم عمليات سير العمل أحد الخيارين التاليين:

- أسلوب الجهاز لعرض صفحات PDF إلى تنسيقات الصور النقطية
- أسلوب SaveOptions لتصدير محتوى PDF إلى SVG

توضح هذه المقالة كيفية تحويل ملفات PDF إلى TIFF و BMP و EMF و JPEG و PNG و GIF و SVG.

تتضمن المكتبة فئات عرض متعددة. `DocumentDevice` تم تصميمه لتحويل المستند بالكامل، بينما `ImageDevice` يستهدف الصفحات الفردية.

## تحويل PDF باستخدام فئة Document/Device

استخدم `DocumentDevice` عندما تريد عرض ملف PDF بأكمله في ملف TIFF واحد متعدد الصفحات.

ال [جهاز TIFF](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/) يعتمد الفصل على `DocumentDevice` ويوفر [معالجة](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/#methods) طريقة لتحويل جميع الصفحات في ملف PDF إلى إخراج TIFF واحد.

{{% alert color="success" %}}
** حاول تحويل PDF إلى TIFF عبر الإنترنت**

Aspose.PDF لبيثون عبر.NET يقدم لك التطبيق عبر الإنترنت [«PDF إلى TIFF»](https://products.aspose.app/pdf/conversion/pdf-to-tiff)، حيث يمكنك محاولة التحقق من الوظائف والجودة التي تعمل بها.

[![تحويل ملف Aspose.PDF إلى TIFF مع التطبيق](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### تحويل صفحات PDF إلى صورة TIFF واحدة

يمكن لـ Aspose.PDF لـ Python عبر .NET عرض كل صفحة في ملف PDF في صورة TIFF واحدة.

الخطوات: تحويل PDF إلى TIFF في بايثون

1. قم بتحميل ملف PDF المصدر باستخدام [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) فئة.
1. ابتكر [إعدادات TIFF](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffsettings/) و [جهاز TIFF](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/) الكائنات.
1. قم بتكوين خيارات TIFF مثل الضغط وعمق الألوان ومعالجة الصفحات الفارغة.
1. اتصل بـ [معالجة](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/#methods) طريقة لكتابة ملف TIFF.

يوضح مقتطف الشفرة التالي كيفية تحويل جميع صفحات PDF إلى صورة TIFF واحدة.

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_TIFF(infile, outfile):
    document = ap.Document(infile)

    resolution = ap.devices.Resolution(300)
    tiffSettings = ap.devices.TiffSettings()
    tiffSettings.compression = ap.devices.CompressionType.LZW
    tiffSettings.depth = ap.devices.ColorDepth.DEFAULT
    tiffSettings.skip_blank_pages = False

    tiffDevice = ap.devices.TiffDevice(resolution, tiffSettings)
    tiffDevice.process(document, f"{outfile}.tiff")

    print(infile + " converted into " + outfile)
```

## تحويل ملفات PDF باستخدام فئة جهاز الصورة/الجهاز

استخدم `ImageDevice` عندما تحتاج إلى إخراج صفحة بصفحة بتنسيق صورة نقطية.

`ImageDevice` هي الفئة الأساسية لـ `BmpDevice`, `JpegDevice`, `GifDevice`, `PngDevice`، و `EmfDevice`.

- ال [جهاز BMP](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) تسمح لك الفئة بتحويل صفحات PDF إلى صور BMP.
- ال [جهاز EMF](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/emfdevice/) تسمح لك الفئة بتحويل صفحات PDF إلى صور EMF.
- ال [جهاز JPEG](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/jpegdevice/) تسمح لك الفئة بتحويل صفحات PDF إلى صور JPEG.
- ال [جهاز PNG](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/pngdevice/) يسمح لك الفصل بتحويل صفحات PDF إلى صور PNG.
- ال [جهاز GIF](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/gifdevice/) يسمح لك الفصل بتحويل صفحات PDF إلى صور GIF.

سير العمل هو نفسه لكل تنسيق: قم بتحميل المستند، قم بإنشاء الجهاز المناسب، ثم قم بمعالجة الصفحة المطلوبة.

[جهاز BMP](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) يفضح [معالجة](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/#methods) طريقة لعرض صفحة معينة كـ BMP. تتبع فئات أجهزة الصور الأخرى نفس النمط، بحيث يمكنك تبديل التنسيقات عن طريق تغيير فئة الجهاز.

توضح الروابط ونماذج التعليمات البرمجية التالية كيفية تقديم صفحات PDF إلى تنسيقات الصور الشائعة:

- [تحويل PDF إلى BMP في بايثون](#convert-pdf-to-bmp)
- [تحويل PDF إلى EMF في بايثون](#convert-pdf-to-emf)
- [تحويل PDF إلى JPEG في بايثون](#convert-pdf-to-jpeg)
- [تحويل PDF إلى PNG في بايثون](#convert-pdf-to-png)
- [تحويل PDF إلى GIF في بايثون](#convert-pdf-to-gif)

الخطوات: تحويل ملف PDF إلى صورة (BMP، EMF، JPG، PNG، GIF) بلغة بايثون

1. قم بتحميل ملف PDF باستخدام [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) فئة.
1. قم بإنشاء مثيل من المطلوب [جهاز الصورة](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/imagedevice/) فئة فرعية:
    - [جهاز BMP](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) (لتحويل PDF إلى BMP)
    - [جهاز EMF](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/emfdevice/) (لتحويل PDF إلى EMF)
    - [جهاز JPEG](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/jpegdevice/) (لتحويل PDF إلى JPG)
    - [جهاز PNG](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/pngdevice/) (لتحويل PDF إلى PNG)
    - [جهاز GIF](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/gifdevice/) (لتحويل PDF إلى GIF)
1. قم بتكرار الصفحات التي تريد تصديرها.
1. اتصل بـ [جهاز الصورة. العملية ()](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/imagedevice/#methods) طريقة لحفظ كل صفحة كصورة.

### تحويل ملفات PDF إلى BMP

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_BMP(infile, outfile):
    document = ap.Document(infile)
    resolution = ap.devices.Resolution(300)
    device = ap.devices.BmpDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(outfile + str(page_count) + "_out.bmp", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

### تحويل ملفات PDF إلى EMF

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_EMF(infile, outfile):
    document = ap.Document(infile)
    resolution = ap.devices.Resolution(300)
    device = ap.devices.EmfDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(outfile + str(page_count) + "_out.emf", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```  

### تحويل ملفات PDF إلى JPEG

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_JPEG(infile, outfile):
    document = ap.Document(infile)
    resolution = ap.devices.Resolution(300)
    device = ap.devices.JpegDevice(resolution)
    page_count = 1

    while page_count <= len(document.pages):
        image_stream = FileIO(outfile + str(page_count) + "_out.jpeg", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

### تحويل ملفات PDF إلى PNG

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_PNG(infile, outfile):
    document = ap.Document(infile)
    resolution = ap.devices.Resolution(300)

    device = ap.devices.PngDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(outfile + str(page_count) + "_out.png", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1
```

### تحويل PDF إلى PNG باستخدام الخط الافتراضي

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_PNG_with_default_font(infile, outfile):
    document = ap.Document(infile)
    resolution = ap.devices.Resolution(300)

    rendering_options = ap.RenderingOptions()
    rendering_options.default_font_name = "Arial"

    device = ap.devices.PngDevice(resolution)
    device.rendering_options = rendering_options

    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(outfile + str(page_count) + "_out.png", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1
```

### تحويل ملفات PDF إلى GIF

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_GIF(infile, outfile):
    document = ap.Document(infile)
    resolution = ap.devices.Resolution(300)
    device = ap.devices.GifDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(outfile + str(page_count) + "_out.gif", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
** حاول تحويل PDF إلى PNG عبر الإنترنت**

كمثال على كيفية عمل تطبيقاتنا، يرجى التحقق من الميزة التالية.

Aspose.PDF لبيثون يقدم لك التطبيق عبر الإنترنت [«PDF إلى PNG»](https://products.aspose.app/pdf/conversion/pdf-to-png)، حيث يمكنك محاولة التحقق من الوظائف والجودة التي تعمل بها.

[![كيفية تحويل PDF إلى PNG باستخدام التطبيق](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## تحويل ملفات PDF باستخدام فئة SaveOptions

استخدم `SaveOptions` عندما تريد تصدير محتوى PDF إلى SVG.

{{% alert color="success" %}}
** حاول تحويل PDF إلى SVG عبر الإنترنت**

Aspose.PDF لبيثون عبر.NET يقدم لك التطبيق عبر الإنترنت [«PDF إلى SVG»](https://products.aspose.app/pdf/conversion/pdf-to-svg)، حيث يمكنك محاولة التحقق من الوظائف والجودة التي تعمل بها.

[![تحويل ملف Aspose.PDF إلى ملف PDF إلى SVG مع التطبيق](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**الرسومات المتجهة القابلة للتطوير (SVG) ** هي صيغة تستند إلى XML للرسومات المتجهة ثنائية الأبعاد. نظرًا لأن SVG يظل قائمًا على المتجهات، فإنه يكون مفيدًا عندما تحتاج إلى مخرجات قابلة للتطوير للويب أو واجهة المستخدم أو عمليات سير عمل التصميم.

ملفات SVG قائمة على النصوص وقابلة للبحث وسهلة المعالجة في أدوات أخرى.

يمكن لـ Aspose.PDF لبيثون عبر .NET تحويل SVG إلى PDF وتصدير صفحات PDF إلى SVG. للتحويل من PDF إلى SVG، قم بإنشاء ملف [خيارات حفظ SVG](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) اعترض وقم بتمريره إلى [حفظ المستند ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) طريقة.

توضح الخطوات التالية كيفية تحويل ملف PDF إلى SVG باستخدام Python.

الخطوات: تحويل PDF إلى SVG في بايثون

1. قم بتحميل ملف PDF المصدر باستخدام [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) فئة.
1. قم بإنشاء [خيارات حفظ SVG](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) الكائن وتكوين الخيارات المطلوبة.
1. اتصل بـ [حفظ المستند ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) الطريقة مع `SvgSaveOptions` مثيل لكتابة إخراج SVG.

### تحويل ملفات PDF إلى SVG

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_SVG(infile, outfile):
    document = ap.Document(infile)

    save_options = ap.SvgSaveOptions()
    save_options.compress_output_to_zip_archive = False
    save_options.treat_target_file_name_as_directory = True

    document.save(f"{outfile}.svg", save_options)
```

## التحويلات ذات الصلة

- [تحويل تنسيقات الصور إلى PDF](/pdf/ar/python-net/convert-images-format-to-pdf/) عندما تحتاج إلى إعادة إنشاء ملفات PDF من JPG أو PNG أو TIFF أو SVG أو مصادر صور أخرى.
- [تحويل ملفات PDF إلى HTML](/pdf/ar/python-net/convert-pdf-to-html/) للحصول على مخرجات ملائمة للمتصفح بدلاً من الصور النقطية.
- [تحويل PDF إلى تنسيقات أخرى](/pdf/ar/python-net/convert-pdf-to-other-files/) لعمليات سير عمل التصدير الخاصة بـ EPUB وMarkdown والنص وXPS.
