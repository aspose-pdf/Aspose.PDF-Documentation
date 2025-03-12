---
title: WebForms DataGridViewをPDFにレンダリング
linktitle: WebForms DataGridViewをPDFにレンダリング
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ja/net/render-webforms-datagridview-to-pdf/
description: このサンプルは、Aspose.PDFライブラリを使用してWebFormをPDFにレンダリングする方法を示しています。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Render WebForms DataGridView to PDF",
    "alternativeHeadline": "Effortlessly Convert WebForms DataGridView to PDF",
    "abstract": "この機能は、Aspose.PDF for .NETライブラリを使用してWebForms DataGridViewをPDFにシームレスに変換することを可能にします。この機能は、専用のGridViewエクスポートコントロールを統合することでデータのエクスポートプロセスを簡素化し、Webアプリケーションから直接高品質のPDFレンダリングを保証します。効率的なドキュメント生成ソリューションを求める開発者に最適です。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "266",
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
    "url": "/net/render-webforms-datagridview-to-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/render-webforms-datagridview-to-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

## Aspose.PDF/Aspose.HTMLを使用してWebFormをPDFにエクスポートする方法

### はじめに

一般的に、WebFormをPDFドキュメントに変換するには追加のツールを使用します。このサンプルは、Aspose.PDFライブラリを使用してWebFormをPDFにレンダリングする方法を示しています。このサンプルには、_GridViewコントロールをPDFドキュメントにレンダリングする方法を示すために、Aspose Export GridView To Pdf Controlも含まれています。

## WebFormをPDFにレンダリングする方法

WebFormをPDFにレンダリングするための元のアイデアは、[System.Web.UI.Page](https://msdn.microsoft.com/en-US/library/System.Web.UI.Page.aspx)から継承したヘルパークラスを作成し、Renderメソッドをオーバーライドすることです。</em></p>

```csharp
void Render(HtmlTextWriter writer)
{
    if (RenderToPDF)
    {
        // render web page for PDF document
    }
    else
    {
        // render web page in browser
        base.Render(writer);
    }
}
```

HTMLをPDFにレンダリングするために使用できるAsposeツールは2つあります：

- Aspose.PDF for .NET。
- Aspose Export GridViewコントロール（Aspose.PDFに基づく）。

## ソースファイル

このサンプルには2つのデモレポートがあります。

- _Default.aspx_は、Aspose.PDFを使用してPDFにエクスポートする方法を示しています。
- _Report2.aspx_は、Aspose Export GridViewコントロール（Aspose.PDFに基づく）を使用してPDFにエクスポートする方法を示しています。

## 追加ファイル

`Helpers\PdfPage.cs` - Aspose.PDF APIの使用方法を示すヘルパークラスが含まれています。</em>

Aspose.Pdf.GridViewExportプロジェクトには、`Report2.aspx`でのデモ用に拡張されたGridViewコントロールが含まれています。