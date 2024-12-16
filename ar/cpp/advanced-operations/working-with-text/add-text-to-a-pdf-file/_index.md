---
title: إضافة نص إلى PDF باستخدام C++
linktitle: إضافة نص إلى PDF
type: docs
weight: 10
url: /ar/cpp/add-text-to-pdf-file/
description: تصف هذه المقالة جوانب مختلفة من العمل مع النصوص في Aspose.PDF. تعلم كيفية إضافة نص إلى PDF، إضافة أجزاء HTML، أو استخدام خطوط OTF مخصصة.
lastmod: "2021-12-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## إضافة النص

لإضافة نص إلى ملف PDF موجود:

1. افتح ملف PDF المدخل باستخدام كائن Document.
2. احصل على الصفحة المحددة التي تريد إضافة النص إليها.
3. قم بإنشاء كائن TextFragment بالنص المدخل إلى جانب خصائص نصية أخرى. كائن TextBuilder الذي تم إنشاؤه من تلك الصفحة المحددة – التي تريد إضافة النص إليها – يتيح لك إضافة كائن TextFragment إلى الصفحة باستخدام طريقة AppendText.
4. استدعِ طريقة الحفظ لكائن Document واحفظ ملف PDF الناتج.

يظهر لك مقطع الشيفرة التالي كيفية إضافة نص في ملف PDF موجود.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddingText() {
    
    String _dataDir("C:\\Samples\\");

    // String for input file name
    String inputFileName("sample.pdf");
    // String for output file name
    String outputFileName("AddingText_out.pdf");

    // Load the PDF file
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // get particular page
    auto pdfPage = document->get_Pages()->idx_get(1);

    // create text fragment
    auto textFragment = MakeObject<TextFragment>("Aspose.PDF");
    textFragment->set_Position(MakeObject<Position>(80, 700));

    // set text properties
    textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"Verdana"));
    textFragment->get_TextState()->set_FontSize(14);
    textFragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
    textFragment->get_TextState()->set_BackgroundColor(Color::get_LightGray());

    // create TextBuilder object
    auto textBuilder = MakeObject<TextBuilder>(pdfPage);
    // append the text fragment to the PDF page
    textBuilder->AppendText(textFragment);

    // Save resulting PDF document.
    document->Save(_dataDir + outputFileName);
}
```

## تحميل الخط من Stream

يظهر مقطع الشيفرة التالي كيفية تحميل الخط من كائن Stream عند إضافة نص إلى مستند PDF.

```cpp
void LoadingFontFromStream() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("sample.pdf");
    String outputFileName("LoadingFontFromStream_out.pdf");

    String fontFile("C:\\Windows\\Fonts\\Arial.ttf");

    // تحميل ملف PDF المدخل
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // إنشاء كائن منشئ النص للصفحة الأولى من المستند
    auto textBuilder = MakeObject<TextBuilder>(document->get_Pages()->idx_get(1));
    // إنشاء جزء نصي مع سلسلة نصية نموذجية
    auto textFragment = MakeObject<TextFragment>("Hello world");

    if (!fontFile.IsNullOrEmpty()) {
        // تحميل الخط TrueType في كائن stream
        auto fontStream = System::IO::File::OpenRead(fontFile);
        // تعيين اسم الخط للسلسلة النصية
        textFragment->get_TextState()->set_Font(FontRepository::OpenFont(fontStream, FontTypes::TTF));
        // تحديد الموقع للجزء النصي
        textFragment->set_Position(MakeObject<Position>(10, 10));
        // إضافة النص إلى منشئ النص ليتم وضعه فوق ملف PDF
        textBuilder->AppendText(textFragment);

        // حفظ مستند PDF الناتج.
        document->Save(_dataDir + outputFileName);
    }
}
```


## إضافة نص باستخدام TextParagraph

يُظهر مقتطف الشيفرة التالي كيفية إضافة نص في مستند PDF باستخدام فئة [TextParagraph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_paragraph).

```cpp
void AddTextUsingTextParagraph() {

    String _dataDir("C:\\Samples\\");

    // فتح المستند
    auto document = MakeObject<Document>();

    String outputFileName("AddTextUsingTextParagraph_out.pdf");

    // إضافة صفحة إلى مجموعة الصفحات في كائن المستند
    auto page = document->get_Pages()->Add();
    auto builder = MakeObject<TextBuilder>(page);

    // إنشاء فقرة نصية
    auto paragraph = MakeObject<TextParagraph>();

    // تعيين المسافة البادئة للسطور التالية
    paragraph->set_SubsequentLinesIndent(20);

    // تحديد موقع إضافة TextParagraph
    paragraph->set_Rectangle(MakeObject<Rectangle>(100, 300, 200, 700));

    // تحديد وضع التفاف الكلمات
    paragraph->get_FormattingOptions()->set_WrapMode(TextFormattingOptions::WordWrapMode::ByWords);

    // إنشاء جزء نصي
    auto fragment1 = MakeObject<TextFragment>("the quick brown fox jumps over the lazy dog");
    fragment1->get_TextState()->set_Font(FontRepository::FindFont(u"Times New Roman"));
    fragment1->get_TextState()->set_FontSize(12);
    // إضافة الجزء إلى الفقرة
    paragraph->AppendLine(fragment1);
    // إضافة الفقرة
    builder->AppendParagraph(paragraph);

    // حفظ مستند PDF الناتج.
    document->Save(_dataDir + outputFileName);
}

