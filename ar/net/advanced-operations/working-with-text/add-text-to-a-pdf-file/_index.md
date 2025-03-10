---
title: إضافة نص إلى PDF باستخدام C#
linktitle: إضافة نص إلى PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ar/net/add-text-to-pdf-file/
description: تعلم كيفية إضافة نص إلى مستند PDF في .NET باستخدام Aspose.PDF لتعزيز المحتوى وتحرير المستندات.
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
    "headline": "Add Text to PDF using C#",
    "alternativeHeadline": "Add Custom Text to Existing PDFs with C#",
    "abstract": "تتيح ميزة إضافة نص إلى PDF باستخدام C# في Aspose.PDF للمطورين دمج النص والتلاعب به بسلاسة داخل مستندات PDF الموجودة. مع قدرات مثل إضافة أجزاء نصية، واستخدام خطوط OTF مخصصة، وإضافة محتوى HTML، تعزز هذه الوظيفة تنسيق المستندات وعرضها، مما يسهل إنشاء ملفات PDF احترافية ومخصصة برمجياً.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "5625",
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
    "url": "/net/add-text-to-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-text-to-pdf-file/"
    },
    "dateModified": "2024-11-26",
    "description": "تصف هذه المقالة جوانب مختلفة من العمل مع النص في Aspose.PDF. تعلم كيفية إضافة نص إلى PDF، إضافة أجزاء HTML، أو استخدام خطوط OTF مخصصة."
}
</script>

تعمل مقتطفات الشيفرة التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

لإضافة نص إلى ملف PDF موجود:

1. افتح ملف PDF المدخل باستخدام كائن Document.
2. احصل على الصفحة المحددة التي تريد إضافة النص إليها.
3. أنشئ كائن TextFragment مع النص المدخل جنبًا إلى جنب مع خصائص النص الأخرى. يسمح لك كائن TextBuilder الذي تم إنشاؤه من تلك الصفحة المحددة - التي تريد إضافة النص إليها - بإضافة كائن TextFragment إلى الصفحة باستخدام طريقة AppendText.
4. استدعِ طريقة Save لكائن Document واحفظ ملف PDF الناتج.

## إضافة نص

تظهر مقتطفات الشيفرة التالية كيفية إضافة نص في ملف PDF موجود.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddText()
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
        textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray);
        textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Red);

        // Create TextBuilder object
        var textBuilder = new Aspose.Pdf.Text.TextBuilder(page);

        // Append the text fragment to the PDF page
        textBuilder.AppendText(textFragment);

        // Save PDF document
        document.Save(dataDir + "AddText_out.pdf");
    }
}
```

## تحميل الخط من Stream

تظهر مقتطفات الشيفرة التالية كيفية تحميل الخط من كائن Stream عند إضافة نص إلى مستند PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void LoadingFontFromStream()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();
    var fontFile = dataDir + "HPSimplified.ttf";

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "LoadFonts.pdf"))
    {
        // Create text builder object for first page of document
        var textBuilder = new Aspose.Pdf.Text.TextBuilder(document.Pages[1]);
        // Create text fragment with sample string
        var textFragment = new Aspose.Pdf.Text.TextFragment("Hello world");

        if (File.Exists(fontFile))
        {
            // Load the TrueType font into stream object
            using (FileStream fontStream = File.OpenRead(fontFile))
            {
                // Set the font name for text string
                textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.OpenFont(fontStream, Aspose.Pdf.Text.FontTypes.TTF);
                // Specify the position for Text Fragment
                textFragment.Position = new Aspose.Pdf.Text.Position(10, 10);
                // Add the text to TextBuilder so that it can be placed over the PDF file
                textBuilder.AppendText(textFragment);
            }

            // Save PDF document
            document.Save(dataDir + "LoadingFontFromStream_out.pdf");
        }
    }
}
```

## إضافة نص باستخدام TextParagraph

