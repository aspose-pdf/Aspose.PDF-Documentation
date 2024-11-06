---
title: ページプロパティの取得と設定
type: docs
url: ja/net/get-and-set-page-properties/
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "ページプロパティの取得と設定",
    "alternativeHeadline": "PDFページプロパティの取得と設定",
    "author": {
        "@type": "Person",
        "name":"アナスタシア・ホルブ",
        "givenName": "アナスタシア",
        "familyName": "ホルブ",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDFドキュメント生成",
    "keywords": "pdf, c#, ページプロパティの取得, ページプロパティの設定",
    "wordcount": "302",
    "proficiencyLevel":"初心者",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc チーム",
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
                "contactType": "販売",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "販売",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "販売",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/get-and-set-page-properties/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/get-and-set-page-properties/"
    },
    "dateModified": "2022-02-04",
    "description": ""
}
</script>
Aspose.PDF for .NETでは、.NETアプリケーションでPDFファイルのページのプロパティを読み取ったり設定したりすることができます。このセクションでは、PDFファイルのページ数を取得する方法、PDFページのプロパティ（色など）に関する情報を取得する方法、ページプロパティを設定する方法について説明します。例はC#で示されていますが、VB.NETなどの他の.NET言語を使用して同じことを達成することができます。

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリでも動作します。

## PDFファイルのページ数を取得する

ドキュメントを扱う際には、そのページ数を知りたいことがよくあります。Aspose.PDFを使用すると、これはたった2行のコードで済みます。

PDFファイルのページ数を取得するには：

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)クラスを使用してPDFファイルを開きます。
1. 次に、Documentオブジェクトから[PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection)コレクションのCountプロパティを使用して、ドキュメントの総ページ数を取得します。

次のコードスニペットは、PDFファイルのページ数を取得する方法を示しています。
以下のコードスニペットは、PDFファイルのページ数を取得する方法を示しています。

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-GetNumberofPages-GetNumberofPages.cs" >}}

### ドキュメントを保存せずにページ数を取得する

時々私たちはPDFファイルをその場で生成し、PDFファイル作成中に（目次の作成など）システムやストリームにファイルを保存せずにPDFファイルのページ数を取得する必要が出てくるかもしれません。この要件に対応するために、Documentクラスに[ProcessParagraphs](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/processparagraphs)メソッドが導入されました。ドキュメントを保存せずにページ数を取得する手順を示す次のコードスニペットをご覧ください。

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-GetPageCount-GetPageCount.cs" >}}

## ページのプロパティを取得する

PDFファイルの各ページには、幅、高さ、ブリード、クロップ、トリムボックスなどの多くのプロパティがあります。
### **ページプロパティの理解：Artbox、BleedBox、CropBox、MediaBox、TrimBox、Rectプロパティの違い**

- **メディアボックス**: メディアボックスは最大のページボックスです。これは、ドキュメントがPostScriptまたはPDFに印刷されたときに選択されたページサイズ（例えばA4、A5、USレターなど）に対応します。言い換えると、メディアボックスはPDFドキュメントが表示または印刷されるメディアの物理的サイズを決定します。
- **ブリードボックス**: ドキュメントにブリードがある場合、PDFにもブリードボックスがあります。ブリードとは、ページの端を超えて広がる色（またはアートワーク）の量です。これは、ドキュメントが印刷され、サイズにカット（「トリミング」）されたときに、インクがページの端まで行くことを保証するために使用されます。ページがトリムマークからわずかにずれてカットされたとしても - ミストリムされたとしても - ページに白い端が現れることはありません。
- **トリムボックス**: トリムボックスは、印刷およびトリミング後のドキュメントの最終サイズを示します。
- **トリムボックス**: トリムボックスは、印刷およびトリミング後のドキュメントの最終サイズを示します。
- **アートボックス**: アートボックスは、ドキュメントのページの実際の内容を囲むボックスです。このページボックスは、他のアプリケーションでPDFドキュメントをインポートする際に使用されます。
- **クロップボックス**: クロップボックスは、Adobe AcrobatでPDFドキュメントが表示される「ページ」サイズです。通常のビューでは、Adobe Acrobatでクロップボックスの内容のみが表示されます。
  これらのプロパティの詳細な説明については、Adobe.Pdf仕様、特に10.10.1ページ境界を読んでください。
- **Page.Rect**: MediaBoxとDropBoxの交差点（一般に見える矩形）。下の画像はこれらのプロパティを示しています。

詳細については、[このページ](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html)をご覧ください。

### **ページプロパティへのアクセス**

[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) クラスは、特定のPDFページに関連するすべてのプロパティを提供します。
[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) クラスは、特定のPDFページに関連するすべてのプロパティを提供します。

そこから、インデックスを使用して個々のPageオブジェクトにアクセスするか、foreachループを使用してコレクションをループし、すべてのページを取得することができます。個々のページにアクセスすると、そのプロパティを取得できます。以下のコードスニペットは、ページプロパティを取得する方法を示しています。

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-GetProperties-GetProperties.cs" >}}

## PDFファイルの特定のページを取得する

Aspose.PDFを使用すると、[PDFを個々のページに分割](/pdf/net/split-pdf-document/)し、それらをPDFファイルとして保存できます。PDFファイルで指定されたページを取得して新しいPDFとして保存する操作は非常に似ています：ソースドキュメントを開き、ページにアクセスし、新しいドキュメントを作成してそのページを追加します。

[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) オブジェクトの[PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection)は、PDFファイルのページを保持しています。
[ドキュメント](https://reference.aspose.com/pdf/net/aspose.pdf/document) オブジェクトの [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) はPDFファイル内のページを保持しています。

1. Pagesプロパティを使用してページインデックスを指定します。
1. 新しい [ドキュメント](https://reference.aspose.com/pdf/net/aspose.pdf/document) オブジェクトを作成します。
1. 新しい [ドキュメント](https://reference.aspose.com/pdf/net/aspose.pdf/document) オブジェクトに [ページ](https://reference.aspose.com/pdf/net/aspose.pdf/page) オブジェクトを追加します。
1. [保存](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) メソッドを使用して出力を保存します。

以下のコードスニペットは、PDFファイルから特定のページを取得して新しいファイルとして保存する方法を示しています。

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-GetParticularPage-GetParticularPage.cs" >}}

## ページの色を決定する

[ページ](https://reference.aspose.com/pdf/net/aspose.pdf/page) クラスは、PDFドキュメント内の特定のページに関連するプロパティを提供します。これには、ページが使用する色のタイプ - RGB、モノクロ、グレースケール、または未定義 - が含まれます。
[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) クラスは、特定の PDF ドキュメントのページに関連するプロパティを提供します。これには、ページが使用する色のタイプ - RGB、白黒、グレースケール、または未定義 - が含まれます。

PDF ファイルのすべてのページは [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) コレクションに含まれています。ColorType プロパティは、ページ上の要素の色を指定します。特定の PDF ページの色情報を取得または決定するには、[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) オブジェクトの [ColorType](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/colortype) プロパティを使用します。

次のコードスニペットは、PDF ファイルの個々のページを反復処理して色情報を取得する方法を示しています。

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-DeterminePageColor-DeterminePageColor.cs" >}}

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

