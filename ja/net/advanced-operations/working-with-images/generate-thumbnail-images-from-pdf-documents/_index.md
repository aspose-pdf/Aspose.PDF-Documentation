---
title: PDFからサムネイル画像を生成する
linktitle: サムネイル画像を生成する
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 110
url: /ja/net/generate-thumbnail-images-from-pdf-documents/
description: このセクションでは、PDFドキュメントからサムネイル画像を生成する方法について説明します
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Generate Thumbnail Images from PDF",
    "alternativeHeadline": "Generate Thumbnails from PDF Documents Effortlessly",
    "abstract": "この新機能により、ユーザーはPDFドキュメントから直接効率的にサムネイル画像を生成できます。この機能は、PDFページを簡単に共有可能な画像形式に変換することでドキュメント管理を強化し、開発者とユーザーのワークフローを効率化します。さまざまな画像形式をサポートしており、Adobe Acrobatのような外部ソフトウェアを必要とせずにPDFコンテンツを視覚化するプロセスを簡素化します。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Generate Thumbnail Images, PDF documents, Aspose.PDF for .NET, Acrobat SDK, image formats, PDF Manipulation Library, JavaScript, interapplication communication, thumbnail images, JPEG conversion",
    "wordcount": "767",
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
    "url": "/net/generate-thumbnail-images-from-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/generate-thumbnail-images-from-pdf-documents/"
    },
    "dateModified": "2024-11-26",
    "description": "このセクションでは、PDFドキュメントからサムネイル画像を生成する方法について説明します"
}
</script>

{{% alert color="primary" %}}

Adobe Acrobat SDKは、Acrobat技術と対話するソフトウェアを開発するためのツールセットです。SDKには、ヘッダーファイル、タイプライブラリ、簡単なユーティリティ、サンプルコード、およびドキュメントが含まれています。

Acrobat SDKを使用すると、次のようにAcrobatやAdobe Readerと統合するソフトウェアを開発できます：

- **JavaScript** — 個々のPDFドキュメント内または外部でスクリプトを書いて、AcrobatやAdobe Readerの機能を拡張します。
- **プラグイン** — AcrobatやAdobe Readerの機能を動的にリンクして拡張するプラグインを作成します。
- **アプリケーション間通信** — アプリケーション間通信（IAC）を使用してAcrobatの機能を制御する別のアプリケーションプロセスを書きます。DDEとOLEはMicrosoft® Windows®でサポートされており、Mac OS®ではAppleイベント/AppleScriptがサポートされています。IACはUNIX®では利用できません。

Aspose.PDF for .NETは、Adobe Acrobat Automationへの依存から解放される多くの同様の機能を提供します。この記事では、最初にAcrobat SDKを使用し、その後Aspose.PDFを使用してPDFドキュメントからサムネイル画像を生成する方法を示します。

{{% /alert %}}

## Acrobatアプリケーション間通信APIを使用したアプリケーションの開発

Acrobat APIは、Acrobatアプリケーション間通信（IAC）オブジェクトを使用する2つの異なるレイヤーを持っていると考えてください：

- Acrobatアプリケーション（AV）レイヤー。AVレイヤーでは、ドキュメントの表示方法を制御できます。たとえば、ドキュメントオブジェクトの表示はAcrobatに関連付けられたレイヤーに存在します。
- ポータブルドキュメント（PD）レイヤー。PDレイヤーは、ページなどのドキュメント内の情報にアクセスするためのものです。PDレイヤーからは、ページの削除、移動、置換、注釈属性の変更など、PDFドキュメントの基本的な操作を行うことができます。また、PDFページを印刷したり、テキストを選択したり、操作されたテキストにアクセスしたり、サムネイルを作成または削除したりすることもできます。

