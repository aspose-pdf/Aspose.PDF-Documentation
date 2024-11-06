---
title: C#を使用してPDFに画像を追加
linktitle: 画像を追加
type: docs
weight: 10
url: ja/net/add-image-to-existing-pdf-file/
description: このセクションでは、C#ライブラリを使用して既存のPDFファイルに画像を追加する方法について説明します。
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "C#を使用してPDFに画像を追加",
    "alternativeHeadline": "PDFに画像を追加する方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDFドキュメント生成",
    "keywords": "pdf, c#, pdfに画像を追加",
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
    "url": "/net/add-image-to-existing-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-image-to-existing-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "このセクションでは、C#ライブラリを使用して既存のPDFファイルに画像を追加する方法について説明します。"
}
</script>

## 既存のPDFファイルに画像を追加する

PDFページは、リソースと内容のプロパティを含んでいます。例えば、リソースには画像やフォームが含まれ、内容はPDFオペレータのセットによって表されます。各オペレータには名前と引数があります。この例では、PDFファイルに画像を追加するためにオペレータを使用します。

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/) ライブラリでも機能します。

既存のPDFファイルに画像を追加するには：

- Documentオブジェクトを作成し、入力PDFドキュメントを開きます。
- 画像を追加したいページを取得します。
- 画像をページのリソースコレクションに追加します。
- オペレータを使用してページ上に画像を配置します：
  - 現在のグラフィカル状態を保存するためにGSaveオペレータを使用します。
  - 画像を配置する場所を指定するためにConcatenateMatrixオペレータを使用します。
  - Doオペレータを使用してページ上に画像を描画します。
  - 最後に、更新されたグラフィカル状態を保存するためにGRestoreオペレータを使用します。
- ファイルを保存します。
次のコードスニペットは、PDFドキュメントに画像を追加する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir+ "AddImage.pdf");

// 座標を設定
int lowerLeftX = 100;
int lowerLeftY = 100;
int upperRightX = 200;
int upperRightY = 200;

