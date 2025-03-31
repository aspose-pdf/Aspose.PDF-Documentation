---
title: PdfExtractorを使用して画像を抽出する
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ja/net/extract-images/
description: このセクションでは、PdfExtractorクラスを使用してAspose.PDFファサードで画像を抽出する方法を説明します。
lastmod: "2021-07-15"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Images using PdfExtractor",
    "alternativeHeadline": "Extract Images from PDF with PdfExtractor Class",
    "abstract": "Aspose.PDFのPdfExtractor機能は、ユーザーがPDFドキュメントから効率的に画像を抽出できるようにし、ドキュメント全体、特定のページ、または指定された範囲から画像を抽出するなどの複数のオプションを提供します。画像をファイルまたはメモリストリームに直接保存することをサポートし、PDF資産を扱う開発者に柔軟性を高めます。この強力な機能により、画像抽出モードを正確に制御でき、さまざまなPDFコンテンツタイプを扱いやすくなります。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1789",
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
    "url": "/net/extract-images/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-images/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

## PDF全体からファイルに画像を抽出する（ファサード）

[PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor)クラスを使用すると、PDFファイルから画像を抽出できます。まず、[PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor)クラスのオブジェクトを作成し、[BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index)メソッドを使用して入力PDFファイルをバインドする必要があります。その後、[ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage)メソッドを呼び出して、すべての画像をメモリに抽出します。画像が抽出されたら、[HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage)および[GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1)メソッドを使用してそれらの画像を取得できます。抽出されたすべての画像をwhileループを使用してループする必要があります。画像をディスクに保存するには、ファイルパスを引数として受け取る[GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1)メソッドのオーバーロードを呼び出すことができます。以下のコードスニペットは、PDF全体からファイルに画像を抽出する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImagesWholePDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        extractor.BindPdf(dataDir + "sample_cats_dogs.pdf");

        // Extract all the images
        extractor.ExtractImage();

        // Get all the extracted images
        while (extractor.HasNextImage())
        {
            extractor.GetNextImage(dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg");
        }
    }
}
```

## PDF全体からストリームに画像を抽出する（ファサード）

[PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor)クラスを使用すると、PDFファイルからストリームに画像を抽出できます。まず、[PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor)クラスのオブジェクトを作成し、[BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index)メソッドを使用して入力PDFファイルをバインドする必要があります。その後、[ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage)メソッドを呼び出して、すべての画像をメモリに抽出します。画像が抽出されたら、[HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage)および[GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1)メソッドを使用してそれらの画像を取得できます。抽出されたすべての画像をwhileループを使用してループする必要があります。画像をストリームに保存するには、Streamを引数として受け取る[GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1)メソッドのオーバーロードを呼び出すことができます。以下のコードスニペットは、PDF全体からストリームに画像を抽出する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImagesWholePDFStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        extractor.BindPdf(dataDir + "sample_cats_dogs.pdf");

        // Extract images
        extractor.ExtractImage();
        // Get all the extracted images
        while (extractor.HasNextImage())
        {
            // Read image into memory stream
            MemoryStream memoryStream = new MemoryStream();
            extractor.GetNextImage(memoryStream);

            // Write to disk, if you like, or use it otherwise
            using (FileStream fileStream = new FileStream(dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg", FileMode.Create))
            {
                memoryStream.WriteTo(fileStream);
            }
        }
    }
}
```

## PDFの特定のページから画像を抽出する（ファサード）

