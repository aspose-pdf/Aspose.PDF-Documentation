---
title: استبدال النص في PDF
linktitle: استبدال النص في PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ar/net/replace-text-in-pdf/
description: تعرف على المزيد حول الطرق المختلفة لاستبدال وإزالة النص من مكتبة Aspose.PDF for .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Replace Text in PDF",
    "alternativeHeadline": "Efficiently Modify Text Across PDF Pages with Ease",
    "abstract": "تتيح ميزة استبدال النص في PDF في Aspose.PDF for .NET للمستخدمين العثور على النص واستبداله بكفاءة عبر مستند PDF كامل أو ضمن مناطق صفحات محددة. تدعم هذه الميزة قدرات متقدمة، بما في ذلك استبدال النص بناءً على التعبيرات العادية، وإعادة ترتيب محتوى الصفحة تلقائيًا بعد الاستبدالات، والقدرة على إزالة الخطوط غير المستخدمة، مما يعزز تجربة تحرير المستندات.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "2744",
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
    "url": "/net/replace-text-in-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/replace-text-in-pdf/"
    },
    "dateModified": "2024-11-26",
    "description": "تعرف على المزيد حول الطرق المختلفة لاستبدال وإزالة النص من مكتبة Aspose.PDF for .NET."
}
</script>

تعمل مقتطفات الكود التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/) .

## استبدال النص في جميع صفحات مستند PDF

{{% alert color="primary" %}}

يمكنك محاولة العثور على النص واستبداله في المستند باستخدام Aspose.PDF والحصول على النتائج عبر الإنترنت في هذا [الرابط](https://products.aspose.app/pdf/redaction)

{{% /alert %}}

لكي تستبدل النص في جميع صفحات مستند PDF، تحتاج أولاً إلى استخدام TextFragmentAbsorber للعثور على العبارة المحددة التي تريد استبدالها. بعد ذلك، تحتاج إلى المرور عبر جميع TextFragments لاستبدال النص وتغيير أي سمات أخرى. بمجرد الانتهاء من ذلك، تحتاج فقط إلى حفظ ملف PDF الناتج باستخدام طريقة Save لكائن Document. يوضح مقتطف الكود التالي كيفية استبدال النص في جميع صفحات مستند PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceTextInAllPages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ReplaceTextAll.pdf"))
    {
        // Create TextAbsorber object to find all instances of the input search phrase
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber("text");

        // Accept the absorber for all the pages
        document.Pages.Accept(absorber);

        // Get the extracted text fragments
        var textFragmentCollection = absorber.TextFragments;

        // Loop through the fragments
        foreach (var textFragment in textFragmentCollection)
        {
            // Update text and other properties
            textFragment.Text = "TEXT";
            textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Verdana");
            textFragment.TextState.FontSize = 22;
            textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Blue);
            textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
        }

        // Save PDF document
        document.Save(dataDir + "ReplaceTextInAllPages_out.pdf");
    }
}
```

## استبدال النص في منطقة صفحة معينة

لكي تستبدل النص في منطقة صفحة معينة، أولاً، نحتاج إلى إنشاء كائن TextFragmentAbsorber، وتحديد منطقة الصفحة باستخدام خاصية TextSearchOptions.Rectangle ثم التكرار عبر جميع TextFragments لاستبدال النص. بمجرد الانتهاء من هذه العمليات، نحتاج فقط إلى حفظ ملف PDF الناتج باستخدام طريقة Save لكائن Document. يوضح مقتطف الكود التالي كيفية استبدال النص في جميع صفحات مستند PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceTextInParticularPageRegion()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "programaticallyproducedpdf.pdf"))
    {
        // instantiate TextFragment Absorber object
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber();

        // search text within page bound
        absorber.TextSearchOptions.LimitToPageBounds = true;

        // specify the page region for TextSearch Options
        absorber.TextSearchOptions.Rectangle = new Aspose.Pdf.Rectangle(100, 100, 200, 200);

        // search text from first page of PDF file
        document.Pages[1].Accept(absorber);

        // iterate through individual TextFragment
        foreach (var textFragment in absorber.TextFragments)
        {
            // update text to blank characters
            textFragment.Text = "";
        }

        // Save PDF document
        document.Save(dataDir + "ReplaceTextInParticularPageRegion_out.pdf");
    }
}
```

