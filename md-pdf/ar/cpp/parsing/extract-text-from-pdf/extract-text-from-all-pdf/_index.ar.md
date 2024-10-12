---
title: استخراج النص من جميع صفحات PDF باستخدام C++
linktitle: استخراج النص من PDF
type: docs
weight: 10
url: /cpp/extract-text-from-all-pdf/
description: تصف هذه المقالة طرقًا مختلفة لاستخراج النص من مستندات PDF باستخدام Aspose.PDF في C++. من الصفحات الكاملة، من جزء محدد، بناءً على الأعمدة، إلخ.
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## استخراج النص من جميع صفحات مستند PDF

يعد استخراج النص من مستند PDF مطلبًا شائعًا. في هذا المثال، سترى كيف أن Aspose.PDF for C++ يسمح باستخراج النص من جميع صفحات مستند PDF. تحتاج إلى إنشاء كائن من فئة [TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber). بعد ذلك، افتح ملف PDF باستخدام فئة [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) واستدعِ طريقة 'Accept' لمجموعة [Pages](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page). تقوم فئة [TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber) بامتصاص النص من المستند وإعادته في خاصية 'Text'. يوضح لك مقطع الشيفرة التالي كيفية استخراج النص من جميع صفحات مستند PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ExtractTextFromAllThePages() {

    std::clog << __func__ << ": Start" << std::endl;
    // سلسلة لمسار الاسم
    String _dataDir("C:\\Samples\\Parsing\\");

    // سلسلة لاسم الملف
    String infilename("sample-4pages.pdf");
    String outfilename("extracted-text.txt");

    // افتح المستند
    auto document = MakeObject<Document>(_dataDir + infilename);

    // إنشاء كائن TextAbsorber لاستخراج النص
    auto textAbsorber = MakeObject<TextAbsorber>();
    // قبول الماصة لجميع الصفحات
    document->get_Pages()->Accept(textAbsorber);
    // الحصول على النص المستخرج
    auto extractedText = textAbsorber->get_Text();

    System::IO::File::WriteAllText(_dataDir + outfilename, extractedText);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
استدعِ طريقة **Accept** على صفحة معينة من كائن الوثيقة. الفهرس هو رقم الصفحة المحددة التي تحتاج إلى استخراج النص منها.

```cpp
void ExtractTextFromParticularPage() {

    std::clog << __func__ << ": Start" << std::endl;
    // سلسلة لاسم المسار
    String _dataDir("C:\\Samples\\Parsing\\");

    // سلسلة لاسم الملف
    String infilename("sample-4pages.pdf");
    String outfilename("extracted-text.txt");

    // افتح الوثيقة
    auto document = MakeObject<Document>(_dataDir + infilename);

    // إنشاء كائن TextAbsorber لاستخراج النص
    auto textAbsorber = MakeObject<TextAbsorber>();
    // قبول المستخلص لجميع الصفحات
    document->get_Pages()->idx_get(1)->Accept(textAbsorber);
    // الحصول على النص المستخرج
    auto extractedText = textAbsorber->get_Text();

    System::IO::File::WriteAllText(_dataDir + outfilename, extractedText);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## استخراج النص من الصفحات باستخدام جهاز النص

يمكنك استخدام فئة [TextDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.text_device/) لاستخراج النص من ملف PDF. يستخدم TextDevice كائن TextAbsorber في تنفيذه، وبالتالي، في الواقع، يقومون بنفس الشيء ولكن تم تنفيذ TextDevice فقط لتوحيد نهج "الجهاز" لاستخراج أي شيء من الصفحة مثل ImageDevice، PageDevice، إلخ. TextAbsorber يمكنه استخراج النص من الصفحة، أو ملف PDF بالكامل أو XForm، هذا TextAbsorber أكثر شمولاً

### استخراج النص من جميع الصفحات

توضح الخطوات التالية ومقتطف الشيفرة كيفية استخراج النص من ملف PDF باستخدام جهاز النص.

1. إنشاء كائن من فئة Document مع تحديد ملف PDF المدخل
1. إنشاء كائن من فئة TextDevice
1. استخدام كائن من فئة TextExtractOptions لتحديد خيارات الاستخراج
1. استخدام طريقة Process من فئة TextDevice لتحويل المحتويات إلى نص
1. حفظ النص في ملف الإخراج

```cpp
void ExtractTextUsingTextDevice() {

    std::clog << __func__ << ": Start" << std::endl;
    // سلسلة لاسم المسار
    String _dataDir("C:\\Samples\\Parsing\\");

    // سلسلة لاسم الملف
    String infilename("sample-4pages.pdf");
    String outfilename("extracted-text.txt");

    // فتح المستند
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto builder = MakeObject<System::Text::StringBuilder>();
    // سلسلة لحفظ النص المستخرج
    String extractedText;

    for (auto page : document->get_Pages()) {
        auto textStream = MakeObject<System::IO::MemoryStream>();
        // إنشاء جهاز النص
        auto textDevice = MakeObject<Aspose::Pdf::Devices::TextDevice>();

        // تعيين خيارات استخراج النص - تعيين وضع استخراج النص (خام أو نقي)
        auto textExtOptions = MakeObject<TextExtractionOptions>(TextExtractionOptions::TextFormattingMode::Pure);

        textDevice->set_ExtractionOptions(textExtOptions);

        // تحويل صفحة معينة وحفظ النص إلى التدفق
        textDevice->Process(page, textStream);

        // إغلاق تدفق الذاكرة
        textStream->Close();

        // الحصول على النص من تدفق الذاكرة
        extractedText = System::Text::Encoding::get_Unicode()->GetString(textStream->ToArray());
        builder->Append(extractedText);

    }
    // حفظ النص المستخرج في ملف نصي
    System::IO::File::WriteAllText(_dataDir + outfilename, builder->ToString());
    std::clog << __func__ << ": Finish" << std::endl;
}
```
## استخراج النص من منطقة معينة في الصفحة

توفر فئة [TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber) القدرة على استخراج النص من صفحة معينة أو جميع صفحات مستند PDF. تقوم هذه الفئة بإرجاع النص المستخرج في خاصية 'Text'. ومع ذلك، إذا كان لدينا الحاجة لاستخراج النص من منطقة معينة في الصفحة، يمكننا استخدام خاصية **Rectangle** في [TextSearchOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_search_options/). تأخذ خاصية Rectangle كائن مستطيل كقيمة وباستخدام هذه الخاصية، يمكننا تحديد المنطقة من الصفحة التي نحتاج لاستخراج النص منها.

يتم استدعاء طريقة **Accept** للصفحة لاستخراج النص. إنشاء كائنات من أصناف [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) و[TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber). استدعاء الطريقة 'Accept' على الصفحة الفردية، كــ **Page** Index، لكائن [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/). الــ **Index** هو رقم الصفحة المحددة التي يجب استخراج النص منها. يمكنك الحصول على النص من خاصية 'Text' في صنف [TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber). يوضح لك مقتطف الشيفرة التالي كيفية استخراج النص من صفحة فردية.

```cpp
void ExtractTextFromParticularPageRegion() {

    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Parsing\\");

    // String for file name
    String infilename("sample-4pages.pdf");
    String outfilename("extracted-text.txt");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Create TextAbsorber object to extract text
    auto textAbsorber = MakeObject<TextAbsorber>();
    textAbsorber->get_TextSearchOptions()->set_LimitToPageBounds(true);
    textAbsorber->get_TextSearchOptions()->set_Rectangle(MakeObject<Rectangle>(100, 200, 250, 350));

    // Accept the absorber for all the pages
    document->get_Pages()->idx_get(1)->Accept(textAbsorber);
    // Get the extracted text
    auto extractedText = textAbsorber->get_Text();

    System::IO::File::WriteAllText(_dataDir + outfilename, extractedText);
    std::clog << __func__ << ": Finish" << std::endl;

}
```
## استخراج النص بناءً على الأعمدة

PDF هو تنسيق شائع جدًا، ولسبب وجيه: مع PDF، يمكنك أن تكون متأكدًا تقريبًا من أن مستندك سيعرض ويطبع بنفس الطريقة على أجهزة كمبيوتر مختلفة.

ومع ذلك، تعاني مستندات PDF من العيب أنها عادة ما تفتقر إلى المعلومات حول ما هو المحتوى في الفقرات، الجداول، الرسوم، معلومات الرأس/التذييل، وهكذا.

Aspose.PDf for C++ - هي أداة سهلة الاستخدام، تتيح لك استخراج النص بناءً على الأعمدة.

```cpp
void ExtractTextBasedOnColumns() {

    std::clog << __func__ << ": Start" << std::endl;
    // سلسلة لأسم المسار
    String _dataDir("C:\\Samples\\Parsing\\");

    // سلسلة لأسم الملف
    String infilename("sample-4pages.pdf");
    String outfilename("extracted-text.txt");

    // فتح المستند
    auto document = MakeObject<Document>(_dataDir + infilename);

    // إنشاء كائن TextAbsorber لاستخراج النص
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>();


    // قبول ماص النصوص لجميع الصفحات
    document->get_Pages()->Accept(textFragmentAbsorber);

    auto tfc = textFragmentAbsorber->get_TextFragments();
    for (auto tf : tfc)
    {
        // الحاجة إلى تقليل حجم الخط بنسبة 70% على الأقل
        auto size = tf->get_TextState()->get_FontSize() * 0.7f;
        tf->get_TextState()->set_FontSize(size);
    }
    auto stream = MakeObject<System::IO::MemoryStream>();
    document->Save(stream);
    document = MakeObject<Document>(stream);
    auto textAbsorber = MakeObject<TextAbsorber>();
    document->get_Pages()->Accept(textAbsorber);
    String extractedText = textAbsorber->get_Text();

    System::IO::File::WriteAllText(_dataDir + outfilename, extractedText);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

### النهج الثاني - استخدام ScaleFactor

في هذا الإصدار الجديد، قمنا أيضًا بإدخال العديد من التحسينات في TextAbsorber وفي آلية تنسيق النص الداخلية. لذا الآن خلال استخراج النص باستخدام وضع "نقي"، يمكنك تحديد خيار [ScaleFactor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_extraction_options#a4f9a173765d483b493c31e416f8b035a) ويمكن أن يكون هذا نهجًا آخر لاستخراج النص من مستند PDF متعدد الأعمدة بجانب النهج المذكور أعلاه. يمكن ضبط عامل المقياس هذا لتعديل الشبكة التي تُستخدم لآلية تنسيق النص الداخلية خلال استخراج النص. تحديد قيم ScaleFactor بين 1 و0.1 (بما في ذلك 0.1) له نفس تأثير تقليل الخط.

يُعامل تحديد قيم ScaleFactor بين 0.1 و-0.1 كقيمة صفرية، لكنه يجعل الخوارزمية تحسب عامل المقياس اللازم خلال استخراج النص تلقائيًا. حساب يعتمد على متوسط عرض الحروف لأشهر خط في الصفحة، لكن لا يمكننا ضمان أنه في النص المستخرج لا يصل أي نص من عمود إلى بداية العمود التالي. يرجى ملاحظة أنه إذا لم يتم تحديد قيمة ScaleFactor، فسيتم استخدام القيمة الافتراضية 1.0. هذا يعني أنه لن يتم إجراء أي تغيير في الحجم. إذا كانت قيمة ScaleFactor المحددة أكثر من 10 أو أقل من -0.1، فسيتم استخدام القيمة الافتراضية 1.0.

نقترح استخدام تقليل تلقائي (ScaleFactor = 0) عند معالجة عدد كبير من ملفات PDF لاستخراج محتوى النص. أو قم بتعيين تقليل عرض الشبكة يدويًا (حوالي ScaleFactor = 0.5). ومع ذلك، لا يجب عليك تحديد ما إذا كان تقليل الحجم ضروريًا لوثائق معينة أم لا. إذا قمت بتعيين تقليل عرض الشبكة للوثيقة (التي لا تحتاج إليه)، سيظل محتوى النص المستخرج ملائمًا تمامًا. يرجى الاطلاع على مقتطف الشيفرة التالي.

```cpp
void ExtractTextUsingScaleFactor() {

    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Parsing\\");

    // String for file name
    String infilename("sample-4pages.pdf");
    String outfilename("extracted-text.txt");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto textAbsorber = MakeObject<TextAbsorber>();
    textAbsorber->set_ExtractionOptions(MakeObject<TextExtractionOptions>(TextExtractionOptions::TextFormattingMode::Pure));
    // Setting scale factor to 0.5 is enough to split columns in the majority of documents
    // Setting of zero allows to algorithm choose scale factor automatically
    textAbsorber->get_ExtractionOptions()->set_ScaleFactor(0.5); /* 0; */
    document->get_Pages()->Accept(textAbsorber);
    String extractedText = textAbsorber->get_Text();

    System::IO::File::WriteAllText(_dataDir + outfilename, extractedText);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
## استخراج النص المميز من مستند PDF

في مختلف سيناريوهات استخراج النص من مستند PDF، قد تواجه متطلبًا لاستخراج النص المميز فقط من مستند PDF. لتنفيذ هذه الوظيفة، قمنا بإضافة طريقتين TextMarkupAnnotation.GetMarkedText() و TextMarkupAnnotation.GetMarkedTextFragments() في API. يمكنك استخراج النص المميز من مستند PDF عن طريق تصفية TextMarkupAnnotation واستخدام الطرق المذكورة. يوضح مقطع الشيفرة التالي كيفية استخراج النص المميز من مستند PDF.

```cpp
void ExtractHighlightedText() {

    std::clog << __func__ << ": Start" << std::endl;
    // سلسلة لاسم المسار
    String _dataDir("C:\\Samples\\Parsing\\");

    // سلسلة لاسم الملف
    String infilename("sample-highlight.pdf");
    String outfilename("extracted-text.txt");

    // فتح المستند
    auto document = MakeObject<Document>(_dataDir + infilename);

    // التكرار عبر جميع التعليقات التوضيحية
    for (auto annotation : document->get_Pages()->idx_get(1)->get_Annotations())
    {
        // تصفية TextMarkupAnnotation
        if (annotation->get_AnnotationType() == Aspose::Pdf::Annotations::AnnotationType::Highlight)
        {
        auto highlightedAnnotation = System::DynamicCast<Aspose::Pdf::Annotations::HighlightAnnotation>(annotation);

        // استرجاع أجزاء النص المميزة
        auto collection = highlightedAnnotation->GetMarkedTextFragments();
        for (auto tf : collection)
        {
            // عرض النص المميز
            String s = tf->get_Text();
            std::cout << s << std::endl;
        }
        }
    }
}
```

## الوصول إلى عناصر النص والشرائح من XML

في بعض الأحيان نحتاج إلى الوصول إلى عناصر TextFragement أو TextSegment عند معالجة مستندات PDF التي تم إنشاؤها من XML. توفر Aspose.PDF for C++ الوصول إلى هذه العناصر بالاسم. يوضح مقتطف الكود أدناه كيفية استخدام هذه الوظيفة.

```cpp
void AccessTextFragmentandSegmentElementsXML()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Parsing\\");

    // String for file name
    String infilename("sample-doc.xml");
    String outfilename("sample-doc.pdf");

    auto document = MakeObject<Document>();
    document->BindXml(_dataDir + infilename);

    System::SharedPtr<Page> page = System::DynamicCast<Aspose::Pdf::Page>(document->GetObjectById(u"mainSection"));
    // إجراء بعض العمليات مع الصفحة
    // ...

    System::SharedPtr<TextSegment> segment = System::DynamicCast<Aspose::Pdf::Text::TextSegment>(document->GetObjectById(u"product_description"));
    // إجراء بعض العمليات مع الشريحة
    // ...
    document->Save(_dataDir + outfilename);

    std::clog << __func__ << ": Finish" << std::endl;
}
```