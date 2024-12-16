---
title: Obtener Resolución y Dimensiones de Imágenes
linktitle: Obtener Resolución y Dimensiones
type: docs
weight: 40
url: /es/net/get-resolution-and-dimensions-of-embedded-images/
description: Esta sección muestra detalles sobre cómo obtener la resolución y dimensiones de Imágenes Incorporadas
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Obtener Resolución y Dimensiones de Imágenes",
    "alternativeHeadline": "Cómo obtener la Resolución y Dimensiones de Imágenes Incorporadas",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos pdf",
    "keywords": "pdf, c#, obtener resolución, obtener dimensiones",
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
    "url": "/net/get-resolution-and-dimensions-of-embedded-images/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/get-resolution-and-dimensions-of-embedded-images/"
    },
    "dateModified": "2022-02-04",
    "description": "Esta sección muestra detalles sobre cómo obtener la resolución y dimensiones de Imágenes Incorporadas"
}
</script>
El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

Este tema explica cómo utilizar las clases de operadores en el espacio de nombres Aspose.PDF, las cuales proporcionan la capacidad de obtener información sobre la resolución y dimensiones de las imágenes sin necesidad de extraerlas.

Hay diferentes maneras de lograr esto. Este artículo explica cómo usar un `arraylist` y [clases de colocación de imágenes](https://reference.aspose.com/pdf/net/aspose.pdf/imageplacement).

1. Primero, carga el archivo PDF fuente (con imágenes).
2. Luego crea un objeto ArrayList para contener los nombres de las imágenes en el documento.
3. Obtén las imágenes usando la propiedad Page.Resources.Images.
4. Crea un objeto de pila para mantener el estado gráfico de la imagen y úsalo para hacer seguimiento de los diferentes estados de la imagen.
5.
1. Debido a que podemos modificar la matriz con ConcatenateMatrix, también podemos necesitar revertir al estado original de la imagen. Utiliza los operadores GSave y GRestore. Estos operadores están emparejados, por lo que deben llamarse juntos. Por ejemplo, si realizas algún trabajo gráfico con transformaciones complejas y finalmente devuelves las transformaciones al estado inicial, el enfoque será algo así:

```csharp
// Dibuja algo de texto
GSave

ConcatenateMatrix  // rota el contenido después del operador

// Algun trabajo gráfico

ConcatenateMatrix // escala (con la rotación previa) el contenido después del operador

// Algun otro trabajo gráfico

GRestore

// Dibuja algo de texto
```

Como resultado, el texto se dibuja en forma regular pero se realizan algunas transformaciones entre los operadores de texto. Para mostrar la imagen o para dibujar objetos y imágenes de forma, necesitamos usar el operador Do.

También tenemos una clase llamada XImage que proporciona dos propiedades, Width y Height, que se pueden usar para obtener las dimensiones de la imagen.
1. Muestra la información en un símbolo del sistema junto con el nombre de la imagen.

El siguiente fragmento de código te muestra cómo obtener las dimensiones y la resolución de una imagen sin extraer la imagen del documento PDF.

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

// Carga el archivo PDF fuente
Document doc = new Document(dataDir+ "ImageInformation.pdf");

// Define la resolución predeterminada para la imagen
int defaultResolution = 72;
System.Collections.Stack graphicsState = new System.Collections.Stack();
// Define el objeto de lista de arreglo que mantendrá los nombres de las imágenes
System.Collections.ArrayList imageNames = new System.Collections.ArrayList(doc.Pages[1].Resources.Images.Names);
// Inserta un objeto en la pila
graphicsState.Push(new System.Drawing.Drawing2D.Matrix(1, 0, 0, 1, 0, 0));

// Obtén todos los operadores en la primera página del documento
foreach (Operator op in doc.Pages[1].Contents)
{
    // Usa los operadores GSave/GRestore para revertir las transformaciones al estado previamente establecido
    Aspose.Pdf.Operators.GSave opSaveState = op as Aspose.Pdf.Operators.GSave;
    Aspose.Pdf.Operators.GRestore opRestoreState = op as Aspose.Pdf.Operators.GRestore;
    // Instancia el objeto ConcatenateMatrix ya que define la matriz de transformación actual.
    Aspose.Pdf.Operators.ConcatenateMatrix opCtm = op as Aspose.Pdf.Operators.ConcatenateMatrix;
    // Crea el operador Do que dibuja objetos de los recursos. Dibuja objetos Form e imágenes
    Aspose.Pdf.Operators.Do opDo = op as Aspose.Pdf.Operators.Do;

    if (opSaveState != null)
    {
        // Guarda el estado anterior y empuja el estado actual al tope de la pila
        graphicsState.Push(((System.Drawing.Drawing2D.Matrix)graphicsState.Peek()).Clone());
    }
    else if (opRestoreState != null)
    {
        // Descarta el estado actual y restaura el anterior
        graphicsState.Pop();
    }
    else if (opCtm != null)
    {
        System.Drawing.Drawing2D.Matrix cm = new System.Drawing.Drawing2D.Matrix(
           (float)opCtm.Matrix.A,
           (float)opCtm.Matrix.B,
           (float)opCtm.Matrix.C,
           (float)opCtm.Matrix.D,
           (float)opCtm.Matrix.E,
           (float)opCtm.Matrix.F);

        // Multiplica la matriz actual con la matriz de estado
        ((System.Drawing.Drawing2D.Matrix)graphicsState.Peek()).Multiply(cm);

        continue;
    }
    else if (opDo != null)
    {
        // En caso de que este sea un operador de dibujo de imagen
        if (imageNames.Contains(opDo.Name))
        {
            System.Drawing.Drawing2D.Matrix lastCTM = (System.Drawing.Drawing2D.Matrix)graphicsState.Peek();
            // Crea el objeto XImage para contener imágenes de la primera página del PDF
            XImage image = doc.Pages[1].Resources.Images[opDo.Name];

            // Obtiene las dimensiones de la imagen
            double scaledWidth = Math.Sqrt(Math.Pow(lastCTM.Elements[0], 2) + Math.Pow(lastCTM.Elements[1], 2));
            double scaledHeight = Math.Sqrt(Math.Pow(lastCTM.Elements[2], 2) + Math.Pow(lastCTM.Elements[3], 2));
            // Obtiene la información de altura y anchura de la imagen
            double originalWidth = image.Width;
            double originalHeight = image.Height;

            // Calcula la resolución basada en la información anterior
            double resHorizontal = originalWidth * defaultResolution / scaledWidth;
            double resVertical = originalHeight * defaultResolution / scaledHeight;

            // Muestra la información de dimensiones y resolución de cada imagen
            Console.Out.WriteLine(
                    string.Format(dataDir + "imagen {0} ({1:.##}:{2:.##}): res {3:.##} x {4:.##}",
                                 opDo.Name, scaledWidth, scaledHeight, resHorizontal,
                                 resVertical));
        }
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
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/destacado",
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

