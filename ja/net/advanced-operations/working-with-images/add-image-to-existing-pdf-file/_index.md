---
title: C#を使用してPDFに画像を追加
linktitle: 画像を追加
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ja/net/add-image-to-existing-pdf-file/
description: このセクションでは、C#ライブラリを使用して既存のPDFファイルに画像を追加する方法について説明します。
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Image to PDF using C#",
    "alternativeHeadline": "Add Images PDFs in C#",
    "abstract": "Aspose.PDFライブラリの新機能により、ユーザーはC#を使用して既存のPDFファイルに画像をシームレスに追加できます。この機能は、文書内で画像を正確に配置およびスケーリングできるようにすることで、PDF操作を簡素化し、高品質な統合と視覚要素の制御を保証します。さまざまな画像形式と構成をサポートするこのツールは、PDFコンテンツ管理の柔軟性を向上させます。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Add Image to PDF, C#, Aspose.PDF, PDF document generation, image compression, image aspect ratio, PDF file manipulation, add image method, XImage class, clipping mask",
    "wordcount": "1692",
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
    "url": "/net/add-image-to-existing-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-image-to-existing-pdf-file/"
    },
    "dateModified": "2025-04-08",
    "description": "このセクションでは、C#ライブラリを使用して既存のPDFファイルに画像を追加する方法について説明します。"
}
</script>

## 既存のPDFファイルに画像を追加

すべてのPDFページには、リソースとコンテンツのプロパティが含まれています。リソースには画像やフォームなどが含まれ、コンテンツはPDFオペレーターのセットで表されます。各オペレーターには名前と引数があります。この例では、オペレーターを使用してPDFファイルに画像を追加します。

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/)ライブラリでも動作します。

既存のPDFファイルに画像を追加するには：

- ドキュメントオブジェクトを作成し、入力PDFドキュメントを開きます。
- 画像を追加したいページを取得します。
- ページのリソースコレクションに画像を追加します。
- オペレーターを使用してページに画像を配置します：
- GSaveオペレーターを使用して現在のグラフィカル状態を保存します。
- ConcatenateMatrixオペレーターを使用して画像を配置する位置を指定します。
- Doオペレーターを使用してページに画像を描画します。
- 最後に、GRestoreオペレーターを使用して更新されたグラフィカル状態を保存します。
- ファイルを保存します。
次のコードスニペットは、PDFドキュメントに画像を追加する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageToPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddImage.pdf"))
    {
        // Set coordinates for the image placement
        int lowerLeftX = 100;
        int lowerLeftY = 100;
        int upperRightX = 200;
        int upperRightY = 200;

        // Get the page where image needs to be added
        var page = document.Pages[1];

        // Load image into stream
        using (var imageStream = new FileStream(dataDir + "AddImage.jpg", FileMode.Open))
        {
            // Add image to Images collection of Page Resources
            page.Resources.Images.Add(imageStream);

            // Using GSave operator: this operator saves the current graphics state
            page.Contents.Add(new Aspose.Pdf.Operators.GSave());

            // Create Rectangle and Matrix objects to define image positioning
            var rectangle = new Aspose.Pdf.Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
            var matrix = new Aspose.Pdf.Matrix(new double[] { rectangle.URX - rectangle.LLX, 0, 0, rectangle.URY - rectangle.LLY, rectangle.LLX, rectangle.LLY });

            // Using ConcatenateMatrix operator: defines how the image must be placed
            page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(matrix));

            // Retrieve the added image and use Do operator to draw it
            var ximage = page.Resources.Images[page.Resources.Images.Count];
            page.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));

            // Using GRestore operator: this operator restores the graphics state
            page.Contents.Add(new Aspose.Pdf.Operators.GRestore());
        }

        // Save PDF document
        document.Save(dataDir + "AddImage_out.pdf");
    }
}
```

{{% alert color="primary" %}}

デフォルトでは、JPEGの品質は100%に設定されています。より良い圧縮と品質を適用するには、次のオーバーロードを使用します：

{{% /alert %}}

- XImageCollectionクラスに追加されたReplaceメソッドのオーバーロード：public void Replace(int index, Stream stream, int quality)
- XImageCollectionクラスに追加されたAddメソッドのオーバーロード：public void Add(Stam stream, int quality)

## 既存のPDFファイルに画像を追加（ファサード）

PDFファイルに画像を追加するための別の簡単な方法もあります。[PdfFileMend](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffilemend)クラスの[AddImage](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffilemend/methods/addimage/index)メソッドを使用できます。[AddImage](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffilemend/methods/addimage/index)メソッドは、追加する画像、画像を追加するページ番号、および座標情報を必要とします。その後、Closeメソッドを使用して更新されたPDFファイルを保存します。次のコードスニペットは、既存のPDFファイルに画像を追加する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageToPDFUsingPdfFileMender()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Define image file and output PDF file paths
    var imageFileName = Path.Combine(dataDir, "Images", "Sample-01.jpg");

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add first page with specified size
        var page = document.Pages.Add();
        page.SetPageSize(Aspose.Pdf.PageSize.A3.Height, Aspose.Pdf.PageSize.A3.Width);

        // Add second page
        page = document.Pages.Add();

        // Create PdfFileMend object
        var mender = new Aspose.Pdf.Facades.PdfFileMend(document);

        // Add image to the first page using the mender
        mender.AddImage(imageFileName, 1, 0, 0, (float)page.CropBox.Width, (float)page.CropBox.Height);

        // Save PDF document
        document.Save(dataDir + "AddImageMender_out.pdf");
    }
}
```

