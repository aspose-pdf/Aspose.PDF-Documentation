---
title: إنشاء PDF مع علامات باستخدام C#
linktitle: إنشاء PDF مع علامات
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ar/net/create-tagged-pdf/
description: يشرح هذا المقال كيفية إنشاء عناصر الهيكل لوثيقة PDF مع علامات برمجيًا باستخدام Aspose.PDF for .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Create Tagged PDF using C#",
    "alternativeHeadline": "Programmatically create tagged PDFs using C#",
    "abstract": "إنشاء وثائق PDF مع علامات برمجيًا باستخدام C# و Aspose.PDF، مع ضمان الامتثال لمعايير PDF/UA. تتيح هذه الميزة إنشاء وثائق PDF منظمة مع عناصر مثل العناوين والفقرات، تدعم الهياكل المتداخلة وتنسيق النص للوصول. تتضمن المكتبة أيضًا التحقق للتأكد من تلبية معايير PDF/UA",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Tagged PDF, C#, Aspose.PDF, PDF/UA, Structure Elements, ITaggedContent, AppendChild,  StructureTextState",
    "wordcount": "2921",
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
    "url": "/net/create-tagged-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-tagged-pdf/"
    },
    "dateModified": "2025-03-26",
    "description": "يشرح هذا المقال كيفية إنشاء عناصر الهيكل لوثيقة PDF مع علامات برمجيًا باستخدام Aspose.PDF for .NET."
}
</script>

إنشاء PDF مع علامات يعني إضافة (أو إنشاء) عناصر معينة إلى الوثيقة التي ستمكن الوثيقة من التحقق وفقًا لمتطلبات PDF/UA. تُسمى هذه العناصر غالبًا عناصر الهيكل.

تعمل مقتطفات الكود التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

## إنشاء PDF مع علامات (سيناريو بسيط)