## استبدال النص بناءً على تعبير عادي

إذا كنت ترغب في استبدال بعض العبارات بناءً على تعبير عادي، تحتاج أولاً إلى العثور على جميع العبارات التي تطابق ذلك التعبير العادي المحدد باستخدام TextFragmentAbsorber. سيتعين عليك تمرير التعبير العادي كمعامل إلى مُنشئ TextFragmentAbsorber. تحتاج أيضًا إلى إنشاء كائن TextSearchOptions الذي يحدد ما إذا كان يتم استخدام التعبير العادي أم لا. بمجرد الحصول على العبارات المطابقة في TextFragments، تحتاج إلى التكرار عبر جميعها وتحديثها حسب الحاجة. أخيرًا، تحتاج إلى حفظ ملف PDF المحدث باستخدام طريقة Save لكائن Document. يوضح مقتطف الكود التالي كيفية استبدال النص بناءً على تعبير عادي.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceTextBasedOnARegularExpression()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchRegularExpressionPage.pdf"))
    {

        // Create TextAbsorber object to find all the phrases matching the regular expression
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber("\\d{4}-\\d{4}"); // Like 1999-2000

        // Set text search option to specify regular expression usage
        absorber.TextSearchOptions = new Aspose.Pdf.Text.TextSearchOptions(true);

        // Accept the absorber for a single page
        document.Pages[1].Accept(absorber);

        // Get the extracted text fragments
        var collection = absorber.TextFragments;

        // Loop through the fragments
        foreach (var textFragment in collection)
        {
            // Update text and other properties
            textFragment.Text = "New Phrase";
            // Set to an instance of an object.
            textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Verdana");
            textFragment.TextState.FontSize = 22;
            textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Blue);
            textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
        }

        // Save PDF document
        document.Save(dataDir + "ReplaceTextonRegularExpression_out.pdf");
    }
}
```

## استبدال الخطوط في ملف PDF موجود

تدعم Aspose.PDF for .NET القدرة على استبدال النص في مستند PDF. ومع ذلك، في بعض الأحيان لديك متطلبات لاستبدال الخط المستخدم داخل مستند PDF فقط. لذا بدلاً من استبدال النص، يتم استبدال الخط المستخدم فقط. أحد التحميلات الزائدة لمُنشئ TextFragmentAbsorber يقبل كائن TextEditOptions كمعامل ويمكننا استخدام قيمة RemoveUnusedFonts من تعداد TextEditOptions.FontReplace لتحقيق متطلباتنا. يوضح مقتطف الكود التالي كيفية استبدال الخط داخل مستند PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceFonts()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ReplaceTextPage.pdf"))
    {
        // Create text edit options
        var options = new Aspose.Pdf.Text.TextEditOptions(Aspose.Pdf.Text.TextEditOptions.FontReplace.RemoveUnusedFonts);

        // Search text fragments and set edit option as remove unused fonts
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber(options);

        // Accept the absorber for all the pages
        document.Pages.Accept(absorber);

        // Traverse through all the TextFragments
        foreach (var textFragment in absorber.TextFragments)
        {
            // If the font name is ArialMT, replace font name with Arial
            if (textFragment.TextState.Font.FontName == "Arial,Bold")
            {
                textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
            }
        }

        // Save PDF document
        document.Save(dataDir + "ReplaceFonts_out.pdf");
    }
}
```

## يجب أن يقوم استبدال النص بإعادة ترتيب محتويات الصفحة تلقائيًا

تدعم Aspose.PDF for .NET ميزة البحث واستبدال النص داخل ملف PDF. ومع ذلك، واجه بعض العملاء مؤخرًا مشاكل أثناء استبدال النص عندما يتم استبدال TextFragment معين بمحتويات أصغر وتظهر بعض المسافات الإضافية في ملف PDF الناتج أو في حالة استبدال TextFragment بسلسلة أطول، تتداخل الكلمات مع محتويات الصفحة الموجودة. لذا كانت المتطلبات هي تقديم آلية أنه بمجرد استبدال النص داخل مستند PDF، يجب إعادة ترتيب المحتويات.

