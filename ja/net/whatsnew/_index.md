---
title: 新機能
linktitle: 新機能
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ja/net/whatsnew/
description: このページでは、最近のリリースで導入されたAspose.PDF for .NETの最も人気のある新機能を紹介します。
sitemap:
    changefreq: "monthly"
    priority: 0.8
lastmod: "2025-01-31"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Whats new",
    "alternativeHeadline": "Discover the latest enhancements in Aspose.PDF for .NET",
    "abstract": "Aspose.PDF for .NETの最新の強化を発見してください。これには、堅牢な文書署名と検証のための楕円曲線デジタル署名アルゴリズム（ECDSA）の導入と、複数の楕円曲線のサポートが含まれます。さらに、新機能により、PDFへの挿入時に画像をトリミングできるようになり、エラー処理の改善のためのクラッシュレポートの生成が可能になります。これらの更新により、PDF管理が効率化され、文書ワークフローのセキュリティが強化されます。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "8022",
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
    "url": "/net/whatsnew/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/whatsnew/"
    },
    "dateModified": "2024-12-04",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

## Aspose.PDF 25.2の新機能

**最も重要な変更点**

Aspose.PDF 25.2では、以下を追加しました：
* [PDFからPDF/X-4](https://docs.aspose.com/pdf/net/convert-pdf-to-pdfx/)標準への変換のサポート。
* 署名中にCustomSignHashデリゲートを二度呼び出さないための[オプション](https://docs.aspose.com/pdf/net/digitally-sign-pdf-file/#sign-a-pdf-with-hash-signing-function)。
* PDFの[digital signatures](https://docs.aspose.com/pdf/net/digitally-sign-pdf-file/#sign-pdf-with-digital-signatures)に関する情報を取得するための新しい`GetSignatureNames()`メソッド。
* 複数のウィジェット注釈を持つ[TextBoxField](https://docs.aspose.com/pdf/net/create-form/#adding-radiobuttonfield)の作成の可能性。
> [!NOTE]
> 変更に関する詳細情報と使用例は、[Aspose.PDF 25.2リリースノート](https://releases.aspose.com/pdf/net/release-notes/2025/aspose-pdf-for-net-25-2-release-notes/)ページで確認できます。

**その他の注目すべき強化**

* [PDF最適化](https://docs.aspose.com/pdf/net/optimize-pdf/#shrinking-or-compressing-all-images)における品質損失なしの画像圧縮が強化されました。圧縮された文書のサイズが削減されました。
* 文書の[Repair](https://reference.aspose.com/pdf/ja/net/aspose.pdf/document/repair/)メソッドが改善されました。これにより、Annotation.Rect配列内の値をチェックして修正できるようになりました。
* システムのText.Json依存関係のバージョンが更新され、潜在的な脆弱性CVE-2024-43485を回避しました。
* PDF署名攻撃の検出が改善され、誤検知の結果を防止します。
* リソース辞書を削除するための公開APIが提供されました：

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddingNewExtGState()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDirAsposePdfFacadesPages();

    // Graphics state parameter dictionary new name
    var gsName = "GS0";

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        var page = doc.Pages[1];
        var dictionaryEditor = new DictionaryEditor(page.Resources);
        var states = dictionaryEditor["ExtGState"].ToCosPdfDictionary();

        var newGs = CosPdfDictionary.CreateEmptyDictionary(doc);
        var pairs = new KeyValuePair<string, ICosPdfPrimitive>[3]
        {
            new KeyValuePair<string, ICosPdfPrimitive>("CA", new CosPdfNumber(1)),
            new KeyValuePair<string, ICosPdfPrimitive>("ca", new CosPdfNumber(0.5)),
            new KeyValuePair<string, ICosPdfPrimitive>("BM", new CosPdfName("Normal"))
        };

        foreach (var p in pairs)
        {
            newGs.Add(p);
        }
        states.Add(gsName, newGs);

        // Save PDF document
        doc.Save(outputPath);
    }
}
```

## Aspose.PDF 25.1の新機能

Aspose.PDF 25.1では、以下を追加しました：
* すべてのラスタ画像をスキップしてPDFをHTMLに保存するオプション。
* 証明書機関（CA）サーバーを使用してPDF署名を検証する機能。
* SHA-3ハッシュアルゴリズムを使用したクロスプラットフォームPDF署名検証。

変更に関する詳細情報と使用例は、[Aspose.PDF 25.1リリースノート](https://releases.aspose.com/pdf/net/release-notes/2025/aspose-pdf-for-net-25-1-release-notes/)ページで確認できます。

## Aspose.PDF 24.12の新機能

PDF/XおよびPDF/A変換のための外部ICCプロファイルへのパスを渡す機能は、PdfFormatConversionOptions.IccProfileFileNameプロパティによって数年前からライブラリに存在していました。現在、OutputIntentクラスのオブジェクトを使用してOutputIntentプロパティにデータを渡すことも可能です。

次のスニペットは、注釈FOGRA39 ICCプロファイルを使用して注釈文書をPDF/X-1に変換する方法を示しています：
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPdfToPdfx1UsingCustomIccProfile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SimpleResume.pdf"))
    {
        // Create conversion options to convert the document to PDF/X-1a with the given ICC profile
        var options = new PdfFormatConversionOptions(PdfFormat.PDF_X_1A, ConvertErrorAction.Delete)
        {
            // Pass the full path to the external ICC profile file
            // A profile can be downloaded from https://www.color.org/registry/Coated_Fogra39L_VIGC_300.xalter
            IccProfileFileName = "Coated_Fogra39L_VIGC_300.icc",

            // Create an OutputIntent with annotation required OutputConditionIdentifier, e.g. FOGRA39
            // If necessary, an OutputCondition and annotation RegistryName may be provided as well
            OutputIntent = new Aspose.Pdf.OutputIntent("FOGRA39")
        };

        // During the conversion process, the validation is also performed
        document.Convert(options);

        // Save PDF document
        document.Save(dataDir + "outputPdfx.pdf");
    }
}
```

文書生成、変換、およびテキスト置換のために最も適したフォントを見つけるためのアナライザーが追加されました。最も適したフォントの検索は、ソースPDFに要求された操作を実行するためのフォント情報が不足している場合に行われます。「最も適した」フォントは、PDFフォントに関する情報と要求されたテキスト言語および文字セットに基づいて、環境にインストールされているフォントの中から決定されます。

次のサンプルは、テキストが空白の四角に変わらないようにPDFからPNGへの変換でこれをどのように使用できるかを示しています。
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PdfToPngWithAnalyzingFonts()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ConvertAllPagesToBmp.pdf"))
    {
        var pngDevice = new Aspose.Pdf.Devices.PngDevice();
        pngDevice.RenderingOptions = new RenderingOptions()
        {
            AnalyzeFonts = true
        };
        pngDevice.Process(document.Pages[1], dataDir + "converted.png");
    }
}
```

Aspose.PDF 24.12以降、注釈PDFファイルにテキストスタンプを追加する際にフォントサイズを自動調整することができます。

次のコードスニペットは、注釈PDFファイルに注釈テキストスタンプを追加し、スタンプの矩形に合わせてフォントサイズを自動調整する方法を示しています。
```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AutoSetTheFontSizeOfTextStamp()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDirAsposePdfFacadesPages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Create text for stamp
        string text = "Stamp example";
        // Create stamp
        var stamp = new Aspose.Pdf.TextStamp(text);
        stamp.AutoAdjustFontSizeToFitStampRectangle = true;
        stamp.AutoAdjustFontSizePrecision = 0.01f;
        stamp.WordWrapMode = Aspose.Pdf.Text.TextFormattingOptions.WordWrapMode.ByWords;
        stamp.Scale = false;
        stamp.Width = 400;
        stamp.Height = 200;
        //Add stamp
        document.Pages[1].AddStamp(stamp);

        // Save PDF document
        document.Save(dataDir + "AutoSetTheFontSizeOfTextStamp_out.pdf");
    }
}
```

次のコードスニペットは、注釈PDFファイルに注釈テキストスタンプを追加し、ページサイズに合わせてフォントサイズを自動調整する方法を示しています。
```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AutoSetTheFontSizeOfTextStampToFitPage()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDirAsposePdfFacadesPages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Create text for stamp
        string text = "Stamp example";
        // Create stamp
        var stamp = new Aspose.Pdf.TextStamp(text);
        stamp.AutoAdjustFontSizeToFitStampRectangle = true;
        stamp.AutoAdjustFontSizePrecision = 0.01f;
        stamp.WordWrapMode = Aspose.Pdf.Text.TextFormattingOptions.WordWrapMode.ByWords;
        stamp.Scale = false;
        //Add stamp
        document.Pages[1].AddStamp(stamp);

        // Save PDF document
        document.Save(dataDir + "AutoSetTheFontSizeOfTextStampToFItPage_out.pdf");
    }
}
```

## Aspose.PDF 24.11の新機能

新しいページを追加または挿入する際にページ番号と日付のヘッダー/フッターのアーティファクトを更新するための`PageCollection`拡張メソッドが追加されました。ページ番号と日付形式の設定は、Adobe Acrobatによって実装されたPDF仕様に従って元の文書に保存される必要があります。

次のコードスニペットは、文書内のページ付けを更新する方法を示しています：
```csharp
private static void UpdatePagination()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document that contains at least one page with pagination artifacts
    using (var document = new Aspose.Pdf.Document(dataDir + "DocumentWithPaginationArtifacts.pdf"))
    {
        // Update pages
        document.Pages.Insert(1, document.Pages[2]);
        document.Pages.Add();

        // Update pagination artifacts
        document.Pages.UpdatePagination();

        // Save PDF document
        document.Save(dataDir + "DocumentWithUpdatedPagination.pdf");
    }
}
```

バージョン24.11以降、Pkcs7Detachedのハッシュアルゴリズムを選択する機能が追加されました。デフォルトはSHA-256です。ECDSAデジタル署名の場合、デフォルトのダイジェストアルゴリズムはキーの長さに依存します。

ECDSAはSHA-1、SHA-256、SHA-384、SHA-512、SHA3-256、SHA3-384、およびSHA3-512をサポートしています。SHA3-256、SHA3-384、およびSHA3-512アルゴリズムは、.NET 8および新しいバージョンでのみサポートされています。SHA-3のサポートプラットフォームの詳細については、[ドキュメント](https://learn.microsoft.com/en-us/dotnet/standard/security/cross-platform-cryptography#sha-3)を参照してください。

RSAはSHA-1、SHA-256、SHA-384、およびSHA-512をサポートしています。

DSAはSHA-1のみをサポートしています。SHA-1は古く、現在のセキュリティ基準を満たしていないことに注意してください。

次のコードスニペットは、Pkcs7Detachedのハッシュアルゴリズムを設定する方法を示しています：
```csharp
private static void SignWithManualDigestHashAlgorithm(string cert, string pass)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DigitallySign.pdf"))
    {
        // Instantiate PdfFileSignature object
        using (var signature = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {
            // Create PKCS#7 detached object for sign
            var pkcs = new Aspose.Pdf.Forms.PKCS7Detached(cert, pass, Aspose.Pdf.DigestHashAlgorithm.Sha512);
            // Sign PDF file
            signature.Sign(1, true, new System.Drawing.Rectangle(300, 100, 400, 200), pkcs);
            // Save PDF document
            signature.Save(dataDir + "DigitallySign_out.pdf");
        }
    }
}
```

`HtmlSaveOptions`クラスに新しい`FontEncodingStrategy`プロパティが追加されました。PDF仕様では、PDFからテキストコンテンツを抽出するために`ToUnicode`テーブルを使用することを推奨しています。ただし、フォントのCMapテーブルを使用すると、特定のタイプの文書に対してより良い結果が得られる場合があります。バージョン24.11以降、どのテーブルをデコードに使用するかを選択できます。デフォルトでは、`ToUnicode`テーブルが使用されます。

次のサンプルは、新しいオプションの使用方法を示しています：
```csharp
private static void ConvertPdfToHtmlUsingCMap()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Instantiate HTML SaveOptions object
        var options = new Aspose.Pdf.HtmlSaveOptions
        {
            // New option there
            FontEncodingStrategy = Aspose.Pdf.HtmlSaveOptions.FontEncodingRules.DecreaseToUnicodePriorityLevel
        };
        // Save HTML document
        document.Save(dataDir + "CmapFontHTML_out.html", options);
    }
}
```

## Aspose.PDF 24.10の新機能

楕円曲線デジタル署名アルゴリズム（ECDSA）は、従来のアルゴリズムと比較して小さなキーサイズで強力なセキュリティを提供することで知られる現代の暗号アルゴリズムです。バージョン24.10以降、ECDSAを使用してPDF文書に署名し、ECDSA署名を検証することが可能になりました。デジタル署名の作成と検証にサポートされている楕円曲線は次のとおりです：
* P-256 (secp256r1)。
* P-384 (secp384r1)。
* P-521 (secp521r1)。
* brainpoolP256r1。
* brainpoolP384r1。
* brainpoolP512r1。

署名を生成するためにSHA-256ハッシュアルゴリズムが使用されます。ECDSA署名は、次のハッシュアルゴリズムを使用して検証できます：SHA-256、SHA-384、SHA-512、SHA3-256、SHA3-384、およびSHA3-512。

通常のコードを使用して、ECDSAで文書に署名し、署名を検証できます：
 
```cs
private static void Sign(string cert, string pass)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DigitallySign.pdf"))
    {
        // Instantiate PdfFileSignature object
        using (var signature = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {
            // Create PKCS#7 detached object for sign
            var pkcs = new Aspose.Pdf.Forms.PKCS7Detached(cert, pass);
            // Sign PDF file
            signature.Sign(1, true, new System.Drawing.Rectangle(300, 100, 400, 200), pkcs);
            // Save PDF document
            signature.Save(dataDir + "DigitallySign_out.pdf");
        }
    }
}

