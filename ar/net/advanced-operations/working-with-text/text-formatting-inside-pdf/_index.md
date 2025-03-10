---
title: تنسيق النص داخل PDF باستخدام C#
linktitle: تنسيق النص داخل PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ar/net/text-formatting-inside-pdf/
description: تعلم كيفية تنسيق النص داخل مستند PDF في .NET باستخدام Aspose.PDF لتعزيز العرض المرئي للمستند.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Text Formatting inside PDF using C#",
    "alternativeHeadline": "Enhance PDF Text Formatting with New C# Features",
    "abstract": "اكتشف قدرات تنسيق النص القوية لـ Aspose.PDF for .NET، مما يتيح لك إضافة مسافات بادئة، وحدود نصية، وتأثيرات تحتية، والمزيد إلى مستندات PDF الخاصة بك. تتيح لك هذه الميزة التحكم الدقيق في جمالية النص وتخطيطه، مما يعزز العرض العام لملفات PDF الخاصة بك. قم بتحسين سير عمل إنشاء PDF الخاص بك مع خيارات تنسيق متعددة مصممة للمطورين",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1642",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
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
    "dateModified": "2024-11-26",
    "description": "تشرح هذه الصفحة كيفية تنسيق النص داخل ملف PDF الخاص بك. هناك إضافة مسافة بادئة، إضافة حدود نصية، إضافة نص تحت، وما إلى ذلك."
}
</script>

تعمل مقتطفات الشيفرة التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/) .

## كيفية إضافة مسافة بادئة إلى PDF

تقدم Aspose.PDF for .NET خاصية SubsequentLinesIndent في فئة [TextFormattingOptions](https://reference.aspose.com/pdf/net/aspose.pdf.text/textformattingoptions). والتي يمكن استخدامها لتحديد المسافة البادئة في سيناريوهات توليد PDF مع TextFragment ومجموعة الفقرات.

يرجى استخدام مقتطف الشيفرة التالي لاستخدام الخاصية:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void TextFormattingInsidePdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();

        string textFragment = string.Concat(Enumerable.Repeat("A quick brown fox jumped over the lazy dog. ", 10));

        Aspose.Pdf.Text.TextFragment text = new Aspose.Pdf.Text.TextFragment(textFragment);

        // Initilize TextFormattingOptions for the text fragment and specify SubsequentLinesIndent value
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

        // Save PDF document
        document.Save(dataDir + "SubsequentIndent_out.pdf");
    }
}
```

## كيفية إضافة حدود نصية

تظهر مقتطفات الشيفرة التالية كيفية إضافة حدود إلى نص باستخدام TextBuilder وتعيين خاصية DrawTextRectangleBorder من TextState:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextBorder()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Get particular page
        var page = document.Pages.Add();
        // Create text fragment
        var textFragment = new Aspose.Pdf.Text.TextFragment("main text");
        textFragment.Position = new Aspose.Pdf.Text.Position(100, 600);
        // Set text properties
        textFragment.TextState.FontSize = 12;
        textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
        textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
        textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;
        // Set StrokingColor property for drawing border (stroking) around text rectangle
        textFragment.TextState.StrokingColor = Aspose.Pdf.Color.DarkRed;
        // Set DrawTextRectangleBorder property value to true
        textFragment.TextState.DrawTextRectangleBorder = true;
        var tb = new Aspose.Pdf.Text.TextBuilder(page);
        tb.AppendText(textFragment);

        // Save PDF document
        document.Save(dataDir + "PDFWithTextBorder_out.pdf");
    }
}
```

## كيفية إضافة نص تحت