لتلبية السيناريوهات المذكورة أعلاه، تم تحسين Aspose.PDF for .NET بحيث لا تظهر مثل هذه المشكلات عند استبدال النص داخل ملف PDF. يوضح مقتطف الكود التالي كيفية استبدال النص داخل ملف PDF ويجب إعادة ترتيب محتويات الصفحة تلقائيًا.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AutomaticallyReArrangePageContents()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractTextPage.pdf"))
    {
        // Create TextFragment Absorber object with regular expression
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber("[TextFragmentAbsorber,companyname,Textbox,50]");
        document.Pages.Accept(absorber);

        // Replace each TextFragment
        foreach (var textFragment in absorber.TextFragments)
        {
            // Set font of text fragment being replaced
            textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
            // Set font size
            textFragment.TextState.FontSize = 12;
            textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Navy;
            // Replace the text with larger string than placeholder
            textFragment.Text = "This is a Larger String for the Testing of this issue";
        }

        // Save PDF document
        document.Save(dataDir + "AutomaticallyReArrangePageContents_out.pdf");
    }
}
```

## عرض الرموز القابلة للاستبدال أثناء إنشاء PDF

الرموز القابلة للاستبدال هي رموز خاصة في سلسلة نصية يمكن استبدالها بمحتوى مطابق في وقت التشغيل. الرموز القابلة للاستبدال المدعومة حاليًا من نموذج كائن المستند الجديد في مساحة Aspose.PDF هي `$P`، `$p`، `\n`، `\r`. يتم استخدام `$p` للتعامل مع ترقيم الصفحات في وقت التشغيل. يتم استبدال `$p` برقم الصفحة التي تتواجد فيها فئة الفقرة الحالية. يتم استبدال `$P` بإجمالي عدد الصفحات في المستند. عند إضافة `TextFragment` إلى مجموعة الفقرات في مستندات PDF، لا تدعم فواصل الأسطر داخل النص. ومع ذلك، لإضافة نص مع فاصل سطر، يرجى استخدام `TextFragment` مع `TextParagraph`:

- استخدم "\r\n" أو Environment.NewLine في TextFragment بدلاً من "\n" المفرد.
- أنشئ كائن TextParagraph. سيضيف نصًا مع تقسيم الأسطر.
- أضف TextFragment مع TextParagraph.AppendLine.
- أضف TextParagraph مع TextBuilder.AppendParagraph.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RenderingReplaceableSymbols()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();

        // Initialize new TextFragment with text containing required newline markers
        Aspose.Pdf.Text.TextFragment textFragment = new Aspose.Pdf.Text.TextFragment("Applicant Name: " + Environment.NewLine + " Joe Smoe");

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
        document.Save(dataDir + "RenderingReplaceableSymbols_out.pdf");
    }
}
```

## الرموز القابلة للاستبدال في منطقة الرأس/التذييل

