---
title: Trabajando con Operadores
linktitle: Trabajando con Operadores
type: docs
weight: 170
url: /es/net/operators/
description: Este tema explica cómo usar operadores con Aspose.PDF. Las clases de operadores ofrecen excelentes características para la manipulación de PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Trabajando con Operadores",
    "alternativeHeadline": "Cómo usar operadores en PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, c#, operadores en pdf, usar operadores de pdf",
    "wordcount": "302",
    "proficiencyLevel":"Principiante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipo Documental de Aspose.PDF",
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
                "contactType": "ventas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "ventas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventas",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/operators/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/operators/"
    },
    "dateModified": "2022-02-04",
    "description": "Este tema explica cómo usar operadores con Aspose.PDF. Las clases de operadores ofrecen excelentes características para la manipulación de PDF."
}
</script>

## Introducción a los operadores PDF y su uso

Un operador es una palabra clave de PDF que especifica alguna acción que debe realizarse, como pintar una forma gráfica en la página. Una palabra clave de operador se distingue de un objeto nombrado por la ausencia de un carácter inicial sólido (2Fh). Los operadores solo tienen sentido dentro del flujo de contenido.

Un flujo de contenido es un objeto de flujo PDF cuyos datos constan de instrucciones que describen los elementos gráficos que se pintarán en una página. Puede encontrar más detalles sobre los operadores PDF en la [especificación PDF](https://opensource.adobe.com/dc-acrobat-sdk-docs/).

### Detalles de implementación

Este tema explica cómo usar operadores con Aspose.PDF.
Este tema explica cómo usar operadores con Aspose.PDF.

- El operador **GSave** guarda el estado gráfico actual del PDF.
- El operador **ConcatenateMatrix** (concatenar matriz) se utiliza para definir cómo se debe colocar una imagen en la página del PDF.
- El operador **Do** dibuja la imagen en la página.
- El operador **GRestore** restaura el estado gráfico.

Para añadir una imagen en un archivo PDF:

1. Crea un objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) y abre el documento PDF de entrada.
1. Obtén la página específica donde se añadirá la imagen.
1. Añade la imagen en la colección de Recursos de la página.
1. Utiliza los operadores para colocar la imagen en la página:
   - Primero, usa el operador GSave para guardar el estado gráfico actual.
   - Luego usa el operador ConcatenateMatrix para especificar dónde se debe colocar la imagen.
   - Usa el operador Do para dibujar la imagen en la página.
1. Finalmente, usa el operador GRestore para guardar el estado gráfico actualizado.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).
El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

El siguiente fragmento de código muestra cómo usar operadores PDF.

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Operators();

// Abrir documento
Document pdfDocument = new Document(dataDir+ "PDFOperators.pdf");

// Establecer coordenadas
int lowerLeftX = 100;
int lowerLeftY = 100;
int upperRightX = 200;
int upperRightY = 200;