تظهر مقتطفات الشيفرة التالية كيفية إضافة نص تحت أثناء إنشاء ملف PDF جديد.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddUnderlineText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add age page to PDF document
        document.Pages.Add();
        // Create TextBuilder for first page
        var tb = new Aspose.Pdf.Text.TextBuilder(document.Pages[1]);
        // TextFragment with sample text
        var fragment = new Aspose.Pdf.Text.TextFragment("Test message");
        // Set the font for TextFragment
        fragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
        fragment.TextState.FontSize = 10;
        // Set the formatting of text as Underline
        fragment.TextState.Underline = true;
        // Specify the position where TextFragment needs to be placed
        fragment.Position = new Aspose.Pdf.Text.Position(10, 800);
        // Append TextFragment to PDF file
        tb.AppendText(fragment);

        // Save PDF document
        document.Save(dataDir + "AddUnderlineText_out.pdf");
    }
}
```

## كيفية إضافة حدود حول النص المضاف

لديك السيطرة على الشكل والمظهر للنص الذي تضيفه. المثال أدناه يوضح كيفية إضافة حدود حول قطعة من النص التي أضفتها عن طريق رسم مستطيل حولها. تعرف على المزيد حول فئة [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) .

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddBorder()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();
    
    // Open PDF document
    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "AddBorder.pdf");
        var lineInfo = new Aspose.Pdf.Facades.LineInfo();
        lineInfo.LineWidth = 2;
        lineInfo.VerticeCoordinate = new float[] { 0, 0, 100, 100, 50, 100 };
        lineInfo.Visibility = true;
        // Add border
        editor.CreatePolygon(lineInfo, 1, new System.Drawing.Rectangle(0, 0, 0, 0), "");

        // Save PDF document
        editor.Save(dataDir + "AddingBorderAroundAddedText_out.pdf");
    }
}
```

## كيفية إضافة فاصل سطر جديد

لا تدعم TextFragment فاصل السطر داخل النص. ومع ذلك، لإضافة نص مع فاصل سطر، يرجى استخدام TextFragment مع TextParagraph:

- استخدم "\r\n" أو Environment.NewLine في TextFragment بدلاً من "\n" المفرد.
- أنشئ كائن TextParagraph. سيضيف نصًا مع تقسيم الأسطر.
- أضف TextFragment مع TextParagraph.AppendLine.
- أضف TextParagraph مع TextBuilder.AppendParagraph.

يرجى استخدام مقتطف الشيفرة أدناه.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddNewLine()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();

        // Initialize new TextFragment with text containing required newline markers
        var textFragment = new Aspose.Pdf.Text.TextFragment("Applicant Name: " + Environment.NewLine + " Joe Smoe");

        // Set text fragment properties if necessary
        textFragment.TextState.FontSize = 12;
        textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
        textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
        textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;

        // Create TextParagraph object
        var par = new Aspose.Pdf.Text.TextParagraph();

        // Add new TextFragment to paragraph
        par.AppendLine(textFragment);

        // Set paragraph position
        par.Position = new Aspose.Pdf.Text.Position(100, 600);

        // Create TextBuilder object
        var textBuilder = new Aspose.Pdf.Text.TextBuilder(page);
        // Add the TextParagraph using TextBuilder
        textBuilder.AppendParagraph(par);

        // Save PDF document
        document.Save(dataDir + "AddNewLineFeed_out.pdf");
    }
}
```

## كيفية إضافة نص مخطط

توفر فئة TextState القدرات لتعيين التنسيق لـ TextFragments الموضوعة داخل مستند PDF. يمكنك استخدام هذه الفئة لتعيين تنسيق النص كعريض، مائل، تحت، وبدءًا من هذا الإصدار، قدمت واجهة برمجة التطبيقات القدرات لوضع علامة على تنسيق النص كمخطط. يرجى تجربة استخدام مقتطف الشيفرة التالي لإضافة TextFragment مع تنسيق مخطط.

يرجى استخدام مقتطف الشيفرة الكامل:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddStrikeoutText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Get particular page
        var page = document.Pages.Add();

        // Create text fragment
        var textFragment = new Aspose.Pdf.Text.TextFragment("main text");
        textFragment.Position = new Aspose.Pdf.Text.Position(100, 600);

        // Set text properties
        textFragment.TextState.FontSize = 12;
        textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
        textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
        textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;
        // Set StrikeOut property
        textFragment.TextState.StrikeOut = true;
        // Mark text as Bold
        textFragment.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;

        // Create TextBuilder object
        var textBuilder = new Aspose.Pdf.Text.TextBuilder(page);
        // Append the text fragment to the PDF page
        textBuilder.AppendText(textFragment);

        // Save PDF document
        document.Save(dataDir + "AddStrikeOutText_out.pdf");
    }
}
```

## تطبيق تظليل متدرج على النص