PDFファイルの特定のページから画像を抽出できます。そのためには、[StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage)および[EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage)プロパティを、画像を抽出したい特定のページに設定する必要があります。まず、[PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor)クラスのオブジェクトを作成し、[BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index)メソッドを使用して入力PDFファイルをバインドする必要があります。次に、[StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage)および[EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage)プロパティを設定する必要があります。その後、[ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage)メソッドを呼び出して、すべての画像をメモリに抽出します。画像が抽出されたら、[HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage)および[GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1)メソッドを使用してそれらの画像を取得できます。抽出されたすべての画像をwhileループを使用してループする必要があります。画像をディスクまたはストリームに保存できます。適切なオーバーロードの[GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1)メソッドを呼び出すだけで済みます。以下のコードスニペットは、PDFの特定のページからストリームに画像を抽出する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImagesParticularPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        extractor.BindPdf(dataDir + "sample_cats_dogs.pdf");

        // Set StartPage and EndPage properties to the page number to
        // You want to extract images from
        extractor.StartPage = 2;
        extractor.EndPage = 2;

        // Extract images
        extractor.ExtractImage();
        // Get extracted images
        while (extractor.HasNextImage())
        {
            // Read image into memory stream
            MemoryStream memoryStream = new MemoryStream();
            extractor.GetNextImage(memoryStream);

            // Write to disk, if you like, or use it otherwise
            using (FileStream fileStream = new FileStream(dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg", FileMode.Create))
            {
                memoryStream.WriteTo(fileStream);
            }
        }
    }
}
```

## PDFのページ範囲から画像を抽出する（ファサード）

PDFファイルのページ範囲から画像を抽出できます。そのためには、[StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage)および[EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage)プロパティを、画像を抽出したいページ範囲に設定する必要があります。まず、[PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor)クラスのオブジェクトを作成し、[BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index)メソッドを使用して入力PDFファイルをバインドする必要があります。次に、[StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage)および[EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage)プロパティを設定する必要があります。その後、[ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage)メソッドを呼び出して、すべての画像をメモリに抽出します。画像が抽出されたら、[HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage)および[GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1)メソッドを使用してそれらの画像を取得できます。抽出されたすべての画像をwhileループを使用してループする必要があります。画像をディスクまたはストリームに保存できます。適切なオーバーロードの[GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1)メソッドを呼び出すだけで済みます。以下のコードスニペットは、PDFのページ範囲からストリームに画像を抽出する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImagesRangePages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open input PDF
    using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        extractor.BindPdf(dataDir + "sample_cats_dogs.pdf");

        // Set StartPage and EndPage properties to the page number to
        // You want to extract images from
        extractor.StartPage = 2;
        extractor.EndPage = 2;

        // Extract images
        extractor.ExtractImage();

        // Get extracted images
        while (extractor.HasNextImage())
        {
            // Read image into memory stream
            MemoryStream memoryStream = new MemoryStream();
            extractor.GetNextImage(memoryStream);

            // Write to disk, if you like, or use it otherwise
            using (FileStream fileStream = new
            FileStream(dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg", FileMode.Create))
            {
                memoryStream.WriteTo(fileStream);
            }
        }
    }
}
```

## 画像抽出モードを使用して画像を抽出する（ファサード）

[PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor)クラスを使用すると、PDFファイルから画像を抽出できます。Aspose.PDFは2つの抽出モードをサポートしています。最初は、PDFドキュメントで実際に使用されている画像を抽出するActuallyUsedImageです。2番目のモードは、PDFドキュメントのリソースに定義されている画像を抽出する[DefinedInResources](https://reference.aspose.com/pdf/net/aspose.pdf/extractimagemode)です（デフォルトの抽出モード）。まず、[PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor)クラスのオブジェクトを作成し、[BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index)メソッドを使用して入力PDFファイルをバインドする必要があります。その後、[PdfExtractor.ExtractImageMode](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/extractimagemode)プロパティを使用して画像抽出モードを指定します。次に、指定したモードに応じて、[ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage)メソッドを呼び出して、すべての画像をメモリに抽出します。画像が抽出されたら、[HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage)および[GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1)メソッドを使用してそれらの画像を取得できます。抽出されたすべての画像をwhileループを使用してループする必要があります。画像をディスクに保存するには、ファイルパスを引数として受け取る[GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1)メソッドのオーバーロードを呼び出すことができます。

以下のコードスニペットは、ExtractImageModeオプションを使用してPDFファイルから画像を抽出する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImagesImageExtractionMode()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        extractor.BindPdf(dataDir + "sample_cats_dogs.pdf");

        // Specify Image Extraction Mode
        //extractor.ExtractImageMode = ExtractImageMode.ActuallyUsed;
        extractor.ExtractImageMode = Aspose.Pdf.ExtractImageMode.DefinedInResources;

        // Extract Images based on Image Extraction Mode
        extractor.ExtractImage();

        // Get all the extracted images
        while (extractor.HasNextImage())
        {
            extractor.GetNextImage(dataDir + DateTime.Now.Ticks.ToString() + "_out.png", System.Drawing.Imaging.ImageFormat.Png);
        }
    }
}
```

PDFにテキストまたは画像が含まれているかどうかを確認するには、次のコードスニペットを使用します：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CheckIfPdfContainsTextOrImages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Instantiate a memoryStream object to hold the extracted text from Document
    MemoryStream ms = new MemoryStream();
    // Instantiate PdfExtractor object
    using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        extractor.BindPdf(dataDir + "FilledForm.pdf");
        // Extract text from the input PDF document
        extractor.ExtractText();
        // Save the extracted text to a text file
        extractor.GetText(ms);
        // Check if the MemoryStream length is greater than or equal to 1

        bool containsText = ms.Length >= 1;

        // Extract images from the input PDF document
        extractor.ExtractImage();

        // Calling HasNextImage method in while loop. When images will finish, loop will exit
        bool containsImage = extractor.HasNextImage();

        // Now find out whether this PDF is text only or image only

        if (containsText && !containsImage)
        {
            Console.WriteLine("PDF contains text only");
        }
        else if (!containsText && containsImage)
        {
            Console.WriteLine("PDF contains image only");
        }
        else if (containsText && containsImage)
        {
            Console.WriteLine("PDF contains both text and image");
        }
        else if (!containsText && !containsImage)
        {
            Console.WriteLine("PDF contains neither text or nor image");
        }
    }
}
```