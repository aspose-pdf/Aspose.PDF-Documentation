---
title: PDFでのポートフォリオの操作
linktitle: ポートフォリオ
type: docs
weight: 40
url: /ja/net/portfolio/
description: C#を使用してPDFポートフォリオを作成する方法。Microsoft Excelファイル、Wordドキュメント、および画像ファイルを使用してPDFポートフォリオを作成する必要があります。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDFでのポートフォリオの操作",
    "alternativeHeadline": "PDFドキュメントでポートフォリオを作成",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDFドキュメント生成",
    "keywords": "pdf, c#, ポートフォリオ",
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
    "url": "/net/portfolio/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/portfolio/"
    },
    "dateModified": "2022-02-04",
    "description": "C#を使用してPDFポートフォリオを作成する方法。Microsoft Excelファイル、Wordドキュメント、および画像ファイルを使用してPDFポートフォリオを作成する必要があります。"
}
</script>
## PDFポートフォリオの作成方法

Aspose.PDFを使用してPDFポートフォリオドキュメントを作成できます。[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)クラスを使用し、[FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification)クラスで取得したファイルをDocument.Collectionオブジェクトに追加します。ファイルが追加された後、DocumentクラスのSaveメソッドを使用してポートフォリオドキュメントを保存します。

以下の例では、Microsoft Excelファイル、Wordドキュメント、画像ファイルを使用してPDFポートフォリオを作成します。

以下のコードは、次のポートフォリオを生成します。

以下のコードスニペットも[Aspose.PDF.Drawing](/pdf/ja/net/drawing/)ライブラリで動作します。

### Aspose.PDFで作成されたPDFポートフォリオ

![Aspose.PDF for .NETで作成されたPDFポートフォリオ](working-with-pdf-portfolio_1.jpg)

```csharp
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_TechnicalArticles();

// Documentオブジェクトのインスタンス化
Document doc = new Document();

// ドキュメントコレクションオブジェクトのインスタンス化
doc.Collection = new Collection();

// ポートフォリオに追加するファイルを取得
FileSpecification excel = new FileSpecification( dataDir + "HelloWorld.xlsx");
FileSpecification word = new FileSpecification( dataDir + "HelloWorld.docx");
FileSpecification image = new FileSpecification(dataDir + "aspose-logo.jpg");

// ファイルの説明を提供
excel.Description = "Excelファイル";
word.Description = "Wordファイル";
image.Description = "画像ファイル";

// ファイルをドキュメントコレクションに追加
doc.Collection.Add(excel);
doc.Collection.Add(word);
doc.Collection.Add(image);

// ポートフォリオドキュメントを保存
doc.Save(dataDir + "CreatePDFPortfolio_out.pdf");
```
## PDFポートフォリオからファイルを抽出する

PDFポートフォリオを使用すると、さまざまなソース（例えば、PDF、Word、Excel、JPEGファイルなど）からのコンテンツを一つの統合コンテナにまとめることができます。元のファイルはそれぞれの個性を保ちながらPDFポートフォリオファイルに組み立てられます。ユーザーは、他のコンポーネントファイルと独立して、各コンポーネントファイルを開いたり、読んだり、編集したり、形式を整えたりすることができます。

Aspose.PDFは、[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)クラスを使用してPDFポートフォリオドキュメントの作成を可能にします。また、PDFポートフォリオからファイルを抽出する機能も提供しています。

次のコードスニペットは、PDFポートフォリオからファイルを抽出する手順を示しています。

```csharp
// 完全な例やデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパスです。
string dataDir = RunExamples.GetDataDir_AsposePdf_TechnicalArticles();

// ソースPDFポートフォリオを読み込む
Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(dataDir + "PDFPortfolio.pdf");
// 埋め込まれたファイルのコレクションを取得する
EmbeddedFileCollection embeddedFiles = pdfDocument.EmbeddedFiles;
// ポートフォリオの個々のファイルを反復処理する
foreach (FileSpecification fileSpecification in embeddedFiles)
{
    // 添付ファイルを取得してファイルまたはストリームに書き込む
    byte[] fileContent = new byte[fileSpecification.Contents.Length];
    fileSpecification.Contents.Read(fileContent, 0, fileContent.Length);
    string filename = Path.GetFileName(fileSpecification.Name);
    // 抽出したファイルを何らかの場所に保存する
    FileStream fileStream = new FileStream(dataDir + "_out" + filename, FileMode.Create);
    fileStream.Write(fileContent, 0, fileContent.Length);
    // ストリームオブジェクトを閉じる
    fileStream.Close();
}
```
![PDFポートフォリオからファイルを抽出する](working-with-pdf-portfolio_2.jpg)

## PDFポートフォリオからファイルを削除する

PDFポートフォリオからファイルを削除するには、以下のコード行を使用してみてください。

```csharp
// 完全な例やデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパスです。
string dataDir = RunExamples.GetDataDir_AsposePdf_TechnicalArticles();

// ソースPDFポートフォリオをロードします
Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(dataDir + "PDFPortfolio.pdf");
pdfDocument.Collection.Delete();
pdfDocument.Save(dataDir + "No_PortFolio_out.pdf");
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


