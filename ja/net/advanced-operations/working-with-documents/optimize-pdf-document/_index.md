---
title: C#でPDFサイズを最適化、圧縮、または削減する
linktitle: PDFを最適化
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ja/net/optimize-pdf/
description: C#を使用してPDFファイルを最適化し、すべての画像を縮小し、PDFのサイズを削減し、フォントをアンエンベッドし、未使用のオブジェクトを削除します。
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Optimize, Compress or Reduce PDF Size in C#",
    "alternativeHeadline": "Optimize PDF Files Efficiently with C#",
    "abstract": "C#の新しいPDF最適化機能により、開発者は画像の圧縮、フォントのアンエンベッド、未使用オブジェクトの削除など、複数の戦略を使用してPDFファイルのサイズを大幅に削減できます。この改善により、ウェブ出版、メール共有、ストレージの効率が向上し、大きなPDFドキュメントの管理に効果的なソリューションを提供します。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "optimize pdf, compress pdf size, reduce pdf size, optimize pdf c#, unembed fonts, remove unused objects, shrink images, optimization methods, pdf document generation, Aspose.PDF",
    "wordcount": "2282",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
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
    "dateModified": "2024-11-25",
    "description": "C#を使用してPDFファイルを最適化し、すべての画像を縮小し、PDFのサイズを削減し、フォントをアンエンベッドし、未使用のオブジェクトを削除します。"
}
</script>

PDFドキュメントには、時折追加データが含まれることがあります。PDFファイルのサイズを削減することで、ネットワーク転送とストレージを最適化できます。これは、ウェブページへの公開、ソーシャルネットワークでの共有、電子メールでの送信、またはストレージへのアーカイブに特に便利です。PDFを最適化するために、いくつかの技術を使用できます：

- オンラインブラウジング用にページコンテンツを最適化します。
- すべての画像を縮小または圧縮します。
- ページコンテンツの再利用を有効にします。
- 重複ストリームをマージします。
- フォントをアンエンベッドします。
- 未使用のオブジェクトを削除します。
- フラッティングフォームフィールドを削除します。
- 注釈を削除またはフラット化します。

{{% alert color="primary" %}}

最適化方法の詳細な説明は、最適化方法の概要ページにあります。

{{% /alert %}}

## ウェブ用にPDFドキュメントを最適化する

最適化、またはウェブ用の線形化は、PDFファイルをウェブブラウザでオンラインブラウジングに適したものにするプロセスを指します。ウェブ表示用にファイルを最適化するには：

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)オブジェクトで入力ドキュメントを開きます。
1. [Optimize](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/optimize)メソッドを使用します。
1. [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save)メソッドを使用して最適化されたドキュメントを保存します。

以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/)ライブラリでも機能します。

以下のコードスニペットは、ウェブ用にPDFドキュメントを最適化する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizeDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Optimize for web
        document.Optimize();

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");
    }
}
```

## PDFサイズを削減する

[OptimizeResources()](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/optimizeresources)メソッドを使用すると、不要な情報を取り除くことでドキュメントサイズを削減できます。デフォルトでは、このメソッドは次のように機能します：

- ドキュメントページで使用されていないリソースが削除されます。
- 同じリソースが1つのオブジェクトに結合されます。
- 未使用のオブジェクトが削除されます。

以下のスニペットはその例です。ただし、このメソッドはドキュメントの縮小を保証するものではありません。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ShrinkDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ShrinkDocument.pdf"))
    {
        // Optimize PDF document. Note, though, that this method cannot guarantee document shrinking
        document.OptimizeResources();

        // Save PDF document
        document.Save(dataDir + "ShrinkDocument_out.pdf");
    }
}
```

## 最適化戦略の管理

