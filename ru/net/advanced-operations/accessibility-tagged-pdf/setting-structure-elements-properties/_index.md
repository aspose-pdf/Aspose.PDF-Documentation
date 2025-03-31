---
title: Установка свойств элементов структуры
linktitle: Установка свойств элементов структуры
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ru/net/setting-structure-elements-properties/
description: Вы можете установить различные свойства элементов структуры в PDF-документе с Aspose.PDF for .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Setting Structure Elements Properties",
    "alternativeHeadline": "Setting Properties for Structure Elements in PDFs",
    "abstract": "Улучшите доступность вашего PDF-документа с помощью новой функции в Aspose.PDF for .NET, которая позволяет пользователям устанавливать свойства для элементов структуры. Эта функциональность обеспечивает точный контроль над заголовками, языками и пользовательскими тегами для различных элементов в помеченном PDF, обеспечивая соответствие и улучшенную навигацию для экранных считывателей.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Setting Structure Elements Properties, Aspose.PDF for .NET, Tagged PDF Document, CreateSectElement, CreateHeaderElement, SetTitle, SetLanguage, NoteElement, StructureElement, LinkElement",
    "wordcount": "2730",
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
    "url": "/net/setting-structure-elements-properties/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/setting-structure-elements-properties/"
    },
    "dateModified": "2024-11-25",
    "description": "Вы можете установить различные свойства элементов структуры в PDF-документе с Aspose.PDF for .NET."
}
</script>

