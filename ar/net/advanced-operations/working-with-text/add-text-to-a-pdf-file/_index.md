---
title: إضافة نص إلى PDF باستخدام C#
linktitle: إضافة نص إلى PDF
type: docs
weight: 10
url: ar/net/add-text-to-pdf-file/
description: يصف هذا المقال الجوانب المختلفة للعمل مع النص في Aspose.PDF. تعلم كيفية إضافة نص إلى PDF، إضافة أجزاء HTML، أو استخدام خطوط OTF المخصصة.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /net/add-text-to-a-pdf-file/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "إضافة نص إلى PDF باستخدام C#",
    "alternativeHeadline": "كيفية إضافة نص إلى PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد وثيقة PDF",
    "keywords": "pdf, c#, إضافة نص إلى pdf",
    "wordcount": "302",
    "proficiencyLevel":"مبتدئ",
    "publisher": {
        "@type": "Organization",
        "name": "فريق وثائق Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/add-text-to-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-text-to-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "يصف هذا المقال الجوانب المختلفة للعمل مع النص في Aspose.PDF. تعلم كيفية إضافة نص إلى PDF، إضافة أجزاء HTML، أو استخدام خطوط OTF المخصصة."
}
</script>
يعمل الجزء التالي من الشفرة أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

لإضافة نص إلى ملف PDF موجود:

1. افتح ملف PDF المدخل باستخدام كائن الوثيقة.
2. احصل على الصفحة المعينة التي ترغب في إضافة النص إليها.
3. قم بإنشاء كائن TextFragment بالنص المدخل مع خصائص نص أخرى. يتيح لك كائن TextBuilder المُنشأ من تلك الصفحة المعينة – التي تريد إضافة النص إليها – إضافة كائن TextFragment إلى الصفحة باستخدام طريقة AppendText.
4. استدعي طريقة الحفظ Save لكائن الوثيقة واحفظ ملف PDF الناتج.

## إضافة نص

يوضح الجزء التالي من الشفرة كيفية إضافة نص في ملف PDF موجود.

```csharp
// للأمثلة الكاملة وملفات البيانات، يُرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// فتح المستند
Document pdfDocument = new Document(dataDir + "input.pdf");

// الحصول على الصفحة المحددة
Page pdfPage = (Page)pdfDocument.Pages[1];

// إنشاء قطعة نصية
TextFragment textFragment = new TextFragment("main text");
textFragment.Position = new Position(100, 600);

// تعيين خصائص النص
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray);
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Red);

// إنشاء كائن TextBuilder
TextBuilder textBuilder = new TextBuilder(pdfPage);

// إلحاق قطعة النص بصفحة PDF
textBuilder.AppendText(textFragment);

dataDir = dataDir + "AddText_out.pdf";

// حفظ مستند PDF الناتج.
pdfDocument.Save(dataDir);
```
## تحميل الخط من تدفق

الشفرة التالية توضح كيفية تحميل خط من كائن تدفق عند إضافة نص إلى مستند PDF.

```csharp
// للحصول على الأمثلة الكاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار إلى مجلد الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
string fontFile = "";

// تحميل ملف PDF الإدخال
Document doc = new Document(dataDir + "input.pdf");
// إنشاء كائن بناء نص للصفحة الأولى من المستند
TextBuilder textBuilder = new TextBuilder(doc.Pages[1]);
// إنشاء قطعة نصية بسلسلة عينة
TextFragment textFragment = new TextFragment("Hello world");

if (fontFile != "")
{
    // تحميل الخط TrueType إلى كائن تدفق
    using (FileStream fontStream = File.OpenRead(fontFile))
    {
        // تعيين اسم الخط لسلسلة النص
        textFragment.TextState.Font = FontRepository.OpenFont(fontStream, FontTypes.TTF);
        // تحديد الموقع لقطعة النص
        textFragment.Position = new Position(10, 10);
        // إضافة النص إلى TextBuilder حتى يمكن وضعه على ملف PDF
        textBuilder.AppendText(textFragment);
    }

    dataDir = dataDir + "LoadingFontFromStream_out.pdf";

    // حفظ مستند PDF الناتج.
    doc.Save(dataDir);
}
```
## إضافة نص باستخدام TextParagraph

