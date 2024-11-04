---
title: تنسيق النص داخل PDF باستخدام بايثون
linktitle: تنسيق النص داخل PDF
type: docs
weight: 30
url: /python-net/text-formatting-inside-pdf/
description: توضح هذه الصفحة كيفية تنسيق النص داخل ملف PDF الخاص بك. هناك إضافة مسافة بادئة للسطر، إضافة حدود للنص، إضافة نص تحت الخط، إلخ.
lastmod: "2024-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "تنسيق النص داخل PDF باستخدام بايثون",
    "alternativeHeadline": "كيفية تنسيق النص في ملف PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد مستندات pdf",
    "keywords": "pdf, python, تنسيق النص في pdf",
    "wordcount": "302",
    "proficiencyLevel":"مبتدئ",
    "publisher": {
        "@type": "Organization",
        "name": "فريق مستندات Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "url": "/python-net/text-formatting-inside-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/text-formatting-inside-pdf/"
    },
    "dateModified": "2024-02-04",
    "description": "توضح هذه الصفحة كيفية تنسيق النص داخل ملف PDF الخاص بك. هناك إضافة مسافة بادئة للسطر، إضافة حدود للنص، إضافة نص تحت الخط، إلخ."
}
</script>


## كيفية إضافة مسافة بادئة للسطر إلى ملف PDF

يقدم Aspose.PDF for .NET خاصية SubsequentLinesIndent ضمن فئة [TextFormattingOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textformattingoptions). والتي يمكن استخدامها لتحديد المسافة البادئة للسطر في سيناريوهات توليد PDF مع TextFragment ومجموعة Paragraphs.

يرجى استخدام مقطع الكود التالي لاستخدام الخاصية:

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// إنشاء كائن مستند جديد
Aspose.Pdf.Document document = new Aspose.Pdf.Document();
Aspose.Pdf.Page page = document.Pages.Add();

string textFragment = string.Concat(Enumerable.Repeat("A quick brown fox jumped over the lazy dog. ", 10));

Aspose.Pdf.Text.TextFragment text = new Aspose.Pdf.Text.TextFragment(textFragment);

// تهيئة خيارات تنسيق النص لمقطع النص وتحديد قيمة SubsequentLinesIndent
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

يوضح مقتطف الكود التالي كيفية إضافة حدود لنص باستخدام TextBuilder وتعيين خاصية DrawTextRectangleBorder في TextState:

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// إنشاء كائن مستند جديد
Document pdfDocument = new Document();
// الحصول على صفحة معينة
Page pdfPage = (Page)pdfDocument.Pages.Add();
// إنشاء مقطع نصي
TextFragment textFragment = new TextFragment("main text");
textFragment.Position = new Position(100, 600);
// تعيين خصائص النص
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;
// تعيين خاصية StrokingColor لرسم الحدود (الشطب) حول مستطيل النص
textFragment.TextState.StrokingColor = Aspose.Pdf.Color.DarkRed;
// تعيين قيمة خاصية DrawTextRectangleBorder إلى true
textFragment.TextState.DrawTextRectangleBorder = true;
TextBuilder tb = new TextBuilder(pdfPage);
tb.AppendText(textFragment);
// حفظ المستند
pdfDocument.Save(dataDir + "PDFWithTextBorder_out.pdf");
```


## كيفية إضافة نص مسطر

يوضح مقطع الشفرة التالي كيفية إضافة نص مسطر أثناء إنشاء ملف PDF جديد.

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// إنشاء كائن الوثيقة
Document pdfDocument = new Document();
// إضافة صفحة إلى وثيقة PDF
pdfDocument.Pages.Add();
// إنشاء TextBuilder للصفحة الأولى
TextBuilder tb = new TextBuilder(pdfDocument.Pages[1]);
// TextFragment مع نص مثال
TextFragment fragment = new TextFragment("Test message");
// تعيين الخط لـ TextFragment
fragment.TextState.Font = FontRepository.FindFont("Arial");
fragment.TextState.FontSize = 10;
// تعيين تنسيق النص كمسطر
fragment.TextState.Underline = true;
// تحديد الموقع حيث يجب وضع TextFragment
fragment.Position = new Position(10, 800);
// إلحاق TextFragment بملف PDF
tb.AppendText(fragment);

dataDir = dataDir + "AddUnderlineText_out.pdf";

// حفظ مستند PDF الناتج.
pdfDocument.Save(dataDir);
```


## كيفية إضافة حدود حول النص المضاف

لديك السيطرة على الشكل والمظهر للنص الذي تضيفه. يوضح المثال أدناه كيفية إضافة حدود حول قطعة من النص التي قمت بإضافتها برسم مستطيل حولها. اكتشف المزيد حول فئة [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor).

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

PdfContentEditor editor = new PdfContentEditor();
editor.BindPdf(dataDir + "input.pdf");
LineInfo lineInfo = new LineInfo();
lineInfo.LineWidth = 2;
lineInfo.VerticeCoordinate = new float[] { 0, 0, 100, 100, 50, 100 };
lineInfo.Visibility = true;
editor.CreatePolygon(lineInfo, 1, new System.Drawing.Rectangle(0, 0, 0, 0), "");

dataDir = dataDir + "AddingBorderAroundAddedText_out.pdf";

