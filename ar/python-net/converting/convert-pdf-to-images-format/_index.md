---
title: تحويل PDF إلى صيغ صور مختلفة في بايثون
linktitle: تحويل PDF إلى صور
type: docs
weight: 70
url: /ar/python-net/convert-pdf-to-images-format/
lastmod: "2025-09-27"
description: استكشف كيفية تحويل صفحات PDF إلى صور مثل PNG أو JPEG أو TIFF باستخدام Aspose.PDF في بايثون عبر .NET.
sitemap: 
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: كيفية تحويل PDF إلى صيغ صور في بايثون
Abstract: توفر هذه المقالة دليلًا شاملاً حول تحويل ملفات PDF إلى صيغ صور مختلفة باستخدام بايثون، مع الاستفادة من مكتبة Aspose.PDF للبايثون. يوضح المستند طرق تحويل ملفات PDF إلى صيغ صور تشمل TIFF و BMP و EMF و JPG و PNG و GIF و SVG. يتم مناقشة نهجين أساسيين للتحويل - استخدام نهج Device و SaveOption. يتضمن نهج Device استخدام فئات مثل `DocumentDevice` و `ImageDevice` للتحويل على مستوى المستند الكامل أو صفحة معينة. يتم تقديم خطوات مفصلة وأمثلة على أكواد بايثون لتحويل صفحات PDF إلى صيغ مختلفة مثل TIFF باستخدام `TiffDevice`، و BMP و EMF و JPEG و PNG و GIF باستخدام الفئات المناسبة (`BmpDevice`، `EmfDevice`، `JpegDevice`، `PngDevice`، `GifDevice`). بالنسبة لتحويل SVG، يتم تقديم فئة `SvgSaveOptions`. كما تسلط المقالة الضوء على الأدوات عبر الإنترنت لتجربة هذه التحويلات.
---

## بايثون تحويل PDF إلى صورة

**Aspose.PDF للبايثون** يستخدم عدة طرق لتحويل PDF إلى صورة. بشكل عام، نستخدم نهجين: التحويل باستخدام نهج Device والتحويل باستخدام SaveOption. سيعرض هذا القسم كيفية تحويل مستندات PDF إلى صيغ صور مثل BMP و JPEG و GIF و PNG و EMF و TIFF و SVG باستخدام أحد هذه النهجين.

هناك عدة فئات في المكتبة تتيح لك استخدام جهاز افتراضي لتحويل الصور. يتم توجيه DocumentDevice لتحويل المستند بالكامل، بينما يُستخدم ImageDevice لصفحة معينة.

## تحويل PDF باستخدام فئة DocumentDevice

**Aspose.PDF للبايثون** يجعل من الممكن تحويل صفحات PDF إلى صور TIFF.

