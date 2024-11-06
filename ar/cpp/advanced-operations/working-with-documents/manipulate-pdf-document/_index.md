---
title: معالجة وثيقة PDF 
linktitle: معالجة وثيقة PDF 
type: docs
weight: 30
url: ar/cpp/manipulate-pdf-document/
lastmod: "2021-11-11"
description: تشرح هذه القسم عن التحقق من صحة وثيقة PDF لمعيار PDF A، كيفية العمل مع TOC، كيفية تعيين تاريخ انتهاء صلاحية PDF، وكيفية تحديد تقدم توليد ملف PDF.
lastmod: "2021-11-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## التحقق من وثيقة PDF لمعيار PDF A (A 1A و A 1B)

للتحقق من وثيقة PDF للتوافق مع PDF/A-1a أو PDF/A-1b، استخدم طريقة [Validate](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#aa1ac4565b320807c718c44eeee7cda8c) لفئة [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). تسمح لك هذه الطريقة بتحديد اسم الملف الذي سيتم حفظ النتيجة فيه ونوع التحقق المطلوب [PdfFormat](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#ac83739fd7c818167c2fdc4dd554de763) التعداد : PDF_A_1A أو PDF_A_1B.

{{% alert color="primary" %}}

تنسيق XML الناتج هو تنسيق Aspose مخصص. يحتوي XML على مجموعة من العلامات بالاسم Problem؛ تحتوي كل علامة على تفاصيل مشكلة معينة. يمثل السمة ObjectID للعلامة Problem معرف الكائن المحدد الذي تتعلق به هذه المشكلة. تمثل السمة Clause قاعدة مقابلة في مواصفات PDF.

{{% /alert %}}

يوضح لك مقتطف الشيفرة التالي كيفية التحقق من صحة مستند PDF لـ PDF/A-1A.

```cpp
void ExampleValidate01() {
    // String for path name.
    String _dataDir("C:\\Samples\\");

    // String for file name.
    String inputFileName("ValidatePDFAStandard.pdf");
    String outputFileName("Validation-result-A1A.xml");

    // Open document
    auto document = MakeObject<Document>(_dataDir + inputFileName);
    // Validate PDF for PDF/A-1a
    document->Validate(_dataDir + outputFileName, PdfFormat::PDF_A_1A);
}
```

يوضح لك مقتطف الشيفرة التالي كيفية التحقق من صحة مستند PDF لـ PDF/A-1B.

```cpp
void ExampleValidate02() {
    // String for path name.
    String _dataDir("C:\\Samples\\");

    // String for file name.
    String inputFileName("ValidatePDFAStandard.pdf");
    String outputFileName("Validation-result-A1B.xml");

    // Open document
    auto document = MakeObject<Document>(_dataDir + inputFileName);
    // Validate PDF for PDF/A-1a
    document->Validate(_dataDir + outputFileName, PdfFormat::PDF_A_1B);
}
```

## العمل مع جدول المحتويات

### إضافة جدول محتويات إلى ملف PDF موجود

تتيح لك Aspose.PDF API إضافة جدول محتويات عند إنشاء ملف PDF أو إلى ملف موجود.

لإضافة جدول محتويات إلى ملف PDF موجود، استخدم فئة [Heading](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.heading) في مساحة الأسماء Aspose.Pdf. تتيح لك مساحة الأسماء Aspose.Pdf إنشاء ملفات PDF جديدة والتلاعب بالملفات الموجودة. لإضافة جدول محتويات إلى ملف PDF موجود، استخدم مساحة الأسماء Aspose.Pdf.

يعرض مقتطف الشيفرة التالي كيفية إنشاء جدول محتويات داخل ملف PDF موجود.

```cpp
void ExampleToc01() {
    // سلسلة لأسماء المسارات.
    String _dataDir("C:\\Samples\\");

    // سلسلة لأسماء الملفات
    String inputFileName("AddTOC.pdf");
    String outputFileName("TOC_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // الوصول إلى الصفحة الأولى من ملف PDF
    auto tocPage = document->get_Pages()->Insert(1);

    // إنشاء كائن لتمثيل معلومات جدول المحتويات
    auto tocInfo = MakeObject<TocInfo>();
    auto title = MakeObject<TextFragment>("جدول المحتويات");
    title->get_TextState()->set_FontSize(20);
    title->get_TextState()->set_FontStyle(FontStyles::Bold);

    // تعيين العنوان لجدول المحتويات
    tocInfo->set_Title(title);
    tocPage->set_TocInfo(tocInfo);

    // إنشاء كائنات سلسلة سيتم استخدامها كعناصر جدول المحتويات
    auto titles = MakeArray<String>(4);
    titles->SetValue(u"الصفحة الأولى", 0);
    titles->SetValue(u"الصفحة الثانية", 1);
    titles->SetValue(u"الصفحة الثالثة", 2);
    titles->SetValue(u"الصفحة الرابعة", 3);

    for (int i = 0; i < 2; i++)
    {
        // إنشاء كائن العنوان
        auto heading2 = MakeObject<Heading>(1);
        auto segment2 = MakeObject<TextSegment>();
        heading2->set_TocPage(tocPage);
        heading2->get_Segments()->Add(segment2);

        // تحديد الصفحة الوجهة لكائن العنوان

        heading2->set_DestinationPage(document->get_Pages()->idx_get(i + 2));

        // الصفحة الوجهة
        heading2->set_Top(document->get_Pages()->idx_get(i + 2)->get_Rect()->get_Height());

        // إحداثيات الوجهة
        segment2->set_Text(titles[i]);

        // إضافة العنوان إلى الصفحة التي تحتوي على جدول المحتويات
        tocPage->get_Paragraphs()->Add(heading2);
    }

    // حفظ المستند المحدث
    document->Save(_dataDir + outputFileName);
}
```

### تعيين نوع TabLeaderType مختلف لمستويات TOC المختلفة

تسمح Aspose.PDF لـ C++ أيضًا بتعيين نوع TabLeaderType مختلف لمستويات TOC المختلفة. تحتاج إلى تعيين خاصية LineDash لـ FormatArray بالقيمة المناسبة لـ TabLeaderType. بعد ذلك، يمكنك إضافة قسم القائمة إلى مجموعة الأقسام في مستند Pdf. بعد ذلك، قم بإنشاء قسم في مستند Pdf واحفظ ملف PDF.

```cpp
void ExampleToc02() {
    // سلسلة لاسم المسار.
    String _dataDir("C:\\Samples\\");

    // سلسلة لاسم الملف.
    String inputFileName("AddTOC.pdf");

    String outputFileName("TOC_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto tocPage = document->get_Pages()->Add();
    auto tocInfo = MakeObject<TocInfo>();

    // تعيين نوع القائد
    tocInfo->set_LineDash(TabLeaderType::Solid);

    // إنشاء كائن لتمثيل معلومات TOC
    auto tocInfo = MakeObject<TocInfo>();
    auto title = MakeObject<TextFragment>("Table Of Contents");
    title->get_TextState()->set_FontSize(20);
    title->get_TextState()->set_FontStyle(FontStyles::Bold);

    // تعيين العنوان لـ TOC
    tocInfo->set_Title(title);

    // إضافة قسم القائمة إلى مجموعة الأقسام في مستند Pdf
    tocPage->set_TocInfo(tocInfo);

    // تعريف تنسيق قائمة المستويات الأربعة عن طريق تعيين الهوامش اليسرى
    // و
    // إعدادات تنسيق النص لكل مستوى

    tocInfo->set_FormatArrayLength(4);
    tocInfo->get_FormatArray()->idx_get(0)->get_Margin()->set_Left(0);
    tocInfo->get_FormatArray()->idx_get(0)->get_Margin()->set_Right(30);
    tocInfo->get_FormatArray()->idx_get(0)->set_LineDash(TabLeaderType::Dot);
    tocInfo->get_FormatArray()->idx_get(0)->get_TextState()->set_FontStyle(FontStyles::Bold | FontStyles::Italic);
    tocInfo->get_FormatArray()->idx_get(1)->get_Margin()->set_Left(10);
    tocInfo->get_FormatArray()->idx_get(1)->get_Margin()->set_Right(30);
    tocInfo->get_FormatArray()->idx_get(1)->set_LineDash(TabLeaderType::None);
    tocInfo->get_FormatArray()->idx_get(1)->get_TextState()->set_FontSize(10);
    tocInfo->get_FormatArray()->idx_get(2)->get_Margin()->set_Left(20);
    tocInfo->get_FormatArray()->idx_get(2)->get_Margin()->set_Right(30);
    tocInfo->get_FormatArray()->idx_get(2)->get_TextState()->set_FontStyle(FontStyles::Bold);
    tocInfo->get_FormatArray()->idx_get(3)->set_LineDash(TabLeaderType::Solid);
    tocInfo->get_FormatArray()->idx_get(3)->get_Margin()->set_Left(30);
    tocInfo->get_FormatArray()->idx_get(3)->get_Margin()->set_Right(30);
    tocInfo->get_FormatArray()->idx_get(3)->get_TextState()->set_FontStyle(FontStyles::Bold);

    // إنشاء قسم في مستند Pdf
    auto page = document->get_Pages()->Add();

    // إضافة أربعة عناوين في القسم
    for (int Level = 1; Level <= 4; Level++)
    {
    auto heading2 = MakeObject<Heading>(Level);
    auto segment2 = MakeObject<TextSegment>();

    heading2->get_Segments()->Add(segment2);
    heading2->set_IsAutoSequence(true);
    heading2->set_TocPage(tocPage);
    segment2->set_Text(u"Sample Heading" + Level);
    heading2->get_TextState()->set_Font(FontRepository::FindFont(u"Arial Unicode MS"));

    // إضافة العنوان إلى جدول المحتويات.
    heading2->set_IsInList(true);
    page->get_Paragraphs()->Add(heading2);
    }

    // حفظ ملف Pdf
    document->Save(_dataDir + outputFileName);
}
```

### إخفاء أرقام الصفحات في جدول المحتويات

إذا كنت ترغب في إخفاء أرقام الصفحات مع العناوين في جدول المحتويات، يمكنك استخدام خاصية [IsShowPageNumbers](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.toc_info#ada10e841699bba062dcd0b440c26b832) في فئة [TOCInfo](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.toc_info) كـ false.

يرجى مراجعة مقتطف الشيفرة التالي لإخفاء أرقام الصفحات في جدول المحتويات:

```cpp
void ExampleToc03() {
    // سلسلة لاسم المسار.
    String _dataDir("C:\\Samples\\");

    // سلسلة لاسم الملف.
    String inputFileName("AddTOC.pdf");

    String outputFileName("TOC_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);
    auto tocPage = document->get_Pages()->Add();

    // إنشاء كائن لتمثيل معلومات جدول المحتويات
    auto tocInfo = MakeObject<TocInfo>();
    auto title = MakeObject<TextFragment>("Table Of Contents");
    title->get_TextState()->set_FontSize(20);
    title->get_TextState()->set_FontStyle(FontStyles::Bold);

    // تعيين العنوان لجدول المحتويات
    tocInfo->set_Title(title);

    // إضافة قسم القائمة إلى مجموعة الأقسام في مستند Pdf
    tocPage->set_TocInfo(tocInfo);

    tocInfo->set_IsShowPageNumbers(false);

    // تعريف تنسيق قائمة المستويات الأربعة بتعيين الهوامش اليسرى
    // وإعدادات تنسيق النص لكل مستوى

    tocInfo->set_FormatArrayLength(4);
    tocInfo->get_FormatArray()->idx_get(0)->get_Margin()->set_Right(0);
    tocInfo->get_FormatArray()->idx_get(0)->get_TextState()->set_FontStyle(FontStyles::Bold | FontStyles::Italic);
    tocInfo->get_FormatArray()->idx_get(1)->get_Margin()->set_Left(30);
    tocInfo->get_FormatArray()->idx_get(1)->get_TextState()->set_Underline(true);
    tocInfo->get_FormatArray()->idx_get(1)->get_TextState()->set_FontSize(10);
    tocInfo->get_FormatArray()->idx_get(2)->get_TextState()->set_FontStyle(FontStyles::Bold);
    tocInfo->get_FormatArray()->idx_get(3)->get_TextState()->set_FontStyle(FontStyles::Bold);

    auto page = document->get_Pages()->Add();
    // إضافة أربعة عناوين في القسم
    for (int Level = 1; Level != 5; Level++)
    {
        auto heading2 = MakeObject<Heading>(Level);
        auto segment2 = MakeObject<TextSegment>();
        heading2->set_TocPage(tocPage);
        heading2->get_Segments()->Add(segment2);
        heading2->set_IsAutoSequence(true);
        segment2->set_Text(u"هذا هو عنوان المستوى " + Level);
        heading2->set_IsInList(true);
        page->get_Paragraphs()->Add(heading2);
    }
    // حفظ ملف Pdf
    document->Save(_dataDir + outputFileName);
}
```

## كيفية تعيين تاريخ انتهاء صلاحية PDF

نقوم بتطبيق امتيازات الوصول على ملفات PDF بحيث يمكن لمجموعة معينة من المستخدمين الوصول إلى ميزات/عناصر معينة من مستندات PDF. من أجل تقييد الوصول إلى ملف PDF، نقوم عادةً بتطبيق التشفير وقد يكون لدينا متطلب لتعيين انتهاء صلاحية ملف PDF، بحيث يحصل المستخدم الذي يصل/يعرض المستند على إشعار صالح بشأن انتهاء صلاحية ملف PDF.

من أجل تحقيق المتطلب المذكور أعلاه، يمكننا استخدام كائن [JavascriptAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.javascript_action/). يرجى التحقق من الكود المقتطف التالي.

```cpp
void SetPDFexpiryDate() {

    // String for path name.
    String _dataDir("C:\\Samples\\");

    // String for file name. 
    String outputFileName("SetExpiryDate_out.pdf");

    // Instantiate Document object
    auto document = MakeObject<Document>();

    // Add page to pages collection of PDF file
    document->get_Pages()->Add();

    // Add text fragment to paragraphs collection of page object
    document->get_Pages()->idx_get(1)->get_Paragraphs()->Add(new TextFragment(u"Hello World..."));

    String javascriptCode(u"var year=2017;");
    javascriptCode += u"var month=5;";
    javascriptCode += u"today = new Date(); today = new Date(today.getFullYear(), today.getMonth());";
    javascriptCode += u"expiry = new Date(year, month);";
    javascriptCode += u"if (today.getTime() > expiry.getTime())";
    javascriptCode += u"app.alert('The file is expired. You need a new one.');";

    // Create JavaScript object to set PDF expiry date
    auto javaScript = MakeObject<Aspose::Pdf::Annotations::JavascriptAction>(javascriptCode);

    // Set JavaScript as PDF open action
    document->set_OpenAction(javaScript);

    // Save PDF Document
    document->Save(_dataDir + outputFileName);
}
```

## تحديد تقدم إنشاء ملف PDF

طلب منا أحد العملاء إضافة ميزة تسمح للمطورين بتحديد تقدم إنشاء ملف PDF. إليك الرد على هذا الطلب.

حقل [CustomerProgressHandler](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.doc_save_options#a712bcc865fa8f75bbdc2a3b55e4581fb) في فئة [DocSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.doc_save_options) يسمح لك بتحديد كيفية تقدم إنشاء ملف PDF.

توضح مقتطفات الشيفرة أدناه كيفية استخدام [CustomerProgressHandler](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.doc_save_options#a712bcc865fa8f75bbdc2a3b55e4581fb).

```cpp
using ProgressHandler = System::MulticastDelegate<void(SharedPtr<UnifiedSaveOptions::ProgressEventHandlerInfo>)>;
void ConversionProgressCallback(SharedPtr<UnifiedSaveOptions::ProgressEventHandlerInfo> eventInfo)
{
    String eventType;
    switch (eventInfo->EventType)
    {
    case ProgressEventType::ResultPageCreated:
        eventType = u"ResultPageCreated";
        break;
    case ProgressEventType::ResultPageSaved:
        eventType = u"ResultPageSaved";
        break;
    case ProgressEventType::SourcePageAnalysed:
        eventType = u"SourcePageAnalysed";
        break;
    case ProgressEventType::TotalProgress:
        eventType = u"TotalProgress";
        break;
    }
    Console::WriteLine(String::Format(u"Event type: {0}, Value: {1}, MaxValue: {2}", 
        eventType, eventInfo->Value, eventInfo->MaxValue));
}
```

```cpp
void DetermineProgressOfPDFfileGeneration() {
    // String for path name.
    String _dataDir("C:\\Samples\\");

    // String for file name.
    String inputFileName("AddTOC.pdf");

    String outputFileName("TOC_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);
    // Open document
    auto saveOptions = MakeObject<DocSaveOptions>();

    saveOptions->CustomProgressHandler = ProgressHandler(ConversionProgressCallback);

    document->Save(_dataDir + outputFileName, saveOptions);
}
```

## تسطيح PDF القابلة للتعبئة في C++

غالبًا ما تتضمن مستندات PDF نماذج تحتوي على عناصر تفاعلية قابلة للتعبئة مثل أزرار الاختيار، مربعات الاختيار، مربعات النص، القوائم، وما إلى ذلك. لجعلها غير قابلة للتعديل لأغراض تطبيقية مختلفة، نحتاج إلى تسطيح ملف الPDF.
يوفر Aspose.PDF for C++ وظيفة لتسطيح الPDF في C++ ببضع سطور من الكود فقط:

```cpp
void FlattenFillablePDF() {
    // String for path name.
    String _dataDir("C:\\Samples\\");
    // String for file name.
    String inputFileName("sample-form.pdf");
    String outputFileName("FlattenForms_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // تسطيح PDF القابلة للتعبئة
    if (document->get_Form()->get_Fields()->get_Count() > 0)
    {
        for (auto item : document->get_Form()->get_Fields())
        item->Flatten();
    }

    // حفظ المستند المحدث
    document->Save(_dataDir + outputFileName);
}
```