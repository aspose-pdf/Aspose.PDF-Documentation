---
title: C#でPDFサイズの最適化、圧縮、削減
linktitle: PDFの最適化
type: docs
weight: 30
url: /ja/net/optimize-pdf/
description: PDFファイルを最適化し、すべての画像を縮小し、PDFサイズを削減し、フォントの埋め込みを解除し、使用されていないオブジェクトを削除します。
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "C#を使用してPDFを最適化",
    "alternativeHeadline": ".NETでPDFを最適化する方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDFドキュメント生成",
    "keywords": "pdf, c#, optimize pdf",
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
    "url": "/net/optimize-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/optimize-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": "PDFファイルを最適化し、すべての画像を縮小し、PDFサイズを削減し、フォントの埋め込みを解除し、使用されていないオブジェクトを削除します。"
}
</script>
PDFドキュメントには時々追加データが含まれていることがあります。PDFファイルのサイズを小さくすることで、ネットワーク転送とストレージの最適化に役立ちます。これは、Webページへの公開、ソーシャルネットワークでの共有、電子メールでの送信、またはストレージでのアーカイブに特に便利です。PDFを最適化するためにいくつかの技術を使用できます：

- オンライン閲覧用にページコンテンツを最適化する
- すべての画像を縮小または圧縮する
- ページコンテンツの再利用を有効にする
- 重複するストリームをマージする
- 埋め込まれていないフォント
- 使用されていないオブジェクトを削除する
- フォームフィールドのフラット化を解除する
- アノテーションを削除またはフラット化する

{{% alert color="primary" %}}

最適化方法の詳細な説明は、最適化方法の概要ページで見ることができます。

{{% /alert %}}

## Web用PDFドキュメントの最適化

Web用の最適化、または線形化は、Webブラウザを使用してオンライン閲覧に適したPDFファイルを作成するプロセスを指します。ファイルをWeb表示用に最適化するには：

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)オブジェクトで入力ドキュメントを開く。
1. 最適化されたドキュメントを[保存](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save)メソッドを使用して保存します。

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/)ライブラリでも動作します。

次のコードスニペットは、PDFドキュメントをウェブ用に最適化する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");

// ウェブ用に最適化
pdfDocument.Optimize();

dataDir = dataDir + "OptimizeDocument_out.pdf";

// 出力ドキュメントを保存
pdfDocument.Save(dataDir);
```

## PDFサイズを縮小

[OptimizeResources()](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/optimizeresources)メソッドを使用すると、不要な情報を省くことでドキュメントのサイズを削減できます。
[OptimizeResources()](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/optimizeresources) メソッドは、不要な情報を取り除くことで文書サイズを削減することができます。

- 文書のページで使用されていないリソースは削除されます
- 同じリソースは一つのオブジェクトに結合されます
- 使用されていないオブジェクトは削除されます

以下のスニペットは一例です。ただし、この方法が文書の縮小を保証するわけではないことに注意してください。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "ShrinkDocument.pdf");
// PDFドキュメントを最適化します。ただし、この方法が文書の縮小を保証するわけではないことに注意してください。
pdfDocument.OptimizeResources();
dataDir = dataDir + "ShrinkDocument_out.pdf";
// 更新されたドキュメントを保存する
pdfDocument.Save(dataDir);
```

## 最適化戦略の管理

最適化戦略をカスタマイズすることもできます。
最適化戦略をカスタマイズすることもできます。

### すべての画像の圧縮または縮小

画像を扱う方法は2つあります: 画像の品質を下げるか、解像度を変更するかです。いずれの場合も、[ImageCompressionOptions](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/imagecompressionoptions)を適用する必要があります。次の例では、[ImageQuality](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/imagecompressionoptions/properties/imagequality)を50に減らすことにより画像を縮小しています。

