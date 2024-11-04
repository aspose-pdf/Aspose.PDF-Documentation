---
title: JavaScriptの利用方法
type: docs
url: /net/working-with-javascript/
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "JavaScriptの利用方法",
    "alternativeHeadline": "PDFでJavaScriptを扱う方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF文書生成",
    "keywords": "PDF, C#, PDF内のJavaScript",
    "wordcount": "302",
    "proficiencyLevel":"初心者",
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
    "url": "/net/working-with-javascript/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-javascript/"
    },
    "dateModified": "2022-02-04",
    "description": ""
}
</script>
## JavaScript (DOM) の追加

### Acrobat JavaScript とは何ですか？

Acrobat JavaScriptは、ISO-16262のバージョン1.5に基づいているJavaScriptのコアに基づいた言語で、以前はECMAScriptとして知られており、Netscape Communicationsによって開発されたオブジェクト指向スクリプト言語です。JavaScriptは、WebベースのアプリケーションでサーバーからクライアントへのWebページ処理のオフロードを目的として作成されました。Acrobat JavaScriptは、新しいオブジェクトとそれに伴うメソッドとプロパティの形で拡張を実装しています。これらAcrobat固有のオブジェクトにより、開発者はドキュメントのセキュリティを管理し、データベースと通信し、ファイル添付を扱い、PDFファイルをインタラクティブでWeb対応のフォームのように操作することができます。Acrobat固有のオブジェクトはコアJavaScriptの上に追加されるため、Math、String、Date、Array、RegExpを含む標準クラスに引き続きアクセスできます。

### Acrobat JavaScript と HTML（Web）JavaScript の対比

PDFドキュメントは、Acrobatソフトウェア内だけでなく、Webブラウザでも表示できるため、非常に汎用性があります。
PDF文書は、Acrobatソフトウェア内だけでなく、Webブラウザー内でも表示できるため、非常に汎用性が高いです。

- Acrobat JavaScriptはHTMLページ内のオブジェクトにアクセスできません。同様に、HTML JavaScriptはPDFファイル内のオブジェクトにアクセスできません。
- HTML JavaScriptはWindowなどのオブジェクトを操作できます。Acrobat JavaScriptはこの特定のオブジェクトにアクセスできませんが、PDF固有のオブジェクトを操作できます。

[Aspose.PDF for .NET](/pdf/net/) を使用して、ドキュメントレベルとページレベルの両方にJavaScriptを追加できます。JavaScriptを追加するには：

### ドキュメントまたはページアクションにJavaScriptを追加

1. 望ましいJavaScriptステートメントをコンストラクタ引数としてJavascriptActionオブジェクトを宣言してインスタンス化します。
1. JavascriptActionオブジェクトをPDFドキュメントまたはページの望ましいアクションに割り当てます。

以下の例では、特定のドキュメントにOpenActionを適用しています。

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Working-Document-AddJavaScriptToPage-AddJavaScriptToPage.cs" >}}

### **ドキュメントレベルでのJavaScriptの追加/削除**
### **ドキュメントレベルへのJavaScriptの追加/削除**

DocumentクラスにJavaScriptという新しいプロパティが追加されました。これはJavaScriptコレクションタイプを持ち、キーによってJavaScriptシナリオにアクセスを提供します。このプロパティはドキュメントレベルのJavaScriptを追加するために使用されます。JavaScriptコレクションには以下のプロパティとメソッドがあります：

- string this(string key) – 名前によってJavaScriptを取得または設定します
- IList Keys – JavaScriptコレクション内の既存のキーのリストを提供します
- bool Remove(string key) – キーによってJavaScriptを削除します。

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Working-Document-AddRemoveJavascriptToDoc-AddRemoveJavascriptToDoc.cs" >}}

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


