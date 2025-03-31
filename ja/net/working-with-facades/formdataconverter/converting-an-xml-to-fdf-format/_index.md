---
title: XMLをFDF形式に変換する
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ja/net/converting-an-xml-to-fdf-format/
description: このセクションでは、FormDataConverterを使用してXMLをFDF形式に変換する方法を説明します。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Converting an XML to FDF format",
    "alternativeHeadline": "Convert XML Files to FDF Format Easily",
    "abstract": "この機能により、開発者はAspose.PDF for .NETのFormDataConverterクラスを使用してXMLファイルをシームレスにFDF形式に変換できます。この機能は、ドキュメント形式間のデータのやり取りを強化し、アプリケーション内のフォームデータの効率的な管理を促進します。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "274",
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
    "url": "/net/converting-an-xml-to-fdf-format/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/converting-an-xml-to-fdf-format/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

{{% alert color="primary" %}}

[Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades)名前空間は、[Aspose.PDF for .NET](/pdf/ja/net/)でAcroFormsを非常によくサポートしています。また、FDF、XFDF、XMLなどの異なるファイル形式へのフォームデータのインポートとエクスポートもサポートしています。しかし、時には開発者がある形式を別の形式に変換する必要があります。この記事では、FDF形式をXMLに変換する機能について見ていきます。

{{% /alert %}}

## 実装の詳細

FDFはForms Data Formatの略で、FDFファイルにはキー/バリューのペアでフォームの値が含まれています。また、XMLファイルにはタグとして値が含まれていることも知っています。ここで、主にキーはタグ名として表され、値はそのタグ内の値として表されます。現在、[Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades)は、XMLファイル形式をFDF形式に変換する柔軟性を提供します。

この目的のために、[FormDataConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormDataConverter)クラスを使用します。このクラスは、あるデータ形式を別のデータ形式に変換するためのさまざまなメソッドを提供します。この記事では、FDFファイルを入力またはソースストリームとして受け取り、XML形式に保存するConvertXmlToFdf(..)メソッドの使用方法を示します。以下のコードスニペットは、FDFファイルをXMLファイルに変換する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void ConvertXmlToFdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();

    using (var src = new FileStream(dataDir + "log.xml", FileMode.Open, FileAccess.Read))
    {
        using (var dest = new FileStream(dataDir + "XMLToPdf_out.pdf", FileMode.Create, FileAccess.ReadWrite))
        {
            FormDataConverter.ConvertXmlToFdf(src, dest);
        }
    }
}
```