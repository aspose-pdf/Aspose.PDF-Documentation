---
title: تحويل PDF إلى صيغ الصور
linktitle: تحويل PDF إلى الصور
type: docs
weight: 70
url: /php-java/convert-pdf-to-images-format/
lastmod: "2024-05-20"
description: يوضح هذا الموضوع كيف يسمح لك Aspose.PDF بتحويل PDF إلى صيغ الصور المختلفة. تحويل صفحات PDF إلى صور PNG وJPEG وBMP ببضع سطور من الشيفرة.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

**Aspose.PDF لـ PHP** يتيح لك تحويل مستندات PDF إلى صيغ الصور مثل BMP وJPEG وGIF وPNG وEMF وTIFF وSVG باستخدام طريقتين. يتم التحويل باستخدام `Device` واستخدام `SaveOption`.

هناك عدة فئات في المكتبة التي تسمح لك باستخدام جهاز افتراضي لتحويل الصور. يتم توجيه `DocumentDevice` لتحويل المستند بالكامل، ولكن `ImageDevice` - لصفحة معينة.

## تحويل PDF باستخدام فئة DocumentDevice

يجعل **Aspose.PDF لـ PHP** من الممكن تحويل صفحات PDF إلى صور TIFF.

تسمح لك [فئة TiffDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffdevice) بتحويل صفحات PDF إلى صور TIFF.
 هذه الفئة توفر طريقة باسم Process والتي تتيح لك تحويل جميع الصفحات في ملف PDF إلى صورة TIFF واحدة.

### تحويل صفحات PDF إلى صورة TIFF واحدة

Aspose.PDF for PHP يوضح كيفية تحويل جميع الصفحات في ملف PDF إلى صورة TIFF واحدة:

1. قم بإنشاء كائن من فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
2. قم باستدعاء طريقة [Process](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/DocumentDevice#process-com.aspose.pdf.IDocument-int-int-java.io.OutputStream-) لتحويل المستند.
3. لاستخدام خصائص ملف الخرج، استخدم فئة [TiffSettings](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/TiffSettings).

يظهر مقتطف الشيفرة التالي كيفية تحويل جميع صفحات PDF إلى صورة TIFF واحدة.

```php
// تحميل مستند PDF
$document = new Document($inputFile);

// إنشاء كائن TiffSettings جديد
$tiffSettings = new devices_TiffSettings();

// إزالة التعليق من الأسطر التالية لتخصيص إعدادات TIFF
// $tiffSettings->setCompression(devices_CompressionType::$NoneNone);
// $tiffSettings->setDepth(devices_ColorDepth::$DefaultDefault);
// $tiffSettings->setShape(devices_ShapeType::$Portrait);
// $tiffSettings->setSkipBlankPages(false);

// تعيين الدقة لصورة TIFF
$resolution = new devices_Resolution(300);

// إنشاء كائن TiffDevice جديد بالدقة والإعدادات المحددة
$tiffDevice = new devices_TiffDevice($resolution, $tiffSettings);

// تحويل مستند PDF إلى TIFF باستخدام TiffDevice
$tiffDevice->process($document, $outputFile);
```

### تحويل صفحة واحدة إلى صورة TIFF

تسمح Aspose.PDF لـ PHP بتحويل صفحة معينة في ملف PDF إلى صورة TIFF، باستخدام نسخة مفرطة التحميل من طريقة Process(..) التي تأخذ رقم الصفحة كمعامل للتحويل. يُظهر مقطع الكود التالي كيفية تحويل الصفحة الأولى من PDF إلى تنسيق TIFF.

```php
// تحميل مستند PDF
$document = new Document($inputFile);

// إنشاء كائن TiffSettings جديد
$tiffSettings = new devices_TiffSettings();

// قم بإلغاء تعليق السطور التالية لتخصيص إعدادات TIFF
// $tiffSettings->setCompression(devices_CompressionType::$NoneNone);
// $tiffSettings->setDepth(devices_ColorDepth::$DefaultDefault);
// $tiffSettings->setShape(devices_ShapeType::$Portrait);
// $tiffSettings->setSkipBlankPages(false);

// تعيين الدقة لصورة TIFF
$resolution = new devices_Resolution(300);

// إنشاء كائن TiffDevice جديد بالدقة والإعدادات المحددة
$tiffDevice = new devices_TiffDevice($resolution, $tiffSettings);

// تحويل مستند PDF إلى TIFF باستخدام TiffDevice
$tiffDevice->process($document, 1, 1, $outputFile);
```


### استخدام خوارزمية برادلي أثناء التحويل

يدعم Aspose.PDF لـ PHP ميزة تحويل PDF إلى TIFF باستخدام ضغط LZW ثم باستخدام AForge، يمكن تطبيق التحويل الثنائي. ومع ذلك، طلب أحد العملاء أنه لبعض الصور، يحتاجون إلى الحصول على العتبة باستخدام Otsu، لذا يرغبون أيضًا في استخدام برادلي.

```php
// إنشاء كائن TiffSettings جديد
$tiffSettings = new devices_TiffSettings();

// قم بإلغاء تعليق الأسطر التالية لتخصيص إعدادات TIFF
// $tiffSettings->setCompression(devices_CompressionType::$NoneNone);
// $tiffSettings->setDepth(devices_ColorDepth::$DefaultDefault);
// $tiffSettings->setShape(devices_ShapeType::$Portrait);
// $tiffSettings->setSkipBlankPages(false);

$outputImageFile = new java("java.io.FileOutputStream", $outputImageFileName);
$outputBinImageFile = new java("java.io.FileOutputStream", $outputBinImageFileName);

// تعيين الدقة لصورة TIFF
$resolution = new devices_Resolution(300);

// إنشاء كائن TiffDevice جديد مع الدقة والإعدادات المحددة
$tiffDevice = new devices_TiffDevice($resolution, $tiffSettings);

// تحويل مستند PDF إلى TIFF باستخدام TiffDevice
$tiffDevice->process($document, 1, 1, $outputFile);

// إنشاء كائن تدفق لحفظ صورة المخرجات
$inStream = new java("java.io.FileInputStream",$outputImageFileName);
$tiffDevice->binarizeBradley($inStream, $outputBinImageFile, 0.1);
```


### تحويل صفحات PDF إلى صور TIFF متقطعة

لتحويل جميع الصفحات في ملف PDF إلى تنسيق TIFF متقطع، استخدم خيار Pixelated من IndexedConversionType

```php
// إنشاء كائن TiffSettings جديد
$tiffSettings = new devices_TiffSettings();

// قم بإلغاء تعليق السطور التالية لتخصيص إعدادات TIFF
// $tiffSettings->setCompression(devices_CompressionType::$NoneNone);
// $tiffSettings->setDepth(devices_ColorDepth::$DefaultDefault);
// $tiffSettings->setShape(devices_ShapeType::$Portrait);
// $tiffSettings->setSkipBlankPages(false);
// ضبط سطوع الصورة
$tiffSettings->setBrightness(0.5f);
// ضبط نوع IndexedConversion، القيمة الافتراضية هي بسيطة
$tiffSettings->setIndexedConversionType(IndexedConversionType::Pixelated);


$outputImageFile = new java("java.io.FileOutputStream", $outputImageFileName);
$outputBinImageFile = new java("java.io.FileOutputStream", $outputBinImageFileName);

// ضبط الدقة لصورة TIFF
$resolution = new devices_Resolution(300);

// إنشاء كائن TiffDevice جديد مع الدقة والإعدادات المحددة
$tiffDevice = new devices_TiffDevice($resolution, $tiffSettings);

// تحويل مستند PDF إلى TIFF باستخدام TiffDevice
$tiffDevice->process($document, 1, 1, $outputFile);

// إنشاء كائن stream لحفظ الصورة الناتجة
$inStream = new java("java.io.FileInputStream",$outputImageFileName);
$tiffDevice->binarizeBradley($inStream, $outputBinImageFile, 0.1);
```


{{% alert color="success" %}}
**حاول تحويل PDF إلى TIFF عبر الإنترنت**

Aspose.PDF for PHP يقدم لك تطبيقًا مجانيًا على الإنترنت ["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF من PDF إلى TIFF باستخدام التطبيق المجاني](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

## تحويل PDF باستخدام فئة ImageDevice

`ImageDevice` هو السلف لـ `BmpDevice`، `JpegDevice`، `GifDevice`، `PngDevice` و `EmfDevice`.

- فئة [BmpDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/BmpDevice) تسمح لك بتحويل صفحات PDF إلى صور <abbr title="ملف صورة نقطية">BMP</abbr>.
- فئة [EmfDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/EmfDevice) تسمح لك بتحويل صفحات PDF إلى صور <abbr title="ملف ميتا محسن">EMF</abbr>.

- فئة [JpegDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/JpegDevice) تسمح لك بتحويل صفحات PDF إلى صور JPEG.
- تسمح لك فئة [PngDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/PngDevice) بتحويل صفحات PDF إلى صور <abbr title="Portable Network Graphics">PNG</abbr>.
- تسمح لك فئة [GifDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/GifDevice) بتحويل صفحات PDF إلى صور <abbr title="Graphics Interchange Format">GIF</abbr>.

دعونا نلقي نظرة على كيفية تحويل صفحة PDF إلى صورة.

توفر فئة [BmpDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/BmpDevice) طريقة تسمى [Process](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/BmpDevice#process-com.aspose.pdf.Page-com.aspose.ms.System.Drawing.Graphics-) والتي تسمح لك بتحويل صفحة معينة من ملف PDF إلى تنسيق صورة BMP. الفئات الأخرى لديها نفس الطريقة. لذا، إذا كنا بحاجة إلى تحويل صفحة PDF إلى صورة، فإننا نقوم فقط بإنشاء مثيل للفئة المطلوبة.

يظهر مقتطف الشيفرة التالي هذه الإمكانية:

```php
// تحميل مستند PDF
$document = new Document($inputFile);

// الحصول على مجموعة الصفحات في المستند
$pages = $document->getPages();

// الحصول على العدد الإجمالي للصفحات في المستند
$count = $pages->size();

// تعيين الدقة للصور PNG
$resolution = new devices_Resolution(300);

// إنشاء جهاز PNG جديد بالدقة المحددة
$imageDevice = new devices_PngDevice($resolution);

// تكرار عبر كل صفحة في المستند
for ($pageCount = 1; $pageCount <= $document->getPages()->size(); $pageCount++) {
    // تعيين اسم ملف الصورة الناتجة للصفحة الحالية
    $imageFileName = $imageFileNameTemplate . $pageCount . '.png';

    // الحصول على الصفحة الحالية من المجموعة
    $page = $document->getPages()->get_Item($pageCount);

    // معالجة الصفحة الحالية وحفظها كصورة PNG
    $imageDevice->process($page, $imageFileName);
}
```


{{% alert color="success" %}}
**حاول تحويل PDF إلى PNG عبر الإنترنت**

كمثال على كيفية عمل تطبيقاتنا المجانية، يرجى التحقق من الميزة التالية.

تقدم Aspose.PDF لـ PHP تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png)، حيث يمكنك محاولة التحقيق في الوظائف والجودة التي يعمل بها.

[![كيفية تحويل PDF إلى PNG باستخدام تطبيق مجاني](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## تحويل PDF باستخدام فئة SaveOptions

يُظهر لك هذا الجزء من المقالة كيفية تحويل PDF إلى <abbr title="الرسوميات المتجهة القابلة للتحجيم">SVG</abbr> باستخدام Java وفئة SaveOptions.

{{% alert color="success" %}}
**حاول تحويل PDF إلى SVG عبر الإنترنت**

تقدم Aspose.PDF لـ PHP تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg)، حيث يمكنك محاولة التحقيق في الوظائف والجودة التي يعمل بها.

[![تحويل PDF إلى SVG باستخدام تطبيق مجاني من Aspose.PDF](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**رسومات المتجهات القابلة للتوسع (SVG)** هي عائلة من المواصفات لتنسيق الملفات القائم على XML للرسومات المتجهة ثنائية الأبعاد، سواء كانت ثابتة أو ديناميكية (تفاعلية أو متحركة). مواصفة SVG هي معيار مفتوح تم تطويره من قبل اتحاد شبكة الويب العالمية (W3C) منذ عام 1999.

يتم تعريف صور SVG وسلوكياتها في ملفات نصية بصيغة XML. هذا يعني أنه يمكن البحث فيها وفهرستها وبرمجتها وضغطها إذا لزم الأمر. كملفات XML، يمكن إنشاء صور SVG وتحريرها باستخدام أي محرر نصوص، ولكن غالبًا ما يكون من الأنسب إنشاؤها باستخدام برامج الرسم مثل Inkscape.

### تحويل صفحات PDF إلى صور SVG

يدعم Aspose.PDF for PHP ميزة تحويل ملف PDF إلى تنسيق SVG.
  لتحقيق هذا المتطلب، تم تقديم فئة [SvgSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/SvgSaveOptions) في حزمة com.aspose.pdf. قم بإنشاء كائن من [SvgSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/SvgSaveOptions) ومرره كمعامل ثانٍ لطريقة [Document.save(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

يوضح المقتطف البرمجي التالي الخطوات لتحويل ملف PDF إلى تنسيق SVG.

```php
// تحميل مستند PDF
$document = new Document($inputFile);

// إنشاء مثيل لفئة SvgSaveOptions
$saveOption = new SvgSaveOptions();

// حفظ مستند PDF كـ SVG
$document->save($outputFile, $saveOption);
```