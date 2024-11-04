---
title: XSLTを使用してXMLからPDFを作成する
linktitle: XSLTを使用してXMLからPDFを作成する
type: docs
weight: 10
url: /net/create-a-hello-world-pdf-document-through-xml-and-xslt/
description: C#ライブラリは、入力XMLファイルがAspose.PDFスキーマに従う必要があることを前提に、XMLファイルをPDFドキュメントに変換する機能を提供します。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "XSLTを使用してXMLからPDFを作成する",
    "alternativeHeadline": "XSLTを使用してXMLからPDFを作成する方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, c#, create pdf xml, pdf with xslt",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "dateModified": "2022-02-04",
    "description": "C#ライブラリは、入力XMLファイルがAspose.PDFスキーマに従う必要があることを前提に、XMLファイルをPDFドキュメントに変換する機能を提供します。"
}
</script>
以下のコードスニペットは[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリでも動作します。

既存のXMLファイルにアプリケーションデータが含まれていて、これらのファイルを使用してPDFレポートを生成したい場合があります。XSLTを使用して既存のXMLドキュメントをAspose.Pdf互換のXMLドキュメントに変換し、PDFファイルを生成することができます。XMLとXSLTを使用してPDFを生成するには、3つのステップがあります。

以下のステップに従って、XSLTを使用してXMLファイルをPDFドキュメントに変換してください:

* PDFドキュメントを表すPDFクラスのインスタンスを作成
* ライセンスを購入している場合は、Aspose.Pdf名前空間のLicenseクラスを使用してそのライセンスを使用するコードを埋め込む
* BindXMLメソッドを呼び出して、入力XMLとXSLTファイルをPDFクラスのインスタンスにバインド
* バインドされたXMLをPDFインスタンスとして保存し、PDFドキュメントとして保存

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
{{< gist "aspose-com-gists" "63473b1ba28e09e229cfbf4430eabd8a" "Examples-CSharp-AsposePDF-Working-Document-HelloWorldPDFUsingXmlAndXslt-HelloWorldPDFUsingXmlAndXslt.cs" >}}

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

---
id: tutorials
title: "Tutorials"
sidebar_label: "Tutorials"
slug: /category/tutorials
type: docs
---

## チュートリアルへようこそ

このセクションでは、初めてのプロジェクトを始めるためのステップバイステップのガイドを提供します。各チュートリアルは、特定のタスクを達成するための実践的なアプローチを取ります。

### 基本チュートリアル

- **入門ガイド**: このガイドでは、基本的なセットアップと最初のプロジェクトの作成方法について説明します。
- **データモデリング**: このチュートリアルでは、データベースの設計とデータモデルの作成方法について学びます。
- **API 開発**: このガイドでは、RESTful API の作成とそれに関連するベストプラクティスについて説明します。

### 高度なチュートリアル

- **認証と認可**: このチュートリアルでは、ユーザー認証と認可の実装方法について学びます。
- **パフォーマンス最適化**: このガイドでは、アプリケーションのパフォーマンスを向上させるための戦略を紹介します。
- **デプロイとスケーリング**: このチュートリアルでは、アプリケーションのデプロイメントとスケーリングの方法について学びます。

## よくある質問

### チュートリアルの前提条件は何ですか？

各チュートリアルの前提条件は、個々のチュートリアルの冒頭に記載されています。基本的なプログラミング知識があれば、ほとんどのチュートリアルを理解できるでしょう。

### サポートを受けるにはどうすればいいですか？

ドキュメンテーションやコミュニティフォーラムをチェックしてください。そこで質問を投稿したり、他のユーザーからのフィードバックを受け取ることができます。

## 変更履歴

- **バージョン 1.0** - 初版リリース
- **バージョン 1.1** - 誤字修正と内容の更新

## フィードバック

私たちは、あなたのフィードバックを大切にします。改善点や提案があれば、お知らせください。

---

changefreq: "monthly"
```
