---
title: Добавить заголовок и нижний колонтитул в PDF
linktitle: Добавить заголовок и нижний колонтитул в PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /ru/net/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF for .NET позволяет добавлять заголовки и нижние колонтитулы в ваш PDF-файл с помощью класса TextStamp.
lastmod: "2022-02-17"
sitemap:
changefreq: "monthly"
priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Header and Footer to PDF",
    "alternativeHeadline": "Add Custom Headers and Footers to PDF Files",
    "abstract": "Aspose.PDF for .NET представляет собой мощную функцию, которая позволяет пользователям обогащать свои PDF-документы, добавляя настраиваемые заголовки и нижние колонтитулы. Используя классы TextStamp и ImageStamp, разработчики могут легко интегрировать как текст, так и изображения, настраивая их размещение и внешний вид в соответствии с различными форматами и стилями документов. Это повышает профессионализм и читаемость документа, что делает его идеальным для отчетов, счетов и других официальных коммуникаций.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1076",
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
    "url": "/net/add-headers-and-footers-of-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-headers-and-footers-of-pdf-file/"
    },
    "dateModified": "2025-03-27",
    "description": "Aspose.PDF for .NET позволяет добавлять заголовки и нижние колонтитулы в ваш PDF-файл с помощью класса TextStamp."
}
</script>

**Aspose.PDF for .NET** позволяет добавлять заголовки и нижние колонтитулы в существующий PDF-файл. Вы можете вставлять как изображения, так и текст в документ.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

## Добавление заголовков и нижних колонтитулов в виде текстовых фрагментов