`ImageQuality`はJPEGの品質と同様に機能し、値0は最低、値100は最高です。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET を参照してください
// 文書ディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();
// 文書を開く
Document pdfDocument = new Document(dataDir + "Shrinkimage.pdf");
// OptimizationOptionsを初期化
var optimizeOptions = new Pdf.Optimization.OptimizationOptions();
// CompressImagesオプションを設定
optimizeOptions.ImageCompressionOptions.CompressImages = true;
// ImageQualityオプションを設定
optimizeOptions.ImageCompressionOptions.ImageQuality = 50;
// OptimizationOptionsを使用してPDF文書を最適化
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "Shrinkimage_out.pdf";
// 更新された文書を保存
pdfDocument.Save(dataDir);
```
画像のサイズを低解像度でリサイズする方法もあります。この場合、ResizeImagesをtrueに設定し、MaxResolutionを適切な値に設定する必要があります。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// 時間の初期化
var time = DateTime.Now.Ticks;
// ドキュメントディレクトリへのパス
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();
// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "ResizeImage.pdf");
// OptimizationOptionsの初期化
var optimizeOptions = new Pdf.Optimization.OptimizationOptions();
// CompressImagesオプションを設定
optimizeOptions.ImageCompressionOptions.CompressImages = true;
// ImageQualityオプションを設定
optimizeOptions.ImageCompressionOptions.ImageQuality = 75;
// ResizeImageオプションを設定
optimizeOptions.ImageCompressionOptions.ResizeImages = true;
// MaxResolutionオプションを設定
optimizeOptions.ImageCompressionOptions.MaxResolution = 300;
// OptimizationOptionsを使用してPDFドキュメントを最適化
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "ResizeImages_out.pdf";
// 更新されたドキュメントを保存
pdfDocument.Save(dataDir);
```
もう一つの重要な問題は実行時間です。しかし、この設定も管理できます。現在、私たちは二つのアルゴリズム - スタンダードとファストを使用できます。実行時間を制御するために、[バージョン](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/imagecompressionoptions/properties/version) プロパティを設定する必要があります。次のスニペットはファストアルゴリズムを示しています：

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET にアクセスしてください。
// 時間の初期化
var time = DateTime.Now.Ticks;
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();
// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "Shrinkimage.pdf");
// OptimizationOptionsの初期化
var optimizeOptions = new Pdf.Optimization.OptimizationOptions();
// CompressImagesオプションを設定
optimizeOptions.ImageCompressionOptions.CompressImages = true;
// ImageQualityオプションを設定
optimizeOptions.ImageCompressionOptions.ImageQuality = 75;
// イメージ圧縮バージョンをファストに設定
optimizeOptions.ImageCompressionOptions.Version = Pdf.Optimization.ImageCompressionVersion.Fast;
// OptimizationOptionsを使用してPDFドキュメントを最適化
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "FastShrinkImages_out.pdf";
// 更新されたドキュメントを保存
pdfDocument.Save(dataDir);
Console.WriteLine("Ticks: {0}", DateTime.Now.Ticks - time);
```
### 使用されていないオブジェクトの削除

PDFドキュメントには、ドキュメント内の他のオブジェクトから参照されていないPDFオブジェクトが含まれていることがあります。たとえば、ドキュメントのページツリーからページが削除された場合でも、ページオブジェクト自体が削除されない場合があります。これらのオブジェクトを削除してもドキュメントが無効になるわけではなく、ドキュメントが縮小されます。

```csharp
// 完全な例やデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// RemoveUsedObject オプションを設定
var optimizeOptions = new Pdf.Optimization.OptimizationOptions
{
    RemoveUnusedObjects = true
};
// OptimizationOptions を使用して PDF ドキュメントを最適化
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "OptimizeDocument_out.pdf";
// 更新されたドキュメントを保存
pdfDocument.Save(dataDir);
```

### 使用されていないストリームの削除

ドキュメントには使用されていないリソースストリームが含まれていることがあります。
時々、ドキュメントには使用されていないリソースストリームが含まれています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパスです。
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// RemoveUsedStreams オプションを設定する
var optimizeOptions = new Pdf.Optimization.OptimizationOptions
{
    RemoveUnusedStreams = true
};
// OptimizationOptions を使用して PDF ドキュメントを最適化する
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "OptimizeDocument_out.pdf";
// 更新されたドキュメントを保存する
pdfDocument.Save(dataDir);
```

### 重複するストリームのリンク

一部のドキュメントには、複数の同一のリソースストリーム（例えば画像など）が含まれている場合があります。
いくつかのドキュメントには、同一のリソースストリーム（例えば画像など）がいくつも含まれている場合があります。

```csharp
// 完全な例やデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパスです。
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// LinkDuplcateStreams オプションを設定する
var optimizeOptions = new Pdf.Optimization.OptimizationOptions
{
    LinkDuplcateStreams = true
};
// OptimizationOptions を使用して PDF ドキュメントを最適化する
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "OptimizeDocument_out.pdf";
// 更新されたドキュメントを保存する
pdfDocument.Save(dataDir);
```

さらに、[AllowReusePageContent](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/optimizationoptions/properties/allowreusepagecontent) の設定を使用することができます。
さらに、[AllowReusePageContent](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/optimizationoptions/properties/allowreusepagecontent) 設定を使用することができます。

```csharp
// 完全な例やデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// AllowReusePageContent オプションを設定
var optimizeOptions = new Pdf.Optimization.OptimizationOptions
{
    AllowReusePageContent = true
};
Console.WriteLine("開始");
// OptimizationOptions を使用して PDF ドキュメントを最適化
pdfDocument.OptimizeResources(optimizeOptions);
// 更新されたドキュメントを保存
pdfDocument.Save(dataDir + "OptimizeDocument_out.pdf");
Console.WriteLine("完了");
var fi1 = new System.IO.FileInfo(dataDir + "OptimizeDocument.pdf");
var fi2 = new System.IO.FileInfo(dataDir + "OptimizeDocument_out.pdf");
Console.WriteLine("元のファイルサイズ: {0}. 削減後のファイルサイズ: {1}", fi1.Length, fi2.Length);
```
### フォントの埋め込み解除