تظهر مقتطفات الشيفرة التالية كيفية إضافة نص في مستند PDF باستخدام فئة [TextParagraph](https://reference.aspose.com/pdf/net/aspose.pdf.text/textparagraph).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextWithTextParagraph()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page to pages collection of Document object
        var page = document.Pages.Add();
        var builder = new Aspose.Pdf.Text.TextBuilder(page);
        // Create text paragraph
        var paragraph = new Aspose.Pdf.Text.TextParagraph();
        // Set subsequent lines indent
        paragraph.SubsequentLinesIndent = 20;
        // Specify the location to add TextParagraph
        paragraph.Rectangle = new Aspose.Pdf.Rectangle(100, 300, 200, 700);
        // Specify word wraping mode
        paragraph.FormattingOptions.WrapMode = Aspose.Pdf.Text.TextFormattingOptions.WordWrapMode.ByWords;
        // Create text fragment
        var fragment = new Aspose.Pdf.Text.TextFragment("the quick brown fox jumps over the lazy dog");
        fragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Times New Roman");
        fragment.TextState.FontSize = 12;
        // Add fragment to paragraph
        paragraph.AppendLine(fragment);
        // Add paragraph
        builder.AppendParagraph(paragraph);

        // Save PDF document
        document.Save(dataDir + "AddTextUsingTextParagraph_out.pdf");
    }
}
```

## إضافة رابط تشعبي إلى TextSegment

قد تتكون صفحة PDF من كائنات TextFragment واحدة أو أكثر، حيث يمكن أن يحتوي كل كائن TextFragment على مثيل واحد أو أكثر من TextSegment. لتعيين رابط تشعبي لـ TextSegment، يمكن استخدام خاصية Hyperlink من فئة [TextSegment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textsegment) مع توفير كائن من مثيل Aspose.Pdf.WebHyperlink. يرجى محاولة استخدام مقتطف الشيفرة التالية لتحقيق هذا المتطلب.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHyperlinkToTextSegment()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Create TextFragment instance
        var fragment = new Aspose.Pdf.Text.TextFragment("Sample Text Fragment");
        // Set horizontal alignment for TextFragment
        fragment.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
        // Create a textsegment with sample text
        var segment = new Aspose.Pdf.Text.TextSegment(" ... Text Segment 1...");
        // Add segment to segments collection of TextFragment
        fragment.Segments.Add(segment);
        // Create a new TextSegment
        segment = new Aspose.Pdf.Text.TextSegment("Link to Google");
        // Add segment to segments collection of TextFragment
        fragment.Segments.Add(segment);
        // Set hyperlink for TextSegment
        segment.Hyperlink = new Aspose.Pdf.WebHyperlink("www.google.com");
        // Set forground color for text segment
        segment.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
        // Set text formatting as italic
        segment.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Italic;
        // Create another TextSegment object
        segment = new Aspose.Pdf.Text.TextSegment("TextSegment without hyperlink");
        // Add segment to segments collection of TextFragment
        fragment.Segments.Add(segment);
        // Add TextFragment to paragraphs collection of page object
        page.Paragraphs.Add(fragment);

        // Save PDF document
        document.Save(dataDir + "AddHyperlinkToTextSegment_out.pdf");
    }
}
```

## استخدام خط OTF

تقدم Aspose.PDF for .NET ميزة استخدام خطوط مخصصة/TrueType أثناء إنشاء/تلاعب محتويات ملف PDF بحيث يتم عرض محتويات الملف باستخدام محتويات غير الخطوط النظامية الافتراضية. بدءًا من إصدار Aspose.PDF for .NET 10.3.0، قدمنا دعمًا لخطوط Open Type.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void UseOTFFont()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Create TextFragment instnace with sample text
        var fragment = new Aspose.Pdf.Text.TextFragment("Sample Text in OTF font");
        // Find font inside system font directory
        // Fragment.TextState.Font = FontRepository.FindFont("HelveticaNeueLT Pro 45 Lt");
        // Or you can even specify the path of OTF font in system directory
        fragment.TextState.Font = Aspose.Pdf.Text.FontRepository.OpenFont(dataDir + "space age.otf");
        // Specify to emend font inside PDF file, so that its displayed properly,
        // Even if specific font is not installed/present over target machine
        fragment.TextState.Font.IsEmbedded = true;
        // Add TextFragment to paragraphs collection of Page instance
        page.Paragraphs.Add(fragment);

        // Save PDF document
        document.Save(dataDir + "OTFFont_out.pdf");
    }
}
```

## إضافة سلسلة HTML باستخدام DOM

تحتوي فئة Aspose.Pdf.Generator.Text على خاصية تسمى IsHtmlTagSupported مما يجعل من الممكن إضافة علامات/محتويات HTML إلى ملفات PDF. يتم عرض المحتوى المضاف في علامات HTML الأصلية بدلاً من الظهور كسلسلة نصية بسيطة. لدعم ميزة مماثلة في نموذج كائن المستند (DOM) الجديد من مساحة Aspose.Pdf، تم تقديم فئة HtmlFragment.

يمكن استخدام مثيل [HtmlFragment](https://reference.aspose.com/pdf/net/aspose.pdf/htmlfragment) لتحديد محتويات HTML التي يجب وضعها داخل ملف PDF. مشابهًا لـ TextFragment، يعد HtmlFragment كائنًا على مستوى الفقرة ويمكن إضافته إلى مجموعة الفقرات لكائن الصفحة. تظهر مقتطفات الشيفرة التالية الخطوات لوضع محتويات HTML داخل ملف PDF باستخدام نهج DOM.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHTMLStringUsingDOM()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add a page to pages collection of PDF file
        var page = document.Pages.Add();
        // Instantiate HtmlFragment with HTML contnets
        var title = new Aspose.Pdf.HtmlFragment("<fontsize=10><b><i>Table</i></b></fontsize>");
        // Set bottom margin information
        title.Margin.Bottom = 10;
        // Set top margin information
        title.Margin.Top = 200;
        // Add HTML Fragment to paragraphs collection of page
        page.Paragraphs.Add(title);

        // Save PDF document
        document.Save(dataDir + "AddHTMLUsingDOM_out.pdf");
    }
}
```

