---
title: Agregar Imágenes y Texto
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /es/net/adding-images-and-text-using-pdffilemend-class/
description: Esta sección explica cómo agregar imágenes y texto utilizando la clase PdfFileMend.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adding Images and Text",
    "alternativeHeadline": "Enhance PDF by Adding Images and Text Precisely",
    "abstract": "Mejora tus documentos PDF sin esfuerzo con la nueva clase PdfFileMend, que te permite agregar imágenes y texto en ubicaciones específicas dentro de PDFs existentes. Utiliza los métodos intuitivos AddImage y AddText para integrar varios formatos de imagen y texto formateado sin problemas, asegurando precisión en la colocación y selección de páginas. Agiliza tus tareas de manipulación de PDF con la capacidad de personalizar superposiciones de imágenes y ajuste de texto, haciendo que tus documentos sean visualmente atractivos e informativos.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1324",
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
    "url": "/net/adding-images-and-text-using-pdffilemend-class/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/adding-images-and-text-using-pdffilemend-class/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también hacer frente a objetivos más complejos. Consulta la siguiente sección para usuarios avanzados y desarrolladores."
}
</script>

La clase [PdfFileMend](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilemend) puede ayudarte a agregar imágenes y texto en un documento PDF existente, en una ubicación específica. Proporciona dos métodos con los nombres [AddImage](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) y [AddText](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilemend/methods/addtext/index). El método [AddImage](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) te permite agregar imágenes de tipo JPG, GIF, PNG y BMP. El método [AddText](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilemend/methods/addtext/index) toma un argumento de tipo [FormattedText](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/formattedtext) y lo agrega en el archivo PDF existente. Las imágenes y el texto se pueden agregar en una región rectangular especificada por las coordenadas de los puntos inferior izquierdo y superior derecho. Al agregar imágenes, puedes especificar ya sea la ruta del archivo de imagen o un flujo de un archivo de imagen. Para especificar el número de página en la que se necesita agregar la imagen o el texto, ambos métodos proporcionan un argumento de número de página. Así que no solo puedes agregar las imágenes y el texto en la ubicación especificada, sino también en una página específica.

Las imágenes son una parte importante del contenido de un documento PDF. Manipular imágenes en un archivo PDF existente es un requisito común para las personas que trabajan con archivos PDF. En este artículo, exploraremos cómo se pueden manipular las imágenes en un archivo PDF existente, con la ayuda del [espacio de nombres Aspose.Pdf.Facades](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades) de [Aspose.PDF for .NET](/pdf/es/net/). Todas las operaciones relacionadas con imágenes del [espacio de nombres Aspose.Pdf.Facades](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades) se han consolidado en este artículo.

## Detalles de implementación

El [espacio de nombres Aspose.Pdf.Facades](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades) te permite agregar nuevas imágenes en un archivo PDF existente. También puedes reemplazar o eliminar una imagen existente. Un archivo PDF también se puede convertir a imágenes. Puedes convertir cada página individual en una sola imagen o un archivo PDF completo en una imagen. Permite formatos como JPEG, BMP, PNG y TIFF, etc. También puedes extraer las imágenes de un archivo PDF. Puedes usar cuatro clases del [espacio de nombres Aspose.Pdf.Facades](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades) para implementar estas operaciones, es decir, [PdfFileMend](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilemend), [PdfContentEditor](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdfcontenteditor), [PdfExtractor](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdfextractor) y [PdfConverter](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdfconverter).

## Operaciones de imagen

En esta sección, echaremos un vistazo detallado a estas operaciones de imagen. También veremos fragmentos de código para mostrar el uso de las clases y métodos relacionados. Primero, echemos un vistazo a cómo agregar una imagen en un archivo PDF existente. Podemos usar el método [AddImage](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) de la clase [PdfFileMend](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilemend) para agregar una nueva imagen. Usando este método, no solo puedes especificar el número de página en la que deseas agregar la imagen, sino que también se puede especificar la ubicación de la imagen.

## Agregar Imagen en un Archivo PDF Existente (Facades)

Puedes usar el método [AddImage](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilemend/methods/addimage) de la clase [PdfFileMend](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilemend). El método [AddImage](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilemend/methods/addimage) requiere la imagen que se va a agregar, el número de página en la que se necesita agregar la imagen y la información de coordenadas. Después de eso, guarda el archivo PDF actualizado usando el método [Close](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdfcontenteditor/methods/close).

