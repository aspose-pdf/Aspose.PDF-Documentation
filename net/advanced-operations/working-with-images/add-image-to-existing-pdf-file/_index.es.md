---
title: Añadir imagen a PDF usando C#
linktitle: Añadir imagen
type: docs
weight: 10
url: /net/add-image-to-existing-pdf-file/
description: Esta sección describe cómo añadir una imagen a un archivo PDF existente usando la biblioteca C#.
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Añadir imagen a PDF usando C#",
    "alternativeHeadline": "Cómo añadir imagen a PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, c#, añadir imagen a pdf",
    "wordcount": "302",
    "proficiencyLevel":"Principiante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipo de Documentación de Aspose.PDF",
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
    "url": "/net/add-image-to-existing-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-image-to-existing-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "Esta sección describe cómo añadir una imagen a un archivo PDF existente usando la biblioteca C#."
}
</script>

## Agregar Imagen en un Archivo PDF Existente

Cada página de PDF contiene propiedades de Recursos y Contenidos. Los recursos pueden ser imágenes y formularios, por ejemplo, mientras que el contenido está representado por un conjunto de operadores PDF. Cada operador tiene su nombre y argumento. Este ejemplo utiliza operadores para agregar una imagen a un archivo PDF.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

Para agregar una imagen a un archivo PDF existente:

- Crear un objeto Document y abrir el documento PDF de entrada.
- Obtener la página a la que desea agregar una imagen.
- Añadir la imagen a la colección de Recursos de la página.
- Usar operadores para colocar la imagen en la página:
  - Usar el operador GSave para guardar el estado gráfico actual.
  - Usar el operador ConcatenateMatrix para especificar dónde se debe colocar la imagen.
  - Usar el operador Do para dibujar la imagen en la página.
  - Finalmente, usar el operador GRestore para guardar el estado gráfico actualizado.
- Guardar el archivo.
El siguiente fragmento de código muestra cómo agregar la imagen en un documento PDF.

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

// Abrir documento
Document pdfDocument = new Document(dataDir+ "AddImage.pdf");

// Establecer coordenadas
int lowerLeftX = 100;
int lowerLeftY = 100;
int upperRightX = 200;
int upperRightY = 200;