توضح مقتطفات الشيفرة التالية الخطوات لإضافة قوائم مرتبة HTML إلى المستند:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHTMLOrderedListIntoDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Instantiate HtmlFragment object with corresponding HTML fragment 
        var fragment = new Aspose.Pdf.HtmlFragment("`<body style='line-height: 100px;'><ul><li>First</li><li>Second</li><li>Third</li><li>Fourth</li><li>Fifth</li></ul>Text after the list.<br/>Next line<br/>Last line</body>`");
        // Add Page in Pages Collection 
        var page = document.Pages.Add();
        // Add HtmlFragment inside page 
        page.Paragraphs.Add(fragment);

        // Save PDF document
        document.Save(dataDir + "AddHTMLOrderedListIntoDocuments_out.pdf");
    }
}
```

يمكنك أيضًا تعيين تنسيق سلسلة HTML باستخدام كائن TextState كما يلي:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetHTMLStringFormatting()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var fragment = new Aspose.Pdf.HtmlFragment("some text");
        fragment.TextState = new Aspose.Pdf.Text.TextState();
        fragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Calibri");
        // Add Page in Pages Collection 
        var page = document.Pages.Add();
        // Add HtmlFragment inside page 
        page.Paragraphs.Add(fragment);

        // Save PDF document
        document.Save(dataDir + "SetHTMLStringFormatting_out.pdf");
    }
}
```

في حالة إذا قمت بتعيين بعض قيم خصائص النص عبر ترميز HTML ثم قدمت نفس القيم في خصائص TextState، ستقوم هذه القيم بكتابة معلمات HTML بواسطة خصائص مثيل TextState. تظهر مقتطفات الشيفرة التالية السلوك الموصوف.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHTMLUsingDOMAndOverwrite()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add a page to pages collection of PDF file
        var page = document.Pages.Add();
        // Instantiate HtmlFragment with HTML contnets
        var title = new Aspose.Pdf.HtmlFragment("<p style='font-family: Verdana'><b><i>Table contains text</i></b></p>");
        //Font-family from 'Verdana' will be reset to 'Arial'
        title.TextState = new Aspose.Pdf.Text.TextState("Arial");
        title.TextState.FontSize = 20;
        // Set bottom margin information
        title.Margin.Bottom = 10;
        // Set top margin information
        title.Margin.Top = 400;
        // Add HTML Fragment to paragraphs collection of page
        page.Paragraphs.Add(title);
        
        // Save PDF document
        document.Save(dataDir + "AddHTMLUsingDOMAndOverwrite_out.pdf");
    }
}
```

## الحواشي السفلية والملاحظات الختامية (DOM)

تشير الحواشي السفلية إلى الملاحظات في نص ورقتك باستخدام أرقام متسلسلة. يتم إزاحة الملاحظة الفعلية ويمكن أن تحدث كحاشية في أسفل الصفحة.

### إضافة حاشية سفلية

في نظام الإشارة إلى الحواشي السفلية، حدد إشارة مرجعية عن طريق:

- ضع رقمًا صغيرًا فوق سطر النص مباشرة بعد المادة المصدر. يُطلق على هذا الرقم معرف الملاحظة. يجلس فوق سطر النص قليلاً.
- ضع نفس الرقم، متبوعًا بإشارة مرجعية لمصدرك، في أسفل الصفحة. يجب أن تكون الحواشي السفلية عددية وتاريخية: الإشارة المرجعية الأولى هي 1، والثانية هي 2، وهكذا.

تتمثل ميزة الحواشي السفلية في أن القارئ يمكنه ببساطة إلقاء نظرة على أسفل الصفحة لاكتشاف مصدر الإشارة المرجعية التي تهمه.

يرجى اتباع الخطوات المحددة أدناه لإنشاء حاشية سفلية:

- أنشئ مثيل Document.
- أنشئ كائن Page.
- أنشئ كائن TextFragment.
- أنشئ مثيل Note ومرر قيمته إلى خاصية TextFragment.FootNote.
- أضف TextFragment إلى مجموعة الفقرات لمثيل الصفحة.

### نمط خط مخصص للحاشية السفلية

توضح المثال التالي كيفية إضافة الحواشي السفلية إلى أسفل صفحة PDF وتحديد نمط خط مخصص.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CustomLineStyleForFootNote()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Create GraphInfo object
        var graph = new Aspose.Pdf.GraphInfo();
        // Set line width as 2
        graph.LineWidth = 2;
        // Set the color for graph object
        graph.Color = Aspose.Pdf.Color.Red;
        // Set dash array value as 3
        graph.DashArray = new int[] { 3 };
        // Set dash phase value as 1
        graph.DashPhase = 1;
        // Set footnote line style for page as graph
        page.NoteLineStyle = graph;
        // Create TextFragment instance
        var text = new Aspose.Pdf.Text.TextFragment("Hello World");
        // Set FootNote value for TextFragment
        text.FootNote = new Aspose.Pdf.Note("foot note for test text 1");
        // Add TextFragment to paragraphs collection of first page of document
        page.Paragraphs.Add(text);
        // Create second TextFragment
        text = new Aspose.Pdf.Text.TextFragment("Aspose.PDF for .NET");
        // Set FootNote for second text fragment
        text.FootNote = new Aspose.Pdf.Note("foot note for test text 2");
        // Add second text fragment to paragraphs collection of PDF file
        page.Paragraphs.Add(text);

        // Save PDF document
        document.Save(dataDir + "CustomLineStyleForFootNote_out.pdf");
    }
}
```

