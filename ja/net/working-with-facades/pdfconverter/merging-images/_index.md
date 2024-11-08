---
title: 画像をマージする
type: docs
weight: 20
url: /ja/net/merge-images/
description: このセクションでは画像をマージする方法を説明し、Tiff形式で保存することができます。
lastmod: "2021-06-05"
draft: false
---

Aspose.PDF 21.4を使用すると、画像を結合することができます。[画像をマージ](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/mergeimages)メソッドは、特定のフォルダーの内容をチェックし、その中の指定されたタイプのファイルを処理します。画像をマージする際には、'inputImagesStreams'、画像形式、および画像マージモード（例: 垂直）を指定します。その後、結果をFileOutputStreamに保存します。

次のコードスニペットに従って、タスクを解決してください。

## 画像をマージする

```csharp
public static class ExamplePdfConverter
    {
        private static readonly string _dataDir = @"C:\Samples\Facades\PdfConverter\";
        public static void MergeImages01()
        {
            var fileStreams = Directory.GetFiles(_dataDir, "cat*.jpg")
                                    .OrderBy(f => f)
                                    .Select(f => File.OpenRead(f))
                                    .Cast<Stream>()
                                    .ToList();

            using (Stream inputStream =
                    PdfConverter.MergeImages(fileStreams, ImageFormat.Jpeg, ImageMergeMode.Vertical, 1, 1))
            {
                FileStream outputStream = new FileStream(_dataDir+"merged_images.jpg", FileMode.Create);
                inputStream.CopyTo(outputStream);
            }
        }
```

前の例と同様に2番目の例も機能しますが、結合された画像は水平に保存されます。

```csharp
public static void MergeImages02()
        {
            var fileStreams = Directory.GetFiles(_dataDir, "cat*.jpg")
                                    .OrderBy(f => f)
                                    .Select(f => File.OpenRead(f))
                                    .Cast<Stream>()
                                    .ToList();

            using (Stream inputStream =
                    PdfConverter.MergeImages(fileStreams, ImageFormat.Jpeg, ImageMergeMode.Horizontal, 1, 1))
            {
                FileStream outputStream = new FileStream(_dataDir + "merged_images.jpg", FileMode.Create);
                inputStream.CopyTo(outputStream);
            }
        }
```

3番目の例では、画像を中央に配置して結合します。2枚は水平に、2枚は垂直に。

```csharp
public static void MergeImages03()
        {
            var fileStreams = Directory.GetFiles(_dataDir, "cat*.jpg")
                                    .OrderBy(f => f)
                                    .Select(f => File.OpenRead(f))
                                    .Cast<Stream>()
                                    .ToList();

            using (Stream inputStream =
                    PdfConverter.MergeImages(fileStreams, ImageFormat.Jpeg, ImageMergeMode.Center, 2, 2))
            {
                FileStream outputStream = new FileStream(_dataDir + "merged_images.jpg", FileMode.Create);
                inputStream.CopyTo(outputStream);
            }
        }

```

また、Aspose.PDF for Javaは、[MergeImagesAsTiff メソッド](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#saveAsTIFF-java.io.OutputStream-)を使用して、画像を組み合わせてTiff形式で保存する機能を提供します。

```csharp
public static void MergeImages04()
        {
            var fileStreams = Directory.GetFiles(_dataDir, "cat*.jpg")
                                    .OrderBy(f => f)
                                    .Select(f => File.OpenRead(f))
                                    .Cast<Stream>()
                                    .ToList();

            using (Stream inputStream =
                    PdfConverter.MergeImagesAsTiff(fileStreams))
            {
                FileStream outputStream = new FileStream(_dataDir + "merged_images.tiff", FileMode.Create);
                inputStream.CopyTo(outputStream);
            }
        }
```

PDFページに1枚の画像として結合した画像を保存するために、imageStreamに配置し、addImageメソッドでページに結果を配置します。ここで、配置したい座標を指定します。

```csharp
   public static void MergeImages05()
        {
            var fileStreams = Directory.GetFiles(_dataDir, "cat*.jpg")
                                    .OrderBy(f => f)
                                    .Select(f => File.OpenRead(f))
                                    .Cast<Stream>()
                                    .ToList();

            using (Stream inputStream =
                    PdfConverter.MergeImages(fileStreams, ImageFormat.Jpeg, ImageMergeMode.Vertical, 1, 1))
            {
                MemoryStream outputStream = new MemoryStream();
                inputStream.CopyTo(outputStream);
                var document = new Document();
                var pages = document.Pages.Add();
                pages.AddImage(outputStream, new Rectangle(10,120,400,720));
                document.Save(_dataDir + "merged_images.pdf");
            }

        }
```

公共静的 void MergeImages05()
{
    var fileStreams = Directory.GetFiles(_dataDir, "cat*.jpg")
                                .OrderBy(f => f)
                                .Select(f => File.OpenRead(f))
                                .Cast<Stream>()
                                .ToList();

    using (Stream inputStream =
            PdfConverter.MergeImages(fileStreams, ImageFormat.Jpeg, ImageMergeMode.Vertical, 1, 1))
    {
        MemoryStream outputStream = new MemoryStream();
        inputStream.CopyTo(outputStream);
        var document = new Document();
        var pages = document.Pages.Add();
        pages.AddImage(outputStream, new Rectangle(10,120,400,720));
        document.Save(_dataDir + "merged_images.pdf");
    }

}
```