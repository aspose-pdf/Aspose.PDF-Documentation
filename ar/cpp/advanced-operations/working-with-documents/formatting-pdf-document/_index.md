---
title: تنسيق مستند PDF باستخدام C++
linktitle: تنسيق مستند PDF
type: docs
weight: 20
url: /ar/cpp/formatting-pdf-document/
description: أنشئ وقم بتنسيق مستند PDF باستخدام Aspose.PDF لـ C++. استخدم مقتطف الشيفرة التالي لحل مهامك.
lastmod: "2021-11-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## تنسيق مستند PDF

### الحصول على خصائص نافذة المستند وعرض الصفحة

يساعدك هذا الموضوع في فهم كيفية الحصول على خصائص نافذة المستند، وتطبيق المشاهد، وكيفية عرض الصفحات. لتعيين هذه الخصائص، افتح ملف PDF باستخدام فئة [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). يمكنك الآن تعيين خصائص كائن المستند، مثل:

- CenterWindow – مركز نافذة المستند على الشاشة. الافتراضي: خطأ.
- Direction – ترتيب القراءة. يحدد هذا كيفية ترتيب الصفحات عند عرضها جنبًا إلى جنب. الافتراضي: من اليسار إلى اليمين.
- DisplayDocTitle – عرض عنوان المستند في شريط عنوان نافذة المستند. 
- Default: false (يتم عرض العنوان).
- HideMenuBar – إخفاء أو عرض شريط قائمة نافذة المستند. Default: false (يتم عرض شريط القوائم).
- HideToolBar – إخفاء أو عرض شريط أدوات نافذة المستند. Default: false (يتم عرض شريط الأدوات).
- HideWindowUI – إخفاء أو عرض عناصر واجهة مستخدم نافذة المستند مثل أشرطة التمرير. Default: false (يتم عرض عناصر واجهة المستخدم).
- NonFullScreenPageMode – كيفية عرض المستند عند عدم عرضه في وضع الصفحة الكاملة.
- PageLayout – تخطيط الصفحة.
- PageMode – كيفية عرض المستند عند فتحه لأول مرة. الخيارات هي عرض الصور المصغرة، الشاشة الكاملة، عرض لوحة المرفقات.

يوضح لك مقطع الشيفرة التالي كيفية الحصول على الخصائص باستخدام فئة [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).

