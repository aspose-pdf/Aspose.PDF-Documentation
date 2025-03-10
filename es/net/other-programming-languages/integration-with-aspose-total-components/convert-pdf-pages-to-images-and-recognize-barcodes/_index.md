---
title: Convertir Páginas de PDF a Imágenes y Reconocer Códigos de Barras
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /es/net/convert-pdf-pages-to-images-and-recognize-barcodes/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF Pages to Images and Recognize Barcodes",
    "alternativeHeadline": "Convert PDF Pages to Images with Barcode Recognition in C#",
    "abstract": "La nueva función permite la conversión fluida de páginas de PDF a varios formatos de imagen, facilitando la identificación de códigos de barras incrustados utilizando Aspose.Barcode para .NET. Esta funcionalidad optimiza el procesamiento de documentos al permitir a los usuarios transformar el contenido de PDF en imágenes y reconocer con precisión los códigos de barras para un manejo eficiente de datos.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "858",
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
    "url": "/net/convert-pdf-pages-to-images-and-recognize-barcodes/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-pages-to-images-and-recognize-barcodes/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

{{% alert color="primary" %}}

Los documentos PDF generalmente comprenden texto, imágenes, tablas, adjuntos, gráficos, anotaciones y otros objetos. Algunos de nuestros clientes necesitan incrustar códigos de barras en documentos y luego identificar códigos de barras en el archivo PDF. El siguiente artículo explica cómo transformar las páginas de un archivo PDF en imágenes e identificar códigos de barras en las imágenes con Aspose.Barcode para .NET.

{{% /alert %}}

## Convertir Páginas a Imágenes y Reconocer Códigos de Barras

{{% alert color="primary" %}}

Aspose.PDF for .NET es un producto muy poderoso para gestionar documentos PDF. Facilita la conversión de páginas en documentos PDF a imágenes. Aspose.BarCode para .NET es un producto igualmente poderoso para generar y reconocer códigos de barras.

La clase PdfConverter bajo el espacio de nombres Aspose.Pdf.Facades admite la conversión de páginas PDF a varios formatos de imagen. El PngDevice bajo el espacio de nombres Aspose.Pdf.Devices admite la conversión de páginas PDF a archivos PNG. Cualquiera de estas clases se puede utilizar para transformar páginas de un archivo PDF en imágenes.

Cuando las páginas se han convertido a un formato de imagen, podemos usar Aspose.BarCode para .NET para identificar códigos de barras dentro de ellas. Los ejemplos de código a continuación muestran cómo convertir páginas utilizando PdfConverter o PngDevice.

{{% /alert %}}

### Usando Aspose.Pdf.Facades

{{% alert color="primary" %}}

La clase PdfConverter contiene un método llamado GetNextImage que genera una imagen de la página PDF actual. Para especificar el formato de imagen de salida, este método acepta un argumento de la enumeración System.Drawing.Imaging.ImageFormat.

Aspose.Barcode contiene un espacio de nombres, BarCodeRecognition, que contiene la clase BarCodeReader. La clase BarCodeReader te permite leer, determinar e identificar códigos de barras de archivos de imagen.

Para los propósitos de este ejemplo, primero convierte una página en un archivo PDF en una imagen con Aspose.Pdf.Facades.PdfConverter. Luego usa la clase Aspose.BarCodeRecognition.BarCodeReader para reconocer el código de barras en la imagen.

{{% /alert %}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void IdentifyBarcodesConverter()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Create a PdfConverter object
    var converter = new Aspose.Pdf.Facades.PdfConverter();

    // Bind PDF document
    converter.BindPdf(dataDir + "IdentifyBarcodes.pdf");

    // Specify the start page to be processed
    converter.StartPage = 1;

    // Specify the end page for processing
    converter.EndPage = 1;

    // Create a Resolution object to specify the resolution of resultant image
    converter.Resolution = new Aspose.Pdf.Devices.Resolution(300);

    // Initialize the convertion process
    converter.DoConvert();

    // Create a MemoryStream object to hold the resultant image
    using (var imageStream = new MemoryStream())
    {
        // Check if pages exist and then convert to image one by one
        while (converter.HasNextImage())
        {
            // Save the image in the given image Format
            converter.GetNextImage(imageStream, System.Drawing.Imaging.ImageFormat.Png);

            // Set the stream position to the beginning of the stream
            imageStream.Position = 0;

            // Instantiate a BarCodeReader object
            var barcodeReader = new Aspose.BarCodeRecognition.BarCodeReader(imageStream, Aspose.BarCodeRecognition.BarCodeReadType.Code39Extended);

            // String txtResult.Text = "";
            while (barcodeReader.Read())
            {
                // Get the barcode text from the barcode image
                var code = barcodeReader.GetCodeText();

                // Write the barcode text to Console output
                Console.WriteLine("BARCODE : " + code);
            }

            // Close the BarCodeReader object to release the image file
            barcodeReader.Close();
        }

        // Close the PdfConverter instance and release the resources
        converter.Close();
    }
}
```

{{% alert color="primary" %}}

En los fragmentos de código anteriores, la imagen de salida se guarda en un objeto MemoryStream. La imagen también se puede guardar en disco. Para hacerlo, reemplaza el objeto MemoryStream con un objeto de cadena que represente la ruta del archivo en el método GetNextImage de la clase PdfConverter.

{{% /alert %}}

#### Usando la Clase PngDevice

En Aspose.Pdf.Devices, está el PngDevice. Esta clase te permite convertir páginas en documentos PDF a imágenes PNG.

Para los propósitos de este ejemplo, carga el archivo PDF de origen en las páginas del documento en imágenes PNG. Cuando se hayan creado las imágenes, usa la clase BarCodeReader bajo Aspose.BarCodeRecognition para identificar y leer códigos de barras en las imágenes.

{{% alert color="primary" %}}

Los ejemplos de código dados aquí recorren las páginas del documento PDF y tratan de identificar códigos de barras en cada página.

{{% /alert %}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void IdentifyBarcodes()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "IdentifyBarcodes.pdf"))
    {
        // Traverse through the individual pages of the PDF file
        for (int pageCount = 1; pageCount <= document.Pages.Count; pageCount++)
        {
            using (var imageStream = new MemoryStream())
            {
                // Create a Resolution object
                var resolution = new Aspose.Pdf.Devices.Resolution(300);

                // Instantiate a PngDevice object while passing a Resolution object as an argument to its constructor
                var pngDevice = new Aspose.Pdf.Devices.PngDevice(resolution);

                // Convert a particular page and save the image to stream
                pngDevice.Process(document.Pages[pageCount], imageStream);

                // Set the stream position to the beginning of Stream
                imageStream.Position = 0;

                // Instantiate a BarCodeReader object
                var barcodeReader = new Aspose.BarCodeRecognition.BarCodeReader(imageStream, Aspose.BarCodeRecognition.BarCodeReadType.Code39Extended);

                // String txtResult.Text = "";
                while (barcodeReader.Read())
                {
                    // Get the barcode text from the barcode image
                    var code = barcodeReader.GetCodeText();

                    // Write the barcode text to Console output
                    Console.WriteLine("BARCODE : " + code);
                }

                // Close the BarCodeReader object to release the image file
                barcodeReader.Close();
            }
        }
    }
}
```

{{% alert color="primary" %}}

Para más información sobre los temas cubiertos en este artículo, visita:

- Convertir Páginas de PDF a Diferentes Formatos de Imagen (Facades)
- Convertir todas las páginas de PDF a Imágenes PNG
- [Leer Códigos de Barras](https://docs.aspose.com/barcode/net/barcode-recognition/)

{{% /alert %}}