private static void Verify()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DigitallySign_out.pdf"))
    {
        // Instantiate PdfFileSignature object
        using (var signature = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {
            // Get annotation list of signature names in the document
            var sigNames = signature.GetSignNames();

            // Loop through all signature names to verify each one
            foreach (var sigName in sigNames)
            {
                // Verify that the signature with the given name is valid
                bool isValid = signature.VerifySignature(sigName);
                Console.WriteLine("Signature '{0}' validation returns {1}", sigName, isValid);
            }
        }
    }
}
```

時には、PDFに挿入する前に画像をトリミングする必要があります。トリミングされた画像を追加するために`AddImage()`メソッドのオーバーロードバージョンを追加しました：

```cs
private static void AddCroppedImageToPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Open image stream
        using (Stream imgStream = File.OpenRead(Path.Combine(dataDir, "Images", "Sample-01.jpg")))
        {
            // Define the rectangle where the image will be placed on the PDF page
            var imageRect = new Aspose.Pdf.Rectangle(17.62, 65.25, 602.62, 767.25);

            // Crop the image to half its original width and height
            var w = imageRect.Width / 2;
            var h = imageRect.Height / 2;
            var bbox = new Aspose.Pdf.Rectangle(imageRect.LLX, imageRect.LLY, imageRect.LLX + w, imageRect.LLY + h);

            // Add page
            var page = document.Pages.Add();

            // Insert the cropped image onto the page, specifying the original position (imageRect)
            // and the cropping area (bbox)
            page.AddImage(imgStream, imageRect, bbox);
        }

        // Save PDF document
        document.Save(dataDir + "AddCroppedImageMender_out.pdf");
    }
}
```

## Aspose.PDF 24.9の新機能

バージョン24.9以降、ライブラリが例外をスローしたときにクラッシュレポートを生成することが可能になりました。クラッシュレポートには、例外の種類、アプリケーションのタイトル、Aspose.PDFのバージョン、OSのバージョン、エラーメッセージ、およびスタックトレースに関する情報が含まれます。

次のコードスニペットは、クラッシュレポートを生成する一般的なシナリオを示しています：

```cs
private static void GenerateCrashReportExample()
{
    try
    {
        // some code
        // ....

        // Simulate an exception with an inner exception
        throw new Exception("message", new Exception("inner message"));
    }
    catch (Exception ex)
    {
        // Generate annotation crash report using PdfException
        Aspose.Pdf.PdfException.GenerateCrashReport(new Aspose.Pdf.CrashReportOptions(ex));
    }
}
```

PDF文書のレイヤー要素を抽出し、新しいPDFストリームに保存することが可能になりました。PDF文書では、レイヤー（オプショナルコンテンツグループまたはOCGとも呼ばれる）は、主に文書内のコンテンツの可視性を管理および制御するために使用されます。この機能は、設計、エンジニアリング、および出版に特に便利です。たとえば：青写真の側面、複雑な図のコンポーネント、同じコンテンツの言語バージョン。

```cs
private static void ExtractPdfLayer()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var inputDocument = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get layers from the first page
        var layers = inputDocument.Pages[1].Layers;

        // Save each layer to the output path
        foreach (var layer in layers)
        {
            layer.Save(dataDir + string.Format("Layer_{0}.pdf", layer.Id));
        }
    }
}
```

`GraphicalPdfComparer`クラスが追加され、PDF文書とページのグラフィック比較が可能になりました。グラフィック比較は、文書ページの画像を扱います。結果は`ImagesDifference`オブジェクトまたは、元の画像と差分をマージしたPDF文書として返されます。グラフィック比較は、テキストやグラフィックコンテンツにわずかな違いがある文書に最も役立ちます。

次のコードスニペットは、2つのPDF文書のグラフィック比較を示し、差分を含む画像を結果のPDF文書に保存します：

```cs
private static void ComparePDFWithCompareDocumentsToPdfMethod()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentCompare();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "ComparePDFWithCompareDocumentsToPdfMethod1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "ComparePDFWithCompareDocumentsToPdfMethod2.pdf"))
        {
            // Create comparer
            var comparer = new Aspose.Pdf.Comparison.GraphicalPdfComparer()
            {
                Threshold = 3.0,
                Color = Aspose.Pdf.Color.Blue,
                Resolution = new Aspose.Pdf.Devices.Resolution(300)
            };
            // Compare and save result
            comparer.CompareDocumentsToPdf(document1, document2, dataDir + "compareDocumentsToPdf_out.pdf");
        }
    }
}
```

APIがFileFormat.HEICとAspose.PDFの統合のために実装されました。HEIC（High-Efficiency Image Coding）は、2017年にAppleによってiOS 11で導入された現代の画像ファイル形式で、iPhoneやiPadのデフォルトの画像形式です。

HEIC画像をPDFに変換するには、`FileFormat.HEIC` NuGetパッケージへの参照を追加し、次のコードスニペットを使用する必要があります：

```cs
private static void ConvertHEICtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open HEIC file
    using (var fs = new FileStream(dataDir + "HEICtoPDF.heic", FileMode.Open))
    {
        var image = FileFormat.Heic.Decoder.HeicImage.Load(fs);
        var pixels = image.GetByteArray(FileFormat.Heic.Decoder.PixelFormat.Rgb24);
        var width = (int)image.Width;
        var height = (int)image.Height;

        // Open PDF document
        using (var document = new Aspose.Pdf.Document())
        {
            var page = document.Pages.Add();
            var asposeImage = new Aspose.Pdf.Image();
            asposeImage.BitmapInfo = new Aspose.Pdf.BitmapInfo(pixels, width, height, Aspose.Pdf.BitmapInfo.PixelFormat.Rgb24);
            page.PageInfo.Height = height;
            page.PageInfo.Width = width;
            page.PageInfo.Margin.Bottom = 0;
            page.PageInfo.Margin.Top = 0;
            page.PageInfo.Margin.Right = 0;
            page.PageInfo.Margin.Left = 0;

            page.Paragraphs.Add(asposeImage);

            // Save PDF document
            document.Save(dataDir + "HEICtoPDF_out.pdf");
        }
    }
}
```

## Aspose.PDF 24.8の新機能

PDF文書をPDF/A-4形式に変換する

バージョン24.8以降、PDF文書をPDF/A-4に変換することが可能になりました。標準の第4部は、PDF 2.0に基づいており、2020年末に公開されました。

次のコードスニペットは、入力文書が2.0よりも古いPDFバージョンである場合に、文書をPDF/A-4形式に変換する方法を示しています。

```cs
private static void ConvertPdfToPdfA4()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToPDFA.pdf"))
    {
        // If the document version is less than PDF-2.0, it must be converted to PDF-2.0
        document.Convert(Stream.Null, Aspose.Pdf.PdfFormat.v_2_0, Aspose.Pdf.ConvertErrorAction.Delete);

        // Convert to the PDF/A-4 format
        document.Convert(dataDir + "PDFA4ConversionLog.xml", Aspose.Pdf.PdfFormat.PDF_A_4, Aspose.Pdf.ConvertErrorAction.Delete);

        // Save PDF document
        document.Save(dataDir + "PDFToPDFA4_out.pdf");
    }
}
```

24.8以降、PDF文書内の透明なコンテンツをフラット化するためのメソッドが導入されました：

```cs
private static void FlattenTransparency()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PdfWithTransparentImage.pdf"))
    {
        // Flatten image transparency
        document.FlattenTransparency();
        // Save PDF document
        document.Save(dataDir + "PdfWithFlattenedImage.pdf");
    }
}
```

## Aspose.PDF 24.7の新機能

Aspose.PDF for .NETを使用してPDF文書を比較する

24.7以降、注釈マークと並列出力を使用してPDF文書の内容を比較することが可能になりました：

最初のコードスニペットは、2つのPDF文書の最初のページを比較する方法を示しています。

```cs
private static void ComparingSpecificPagesSideBySide()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentCompare();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "ComparingSpecificPages1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "ComparingSpecificPages2.pdf"))
        {
            // Compare
            Aspose.Pdf.Comparison.SideBySidePdfComparer.Compare(document1.Pages[1], document2.Pages[1],
                dataDir + "ComparingSpecificPages_out.pdf", new Aspose.Pdf.Comparison.SideBySideComparisonOptions
            {
                AdditionalChangeMarks = true,
                ComparisonMode = Aspose.Pdf.Comparison.ComparisonMode.IgnoreSpaces
            });
        }
    }
}
```

2番目のコードスニペットは、2つのPDF文書の全内容を比較する範囲を拡大します。

```cs
private static void ComparingEntireDocumentsSideBySide()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentCompare();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "ComparingEntireDocuments1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "ComparingEntireDocuments2.pdf"))
        {
            // Compare
            Aspose.Pdf.Comparison.SideBySidePdfComparer.Compare(
                document1,
                document2,
                dataDir + "ComparingEntireDocuments_out.pdf",
                new Aspose.Pdf.Comparison.SideBySideComparisonOptions
                {
                    AdditionalChangeMarks = true,
                    ComparisonMode = Aspose.Pdf.Comparison.ComparisonMode.IgnoreSpaces
                });
        }
    }
}
```

また、このリリースからAspose.PDF Security for .NETプラグインが追加されました：

暗号化機能：

```cs
var input = "sample.pdf";
var output = "encrypted.pdf";