يمكننا تعيين تنسيق ملصق الحاشية السفلية (معرف الملاحظة) باستخدام كائن TextState كما يلي:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FormattingUsingTextStateObject()
{
    var text = new Aspose.Pdf.Text.TextFragment("test text 1");
    text.FootNote = new Aspose.Pdf.Note("foot note for test text 1");
    text.FootNote.Text = "21";
    text.FootNote.TextState = new Aspose.Pdf.Text.TextState();
    text.FootNote.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
    text.FootNote.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Italic;
}
```

### تخصيص ملصق الحاشية السفلية

بشكل افتراضي، يكون رقم الحاشية السفلية متزايدًا بدءًا من 1. ومع ذلك، قد يكون لدينا متطلب لتعيين ملصق حاشية سفلية مخصص. لتحقيق هذا المتطلب، يرجى محاولة استخدام مقتطف الشيفرة التالية

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CustomizeFootNoteLabel()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Create GraphInfo object
        var graph = new Aspose.Pdf.GraphInfo();
        // Set line width as 2
        graph.LineWidth = 2;
        // Set the color for graph object
        graph.Color = Aspose.Pdf.Color.Red;
        // Set dash array value as 3
        graph.DashArray = new int[] { 3 };
        // Set dash phase value as 1
        graph.DashPhase = 1;
        // Set footnote line style for page as graph
        page.NoteLineStyle = graph;
        // Create TextFragment instance
        var text = new Aspose.Pdf.Text.TextFragment("Hello World");
        // Set FootNote value for TextFragment
        text.FootNote = new Aspose.Pdf.Note("foot note for test text 1");
        // Specify custom label for FootNote
        text.FootNote.Text = " Aspose(2015)";
        // Add TextFragment to paragraphs collection of first page of document
        page.Paragraphs.Add(text);

        // Save PDF document
        document.Save(dataDir + "CustomizeFootNoteLabel_out.pdf");
    }
}
```

## إضافة صورة وجدول إلى الحاشية السفلية

في الإصدارات السابقة، تم توفير دعم الحاشية السفلية ولكن كان ذلك ينطبق فقط على كائن TextFragment. ومع ذلك، بدءًا من إصدار Aspose.PDF for .NET 10.7.0، يمكنك أيضًا إضافة حاشية سفلية إلى كائنات أخرى داخل مستند PDF مثل الجدول، والخلايا، إلخ. توضح مقتطفات الشيفرة التالية الخطوات لإضافة حاشية سفلية إلى كائن TextFragment ثم إضافة كائن صورة وجدول إلى مجموعة الفقرات لقسم الحاشية السفلية.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageAndTable()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();
        var text = new Aspose.Pdf.Text.TextFragment("some text");
        page.Paragraphs.Add(text);

        text.FootNote = new Aspose.Pdf.Note();
        // Create image
        Aspose.Pdf.Image image = new Aspose.Pdf.Image();
        image.File = dataDir + "aspose-logo.jpg";
        image.FixHeight = 20;
        text.FootNote.Paragraphs.Add(image);

        var footNote = new Aspose.Pdf.Text.TextFragment("footnote text");
        footNote.TextState.FontSize = 20;
        footNote.IsInLineParagraph = true;
        text.FootNote.Paragraphs.Add(footNote);

        var table = new Aspose.Pdf.Table();
        table.Rows.Add().Cells.Add().Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Row 1 Cell 1"));
        text.FootNote.Paragraphs.Add(table);

        // Save PDF document
        document.Save(dataDir + "AddImageAndTable_out.pdf");
    }
}
```

## كيفية إنشاء ملاحظات ختامية

الملاحظة الختامية هي إشارة مصدر تشير إلى القراء إلى مكان محدد في نهاية الورقة حيث يمكنهم معرفة مصدر المعلومات أو الكلمات المقتبسة أو المذكورة في الورقة. عند استخدام الملاحظات الختامية، تتبع جملتك المقتبسة أو المعاد صياغتها أو المواد الملخصة برقم مرتفع.

يوضح المثال التالي كيفية إضافة ملاحظة ختامية في صفحة PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateEndNotes()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Create TextFragment instance
        var text = new Aspose.Pdf.Text.TextFragment("Hello World");
        // Set FootNote value for TextFragment
        text.EndNote = new Aspose.Pdf.Note("sample End note");
        // Specify custom label for FootNote
        text.EndNote.Text = " Aspose(2015)";
        // Add TextFragment to paragraphs collection of first page of document
        page.Paragraphs.Add(text);

        // Save PDF document
        document.Save(dataDir + "CreateEndNotes_out.pdf");
    }
}
```

## النص والصورة كفقرة داخل السطر

