---
title: Ajouter un en-tête et un pied de page au PDF
linktitle: Ajouter un en-tête et un pied de page au PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /fr/net/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF for .NET vous permet d'ajouter des en-têtes et des pieds de page à votre fichier PDF en utilisant la classe TextStamp.
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
    "abstract": "Aspose.PDF for .NET introduit une fonctionnalité puissante qui permet aux utilisateurs d'enrichir leurs documents PDF en ajoutant des en-têtes et des pieds de page personnalisables. En utilisant les classes TextStamp et ImageStamp, les développeurs peuvent facilement intégrer à la fois du texte et des images, adaptant leur placement et leur apparence pour s'adapter à divers formats et styles de documents. Cela améliore le professionnalisme et la lisibilité des documents, ce qui le rend idéal pour les rapports, les factures et autres communications formelles.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1123",
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
    "description": "Aspose.PDF for .NET vous permet d'ajouter des en-têtes et des pieds de page à votre fichier PDF en utilisant la classe TextStamp."
}
</script>

**Aspose.PDF for .NET** vous permet d'ajouter des en-têtes et des pieds de page à un fichier PDF existant. Vous pouvez insérer à la fois des images et du texte dans le document.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

## Ajouter des en-têtes et des pieds de page en tant que fragments de texte

Le code suivant montre comment ajouter des en-têtes et des pieds de page en tant que fragments de texte dans un PDF en utilisant C#.

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
            header.Margin = new MarginInfo
            {
                Left = 50,
                Top = 20
            };
            
            // Set footer margin
            footer.Margin = new MarginInfo
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
        header.Margin = new MarginInfo
        {
            Left = 50,
            Top = 20
        };
    
        // Set footer margin
        footer.Margin = new MarginInfo
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


## Ajouter des en-têtes et des pieds de page en tant que fragments HTML

Le code suivant montre comment ajouter des en-têtes et des pieds de page en tant que fragments HTML à un PDF en utilisant C#.

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
            header.Margin = new MarginInfo
            {
                Left = 50,
                Top = 20
            };
            
            // Set footer margin
            footer.Margin = new MarginInfo
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
        header.Margin = new MarginInfo
        {
            Left = 50,
            Top = 20
        };
    
        // Set footer margin
        footer.Margin = new MarginInfo
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

## Ajouter des en-têtes et des pieds de page en tant qu'images

Le code suivant montre comment ajouter des en-têtes et des pieds de page en tant qu'images à un PDF en utilisant C#.

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
            header.Margin = new MarginInfo
            {
                Left = 50
            };
            
            // Set footer margin
            footer.Margin = new MarginInfo
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
        header.Margin = new MarginInfo
        {
            Left = 50
        };
            
        // Set footer margin
        footer.Margin = new MarginInfo
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