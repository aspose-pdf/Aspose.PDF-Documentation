---
title: Merge images 
type: docs
weight: 20
url: /net/merge-images/
description: Discover how to merge images into a single PDF document in .NET using Aspose.PDF for streamlined document creation.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Merge images",
    "alternativeHeadline": "Merge Images with Flexible Formats and Arrangements",
    "abstract": "Aspose.PDF for .NET introduces a powerful new feature that enables users to merge images seamlessly. This functionality allows for combining images in various formats and styles such as vertical, horizontal, or centered while also offering the option to save the final output in the highly versatile TIFF format. Ideal for enhancing document presentations, this feature simplifies the process of creating merged image files using a straightforward code integration",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "482",
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
    "url": "/net/merge-images/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/merge-images/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

Aspose.PDF 21.4 allows you to combine Images. [Merge Images](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/mergeimages) method checks the contents of a specific folder and works with the specified type of files in it. When working with merging pictures, we specify 'inputImagesStreams', Image Format and Image Merge Mode (as example - vertical) of our file. Then we save our result in FileOutputStream.

Follow the next code snippet for resolve your task:

## Merge Images

```csharp
public static class ExamplePdfConverter
{
    private static readonly string dataDir = @"C:\Samples\Facades\PdfConverter\";
    public static void MergeImages01()
    {
        var fileStreams = Directory.GetFiles(dataDir, "cat*.jpg")
                                .OrderBy(f => f)
                                .Select(f => File.OpenRead(f))
                                .Cast<Stream>()
                                .ToList();

        using (Stream inputStream =
                PdfConverter.MergeImages(fileStreams, ImageFormat.Jpeg, ImageMergeMode.Vertical, 1, 1))
        {
            FileStream outputStream = new FileStream(dataDir + "merged_images.jpg", FileMode.Create);
            inputStream.CopyTo(outputStream);
        }
    }
}
```

The second example works the same as the previous one, but the merged images will be saved horizontally.

```csharp
public static void MergeImages02()
{
    var fileStreams = Directory.GetFiles(dataDir, "cat*.jpg")
                            .OrderBy(f => f)
                            .Select(f => File.OpenRead(f))
                            .Cast<Stream>()
                            .ToList();

    using (Stream inputStream =
            PdfConverter.MergeImages(fileStreams, ImageFormat.Jpeg, ImageMergeMode.Horizontal, 1, 1))
    {
        FileStream outputStream = new FileStream(dataDir + "merged_images.jpg", FileMode.Create);
        inputStream.CopyTo(outputStream);
    }
}
```

In the third example, we will merge the pictures by centering them. Two horizontally, two vertically.

```csharp
public static void MergeImages03()
{
    var fileStreams = Directory.GetFiles(dataDir, "cat*.jpg")
                            .OrderBy(f => f)
                            .Select(f => File.OpenRead(f))
                            .Cast<Stream>()
                            .ToList();

    using (Stream inputStream =
            PdfConverter.MergeImages(fileStreams, ImageFormat.Jpeg, ImageMergeMode.Center, 2, 2))
    {
        FileStream outputStream = new FileStream(dataDir + "merged_images.jpg", FileMode.Create);
        inputStream.CopyTo(outputStream);
    }
}
```

Also, Aspose.PDF for Java present you the opportunity to combine pictures and save them in the Tiff format, using  [MergeImagesAsTiff Method](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#saveAsTIFF-java.io.OutputStream-).

```csharp
public static void MergeImages04()
{
    var fileStreams = Directory.GetFiles(dataDir, "cat*.jpg")
                            .OrderBy(f => f)
                            .Select(f => File.OpenRead(f))
                            .Cast<Stream>()
                            .ToList();

    using (Stream inputStream =
            PdfConverter.MergeImagesAsTiff(fileStreams))
    {
        FileStream outputStream = new FileStream(dataDir + "merged_images.tiff", FileMode.Create);
        inputStream.CopyTo(outputStream);
    }
}
```

To save the merged images as one image on PDF page, we place them in the imageStream, place the result on the page with addImage method, where we specify the coordinates where we want to place them.

```csharp
   public static void MergeImages05()
        {
            var fileStreams = Directory.GetFiles(dataDir, "cat*.jpg")
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
        document.Save(dataDir + "merged_images.pdf");
    }
}
```