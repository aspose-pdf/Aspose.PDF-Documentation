---
title: Mesclar imagens
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /pt/net/merge-images/
description: Descubra como mesclar imagens em um único documento PDF no .NET usando Aspose.PDF para uma criação de documentos simplificada.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Merge images",
    "alternativeHeadline": "Merge Images with Flexible Formats and Arrangements",
    "abstract": "Aspose.PDF for .NET introduz um novo recurso poderoso que permite aos usuários mesclar imagens de forma contínua. Essa funcionalidade permite combinar imagens em vários formatos e estilos, como vertical, horizontal ou centralizado, enquanto também oferece a opção de salvar a saída final no versátil formato TIFF. Ideal para aprimorar apresentações de documentos, esse recurso simplifica o processo de criação de arquivos de imagem mesclados usando uma integração de código simples.",
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
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

Aspose.PDF 21.4 permite que você combine Imagens. O método [Merge Images](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/mergeimages) verifica o conteúdo de uma pasta específica e trabalha com o tipo de arquivos especificado nela. Ao trabalhar com a mesclagem de imagens, especificamos 'inputImagesStreams', Formato da Imagem e Modo de Mesclagem de Imagem (como exemplo - vertical) do nosso arquivo. Em seguida, salvamos nosso resultado em FileOutputStream.

Siga o próximo trecho de código para resolver sua tarefa:

## Mesclar Imagens

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

O segundo exemplo funciona da mesma forma que o anterior, mas as imagens mescladas serão salvas horizontalmente.

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

No terceiro exemplo, mesclaremos as imagens centralizando-as. Duas horizontalmente, duas verticalmente.

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

Além disso, Aspose.PDF para Java apresenta a oportunidade de combinar imagens e salvá-las no formato Tiff, usando o [MergeImagesAsTiff Method](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#saveAsTIFF-java.io.OutputStream-).

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

Para salvar as imagens mescladas como uma única imagem na página PDF, colocamos elas no imageStream, colocamos o resultado na página com o método addImage, onde especificamos as coordenadas onde queremos colocá-las.

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