// 画像を追加するページを取得
Page page = pdfDocument.Pages[1];
// 画像をストリームにロード
FileStream imageStream = new FileStream(dataDir + "aspose-logo.jpg", FileMode.Open);
// ページリソースの画像コレクションに画像を追加
page.Resources.Images.Add(imageStream);
// GSaveオペレータを使用：このオペレータは現在のグラフィックス状態を保存します
page.Contents.Add(new Aspose.Pdf.Operators.GSave());
// RectangleとMatrixオブジェクトを作成
Aspose.Pdf.Rectangle rectangle = new Aspose.Pdf.Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
Matrix matrix = new Matrix(new double[] { rectangle.URX - rectangle.LLX, 0, 0, rectangle.URY - rectangle.LLY, rectangle.LLX, rectangle.LLY });
// ConcatenateMatrix（行列を結合）オペレータを使用：画像が配置される方法を定義
page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(matrix));
XImage ximage = page.Resources.Images[page.Resources.Images.Count];
// Doオペレータを使用：このオペレータは画像を描画します
page.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));
// GRestoreオペレータを使用：このオペレータはグラフィクス状態を復元します
page.Contents.Add(new Aspose.Pdf.Operators.GRestore());
dataDir = dataDir + "AddImage_out.pdf";
// 更新されたドキュメントを保存
pdfDocument.Save(dataDir);
```
{{% alert color="primary" %}}

デフォルトでは、JPEGの品質は100％に設定されています。より良い圧縮と品質を適用するには、以下のオーバーロードを使用します：

{{% /alert %}}

- XImageCollection クラスに追加された Replace メソッドのオーバーロード：public void Replace(int index, Stream stream, int quality)
- XImageCollection クラスに追加された Add メソッドのオーバーロード：public void Add(Stream stream, int quality)

## 既存のPDFファイルに画像を追加する (Facades)

PDFファイルに画像を追加する別の簡単な方法もあります。
PDFファイルに画像を追加するもう一つの簡単な方法があります。

```csharp
string imageFileName = Path.Combine(_dataDir, "Images", "Sample-01.jpg");
string outputPdfFileName = Path.Combine(_dataDir, "Example-add-image-mender.pdf");
Document document = new Document();
Page page = document.Pages.Add();
page.SetPageSize(PageSize.A3.Height, PageSize.A3.Width);
page = document.Pages.Add();
Aspose.Pdf.Facades.PdfFileMend mender = new Aspose.Pdf.Facades.PdfFileMend(document);
mender.AddImage(imageFileName, 1, 0, 0, (float)page.CropBox.Width, (float)page.CropBox.Height);
document.Save(outputPdfFileName);
```

## ページに画像を配置してアスペクト比を保持（制御）する

画像の寸法がわからない場合、ページ上の画像が歪む可能性があります。以下の例は、これを避ける方法の一つを示しています。

```csharp
public static void AddingImageAndPreserveAspectRatioIntoPDF()
{
    var bitmap = System.Drawing.Image.FromFile(_dataDir + "3410492.jpg");

    int width;
    int height;

    width = bitmap.Width;
    height = bitmap.Height;

    var document = new Aspose.Pdf.Document();

    var page = document.Pages.Add();

    int scaledWidth = 400;
    int scaledHeight = scaledWidth * height / width;

    page.AddImage(_dataDir + "3410492.jpg", new Aspose.Pdf.Rectangle(10, 10, scaledWidth, scaledHeight));
    document.Save(_dataDir + "sample_image.pdf");
}
```
## PDF内の画像がカラーか白黒かを識別する

画像のサイズを削減するために、異なるタイプの圧縮を画像に適用できます。画像に適用される圧縮のタイプは、ソース画像のカラースペースに依存します。つまり、画像がカラー（RGB）の場合はJPEG2000圧縮を適用し、白黒の場合はJBIG2/JBIG2000圧縮を適用すべきです。したがって、各画像タイプを識別し、適切なタイプの圧縮を使用することで、最適化された出力を作成できます。

PDFファイルにはテキスト、画像、グラフ、添付ファイル、注釈などの要素が含まれており、ソースPDFファイルに画像が含まれている場合、画像のカラースペースを決定し、PDFファイルのサイズを削減するために適切な圧縮を適用できます。以下のコードスニペットは、PDF内の画像がカラーか白黒かを識別する手順を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// 文書ディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

// グレースケール画像のカウンター
int grayscaled = 0;
// RGB画像のカウンター
int rgd = 0;

using (Document document = new Document(dataDir + "ExtractImages.pdf"))
{
    foreach (Page page in document.Pages)
    {
        Console.WriteLine("--------------------------------");
        ImagePlacementAbsorber abs = new ImagePlacementAbsorber();
        page.Accept(abs);
        // 特定のページ上の画像の数を取得
        Console.WriteLine("Total Images = {0} over page number {1}", abs.ImagePlacements.Count, page.Number);
        // Document.Pages[29].Accept(abs);
        int image_counter = 1;
        foreach (ImagePlacement ia in abs.ImagePlacements)
        {
            ColorType colorType = ia.Image.GetColorType();
            switch (colorType)
            {
                case ColorType.Grayscale:
                    ++grayscaled;
                    Console.WriteLine("Image {0} is GrayScale...", image_counter);
                    break;
                case ColorType.Rgb:
                    ++rgd;
                    Console.WriteLine("Image {0} is RGB...", image_counter);
                    break;
            }
            image_counter += 1;
        }
    }
}
```
## 画質の制御

PDFファイルに追加される画像の品質を制御することができます。[XImageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/ximagecollection) クラスの [Replace](https://reference.aspose.com/pdf/net/aspose.pdf.ximagecollection/replace/methods/1) メソッドを使用します。

次のコードスニペットは、すべてのドキュメント画像を80％の品質で圧縮を使用するJPEGに変換する方法を示しています。

```csharp
Aspose.PDF.Document pdfDocument = new Aspose.PDF.Document(inFile);
foreach (Aspose.PDF.Page page in pdfDocument.Pages)
{
    int idx = 1;
    foreach (Aspose.PDF.XImage image in page.Resources.Images)
    {
        using (MemoryStream imageStream = new MemoryStream())
        {
            image.Save(imageStream, System.Drawing.Imaging.ImageFormat.Jpeg);
            page.Resources.Images.Replace(idx, imageStream, 80);
            idx = idx + 1;
        }
    }
}

// pdfDocument.OptimizeResources();

pdfDocument.Save(outFile);
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET ライブラリ",
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
                "contactType": "営業",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "営業",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "営業",
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

