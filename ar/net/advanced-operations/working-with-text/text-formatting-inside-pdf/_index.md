---
title: تنسيق النص داخل ملف PDF باستخدام C#
linktitle: تنسيق النص داخل PDF
type: docs
weight: 30
url: ar/net/text-formatting-inside-pdf/
description: تشرح هذه الصفحة كيفية تنسيق النص داخل ملف PDF الخاص بك. هناك إضافة مسافة بادئة للسطر، إضافة حد للنص، إضافة تسطير للنص، وغير ذلك.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "تنسيق النص داخل ملف PDF باستخدام C#",
    "alternativeHeadline": "كيفية تنسيق النص في ملف PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "إنشاء مستند PDF",
    "keywords": "pdf, c#, تنسيق النص في pdf",
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
    "url": "/net/text-formatting-inside-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/text-formatting-inside-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": "تشرح هذه الصفحة كيفية تنسيق النص داخل ملف PDF الخاص بك. هناك إضافة مسافة بادئة للسطر، إضافة حد للنص، إضافة تسطير للنص، وغير ذلك."
}
</script>

الشفرة التالية تعمل أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

## كيفية إضافة مسافة بادئة للسطور في ملف PDF

يقدم Aspose.PDF لـ .NET خاصية SubsequentLinesIndent ضمن الفئة [TextFormattingOptions](https://reference.aspose.com/pdf/net/aspose.pdf.text/textformattingoptions). والتي يمكن استخدامها لتحديد المسافة البادئة للسطور في سيناريوهات إنشاء PDF باستخدام TextFragment ومجموعة Paragraphs.

يرجى استخدام الشفرة التالية لاستخدام الخاصية:

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// إنشاء كائن مستند جديد
Aspose.Pdf.Document document = new Aspose.Pdf.Document();
Aspose.Pdf.Page page = document.Pages.Add();

string textFragment = string.Concat(Enumerable.Repeat("A quick brown fox jumped over the lazy dog. ", 10));

Aspose.Pdf.Text.TextFragment text = new Aspose.Pdf.Text.TextFragment(textFragment);

// تهيئة TextFormattingOptions لجزء النص وتحديد قيمة SubsequentLinesIndent
text.TextState.FormattingOptions = new Aspose.Pdf.Text.TextFormattingOptions()
{
    SubsequentLinesIndent = 20
};

page.Paragraphs.Add(text);

text = new Aspose.Pdf.Text.TextFragment("Line2");
page.Paragraphs.Add(text);

text = new Aspose.Pdf.Text.TextFragment("Line3");
page.Paragraphs.Add(text);

text = new Aspose.Pdf.Text.TextFragment("Line4");
page.Paragraphs.Add(text);

text = new Aspose.Pdf.Text.TextFragment("Line5");
page.Paragraphs.Add(text);

document.Save(dataDir + "SubsequentIndent_out.pdf");
```

## كيفية إضافة حدود للنص

الشفرة التالية توضح كيفية إضافة حد لنص باستخدام TextBuilder وتعيين خاصية DrawTextRectangleBorder لـ TextState:

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى مجلد الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// إنشاء كائن وثيقة جديد
Document pdfDocument = new Document();
// الحصول على صفحة معينة
Page pdfPage = (Page)pdfDocument.Pages.Add();
// إنشاء قطعة نص
TextFragment textFragment = new TextFragment("النص الرئيسي");
textFragment.Position = new Position(100, 600);
// تعيين خصائص النص
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;
// تعيين خاصية StrokingColor لرسم حد (التخطيط) حول مستطيل النص
textFragment.TextState.StrokingColor = Aspose.Pdf.Color.DarkRed;
// تعيين قيمة خاصية DrawTextRectangleBorder إلى true
textFragment.TextState.DrawTextRectangleBorder = true;
TextBuilder tb = new TextBuilder(pdfPage);
tb.AppendText(textFragment);
// حفظ الوثيقة
pdfDocument.Save(dataDir + "PDFWithTextBorder_out.pdf");
```
## كيفية إضافة نص مُسطَّر

الشفرة التالية تُظهر لك كيفية إضافة نص مُسطَّر أثناء إنشاء ملف PDF جديد.

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// إنشاء كائن التوثيق
Document pdfDocument = new Document();
// إضافة صفحة إلى مستند PDF
pdfDocument.Pages.Add();
// إنشاء TextBuilder للصفحة الأولى
TextBuilder tb = new TextBuilder(pdfDocument.Pages[1]);
// TextFragment مع نص عينة
TextFragment fragment = new TextFragment("Test message");
// تحديد الخط لـ TextFragment
fragment.TextState.Font = FontRepository.FindFont("Arial");
fragment.TextState.FontSize = 10;
// تحديد تنسيق النص كمُسطَّر
fragment.TextState.Underline = true;
// تحديد الموقع الذي يجب وضع TextFragment فيه
fragment.Position = new Position(10, 800);
// إلحاق TextFragment بملف PDF
tb.AppendText(fragment);

dataDir = dataDir + "AddUnderlineText_out.pdf";

// حفظ مستند PDF الناتج.
pdfDocument.Save(dataDir);
```
## كيفية إضافة حد حول النص المضاف

لديك السيطرة على مظهر النص الذي تضيفه. يوضح المثال أدناه كيفية إضافة حد حول قطعة من النص التي أضفتها عن طريق رسم مستطيل حولها. تعرف على المزيد حول فئة [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor).

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

PdfContentEditor editor = new PdfContentEditor();
editor.BindPdf(dataDir + "input.pdf");
LineInfo lineInfo = new LineInfo();
lineInfo.LineWidth = 2;
lineInfo.VerticeCoordinate = new float[] { 0, 0, 100, 100, 50, 100 };
lineInfo.Visibility = true;
editor.CreatePolygon(lineInfo, 1, new System.Drawing.Rectangle(0, 0, 0, 0), "");

dataDir = dataDir + "AddingBorderAroundAddedText_out.pdf";

// حفظ الوثيقة PDF الناتجة.
editor.Save(dataDir);
```

## كيفية إضافة تغذية خط جديد
## كيفية إضافة خط جديد

لا يدعم TextFragment تغذية الخط داخل النص. ومع ذلك، لإضافة نص مع تغذية خط، يرجى استخدام TextFragment مع TextParagraph:

- استخدم "\r\n" أو Environment.NewLine في TextFragment بدلاً من "\n" المفرد؛
- إنشاء كائن TextParagraph. سيقوم بإضافة نص مع تقسيم النص؛
- أضف TextFragment مع TextParagraph.AppendLine؛
- أضف TextParagraph مع TextBuilder.AppendParagraph.
يرجى استخدام الجزء البرمجي أدناه.

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
Aspose.Pdf.Document pdfApplicationDoc = new Aspose.Pdf.Document();
Aspose.Pdf.Page applicationFirstPage = (Aspose.Pdf.Page)pdfApplicationDoc.Pages.Add();

// تهيئة TextFragment جديد بنص يحتوي على علامات تغذية الخط المطلوبة
Aspose.Pdf.Text.TextFragment textFragment = new Aspose.Pdf.Text.TextFragment("Applicant Name: " + Environment.NewLine + " Joe Smoe");

// تعيين خصائص قطعة النص إذا لزم الأمر
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;

// إنشاء كائن TextParagraph
TextParagraph par = new TextParagraph();

// إضافة TextFragment جديد إلى الفقرة
par.AppendLine(textFragment);

// تعيين موقع الفقرة
par.Position = new Aspose.Pdf.Text.Position(100, 600);

// إنشاء كائن TextBuilder
TextBuilder textBuilder = new TextBuilder(applicationFirstPage);
// إضافة TextParagraph باستخدام TextBuilder
textBuilder.AppendParagraph(par);


dataDir = dataDir + "AddNewLineFeed_out.pdf";

// حفظ الوثيقة PDF الناتجة.
pdfApplicationDoc.Save(dataDir);
```
## كيفية إضافة نص مشطوب

توفر فئة TextState القدرة على تعيين التنسيقات لـ TextFragments التي يتم وضعها داخل مستند PDF. يمكنك استخدام هذه الفئة لتعيين تنسيقات النص مثل الغامق، المائل، التسطير، وابتداءً من هذا الإصدار، قدمت الواجهة البرمجية القدرات لوضع علامة تنسيق النص كمشطوب. يرجى استخدام قطعة الكود التالية لإضافة TextFragment بتنسيق مشطوب.

يرجى استخدام قطعة الكود كاملة:

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى مجلد المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// فتح المستند
Document pdfDocument = new Document();
// الحصول على صفحة معينة
Page pdfPage = (Page)pdfDocument.Pages.Add();

// إنشاء جزء نصي
TextFragment textFragment = new TextFragment("النص الرئيسي");
textFragment.Position = new Position(100, 600);

// تعيين خصائص النص
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;
// تعيين خاصية الشطب
textFragment.TextState.StrikeOut = true;
// وضع علامة النص كغامق
textFragment.TextState.FontStyle = FontStyles.Bold;

// إنشاء كائن TextBuilder
TextBuilder textBuilder = new TextBuilder(pdfPage);
// إلحاق جزء النص بصفحة PDF
textBuilder.AppendText(textFragment);


dataDir = dataDir + "AddStrikeOutText_out.pdf";

// حفظ مستند PDF الناتج.
pdfDocument.Save(dataDir);
```
## تطبيق التظليل التدريجي على النص

تم تحسين تنسيق النص بشكل أكبر في واجهة برمجة التطبيقات لسيناريوهات تحرير النصوص والآن يمكنك إضافة نص بفضاء ألوان النمط داخل مستند PDF. تم تعزيز صف Aspose.Pdf.Color بشكل أكبر من خلال تقديم خاصية جديدة لفضاء ألوان النمط، والتي يمكن استخدامها لتحديد ألوان التظليل للنص. تضيف هذه الخاصية الجديدة أنواع مختلفة من التظليل التدريجي للنص مثل التظليل المحوري، التظليل الشعاعي (النوع 3) كما هو موضح في مقتطف الكود التالي:

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

using (Document pdfDocument = new Document(dataDir + "text_sample4.pdf"))
{
    TextFragmentAbsorber absorber = new TextFragmentAbsorber("Lorem ipsum");
    pdfDocument.Pages.Accept(absorber);

    TextFragment textFragment = absorber.TextFragments[1];

    // إنشاء لون جديد مع فضاء ألوان النمط
    textFragment.TextState.ForegroundColor = new Aspose.Pdf.Color()
    {
        PatternColorSpace = new Aspose.Pdf.Drawing.GradientAxialShading(Color.Red, Color.Blue)
    };
    textFragment.TextState.Underline = true;

    pdfDocument.Save(dataDir + "text_out.pdf");
}
```
>لتطبيق تدرج شعاعي، يمكنك ضبط خاصية 'PatternColorSpace' لتساوي 'Aspose.Pdf.Drawing.GradientRadialShading(اللون_الابتدائي، اللون_النهائي)' في مقتطف الكود أعلاه.

## كيفية محاذاة النص ليطفو على المحتوى

يدعم Aspose.PDF ضبط محاذاة النص للمحتويات داخل عنصر صندوق عائم. يمكن استخدام خصائص المحاذاة لعنصر Aspose.Pdf.FloatingBox لتحقيق ذلك كما هو موضح في مثال الكود التالي.

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Aspose.Pdf.Document doc = new Document();
doc.Pages.Add();

Aspose.Pdf.FloatingBox floatBox = new Aspose.Pdf.FloatingBox(100, 100);
floatBox.VerticalAlignment = VerticalAlignment.Bottom;
floatBox.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
floatBox.Paragraphs.Add(new TextFragment("FloatingBox_bottom"));
floatBox.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Blue);
doc.Pages[1].Paragraphs.Add(floatBox);

Aspose.Pdf.FloatingBox floatBox1 = new Aspose.Pdf.FloatingBox(100, 100);
floatBox1.VerticalAlignment = VerticalAlignment.Center;
floatBox1.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
floatBox1.Paragraphs.Add(new TextFragment("FloatingBox_center"));
floatBox1.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Blue);
doc.Pages[1].Paragraphs.Add(floatBox1);

Aspose.Pdf.FloatingBox floatBox2 = new Aspose.Pdf.FloatingBox(100, 100);
floatBox2.VerticalAlignment = VerticalAlignment.Top;
floatBox2.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
floatBox2.Paragraphs.Add(new TextFragment("FloatingBox_top"));
floatBox2.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Blue);
doc.Pages[1].Paragraphs.Add(floatBox2);

doc.Save(dataDir + "FloatingBox_alignment_review_out.pdf");
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
        "priceCurrency": "دولار أمريكي"
    },
    "applicationCategory": "مكتبة تعديل ملفات PDF لـ .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "ويندوز، ماك أو إس، لينكس",
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