```cpp
void GetDocumentWindowAndPageDisplayProperties()
{
    // سلسلة لاسم المسار.
    String _dataDir("C:\\Samples\\");
    // سلسلة لاسم الملف.
    String inputFileName("sample.pdf");

    auto document = MakeObject<Document>(inputFileName);

    // الحصول على خصائص المستند المختلفة
    // موضع نافذة المستند - Default: false
    Console::WriteLine(u"CenterWindow : {0}", document->get_CenterWindow());

    // ترتيب القراءة الأساسي؛ يحدد موضع الصفحة
    // عند العرض جنبًا إلى جنب - Default: L2R
    Console::WriteLine(u"Direction : {0}", document->get_Direction());

    // ما إذا كان شريط عنوان النافذة يجب أن يعرض عنوان المستند
    // إذا كان false، يعرض شريط العنوان اسم ملف PDF - Default: false
    Console::WriteLine(u"DisplayDocTitle : {0}", document->get_DisplayDocTitle());

    // ما إذا كان سيتم تغيير حجم نافذة المستند لتناسب حجم
    // الصفحة المعروضة أولاً - Default: false
    Console::WriteLine(u"FitWindow : {0}", document->get_FitWindow());

    // ما إذا كان سيتم إخفاء شريط القوائم لتطبيق العارض - Default: false
    Console::WriteLine(u"HideMenuBar : {0}", document->get_HideMenubar());

    // ما إذا كان سيتم إخفاء شريط الأدوات لتطبيق العارض - Default: false
    Console::WriteLine(u"HideToolBar : {0}", document->get_HideToolBar());

    // ما إذا كان سيتم إخفاء عناصر واجهة المستخدم مثل أشرطة التمرير
    // وترك محتويات الصفحة فقط معروضة - Default: false
    Console::WriteLine(u"HideWindowUI : {0}", document->get_HideWindowUI());

    // وضع صفحة المستند. كيفية عرض المستند عند الخروج من وضع الشاشة الكاملة.
    Console::WriteLine(u"NonFullScreenPageMode : {0}", document->get_NonFullScreenPageMode());

    // تخطيط الصفحة أي صفحة واحدة، عمود واحد
    Console::WriteLine(u"PageLayout : {0}", document->get_PageLayout());

    // كيفية عرض المستند عند فتحه
    // أي عرض الصور المصغرة، الشاشة الكاملة، عرض لوحة المرفقات
    Console::WriteLine(u"pageMode : {0}", document->get_PageMode());
}
```
```
### ضبط خصائص نافذة المستند وعرض الصفحة

يشرح هذا الموضوع كيفية ضبط خصائص نافذة المستند، وتطبيق العارض، وعرض الصفحة. لضبط هذه الخصائص المختلفة:

1. افتح ملف PDF باستخدام فئة [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. اضبط خصائص المستند المختلفة:

- CenterWindow
- Direction
- DisplayDocTitle
- FitWindow
- HideMenuBar
- HideToolBar
- HideWindowUI
- NonFullScreenPageMode
- PageLayout
- PageMode

1. [احفظ](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/#ac082fe8e67b25685fc51d33e804269fa) ملف PDF المحدث باستخدام طريقة الحفظ.

الخصائص المتاحة هي:

- CenterWindow
- Direction
- DisplayDocTitle
- FitWindow
- HideMenuBar
- HideToolBar
- HideWindowUI
- NonFullScreenPageMode
- PageLayout
- PageMode

يتم استخدام كل منها ووصفها في الكود أدناه. النص التالي - يوضح لك كيفية تعيين الخصائص باستخدام فئة [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).

```cpp
void SetDocumentWindowAndPageDisplayProperties()
{
    // سلسلة لمسار الاسم.
    String _dataDir("C:\\Samples\\");
    // سلسلة لاسم الملف.
    String inputFileName("sample.pdf");
    String outputFileName("sample_page_display_properties.pdf");

    auto document = MakeObject<Document>(inputFileName);

    // تعيين خصائص مختلفة للمستند
    // تحديد موضع نافذة المستند - الافتراضي: false
    document->set_CenterWindow(true);

    // اتجاه القراءة السائد؛ يحدد موضع الصفحة
    // عند العرض جنبًا إلى جنب - الافتراضي: L2R
    document->set_Direction(Direction::R2L);

    // تحديد ما إذا كان شريط عنوان النافذة يجب أن يعرض عنوان المستند
    // إذا كان false، يعرض شريط العنوان اسم ملف PDF - الافتراضي: false
    document->set_DisplayDocTitle(true);

    // تحديد ما إذا كان يجب تغيير حجم نافذة المستند لتناسب حجم
    // أول صفحة معروضة - الافتراضي: false
    document->set_FitWindow(true);

    // تحديد ما إذا كان يجب إخفاء شريط القوائم لتطبيق العارض - الافتراضي: false
    document->set_HideMenubar(true);

    // تحديد ما إذا كان يجب إخفاء شريط الأدوات لتطبيق العارض - الافتراضي: false
    document->set_HideToolBar(true);

    // تحديد ما إذا كان يجب إخفاء عناصر واجهة المستخدم مثل أشرطة التمرير
    // وترك محتويات الصفحة فقط معروضة - الافتراضي: false
    document->set_HideWindowUI(true);

    // وضع الصفحة للمستند. تحديد كيفية عرض المستند عند الخروج من وضع الشاشة الكاملة.
    document->set_NonFullScreenPageMode(PageMode::UseOC);

    // تحديد تخطيط الصفحة أي صفحة واحدة، عمود واحد
    document->set_PageLayout(PageLayout::TwoColumnLeft);

    // تحديد كيفية عرض المستند عند فتحه
    // أي عرض الصور المصغرة، وضع الشاشة الكاملة، عرض لوحة المرفقات
    document->set_PageMode(PageMode::UseThumbs);

    // حفظ ملف PDF المحدث
    document->Save(_dataDir + outputFileName);
}
```
### تضمين الخطوط في ملف PDF موجود

تدعم قارئات PDF [مجموعة من 14 خطًا](https://en.wikipedia.org/wiki/PDF#Text) حتى يمكن عرض المستندات بالطريقة نفسها بغض النظر عن النظام الأساسي الذي يُعرض عليه المستند. عندما يحتوي ملف PDF على خط ليس من بين 14 خطًا أساسيًا، قم بتضمين الخط في ملف PDF لتجنب استبدال الخط.

يدعم Aspose.PDF لـ C++ تضمين الخطوط في ملفات PDF الموجودة. يمكنك تضمين خط كامل أو جزء من الخط. لتضمين الخط، افتح ملف PDF باستخدام فئة [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). ثم استخدم فئة [Aspose.Pdf.Text.Font](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.font) لتضمين الخط في ملف PDF. لتضمين الخط بالكامل، استخدم خاصية IsEmbeded لفئة Font؛ لاستخدام جزء من الخط، استخدم خاصية IsSubset.

{{% alert color="primary" %}}

يضم جزء من الخط فقط الأحرف التي يتم استخدامها وهو مفيد حيث تُستخدم الخطوط لجمل قصيرة أو شعارات، على سبيل المثال حيث يُستخدم خط الشركة لشعار، ولكن ليس للنص الأساسي. باستخدام مجموعة فرعية يتم تقليل حجم ملف PDF الناتج. ومع ذلك، إذا تم استخدام خط مخصص للنص الأساسي، قم بتضمينه بالكامل.

{{% /alert %}}

يوضح مقتطف الشيفرة التالي كيفية تضمين خط في ملف PDF.

### تضمين الخطوط القياسية من النوع 1

هناك مستندات PDF تستخدم خطوطًا من مجموعة خاصة تسمى "الخطوط القياسية من النوع 1". تتضمن هذه المجموعة 14 خطًا وتضمين هذا النوع من الخطوط يتطلب استخدام علامات خاصة مثل [Aspose.Pdf.Document.EmbedStandardFonts](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a8f1a88eef22e05ee9ee22a79db9cb9f6).

فيما يلي مقتطف الشيفرة الذي يمكن استخدامه للحصول على مستند يتضمن جميع الخطوط بما في ذلك الخطوط القياسية من النوع 1:

```cpp
void EmbeddingStandardType1Fonts()
{

    // String for path name.
    String _dataDir("C:\\Samples\\");
    // String for file name.
    String inputFileName("sample.pdf");
    String outputFileName("embedded-fonts-updated_out.pdf");

    auto document = MakeObject<Document>(inputFileName);

    // Set EmbedStandardFonts property of document
    document->set_EmbedStandardFonts(true);
    for (auto page : document->get_Pages())
    {
        auto fonts = page->get_Resources()->get_Fonts();
        if (fonts != nullptr)
        {
            for (auto pageFont : fonts)
            {
                // Check if font is already embedded
                if (!pageFont->get_IsEmbedded())
                {
                    pageFont->set_IsEmbedded(true);
                }
            }
        }
    }
    document->Save(_dataDir + outputFileName);
}
```
### تضمين الخطوط أثناء إنشاء PDF

إذا كنت بحاجة إلى استخدام أي خط آخر غير الخطوط الأساسية الـ 14 المدعومة من Adobe Reader، فيجب عليك تضمين وصف الخط أثناء إنشاء ملف Pdf. إذا لم يتم تضمين معلومات الخط، سيقوم Adobe Reader بأخذها من نظام التشغيل إذا كان مثبتًا على النظام، أو سيقوم بإنشاء خط بديل وفقًا لوصف الخط في Pdf.

>يرجى ملاحظة أن الخط المضمن يجب أن يكون مثبتًا على الجهاز المضيف أي في حالة الكود التالي يجب أن يكون خط 'Univers Condensed' مثبتًا على النظام.

نستخدم خاصية IsEmbedded لفئة Font لتضمين معلومات الخط في ملف Pdf. تعيين قيمة هذه الخاصية إلى ‘True’ سيقوم بتضمين ملف الخط الكامل في Pdf، مع العلم أن ذلك سيزيد من حجم ملف Pdf. فيما يلي مقتطف الكود الذي يمكن استخدامه لتضمين معلومات الخط في Pdf.

```cpp
void EmbeddingFontsWhileCreatingPDF()
{
    // String for path name.
    String _dataDir("C:\\Samples\\");
    // String for file name.
    String inputFileName("sample.pdf");
    String outputFileName("EmbedFontWhileDocCreation_out.pdf");

    auto document = MakeObject<Document>(inputFileName);

    // Create a section in the Pdf object
    auto page = document->get_Pages()->Add();

    auto fragment = MakeObject<TextFragment>("");
    auto segment = MakeObject <TextSegment>(u"This is a sample text using Custom font.");

    auto ts = MakeObject<TextState>();

    ts->set_Font(FontRepository::FindFont(u"Arial"));
    ts->get_Font()->set_IsEmbedded(true);
    segment->set_TextState(ts);
    fragment->get_Segments()->Add(segment);
    page->get_Paragraphs()->Add(fragment);

    // Save PDF Document
    document->Save(_dataDir);
}
```

### تعيين اسم الخط الافتراضي عند حفظ PDF

عندما يحتوي مستند PDF على خطوط غير متوفرة في المستند نفسه وعلى الجهاز، تقوم API باستبدال هذه الخطوط بالخط الافتراضي. عندما يكون الخط متاحًا (مثبتًا على الجهاز أو مضمنًا في المستند)، يجب أن يحتوي ملف PDF الناتج على نفس الخط (لا يجب استبداله بالخط الافتراضي). يجب أن تحتوي قيمة الخط الافتراضي على اسم الخط (وليس مسار ملفات الخط). قامت Apose.PDF for C++ بتطبيق ميزة لتعيين اسم الخط الافتراضي أثناء حفظ المستند كملف PDF. يمكن استخدام جزء الكود التالي لتعيين الخط الافتراضي:

```cpp
void SetDefaultFontNameWhileSavingPDF()
{
    // String for path name.
    String _dataDir("C:\\Samples\\");
    // String for file name.
    String inputFileName("sample.pdf");
    String outputFileName("output_out.pdf");
    String newName("Arial");

    auto document = MakeObject<Document>(inputFileName);

    auto pdfSaveOptions = MakeObject<PdfSaveOptions>();

    // Specify Default Font Name
    pdfSaveOptions->set_DefaultFontName(newName);
    document->Save(_dataDir + outputFileName, pdfSaveOptions);
}
```

### الحصول على جميع الخطوط من مستند PDF

في حال كنت ترغب في الحصول على جميع الخطوط من مستند PDF، يمكنك استخدام [FontUtilities](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a2e22a508e8baef176dfc34734cf0def9).GetAllFonts() الطريقة المقدمة في فئة [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).

يرجى التحقق من مقتطف الشيفرة التالي للحصول على جميع الخطوط من مستند PDF موجود:

```cpp
void GetAllFontsFromPDFdocument()
{
    // سلسلة لاسم المسار.
    String _dataDir("C:\\Samples\\");
    // سلسلة لاسم الملف.
    String inputFileName("sample.pdf");
    String outputFileName("output_out.pdf");
    String newName("Arial");

    auto document = MakeObject<Document>(inputFileName);
    auto fonts = document->get_FontUtilities()->GetAllFonts();
    for (auto font : fonts)
    {
        std::cerr << font->get_FontName() << std::endl;
    }
}
```

### الحصول على تحذيرات لاستبدال الخط

يوفر Aspose.PDF لـ C++ طرقًا للحصول على إشعارات حول استبدال الخط للتعامل مع حالات استبدال الخطوط. الجزء المقتبس من الشيفرة أدناه يوضح كيفية استخدام الوظيفة المقابلة.

```cpp
void GetWarningsForFontSubstitution()
{
    // سلسلة لاسم المسار.
    String _dataDir("C:\\Samples\\");

    // سلسلة لاسم الملف.
    String inputFileName("sample.pdf");
    String outputFileName("output_out.pdf");

    auto document = MakeObject<Document>(inputFileName);

    document->FontSubstitution = Aspose::Pdf::Document::FontSubstitutionHandler(OnFontSubstitution);
}
```

طريقة [OnFontSubstitution](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac776d8736d430532bdaa530a36eb51a0) مذكورة أدناه.

```cpp
void OnFontSubstitution(Aspose::Pdf::Text::Font &font, Aspose::Pdf::Text::Font& newFont) {
    std::cout << "تحذير: الخط " << font.get_FontName() 
            << " تم استبداله بخط آخر -> " 
            << newFont.get_FontName() << std::endl;
}
```

### تحسين تضمين الخطوط باستخدام FontSubsetStrategy

يمكن تحقيق ميزة تضمين الخطوط كجزء فرعي باستخدام خاصية IsSubset، ولكن أحيانًا ترغب في تقليل مجموعة الخطوط المدمجة بالكامل إلى الأجزاء الفرعية التي تُستخدم في المستند فقط. [Aspose.Pdf.Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) يحتوي على خاصية [FontUtilities](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document.i_document_font_utilities/) والتي تتضمن الطريقة SubsetFonts(FontSubsetStrategy subsetStrategy). في الطريقة SubsetFonts()، يساعد المعامل subsetStrategy على ضبط استراتيجية الجزئية. يدعم FontSubsetStrategy نوعين من جزئية الخطوط.

- SubsetAllFonts - سيقوم هذا بتجزئة جميع الخطوط المستخدمة في المستند.
- SubsetEmbeddedFontsOnly - سيقوم هذا بتجزئة فقط تلك الخطوط التي تم تضمينها بالكامل في المستند.

يوضح مقتطف الشفرة التالي كيفية تعيين FontSubsetStrategy:

```cpp
void ImproveFontsEmbeddingUsingFontSubsetStrategy()
{
    // سلسلة لمسار الاسم.
    String _dataDir("C:\\Samples\\");

    // سلسلة لاسم الملف.
    String inputFileName("sample.pdf");
    // سلسلة لاسم الملف.
    String outputFileName("sample_out.pdf");

    auto document = MakeObject<Document>(inputFileName);
    // سيتم تضمين جميع الخطوط كجزء في المستند في حالة SubsetAllFonts.
    document->get_FontUtilities()->SubsetFonts(FontSubsetStrategy::SubsetAllFonts);
    // سيتم تضمين جزئية الخطوط للخطوط المضمنة بالكامل ولكن الخطوط التي لم يتم تضمينها في المستند لن تتأثر.
    document->get_FontUtilities()->SubsetFonts(FontSubsetStrategy::SubsetEmbeddedFontsOnly);
    document->Save(_dataDir + outputFileName);
}
```
### الحصول على وتعيين عامل تكبير ملف PDF

في بعض الأحيان، ترغب في تعيين عامل التكبير لوثيقة PDF. باستخدام Aspose.PDF for C++، يمكنك تعيين قيمة عامل التكبير باستخدام [دالة set_OpenAction(…)](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#abb5c84979077034d06a673409b666e21) من فئة Document.

خاصية Destination في فئة [GoToAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.go_to_action/) تتيح لك الحصول على قيمة التكبير المرتبطة بملف PDF. وبالمثل، يمكن استخدامها لتعيين عامل التكبير لملف.

#### تعيين عامل التكبير

يوضح مقطع الشيفرة التالي كيفية تعيين عامل التكبير لملف PDF.

```cpp
void SetZoomFactor() {
    // String for path name.
    String _dataDir("C:\\Samples\\");

    // String for file name.
    String inputFileName("sample.pdf");
    // String for file name.
    String outputFileName("Zoomed_pdf_out.pdf");

    auto document = MakeObject<Document>(inputFileName);
    auto action = MakeObject<Aspose::Pdf::Annotations::GoToAction>(MakeObject<Aspose::Pdf::Annotations::XYZExplicitDestination>(1, 0, 0, .5));

    document->set_OpenAction(action);
    // Save the document
    document->Save(_dataDir + outputFileName);
}
```

#### الحصول على عامل التكبير

احصل على عامل التكبير في ملف PDF الخاص بك باستخدام Aspose.PDF لـ C++.

يُظهر مقتطف الشيفرة التالي كيفية الحصول على عامل التكبير لملف PDF:

```cpp
void GetZoomFactor() 
{
    // سلسلة لاسم المسار.
    String _dataDir("C:\\Samples\\");

    // سلسلة لاسم الملف.
    String inputFileName("sample.pdf");

    auto document = MakeObject<Document>(inputFileName);

    // إنشاء كائن GoToAction
    auto action = System::DynamicCast<Aspose::Pdf::Annotations::GoToAction>(document->get_OpenAction());

    // الحصول على عامل التكبير لملف PDF
    auto zoom = System::DynamicCast<Aspose::Pdf::Annotations::XYZExplicitDestination>(action->get_Destination());
    Console::WriteLine(zoom->get_Zoom()); // قيمة تكبير المستند;
}
```

### إعداد خصائص عرض مربع حوار الطباعة

يسمح Aspose.PDF لـ C++ بإعداد خصائص عرض مربع حوار الطباعة لوثيقة PDF. إنه يسمح لك بتغيير خاصية DuplexMode لوثيقة PDF التي تكون مضبوطة على البسيطة افتراضياً. يمكن تحقيق ذلك باستخدام منهجيتين مختلفتين كما هو موضح أدناه.

```cpp
void SettingPrintDialogPresetProperties()
{
    // سلسلة لمسار الاسم.
    String _dataDir("C:\\Samples\\");
    // سلسلة لاسم الملف.
    String outputFileName("SettingPrintDialogPresetProperties.pdf");

    auto document = MakeObject<Document>();
    document->get_Pages()->Add();
    document->set_Duplex(PrintDuplex::DuplexFlipLongEdge);
    document->Save(_dataDir + outputFileName);
}
```

### ضبط خصائص مربع حوار الطباعة باستخدام محرر محتوى PDF

```cpp
void SettingPrintDialogPresetPropertiesUsingContentEditor() {
    // سلسلة لمسار الاسم.
    String _dataDir("C:\\Samples\\");

    // سلسلة لاسم الملف.
    String inputFileName("sample.pdf");
    String outputFileName("SetPrintDlgPropertiesUsingPdfContentEditor_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto contentEditor = MakeObject<Aspose::Pdf::Facades::PdfContentEditor>();

    contentEditor->BindPdf(outputFileName);
    if ((contentEditor->GetViewerPreference() & Aspose::Pdf::Facades::ViewerPreference::DuplexFlipShortEdge) > 0)
    {
    std::cout << "The file has duplex flip short edge" << std::endl;
    }

    contentEditor->ChangeViewerPreference(Aspose::Pdf::Facades::ViewerPreference::DuplexFlipShortEdge);
    contentEditor->Save(_dataDir + outputFileName);
}
```