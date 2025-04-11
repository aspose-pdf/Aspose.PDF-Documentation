---
title: Trabajando con Operadores
linktitle: Trabajando con Operadores
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 90
url: /es/net/working-with-operators/
description: Este tema explica cómo usar operadores con Aspose.PDF. Las clases de operadores proporcionan grandes características para la manipulación de PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Operators",
    "alternativeHeadline": "Empowered PDF Manipulation with Operators Integration",
    "abstract": "La función de Operadores en Aspose.PDF for .NET mejora las capacidades de manipulación de PDF al permitir a los usuarios utilizar clases de operadores específicas para tareas como agregar imágenes y eliminar gráficos. Esta funcionalidad simplifica el proceso de definir elementos gráficos y sus estados dentro de un PDF, proporcionando a los desarrolladores herramientas poderosas para la edición y procesamiento de documentos.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "operators, Aspose.PDF, PDF manipulation, GSave operator, ConcatenateMatrix operator, Do operator, GRestore operator, graphics state, remove graphics",
    "wordcount": "1233",
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
    "url": "/net/working-with-operators/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-operators/"
    },
    "dateModified": "2024-11-26",
    "description": "Este tema explica cómo usar operadores con Aspose.PDF. Las clases de operadores proporcionan grandes características para la manipulación de PDF."
}
</script>

## Introducción a los Operadores PDF y su Uso

Un operador es una palabra clave PDF que especifica alguna acción que se debe realizar, como pintar una forma gráfica en la página. Una palabra clave de operador se distingue de un objeto nombrado por la ausencia de un carácter de barra sólida inicial (2Fh). Los operadores solo tienen significado dentro del flujo de contenido.

