---
title: Extraer imágenes de PDF y reconocer códigos de barras
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /es/net/extract-images-from-pdf-and-recognize-barcodes/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Images from PDF and recognize BarCodes",
    "alternativeHeadline": "Extract Images and Barcodes from PDF files in C#",
    "abstract": "Descubre cómo extraer imágenes de documentos PDF de manera eficiente y reconocer con precisión los códigos de barras incrustados utilizando Aspose.PDF for .NET. Esta nueva funcionalidad simplifica el proceso de identificación de información de códigos de barras al procesar imágenes extraídas de cada página de un PDF, mejorando la recuperación y gestión de datos. Explora los pasos detallados y la implementación del código para optimizar tus flujos de trabajo de manejo de documentos",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "317",
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
    "url": "/net/extract-images-from-pdf-and-recognize-barcodes/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-images-from-pdf-and-recognize-barcodes/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

{{% alert color="primary" %}}

Los documentos PDF suelen estar compuestos de texto, imágenes, tablas, archivos adjuntos, gráficos, anotaciones y otros objetos relacionados. Hay casos en los que los códigos de barras están incrustados dentro del archivo PDF y algunos clientes tienen el requisito de identificar los códigos de barras presentes dentro del archivo PDF. El siguiente artículo explica los pasos sobre cómo extraer imágenes de las páginas PDF e identificar los códigos de barras dentro de ellas.

{{% /alert %}}

De acuerdo con el Modelo de Objetos de Documento de Aspose.PDF for .NET, un archivo PDF contiene una o más páginas donde cada página contiene una colección de imágenes, formularios y fuentes en el objeto de recursos. Por lo tanto, para extraer imágenes de un archivo PDF, recorreremos las páginas individuales del archivo PDF, obtendremos la colección de imágenes de una página particular y las guardaremos en un objeto MemoryStream para su posterior procesamiento con la clase BarCodeReader de Aspose.BarCodeRecognition.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void IdentifyBarcodes()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "IdentifyBarcodes.pdf"))
    {
        // Traverse through individual pages of PDF file
        for (int pageCount = 1; pageCount <= document.Pages.Count; pageCount++)
        {
            // Traverse through each image extracted from PDF pages
            foreach (var xImage in document.Pages[pageCount].Resources.Images)
            {
                using (var imageStream = new MemoryStream())
                {
                    // Save PDF document image
                    xImage.Save(imageStream, System.Drawing.Imaging.ImageFormat.Jpeg);
        
                    // Set the stream position to the begining of Stream
                    imageStream.Position = 0;
        
                    // Instantiate BarCodeReader object
                    var barcodeReader = new Aspose.BarCodeRecognition.BarCodeReader(imageStream, Aspose.BarCodeRecognition.BarCodeReadType.Code39Extended);
        
                    while (barcodeReader.Read())
                    {
                        // Get BarCode text from BarCode image
                        var code = barcodeReader.GetCodeText();
        
                        // Write the BarCode text to Console output
                        Console.WriteLine("BARCODE : " + code);
                    }
        
                    // Close BarCodeReader object to release the Image file
                    barcodeReader.Close();
                }
            }
        }
    }
}
```

Para más detalles sobre los temas cubiertos en este artículo, visita los siguientes enlaces:

- [Extraer imágenes del archivo PDF](/net/extract-images-from-the-pdf-file/)
- [Leer códigos de barras](https://docs.aspose.com/barcode/net/barcode-recognition/)