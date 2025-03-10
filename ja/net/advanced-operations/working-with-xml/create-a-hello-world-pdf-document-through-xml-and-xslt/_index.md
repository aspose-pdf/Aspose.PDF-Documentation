---
title: XMLからXSLTを使用してPDFを作成する
linktitle: XMLからXSLTを使用してPDFを作成する
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ja/net/create-a-hello-world-pdf-document-through-xml-and-xslt/
description: C#ライブラリは、入力XMLファイルがAspose.PDFスキーマに従う必要があるPDFドキュメントへのXMLファイルの変換機能を提供します。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Creating PDF from XML using XSLT",
    "alternativeHeadline": "Generate PDF from XML using XSLT and C#",
    "abstract": "XSLTとC#ライブラリを使用してXMLファイルから直接PDFを生成します。この新しい機能は、既存のXMLデータをPDF互換形式に変換することでレポート生成を効率化します。このプロセスは、変換のためにXSLTを活用し、Aspose.PDFスキーマに従う必要があります。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "323",
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
    "url": "/net/create-a-hello-world-pdf-document-through-xml-and-xslt/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-a-hello-world-pdf-document-through-xml-and-xslt/"
    },
    "dateModified": "2024-11-26",
    "description": "C#ライブラリは、入力XMLファイルがAspose.PDFスキーマに従う必要があるPDFドキュメントへのXMLファイルの変換機能を提供します。"
}
</script>

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/)ライブラリでも動作します。

既存のXMLファイルにアプリケーションデータが含まれていて、これらのファイルを使用してPDFレポートを生成したい場合があります。XSLTを使用して、既存のXMLドキュメントをAspose.Pdfの互換XMLドキュメントに変換し、その後PDFファイルを生成できます。XMLとXSLTを使用してPDFを生成するには、3つのステップがあります。

XSLTを使用してXMLファイルをPDFドキュメントに変換するには、次の手順に従ってください。

* PDFドキュメントを表すPDFクラスのインスタンスを作成します
* ライセンスを購入した場合は、Aspose.Pdf名前空間のLicenseクラスを使用してそのライセンスを使用するためのコードも埋め込む必要があります
* PDFクラスのインスタンスに対してBindXMLメソッドを呼び出すことで、入力XMLおよびXSLTファイルをバインドします
* バインドされたXMLをPDFインスタンスとともにPDFドキュメントとして保存します

## 入力XMLファイル

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Contents>
  <Content>Hello World!</Content>
</Contents>
```

## 入力XSLTファイル

```xml
<?xml version="1.0" encoding="utf-8" ?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="text()"/>
    <xsl:template match="/Contents">
    <html>
      <Document xmlns="Aspose.Pdf" IsAutoHyphenated="false">
        <PageInfo>
          <DefaultTextState
                            Font = "Helvetica" FontSize="8" LineSpacing="4"/>
          <Margin Left="5cm" Right="5cm" Top="3cm" Bottom="15cm" />
        </PageInfo>
        <Page id="mainSection">
          <TextFragment>
            <TextSegment>
              <xsl:value-of select="Content"/>
            </TextSegment>
          </TextFragment>
        </Page>
      </Document>
    </html>
</xsl:template>
</xsl:stylesheet>
```

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocument();

    //Create pdf document
    using (var document = new Aspose.Pdf.Document())
    {
        //Bind XML and XSLT files to the document
        document.BindXml(dataDir + "HelloWorld.xml", dataDir + "HelloWorld.xslt");

        // Save PDF document
        document.Save(dataDir + "HelloWorldUsingXmlAndXslt.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocument();

    //Create pdf document
    using var document = new Aspose.Pdf.Document();

    //Bind XML and XSLT files to the document
    document.BindXml(dataDir + "HelloWorld.xml", dataDir + "HelloWorld.xslt");

    // Save PDF document
    document.Save(dataDir + "HelloWorldUsingXmlAndXslt.pdf");
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