Следующий фрагмент кода демонстрирует, как добавить заголовки и нижние колонтитулы в виде текстовых фрагментов в PDF с использованием C#.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHeaderAndFooterAsText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_HeaderFooter();
  
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddHeaderAndFooterAsTextInput.pdf"))
    {
        for (var i = 1; i <= document.Pages.Count; i++)
        {
            // Create header text
            var headerText = new Aspose.Pdf.Text.TextFragment("header");
            
            // Create header
            var header = new Aspose.Pdf.HeaderFooter();
            header.Paragraphs.Add(headerText);
                    
            // Create footer text
            var footerText = new Aspose.Pdf.Text.TextFragment("footer");
            
            // Create footer 
            var footer = new Aspose.Pdf.HeaderFooter();
            footer.Paragraphs.Add(footerText);
            
            // Set header margin
            header.Margin = new Aspose.Pdf.MarginInfo
            {
                Left = 50,
                Top = 20
            };
            
            // Set footer margin
            footer.Margin = new Aspose.Pdf.MarginInfo
            {
                Left = 50,
                Top = 20
            };
                    
            // Bind the header and footer to the page
            document.Pages[i].Header = header;
            document.Pages[i].Footer = footer;
        }
            
        // Save PDF document
        document.Save(dataDir + "AddHeaderAndFooterAsText_out.pdf");
    }
}
```
{{< /tab >}}
{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHeaderAndFooterAsText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_HeaderFooter();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "AddHeaderAndFooterAsTextInput.pdf");
    
    for (var i = 1; i <= document.Pages.Count; i++)
    {
        // Create header text
        var headerText = new Aspose.Pdf.Text.TextFragment("header");
    
        // Create header
        var header = new Aspose.Pdf.HeaderFooter();
        header.Paragraphs.Add(headerText);
            
        // Create footer text
        var footerText = new Aspose.Pdf.Text.TextFragment("footer");
    
        // Create footer 
        var footer = new Aspose.Pdf.HeaderFooter();
        footer.Paragraphs.Add(footerText);
    
        // Set header margin
        header.Margin = new Aspose.Pdf.MarginInfo
        {
            Left = 50,
            Top = 20
        };
    
        // Set footer margin
        footer.Margin = new Aspose.Pdf.MarginInfo
        {
            Left = 50,
            Top = 20
        };
            
        // Bind the header and footer to the page
        document.Pages[i].Header = header;
        document.Pages[i].Footer = footer;
    }
    
    // Save PDF document
    document.Save(dataDir + "AddHeaderAndFooterAsText_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}


## Добавление заголовков и нижних колонтитулов в виде HTML-фрагментов

Следующий фрагмент кода демонстрирует, как добавить заголовки и нижние колонтитулы в виде HTML-фрагментов в PDF с использованием C#.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHeaderAndFooterAsHTML()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_HeaderFooter();
  
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddHeaderAndFooterAsHTMLInput.pdf"))
    {
        for (var i = 1; i <= document.Pages.Count; i++)
        {
            // Create header HTML
            var headerHTML = new Aspose.Pdf.HtmlFragment("<span>header</span>");
            
            // Create header
            var header = new Aspose.Pdf.HeaderFooter();
            header.Paragraphs.Add(headerHTML);
                    
            // Create footer HTML
            var footerHTML = new Aspose.Pdf.HtmlFragment("<span>footer</span>");
            
            // Create footer 
            var footer = new Aspose.Pdf.HeaderFooter();
            footer.Paragraphs.Add(footerHTML);
            
            // Set header margin
            header.Margin = new Aspose.Pdf.MarginInfo
            {
                Left = 50,
                Top = 20
            };
            
            // Set footer margin
            footer.Margin = new Aspose.Pdf.MarginInfo
            {
                Left = 50,
                Top = 20
            };
                    
            // Bind the header and footer to the page
            document.Pages[i].Header = header;
            document.Pages[i].Footer = footer;
        }
            
        // Save PDF document
        document.Save(dataDir + "AddHeaderAndFooterAsHTML_out.pdf");
    }
}
```
{{< /tab >}}
{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHeaderAndFooterAsHTML()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_HeaderFooter();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "AddHeaderAndFooterAsHTMLInput.pdf");
    
    for (var i = 1; i <= document.Pages.Count; i++)
    {
        // Create header HTML
        var headerHTML = new Aspose.Pdf.HtmlFragment("<span>header</span>");
    
        // Create header
        var header = new Aspose.Pdf.HeaderFooter();
        header.Paragraphs.Add(headerHTML);
            
        // Create footer HTML
        var footerHTML = new Aspose.Pdf.HtmlFragment("<span>footer</span>");
    
        // Create footer 
        var footer = new Aspose.Pdf.HeaderFooter();
        footer.Paragraphs.Add(footerHTML);
    
        // Set header margin
        header.Margin = new Aspose.Pdf.MarginInfo
        {
            Left = 50,
            Top = 20
        };
    
        // Set footer margin
        footer.Margin = new Aspose.Pdf.MarginInfo
        {
            Left = 50,
            Top = 20
        };
            
        // Bind the header and footer to the page
        document.Pages[i].Header = header;
        document.Pages[i].Footer = footer;
    }
    
    // Save PDF document
    document.Save(dataDir + "AddHeaderAndFooterAsHTML_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Добавление заголовков и нижних колонтитулов в виде изображений

Следующий фрагмент кода демонстрирует, как добавить заголовки и нижние колонтитулы в виде изображений в PDF с использованием C#.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHeaderAndFooterAsImage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_HeaderFooter();
  
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddHeaderAndFooterAsImageInput.pdf"))
    {
        for (var i = 1; i <= document.Pages.Count; i++)
        {
            // Create header image
            var headerImage = new Aspose.Pdf.Image();
            headerImage.File = dataDir + "ImageExample.png";
            
            // Create header
            var header = new Aspose.Pdf.HeaderFooter();
            header.Paragraphs.Add(headerImage);
                    
            // Create footer image
            var footerImage = new Aspose.Pdf.Image();
            footerImage.File = dataDir + "ImageExample.png";
            
            // Create footer 
            var footer = new Aspose.Pdf.HeaderFooter();
            footer.Paragraphs.Add(footerImage);
            
            // Set header margin
            header.Margin = new Aspose.Pdf.MarginInfo
            {
                Left = 50
            };
            
            // Set footer margin
            footer.Margin = new Aspose.Pdf.MarginInfo
            {
                Left = 50
            };
                    
            // Bind the header and footer to the page
            document.Pages[i].Header = header;
            document.Pages[i].Footer = footer;
        }
            
        // Save PDF document
        document.Save(dataDir + "AddHeaderAndFooterAsImage_out.pdf");
    }
}
```
{{< /tab >}}
{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHeaderAndFooterAsImage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_HeaderFooter();
  
    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "AddHeaderAndFooterAsImageInput.pdf");
    
    for (var i = 1; i <= document.Pages.Count; i++)
    {
        // Create header image
        var headerImage = new Aspose.Pdf.Image();
        headerImage.File = dataDir + "ImageExample.png";
            
        // Create header
        var header = new Aspose.Pdf.HeaderFooter();
        header.Paragraphs.Add(headerImage);
                    
        // Create footer image
        var footerImage = new Aspose.Pdf.Image();
        footerImage.File = dataDir + "ImageExample.png";
            
        // Create footer 
        var footer = new Aspose.Pdf.HeaderFooter();
        footer.Paragraphs.Add(footerImage);
            
        // Set header margin
        header.Margin = new Aspose.Pdf.MarginInfo
        {
            Left = 50
        };
            
        // Set footer margin
        footer.Margin = new Aspose.Pdf.MarginInfo
        {
            Left = 50
        };
                    
        // Bind the header and footer to the page
        document.Pages[i].Header = header;
        document.Pages[i].Footer = footer;
    }
            
    // Save PDF document
    document.Save(dataDir + "AddHeaderAndFooterAsImage_out.pdf");
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