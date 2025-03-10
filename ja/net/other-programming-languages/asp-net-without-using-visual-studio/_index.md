---
title: Visual Studioを使用せずにASP.NET
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /ja/net/asp-net-without-using-visual-studio/
description: Visual Studioに依存せずにASP.NETプロジェクトでAspose.PDF for .NETを使用する方法を学びます。この実用的なガイドに従ってください。
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "ASP.NET without using Visual Studio",
    "alternativeHeadline": "Create ASP.NET Applications Without Visual Studio",
    "abstract": "Visual Studioに依存せずにAspose.PDF for .NETを使用してASP.NETアプリケーションを作成する方法を発見してください。この革新的なアプローチにより、開発者は単一の .aspx ファイル内でHTMLとC#またはVB.NETコードを書くことができ、ASP.NETページ内でPDFドキュメントを直接生成するプロセスを効率化します。このシームレスな統合で開発効率を最大化しましょう。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "263",
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
    "url": "/net/asp-net-without-using-visual-studio/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/asp-net-without-using-visual-studio/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

{{% alert color="primary" %}}

[Aspose.PDF for .NET](/pdf/net/)を使用して、Visual Studioを使用せずにASP.NETページまたはアプリケーションを開発できます。この例では、HTMLとC#またはVB.NETコードを単一の .aspx ファイルに記述します。これは一般的にインスタントASP.NETとして知られています。

{{% /alert %}}

## 実装の詳細

{{% alert color="primary" %}}

サンプルWebアプリケーションを作成し、Aspose.PDF.dllをウェブサイトディレクトリ内の「Bin」という名前のディレクトリにコピーします（*binフォルダーが存在しない場合は作成してください*）。次に、.aspxページを作成し、以下のコードをコピーします。
この例では、ASP.NETページ内でインラインコードを使用して[Aspose.PDF for .NET](/pdf/net/)を使用し、サンプルテキストを含むシンプルなPDFドキュメントを作成する方法を示します。
{{% /alert %}}

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
<%@ Page Language ="C#" %>
<%@ Import Namespace="System" %>
<%@ Import Namespace="System.IO" %>
<%@ Import Namespace="System.Data" %>
<%@ Import Namespace="Aspose.PDF" %>

<html>
    <head>
        <title> using Aspose.PDF for .NET with Inline ASP.NET</title>
    </head>
    <body>
        <h3>creation of simple PDF document while using Aspose.PDF for .NET with Inline ASP.NET</h3>
<%
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    // Set license
    Aspose.Pdf.License lic = new Aspose.Pdf.License();
    lic.SetLicense("Aspose.Total.lic");

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        Aspose.Pdf.Page page = document.Pages.Add();
        // Add text to new page
        page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World!"));
        // Save PDF document
        document.Save(dataDir + "HelloWorld_out.pdf");
    }
%>

    </body>
</html>
```