最適化戦略をカスタマイズすることもできます。現在、[OptimizeResources()](https://reference.aspose.com/pdf/net/aspose.pdf.document/optimizeresources/methods/1)メソッドは5つの技術を使用しています。これらの技術は、[OptimizationOptions](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/optimizationoptions)パラメータを使用してOptimizeResources()メソッドで適用できます。

### すべての画像を縮小または圧縮する

画像で作業する方法は2つあります：画像の品質を低下させるか、解像度を変更するかです。いずれの場合でも、[ImageCompressionOptions](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/imagecompressionoptions)を適用する必要があります。次の例では、[ImageQuality](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/imagecompressionoptions/properties/imagequality)を50に設定して画像を縮小します。

`ImageQuality`はJPEG品質と同様に機能し、値0が最低、値100が最高です。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ShrinkImage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Shrinkimage.pdf"))
    {
        // Initialize OptimizationOptions
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions();

        // Set CompressImages option
        optimizeOptions.ImageCompressionOptions.CompressImages = true;

        // Set ImageQuality option
        optimizeOptions.ImageCompressionOptions.ImageQuality = 50;

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "Shrinkimage_out.pdf");
    }
}
```

もう1つの方法は、解像度を下げて画像のサイズを変更することです。この場合、ResizeImagesをtrueに設定し、MaxResolutionを適切な値に設定する必要があります。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ResizeImages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ResizeImage.pdf"))
    {
        // Initialize OptimizationOptions
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions();

        // Set CompressImages option
        optimizeOptions.ImageCompressionOptions.CompressImages = true;

        // Set ImageQuality option
        optimizeOptions.ImageCompressionOptions.ImageQuality = 75;

        // Set ResizeImage option
        optimizeOptions.ImageCompressionOptions.ResizeImages = true;

        // Set MaxResolution option
        optimizeOptions.ImageCompressionOptions.MaxResolution = 300;

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "ResizeImages_out.pdf");
    }
}
```

もう1つの重要な問題は、実行時間です。しかし、再度、この設定も管理できます。現在、2つのアルゴリズム - 標準と高速を使用できます。実行時間を制御するには、[Version](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/imagecompressionoptions/properties/version)プロパティを設定する必要があります。以下のスニペットは、高速アルゴリズムを示しています：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FastShrinkImages()
{
    // Initialize Time
    var time = DateTime.Now.Ticks;

    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Shrinkimage.pdf"))
    {
        // Initialize OptimizationOptions
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions();

        // Set CompressImages option
        optimizeOptions.ImageCompressionOptions.CompressImages = true;

        // Set ImageQuality option
        optimizeOptions.ImageCompressionOptions.ImageQuality = 75;

        // Set Image Compression Version to fast
        optimizeOptions.ImageCompressionOptions.Version = Aspose.Pdf.Optimization.ImageCompressionVersion.Fast;

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "FastShrinkImages_out.pdf");
    }

    // Output the time taken for the operation
    Console.WriteLine("Ticks: {0}", DateTime.Now.Ticks - time);
}
```

### 未使用のオブジェクトを削除する

PDFドキュメントには、他のオブジェクトから参照されていないPDFオブジェクトが含まれていることがあります。これは、たとえば、ドキュメントページツリーからページが削除されたが、ページオブジェクト自体が削除されていない場合に発生することがあります。これらのオブジェクトを削除してもドキュメントが無効になることはありませんが、むしろサイズが縮小されます。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizeDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Set RemoveUsedObject option
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions
        {
            RemoveUnusedObjects = true
        };
        
        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");
    }
}
```

### 未使用のストリームを削除する

