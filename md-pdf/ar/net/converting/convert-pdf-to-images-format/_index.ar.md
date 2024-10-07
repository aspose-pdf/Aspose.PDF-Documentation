---
title: تحويل PDF إلى صيغ صور مختلفة في C#
linktitle: تحويل PDF إلى صور
type: docs
weight: 70
url: /net/convert-pdf-to-images-format/
lastmod: "2021-11-01"
description: يوضح هذا الموضوع كيفية استخدام Aspose.PDF لتحويل PDF إلى صيغ صور متنوعة مثل TIFF، BMP، EMF، JPEG، PNG، GIF، SVG ببضعة أسطر من الكود.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## نظرة عامة

يشرح هذا المقال كيفية تحويل PDF إلى صيغ صور مختلفة باستخدام C#. يغطي المواضيع التالية.

_صيغة الصورة_: **TIFF**
- [C# PDF إلى TIFF](#csharp-pdf-to-tiff)
- [C# تحويل PDF إلى TIFF](#csharp-pdf-to-tiff)
- [C# تحويل صفحات مفردة أو معينة من PDF إلى TIFF](#csharp-pdf-to-tiff-pages)

_صيغة الصورة_: **BMP**
- [C# PDF إلى BMP](#csharp-pdf-to-bmp)
- [C# تحويل PDF إلى BMP](#csharp-pdf-to-bmp)
- [C# محول PDF إلى BMP](#csharp-pdf-to-bmp)

_صيغة الصورة_: **EMF**
- [C# PDF إلى EMF](#csharp-pdf-to-emf)
- [C# تحويل PDF إلى EMF](#csharp-pdf-to-emf)
- [C# محول PDF إلى EMF](#csharp-pdf-to-emf)
- [محول PDF إلى EMF بلغة C#](#csharp-pdf-to-emf)

_تنسيق الصورة_: **JPG**
- [C# PDF إلى JPG](#csharp-pdf-to-jpg)
- [C# تحويل PDF إلى JPG](#csharp-pdf-to-jpg)
- [محول PDF إلى JPG بلغة C#](#csharp-pdf-to-jpg)

_تنسيق الصورة_: **PNG**
- [C# PDF إلى PNG](#csharp-pdf-to-png)
- [C# تحويل PDF إلى PNG](#csharp-pdf-to-png)
- [محول PDF إلى PNG بلغة C#](#csharp-pdf-to-png)

_تنسيق الصورة_: **GIF**
- [C# PDF إلى GIF](#csharp-pdf-to-gif)
- [C# تحويل PDF إلى GIF](#csharp-pdf-to-gif)
- [محول PDF إلى GIF بلغة C#](#csharp-pdf-to-gif)

_تنسيق الصورة_: **SVG**
- [C# PDF إلى SVG](#csharp-pdf-to-svg)
- [C# تحويل PDF إلى SVG](#csharp-pdf-to-svg)
- [محول PDF إلى SVG بلغة C#](#csharp-pdf-to-svg)

## C# تحويل PDF إلى صورة

الشيفرة البرمجية التالية تعمل أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

**Aspose.PDF لـ .NET** يستخدم عدة طرق لتحويل PDF إلى صورة.
**Aspose.PDF لـ .NET** يستخدم عدة طرق لتحويل PDF إلى صورة.

هناك عدة فئات في المكتبة تتيح لك استخدام جهاز افتراضي لتحويل الصور. يتجه DocumentDevice لتحويل الوثيقة بأكملها، لكن ImageDevice - لصفحة معينة.

## تحويل PDF باستخدام فئة DocumentDevice

**Aspose.PDF لـ .NET** يجعل من الممكن تحويل صفحات PDF إلى صور TIFF.

تتيح لك فئة TiffDevice (المبنية على DocumentDevice) تحويل صفحات PDF إلى صور TIFF. توفر هذه الفئة طريقة تُسمى `Process` تتيح لك تحويل جميع الصفحات في ملف PDF إلى صورة TIFF واحدة.

{{% alert color="success" %}}
**جرب تحويل PDF إلى TIFF عبر الإنترنت**

يقدم Aspose.PDF لـ .NET لك تطبيق مجاني على الإنترنت ["PDF إلى TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff)، حيث يمكنك تجربة استكشاف الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF PDF إلى TIFF مع التطبيق المجاني](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}
{{% /alert %}}

### تحويل صفحات PDF إلى صورة TIFF واحدة

يشرح Aspose.PDF لـ .NET كيفية تحويل جميع الصفحات في ملف PDF إلى صورة TIFF واحدة:

<a name="csharp-pdf-to-tiff"><strong>الخطوات: تحويل PDF إلى TIFF في C#</strong></a>

1. إنشاء كائن من فئة **Document**.
2. إنشاء كائنات **TiffSettings** و **TiffDevice**
3. استدعاء طريقة **TiffDevice.Process()** لتحويل مستند PDF إلى TIFF.
4. لتعيين خصائص ملف الخروج، استخدم فئة **TiffSettings**.

يوضح الجزء التالي من الكود كيفية تحويل جميع صفحات PDF إلى صورة TIFF واحدة.

```csharp
public static void ConvertPDFtoTIFF()
{
    // فتح المستند
    Document pdfDocument = new Document(_dataDir + "PageToTIFF.pdf");

    // إنشاء كائن Resolution
    Resolution resolution = new Resolution(300);

    // إنشاء كائن TiffSettings
    TiffSettings tiffSettings = new TiffSettings
    {
        Compression = CompressionType.None,
        Depth = ColorDepth.Default,
        Shape = ShapeType.Landscape,
        SkipBlankPages = false
    };

    // إنشاء جهاز TIFF
    TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);

    // تحويل صفحة معينة وحفظ الصورة إلى تيار
    tiffDevice.Process(pdfDocument, _dataDir + "AllPagesToTIFF_out.tif");
}
```
### تحويل صفحة واحدة إلى صورة TIFF

يتيح Aspose.PDF لـ .NET تحويل صفحة معينة في ملف PDF إلى صورة TIFF، استخدم النسخة المحملة من الطريقة Process(..) التي تأخذ رقم الصفحة كمعامل للتحويل. يوضح جزء الكود التالي كيفية تحويل الصفحة الأولى من PDF إلى تنسيق TIFF.

<a name="csharp-pdf-to-tiff-pages"><strong>الخطوات: تحويل صفحة واحدة أو صفحات معينة من PDF إلى TIFF في C#</strong></a>

1. إنشاء كائن من فئة **Document**.
2. إنشاء كائنات **TiffSettings** و **TiffDevice**.
3. استدعاء الطريقة المحملة **TiffDevice.Process()** مع معاملات **fromPage** و **toPage** لتحويل صفحات مستند PDF إلى TIFF.

```csharp
public static void ConvertPDFtoTiffSinglePage()
{
    // فتح المستند
    Document pdfDocument = new Document(_dataDir + "PageToTIFF.pdf");

    // إنشاء كائن Resolution
    Resolution resolution = new Resolution(300);

    // إنشاء كائن TiffSettings
    TiffSettings tiffSettings = new TiffSettings
    {
        Compression = CompressionType.None,
        Depth = ColorDepth.Default,
        Shape = ShapeType.Landscape,
    };

    // إنشاء جهاز TIFF
    TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);

    // تحويل صفحة معينة وحفظ الصورة إلى تيار
    tiffDevice.Process(pdfDocument, 1, 1, _dataDir + "PageToTIFF_out.tif");
}
```
### استخدام خوارزمية برادلي أثناء التحويل

لقد كان Aspose.PDF لـ .NET يدعم إمكانية تحويل PDF إلى TIF باستخدام ضغط LZW، ومن ثم باستخدام AForge، يمكن تطبيق التبييض. ومع ذلك، طلب أحد العملاء أنه بالنسبة لبعض الصور، يحتاجون إلى الحصول على العتبة باستخدام Otsu، لذا فهم يرغبون أيضًا في استخدام برادلي.

```csharp
  public static void ConvertPDFtoTiffBradleyBinarization()
{
     // فتح المستند
     Document pdfDocument = new Document(_dataDir + "PageToTIFF.pdf");

    string outputImageFile = _dataDir + "resultant_out.tif";
    string outputBinImageFile = _dataDir + "37116-bin_out.tif";

    // إنشاء كائن Resolution
    Resolution resolution = new Resolution(300);
    // إنشاء كائن TiffSettings
    TiffSettings tiffSettings = new TiffSettings
    {
        Compression = CompressionType.LZW,
        Depth = Aspose.Pdf.Devices.ColorDepth.Format1bpp
    };
    // إنشاء جهاز TIFF
    TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);
    // تحويل صفحة معينة وحفظ الصورة إلى الدفق
    tiffDevice.Process(pdfDocument, outputImageFile);

    using (FileStream inStream = new FileStream(outputImageFile, FileMode.Open))
    {
        using (FileStream outStream = new FileStream(outputBinImageFile, FileMode.Create))
        {
            tiffDevice.BinarizeBradley(inStream, outStream, 0.1);
        }
    }
} 
```
## تحويل ملف PDF باستخدام فئة ImageDevice

`ImageDevice` هو الأصل لـ `BmpDevice`, `JpegDevice`, `GifDevice`, `PngDevice` و `EmfDevice`.

- تسمح لك فئة [BmpDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/bmpdevice) بتحويل صفحات PDF إلى صور <abbr title="Bitmap Image File">BMP</abbr>.
- تسمح لك فئة [EmfDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/emfdevice) بتحويل صفحات PDF إلى صور <abbr title="Enhanced Meta File">EMF</abbr>.
- تسمح لك فئة [JpegDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/jpegdevice) بتحويل صفحات PDF إلى صور JPEG.
- تسمح لك فئة [PngDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/pngdevice) بتحويل صفحات PDF إلى صور <abbr title="Portable Network Graphics">PNG</abbr>.
- تسمح لك فئة [GifDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/gifdevice) بتحويل صفحات PDF إلى صور <abbr title="Graphics Interchange Format">GIF</abbr>.

دعونا نلقي نظرة على كيفية تحويل صفحة PDF إلى صورة.
لنلقِ نظرة على كيفية تحويل صفحة PDF إلى صورة.

فئة `BmpDevice` توفر طريقة تُسمى [Process](https://reference.aspose.com/pdf/net/aspose.pdf.devices/bmpdevice/methods/process) التي تسمح لك بتحويل صفحة معينة من ملف PDF إلى صيغة صورة BMP. تمتلك الفئات الأخرى نفس الطريقة. لذا، إذا كنا بحاجة إلى تحويل صفحة PDF إلى صورة، نقوم فقط بإنشاء فئة مطلوبة.

الخطوات التالية وقطعة الكود في C# تظهر هذه الإمكانية

 - [تحويل PDF إلى BMP في C#](#csharp-pdf-to-image)
 - [تحويل PDF إلى EMF في C#](#csharp-pdf-to-image)
 - [تحويل PDF إلى JPG في C#](#csharp-pdf-to-image)
 - [تحويل PDF إلى PNG في C#](#csharp-pdf-to-image)
 - [تحويل PDF إلى GIF في C#](#csharp-pdf-to-image)

<a name="csharp-pdf-to-image"><strong>الخطوات: PDF إلى صورة (BMP, EMF, JPG, PNG, GIF) في C#</strong></a>

1.
1.
2. قم بإنشاء نسخة من الفئة الفرعية لـ **ImageDevice** مثل:
   * **BmpDevice** (لتحويل PDF إلى BMP)
   * **EmfDevice** (لتحويل PDF إلى Emf)
   * **JpegDevice** (لتحويل PDF إلى JPG)
   * **PngDevice** (لتحويل PDF إلى PNG)
   * **GifDevice** (لتحويل PDF إلى GIF)
3. استدعي طريقة **ImageDevice.Process()** لأداء تحويل PDF إلى صورة.

```csharp
public static class ExampleConvertPdfToImage
{
     private static readonly string _dataDir = @"C:\Samples\";
    // BMP, JPEG, GIF, PNG, EMF
    public static void ConvertPDFusingImageDevice()
    {
        // إنشاء كائن Resolution            
        Resolution resolution = new Resolution(300);
        BmpDevice bmpDevice = new BmpDevice(resolution);
        JpegDevice jpegDevice = new JpegDevice(resolution);
        GifDevice gifDevice = new GifDevice(resolution);
        PngDevice pngDevice = new PngDevice(resolution);
        EmfDevice emfDevice = new EmfDevice(resolution);

        Document document = new Document(_dataDir + 
            "ConvertAllPagesToBmp.pdf");
            
        ConvertPDFtoImage(bmpDevice, "bmp", document);
        ConvertPDFtoImage(jpegDevice,"jpeg", document);
        ConvertPDFtoImage(gifDevice, "gif", document);
        ConvertPDFtoImage(pngDevice, "png", document);
        ConvertPDFtoImage(emfDevice, "emf", document);
            
    }
}

public static void ConvertPDFtoImage(ImageDevice imageDevice, 
        string ext, Document pdfDocument)
{
    for (int pageCount = 1; pageCount <= pdfDocument.Pages.Count; pageCount++)
    {
        using (FileStream imageStream = 
        new FileStream($"{_dataDir}image{pageCount}_out.{ext}", 
        FileMode.Create))
        {
            // تحويل صفحة معينة وحفظ الصورة في البث
            imageDevice.Process(pdfDocument.Pages[pageCount], imageStream);

            // إغلاق البث
            imageStream.Close();
        }
    }
}
```
{{% alert color="success" %}}
**حاول تحويل PDF إلى PNG عبر الإنترنت**

كمثال على كيفية عمل تطبيقاتنا المجانية، يرجى التحقق من الميزة التالية.

يقدم لك Aspose.PDF لـ .NET تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png)، حيث يمكنك تجربة استكشاف الوظائف والجودة التي يعمل بها.

[![كيفية تحويل PDF إلى PNG باستخدام التطبيق المجاني](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## تحويل PDF باستخدام فئة SaveOptions

هذا الجزء من المقال يوضح لك كيفية تحويل PDF إلى <abbr title="Scalable Vector Graphics">SVG</abbr> باستخدام C# وفئة SaveOptions.

{{% alert color="success" %}}
**حاول تحويل PDF إلى SVG عبر الإنترنت**

يقدم لك Aspose.PDF لـ .NET تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg)، حيث يمكنك تجربة استكشاف الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF لـ PDF إلى SVG بالتطبيق المجاني](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
**رسومات الفيكتور المتجهة القابلة للتوسيع (SVG)** هي مجموعة من المواصفات لتنسيق ملف قائم على XML للرسومات المتجهة ثنائية الأبعاد، سواء كانت ثابتة أو ديناميكية (تفاعلية أو متحركة). مواصفات SVG هي معيار مفتوح تم تطويره بواسطة مجموعة الشبكة العالمية (W3C) منذ عام 1999.

تُعرف صور SVG وسلوكياتها في ملفات نصية XML. هذا يعني أنه يمكن البحث عنها، وفهرستها، وكتابة سكريبتات لها، وإذا لزم الأمر، ضغطها. كملفات XML، يمكن إنشاء صور SVG وتحريرها بأي محرر نصوص، لكن غالبًا ما يكون من الأسهل إنشاؤها باستخدام برامج الرسم مثل Inkscape.

يدعم Aspose.PDF لـ .NET ميزة تحويل صورة SVG إلى تنسيق PDF ويقدم أيضًا القدرة على تحويل ملفات PDF إلى تنسيق SVG.
Aspose.PDF لـ .NET يدعم ميزة تحويل صورة SVG إلى تنسيق PDF ويقدم أيضًا القدرة على تحويل ملفات PDF إلى تنسيق SVG.

يُظهر مقتطف الكود التالي الخطوات لتحويل ملف PDF إلى تنسيق SVG باستخدام .NET.

<a name="csharp-pdf-to-svg"><strong>الخطوات: تحويل PDF إلى SVG في C#</strong></a>

1. إنشاء كائن من الفئة **Document**.
2. إنشاء كائن **SvgSaveOptions** مع الإعدادات المطلوبة.
3. استدعاء الطريقة **Document.Save()** ومرر لها كائن **SvgSaveOptions** لتحويل وثيقة PDF إلى SVG.

```csharp
public static void ConvertPDFtoSVG()
{
    // تحميل وثيقة PDF
    Document document = new Document(System.IO.Path.Combine(_dataDir, "input.pdf"));
    // تجسيد كائن من SvgSaveOptions
    SvgSaveOptions saveOptions = new SvgSaveOptions
    {
        // عدم ضغط صورة SVG إلى أرشيف Zip
        CompressOutputToZipArchive = false,
        TreatTargetFileNameAsDirectory = true                
    };
            
    // حفظ الناتج في ملفات SVG
    document.Save(System.IO.Path.Combine(_dataDir, "PDFToSVG_out.svg"), saveOptions);
}
```

