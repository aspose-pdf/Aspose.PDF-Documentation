---
title: ASP - COM相互運用を介したJScript
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ja/net/asp-jscript-via-com-interop/
description: COM Interopを通じてASPおよびJScriptアプリケーションでAspose.PDF for .NETを使用する方法を学びます。高度なPDF機能を有効にします。
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "ASP - JScript via COM Interop",
    "alternativeHeadline": "Integrate JScript with ASP for PDF Creation",
    "abstract": "ASP開発者がCOM Interopを通じてJScriptを利用し、シームレスなPDFドキュメント作成を可能にする強力な機能を紹介します。この機能により、ユーザーはASPアプリケーション内で直接PDFファイルにテキスト文字列を動的に追加でき、ドキュメント生成ワークフローを効率化します。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "182",
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
    "url": "/net/asp-jscript-via-com-interop/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/asp-jscript-via-com-interop/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

{{% alert color="primary" %}}

これは、[Aspose.PDF for .NET](/pdf/ja/net/)とCOM Interopを通じてPDFファイルに単純なテキスト文字列を追加する方法を示すシンプルなASPアプリケーションです。

{{% /alert %}}

Example:

```javascript
<%@ LANGUAGE = JScript %>
<html>
    <head>
        <title> using Aspose.PDF for .NET in classical ASP sample</title>
    </head>
    <body>
        <h3>creation of sample PDF document while using Aspose.PDF for .NET with classical ASP and JScript</h3>
<%
// set license
var lic = Server.CreateObject("Aspose.Pdf.License");
lic.SetLicense("D:\\ASPOSE\\Aspose.Total.lic");

// Instantiate Pdf instance by calling its empty constructor
var pdf = Server.CreateObject("Aspose.Pdf.Document");

// Create a new Page in the PDF object
var pdfpage = pdf.Pages.Add();

// Create Text Fragment object
var sampleText = Server.CreateObject("Aspose.Pdf.Text.TextFragment");

// Assign some content to the Fragment
sampleText.Text =  = "HelloWorld using ASP and JScript";

// Add Text paragraph to paragraphs collection of a section
pdfpage.Paragraphs.Add(SampleText);

// Save PDF document
pdf.Save("d:\\pdftest\\HelloWorldinASP.pdf");

%>
    </body>
</html>
```