var plugin = new Security();
var opt = new EncryptionOptions("123456789", "123", DocumentPrivilege.ForbidAll);
opt.AddInput(new FileDataSource(input));
opt.AddOutput(new FileDataSource(output));
plugin.Process(opt);
```

復号化機能：

```cs
var input = "encrypted.pdf";
var output = "decrypted.pdf";

var plugin = new Security();
var opt = new DecryptionOptions("123456789");
opt.AddInput(new FileDataSource(input));
opt.AddOutput(new FileDataSource(output));
plugin.Process(opt);
```

## Aspose.PDF 24.6の新機能

24.6リリース以降、タグ付きPDFの編集の一環として、**Aspose.Pdf.LogicalStructure.Element**にメソッドが追加されました：

- タグ（画像、テキスト、リンクなどの特定のオペレーターにタグを追加）
- InsertChild
- RemoveChild
- ClearChilds

また、このリリースでは、低レベルの関数を使用してアクセシブルなPDFを作成することが可能になりました：

次のコードスニペットは、PDF文書とそのタグ付きコンテンツを処理するためにAspose.PDFライブラリを利用します。

```cs
private static void CreateAnAccessibleDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "tourguidev2_gb_tags.pdf"))
    {
        // Access tagged content
        Aspose.Pdf.Tagged.ITaggedContent content = document.TaggedContent;
        // Create annotation span element
        Aspose.Pdf.LogicalStructure.SpanElement span = content.CreateSpanElement();
        // Append span to root element
        content.RootElement.AppendChild(span);
        // Iterate over page contents
        foreach (var op in document.Pages[1].Contents)
        {
            var bdc = op as Aspose.Pdf.Operators.BDC;
            if (bdc != null)
            {
                span.Tag(bdc);
            }
        }
        // Save PDF document
        document.Save(dataDir + "AccessibleDocument_out.pdf");
    }
}
```

24.6以降、Aspose.PDF for .NETはbase64形式のX509Certificate2でPDFに署名することを許可します：

```cs
private static void SignWithBase64Certificate(string pfxFilePath, string password)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    var base64Str = "Certificate in base64 format";
    using (var pdfSign = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        var sign = new Aspose.Pdf.Forms.ExternalSignature(base64Str, false);// without Private Key
        sign.ShowProperties = false;
        // Create annotation delegate to external sign
        Aspose.Pdf.Forms.SignHash customSignHash = delegate (byte[] signableHash, Aspose.Pdf.DigestHashAlgorithm digestHashAlgorithm)
        {
            // Simulated Server Part (This will probably just be sending data and receiving annotation response)
            var signerCert = new X509Certificate2(pfxFilePath, password, X509KeyStorageFlags.Exportable);// must have Private Key
            var rsaCSP = new RSACryptoServiceProvider();
            var xmlString = signerCert.PrivateKey.ToXmlString(true);
            rsaCSP.FromXmlString(xmlString);
            byte[] signedData = rsaCSP.SignData(signableHash, CryptoConfig.MapNameToOID("SHA1"));
            return signedData;
        };
        sign.CustomSignHash = customSignHash;
        // Bind PDF document
        pdfSign.BindPdf(dataDir + "input.pdf");
        // Sign the file
        pdfSign.Sign(1, "second approval", "second_user@example.com", "Australia", false,
            new System.Drawing.Rectangle(200, 200, 200, 100),
            sign);
        // Save PDF document
        pdfSign.Save(dataDir + "SignWithBase64Certificate_out.pdf");
    }
}
```

## Aspose.PDF 24.5の新機能

このリリースでは、PDFレイヤーを操作することが可能になりました。たとえば：

- PDFレイヤーをロックする
- PDFレイヤー要素を抽出する
- レイヤー付きPDFをフラット化する
- PDF内のすべてのレイヤーを1つにマージする

### PDFレイヤーをロックする

24.5リリース以降、PDFを開き、最初のページの特定のレイヤーをロックし、変更を加えた文書を保存することができます。2つの新しいメソッドと1つのプロパティが追加されました：

Layer.Lock(); - レイヤーをロックします。
Layer.Unlock(); - レイヤーのロックを解除します。
Layer.Locked; - レイヤーのロック状態を示すプロパティ。

```cs
private static void LockLayerInPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Layers();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get the first page and the first layer
        var page = document.Pages[1];
        var layer = page.Layers[0];

        // Lock the layer
        layer.Lock();

        // Save PDF document
        document.Save(dataDir + "LockLayerInPDF_out.pdf");
    }
}
```

### PDFレイヤー要素を抽出する

Aspose.PDF for .NETライブラリは、最初のページから各レイヤーを抽出し、各レイヤーを別々のファイルに保存することを許可します。

レイヤーから新しいPDFを作成するには、次のコードスニペットを使用できます：

```cs
private static void ExtractPdfLayer()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var inputDocument = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get layers from the first page
        var layers = inputDocument.Pages[1].Layers;

        // Save each layer to the output path
        foreach (var layer in layers)
        {
            layer.Save(dataDir + string.Format("Layer_{0}.pdf", layer.Id));
        }
    }
}
```

### レイヤー付きPDFをフラット化する

Aspose.PDF for .NETライブラリはPDFを開き、最初のページの各レイヤーを反復処理し、各レイヤーをフラット化してページに永続化します。

```cs
private static void FlattenPdfLayers()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get the first page
        var page = document.Pages[1];

        // Flatten each layer on the page
        foreach (var layer in page.Layers)
        {
            layer.Flatten(true);
        }

        // Save PDF document
        document.Save(dataDir + "FlattenedLayersPdf_out.pdf");
    }
}
```

'Layer.Flatten(bool cleanupContentStream)'メソッドは、オプショナルコンテンツグループマーカーをコンテンツストリームから削除するかどうかを指定するブールパラメータを受け入れます。cleanupContentStreamパラメータをfalseに設定すると、フラット化のプロセスが高速化されます。

### PDF内のすべてのレイヤーを1つにマージする

Aspose.PDF for .NETライブラリは、すべてのPDFレイヤーまたは最初のページの特定のレイヤーを新しいレイヤーにマージし、更新された文書を保存することを許可します。

ページ上のすべてのレイヤーをマージするために2つのメソッドが追加されました：

- void MergeLayers(string newLayerName);
- void MergeLayers(string newLayerName, string newOptionalContentGroupId); 

2番目のパラメータは、オプショナルコンテンツグループマーカーの名前を変更することを許可します。デフォルト値は"oc1" (/OC /oc1 BDC)です。

```cs
private static void MergePdfLayers()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get the first page
        var page = document.Pages[1];

        page.MergeLayers("NewLayerName");
        // Or
        // page.MergeLayers("NewLayerName", "OC1");

        // Save PDF document
        document.Save(dataDir + "MergeLayersInPdf_out.pdf");
    }
}
```

## Aspose.PDF 24.4の新機能

このリリースでは、画像にクリッピングマスクを適用することがサポートされました：

```cs
private static void AddStencilMasksToImages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddStencilMasksToImages.pdf"))
    {
        // Open the first mask image file
        using (var fs1 = new FileStream(dataDir + "mask1.jpg", FileMode.Open))
        {
            // Open the second mask image file
            using (var fs2 = new FileStream(dataDir + "mask2.png", FileMode.Open))
            {
                // Apply stencil mask to the first image on the first page
                document.Pages[1].Resources.Images[1].AddStencilMask(fs1);

                // Apply stencil mask to the second image on the first page
                document.Pages[1].Resources.Images[2].AddStencilMask(fs2);
            }
        }

        // Save PDF document
        document.Save(dataDir + "AddStencilMasksToImages_out.pdf");
    }
}
```

24.4以降、印刷ダイアログでPDFページサイズによって用紙ソースを選択できるようになりました。

Aspose.PDF 24.4以降、この設定はDocument.PickTrayByPdfSizeプロパティまたはPdfContentEditorファサードを使用してオンまたはオフに切り替えることができます：

```cs
private static void PickTrayByPdfSize()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello world!"));

        // Set the flag to choose annotation paper tray using the PDF page size
        document.PickTrayByPdfSize = true;

        // Save PDF document
        document.Save(dataDir + "PickTrayByPdfSize_out.pdf");
    }
}
```

```cs
private static void PickTrayByPdfSizeFacade()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create the PdfContentEditor facade
    using (var contentEditor = new Aspose.Pdf.Facades.PdfContentEditor())
    {
        // Bind PDF document
        contentEditor.BindPdf(dataDir + "PrintDocument.pdf");

        // Set the flag to choose annotation paper tray using the PDF page size
        contentEditor.ChangeViewerPreference(Aspose.Pdf.Facades.ViewerPreference.PickTrayByPDFSize);

        // Save PDF document
        contentEditor.Save(dataDir + "PickTrayByPdfSizeFacade_out.pdf");
    }
}
```

このリリースから、Aspose.PDF Signature for .NETプラグインが追加されました：

- 新しいフィールドとオプションを作成する例：

```cs
// create Signature
var plugin = new Signature();
// create SignOptions object to set instructions
var opt = new SignOptions(inputPfxPath, inputPfxPassword);
// add input file path
opt.AddInput(new FileDataSource(inputPath));
// set output file path
opt.AddOutput(new FileDataSource(outputPath));
// set extra options
opt.Reason = "my Reason";
opt.Contact = "my Contact";
opt.Location = "my Location";
// perform the process
plugin.Process(opt);
```

- 既存の空のフィールドの例

```cs
// create Signature
var plugin = new Signature();
// create SignOptions object to set instructions
var opt = new SignOptions(inputPfxPath, inputPfxPassword);
// add input file path with empty signature field
opt.AddInput(new FileDataSource(inputPath));
// set output file path
opt.AddOutput(new FileDataSource(outputPath));
// set name of existing signature field
opt.Name = "Signature1";
// perform the process
plugin.Process(opt);
```

## Aspose.PDF 24.3の新機能

このリリースから、PDF/A Converter for .NETプラグインが追加されました：

```cs
var options = new PdfAConvertOptions
{
    PdfAVersion = PdfAStandardVersion.PDF_A_3B
};

