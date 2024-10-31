---
title: PDF ハイライト注釈を使用したPython
linktitle: ハイライト注釈
type: docs
weight: 20
url: /python-net/highlights-annotation/
description: マークアップ注釈は、ドキュメントのテキスト中にハイライト、下線、取り消し線、またはギザギザの下線として表示されます。
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF ハイライト注釈を使用したPython",
    "alternativeHeadline": "PDFにハイライト注釈を追加する方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf ドキュメント生成",
    "keywords": "pdf, python, ハイライト注釈, テキストマークアップ注釈",
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
    "url": "/python-net/highlights-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/highlights-annotation/"
    },
    "dateModified": "2023-02-04",
    "description": "マークアップ注釈は、ドキュメントのテキスト中にハイライト、下線、取り消し線、またはギザギザの下線として表示されます。"
}
</script>


PDFのテキストマークアップ注釈は、ドキュメント内のテキストをハイライト、下線、スキップ、またはメモを追加するために使用されます。これらの注釈は、テキストの特定の部分を強調したり、注意を引くことを目的としています。このような注釈により、ユーザーはPDFファイルの内容を視覚的にマークしたり、変更したりすることができます。

ハイライト注釈は、通常黄色の背景色でテキストをマークし、その重要性や関連性を示すために使用されます。

下線注釈は、選択したテキストの下に線を引いて、重要性や強調、または提案された編集を示すために使用されます。

取り消し線注釈は、特定のテキストを打ち消し線または取り消し線で示し、それが削除されたこと、置き換えられたこと、または無効であることを示します。

波線は、テキストの下に引いて、スペルミス、潜在的な問題、または提案された変更など、異なる種類のアクセントを示すために使用されます。

## テキストマークアップ注釈を追加

PDFドキュメントにテキストマークアップ注釈を追加するためには、次のアクションを実行する必要があります。

1. PDFファイルを読み込む - 新しい[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)オブジェクト。
1. 注釈を作成する：
    - [HighlightAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/highlightannotation/)を作成し、パラメータ（タイトル、色）を設定する。
    - [StrikeOutAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/strikeoutannotation/)を作成し、パラメータ（タイトル、色）を設定する。
    - [SquigglyAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squigglyannotation/)を作成し、パラメータ（タイトル、色）を設定する。
    - [UnderlineAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/underlineannotation/)を作成し、パラメータ（タイトル、色）を設定する。
1. その後、すべての注釈をページに追加する必要があります。

### ハイライト注釈を追加する

```python

    import aspose.pdf as ap

    # ドキュメントを開く
    document = ap.Document(input_file)

    # 円形注釈を作成する
    highlightAnnotation = ap.annotations.HighlightAnnotation(
        document.pages[1], ap.Rectangle(300, 750, 320, 770, True)
    )
    document.pages[1].annotations.append(highlightAnnotation)
    document.save(output_file)
```


### 打ち消し線注釈を追加

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    strikeoutAnnotation = ap.annotations.StrikeOutAnnotation(
        document.pages[1], ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)
    )
    strikeoutAnnotation.title = "Aspose User"
    strikeoutAnnotation.subject = "挿入されたテキスト 1"
    strikeoutAnnotation.flags = ap.annotations.AnnotationFlags.PRINT
    strikeoutAnnotation.color = ap.Color.blue

    document.pages[1].annotations.append(strikeoutAnnotation)
    document.save(output_file)
```

### 波線注釈を追加

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    page = document.pages[1]
    squigglyAnnotation = ap.annotations.SquigglyAnnotation(page, ap.Rectangle(67, 317, 261, 459, True))
    squigglyAnnotation.title = "John Smith"
    squigglyAnnotation.color = ap.Color.blue

    page.annotations.append(squigglyAnnotation)

    document.save(output_file)
```

### 下線注釈を追加

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    underlineAnnotation = ap.annotations.UnderlineAnnotation(
        document.pages[1], ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)
    )
    underlineAnnotation.title = "Aspose User"
    underlineAnnotation.subject = "挿入された下線 1"
    underlineAnnotation.flags = ap.annotations.AnnotationFlags.PRINT
    underlineAnnotation.color = ap.Color.blue

    document.pages[1].annotations.append(underlineAnnotation)
    document.save(output_file)
```


## テキストマークアップ注釈を取得

PDFドキュメントからテキストマークアップ注釈を取得するには、次のコードスニペットを試してください。

### ハイライト注釈を取得

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    highlightAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.HIGHLIGHT)
    ]

    for ha in highlightAnnotations:
        print(ha.rect)
```

### 打ち消し線注釈を取得

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    StrikeoutAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT)
    ]

    for pa in StrikeoutAnnotations:
        print(pa.rect)
```

### 波線注釈を取得

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    squigglyAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.SQUIGGLY)
    ]

    for pa in squigglyAnnotations:
        print(pa.rect)
```


### 下線注釈を取得

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    UnderlineAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.UNDERLINE)
    ]

    for ta in UnderlineAnnotations:
        print(ta.rect)
```

## テキストマークアップ注釈の削除

以下のコードスニペットは、PDFファイルからテキストマークアップ注釈を削除する方法を示しています。

### ハイライト注釈の削除

```python

    import aspose.pdf as ap

    # PDFファイルをロード
    document = ap.Document(input_file)
    highlightAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.HIGHLIGHT)
    ]

    for hs in highlightAnnotations:
        document.pages[1].annotations.delete(hs)

    document.save(output_file)
```

### 打ち消し線注釈の削除

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    StrikeoutAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT)
    ]

    for pa in StrikeoutAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
```


### 波線注釈を削除

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    squigglyAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.SQUIGGLY)
    ]

    # 波線注釈を削除
    for pa in squigglyAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
```

### 下線注釈を削除

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    underlineAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.UNDERLINE)
    ]

    # 下線注釈を削除
    for ta in underlineAnnotations:
        document.pages[1].annotations.delete(ta)

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