時には、PDFに挿入する前に画像をトリミングする必要があります。`AddImage()`メソッドを使用してトリミングされた画像を追加できます：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddCroppedImageToPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Define image file and output PDF file paths
    var imageFileName = Path.Combine(dataDir, "Images", "Sample-01.jpg");
    var outputPdfFileName = dataDir + "Example-add-image-mender.pdf";

    // Open PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Open image stream
        using (var imgStream = File.OpenRead(imageFileName))
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

        // Save PDF document to the specified file path
        document.Save(dataDir + "AddCroppedImageMender_out.pdf");
    }
}
```

## ページに画像を配置し、アスペクト比を保持（制御）する

画像の寸法がわからない場合、ページ上で歪んだ画像が表示される可能性があります。次の例は、これを回避する方法の一つを示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddingImageAndPreserveAspectRatioIntoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Load the image
    using (var bitmap = System.Drawing.Image.FromFile(dataDir + "InputImage.jpg"))
    {
        // Get the original width and height of the image
        int width = bitmap.Width;
        int height = bitmap.Height;

        // Create PDF document
        using (var document = new Aspose.Pdf.Document())
        {
            // Add page
            var page = document.Pages.Add();

            // Define the scaled width and height while preserving the aspect ratio
            int scaledWidth = 400;
            int scaledHeight = scaledWidth * height / width;

            // Add the image to the page
            page.AddImage(dataDir + "InputImage.jpg", new Aspose.Pdf.Rectangle(10, 10, scaledWidth, scaledHeight));

            // Save PDF document
            document.Save(dataDir + "PreserveAspectRatio.pdf");
        }
    }
}
```

時には、大きな画像がPDFに追加されるときにスケーリングの問題が発生します。次のコードスニペットは、PDFページの寸法に応じて画像をスケーリングし、画像が適切にフィットし、見栄えが良くなるようにします。

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddingImageAndPreserveAspectRatioIntoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();
    var file = dataDir + "AddImageAccordingToPage.jpg";

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var pdfImageSection = document.Pages.Add();
        using (var stream = new FileStream(file, FileMode.Open))
        {
            // Open bitmap
            using (var img = new Bitmap(stream))
            {
                // Scale image according to page dimensions
                using (var scaledImg = ScaleImage(img, (int)pdfImageSection.PageInfo.Width, (int)pdfImageSection.PageInfo.Height))
                {
                    using (var ms = new MemoryStream())
                    {
                        scaledImg.Save(ms, ImageFormat.Jpeg);
                        ms.Seek(0, SeekOrigin.Begin);
                        var image = new Aspose.Pdf.Image
                        {
                            ImageStream = ms
                        };

                        // Add the image to the page
                        pdfImageSection.Paragraphs.Add(image);

                        // Save PDF document
                        document.Save("AddImageAccordingToPage.pdf");
                    }
                }
            }
        }
    }
}

private static Image ScaleImage(Image image, int maxWidth, int maxHeight)
{
    var ratioX = (double)maxWidth / image.Width;
    var ratioY = (double)maxHeight / image.Height;
    var ratio = Math.Min(ratioX, ratioY);
    var newWidth = (int)(image.Width * ratio);
    var newHeight = (int)(image.Height * ratio);
    var newImage = new Bitmap(newWidth, newHeight);
    using (var graphics = Graphics.FromImage(newImage))
    {
        graphics.DrawImage(image, 0, 0, newWidth, newHeight);
    }
    return newImage;
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddingImageAndPreserveAspectRatioIntoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();
    var file = dataDir + "AddImageAccordingToPage.jpg";

    // Create PDF document
    using var document = new Aspose.Pdf.Document();
    
    // Add page
    var pdfImageSection = document.Pages.Add();
    using var stream = new FileStream(file, FileMode.Open);
    // Open bitmap
    using var img = new Bitmap(stream);
    // Scale image according to page dimensions
    using var scaledImg = ScaleImage(img, (int)pdfImageSection.PageInfo.Width, (int)pdfImageSection.PageInfo.Height);
    using var ms = new MemoryStream();
    scaledImg.Save(ms, ImageFormat.Jpeg);
    ms.Seek(0, SeekOrigin.Begin);
    var image = new Aspose.Pdf.Image
    {
        ImageStream = ms
    };

    // Add the image to the page
    pdfImageSection.Paragraphs.Add(image);

    // Save PDF document
    document.Save("AddImageAccordingToPage.pdf");

}