التخطيط الافتراضي لملف PDF هو تخطيط تدفق (من أعلى اليسار إلى أسفل اليمين). لذلك، يتم إضافة كل عنصر جديد يتم إضافته إلى ملف PDF في تدفق أسفل اليمين. ومع ذلك، قد يكون لدينا متطلب لعرض عناصر الصفحة المختلفة مثل الصورة والنص على نفس المستوى (واحد بعد الآخر). يمكن أن تكون إحدى الطرق هي إنشاء مثيل جدول وإضافة كلا العنصرين إلى كائنات الخلايا الفردية. ومع ذلك، يمكن أن تكون طريقة أخرى هي الفقرة داخل السطر. من خلال تعيين خاصية IsInLineParagraph للصورة والنص كصحيح، ستظهر هذه الفقرات كفقرة داخل السطر بالنسبة لعناصر الصفحة الأخرى.

تظهر مقتطفات الشيفرة التالية كيفية إضافة نص وصورة كفقرات داخل السطر في ملف PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void TextAndImageAsParagraph()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page to pages collection of Document instance
        var page = document.Pages.Add();
        // Create TextFragmnet
        var text = new Aspose.Pdf.Text.TextFragment("Hello World.. ");
        // Add text fragment to paragraphs collection of Page object
        page.Paragraphs.Add(text);
        // Create an image instance
        var image = new Aspose.Pdf.Image();
        // Set image as inline paragraph so that it appears right after
        // The previous paragraph object (TextFragment)
        image.IsInLineParagraph = true;
        // Specify image file path
        image.File = dataDir + "aspose-logo.jpg";
        // Set image Height (optional)
        image.FixHeight = 30;
        // Set Image Width (optional)
        image.FixWidth = 100;
        // Add image to paragraphs collection of page object
        page.Paragraphs.Add(image);
        // Re-initialize TextFragment object with different contents
        text = new Aspose.Pdf.Text.TextFragment(" Hello Again..");
        // Set TextFragment as inline paragraph
        text.IsInLineParagraph = true;
        // Add newly created TextFragment to paragraphs collection of page
        page.Paragraphs.Add(text);

        // Save PDF document
        document.Save(dataDir + "TextAndImageAsParagraph_out.pdf");
    }
}
```

## تحديد تباعد الأحرف عند إضافة نص

يمكن إضافة نص داخل مجموعة الفقرات لملفات PDF باستخدام مثيل TextFragment أو باستخدام كائن TextParagraph وحتى يمكنك ختم النص داخل PDF باستخدام فئة TextStamp. عند إضافة النص، قد يكون لدينا متطلب لتحديد تباعد الأحرف لكائنات النص. لتحقيق هذا المتطلب، تم تقديم خاصية جديدة تسمى خاصية CharacterSpacing. يرجى إلقاء نظرة على النهج التالية لتلبية هذا المتطلب.

تظهر النهج التالية الخطوات لتحديد تباعد الأحرف عند إضافة نص داخل مستند PDF.

### باستخدام TextBuilder وTextFragment

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CharacterSpacingUsingTextBuilderAndFragment()
{            
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page to pages collection of Document
        document.Pages.Add();
        // Create TextBuilder instance
        var builder = new Aspose.Pdf.Text.TextBuilder(document.Pages[1]);
        // Create text fragment instance with sample contents
        var wideFragment = new Aspose.Pdf.Text.TextFragment("Text with increased character spacing");
        wideFragment.TextState.ApplyChangesFrom(new Aspose.Pdf.Text.TextState("Arial", 12));
        // Specify character spacing for TextFragment
        wideFragment.TextState.CharacterSpacing = 2.0f;
        // Specify the position of TextFragment
        wideFragment.Position = new Aspose.Pdf.Text.Position(100, 650);
        // Append TextFragment to TextBuilder instance
        builder.AppendText(wideFragment);

        // Save PDF document
        document.Save(dataDir + "CharacterSpacingUsingTextBuilderAndFragment_out.pdf");
    }
}
```

### باستخدام TextParagraph

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CharacterSpacingUsingTextBuilderAndParagraph()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page to pages collection of Document
        var page = document.Pages.Add();
        // Create TextBuilder instance
        var builder = new Aspose.Pdf.Text.TextBuilder(page);
        // Instantiate TextParagraph instance
        var paragraph = new Aspose.Pdf.Text.TextParagraph();
        // Create TextState instance to specify font name and size
        var state = new Aspose.Pdf.Text.TextState("Arial", 12);
        // Specify the character spacing
        state.CharacterSpacing = 1.5f;
        // Append text to TextParagraph object
        paragraph.AppendLine("This is paragraph with character spacing", state);
        // Specify the position for TextParagraph
        paragraph.Position = new Aspose.Pdf.Text.Position(100, 550);
        // Append TextParagraph to TextBuilder instance
        builder.AppendParagraph(paragraph);

        // Save PDF document
        document.Save(dataDir + "CharacterSpacingUsingTextBuilderAndParagraph_out.pdf");
    }
}
```

### باستخدام TextStamp

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CharacterSpacingUsingTextStamp()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page to pages collection of Document
        var page = document.Pages.Add();
        // Instantiate TextStamp instance with sample text
        var stamp = new Aspose.Pdf.TextStamp("This is text stamp with character spacing");
        // Specify font name for Stamp object
        stamp.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
        // Specify Font size for TextStamp
        stamp.TextState.FontSize = 12;
        // Specify character specing as 1f
        stamp.TextState.CharacterSpacing = 1f;
        // Set the XIndent for Stamp
        stamp.XIndent = 100;
        // Set the YIndent for Stamp
        stamp.YIndent = 500;
        // Add textual stamp to page instance
        stamp.Put(page);

        // Save PDF document
        document.Save(dataDir + "CharacterSpacingUsingTextStamp_out.pdf");
    }
}
```