يمكن أيضًا وضع الرموز القابلة للاستبدال داخل قسم الرأس/التذييل لملف PDF. يرجى إلقاء نظرة على مقتطف الكود التالي للحصول على تفاصيل حول كيفية إضافة رمز قابل للاستبدال في قسم التذييل.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceableSymbolsInHeaderOrFooterArea()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();

        // Create margin info
        var marginInfo = new Aspose.Pdf.MarginInfo();
        marginInfo.Top = 90;
        marginInfo.Bottom = 50;
        marginInfo.Left = 50;
        marginInfo.Right = 50;
        // Assign the marginInfo instance to Margin property of sec1.PageInfo
        page.PageInfo.Margin = marginInfo;

        var headerFooterFirst = new Aspose.Pdf.HeaderFooter();
        page.Header = headerFooterFirst;
        headerFooterFirst.Margin.Left = 50;
        headerFooterFirst.Margin.Right = 50;

        // Instantiate a Text paragraph that will store the content to show as header
        var fragment1 = new Aspose.Pdf.Text.TextFragment("report title");
        fragment1.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
        fragment1.TextState.FontSize = 16;
        fragment1.TextState.ForegroundColor = Aspose.Pdf.Color.Black;
        fragment1.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;
        fragment1.TextState.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        fragment1.TextState.LineSpacing = 5f;
        headerFooterFirst.Paragraphs.Add(fragment1);

        var fragment2 = new Aspose.Pdf.Text.TextFragment("Report_Name");
        fragment2.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
        fragment2.TextState.ForegroundColor = Aspose.Pdf.Color.Black;
        fragment2.TextState.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        fragment2.TextState.LineSpacing = 5f;
        fragment2.TextState.FontSize = 12;
        headerFooterFirst.Paragraphs.Add(fragment2);

        // Create a HeaderFooter object for the section
        var headerFooterFoot = new Aspose.Pdf.HeaderFooter();

        // Set the HeaderFooter object to odd & even footer
        page.Footer = headerFooterFoot;
        headerFooterFoot.Margin.Left = 50;
        headerFooterFoot.Margin.Right = 50;

        // Add a text paragraph containing current page number of total number of pages
        var fragment3 = new Aspose.Pdf.Text.TextFragment("Generated on test date");
        var fragment4 = new Aspose.Pdf.Text.TextFragment("report name ");
        var fragment5 = new Aspose.Pdf.Text.TextFragment("Page $p of $P");

        // Instantiate a table object
        var table2 = new Aspose.Pdf.Table();

        // Add the table in paragraphs collection of the desired section
        headerFooterFoot.Paragraphs.Add(table2);

        // Set with column widths of the table
        table2.ColumnWidths = "165 172 165";

        // Create rows in the table and then cells in the rows
        var row3 = table2.Rows.Add();

        row3.Cells.Add();
        row3.Cells.Add();
        row3.Cells.Add();

        // Set the vertical allignment of the text as center alligned
        row3.Cells[0].Alignment = Aspose.Pdf.HorizontalAlignment.Left;
        row3.Cells[1].Alignment = Aspose.Pdf.HorizontalAlignment.Center;
        row3.Cells[2].Alignment = Aspose.Pdf.HorizontalAlignment.Right;

        row3.Cells[0].Paragraphs.Add(fragment3);
        row3.Cells[1].Paragraphs.Add(fragment4);
        row3.Cells[2].Paragraphs.Add(fragment5);

        // Sec1.Paragraphs.Add(New Text("Aspose.Total for Java is a compilation of every Java component offered by Aspose. It is compiled on a#$NL" + "daily basis to ensure it contains the most up to date versions of each of our Java components. #$NL " + "Using Aspose.Total for Java developers can create a wide range of applications. #$NL #$NL #$NP" + "Aspose.Total for Java is a compilation of every Java component offered by Aspose. It is compiled on a#$NL" + "daily basis to ensure it contains the most up to date versions of each of our Java components. #$NL " + "Using Aspose.Total for Java developers can create a wide range of applications. #$NL #$NL #$NP" + "Aspose.Total for Java is a compilation of every Java component offered by Aspose. It is compiled on a#$NL" + "daily basis to ensure it contains the most up to date versions of each of our Java components. #$NL " + "Using Aspose.Total for Java developers can create a wide range of applications. #$NL #$NL"))
        var table = new Aspose.Pdf.Table();

        table.ColumnWidths = "33% 33% 34%";
        table.DefaultCellPadding = new Aspose.Pdf.MarginInfo();
        table.DefaultCellPadding.Top = 10;
        table.DefaultCellPadding.Bottom = 10;

        // Add the table in paragraphs collection of the desired section
        page.Paragraphs.Add(table);

        // Set default cell border using BorderInfo object
        table.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.1f);

        // Set table border using another customized BorderInfo object
        table.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 1f);

        table.RepeatingRowsCount = 1;

        // Create rows in the table and then cells in the rows
        var row1 = table.Rows.Add();

        row1.Cells.Add("col1");
        row1.Cells.Add("col2");
        row1.Cells.Add("col3");
        const string CRLF = "\r\n";
        for (int i = 0; i <= 10; i++)
        {
            var row = table.Rows.Add();
            row.IsRowBroken = true;
            for (int c = 0; c <= 2; c++)
            {
                Aspose.Pdf.Cell c1;
                if (c == 2)
                {
                    c1 = row.Cells.Add("Aspose.Total for Java is a compilation of every Java component offered by Aspose. It is compiled on a" + CRLF + "daily basis to ensure it contains the most up to date versions of each of our Java components. " + CRLF + "daily basis to ensure it contains the most up to date versions of each of our Java components. " + CRLF + "Using Aspose.Total for Java developers can create a wide range of applications.");
                }
                else
                {
                    c1 = row.Cells.Add("item1" + c);
                }
                c1.Margin = new Aspose.Pdf.MarginInfo();
                c1.Margin.Left = 30;
                c1.Margin.Top = 10;
                c1.Margin.Bottom = 10;
            }
        }

        // Save PDF document
        document.Save(dataDir + "ReplaceableSymbolsInHeaderFooter_out.pdf");
    }
}
```

## إزالة الخطوط غير المستخدمة من ملف PDF

تدعم Aspose.PDF for .NET ميزة تضمين الخطوط أثناء إنشاء مستند PDF، بالإضافة إلى القدرة على تضمين الخطوط في ملفات PDF الموجودة. بدءًا من Aspose.PDF for .NET 7.3.0، تتيح لك أيضًا إزالة الخطوط المكررة أو غير المستخدمة من مستندات PDF.

لاستبدال الخطوط، استخدم النهج التالي:

1. استدعاء فئة [TextFragmentAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragmentabsorber) .
1. استدعاء معلمة TextFragmentAbsorber class’ TextEditOptions.FontReplace.RemoveUnusedFonts. (هذا يزيل الخطوط التي أصبحت غير مستخدمة أثناء استبدال الخط).
1. تعيين الخط بشكل فردي لكل جزء نص.

يستبدل مقتطف الكود التالي الخط لجميع أجزاء النص في جميع صفحات المستند ويزيل الخطوط غير المستخدمة.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveUnusedFonts()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ReplaceTextPage.pdf"))
    {
        var options = new Aspose.Pdf.Text.TextEditOptions(Aspose.Pdf.Text.TextEditOptions.FontReplace.RemoveUnusedFonts);
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
        document.Pages.Accept(absorber);

        // Iterate through all the TextFragments
        foreach (var textFragment in absorber.TextFragments)
        {
            textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial, Bold");
        }

        // Save PDF document
        document.Save(dataDir + "RemoveUnusedFonts_out.pdf");
    }
}
```