private static Image ScaleImage(Image image, int maxWidth, int maxHeight)
{
    var ratioX = (double)maxWidth / image.Width;
    var ratioY = (double)maxHeight / image.Height;
    var ratio = Math.Min(ratioX, ratioY);
    var newWidth = (int)(image.Width * ratio);
    var newHeight = (int)(image.Height * ratio);
    var newImage = new Bitmap(newWidth, newHeight);
    using var graphics = Graphics.FromImage(newImage);
    graphics.DrawImage(image, 0, 0, newWidth, newHeight);
    return newImage;
}
```
{{< /tab >}}
{{< /tabs >}}

## PDF内の画像がカラーか白黒かを識別する

画像のサイズを減らすために、さまざまなタイプの圧縮を画像に適用できます。画像に適用される圧縮のタイプは、ソース画像のColorSpaceに依存します。つまり、画像がカラー（RGB）の場合はJPEG2000圧縮を適用し、白黒の場合はJBIG2/JBIG2000圧縮を適用する必要があります。したがって、各画像タイプを識別し、適切な圧縮タイプを使用することで、最適化された出力を作成できます。

PDFファイルには、テキスト、画像、グラフ、添付ファイル、注釈などの要素が含まれており、ソースPDFファイルに画像が含まれている場合、画像のカラースペースを特定し、PDFファイルサイズを減らすために適切な圧縮を適用できます。次のコードスニペットは、PDF内の画像がカラーか白黒かを識別する手順を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImageTypesFromPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Counters for grayscale and RGB images
    int grayscaled = 0;
    int rgb = 0;

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractImages.pdf"))
    {
        // Iterate through all pages in the document
        foreach (Aspose.Pdf.Page page in document.Pages)
        {
            Console.WriteLine("--------------------------------");
            var abs = new Aspose.Pdf.ImagePlacementAbsorber();
            page.Accept(abs);

            // Get the count of images on the current page
            Console.WriteLine("Total Images = {0} on page number {1}", abs.ImagePlacements.Count, page.Number);

            // Iterate through all the image placements on the page
            int image_counter = 1;
            foreach (Aspose.Pdf.ImagePlacement ia in abs.ImagePlacements)
            {
                // Determine the color type of the image
                var colorType = ia.Image.GetColorType();
                switch (colorType)
                {
                    case Aspose.Pdf.ColorType.Grayscale:
                        ++grayscaled;
                        Console.WriteLine("Image {0} is Grayscale...", image_counter);
                        break;
                    case Aspose.Pdf.ColorType.Rgb:
                        ++rgb;
                        Console.WriteLine("Image {0} is RGB...", image_counter);
                        break;
                }
                image_counter += 1;
            }
        }
    }
}
```

## 画像の品質を制御する

PDFファイルに追加される画像の品質を制御することが可能です。[XImageCollection](https://reference.aspose.com/pdf/ja/net/aspose.pdf/ximagecollection)クラスのオーバーロードされた[Replace](https://reference.aspose.com/pdf/ja/net/aspose.pdf.ximagecollection/replace/methods/1)メソッドを使用します。

次のコードスニペットは、すべてのドキュメント画像をJPEGに変換し、圧縮に80%の品質を使用する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceImagesInPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ReplaceImages.pdf"))
    {
        // Iterate through all pages in the document
        foreach (Aspose.Pdf.Page page in document.Pages)
        {
            int idx = 1;
            // Iterate through all images in the page's resources
            foreach (Aspose.Pdf.XImage image in page.Resources.Images)
            {
                using (var imageStream = new MemoryStream())
                {
                    // Save the image as JPEG with 80% quality
                    image.Save(imageStream, System.Drawing.Imaging.ImageFormat.Jpeg);
                    // Replace the image in the page's resources
                    page.Resources.Images.Replace(idx, imageStream, 80);
                    idx = idx + 1;
                }
            }
        }

        // Save PDF document
        document.Save(dataDir + "ReplaceImages_out.pdf");
    }
}
```

## 画像にクリッピングマスクを適用するサポート

ベースのビットマップ画像の上にベクター形状を配置することはマスクとして機能し、ベクター形状と一致するベースデザインの部分のみを露出させます。形状の外側のすべての領域は隠されます。

コードスニペットは、PDFを読み込み、2つの画像ファイルを開き、これらの画像をPDFの最初のページの最初の2つの画像にステンシルマスクとして適用します。

ステンシルマスクは、'XImage.AddStencilMask(Stream maskStream)'メソッドで追加できます：

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
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