## إنشاء مستند PDF متعدد الأعمدة

في المجلات والصحف، نرى غالبًا أن الأخبار تُعرض في أعمدة متعددة على الصفحات الفردية بدلاً من الكتب حيث يتم طباعة فقرات النص في الغالب على الصفحات بالكامل من اليسار إلى اليمين. تسمح العديد من تطبيقات معالجة المستندات مثل Microsoft Word وAdobe Acrobat Writer للمستخدمين بإنشاء أعمدة متعددة على صفحة واحدة ثم إضافة بيانات إليها.

تقدم [Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) أيضًا ميزة إنشاء أعمدة متعددة داخل صفحات مستندات PDF. لإنشاء ملف PDF متعدد الأعمدة، يمكننا استخدام فئة Aspose.Pdf.FloatingBox حيث توفر خاصية ColumnInfo.ColumnCount لتحديد عدد الأعمدة داخل FloatingBox ويمكننا أيضًا تحديد المسافة بين الأعمدة وعرض الأعمدة باستخدام خصائص ColumnInfo.ColumnSpacing وColumnInfo.ColumnWidths وفقًا لذلك. يرجى ملاحظة أن FloatingBox هو عنصر داخل نموذج كائن المستند ويمكن أن يكون له موضع قديم مقارنة بالموضع النسبي (مثل النص، الرسم، الصورة، إلخ).

تشير مسافة العمود إلى المسافة بين الأعمدة والمسافة الافتراضية بين الأعمدة هي 1.25 سم. إذا لم يتم تحديد عرض العمود، فإن [Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) يحسب العرض لكل عمود تلقائيًا وفقًا لحجم الصفحة ومسافة العمود.

