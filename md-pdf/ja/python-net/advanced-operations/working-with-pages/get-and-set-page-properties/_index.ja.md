---
title: Pythonを使用してページプロパティを取得および設定する
linktitle: ページプロパティの取得と設定
type: docs
weight: 90
url: /python-net/get-and-set-page-properties/
description: このセクションでは、PDFファイル内のページ数を取得し、色などのPDFページプロパティに関する情報を取得し、ページプロパティを設定する方法を示します。
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Pythonを使用してページプロパティを取得および設定する",
    "alternativeHeadline": "PDFページプロパティの取得と設定",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf ドキュメント生成",
    "keywords": "pdf, python, ページプロパティを取得, ページプロパティを設定",
    "wordcount": "302",
    "proficiencyLevel":"初心者",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "url": "/python-net/get-and-set-page-properties/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/get-and-set-page-properties/"
    },
    "dateModified": "2023-04-04",
    "description": ""
}
</script>


Aspose.PDF for Python via .NETを使用すると、Pythonアプリケーション内でPDFファイルのページのプロパティを読み取り、設定することができます。このセクションでは、PDFファイルのページ数を取得し、色などのPDFページプロパティに関する情報を取得し、ページプロパティを設定する方法を示します。例はPythonで示されています。

## PDFファイルのページ数を取得する

ドキュメントを扱う際、多くの場合、ページ数を知りたいと思うでしょう。Aspose.PDFを使用すると、これは2行のコードで実現できます。

PDFファイルのページ数を取得するには：

1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)クラスを使用してPDFファイルを開きます。
1. 次に、[PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)コレクションのCountプロパティ（Documentオブジェクトから）を使用して、ドキュメント内のページの総数を取得します。

次のコードスニペットは、PDFファイルのページ数を取得する方法を示しています。

```python

    import aspose.pdf as ap

    # ドキュメントを開く
    document = ap.Document(input_pdf)

    # ページ数を取得
    print("Page Count:", str(len(document.pages)))
```


### ドキュメントを保存せずにページ数を取得する

時々、PDFファイルをその場で生成し、PDFファイルの作成中に（目次の作成など）ファイルをシステムやストリームに保存せずにページ数を取得する必要が生じることがあります。この要件に対応するために、Documentクラスには[process_paragraphs()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)メソッドが導入されています。以下のコードスニペットは、ドキュメントを保存せずにページ数を取得する手順を示しています。

```python

    import aspose.pdf as ap

    # Documentインスタンスをインスタンス化する
    document = ap.Document()
    # PDFファイルのpagesコレクションにページを追加する
    page = document.pages.add()
    # ループインスタンスを作成する
    for i in range(0, 300):
        # TextFragmentをページオブジェクトのparagraphsコレクションに追加する
        page.paragraphs.add(ap.text.TextFragment("ページ数テスト"))
    # 正確なページ数を取得するためにPDFファイル内の段落を処理する
    document.process_paragraphs()
    # ドキュメントのページ数を印刷する
    print("ドキュメント内のページ数 =", str(len(document.pages)))
```


## ページプロパティを取得する

PDFファイルの各ページには、幅、高さ、裁ち落とし、トリムボックスなどの多くのプロパティがあります。Aspose.PDFを使用すると、これらのプロパティにアクセスできます。

### **ページプロパティの理解: Artbox, BleedBox, CropBox, MediaBox, TrimBoxおよびRectプロパティの違い**

- **メディアボックス**: メディアボックスは最も大きなページボックスです。これは、ドキュメントがPostScriptまたはPDFに印刷されたときに選択されたページサイズ（例えば、A4、A5、USレターなど）に対応します。言い換えれば、メディアボックスはPDFドキュメントが表示または印刷されるメディアの物理サイズを決定します。
- **裁ち落としボックス**: ドキュメントに裁ち落としがある場合、PDFにも裁ち落としボックスがあります。
 Bleedは、ページの端を超えて広がる色（またはアートワーク）の量です。これは、ドキュメントが印刷されてサイズにカットされたとき（「トリム」）、インクがページの端まで届くようにするために使用されます。ページが誤ってカットされた場合でも（トリムマークからわずかにずれてカットされた場合でも）、ページに白い端が現れることはありません。
- **Trim box**: トリムボックスは、印刷およびトリミング後のドキュメントの最終サイズを示します。
- **Art box**: アートボックスは、ドキュメント内のページの実際の内容の周りに描かれるボックスです。このページボックスは、他のアプリケーションでPDFドキュメントをインポートするときに使用されます。
- **Crop box**: クロップボックスは、Adobe AcrobatでPDFドキュメントが表示される「ページ」サイズです。通常のビューでは、Adobe Acrobatに表示されるのはクロップボックスの内容のみです。
  これらのプロパティの詳細な説明については、Adobe.Pdf仕様書、特に10.10.1ページ境界を参照してください。
- **Page.Rect**: MediaBoxとDropBoxの交点（通常は可視の長方形）。 下の図は、これらのプロパティを示しています。

詳細については、[このページ](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html)をご覧ください。

### **ページプロパティへのアクセス**

[Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) クラスは、特定のPDFページに関連するすべてのプロパティを提供します。PDFファイルのすべてのページは、[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) オブジェクトの [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) コレクションに含まれています。

そこから、インデックスを使用して個別のページオブジェクトにアクセスするか、foreachループを使用してコレクション全体をループしてすべてのページを取得することができます。個別のページにアクセスすると、そのプロパティを取得することができます。次のコードスニペットは、ページプロパティを取得する方法を示しています。

```python

    import aspose.pdf as ap

    # ドキュメントを開く
    document = ap.Document(input_pdf)
    # 特定のページを取得
    page = document.pages[1]
    # ページプロパティを取得
    print(
        "ArtBox : Height={},Width={},LLX={},LLY={},URX={},URY={}".format(
            page.art_box.height,
            page.art_box.width,
            page.art_box.llx,
            page.art_box.lly,
            page.art_box.urx,
            page.art_box.ury,
        )
    )
    print(
        "BleedBox : Height={},Width={},LLX={},LLY={},URX={},URY={}".format(
            page.bleed_box.height,
            page.bleed_box.width,
            page.bleed_box.llx,
            page.bleed_box.lly,
            page.bleed_box.urx,
            page.bleed_box.ury,
        )
    )
    print(
        "CropBox : Height={},Width={},LLX={},LLY={},URX={},URY={}".format(
            page.crop_box.height,
            page.crop_box.width,
            page.crop_box.llx,
            page.crop_box.lly,
            page.crop_box.urx,
            page.crop_box.ury,
        )
    )
    print(
        "MediaBox : Height={},Width={},LLX={},LLY={},URX={},URY={}".format(
            page.media_box.height,
            page.media_box.width,
            page.media_box.llx,
            page.media_box.lly,
            page.media_box.urx,
            page.media_box.ury,
        )
    )
    print(
        "TrimBox : Height={},Width={},LLX={},LLY={},URX={},URY={}".format(
            page.trim_box.height,
            page.trim_box.width,
            page.trim_box.llx,
            page.trim_box.lly,
            page.trim_box.urx,
            page.trim_box.ury,
        )
    )
    print(
        "Rect : Height={},Width={},LLX={},LLY={},URX={},URY={}".format(
            page.rect.height,
            page.rect.width,
            page.rect.llx,
            page.rect.lly,
            page.rect.urx,
            page.rect.ury,
        )
    )
    print("Page Number :", page.number)
    print("Rotate :", page.rotate)
```

## PDFファイルの特定のページを取得する

Aspose.PDF for Pythonを使用すると、[PDFを個々のページに分割](/pdf/python-net/split-pdf-document/)し、それらをPDFファイルとして保存できます。PDFファイル内の指定したページを取得して新しいPDFとして保存する操作も非常に似ています。ソースドキュメントを開き、ページにアクセスし、新しいドキュメントを作成してそのページを追加します。

[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document)オブジェクトの[PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection)には、PDFファイル内のページが含まれています。このコレクションから特定のページを取得するには：

1. Pagesプロパティを使用してページインデックスを指定します。
1. 新しい[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)オブジェクトを作成します。
1. [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)オブジェクトを新しいDocumentオブジェクトに追加します。
1. [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)メソッドを使用して出力を保存します。

次のコードスニペットは、PDFファイルから特定のページを取得し、新しいファイルとして保存する方法を示しています。

```python

    import aspose.pdf as ap

    # ドキュメントを開く
    document = ap.Document(input_pdf)

    # 特定のページを取得
    page = document.pages[2]

    # ページをPDFファイルとして保存
    new_document = ap.Document()
    new_document.pages.add(page)
    new_document.save(output_pdf)
```

## ページの色を決定

[Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) クラスは、PDFドキュメント内の特定のページに関連するプロパティを提供し、ページが使用する色の種類（RGB、白黒、グレースケールまたは未定義）を含みます。

すべてのPDFファイルのページは、[PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) コレクションによって保持されています。
 The [color_type](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) プロパティは、ページ上の要素の色を指定します。特定のPDFページの色情報を取得または判断するには、[Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) オブジェクトの [color_type](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) プロパティを使用します。

次のコードスニペットは、PDFファイルの個々のページを反復して色情報を取得する方法を示しています。

```python

    import aspose.pdf as ap

    # ソースPDFファイルを開く
    document = ap.Document(input_pdf)
    # PDFファイルのすべてのページを反復する
    for page_n in range(0, len(document.pages)):
        page_number = page_n + 1
        # 特定のPDFページの色タイプ情報を取得する
        page_color_type = document.pages[page_number].color_type
        if page_color_type == ap.ColorType.BLACK_AND_WHITE:
            print("ページ # " + str(page_number) + " は白黒です。")

        if page_color_type == ap.ColorType.GRAYSCALE:
            print("ページ # " + str(page_number) + " はグレースケールです。")

        if page_color_type == ap.ColorType.RGB:
            print("ページ # " + str(page_number) + " はRGBです。")

        if page_color_type == ap.ColorType.UNDEFINED:
            print("ページ # " + str(page_number) + " の色は未定義です。")
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python via .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "applicationCategory": "Python用PDF操作ライブラリ",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/example.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>