// Add the source file
options.AddInput(new FileDataSource("path_to_your_pdf_file.pdf")); // replace with your actual file path

// Add the path to save the converted file
options.AddOutput(new FileDataSource("path_to_the_converted_file.pdf"));

// Create the plugin instance
var plugin = new PdfAConverter();

// Run the conversion
plugin.Process(options);
```

- TextFragmentAbsorber内のフレーズのリストを検索する機能を実装：

```cs
private static void SearchMultipleRegex()
{
    // Create resular expressions
    var regexes = new Regex[]
    {
        new Regex(@"(?s)document\s+(?:(?:no\(?s?\)?\.?)|(?:number(?:\(?s\)?)?))\s+(?:(?:[\w-]*\d[\w-]*)+(?:[,;\s]|and)*)", RegexOptions.IgnoreCase),
        new Regex(@"[\s\r\n]+Tract[\s\r\n]+of:? ", RegexOptions.IgnoreCase),
        new Regex(@"vested[\s\r\n]+in", RegexOptions.IgnoreCase),
        new Regex("Vested in:", RegexOptions.IgnoreCase),
        new Regex(@"file.?[\s\r\n]+(?:nos?|numbers?|#s?|nums?).?[\s\r\n]+(\d+)-(\d+)", RegexOptions.IgnoreCase),
        new Regex(@"file.?[\s\r\n]+nos?.?:?[\s\r\n]+([\d\r\n-]+)", RegexOptions.IgnoreCase)
    };

    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchRegularExpressionAll.pdf"))
    {
        // Create TextAbsorber object to find all instances of the input search phrase
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber(regexes, new Aspose.Pdf.Text.TextSearchOptions(true));
        document.Pages.Accept(absorber);
        // Get result
        var result = absorber.RegexResults;
    }
}
```

24.3以降、PDF/Aファイルのすべてのページに空の署名フィールドを追加することが可能になりました。

```cs
private static void AddEmptySignatureFieldOnEveryPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    var fieldName = "signature_1234";

    using (var document = new Aspose.Pdf.Document(dataDir + "PDFAToPDF.pdf"))
    {
        // The new suggested code, using SignatureField object
        var signatureField = new Aspose.Pdf.Forms.SignatureField(document.Pages[1], new Aspose.Pdf.Rectangle(10, 10, 100, 100));

        // Add the default appearance for the signature field
        signatureField.DefaultAppearance = new Aspose.Pdf.Annotations.DefaultAppearance("Helv", 12, System.Drawing.Color.Black);
        var newAddedField = document.Form.Add(signatureField, fieldName, 1);

        // Find annotation associated with the field
        Aspose.Pdf.Annotations.Annotation addedAnnotation = null;
        foreach (Aspose.Pdf.Annotations.Annotation annotation in document.Pages[1].Annotations)
        {
            if (annotation.FullName == fieldName)
            {
                addedAnnotation = annotation;
                break;
            }
        }

        // Add the annotation to every page except of initial
        if (addedAnnotation != null)
        {
            for (int p = 2; p <= document.Pages.Count; p++)
            {
                document.Pages[p].Annotations.Add(addedAnnotation);
            }
        }

        // Save PDF document
        document.Save(dataDir + "outputPdfaWithSignatureFields.pdf");
    }
}
```

## Aspose.PDF 24.2の新機能

24.2以降、PDFファイルからベクターデータを取得することが可能になりました。

GraphicsAbsorberを実装して文書からベクターデータを取得します：

```cs
private static void UsingGraphicsAbsorber()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open the document
    using (var document = new Aspose.Pdf.Document(dataDir + "DocumentWithVectorGraphics.pdf"))
    {
        // Create an instance of GraphicsAbsorber
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Select the first page of the document
            var page = document.Pages[1];

            // Use the `Visit` method to extract graphics from the page
            graphicsAbsorber.Visit(page);

            // Step 5: Display information about the extracted elements
            foreach (var element in graphicsAbsorber.Elements)
            {
                Console.WriteLine($"Page Number: {element.SourcePage.Number}");
                Console.WriteLine($"Position: ({element.Position.X}, {element.Position.Y})");
                Console.WriteLine($"Number of Operators: {element.Operators.Count}");
            }
        }
    }
}
```

## Aspose.PDF 24.1の新機能

24.1リリース以降、FDF形式の注釈をPDFにインポートすることが可能になりました。

```cs
private static void ImportFDFByForm()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var form = new Aspose.Pdf.Facades.Form(dataDir + "input.pdf"))
    {
        // Open FDF file
        using (var fdfInputStream = new FileStream(dataDir + "student.fdf", FileMode.Open))
        {
            form.ImportFdf(fdfInputStream);
        }
        // Save PDF document
        form.Save(dataDir + "ImportDataFromPdf_Form_out.pdf");
    }
}
```

また、ページ辞書または文書カタログへのアクセスをサポートしています。

DictionaryEditorのコード例は次のとおりです：

- 新しい値を追加

```cs
/private static void AddNewKeysToPdfPageDicrionary()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // example of key's names
    string KEY_NAME = "name";
    string KEY_STRING = "str";
    string KEY_BOOL = "bool";
    string KEY_NUMBER = "number";

    // Open the document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();
        var dictionaryEditor = new Aspose.Pdf.DataEditor.DictionaryEditor(page);

        dictionaryEditor.Add(KEY_NAME, new Aspose.Pdf.DataEditor.CosPdfName("name data"));
        dictionaryEditor.Add(KEY_STRING, new Aspose.Pdf.DataEditor.CosPdfString("string data"));
        dictionaryEditor.Add(KEY_BOOL, new Aspose.Pdf.DataEditor.CosPdfBoolean(true));
        dictionaryEditor.Add(KEY_NUMBER, new Aspose.Pdf.DataEditor.CosPdfNumber(11.2));

        // Save PDF document
        document.Save(dataDir + "PageDictionaryEditor_out.pdf");
    }
}
```

- 辞書に値を追加して設定

```cs
private static void ModifyKeysInPdfPageDicrionary()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    string KEY_NAME = "name";

    // Open the document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();
        var dictionaryEditor = new Aspose.Pdf.DataEditor.DictionaryEditor(page);
        dictionaryEditor.Add(KEY_NAME, new Aspose.Pdf.DataEditor.CosPdfName("Old data"));
        // Modify existing value
        dictionaryEditor[KEY_NAME] = new Aspose.Pdf.DataEditor.CosPdfName("New data");

        // Save PDF document
        document.Save(dataDir + "PageDictionaryEditorEdit_out.pdf");
    }
}
```

- 辞書から値を取得

```cs
private static void GetValuesFromPdfPageDicrionary()
{
    string KEY_NAME = "name";

    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();
        var dictionaryEditor = new Aspose.Pdf.DataEditor.DictionaryEditor(page);
        dictionaryEditor[KEY_NAME] = new Aspose.Pdf.DataEditor.CosPdfName("name");
        var value = dictionaryEditor[KEY_NAME];
        // or 
        Aspose.Pdf.DataEditor.ICosPdfPrimitive primitive;
        dictionaryEditor.TryGetValue(KEY_NAME, out primitive);
    }
}
```

- 辞書から値を削除

```cs
private static void RemoveFromPdfPageDicrionary()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    string KEY_NAME = "name";
    string EXPECTED_NAME = "name data";

    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();
        var dictionaryEditor = new Aspose.Pdf.DataEditor.DictionaryEditor(page);
        dictionaryEditor.Add(KEY_NAME, new Aspose.Pdf.DataEditor.CosPdfName(EXPECTED_NAME));
        dictionaryEditor.Remove(KEY_NAME);

        // Save PDF document
        document.Save(dataDir + "PageDictionaryEditorRemove_out.pdf");
    }
}
```

## Aspose.PDF 23.12の新機能

フォームを見つけてテキストを置き換えるには、次のコードスニペットを使用します：

```cs
private static void ReplaceTextInPdfForm()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextBox.pdf"))
    {
        // Get the forms from the first page
        var forms = document.Pages[1].Resources.Forms;

        foreach (var form in forms)
        {
            // Check if the form is of type "Typewriter" and subtype "Form"
            if (form.IT == "Typewriter" && form.Subtype == "Form")
            {
                // Create a TextFragmentAbsorber to find text fragments
                var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
                absorber.Visit(form);

                // Clear the text in each fragment
                foreach (var fragment in absorber.TextFragments)
                {
                    fragment.Text = "";
                }
            }
        }

        // Save PDF document
        document.Save(dataDir + "TextBox_out.pdf");
    }
}
```            

または、フォームを完全に削除することもできます：

```cs
private static void DeleteSpecifiedForm1()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextField.pdf"))
    {
        // Get the forms from the first page
        var forms = document.Pages[1].Resources.Forms;

        // Iterate through the forms and delete the ones with type "Typewriter" and subtype "Form"
        for (int i = forms.Count; i > 0; i--)
        {
            if (forms[i].IT == "Typewriter" && forms[i].Subtype == "Form")
            {
                forms.Delete(forms[i].Name);
            }
        }

        // Save PDF document
        document.Save(dataDir + "TextBox_out.pdf");
    }
}
```            

フォームを削除する別の方法：

```cs
private static void DeleteSpecifiedForm2()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextField.pdf"))
    {
        // Get the forms from the first page
        var forms = document.Pages[1].Resources.Forms;

        // Iterate through the forms and delete the ones with type "Typewriter" and subtype "Form"
        foreach (var form in forms)
        {
            if (form.IT == "Typewriter" && form.Subtype == "Form")
            {
                var name = forms.GetFormName(form);
                forms.Delete(name);
            }
        }

        // Save PDF document
        document.Save(dataDir + "TextBox_out.pdf");
    }
}
``` 

- 次のコードスニペットを使用してすべてのフォームを削除できます：

```cs
private static void RemoveAllForms()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextField.pdf"))
    {
        // Get the forms from the first page
        var forms = document.Pages[1].Resources.Forms;

        // Clear all forms
        forms.Clear();

        // Save PDF document
        document.Save(dataDir + "TextBox_out.pdf");
    }
}
```

- PDFからMarkdownへの変換を実装：

```cs
private static void ConvertPDFtoMarkup()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "demo.pdf"))
    {
        // Create an instance of MarkdownSaveOptions to configure the Markdown export settings
        var saveOptions = new MarkdownSaveOptions()
        {
            // Set to false to prevent the use of HTML <img> tags for images in the Markdown output
            UseImageHtmlTag = false
        };
        
        // Specify the directory name where resources (like images) will be stored
        saveOptions.ResourcesDirectoryName = "images";

        // Save PDF document in Markdown format to the specified output file path using the defined save options
        document.Save(dataDir + "PDFtoMarkup_out.md", saveOptions);
    }
}
```

- OFDからPDFへの変換を実装：

```cs
private static void ConvertOFDToPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    // Convert options
    var options = new Aspose.Pdf.OfdLoadOptions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ConvertOFDToPDF.ofd", options))
    {
        // Save PDF document
        document.Save(dataDir + "ConvertOFDToPDF_out.pdf");
    }
}
```

このリリースから、Mergerプラグインが追加されました：

```cs
private static void PdfMergeUsingPlugin()
{
    string dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Create annotation new instance of Merger
    using (var merger = new Aspose.Pdf.Plugins.Merger())
    {
        // Create MergeOptions
        var opt = new Aspose.Pdf.Plugins.MergeOptions();
        opt.AddInput(new Aspose.Pdf.Plugins.FileDataSource(dataDir + "Concat1.pdf"));
        opt.AddInput(new Aspose.Pdf.Plugins.FileDataSource(dataDir + "Concat2.pdf"));
        opt.AddOutput(new Aspose.Pdf.Plugins.FileDataSource(dataDir + "ConcatenatePdfFiles_out.pdf"));

        // Process the PDF merging
        merger.Process(opt);
    }
}
```

また、このリリースからChatGPTプラグインが追加されました：

```cs
private static async void InvokeChatGptPlugin()
{
    using (var plugin = new Aspose.Pdf.Plugins.PdfChatGpt())
    {
        var options = new Aspose.Pdf.Plugins.PdfChatGptRequestOptions();
        options.AddOutput(new Aspose.Pdf.Plugins.FileDataSource("PdfChatGPT_output.pdf")); // Add the output file path.
        options.ApiKey = "Your API key."; // You need to provide the key to access the API.
        options.MaxTokens = 1000; // The maximum number of tokens to generate in the chat completion.

        // Add the request messages.
        options.Messages.Add(new Aspose.Pdf.Plugins.Message
        {
            Content = "You are annotation helpful assistant.",
            Role = Aspose.Pdf.Plugins.Role.System
        });
        options.Messages.Add(new Aspose.Pdf.Plugins.Message
        {
            Content = "What is the biggest pizza diameter ever made?",
            Role = Aspose.Pdf.Plugins.Role.User
        });

        // Process the request.
        var result = await plugin.ProcessAsync(options);

        var fileResultPath = result.ResultCollection[0].Data;

        // The ChatGPT API chat completion object.
        var chatCompletionObject = result.ResultCollection[1].Data as Aspose.Pdf.Plugins.ChatCompletion;
    }
}
```

## Aspose.PDF 23.11の新機能

このリリースから、PDFファイルから隠れたテキストを削除することが可能になりました：

```cs
private static void RemoveHiddenText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "HiddenText.pdf"))
    {
        // Use TextFragmentAbsorber with no parameters to get all text
        var textAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber();

        // This option can be used to prevent other text fragments from moving after hidden text replacement
        textAbsorber.TextReplaceOptions = new Aspose.Pdf.Text.TextReplaceOptions(Aspose.Pdf.Text.TextReplaceOptions.ReplaceAdjustment.None);

        document.Pages.Accept(textAbsorber);

        // Remove hidden text
        foreach (var fragment in textAbsorber.TextFragments)
        {
            if (fragment.TextState.Invisible)
            {
                fragment.Text = "";
            }
        }

        // Save PDF document
        document.Save(dataDir + "HiddenText_out.pdf");
    }
}
```

23.11以降、スレッドの中断をサポートしています：

```cs
private static void InterruptExample()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    using (var monitor = new Aspose.Pdf.Multithreading.InterruptMonitor())
    {
        // An class that can produce long-drawn-out work
        RowSpanWorker worker = new RowSpanWorker(dataDir + "RowSpanWorker_out.pdf", monitor);

        var thread = new System.Threading.Thread(new System.Threading.ThreadStart(worker.Work));
        thread.Start();

        // The timeout should be less than the time required for full document save (without interruption)
        System.Threading.Thread.Sleep(500);

        // Interrupt the process
        monitor.Interrupt();

        // Wait for interruption...
        thread.Join();
    }
}

