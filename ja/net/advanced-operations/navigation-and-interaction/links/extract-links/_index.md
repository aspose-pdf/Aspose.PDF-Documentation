---
title: PDFファイルからリンクを抽出する
linktitle: リンクを抽出する
type: docs
weight: 30
url: /ja/net/extract-links/
description: C#を使用してPDFからリンクを抽出します。このトピックでは、AnnotationSelectorクラスを使用してリンクを抽出する方法を説明します。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDFファイルからリンクを抽出する",
    "alternativeHeadline": "PDFからリンクを抽出する方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF文書生成",
    "keywords": "pdf, c#, pdfからリンクを抽出する",
    "wordcount": "302",
    "proficiencyLevel":"初心者",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDFドキュメントチーム",
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
    "url": "/net/extract-links/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-links/"
    },
    "dateModified": "2022-02-04",
    "description": "C#を使用してPDFからリンクを抽出します。このトピックでは、AnnotationSelectorクラスを使用してリンクを抽出する方法を説明します。"
}
</script>
以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/) ライブラリとも連携します。

## PDFファイルからリンクを抽出する

リンクはPDFファイル内で注釈として表現されるため、リンクを抽出するには、すべての [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) オブジェクトを抽出します。

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) オブジェクトを作成します。
1. リンクを抽出したい [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) を取得します。
1. [AnnotationSelector](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationselector) クラスを使用して、指定されたページからすべての [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) オブジェクトを抽出します。
1. [AnnotationSelector](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationselector) オブジェクトをページオブジェクトのAcceptメソッドに渡します。
以下のコードスニペットは、PDFファイルからリンクを抽出する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパスです。
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// ドキュメントを開く
Document document = new Document(dataDir+ "ExtractLinks.pdf");
// アクションを抽出する
Page page = document.Pages[1];
AnnotationSelector selector = new AnnotationSelector(new LinkAnnotation(page, Aspose.Pdf.Rectangle.Trivial));
page.Accept(selector);
IList<Annotation> list = selector.Selected;
Annotation annotation = (Annotation)list[0];
dataDir = dataDir + "ExtractLinks_out.pdf";
// 更新されたドキュメントを保存する
document.Save(dataDir);
```

