---
title: البحث والحصول على نص من صفحات PDF
linktitle: البحث والحصول على نص
type: docs
weight: 60
url: ar/net/search-and-get-text-from-pdf/
description: يشرح هذا المقال كيفية استخدام الأدوات المختلفة للبحث والحصول على نص من Aspose.PDF لـ .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "البحث والحصول على نص من صفحات PDF",
    "alternativeHeadline": "أدوات للبحث والحصول على نص من صفحات PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد وثيقة PDF",
    "keywords": "pdf, c#, بحث نص, الحصول على نص من pdf",
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
    "url": "/net/search-and-get-text-from-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/search-and-get-text-from-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": "يشرح هذا المقال كيفية استخدام الأدوات المختلفة للبحث والحصول على نص من Aspose.PDF لـ .NET."
}
</script>
الشفرة التالية تعمل أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

## البحث والحصول على نص من جميع صفحات مستند PDF

تتيح لك الفئة [TextFragmentAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragmentabsorber) إيجاد نص يطابق عبارة معينة من جميع صفحات مستند PDF. للبحث عن النص من جميع المستندات، تحتاج إلى استدعاء طريقة Accept لمجموعة الصفحات. تأخذ الطريقة [Accept](https://reference.aspose.com/pdf/net/aspose.pdf.page/accept/methods/3) كائن TextFragmentAbsorber كمعامل، والذي يعيد مجموعة من كائنات TextFragment. يمكنك التكرار من خلال جميع القطع والحصول على خصائصها مثل النص، الموقع (XIndent, YIndent)، اسم الخط، حجم الخط، IsAccessible، IsEmbedded، IsSubset، لون الخلفية، وغيرها.

الشفرة التالية تظهر لك كيفية البحث عن نص من جميع الصفحات.

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// فتح مستند
Document pdfDocument = new Document(dataDir + "SearchAndGetTextFromAll.pdf");

// إنشاء كائن TextAbsorber لإيجاد جميع نماذج العبارة المدخلة
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("text");

// قبول الامتصاص لجميع الصفحات
pdfDocument.Pages.Accept(textFragmentAbsorber);

// الحصول على مقتطفات النص المستخرجة
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// التكرار خلال القطع
foreach (TextFragment textFragment in textFragmentCollection)
{

    Console.WriteLine("Text : {0} ", textFragment.Text);
    Console.WriteLine("Position : {0} ", textFragment.Position);
    Console.WriteLine("XIndent : {0} ", textFragment.Position.XIndent);
    Console.WriteLine("YIndent : {0} ", textFragment.Position.YIndent);
    Console.WriteLine("Font - Name : {0}", textFragment.TextState.Font.FontName);
    Console.WriteLine("Font - IsAccessible : {0} ", textFragment.TextState.Font.IsAccessible);
    Console.WriteLine("Font - IsEmbedded : {0} ", textFragment.TextState.Font.IsEmbedded);
    Console.WriteLine("Font - IsSubset : {0} ", textFragment.TextState.Font.IsSubset);
    Console.WriteLine("Font Size : {0} ", textFragment.TextState.FontSize);
    Console.WriteLine("Foreground Color : {0} ", textFragment.TextState.ForegroundColor);
}
```
في حال كنت بحاجة إلى البحث عن نص داخل صفحة معينة من ملف PDF، يرجى تحديد رقم الصفحة من مجموعة الصفحات في مثيل المستند واستدعاء طريقة Accept ضد هذه الصفحة (كما هو موضح في سطر الكود أدناه).

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// قبول الامتصاص لصفحة معينة
pdfDocument.Pages[2].Accept(textFragmentAbsorber);
```

## البحث والحصول على أجزاء النص من جميع صفحات مستند PDF

للبحث عن أجزاء النص من جميع الصفحات، تحتاج أولاً إلى الحصول على كائنات TextFragment من المستند.
للبحث عن أجزاء نصية من جميع الصفحات، يجب عليك أولاً الحصول على كائنات TextFragment من المستند.

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// فتح المستند
Document pdfDocument = new Document(dataDir + "SearchAndGetTextPage.pdf");

// إنشاء كائن TextAbsorber للعثور على جميع الحالات لعبارة البحث المدخلة
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("Figure");
// قبول الامتصاص لجميع الصفحات
pdfDocument.Pages.Accept(textFragmentAbsorber);
// الحصول على أجزاء النص المستخرجة
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;
// التكرار خلال الأجزاء
foreach (TextFragment textFragment in textFragmentCollection)
{
    foreach (TextSegment textSegment in textFragment.Segments)
    {
        Console.WriteLine("النص : {0} ", textSegment.Text);
        Console.WriteLine("الموقع : {0} ", textSegment.Position);
        Console.WriteLine("المسافة البادئة X : {0} ", textSegment.Position.XIndent);
        Console.WriteLine("المسافة البادئة Y : {0} ", textSegment.Position.YIndent);
        Console.WriteLine("الخط - الاسم : {0}", textSegment.TextState.Font.FontName);
        Console.WriteLine("الخط - قابل للوصول : {0} ", textSegment.TextState.Font.IsAccessible);
        Console.WriteLine("الخط - مضمن : {0} ", textSegment.TextState.Font.IsEmbedded);
        Console.WriteLine("الخط - جزء من مجموعة : {0} ", textSegment.TextState.Font.IsSubset);
        Console.WriteLine("حجم الخط : {0} ", textSegment.TextState.FontSize);
        Console.WriteLine("لون الخلفية : {0} ", textSegment.TextState.ForegroundColor);
    }
}
```
للبحث والحصول على قطع نصية من صفحة معينة في ملف PDF، يجب تحديد مؤشر الصفحة المعين عند استدعاء الطريقة Accept(..). يرجى الاطلاع على الأسطر البرمجية التالية.

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// قبول الامتصاص لجميع الصفحات
pdfDocument.Pages[2].Accept(textFragmentAbsorber);
```

## البحث والحصول على النص من جميع الصفحات باستخدام التعبير النظامي

يساعدك TextFragmentAbsorber على البحث واسترجاع النص، من جميع الصفحات، بناءً على تعبير نظامي.
TextFragmentAbsorber يساعدك في البحث عن النصوص واسترجاعها من جميع الصفحات، استنادًا إلى تعبير نظامي.

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى مجلد الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// فتح الوثيقة
Document pdfDocument = new Document(dataDir + "SearchRegularExpressionAll.pdf");

// إنشاء كائن TextAbsorber للعثور على جميع العبارات التي تطابق التعبير النظامي
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("\\d{4}-\\d{4}"); // مثل 1999-2000

// تعيين خيار البحث عن النص لتحديد استخدام التعبير النظامي
TextSearchOptions textSearchOptions = new TextSearchOptions(true);

textFragmentAbsorber.TextSearchOptions = textSearchOptions;

// قبول الامتصاص لجميع الصفحات
pdfDocument.Pages.Accept(textFragmentAbsorber);

// الحصول على مجموعات النصوص المستخرجة
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// التكرار عبر الشظايا
foreach (TextFragment textFragment in textFragmentCollection)
{
    Console.WriteLine("النص : {0} ", textFragment.Text);
    Console.WriteLine("الموقع : {0} ", textFragment.Position);
    Console.WriteLine("المسافة البادئة الأفقية : {0} ", textFragment.Position.XIndent);
    Console.WriteLine("المسافة البادئة الرأسية : {0} ", textFragment.Position.YIndent);
    Console.WriteLine("الخط - الاسم : {0}", textFragment.TextState.Font.FontName);
    Console.WriteLine("الخط - متاح : {0} ", textFragment.TextState.Font.IsAccessible);
    Console.WriteLine("الخط - مدمج : {0} ", textFragment.TextState.Font.IsEmbedded);
    Console.WriteLine("الخط - جزئي : {0} ", textFragment.TextState.Font.IsSubset);
    Console.WriteLine("حجم الخط : {0} ", textFragment.TextState.FontSize);
    Console.WriteLine("لون الخط الأمامي : {0} ", textFragment.TextState.ForegroundColor);
}
```
```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
TextFragmentAbsorber textFragmentAbsorber;
// للبحث عن تطابق دقيق لكلمة، يمكنك استخدام التعبير النظامي.
textFragmentAbsorber = new TextFragmentAbsorber(@"\bWord\b", new TextSearchOptions(true));

// للبحث عن سلسلة بأحرف كبيرة أو صغيرة، يمكنك استخدام التعبير النظامي.
textFragmentAbsorber = new TextFragmentAbsorber("(?i)Line", new TextSearchOptions(true));

// للبحث عن جميع السلاسل (تحليل جميع السلاسل) داخل مستند PDF، يرجى استخدام التعبير النظامي التالي.
textFragmentAbsorber = new TextFragmentAbsorber(@"[\S]+");

// العثور على تطابق لسلسلة البحث والحصول على أي شيء بعد السلسلة حتى نهاية السطر.
textFragmentAbsorber = new TextFragmentAbsorber(@"(?i)the ((.)*)");

// يرجى استخدام التعبير النظامي التالي للعثور على نص يلي تطابق التعبير النظامي.
textFragmentAbsorber = new TextFragmentAbsorber(@"(?<=word).*");

// للبحث عن روابط تشعبية/URL داخل مستند PDF، يرجى استخدام التعبير النظامي التالي.
textFragmentAbsorber = new TextFragmentAbsorber(@"(http|ftp|https):\/\/([\w\-_]+(?:(?:\.[\w\-_]+)+))([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?");
```
## البحث عن نص بناءً على Regex وإضافة رابط تشعبي

إذا كنت ترغب في إضافة رابط تشعبي فوق عبارة نصية استنادًا إلى التعبير العادي، ابحث أولاً عن جميع العبارات التي تطابق ذلك التعبير العادي باستخدام TextFragmentAbsorber وأضف رابطًا تشعبيًا فوق هذه العبارات.

للعثور على عبارة وإضافة رابط تشعبي فوقها:

1. قم بتمرير التعبير العادي كمعامل إلى مُنشئ TextFragmentAbsorber.
2. قم بإنشاء كائن TextSearchOptions الذي يحدد ما إذا كان يستخدم التعبير العادي أم لا.
3. احصل على العبارات المطابقة في TextFragments.
4. قم بالتكرار عبر المطابقات للحصول على أبعادها المستطيلة، غير لون الخلفية إلى الأزرق (اختياري - لجعله يظهر مثل رابط تشعبي وإنشاء رابط باستخدام طريقة CreateWebLink(..) في فئة PdfContentEditor.
5. احفظ PDF المُحدث باستخدام طريقة Save لكائن Document.
يوضح المقتطف التالي من الكود كيفية البحث عن نص داخل ملف PDF باستخدام تعبير عادي وإضافة روابط تشعبية فوق المطابقات.

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى الانتقال إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// إنشاء كائن الماص للعثور على جميع حالات عبارة البحث المدخلة
TextFragmentAbsorber absorber = new TextFragmentAbsorber("\\d{4}-\\d{4}");
// تمكين بحث التعبير العادي
absorber.TextSearchOptions = new TextSearchOptions(true);
// فتح المستند
PdfContentEditor editor = new PdfContentEditor();
// ربط ملف PDF المصدر
editor.BindPdf(dataDir + "SearchRegularExpressionPage.pdf");
// قبول الماص للصفحة
editor.Document.Pages[1].Accept(absorber);

int[] dashArray = { };
String[] LEArray = { };
System.Drawing.Color blue = System.Drawing.Color.Blue;

// التكرار عبر القطع
foreach (TextFragment textFragment in absorber.TextFragments)
{
    textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
    System.Drawing.Rectangle rect = new System.Drawing.Rectangle((int)textFragment.Rectangle.LLX,
        (int)Math.Round(textFragment.Rectangle.LLY), (int)Math.Round(textFragment.Rectangle.Width + 2),
        (int)Math.Round(textFragment.Rectangle.Height + 1));
    Enum[] actionName = new Enum[2] { Aspose.Pdf.Annotations.PredefinedAction.Document_AttachFile, Aspose.Pdf.Annotations.PredefinedAction.Document_ExtractPages };
    editor.CreateWebLink(rect, "http:// Www.aspose.com", 1, blue, actionName);
    editor.CreateLine(rect, "", (float)textFragment.Rectangle.LLX + 1, (float)textFragment.Rectangle.LLY - 1,
        (float)textFragment.Rectangle.URX, (float)textFragment.Rectangle.LLY - 1, 1, 1, blue, "S", dashArray, LEArray);
}

dataDir = dataDir + "SearchTextAndAddHyperlink_out.pdf";
editor.Save(dataDir);
editor.Close();
```
## البحث ورسم مستطيل حول كل قطعة نص

Aspose.PDF لـ .NET يدعم ميزة البحث والحصول على إحداثيات كل حرف أو قطع نصية. لذا من أجل التأكد من الإحداثيات المعادة لكل حرف، قد نفكر في التمييز (إضافة مستطيل) حول كل حرف.

في حالة فقرة نصية، قد تفكر في استخدام بعض التعبيرات النظامية لتحديد نهاية الفقرة ورسم مستطيل حولها. الرجاء الإطلاع على المقتطف التالي من الكود. يحصل المقتطف التالي من الكود على إحداثيات كل حرف وينشئ مستطيل حول كل حرف.

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// فتح المستند
Document document = new Document(dataDir + "SearchAndGetTextFromAll.pdf");

// إنشاء كائن TextAbsorber للعثور على جميع العبارات التي تطابق التعبير النظامي

TextFragmentAbsorber textAbsorber = new TextFragmentAbsorber(@"[\S]+");

TextSearchOptions textSearchOptions = new TextSearchOptions(true);

textAbsorber.TextSearchOptions = textSearchOptions;

document.Pages.Accept(textAbsorber);

var editor = new PdfContentEditor(document);

foreach (TextFragment textFragment in textAbsorber.TextFragments)
{
    foreach (TextSegment textSegment in textFragment.Segments)
    {
        DrawBox(editor, textFragment.Page.Number, textSegment, System.Drawing.Color.Red);
    }

}
dataDir = dataDir + "SearchTextAndDrawRectangle_out.pdf";
document.Save(dataDir);
```
## تمييز كل حرف في مستند PDF

{{% alert color="primary" %}}

يمكنك تجربة البحث عن نص في مستند باستخدام Aspose.PDF والحصول على النتائج عبر الإنترنت في هذا [الرابط](https://products.aspose.app/pdf/search)

{{% /alert %}}

يدعم Aspose.PDF لـ .NET ميزة البحث والحصول على إحداثيات كل حرف أو أجزاء من النص. لذا من أجل التأكد من الإحداثيات التي يتم إرجاعها لكل حرف، قد نفكر في تمييز (إضافة مستطيل) حول كل حرف. يقوم الجزء التالي من الكود بالحصول على إحداثيات كل حرف وينشئ مستطيل حول كل حرف.

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

int resolution = 150;

Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(dataDir + "input.pdf");

using (MemoryStream ms = new MemoryStream())
{
    PdfConverter conv = new PdfConverter(pdfDocument);
    conv.Resolution = new Resolution(resolution, resolution);
    conv.GetNextImage(ms, System.Drawing.Imaging.ImageFormat.Png);

    Bitmap bmp = (Bitmap)Bitmap.FromStream(ms);

    using (System.Drawing.Graphics gr = System.Drawing.Graphics.FromImage(bmp))
    {
        float scale = resolution / 72f;
        gr.Transform = new System.Drawing.Drawing2D.Matrix(scale, 0, 0, -scale, 0, bmp.Height);

        for (int i = 0; i < pdfDocument.Pages.Count; i++)
        {
Page page = pdfDocument.Pages[1];
// إنشاء كائن TextAbsorber للعثور على جميع الكلمات
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(@"[\S]+");
textFragmentAbsorber.TextSearchOptions.IsRegularExpressionUsed = true;
page.Accept(textFragmentAbsorber);
// الحصول على أجزاء النص المستخرجة
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;
// التكرار خلال الأجزاء
foreach (TextFragment textFragment in textFragmentCollection)
{
    if (i == 0)
    {
        gr.DrawRectangle(
        Pens.Yellow,
        (float)textFragment.Position.XIndent,
        (float)textFragment.Position.YIndent,
        (float)textFragment.Rectangle.Width,
        (float)textFragment.Rectangle.Height);

        for (int segNum = 1; segNum <= textFragment.Segments.Count; segNum++)
        {
TextSegment segment = textFragment.Segments[segNum];

for (int charNum = 1; charNum <= segment.Characters.Count; charNum++)
{
    CharInfo characterInfo = segment.Characters[charNum];

    Aspose.Pdf.Rectangle rect = page.GetPageRect(true);
    Console.WriteLine("TextFragment = " + textFragment.Text + "    Page URY = " + rect.URY +
          "   TextFragment URY = " + textFragment.Rectangle.URY);

    gr.DrawRectangle(
    Pens.Black,
    (float)characterInfo.Rectangle.LLX,
    (float)characterInfo.Rectangle.LLY,
    (float)characterInfo.Rectangle.Width,
    (float)characterInfo.Rectangle.Height);
}

gr.DrawRectangle(
Pens.Green,
(float)segment.Rectangle.LLX,
(float)segment.Rectangle.LLY,
(float)segment.Rectangle.Width,
(float)segment.Rectangle.Height);
        }
    }
}
        }
    }
    dataDir = dataDir + "HighlightCharacterInPDF_out.png";
    bmp.Save(dataDir, System.Drawing.Imaging.ImageFormat.Png);
}
```
## إضافة وبحث نص مخفي

أحيانًا نرغب في إضافة نص مخفي في مستند PDF ثم البحث عن النص المخفي واستخدام موضعه للمعالجة اللاحقة. لراحتك، يوفر Aspose.PDF لـ .NET هذه الإمكانيات. يمكنك إضافة نص مخفي أثناء إنشاء المستند. كما يمكنك العثور على النص المخفي باستخدام TextFragmentAbsorber. لإضافة نص مخفي، اضبط خاصية TextState.Invisible على 'true' للنص المضاف. يجد TextFragmentAbsorber كل النص الذي يطابق النمط (إذا تم تحديده). هذا هو السلوك الافتراضي الذي لا يمكن تغييره. للتحقق من أن النص الموجود فعلاً غير مرئي، يمكن استخدام خاصية TextState.Invisible. يوضح الجزء المقطعي أدناه كيفية استخدام هذه الميزة.

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الانتقال إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

//إنشاء مستند بنص مخفي
Aspose.Pdf.Document doc = new Aspose.Pdf.Document();
Page page = doc.Pages.Add();
TextFragment frag1 = new TextFragment("هذا نص شائع.");
TextFragment frag2 = new TextFragment("هذا نص غير مرئي.");

//تعيين خاصية النص - غير مرئي
frag2.TextState.Invisible = true;

page.Paragraphs.Add(frag1);
page.Paragraphs.Add(frag2);
doc.Save(dataDir + "39400_out.pdf");
doc.Dispose();

//البحث عن النص في المستند
doc = new Aspose.Pdf.Document(dataDir + "39400_out.pdf");
TextFragmentAbsorber absorber = new TextFragmentAbsorber();
absorber.Visit(doc.Pages[1]);

foreach (TextFragment fragment in absorber.TextFragments)
{
    //القيام بشيء ما مع القطع
    Console.WriteLine("النص '{0}' في الموضع {1} غير مرئية: {2} ",
    fragment.Text, fragment.Position.ToString(), fragment.TextState.Invisible);
}
doc.Dispose();
```
## البحث عن نص باستخدام .NET Regex

Aspose.PDF لـ .NET يوفر القدرة على البحث في الوثائق باستخدام خيار Regex القياسي لـ .NET. يمكن استخدام TextFragmentAbsorber لهذا الغرض كما هو موضح في مثال الكود أدناه.

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// إنشاء كائن Regex للعثور على جميع الكلمات
System.Text.RegularExpressions.Regex regex = new System.Text.RegularExpressions.Regex(@"[\S]+");

// فتح الوثيقة
Aspose.Pdf.Document document = new Aspose.Pdf.Document(dataDir + "SearchTextRegex.pdf");

// الحصول على صفحة معينة
Page page = document.Pages[1];

// إنشاء كائن TextAbsorber للعثور على جميع الحالات للتعبير النظامي المدخل
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(regex);
textFragmentAbsorber.TextSearchOptions.IsRegularExpressionUsed = true;

// قبول الامتصاص للصفحة
page.Accept(textFragmentAbsorber);

// الحصول على النصوص المستخرجة
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// التكرار عبر القطع النصية
foreach (TextFragment textFragment in textFragmentCollection)
{
    Console.WriteLine(textFragment.Text);
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
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
                "areaServed": "الولايات المتحدة الأمريكية",
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

