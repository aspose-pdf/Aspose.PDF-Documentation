---
title: إنشاء PDF معقد
linktitle: إنشاء PDF معقد
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /ar/net/complex-pdf-example/
description: Aspose.PDF لـ NET يتيح لك إنشاء مستندات أكثر تعقيدًا تحتوي على صور وقطع نصية وجداول في مستند واحد.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Creating a complex PDF",
    "alternativeHeadline": "Create Complex PDFs with Images, Text, and Tables in C#",
    "abstract": "Aspose.PDF for .NET يقدم ميزة قوية لإنشاء PDFs معقدة، مما يمكّن المطورين من دمج الصور وقطع النص والجداول بسلاسة في مستند واحد. تستفيد هذه الوظيفة من نهج قائم على DOM، مما يسمح بتخصيص مفصل والتحكم في التخطيط في إنشاء PDF، مما يجعلها مثالية لإنشاء مستندات ذات جودة احترافية بكفاءة",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "632",
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
    "url": "/net/complex-pdf-example/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/complex-pdf-example/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسريعة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

مثال [Hello, World](/pdf/net/hello-world-example/) أظهر خطوات بسيطة لإنشاء مستند PDF باستخدام C# وAspose.PDF. في هذه المقالة، سنلقي نظرة على إنشاء مستند أكثر تعقيدًا باستخدام C# وAspose.PDF for .NET. كمثال، سنأخذ مستندًا من شركة وهمية تعمل في خدمات عبّارات الركاب.
سيحتوي مستندنا على صورة، وقطعتين نصيتين (عنوان وفقرة)، وجدول. لبناء مثل هذا المستند، سنستخدم نهج قائم على DOM. يمكنك قراءة المزيد في قسم [أساسيات واجهة برمجة تطبيقات DOM](/pdf/net/basics-of-dom-api/).

إذا قمنا بإنشاء مستند من الصفر، نحتاج إلى اتباع خطوات معينة:

1. إنشاء كائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). في هذه الخطوة، سنقوم بإنشاء مستند PDF فارغ مع بعض البيانات الوصفية ولكن بدون صفحات.
1. إضافة [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) إلى كائن المستند. لذا، الآن سيكون لمستندنا صفحة واحدة.
1. إضافة [Image](https://reference.aspose.com/pdf/net/aspose.pdf/image/methods/index) إلى الصفحة.
1. إنشاء [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment) للعنوان. بالنسبة للعنوان، سنستخدم خط Arial بحجم 24pt ومحاذاة مركزية.
1. إضافة العنوان إلى [Paragraphs](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs) الصفحة.
1. إنشاء [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment) للوصف. بالنسبة للوصف، سنستخدم خط Arial بحجم 24pt ومحاذاة مركزية.
1. إضافة (الوصف) إلى فقرات الصفحة.
1. إنشاء جدول، إضافة خصائص الجدول.
1. إضافة (الجدول) إلى [Paragraphs](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs) الصفحة.
1. حفظ المستند "Complex.pdf".

تعمل مقتطفات الكود التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreatingComplexPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Add image
        page.AddImage(dataDir + "logo.png", new Aspose.Pdf.Rectangle(20, 730, 120, 830));

        // Add Header
        var header = new Aspose.Pdf.Text.TextFragment("New ferry routes in Fall 2020");
        header.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
        header.TextState.FontSize = 24;
        header.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        header.Position = new Aspose.Pdf.Text.Position(130, 720);
        page.Paragraphs.Add(header);

        // Add description
        var descriptionText = "Visitors must buy tickets online and tickets are limited to 5,000 per day. Ferry service is operating at half capacity and on a reduced schedule. Expect lineups.";
        var description = new Aspose.Pdf.Text.TextFragment(descriptionText);
        description.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Times New Roman");
        description.TextState.FontSize = 14;
        description.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Left;
        page.Paragraphs.Add(description);

        // Add table
        var table = new Aspose.Pdf.Table
        {
            ColumnWidths = "200",
            Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.Box, 1f, Aspose.Pdf.Color.DarkSlateGray),
            DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.Box, 0.5f, Aspose.Pdf.Color.Black),
            DefaultCellPadding = new Aspose.Pdf.MarginInfo(4.5, 4.5, 4.5, 4.5),
            Margin =
            {
                Bottom = 10
            },
            DefaultCellTextState =
            {
                Font =  Aspose.Pdf.Text.FontRepository.FindFont("Helvetica")
            }
        };

        var headerRow = table.Rows.Add();
        headerRow.Cells.Add("Departs City");
        headerRow.Cells.Add("Departs Island");
        foreach (Aspose.Pdf.Cell headerRowCell in headerRow.Cells)
        {
            headerRowCell.BackgroundColor = Aspose.Pdf.Color.Gray;
            headerRowCell.DefaultCellTextState.ForegroundColor = Aspose.Pdf.Color.WhiteSmoke;
        }

        var time = new TimeSpan(6, 0, 0);
        var incTime = new TimeSpan(0, 30, 0);
        for (int i = 0; i < 10; i++)
        {
            var dataRow = table.Rows.Add();
            dataRow.Cells.Add(time.ToString(@"hh\:mm"));
            time = time.Add(incTime);
            dataRow.Cells.Add(time.ToString(@"hh\:mm"));
        }

        page.Paragraphs.Add(table);
        // Save PDF document
        document.Save(dataDir + "Complex_out.pdf");
    }
}
```