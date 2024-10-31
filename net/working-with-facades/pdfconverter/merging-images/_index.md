---
title: Merge images 
type: docs
weight: 20
url: /net/merge-images/
description: This section explains how to merge Images, and it is possible to save in the Tiff format.
lastmod: "2021-06-05"
draft: false
---

Aspose.PDF 21.4 allows you to combine Images. [Merge Images](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/mergeimages) method checks the contents of a specific folder and works with the specified type of files in it. When working with merging pictures, we specify 'inputImagesStreams', Image Format and Image Merge Mode (as example - vertical) of our file. Then we save our result in FileOutputStream.

Follow the next code snippet for resolve your task:

## Merge Images

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
}
```

The second example works the same as the previous one, but the merged images will be saved horizontally.

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

In the third example, we will merge the pictures by centering them. Two horizontally, two vertically.

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

Also, Aspose.PDF for Java present you the opportunity to combine pictures and save them in the Tiff format, using  [MergeImagesAsTiff Method](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#saveAsTIFF-java.io.OutputStream-).

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

To save the merged images as one image on PDF page, we place them in the imageStream, place the result on the page with addImage method, where we specify the coordinates where we want to place them.

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