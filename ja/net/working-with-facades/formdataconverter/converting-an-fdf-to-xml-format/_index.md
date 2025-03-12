---
title: FDFをXML形式に変換する
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ja/net/converting-an-fdf-to-xml-format/
description: このセクションでは、FormDataConverterクラスを使用してFDFをXML形式に変換する方法を説明します。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Converting an FDF to XML format",
    "alternativeHeadline": "Convert FDF Files to XML Easily",
    "abstract": "FormDataConverterクラスを使用してFDFファイルをXML形式に効率的に変換する方法を発見してください。この機能は、FDFからキー/バリューのペアを読みやすいXML構造に変換することでデータ処理を簡素化し、アプリケーションにおける相互運用性とデータ管理を向上させます。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "288",
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
    "url": "/net/converting-an-fdf-to-xml-format/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/converting-an-fdf-to-xml-format/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

{{% alert color="primary" %}}

[Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades)名前空間は[Aspose.PDF for .NET](/pdf/ja/net/)でAcroFormsを非常によくサポートしています。また、FDF、XFDF、XMLなどの異なるファイル形式へのフォームデータのインポートおよびエクスポートもサポートしています。しかし、時には開発者がある形式を別の形式に変換する必要があるかもしれません。この記事では、FDFをXMLに変換する機能について説明します。

{{% /alert %}}

## 実装の詳細

FDFはForms Data Formatの略で、FDFファイルにはキー/バリューのペアとしてフォームの値が含まれています。また、XMLファイルには値がタグとして含まれています。ここで、主にキーはタグ名として表され、値はそのタグ内の値として表されます。現在、[Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades)は、FDFファイル形式をXML形式に変換する柔軟性を提供しています。

この目的のために[FormDataConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formdataconverter)クラスを使用できます。このクラスは、1つのデータ形式を別の形式に変換するためのさまざまなメソッドを提供します。この記事では、[ConvertFdfToXml](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formdataconverter/methods/convertfdftoxml)という名前の1つのメソッドを使用します。このメソッドは、FDFファイルを入力またはソースストリームとして受け取り、XML形式に保存します。

以下のコードスニペットは、FDFファイルをXMLファイルに変換する方法を示しています：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void ConvertFdftoXml()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();

    // Create a file stream for FDF file - input file
    using (var fdfInputStream = new FileStream(dataDir + "input.fdf", FileMode.Open))
    {
        // Create a file stream for XML file - output file
        using (var xmlOutputStream = new FileStream(dataDir + "ConvertFdfToXML_out.xml", FileMode.Create))
        {
            FormDataConverter.ConvertFdfToXml(fdfInputStream, xmlOutputStream);
        }
    }
}
```