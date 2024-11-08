---
title: 合并图片
type: docs
weight: 20
url: /zh/net/merge-images/
description: 本节解释如何合并图像，并可以保存为Tiff格式。
lastmod: "2021-06-05"
draft: false
---

Aspose.PDF 21.4允许您合并图像。[合并图像](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/mergeimages)方法检查特定文件夹的内容，并处理其中指定类型的文件。在处理合并图片时，我们指定文件的'inputImagesStreams'、图像格式和图像合并模式（例如 - 垂直）。然后我们将结果保存到FileOutputStream中。

遵循下一个代码片段以解决您的任务：

## 合并图片

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

第二个例子与前一个例子相同，但合并后的图像将水平保存。

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

在第三个例子中，我们将通过居中合并图片。两个水平，两个垂直。

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

同时，Aspose.PDF for Java 为您提供了将图片合并并以 Tiff 格式保存的机会，使用 [MergeImagesAsTiff 方法](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#saveAsTIFF-java.io.OutputStream-)。

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

为了将合并后的图像保存为 PDF 页上的一张图片，我们将它们放在 imageStream 中，使用 addImage 方法将结果放置在页面上，在这里我们指定我们希望放置它们的坐标。

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