私たちの目的はPDFページをサムネイル画像に変換することなので、IACにより重点を置いています。IAC APIには、PDDoc、PDPage、PDAnnotなどのオブジェクトが含まれており、ユーザーがポータブルドキュメント（PD）レイヤーを扱うことを可能にします。以下のコードサンプルは、フォルダーをスキャンし、PDFページをサムネイル画像に変換します。Acrobat SDKを使用することで、PDFメタデータを読み取り、ドキュメント内のページ数を取得することもできます。

### Acrobatアプローチ

各ドキュメントのサムネイル画像を生成するために、Adobe Acrobat 7.0 SDKとMicrosoft .NET 2.0 Frameworkを使用しました。

[Acrobat SDK](https://opensource.adobe.com/dc-acrobat-sdk-docs/acrobatsdk/)は、Adobe Acrobatのフルバージョンと組み合わせることで、PDF情報を操作およびアクセスするために使用できるCOMオブジェクトのライブラリを公開します（残念ながら無料のAdobe ReaderはCOMインターフェースを公開していません）。これらのCOMオブジェクトをCOM Interop経由で使用して、PDFドキュメントを読み込み、最初のページを取得し、そのページをクリップボードにレンダリングします。その後、.NET Frameworkを使用して、これをビットマップにコピーし、画像をスケーリングして結合し、結果をGIFまたはPNGファイルとして保存します。

Adobe Acrobatがインストールされると、regedit.exeを使用してHKEY_CLASSES_ROOTの下にあるAcroExch.PDDocというエントリを探します。

**AcroExch.PDDocエントリを示すレジストリ**

![todo:image_alt_text](generate-thumbnail-images-from-pdf-documents_1.png)

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GenerateThumbnailImagesFromPDF()
{
    // Acrobat objects
    Acrobat.CAcroPDDoc pdfDoc;
    Acrobat.CAcroPDPage pdfPage;
    Acrobat.CAcroRect pdfRect;
    Acrobat.CAcroPoint pdfPoint;

    AppSettingsReader appSettings = new AppSettingsReader();
    string pdfInputPath = appSettings.GetValue("pdfInputPath", typeof(string)).ToString();
    string pngOutputPath = appSettings.GetValue("pngOutputPath", typeof(string)).ToString();
    string templatePortraitFile = Application.StartupPath + @"\pdftemplate_portrait.gif";
    string templateLandscapeFile = Application.StartupPath + @"\pdftemplate_landscape.gif";

    // Get list of files to process from the input path
    string[] files = Directory.GetFiles(pdfInputPath, "*.pdf");

    for (int n = 0; n < files.Length; n++)
    {
        string inputFile = files[n];
        string outputFile = Path.Combine(pngOutputPath, Path.GetFileNameWithoutExtension(inputFile) + ".png");

        // Create PDF document
        pdfDoc = (Acrobat.CAcroPDDoc)Microsoft.VisualBasic.Interaction.CreateObject("AcroExch.PDDoc", "");

        if (pdfDoc.Open(inputFile) == 0)
        {
            throw new FileNotFoundException($"Unable to open PDF file: {inputFile}");
        }

        int pageCount = pdfDoc.GetNumPages();
        pdfPage = (Acrobat.CAcroPDPage)pdfDoc.AcquirePage(0);
        pdfPoint = (Acrobat.CAcroPoint)pdfPage.GetSize();

        pdfRect = (Acrobat.CAcroRect)Microsoft.VisualBasic.Interaction.CreateObject("AcroExch.Rect", "");
        pdfRect.Left = 0;
        pdfRect.right = pdfPoint.x;
        pdfRect.Top = 0;
        pdfRect.bottom = pdfPoint.y;

        pdfPage.CopyToClipboard(pdfRect, 0, 0, 100);
        IDataObject clipboardData = Clipboard.GetDataObject();

        if (clipboardData.GetDataPresent(DataFormats.Bitmap))
        {
            Bitmap pdfBitmap = (Bitmap)clipboardData.GetData(DataFormats.Bitmap);

            int thumbnailWidth = 45;
            int thumbnailHeight = 59;
            string templateFile = pdfPoint.x < pdfPoint.y ? templatePortraitFile : templateLandscapeFile;

            if (pdfPoint.x > pdfPoint.y)
            {
                // Swap width and height for landscape orientation
                (thumbnailWidth, thumbnailHeight) = (thumbnailHeight, thumbnailWidth);
            }

            Bitmap templateBitmap = new Bitmap(templateFile);
            Image pdfImage = pdfBitmap.GetThumbnailImage(thumbnailWidth, thumbnailHeight, null, IntPtr.Zero);

            Bitmap thumbnailBitmap = new Bitmap(thumbnailWidth + 7, thumbnailHeight + 7, System.Drawing.Imaging.PixelFormat.Format32bppArgb);

            templateBitmap.MakeTransparent();

            using (Graphics thumbnailGraphics = Graphics.FromImage(thumbnailBitmap))
            {
                thumbnailGraphics.DrawImage(pdfImage, 2, 2, thumbnailWidth, thumbnailHeight);
                thumbnailGraphics.DrawImage(templateBitmap, 0, 0);
                thumbnailBitmap.Save(outputFile, System.Drawing.Imaging.ImageFormat.Png);
            }

            Console.WriteLine("Generated thumbnail: {0}", outputFile);

            pdfDoc.Close();
            Marshal.ReleaseComObject(pdfPage);
            Marshal.ReleaseComObject(pdfRect);
            Marshal.ReleaseComObject(pdfDoc);
        }
    }
}
```

## Aspose.PDF for .NETアプローチ

Aspose.PDF for .NETは、PDFドキュメントを扱うための広範なサポートを提供します。また、PDFドキュメントのページをさまざまな画像形式に変換する機能もサポートしています。上記の機能は、Aspose.PDF for .NETを使用することで簡単に実現できます。

Aspose.PDFには明確な利点があります：

- PDFファイルを扱うためにAdobe Acrobatをシステムにインストールする必要がありません。
- Aspose.PDF for .NETの使用は、Acrobat Automationと比較してシンプルで理解しやすいです。

PDFページをJPEGに変換する必要がある場合、[Aspose.PDF.Devices](https://reference.aspose.com/pdf/ja/net/aspose.pdf.devices)名前空間には、PDFページをJPEG画像にレンダリングするための[JpegDevice](https://reference.aspose.com/pdf/ja/net/aspose.pdf.devices/jpegdevice)というクラスがあります。以下のコードスニペットを見てください。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GenerateThumbnailImagesFromPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Retrieve names of all the PDF files in a particular directory
    string[] fileEntries = Directory.GetFiles(dataDir, "*.pdf");

    // Iterate through all the files entries in array
    for (int counter = 0; counter < fileEntries.Length; counter++)
    {
        // Open PDF document
        using (var document = new Aspose.Pdf.Document(fileEntries[counter]))
        {
            for (int pageCount = 1; pageCount <= document.Pages.Count; pageCount++)
            {
                using (FileStream imageStream = new FileStream(dataDir + @"\Thumbanils" + counter.ToString() + "_" + pageCount + ".jpg", FileMode.Create))
                {
                    var resolution = new Aspose.Pdf.Devices.Resolution(300);
                    var jpegDevice = new Aspose.Pdf.Devices.JpegDevice(45, 59, resolution, 100);
                    // Convert a particular page and save the image to stream
                    jpegDevice.Process(document.Pages[pageCount], imageStream);
                }
            }
        }
    }
}
```

{{% alert color="primary" %}}

- PDFドキュメントからサムネイル画像を生成するためにCodeProjectに感謝します。[Generate Thumbnail Image from PDF document](https://www.codeproject.com/Articles/5887/Generate-Thumbnail-Images-from-PDF-Documents)。
- Acrobat SDKリファレンスに感謝します。[Acrobat SDK reference](https://opensource.adobe.com/dc-acrobat-sdk-docs/acrobatsdk/documentation.html)。

{{% /alert %}}

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