// احفظ مستند PDF الناتج.
editor.Save(dataDir);
```

## كيفية إضافة تغذية سطر جديد

TextFragment لا يدعم تغذية السطر داخل النص. ومع ذلك، لإضافة نص مع تغذية السطر، يرجى استخدام TextFragment مع TextParagraph:

- استخدم "\r\n" أو Environment.NewLine في TextFragment بدلاً من "\n" الواحد;
- أنشئ كائن TextParagraph. سيضيف نصًا مع تقسيم السطر;
- أضف الـ TextFragment مع TextParagraph.AppendLine;
- أضف الـ TextParagraph مع TextBuilder.AppendParagraph.
يرجى استخدام الكود أدناه.

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
Aspose.Pdf.Document pdfApplicationDoc = new Aspose.Pdf.Document();
Aspose.Pdf.Page applicationFirstPage = (Aspose.Pdf.Page)pdfApplicationDoc.Pages.Add();

// تهيئة TextFragment جديد يحتوي على نص بعلامات السطر الجديدة المطلوبة
Aspose.Pdf.Text.TextFragment textFragment = new Aspose.Pdf.Text.TextFragment("Applicant Name: " + Environment.NewLine + " Joe Smoe");

// ضبط خصائص جزء النص إذا لزم الأمر
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;

// إنشاء كائن TextParagraph
TextParagraph par = new TextParagraph();

// إضافة TextFragment جديد إلى الفقرة
par.AppendLine(textFragment);

// ضبط موضع الفقرة
par.Position = new Aspose.Pdf.Text.Position(100, 600);

// إنشاء كائن TextBuilder
TextBuilder textBuilder = new TextBuilder(applicationFirstPage);
// إضافة TextParagraph باستخدام TextBuilder
textBuilder.AppendParagraph(par);


dataDir = dataDir + "AddNewLineFeed_out.pdf";

// حفظ مستند PDF الناتج.
pdfApplicationDoc.Save(dataDir);
```


## كيفية إضافة نص مشطوب

توفر فئة TextState الإمكانيات لتعيين التنسيق لـ TextFragments التي يتم وضعها داخل مستند PDF. يمكنك استخدام هذه الفئة لتعيين تنسيق النص كعريض، مائل، مسطر وبداية من هذا الإصدار، وفرت واجهة برمجة التطبيقات الإمكانيات لتحديد تنسيق النص كمشطوب. يرجى محاولة استخدام مقطع الكود التالي لإضافة TextFragment بتنسيق مشطوب.

يرجى استخدام مقطع الكود الكامل:

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// فتح المستند
Document pdfDocument = new Document();
// الحصول على صفحة معينة
Page pdfPage = (Page)pdfDocument.Pages.Add();

// إنشاء مقطع نصي
TextFragment textFragment = new TextFragment("main text");
textFragment.Position = new Position(100, 600);

// تعيين خصائص النص
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;
// تعيين خاصية الشطب
textFragment.TextState.StrikeOut = true;
// تحديد النص كعريض
textFragment.TextState.FontStyle = FontStyles.Bold;

// إنشاء كائن TextBuilder
TextBuilder textBuilder = new TextBuilder(pdfPage);
// إلحاق المقطع النصي بصفحة PDF
textBuilder.AppendText(textFragment);

dataDir = dataDir + "AddStrikeOutText_out.pdf";

// حفظ مستند PDF الناتج.
pdfDocument.Save(dataDir);
```


## تطبيق تظليل التدرج اللوني على النص

تم تحسين تنسيق النص بشكل أكبر في واجهة برمجة التطبيقات لسيناريوهات تحرير النصوص، ويمكنك الآن إضافة نص بألوان نمطية داخل مستند PDF. تم تحسين فئة Aspose.Pdf.Color بشكل أكبر من خلال تقديم خاصية جديدة لـ PatternColorSpace، والتي يمكن استخدامها لتحديد ألوان التظليل للنص. تضيف هذه الخاصية الجديدة تظليل تدرج مختلف للنص مثل تظليل محوري، وتظليل شعاعي (النوع 3) كما هو موضح في مقطع الشيفرة التالي:

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

using (Document pdfDocument = new Document(dataDir + "text_sample4.pdf"))
{
    TextFragmentAbsorber absorber = new TextFragmentAbsorber("Lorem ipsum");
    pdfDocument.Pages.Accept(absorber);

    TextFragment textFragment = absorber.TextFragments[1];

    // إنشاء لون جديد باستخدام مساحة الألوان النمطية
    textFragment.TextState.ForegroundColor = new Aspose.Pdf.Color()
    {
        PatternColorSpace = new Aspose.Pdf.Drawing.GradientAxialShading(Color.Red, Color.Blue)
    };
    textFragment.TextState.Underline = true;

    pdfDocument.Save(dataDir + "text_out.pdf");
}
```


> لتطبيق التدرج الشعاعي، يمكنك تعيين خاصية ‘PatternColorSpace’ مساوية لـ ‘Aspose.Pdf.Drawing.GradientRadialShading(startingColor, endingColor)’ في الكود أعلاه.

## كيفية محاذاة النص مع المحتوى العائم

يدعم Aspose.PDF تعيين محاذاة النص للمحتويات داخل عنصر صندوق عائم. يمكن استخدام خصائص المحاذاة لنسخة Aspose.Pdf.FloatingBox لتحقيق ذلك كما هو موضح في نموذج الكود التالي.

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
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
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
                "contactType": "مبيعات",
                "areaServed": "الولايات المتحدة",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "مبيعات",
                "areaServed": "المملكة المتحدة",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "مبيعات",
                "areaServed": "أستراليا",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "مكتبة معالجة PDF لـ .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2024.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>