private class RowSpanWorker
{
    private readonly string outputPath;
    private readonly Aspose.Pdf.Multithreading.InterruptMonitor monitor;

    public RowSpanWorker(string outputPath, Aspose.Pdf.Multithreading.InterruptMonitor monitor)
    {
        this.outputPath = outputPath;
        this.monitor = monitor;
    }

    public void Work()
    {
        // This is some large text, used Lorem Ipsum in 10000 characters to cause suspension in processing
        string text = RunExamples.GetLoremIpsumString(10000);

        // Open PDF document
        using (var document = new Aspose.Pdf.Document())
        {
            Aspose.Pdf.Multithreading.InterruptMonitor.ThreadLocalInstance = this.monitor;
            var page = document.Pages.Add();

            var table = new Aspose.Pdf.Table
            {
                DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.1F)
            };

            var row0 = table.Rows.Add();

            // Add annotation cell that spans for two rows and contains annotation long-long text
            var cell00 = row0.Cells.Add(text);
            cell00.RowSpan = 2;
            cell00.IsWordWrapped = true;
            row0.Cells.Add("Ipsum Ipsum Ipsum Ipsum Ipsum Ipsum ");
            row0.Cells.Add("Dolor Dolor Dolor Dolor Dolor Dolor ");

            var row1 = table.Rows.Add();
            row1.Cells.Add("IpsumDolor Dolor Dolor Dolor Dolor ");
            row1.Cells.Add("DolorDolor Dolor Dolor Dolor Dolor ");

            page.Paragraphs.Add(table);

            try
            {
                // Save PDF document
                document.Save(this.outputPath);
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
        }
    }
}
```

## Aspose.PDF 23.10の新機能

現在の更新では、タグ付きPDFからタグを削除する3つのバージョンが紹介されています。

- documentElement（ルートツリー要素）からいくつかのノード要素を削除：

```cs
private static void RemoveStructElement()
{
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "StructureElementsTree.pdf"))
    {
        // Access to root element(s)
        var structure = document.LogicalStructure;
        var documentElement = structure.Children[0];
        var structElement = documentElement.Children.Count > 1 ? documentElement.Children[1] as Aspose.Pdf.Structure.StructElement : null;

        if (documentElement.Children.Remove(structElement))
        {
            // Element removed. Save PDF document.
            document.Save(dataDir + "StructureElementsRemoved.pdf");
        }

        // You can also delete the structElement itself
        //if (structElement != null)
        //{
        //    structElement.Remove();
        //    document.Save(outputPdfPath);
        //}
    }
}
```

- 文書からすべてのマークされた要素のタグを削除しますが、構造要素は保持します：

```cs
private static void RemoveMarkedElementsTags()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TH.pdf"))
    {
        // Access to root element(s)
        var structure = document.LogicalStructure;
        var root = structure.Children[0];
        var queue = new Queue<Aspose.Pdf.Structure.Element>();
        queue.Enqueue(root);

        while (queue.TryDequeue(out var element))
        {
            foreach (var child in element.Children)
            {
                queue.Enqueue(child);
            }

            if (element is Aspose.Pdf.Structure.TextElement || element is Aspose.Pdf.Structure.FigureElement)
            {
                element.Remove();
            }
        }

        // Save PDF document
        document.Save(dataDir + "MarkedElementsTagsRemoved.pdf");
    }
}
```

- すべてのタグを削除：

```cs
private static void RemoveTags()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TH.pdf"))
    {
        // Access to root element(s)
        var structure = document.LogicalStructure;
        var documentElement = structure.Children[0];
        documentElement.Remove();

        // Save PDF document
        document.Save(dataDir + "TagsRemoved.pdf");
    }
}
```

23.10以降、文字の高さを測定する新機能が実装されました。文字の高さを測定するには、次のコードを使用します。

```cs
private static void DisplayCharacterHeight()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractTextAll.pdf"))
    {
        // Create TextFragmentAbsorber to get information about state of document text
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
        absorber.Visit(document.Pages[1]);

        // Get height of 'A' character being displayed with font of first text fragment
        var textState = absorber.TextFragments[1].TextState;
        var height = textState.MeasureHeight('A');
        Console.WriteLine("The height of 'A' character displayed with {0} font size of {1} is {2:N3}", textState.Font.FontName, textState.FontSize,height);
    }
}
```

測定は文書に埋め込まれたフォントに基づいていることに注意してください。寸法に関する情報が不足している場合、このメソッドは0を返します。

また、このリリースでは、署名されたHASHを使用してPDFに署名する機能が提供されます：

```cs
private static void SignPdfUsingSignedHash(string certP12, string pfxPassword)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Instantiate PdfFileSignature object
    using (var sign = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        sign.BindPdf(dataDir + "input.pdf");
        var pkcs7 = new Aspose.Pdf.Forms.PKCS7(certP12, pfxPassword);

        // Create a delegate to external sign
        pkcs7.CustomSignHash = delegate (byte[] signableHash, Aspose.Pdf.DigestHashAlgorithm digestHashAlgorithm)
        {
            X509Certificate2 signerCert = new X509Certificate2(certP12, pfxPassword, X509KeyStorageFlags.Exportable);
            RSACryptoServiceProvider rsaCSP = new RSACryptoServiceProvider();
            var xmlString = signerCert.PrivateKey.ToXmlString(true);    //not supported on core 2.0
            rsaCSP.FromXmlString(xmlString);                            //not supported on core 2.0

            byte[] signedData = rsaCSP.SignHash(signableHash, CryptoConfig.MapNameToOID("SHA1"));
            return signedData;
        };

        // Sign PDF file
        sign.Sign(1, "reason", "cont", "loc", false, new System.Drawing.Rectangle(0, 0, 500, 500), pkcs7);

        // Save PDF document
        sign.Save(dataDir + "SignWithCertificate_out.pdf");
    }

    // Verify
    using (var sign = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        sign.BindPdf(dataDir + "SignWithCertificate_out.pdf");

        if (!sign.VerifySignature("Signature1"))
        {
            throw new Exception("Not verified");
        }
    }
}
```

もう1つの新機能は、印刷ダイアログのプリセットページスケーリングです：

```cs
private static void SetPrintScaling()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        document.Pages.Add();

        // Disable print scaling
        document.PrintScaling = PrintScaling.None;

        // Save PDF document
        document.Save(dataDir + "SetPrintScaling_out.pdf");
    }
}
```

## Aspose.PDF 23.9の新機能

23.9以降、フィル可能なフィールドから子注釈を削除するサポートが追加されました。

```cs
private static void RemoveChildAnnotationFromFillableField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "FieldWithChildAnnots.pdf"))
    {
        // Get field with child annotations
        var field = (Aspose.Pdf.Forms.Field)document.Form["1 Vehicle Identification Number"];
        // Get first child annotation
        var annotation = field[1];
        // Remove the annotation
        document.Pages[annotation.PageIndex].Annotations.Remove(annotation);

        // Save PDF document
        document.Save(dataDir + "RemoveChildAnnotation_out.pdf");
    }
}
```

## Aspose.PDF 23.8の新機能

23.8以降、増分更新の検出を追加するサポートが追加されました。

PDF文書内の増分更新を検出する機能が追加されました。この機能は、文書が増分更新で保存された場合に'true'を返し、そうでない場合は'false'を返します。

```cs
private static bool HasIncrementalUpdate()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PdfWithIncrementalUpdate.pdf"))
    {
        // New method
        bool hasIncrementalUpdate = document.HasIncrementalUpdate();

        Console.WriteLine("Document {0} incremental update check returns: {1}", document.FileName, hasIncrementalUpdate);
        return hasIncrementalUpdate;
    }
}
```

また、23.8では、ネストされたチェックボックスフィールドを操作する方法がサポートされています。多くのフィル可能なPDFフォームには、ラジオグループとして機能するチェックボックスフィールドがあります：

- 複数値チェックボックスフィールドを作成：

```cs
private static void CreateMultivalueCheckboxField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();

        var checkbox = new Aspose.Pdf.Forms.CheckboxField(page, new Aspose.Pdf.Rectangle(50, 50, 70, 70));

        // Set the first checkbox group option value
        checkbox.ExportValue = "option 1";

        // Add new option right under existing ones
        checkbox.AddOption("option 2");

        // Add new option at the given rectangle
        checkbox.AddOption("option 3", new Aspose.Pdf.Rectangle(100, 100, 120, 120));

        document.Form.Add(checkbox);

        // Select the added checkbox
        checkbox.Value = "option 2";

        // Save PDF document
        document.Save(dataDir + "MultivalueCheckboxField.pdf");
    }
}
```

- 複数値チェックボックスの値を取得および設定：

```cs
private static void GetAndSetValueOfMultivalueCheckboxField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "MultivalueCheckboxField.pdf"))
    {
        var form = document.Form;
        var checkbox = form.Fields[0] as Aspose.Pdf.Forms.CheckboxField;

        // Allowed values may be retrieved from the AllowedStates collection
        // Set the checkbox value using Value property
        checkbox.Value = checkbox.AllowedStates[0];
        var checkboxValue = checkbox.Value; // the previously set value, e.g. "option 1"

        // The value should be any element of AllowedStates
        checkbox.Value = "option 2";
        checkboxValue = checkbox.Value; // option 2

        // Uncheck boxes by either setting Value to "Off" or setting Checked to false
        checkbox.Value = "Off";
        // or, alternately:
        // checkbox.Checked = false;
        checkboxValue = checkbox.Value; // Off
    }
}
```

## Aspose.PDF 23.7の新機能

Aspose.PDF 23.7以降、形状抽出を追加するサポートが追加されました：

```cs
private static void CopyShape()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Graphs();

    // Open PDF document
    using (var sourceDocument = new Aspose.Pdf.Document(dataDir + "test.pdf"))
    {
        // Create PDF document
        using (var destDocument = new Aspose.Pdf.Document())
        {
            // Absorb vector graphics from the source document
            var graphicAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber();
            graphicAbsorber.Visit(sourceDocument.Pages[1]);

            // Copy the graphics into the destination document specified page and area
            var area = new Aspose.Pdf.Rectangle(90, 250, 300, 400);
            destDocument.Pages[1].AddGraphics(graphicAbsorber.Elements, area);

            // Save PDF document
            destDocument.Save(dataDir + "CopyShape_out.pdf");
        }
    }
}
```

また、テキストを追加する際のオーバーフローを検出する機能がサポートされています：

```cs
private static void FitTextIntoRectangle()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document()) 
    {
        // Generate text to add: "Lorem Ipsum" text of 1000 characters
        var paragraphContent = RunExamples.GetLoremIpsumString(1000);
        // Create a text fragment with the desired text
        var fragment = new Aspose.Pdf.Text.TextFragment(paragraphContent);
        // Declare the rectangle to fit text into
        var rectangle = new Aspose.Pdf.Rectangle(100, 600, 500, 700, false);
        
        // Check whether the text fits into the rectangle
        var isFitRectangle = fragment.TextState.IsFitRectangle(paragraphContent, rectangle);

        // Iteratively decrease font size until text fits the rectangle
        while (!isFitRectangle)
        {
            fragment.TextState.FontSize -= 0.5f;
            isFitRectangle = fragment.TextState.IsFitRectangle(paragraphContent, rectangle);
        }

        // Create a paragraph from the text fragment in the specified rectangle. Now you may be sure it fits.
        var paragraph = new Aspose.Pdf.Text.TextParagraph();
        paragraph.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
        paragraph.FormattingOptions.WrapMode = Aspose.Pdf.Text.TextFormattingOptions.WordWrapMode.ByWords;
        paragraph.Rectangle = rectangle;
        paragraph.AppendLine(fragment);

        // Create a text builder to place the paragraph on the document page
        var builder = new Aspose.Pdf.Text.TextBuilder(document.Pages.Add());
        builder.AppendParagraph(paragraph);

        // Save PDF document
        document.Save(dataDir + "FitTextIntoRectangle_out.pdf");
    }
}
```

## Aspose.PDF 23.6の新機能

Aspose.PDF 23.6以降、次のプラグインを追加するサポートが追加されました：

- Aspose PdfConverter Html to PDF 
- Aspose PdfOrganizer Resize API
- Aspose PdfOrganizer Compress API

Aspose.PdfFormを更新 
- 文書内のフィールドから「値」をCSVファイルにエクスポートする機能を追加
- 個別のフィールドのプロパティを設定する機能を追加

また、HTML、Epubページのタイトルを設定する機能が追加されました：

```cs
private static void SetHtmlTitle()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        var options = new Aspose.Pdf.HtmlSaveOptions
        {
            ExplicitListOfSavedPages = new[] { 1 },
            SplitIntoPages = false,
            FixedLayout = true,
            CompressSvgGraphicsIfAny = false,
            SaveTransparentTexts = true,
            SaveShadowedTextsAsTransparentTexts = true,
            FontSavingMode = Aspose.Pdf.HtmlSaveOptions.FontSavingModes.AlwaysSaveAsWOFF,
            RasterImagesSavingMode = Aspose.Pdf.HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground,
            PartsEmbeddingMode = Aspose.Pdf.HtmlSaveOptions.PartsEmbeddingModes.EmbedAllIntoHtml,
            // New property
            Title = "Title for page"
        };

        // Save HTML document
        document.Save(dataDir + "SetHtmlTitle_out.html", options);
    }
}
```

## Aspose.PDF 23.5の新機能

23.5以降、RedactionAnnotation FontSizeオプションを追加するサポートが追加されました。このタスクを解決するために次のコードスニペットを使用します：

```cs
private static void AddRedactionAnnotationFontSize() 
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf")) 
    {
        // Create RedactionAnnotation instance for specific page region
        var annot = new Aspose.Pdf.Annotations.RedactionAnnotation(document.Pages[1],
            new Aspose.Pdf.Rectangle(367, 756.919982910156, 420, 823.919982910156));
        annot.FillColor = Aspose.Pdf.Color.Black;

        annot.BorderColor = Aspose.Pdf.Color.Yellow;
        annot.Color = Aspose.Pdf.Color.Blue;
        // Text to be printed on redact annotation
        annot.OverlayText = "(Unknown)";
        annot.TextAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        // Repat Overlay text over redact Annotation
        annot.Repeat = false;

        // New property
        annot.FontSize = 20;

        // Add annotation to annotations collection of first page
        document.Pages[1].Annotations.Add(annot);
        // Flattens annotation and redacts page contents (i.e. removes text and image under redacted annotation)
        annot.Redact();
        // Save PDF document
        document.Save(dataDir + "AddRedactionAnnotationFontSize_out.pdf");
    }
}
```

## Aspose.PDF 23.4の新機能

Aspose.PDFは.NET 7 SDKのリリースを発表しました。

## Aspose.PDF 23.3.1の新機能

Aspose.PDF 23.3以降、次のプラグインを追加するサポートが追加されました：

- Aspose.PdfForm
- Aspose.PdfConverter PDF to HTML
- Aspose.PdfConverter PDF to XLSX
- Aspose.PdfOrganizer Rotate
- Aspose.PdfExtrator for Images

## Aspose.PDF 23.3の新機能

バージョン23.3では、ページに挿入する際に画像の比率と解像度を保持するサポートが追加されました。この問題を解決するために2つのメソッドを使用できます：

```cs
private static void InsertImageWithNativeResolutionAsTable()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();

        var table = new Aspose.Pdf.Table
        {
            ColumnWidths = "600"
        };

        for (var j = 0; j < 2; j++)
        {
            var row = table.Rows.Add();
            var cell = row.Cells.Add();
            cell.Paragraphs.Add(new Aspose.Pdf.Image()
            {
                IsApplyResolution = true,
                File = dataDir + "Image1.jpg"
            });
        }

        page.Paragraphs.Add(table);

        // Save PDF document
        document.Save(dataDir + "ImageWithNativeResolutionAsTable_out.pdf");
    }
}
```

2番目のアプローチ：

```cs
private static void InsertImageWithNativeResolutionAsParagraph()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();

        for (var j = 0; j < 2; j++)
        {
            page.Paragraphs.Add(new Aspose.Pdf.Image()
            {
                IsApplyResolution = true,
                File = dataDir + "Image1.jpg"
            });
        }

        // Save PDF document
        document.Save(dataDir + "ImageWithNativeResolutionAsParagraph_out.pdf");
    }
}
```

画像はスケーリングされたサイズとネイティブ解像度で配置されます。FixedWidthまたはFixedHeightプロパティをIsApplyResolutionと組み合わせて設定できます。

## Aspose.PDF 23.1.1の新機能

Aspose.PDF 23.1.1以降、次のプラグインを追加するサポートが追加されました：

- Aspose.PdfOrganizerプラグイン
- Aspose.PdfExtractorプラグイン

## Aspose.PDF 23.1の新機能

23.1バージョン以降、PrinterMark注釈を作成するサポートが追加されました。

プリンターのマークは、複数のプレートジョブのコンポーネントを特定し、生産中の一貫した出力を維持するために、ページに追加されるグラフィックシンボルまたはテキストです。印刷業界で一般的に使用される例には、次のようなものがあります：

- プレートを整列させるための登録ターゲット
- 色とインク密度を測定するためのグレーランプとカラーバー
- 出力媒体がトリミングされる場所を示すカットマーク

色とインク密度を測定するためのカラーバーのオプションの例を示します。基本的な抽象クラスPrinterMarkAnnotationから、これらのストライプをすでに実装している子クラスColorBarAnnotationがあります。例を確認しましょう：

```cs
private static void AddPrinterMarkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();
        page.TrimBox = new Aspose.Pdf.Rectangle(20, 20, 580, 820);

        var rectBlack = new Aspose.Pdf.Rectangle(100, 300, 300, 320);
        var rectCyan = new Aspose.Pdf.Rectangle(200, 600, 260, 690);
        var rectMagenta = new Aspose.Pdf.Rectangle(10, 650, 140, 670);

        var colorBarBlack = new Aspose.Pdf.Annotations.ColorBarAnnotation(page, rectBlack);
        var colorBarCyan = new Aspose.Pdf.Annotations.ColorBarAnnotation(page, rectCyan,
            Aspose.Pdf.Annotations.ColorsOfCMYK.Cyan);
        var colorBarMagenta = new Aspose.Pdf.Annotations.ColorBarAnnotation(page, rectMagenta);
        colorBarMagenta.ColorOfCMYK = Aspose.Pdf.Annotations.ColorsOfCMYK.Magenta;
        var colorBarYellow = new Aspose.Pdf.Annotations.ColorBarAnnotation(page,
            new Aspose.Pdf.Rectangle(400, 250, 450, 700), Aspose.Pdf.Annotations.ColorsOfCMYK.Yellow);

        page.Annotations.Add(colorBarBlack);
        page.Annotations.Add(colorBarCyan);
        page.Annotations.Add(colorBarMagenta);
        page.Annotations.Add(colorBarYellow);

        // Save PDF document
        document.Save(dataDir + "PrinterMarkAnnotation_out.pdf");
    }
}
```
また、ベクター画像の抽出もサポートしています。次のコードを使用してベクターグラフィックスを検出および抽出してみてください：

```cs
private static void SavePdfVectorGraphicToSvg()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Graphs();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "test.pdf"))
    {
        // Attempt to save the vector graphics into a specified SVG file
        document.Pages[1].TrySaveVectorGraphics(dataDir + "PdfVectorGraphicToSvg.svg");
    }
}
```

## Aspose.PDF 22.12の新機能

このリリースから、PDFをDICOM画像に変換するサポートが追加されました。

```cs
private static void PdfToDicom()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PagesToImages.pdf"))
    {
        var dicom = new Aspose.Pdf.Devices.DicomDevice();
        FileStream outStream = new FileStream(dataDir + "PdfToDicom_out.dcm", FileMode.Create, FileAccess.ReadWrite);
        dicom.Process(document.Pages[1], outStream);
    }
}
```    

## Aspose.PDF 22.09の新機能

22.09以降、署名内の主題の見出しの順序（E=、CN=、O=、OU=）を変更するプロパティを追加するサポートが追加されました。

```cs
private static void SignPdfWithModifiedOrderOfSubjectRubrics(string pfxFilePath, string password)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Instantiate PdfFileSignature object
    using (var fileSign = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        fileSign.BindPdf(dataDir + "DigitallySign.pdf");

        var rect = new System.Drawing.Rectangle(100, 100, 400, 100);
        var signature = new Aspose.Pdf.Forms.PKCS7Detached(pfxFilePath, password);

        // Set signature custom appearance
        signature.CustomAppearance = new Aspose.Pdf.Forms.SignatureCustomAppearance()
        {
            UseDigitalSubjectFormat = true,
            DigitalSubjectFormat = new Aspose.Pdf.Forms.SubjectNameElements[] { Aspose.Pdf.Forms.SubjectNameElements.CN, Aspose.Pdf.Forms.SubjectNameElements.O }
            //or
            //DigitalSubjectFormat = new Aspose.Pdf.Forms.SubjectNameElements[] { Aspose.Pdf.Forms.SubjectNameElements.OU, Aspose.Pdf.Forms.SubjectNameElements.S, Aspose.Pdf.Forms.SubjectNameElements.C }
        };

        // Sign PDF file
        fileSign.Sign(1, true, rect, signature);
        // Save PDF document
        fileSign.Save(dataDir + "SignPdfWithModifiedOrderOfSubjectRubrics_out.pdf");
    }
}
```

## Aspose.PDF 22.6の新機能

22.5以降、PDFから下付き文字および上付き文字のテキストを抽出するサポートが追加されました。

PDF文書にH2Oのような下付き文字および上付き文字のテキストが含まれている場合、PDFからテキストを抽出する際には、そのフォーマット情報も抽出する必要があります（抽出されたプレーンテキストにおいて）。
PDFにイタリック体のテキストが含まれている場合、それも抽出されたコンテンツに含める必要があります。

```cs
private static void ExtractTextSuperscript()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextWithSubscriptsSuperscripts.pdf"))
    {
        // Use TextFragmentAbsorber with no parameters to get all text
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
        absorber.Visit(document.Pages[1]);

        // Iterate through text fragments to find superscript text
        foreach (var textFragment in absorber.TextFragments) 
        {
            if (textFragment.TextState.Superscript)
            {
                Console.WriteLine(String.Format("Text {0} at {1} is superscript!", textFragment.Text, textFragment.Position));
            }
        }
    }
}
```

## Aspose.PDF 22.4の新機能

このリリースには、Aspose.PDF for .NETに関する情報が含まれています：

- PDFからODS：下付き文字および上付き文字のテキストを認識します；

**例**

```cs
private static void ConvertPdfToOds()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate ExcelSaveOptions object
        var saveOptions = new Aspose.Pdf.ExcelSaveOptions
        {
            // Specify the desired table file format
            Format = Aspose.Pdf.ExcelSaveOptions.ExcelFormat.ODS
        };

        // Save the file in ODS format
        document.Save(dataDir + "PDFToODS_out.ods", saveOptions);
    }
}
```

- PDFからXMLSpreadSheet2003：下付き文字および上付き文字のテキストを認識します；

- PDFからExcel：下付き文字および上付き文字のテキストを認識します；

- 文書を保存する際にUR署名を削除します；

- 文書を保存する際にMarkInfo内のSuspectsフラグを削除します；

- 文書を保存する際にInfoを削除します。

## Aspose.PDF 22.3の新機能

このリリースには、以下の更新が含まれています：

- AFRelationshipのサポート；

- PDFヘッダーの検証；

- 文書を保存する際にadbe.x509.rsa_sha1サブフィルターを削除します；

- フィールドを数値および日付形式としてフォーマットします；

- FDF 2.0でRC4暗号化の使用を禁止します。

## Aspose.PDF 22.2の新機能

22.2バージョン以降、LTVを使用してPdfFileSignatureで文書に署名することが可能になり、ハッシュをSHA1からSHA256に変更できるようになりました。

```csharp
private static void SignPdfWithSha256(string pfxFilePath, string password)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Instantiate PdfFileSignature object
    using (var fileSign = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        fileSign.BindPdf(dataDir + "DigitallySign.pdf");

        var rect = new System.Drawing.Rectangle(300, 100, 1, 1);
        var signature = new Aspose.Pdf.Forms.PKCS7(pfxFilePath, password)
        {
            UseLtv = true,
            TimestampSettings = new Aspose.Pdf.TimestampSettings("http://freetsa.org/tsr", string.Empty, Aspose.Pdf.DigestHashAlgorithm.Sha256)
        };

        // Sign PDF file
        fileSign.Sign(1, false, rect, signature);
        // Save PDF document
        fileSign.Save(dataDir + "SignPdfWithSha256_out.pdf");
    }
}
```

## Aspose.PDF 22.1の新機能

現在、Aspose.PDF for .NETは、最も人気のある文書形式の1つであるポータブル文書形式（PDF）バージョン2.0から文書を読み込むことをサポートしています。

## Aspose.PDF 21.11の新機能

### パスワードに非ラテン文字を許可

```csharp
private static void EncriptPdfNonlatinPassCharacters()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    using (var fileSecurity = new Aspose.Pdf.Facades.PdfFileSecurity())
    {
        // Bind PDF document
        fileSecurity.BindPdf(dataDir + "input.pdf");
        // Encrypt file using 256-bit encryption
        bool isSuccessful = fileSecurity.EncryptFile("æøå", "æøå", Aspose.Pdf.Facades.DocumentPrivilege.Print,
            Aspose.Pdf.Facades.KeySize.x256, Aspose.Pdf.Facades.Algorithm.AES);
        Console.WriteLine(isSuccessful);
        // Save PDF document
        fileSecurity.Save(dataDir + "PdfNonlatinPassEncrypted_out.pdf");
    }
}
```

## Aspose.PDF 21.10の新機能

### 隠れたテキストを検出するには？

TextState.Invisibleを使用して、レンダリングモード設定からのテキストの不可視性に関する情報を取得してください。

テストには次のコードを使用しました：

```csharp
private static void DisplayTextInvisibility()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PdfWithHiddenText.pdf"))
    {
        Console.WriteLine(document.FileName);

        // Use TextFragmentAbsorber with no parameters to get all text
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
        absorber.Visit(document.Pages[1]);
        var textFragmentCollection = absorber.TextFragments;

        // Iterate through text fragments to find hidden text
        for (int i = 1; i <= textFragmentCollection.Count; i++)
        {
            var fragment = textFragmentCollection[i];
            Console.WriteLine("Fragment {0} at {1}", i, fragment.Rectangle.ToString());
            Console.WriteLine("Text: {0}", fragment.Text);
            Console.WriteLine("RenderingMode: {0}", fragment.TextState.RenderingMode.ToString());
            Console.WriteLine("Invisibility: {0}", fragment.TextState.Invisible);
            Console.WriteLine("---");
        }
    }
}
```

### PDF文書内のレイヤーの数に関する情報を取得するには？

```csharp
private static void GetPdfLayers()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Layers();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PdfWithLayers.pdf"))
    {
        // Get layers from the first page
        var layers = document.Pages[1].Layers;
        // Save each layer to the output path
        foreach (var layer in layers)
        {
            Console.WriteLine("Document {0} contains a layer named: {1} ", document.FileName, layer.Name);
        }
    }
}
```

## Aspose.PDF 21.9の新機能

Aspose.PDF for .NETを使用して署名領域のラベルのフォント色と署名の外観の背景色をカスタマイズします。

```csharp
private static void SignPdfWithCustomColorsInAppearance(string pfxFilePath, string password)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Instantiate PdfFileSignature object
    using (var pdfFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdfFileSignature.BindPdf(dataDir + "DigitallySign.pdf");
        var rect = new System.Drawing.Rectangle(310, 45, 200, 50);
        // Create PKCS#7 object for sign
        var pkcs = new Aspose.Pdf.Forms.PKCS7(pfxFilePath, password);

        // Set signature custom appearance
        pkcs.CustomAppearance = new Aspose.Pdf.Forms.SignatureCustomAppearance()
        {
            // Set colors
            ForegroundColor = Aspose.Pdf.Color.DarkGreen,
            BackgroundColor = Aspose.Pdf.Color.LightSeaGreen,
        };
        // Sign PDF file
        pdfFileSignature.Sign(1, true, rect, pkcs);
        // Save PDF document
        pdfFileSignature.Save(dataDir + "SignPdfWithCustomColorsInAppearance_out.pdf");
    }
}
```

## Aspose.PDF 21.8の新機能

### デジタル署名のテキスト色を変更するには？

21.8バージョンでは、ForegroundColorプロパティを使用してデジタル署名のテキスト色を変更できます。

```csharp
private static void SignPdfWithForegroundColorInAppearance(string pfxFilePath, string password)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Instantiate PdfFileSignature object
    using (var pdfSign = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdfSign.BindPdf(dataDir + "DigitallySign.pdf");
        var rect = new System.Drawing.Rectangle(310, 45, 200, 50);
        // Create PKCS#7 object for sign
        var pkcs = new Aspose.Pdf.Forms.PKCS7(pfxFilePath, password);

        // Set signature custom appearance
        pkcs.CustomAppearance = new Aspose.Pdf.Forms.SignatureCustomAppearance()
        {
            // Set text color
            ForegroundColor = Aspose.Pdf.Color.Green
        };
        // Sign PDF file
        pdfSign.Sign(1, true, rect, pkcs);
        // Save PDF document
        pdfSign.Save(dataDir + "SignPdfWithForegroundInAppearance_out.pdf");
    }
}
```

## Aspose.PDF 21.7の新機能

### パラメータ付きXMLおよびXLSに基づくPDF作成

XSLパラメータを追加するには、独自の[XsltArgumentList](https://docs.microsoft.com/en-us/dotnet/api/system.xml.xsl.xsltargumentlist?view=net-5.0)を作成し、[XslFoLoadOptions](https://reference.aspose.com/pdf/ja/net/aspose.pdf/xslfoloadoptions)のプロパティとして設定する必要があります。次のスニペットは、上記のサンプルファイルとともにこのクラスを使用する方法を示しています。

```csharp
private static void ConvertXslfoToPdfWithArgumentList()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Create convert options
    var options = new Aspose.Pdf.XslFoLoadOptions(dataDir + "XSLFOToPdfInput.xslt");

    // Example of using XsltArgumentList
    options.XsltArgumentList = new XsltArgumentList();
    options.XsltArgumentList.AddParam("isBoldName", "", "yes");

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "XSLFOToPdfInput.xml", options))
    {
        // Save PDF document
        document.Save(dataDir + "XslfoToPdfWithArgumentList_out.pdf");
    }
}
```

## Aspose.PDF 21.6の新機能

Aspose.PDF for .NETを使用して、ImagePlacementAbsorberを使用して文書内の画像を非表示にすることができます：

```csharp
private static void HideImageInPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ImagePlacement.pdf"))
    {
        // Create ImagePlacementAbsorber instance
        var absorber = new Aspose.Pdf.ImagePlacementAbsorber();
        // Load the images of the first page
        document.Pages[1].Accept(absorber);

        // Iterate through each image placement on the first page
        foreach (var imagePlacement in absorber.ImagePlacements)
        {
            // Hide image
            imagePlacement.Hide();
        }

        // Save PDF document
        document.Save(dataDir + "HideImageInPdf_out.pdf");
    }
}
```

## Aspose.PDF 21.5の新機能

### PDFからフォントのフルネームを抽出するには？

FontクラスのBaseFontプロパティを使用して、プレフィックス付きのフルフォントを取得できます。

```csharp
private static void DisplayFontFullNames()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "BreakfastMenu.pdf"))
    {
        // Get document fonts
        var fonts = document.FontUtilities.GetAllFonts();

        // Iterate through the fonts
        foreach (var font in fonts)
        {
            // Show font names
            Console.WriteLine($"font name : {font.FontName} BaseFont name : {font.BaseFont}");
        }
    }
}
```

## Aspose.PDF 21.4の新機能

### 画像をマージするAPIを追加

Aspose.PDF 21.4では、画像を結合することができます。次のコードスニペットに従ってください：

```csharp
private static void MergeAsJpeg()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    List<Stream> inputImagesStreams = new List<Stream>();
    using (FileStream firstImageStream = new FileStream(dataDir + "aspose.jpg", FileMode.Open))
    {
        inputImagesStreams.Add(firstImageStream);
        using (FileStream secondImageStream = new FileStream(dataDir + "aspose-logo.jpg", FileMode.Open))
        {
            inputImagesStreams.Add(secondImageStream);

            // Invoke PdfConverter.MergeImages to perform merge
            using (Stream inputStream = Aspose.Pdf.Facades.PdfConverter.MergeImages(inputImagesStreams,
                  Aspose.Pdf.Drawing.ImageFormat.Jpeg, Aspose.Pdf.Facades.ImageMergeMode.Vertical, 1, 1))
            {
                using (FileStream outputStream = new FileStream(dataDir + "Merge_out.jpg", FileMode.Create))
                {
                    byte[] buffer = new byte[32768];
                    int read;
                    while ((read = inputStream.Read(buffer, 0, buffer.Length)) > 0)
                    {
                        outputStream.Write(buffer, 0, read);
                    }
                }
            }
        }
    }
}
```

また、画像をTiff形式でマージすることもできます：

```csharp
private static void MergeAsTiff()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    List<Stream> inputImagesStreams = new List<Stream>();
    using (FileStream firstImageStream = new FileStream(dataDir + "aspose.jpg", FileMode.Open))
    {
        inputImagesStreams.Add(firstImageStream);
        using (FileStream secondImageStream = new FileStream(dataDir + "aspose-logo.jpg", FileMode.Open))
        {
            inputImagesStreams.Add(secondImageStream);

            // Invoke PdfConverter.MergeImagesAsTiff to perform merge
            using (Stream inputStream = Aspose.Pdf.Facades.PdfConverter.MergeImagesAsTiff(inputImagesStreams))
            {
                using (FileStream outputStream = new FileStream(dataDir + "Merge_out.tiff", FileMode.Create))
                {
                    byte[] buffer = new byte[32768];
                    int read;
                    while ((read = inputStream.Read(buffer, 0, buffer.Length)) > 0)
                    {
                        outputStream.Write(buffer, 0, read);
                    }
                }
            }
        }
    }
}
```

## Aspose.PDF 21.3の新機能

### Azure Information Protectionを検出するためのプロパティの公開

次のコードスニペットを使用すると、Azure Information Protectionで保護されたPDFファイルの暗号化されたペイロードにアクセスできるはずです：

```csharp
private static void AzureInformationProtection()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetAlltheAttachments.pdf"))
    {
        if (document.EmbeddedFiles[1].AFRelationship == Aspose.Pdf.AFRelationship.EncryptedPayload)
        {
            if (document.EmbeddedFiles[1].EncryptedPayload != null)
            {
                // document.EmbeddedFiles[1].EncryptedPayload.Type == "EncryptedPayload"
                // document.EmbeddedFiles[1].EncryptedPayload.Subtype == "MicrosoftIRMServices"
                // document.EmbeddedFiles[1].EncryptedPayload.Version == "2"
            }
        }
    }
}
```

## Aspose.PDF 21.1の新機能

### TextFragmentの背景色を取得するサポートを追加

このバージョンのAspose.PDFでは、背景色を取得する機能が利用可能になりました。TextFragmentAbsorberオブジェクトのオプションでsearchOptions.SearchForTextRelatedGraphics = true;を指定する必要があります。

次のコードを考慮してください：

```csharp
private static void DisplayPdfTextBackgroundColor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PdfWithTextBackgroundColor.pdf"))
    {
        // Use TextFragmentAbsorber with no parameters to get all text
        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber();

        var searchOptions = new Aspose.Pdf.Text.TextSearchOptions(false);
        // Setting this option into the 'true' is necessary 
        searchOptions.SearchForTextRelatedGraphics = true;
        textFragmentAbsorber.TextSearchOptions = searchOptions;

        // Accept the absorber for all the pages
        document.Pages.Accept(textFragmentAbsorber);
        
        // Loop through the fragments
        foreach (var textFragment in textFragmentAbsorber.TextFragments)
        {
            Console.WriteLine("Text: '{0}'", textFragment.Text);
            Console.WriteLine("BackgroundColor: '{0}'", textFragment.TextState.BackgroundColor);
            Console.WriteLine("ForegroundColor: '{0}'", textFragment.TextState.ForegroundColor);
            Console.WriteLine("Segment BackgroundColor: '{0}'", textFragment.Segments[1].TextState.BackgroundColor);
        }
    }
}
```

### HTMLに変換後、フォントが出力に完全に埋め込まれる

また、Aspose.PDF 21.1では、PDFをHTMLに変換した後、出力HTML文書に埋め込まれたフォントが利用可能になりました。これは、新しいブール保存オプションHtmlSaveParameter.SaveFullFontによって可能です。

次のコードスニペットを示します：

```csharp
private static void PdfToHtmlWithFullFont()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Instantiate HTML SaveOptions object
        var options = new Aspose.Pdf.HtmlSaveOptions
        {
            RasterImagesSavingMode = Aspose.Pdf.HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground,
            PartsEmbeddingMode = Aspose.Pdf.HtmlSaveOptions.PartsEmbeddingModes.EmbedAllIntoHtml,
            LettersPositioningMethod = Aspose.Pdf.HtmlSaveOptions.LettersPositioningMethods.UseEmUnitsAndCompensationOfRoundingErrorsInCss,
            FontSavingMode = Aspose.Pdf.HtmlSaveOptions.FontSavingModes.AlwaysSaveAsTTF,
            SaveTransparentTexts = true,
            // New option
            SaveFullFont = true
        };
        // Save HTML document
        document.Save(dataDir + "PdfToHtmlWithFullFont_out.html", options);
    }
}
```