時々、ドキュメントには未使用のリソースストリームが含まれています。これらのストリームは、ページリソース辞書から参照されているため、「未使用オブジェクト」ではありません。したがって、「未使用のオブジェクトを削除する」メソッドでは削除されません。しかし、これらのストリームはページコンテンツでは決して使用されません。これは、ページから画像が削除されたが、ページリソースからは削除されていない場合に発生することがあります。また、この状況は、ページがドキュメントから抽出され、ドキュメントページが「共通」リソース、つまり同じResourcesオブジェクトを持つ場合によく発生します。リソースストリームが使用されているかどうかを判断するためにページコンテンツが分析されます。未使用のストリームが削除されます。これにより、ドキュメントサイズが減少することがあります。この技術の使用は前のステップと似ています：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizePdfDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Set RemoveUsedStreams option
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions
        {
            RemoveUnusedStreams = true
        };

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");
    }
}
```

### 重複ストリームをリンクする

一部のドキュメントには、同一のリソースストリーム（たとえば画像など）が複数含まれていることがあります。これは、たとえば、ドキュメントが自分自身と連結された場合に発生することがあります。出力ドキュメントには、同じリソースストリームの2つの独立したコピーが含まれています。すべてのリソースストリームを分析し、比較します。ストリームが重複している場合、それらはマージされ、つまり1つのコピーだけが残ります。参照は適切に変更され、オブジェクトのコピーは削除されます。場合によっては、これによりドキュメントサイズが減少するのに役立ちます。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizePdfDocumentWithLinkDuplicateStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Set LinkDuplicateStreams option
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions
        {
            LinkDuplicateStreams = true
        };

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");
    }
}
```

さらに、[AllowReusePageContent](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/optimizationoptions/properties/allowreusepagecontent)設定を使用できます。このプロパティがtrueに設定されている場合、同一ページの最適化時にページコンテンツが再利用されます。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizePdfDocumentWithReusePageContent()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Set AllowReusePageContent option
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions
        {
            AllowReusePageContent = true
        };

        Console.WriteLine("Start");

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");
    }

    Console.WriteLine("Finished");

    // Calculate and display file sizes
    var fi1 = new FileInfo(dataDir + "OptimizeDocument.pdf");
    var fi2 = new FileInfo(dataDir + "OptimizeDocument_out.pdf");
    Console.WriteLine("Original file size: {0}. Reduced file size: {1}", fi1.Length, fi2.Length);
}
```

### フォントのアンエンベッド

ドキュメントが埋め込まれたフォントを使用している場合、すべてのフォントデータがドキュメントに保存されていることを意味します。利点は、フォントがユーザーのマシンにインストールされているかどうかに関係なく、ドキュメントが表示可能であることです。しかし、フォントを埋め込むとドキュメントが大きくなります。フォントのアンエンベッドメソッドは、すべての埋め込まれたフォントを削除します。これにより、ドキュメントサイズが減少しますが、正しいフォントがインストールされていない場合、ドキュメント自体が読めなくなる可能性があります。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizePdfDocumentWithUnembedFonts()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Set UnembedFonts option
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions
        {
            UnembedFonts = true
        };

        Console.WriteLine("Start");

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");	
    }
	
    Console.WriteLine("Finished");

    // Calculate and display file sizes
    var fi1 = new FileInfo(dataDir + "OptimizeDocument.pdf");
    var fi2 = new FileInfo(dataDir + "OptimizeDocument_out.pdf");
    Console.WriteLine("Original file size: {0}. Reduced file size: {1}", fi1.Length, fi2.Length);
}
```

最適化リソースは、これらのメソッドをドキュメントに適用します。これらのメソッドのいずれかが適用されると、ドキュメントサイズはおそらく減少します。これらのメソッドが適用されない場合、ドキュメントサイズは変わらないことは明らかです。

## PDFドキュメントサイズを削減するための追加方法

### 注釈を削除またはフラット化する

注釈は、不要な場合に削除できます。必要だが追加の編集を必要としない場合は、フラット化できます。これらの技術の両方は、ファイルサイズを削減します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FlattenAnnotationsInPdfDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Flatten annotations
        foreach (var page in document.Pages)
        {
            foreach (var annotation in page.Annotations)
            {
                annotation.Flatten();
            }
        }

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");
    }
}
```

### フォームフィールドを削除する

PDFドキュメントにAcroFormsが含まれている場合、フォームフィールドをフラット化することでファイルサイズを削減できるかもしれません。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FlattenPdfForms()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Load source PDF form
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Flatten Forms
        if (document.Form.Fields.Lenght > 0)
        {
            foreach (var item in document.Form.Fields)
            {
                item.Flatten();
            }
        }

        // Save PDF document
        document.Save(dataDir + "FlattenForms_out.pdf");
    }
}
```

