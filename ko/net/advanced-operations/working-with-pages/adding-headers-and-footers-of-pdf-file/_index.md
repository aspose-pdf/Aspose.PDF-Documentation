---
title: PDF에 머리글 및 바닥글 추가
linktitle: PDF에 머리글 및 바닥글 추가
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /ko/net/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF for .NET을 사용하여 TextStamp 클래스를 통해 PDF 파일에 머리글과 바닥글을 추가할 수 있습니다.
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
    "abstract": "Aspose.PDF for .NET은 사용자가 사용자 정의 가능한 머리글과 바닥글을 추가하여 PDF 문서를 풍부하게 만들 수 있는 강력한 기능을 소개합니다. TextStamp 및 ImageStamp 클래스를 사용하여 개발자는 텍스트와 이미지를 쉽게 통합하고, 다양한 문서 형식과 스타일에 맞게 배치 및 모양을 조정할 수 있습니다. 이는 문서의 전문성과 가독성을 향상시켜 보고서, 송장 및 기타 공식 커뮤니케이션에 적합합니다.",
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
    "description": "Aspose.PDF for .NET을 사용하여 TextStamp 클래스를 통해 PDF 파일에 머리글과 바닥글을 추가할 수 있습니다."
}
</script>

**Aspose.PDF for .NET**은 기존 PDF 파일에 머리글과 바닥글을 추가할 수 있게 해줍니다. 문서에 이미지와 텍스트를 모두 삽입할 수 있습니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

## 텍스트 조각으로 머리글 및 바닥글 추가

다음 코드 스니펫은 C#을 사용하여 PDF에 텍스트 조각으로 머리글과 바닥글을 추가하는 방법을 보여줍니다.

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


## HTML 조각으로 머리글 및 바닥글 추가

다음 코드 스니펫은 C#을 사용하여 PDF에 HTML 조각으로 머리글과 바닥글을 추가하는 방법을 보여줍니다.

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

## 이미지로 머리글 및 바닥글 추가

다음 코드 스니펫은 C#을 사용하여 PDF에 이미지로 머리글과 바닥글을 추가하는 방법을 보여줍니다.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHeaderAndFooterAsImage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_HeaderFooter();
  
    // Open PDF document
    using (var document =