تم تعزيز تنسيق النص بشكل أكبر في واجهة برمجة التطبيقات لسيناريوهات تحرير النص والآن يمكنك إضافة نص مع مساحة ألوان نمط داخل مستند PDF. تم تعزيز فئة Aspose.Pdf.Color بشكل أكبر من خلال تقديم خاصية جديدة لـ PatternColorSpace، والتي يمكن استخدامها لتحديد ألوان التظليل للنص. تضيف هذه الخاصية الجديدة تظليل متدرج مختلف للنص مثل تظليل محوري، تظليل شعاعي (النوع 3) كما هو موضح في مقتطف الشيفرة التالي:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ApplyGradientShadingToText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "text_sample4.pdf"))
    {
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber("Lorem ipsum");
        document.Pages.Accept(absorber);

        var textFragment = absorber.TextFragments[1];

        // Create new color with pattern colorspace
        textFragment.TextState.ForegroundColor = new Aspose.Pdf.Color()
        {
            PatternColorSpace = new Aspose.Pdf.Drawing.GradientAxialShading(Aspose.Pdf.Color.Red, Aspose.Pdf.Color.Blue)
        };
        textFragment.TextState.Underline = true;

        // Save PDF document
        document.Save(dataDir +"ApplyGradientShadingToText_out.pdf");
    }
}
```

>لتطبيق تدرج شعاعي، يمكنك تعيين خاصية 'PatternColorSpace' تساوي 'Aspose.Pdf.Drawing.GradientRadialShading(startingColor, endingColor)' في مقتطف الشيفرة أعلاه.

## كيفية محاذاة النص مع المحتوى العائم

يدعم Aspose.PDF تعيين محاذاة النص للمحتويات داخل عنصر Floating Box. يمكن استخدام خصائص المحاذاة من مثيل Aspose.Pdf.FloatingBox لتحقيق ذلك كما هو موضح في مقتطف الشيفرة التالي.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AlignTextToFloat()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();

        // Create float box
        Aspose.Pdf.FloatingBox floatBox = new Aspose.Pdf.FloatingBox(100, 100);
        // Set settings to float box
        floatBox.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Bottom;
        floatBox.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
        floatBox.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("FloatingBox_bottom"));
        floatBox.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Blue);
        // Add float box
        page.Paragraphs.Add(floatBox);

        // Create float box
        Aspose.Pdf.FloatingBox floatBox1 = new Aspose.Pdf.FloatingBox(100, 100);
        // Set settings to float box
        floatBox1.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Center;
        floatBox1.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
        floatBox1.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("FloatingBox_center"));
        floatBox1.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Blue);
        // Add float box
        page.Paragraphs.Add(floatBox1);

        // Create float box
        Aspose.Pdf.FloatingBox floatBox2 = new Aspose.Pdf.FloatingBox(100, 100);
        // Set settings to float box
        floatBox2.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
        floatBox2.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
        floatBox2.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("FloatingBox_top"));
        floatBox2.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Blue);
        // Add float box
        page.Paragraphs.Add(floatBox2);

        // Save PDF document
        document.Save(dataDir + "FloatingBox_alignment_review_out.pdf");
    }
}
```

## كيفية إزالة النص المخفي من ملف PDF

أولاً، ينشئ مقتطف الشيفرة كائن Document من ملف. ثم، يضيف TextFragmentAbsorber للعثور على النص وتحريره. ثم يتحقق من النص المخفي ويحذفه. أخيرًا، يحفظ المستند المحدث.

تحتفظ هذه الطريقة بالنص المرئي سليمًا وتحافظ على التخطيط.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveHiddenText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "HiddenText.pdf"))
    {
        var textAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber();

        // This option can be used to prevent other text fragments from moving after hidden text replacement
        textAbsorber.TextReplaceOptions = new Aspose.Pdf.Text.TextReplaceOptions(Aspose.Pdf.Text.TextReplaceOptions.ReplaceAdjustment.None);

        document.Pages.Accept(textAbsorber);

        // Remove hidden text
        foreach (var fragment in textAbsorber.TextFragments)
        {
            if (fragment.TextState.Invisible)
            {
                fragment.Text = "";
            }
        }

        // Save PDF document
        document.Save(dataDir + "HiddenText_out.pdf");
    }
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
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