Чтобы установить свойства элементов структуры в помеченном PDF-документе, Aspose.PDF предлагает методы [CreateSectElement](https://reference.aspose.com/pdf/ru/net/aspose.pdf.tagged/itaggedcontent/methods/createsectelement) и [CreateHeaderElement](https://reference.aspose.com/pdf/ru/net/aspose.pdf.tagged/itaggedcontent/methods/createheaderelement/index) интерфейса [ITaggedContent](https://reference.aspose.com/pdf/ru/net/aspose.pdf.tagged/itaggedcontent).

Следующий фрагмент кода показывает, как установить свойства элементов структуры помеченного PDF-документа:

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF Document
    using (var document = new Aspose.Pdf.Document())
    {
        // Get Content for work with Tagged PDF
        Aspose.Pdf.Tagged.ITaggedContent taggedContent = document.TaggedContent;

        // Set Title and Language for Document
        taggedContent.SetTitle("Tagged Pdf Document");
        taggedContent.SetLanguage("en-US");

        // Create Structure Elements
        Aspose.Pdf.LogicalStructure.StructureElement rootElement = taggedContent.RootElement;

        Aspose.Pdf.LogicalStructure.SectElement sect = taggedContent.CreateSectElement();
        rootElement.AppendChild(sect);

        Aspose.Pdf.LogicalStructure.HeaderElement h1 = taggedContent.CreateHeaderElement(1);
        sect.AppendChild(h1);
        h1.SetText("The Header");

        h1.Title = "Title";
        h1.Language = "en-US";
        h1.AlternativeText = "Alternative Text";
        h1.ExpansionText = "Expansion Text";
        h1.ActualText = "Actual Text";

        // Save Tagged PDF Document
        document.Save(dataDir + "StructureElementsProperties_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF Document
    using var document = new Aspose.Pdf.Document();

    // Get Content for work with Tagged PDF
    Aspose.Pdf.Tagged.ITaggedContent taggedContent = document.TaggedContent;

    // Set Title and Language for Document
    taggedContent.SetTitle("Tagged Pdf Document");
    taggedContent.SetLanguage("en-US");

    // Create Structure Elements
    Aspose.Pdf.LogicalStructure.StructureElement rootElement = taggedContent.RootElement;

    Aspose.Pdf.LogicalStructure.SectElement sect = taggedContent.CreateSectElement();
    rootElement.AppendChild(sect);

    Aspose.Pdf.LogicalStructure.HeaderElement h1 = taggedContent.CreateHeaderElement(1);
    sect.AppendChild(h1);
    h1.SetText("The Header");

    h1.Title = "Title";
    h1.Language = "en-US";
    h1.AlternativeText = "Alternative Text";
    h1.ExpansionText = "Expansion Text";
    h1.ActualText = "Actual Text";

    // Save Tagged PDF Document
    document.Save(dataDir + "StructureElementsProperties_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Установка текстовых элементов структуры

Чтобы установить текстовые элементы структуры помеченного PDF-документа, Aspose.PDF предлагает класс [ParagraphElement](https://reference.aspose.com/pdf/ru/net/aspose.pdf.logicalstructure/paragraphelement). Следующий фрагмент кода показывает, как установить текстовые элементы структуры помеченного PDF-документа:

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetTextElements()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF Document
    using (var document = new Aspose.Pdf.Document())
    {
        // Get Content for work with Tagged PDF
        Aspose.Pdf.Tagged.ITaggedContent taggedContent = document.TaggedContent;

        // Set Title and Language for Document
        taggedContent.SetTitle("Tagged Pdf Document");
        taggedContent.SetLanguage("en-US");

        // Get Root Structure Elements
        Aspose.Pdf.LogicalStructure.StructureElement rootElement = taggedContent.RootElement;

        Aspose.Pdf.LogicalStructure.ParagraphElement p = taggedContent.CreateParagraphElement();

        // Set Text to Text Structure Element
        p.SetText("Paragraph.");
        rootElement.AppendChild(p);

        // Save Tagged PDF Document
        document.Save(dataDir + "TextStructureElement_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetTextElements()
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

    // Get Root Structure Elements
    Aspose.Pdf.LogicalStructure.StructureElement rootElement = taggedContent.RootElement;

    Aspose.Pdf.LogicalStructure.ParagraphElement p = taggedContent.CreateParagraphElement();

    // Set Text to Text Structure Element
    p.SetText("Paragraph.");
    rootElement.AppendChild(p);

    // Save Tagged PDF Document
    document.Save(dataDir + "TextStructureElement_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Установка элементов структуры текстового блока

Чтобы установить элементы структуры текстового блока помеченного PDF-документа, Aspose.PDF предлагает классы [HeaderElement](https://reference.aspose.com/pdf/ru/net/aspose.pdf.logicalstructure/headerelement) и [ParagraphElement](https://reference.aspose.com/pdf/ru/net/aspose.pdf.logicalstructure/paragraphelement). Вы можете добавить объекты этих классов в качестве дочерних элементов объекта [StructureElement](https://reference.aspose.com/pdf/ru/net/aspose.pdf.logicalstructure/structureelement).
Следующий фрагмент кода показывает, как установить элементы структуры текстового блока помеченного PDF-документа:

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetTextBlockElements()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF Document
    using (var document = new Aspose.Pdf.Document())
    {
        // Get Content for work with Tagged PDF
        Aspose.Pdf.Tagged.ITaggedContent taggedContent = document.TaggedContent;

        // Set Title and Language for Document
        taggedContent.SetTitle("Tagged Pdf Document");
        taggedContent.SetLanguage("en-US");

        // Get Root Structure Element
        Aspose.Pdf.LogicalStructure.StructureElement rootElement = taggedContent.RootElement;

        Aspose.Pdf.LogicalStructure.HeaderElement h1 = taggedContent.CreateHeaderElement(1);
        Aspose.Pdf.LogicalStructure.HeaderElement h2 = taggedContent.CreateHeaderElement(2);
        Aspose.Pdf.LogicalStructure.HeaderElement h3 = taggedContent.CreateHeaderElement(3);
        Aspose.Pdf.LogicalStructure.HeaderElement h4 = taggedContent.CreateHeaderElement(4);
        Aspose.Pdf.LogicalStructure.HeaderElement h5 = taggedContent.CreateHeaderElement(5);
        Aspose.Pdf.LogicalStructure.HeaderElement h6 = taggedContent.CreateHeaderElement(6);
        h1.SetText("H1. Header of Level 1");
        h2.SetText("H2. Header of Level 2");
        h3.SetText("H3. Header of Level 3");
        h4.SetText("H4. Header of Level 4");
        h5.SetText("H5. Header of Level 5");
        h6.SetText("H6. Header of Level 6");
        rootElement.AppendChild(h1);
        rootElement.AppendChild(h2);
        rootElement.AppendChild(h3);
        rootElement.AppendChild(h4);
        rootElement.AppendChild(h5);
        rootElement.AppendChild(h6);

        Aspose.Pdf.LogicalStructure.ParagraphElement p = taggedContent.CreateParagraphElement();
        p.SetText("P. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean nec lectus ac sem faucibus imperdiet. Sed ut erat ac magna ullamcorper hendrerit. Cras pellentesque libero semper, gravida magna sed, luctus leo. Fusce lectus odio, laoreet nec ullamcorper ut, molestie eu elit. Interdum et malesuada fames ac ante ipsum primis in faucibus. Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat sem tristique eget. Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper pellentesque justo rhoncus accumsan. Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus ac iaculis eget, tempus et magna. Sed non consectetur elit. Sed vulputate, quam sed lacinia luctus, ipsum nibh fringilla purus, vitae posuere risus odio id massa. Cras sed venenatis lacus.");
        rootElement.AppendChild(p);

        // Save Tagged PDF Document
        document.Save(dataDir + "TextBlockStructureElements_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetTextBlockElements()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF Document
    using var document = new Aspose.Pdf.Document();

    // Get Content for work with Tagged PDF
    Aspose.Pdf.Tagged.ITaggedContent taggedContent = document.TaggedContent;

    // Set Title and Language for Document
    taggedContent.SetTitle("Tagged Pdf Document");
    taggedContent.SetLanguage("en-US");

    // Get Root Structure Element
    Aspose.Pdf.LogicalStructure.StructureElement rootElement = taggedContent.RootElement;

    Aspose.Pdf.LogicalStructure.HeaderElement h1 = taggedContent.CreateHeaderElement(1);
    Aspose.Pdf.LogicalStructure.HeaderElement h2 = taggedContent.CreateHeaderElement(2);
    Aspose.Pdf.LogicalStructure.HeaderElement h3 = taggedContent.CreateHeaderElement(3);
    Aspose.Pdf.LogicalStructure.HeaderElement h4 = taggedContent.CreateHeaderElement(4);
    Aspose.Pdf.LogicalStructure.HeaderElement h5 = taggedContent.CreateHeaderElement(5);
    Aspose.Pdf.LogicalStructure.HeaderElement h6 = taggedContent.CreateHeaderElement(6);
    h1.SetText("H1. Header of Level 1");
    h2.SetText("H2. Header of Level 2");
    h3.SetText("H3. Header of Level 3");
    h4.SetText("H4. Header of Level 4");
    h5.SetText("H5. Header of Level 5");
    h6.SetText("H6. Header of Level 6");
    rootElement.AppendChild(h1);
    rootElement.AppendChild(h2);
    rootElement.AppendChild(h3);
    rootElement.AppendChild(h4);
    rootElement.AppendChild(h5);
    rootElement.AppendChild(h6);

    Aspose.Pdf.LogicalStructure.ParagraphElement p = taggedContent.CreateParagraphElement();
    p.SetText("P. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean nec lectus ac sem faucibus imperdiet. Sed ut erat ac magna ullamcorper hendrerit. Cras pellentesque libero semper, gravida magna sed, luctus leo. Fusce lectus odio, laoreet nec ullamcorper ut, molestie eu elit. Interdum et malesuada fames ac ante ipsum primis in faucibus. Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat sem tristique eget. Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper pellentesque justo rhoncus accumsan. Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus ac iaculis eget, tempus et magna. Sed non consectetur elit. Sed vulputate, quam sed lacinia luctus, ipsum nibh fringilla purus, vitae posuere risus odio id massa. Cras sed venenatis lacus.");
    rootElement.AppendChild(p);

    // Save Tagged PDF Document
    document.Save(dataDir + "TextBlockStructureElements_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Установка встроенных элементов структуры

Чтобы установить встроенные элементы структуры помеченного PDF-документа, Aspose.PDF предлагает классы [SpanElement](https://reference.aspose.com/pdf/ru/net/aspose.pdf.logicalstructure/spanelement) и [ParagraphElement](https://reference.aspose.com/pdf/ru/net/aspose.pdf.logicalstructure/paragraphelement). Вы можете добавить объекты этих классов в качестве дочерних элементов объекта [StructureElement](https://reference.aspose.com/pdf/ru/net/aspose.pdf.logicalstructure/structureelement). Следующий фрагмент кода показывает, как установить встроенные элементы структуры помеченного PDF-документа:

{{< tabs tabID="4" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetInlineElements()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF Document
    using (var document = new Aspose.Pdf.Document())
    {
        // Get Content for work with Tagged PDF
        Aspose.Pdf.Tagged.ITaggedContent taggedContent = document.TaggedContent;

        // Set Title and Language for Document
        taggedContent.SetTitle("Tagged Pdf Document");
        taggedContent.SetLanguage("en-US");

        // Get Root Structure Element
        Aspose.Pdf.LogicalStructure.StructureElement rootElement = taggedContent.RootElement;

        Aspose.Pdf.LogicalStructure.HeaderElement h1 = taggedContent.CreateHeaderElement(1);
        Aspose.Pdf.LogicalStructure.HeaderElement h2 = taggedContent.CreateHeaderElement(2);
        Aspose.Pdf.LogicalStructure.HeaderElement h3 = taggedContent.CreateHeaderElement(3);
        Aspose.Pdf.LogicalStructure.HeaderElement h4 = taggedContent.CreateHeaderElement(4);
        Aspose.Pdf.LogicalStructure.HeaderElement h5 = taggedContent.CreateHeaderElement(5);
        Aspose.Pdf.LogicalStructure.HeaderElement h6 = taggedContent.CreateHeaderElement(6);
        rootElement.AppendChild(h1);
        rootElement.AppendChild(h2);
        rootElement.AppendChild(h3);
        rootElement.AppendChild(h4);
        rootElement.AppendChild(h5);
        rootElement.AppendChild(h6);

        Aspose.Pdf.LogicalStructure.SpanElement spanH11 = taggedContent.CreateSpanElement();
        spanH11.SetText("H1. ");
        h1.AppendChild(spanH11);
        Aspose.Pdf.LogicalStructure.SpanElement spanH12 = taggedContent.CreateSpanElement();
        spanH12.SetText("Level 1 Header");
        h1.AppendChild(spanH12);

        Aspose.Pdf.LogicalStructure.SpanElement spanH21 = taggedContent.CreateSpanElement();
        spanH21.SetText("H2. ");
        h2.AppendChild(spanH21);
        Aspose.Pdf.LogicalStructure.SpanElement spanH22 = taggedContent.CreateSpanElement();
        spanH22.SetText("Level 2 Header");
        h2.AppendChild(spanH22);

        Aspose.Pdf.LogicalStructure.SpanElement spanH31 = taggedContent.CreateSpanElement();
        spanH31.SetText("H3. ");
        h3.AppendChild(spanH31);
        Aspose.Pdf.LogicalStructure.SpanElement spanH32 = taggedContent.CreateSpanElement();
        spanH32.SetText("Level 3 Header");
        h3.AppendChild(spanH32);

        Aspose.Pdf.LogicalStructure.SpanElement spanH41 = taggedContent.CreateSpanElement();
        spanH41.SetText("H4. ");
        h4.AppendChild(spanH41);
        Aspose.Pdf.LogicalStructure.SpanElement spanH42 = taggedContent.CreateSpanElement();
        spanH42.SetText("Level 4 Header");
        h4.AppendChild(spanH42);

        Aspose.Pdf.LogicalStructure.SpanElement spanH51 = taggedContent.CreateSpanElement();
        spanH51.SetText("H5. ");
        h5.AppendChild(spanH51);
        Aspose.Pdf.LogicalStructure.SpanElement spanH52 = taggedContent.CreateSpanElement();
        spanH52.SetText("Level 5 Header");
        h5.AppendChild(spanH52);

        Aspose.Pdf.LogicalStructure.SpanElement spanH61 = taggedContent.CreateSpanElement();
        spanH61.SetText("H6. ");
        h6.AppendChild(spanH61);
        Aspose.Pdf.LogicalStructure.SpanElement spanH62 = taggedContent.CreateSpanElement();
        spanH62.SetText("Level 6 Header");
        h6.AppendChild(spanH62);

        Aspose.Pdf.LogicalStructure.ParagraphElement p = taggedContent.CreateParagraphElement();
        p.SetText("P. ");
        rootElement.AppendChild(p);
        Aspose.Pdf.LogicalStructure.SpanElement span1 = taggedContent.CreateSpanElement();
        span1.SetText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. ");
        p.AppendChild(span1);
        Aspose.Pdf.LogicalStructure.SpanElement span2 = taggedContent.CreateSpanElement();
        span2.SetText("Aenean nec lectus ac sem faucibus imperdiet. ");
        p.AppendChild(span2);
        Aspose.Pdf.LogicalStructure.SpanElement span3 = taggedContent.CreateSpanElement();
        span3.SetText("Sed ut erat ac magna ullamcorper hendrerit. ");
        p.AppendChild(span3);
        Aspose.Pdf.LogicalStructure.SpanElement span4 = taggedContent.CreateSpanElement();
        span4.SetText("Cras pellentesque libero semper, gravida magna sed, luctus leo. ");
        p.AppendChild(span4);
        Aspose.Pdf.LogicalStructure.SpanElement span5 = taggedContent.CreateSpanElement();
        span5.SetText("Fusce lectus odio, laoreet nec ullamcorper ut, molestie eu elit. ");
        p.AppendChild(span5);
        Aspose.Pdf.LogicalStructure.SpanElement span6 = taggedContent.CreateSpanElement();
        span6.SetText("Interdum et malesuada fames ac ante ipsum primis in faucibus. ");
        p.AppendChild(span6);
        Aspose.Pdf.LogicalStructure.SpanElement span7 = taggedContent.CreateSpanElement();
        span7.SetText("Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat sem tristique eget. ");
        p.AppendChild(span7);
        Aspose.Pdf.LogicalStructure.SpanElement span8 = taggedContent.CreateSpanElement();
        span8.SetText("Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper pellentesque justo rhoncus accumsan. ");
        p.AppendChild(span8);
        Aspose.Pdf.LogicalStructure.SpanElement span9 = taggedContent.CreateSpanElement();
        span9.SetText("Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus ac iaculis eget, tempus et magna. Sed non consectetur elit. ");
        p.AppendChild(span9);
        Aspose.Pdf.LogicalStructure.SpanElement span10 = taggedContent.CreateSpanElement();
        span10.SetText("Sed vulputate, quam sed lacinia luctus, ipsum nibh fringilla purus, vitae posuere risus odio id massa. Cras sed venenatis lacus.");
        p.AppendChild(span10);

        // Save Tagged PDF Document
        document.Save(dataDir + "InlineStructureElements_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetInlineElements()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF Document
    using var document = new Aspose.Pdf.Document();

    // Get Content for work with Tagged PDF
    Aspose.Pdf.Tagged.ITaggedContent taggedContent = document.TaggedContent;

    // Set Title and Language for Document
    taggedContent.SetTitle("Tagged Pdf Document");
    taggedContent.SetLanguage("en-US");

    // Get Root Structure Element
    Aspose.Pdf.LogicalStructure.StructureElement rootElement = taggedContent.RootElement;

    Aspose.Pdf.LogicalStructure.HeaderElement h1 = taggedContent.CreateHeaderElement(1);
    Aspose.Pdf.LogicalStructure.HeaderElement h2 = taggedContent.CreateHeaderElement(2);
    Aspose.Pdf.LogicalStructure.HeaderElement h3 = taggedContent.CreateHeaderElement(3);
    Aspose.Pdf.LogicalStructure.HeaderElement h4 = taggedContent.CreateHeaderElement(4);
    Aspose.Pdf.LogicalStructure.HeaderElement h5 = taggedContent.CreateHeaderElement(5);
    Aspose.Pdf.LogicalStructure.HeaderElement h6 = taggedContent.CreateHeaderElement(6);
    rootElement.AppendChild(h1);
    rootElement.AppendChild(h2);
    rootElement.AppendChild(h3);
    rootElement.AppendChild(h4);
    rootElement.AppendChild(h5);
    rootElement.AppendChild(h6);

    Aspose.Pdf.LogicalStructure.SpanElement spanH11 = taggedContent.CreateSpanElement();
    spanH11.SetText("H1. ");
    h1.AppendChild(spanH11);
    Aspose.Pdf.LogicalStructure.SpanElement spanH12 = taggedContent.CreateSpanElement();
    spanH12.SetText("Level 1 Header");
    h1.AppendChild(spanH12);

    Aspose.Pdf.LogicalStructure.SpanElement spanH21 = taggedContent.CreateSpanElement();
    spanH21.SetText("H2. ");
    h2.AppendChild(spanH21);
    Aspose.Pdf.LogicalStructure.SpanElement spanH22 = taggedContent.CreateSpanElement();
    spanH22.SetText("Level 2 Header");
    h2.AppendChild(spanH22);

    Aspose.Pdf.LogicalStructure.SpanElement spanH31 = taggedContent.CreateSpanElement();
    spanH31.SetText("H3. ");
    h3.AppendChild(spanH31);
    Aspose.Pdf.LogicalStructure.SpanElement spanH32 = taggedContent.CreateSpanElement();
    spanH32.SetText("Level 3 Header");
    h3.AppendChild(spanH32);

    Aspose.Pdf.LogicalStructure.SpanElement spanH41 = taggedContent.CreateSpanElement();
    spanH41.SetText("H4. ");
    h4.AppendChild(spanH41);
    Aspose.Pdf.LogicalStructure.SpanElement spanH42 = taggedContent.CreateSpanElement();
    spanH42.SetText("Level 4 Header");
    h4.AppendChild(spanH42);

    Aspose.Pdf.LogicalStructure.SpanElement spanH51 = taggedContent.CreateSpanElement();
    spanH51.SetText("H5. ");
    h5.AppendChild(spanH51);
    Aspose.Pdf.LogicalStructure.SpanElement spanH52 = taggedContent.CreateSpanElement();
    spanH52.SetText("Level 5 Header");
    h5.AppendChild(spanH52);

    Aspose.Pdf.LogicalStructure.SpanElement spanH61 = taggedContent.CreateSpanElement();
    spanH61.SetText("H6. ");
    h6.AppendChild(spanH61);
    Aspose.Pdf.LogicalStructure.SpanElement spanH62 = taggedContent.CreateSpanElement();
    spanH62.SetText("Level 6 Header");
    h6.AppendChild(spanH62);

    Aspose.Pdf.LogicalStructure.ParagraphElement p = taggedContent.CreateParagraphElement();
    p.SetText("P. ");
    rootElement.AppendChild(p);
    Aspose.Pdf.LogicalStructure.SpanElement span1 = taggedContent.CreateSpanElement();
    span1.SetText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. ");
    p.AppendChild(span1);
    Aspose.Pdf.LogicalStructure.SpanElement span2 = taggedContent.CreateSpanElement();
    span2.SetText("Aenean nec lectus ac sem faucibus imperdiet. ");
    p.AppendChild(span2);
    Aspose.Pdf.LogicalStructure.SpanElement span3 = taggedContent.CreateSpanElement();
    span3.SetText("Sed ut erat ac magna ullamcorper hendrerit. ");
    p.AppendChild(span3);
    Aspose.Pdf.LogicalStructure.SpanElement span4 = taggedContent.CreateSpanElement();
    span4.SetText("Cras pellentesque libero semper, gravida magna sed, luctus leo. ");
    p.AppendChild(span4);
    Aspose.Pdf.LogicalStructure.SpanElement span5 = taggedContent.CreateSpanElement();
    span5.SetText("Fusce lectus odio, laoreet nec ullamcorper ut, molestie eu elit. ");
    p.AppendChild(span5);
    Aspose.Pdf.LogicalStructure.SpanElement span6 = taggedContent.CreateSpanElement();
    span6.SetText("Interdum et malesuada fames ac ante ipsum primis in faucibus. ");
    p.AppendChild(span6);
    Aspose.Pdf.LogicalStructure.SpanElement span7 = taggedContent.CreateSpanElement();
    span7.SetText("Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat sem tristique eget. ");
    p.AppendChild(span7);
    Aspose.Pdf.LogicalStructure.SpanElement span8 = taggedContent.CreateSpanElement();
    span8.SetText("Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper pellentesque justo rhoncus accumsan. ");
    p.AppendChild(span8);
    Aspose.Pdf.LogicalStructure.SpanElement span9 = taggedContent.CreateSpanElement();
    span9.SetText("Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus ac iaculis eget, tempus et magna. Sed non consectetur elit. ");
    p.AppendChild(span9);
    Aspose.Pdf.LogicalStructure.SpanElement span10 = taggedContent.CreateSpanElement();
    span10.SetText("Sed vulputate, quam sed lacinia luctus, ipsum nibh fringilla purus, vitae posuere risus odio id massa. Cras sed venenatis lacus.");
    p.AppendChild(span10);

    // Save Tagged PDF Document
    document.Save(dataDir + "InlineStructureElements_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Установка пользовательского имени тега

Чтобы установить пользовательское имя тега для элементов помеченного PDF-документа, Aspose.PDF предлагает метод [SetTag](https://reference.aspose.com/pdf/ru/net/aspose.pdf.logicalstructure/structureelement/methods/settag) класса StructureElement для элементов. Следующий фрагмент кода показывает, как установить пользовательское имя тега:

{{< tabs tabID="5" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetTagName()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF Document
    using (var document = new Aspose.Pdf.Document())
    {
        // Get Content for work with Tagged PDF
        Aspose.Pdf.Tagged.ITaggedContent taggedContent = document.TaggedContent;

        // Set Title and Language for Document
        taggedContent.SetTitle("Tagged Pdf Document");
        taggedContent.SetLanguage("en-US");

        // Create Logical Structure Elements
        Aspose.Pdf.LogicalStructure.SectElement sect = taggedContent.CreateSectElement();
        taggedContent.RootElement.AppendChild(sect);

        Aspose.Pdf.LogicalStructure.ParagraphElement p1 = taggedContent.CreateParagraphElement();
        Aspose.Pdf.LogicalStructure.ParagraphElement p2 = taggedContent.CreateParagraphElement();
        Aspose.Pdf.LogicalStructure.ParagraphElement p3 = taggedContent.CreateParagraphElement();
        Aspose.Pdf.LogicalStructure.ParagraphElement p4 = taggedContent.CreateParagraphElement();

        p1.SetText("P1. ");
        p2.SetText("P2. ");
        p3.SetText("P3. ");
        p4.SetText("P4. ");

        p1.SetTag("P1");
        p2.SetTag("Para");
        p3.SetTag("Para");
        p4.SetTag("Paragraph");

        sect.AppendChild(p1);
        sect.AppendChild(p2);
        sect.AppendChild(p3);
        sect.AppendChild(p4);

        Aspose.Pdf.LogicalStructure.SpanElement span1 = taggedContent.CreateSpanElement();
        Aspose.Pdf.LogicalStructure.SpanElement span2 = taggedContent.CreateSpanElement();
        Aspose.Pdf.LogicalStructure.SpanElement span3 = taggedContent.CreateSpanElement();
        Aspose.Pdf.LogicalStructure.SpanElement span4 = taggedContent.CreateSpanElement();

        span1.SetText("Span 1.");
        span2.SetText("Span 2.");
        span3.SetText("Span 3.");
        span4.SetText("Span 4.");

        span1.SetTag("SPAN");
        span2.SetTag("Sp");
        span3.SetTag("Sp");
        span4.SetTag("TheSpan");

        p1.AppendChild(span1);
        p2.AppendChild(span2);
        p3.AppendChild(span3);
        p4.AppendChild(span4);

        // Save Tagged PDF Document
        document.Save(dataDir + "CustomTag_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetTagName()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF Document
    using var document = new Aspose.Pdf.Document();

    // Get Content for work with Tagged PDF
    Aspose.Pdf.Tagged.ITaggedContent taggedContent = document.TaggedContent;

    // Set Title and Language for Document
    taggedContent.SetTitle("Tagged Pdf Document");
    taggedContent.SetLanguage("en-US");

    // Create Logical Structure Elements
    Aspose.Pdf.LogicalStructure.SectElement sect = taggedContent.CreateSectElement();
    taggedContent.RootElement.AppendChild(sect);

    Aspose.Pdf.LogicalStructure.ParagraphElement p1 = taggedContent.CreateParagraphElement();
    Aspose.Pdf.LogicalStructure.ParagraphElement p2 = taggedContent.CreateParagraphElement();
    Aspose.Pdf.LogicalStructure.ParagraphElement p3 = taggedContent.CreateParagraphElement();
    Aspose.Pdf.LogicalStructure.ParagraphElement p4 = taggedContent.CreateParagraphElement();

    p1.SetText("P1. ");
    p2.SetText("P2. ");
    p3.SetText("P3. ");
    p4.SetText("P4. ");

    p1.SetTag("P1");
    p2.SetTag("Para");
    p3.SetTag("Para");
    p4.SetTag("Paragraph");

    sect.AppendChild(p1);
    sect.AppendChild(p2);
    sect.AppendChild(p3);
    sect.AppendChild(p4);

    Aspose.Pdf.LogicalStructure.SpanElement span1 = taggedContent.CreateSpanElement();
    Aspose.Pdf.LogicalStructure.SpanElement span2 = taggedContent.CreateSpanElement();
    Aspose.Pdf.LogicalStructure.SpanElement span3 = taggedContent.CreateSpanElement();
    Aspose.Pdf.LogicalStructure.SpanElement span4 = taggedContent.CreateSpanElement();

    span1.SetText("Span 1.");
    span2.SetText("Span 2.");
    span3.SetText("Span 3.");
    span4.SetText("Span 4.");

    span1.SetTag("SPAN");
    span2.SetTag("Sp");
    span3.SetTag("Sp");
    span4.SetTag("TheSpan");

    p1.AppendChild(span1);
    p2.AppendChild(span2);
    p3.AppendChild(span3);
    p4.AppendChild(span4);

    // Save Tagged PDF Document
    document.Save(dataDir + "CustomTag_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Добавление элемента структуры в элементы

**Эта функция поддерживается версией 19.4 или выше.**

Чтобы установить элементы структуры ссылок в помеченном PDF-документе, Aspose.PDF предлагает метод [CreateLinkElement](https://reference.aspose.com/pdf/ru/net/aspose.pdf.tagged/itaggedcontent/methods/createlinkelement) интерфейса [ITaggedContent](https://reference.aspose.com/pdf/ru/net/aspose.pdf.tagged/itaggedcontent). Следующий фрагмент кода показывает, как установить элементы структуры в абзаце с текстом помеченного PDF-документа:

{{< tabs tabID="6" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetElements()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        Aspose.Pdf.Tagged.ITaggedContent taggedContent = document.TaggedContent;

        // Setting Title and Nature Language for document
        taggedContent.SetTitle("Link Elements Example");
        taggedContent.SetLanguage("en-US");

        // Getting Root structure element (Document structure element)
        Aspose.Pdf.LogicalStructure.StructureElement rootElement = taggedContent.RootElement;

        Aspose.Pdf.LogicalStructure.ParagraphElement p1 = taggedContent.CreateParagraphElement();
        rootElement.AppendChild(p1);
        Aspose.Pdf.LogicalStructure.LinkElement link1 = taggedContent.CreateLinkElement();
        p1.AppendChild(link1);
        link1.Hyperlink = new Aspose.Pdf.WebHyperlink("http://google.com");
        link1.SetText("Google");
        link1.AlternateDescriptions = "Link to Google";

        Aspose.Pdf.LogicalStructure.ParagraphElement p2 = taggedContent.CreateParagraphElement();
        rootElement.AppendChild(p2);
        Aspose.Pdf.LogicalStructure.LinkElement link2 = taggedContent.CreateLinkElement();
        p2.AppendChild(link2);
        link2.Hyperlink = new Aspose.Pdf.WebHyperlink("http://google.com");
        Aspose.Pdf.LogicalStructure.SpanElement span2 = taggedContent.CreateSpanElement();
        span2.SetText("Google");
        link2.AppendChild(span2);
        link2.AlternateDescriptions = "Link to Google";

        Aspose.Pdf.LogicalStructure.ParagraphElement p3 = taggedContent.CreateParagraphElement();
        rootElement.AppendChild(p3);
        Aspose.Pdf.LogicalStructure.LinkElement link3 = taggedContent.CreateLinkElement();
        p3.AppendChild(link3);
        link3.Hyperlink = new Aspose.Pdf.WebHyperlink("http://google.com");
        Aspose.Pdf.LogicalStructure.SpanElement span31 = taggedContent.CreateSpanElement();
        span31.SetText("G");
        Aspose.Pdf.LogicalStructure.SpanElement span32 = taggedContent.CreateSpanElement();
        span32.SetText("oogle");
        link3.AppendChild(span31);
        link3.SetText("-");
        link3.AppendChild(span32);
        link3.AlternateDescriptions = "Link to Google";

        Aspose.Pdf.LogicalStructure.ParagraphElement p4 = taggedContent.CreateParagraphElement();
        rootElement.AppendChild(p4);
        Aspose.Pdf.LogicalStructure.LinkElement link4 = taggedContent.CreateLinkElement();
        p4.AppendChild(link4);
        link4.Hyperlink = new Aspose.Pdf.WebHyperlink("http://google.com");
        link4.SetText("The multiline link: Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google");
        link4.AlternateDescriptions = "Link to Google (multiline)";

        Aspose.Pdf.LogicalStructure.ParagraphElement p5 = taggedContent.CreateParagraphElement();
        rootElement.AppendChild(p5);
        Aspose.Pdf.LogicalStructure.LinkElement link5 = taggedContent.CreateLinkElement();
        p5.AppendChild(link5);
        link5.Hyperlink = new Aspose.Pdf.WebHyperlink("http://google.com");
        Aspose.Pdf.LogicalStructure.FigureElement figure5 = taggedContent.CreateFigureElement();
        figure5.SetImage(dataDir + "google-icon-512.png", 1200);
        figure5.AlternativeText = "Google icon";
        Aspose.Pdf.LogicalStructure.StructureAttributes linkLayoutAttributes = link5.Attributes.GetAttributes(Aspose.Pdf.LogicalStructure.AttributeOwnerStandard.Layout);
        var placementAttribute = new Aspose.Pdf.LogicalStructure.StructureAttribute(Aspose.Pdf.LogicalStructure.AttributeKey.Placement);
        placementAttribute.SetNameValue(Aspose.Pdf.LogicalStructure.AttributeName.Placement_Block);
        linkLayoutAttributes.SetAttribute(placementAttribute);
        link5.AppendChild(figure5);
        link5.AlternateDescriptions = "Link to Google";

        // Save Tagged PDF Document
        document.Save(dataDir + "LinkStructureElements_out.pdf");
    }

    // Check PDF/UA compliance
    using (var document = new Aspose.Pdf.Document(dataDir + "LinkStructureElements_out.pdf"))
    {
        bool isPdfUaCompliance = document.Validate(dataDir + "LinkStructureElements_log.xml", Aspose.Pdf.PdfFormat.PDF_UA_1);
        Console.WriteLine(String.Format("PDF/UA compliance: {0}", isPdfUaCompliance));
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetElements()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using var document1 = new Aspose.Pdf.Document();
    Aspose.Pdf.Tagged.ITaggedContent taggedContent = document1.TaggedContent;

    // Setting Title and Nature Language for document
    taggedContent.SetTitle("Link Elements Example");
    taggedContent.SetLanguage("en-US");

    // Getting Root structure element (Document structure element)
    Aspose.Pdf.LogicalStructure.StructureElement rootElement = taggedContent.RootElement;

    Aspose.Pdf.LogicalStructure.ParagraphElement p1 = taggedContent.CreateParagraphElement();
    rootElement.AppendChild(p1);
    Aspose.Pdf.LogicalStructure.LinkElement link1 = taggedContent.CreateLinkElement();
    p1.AppendChild(link1);
    link1.Hyperlink = new Aspose.Pdf.WebHyperlink("http://google.com");
    link1.SetText("Google");
    link1.AlternateDescriptions = "Link to Google";

    Aspose.Pdf.LogicalStructure.ParagraphElement p2 = taggedContent.CreateParagraphElement();
    rootElement.AppendChild(p2);
    Aspose.Pdf.LogicalStructure.LinkElement link2 = taggedContent.CreateLinkElement();
    p2.AppendChild(link2);
    link2.Hyperlink = new Aspose.Pdf.WebHyperlink("http://google.com");
    Aspose.Pdf.LogicalStructure.SpanElement span2 = taggedContent.CreateSpanElement();
    span2.SetText("Google");
    link2.AppendChild(span2);
    link2.AlternateDescriptions = "Link to Google";

    Aspose.Pdf.LogicalStructure.ParagraphElement p3 = taggedContent.CreateParagraphElement();
    rootElement.AppendChild(p3);
    Aspose.Pdf.LogicalStructure.LinkElement link3 = taggedContent.CreateLinkElement();
    p3.AppendChild(link3);
    link3.Hyperlink = new Aspose.Pdf.WebHyperlink("http://google.com");
    Aspose.Pdf.LogicalStructure.SpanElement span31 = taggedContent.CreateSpanElement();
    span31.SetText("G");
    Aspose.Pdf.LogicalStructure.SpanElement span32 = taggedContent.CreateSpanElement();
    span32.SetText("oogle");
    link3.AppendChild(span31);
    link3.SetText("-");
    link3.AppendChild(span32);
    link3.AlternateDescriptions = "Link to Google";

    Aspose.Pdf.LogicalStructure.ParagraphElement p4 = taggedContent.CreateParagraphElement();
    rootElement.AppendChild(p4);
    Aspose.Pdf.LogicalStructure.LinkElement link4 = taggedContent.CreateLinkElement();
    p4.AppendChild(link4);
    link4.Hyperlink = new Aspose.Pdf.WebHyperlink("http://google.com");
    link4.SetText("The multiline link: Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google");
    link4.AlternateDescriptions = "Link to Google (multiline)";

    Aspose.Pdf.LogicalStructure.ParagraphElement p5 = taggedContent.CreateParagraphElement();
    rootElement.AppendChild(p5);
    Aspose.Pdf.LogicalStructure.LinkElement link5 = taggedContent.CreateLinkElement();
    p5.AppendChild(link5);
    link5.Hyperlink = new Aspose.Pdf.WebHyperlink("http://google.com");
    Aspose.Pdf.LogicalStructure.FigureElement figure5 = taggedContent.CreateFigureElement();
    figure5.SetImage(dataDir + "google-icon-512.png", 1200);
    figure5.AlternativeText = "Google icon";
    Aspose.Pdf.LogicalStructure.StructureAttributes linkLayoutAttributes = link5.Attributes.GetAttributes(Aspose.Pdf.LogicalStructure.AttributeOwnerStandard.Layout);
    var placementAttribute = new Aspose.Pdf.LogicalStructure.StructureAttribute(Aspose.Pdf.LogicalStructure.AttributeKey.Placement);
    placementAttribute.SetNameValue(Aspose.Pdf.LogicalStructure.AttributeName.Placement_Block);
    linkLayoutAttributes.SetAttribute(placementAttribute);
    link5.AppendChild(figure5);
    link5.AlternateDescriptions = "Link to Google";

    // Save Tagged PDF Document
    document1.Save(dataDir + "LinkStructureElements_out.pdf");

    // Check PDF/UA compliance
    using var document2 = new Aspose.Pdf.Document(dataDir + "LinkStructureElements_out.pdf");
    bool isPdfUaCompliance = document2.Validate(dataDir + "LinkStructureElements_log.xml", Aspose.Pdf.PdfFormat.PDF_UA_1);
    Console.WriteLine(String.Format("PDF/UA compliance: {0}", isPdfUaCompliance));
}
```
{{< /tab >}}
{{< /tabs >}}

## Установка элемента структуры ссылки

**Эта функция поддерживается версией 19.4 или выше.**

API Aspose.PDF for .NET также позволяет добавлять элементы структуры ссылок. Следующий фрагмент кода показывает, как добавить элемент структуры ссылки в помеченный PDF-документ:

{{< tabs tabID="7" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddLinkElement()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        Aspose.Pdf.Tagged.ITaggedContent taggedContent = document.TaggedContent;

        // Setting Title and Nature Language for document
        taggedContent.SetTitle("Text Elements Example");
        taggedContent.SetLanguage("en-US");

        // Getting Root structure element (Document structure element)
        Aspose.Pdf.LogicalStructure.StructureElement rootElement = taggedContent.RootElement;

        Aspose.Pdf.LogicalStructure.ParagraphElement p1 = taggedContent.CreateParagraphElement();
        rootElement.AppendChild(p1);
        Aspose.Pdf.LogicalStructure.SpanElement span11 = taggedContent.CreateSpanElement();
        span11.SetText("Span_11");
        Aspose.Pdf.LogicalStructure.SpanElement span12 = taggedContent.CreateSpanElement();
        span12.SetText(" and Span_12.");
        p1.SetText("Paragraph with ");
        p1.AppendChild(span11);
        p1.AppendChild(span12);

        Aspose.Pdf.LogicalStructure.ParagraphElement p2 = taggedContent.CreateParagraphElement();
        rootElement.AppendChild(p2);
        Aspose.Pdf.LogicalStructure.SpanElement span21 = taggedContent.CreateSpanElement();
        span21.SetText("Span_21");
        Aspose.Pdf.LogicalStructure.SpanElement span22 = taggedContent.CreateSpanElement();
        span22.SetText("Span_22.");
        p2.AppendChild(span21);
        p2.SetText(" and ");
        p2.AppendChild(span22);

        Aspose.Pdf.LogicalStructure.ParagraphElement p3 = taggedContent.CreateParagraphElement();
        rootElement.AppendChild(p3);
        Aspose.Pdf.LogicalStructure.SpanElement span31 = taggedContent.CreateSpanElement();
        span31.SetText("Span_31");
        Aspose.Pdf.LogicalStructure.SpanElement span32 = taggedContent.CreateSpanElement();
        span32.SetText(" and Span_32");
        p3.AppendChild(span31);
        p3.AppendChild(span32);
        p3.SetText(".");

        Aspose.Pdf.LogicalStructure.ParagraphElement p4 = taggedContent.CreateParagraphElement();
        rootElement.AppendChild(p4);
        Aspose.Pdf.LogicalStructure.SpanElement span41 = taggedContent.CreateSpanElement();
        Aspose.Pdf.LogicalStructure.SpanElement span411 = taggedContent.CreateSpanElement();
        span411.SetText("Span_411, ");
        span41.SetText("Span_41, ");
        span41.AppendChild(span411);
        Aspose.Pdf.LogicalStructure.SpanElement span42 = taggedContent.CreateSpanElement();
        Aspose.Pdf.LogicalStructure.SpanElement span421 = taggedContent.CreateSpanElement();
        span421.SetText("Span 421 and ");
        span42.AppendChild(span421);
        span42.SetText("Span_42");
        p4.AppendChild(span41);
        p4.AppendChild(span42);
        p4.SetText(".");

        // Save Tagged PDF Document
        document.Save(dataDir + "AddStructureElementIntoElement_out.pdf");
    }

    // Check PDF/UA compliance
    using (var document = new Aspose.Pdf.Document(dataDir + "AddStructureElementIntoElement_out.pdf"))
    {
        bool isPdfUaCompliance = document.Validate(dataDir + "46144_log.xml", Aspose.Pdf.PdfFormat.PDF_UA_1);
        Console.WriteLine(String.Format("PDF/UA compliance: {0}", isPdfUaCompliance));
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddLinkElement()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using var document1 = new Aspose.Pdf.Document();
    Aspose.Pdf.Tagged.ITaggedContent taggedContent = document1.TaggedContent;

    // Setting Title and Nature Language for document
    taggedContent.SetTitle("Text Elements Example");
    taggedContent.SetLanguage("en-US");

    // Getting Root structure element (Document structure element)
    Aspose.Pdf.LogicalStructure.StructureElement rootElement = taggedContent.RootElement;

    Aspose.Pdf.LogicalStructure.ParagraphElement p1 = taggedContent.CreateParagraphElement();
    rootElement.AppendChild(p1);
    Aspose.Pdf.LogicalStructure.SpanElement span11 = taggedContent.CreateSpanElement();
    span11.SetText("Span_11");
    Aspose.Pdf.LogicalStructure.SpanElement span12 = taggedContent.CreateSpanElement();
    span12.SetText(" and Span_12.");
    p1.SetText("Paragraph with ");
    p1.AppendChild(span11);
    p1.AppendChild(span12);

    Aspose.Pdf.LogicalStructure.ParagraphElement p2 = taggedContent.CreateParagraphElement();
    rootElement.AppendChild(p2);
    Aspose.Pdf.LogicalStructure.SpanElement span21 = taggedContent.CreateSpanElement();
    span21.SetText("Span_21");
    Aspose.Pdf.LogicalStructure.SpanElement span22 = taggedContent.CreateSpanElement();
    span22.SetText("Span_22.");
    p2.AppendChild(span21);
    p2.SetText(" and ");
    p2.AppendChild(span22);

    Aspose.Pdf.LogicalStructure.ParagraphElement p3 = taggedContent.CreateParagraphElement();
    rootElement.AppendChild(p3);
    Aspose.Pdf.LogicalStructure.SpanElement span31 = taggedContent.CreateSpanElement();
    span31.SetText("Span_31");
    Aspose.Pdf.LogicalStructure.SpanElement span32 = taggedContent.CreateSpanElement();
    span32.SetText(" and Span_32");
    p3.AppendChild(span31);
    p3.AppendChild(span32);
    p3.SetText(".");

    Aspose.Pdf.LogicalStructure.ParagraphElement p4 = taggedContent.CreateParagraphElement();
    rootElement.AppendChild(p4);
    Aspose.Pdf.LogicalStructure.SpanElement span41 = taggedContent.CreateSpanElement();
    Aspose.Pdf.LogicalStructure.SpanElement span411 = taggedContent.CreateSpanElement();
    span411.SetText("Span_411, ");
    span41.SetText("Span_41, ");
    span41.AppendChild(span411);
    Aspose.Pdf.LogicalStructure.SpanElement span42 = taggedContent.CreateSpanElement();
    Aspose.Pdf.LogicalStructure.SpanElement span421 = taggedContent.CreateSpanElement();
    span421.SetText("Span 421 and ");
    span42.AppendChild(span421);
    span42.SetText("Span_42");
    p4.AppendChild(span41);
    p4.AppendChild(span42);
    p4.SetText(".");

    // Save Tagged PDF Document
    document1.Save(dataDir + "AddStructureElementIntoElement_out.pdf");

    // Check PDF/UA compliance
    using var document2 = new Aspose.Pdf.Document(dataDir + "AddStructureElementIntoElement_out.pdf");
    bool isPdfUaCompliance = document2.Validate(dataDir + "46144_log.xml", Aspose.Pdf.PdfFormat.PDF_UA_1);
    Console.WriteLine(String.Format("PDF/UA compliance: {0}", isPdfUaCompliance));
}
```
{{< /tab >}}
{{< /tabs >}}

## Установка элемента структуры заметки

API Aspose.PDF for .NET также позволяет добавлять [NoteElement](https://reference.aspose.com/pdf/ru/net/aspose.pdf.logicalstructure/noteelement) в помеченный PDF-документ. Следующий фрагмент кода показывает, как добавить элемент заметки в помеченный PDF-документ:

{{< tabs tabID="8" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetNoteElement()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF Document
    using (var document = new Aspose.Pdf.Document())
    {
        Aspose.Pdf.Tagged.ITaggedContent taggedContent = document.TaggedContent;

        taggedContent.SetTitle("Sample of Note Elements");
        taggedContent.SetLanguage("en-US");

        // Add Paragraph Element
        Aspose.Pdf.LogicalStructure.ParagraphElement paragraph = taggedContent.CreateParagraphElement();
        taggedContent.RootElement.AppendChild(paragraph);

        // Add NoteElement
        Aspose.Pdf.LogicalStructure.NoteElement note1 = taggedContent.CreateNoteElement();
        paragraph.AppendChild(note1);
        note1.SetText("Note with auto generate ID. ");

        // Add NoteElement
        Aspose.Pdf.LogicalStructure.NoteElement note2 = taggedContent.CreateNoteElement();
        paragraph.AppendChild(note2);
        note2.SetText("Note with ID = 'note_002'. ");
        note2.SetId("note_002");

        // Add NoteElement
        Aspose.Pdf.LogicalStructure.NoteElement note3 = taggedContent.CreateNoteElement();
        paragraph.AppendChild(note3);
        note3.SetText("Note with ID = 'note_003'. ");
        note3.SetId("note_003");

        // Must throw exception - Aspose.Pdf.Tagged.TaggedException : Structure element with ID='note_002' already exists
        //note3.SetId("note_002");

        // Resultant document does not compliance to PDF/UA If ClearId() used for Note Structure Element
        //note3.ClearId();

        // Save Tagged PDF Document
        document.Save(dataDir + "SetNoteElement_out.pdf");
    }

    // Check PDF/UA compliance
    using (var document = new Aspose.Pdf.Document(dataDir + "SetNoteElement_out.pdf"))
    {
        bool isPdfUaCompliance = document.Validate(dataDir + "SetNoteElement_log.xml", Aspose.Pdf.PdfFormat.PDF_UA_1);
        Console.WriteLine(String.Format("PDF/UA compliance: {0}", isPdfUaCompliance));
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetNoteElement()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF Document
    using var document1 = new Aspose.Pdf.Document();
    Aspose.Pdf.Tagged.ITaggedContent taggedContent = document1.TaggedContent;

    taggedContent.SetTitle("Sample of Note Elements");
    taggedContent.SetLanguage("en-US");

    // Add Paragraph Element
    Aspose.Pdf.LogicalStructure.ParagraphElement paragraph = taggedContent.CreateParagraphElement();
    taggedContent.RootElement.AppendChild(paragraph);

    // Add NoteElement
    Aspose.Pdf.LogicalStructure.NoteElement note1 = taggedContent.CreateNoteElement();
    paragraph.AppendChild(note1);
    note1.SetText("Note with auto generate ID. ");

    // Add NoteElement
    Aspose.Pdf.LogicalStructure.NoteElement note2 = taggedContent.CreateNoteElement();
    paragraph.AppendChild(note2);
    note2.SetText("Note with ID = 'note_002'. ");
    note2.SetId("note_002");

    // Add NoteElement
    Aspose.Pdf.LogicalStructure.NoteElement note3 = taggedContent.CreateNoteElement();
    paragraph.AppendChild(note3);
    note3.SetText("Note with ID = 'note_003'. ");
    note3.SetId("note_003");

    // Must throw exception - Aspose.Pdf.Tagged.TaggedException : Structure element with ID='note_002' already exists
    //note3.SetId("note_002");

    // Resultant document does not compliance to PDF/UA If ClearId() used for Note Structure Element
    //note3.ClearId();

    // Save Tagged PDF Document
    document1.Save(dataDir + "SetNoteElement_out.pdf");

    // Check PDF/UA compliance
    using var document2 = new Aspose.Pdf.Document(dataDir + "SetNoteElement_out.pdf");
    bool isPdfUaCompliance = document2.Validate(dataDir + "SetNoteElement_log.xml", Aspose.Pdf.PdfFormat.PDF_UA_1);
    Console.WriteLine(String.Format("PDF/UA compliance: {0}", isPdfUaCompliance));
}
```
{{< /tab >}}
{{< /tabs >}}

## Установка языка и заголовка

**Эта функция поддерживается версией 19.6 или выше.**

API Aspose.PDF for .NET также позволяет устанавливать язык и заголовок для документа в соответствии со спецификацией PDF/UA. Язык может быть установлен как для всего документа, так и для его отдельных структурных элементов. Следующий фрагмент кода показывает, как установить язык и заголовок в помеченном PDF-документе:

{{< tabs tabID="9" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetLanguageAndTitle()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF Document
    using (var document = new Aspose.Pdf.Document())
    {
        // Get TaggedContent
        Aspose.Pdf.Tagged.ITaggedContent taggedContent = document.TaggedContent;

        // Set Title and Language
        taggedContent.SetTitle("Example Tagged Document");
        taggedContent.SetLanguage("en-US");

        // Header (en-US, inherited from document)
        Aspose.Pdf.LogicalStructure.HeaderElement h1 = taggedContent.CreateHeaderElement(1);
        h1.SetText("Phrase on different languages");
        taggedContent.RootElement.AppendChild(h1);

        // Paragraph (English)
        Aspose.Pdf.LogicalStructure.ParagraphElement pEN = taggedContent.CreateParagraphElement();
        pEN.SetText("Hello, World!");
        pEN.Language = "en-US";
        taggedContent.RootElement.AppendChild(pEN);

        // Paragraph (German)
        Aspose.Pdf.LogicalStructure.ParagraphElement pDE = taggedContent.CreateParagraphElement();
        pDE.SetText("Hallo Welt!");
        pDE.Language = "de-DE";
        taggedContent.RootElement.AppendChild(pDE);

        // Paragraph (French)
        Aspose.Pdf.LogicalStructure.ParagraphElement pFR = taggedContent.CreateParagraphElement();
        pFR.SetText("Bonjour le monde!");
        pFR.Language = "fr-FR";
        taggedContent.RootElement.AppendChild(pFR);

        // Paragraph (Spanish)
        Aspose.Pdf.LogicalStructure.ParagraphElement pSP = taggedContent.CreateParagraphElement();
        pSP.SetText("¡Hola Mundo!");
        pSP.Language = "es-ES";
        taggedContent.RootElement.AppendChild(pSP);

        // Save Tagged PDF Document
        document.Save(dataDir + "SetupLanguageAndTitle_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetLanguageAndTitle()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF Document
    using var document = new Aspose.Pdf.Document();

    // Get TaggedContent
    Aspose.Pdf.Tagged.ITaggedContent taggedContent = document.TaggedContent;

    // Set Title and Language
    taggedContent.SetTitle("Example Tagged Document");
    taggedContent.SetLanguage("en-US");

    // Header (en-US, inherited from document)
    Aspose.Pdf.LogicalStructure.HeaderElement h1 = taggedContent.CreateHeaderElement(1);
    h1.SetText("Phrase on different languages");
    taggedContent.RootElement.AppendChild(h1);

    // Paragraph (English)
    Aspose.Pdf.LogicalStructure.ParagraphElement pEN = taggedContent.CreateParagraphElement();
    pEN.SetText("Hello, World!");
    pEN.Language = "en-US";
    taggedContent.RootElement.AppendChild(pEN);

    // Paragraph (German)
    Aspose.Pdf.LogicalStructure.ParagraphElement pDE = taggedContent.CreateParagraphElement();
    pDE.SetText("Hallo Welt!");
    pDE.Language = "de-DE";
    taggedContent.RootElement.AppendChild(pDE);

    // Paragraph (French)
    Aspose.Pdf.LogicalStructure.ParagraphElement pFR = taggedContent.CreateParagraphElement();
    pFR.SetText("Bonjour le monde!");
    pFR.Language = "fr-FR";
    taggedContent.RootElement.AppendChild(pFR);

    // Paragraph (Spanish)
    Aspose.Pdf.LogicalStructure.ParagraphElement pSP = taggedContent.CreateParagraphElement();
    pSP.SetText("¡Hola Mundo!");
    pSP.Language = "es-ES";
    taggedContent.RootElement.AppendChild(pSP);

    // Save Tagged PDF Document
    document.Save(dataDir + "SetupLanguageAndTitle.pdf");
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