---
title: 改行を決定する
linktitle: 改行を決定する
type: docs
weight: 70
url: /ja/python-net/determine-line-break/
description: Pythonを使用して複数行のTextFragmentの改行を決定する方法について詳しく学ぶ
lastmod: "2024-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "改行を決定する",
    "alternativeHeadline": "TextFragmentの改行を決定する方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, python, 改行を決定する",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
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
    "url": "/python-net/determine-line-break/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/determine-line-break/"
    },
    "dateModified": "2024-02-04",
    "description": "Pythonを使用して複数行のTextFragmentの改行を決定する方法について詳しく学ぶ"
}
</script>


## 複数行テキストフラグメントの改行を追跡

次のコードスニペットは、PDFドキュメント内の複数行テキストフラグメントの改行挙動を追跡する方法を示しています。

track_line_breaking() 関数は、この機能を示すために定義されています。これは、生成されたPDFドキュメントと改行情報を含む対応するテキストファイルの両方の出力ファイルパスを指定することから始まります。

関数内では、新しいPDFドキュメントオブジェクトが作成され、新しいページが追加されます。その後、ループを使用して、文字列内に改行 ("\r\n") を挿入して複数行のテキストをシミュレートするテキストフラグメントの4つのインスタンスを生成します。

各テキストフラグメントは、ページの段落に追加される前にフォントサイズを20ポイントに設定されます。

すべてのテキストフラグメントが追加された後、ドキュメントが保存されます。

次に、関数は、get_notifications() メソッドを使用して、生成されたPDFドキュメントの2ページ目から改行に関する通知を抽出します。
 これらの通知は、前に指定されたテキストファイルに書き込まれます。

このコードスニペットは、複数行のテキストを含むPDFドキュメントを作成し、行の折り返し動作に関する情報を抽出して、ドキュメント内でテキストがどのように配置されているかについての洞察を提供する方法を示しています。

```python

    import aspose.pdf as ap

    def track_line_breaking():
        """複数行のTextFragmentの行の折り返しを追跡する"""
        output_pdf = DIR_OUTPUT_TEXTS + "track_line_breaking.pdf"
        output_txt = DIR_OUTPUT_TEXTS + "track_line_breaking.txt"

        # 新しいドキュメントオブジェクトを作成
        document = ap.Document()
        page = document.pages.add()

        for i in range(4):
            text = ap.text.TextFragment(
                "Lorem ipsum \r\ndolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
            )
            text.text_state.font_size = 20
            page.paragraphs.add(text)
        document.save(output_pdf)

        notifications = document.pages[1].get_notifications()
        with open(output_txt, "w") as f:
            f.write(notifications)
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF操作ライブラリ for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2024.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>