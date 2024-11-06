---
title: تحويل PDF إلى تنسيقات PDF/A
linktitle: تحويل PDF إلى تنسيقات PDF/A
type: docs
weight: 100
url: ar/cpp/convert-pdf-to-pdfa/
lastmod: "2021-11-01"
description: يوضح لك هذا الموضوع كيف يسمح Aspose.PDF بتحويل ملف PDF إلى ملف PDF متوافق مع PDF/A.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF for C++** يسمح لك بتحويل ملف PDF إلى ملف متوافق مع <abbr title="Portable Document Format / A">PDF/A</abbr>. قبل القيام بذلك، يجب التحقق من صحة الملف. يوضح هذا الموضوع كيفية القيام بذلك.

{{% alert color="primary" %}}

يرجى ملاحظة أننا نتبع Adobe Preflight للتحقق من توافق PDF/A. كل الأدوات في السوق لديها "تمثيلها" الخاص لتوافق PDF/A. يرجى مراجعة هذه المقالة حول أدوات التحقق من صحة PDF/A كمرجع. اخترنا منتجات Adobe للتحقق من كيفية إنتاج Aspose.PDF لملفات PDF لأن Adobe في مركز كل ما يتعلق بـ PDF.

{{% /alert %}}

قم بتحويل الملف باستخدام طريقة التحويل الخاصة بفئة Document. قبل تحويل ملف PDF إلى ملف متوافق مع PDF/A، قم بالتحقق من صحة ملف PDF باستخدام طريقة Validate. يتم تخزين نتيجة التحقق في ملف XML ثم يتم تمرير هذه النتيجة أيضًا إلى طريقة Convert. يمكنك أيضًا تحديد الإجراء للعناصر التي لا يمكن تحويلها باستخدام التعداد ConvertErrorAction.
## تحويل ملف PDF إلى PDF/A-1b

يوضح مقطع الشيفرة التالي كيفية تحويل ملفات PDF إلى PDF متوافق مع PDF/A-1b.

```cpp
void ConverttoPDFA_1b()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Conversion\\");

    // String for input file name
    String infilename("sample.pdf");
    // String for log file name
    String logfilename("log.xml");
    // String for input file name
    String outfilename("PDFToPDFA_out.pdf");

    // Open document
    auto document = new Document(_dataDir + infilename);

    // Convert to PDF/A compliant document
    // During conversion process, the validation is also performed
    document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_1B, ConvertErrorAction::Delete);

    // Save output document
    document->Save(_dataDir + outfilename);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
لإجراء التحقق فقط، استخدم السطر التالي من الكود:

```cpp
void ConverttoPDFA_1b_Validation()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Conversion\\");

    // String for input file name
    String infilename("sample.pdf");
    // String for log file name
    String logfilename("log.xml");

    // Open document
    auto document = new Document(_dataDir + infilename);

    // Convert to PDF/A compliant document
    // During conversion process, the validation is also performed
    document->Validate(_dataDir + logfilename, PdfFormat::PDF_A_1B);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## تحويل ملف PDF إلى PDF/A-3b

Aspose.PDF لـ C++ يدعم أيضًا ميزة تحويل ملف PDF إلى تنسيق PDF/A-3b.

```cpp
void ConverttoPDFA_3b()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Conversion\\");

    // String for input file name
    String infilename("sample.pdf");
    // String for log file name
    String logfilename("log.xml");
    // String for input file name
    String outfilename("PDFToPDFA3b_out.pdf");

    // Open document
    auto document = new Document(_dataDir + infilename);

    // Convert to PDF/A compliant document
    // During conversion process, the validation is also performed
    document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_3B, ConvertErrorAction::Delete);

    // Save output document
    document->Save(_dataDir + outfilename);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## تحويل ملف PDF إلى PDF/A-2u

يدعم Aspose.PDF for C++ أيضًا ميزة تحويل ملف PDF إلى تنسيق PDF/A-2u.

```cpp
void ConverttoPDFA_2u()
{
    std::clog << __func__ << ": Start" << std::endl;
    // سلسلة لمسار الاسم
    String _dataDir("C:\\Samples\\Conversion\\");

    // سلسلة لاسم الملف المدخل
     String infilename("sample.pdf");
    // سلسلة لاسم ملف السجل
    String logfilename("log.xml");
    // سلسلة لاسم الملف الناتج
    String outfilename("PDFToPDFA3b_out.pdf");

    // فتح المستند
    auto document = new Document(_dataDir + infilename);

    // تحويل إلى مستند متوافق مع PDF/A
    // أثناء عملية التحويل، يتم أيضًا إجراء التحقق
    document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_2U, ConvertErrorAction::Delete);

    // حفظ المستند الناتج
    document->Save(_dataDir + outfilename);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## تحويل ملف PDF إلى PDF/A-3u