ドキュメントが埋め込みフォントを使用している場合、すべてのフォントデータがドキュメントに保存されています。その利点は、ユーザーのマシンにフォントがインストールされているかどうかに関わらず、ドキュメントが表示できることです。しかし、フォントを埋め込むとドキュメントのサイズが大きくなります。フォントの埋め込み解除メソッドは、すべての埋め込みフォントを削除します。これにより、ドキュメントのサイズは減少しますが、正しいフォントがインストールされていない場合、ドキュメント自体が読めなくなる可能性があります。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// UnembedFonts オプションを設定
var optimizeOptions = new Pdf.Optimization.OptimizationOptions
{
    UnembedFonts = true
};
Console.WriteLine("開始");
// OptimizationOptionsを使用してPDFドキュメントを最適化
pdfDocument.OptimizeResources(optimizeOptions);
// 更新されたドキュメントを保存
pdfDocument.Save(dataDir + "OptimizeDocument_out.pdf");
Console.WriteLine("完了");
var fi1 = new System.IO.FileInfo(dataDir + "OptimizeDocument.pdf");
var fi2 = new System.IO.FileInfo(dataDir + "OptimizeDocument_out.pdf");
Console.WriteLine("元のファイルサイズ: {0}. 減少したファイルサイズ: {1}", fi1.Length, fi2.Length);
```
最適化リソースは、これらの方法をドキュメントに適用します。これらの方法のいずれかが適用された場合、ドキュメントのサイズはおそらく減少します。これらの方法が適用されない場合、ドキュメントのサイズは変わらないでしょう。

## PDFドキュメントサイズを減らす追加の方法

### 注釈の削除またはフラット化

注釈は不要な場合に削除できます。編集が必要ないが必要な場合には、フラット化できます。これらの技術はファイルサイズを減らします。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// 注釈をフラット化
foreach (var page in pdfDocument.Pages)
{
    foreach (var annotation in page.Annotations)
    {
        annotation.Flatten();
    }

}
// 更新されたドキュメントを保存
pdfDocument.Save(dataDir + "OptimizeDocument_out.pdf");
```
### フォームフィールドの削除

PDFドキュメントにAcroFormsが含まれている場合、フォームフィールドをフラット化することでファイルサイズを減らすことができます。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// ソースPDFフォームを読み込む
Document doc = new Document(dataDir + "input.pdf");

// フォームをフラット化
if (doc.Form.Fields.Count() > 0)
{
    foreach (var item in doc.Form.Fields)
    {
        item.Flatten();
    }
}

dataDir = dataDir + "FlattenForms_out.pdf";
// 更新されたドキュメントを保存
doc.Save(dataDir);
```

### PDFをRGBカラースペースからグレースケールに変換する

PDFファイルはテキスト、イメージ、添付ファイル、注釈、グラフ、その他のオブジェクトで構成されています。
PDFファイルにはテキスト、画像、添付ファイル、注釈、グラフ、その他のオブジェクトが含まれています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// ソースPDFファイルをロード
using (Document document = new Document(dataDir + "input.pdf"))
{
    Aspose.Pdf.RgbToDeviceGrayConversionStrategy strategy = new Aspose.Pdf.RgbToDeviceGrayConversionStrategy();
    for (int idxPage = 1; idxPage <= document.Pages.Count; idxPage++)
    {
        // PDF内の特定のページのインスタンスを取得
        Page page = document.Pages[idxPage];
        // RGBカラースペースの画像をグレースケールカラースペースに変換
        strategy.Convert(page);
    }
    // 結果のファイルを保存
    document.Save(dataDir + "Test-gray_out.pdf");
}
```

### FlateDecode圧縮

{{% alert color="primary" %}}

この機能はバージョン18.12以降でサポートされています。

{{% /alert %}}

Aspose.PDF for .NETは、PDF最適化機能のためのFlateDecode圧縮をサポートしています。
Aspose.PDF for .NETは、PDF最適化機能のためのFlateDecode圧縮をサポートしています。

{{< gist "aspose-com-gists" "63473b1ba28e09e229cfbf4430eabd8a" "Examples-CSharp-AsposePDF-Images-FlateDecodeCompression-1.cs" >}}

### **XImageCollectionに画像を保存する**

Aspose.PDF for .NETは、**XImageCollection**に新しい画像をFlateDecode圧縮で保存する機能を提供します。このオプションを有効にするには、**ImageFilterType.Flate**フラグを使用できます。以下のコードスニペットは、この機能を使用する方法を示しています:

{{< gist "aspose-com-gists" "63473b1ba28e09e229cfbf4430eabd8a" "Examples-CSharp-AsposePDF-Images-StoreImageInXImageCollection-1.cs" >}}

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