تسمح لك فئة [TiffDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/) (المبنية على DocumentDevice) بتحويل صفحات PDF إلى صور TIFF. توفر هذه الفئة طريقة تسمى [process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/#methods) والتي تسمح لك بتحويل جميع الصفحات في ملف PDF إلى صورة TIFF واحدة.

{{% alert color="success" %}}
**حاول تحويل PDF إلى TIFF عبر الإنترنت**

يقدم لك Aspose.PDF للبايثون عبر .NET تطبيقًا مجانيًا عبر الإنترنت ["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff)، حيث يمكنك تجربة وظيفة وجودة الأداء.

[![تحويل Aspose.PDF من PDF إلى TIFF مع التطبيق المجاني](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### تحويل صفحات PDF إلى صورة TIFF واحدة

يوضح Aspose.PDF للبايثون كيفية تحويل جميع الصفحات في ملف PDF إلى صورة TIFF واحدة:

خطوات: تحويل PDF إلى TIFF في بايثون

1. أنشئ كائنًا من فئة [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. أنشئ كائنات [TiffSettings](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffsettings/) و [TiffDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/).
1. استدعِ طريقة [process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/#methods) لتحويل مستند PDF إلى TIFF.
1. لضبط خصائص ملف الإخراج، استخدم فئة [TiffSettings](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffsettings/).

يعرض المقتطع البرمجي التالي كيفية تحويل جميع صفحات PDF إلى صورة TIFF واحدة.

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)

    resolution = apdf.devices.Resolution(300)
    tiffSettings = apdf.devices.TiffSettings()
    tiffSettings.compression = apdf.devices.CompressionType.LZW
    tiffSettings.depth = apdf.devices.ColorDepth.DEFAULT
    tiffSettings.skip_blank_pages = False

    tiffDevice = apdf.devices.TiffDevice(resolution, tiffSettings)
    tiffDevice.process(document, path_outfile)

    print(infile + " converted into " + outfile)
```

## تحويل PDF باستخدام فئة ImageDevice

`ImageDevice` هو الفئة الأصلية لـ `BmpDevice` و `JpegDevice` و `GifDevice` و `PngDevice` و `EmfDevice`.

- تتيح لك فئة [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) تحويل صفحات PDF إلى صور <abbr title="Bitmap Image File">BMP</abbr>.
- تتيح لك فئة [EmfDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/emfdevice/) تحويل صفحات PDF إلى صور <abbr title="Enhanced Meta File">EMF</abbr>.
- تتيح لك فئة [JpegDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/jpegdevice/) تحويل صفحات PDF إلى صور JPEG.
- تتيح لك فئة [PngDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/pngdevice/) تحويل صفحات PDF إلى صور <abbr title="Portable Network Graphics">PNG</abbr>.
- تتيح لك فئة [GifDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/gifdevice/) تحويل صفحات PDF إلى صور <abbr title="Graphics Interchange Format">GIF</abbr>.

لنلقِ نظرة على كيفية تحويل صفحة PDF إلى صورة.

توفر فئة [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) طريقة تسمى [process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/#methods) والتي تسمح لك بتحويل صفحة معينة من ملف PDF إلى صيغة صورة BMP. الفئات الأخرى لها نفس الطريقة. لذا، إذا كنا بحاجة لتحويل صفحة PDF إلى صورة، فإننا نقوم بإنشاء كائن من الفئة المطلوبة.

تظهر الخطوات التالية والمقتطف البرمجي في بايثون هذه الإمكانية:

- [تحويل PDF إلى BMP في بايثون](#python-pdf-to-image)
- [تحويل PDF إلى EMF في بايثون](#python-pdf-to-image)
- [تحويل PDF إلى JPG في بايثون](#python-pdf-to-image)
- [تحويل PDF إلى PNG في بايثون](#python-pdf-to-image)
- [تحويل PDF إلى GIF في بايثون](#python-pdf-to-image)

خطوات: PDF إلى صورة (BMP, EMF, JPG, PNG, GIF) في بايثون

1. حمّل ملف PDF باستخدام فئة [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. أنشئ مثلاً لفئة فرعية من [ImageDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/imagedevice/) أي.
* [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) (لتحويل PDF إلى BMP)
* [EmfDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/emfdevice/) (لتحويل PDF إلى Emf)
* [JpegDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/jpegdevice/) (لتحويل PDF إلى JPG)
* [PngDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/pngdevice/) (لتحويل PDF إلى PNG)
* [GifDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/gifdevice/) (لتحويل PDF إلى GIF)
1. استدعِ طريقة [ImageDevice.process()](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/imagedevice/#methods) لتنفيذ تحويل PDF إلى صورة.

### تحويل PDF إلى BMP

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    resolution = apdf.devices.Resolution(300)
    device = apdf.devices.BmpDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(path_outfile + str(page_count) + "_out.bmp", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

### تحويل PDF إلى EMF

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    resolution = apdf.devices.Resolution(300)
    device = apdf.devices.EmfDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(path_outfile + str(page_count) + "_out.emf", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```  

### تحويل PDF إلى JPEG

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    resolution = apdf.devices.Resolution(300)
    device = apdf.devices.JpegDevice(resolution)
    page_count = 1

    while page_count <= len(document.pages):
        image_stream = FileIO(path_outfile + str(page_count) + "_out.jpeg", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```


### تحويل PDF إلى PNG

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    resolution = apdf.devices.Resolution(300)

    device = apdf.devices.PngDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(path_outfile + str(page_count) + "_out.png", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

### تحويل PDF إلى PNG باستخدام الخط الافتراضي

```python

    from os import path
    import aspose.pdf as ap
    from io import FileIO


    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    resolution = ap.devices.Resolution(300)

    rendering_options = ap.RenderingOptions()
    rendering_options.default_font_name = "Arial"

    device = ap.devices.PngDevice(resolution)
    device.rendering_options = rendering_options

    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(path_outfile + str(page_count) + "_out.png", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

### تحويل PDF إلى GIF

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    resolution = apdf.devices.Resolution(300)
    device = apdf.devices.GifDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(path_outfile + str(page_count) + "_out.gif", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**حاول تحويل PDF إلى PNG عبر الإنترنت**

كمثال على كيفية عمل تطبيقاتنا المجانية، يرجى إلقاء نظرة على الميزة التالية.

Aspose.PDF للـ Python يقدم لك تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), حيث يمكنك تجربة استكشاف الوظائف والجودة التي يعمل بها.

[![كيفية تحويل PDF إلى PNG باستخدام التطبيق المجاني](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## تحويل PDF باستخدام فئة SaveOptions

هذا الجزء من المقال يوضح لك كيفية تحويل PDF إلى <abbr title="Scalable Vector Graphics">SVG</abbr> باستخدام Python وفئة SaveOptions.

{{% alert color="success" %}}
**حاول تحويل PDF إلى SVG عبر الإنترنت**

Aspose.PDF للـ Python عبر .NET يقدم لك تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), حيث يمكنك تجربة استكشاف الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF من PDF إلى SVG باستخدام التطبيق المجاني](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**Scalable Vector Graphics (SVG)** هو عائلة من المواصفات لتنسيق ملف قائم على XML لرسومات المتجهات ثنائية الأبعاد، ثابتة وديناميكية (تفاعلية أو متحركة). مواصفة SVG هي معيار مفتوح يتم تطويره من قبل اتحاد الويب العالمي (W3C) منذ عام 1999.

يتم تعريف صور SVG وسلوكياتها في ملفات نصية XML. وهذا يعني أنه يمكن البحث عنها، وفهرستها، وبرمجتها، وإذا لزم الأمر، ضغطها. كملفات XML، يمكن إنشاء صور SVG وتحريرها بأي محرر نصوص، لكن غالبًا ما يكون من الأسهل إنشاءها باستخدام برامج الرسم مثل Inkscape.

يدعم Aspose.PDF للـ Python ميزة تحويل صورة SVG إلى تنسيق PDF ويقدم أيضًا القدرة على تحويل ملفات PDF إلى تنسيق SVG. لتحقيق هذا المتطلب، تم إدخال الفئة [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) في مساحة أسماء Aspose.PDF. أنشئ كائنًا من SvgSaveOptions ومرره كوسيطة ثانية إلى طريقة [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

يظهر مقتطف الكود التالي الخطوات اللازمة لتحويل ملف PDF إلى تنسيق SVG باستخدام Python.

الخطوات: تحويل PDF إلى SVG في Python

1. أنشئ كائنًا من الفئة [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. أنشئ كائن [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) بالإعدادات المطلوبة.
1. استدعِ طريقة [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) ومرّر كائن [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) لتحويل وثيقة PDF إلى SVG.

### تحويل PDF إلى SVG

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)

    save_options = apdf.SvgSaveOptions()
    save_options.compress_output_to_zip_archive = False
    save_options.treat_target_file_name_as_directory = True

    document.save(path_outfile, save_options)
    print(infile + " converted into " + outfile)
```