```

## إضافة رابط تشعبي إلى TextSegment

قد تتكون صفحة PDF من كائنات TextFragment واحدة أو أكثر، حيث يمكن لكل كائن TextFragment أن يحتوي على أكثر من مثيل TextSegment. من أجل تعيين رابط تشعبي لـ TextSegment، يمكن استخدام خاصية Hyperlink لفئة [TextSegment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_segment) أثناء توفير كائن Aspose.Pdf.WebHyperlink. يرجى محاولة استخدام مقتطف الشيفرة التالي لتحقيق هذا المتطلب.

```cpp
void AddHyperlinkToTextSegment() {
    
    String _dataDir("C:\\Samples\\");
    String outputFileName("AddHyperlinkToTextSegment_out.pdf");

    // إنشاء مثيل للمستند
    auto document = MakeObject<Document>();

    // إضافة صفحة إلى مجموعة الصفحات لملف PDF
    auto page1 = document->get_Pages()->Add();

    // إنشاء مثيل TextFragment
    auto tf = MakeObject<TextFragment>("Sample Text Fragment");
    // تعيين المحاذاة الأفقية لـ TextFragment
    tf->set_HorizontalAlignment(HorizontalAlignment::Right);

    // إنشاء نص مقطع مع نص عينة
    auto segment = MakeObject<TextSegment>(" ... Text Segment 1...");
    // إضافة المقطع إلى مجموعة المقاطع لـ TextFragment
    tf->get_Segments()->Add(segment);

    // إنشاء TextSegment جديد
    segment = MakeObject<TextSegment>("Link to Google");
    // إضافة المقطع إلى مجموعة المقاطع لـ TextFragment

    tf->get_Segments()->Add(segment);

    // تعيين رابط تشعبي لـ TextSegment
    segment->set_Hyperlink(MakeObject<Aspose::Pdf::WebHyperlink>("www.aspose.com"));

    // تعيين لون المقدمة لمقطع النص
    segment->get_TextState()->set_ForegroundColor(Color::get_Blue());

    // تعيين تنسيق النص كـ مائل
    segment->get_TextState()->set_FontStyle(FontStyles::Italic);

    // إنشاء كائن TextSegment آخر
    segment = MakeObject<TextSegment>(u"TextSegment without hyperlink");

    // إضافة المقطع إلى مجموعة المقاطع لـ TextFragment
    tf->get_Segments()->Add(segment);

    // إضافة TextFragment إلى مجموعة الفقرات لكائن الصفحة
    page1->get_Paragraphs()->Add(tf);

    // حفظ مستند PDF الناتج.
    document->Save(_dataDir + outputFileName);

}
```

## استخدام خط OTF

يوفر Aspose.PDF لـ С++ ميزة استخدام الخطوط المخصصة/TrueType أثناء إنشاء/التلاعب بمحتويات ملف PDF بحيث يتم عرض المحتويات باستخدام خطوط غير الخطوط الافتراضية للنظام.

```cpp
void UseOTFFont() {

    String _dataDir("C:\\Samples\\");
    String outputFileName("OTFFont_out.pdf");

    // إنشاء مثيل وثيقة جديد    
    auto document = MakeObject<Document>();

    // إضافة صفحة إلى مجموعة الصفحات في ملف PDF
    auto page = document->get_Pages()->Add();

    // إنشاء مثيل TextFragment مع نص عينة
    auto fragment = MakeObject<TextFragment>("نص عينة بخط OTF");

    // أو يمكنك حتى تحديد مسار خط OTF في دليل النظام
    fragment->get_TextState()->set_Font(FontRepository::OpenFont(u"C:\\Samples\\Fonts\\Montserrat-Black.otf"));
    // تحديد تضمين الخط داخل ملف PDF، بحيث يتم عرضه بشكل صحيح،
    // حتى إذا لم يكن الخط المحدد مثبتًا/موجودًا على الجهاز المستهدف
    fragment->get_TextState()->get_Font()->set_IsEmbedded(true);
    // إضافة TextFragment إلى مجموعة الفقرات في مثيل الصفحة
    page->get_Paragraphs()->Add(fragment);
    // حفظ مستند PDF الناتج.
    document->Save(_dataDir + outputFileName);
}
```

## إضافة سلسلة HTML باستخدام DOM

تحتوي فئة Aspose.Pdf.Generator.Text على خاصية تُسمى IsHtmlTagSupported والتي تجعل من الممكن إضافة علامات/محتويات HTML إلى ملفات PDF. يتم عرض المحتوى المضاف في علامات HTML الأصلية بدلاً من الظهور كسلسلة نصية بسيطة. لدعم ميزة مماثلة في نموذج كائن الوثيقة الجديد (DOM) لمساحة الاسم Aspose.Pdf، تم تقديم فئة HtmlFragment.

يمكن استخدام مثيل [HtmlFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.html_fragment) لتحديد محتويات HTML التي يجب وضعها داخل ملف PDF. مثل TextFragment، فإن HtmlFragment هو كائن على مستوى الفقرة ويمكن إضافته إلى مجموعة الفقرات الخاصة بكائن الصفحة. تعرض القوالب البرمجية التالية الخطوات اللازمة لوضع محتويات HTML داخل ملف PDF باستخدام نهج DOM.

```cpp
void AddingHtmlString() {
    
    String _dataDir("C:\\Samples\\");

    // String for input file name
    String inputFileName("sample.pdf");

    // String for output file name
    String outputFileName("sample_html_out.pdf");

    // create Document instance
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Add a page to pages collection of PDF file
    auto page = document->get_Pages()->Add();

    // Instantiate HtmlFragment with HTML contents
    auto title = MakeObject<HtmlFragment>("<h1 style=\"color:blue\"><strong>HTML String Demo</strong></h1>");

    // set MarginInfo for margin details
    auto margin = MakeObject<MarginInfo>();
    margin->set_Bottom(10);
    margin->set_Top(200);
    // Set margin information
    title->set_Margin(margin);

    // Add HTML Fragment to paragraphs collection of page
    page->get_Paragraphs()->Add(title);
    // Save PDF file
    document->Save(_dataDir + outputFileName);
}
```

التالي هو مقتطف الكود الذي يوضح الخطوات لكيفية إضافة قوائم HTML مرتبة إلى المستند:

```cpp
void AddHTMLOrderedListIntoDocuments() {
    
    String _dataDir("C:\\Samples\\");

    // String for output file name
    String outputFileName("AddHTMLOrderedListIntoDocuments_out.pdf");

    // Instantiate Document object    
    auto document = MakeObject<Document>();

    // Instantiate HtmlFragment object with corresponding HTML fragment
    auto htmlFragment = MakeObject<HtmlFragment>(
        "<div style=\"font-family: sans-serif\"><ul><li>First</li><li>Second</li><li>Third</li><li>Fourth</li><li>Fifth</li></ul><p>Text after the list.</p><p>Next line<br/>Last line</p></div>");
    // Add Page in Pages Collection
    auto page = document->get_Pages()->Add();

    // Add HtmlFragment inside page
    page->get_Paragraphs()->Add(htmlFragment);

    // Save resultant PDF file
    document->Save(_dataDir + outputFileName);
}
```

يمكنك أيضًا تعيين تنسيق سلسلة HTML باستخدام كائن TextState كما يلي:

```cpp
void AddHTMLStringFormatting() {
    
    String _dataDir("C:\\Samples\\");

    // String for output file name
    String outputFileName("sample_html_out.pdf");

    // Instantiate Document object    
    auto document = MakeObject<Document>();

    // Add Page in Pages Collection
    auto page = document->get_Pages()->Add();

    // Instantiate HtmlFragment with HTML contents
    auto title = MakeObject<HtmlFragment>("<h1><strong>HTML String Demo</strong></h1>");

    auto textState = MakeObject<TextState>(12);

    textState->set_Font(FontRepository::FindFont(u"Calibri"));
    textState->set_ForegroundColor(Color::get_Green());
    textState->set_BackgroundColor(Color::get_Coral());
    title->set_TextState(textState);

    // Add HTML Fragment to paragraphs collection of page
    page->get_Paragraphs()->Add(title);
    // Save PDF file
    document->Save(_dataDir + outputFileName);
}
```

في حالة إذا قمت بتعيين قيم سمات النص عبر ترميز HTML ثم وفرت نفس القيم في خصائص TextState فإنها ستستبدل معلمات HTML بواسطة خصائص من نموذج TextState. تعرض مقتطفات الشيفرة التالية السلوك الموصوف.

```cpp
void AddHTMLUsingDOMAndOverwrite() {

    String _dataDir("C:\\Samples\\");
    // سلسلة لاسم ملف الإخراج
    String outputFileName("AddHTMLUsingDOMAndOverwrite_out.pdf");

    // إنشاء كائن Document
    auto document = MakeObject<Document>();

    // إضافة صفحة في مجموعة Pages
    auto page = document->get_Pages()->Add();

    // إنشاء HtmlFragment بمحتويات HTML
    auto title = MakeObject<HtmlFragment>("<p style='font-family: Verdana'><b><i>Table contains text</i></b></p>");

    // سيتم إعادة تعيين نوع الخط من 'Verdana' إلى 'Arial'
    title->set_TextState(new TextState(u"Arial Black"));
    title->set_TextState(new TextState(20));

    // ضبط معلومات الهامش السفلي
    title->get_Margin()->set_Bottom(10);
    // ضبط معلومات الهامش العلوي
    title->get_Margin()->set_Top(400);
    // إضافة HTML Fragment إلى مجموعة الفقرات في الصفحة
    page->get_Paragraphs()->Add(title);
    // حفظ ملف PDF
    document->Save(_dataDir + outputFileName);
}
```


## الحواشي والملاحظات الختامية (DOM)

تشير الحواشي إلى الملاحظات في نص ورقتك باستخدام أرقام مرتفعة متتالية. تكون الملاحظة الفعلية مسافة بادئة ويمكن أن تحدث كحاشية في أسفل الصفحة.

### إضافة حاشية

في نظام الإشارة بالحواشي، يتم الإشارة إلى المرجع عن طريق:

- وضع رقم صغير فوق خط الكتابة مباشرة بعد المادة المصدرية. يُسمى هذا الرقم معرف الملاحظة. يجلس قليلاً فوق سطر النص.
- وضع نفس الرقم، يليه اقتباس للمصدر الخاص بك، في أسفل الصفحة. يجب أن تكون الحواشي رقمية وزمنية: المرجع الأول هو 1، الثاني هو 2، وهكذا.

ميزة الحواشي هي أن القارئ يمكنه ببساطة إلقاء نظرة إلى أسفل الصفحة لاكتشاف مصدر المرجع الذي يهمهم.

اتبع الخطوات التالية:

- إنشاء مثيل من [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)
- إنشاء كائن [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page)

- إنشاء كائن [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment)
```
- قم بإنشاء مثيل Note ومرر قيمته إلى خاصية TextFragment [FootNote](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment#abe1663009fbceed84a0a392527463219)
- أضف TextFragment إلى مجموعة الفقرات لمثيل الصفحة

```cpp
void AddFootNote() {
    
    String _dataDir("C:\\Samples\\");

    // String for output file name
    String inputFileName("sample.pdf");
    String outputFileName("sample_footnote_out.pdf");

    // Instantiate Document object    
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Add Page in Pages Collection
    auto page = document->get_Pages()->idx_get(1);

    auto tfa = MakeObject<TextFragmentAbsorber>("Portable Document Format");
    tfa->Visit(page);

    auto t = tfa->get_TextFragments()->idx_get(1);
    auto note = MakeObject<Note>();
    note->set_Text(u"Demo");
    t->set_FootNote(note);

    // create TextFragment instance
    auto text = MakeObject<TextFragment>("Hello World");
    // set FootNote value for TextFragment
    text->set_FootNote(MakeObject<Note>("foot note for test text 1"));
    // add TextFragment to paragraphs collection of first page of document
    page->get_Paragraphs()->Add(text);
    // create second TextFragment
    text = MakeObject<TextFragment>("Aspose.Pdf for Java");
    // set FootNote for second text fragment
    text->set_FootNote(MakeObject<Note>("foot note for test text 2"));
    // add second text fragment to paragraphs collection of PDF file
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

### نمط خط مخصص للحاشية

يوضح المثال التالي كيفية إضافة حواشي إلى أسفل صفحة Pdf وتحديد نمط خط مخصص.

```cpp
void CustomFootNote_Line() {
    
    String _dataDir("C:\\Samples\\");

    // String for output file name    
    String outputFileName("customFootNote_Line.pdf");

    // إنشاء مثيل للمستند
    auto document = MakeObject<Document>();

    // إضافة صفحة إلى مجموعة الصفحات في PDF
    auto page = document->get_Pages()->Add();
    
    // إنشاء كائن GraphInfo
    auto graph = MakeObject<GraphInfo>();
    // تعيين عرض الخط كـ 2
    graph->set_LineWidth(2);
    // تعيين اللون لكائن الرسم
    graph->set_Color(Color::get_Red());
    // تعيين قيمة مصفوفة التقطيع كـ 3
    graph->set_DashArray(MakeArray<int>(3));
    // تعيين قيمة مرحلة التقطيع كـ 1
    graph->set_DashPhase(1);
    // تعيين نمط خط الحاشية للصفحة كالرسم
    page->set_NoteLineStyle(graph);

    // إنشاء مثيل لـ TextFragment
    auto text = MakeObject<TextFragment>("Hello World");
    // تعيين قيمة الحاشية لـ TextFragment
    text->set_FootNote(MakeObject<Note>("حاشية لنص الاختبار 1"));
    // إضافة TextFragment إلى مجموعة الفقرات في الصفحة الأولى من المستند
    page->get_Paragraphs()->Add(text);
    // إنشاء TextFragment ثاني
    text = MakeObject<TextFragment>("Aspose.Pdf for Java");
    // تعيين حاشية للنص الثاني
    text->set_FootNote(MakeObject<Note>("حاشية لنص الاختبار 2"));
    // إضافة النص الثاني إلى مجموعة الفقرات في ملف PDF
    page->get_Paragraphs()->Add(text);
    // حفظ ملف PDF
    document->Save(_dataDir + outputFileName);
}
```

يمكننا تعيين تنسيق تسمية الحاشية السفلية (معرف الملاحظة) باستخدام كائن TextState كما يلي:

```csharp
void AddCustomFootNoteLabel() {
    
    String _dataDir("C:\\Samples\\");

    // سلسلة لاسم الملف المدخل    
    String inputFileName("sample.pdf");

    // سلسلة لاسم الملف الناتج    
    String outputFileName("sample_footnote.pdf");

    // إنشاء مثيل Document
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto page = document->get_Pages()->idx_get(1);

    auto tfa = MakeObject<TextFragmentAbsorber>("Portable Document Format");
    tfa->Visit(page);

    auto t = tfa->get_TextFragments()->idx_get(1);
    auto note = MakeObject<Note>("Demo");
    t->set_FootNote(note);

    // إنشاء مثيل TextFragment
    auto text = MakeObject<TextFragment>("Hello World");
    // تعيين قيمة الحاشية السفلية لـ TextFragment
    text->set_FootNote(MakeObject<Note>("foot note for test text 1"));
    text->get_FootNote()->set_Text(u"21");

    auto ts = MakeObject<TextState>();
    ts->set_ForegroundColor(Color::get_Blue());
    ts->set_FontStyle(FontStyles::Italic);
    text->get_FootNote()->set_TextState(ts);

    // إضافة TextFragment إلى مجموعة الفقرات على الصفحة الأولى للوثيقة
    page->get_Paragraphs()->Add(text);
    // إنشاء TextFragment ثاني
    text = MakeObject<TextFragment>(u"Aspose.Pdf for C++");
    // تعيين الحاشية السفلية للجزء الثاني من النص
    text->set_FootNote(MakeObject<Note>("foot note for test text 2"));
    // إضافة الجزء الثاني من النص إلى مجموعة الفقرات في ملف PDF
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

### تخصيص تسمية الحاشية

افتراضيًا، يكون رقم الحاشية تزايديًا بدءًا من 1. ومع ذلك، قد يكون لدينا متطلب لتعيين تسمية حاشية مخصصة. لتحقيق هذا المتطلب، يرجى محاولة استخدام مقتطف الشيفرة التالي

```cpp
void CustomFootNote_Label() {

    String _dataDir("C:\\Samples\\");
    // String for output file name    
    String outputFileName("CustomizeFootNoteLabel_out.pdf");

    // Create Document instance
    auto document = MakeObject<Document>();

    // Add page to pages collection of PDF
    auto page = document->get_Pages()->Add();

    // Create GraphInfo object
    auto graph = MakeObject<GraphInfo>();

    // Set line width as 2
    graph->set_LineWidth(2);

    // Set the color for graph object
    graph->set_Color(Color::get_Red());

    // Set dash array value as 3
    graph->set_DashArray(MakeArray<int>(3));

    // Set dash phase value as 1
    graph->set_DashPhase(1);

    // Set footnote line style for page as graph
    page->set_NoteLineStyle(graph);

    // Create TextFragment instance
    auto text = MakeObject<TextFragment>("Hello World");
    // Set FootNote value for TextFragment
    text->set_FootNote(MakeObject<Note>("foot note for test text 1"));
    // Specify custom label for FootNote
    text->get_FootNote()->set_Text(u" Aspose(2021)");
    // Add TextFragment to paragraphs collection of first page of document
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

## إضافة صورة وجدول إلى الحاشية

يعرض مقتطف الشيفرة التالي الخطوات لإضافة [حاشية](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment#a017ff999979d9f799b8e3cd32ab95722) إلى كائن [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment) ثم إضافة كائن الصورة والجدول إلى مجموعة الفقرات في قسم الحاشية.

```cpp

void AddingImageAndTableToFootnote() {
    
    String _dataDir("C:\\Samples\\");

    // String for output file name    
    String outputFileName("AddImageAndTableToFootNote_out.pdf");

    // Create Document instance
    auto document = new Document();
    // Add page to pages collection of PDF
    auto page = document->get_Pages()->Add();

    // Create TextFragment instance
    auto text = MakeObject<TextFragment>("Hello World");

    page->get_Paragraphs()->Add(text);

    text->set_FootNote(MakeObject<Note>());
    auto image = MakeObject<Image>();
    image->set_File(_dataDir + u"aspose-logo.jpg");
    image->set_FixHeight(20);

    text->get_FootNote()->get_Paragraphs()->Add(image);

    auto footNote = MakeObject<TextFragment>("footnote text");
    footNote->get_TextState()->set_FontSize(20);
    footNote->set_IsInLineParagraph(true);
    text->get_FootNote()->get_Paragraphs()->Add(footNote);
    
    auto table = MakeObject<Table>();
    table->get_Rows()->Add()->get_Cells()->Add()->get_Paragraphs()->Add(MakeObject<TextFragment>("Row 1 Cell 1"));
    text->get_FootNote()->get_Paragraphs()->Add(table);

    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

## كيفية إنشاء الحواشي

الحاشية هي استشهاد بالمصدر يشير القراء إلى مكان محدد في نهاية الورقة حيث يمكنهم معرفة مصدر المعلومات أو الكلمات المقتبسة أو المذكورة في الورقة. عند استخدام الحواشي، يتبع جملتك المقتبسة أو المُعاد صياغتها أو المادة المُلخصة برقم مرتفع.

يوضح المثال التالي كيفية إضافة الحاشية في صفحة PDF.

```cpp
void HowToCreateEndNotes() {
    
    String _dataDir("C:\\Samples\\");

    // String for output file name    
    String outputFileName("endNote_out.pdf");

    // Create Document instance
    auto document = new Document();
    // Add page to pages collection of PDF
    auto page = document->get_Pages()->Add();

    // create TextFragment instance
    auto text = MakeObject<TextFragment>("Hello World");

    // set FootNote value for TextFragment
    text->set_EndNote(MakeObject<Note>("sample End note"));

    // specify custom label for FootNote
    text->get_EndNote()->set_Text(u" Aspose(2021)");
    // add TextFragment to paragraphs collection of first page of document
    page->get_Paragraphs()->Add(text);
    // save the PDF file
    document->Save(_dataDir + outputFileName);
}
```

## نص وصورة كفقرة مدمجة

التخطيط الافتراضي لملف PDF هو تخطيط متدفق (من الأعلى-اليسار إلى الأسفل-اليمين). لذلك يتم إضافة كل عنصر جديد يُضاف إلى ملف PDF في التدفق السفلي الأيمن. ومع ذلك، قد نحتاج إلى عرض عناصر صفحة مختلفة، أي صورة ونص في نفس المستوى (واحد بعد الآخر). يمكن أن تكون إحدى الطرق إنشاء مثيل جدول وإضافة كلا العنصرين إلى كائنات الخلايا الفردية. ومع ذلك، يمكن أن تكون طريقة أخرى هي الفقرة المدمجة. من خلال تعيين خاصية IsInLineParagraph للصورة والنص كحقيقة، ستظهر هذه الفقرات كمدمجة مع عناصر الصفحة الأخرى.

يوضح لك مقتطف الشيفرة التالي كيفية إضافة نص وصورة كفقرات مدمجة في ملف PDF.

```cpp
void TextAndImageAsInLineParagraph() {

    String _dataDir("C:\\Samples\\");
    String outputFileName("TextAndImageAsParagraph_out.pdf");

    // Instantiate Document instance
    auto document = MakeObject<Document>();

    // Add page to pages collection of Document instance
    auto page = document->get_Pages()->Add();

    // Create TextFragmnet
    auto text = MakeObject<TextFragment>("Hello World.. ");
    // Add text fragment to paragraphs collection of Page object
    page->get_Paragraphs()->Add(text);

    // Create an image instance
    auto image = MakeObject<Image>();

    // Set image as inline paragraph so that it appears right after
    // The previous paragraph object (TextFragment)
    image->set_IsInLineParagraph(true);

    // Specify image file path
    image->set_File(_dataDir + u"aspose-logo.jpg");
    // Set image Height (optional)
    image->set_FixHeight(30);
    // Set Image Width (optional)
    image->set_FixWidth(100);
    // Add image to paragraphs collection of page object
    page->get_Paragraphs()->Add(image);
    // Re-initialize TextFragment object with different contents
    text = MakeObject<TextFragment>(" Hello Again..");
    // Set TextFragment as inline paragraph
    text->set_IsInLineParagraph(true);
    // Add newly created TextFragment to paragraphs collection of page
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

## تحديد تباعد الحروف عند إضافة نص

يمكن إضافة النص إلى مجموعة الفقرات في ملف PDF باستخدام مثيل TextFragment أو كائن TextParagraph، ويمكنك أيضًا ختم النص داخل ملف PDF باستخدام فئة TextStamp. عند إضافة النص، قد نحتاج إلى تحديد التباعد بين الحروف لكائنات النص. لتلبية هذا المتطلب، تم تقديم خاصية جديدة باسم CharacterSpacing.

يرجى النظر في الأساليب التالية لتلبية هذا المتطلب.

تظهر الأساليب التالية الخطوات لتحديد تباعد الحروف عند إضافة نص داخل مستند PDF.

### استخدام TextBuilder وTextFragment

```cpp
// تحديد تباعد الحروف عند إضافة نص باستخدام TextBuilder وTextFragment
void CharacterSpacing_TextFragment() {
    
    String _dataDir("C:\\Samples\\");

    // سلسلة لاسم ملف الإخراج
    String outputFileName("CharacterSpacingUsingTextBuilderAndFragment_out.pdf");

    // إنشاء مثيل للمستند
    auto document = MakeObject<Document>();
    // إضافة صفحة إلى مجموعة الصفحات في المستند
    auto page = document->get_Pages()->Add();

    // إنشاء مثيل TextBuilder
    auto builder = MakeObject<TextBuilder>(page);

    // إنشاء مثيل نصي مع محتويات نموذجية
    auto wideFragment = MakeObject<TextFragment>("Text with increased character spacing");
    wideFragment->get_TextState()->ApplyChangesFrom(MakeObject<TextState>("Arial", 12));

    // تحديد تباعد الحروف لـ TextFragment
    wideFragment->get_TextState()->set_CharacterSpacing(2.0f);

    // تحديد موضع TextFragment
    wideFragment->set_Position(MakeObject<Position>(100, 650));

    // إلحاق TextFragment بمثيل TextBuilder
    builder->AppendText(wideFragment);

    // حفظ مستند PDF الناتج.
    document->Save(_dataDir + outputFileName);
}
```

### استخدام TextParagraph

```cpp
void CharacterSpacing_TextParagraph() {
    
    String _dataDir("C:\\Samples\\");

    // سلسلة لاسم الملف الناتج
    String outputFileName("CharacterSpacingUsingTextBuilderAndFragment_out.pdf");

    // إنشاء مثيل للوثيقة
    auto document = MakeObject<Document>();

    // إضافة صفحة إلى مجموعة الصفحات في الوثيقة
    auto page = document->get_Pages()->Add();

    // إنشاء مثيل TextBuilder
    auto builder = MakeObject<TextBuilder>(page);

    // إنشاء مثيل TextParagraph
    auto paragraph = MakeObject<TextParagraph>();

    // إنشاء مثيل TextState لتحديد اسم الخط والحجم
    auto state = MakeObject<TextState>("Arial", 12);

    // تحديد تباعد الأحرف
    state->set_CharacterSpacing(1.5f);

    // إضافة نص إلى كائن TextParagraph
    paragraph->AppendLine(u"This is paragraph with character spacing", state);

    // تحديد الموقع لـ TextParagraph
    paragraph->set_Position(MakeObject<Position>(100, 550));

    // إضافة TextParagraph إلى مثيل TextBuilder
    builder->AppendParagraph(paragraph);

    // حفظ مستند PDF الناتج.
    document->Save(_dataDir + outputFileName);
}
```

### باستخدام TextStamp

```cpp
void CharacterSpacing_TextStamp() {
    
    String _dataDir("C:\\Samples\\");
    String outputFileName("CharacterSpacingUsingTextStamp_out.pdf");
    // إنشاء مثيل للمستند
    auto document = MakeObject<Document>();

    // إضافة صفحة إلى مجموعة الصفحات في المستند   
    auto page = document->get_Pages()->Add();

    // إنشاء مثيل TextStamp مع نص عينة
    auto stamp = MakeObject<TextStamp>("هذه طابع نصي مع تباعد بين الحروف");

    // تحديد اسم الخط لكائن الطابع
    stamp->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
    // تحديد حجم الخط لـ TextStamp
    stamp->get_TextState()->set_FontSize(12);
    // تحديد تباعد الحروف كـ 1f
    stamp->get_TextState()->set_CharacterSpacing(1.0f);
    // تعيين XIndent للطابع
    stamp->set_XIndent(100);
    // تعيين YIndent للطابع
    stamp->set_YIndent(500);
    // إضافة الطابع النصي إلى مثيل الصفحة
    stamp->Put(page);
    // حفظ مستند PDF الناتج.
    document->Save(_dataDir + outputFileName);
}
```

## إنشاء مستند PDF متعدد الأعمدة

يستعرض هذا الموضوع كيفية إنشاء مستند PDF متعدد الأعمدة باستخدام Aspose.Pdf لـ C++.

في الوقت الحاضر، نرى الأخبار غالبًا معروضة في أعمدة متعددة على صفحات منفصلة، بدلاً من الكتب، حيث تُطبع الفقرات النصية غالبًا على جميع الصفحات من اليسار إلى اليمين. تتيح العديد من تطبيقات معالجة المستندات، مثل Microsoft Word وAdobe Acrobat Writer، للمستخدمين إنشاء أعمدة متعددة على صفحة واحدة ثم إضافة البيانات إليها.

يوفر Aspose.Pdf لـ C++ أيضًا القدرة على إنشاء أعمدة متعددة في صفحات مستند PDF. لإنشاء PDF مع أعمدة متعددة، يمكننا استخدام فئة [Aspose.Pdf.FloatingBox](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.floating_box) حيث توفر خاصية ColumnInfo.ColumnCount لتحديد عدد الأعمدة داخل FloatingBox، ويمكننا أيضًا تحديد تباعد الأعمدة وعرض الأعمدة باستخدام ColumnInfo.ColumnSpacing وColumnInfo.ColumnWidths على التوالي.

يُعطى المثال أدناه لتوضيح إنشاء عمودين مع كائنات رسومية (خط) ويتم إضافتها إلى مجموعة الفقرات لـ FloatingBox، التي تُضاف بعدها إلى مجموعة الفقرات لنسخة Page.

```cpp
void CreateMultiColumn() {

    String _dataDir("C:\\Samples\\");
    String outputFileName("CreateMultiColumnPdf_out.pdf");

    // إنشاء مثيل مستند جديد
    auto document = MakeObject<Document>();

    // تحديد معلومات الهامش الأيسر لملف PDF
    document->get_PageInfo()->get_Margin()->set_Left(40);

    // تحديد معلومات الهامش الأيمن لملف PDF
    document->get_PageInfo()->get_Margin()->set_Right(40);

    // إضافة صفحة إلى مجموعة الصفحات لملف PDF
    auto page = document->get_Pages()->Add();

    auto graph1 = MakeObject<Aspose::Pdf::Drawing::Graph>(500, 2);

    // إضافة الخط إلى مجموعة الفقرات لكائن القسم
    page->get_Paragraphs()->Add(graph1);

    // تحديد إحداثيات الخط
    auto posArr = MakeArray<float>({ 1, 2, 500, 2 });
    auto l1 = MakeObject<Aspose::Pdf::Drawing::Line>(posArr);
    graph1->get_Shapes()->Add(l1);

    // إنشاء متغيرات سلسلة تحتوي على نص يحتوي على وسوم HTML
    String s ("<span style=\"font-family: \"Times New Roman\", Times, serif;\" font-size=\"14pt\" \">\
<strong> كيفية تجنب عمليات الاحتيال المالي </<strong> </span>");

    // إنشاء فقرات نصية تحتوي على نص HTML

    auto heading_text = MakeObject<HtmlFragment>(s);
    page->get_Paragraphs()->Add(heading_text);

    auto box = MakeObject<FloatingBox>();

    // إضافة أربعة أعمدة في القسم
    box->get_ColumnInfo()->set_ColumnCount(2);
    // ضبط المسافة بين الأعمدة
    box->get_ColumnInfo()->set_ColumnSpacing(u"5");

    box->get_ColumnInfo()->set_ColumnWidths(u"105 105");
    auto text1 = MakeObject<TextFragment>("بقلم غوغلر (المدونة الرسمية لجوجل)");
    text1->get_TextState()->set_FontSize(8);
    text1->get_TextState()->set_LineSpacing(2);
    text1->get_TextState()->set_FontSize(10);
    text1->get_TextState()->set_FontStyle(FontStyles::Italic);

    box->get_Paragraphs()->Add(text1);

    // إنشاء كائن رسومات لرسم خط
    auto graph2 = MakeObject<Aspose::Pdf::Drawing::Graph>(50, 10);
    // تحديد إحداثيات الخط
    auto posArr2 = MakeArray<float>({ 1, 10, 100, 10 });

    auto l2 = MakeObject<Aspose::Pdf::Drawing::Line>(posArr2);
    graph2->get_Shapes()->Add(l2);

    // إضافة الخط إلى مجموعة الفقرات لكائن القسم
    box->get_Paragraphs()->Add(graph2);

    auto text2 = MakeObject<TextFragment>(
        "سد أوج تور، صودالس إد، لوكتس إت، بولفينار أوت، إيروس. سوسبيندسه فيل دولار. \
        سد كوام. كيورابيتور أوت ماسا فيتاي إيروس أيوسمود أليكوام. بيلنتيسك سيت أميت إليت. فيستيبيولوم إنديردوم بيلنتيسك أوج.\
        كراس موليس أركو سيت أميت بوروس. دونك أوج. نام موليس تورتر أ إليت. نولا فيفيرا نيسل فيل موريس. فيفاموس سابين. ناسكتور \
        ريديكولوس موس. نام جوستو لوريم، أليكوام لوكتس، صودالس إت، سيمبر سد، إنيم نام جوستو لوريم، أليكوام لوكتس، صودالس إت، أيين \
        بوسير أنتي أوت نيكي. موربي سوليسيتودين كونج فيليس. برازينت توربيس ديام، إيكوليس سد، فاريترا نون، موليس أك، موريس. \
        فاسيليسيس نيسي إيبسوم، بريتيوم فيتاي، تيمبور سد، موليستيه إيو، دوي. دويس لاكوس بوروس، تريستيك أوت، إيكوليس كورسوس، تينكينت فيتاي، \
        ريزوس. سد كومودو. *** سوسيس ناتوك بيناتيوبس إت ماجنيس ديس بارتورينت مونتيس، ناسكتور ريديكولوس موس. نام جوستو لوريم، أليكوام \
        لوكتس، صودالس إت، سيمبر سد، إنيم نام جوستو لوريم، أليكوام لوكتس، صودالس إت، سيمبر سد، إنيم نام جوستو لوريم، أليكوام لوكتس، \
        صودالس إت، سيمبر سد، إنيم أيين بوسير أنتي أوت نيكي. موربي سوليسيتودين كونج فيليس. برازينت توربيس ديام، إيكوليس سد، \
        فاريترا نون، موليس أك، موريس. فاسيليسيس نيسي إيبسوم، بريتيوم فيتاي، تيمبور سد، موليستيه إيو، دوي. دويس لاكوس بوروس، تريستيك أوت،\
        إيكوليس كورسوس، تينكينت فيتاي، ريزوس. سد كومودو. *** سوسيس ناتوك بيناتيوبس إت ماجنيس ديس بارتورينت مونتيس، ناسكتور ريديكولوس \
        موس. سد أورنا. . دويس كونفاليس ألتريس نيسي. مايكيناس نون ليجولا. نونك نيب إست، تينكينت إن، بليسيرات سيت أميت، فيستيبيولوم أ، نولا.\
        برازينت بورتتور توربيس إيليفند أنت. موربي صودالس. أيين بوسير أنتي أوت نيكي. موربي سوليسيتودين كونج فيليس. برازينت توربيس ديام,\
        إيكوليس سد، فاريترا نون، موليس أك، موريس. فاسيليسيس نيسي إيبسوم، بريتيوم فيتاي، تيمبور سد، موليستيه إيو، دوي. دويس لاكوس بوروس، تريستيك\
        أوت، إيكوليس كورسوس، تينكينت فيتاي، ريزوس. سد كومودو. *** سوسيس ناتوك بيناتيوبس إت ماجنيس ديس بارتورينت مونتيس، ناسكتور ريديكولوس موس.\
        سد أورنا. . دويس كونفاليس ألتريس نيسي. مايكيناس نون ليجولا. نونك نيب إست، تينكينت إن، بليسيرات سيت أميت، فيستيبيولوم أ، نولا. \
        برازينت بورتتور توربيس إيليفند أنت. موربي صودالس.");
    box->get_Paragraphs()->Add(text2);

    page->get_Paragraphs()->Add(box);

    // حفظ ملف PDF
    document->Save(_dataDir + outputFileName);
}
```

## العمل مع نقاط التوقف المخصصة للتبويب

نقطة توقف التبويب هي نقطة توقف للتبويب. في معالجة الكلمات، يحتوي كل سطر على عدد من نقاط التوقف للتبويب الموضوعة على فترات منتظمة (على سبيل المثال، كل نصف بوصة). يمكن تغييرها، ومع ذلك، حيث تسمح معظم معالجات النصوص لك بتعيين نقاط التوقف للتبويب في أي مكان تريده. عندما تضغط على مفتاح التبويب، يقفز المؤشر أو نقطة الإدخال إلى نقطة التوقف التالية، التي تكون غير مرئية بذاتها. على الرغم من أن نقاط التوقف للتبويب لا توجد في ملف النص، إلا أن معالج النصوص يتتبعها بحيث يمكنه التفاعل بشكل صحيح مع مفتاح التبويب.

هنا مثال على كيفية تعيين نقاط توقف التبويب المخصصة.

```cpp
void CustomTabStops() {
    String _dataDir("C:\\Samples\\");
    String outputFileName("CustomTabStops_out.pdf");

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto ts = MakeObject<TabStops>();
    auto ts1 = ts->Add(100);

    ts1->set_AlignmentType(TabAlignmentType::Right);
    ts1->set_LeaderType(TabLeaderType::Solid);

    auto ts2 = ts->Add(200);
    ts2->set_AlignmentType(TabAlignmentType::Center);
    ts2->set_LeaderType(TabLeaderType::Dash);

    auto ts3 = ts->Add(300);
    ts3->set_AlignmentType(TabAlignmentType::Left);
    ts3->set_LeaderType(TabLeaderType::Dot);

    auto header = MakeObject<TextFragment>("This is a example of forming table with TAB stops", ts);
    auto text0 =  MakeObject<TextFragment>("#$TABHead1 #$TABHead2 #$TABHead3", ts);

    auto text1 = MakeObject<TextFragment>("#$TABdata11 #$TABdata12 #$TABdata13", ts);
    auto text2 = MakeObject<TextFragment>("#$TABdata21 ", ts);
    text2->get_Segments()->Add(MakeObject<TextSegment>("#$TAB"));
    text2->get_Segments()->Add(MakeObject<TextSegment>("data22 "));
    text2->get_Segments()->Add(MakeObject<TextSegment>("#$TAB"));
    text2->get_Segments()->Add(MakeObject<TextSegment>("data23"));
              
    page->get_Paragraphs()->Add(header);
    page->get_Paragraphs()->Add(text0);
    page->get_Paragraphs()->Add(text1);
    page->get_Paragraphs()->Add(text2);

    document->Save(_dataDir + outputFileName);
}
```

## كيفية إضافة نص شفاف في PDF

كانت PDF 1.4 (وهو تنسيق ملف مدعوم من Acrobat 5) هي النسخة الأولى من PDF التي تدعم الشفافية. ظهر هذا النوع من PDF في السوق في نفس الوقت تقريبًا مع Adobe Illustrator 9.

يحتوي ملف PDF على كائنات مثل الصورة، النص، الرسم البياني، المرفقات، والتعليقات، وأثناء إنشاء TextFragment، يمكنك تعيين معلومات اللون الأمامي والخلفي وكذلك تنسيق النص. يدعم Aspose.PDF for C++ ميزة إضافة النص مع قناة لون ألفا. يوضح الشيفرة التالية كيفية إضافة نص بلون شفاف.

```cpp
void AddTransparentText() {

    String _dataDir("C:\\Samples\\");
    String outputFileName("AddTransparentText_out.pdf");

    // Create Document instance
    auto document = MakeObject<Document>();    
    // Create page to pages collection of PDF file
    auto page = document->get_Pages()->Add();

    // Create Graph object
    auto canvas = MakeObject<Aspose::Pdf::Drawing::Graph>(100, 400);

    // Create rectangle instance with certain dimensions
    auto rect = MakeObject<Aspose::Pdf::Drawing::Rectangle>(100, 100, 400, 400);
    // Create color object from Alpha color channel
    int alpha = 10;
    int green = 0;
    int red = 100;
    int blue = 0;

    auto alphaColor = Color::FromArgb(alpha, red, green, blue);

    rect->get_GraphInfo()->set_FillColor(alphaColor);

    // Add rectanlge to shapes collection of Graph object
    canvas->get_Shapes()->Add(rect);

    // Add graph object to paragraphs collection of page object
    page->get_Paragraphs()->Add(canvas);

    // Set value to not change position for graph object
    canvas->set_IsChangePosition(false);

    // Create TextFragment instance with sample value
    auto text = MakeObject<TextFragment>(
        "transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text ");
    // Create color object from Alpha channel
    alpha = 30;
    alphaColor = Color::FromArgb(alpha, red, green, blue);
    // Set color information for text instance
    text->get_TextState()->set_ForegroundColor(alphaColor);
    // Add text to paragraphs collection of page instance
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

## تحديد تباعد الأسطر للخطوط

فئة [Aspose.Pdf.Text.TextFormattingOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options) تحتوي على تعداد [LineSpacingMode](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options#a240276fd8a270b7c134d3355c5fb1c91) والذي تم تصميمه للخطوط المحددة مثل الخط المدخل "HPSimplified.ttf". أيضًا فئة [Aspose.Pdf.Text.TextFormattingOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options) تحتوي على خاصية [LineSpacing](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options#a240276fd8a270b7c134d3355c5fb1c91a9e120eead36071a90367e425c96b5eaf) من نوع LineSpacingMode. تحتاج فقط إلى تعيين LineSpacing إلى LineSpacingMode.FullSize. سيكون جزء الشيفرة لعرض الخط بشكل صحيح كما يلي:

```cpp
void SpecifyLineSpacingForFonts() {

    String _dataDir("C:\\Samples\\");
    String outputFileName("SpecifyLineSpacing_out.pdf");

    String fontFile ("hp-simplified-265.ttf");

    // تحميل ملف PDF المدخل
    auto document = MakeObject<Document>();
    
    // إنشاء TextFormattingOptions مع LineSpacingMode.FullSize
    auto formattingOptions = MakeObject<TextFormattingOptions>();
    formattingOptions->set_LineSpacing(TextFormattingOptions::LineSpacingMode::FullSize);
    
    // إنشاء جزء نص مع نص عينة
    auto textFragment = MakeObject<TextFragment>("Hello world");

    // تحميل خط TrueType إلى كائن دفق
    auto fontStream = System::IO::File::OpenRead(_dataDir + fontFile);
    
    // تعيين اسم الخط لسلسلة النص
    textFragment->get_TextState()->set_Font(FontRepository::OpenFont(fontStream, FontTypes::TTF));
    // تحديد الموضع لجزء النص
    textFragment->set_Position(MakeObject<Position>(100, 600));
    // تعيين TextFormattingOptions للجزء الحالي إلى المحدد مسبقًا (الذي يشير إلى
    // LineSpacingMode.FullSize)
    textFragment->get_TextState()->set_FormattingOptions(formattingOptions);
    
    // إضافة النص إلى TextBuilder بحيث يمكن وضعه فوق ملف PDF    
    auto page = document->get_Pages()->Add();
    page->get_Paragraphs()->Add(textFragment);

    // حفظ مستند PDF الناتج
    document->Save(_dataDir + outputFileName);
}
```

## الحصول على عرض النص ديناميكيًا

فئة [Aspose.Pdf.Text.TextState](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_state) توضح كيفية الحصول على عرض النص ديناميكيًا في مستند PDF.

أحيانًا، يكون من الضروري الحصول على عرض النص ديناميكيًا. يتضمن Aspose.PDF لـ C++ طريقتين لقياس عرض السلسلة النصية. يمكنك استدعاء طريقة [MeasureString](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_state#a084c1781028cd3483c82b4fd4cec4967) من فئات Aspose.Pdf.Text.Font أو Aspose.Pdf.Text.TextState (أو كليهما). يُظهر الشيفرة البرمجية أدناه كيفية استخدام هذه الوظيفة.

```cpp
void GetTextWidthDynamicaly() {
    auto font = FontRepository::FindFont(u"Arial");
    auto ts = MakeObject<TextState>();

    ts->set_Font(font);
    ts->set_FontSize(14);

    if (Math::Abs(font->MeasureString(u"A", 14) - 9.337) > 0.001)
        Console::WriteLine(u"قياس سلسلة الخط غير متوقع!");

    if (Math::Abs(ts->MeasureString(u"z") - 7.0) > 0.001)
        Console::WriteLine(u"قياس سلسلة الخط غير متوقع!");

    for (char c = 'A'; c <= 'z'; c++) {
        String v(c);
        double fnMeasure = font->MeasureString(v, 14);
        double tsMeasure = ts->MeasureString(v);

        if (Math::Abs(fnMeasure - tsMeasure) > 0.001)
            Console::WriteLine(u"قياس سلسلة الخط والحالة لا يتطابقان!");
    }
}
```