// Obtener la página donde se necesita agregar la imagen
Page page = pdfDocument.Pages[1];
// Cargar imagen en el flujo
FileStream imageStream = new FileStream(dataDir + "PDFOperators.jpg", FileMode.Open);
// Agregar imagen a la colección de Imágenes de Recursos de Página
page.Resources.Images.Add(imageStream);
// Usando el operador GSave: este operador guarda el estado gráfico actual
page.Contents.Add(new Aspose.Pdf.Operators.GSave());
// Crear objetos Rectángulo y Matriz
Aspose.Pdf.Rectangle rectangle = new Aspose.Pdf.Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
Matrix matrix = new Matrix(new double[] { rectangle.URX - rectangle.LLX, 0, 0, rectangle.URY - rectangle.LLY, rectangle.LLX, rectangle.LLY });
// Usando el operador ConcatenateMatrix (concatenar matriz): define cómo debe colocarse la imagen
page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(matrix));
XImage ximage = page.Resources.Images[page.Resources.Images.Count];
// Usando el operador Do: este operador dibuja la imagen
page.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));
// Usando el operador GRestore: este operador restaura el estado gráfico
page.Contents.Add(new Aspose.Pdf.Operators.GRestore());
dataDir = dataDir + "PDFOperators_out.pdf";
// Guardar documento actualizado
pdfDocument.Save(dataDir);
```
## Dibujar XForm en la Página Usando Operadores

Este tema demuestra cómo usar los operadores GSave/GRestore, el operador ContatenateMatrix para posicionar un xForm y el operador Do para dibujar un xForm en una página.

El código a continuación envuelve los contenidos existentes de un archivo PDF con el par de operadores GSave/GRestore. Este enfoque ayuda a obtener el estado gráfico inicial al final de los contenidos existentes. Sin este enfoque, podrían permanecer transformaciones indeseables al final de la cadena de operadores existente.

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Operators();


string imageFile = dataDir+ "aspose-logo.jpg";
string inFile = dataDir + "DrawXFormOnPage.pdf";
string outFile = dataDir + "blank-sample2_out.pdf";

using (Document doc = new Document(inFile))
{
    OperatorCollection pageContents = doc.Pages[1].Contents;

    // El ejemplo demuestra
    // el uso de operadores GSave/GRestore
    // el uso del operador ContatenateMatrix para posicionar xForm
    // el uso del operador Do para dibujar xForm en la página

    // Envolver los contenidos existentes con el par de operadores GSave/GRestore
    //        esto es para obtener el estado gráfico inicial al final de los contenidos existentes
    //        de lo contrario, podrían permanecer algunas transformaciones indeseables al final de la cadena de operadores existente
    pageContents.Insert(1, new Aspose.Pdf.Operators.GSave());
    pageContents.Add(new Aspose.Pdf.Operators.GRestore());

    // Agregar operador de guardar estado gráfico para limpiar adecuadamente el estado gráfico después de nuevos comandos
    pageContents.Add(new Aspose.Pdf.Operators.GSave());

    #region crear xForm

    // Crear xForm
    XForm form = XForm.CreateNewForm(doc.Pages[1], doc);
    doc.Pages[1].Resources.Forms.Add(form);
    form.Contents.Add(new Aspose.Pdf.Operators.GSave());
    // Definir ancho y alto de la imagen
    form.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(200, 0, 0, 200, 0, 0));
    // Cargar imagen en el flujo
    Stream imageStream = new FileStream(imageFile, FileMode.Open);
    // Añadir imagen a la colección de Imágenes de los Recursos de XForm
    form.Resources.Images.Add(imageStream);
    XImage ximage = form.Resources.Images[form.Resources.Images.Count];
    // Usando el operador Do: este operador dibuja la imagen
    form.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));
    form.Contents.Add(new Aspose.Pdf.Operators.GRestore());

    #endregion

    pageContents.Add(new Aspose.Pdf.Operators.GSave());
    // Colocar el formulario en las coordenadas x=100 y=500
    pageContents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(1, 0, 0, 1, 100, 500));
    // Dibujar formulario con el operador Do
    pageContents.Add(new Aspose.Pdf.Operators.Do(form.Name));
    pageContents.Add(new Aspose.Pdf.Operators.GRestore());

    pageContents.Add(new Aspose.Pdf.Operators.GSave());
    // Colocar el formulario en las coordenadas x=100 y=300
    pageContents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(1, 0, 0, 1, 100, 300));
    // Dibujar formulario con el operador Do
    pageContents.Add(new Aspose.Pdf.Operators.Do(form.Name));
    pageContents.Add(new Aspose.Pdf.Operators.GRestore());

    // Restaurar el estado gráfico con GRestore después del GSave
    pageContents.Add(new Aspose.Pdf.Operators.GRestore());
    doc.Save(outFile);
}
```
## Eliminar Objetos Gráficos usando Clases de Operadores

Las clases de operadores proporcionan excelentes características para la manipulación de archivos PDF. Cuando un archivo PDF contiene gráficos que no pueden ser eliminados utilizando el método [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/deleteimage) de la clase [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor), las clases de operadores pueden usarse para eliminarlos en su lugar.

El siguiente fragmento de código muestra cómo eliminar gráficos. Tenga en cuenta que si el archivo PDF contiene etiquetas de texto para los gráficos, estas podrían persistir en el archivo PDF al usar este enfoque. Por lo tanto, busque en los operadores gráficos un método alternativo para eliminar dichas imágenes.

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Operators();

Document doc = new Document(dataDir+ "RemoveGraphicsObjects.pdf");
Page page = doc.Pages[2];
OperatorCollection oc = page.Contents;

// Operadores de pintura de caminos utilizados
Operator[] operators = new Operator[] {
        new Aspose.Pdf.Operators.Stroke(),
        new Aspose.Pdf.Operators.ClosePathStroke(),
        new Aspose.Pdf.Operators.Fill()
};

oc.Delete(operators);
doc.Save(dataDir+ "No_Graphics_out.pdf");
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
                "contactType": "ventas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "ventas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventas",
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
    "applicationCategory": "Biblioteca de manipulación de PDF para .NET",
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
```
Por supuesto, me encantaría ayudarte a traducir tu documento al español manteniendo el formato markdown original. Sin embargo, necesitaría ver el contenido específico del documento para poder realizar la traducción. Por favor, proporciona el texto que necesitas traducir.