يدعم Aspose.PDF for C++ أيضًا ميزة تحويل ملف PDF إلى تنسيق PDF/A-3u.

```cpp
void ConverttoPDFA_3u()
{
    std::clog << __func__ << ": ابدأ" << std::endl;
    // سلسلة لاسم المسار
    String _dataDir("C:\\Samples\\Conversion\\");

    // سلسلة لاسم الملف المدخل
    String infilename("sample.pdf");
    // سلسلة لاسم ملف السجل
    String logfilename("log.xml");
    // سلسلة لاسم الملف المدخل
    String outfilename("PDFToPDFA3b_out.pdf");

    // فتح المستند
    auto document = new Document(_dataDir + infilename);

    // تحويل إلى مستند متوافق مع PDF/A
    // أثناء عملية التحويل، يتم أيضًا إجراء التحقق
    document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_2U, ConvertErrorAction::Delete);

    // حفظ المستند الناتج
    document->Save(_dataDir + outfilename);
    std::clog << __func__ << ": انتهاء" << std::endl;
}
```

## إضافة مرفق إلى ملف PDF/A

في حالة كان لديك متطلب لإرفاق ملفات بتنسيق التوافق PDF/A، فإننا نوصي باستخدام القيمة PDF_A_3A من تعداد Aspose.PDF.PdfFormat.

PDF/A_3a هو التنسيق الذي يوفر ميزة إرفاق أي تنسيق ملف كملف مرفق إلى ملف متوافق مع PDF/A.

```cpp
void ConverttoPDFA_AddAttachment()
{
    std::clog << __func__ << ": البداية" << std::endl;
    // سلسلة لاسم المسار
    String _dataDir("C:\\Samples\\Conversion\\");

    // سلسلة لاسم الملف المدخل
    String infilename("sample.pdf");
    // سلسلة لاسم ملف السجل
    String logfilename("log.xml");
    // سلسلة لاسم الملف المدخل
    String outfilename("PDFToPDFA3b_out.pdf");

    // فتح المستند
    auto document = new Document(_dataDir + infilename);

    // إعداد ملف جديد ليتم إضافته كمرفق
    auto fileSpecification = MakeObject<FileSpecification>(_dataDir + String("aspose-logo.jpg"), String("ملف صورة كبيرة"));
    // إضافة المرفق إلى مجموعة مرفقات المستند
    document->get_EmbeddedFiles()->Add(fileSpecification);

    // تحويل إلى مستند متوافق مع PDF/A
    // أثناء عملية التحويل، يتم أيضًا إجراء التحقق
    document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_3A, ConvertErrorAction::Delete);

    // حفظ المستند الناتج
    document->Save(_dataDir + outfilename);
    std::clog << __func__ << ": النهاية" << std::endl;
}
```

## استبدال الخطوط المفقودة بخطوط بديلة

وفقًا لمعايير PDFA، يجب تضمين الخطوط في مستند PDFA. ومع ذلك، إذا لم يتم تضمين الخطوط في المستند المصدر أو لم تكن موجودة على الجهاز، فإن PDFA يفشل في التحقق من الصحة. في هذه الحالة، لدينا مطلب لاستبدال الخطوط المفقودة ببعض الخطوط البديلة من الجهاز. يمكننا استبدال الخطوط المفقودة باستخدام طريقة SimpleFontSubsituation كما يلي أثناء تحويل PDF إلى PDFA.

```cpp
void ConverttoPDFA_ReplaceFont()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Conversion\\");

    // String for input file name
    String infilename("sample.pdf");
    // String for log file name
    String logfilename("log.xml");
    // String for input file name
    String outfilename("PDFToPDFA3b_out.pdf");

    // Open document
    auto document = new Document(_dataDir + infilename);

    System::SharedPtr<Aspose::Pdf::Text::Font> originalFont;
    try
    {
        originalFont = FontRepository::FindFont(String("AgencyFB"));
    }
    catch (Exception)
    {
        // Font is missing on destination machine
        auto substitutions = FontRepository::get_Substitutions();
        auto substitution = MakeObject<SimpleFontSubstitution>(String("AgencyFB"), String("Helvetica"));
        substitutions->Add(substitution);
    }

    // Convert to PDF/A compliant document
    try {
        // During conversion process, the validation is also performed
        document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_1B, ConvertErrorAction::Delete);

        // Save output document
        document->Save(_dataDir + outfilename);
    }
    catch (Exception ex) {
        std::cerr << ex->get_Message();
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```


{{% alert color="primary" %}}
**حاول تحويل PDF إلى PDF/A عبر الإنترنت**

تقدم لك Aspose.PDF for C++ تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![Aspose.PDF تحويل PDF إلى PDF/A مع تطبيق مجاني](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}
```