En el siguiente ejemplo, agregamos una imagen a la página usando imageStream:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImage01()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images(); 

    // Create PDF document and PdfFileMend objects
    using (var document = new Aspose.Pdf.Document(dataDir + "AddImage.pdf"))
    {
        using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
        {
            // Load image into stream
            using (var imageStream = File.OpenRead(dataDir + "AddImage.png"))
            {
                // Bind PDF document
                mender.BindPdf(document);

                // Add image to first page
                mender.AddImage(imageStream, 1, 10, 650, 110, 750);

                // Save PDF document
                mender.Save(dataDir + "AddImage_out.pdf");
            }
        }
    }
}
```

![Agregar Imagen](/pdf/es/net/images/add_image1.png)

Con la ayuda de [CompositingParameters](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades.pdffilemend/addimage/methods/1), podemos superponer una imagen sobre otra:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImage02()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document and PdfFileMend objects
    using (var document = new Aspose.Pdf.Document(dataDir + "AddImage.pdf"))
    {
        using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
        {
            // Load image into stream
            using (var imageStream = File.OpenRead(dataDir + "AddImage.png"))
            {
                // Bind PDF document
                mender.BindPdf(document);

                int pageNum = 1;
                int lowerLeftX = 10;
                int lowerLeftY = 650;
                int upperRightX = 110;
                int upperRightY = 750;

                // Use compositing parameters for the image
                var compositingParameters = new Aspose.Pdf.CompositingParameters(Aspose.Pdf.BlendMode.Multiply);

                mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

                // Save PDF document
                mender.Save(dataDir + "AddImage_out.pdf");
            }
        }
    }
}
```

![Agregar Imagen](/pdf/es/net/images/add_image2.png)

Hay varias formas de almacenar una imagen en un archivo PDF. Demostraremos una de ellas en el siguiente ejemplo:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImage03()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddImage.pdf"))
    {
        using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
        {
            // Load image into stream
            using (var imageStream = File.OpenRead(dataDir + "AddImage.png"))
            {
                // Bind PDF document
                mender.BindPdf(document);

                int pageNum = 1;
                int lowerLeftX = 10;
                int lowerLeftY = 650;
                int upperRightX = 110;
                int upperRightY = 750;

                // Use compositing parameters with BlendMode.Exclusion and ImageFilterType.Flate
                var compositingParameters = new Aspose.Pdf.CompositingParameters(
                    Aspose.Pdf.BlendMode.Exclusion,
                    Aspose.Pdf.ImageFilterType.Flate);

                mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

                // Save PDF document
                mender.Save(dataDir + "AddImage_out.pdf");
            }
        }
    }
}
```

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImage04()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddImage.pdf"))
    {
        using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
        {
            // Load image into stream
            using (var imageStream = File.OpenRead(dataDir + "AddImage.png"))
            {
                // Bind PDF document
                mender.BindPdf(document);

                int pageNum = 1;
                int lowerLeftX = 10;
                int lowerLeftY = 650;
                int upperRightX = 110;
                int upperRightY = 750;

                // Use compositing parameters with BlendMode.Multiply, ImageFilterType.Flate and false
                var compositingParameters = new Aspose.Pdf.CompositingParameters(
                    Aspose.Pdf.BlendMode.Multiply,
                    Aspose.Pdf.ImageFilterType.Flate,
                    false);

                mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

                // Save PDF document
                mender.Save(dataDir + "AddImage_outp.pdf");
            }
        }
    }
}
```

## Agregar Texto en un Archivo PDF Existente (facades)

Podemos agregar texto de varias maneras. Consideremos la primera. Tomamos el [FormattedText](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/formattedtext) y lo agregamos a la Página. Después, indicamos las coordenadas de la esquina inferior izquierda, y luego agregamos nuestro texto a la Página.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddText01()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileMend object
    using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
    {
        // Bind PDF document
        mender.BindPdf(dataDir + "AddImage.pdf");

        // Create formatted text
        var message = new Aspose.Pdf.Facades.FormattedText("Welcome to Aspose!");

        // Add text to the first page at position (10, 750)
        mender.AddText(message, 1, 10, 750);

        // Save PDF document
        mender.Save(dataDir + "AddText_out.pdf");
    }
}
```

Mira cómo se ve:

![Agregar Texto](/pdf/es/net/images/add_text.png)

La segunda forma de agregar [FormattedText](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/formattedtext). Además, indicamos un rectángulo en el que nuestro texto debe encajar.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddText02()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileMend object
    using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
    {
        // Bind PDF document
        mender.BindPdf(dataDir + "AddImage.pdf");

        // Create formatted text
        var message = new Aspose.Pdf.Facades.FormattedText("Welcome to Aspose! Welcome to Aspose!");

        // Add text to the first page at the specified position with wrapping
        mender.AddText(message, 1, 10, 700, 55, 810);

        // Set word wrapping mode to wrap by words
        mender.WrapMode = Aspose.Pdf.Facades.WordWrapMode.ByWords;

        // Save PDF document
        mender.Save(dataDir + "AddText_out.pdf");
    }
}
```

El tercer ejemplo proporciona la capacidad de agregar texto a páginas específicas. En nuestro ejemplo, agreguemos un pie de foto en las páginas 1 y 3 del documento.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddText03()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddImage.pdf"))
    {
        document.Pages.Add();
        document.Pages.Add();
        document.Pages.Add();

        // Create PdfFileMend object
        using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
        {
            // Bind PDF document
            mender.BindPdf(document);

            // Create formatted text
            var message = new Aspose.Pdf.Facades.FormattedText("Welcome to Aspose!");

            // Specify the pages where text should be added
            int[] pageNums = new int[] { 1, 3 };

            // Add text to the specified pages at the specified coordinates
            mender.AddText(message, pageNums, 10, 750, 310, 760);

            // Save PDF document
            mender.Save(dataDir + "AddText_out.pdf");
        }
    }
}
```