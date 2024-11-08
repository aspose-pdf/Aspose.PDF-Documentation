---
title: تحويل PDF إلى تنسيقات الصور
linktitle: تحويل PDF إلى صور
type: docs
weight: 70
url: /ar/cpp/convert-pdf-to-images-format/
lastmod: "2021-11-19"
description: يوضح هذا الموضوع كيف يسمح Aspose.PDF بتحويل PDF إلى تنسيقات صور مختلفة. تحويل صفحات PDF إلى صور PNG وJPEG وBMP ببضع سطور من الكود.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

**Aspose.PDF for C++** يستخدم بعض الأساليب لتحويل PDF إلى صورة. بشكل عام، نستخدم نهجين: التحويل باستخدام نهج الجهاز والتحويل باستخدام SaveOption. ستوضح لك هذه القسم كيفية تحويل مستندات PDF إلى تنسيقات الصور مثل BMP وJPEG وPNG وTIFF وSVG باستخدام أحد هذه الأساليب.

هناك العديد من الفئات في المكتبة التي تسمح لك باستخدام جهاز افتراضي لتحويل الصور. DocumentDevice موجه لتحويل المستند بالكامل، ولكن ImageDevice - لصفحة معينة.

## تحويل PDF باستخدام فئة DocumentDevice

**Aspose.PDF for C++** يجعل من الممكن تحويل صفحات PDF إلى صور TIFF.