لإنشاء عناصر الهيكل في وثيقة PDF مع علامات، تقدم Aspose.PDF طرقًا لإنشاء عناصر الهيكل باستخدام واجهة [ITaggedContent](https://reference.aspose.com/pdf/ar/net/aspose.pdf.tagged/itaggedcontent). تُظهر مقتطفات الكود التالية كيفية إنشاء PDF مع علامات يحتوي على عنصرين: عنوان وفقرة.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateTaggedPdfDocument01()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Get Content for work with TaggedPdf
        Aspose.Pdf.Tagged.ITaggedContent taggedContent = document.TaggedContent;
        var rootElement = taggedContent.RootElement;

        // Set Title and Language for Document
        taggedContent.SetTitle("Tagged Pdf Document");
        taggedContent.SetLanguage("en-US");

        Aspose.Pdf.LogicalStructure.HeaderElement mainHeader = taggedContent.CreateHeaderElement();
        mainHeader.SetText("Main Header");

        Aspose.Pdf.LogicalStructure.ParagraphElement paragraphElement = taggedContent.CreateParagraphElement();
        paragraphElement.SetText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. " +
            "Aenean nec lectus ac sem faucibus imperdiet. Sed ut erat ac magna ullamcorper hendrerit. " +
            "Cras pellentesque libero semper, gravida magna sed, luctus leo. Fusce lectus odio, laoreet" +
            "nec ullamcorper ut, molestie eu elit. Interdum et malesuada fames ac ante ipsum primis in faucibus." +
            "Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat" +
            "sem tristique eget. Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper" +
            "pellentesque justo rhoncus accumsan. Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus" +
            "ac iaculis eget, tempus et magna. Sed non consectetur elit. Sed vulputate, quam sed lacinia luctus," +
            "ipsum nibh fringilla purus, vitae posuere risus odio id massa. Cras sed venenatis lacus.");

        rootElement.AppendChild(mainHeader);
        rootElement.AppendChild(paragraphElement);

        // Save Tagged PDF Document
        document.Save(dataDir + "TaggedPdfDocument_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateTaggedPdfDocument01()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF Document
    using var document = new Aspose.Pdf.Document();

    // Get Content for work with TaggedPdf
    Aspose.Pdf.Tagged.ITaggedContent taggedContent = document.TaggedContent;
    var rootElement = taggedContent.RootElement;

    // Set Title and Language for Document
    taggedContent.SetTitle("Tagged Pdf Document");
    taggedContent.SetLanguage("en-US");

    Aspose.Pdf.LogicalStructure.HeaderElement mainHeader = taggedContent.CreateHeaderElement();
    mainHeader.SetText("Main Header");

    Aspose.Pdf.LogicalStructure.ParagraphElement paragraphElement = taggedContent.CreateParagraphElement();
    paragraphElement.SetText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. " +
        "Aenean nec lectus ac sem faucibus imperdiet. Sed ut erat ac magna ullamcorper hendrerit. " +
        "Cras pellentesque libero semper, gravida magna sed, luctus leo. Fusce lectus odio, laoreet" +
        "nec ullamcorper ut, molestie eu elit. Interdum et malesuada fames ac ante ipsum primis in faucibus." +
        "Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat" +
        "sem tristique eget. Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper" +
        "pellentesque justo rhoncus accumsan. Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus" +
        "ac iaculis eget, tempus et magna. Sed non consectetur elit. Sed vulputate, quam sed lacinia luctus," +
        "ipsum nibh fringilla purus, vitae posuere risus odio id massa. Cras sed venenatis lacus.");

    rootElement.AppendChild(mainHeader);
    rootElement.AppendChild(paragraphElement);

    // Save Tagged PDF Document
    document.Save(dataDir + "TaggedPdfDocument_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

سنحصل على الوثيقة التالية بعد الإنشاء:

![وثيقة PDF مع علامات تحتوي على عنصرين - عنوان وفقرة](taggedpdf-01.png)

## إنشاء PDF مع علامات مع عناصر متداخلة (إنشاء شجرة عناصر الهيكل)

في بعض الحالات، نحتاج إلى إنشاء هيكل أكثر تعقيدًا، على سبيل المثال، وضع اقتباسات في فقرة. 
لإنشاء شجرة عناصر الهيكل، يجب علينا استخدام طريقة [AppendChild](https://reference.aspose.com/pdf/ar/net/aspose.pdf.logicalstructure/element/methods/appendchild).
تُظهر مقتطفات الكود التالية كيفية إنشاء شجرة عناصر الهيكل لوثيقة PDF مع علامات:

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateTaggedPdfDocument02()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF Document
    using (var document = new Aspose.Pdf.Document())
    {
        // Get Content for work with TaggedPdf
        Aspose.Pdf.Tagged.ITaggedContent taggedContent = document.TaggedContent;
        var rootElement = taggedContent.RootElement;

        // Set Title and Language for Document
        taggedContent.SetTitle("Tagged Pdf Document");
        taggedContent.SetLanguage("en-US");

        Aspose.Pdf.LogicalStructure.HeaderElement header1 = taggedContent.CreateHeaderElement(1);
        header1.SetText("Header Level 1");

        Aspose.Pdf.LogicalStructure.ParagraphElement paragraphWithQuotes = taggedContent.CreateParagraphElement();
        paragraphWithQuotes.StructureTextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Calibri");
        paragraphWithQuotes.AdjustPosition(new Aspose.Pdf.Tagged.PositionSettings
            {
                Margin = new Aspose.Pdf.MarginInfo(10, 5, 10, 5)
            });

        Aspose.Pdf.LogicalStructure.SpanElement spanElement1 = taggedContent.CreateSpanElement();
        spanElement1.SetText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean nec lectus ac sem faucibus imperdiet. Sed ut erat ac magna ullamcorper hendrerit. Cras pellentesque libero semper, gravida magna sed, luctus leo. Fusce lectus odio, laoreet nec ullamcorper ut, molestie eu elit. Interdum et malesuada fames ac ante ipsum primis in faucibus. Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat sem tristique eget. Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper pellentesque justo rhoncus accumsan. Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus ac iaculis eget, tempus et magna. Sed non consectetur elit. ");

        Aspose.Pdf.LogicalStructure.QuoteElement quoteElement = taggedContent.CreateQuoteElement();
        quoteElement.SetText("Sed vulputate, quam sed lacinia luctus, ipsum nibh fringilla purus, vitae posuere risus odio id massa.");
        quoteElement.StructureTextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold | Aspose.Pdf.Text.FontStyles.Italic;
        Aspose.Pdf.LogicalStructure.SpanElement spanElement2 = taggedContent.CreateSpanElement();
        spanElement2.SetText(" Sed non consectetur elit.");

        paragraphWithQuotes.AppendChild(spanElement1);
        paragraphWithQuotes.AppendChild(quoteElement);
        paragraphWithQuotes.AppendChild(spanElement2);

        rootElement.AppendChild(header1);
        rootElement.AppendChild(paragraphWithQuotes);

        // Save Tagged PDF Document
        document.Save(dataDir + "TaggedPdfDocument_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateTaggedPdfDocument02()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF Document
    using var document = new Aspose.Pdf.Document();

    // Get Content for work with TaggedPdf
    Aspose.Pdf.Tagged.ITaggedContent taggedContent = document.TaggedContent;
    var rootElement = taggedContent.RootElement;

    // Set Title and Language for Document
    taggedContent.SetTitle("Tagged Pdf Document");
    taggedContent.SetLanguage("en-US");

    Aspose.Pdf.LogicalStructure.HeaderElement header1 = taggedContent.CreateHeaderElement(1);
    header1.SetText("Header Level 1");

    Aspose.Pdf.LogicalStructure.ParagraphElement paragraphWithQuotes = taggedContent.CreateParagraphElement();
    paragraphWithQuotes.StructureTextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Calibri");
    
    paragraphWithQuotes.AdjustPosition(new Aspose.Pdf.Tagged.PositionSettings
        {
            Margin = new Aspose.Pdf.MarginInfo(10, 5, 10, 5)
        });

    Aspose.Pdf.LogicalStructure.SpanElement spanElement1 = taggedContent.CreateSpanElement();
    spanElement1.SetText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean nec lectus ac sem faucibus imperdiet. Sed ut erat ac magna ullamcorper hendrerit. Cras pellentesque libero semper, gravida magna sed, luctus leo. Fusce lectus odio, laoreet nec ullamcorper ut, molestie eu elit. Interdum et malesuada fames ac ante ipsum primis in faucibus. Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat sem tristique eget. Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper pellentesque justo rhoncus accumsan. Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus ac iaculis eget, tempus et magna. Sed non consectetur elit. ");

    Aspose.Pdf.LogicalStructure.QuoteElement quoteElement = taggedContent.CreateQuoteElement();
    quoteElement.SetText("Sed vulputate, quam sed lacinia luctus, ipsum nibh fringilla purus, vitae posuere risus odio id massa.");
    quoteElement.StructureTextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold | Aspose.Pdf.Text.FontStyles.Italic;
    Aspose.Pdf.LogicalStructure.SpanElement spanElement2 = taggedContent.CreateSpanElement();
    spanElement2.SetText(" Sed non consectetur elit.");

    paragraphWithQuotes.AppendChild(spanElement1);
    paragraphWithQuotes.AppendChild(quoteElement);
    paragraphWithQuotes.AppendChild(spanElement2);

    rootElement.AppendChild(header1);
    rootElement.AppendChild(paragraphWithQuotes);

    // Save Tagged PDF Document
    document.Save(dataDir + "TaggedPdfDocument_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

سنحصل على الوثيقة التالية بعد الإنشاء:
![وثيقة PDF مع علامات تحتوي على عناصر متداخلة - span واقتباسات](taggedpdf-02.png)

## تنسيق هيكل النص

لتهيئة هيكل النص في وثيقة PDF مع علامات، تقدم Aspose.PDF خصائص [Font](https://reference.aspose.com/pdf/ar/net/aspose.pdf.logicalstructure/structuretextstate/properties/font)، [FontSize](https://reference.aspose.com/pdf/ar/net/aspose.pdf.logicalstructure/structuretextstate/properties/fontsize)، [FontStyle](https://reference.aspose.com/pdf/ar/net/aspose.pdf.logicalstructure/structuretextstate/properties/fontstyle) و [ForegroundColor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.logicalstructure/structuretextstate/properties/foregroundcolor) من فئة [StructureTextState](https://reference.aspose.com/pdf/ar/net/aspose.pdf.logicalstructure/structuretextstate). تُظهر مقتطفات الكود التالية كيفية تنسيق هيكل النص في وثيقة PDF مع علامات:

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddStyle()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF Document
    using (var document = new Aspose.Pdf.Document())
    {
        // Get Content for work with TaggedPdf
        Aspose.Pdf.Tagged.ITaggedContent taggedContent = document.TaggedContent;

        // Set Title and Language for Document
        taggedContent.SetTitle("Tagged Pdf Document");
        taggedContent.SetLanguage("en-US");

        Aspose.Pdf.LogicalStructure.ParagraphElement p = taggedContent.CreateParagraphElement();
        taggedContent.RootElement.AppendChild(p);

        p.StructureTextState.FontSize = 18F;
        p.StructureTextState.ForegroundColor = Aspose.Pdf.Color.Red;
        p.StructureTextState.FontStyle = Aspose.Pdf.Text.FontStyles.Italic;

        p.SetText("Red italic text.");

        // Save Tagged PDF Document
        document.Save(dataDir + "StyleTextStructure_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddStyle()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF Document
    using var document = new Aspose.Pdf.Document();

    // Get Content for work with TaggedPdf
    Aspose.Pdf.Tagged.ITaggedContent taggedContent = document.TaggedContent;

    // Set Title and Language for Document
    taggedContent.SetTitle("Tagged Pdf Document");
    taggedContent.SetLanguage("en-US");

    Aspose.Pdf.LogicalStructure.ParagraphElement p = taggedContent.CreateParagraphElement();
    taggedContent.RootElement.AppendChild(p);

    p.StructureTextState.FontSize = 18F;
    p.StructureTextState.ForegroundColor = Aspose.Pdf.Color.Red;
    p.StructureTextState.FontStyle = Aspose.Pdf.Text.FontStyles.Italic;

    p.SetText("Red italic text.");

    // Save Tagged PDF Document
    document.Save(dataDir + "StyleTextStructure_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## توضيح عناصر الهيكل

لتوضيح عناصر الهيكل في وثيقة PDF مع علامات، تقدم Aspose.PDF فئة [IllustrationElement](https://reference.aspose.com/pdf/ar/net/aspose.pdf.logicalstructure/illustrationelement). تُظهر مقتطفات الكود التالية كيفية توضيح عناصر الهيكل في وثيقة PDF مع علامات:

{{< tabs tabID="4" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void IllustrateStructureElements()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF Document
    using (var document = new Aspose.Pdf.Document())
    {
        // Get Content for work with TaggedPdf
        Aspose.Pdf.Tagged.ITaggedContent taggedContent = document.TaggedContent;

        // Set Title and Language for Document
        taggedContent.SetTitle("Tagged Pdf Document");
        taggedContent.SetLanguage("en-US");

        Aspose.Pdf.LogicalStructure.IllustrationElement figure1 = taggedContent.CreateFigureElement();
        taggedContent.RootElement.AppendChild(figure1);
        figure1.AlternativeText = "Figure One";
        figure1.Title = "Image 1";
        figure1.SetTag("Fig1");
        figure1.SetImage(dataDir + "image.png");
        
        // Adjust position
        figure1.AdjustPosition(new Aspose.Pdf.Tagged.PositionSettings
        {
            Margin = new Aspose.Pdf.MarginInfo
            {
                Left = 50,
                Top = 20
            },
        });

        // Save Tagged PDF Document
        document.Save(dataDir + "IllustrationStructureElements_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void IllustrateStructureElements()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF Document
    using var document = new Aspose.Pdf.Document();

    // Get Content for work with TaggedPdf
    Aspose.Pdf.Tagged.ITaggedContent taggedContent = document.TaggedContent;

    // Set Title and Language for Document
    taggedContent.SetTitle("Tagged Pdf Document");
    taggedContent.SetLanguage("en-US");

    Aspose.Pdf.LogicalStructure.IllustrationElement figure1 = taggedContent.CreateFigureElement();
    taggedContent.RootElement.AppendChild(figure1);
    figure1.AlternativeText = "Figure One";
    figure1.Title = "Image 1";
    figure1.SetTag("Fig1");
    figure1.SetImage(dataDir + "image.png");
    
    // Adjust position
    figure1.AdjustPosition(new Aspose.Pdf.Tagged.PositionSettings
    {
        Margin = new Aspose.Pdf.MarginInfo
        {
            Left = 50,
            Top = 20
        },
    });

    // Save Tagged PDF Document
    document.Save(dataDir + "IllustrationStructureElements_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## التحقق من PDF مع علامات

تقدم Aspose.PDF for .NET القدرة على التحقق من وثيقة PDF مع علامات وفقًا لمعايير PDF/UA. يدعم التحقق من معيار PDF/UA:

- التحقق من XObjects.
- التحقق من الإجراءات.
- التحقق من المحتوى الاختياري.
- التحقق من الملفات المضمنة.
- التحقق من حقول Acroform (التحقق من اللغة الطبيعية والاسم البديل والتوقيعات الرقمية).
- التحقق من حقول نموذج XFA.
- التحقق من إعدادات الأمان.
- التحقق من التنقل.
- التحقق من التعليقات.

تُظهر مقتطفات الكود أدناه كيفية التحقق من وثيقة PDF مع علامات. ستظهر المشاكل المقابلة في تقرير سجل XML.

{{< tabs tabID="5" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ValidateTaggedPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "StructureElements.pdf"))
    {
        bool isValid = document.Validate(dataDir + "StructureElements_log.xml", Aspose.Pdf.PdfFormat.PDF_UA_1);
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ValidateTaggedPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "StructureElements.pdf");

    bool isValid = document.Validate(dataDir + "StructureElements_log.xml", Aspose.Pdf.PdfFormat.PDF_UA_1);
}
```
{{< /tab >}}
{{< /tabs >}}

## ضبط موضع هيكل النص

تُظهر مقتطفات الكود التالية كيفية ضبط موضع هيكل النص في وثيقة PDF مع علامات:

{{< tabs tabID="6" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AdjustPosition()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF Document
    using (var document = new Aspose.Pdf.Document())
    {
        // Get Content for work with TaggedPdf
        var taggedContent = document.TaggedContent;

        // Set Title and Language for Document
        taggedContent.SetTitle("Tagged Pdf Document");
        taggedContent.SetLanguage("en-US");

        // Create paragraph
        var p = taggedContent.CreateParagraphElement();
        taggedContent.RootElement.AppendChild(p);
        p.SetText("Text.");

        // Adjust position
        p.AdjustPosition(new Aspose.Pdf.Tagged.PositionSettings
        {
            HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.None,
            Margin = new Aspose.Pdf.MarginInfo
            {
                Left = 300,
                Right = 0,
                Top = 20,
                Bottom = 0
            },
            VerticalAlignment = Aspose.Pdf.VerticalAlignment.None,
            IsFirstParagraphInColumn = false,
            IsKeptWithNext = false,
            IsInNewPage = false,
            IsInLineParagraph = false
        });

        // Save Tagged PDF Document
        document.Save(dataDir + "AdjustTextPosition_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AdjustPosition()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF Document
    using var document = new Aspose.Pdf.Document();
    
    // Get Content for work with TaggedPdf
    var taggedContent = document.TaggedContent;

    // Set Title and Language for Document
    taggedContent.SetTitle("Tagged Pdf Document");
    taggedContent.SetLanguage("en-US");

    // Create paragraph
    var p = taggedContent.CreateParagraphElement();
    taggedContent.RootElement.AppendChild(p);
    p.SetText("Text.");

    // Adjust position
    p.AdjustPosition(new Aspose.Pdf.Tagged.PositionSettings
    {
        HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.None,
        Margin = new Aspose.Pdf.MarginInfo
        {
            Left = 300,
            Right = 0,
            Top = 20,
            Bottom = 0
        },
        VerticalAlignment = Aspose.Pdf.VerticalAlignment.None,
        IsFirstParagraphInColumn = false,
        IsKeptWithNext = false,
        IsInNewPage = false,
        IsInLineParagraph = false
    });

    // Save Tagged PDF Document
    document.Save(dataDir + "AdjustTextPosition_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## إنشاء PDF مع علامات تلقائيًا مع تحويل PDF/UA-1

تتيح Aspose.PDF إنشاء ترميز هيكل منطقي أساسي تلقائيًا عند تحويل وثيقة إلى PDF/UA-1. يمكن للمستخدمين بعد ذلك تحسين هذا الهيكل المنطقي الأساسي يدويًا، مما يوفر رؤى إضافية حول محتويات الوثيقة.

لإنشاء هيكل وثيقة منطقي، قم بإنشاء مثيل من فئة [Aspose.Pdf.AutoTaggingSettings](https://reference.aspose.com/pdf/ar/net/aspose.pdf/autotaggingsettings/)، واضبط خاصية [AutoTaggingSettings.EnableAutoTagging](https://reference.aspose.com/pdf/ar/net/aspose.pdf/autotaggingsettings/enableautotagging/) على `true`، وخصصها إلى خاصية [PdfFormatConversionOptions.AutoTaggingSettings](https://reference.aspose.com/pdf/ar/net/aspose.pdf/pdfformatconversionoptions/autotaggingsettings/).

{{% alert color="warning" %}}
إذا كانت الوثيقة تحتوي بالفعل على علامات هيكل منطقي، فإن تمكين التمييز التلقائي سيدمر الهيكل المنطقي الحالي وينشئ هيكلًا جديدًا.
{{% /alert %}}

{{< tabs tabID="7" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertToPdfUAWithAutomaticTagging()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (Aspose.Pdf.Document document = new Aspose.Pdf.Document(dataDir + "BreakfastMenu.pdf"))
    {
        // Create conversion options
        Aspose.Pdf.PdfFormatConversionOptions options = new Aspose.Pdf.PdfFormatConversionOptions(dataDir + "ConvertToPdfUAWithAutomaticTagging.xml", PdfFormat.PDF_UA_1, ConvertErrorAction.Delete);

        // Create auto-tagging settings
        // Aspose.Pdf.AutoTaggingSettings.Default may be used to set the same settings as given below
        Aspose.Pdf.AutoTaggingSettings autoTaggingSettings = new Aspose.Pdf.AutoTaggingSettings();

        // Enable auto-tagging during the conversion process
        autoTaggingSettings.EnableAutoTagging = true;

        // Use the heading recognition strategy that's optimal for the given document structure
        autoTaggingSettings.HeadingRecognitionStrategy = Aspose.Pdf.HeadingRecognitionStrategy.Auto;

        // Assign auto-tagging settings to be used during the conversion process
        options.AutoTaggingSettings = autoTaggingSettings;

        // During the conversion, the document logical structure will be automatically created
        document.Convert(options);

        // Save PDF document
        document.Save(dataDir + "ConvertToPdfUAWithAutomaticTagging_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertToPdfUAWithAutomaticTagging()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using Aspose.Pdf.Document document = new Aspose.Pdf.Document(dataDir + "BreakfastMenu.pdf");

    // Create conversion options
    Aspose.Pdf.PdfFormatConversionOptions options = new Aspose.Pdf.PdfFormatConversionOptions(dataDir + "ConvertToPdfUAWithAutomaticTagging.xml", PdfFormat.PDF_UA_1, ConvertErrorAction.Delete);

    // Create auto-tagging settings
    // Aspose.Pdf.AutoTaggingSettings.Default may be used to set the same settings as given below
    Aspose.Pdf.AutoTaggingSettings autoTaggingSettings = new Aspose.Pdf.AutoTaggingSettings
    {
        // Enable auto-tagging during the conversion process
        EnableAutoTagging = true,

        // Use the heading recognition strategy that's optimal for the given document structure
        HeadingRecognitionStrategy = Aspose.Pdf.HeadingRecognitionStrategy.Auto
    };

    // Assign auto-tagging settings to be used during the conversion process
    options.AutoTaggingSettings = autoTaggingSettings;

    // During the conversion, the document logical structure will be automatically created
    document.Convert(options);

    // Save PDF document
    document.Save(dataDir + "ConvertToPdfUAWithAutomaticTagging_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

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