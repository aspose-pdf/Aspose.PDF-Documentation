---
title: البحث واستخراج النص من صفحات PDF
linktitle: البحث واستخراج النص
type: docs
weight: 60
url: /python-net/search-and-get-text-from-pdf/
description: توضح هذه المقالة كيفية استخدام أدوات مختلفة للبحث واستخراج النص من Aspose.PDF for .NET.
lastmod: "2024-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "البحث واستخراج النص من صفحات PDF",
    "alternativeHeadline": "أدوات للبحث واستخراج النص من صفحات PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, python, search text, get text from pdf",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/python-net/search-and-get-text-from-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/search-and-get-text-from-pdf/"
    },
    "dateModified": "2024-02-04",
    "description": "توضح هذه المقالة كيفية استخدام أدوات مختلفة للبحث واستخراج النص من Aspose.PDF for .NET."
}
</script>


## البحث والحصول على النص من جميع صفحات مستند PDF

تسمح لك فئة [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber) بالبحث عن النص الذي يطابق عبارة معينة من جميع صفحات مستند PDF. من أجل البحث عن النص من المستند بأكمله، تحتاج إلى استدعاء طريقة Accept من مجموعة Pages. تأخذ طريقة [Accept](https://reference.aspose.com/pdf/python-net/aspose.pdf.page/accept/methods/3) كائن TextFragmentAbsorber كمعامل، والذي يعيد مجموعة من كائنات TextFragment. يمكنك التكرار عبر جميع الأجزاء والحصول على خصائصها مثل النص، الموقع (XIndent, YIndent)، اسم الخط، حجم الخط، IsAccessible، IsEmbedded، IsSubset، لون المقدمة، إلخ.

يُظهر لك جزء الكود التالي كيفية البحث عن نص من جميع الصفحات.

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// فتح المستند
Document pdfDocument = new Document(dataDir + "SearchAndGetTextFromAll.pdf");

// إنشاء كائن TextAbsorber للعثور على جميع حالات عبارة البحث المدخلة
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("text");

// قبول الممتص لجميع الصفحات
pdfDocument.Pages.Accept(textFragmentAbsorber);

// الحصول على أجزاء النص المستخرجة
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// التكرار عبر الأجزاء
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


في حالة الحاجة للبحث عن نص داخل أي صفحة معينة من ملف PDF، يرجى تحديد رقم الصفحة من مجموعة صفحات كائن الوثيقة واستدعاء طريقة Accept ضد تلك الصفحة (كما هو موضح في سطر الكود أدناه).

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// قبول الماص لـصفحة معينة
pdfDocument.Pages[2].Accept(textFragmentAbsorber);
```

## البحث والحصول على مقاطع النص من جميع صفحات مستند PDF

من أجل البحث عن مقاطع النص من جميع الصفحات، تحتاج أولاً إلى الحصول على كائنات TextFragment من الوثيقة.
 TextFragmentAbsorber يسمح لك بالعثور على النص، المطابق لعبارة معينة، من جميع صفحات مستند PDF. من أجل البحث عن النص من المستند بأكمله، تحتاج إلى استدعاء طريقة Accept من مجموعة Pages. تأخذ طريقة Accept كائن TextFragmentAbsorber كمعامل، والذي يعيد مجموعة من كائنات TextFragment. بمجرد الحصول على TextFragmentCollection من المستند، تحتاج إلى التجول عبر هذه المجموعة والحصول على TextSegmentCollection لكل كائن TextFragment. بعد ذلك، يمكنك الحصول على جميع خصائص الكائن الفردي TextSegment. يوضح لك مقتطف الشيفرة التالي كيفية البحث عن مقاطع النص من جميع الصفحات.

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار دليل الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// افتح المستند
Document pdfDocument = new Document(dataDir + "SearchAndGetTextPage.pdf");

// إنشاء كائن TextAbsorber للعثور على جميع الحالات لعبارة البحث المدخلة
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("Figure");
// قبول الممتص لجميع الصفحات
pdfDocument.Pages.Accept(textFragmentAbsorber);
// الحصول على مقاطع النص المستخرجة
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;
// التجول عبر المقاطع
foreach (TextFragment textFragment in textFragmentCollection)
{
    foreach (TextSegment textSegment in textFragment.Segments)
    {
        Console.WriteLine("النص : {0} ", textSegment.Text);
        Console.WriteLine("الموقع : {0} ", textSegment.Position);
        Console.WriteLine("XIndent : {0} ", textSegment.Position.XIndent);
        Console.WriteLine("YIndent : {0} ", textSegment.Position.YIndent);
        Console.WriteLine("الخط - الاسم : {0}", textSegment.TextState.Font.FontName);
        Console.WriteLine("الخط - يمكن الوصول إليه : {0} ", textSegment.TextState.Font.IsAccessible);
        Console.WriteLine("الخط - مدمج : {0} ", textSegment.TextState.Font.IsEmbedded);
        Console.WriteLine("الخط - مجموعة فرعية : {0} ", textSegment.TextState.Font.IsSubset);
        Console.WriteLine("حجم الخط : {0} ", textSegment.TextState.FontSize);
        Console.WriteLine("اللون الأمامي : {0} ", textSegment.TextState.ForegroundColor);
    }
}
```

من أجل البحث والحصول على TextSegments من صفحة معينة من ملف PDF، تحتاج إلى تحديد فهرس الصفحة المحددة عند استدعاء طريقة Accept(..). يرجى إلقاء نظرة على أسطر الكود التالية.

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// قبول المستخلص لكل الصفحات
pdfDocument.Pages[2].Accept(textFragmentAbsorber);
```

## البحث والحصول على النص من جميع الصفحات باستخدام التعبير العادي

TextFragmentAbsorber يساعدك في البحث واسترجاع النص، من جميع الصفحات، بناءً على تعبير عادي.
 أولاً، تحتاج إلى تمرير تعبير عادي إلى منشئ TextFragmentAbsorber كعبارة. بعد ذلك، يجب عليك تعيين خاصية TextSearchOptions لكائن TextFragmentAbsorber. تتطلب هذه الخاصية كائن TextSearchOptions وتحتاج إلى تمرير true كمعامل لمنشئها أثناء إنشاء كائنات جديدة. نظرًا لأنك تريد استرداد النص المطابق من جميع الصفحات، تحتاج إلى استدعاء طريقة Accept على مجموعة Pages. يقوم TextFragmentAbsorber بإرجاع TextFragmentCollection يحتوي على جميع الأجزاء التي تطابق المعايير المحددة بواسطة التعبير العادي. يوضح لك جزء الكود التالي كيفية البحث والحصول على النص من جميع الصفحات بناءً على تعبير عادي.

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// فتح المستند
Document pdfDocument = new Document(dataDir + "SearchRegularExpressionAll.pdf");

// إنشاء كائن TextAbsorber للعثور على جميع العبارات التي تطابق التعبير العادي
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("\\d{4}-\\d{4}"); // مثل 1999-2000

// تعيين خيار بحث النص لتحديد استخدام التعبير العادي
TextSearchOptions textSearchOptions = new TextSearchOptions(true);

textFragmentAbsorber.TextSearchOptions = textSearchOptions;

// قبول الممتص لجميع الصفحات
pdfDocument.Pages.Accept(textFragmentAbsorber);

// الحصول على أجزاء النص المستخرجة
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// التكرار عبر الأجزاء
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

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
TextFragmentAbsorber textFragmentAbsorber;
// من أجل البحث عن تطابق دقيق لكلمة، يمكنك النظر في استخدام التعبير العادي.
textFragmentAbsorber = new TextFragmentAbsorber(@"\bWord\b", new TextSearchOptions(true));

// من أجل البحث عن سلسلة في حالات الأحرف الكبيرة أو الصغيرة، يمكنك النظر في استخدام التعبير العادي.
textFragmentAbsorber = new TextFragmentAbsorber("(?i)Line", new TextSearchOptions(true));

// من أجل البحث عن جميع السلاسل (تحليل جميع السلاسل) داخل مستند PDF، يرجى محاولة استخدام التعبير العادي التالي.
textFragmentAbsorber = new TextFragmentAbsorber(@"[\S]+");

// ابحث عن تطابق سلسلة البحث واحصل على أي شيء بعد السلسلة حتى كسر السطر.
textFragmentAbsorber = new TextFragmentAbsorber(@"(?i)the ((.)*)");

// يرجى استخدام التعبير العادي التالي للعثور على النص الذي يتبع تطابق التعبير العادي.
textFragmentAbsorber = new TextFragmentAbsorber(@"(?<=word).*");

// من أجل البحث عن الروابط/عناوين URL داخل مستند PDF، يرجى محاولة استخدام التعبير العادي التالي.
textFragmentAbsorber = new TextFragmentAbsorber(@"(http|ftp|https):\/\/([\w\-_]+(?:(?:\.[\w\-_]+)+))([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?");
```


## البحث عن نص بناءً على تعبير عادي وإضافة رابط تشعبي

إذا كنت ترغب في إضافة رابط تشعبي على عبارة نصية بناءً على تعبير عادي، أولاً قم بالعثور على جميع العبارات المطابقة لذلك التعبير العادي باستخدام TextFragmentAbsorber وأضف رابطًا تشعبيًا على هذه العبارات.

للعثور على عبارة وإضافة رابط تشعبي عليها:

1. مرر التعبير العادي كمعامل إلى منشئ TextFragmentAbsorber.
2. أنشئ كائن TextSearchOptions الذي يحدد ما إذا كان سيتم استخدام التعبير العادي أم لا.
3. احصل على العبارات المطابقة في TextFragments.
4. قم بالتكرار عبر المطابقات للحصول على أبعادها المستطيلة، وقم بتغيير لون المقدمة إلى الأزرق (اختياري - لجعله يظهر كرابط تشعبي واستخدم طريقة CreateWebLink(..) لفئة PdfContentEditor لإنشاء رابط.
5. احفظ ملف PDF المحدث باستخدام طريقة Save لكائن Document.
يظهر لك مقتطف الشيفرة التالي كيفية البحث عن نص داخل ملف PDF باستخدام تعبير عادي وإضافة روابط تشعبية فوق المطابقات.

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// إنشاء كائن ماص للعثور على جميع الحالات لعبارة البحث المدخلة
TextFragmentAbsorber absorber = new TextFragmentAbsorber("\\d{4}-\\d{4}");
// تمكين البحث بالتعبير العادي
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

// التكرار عبر الشظايا
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


## البحث ورسم مستطيل حول كل جزء نصي

يدعم Aspose.PDF for .NET ميزة البحث والحصول على إحداثيات كل حرف أو أجزاء النص. لذلك من أجل التأكد من الإحداثيات التي يتم إرجاعها لكل حرف، يمكننا النظر في تسليط الضوء (إضافة مستطيل) حول كل حرف.

في حالة فقرة النص، يمكنك التفكير في استخدام بعض التعبيرات العادية لتحديد فاصل الفقرة ورسم مستطيل حولها. يرجى إلقاء نظرة على مقتطف الشيفرة التالي. يحصل مقتطف الشيفرة التالي على إحداثيات كل حرف وينشئ مستطيلًا حول كل حرف.

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// افتح المستند
Document document = new Document(dataDir + "SearchAndGetTextFromAll.pdf");

// إنشاء كائن TextAbsorber للعثور على جميع العبارات التي تطابق التعبير العادي

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


## تسليط الضوء على كل حرف في مستند PDF

{{% alert color="primary" %}}

يمكنك محاولة البحث عن نص في مستند باستخدام Aspose.PDF والحصول على النتائج عبر الإنترنت في هذا [الرابط](https://products.aspose.app/pdf/search)

{{% /alert %}}

يدعم Aspose.PDF لـ .NET ميزة البحث والحصول على إحداثيات كل حرف أو أجزاء النص. لذلك للتأكد من الإحداثيات التي يتم إرجاعها لكل حرف، يمكننا النظر في تسليط الضوء (إضافة مستطيل) حول كل حرف. يوضح مقتطف الشيفرة البرمجية التالي كيفية الحصول على إحداثيات كل حرف وإنشاء مستطيل حول كل حرف.

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار دليل المستندات.
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
// إنشاء كائن TextAbsorber للعثور على كل الكلمات
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(@"[\S]+");
textFragmentAbsorber.TextSearchOptions.IsRegularExpressionUsed = true;
page.Accept(textFragmentAbsorber);
// الحصول على أجزاء النص المستخرجة
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;
// التكرار عبر الأجزاء
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


## إضافة والبحث عن النص المخفي

أحيانًا نريد إضافة نص مخفي في مستند PDF ثم البحث عن النص المخفي واستخدام موقعه لمعالجة لاحقة. لراحتك، توفر Aspose.PDF لـ .NET هذه القدرات. يمكنك إضافة نص مخفي أثناء إنشاء المستند. أيضًا، يمكنك العثور على النص المخفي باستخدام TextFragmentAbsorber. لإضافة نص مخفي، قم بتعيين TextState.Invisible إلى 'true' للنص المضاف. يجد TextFragmentAbsorber جميع النصوص التي تطابق النمط (إذا تم تحديده). هذا هو السلوك الافتراضي الذي لا يمكن تغييره. للتحقق مما إذا كان النص الذي تم العثور عليه غير مرئي بالفعل، يمكن استخدام خاصية TextState.Invisible. يوضح مقتطف الكود أدناه كيفية استخدام هذه الميزة.

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

//إنشاء مستند يحتوي على نص مخفي
Aspose.Pdf.Document doc = new Aspose.Pdf.Document();
Page page = doc.Pages.Add();
TextFragment frag1 = new TextFragment("This is common text.");
TextFragment frag2 = new TextFragment("This is invisible text.");

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
    //قم بعمل شيء ما مع الأجزاء
    Console.WriteLine("Text '{0}' on pos {1} invisibility: {2} ",
    fragment.Text, fragment.Position.ToString(), fragment.TextState.Invisible);
}
doc.Dispose();
```


## البحث عن النص باستخدام .NET Regex

يوفر Aspose.PDF لـ .NET القدرة على البحث في المستندات باستخدام خيار .NET Regex القياسي. يمكن استخدام TextFragmentAbsorber لهذا الغرض كما هو موضح في نموذج الكود أدناه.

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// إنشاء كائن Regex للعثور على جميع الكلمات
System.Text.RegularExpressions.Regex regex = new System.Text.RegularExpressions.Regex(@"[\S]+");

// فتح المستند
Aspose.Pdf.Document document = new Aspose.Pdf.Document(dataDir + "SearchTextRegex.pdf");

// الحصول على صفحة معينة
Page page = document.Pages[1];

// إنشاء كائن TextAbsorber للعثور على جميع الحالات المدخلة في regex
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(regex);
textFragmentAbsorber.TextSearchOptions.IsRegularExpressionUsed = true;

// قبول الممتص للصفحة
page.Accept(textFragmentAbsorber);

// الحصول على أجزاء النص المستخرجة
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// حلقة عبر الأجزاء
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