### PDFをRGBカラースペースからグレースケールに変換する

PDFファイルは、テキスト、画像、添付ファイル、注釈、グラフ、その他のオブジェクトで構成されています。PDFをRGBカラースペースからグレースケールに変換する必要がある場合があります。これにより、これらのPDFファイルを印刷する際に速度が向上します。また、ファイルがグレースケールに変換されると、ドキュメントサイズも削減されますが、ドキュメントの品質が低下する可能性もあります。この機能は現在、Adobe AcrobatのPre-Flight機能によってサポートされていますが、Office自動化について話すと、Aspose.PDFはドキュメント操作のための究極のソリューションです。この要件を達成するために、以下のコードスニペットを使用できます。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertRgbToGrayScale()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Create RGB to DeviceGray conversion strategy
        var strategy = new Aspose.Pdf.RgbToDeviceGrayConversionStrategy();

        // Iterate through each page
        for (int idxPage = 1; idxPage <= document.Pages.Count; idxPage++)
        {
            // Get instance of particular page inside PDF
            var page = document.Pages[idxPage];

            // Convert the RGB colorspace image to GrayScale colorspace
            strategy.Convert(page);
        }

        // Save PDF document
        document.Save(dataDir + "TestGray_out.pdf");
    }
}
```

### FlateDecode圧縮

{{% alert color="primary" %}}

この機能はバージョン18.12以上でサポートされています。

{{% /alert %}}

Aspose.PDF for .NETは、PDF最適化機能のためのFlateDecode圧縮をサポートしています。以下のコードスニペットは、**FlateDecode**圧縮で画像を保存するためのオプションを最適化で使用する方法を示しています：

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizeDocumentImagesWithFlateCompression()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddImage.pdf"))
    {
        // Initialize OptimizationOptions
        var optimizationOptions = new Aspose.Pdf.Optimization.OptimizationOptions();

        // To optimize images using FlateDecode compression, set optimization options to Flate
        optimizationOptions.ImageCompressionOptions.Encoding = Aspose.Pdf.Optimization.ImageEncoding.Flate;

        // Set optimization options
        document.OptimizeResources(optimizationOptions);

        // Save PDF document
        document.Save(dataDir + "OptimizeDocumentImagesWithFlateCompression_out.pdf");
    }
}
```

### XImageCollectionに画像を保存する

Aspose.PDF for .NETは、FlateDecode圧縮で新しい画像を**XImageCollection**に保存する機能を提供します。このオプションを有効にするには、**ImageFilterType.Flate**フラグを使用できます。以下のコードスニペットは、この機能を使用する方法を示しています：

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageToPdfWithFlateCompression()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Open the image file stream
        using (var imageStream = new FileStream(dataDir + "aspose-logo.jpg", FileMode.Open))
        {
            // Add the image to the page resources with Flate compression
            page.Resources.Images.Add(imageStream, Aspose.Pdf.ImageFilterType.Flate);
        }

        // Get the added image
        var ximage = page.Resources.Images[page.Resources.Images.Count];

        // Save the current graphics state
        page.Contents.Add(new Aspose.Pdf.Operators.GSave());

        // Set coordinates for the image placement
        int lowerLeftX = 0;
        int lowerLeftY = 0;
        int upperRightX = 600;
        int upperRightY = 600;

        var rectangle = new Aspose.Pdf.Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
        var matrix = new Aspose.Pdf.Matrix(new double[]
        {
            rectangle.URX - rectangle.LLX, 0, 0, rectangle.URY - rectangle.LLY, rectangle.LLX, rectangle.LLY
        });

        // Use ConcatenateMatrix operator to define how the image must be placed
        page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(matrix));
        page.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));

        // Restore the graphics state
        page.Contents.Add(new Aspose.Pdf.Operators.GRestore());

        // Save the document
        document.Save(dataDir + "AddImageToPdfWithFlateCompression_out.pdf");
    }
}
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