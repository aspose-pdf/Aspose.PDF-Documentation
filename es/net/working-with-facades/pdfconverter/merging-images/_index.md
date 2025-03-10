---
title: Combinar imágenes
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /es/net/merge-images/
description: Descubre cómo combinar imágenes en un solo documento PDF en .NET utilizando Aspose.PDF para una creación de documentos simplificada.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Merge images",
    "alternativeHeadline": "Merge Images with Flexible Formats and Arrangements",
    "abstract": "Aspose.PDF for .NET introduce una nueva característica poderosa que permite a los usuarios combinar imágenes sin problemas. Esta funcionalidad permite combinar imágenes en varios formatos y estilos, como vertical, horizontal o centrado, mientras que también ofrece la opción de guardar la salida final en el versátil formato TIFF. Ideal para mejorar las presentaciones de documentos, esta característica simplifica el proceso de creación de archivos de imágenes combinadas utilizando una integración de código sencilla.",
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
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

Aspose.PDF 21.4 te permite combinar imágenes. El método [Merge Images](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/mergeimages) verifica el contenido de una carpeta específica y trabaja con el tipo de archivos especificado en ella. Al trabajar con la combinación de imágenes, especificamos 'inputImagesStreams', el formato de imagen y el modo de combinación de imágenes (por ejemplo, vertical) de nuestro archivo. Luego guardamos nuestro resultado en FileOutputStream.

Sigue el siguiente fragmento de código para resolver tu tarea:

## Combinar Imágenes

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MergeImages01()
{
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();  // Updated to use dynamic path
    // Get all image files matching the pattern "MergeImages*.jpg"
    var fileStreams = Directory.GetFiles(dataDir, "MergeImages*.jpg")
                                .OrderBy(f => f)
                                .Select(f => File.OpenRead(f))
                                .Cast<Stream>()
                                .ToList();

    using (Stream inputStream = Aspose.Pdf.Facades.PdfConverter.MergeImages(fileStreams, Aspose.Pdf.Drawing.ImageFormat.Jpeg, ImageMergeMode.Vertical, 1, 1))
    using (FileStream outputStream = new FileStream(dataDir + "MergeImages_out.jpg", FileMode.Create))
    {
        // Copy merged images to the output file
        inputStream.CopyTo(outputStream);
    }
}
```

El segundo ejemplo funciona igual que el anterior, pero las imágenes combinadas se guardarán horizontalmente.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MergeImages02()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Get all image files matching the pattern "MergeImages*.jpg"
    var fileStreams = Directory.GetFiles(dataDir, "MergeImages*.jpg")
                            .OrderBy(f => f)
                            .Select(f => File.OpenRead(f))
                            .Cast<Stream>()
                            .ToList();

    using (Stream inputStream =
            Aspose.Pdf.Facades.PdfConverter.MergeImages(fileStreams, Aspose.Pdf.Drawing.ImageFormat.Jpeg, ImageMergeMode.Horizontal, 1, 1))
    using (FileStream outputStream = new FileStream(dataDir + "MergeImages02_out.jpg", FileMode.Create))
    {
        // Copy merged images to the output file
        inputStream.CopyTo(outputStream);
    }
}
```

En el tercer ejemplo, combinaremos las imágenes centrándolas. Dos horizontalmente, dos verticalmente.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MergeImages03()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Get all image files matching the pattern "MergeImages*.jpg"
    var fileStreams = Directory.GetFiles(dataDir, "MergeImages*.jpg")
                            .OrderBy(f => f)
                            .Select(f => File.OpenRead(f))
                            .Cast<Stream>()
                            .ToList();

    using (Stream inputStream =
            Aspose.Pdf.Facades.PdfConverter.MergeImages(fileStreams, Aspose.Pdf.Drawing.ImageFormat.Jpeg, ImageMergeMode.Center, 2, 2))
    using (FileStream outputStream = new FileStream(dataDir + "MergeImages03_out.jpg", FileMode.Create))
    {
        // Copy merged images to the output file
        inputStream.CopyTo(outputStream);
    }
}
```

Además, Aspose.PDF para Java te presenta la oportunidad de combinar imágenes y guardarlas en formato Tiff, utilizando el [MergeImagesAsTiff Method](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#saveAsTIFF-java.io.OutputStream-).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MergeImages04()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Get all image files matching the pattern "MergeImages*.jpg"
    var fileStreams = Directory.GetFiles(dataDir, "MergeImages*.jpg")
                            .OrderBy(f => f)
                            .Select(f => File.OpenRead(f))
                            .Cast<Stream>()
                            .ToList();

    using (Stream inputStream =
            Aspose.Pdf.Facades.PdfConverter.MergeImagesAsTiff(fileStreams))
    using (FileStream outputStream = new FileStream(dataDir + "MergeImages_out.tiff", FileMode.Create))
    {
        // Copy merged images to the output file
        inputStream.CopyTo(outputStream);
    }
}
```

Para guardar las imágenes combinadas como una sola imagen en la página PDF, las colocamos en el imageStream, colocamos el resultado en la página con el método addImage, donde especificamos las coordenadas donde queremos colocarlas.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MergeImages05()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Get all image files matching the pattern "MergeImages*.jpg"
    var fileStreams = Directory.GetFiles(dataDir, "MergeImages*.jpg")
                                .OrderBy(f => f)
                                .Select(f => File.OpenRead(f))
                                .Cast<Stream>()
                                .ToList();

    using (Stream inputStream =
            Aspose.Pdf.Facades.PdfConverter.MergeImages(fileStreams, Aspose.Pdf.Drawing.ImageFormat.Jpeg, ImageMergeMode.Vertical, 1, 1))
    using (MemoryStream outputStream = new MemoryStream())  // Output to MemoryStream
    {
        // Copy merged images to the MemoryStream
        inputStream.CopyTo(outputStream);

        // Create PDF document
        using (var document = new Aspose.Pdf.Document())
        {
            // Add page
            var page = document.Pages.Add();

            // Add the image from the MemoryStream to the page
            page.AddImage(outputStream, new Aspose.Pdf.Rectangle(10, 120, 400, 720));

            // Save PDF document
            document.Save(dataDir + "MergeImages_out.pdf");
        }
    }
}
```