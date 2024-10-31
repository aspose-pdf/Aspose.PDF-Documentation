---
title: Pythonを使用した追加注釈
linktitle: 追加注釈
type: docs
weight: 60
url: /python-net/extra-annotations/
description: このセクションでは、PDFドキュメントに追加の種類の注釈を追加、取得、削除する方法について説明します。
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Pythonを使用した追加注釈",
    "alternativeHeadline": "PDFに追加注釈を追加する方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdfドキュメント生成",
    "keywords": "pdf, python, リンク注釈, キャレット注釈",
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
    "url": "/python-net/extra-annotations/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/extra-annotations/"
    },
    "dateModified": "2023-02-04",
    "description": "このセクションでは、Pythonを使用してPDFドキュメントに追加の種類の注釈を追加、取得、削除する方法について説明します。"
}
</script>


## 既存のPDFファイルにキャレット注釈を追加する方法（Python使用）

キャレット注釈は、テキスト編集を示す記号です。キャレット注釈はマークアップ注釈でもあるため、CaretクラスはMarkupクラスから派生しており、キャレット注釈のプロパティを取得または設定する機能や、キャレット注釈の外観の流れをリセットする機能を提供します。キャレット注釈は、テキストの変更、追加、または修正を提案するためによく使用されます。

キャレット注釈を作成する手順：

1. PDFファイルを読み込む - 新しい[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)。
1. 新しい[CaretAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/caretannotation/)を作成し、キャレットのパラメータ（新しいRectangle、タイトル、件名、フラグ、色）を設定します。この注釈はテキストの挿入を示すために使用されます。
1. ページに注釈を追加できたら。

次のコードスニペットは、PDFファイルにキャレット注釈を追加する方法を示しています：

```python

    import aspose.pdf as ap

    # ドキュメントを開く
    document = ap.Document(input_file)

    caretAnnotation1 = ap.annotations.CaretAnnotation(
        document.pages[1], ap.Rectangle(200, 700.664, 308.708, 740.769, True)
    )
    caretAnnotation1.title = "Aspose User"
    caretAnnotation1.subject = "挿入されたテキスト 1"
    caretAnnotation1.flags = ap.annotations.AnnotationFlags.PRINT
    caretAnnotation1.color = ap.Color.blue

    document.pages[1].annotations.append(caretAnnotation1)
    document.save(output_file)
```


### カレット注釈を取得

PDFドキュメントでカレット注釈を取得するために、次のコードスニペットを試してください。

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    caretAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.CARET)
    ]

    for ca in caretAnnotations:
        print(ca.rect)
```

### カレット注釈を削除

次のコードスニペットは、Pythonを使用してPDFファイルからカレット注釈を削除する方法を示しています。

```python

    import aspose.pdf as ap

    # PDFファイルの読み込み
    document = ap.Document(input_file)
    caretAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.CARET)
    ]

    for ca in caretAnnotations:
        document.pages[1].annotations.delete(ca)

    document.save(output_file)
```

## リンク注釈を追加

[リンク](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/linkannotation/)は、クリックするとURLを開くか、同じドキュメント内または外部ドキュメント内の特定の位置に移動する注釈です。

A Link Annotationsは、ページ上の任意の場所に配置できる長方形の領域です。各リンクには、それに関連付けられた対応するPDFアクションがあります。ユーザーがこのリンクの領域をクリックすると、このアクションが実行されます。

次のコードスニペットは、電話番号の例を使用してPDFファイルにリンク注釈を追加する方法を示しています。

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    # 電話番号を見つけるためのTextFragmentAbsorberオブジェクトを作成
    textFragmentAbsorber = ap.text.TextFragmentAbsorber("file")

    # 1ページ目のみアブソーバを適用
    document.pages[1].accept(textFragmentAbsorber)

    phoneNumberFragment = textFragmentAbsorber.text_fragments[1]

    # リンク注釈を作成し、アクションを電話番号を呼び出すように設定
    linkAnnotation = ap.annotations.LinkAnnotation(document.pages[1], phoneNumberFragment.rectangle)
    linkAnnotation.action = ap.annotations.GoToURIAction("www.aspose.com")

    # ページに注釈を追加
    document.pages[1].annotations.append(linkAnnotation)
    document.save(output_file)
```


### リンク注釈を取得

次のコードスニペットを使用して、PDFドキュメントから[LinkAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/linkannotation/)を取得してください。

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    linkAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in linkAnnotations:
        print(la.rect)
```

### リンク注釈を削除

次のコードスニペットは、PDFファイルからリンク注釈を削除する方法を示しています。これには、1ページ目のすべてのリンク注釈を見つけて削除する必要があります。その後、削除された注釈でドキュメントを保存します。

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    highlightAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for hs in highlightAnnotations:
        document.pages[1].annotations.delete(hs)

    document.save(output_file)
```


## Aspose.PDF for Pythonを使用して特定のページ領域を編集注釈で編集

Aspose.PDF for Python via .NETは、既存のPDFファイルに注釈を追加および操作する機能をサポートしています。PDFドキュメントの編集注釈は、ドキュメントから機密情報を永続的に削除または隠すことを目的としています。情報を編集するプロセスには、特定のコンテンツ（テキスト、画像、グラフィックスなど）を覆ったり、シェーディングしたりして、その可視性やアクセスを制限する方法が含まれます。これにより、機密情報がドキュメント内で隠され、保護され続けることが保証されます。この要件を満たすために、[RedactionAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/redactionannotation/)という名前のクラスが提供されており、特定のページ領域を編集するために使用することができるほか、既存のRedactionAnnotationsを操作してそれらを編集（すなわち、注釈をフラット化してその下のテキストを削除）するために使用することができます。

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    page = document.pages[1]
    redactionAnnotation = ap.annotations.RedactionAnnotation(page, ap.Rectangle(270, 190, 371, 250, True))
    redactionAnnotation.title = "John Smith"
    redactionAnnotation.fill_color = ap.Color.light_gray
    redactionAnnotation.color = ap.Color.red
    redactionAnnotation.redact()

    page.annotations.append(redactionAnnotation)
    document.save(output_file)
```


### 補正注釈を取得する

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    redactionAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.REDACTION)
    ]

    for pa in redactionAnnotations:
        print(pa.rect)
```    

### 補正注釈を削除する

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    redactionAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.REDACTION)
    ]

    for pa in redactionAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
```  

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python Library",
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
    "applicationCategory": "PDF Manipulation Library for Python",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>