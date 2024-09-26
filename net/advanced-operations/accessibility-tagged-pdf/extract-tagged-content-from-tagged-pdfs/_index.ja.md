---
title: PDFからタグ付きコンテンツを抽出する
linktitle: タグ付きコンテンツの抽出
type: docs
weight: 20
url: /net/extract-tagged-content-from-tagged-pdfs/
description: この記事では、Aspose.PDF for .NETを使用してPDFドキュメントからタグ付きコンテンツを抽出する方法について説明します
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDFからタグ付きコンテンツを抽出する",
    "alternativeHeadline": "PDFで画像にタグを付ける方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDFドキュメント生成",
    "keywords": "タグ, PDF, 抽出",
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
    "url": "/net/extract-tagged-content-from-tagged-pdfs/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-tagged-content-from-tagged-pdfs/"
    },
    "dateModified": "2022-02-04",
    "description": "この記事では、Aspose.PDF for .NETを使用してPDFドキュメントからタグ付きコンテンツを抽出する方法について説明します"
}
</script>

この記事では、C#を使用してタグ付きコンテンツPDFドキュメントを抽出する方法を学びます。

以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/) ライブラリでも動作します。

## タグ付きPDFコンテンツの取得

PDFドキュメントのタグ付きテキストのコンテンツを取得するために、Aspose.PDFは[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) クラスの [TaggedContent](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/taggedcontent) プロパティを提供しています。

次のコードスニペットは、タグ付きテキストのPDFドキュメントのコンテンツを取得する方法を示しています：

```csharp
// 完全な例やデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Pdf Documentを作成
Document document = new Document();

// タグ付きPdfのコンテンツを作業用に取得
ITaggedContent taggedContent = document.TaggedContent;

//
// タグ付きPdfコンテンツの作業
//

// ドキュメントのタイトルと言語を設定
taggedContent.SetTitle("Simple Tagged Pdf Document");
taggedContent.SetLanguage("en-US");

// タグ付きPdfドキュメントを保存
document.Save(dataDir + "TaggedPDFContent.pdf");
```
## ルート構造の取得

Tagged PDF Documentのルート構造を取得するために、Aspose.PDFは[ITaggedContent](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent)インターフェースの[StructTreeRootElement](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent/properties/structtreerootelement)プロパティと[StructureElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structureelement)を提供しています。次のコードスニペットは、Tagged PDF Documentのルート構造を取得する方法を示しています：

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Pdf Documentを作成
Document document = new Document();

// TaggedPdfの作業用コンテンツを取得
ITaggedContent taggedContent = document.TaggedContent;

// ドキュメントのタイトルと言語を設定
taggedContent.SetTitle("Tagged Pdf Document");
taggedContent.SetLanguage("en-US");

// StructTreeRootElementプロパティとRootElementプロパティは、
// PDFドキュメントのStructTreeRootオブジェクトとルート構造要素（ドキュメント構造要素）にアクセスするために使用されます。
StructTreeRootElement structTreeRootElement = taggedContent.StructTreeRootElement;
StructureElement rootElement = taggedContent.RootElement;
```
## 子要素にアクセスする

タグ付けされたPDFドキュメントの子要素にアクセスするために、Aspose.PDFは[ElementList](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/elementlist)クラスを提供しています。次のコードスニペットは、タグ付けされたPDFドキュメントの子要素にアクセスする方法を示しています：

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET にアクセスしてください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Pdfドキュメントを開く
Document document = new Document(dataDir + "StructureElementsTree.pdf");

// タグ付けされたPdfの作業用のコンテンツを取得
ITaggedContent taggedContent = document.TaggedContent;

// ルート要素にアクセス
ElementList elementList = taggedContent.StructTreeRootElement.ChildElements;
foreach (Element element in elementList)
{
    if (element is StructureElement)
    {
        StructureElement structureElement = element as StructureElement;

        // プロパティを取得
        string title = structureElement.Title;
        string language = structureElement.Language;
        string actualText = structureElement.ActualText;
        string expansionText = structureElement.ExpansionText;
        string alternativeText = structureElement.AlternativeText;
    }
}

// ルート要素の最初の要素の子要素にアクセス
elementList = taggedContent.RootElement.ChildElements[1].ChildElements;
foreach (Element element in elementList)
{
    if (element is StructureElement)
    {
        StructureElement structureElement = element as StructureElement;

        // プロパティを設定
        structureElement.Title = "title";
        structureElement.Language = "fr-FR";
        structureElement.ActualText = "actual text";
        structureElement.ExpansionText = "exp";
        structureElement.AlternativeText = "alt";
    }
}

// タグ付けされたPdfドキュメントを保存
document.Save(dataDir + "AccessChildElements.pdf");
```
## 既存のPDFで画像にタグを付ける

既存のPDFドキュメントで画像にタグを付けるために、Aspose.PDFは[StructureElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structureelement)クラスの[FindElements](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/element/methods/findelements/_1)メソッドを提供します。[FigureElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/figureelement)クラスの[AlternativeText](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structureelement/properties/alternativetext)プロパティを使用して、図に代替テキストを追加できます。

以下のコードスニペットは、既存のPDFドキュメントに画像にタグを付ける方法を示しています：

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET にアクセスしてください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
string inFile = dataDir + "TH.pdf";
string outFile = dataDir + "TH_out.pdf";
string logFile = dataDir + "TH_out.xml";

// ドキュメントを開く
Document document = new Document(inFile);

// タグ付けされたコンテンツとルート構造要素を取得
ITaggedContent taggedContent = document.TaggedContent;
StructureElement rootElement = taggedContent.RootElement;

// タグ付けされたPDFドキュメントのタイトルを設定
taggedContent.SetTitle("画像付きドキュメント");

foreach (FigureElement figureElement in rootElement.FindElements<FigureElement>(true))
{
    // 図の代替テキストを設定
    figureElement.AlternativeText = "図の代替テキスト (技法2)";


    // BBox属性を作成して設定
    StructureAttribute bboxAttribute = new StructureAttribute(AttributeKey.BBox);
    bboxAttribute.SetRectangleValue(new Rectangle(0.0, 0.0, 100.0, 100.0));

    StructureAttributes figureLayoutAttributes = figureElement.Attributes.GetAttributes(AttributeOwnerStandard.Layout);
    figureLayoutAttributes.SetAttribute(bboxAttribute);
}

// スパン要素を段落に移動（最初のTDで間違ったスパンと段落を見つける）
TableElement tableElement = rootElement.FindElements<TableElement>(true)[0];
SpanElement spanElement = tableElement.FindElements<SpanElement>(true)[0];
TableTDElement firstTdElement = tableElement.FindElements<TableTDElement>(true)[0];
ParagraphElement paragraph = firstTdElement.FindElements<ParagraphElement>(true)[0];

// スパン要素を段落に移動
spanElement.ChangeParentElement(paragraph);


// ドキュメントを保存
document.Save(outFile);



// 出力ドキュメントのPDF/UAコンプライアンスを確認
document = new Document(outFile);

bool isPdfUaCompliance = document.Validate(logFile, PdfFormat.PDF_UA_1);
Console.WriteLine(String.Format("PDF/UAコンプライアンス：{0}", isPdfUaCompliance));
```

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
    "applicationCategory": ".NET用PDF操作ライブラリ",
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
```