يوجد مثال أدناه يوضح إنشاء عمودين مع كائنات الرسوم (خط) ويتم إضافتهما إلى مجموعة الفقرات لـ FloatingBox، والتي تتم إضافتها بعد ذلك إلى مجموعة الفقرات لمثيل الصفحة.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateMultiColumnPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Specify the left margin info for the PDF file
        document.PageInfo.Margin.Left = 40;
        // Specify the Right margin info for the PDF file
        document.PageInfo.Margin.Right = 40;
        var page = document.Pages.Add();

        var graph1 = new Aspose.Pdf.Drawing.Graph(500, 2);
        // Add the line to paraphraphs collection of section object
        page.Paragraphs.Add(graph1);

        // Specify the coordinates for the line
        float[] posArr = new float[] { 1, 2, 500, 2 };
        var line1 = new Aspose.Pdf.Drawing.Line(posArr);
        graph1.Shapes.Add(line1);
        // Create string variables with text containing html tags
        string s = "<font face=\"Times New Roman\" size=4>" +

        "<strong> How to Steer Clear of money scams</<strong> "
        + "</font>";
        // Create text paragraphs containing HTML text
        var heading_text = new Aspose.Pdf.HtmlFragment(s);
        page.Paragraphs.Add(heading_text);

        var box = new Aspose.Pdf.FloatingBox();
        // Add four columns in the section
        box.ColumnInfo.ColumnCount = 2;
        // Set the spacing between the columns
        box.ColumnInfo.ColumnSpacing = "5";

        box.ColumnInfo.ColumnWidths = "105 105";
        var text1 = new Aspose.Pdf.Text.TextFragment("By A Googler (The Official Google Blog)");
        text1.TextState.FontSize = 8;
        text1.TextState.LineSpacing = 2;
        box.Paragraphs.Add(text1);
        text1.TextState.FontSize = 10;

        text1.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Italic;
        // Create a graphs object to draw a line
        var graph2 = new Aspose.Pdf.Drawing.Graph(50, 10);
        // Specify the coordinates for the line
        float[] posArr2 = new float[] { 1, 10, 100, 10 };
        var line2 = new Aspose.Pdf.Drawing.Line(posArr2);
        graph2.Shapes.Add(line2);

        // Add the line to paragraphs collection of section object
        box.Paragraphs.Add(graph2);

        var text2 = new Aspose.Pdf.Text.TextFragment(@"Sed augue tortor, sodales id, luctus et, pulvinar ut, eros. Suspendisse vel dolor. Sed quam. Curabitur ut massa vitae eros euismod aliquam. Pellentesque sit amet elit. Vestibulum interdum pellentesque augue. Cras mollis arcu sit amet purus. Donec augue. Nam mollis tortor a elit. Nulla viverra nisl vel mauris. Vivamus sapien. nascetur ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et,nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. Praesent porttitor turpis eleifend ante. Morbi sodales.nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. Praesent porttitor turpis eleifend ante. Morbi sodales.");
        box.Paragraphs.Add(text2);

        page.Paragraphs.Add(box);

        // Save PDF document
        document.Save(dataDir + "CreateMultiColumnPdf_out.pdf");
    }
}
```

## العمل مع نقاط توقف التبويب المخصصة

نقطة توقف التبويب هي نقطة توقف للتبويب. في معالجة الكلمات، يحتوي كل سطر على عدد من نقاط توقف التبويب الموضوعة على فترات منتظمة (على سبيل المثال، كل نصف بوصة). ومع ذلك، يمكن تغييرها، حيث تسمح معظم معالجات الكلمات لك بتعيين نقاط توقف التبويب في أي مكان تريده. عند الضغط على مفتاح التبويب، يقفز المؤشر أو نقطة الإدراج إلى نقطة التوقف التالية، والتي تكون غير مرئية. على الرغم من أن نقاط التوقف لا توجد في ملف النص، إلا أن معالج الكلمات يتتبعها حتى يتمكن من الاستجابة بشكل صحيح لمفتاح التبويب.

تسمح [Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) للمطورين باستخدام نقاط توقف التبويب المخصصة في مستندات PDF. تُستخدم فئة Aspose.Pdf.Text.TabStop لتعيين نقاط توقف TAB مخصصة في فئة [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment).

تقدم [Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) أيضًا بعض أنواع قادة التبويب المعرفة مسبقًا كعداد يسمى TabLeaderType، حيث يتم إعطاء القيم المعرفة مسبقًا ووصفها أدناه:

|**نوع قائد التبويب**|**الوصف**|
| :- | :- |
|لا شيء|لا يوجد قائد تبويب|
|صلب|قائد تبويب صلب|
|شرط|قائد تبويب شرطي|
|نقطة|قائد تبويب نقطي|

إليك مثال حول كيفية تعيين نقاط توقف TAB مخصصة.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CustomTabStops()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();

        var tabStops = new Aspose.Pdf.Text.TabStops();
        var tabStop1 = tabStops.Add(100);
        tabStop1.AlignmentType = Aspose.Pdf.Text.TabAlignmentType.Right;
        tabStop1.LeaderType = Aspose.Pdf.Text.TabLeaderType.Solid;

        var tabStop2 = tabStops.Add(200);
        tabStop2.AlignmentType = Aspose.Pdf.Text.TabAlignmentType.Center;
        tabStop2.LeaderType = Aspose.Pdf.Text.TabLeaderType.Dash;

        var tabStop3 = tabStops.Add(300);
        tabStop3.AlignmentType = Aspose.Pdf.Text.TabAlignmentType.Left;
        tabStop3.LeaderType = Aspose.Pdf.Text.TabLeaderType.Dot;

        var header = new Aspose.Pdf.Text.TextFragment("This is a example of forming table with TAB stops", tabStops);
        var text0 = new Aspose.Pdf.Text.TextFragment("#$TABHead1 #$TABHead2 #$TABHead3", tabStops);
        var text1 = new Aspose.Pdf.Text.TextFragment("#$TABdata11 #$TABdata12 #$TABdata13", tabStops);
        var text2 = new Aspose.Pdf.Text.TextFragment("#$TABdata21 ", tabStops);
        text2.Segments.Add(new Aspose.Pdf.Text.TextSegment("#$TAB"));
        text2.Segments.Add(new Aspose.Pdf.Text.TextSegment("data22 "));
        text2.Segments.Add(new Aspose.Pdf.Text.TextSegment("#$TAB"));
        text2.Segments.Add(new Aspose.Pdf.Text.TextSegment("data23"));

        // Add text fragments to page
        page.Paragraphs.Add(header);
        page.Paragraphs.Add(text0);
        page.Paragraphs.Add(text1);
        page.Paragraphs.Add(text2);

        // Save PDF document
        document.Save(dataDir + "CustomTabStops_out.pdf");
    }
}
```

## كيفية إضافة نص شفاف في PDF