The [TiffDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.tiff_device/) (بناءً على DocumentDevice) تسمح لك بتحويل صفحات PDF إلى صور TIFF. توفر هذه الفئة طريقة تسمى [Process](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.tiff_device#a0790daa96125c5638a645647e9678f0c) والتي تتيح لك تحويل جميع الصفحات في ملف PDF إلى صورة TIFF واحدة.

{{% alert color="success" %}}
**حاول تحويل PDF إلى TIFF عبر الإنترنت**

Aspose.PDF لـ C++ يقدم لك تطبيقًا مجانيًا عبر الإنترنت ["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![Aspose.PDF conversion PDF to TIFF with Free App](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### تحويل صفحات PDF إلى صورة TIFF واحدة

Aspose.PDF لـ C++ يشرح كيفية تحويل جميع الصفحات في ملف PDF إلى صورة TIFF واحدة:

1. افتح [المستند](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) باستخدام MakeObject.
1. أنشئ كائن Resolution.
1. أنشئ كائن [TIffSettings](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.tiff_settings/).
1. أنشئ [جهاز Tiff](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.tiff_device/) بخصائص محددة.
1. حوّل صفحة معينة واحفظ الصورة في تدفق.

يوضح مقتطف الشيفرة التالي كيفية تحويل جميع صفحات PDF إلى صورة TIFF واحدة.

```cpp
void Convert_PDF_To_Images::ConvertPDFtoTIFF()
{
    std::clog << __func__ << ": Start" << std::endl;
    // سلسلة لأسم المسار
    String _dataDir("C:\\Samples\\Conversion\\");

    // سلسلة لأسم الملف
    String infilename("PageToTiff.pdf");
    String outfilename("PagesToTIFF_out.tif");

    // افتح المستند
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto imageStream = System::IO::File::OpenWrite(_dataDir + outfilename);

    // أنشئ كائن Resolution
    auto resolution = MakeObject<Aspose::Pdf::Devices::Resolution>(300);

    // أنشئ كائن TiffSettings
    auto tiffSettings = MakeObject<Aspose::Pdf::Devices::TiffSettings>();
    tiffSettings->set_Compression(Aspose::Pdf::Devices::CompressionType::None);
    tiffSettings->set_Depth(Aspose::Pdf::Devices::ColorDepth::Default);
    tiffSettings->set_Shape(Aspose::Pdf::Devices::ShapeType::Landscape);
    tiffSettings->set_SkipBlankPages(false);

    // أنشئ جهاز TIFF
    auto tiffDevice = MakeObject<Aspose::Pdf::Devices::TiffDevice>(resolution, tiffSettings);

    // حوّل الصفحات واحفظ الصورة في تدفق
    tiffDevice->Process(document, 1, 2, imageStream);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
### تحويل صفحة واحدة إلى صورة TIFF

يسمح لك Aspose.PDF for C++ بتحويل صفحة معينة في ملف PDF إلى صورة TIFF، استخدم نسخة محملة زائدة من دالة Process(..) التي تأخذ رقم الصفحة كمعامل للتحويل. يوضح مقتطف الشيفرة التالي كيفية تحويل الصفحة الأولى من ملف PDF إلى تنسيق TIFF.

```cpp
void Convert_PDF_To_Images::ConvertPDFtoTiffSinglePage()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Conversion\\");

    // String for file name
    String infilename("PageToTiff.pdf");
    String outfilename("PageToTiff_out.tif");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto imageStream = System::IO::File::OpenWrite(_dataDir + outfilename);

    // Create Resolution object
    auto resolution = MakeObject<Aspose::Pdf::Devices::Resolution>(300);

    // Create TIFF device
    auto tiffDevice = MakeObject<Aspose::Pdf::Devices::TiffDevice>(resolution);

    // Convert a particular page and save the image to stream
    tiffDevice->Process(document, 1, 1, imageStream);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

### استخدم خوارزمية برادلي أثناء التحويل

يدعم Aspose.PDF for C++ ميزة تحويل PDF إلى TIF باستخدام ضغط LZW ثم مع استخدام AForge، يمكن تطبيق التثنيم. ومع ذلك، طلب أحد العملاء أنه لبعض الصور، يحتاجون إلى الحصول على العتبة باستخدام Otsu، لذا يرغبون أيضًا في استخدام Bradley.

```cpp
void Convert_PDF_To_Images::ConvertPDFtoTiffBradleyBinarization()
{
    // String for path name
    String _dataDir("C:\\Samples\\Conversion\\");

    // Open document
    auto pdfDocument = MakeObject<Document>(_dataDir + u"PageToTIFF.pdf");

    String outputImageFile = _dataDir + u"resultant_out.tif";
    String outputBinImageFile = _dataDir + u"37116-bin_out.tif";

    // Create Resolution object 
    auto resolution = MakeObject<Aspose::Pdf::Devices::Resolution>(300);

    // Create TiffSettings object
    auto tiffSettings = MakeObject<Aspose::Pdf::Devices::TiffSettings>();
    tiffSettings->set_Compression(Aspose::Pdf::Devices::CompressionType::LZW);
    tiffSettings->set_Depth(Aspose::Pdf::Devices::ColorDepth::Format1bpp);

    // Create TIFF device
    auto tiffDevice = MakeObject<Aspose::Pdf::Devices::TiffDevice>(resolution, tiffSettings);
    auto imageStream = System::IO::File::OpenWrite(_dataDir + outputImageFile);

    // Convert a particular page and save the image to stream
    tiffDevice->Process(pdfDocument, 1, 2, imageStream);

    imageStream->Close();

    auto inStream = System::IO::File::OpenRead(outputImageFile);
    auto outStream = System::IO::File::OpenWrite(outputBinImageFile);

    tiffDevice->BinarizeBradley(inStream, outStream, 0.1);
}
```

## تحويل PDF باستخدام فئة ImageDevice

`ImageDevice` هو السلف لـ `BmpDevice` و `JpegDevice` و `GifDevice` و `PngDevice` و `EmfDevice`.

- تسمح لك فئة [BmpDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.bmp_device/) بتحويل صفحات PDF إلى صور <abbr title="Bitmap Image File">BMP</abbr>.
- تسمح لك فئة [EmfDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.emf_device/) بتحويل صفحات PDF إلى صور <abbr title="Enhanced Meta File">EMF</abbr>.
- تسمح لك فئة [JpegDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.jpeg_device/) بتحويل صفحات PDF إلى صور JPEG.
- تسمح لك فئة [PngDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.png_device/) بتحويل صفحات PDF إلى صور <abbr title="Portable Network Graphics">PNG</abbr>.

- تسمح لك فئة [GifDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.gif_device/) بتحويل صفحات PDF إلى صور <abbr title="Graphics Interchange Format">GIF</abbr>.

دعونا نلقي نظرة على كيفية تحويل صفحة PDF إلى صورة.

توفر فئة [BmpDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.bmp_device) طريقة باسم [Process](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.bmp_device#a22cefdb47b7c762320fa7973aa4f1f93) والتي تتيح لك تحويل صفحة معينة من ملف PDF إلى تنسيق صورة BMP. تحتوي الفئات الأخرى على نفس الطريقة. لذلك، إذا كنا بحاجة إلى تحويل صفحة PDF إلى صورة، فإننا نقوم فقط بإنشاء الكائن المطلوب.

يعرض مقطع الشيفرة التالي هذه الإمكانية:

```cpp
void Convert_PDF_To_Images::ConvertPDFusingImageDevice()
{
    std::clog << __func__ << ": Start" << std::endl;

    // سلسلة لاسم المسار
    String _dataDir("C:\\Samples\\Conversion\\");

    // إنشاء كائن الدقة            
    auto resolution = MakeObject<Aspose::Pdf::Devices::Resolution>(300); //300 dpi

    System::SmartPtr<Aspose::Pdf::Devices::ImageDevice>
    bmpDevice = MakeObject<Aspose::Pdf::Devices::BmpDevice>(resolution);
    System::SmartPtr<Aspose::Pdf::Devices::ImageDevice>
    jpegDevice = MakeObject<Aspose::Pdf::Devices::JpegDevice>(resolution);
    System::SmartPtr<Aspose::Pdf::Devices::ImageDevice>
    gifDevice = MakeObject<Aspose::Pdf::Devices::GifDevice>(resolution);
    System::SmartPtr<Aspose::Pdf::Devices::ImageDevice>
    pngDevice = MakeObject<Aspose::Pdf::Devices::PngDevice>(resolution);
    System::SmartPtr<Aspose::Pdf::Devices::ImageDevice>
    emfDevice = MakeObject<Aspose::Pdf::Devices::EmfDevice>(resolution);

    auto document = MakeObject<Document>(_dataDir + u"ConvertAllPagesToBmp.pdf");

    ConvertPDFtoImage(bmpDevice, u"bmp", document);
    ConvertPDFtoImage(jpegDevice, u"jpeg", document);
    ConvertPDFtoImage(gifDevice, u"gif", document);
    ConvertPDFtoImage(pngDevice, u"png", document);
    ConvertPDFtoImage(emfDevice, u"emf", document);

    std::clog << __func__ << ": Finish" << std::endl;

}

void Convert_PDF_To_Images::ConvertPDFtoImage(
 System::SmartPtr<Aspose::Pdf::Devices::ImageDevice> imageDevice,
 String ext, System::SmartPtr<Document> document)
{
    // سلسلة لاسم المسار
    String _dataDir("C:\\Samples\\Conversion\\");

    for (int pageCount = 1; pageCount <= document->get_Pages()->get_Count(); pageCount++)
    {
    String outfilename = String::Format(u"{0}PageToBmp{1}_out.{2}",
    _dataDir, pageCount, ext);

    auto imageStream = System::IO::File::OpenWrite(outfilename);

    // إنشاء كائن الدقة
    auto resolution = MakeObject<Aspose::Pdf::Devices::Resolution>(300);

    // تحويل صفحة معينة وحفظ الصورة في الدفق
    imageDevice->Process(document->get_Pages()->idx_get(pageCount), imageStream);

    // إغلاق الدفق
    imageStream->Close();
    }
}
```

{{% alert color="success" %}}
**حاول تحويل PDF إلى PNG عبر الإنترنت**

كمثال على كيفية عمل تطبيقاتنا المجانية، يرجى التحقق من الميزة التالية.

تقدم Aspose.PDF for C++ لك تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![كيفية تحويل PDF إلى PNG باستخدام التطبيق المجاني](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## تحويل PDF باستخدام فئة SaveOptions

هذا الجزء من المقالة يوضح لك كيفية تحويل PDF إلى <abbr title="Scalable Vector Graphics">SVG</abbr> باستخدام C++ وفئة SaveOptions.

{{% alert color="success" %}}
**حاول تحويل PDF إلى SVG عبر الإنترنت**

تقدم Aspose.PDF for C++ لك تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![Aspose.PDF تحويل PDF إلى SVG باستخدام التطبيق المجاني](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

من أجل تحويل PDF إلى SVG، تقدم Aspose.PDF لـ CPP طريقة [Save](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) من فئة [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). تحتاج إلى تمرير مسار الإخراج وenum SaveFormat:: svg إلى طريقة Save لتحويل PDF إلى SVG. يوضح مقطع الشيفرة التالي كيفية تحويل PDF إلى SVG:

تُعلمك هذه المقالة كيفية تحويل PDF إلى <abbr title="Scalable Vector Graphics">SVG</abbr> باستخدام C++.

**Scalable Vector Graphics (SVG)** هو مجموعة من المواصفات لصيغة ملف تعتمد على XML للرسومات المتجهية ثنائية الأبعاد، سواء كانت ثابتة أو ديناميكية (تفاعلية أو متحركة). إن مواصفة SVG هي معيار مفتوح تم تطويره بواسطة اتحاد شبكة الويب العالمية (W3C) منذ عام 1999.

يتم تعريف صور SVG وسلوكياتها في ملفات نصية XML. هذا يعني أنه يمكن البحث عنها وفهرستها وبرمجتها وضغطها إذا لزم الأمر. كملفات XML، يمكن إنشاء صور SVG وتحريرها باستخدام أي محرر نصوص، ولكن غالبًا ما يكون من الأسهل إنشاؤها باستخدام برامج الرسم مثل Inkscape.

يدعم Aspose.PDF for C++ ميزة تحويل صورة SVG إلى تنسيق PDF ويقدم أيضًا القدرة على تحويل ملفات PDF إلى تنسيق SVG. لتحقيق هذا المتطلب، تمت إضافة فئة `SvgSaveOptions` إلى مساحة الأسماء Aspose.PDF. قم بإنشاء كائن من SvgSaveOptions ومرره كوسيط ثاني إلى طريقة [Save](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa).

يُظهر مقتطف الشيفرة التالي خطوات تحويل ملف PDF إلى تنسيق SVG باستخدام C++.

```cpp
void Convert_PDF_To_Images::ConvertPDFtoSvgSinglePage()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Conversion\\");

    // String for file name
    String infilename("PageToSvg.pdf");
    String outfilename("PageToSvg_out.svg");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instantiate an object of SvgSaveOptions
    auto saveOptions = MakeObject<SvgSaveOptions>();
    // Do not compress SVG image to Zip archive
    saveOptions->CompressOutputToZipArchive = false;

    try {
    // Save the output in SVG files
    document->Save(_dataDir + outfilename, saveOptions);
    }
    catch (Exception ex) {
    std::cerr << ex->get_Message();
    }

    std::clog << __func__ << ": Finish" << std::endl;
}
```