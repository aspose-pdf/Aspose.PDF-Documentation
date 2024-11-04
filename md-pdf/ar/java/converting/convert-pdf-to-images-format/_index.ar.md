---
title: تحويل PDF إلى تنسيقات الصور
linktitle: تحويل PDF إلى صور
type: docs
weight: 70
url: /java/convert-pdf-to-images-format/
lastmod: "2021-11-19"
description: يوضح هذا الموضوع كيف يسمح Aspose.PDF بتحويل PDF إلى تنسيقات صور متنوعة. تحويل صفحات PDF إلى صور PNG وJPEG وBMP ببضع سطور من التعليمات البرمجية.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

**Aspose.PDF for Java** يتيح لك تحويل مستندات PDF إلى تنسيقات الصور مثل BMP وJPEG وGIF وPNG وEMF وTIFF وSVG باستخدام طريقتين. يتم التحويل باستخدام Device واستخدام SaveOption.

هناك عدة فئات في المكتبة تتيح لك استخدام جهاز افتراضي لتحويل الصور. تم تصميم DocumentDevice لتحويل المستند بالكامل، بينما ImageDevice - لصفحة معينة.

## تحويل PDF باستخدام فئة DocumentDevice

**Aspose.PDF for Java** يجعل من الممكن تحويل صفحات PDF إلى صور TIFF.

تسمح لك [فئة TiffDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffdevice) بتحويل صفحات PDF إلى صور TIFF.
 هذه الفئة توفر طريقة باسم Process والتي تسمح لك بتحويل جميع الصفحات في ملف PDF إلى صورة TIFF واحدة.

### تحويل صفحات PDF إلى صورة TIFF واحدة

Aspose.PDF for Java يشرح كيفية تحويل جميع الصفحات في ملف PDF إلى صورة TIFF واحدة:

1. أنشئ كائن من فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. استدعِ طريقة [Process](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/DocumentDevice#process-com.aspose.pdf.IDocument-int-int-java.io.OutputStream-) لتحويل المستند.
1. لضبط خصائص ملف الإخراج، استخدم فئة [TiffSettings](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/TiffSettings).

يوضح مقتطف الكود التالي كيفية تحويل جميع صفحات PDF إلى صورة TIFF واحدة.

```java
// فتح المستند
String documentFileName = Paths.get(DATA_DIR.toString(), "PageToTIFF.pdf").toString();
Document document = new Document(documentFileName);

// إنشاء كائن Resolution
Resolution resolution = new Resolution(300);

// إنشاء كائن TiffSettings
TiffSettings tiffSettings = new TiffSettings();
tiffSettings.setCompression(CompressionType.None);
tiffSettings.setDepth(ColorDepth.Default);
tiffSettings.setShape(ShapeType.Landscape);
tiffSettings.setSkipBlankPages(false);

// إنشاء جهاز TIFF
TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);

// تحويل صفحة معينة وحفظ الصورة في تيار
tiffDevice.process(document, DATA_DIR + "AllPagesToTIFF_out.tif");
```

### تحويل صفحة واحدة إلى صورة TIFF

يسمح Aspose.PDF لـ Java بتحويل صفحة معينة في ملف PDF إلى صورة TIFF، استخدم نسخة محملة من طريقة Process(..) التي تأخذ رقم الصفحة كوسيطة للتحويل. يوضح مقتطف الشيفرة التالي كيفية تحويل الصفحة الأولى من PDF إلى صيغة TIFF.

```java
// افتح المستند
String documentFileName = Paths.get(DATA_DIR.toString(), "PageToTIFF.pdf").toString();
String tiffFileName = Paths.get(DATA_DIR.toString(), "PageToTIFF_out.tif").toString();
Document document = new Document(documentFileName);

// إنشاء كائن Resolution
Resolution resolution = new Resolution(300);

// إنشاء كائن TiffSettings
TiffSettings tiffSettings = new TiffSettings();
tiffSettings.setCompression(CompressionType.None);
tiffSettings.setDepth(ColorDepth.Default);
tiffSettings.setShape(ShapeType.Landscape);

// إنشاء جهاز TIFF
TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);

// تحويل صفحة معينة وحفظ الصورة في التدفق
tiffDevice.process(document, 1, 1, tiffFileName);
```


### استخدام خوارزمية برادلي أثناء التحويل

يدعم Aspose.PDF for Java ميزة تحويل PDF إلى TIFF باستخدام ضغط LZW ثم باستخدام AForge يمكن تطبيق التثنيم. ومع ذلك، طلب أحد العملاء أنه لبعض الصور، يحتاجون إلى الحصول على العتبة باستخدام Otsu، لذا يرغبون أيضًا في استخدام برادلي.

```java
// فتح المستند
String documentFileName = Paths.get(DATA_DIR.toString(), "PageToTIFF.pdf").toString();
Document document = new Document(documentFileName);

String outputImageFileName = Paths.get(DATA_DIR.toString(), "resultant_out.tif").toString();
String outputBinImageFileName = Paths.get(DATA_DIR.toString(), "tiff-bin_out.tif").toString();

java.io.OutputStream outputImageFile = new java.io.FileOutputStream(outputImageFileName);
java.io.OutputStream outputBinImageFile = new java.io.FileOutputStream(outputBinImageFileName);

// إنشاء كائن Resolution
Resolution resolution = new Resolution(300);
// إنشاء كائن TiffSettings
TiffSettings tiffSettings = new TiffSettings();
tiffSettings.setCompression(CompressionType.LZW);
tiffSettings.setDepth(ColorDepth.Format1bpp);

// إنشاء جهاز TIFF
TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);
// تحويل صفحة معينة وحفظ الصورة في التدفق
tiffDevice.process(document, outputImageFile);
outputImageFile.close();

// إنشاء كائن التدفق لحفظ الصورة الناتجة
java.io.InputStream inStream = new java.io.FileInputStream(outputImageFileName);
tiffDevice.binarizeBradley(inStream, outputBinImageFile, 0.1);
```


### تحويل صفحات PDF إلى صور TIFF متقطعة

لتحويل جميع الصفحات في ملف PDF إلى صيغة TIFF متقطعة، استخدم خيار Pixelated من IndexedConversionType

```java
// تحويل صفحات PDF إلى صور TIFF متقطعة
// لتحويل جميع الصفحات في ملف PDF إلى صيغة TIFF متقطعة، استخدم خيار Pixelated
// من IndexedConversionType.

// افتح المستند
String documentFileName = Paths.get(DATA_DIR.toString(), "PageToTIFF.pdf").toString();
Document document = new Document(documentFileName);

// أنشئ كائن تدفق لحفظ صورة المخرجات
java.io.OutputStream imageStream = new java.io.FileOutputStream("Image.tiff");

// أنشئ كائن الدقة
com.aspose.pdf.devices.Resolution resolution = new com.aspose.pdf.devices.Resolution(300);

// أنشئ كائن TiffSettings
com.aspose.pdf.devices.TiffSettings tiffSettings = new com.aspose.pdf.devices.TiffSettings();

// تعيين الضغط لصورة TIFF الناتجة
tiffSettings.setCompression(com.aspose.pdf.devices.CompressionType.CCITT4);
// تعيين عمق اللون للصورة الناتجة
tiffSettings.setDepth(com.aspose.pdf.devices.ColorDepth.Format4bpp);
// تخطي الصفحات الفارغة أثناء تحويل PDF إلى TIFF
tiffSettings.setSkipBlankPages(true);
// تعيين سطوع الصورة
tiffSettings.setBrightness(.5f);

// تعيين نوع التحويل المفهرس، القيمة الافتراضية هي بسيطة
tiffSettings.setIndexedConversionType(IndexedConversionType.Pixelated);

// أنشئ كائن TiffDevice مع دقة معينة
TiffDevice tiffDevice = new TiffDevice(2480, 3508, resolution, tiffSettings);

// تحويل صفحة معينة (الصفحة 1) وحفظ الصورة في التدفق
tiffDevice.process(document, 1, 1, imageStream);

// إغلاق التدفق
imageStream.close();
```


{{% alert color="success" %}}
**حاول تحويل PDF إلى TIFF عبر الإنترنت**

يقدم لك Aspose.PDF for Java تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF من PDF إلى TIFF باستخدام التطبيق المجاني](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

## تحويل PDF باستخدام فئة ImageDevice

`ImageDevice` هو السلف لفئات `BmpDevice`، `JpegDevice`، `GifDevice`، `PngDevice` و `EmfDevice`.

- تسمح لك فئة [BmpDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/BmpDevice) بتحويل صفحات PDF إلى صور <abbr title="ملف صورة نقطية">BMP</abbr>.
- تسمح لك فئة [EmfDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/EmfDevice) بتحويل صفحات PDF إلى صور <abbr title="ملف ميتا معزز">EMF</abbr>.

- تسمح لك فئة [JpegDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/JpegDevice) بتحويل صفحات PDF إلى صور JPEG.
- تتيح لك فئة [PngDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/PngDevice) تحويل صفحات PDF إلى صور <abbr title="رسومات الشبكة المحمولة">PNG</abbr>.
- تتيح لك فئة [GifDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/GifDevice) تحويل صفحات PDF إلى صور <abbr title="تنسيق تبادل الرسومات">GIF</abbr>.

لنلقِ نظرة على كيفية تحويل صفحة PDF إلى صورة.

توفر فئة [BmpDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/BmpDevice) طريقة باسم [Process](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/BmpDevice#process-com.aspose.pdf.Page-com.aspose.ms.System.Drawing.Graphics-) والتي تتيح لك تحويل صفحة معينة من ملف PDF إلى تنسيق صورة BMP. تحتوي الفئات الأخرى على نفس الطريقة. لذا، إذا كنا بحاجة إلى تحويل صفحة PDF إلى صورة، فإننا نقوم فقط بإنشاء نسخة من الفئة المطلوبة.

يوضح مقتطف الشيفرة التالي هذا الاحتمال:

```java
package com.aspose.pdf.examples.conversion;

import com.aspose.pdf.Document;
import com.aspose.pdf.devices.*;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

/**
 * تحويل PDF إلى صورة.
 */
public final class ConvertPDFtoImage {
    private static final Path DATA_DIR = Paths.get("/home/aspose/pdf-examples/Samples");

    private ConvertPDFtoImage() {

    }

    public static void run() throws IOException {
        runConvertPdfUsingImageDevice();
    }

    public static void runConvertPdfUsingImageDevice() throws IOException {
        // إنشاء كائن Resolution
        Resolution resolution = new Resolution(300);
        BmpDevice bmpDevice = new BmpDevice(resolution);
        JpegDevice jpegDevice = new JpegDevice(resolution);
        GifDevice gifDevice = new GifDevice(resolution);
        PngDevice pngDevice = new PngDevice(resolution);
        EmfDevice emfDevice = new EmfDevice(resolution);

        Document document = new Document(DATA_DIR + "ConvertAllPagesToBmp.pdf");

        convertPDFtoImages(bmpDevice, "bmp", document);
        convertPDFtoImages(jpegDevice, "jpeg", document);
        convertPDFtoImages(gifDevice, "gif", document);
        convertPDFtoImages(pngDevice, "png", document);
        convertPDFtoImages(emfDevice, "emf", document);
    }

    public static void convertPDFtoImages(
            ImageDevice imageDevice,
            String ext,
            Document document)
            throws IOException {
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            java.io.OutputStream imageStream = new java.io.FileOutputStream(
                    DATA_DIR + "image" + pageCount + "_out." + ext);
            // تحويل صفحة معينة وحفظ الصورة إلى المجرى
            imageDevice.process(document.getPages().get_Item(pageCount), imageStream);

            // إغلاق المجرى
            imageStream.close();
        }
    }
}
```


{{% alert color="success" %}}
**حاول تحويل PDF إلى PNG عبر الإنترنت**

كمثال على كيفية عمل تطبيقاتنا المجانية، يرجى التحقق من الميزة التالية.

يقدم لك Aspose.PDF for Java تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![كيفية تحويل PDF إلى PNG باستخدام التطبيق المجاني](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## تحويل PDF باستخدام فئة SaveOptions

يوضح لك هذا الجزء من المقالة كيفية تحويل PDF إلى <abbr title="رسومات متجهة قابلة للتوسع">SVG</abbr> باستخدام جافا وفئة SaveOptions.

{{% alert color="success" %}}
**حاول تحويل PDF إلى SVG عبر الإنترنت**

يقدم لك Aspose.PDF for Java تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF من PDF إلى SVG باستخدام التطبيق المجاني](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**رسومات المتجهات القابلة للتوسع (SVG)** هي مجموعة من المواصفات لصيغة ملف تعتمد على XML للرسومات المتجهة ثنائية الأبعاد، سواء كانت ثابتة أو ديناميكية (تفاعلية أو متحركة). تعتبر مواصفات SVG معيارًا مفتوحًا قيد التطوير من قبل اتحاد شبكة الويب العالمية (W3C) منذ عام 1999.

يتم تعريف صور SVG وسلوكياتها في ملفات نصية بصيغة XML. هذا يعني أنه يمكن البحث فيها، وفهرستها، وبرمجتها، وضغطها إذا لزم الأمر. وكملفات XML، يمكن إنشاء وتحرير صور SVG باستخدام أي محرر نصوص، ولكن من الأكثر ملاءمة غالبًا إنشاؤها باستخدام برامج رسم مثل Inkscape.

### تحويل صفحات PDF إلى صور SVG

يدعم Aspose.PDF for Java ميزة تحويل ملفات PDF إلى صيغة SVG.
 لتلبية هذا المتطلب، تم تقديم فئة [SvgSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/SvgSaveOptions) في الحزمة com.aspose.pdf. قم بإنشاء كائن من [SvgSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/SvgSaveOptions) ومرره كوسيط ثانٍ إلى طريقة [Document.save(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

يظهر مقطع الشيفرة التالي الخطوات اللازمة لتحويل ملف PDF إلى تنسيق SVG.

```java
package com.aspose.pdf.examples.conversion;

import com.aspose.pdf.Document;
import com.aspose.pdf.SvgSaveOptions;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

/**
 * تحويل PDF إلى SVG.
 */
public class ConvertPDFtoSVG {
    // المسار إلى دليل المستندات.
    private static final Path DATA_DIR = Paths.get("/home/aspose/pdf-examples/Samples");

    private ConvertPDFtoSVG() {

    }

    public static void run() throws IOException {
        String pdfFileName = Paths.get(DATA_DIR.toString(), "input.pdf").toString();
        String svgFileName = Paths.get(DATA_DIR.toString(), "PDFToSVG_out.svg").toString();

        // تحميل مستند PDF
        Document document = new Document(pdfFileName);

        // إنشاء كائن من SvgSaveOptions
        SvgSaveOptions saveOptions = new SvgSaveOptions();

        // عدم ضغط صورة SVG إلى أرشيف Zip
        saveOptions.setCompressOutputToZipArchive(false);

        // حفظ المخرجات في ملفات SVG
        document.save(svgFileName, saveOptions);
        document.close();
    }
}
```