يظهر مقطع الكود التالي طريقة إضافة نص في مستند PDF باستخدام فئة [TextParagraph](https://reference.aspose.com/pdf/net/aspose.pdf.text/textparagraph).

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// فتح المستند
Document doc = new Document();
// إضافة صفحة إلى مجموعة صفحات كائن المستند
Page page = doc.Pages.Add();
TextBuilder builder = new TextBuilder(page);
// إنشاء فقرة نصية
TextParagraph paragraph = new TextParagraph();
// تحديد المسافة البادئة للسطور اللاحقة
paragraph.SubsequentLinesIndent = 20;
// تحديد الموقع لإضافة TextParagraph
paragraph.Rectangle = new Aspose.Pdf.Rectangle(100, 300, 200, 700);
// تحديد وضع تغليف الكلمات
paragraph.FormattingOptions.WrapMode = TextFormattingOptions.WordWrapMode.ByWords;
// إنشاء قطعة نصية
TextFragment fragment1 = new TextFragment("the quick brown fox jumps over the lazy dog");
fragment1.TextState.Font = FontRepository.FindFont("Times New Roman");
fragment1.TextState.FontSize = 12;
// إضافة القطعة إلى الفقرة
paragraph.AppendLine(fragment1);
// إضافة الفقرة
builder.AppendParagraph(paragraph);

dataDir = dataDir + "AddTextUsingTextParagraph_out.pdf";

// حفظ المستند PDF الناتج.
doc.Save(dataDir);
```
## إضافة رابط تشعبي إلى جزء النص

قد تتكون صفحة PDF من واحد أو أكثر من كائنات TextFragment، حيث يمكن لكل كائن TextFragment أن يحتوي على واحد أو أكثر من الحالات TextSegment. من أجل تعيين رابط تشعبي لـ TextSegment، يمكن استخدام خاصية Hyperlink لفئة [TextSegment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textsegment) أثناء توفير كائن من نوع Aspose.Pdf.WebHyperlink. يرجى استخدام مقتطف الكود التالي لتحقيق هذا الشرط.

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// إنشاء مثيل المستند
Document doc = new Document();
// إضافة صفحة إلى مجموعة صفحات ملف PDF
Page page1 = doc.Pages.Add();
// إنشاء مثيل TextFragment
TextFragment tf = new TextFragment("نص تجريبي للجزء");
// تعيين المحاذاة الأفقية لـ TextFragment
tf.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
// إنشاء textsegment بنص تجريبي
TextSegment segment = new TextSegment(" ... الجزء الأول من النص...");
// إضافة segment إلى مجموعة segments لـ TextFragment
tf.Segments.Add(segment);
// إنشاء TextSegment جديد
segment = new TextSegment("رابط إلى Google");
// إضافة segment إلى مجموعة segments لـ TextFragment
tf.Segments.Add(segment);
// تعيين رابط تشعبي لـ TextSegment
segment.Hyperlink = new Aspose.Pdf.WebHyperlink("www.google.com");
// تعيين لون الخط الأمامي لجزء النص
segment.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
// تعيين تنسيق النص كمائل
segment.TextState.FontStyle = FontStyles.Italic;
// إنشاء كائن TextSegment آخر
segment = new TextSegment("TextSegment بدون رابط تشعبي");
// إضافة segment إلى مجموعة segments لـ TextFragment
tf.Segments.Add(segment);
// إضافة TextFragment إلى مجموعة فقرات الصفحة
page1.Paragraphs.Add(tf);

dataDir = dataDir + "AddHyperlinkToTextSegment_out.pdf";

// حفظ المستند PDF الناتج.
doc.Save(dataDir);
```
## استخدام خط OTF

يوفر Aspose.PDF لـ .NET الميزة لاستخدام الخطوط المخصصة/TrueType أثناء إنشاء/معالجة محتويات ملف PDF بحيث يتم عرض محتويات الملف باستخدام محتويات غير الخطوط الافتراضية للنظام. بدءًا من إصدار Aspose.PDF لـ .NET 10.3.0، قدمنا الدعم لخطوط Open Type.

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// إنشاء نموذج جديد للوثيقة
Document pdfDocument = new Document();
// إضافة صفحة إلى مجموعة الصفحات لملف PDF
Aspose.Pdf.Page page = pdfDocument.Pages.Add();
// إنشاء نموذج TextFragment مع نص عينة
TextFragment fragment = new TextFragment("Sample Text in OTF font");
// البحث عن الخط داخل دليل خط النظام
// Fragment.TextState.Font = FontRepository.FindFont("HelveticaNeueLT Pro 45 Lt");
// أو يمكنك حتى تحديد مسار الخط OTF في دليل النظام
fragment.TextState.Font = FontRepository.OpenFont(dataDir + "space age.otf");
// تحديد لتضمين الخط داخل ملف PDF، بحيث يتم عرضه بشكل صحيح،
// حتى لو لم يكن الخط المحدد مثبتًا/موجودًا على جهاز الهدف
fragment.TextState.Font.IsEmbedded = true;
// إضافة TextFragment إلى مجموعة الفقرات لنموذج الصفحة
page.Paragraphs.Add(fragment);

dataDir = dataDir + "OTFFont_out.pdf";

// حفظ مستند PDF الناتج.
pdfDocument.Save(dataDir);
```
## إضافة سلسلة HTML باستخدام DOM

فئة Aspose.Pdf.Generator.Text تحتوي على خاصية تُسمى IsHtmlTagSupported والتي تتيح إمكانية إضافة علامات/محتويات HTML إلى ملفات PDF. يتم تقديم المحتوى المضاف في علامات HTML الأصلية بدلاً من ظهوره كسلسلة نصية بسيطة. لدعم ميزة مماثلة في نموذج كائن المستند الجديد (DOM) لمساحة الاسم Aspose.Pdf، تم تقديم فئة HtmlFragment.

يمكن استخدام مثيل [HtmlFragment](https://reference.aspose.com/pdf/net/aspose.pdf/htmlfragment) لتحديد المحتويات HTML التي يجب وضعها داخل ملف PDF. مشابهًا لـ TextFragment، يعتبر HtmlFragment كائنًا على مستوى الفقرة ويمكن إضافته إلى مجموعة فقرات كائن الصفحة. تظهر الأجزاء التالية من الكود الخطوات لوضع محتويات HTML داخل ملف PDF باستخدام نهج DOM.

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// إنشاء كائن Document
Document doc = new Document();
// إضافة صفحة إلى مجموعة الصفحات لملف PDF
Page page = doc.Pages.Add();
// إنشاء HtmlFragment بمحتويات HTML
HtmlFragment title = new HtmlFragment("<fontsize=10><b><i>Table</i></b></fontsize>");
// تعيين معلومات الهامش السفلي
title.Margin.Bottom = 10;
// تعيين معلومات الهامش العلوي
title.Margin.Top = 200;
// إضافة HtmlFragment إلى مجموعة فقرات الصفحة
page.Paragraphs.Add(title);

dataDir = dataDir + "AddHTMLUsingDOM_out.pdf";
// حفظ ملف PDF
doc.Save(dataDir);
```
يوضح مقتطف الكود التالي الخطوات اللازمة لإضافة قوائم مرتبة بـ HTML إلى المستند:

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// مسار المستند الناتج.
string outFile = dataDir + "AddHTMLOrderedListIntoDocuments_out.pdf";
// توثيق كائن المستند
Document doc = new Document();
// توثيق كائن HtmlFragment مع الجزء HTML المقابل
HtmlFragment t = new HtmlFragment("`<body style='line-height: 100px;'><ul><li>First</li><li>Second</li><li>Third</li><li>Fourth</li><li>Fifth</li></ul>Text after the list.<br/>Next line<br/>Last line</body>`");
// إضافة صفحة في مجموعة الصفحات
Page page = doc.Pages.Add();
// إضافة HtmlFragment داخل الصفحة
page.Paragraphs.Add(t);
// حفظ ملف PDF الناتج
doc.Save(outFile);
```

يمكنك أيضًا ضبط تنسيق سلسلة HTML باستخدام كائن TextState على النحو التالي:

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
HtmlFragment html = new HtmlFragment("some text");
html.TextState = new TextState();
html.TextState.Font = FontRepository.FindFont("Calibri");
```
في حال قمت بتعيين قيم خصائص نصية من خلال ترميز HTML ثم قدمت نفس القيم في خصائص TextState، فإنها ستقوم بالكتابة فوق معاملات HTML بواسطة خصائص مثيل TextState. الأجزاء التالية من الكود تُظهر السلوك الموصوف.

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// إنشاء كائن Document
Document doc = new Document();
// إضافة صفحة إلى مجموعة صفحات ملف PDF
Page page = doc.Pages.Add();
// إنشاء HtmlFragment بمحتويات HTML
HtmlFragment title = new HtmlFragment("<p style='font-family: Verdana'><b><i>Table contains text</i></b></p>");
// سيتم إعادة تعيين خط 'Verdana' إلى 'Arial'
title.TextState = new TextState("Arial");
title.TextState.FontSize = 20;
// تعيين معلومات هامش الأسفل
title.Margin.Bottom = 10;
// تعيين معلومات هامش الأعلى
title.Margin.Top = 400;
// إضافة HTML Fragment إلى مجموعة فقرات الصفحة
page.Paragraphs.Add(title);
// حفظ ملف PDF
dataDir = dataDir + "AddHTMLUsingDOMAndOverwrite_out.pdf";
// حفظ ملف PDF
doc.Save(dataDir);
```
## الحواشي السفلية والحواشي الختامية (DOM)

الحواشي السفلية تشير إلى الملاحظات في نص ورقتك باستخدام أرقام متتالية علوية. الملاحظة الفعلية مُعدة ويمكن أن تظهر كحاشية سفلية في أسفل الصفحة.

### إضافة حاشية سفلية

في نظام إشارة الحواشي السفلية، يتم الإشارة إلى مرجع بـ:

- وضع رقم صغير فوق خط النوع مباشرةً بعد المادة المصدر. يُطلق على هذا الرقم معرف الملاحظة. يجلس قليلاً فوق خط النص.
- وضع نفس الرقم، يليه اقتباس من مصدرك، في أسفل الصفحة. يجب أن تكون الحواشي السفلية عددية وزمنية: المرجع الأول هو 1، الثاني هو 2، وهكذا.

ميزة الحواشي السفلية هي أن القارئ يمكنه ببساطة إلقاء نظرة إلى أسفل الصفحة لاكتشاف مصدر المرجع الذي يهمه.

يرجى اتباع الخطوات المحددة أدناه لإنشاء حاشية سفلية:

- إنشاء نموذج Document
- إنشاء كائن Page
- إنشاء كائن TextFragment
- إنشاء نموذج Note ومرر قيمته إلى خاصية TextFragment.FootNote
- إنشاء نموذج Note وتمرير قيمته إلى خاصية TextFragment.FootNote
- إضافة TextFragment إلى مجموعة الفقرات لنموذج صفحة

### نمط خط مخصص لـ FootNote

المثال التالي يوضح كيفية إضافة Footnotes إلى أسفل صفحة Pdf وتعريف نمط خط مخصص.

```csharp
// للحصول على الأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// إنشاء نموذج Document
Document doc = new Document();
// إضافة صفحة إلى مجموعة الصفحات في PDF
Page page = doc.Pages.Add();
// إنشاء نموذج GraphInfo
Aspose.Pdf.GraphInfo graph = new Aspose.Pdf.GraphInfo();
// تعيين عرض الخط إلى 2
graph.LineWidth = 2;
// تعيين لون لنموذج الرسم
graph.Color = Aspose.Pdf.Color.Red;
// تعيين قيمة مصفوفة الخطوط إلى 3
graph.DashArray = new int[] { 3 };
// تعيين قيمة مرحلة الخطوط إلى 1
graph.DashPhase = 1;
// تعيين نمط خط Footnote للصفحة كما هو موضح
page.NoteLineStyle = graph;
// إنشاء نموذج TextFragment
TextFragment text = new TextFragment("Hello World");
// تعيين قيمة FootNote لـ TextFragment
text.FootNote = new Note("foot note for test text 1");
// إضافة TextFragment إلى مجموعة الفقرات لأول صفحة من المستند
page.Paragraphs.Add(text);
// إنشاء TextFragment ثاني
text = new TextFragment("Aspose.Pdf for .NET");
// تعيين FootNote للنص الثاني
text.FootNote = new Note("foot note for test text 2");
// إضافة النص الثاني إلى مجموعة الفقرات في ملف PDF
page.Paragraphs.Add(text);

dataDir = dataDir + "CustomLineStyleForFootNote_out.pdf";

// حفظ المستند PDF الناتج.
doc.Save(dataDir);
```
يمكننا تعيين تنسيق مُعرف التعليق التوضيحي (مُعرف الهامش) باستخدام كائن TextState كما يلي:

```csharp
TextFragment text = new TextFragment("نص الاختبار 1");
text.FootNote = new Note("ملاحظة الهامش لنص الاختبار 1");
text.FootNote.Text = "21";
text.FootNote.TextState = new TextState();
text.FootNote.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
text.FootNote.TextState.FontStyle = FontStyles.Italic;
```

### تخصيص تسمية الهامش

افتراضيًا، يكون رقم الهامش تصاعديًا بدءًا من 1. ومع ذلك، قد يكون لدينا متطلب لتعيين تسمية هامش مخصصة. لتحقيق هذا المتطلب، يرجى محاولة استخدام الكود التالي

```csharp
// لأمثلة كاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// إنشاء مثال للوثيقة
Document doc = new Document();
// إضافة صفحة إلى مجموعة الصفحات في PDF
Page page = doc.Pages.Add();
// إنشاء كائن GraphInfo
Aspose.Pdf.GraphInfo graph = new Aspose.Pdf.GraphInfo();
// تعيين عرض الخط كـ 2
graph.LineWidth = 2;
// تعيين اللون لكائن الرسم
graph.Color = Aspose.Pdf.Color.Red;
// تعيين قيمة مصفوفة النقط كـ 3
graph.DashArray = new int[] { 3 };
// تعيين قيمة طور النقط كـ 1
graph.DashPhase = 1;
// تعيين نمط خط الهامش للصفحة كرسم
page.NoteLineStyle = graph;
// إنشاء مثال لـ TextFragment
TextFragment text = new TextFragment("مرحبا بالعالم");
// تعيين قيمة الهامش لـ TextFragment
text.FootNote = new Note("ملاحظة الهامش لنص الاختبار 1");
// تحديد تسمية مخصصة للهامش
text.FootNote.Text = " Aspose(2015)";
// إضافة TextFragment إلى مجموعة الفقرات للصفحة الأولى من الوثيقة
page.Paragraphs.Add(text);

dataDir = dataDir + "CustomizeFootNoteLabel_out.pdf";
```
## إضافة صورة وجدول إلى الحاشية السفلية

في الإصدارات السابقة، كان دعم الحاشية السفلية متوفرًا ولكنه كان ينطبق فقط على كائن TextFragment. ومع ذلك، ابتداءً من إصدار Aspose.PDF لـ .NET 10.7.0، يمكنك أيضًا إضافة حاشية سفلية إلى كائنات أخرى داخل مستند PDF مثل الجداول، الخلايا، وغيرها. يوضح المقتطف البرمجي التالي خطوات إضافة حاشية سفلية إلى كائن TextFragment ومن ثم إضافة كائن الصورة والجدول إلى مجموعة الفقرات في قسم الحاشية السفلية.

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Document doc = new Document();
Page page = doc.Pages.Add();
TextFragment text = new TextFragment("بعض النصوص");
page.Paragraphs.Add(text);

text.FootNote = new Note();
Aspose.Pdf.Image image = new Aspose.Pdf.Image();
image.File = dataDir + "aspose-logo.jpg";
image.FixHeight = 20;
text.FootNote.Paragraphs.Add(image);
TextFragment footNote = new TextFragment("نص الحاشية السفلية");
footNote.TextState.FontSize = 20;
footNote.IsInLineParagraph = true;
text.FootNote.Paragraphs.Add(footNote);
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
table.Rows.Add().Cells.Add().Paragraphs.Add(new TextFragment("الصف 1 الخلية 1"));
text.FootNote.Paragraphs.Add(table);

dataDir = dataDir + "AddImageAndTable_out.pdf";

// حفظ المستند PDF الناتج.
doc.Save(dataDir);
```
## كيفية إنشاء الحواشي الختامية

الحاشية الختامية هي استشهاد بمصدر يشير القراء إلى مكان محدد في نهاية الورقة حيث يمكنهم معرفة مصدر المعلومات أو الكلمات المقتبسة أو المذكورة في الورقة. عند استخدام الحواشي الختامية، يتبع الجملة المقتبسة أو المعاد صياغتها أو الملخصة رقمًا مرتفعًا.

يوضح المثال التالي كيفية إضافة حاشية ختامية في صفحة Pdf.

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// إنشاء مثيل Document
Document doc = new Document();
// إضافة صفحة إلى مجموعة صفحات PDF
Page page = doc.Pages.Add();
// إنشاء مثيل TextFragment
TextFragment text = new TextFragment("Hello World");
// تعيين قيمة FootNote لـ TextFragment
text.EndNote = new Note("sample End note");
// تحديد تسمية مخصصة لـ FootNote
text.EndNote.Text = " Aspose(2015)";
// إضافة TextFragment إلى مجموعة فقرات الصفحة الأولى من المستند
page.Paragraphs.Add(text);

dataDir = dataDir + "CreateEndNotes_out.pdf";
// حفظ المستند PDF الناتج.
doc.Save(dataDir);
```
## النص والصورة كفقرة في السطر

تخطيط الملف الافتراضي لملف PDF هو تخطيط الانسياب (من الأعلى اليسار إلى الأسفل اليمين). لذلك، يتم إضافة كل عنصر جديد إلى ملف PDF في تدفق الزاوية السفلية اليمنى. ومع ذلك، قد يكون لدينا متطلب لعرض عناصر الصفحة المختلفة مثل الصورة والنص في نفس المستوى (واحدة تلو الأخرى). يمكن أن يكون أحد الأساليب هو إنشاء مثيل جدول وإضافة كلا العنصرين إلى كائنات خلايا فردية. ومع ذلك، يمكن أن يكون نهج آخر هو فقرة InLine. من خلال تعيين خاصية IsInLineParagraph للصورة والنص على true، ستظهر هذه الفقرات كمضمنة مع عناصر الصفحة الأخرى.

يوضح الكود التالي كيفية إضافة نص وصورة كفقرات InLine في ملف PDF.

```csharp
// لأمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// توثيق مثيل جديد
Document doc = new Document();
// إضافة صفحة إلى مجموعة صفحات الوثيقة
Page page = doc.Pages.Add();
// إنشاء TextFragmnet
TextFragment text = new TextFragment("مرحبا بالعالم.. ");
// إضافة فقرة نصية إلى مجموعة فقرات الصفحة
page.Paragraphs.Add(text);
// إنشاء مثيل صورة
Aspose.Pdf.Image image = new Aspose.Pdf.Image();
// تعيين الصورة كفقرة مضمنة حتى تظهر مباشرة بعد
// الفقرة السابقة (TextFragment)
image.IsInLineParagraph = true;
// تحديد مسار ملف الصورة
image.File = dataDir + "aspose-logo.jpg";
// تعيين ارتفاع الصورة (اختياري)
image.FixHeight = 30;
// تعيين عرض الصورة (اختياري)
image.FixWidth = 100;
// إضافة الصورة إلى مجموعة فقرات الصفحة
page.Paragraphs.Add(image);
// إعادة تهيئة كائن TextFragment بمحتويات مختلفة
text = new TextFragment(" مرحبا مجددا..");
// تعيين TextFragment كفقرة مضمنة
text.IsInLineParagraph = true;
// إضافة فقرة نصية حديثة إلى مجموعة فقرات الصفحة
page.Paragraphs.Add(text);

dataDir = dataDir + "TextAndImageAsParagraph_out.pdf";
doc.Save(dataDir);
```
## تحديد تباعد الأحرف عند إضافة نص

يمكن إضافة نص داخل مجموعة الفقرات لملفات PDF باستخدام مثيل TextFragment أو باستخدام كائن TextParagraph وحتى يمكنك ختم النص داخل PDF باستخدام فئة TextStamp. عند إضافة النص، قد يكون لدينا متطلب لتحديد تباعد الأحرف لكائنات النص. من أجل تحقيق هذا المتطلب، تم تقديم خاصية جديدة تسمى خاصية CharacterSpacing. يرجى الاطلاع على النهج التالية لتلبية هذا المتطلب.

تظهر النهج التالية الخطوات لتحديد تباعد الأحرف عند إضافة نص داخل مستند PDF.

### باستخدام TextBuilder و TextFragment

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// إنشاء مثيل Document
Document pdfDocument = new Document();
// إضافة صفحة إلى مجموعة صفحات الوثيقة
Page page = pdfDocument.Pages.Add();
// إنشاء مثيل TextBuilder
TextBuilder builder = new TextBuilder(pdfDocument.Pages[1]);
// إنشاء مثيل قطعة نصية بمحتويات عينة
TextFragment wideFragment = new TextFragment("نص بتباعد أحرف متزايد");
wideFragment.TextState.ApplyChangesFrom(new TextState("Arial", 12));
// تحديد تباعد الأحرف لـ TextFragment
wideFragment.TextState.CharacterSpacing = 2.0f;
// تحديد موضع TextFragment
wideFragment.Position = new Position(100, 650);
// إلحاق TextFragment بمثيل TextBuilder
builder.AppendText(wideFragment);
dataDir = dataDir + "CharacterSpacingUsingTextBuilderAndFragment_out.pdf";
// حفظ مستند PDF الناتج.
pdfDocument.Save(dataDir);
```
### استخدام TextParagraph

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// إنشاء نموذج Document
Document pdfDocument = new Document();
// إضافة صفحة إلى مجموعة الصفحات للمستند
Page page = pdfDocument.Pages.Add();
// إنشاء نموذج TextBuilder
TextBuilder builder = new TextBuilder(pdfDocument.Pages[1]);
// توثيق نموذج TextParagraph
TextParagraph paragraph = new TextParagraph();
// إنشاء نموذج TextState لتحديد اسم الخط والحجم
TextState state = new TextState("Arial", 12);
// تحديد مسافة الأحرف
state.CharacterSpacing = 1.5f;
// إلحاق النص بكائن TextParagraph
paragraph.AppendLine("هذا فقرة مع مسافة الأحرف", state);
// تحديد الموقع لـ TextParagraph
paragraph.Position = new Position(100, 550);
// إلحاق TextParagraph بنموذج TextBuilder
builder.AppendParagraph(paragraph);

dataDir = dataDir + "CharacterSpacingUsingTextBuilderAndParagraph_out.pdf";
// حفظ المستند PDF الناتج.
pdfDocument.Save(dataDir);
```
### استخدام TextStamp

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار إلى مجلد الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// إنشاء نموذج للوثيقة
Document pdfDocument = new Document();
// أضف صفحة إلى مجموعة الصفحات في الوثيقة
Page page = pdfDocument.Pages.Add();
// توظيف نموذج TextStamp بنص عينة
TextStamp stamp = new TextStamp("هذا هو ختم النص مع تباعد الأحرف");
// حدد اسم الخط لكائن الختم
stamp.TextState.Font = FontRepository.FindFont("Arial");
// حدد حجم الخط لـ TextStamp
stamp.TextState.FontSize = 12;
// حدد تباعد الأحرف كـ 1f
stamp.TextState.CharacterSpacing = 1f;
// ضبط XIndent للختم
stamp.XIndent = 100;
// ضبط YIndent للختم
stamp.YIndent = 500;
// أضف ختم النص إلى نموذج الصفحة
stamp.Put(page);
dataDir = dataDir + "CharacterSpacingUsingTextStamp_out.pdf";
// حفظ الوثيقة PDF الناتجة.
pdfDocument.Save(dataDir);
```
## إنشاء مستند PDF متعدد الأعمدة

في المجلات والصحف، نرى غالبًا أن الأخبار تُعرض في أعمدة متعددة على صفحات فردية بدلاً من الكتب حيث يتم طباعة فقرات النص على كامل الصفحات من اليسار إلى اليمين. تسمح العديد من تطبيقات معالجة المستندات مثل مايكروسوفت وورد وأدوبي أكروبات رايتر للمستخدمين بإنشاء أعمدة متعددة على صفحة واحدة ثم إضافة البيانات إليها.

[Aspose.PDF لـ .NET](https://docs.aspose.com/pdf/net/) يقدم أيضًا الميزة لإنشاء أعمدة متعددة داخل صفحات مستندات PDF.
[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) يقدم أيضًا ميزة إنشاء عدة أعمدة داخل صفحات مستندات PDF.

المسافة بين الأعمدة تعني الفراغ بين الأعمدة والمسافة الافتراضية بين الأعمدة هي 1.25 سم. إذا لم يتم تحديد عرض العمود، فإن [Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) يحسب عرض كل عمود تلقائيًا وفقًا لحجم الصفحة ومسافة العمود.

أدناه مثال لإظهار إنشاء عمودين مع أشياء الرسوم البيانية (خط) والتي يتم إضافتها إلى مجموعة الفقرات لـ FloatingBox، والذي يتم بعد ذلك إضافته إلى مجموعة الفقرات لمثيل الصفحة.

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Document doc = new Document();
// حدد معلومات الهامش الأيسر لملف PDF
doc.PageInfo.Margin.Left = 40;
// حدد معلومات الهامش الأيمن لملف PDF
doc.PageInfo.Margin.Right = 40;
Page page = doc.Pages.Add();

Aspose.Pdf.Drawing.Graph graph1 = new Aspose.Pdf.Drawing.Graph(500, 2);
// أضف الخط إلى مجموعة الفقرات لكائن القسم
page.Paragraphs.Add(graph1);

// حدد الإحداثيات للخط
float[] posArr = new float[] { 1, 2, 500, 2 };
Aspose.Pdf.Drawing.Line l1 = new Aspose.Pdf.Drawing.Line(posArr);
graph1.Shapes.Add(l1);
// إنشاء متغيرات نصية تحتوي على نص يحتوي على علامات html

string s = "<font face=\"Times New Roman\" size=4>" +

"<strong> كيف تتجنب عمليات الاحتيال المالية</strong> "
+ "</font>";
// إنشاء فقرات نصية تحتوي على نص HTML

HtmlFragment heading_text = new HtmlFragment(s);
page.Paragraphs.Add(heading_text);

Aspose.Pdf.FloatingBox box = new Aspose.Pdf.FloatingBox();
// أضف أربعة أعمدة في القسم
box.ColumnInfo.ColumnCount = 2;
// حدد المسافة بين الأعمدة
box.ColumnInfo.ColumnSpacing = "5";

box.ColumnInfo.ColumnWidths = "105 105";
TextFragment text1 = new TextFragment("بواسطة Googler (المدونة الرسمية لجوجل)");
text1.TextState.FontSize = 8;
text1.TextState.LineSpacing = 2;
box.Paragraphs.Add(text1);
text1.TextState.FontSize = 10;

text1.TextState.FontStyle = FontStyles.Italic;
// إنشاء كائن رسوم بيانية لرسم خط
Aspose.Pdf.Drawing.Graph graph2 = new Aspose.Pdf.Drawing.Graph(50, 10);
// حدد الإحداثيات للخط
float[] posArr2 = new float[] { 1, 10, 100, 10 };
Aspose.Pdf.Drawing.Line l2 = new Aspose.Pdf.Drawing.Line(posArr2);
graph2.Shapes.Add(l2);

// أضف الخط إلى مجموعة الفقرات لكائن القسم
box.Paragraphs.Add(graph2);

TextFragment text2 = new TextFragment(@"Sed augue tortor, sodales id, luctus et, pulvinar ut, eros. Suspendisse vel dolor. Sed quam. Curabitur ut massa vitae eros euismod aliquam. Pellentesque sit amet elit. Vestibulum interdum pellentesque augue. Cras mollis arcu sit amet purus. Donec augue. Nam mollis tortor a elit. Nulla viverra nisl vel mauris. Vivamus sapien. nascetur ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et,nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. Praesent porttitor turpis eleifend ante. Morbi sodales.nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. Praesent porttitor turpis eleifend ante. Morbi sodales.");
box.Paragraphs.Add(text2);

page.Paragraphs.Add(box);

dataDir = dataDir + "CreateMultiColumnPdf_out.pdf";
// احفظ ملف PDF
doc.Save(dataDir);
```
## العمل مع توقفات الجدولة المخصصة

نقطة توقف الجدولة هي نقطة توقف للتبويب. في معالجة الكلمات، كل سطر يحتوي على عدد من نقاط توقف الجدولة الموضوعة على فترات منتظمة (على سبيل المثال، كل نصف بوصة). يمكن تغييرها، ومع ذلك، حيث يسمح معظم معالجات الكلمات بضبط نقاط توقف الجدولة حيثما تريد. عند الضغط على مفتاح الجدولة، يقفز المؤشر أو نقطة الإدراج إلى نقطة التوقف التالية، والتي بحد ذاتها غير مرئية. على الرغم من أن نقاط توقف الجدولة لا توجد في ملف النص، إلا أن معالج الكلمات يتتبعها حتى يتمكن من التفاعل بشكل صحيح مع مفتاح الجدولة.

[Aspose.PDF لـ .NET](https://docs.aspose.com/pdf/net/) يسمح للمطورين باستخدام نقاط توقف جدولة مخصصة في مستندات PDF. يتم استخدام فئة Aspose.Pdf.Text.TabStop لتعيين نقاط توقف TAB المخصصة في فئة [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment).

[Aspose.PDF لـ .NET](https://docs.aspose.com/pdf/net/) يقدم أيضًا بعض أنواع قادة الجدولة المعرفة مسبقًا كتعداد يسمى، TabLeaderType الذي تُعطى قيمه المحددة مسبقًا وأوصافها أدناه:
[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) يقدم أيضا بعض أنواع القادة المسبقة الصنع كتعداد يسمى، TabLeaderType الذي تعطى قيمه المحددة مسبقا ووصفها أدناه:

|**نوع القائد**|**الوصف**|
| :- | :- |
|None|لا يوجد قائد|
|Solid|قائد صلب|
|Dash|قائد متقطع|
|Dot|قائد نقطي|

إليك مثال على كيفية تحديد توقفات TAB المخصصة.

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Document _pdfdocument = new Document();
Page page = _pdfdocument.Pages.Add();

Aspose.Pdf.Text.TabStops ts = new Aspose.Pdf.Text.TabStops();
Aspose.Pdf.Text.TabStop ts1 = ts.Add(100);
ts1.AlignmentType = TabAlignmentType.Right;
ts1.LeaderType = TabLeaderType.Solid;
Aspose.Pdf.Text.TabStop ts2 = ts.Add(200);
ts2.AlignmentType = TabAlignmentType.Center;
ts2.LeaderType = TabLeaderType.Dash;
Aspose.Pdf.Text.TabStop ts3 = ts.Add(300);
ts3.AlignmentType = TabAlignmentType.Left;
ts3.LeaderType = TabLeaderType.Dot;

TextFragment header = new TextFragment("This is a example of forming table with TAB stops", ts);
TextFragment text0 = new TextFragment("#$TABHead1 #$TABHead2 #$TABHead3", ts);

TextFragment text1 = new TextFragment("#$TABdata11 #$TABdata12 #$TABdata13", ts);
TextFragment text2 = new TextFragment("#$TABdata21 ", ts);
text2.Segments.Add(new TextSegment("#$TAB"));
text2.Segments.Add(new TextSegment("data22 "));
text2.Segments.Add(new TextSegment("#$TAB"));
text2.Segments.Add(new TextSegment("data23"));

page.Paragraphs.Add(header);
page.Paragraphs.Add(text0);
page.Paragraphs.Add(text1);
page.Paragraphs.Add(text2);

dataDir = dataDir + "CustomTabStops_out.pdf";
_pdfdocument.Save(dataDir);
```
## كيفية إضافة نص شفاف في ملف PDF

يحتوي ملف PDF على صورة، نص، رسم بياني، مرفقات، وكائنات تعليقات توضيحية، وعند إنشاء TextFragment، يمكنك تعيين معلومات اللون الأمامي والخلفي بالإضافة إلى تنسيق النص. يدعم Aspose.PDF لـ .NET ميزة إضافة نص بقناة لون ألفا. يوضح الجزء التالي من الكود كيفية إضافة نص بلون شفاف.

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// إنشاء نموذج مستند
Document doc = new Document();
// إضافة صفحة إلى مجموعة صفحات ملف PDF
Aspose.Pdf.Page page = doc.Pages.Add();

// إنشاء كائن الرسم
Aspose.Pdf.Drawing.Graph canvas = new Aspose.Pdf.Drawing.Graph(100, 400);
// إنشاء نموذج مستطيل بأبعاد معينة
Aspose.Pdf.Drawing.Rectangle rect = new Aspose.Pdf.Drawing.Rectangle(100, 100, 400, 400);
// إنشاء كائن لون من قناة لون ألفا
rect.GraphInfo.FillColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.FromArgb(128, System.Drawing.Color.FromArgb(12957183)));
// إضافة مستطيل إلى مجموعة الأشكال الخاصة بكائن الرسم
canvas.Shapes.Add(rect);
// إضافة كائن الرسم إلى مجموعة الفقرات الخاصة بكائن الصفحة
page.Paragraphs.Add(canvas);
// تعيين القيمة لعدم تغيير موضع كائن الرسم
canvas.IsChangePosition = false;

// إنشاء نموذج TextFragment بقيمة عينة
TextFragment text = new TextFragment("transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text ");
// إنشاء كائن لون من قناة ألفا
Aspose.Pdf.Color color = Aspose.Pdf.Color.FromArgb(30, 0, 255, 0);
// تعيين معلومات اللون لنموذج النص
text.TextState.ForegroundColor = color;
// إضافة نص إلى مجموعة الفقرات الخاصة بنموذج الصفحة
page.Paragraphs.Add(text);

dataDir = dataDir + "AddTransparentText_out.pdf";
doc.Save(dataDir);
```
## تحديد المسافة بين الأسطر للخطوط

كل خط يمتلك مربعًا تجريديًا، وارتفاعه هو المسافة المقصودة بين سطور النوع في نفس حجم الخط.
كل خط له مربع مجرد، وارتفاعه هو المسافة المقصودة بين سطور النوع في نفس حجم النوع.

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

string fontFile = dataDir + "HPSimplified.TTF";
// تحميل ملف PDF الإدخال
Document doc = new Document();
// إنشاء خيارات تنسيق النص مع LineSpacingMode.FullSize
TextFormattingOptions formattingOptions = new TextFormattingOptions();
formattingOptions.LineSpacing = TextFormattingOptions.LineSpacingMode.FullSize;

// إنشاء كائن منشئ النص للصفحة الأولى من الوثيقة
//TextBuilder textBuilder = new TextBuilder(doc.Pages[1]);
// إنشاء جزء نصي بسلسلة عينة
TextFragment textFragment = new TextFragment("Hello world");

if (fontFile != "")
{
    // تحميل خط TrueType في كائن الدفق
    using (FileStream fontStream = System.IO.File.OpenRead(fontFile))
    {
        // تعيين اسم الخط لسلسلة النص
        textFragment.TextState.Font = FontRepository.OpenFont(fontStream, FontTypes.TTF);
        // تحديد الموقع لجزء النص
        textFragment.Position = new Position(100, 600);
        // تعيين خيارات تنسيق النص للجزء الحالي إلى المحددة مسبقًا (التي تشير إلى LineSpacingMode.FullSize)
        textFragment.TextState.FormattingOptions = formattingOptions;
        // إضافة النص إلى منشئ النص حتى يمكن وضعه فوق ملف PDF
        //textBuilder.AppendText(textFragment);
        var page = doc.Pages.Add();
        page.Paragraphs.Add(textFragment);
    }

    dataDir = dataDir + "SpecifyLineSpacing_out.pdf";
    // حفظ المستند PDF الناتج
    doc.Save(dataDir);
}
```
## الحصول على عرض النص بشكل ديناميكي

في بعض الأحيان، يكون من الضروري الحصول على عرض النص بشكل ديناميكي. يتضمن Aspose.PDF لـ .NET طريقتين لقياس عرض السلسلة. يمكنك استدعاء طريقة [MeasureString](https://reference.aspose.com/pdf/net/aspose.pdf.text/font/methods/measurestring) الخاصة بـ Aspose.Pdf.Text.Font أو Aspose.Pdf.Text.TextState (أو كلاهما). يوضح الكود أدناه كيفية استخدام هذه الوظيفة.

```csharp
// للحصول على الأمثلة الكاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Aspose.Pdf.Text.Font font = FontRepository.FindFont("Arial");
TextState ts = new TextState();
ts.Font = font;
ts.FontSize = 14;

if (Math.Abs(font.MeasureString("A", 14) - 9.337) > 0.001)
    Console.WriteLine("قياس سلسلة الخط غير متوقع!");

if (Math.Abs(ts.MeasureString("z") - 7.0) > 0.001)
    Console.WriteLine("قياس سلسلة الخط غير متوقع!");

for (char c = 'A'; c <= 'z'; c++)
{
    double fnMeasure = font.MeasureString(c.ToString(), 14);
    double tsMeasure = ts.MeasureString(c.ToString());

    if (Math.Abs(fnMeasure - tsMeasure) > 0.001)
        Console.WriteLine("قياس الخط وحالة السلسلة لا يتطابقان!");
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "مكتبة Aspose.PDF لـ .NET",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "المبيعات",
                "areaServed": "الولايات المتحدة",
                "availableLanguage": "الإنجليزية"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "المبيعات",
                "areaServed": "المملكة المتحدة",
                "availableLanguage": "الإنجليزية"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "المبيعات",
                "areaServed": "أستراليا",
                "availableLanguage": "الإنجليزية"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "مكتبة تعديل ملفات PDF لـ .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
```