// Obtener la página donde se necesita agregar la imagen
Page page = pdfDocument.Pages[1];
// Cargar imagen en stream
FileStream imageStream = new FileStream(dataDir + "aspose-logo.jpg", FileMode.Open);
// Añadir imagen a la colección de Imágenes de los Recursos de la Página
page.Resources.Images.Add(imageStream);
// Usando el operador GSave: este operador guarda el estado gráfico actual
page.Contents.Add(new Aspose.Pdf.Operators.GSave());
// Crear objetos Rectángulo y Matriz
Aspose.Pdf.Rectangle rectangle = new Aspose.Pdf.Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
Matrix matrix = new Matrix(new double[] { rectangle.URX - rectangle.LLX, 0, 0, rectangle.URY - rectangle.LLY, rectangle.LLX, rectangle.LLY });
// Usando el operador ConcatenateMatrix (concatenar matriz): define cómo se debe colocar la imagen
page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(matrix));
XImage ximage = page.Resources.Images[page.Resources.Images.Count];
// Usando el operador Do: este operador dibuja la imagen
page.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));
// Usando el operador GRestore: este operador restaura el estado gráfico
page.Contents.Add(new Aspose.Pdf.Operators.GRestore());
dataDir = dataDir + "AddImage_out.pdf";
// Guardar el documento actualizado
pdfDocument.Save(dataDir);
```
{{% alert color="primary" %}}

Por defecto, la calidad de JPEG está establecida al 100%. Para aplicar una mejor compresión y calidad, utiliza las siguientes sobrecargas:

{{% /alert %}}

- se añade la sobrecarga del método Replace en la clase XImageCollection: public void Replace(int index, Stream stream, int quality)
- se añade la sobrecarga del método Add en la clase XImageCollection: public void Add(Stream stream, int quality)

## Añadir Imagen en un Archivo PDF Existente (Facades)

También existe una manera alternativa y más fácil de añadir una imagen a un archivo PDF.
Existe también una alternativa más sencilla para añadir una imagen a un archivo PDF.

```csharp
string imageFileName = Path.Combine(_dataDir, "Images", "Sample-01.jpg");
string outputPdfFileName = Path.Combine(_dataDir, "Example-add-image-mender.pdf");
Document document = new Document();
Page page = document.Pages.Add();
page.SetPageSize(PageSize.A3.Height, PageSize.A3.Width);
page = document.Pages.Add();
Aspose.Pdf.Facades.PdfFileMend mender = new Aspose.Pdf.Facades.PdfFileMend(document);
mender.AddImage(imageFileName, 1, 0, 0, (float)page.CropBox.Width, (float)page.CropBox.Height);
document.Save(outputPdfFileName);
```

## Colocar imagen en la página y conservar (controlar) la relación de aspecto

Si no conocemos las dimensiones de la imagen, existe una gran posibilidad de obtener una imagen distorsionada en la página. El siguiente ejemplo muestra una de las formas de evitarlo.

```csharp
public static void AddingImageAndPreserveAspectRatioIntoPDF()
{
    var bitmap = System.Drawing.Image.FromFile(_dataDir + "3410492.jpg");

    int width;
    int height;

    width = bitmap.Width;
    height = bitmap.Height;

    var document = new Aspose.Pdf.Document();

    var page = document.Pages.Add();

    int scaledWidth = 400;
    int scaledHeight = scaledWidth * height / width;

    page.AddImage(_dataDir + "3410492.jpg", new Aspose.Pdf.Rectangle(10, 10, scaledWidth, scaledHeight));
    document.Save(_dataDir + "sample_image.pdf");
}
```
## Identificar si la imagen dentro del PDF es a Color o Blanco y Negro

Diferentes tipos de compresión se pueden aplicar sobre las imágenes para reducir su tamaño. El tipo de compresión que se aplica sobre una imagen depende del Espacio de Color de la imagen fuente, es decir, si la imagen es a Color (RGB), entonces se debe aplicar la compresión JPEG2000, y si es Blanco y Negro, entonces se debe aplicar la compresión JBIG2/JBIG2000. Por lo tanto, identificar cada tipo de imagen y usar un tipo de compresión apropiado creará una salida mejor/optimizada.

Un archivo PDF puede contener elementos de Texto, Imagen, Gráfico, Adjunto, Anotación, etc., y si el archivo PDF fuente contiene imágenes, podemos determinar el espacio de color de la imagen y aplicar la compresión apropiada para reducir el tamaño del archivo PDF. El siguiente fragmento de código muestra los pasos para identificar si la imagen dentro del PDF es a Color o Blanco y Negro.

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// El camino al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

// Contador para imágenes en escala de grises
int grayscaled = 0;
// Contador para imágenes RGB
int rgd = 0;

using (Document document = new Document(dataDir + "ExtractImages.pdf"))
{
    foreach (Page page in document.Pages)
    {
        Console.WriteLine("--------------------------------");
        ImagePlacementAbsorber abs = new ImagePlacementAbsorber();
        page.Accept(abs);
        // Obtener el conteo de imágenes en una página específica
        Console.WriteLine("Total de Imágenes = {0} en la página número {1}", abs.ImagePlacements.Count, page.Number);
        // Document.Pages[29].Accept(abs);
        int image_counter = 1;
        foreach (ImagePlacement ia in abs.ImagePlacements)
        {
            ColorType colorType = ia.Image.GetColorType();
            switch (colorType)
            {
                case ColorType.Grayscale:
                    ++grayscaled;
                    Console.WriteLine("Imagen {0} es Escala de Grises...", image_counter);
                    break;
                case ColorType.Rgb:
                    ++rgd;
                    Console.WriteLine("Imagen {0} es RGB...", image_counter);
                    break;
            }
            image_counter += 1;
        }
    }
}
```
## Controlar la Calidad de la Imagen

Es posible controlar la calidad de una imagen que se está añadiendo a un archivo PDF. Utiliza el método [Replace](https://reference.aspose.com/pdf/net/aspose.pdf.ximagecollection/replace/methods/1) sobrecargado en la clase [XImageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/ximagecollection).

El siguiente fragmento de código demuestra cómo convertir todas las imágenes del documento en JPEGs que usan un 80% de calidad para la compresión.

```csharp
Aspose.PDF.Document pdfDocument = new Aspose.PDF.Document(inFile);
foreach (Aspose.PDF.Page page in pdfDocument.Pages)
{
    int idx = 1;
    foreach (Aspose.PDF.XImage image in page.Resources.Images)
    {
        using (MemoryStream imageStream = new MemoryStream())
        {
            image.Save(imageStream, System.Drawing.Imaging.ImageFormat.Jpeg);
            page.Resources.Images.Replace(idx, imageStream, 80);
            idx = idx + 1;
        }
    }
}

// pdfDocument.OptimizeResources();

pdfDocument.Save(outFile);
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Biblioteca Aspose.PDF para .NET",
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
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/destacados",
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
    "screenshot": "https://docs.aspose.com/pdf/net/crear-documento-pdf/captura-de-pantalla.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
```

