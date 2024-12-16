---
title: تحويل صيغ الصور المختلفة إلى PDF  
linktitle: تحويل الصور إلى PDF  
type: docs  
weight: 60  
url: /ar/cpp/convert-images-format-to-pdf/  
lastmod: "2021-11-19"  
description: يوضح هذا الموضوع كيفية تحويل مكتبة Aspose.PDF for C++ لصيغ الصور المختلفة إلى PDF.  
sitemap:  
    changefreq: "monthly"  
    priority: 0.5  
---
**Aspose.PDF for C++** تتيح لك تحويل صيغ مختلفة من الصور إلى ملفات PDF. توضح مكتبتنا مقتطفات الشيفرة لتحويل أكثر صيغ الصور شيوعًا، مثل - BMP، DICOM، EMF، JPG، PNG، SVG وTIFF.

## تحويل BMP إلى PDF

قم بتحويل ملفات BMP إلى مستند PDF باستخدام مكتبة **Aspose.PDF for C++**.

<abbr title="Bitmap Image File">BMP</abbr> الصور بصيغة BMP هي ملفات ذات الامتداد. BMP تمثل ملفات الصور النقطية التي تُستخدم لتخزين الصور الرقمية النقطية. هذه الصور مستقلة عن محول الرسوميات وتُعرف أيضًا بتنسيق ملف الصور النقطية المستقلة عن الجهاز (DIB).  
يمكنك تحويل ملفات BMP إلى PDF باستخدام Aspose.PDF for C++ API. لذلك، يمكنك اتباع الخطوات التالية لتحويل صور BMP:

1. إنشاء [فئة سلسلة](https://reference.aspose.com/pdf/cpp/class/system.string) لاسم المسار واسم الملف.
2. يتم إنشاء مثيل لكائن مستند جديد.
3. إضافة [صفحة](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) جديدة إلى هذا [المستند](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
4. يتم إنشاء Aspose.Pdf BMP جديد.
5. يتم تهيئة كائن Aspose.PDF BMP باستخدام الملف المدخل.
6. يتم إضافة Aspose.PDF BMP إلى الصفحة كفقرة.
7. وأخيراً، حفظ ملف PDF الناتج.

لذا، فإن الكود المقتطف التالي يتبع هذه الخطوات ويظهر كيفية تحويل BMP إلى PDF باستخدام C++:

```cpp
void ConvertBMPtoPDF() 
{
    std::clog << "BMP to PDF convert: Start" << std::endl;

    // String for path name
    String _dataDir("C:\\Samples\\Conversion\\");

    // String for input file name
    String infilename("sample.bmp");

    // String for input file name
    String outfilename("ImageToPDF-BMP.pdf");

    // Open document
    auto document = MakeObject<Document>();

    // Add empty page in empty document
    auto page = document->get_Pages()->Add();
    auto image = MakeObject<Aspose::Pdf::Image>();
    image->set_File(_dataDir + infilename);

    // Add image on a page
    page->get_Paragraphs()->Add(image);

    // Save output document
    document->Save(_dataDir + outfilename);

    std::clog << "BMP to PDF convert: Finish" << std::endl;
}
```
{{% alert color="success" %}}
**حاول تحويل BMP إلى PDF عبر الإنترنت**

تقدم لك Aspose تطبيقًا مجانيًا عبر الإنترنت ["BMP إلى PDF"](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)، حيث يمكنك تجربة واستكشاف الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF من BMP إلى PDF باستخدام التطبيق المجاني](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)
{{% /alert %}}

## تحويل DICOM إلى PDF

تنسيق <abbr title="التصوير الرقمي والاتصالات في الطب">DICOM</abbr> هو المعيار الصناعي الطبي لإنشاء وتخزين ونقل وعرض الصور والوثائق الطبية الرقمية للمرضى المفحوصين.

**Aspsoe.PDF for C++** يتيح لك تحويل صور DICOM وSVG، ولكن لأسباب تقنية لإضافة الصور تحتاج إلى تحديد نوع الملف الذي سيتم إضافته إلى PDF:

1. إنشاء [فئة سلسلة](https://reference.aspose.com/pdf/cpp/class/system.string) لاسم المسار واسم الملف.
1. Instantiate [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) كائن.
1. أضف [صفحة](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) إلى مجموعة الصفحات في المستند.
1. يتم إضافة Aspose.PDF TDicom إلى الصفحة كفقرة.
1. قم بتحميل وحفظ ملف الصورة المدخل.

يوضح مقطع الشيفرة التالي كيفية تحويل ملفات DICOM إلى تنسيق PDF باستخدام Aspose.PDF. يجب تحميل صورة DICOM، وضع الصورة على صفحة في ملف PDF وحفظ الناتج كملف PDF.

```cpp
void ConvertDICOMtoPDF()
{
    std::clog << "DICOM to PDF convert: Start" << std::endl;

    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("CR_Anno.dcm");
    String outfilename("PDFWithDicomImage_out.pdf");

    // Instantiate Document Object
    auto document = MakeObject<Document>();

    // Add a page to pages collection of document
    auto page = document->get_Pages()->Add();

    auto image = MakeObject<Aspose::Pdf::Image>();
    image->set_File(_dataDir + infilename);
    image->set_FileType(Aspose::Pdf::ImageFileType::Dicom);

    page->get_Paragraphs()->Add(image);

    // Save output as PDF format
    document->Save(_dataDir + outfilename);
    std::clog << "DICOM to PDF convert: Finish" << std::endl;
}
```

{{% alert color="success" %}}
**حاول تحويل DICOM إلى PDF عبر الإنترنت**

تقدم لك Aspose تطبيقًا مجانيًا عبر الإنترنت ["DICOM إلى PDF"](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)، حيث يمكنك تجربة استكشاف الوظائف والجودة التي يعمل بها.

[![Aspose.PDF تحويل DICOM إلى PDF باستخدام التطبيق المجاني](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
{{% /alert %}}

## تحويل EMF إلى PDF

<abbr title="Enhanced metafile format">EMF</abbr>EMF يخزن الصور الرسومية بشكل مستقل عن الجهاز. يتكون ملفات EMF من سجلات بطول متغير بترتيب زمني يمكنها عرض الصورة المخزنة بعد التحليل على أي جهاز إخراج. علاوة على ذلك، يمكنك تحويل EMF إلى صورة PDF باستخدام الخطوات التالية:

1. إنشاء [فئة سلسلة](https://reference.aspose.com/pdf/cpp/class/system.string) لاسم المسار واسم الملف.
1. يتم إنشاء مثيل لكائن مستند جديد.
1. إضافة صفحة جديدة إلى هذا [المستند](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1.
``` 
تم إنشاء Aspose.Pdf TIFF جديد.
1. يتم تهيئة كائن Aspose.PDF TIFF باستخدام الملف المدخل.
1. يتم إضافة Aspose.PDF TIFF إلى الصفحة كفقرة.
1. تحميل و[حفظ](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) ملف الصورة المدخل.

علاوة على ذلك، يوضح الجزء التالي من الشيفرة كيفية تحويل ملف EMF إلى PDF باستخدام C++ في شيفرة البرنامج:

```cpp
void ConvertEMFtoPDF() 
{
    std::clog << "EMF to PDF convert: Start" << std::endl;

    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample.emf");
    String outfilename("ImageToPDF_emf.pdf");

    auto fileStream = System::IO::File::OpenRead(_dataDir + infilename);
    auto myimage = MakeObject<System::Drawing::Bitmap>(fileStream);

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto currentImage = MakeObject<System::IO::MemoryStream>();
    myimage->Save(currentImage, System::Drawing::Imaging::ImageFormat::get_Tiff());

    auto imageht = MakeObject<Aspose::Pdf::Image>();
    imageht->set_ImageStream(currentImage);
    page->get_Paragraphs()->Add(imageht);

    document->Save(_dataDir + outfilename);

    std::clog << "EMF to PDF convert: Finish" << std::endl;
}
```
```
{{% alert color="success" %}}
**حاول تحويل EMF إلى PDF عبر الإنترنت**

تقدم لك Aspose تطبيقًا مجانيًا عبر الإنترنت ["EMF إلى PDF"](https://products.aspose.app/pdf/conversion/emf-to-pdf/)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![Aspose.PDF تحويل EMF إلى PDF باستخدام تطبيق مجاني](emf_to_pdf.png)](https://products.aspose.app/pdf/conversion/emf-to-pdf/)
{{% /alert %}}

## تحويل JPG إلى PDF

لا داعي للتساؤل حول كيفية تحويل JPG إلى PDF، لأن مكتبة **Aspose.PDF for C++** لديها أفضل حل.

يمكنك بسهولة تحويل صور JPG إلى PDF باستخدام Aspose.PDF for C++ من خلال اتباع الخطوات التالية:

1. إنشاء [فئة سلسلة](https://reference.aspose.com/pdf/cpp/class/system.string) لاسم المسار واسم الملف.
1. يتم إنشاء مثيل لجسم مستند جديد.
1. إضافة صفحة جديدة إلى هذا [المستند](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. يتم إنشاء Aspose::Pdf::Image جديدة.
1. يتم تهيئة كائن صورة Aspose.PDF باستخدام الملف المدخل.
1. Aspose.PDF يتم إضافة الصورة إلى الصفحة كفقرة.
1. تحميل وحفظ ملف الصورة المدخل.

يظهر مقتطف الشيفرة أدناه كيفية تحويل صورة JPG إلى PDF باستخدام C++:

```cpp
void ConvertJPEGtoPDF() 
{
    std::clog << "JPEG to PDF convert: Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Conversion\\");

    // String for input file name
    String infilename("sample.jpg");

    // String for input file name
    String outfilename("ImageToPDF-JPEG.pdf");

    // Open document
    auto document = MakeObject<Document>();

    // Add empty page in empty document
    auto page = document->get_Pages()->Add();
    auto image = MakeObject<Aspose::Pdf::Image>();
    image->set_File(_dataDir + infilename);

    // Add image on a page
    page->get_Paragraphs()->Add(image);

    // Save output document
    document->Save(_dataDir + outfilename);
    std::clog << "JPEG to PDF convert: Finish" << std::endl;
}
```

ثم يمكنك رؤية كيفية تحويل صورة إلى PDF مع **نفس ارتفاع وعرض الصفحة**. نحن سوف نحصل على أبعاد الصورة ونضبط وفقًا لذلك أبعاد الصفحة في مستند PDF بالخطوات التالية:

1. تحميل ملف الصورة المدخل
1. الحصول على ارتفاع وعرض الصورة
1. ضبط الارتفاع والعرض والهوامش للصفحة
1. حفظ ملف PDF الناتج

يوضح مقطع الشيفرة التالي كيفية تحويل صورة إلى PDF بنفس ارتفاع وعرض الصفحة باستخدام C++:

```cpp
void ConvertJPGtoPDF_fitsize() 
{
    std::clog << "JPEG to PDF convert: Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Conversion\\");

    // String for input file name
    String infilename("sample.jpg");

    // String for input file name
    String outfilename("ImageToPDF-JPG.pdf");

    // Open document
    auto document = MakeObject<Document>();

    // Add empty page in empty document
    auto page = document->get_Pages()->Add();
    auto fileStream = System::IO::File::OpenRead(_dataDir + infilename);
    auto bitMap = MakeObject<System::Drawing::Bitmap>(fileStream);


    auto image = MakeObject<Aspose::Pdf::Image>();
    image->set_File(_dataDir + infilename);

    // Add image on a page
    page->get_Paragraphs()->Add(image);

    // Set page dimensions and margins
    page->get_PageInfo()->set_Height(bitMap->get_Height());
    page->get_PageInfo()->set_Width(bitMap->get_Width());
    page->get_PageInfo()->get_Margin()->set_Bottom(0);
    page->get_PageInfo()->get_Margin()->set_Top(0);
    page->get_PageInfo()->get_Margin()->set_Right(0);
    page->get_PageInfo()->get_Margin()->set_Left(0);
    page->get_Paragraphs()->Add(image);

    // Save output document
    document->Save(_dataDir + outfilename);
    std::clog << "JPEG to PDF convert: Finish" << std::endl;
}
```
{{% alert color="success" %}}
**حاول تحويل JPG إلى PDF عبر الإنترنت**

تقدم لك Aspose تطبيقًا مجانيًا عبر الإنترنت ["JPG to PDF"](https://products.aspose.app/pdf/conversion/jpg-to-pdf/)، حيث يمكنك تجربة استكشاف الوظائف والجودة التي يعمل بها.

[![Aspose.PDF تحويل JPG إلى PDF باستخدام التطبيق المجاني](jpg_to_pdf.png)](https://products.aspose.app/pdf/conversion/jpg-to-pdf/)
{{% /alert %}}

## تحويل PNG إلى PDF

يدعم **Aspose.PDF for C++** ميزة تحويل صور PNG إلى تنسيق PDF. تحقق من مقتطف الشيفرة التالي لتحقيق مهمتك.

يشير <abbr title="رسومات الشبكة المحمولة">PNG</abbr> إلى نوع من تنسيق ملف الصور النقطية الذي يستخدم ضغطًا بدون فقدان، مما يجعله شائعًا بين مستخدميه.

يمكنك تحويل PNG إلى صورة PDF باستخدام الخطوات التالية:

1. قم بإنشاء [فئة سلسلة](https://reference.aspose.com/pdf/cpp/class/system.string) لاسم المسار واسم الملف.
1. يتم إنشاء مثيل لكائن مستند جديد.
1. أضف صفحة جديدة إلى [المستند](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. يتم إنشاء Aspose.Pdf PNG جديد.
1. يتم تهيئة كائن Aspose.PDF PNG باستخدام الملف المدخل.
1. يتم إضافة Aspose.PDF PNG إلى الصفحة كفقرة.
1. تحميل وحفظ ملف الصورة المدخل.

علاوة على ذلك، يوضح مقتطف الكود أدناه كيفية تحويل PNG إلى PDF في تطبيقات C++ الخاصة بك:

```cpp
void ConvertPNGtoPDF() 
{
    std::clog << "PNG to PDF convert: Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Conversion\\");

    // String for input file name
    String infilename("sample.png");

    // String for input file name
    String outfilename("ImageToPDF-PNG.pdf");

    // Open document
    auto document = MakeObject<Document>();

    // Add empty page in empty document
    auto page = document->get_Pages()->Add();
    auto image = MakeObject<Aspose::Pdf::Image>();
    image->set_File(_dataDir + infilename);

    // Add image on a page
    page->get_Paragraphs()->Add(image);

    // Save output document
    document->Save(_dataDir + outfilename);
    std::clog << "PNG to PDF convert: Finish" << std::endl;
}
```

{{% alert color="success" %}}
**حاول تحويل PNG إلى PDF عبر الإنترنت**

تقدم لك Aspose تطبيقًا مجانيًا عبر الإنترنت ["PNG إلى PDF"](https://products.aspose.app/pdf/conversion/png-to-pdf/)، حيث يمكنك تجربة استكشاف الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF PNG إلى PDF باستخدام التطبيق المجاني](png_to_pdf.png)](https://products.aspose.app/pdf/conversion/png-to-pdf/)
{{% /alert %}}

## تحويل SVG إلى PDF

**Aspose.PDF for C++** يشرح كيفية تحويل صور SVG إلى صيغة PDF وكيفية الحصول على أبعاد ملف <abbr title="Scalable Vector Graphics">SVG</abbr> المصدر.

رسوميات المتجهات القابلة للتحجيم (SVG) هي عائلة من المواصفات لصيغة ملفات XML للرسوميات المتجهة ثنائية الأبعاد، سواء كانت ثابتة أو ديناميكية (تفاعلية أو متحركة). مواصفة SVG هي معيار مفتوح تم تطويره من قبل اتحاد شبكة الويب العالمية (W3C) منذ عام 1999.

يتم تعريف صور SVG وسلوكياتها في ملفات نصية XML.
``` هذا يعني أنه يمكن البحث عنها وفهرستها وبرمجتها، وإذا لزم الأمر، ضغطها. كملفات XML، يمكن إنشاء صور SVG وتعديلها باستخدام أي محرر نصوص، ولكن غالبًا ما يكون من الأكثر ملاءمة إنشاؤها باستخدام برامج الرسم مثل Inkscape.

1. قم بإنشاء [فئة سلسلة](https://reference.aspose.com/pdf/cpp/class/system.string) لاسم المسار واسم الملف.
1. قم بإنشاء مثيل لفئة [`SvgLoadOptions`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.svg_load_options).
1. قم بإنشاء مثيل لفئة [المستند](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) مع ذكر اسم الملف المصدر والخيارات.
1. قم بحفظ المستند بالاسم المطلوب.

يوضح مقطع الشيفرة التالي عملية تحويل ملف SVG إلى تنسيق PDF باستخدام Aspose.PDF لـ C++.

```cpp
void ConvertSVGtoPDF() 
{
    std::clog << "SVG to PDF convert: Start" << std::endl;

    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample.svg");
    String outfilename("ImageToPDF-SVG.pdf");

    auto options = MakeObject<SvgLoadOptions>();
    try {
    auto document = MakeObject<Document>(_dataDir + infilename, options);
    document->Save(_dataDir + outfilename);
    }
    catch (System::Exception ex) {
    std::cerr << ex->get_Message() << std::endl;
    }
    std::clog << "SVG to PDF convert: Finish" << std::endl;
}
```
خذ بعين الاعتبار مثال مع الميزات المتقدمة:

```cpp
void ConvertSVGtoPDF_Advanced()
{
    std::clog << "تحويل SVG إلى PDF: البداية" << std::endl;

    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("Sweden-Royal-flag-grand-coa.svg");
    String outfilename("ImageToPDF-SVG.pdf");

    auto options = MakeObject<SvgLoadOptions>();
    options->set_AdjustPageSize(true);
    options->ConversionEngine = SvgLoadOptions::ConversionEngines::NewEngine;

    try {
    auto document = MakeObject<Document>(_dataDir + infilename, options);
    document->Save(_dataDir + outfilename);
    }
    catch (System::Exception ex) {
    std::cerr << ex->get_Message() << std::endl;
    }

    std::clog << "تحويل SVG إلى PDF: النهاية" << std::endl;
}
```

{{% alert color="success" %}}
**حاول تحويل صيغة SVG إلى PDF عبر الإنترنت**

تقدم لك Aspose.PDF for C++ تطبيقًا مجانيًا عبر الإنترنت ["SVG to PDF"](https://products.aspose.app/pdf/conversion/svg-to-pdf)، حيث يمكنك تجربة استكشاف الوظائف والجودة التي يعمل بها.

[![Aspose.PDF تحويل SVG إلى PDF باستخدام تطبيق مجاني](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)
{{% /alert %}}

## تحويل TIFF إلى PDF

تنسيق ملف **Aspose.PDF** مدعوم، سواء كان صورة <abbr title="تنسيق ملف صورة موسوم">TIFF</abbr> بإطار واحد أو متعدد الإطارات. هذا يعني أنه يمكنك تحويل صورة TIFF إلى PDF في تطبيقات C++ الخاصة بك.

TIFF أو TIF، تنسيق ملف صورة موسوم، يمثل الصور النقطية التي تُستخدم على مجموعة متنوعة من الأجهزة التي تتفق مع معيار تنسيق الملف هذا. يمكن أن تحتوي صورة TIFF على عدة إطارات بصور مختلفة. تنسيق ملف Aspose.PDF مدعوم أيضًا، سواء كان صورة TIFF بإطار واحد أو متعدد الإطارات. لذا يمكنك تحويل صورة TIFF إلى PDF في تطبيقات C++ الخاصة بك. لذلك، سنعتبر مثالاً لتحويل صورة TIFF متعددة الصفحات إلى مستند PDF متعدد الصفحات من خلال الخطوات التالية:

1. قم بإنشاء [فئة سلسلة](https://reference.aspose.com/pdf/cpp/class/system.string) لاسم المسار واسم الملف.
1. 
يتم إنشاء مثيل لكائن Document جديد.
1. أضف صفحة جديدة إلى هذا [الوثيقة](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. يتم إنشاء Aspose.Pdf TIFF جديد.
1. يتم تهيئة كائن Aspose.PDF TIFF باستخدام ملف الإدخال.
1. يتم إضافة Aspose.PDF TIFF إلى الصفحة كفقرة.
1. تحميل وحفظ ملف الصورة المدخل.

علاوة على ذلك، يوضح مقطع الكود التالي كيفية تحويل صورة TIFF متعددة الصفحات أو متعددة الإطارات إلى PDF باستخدام C++:

```cpp
void ConvertTIFFtoPDF() 
{
    std::clog << "TIFF to PDF convert: Start" << std::endl;

    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample.tiff");
    String outfilename("ImageToPDF-TIFF.pdf");

    auto fileStream = System::IO::File::OpenRead(_dataDir + infilename);
    auto myimage = MakeObject<System::Drawing::Bitmap>(fileStream);

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto currentImage = MakeObject<System::IO::MemoryStream>();
    myimage->Save(currentImage, System::Drawing::Imaging::ImageFormat::get_Tiff());

    auto imageht = MakeObject<Aspose::Pdf::Image>();
    imageht->set_ImageStream(currentImage);
    page->get_Paragraphs()->Add(imageht);

    document->Save(_dataDir + outfilename);

    std::clog << "TIFF to PDF convert: Finish" << std::endl;
}
```