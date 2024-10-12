---
linktitle: تحويل صيغ الملفات الأخرى إلى PDF
type: docs
weight: 80
url: /cpp/convert-other-files-to-pdf/
lastmod: "2021-11-19"
description: يوضح هذا الموضوع كيف يسمح Aspose.PDF بتحويل صيغ الملفات الأخرى إلى مستند PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## تحويل EPUB إلى PDF

يسمح **Aspose.PDF for C++** بسهولة تحويل ملفات EPUB إلى صيغة PDF.

<abbr title="electronic publication">EPUB</abbr> (اختصار لـ electronic publication) هو معيار كتاب إلكتروني مجاني ومفتوح من المنتدى الدولي للنشر الرقمي (IDPF). الملفات تحمل الامتداد .epub. تم تصميم EPUB للمحتوى القابل لإعادة التدفق، مما يعني أن قارئ EPUB يمكنه تحسين النص لجهاز عرض معين.

يدعم EPUB أيضًا المحتوى ذو التخطيط الثابت. تم تصميم التنسيق كتنسيق فردي يمكن للناشرين وبيوت التحويل استخدامه داخليًا، وكذلك للتوزيع والبيع. إنه يحل محل معيار Open eBook. يتم أيضًا اعتماد نسخة EPUB 3 من قبل مجموعة دراسة صناعة الكتاب (BISG)، وهي جمعية تجارية رائدة في مجال الكتب لأفضل الممارسات المعيارية والبحث والمعلومات والفعاليات، لتغليف المحتوى.

خطوات التحويل:

1. قم بإنشاء [فئة سلسلة](https://reference.aspose.com/pdf/cpp/class/system.string) لاسم المسار واسم الملف.
1. قم بإنشاء مثيل للفئة [خيارات تحميل Epub](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.load_options).
1. قم بإنشاء مثيل للفئة [المستند](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) مع ذكر اسم الملف المصدر والخيارات.
1. قم بتحميل الملف [واحفظه](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa).

الشفرة التالية توضح لك كيفية تحويل ملفات EPUB إلى تنسيق PDF باستخدام C++.

```cpp
void ConvertEPUBtoPDF()
{
    std::clog << "EPUB to PDF convert: Start" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("aliceDynamic.epub");
    String outfilename("epub_test.pdf");
    auto options = MakeObject<EpubLoadOptions>();
    try {
    auto document = MakeObject<Document>(_dataDir + infilename, options);
    document->Save(_dataDir + outfilename);
    }
    catch (System::Exception ex) {
    std::cerr << ex->get_Message() << std::endl;
    }
    std::clog << "EPUB to PDF convert: End" << std::endl;
}
```
{{% alert color="success" %}}
**حاول تحويل EPUB إلى PDF عبر الإنترنت**

Aspose.PDF لـ C++ يقدم لك تطبيقًا مجانيًا عبر الإنترنت ["EPUB to PDF"](https://products.aspose.app/pdf/conversion/epub-to-pdf)، حيث يمكنك محاولة التحقيق في الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF EPUB إلى PDF مع تطبيق مجاني](epub.png)](https://products.aspose.app/pdf/conversion/epub-to-pdf)
{{% /alert %}}

## تحويل النص إلى PDF

**Aspose.PDF لـ C++** يدعم ميزة تحويل النص العادي وملف النص المسبق التنسيق إلى تنسيق PDF.

تحويل النص إلى PDF يعني إضافة أجزاء من النص إلى صفحة PDF. أما بالنسبة لملفات النصوص، فنحن نتعامل مع نوعين من النصوص: التنسيق المسبق (على سبيل المثال، 25 سطرًا بـ 80 حرفًا لكل سطر) والنص غير المنسق (النص العادي). اعتمادًا على احتياجاتنا، يمكننا التحكم في هذه الإضافة بأنفسنا أو إسنادها إلى خوارزميات المكتبة.

### تحويل ملف نصي عادي إلى PDF

في حالة الملف النصي العادي، يمكننا استخدام التقنية التالية:

1. إنشاء [فئة سلسلة](https://reference.aspose.com/pdf/cpp/class/system.string) لاسم المسار واسم الملف.
1. قراءة ملف النص المصدر باستخدام [قارئ النص](https://reference.aspose.com/pdf/cpp/class/system.i_o.text_reader/.)
1. إنشاء كائن [وثيقة](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. إضافة [صفحة](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) إلى مجموعة الصفحات في الوثيقة.
1. إنشاء كائن جديد من TextFragment وتمرير كائن TextReader إلى المنشئ الخاص به.
1. إضافة فقرة نصية جديدة في مجموعة الفقرات وتمرير كائن TextFragment.
1. تحميل و[حفظ](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) الملف المدخل.

```cpp
void ConvertTextToPDF()
{
    std::clog << "Text to PDF convert: Start" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample.txt");
    String outfilename("TextToPDF.pdf");

    // Read the source text file
    String content = System::IO::File::ReadAllText(_dataDir + infilename);

    // Instantiate a Document object by calling its empty constructor
    auto document = MakeObject<Document>();

    // Add a new page in Pages collection of Document
    auto page = document->get_Pages()->Add();

    // Create an instance of TextFragmet and pass the text from reader object to its constructor as argument
    auto text = MakeObject<TextFragment>(content);

    // Add a new text paragraph in paragraphs collection and pass the TextFragment object
    auto paragraphs = page->get_Paragraphs();
    paragraphs->Add(text);

    // Save resultant PDF file
    document->Save(_dataDir + outfilename);
    std::clog << "Text to PDF convert: End" << std::endl;
}
```
### تحويل ملف نصي مهيأ مسبقاً إلى PDF

تحويل النص المهيأ مسبقاً يشبه النص العادي ولكن تحتاج إلى اتخاذ بعض الإجراءات الإضافية مثل ضبط الهوامش، نوع الخط وحجمه. من الواضح أن الخط يجب أن يكون ثابت العرض (على سبيل المثال Courier New).

اتبع هذه الخطوات لتحويل النص المهيأ مسبقاً إلى PDF باستخدام C++:

1. إنشاء كائن Document عن طريق استدعاء منشئه الفارغ.
1. ضبط الهوامش اليسرى واليمنى لتحسين العرض.
1. إنشاء كائن [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) وإضافة صفحة جديدة في مجموعة Pages.
1. تحميل و[حفظ](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) ملف الصورة المدخل. 

```CPP
void ConvertPreFormattedTextToPdf()
{
    std::clog << "Performatted Text to PDF convert: Start" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("rfc822.txt");
    String outfilename("TextToPDF.pdf");
    // قراءة ملف النص كصفيف من السلاسل
    auto lines = System::IO::File::ReadAllLines(_dataDir + infilename);

    // إنشاء كائن Document عن طريق استدعاء منشئه الفارغ
    auto document = MakeObject<Document>();

    // إضافة صفحة جديدة في مجموعة Pages من Document
    auto page = document->get_Pages()->Add();

    // ضبط الهوامش اليسرى واليمنى لتحسين العرض
    page->get_PageInfo()->get_Margin()->set_Left(20);
    page->get_PageInfo()->get_Margin()->set_Right(10);
    page->get_PageInfo()->get_DefaultTextState()->set_Font(FontRepository::FindFont(u"Courier New"));
    page->get_PageInfo()->get_DefaultTextState()->set_FontSize(12);

    for (int index = 0; index < lines->get_Length(); index++)
    {
        // التحقق مما إذا كانت السطر يحتوي على حرف "تغذية الصفحة"
        // انظر https://en.wikipedia.org/wiki/Page_break
        auto line = lines->idx_get(index);
        if (line.StartsWith(u"\x0c"))
        {
        if (document->get_Pages()->get_Count() > 3) break;
        page = document->get_Pages()->Add();
        // ضبط الهوامش اليسرى واليمنى لتحسين العرض
        page->get_PageInfo()->get_Margin()->set_Left(20);
        page->get_PageInfo()->get_Margin()->set_Right(10);
        page->get_PageInfo()->get_DefaultTextState()->set_Font(FontRepository::FindFont(u"Courier New"));
        page->get_PageInfo()->get_DefaultTextState()->set_FontSize(12);
        }
        else
        {
        // إنشاء مثيل لـ TextFragment و
        // تمرير السطر إلى منشئه كوسيطة
        auto text = MakeObject<TextFragment>(line);

        // إضافة فقرة نصية جديدة في مجموعة الفقرات وتمرير كائن TextFragment
        page->get_Paragraphs()->Add(text);
        }
    }

    // حفظ ملف PDF الناتج
    document->Save(_dataDir + outfilename);
    std::clog << "Performatted Text to PDF convert: End" << std::endl;
}
```


{{% alert color="success" %}}
**جرب تحويل النص إلى PDF عبر الإنترنت**

تقدم Aspose.PDF for C++ تطبيقًا مجانيًا عبر الإنترنت ["Text to PDF"](https://products.aspose.app/pdf/conversion/txt-to-pdf)، حيث يمكنك محاولة التحقق من الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF النص إلى PDF مع التطبيق المجاني](text_to_pdf.png)](https://products.aspose.app/pdf/conversion/txt-to-pdf)
{{% /alert %}}

## تحويل XPS إلى PDF

**Aspose.PDF for C++** يدعم ميزة تحويل ملفات <abbr title="XML Paper Specification">XPS</abbr> إلى تنسيق PDF. تحقق من هذه المقالة لحل مهامك.

نوع ملف XPS يرتبط أساسًا بمواصفات الورق XML من قبل شركة مايكروسوفت. مواصفات الورق XML (XPS)، كانت تعرف سابقًا بالاسم الرمزي Metro وتشمل مفهوم التسويق لمسار الطباعة من الجيل التالي (NGPP)، وهي مبادرة مايكروسوفت لدمج إنشاء المستندات وعرضها في نظام التشغيل Windows.

{{% alert color="primary" %}}

تنسيق الملف هو في الأساس ملف XML مضغوط يستخدم في المقام الأول للتوزيع والتخزين.
``` من الصعب جدًا تحريره ويتم تنفيذه في الغالب بواسطة Microsoft.

{{% /alert %}}

من أجل تحويل XPS إلى PDF باستخدام Aspose.PDF لـ C++، قمنا بتقديم فئة تسمى [XpsLoadOption](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.load_options) والتي تُستخدم لتهيئة كائن [LoadOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.load_options). لاحقًا، يتم تمرير هذا الكائن كوسيط أثناء تهيئة كائن Document ويساعد محرك عرض PDF في تحديد تنسيق إدخال المستند المصدر.

يوضح مقطع الشفرة التالي عملية تحويل ملف XPS إلى تنسيق PDF باستخدام C++.

```cpp
void ConvertXPStoPDF()
{
    std::clog << "XPS to PDF convert: Start" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample.oxps");
    String outfilename("XPStoPDF.pdf");
    auto options = MakeObject<XpsLoadOptions>();
    try {
        auto document = MakeObject<Document>(_dataDir + infilename, options);
        document->Save(_dataDir + outfilename);
    }
    catch (System::Exception ex) {
        std::cerr << ex->get_Message() << std::endl;
    };
    std::clog << "XPS to PDF convert: Finish" << std::endl;
}
```
{{% alert color="success" %}}
**حاول تحويل تنسيق XPS إلى PDF عبر الإنترنت**

يقدم لك Aspose.PDF for C++ تطبيقًا مجانيًا عبر الإنترنت ["XPS to PDF"](https://products.aspose.app/pdf/conversion/xps-to-pdf/)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![Aspose.PDF Convertion XPS to PDF with Free App](xps_to_pdf.png)](https://products.aspose.app/pdf/conversion/xps-to-pdf/)
{{% /alert %}}

## تحويل XML إلى PDF

يستخدم تنسيق XML لتخزين البيانات المنظمة. هناك عدة طرق لتحويل <abbr title="Extensible Markup Language">XML</abbr> إلى PDF في Aspose.PDF.

## تحويل XSL-FO إلى PDF

1. إنشاء [فئة سلسلة](https://reference.aspose.com/pdf/cpp/class/system.string) لاسم المسار واسم الملف.
1. إنشاء [كائن XslFoLoadOption](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.load_options).
1. تعيين استراتيجية معالجة الأخطاء.
1. إنشاء [كائن وثيقة](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). [احفظ](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) ملف الصورة المدخلة.

```cpp
void Convert_XSLFO_to_PDF()
{
    std::clog << "XSL-FO to PDF convert: Start" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilenameXSL("c:\\samples\\employees.xslt");
    String infilenameXML("c:\\samples\\employees.xml");

     String outfilename("XMLFOtoPDF.pdf");
    // Instantiate XslFoLoadOption object
    auto options = new XslFoLoadOptions(infilenameXSL);
    // Set error handling strategy
    options->ParsingErrorsHandlingType = XslFoLoadOptions::ParsingErrorsHandlingTypes::ThrowExceptionImmediately;
    // Create Document object
    auto document = MakeObject<Document>(infilenameXML, options);
    document->Save(_dataDir + outfilename);
}
```

{{% alert color="success" %}}
**حاول تحويل XML إلى PDF عبر الإنترنت**

Aspose.PDF for C++ يقدم لك تطبيقًا مجانيًا عبر الإنترنت ["XML إلى PDF"](https://products.aspose.app/pdf/conversion/xml-to-pdf)، حيث يمكنك محاولة استكشاف الوظيفة والجودة التي يعمل بها.

[![Aspose.PDF تحويل XML إلى PDF باستخدام التطبيق المجاني](xml_to_pdf.png)](https://products.aspose.app/pdf/conversion/xml-to-pdf)
{{% /alert %}}
```