يحتوي ملف PDF على كائنات صورة، نص، رسم، مرفقات، تعليقات توضيحية وعند إنشاء TextFragment، يمكنك تعيين معلومات لون المقدمة والخلفية بالإضافة إلى تنسيق النص. تدعم Aspose.PDF for .NET ميزة إضافة نص مع قناة لون ألفا. توضح مقتطفات الشيفرة التالية كيفية إضافة نص بلون شفاف.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTransparentText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Create page to pages collection of PDF file
        var page = document.Pages.Add();

        // Create Graph object
        var canvas = new Aspose.Pdf.Drawing.Graph(100, 400);
        // Create rectangle instance with certain dimensions
        var rect = new Aspose.Pdf.Drawing.Rectangle(100, 100, 400, 400);
        // Create color object from Alpha color channel
        rect.GraphInfo.FillColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.FromArgb(128, System.Drawing.Color.FromArgb(12957183)));
        // Add rectanlge to shapes collection of Graph object
        canvas.Shapes.Add(rect);
        // Add graph object to paragraphs collection of page object
        page.Paragraphs.Add(canvas);
        // Set value to not change position for graph object
        canvas.IsChangePosition = false;

        // Create TextFragment instance with sample value
        var text = new Aspose.Pdf.Text.TextFragment("transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text ");
        // Create color object from Alpha channel
        Aspose.Pdf.Color color = Aspose.Pdf.Color.FromArgb(30, 0, 255, 0);
        // Set color information for text instance
        text.TextState.ForegroundColor = color;
        // Add text to paragraphs collection of page instance
        page.Paragraphs.Add(text);

        // Save PDF document
        document.Save(dataDir + "AddTransparentText_out.pdf");
    }
}
```

## تحديد تباعد الأسطر للخطوط

يمتلك كل خط مربعًا مجردًا، ارتفاعه هو المسافة المقصودة بين الأسطر من النوع في نفس حجم النوع. يُطلق على هذا المربع اسم مربع em وهو شبكة التصميم التي يتم تعريف خطوطها. تحتوي العديد من حروف الخط المدخل على نقاط تقع خارج حدود مربع em الخاص بالخط، لذا من أجل عرض الخط بشكل صحيح، يلزم استخدام إعداد خاص. يحتوي كائن TextFragment على مجموعة من خيارات تنسيق النص التي يمكن الوصول إليها عبر خصائص TextState.FormattingOptions. آخر خاصية في هذا المسار هي خاصية من نوع Aspose.Pdf.Text.TextFormattingOptions. تحتوي هذه الفئة على تعداد [LineSpacingMode](https://reference.aspose.com/pdf/net/aspose.pdf.text.textformattingoptions/linespacingmode) المصمم لخطوط معينة مثل الخط المدخل "HPSimplified.ttf". أيضًا تحتوي فئة [Aspose.Pdf.Text.TextFormattingOptions](https://reference.aspose.com/pdf/net/aspose.pdf.text/textformattingoptions) على خاصية [LineSpacing](https://reference.aspose.com/pdf/net/aspose.pdf.text/textformattingoptions/properties/linespacing) من نوع LineSpacingMode. تحتاج فقط إلى تعيين LineSpacing إلى LineSpacingMode.FullSize. سيكون مقتطف الشيفرة للحصول على عرض خط بشكل صحيح كما يلي:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SpecifyLineSpacing()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    string fontFile = dataDir + "HPSimplified.TTF";

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        //Create TextFormattingOptions with LineSpacingMode.FullSize
        var formattingOptions = new Aspose.Pdf.Text.TextFormattingOptions();
        formattingOptions.LineSpacing = Aspose.Pdf.Text.TextFormattingOptions.LineSpacingMode.FullSize;

        // Create text builder object for first page of document
        //TextBuilder textBuilder = new TextBuilder(document.Pages[1]);
        // Create text fragment with sample string
        var textFragment = new Aspose.Pdf.Text.TextFragment("Hello world");

        if (fontFile != "")
        {
            // Load the TrueType font into stream object
            using (FileStream fontStream = File.OpenRead(fontFile))
            {
                // Set the font name for text string
                textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.OpenFont(fontStream, Aspose.Pdf.Text.FontTypes.TTF);
                // Specify the position for Text Fragment
                textFragment.Position = new Aspose.Pdf.Text.Position(100, 600);
                //Set TextFormattingOptions of current fragment to predefined(which points to LineSpacingMode.FullSize)
                textFragment.TextState.FormattingOptions = formattingOptions;
                // Add the text to TextBuilder so that it can be placed over the PDF file
                //textBuilder.AppendText(textFragment);
                var page = document.Pages.Add();
                page.Paragraphs.Add(textFragment);
            }

            // Save PDF document
            document.Save(dataDir + "SpecifyLineSpacing_out.pdf");
        }
    }
}
```

## الحصول على عرض النص ديناميكيًا

في بعض الأحيان، يكون من الضروري الحصول على عرض النص ديناميكيًا. تتضمن Aspose.PDF for .NET طريقتين لقياس عرض السلسلة. يمكنك استدعاء طريقة [MeasureString](https://reference.aspose.com/pdf/net/aspose.pdf.text/font/methods/measurestring) من فئات Aspose.Pdf.Text.Font أو Aspose.Pdf.Text.TextState (أو كليهما). توضح مقتطفات الشيفرة أدناه كيفية استخدام هذه الوظيفة.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetTextWidthDynamically()
{            
    var font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
    var textState = new Aspose.Pdf.Text.TextState();
    textState.Font = font;
    textState.FontSize = 14;

    if (Math.Abs(font.MeasureString("A", 14) - 9.337) > 0.001)
    {
        Console.WriteLine("Unexpected font string measure!");
    }

    if (Math.Abs(textState.MeasureString("z") - 7.0) > 0.001)
    {
        Console.WriteLine("Unexpected font string measure!");
    }

    for (char c = 'A'; c <= 'z'; c++)
    {
        double fontMeasure = font.MeasureString(c.ToString(), 14);
        double textStateMeasure = textState.MeasureString(c.ToString());

        if (Math.Abs(fontMeasure - textStateMeasure) > 0.001)
        {
            Console.WriteLine("Font and state string measuring doesn't match!");
        }
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