## إزالة جميع النصوص من مستند PDF

### إزالة جميع النصوص باستخدام العمليات

في بعض عمليات النص، تحتاج إلى إزالة جميع النصوص من مستند PDF ولذا، تحتاج إلى تعيين النص الموجود كقيمة سلسلة فارغة عادة. النقطة هي أن تغيير النص لعدد كبير من أجزاء النص يستدعي عددًا من عمليات التحقق وضبط موضع النص. هذه العمليات ضرورية في سيناريوهات تحرير النص. الصعوبة هي أنك لا تستطيع تحديد عدد أجزاء النص التي سيتم إزالتها في السيناريو الذي تتم معالجته في حلقة.

لذا، نوصي باستخدام نهج آخر لسيناريو إزالة جميع النصوص من صفحات PDF. يرجى النظر في مقتطف الكود التالي الذي يعمل بسرعة كبيرة.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveAllTextFromDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "RemoveAllText.pdf"))
    {
        // Loop through all pages of PDF Document
        for (int i = 1; i <= document.Pages.Count; i++)
        {
            var page = document.Pages[i];
            var operatorSelector = new Aspose.Pdf.OperatorSelector(new Aspose.Pdf.Operators.TextShowOperator());
            // Select all text on the page
            page.Contents.Accept(operatorSelector);
            // Delete all text
            page.Contents.Delete(operatorSelector.Selected);
        }
        // Save PDF document
        document.Save(dataDir + "RemoveAllText_out.pdf", Aspose.Pdf.SaveFormat.Pdf);
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