Un flujo de contenido es un objeto de flujo PDF cuyos datos consisten en instrucciones que describen los elementos gráficos que se deben pintar en una página. Se pueden encontrar más detalles sobre los operadores PDF en la [especificación PDF](https://opensource.adobe.com/dc-acrobat-sdk-docs/).

### Detalles de implementación

Este tema explica cómo usar operadores con Aspose.PDF. El ejemplo seleccionado agrega una imagen a un archivo PDF para ilustrar el concepto. Para agregar una imagen en un archivo PDF, se necesitan diferentes operadores. Este ejemplo utiliza [GSave](https://reference.aspose.com/pdf/es/net/aspose.pdf.ioperatorselector/visit/methods/28), [ConcatenateMatrix](https://reference.aspose.com/pdf/es/net/aspose.pdf.ioperatorselector/visit/methods/10), [Do](https://reference.aspose.com/pdf/es/net/aspose.pdf.ioperatorselector/visit/methods/14) y [GRestore](https://reference.aspose.com/pdf/es/net/aspose.pdf.ioperatorselector/visit/methods/26).

- El operador **GSave** guarda el estado gráfico actual del PDF.
- El operador **ConcatenateMatrix** (matriz de concatenación) se utiliza para definir cómo se debe colocar una imagen en la página PDF.
- El operador **Do** dibuja la imagen en la página.
- El operador **GRestore** restaura el estado gráfico.

Para agregar una imagen a un archivo PDF:

1. Cree un objeto [Document](https://reference.aspose.com/pdf/es/net/aspose.pdf/document) y abra el documento PDF de entrada.
1. Obtenga la página particular a la que se va a agregar la imagen.
1. Agregue la imagen a la colección de Recursos de la página.
1. Use los operadores para colocar la imagen en la página:
   - Primero, use el operador GSave para guardar el estado gráfico actual.
   - Luego use el operador ConcatenateMatrix para especificar dónde se debe colocar la imagen.
   - Use el operador Do para dibujar la imagen en la página.
1. Finalmente, use el operador GRestore para guardar el estado gráfico actualizado.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

El siguiente fragmento de código muestra cómo usar operadores PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageUsingPDFOperators()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFOperators.pdf"))
    {
        // Set coordinates for the image placement
        int lowerLeftX = 100;
        int lowerLeftY = 100;
        int upperRightX = 200;
        int upperRightY = 200;

        // Get the page where the image needs to be added
        var page = document.Pages[1];

        // Load the image into a file stream
        using (var imageStream = new FileStream(dataDir + "PDFOperators.jpg", FileMode.Open))
        {
            // Add the image to the page's Resources collection
            page.Resources.Images.Add(imageStream);
        }

        // Save the current graphics state using the GSave operator
        page.Contents.Add(new Aspose.Pdf.Operators.GSave());

        // Create a rectangle and matrix for positioning the image
        var rectangle = new Aspose.Pdf.Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
        var matrix = new Aspose.Pdf.Matrix(new double[]
        {
            rectangle.URX - rectangle.LLX, 0,
            0, rectangle.URY - rectangle.LLY,
            rectangle.LLX, rectangle.LLY
        });

        // Define how the image must be placed using the ConcatenateMatrix operator
        page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(matrix));

        // Get the image from the Resources collection
        var ximage = page.Resources.Images[page.Resources.Images.Count];

        // Draw the image using the Do operator
        page.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));

        // Restore the graphics state using the GRestore operator
        page.Contents.Add(new Aspose.Pdf.Operators.GRestore());

        // Save PDF document
        document.Save(dataDir + "PDFOperators_out.pdf");
    }
}
```

## Dibujar XForm en la Página usando Operadores

Este tema demuestra cómo usar los operadores GSave/GRestore, el operador ConcatenateMatrix para posicionar un xForm y el operador Do para dibujar un xForm en una página.

El código a continuación envuelve los contenidos existentes de un archivo PDF con el par de operadores GSave/GRestore. Este enfoque ayuda a obtener el estado gráfico inicial al final de los contenidos existentes. Sin este enfoque, transformaciones indeseables podrían permanecer al final de la cadena de operadores existente.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DrawXFormOnPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DrawXFormOnPage.pdf"))
    {
        var pageContents = document.Pages[1].Contents;

        // Wrap existing contents with GSave/GRestore operators to preserve graphics state
        pageContents.Insert(1, new Aspose.Pdf.Operators.GSave());
        pageContents.Add(new Aspose.Pdf.Operators.GRestore());

        // Add GSave operator to start new graphics state
        pageContents.Add(new Aspose.Pdf.Operators.GSave());

        // Create an XForm
        var form = Aspose.Pdf.XForm.CreateNewForm(document.Pages[1], document);
        document.Pages[1].Resources.Forms.Add(form);

        form.Contents.Add(new Aspose.Pdf.Operators.GSave());
        // Define image width and height
        form.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(200, 0, 0, 200, 0, 0));

        // Load image into stream
        using (var imageStream = new FileStream(dataDir + "aspose-logo.jpg", FileMode.Open))
        {
            // Add the image to the XForm's resources
            form.Resources.Images.Add(imageStream);
        }

        var ximage = form.Resources.Images[form.Resources.Images.Count];
        // Draw the image on the XForm
        form.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));
        form.Contents.Add(new Aspose.Pdf.Operators.GRestore());

        // Place and draw the XForm at two different coordinates

        // Draw the XForm at (100, 500)
        pageContents.Add(new Aspose.Pdf.Operators.GSave());
        pageContents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(1, 0, 0, 1, 100, 500));
        pageContents.Add(new Aspose.Pdf.Operators.Do(form.Name));
        pageContents.Add(new Aspose.Pdf.Operators.GRestore());

        // Draw the XForm at (100, 300)
        pageContents.Add(new Aspose.Pdf.Operators.GSave());
        pageContents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(1, 0, 0, 1, 100, 300));
        pageContents.Add(new Aspose.Pdf.Operators.Do(form.Name));
        pageContents.Add(new Aspose.Pdf.Operators.GRestore());

        // Restore graphics state
        pageContents.Add(new Aspose.Pdf.Operators.GRestore());

        // Save PDF document
        document.Save(dataDir + "DrawXFormOnPage_out.pdf");
    }
}
```

## Eliminar Objetos Gráficos usando Clases de Operadores

Las clases de operadores proporcionan grandes características para la manipulación de PDF. Cuando un archivo PDF contiene gráficos que no se pueden eliminar utilizando el método [DeleteImage](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdfcontenteditor/methods/deleteimage) de la clase [PdfContentEditor](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdfcontenteditor), se pueden usar las clases de operadores para eliminarlos en su lugar.

El siguiente fragmento de código muestra cómo eliminar gráficos. Tenga en cuenta que si el archivo PDF contiene etiquetas de texto para los gráficos, pueden persistir en el archivo PDF utilizando este enfoque. Por lo tanto, busque los operadores gráficos para un método alternativo para eliminar tales imágenes.

```csharp
  // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
  private static void RemoveGraphicsObjects()
  {
      // The path to the documents directory
      var dataDir = RunExamples.GetDataDir_AsposePdf();

      // Open PDF document
      using (var document = new Aspose.Pdf.Document(dataDir + "RemoveGraphicsObjects.pdf"))
      {
          // Get the specific page (page 2 in this case)
          var page = document.Pages[2];

          // Get the operator collection from the page contents
          var oc = page.Contents;

          // Define the path-painting operators to be removed
          var operators = new Aspose.Pdf.Operator[]
          {
              new Aspose.Pdf.Operators.Stroke(),
              new Aspose.Pdf.Operators.ClosePathStroke(),
              new Aspose.Pdf.Operators.Fill()
          };

          // Delete the specified operators from the page contents
          oc.Delete(operators);

          // Save PDF document
          document.Save(dataDir + "NoGraphics_out.pdf");
      }
  }
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
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