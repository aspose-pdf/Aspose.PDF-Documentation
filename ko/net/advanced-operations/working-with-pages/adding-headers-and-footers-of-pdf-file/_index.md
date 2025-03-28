---
title: PDF에 헤더 및 푸터 추가
linktitle: PDF에 헤더 및 푸터 추가
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /ko/net/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF for .NET를 사용하여 TextStamp 클래스를 통해 PDF 파일에 헤더와 푸터를 추가할 수 있습니다.
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
    "alternativeHeadline": "Add Custom Headers and Footers to PDFs",
    "abstract": "Aspose.PDF for .NET는 개발자가 PDF 문서에 사용자 정의 가능한 헤더와 푸터를 손쉽게 추가할 수 있는 강력한 기능을 소개합니다. TextStamp 및 ImageStamp 클래스를 활용하여 사용자는 텍스트와 이미지를 모두 포함하여 PDF를 향상시킬 수 있으며, 이는 보고서 및 송장과 같은 공식 문서의 프레젠테이션을 크게 개선합니다. 이 기능은 전문적인 PDF를 생성하는 과정을 간소화하여 개발자에게 필수적인 도구가 됩니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1048",
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
    "description": "Aspose.PDF for .NET를 사용하여 TextStamp 클래스를 통해 PDF 파일에 헤더와 푸터를 추가할 수 있습니다."
}
</script>

**Aspose.PDF for .NET**는 기존 PDF 파일에 헤더와 푸터를 추가할 수 있게 해줍니다. 문서에 이미지와 텍스트를 모두 삽입할 수 있습니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

## 텍스트 조각으로 헤더 및 푸터 추가

다음 코드 스니펫은 C#을 사용하여 PDF에 텍스트 조각으로 헤더와 푸터를 추가하는 방법을 보여줍니다.

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


## HTML 조각으로 헤더 및 푸터 추가

다음 코드 스니펫은 C#을 사용하여 PDF에 HTML 조각으로 헤더와 푸터를 추가하는 방법을 보여줍니다.

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

## 이미지로 헤더 및 푸터 추가

다음 코드 스니펫은 C#을 사용하여 PDF에 이미지로 헤더와 푸터를 추가하는 방법을 보여줍니다.

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