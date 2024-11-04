---
title: إنشاء مستند PDF
linktitle: إنشاء PDF
type: docs
weight: 10
url: /cpp/create-pdf-document/
description: توضح هذه المقالة كيفية إنشاء وتنسيق مستند PDF باستخدام Aspose.PDF لـ C++.
lastmod: "2021-11-11"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

نحن دائمًا نبحث عن طريقة لإنشاء مستندات PDF والعمل معها في مشاريع C++ بشكل أكثر دقة وفعالية. إن وجود وظائف سهلة الاستخدام من مكتبة يسمح لنا بتتبع المزيد من العمل، وأقل على التفاصيل التي تستغرق وقتًا طويلًا لمحاولة إنشاء ملفات PDF، سواء في C++.

## إنشاء PDF باستخدام C++

تتيح لك Aspose.PDF لـ C++ API إنشاء وقراءة ملفات PDF باستخدام C++. يمكن استخدام API في مجموعة متنوعة من تطبيقات C++ بما في ذلك WinForms، وعدة أخرى. في هذه المقالة، سنوضح كيفية استخدام Aspose.PDF لـ C++ API لتوليد وقراءة ملفات PDF بسهولة في تطبيقات C++.

### كيفية إنشاء ملف PDF بسيط

لإنشاء ملف PDF باستخدام C++، يمكن استخدام الخطوات التالية.

1. إنشاء كائن من فئة [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)  
1. إضافة كائن [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) إلى مجموعة 'Pages' لكائن Document  
1. إضافة [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment/) إلى مجموعة [Paragraphs](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.paragraphs) للصفحة  
1. حفظ مستند PDF الناتج  

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void CreateDocument() {
    // String for path name.
    String _dataDir("C:\\Samples\\");

    // String for file name.
    String outputFileName("HelloWorld_out.pdf");

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    // Add text to new page
    auto text = MakeObject<TextFragment>(u"Hello world!");

    auto paragraphs = page->get_Paragraphs();
    paragraphs->Add(text);

    // Save updated PDF
    document->Save(_dataDir + outputFileName);
}
```
## إنشاء مستند PDF قابل للبحث

يوفر Aspose.PDF for C ++ إمكانية إنشاء ملفات PDF من البداية ومعالجة الملفات الحالية. عندما تضيف عناصر نصية إلى ملف PDF، يكون ملف PDF الناتج قابلاً للبحث. ومع ذلك، إذا قمنا بتحويل صورة تحتوي على نص إلى ملف PDF، فإن المحتوى داخل ملف PDF لا يكون قابلاً للبحث. ومع ذلك، كحل بديل، يمكننا استخدام التعرف البصري على الأحرف (OCR) على الملف الناتج لجعله قابلاً للبحث. لذلك، يجب عليك أولاً تثبيت Tesseract-OCR على نظامك، وستحصل على تطبيق كونسول Tesseract.

فيما يلي الكود الكامل لتحقيق هذا المتطلب:

```cpp
void CreateSearchableDocument() {
    // String for path name.
    String _dataDir("C:\\Samples\\");
    // String for file name.
    String inputFileName("sample.pdf");

    auto document = MakeObject<Document>(inputFileName);
    bool convertResult = false;
    try
    {
        convertResult = document->Convert(CallBackGetHocr);
    }
    catch (Exception ex)
    {
        std::cerr << ex->get_Message() << std::endl;
    }
    document->Dispose();
}

static String CallBackGetHocr(System::SharedPtr<System::Drawing::Image> img)
{
    String tmpFile = System::IO::Path::GetTempFileNameSafe();

    auto bmp = MakeObject<System::Drawing::Bitmap>(img);

    bmp->Save(tmpFile, System::Drawing::Imaging::ImageFormat::get_Bmp());
    String inputFile = String::Format(u"\"{0}\"", tmpFile);
    String outputFile = String::Format(u"\"{0}\"", tmpFile);
    String arguments = inputFile + u" " + outputFile + u" -l eng hocr";
    String tesseractProcessName = u"C:\\Program Files\\Tesseract-OCR\\Tesseract.exe";

    auto psi = MakeObject<System::Diagnostics::ProcessStartInfo>(tesseractProcessName, arguments);
    psi->set_UseShellExecute(true);
    psi->set_CreateNoWindow(true);
    psi->set_WindowStyle(System::Diagnostics::ProcessWindowStyle::Hidden);
    psi->set_WorkingDirectory(System::IO::Path::GetDirectoryName(tesseractProcessName));

    auto p = MakeObject<System::Diagnostics::Process>(psi);
    p->Start();
    p->WaitForExit();

    auto streamReader = MakeObject<System::IO::StreamReader>(tmpFile + u".hocr");
    String text = streamReader->ReadToEnd();
    streamReader->Close();

    if (System::IO::File::Exists(tmpFile))
        System::IO::File::Delete(tmpFile);
    if (System::IO::File::Exists(tmpFile + u".hocr"))
        System::IO::File::Delete(tmpFile + u".hocr");

    return text;
}
```