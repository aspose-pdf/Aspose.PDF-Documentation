---
title: 添付ファイルを抽出して保存する
linktitle: 添付ファイルを抽出して保存する
type: docs
weight: 20
url: /ja/net/extract-and-save-an-attachment/
description: Aspose.PDF for .NETでは、PDFドキュメントからすべての添付ファイルを取得することができます。また、ドキュメントから個々の添付ファイルを取得することもできます。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "添付ファイルを抽出して保存する",
    "alternativeHeadline": "添付ファイルの抽出と保存方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDFドキュメント生成",
    "keywords": "pdf, c#, 添付ファイル保存, 添付ファイル抽出",
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
    "url": "/net/extract-and-save-an-attachment/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-and-save-an-attachment/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for .NETでは、PDFドキュメントからすべての添付ファイルを取得することができます。また、ドキュメントから個々の添付ファイルを取得することもできます。"
}
</script>
## すべての添付ファイルを取得

Aspose.PDFを使用すると、PDFドキュメントからすべての添付ファイルを取得することができます。これは、PDFから別々にドキュメントを保存したい場合や、PDFから添付ファイルを削除する必要がある場合に便利です。

PDFファイルからすべての添付ファイルを取得するには：

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) オブジェクトの [EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection) コレクションをループします。[EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection) コレクションにはすべての添付ファイルが含まれています。このコレクションの各要素は [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification) オブジェクトを表します。[EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection) コレクションをforeachループする各反復で [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification) オブジェクトが返されます。
1.

次のコードスニペットは、PDFドキュメントからすべての添付ファイルを取得する方法を示しています。

次のコードスニペットも[Aspose.PDF.Drawing](/pdf/ja/net/drawing/)ライブラリで動作します。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパスです。
string dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "GetAlltheAttachments.pdf");

// 埋め込まれたファイルのコレクションを取得
EmbeddedFileCollection embeddedFiles = pdfDocument.EmbeddedFiles;

// 埋め込まれたファイルの数を取得
Console.WriteLine("合計ファイル数 : {0}", embeddedFiles.Count);

int count = 1;

// コレクションをループしてすべての添付ファイルを取得
foreach (FileSpecification fileSpecification in embeddedFiles)
{
    Console.WriteLine("名前: {0}", fileSpecification.Name);
    Console.WriteLine("説明: {0}",
    fileSpecification.Description);
    Console.WriteLine("MIMEタイプ: {0}", fileSpecification.MIMEType);

    // パラメータオブジェクトにパラメータが含まれているかどうかを確認
    if (fileSpecification.Params != null)
    {
        Console.WriteLine("チェックサム: {0}",
        fileSpecification.Params.CheckSum);
        Console.WriteLine("作成日: {0}",
        fileSpecification.Params.CreationDate);
        Console.WriteLine("変更日: {0}",
        fileSpecification.Params.ModDate);
        Console.WriteLine("サイズ: {0}", fileSpecification.Params.Size);
    }

    // 添付ファイルを取得してファイルまたはストリームに書き込む
    byte[] fileContent = new byte[fileSpecification.Contents.Length];
    fileSpecification.Contents.Read(fileContent, 0,
    fileContent.Length);
    FileStream fileStream = new FileStream(dataDir + count + "_out" + ".txt",
    FileMode.Create);
    fileStream.Write(fileContent, 0, fileContent.Length);
    fileStream.Close();
    count+=1;
}
```
## 個別の添付ファイルを取得

個別の添付ファイルを取得するために、Documentインスタンスの`EmbeddedFiles`オブジェクトで添付ファイルのインデックスを指定することができます。以下のコードスニペットを使用してみてください。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパスです。
string dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "GetIndividualAttachment.pdf");

// 特定の埋め込みファイルを取得
FileSpecification fileSpecification = pdfDocument.EmbeddedFiles[1];

// ファイルのプロパティを取得
Console.WriteLine("名前: {0}", fileSpecification.Name);
Console.WriteLine("説明: {0}", fileSpecification.Description);
Console.WriteLine("MIMEタイプ: {0}", fileSpecification.MIMEType);

// パラメータオブジェクトがパラメータを含んでいるかチェック
if (fileSpecification.Params != null)
{
    Console.WriteLine("チェックサム: {0}",
    fileSpecification.Params.CheckSum);
    Console.WriteLine("作成日: {0}",
    fileSpecification.Params.CreationDate);
    Console.WriteLine("変更日: {0}",
    fileSpecification.Params.ModDate);
    Console.WriteLine("サイズ: {0}", fileSpecification.Params.Size);
}

// 添付ファイルを取得し、ファイルまたはストリームに書き込む
byte[] fileContent = new byte[fileSpecification.Contents.Length];
fileSpecification.Contents.Read(fileContent, 0, fileContent.Length);

FileStream fileStream = new FileStream(dataDir + "test_out" + ".txt", FileMode.Create);
fileStream.Write(fileContent, 0, fileContent.Length);
fileStream.Close();
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
    "applicationCategory": ".NET向けPDF操作ライブラリ",
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

