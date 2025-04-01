---
title: Optimizar, Comprimir o Reducir el Tamaño de PDF en C#
linktitle: Optimizar PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /es/net/optimize-pdf/
description: Optimizar archivo PDF, reducir el tamaño de PDF, desincrustar fuentes, eliminar objetos no utilizados con C#.
lastmod: "2022-02-17"
sitemap:
changefreq: "monthly"
priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Optimize, Compress or Reduce PDF Size in C#",
    "alternativeHeadline": "Optimize PDF Files Efficiently with C#",
    "abstract": "La nueva función de optimización de PDF en C# permite a los desarrolladores reducir significativamente el tamaño de los archivos PDF empleando múltiples estrategias, como comprimir imágenes, desincrustar fuentes y eliminar objetos no utilizados. Esta mejora aumenta la eficiencia para la publicación web, el intercambio por correo electrónico y el almacenamiento, proporcionando una solución efectiva para gestionar documentos PDF grandes.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "optimize pdf, compress pdf size, reduce pdf size, optimize pdf c#, unembed fonts, remove unused objects, shrink images, optimization methods, pdf document generation, Aspose.PDF",
    "wordcount": "2894",
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
    "url": "/net/optimize-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/optimize-pdf/"
    },
    "dateModified": "2025-04-01",
    "description": "Optimizar archivo PDF, reducir el tamaño de PDF, desincrustar fuentes, eliminar objetos no utilizados con C#."
}
</script>

Un documento PDF puede contener a veces datos adicionales. Reducir el tamaño de un archivo PDF te ayudará a optimizar la transferencia de red y el almacenamiento. Esto es especialmente útil para la publicación en páginas web, el intercambio en redes sociales, el envío por correo electrónico o el archivo en almacenamiento. Podemos utilizar varias técnicas para optimizar PDF:

- Optimizar el contenido de la página para la navegación en línea.
- Reducir o comprimir todas las imágenes.
- Permitir la reutilización del contenido de la página.
- Fusionar flujos duplicados.
- Desincrustar fuentes.
- Eliminar objetos no utilizados.
- Eliminar campos de formulario aplanados.
- Eliminar o aplanar anotaciones.

{{% alert color="primary" %}}

La explicación detallada de los métodos de optimización se puede encontrar en la página de Visión General de Métodos de Optimización.

{{% /alert %}}

## Optimizar Documento PDF para la Web

La optimización, o linealización para la Web, se refiere al proceso de hacer que un archivo PDF sea adecuado para la navegación en línea utilizando un navegador web. Para optimizar un archivo para la visualización web:

1. Abre el documento de entrada en un [Document](https://reference.aspose.com/pdf/es/net/aspose.pdf/document) objeto.
1. Utiliza el método [Optimize](https://reference.aspose.com/pdf/es/net/aspose.pdf/document/methods/optimize).
1. Guarda el documento optimizado utilizando el método [Save](https://reference.aspose.com/pdf/es/net/aspose.pdf/document/methods/save).

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

El siguiente fragmento de código muestra cómo optimizar un documento PDF para la web.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizeDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Optimize for web
        document.Optimize();

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");
    }
}
```

## Reducir Tamaño PDF

El método [OptimizeResources()](https://reference.aspose.com/pdf/es/net/aspose.pdf/document/methods/optimizeresources) te permite reducir el tamaño del documento eliminando la información innecesaria. Por defecto, este método funciona de la siguiente manera:

- Los recursos que no se utilizan en las páginas del documento son eliminados.
- Los recursos iguales se unen en un solo objeto.
- Los objetos no utilizados son eliminados.

El fragmento a continuación es un ejemplo. Ten en cuenta, sin embargo, que este método no puede garantizar la reducción del documento.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ShrinkDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ShrinkDocument.pdf"))
    {
        // Optimize PDF document. Note, though, that this method cannot guarantee document shrinking
        document.OptimizeResources();

        // Save PDF document
        document.Save(dataDir + "ShrinkDocument_out.pdf");
    }
}
```

## Gestión de Estrategia de Optimización

También podemos personalizar la estrategia de optimización. Actualmente, el método [OptimizeResources()](https://reference.aspose.com/pdf/es/net/aspose.pdf.document/optimizeresources/methods/1) utiliza 5 técnicas. Estas técnicas se pueden aplicar utilizando el método OptimizeResources() con el parámetro [OptimizationOptions](https://reference.aspose.com/pdf/es/net/aspose.pdf.optimization/optimizationoptions).

### Reducir o Comprimir Todas las Imágenes

Tenemos dos formas de trabajar con imágenes: reducir la calidad de la imagen y/o cambiar su resolución. En cualquier caso, se deben aplicar [ImageCompressionOptions](https://reference.aspose.com/pdf/es/net/aspose.pdf.optimization/imagecompressionoptions). En el siguiente ejemplo, reducimos las imágenes al disminuir [ImageQuality](https://reference.aspose.com/pdf/es/net/aspose.pdf.optimization/imagecompressionoptions/properties/imagequality) a 50.

`ImageQuality` funciona de manera similar a la calidad JPEG, donde el valor 0 es el más bajo y el valor 100 es el más alto.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ShrinkImage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Shrinkimage.pdf"))
    {
        // Initialize OptimizationOptions
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions();

        // Set CompressImages option
        // If this flag is set to true images will be compressed in the document
        optimizeOptions.ImageCompressionOptions.CompressImages = true;

        // Set ImageQuality option
        // Specifies level of image compression when CompressImages flag is used
        optimizeOptions.ImageCompressionOptions.ImageQuality = 50;

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "Shrinkimage_out.pdf");
    }
}
```

Otra forma es cambiar el tamaño de las imágenes con una resolución más baja. En este caso, debemos establecer ResizeImages en verdadero y MaxResolution al valor apropiado.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ResizeImages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ResizeImage.pdf"))
    {
        // Initialize OptimizationOptions
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions();

        // Set CompressImages option
        // If this flag is set to true images will be compressed in the document
        optimizeOptions.ImageCompressionOptions.CompressImages = true;

        // Set ImageQuality option
        // Specifies level of image compression when CompressImages flag is used
        optimizeOptions.ImageCompressionOptions.ImageQuality = 75;

        // Set ResizeImage option
        // If this flag set to true and CompressImages is true images will be resized if image resoultion is greater then specified MaxResolution parameter
        optimizeOptions.ImageCompressionOptions.ResizeImages = true;

        // Set MaxResolution option
        // Specifies maximum resolution of images. If image has higher resolition it will be scaled
        optimizeOptions.ImageCompressionOptions.MaxResolution = 300;

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "ResizeImages_out.pdf");
    }
}
```

Otro tema importante es el tiempo de ejecución. Pero nuevamente, también podemos gestionar esta configuración. Actualmente, podemos utilizar dos algoritmos: Estándar y Rápido. Para controlar el tiempo de ejecución, debemos establecer una propiedad [Version](https://reference.aspose.com/pdf/es/net/aspose.pdf.optimization/imagecompressionoptions/properties/version). El siguiente fragmento demuestra el algoritmo Rápido:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FastShrinkImages()
{
    // Initialize Time
    var time = DateTime.Now.Ticks;

    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Shrinkimage.pdf"))
    {
        // Initialize OptimizationOptions
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions();

        // Set CompressImages option
        // If this flag is set to true images will be compressed in the document
        optimizeOptions.ImageCompressionOptions.CompressImages = true;

        // Set ImageQuality option
        // Specifies level of image compression when CompressImages flag is used
        optimizeOptions.ImageCompressionOptions.ImageQuality = 75;

        // Set Image Compression Version to fast
        // Version of compression algorithm. Possible values are:
        // 1. standard compression
        // 2. fast (improved compression which is faster then standard but may be applicable not for all images)
        // 3. mixed (standard compression is applied to images which can not be compressed by faster algorithm, 
        // this may give best compression but more slow then "fast" algorithm. Version "Fast" is not applicable for 
        // resizing images (standard method will be used). Default is "Standard"
        optimizeOptions.ImageCompressionOptions.Version = Aspose.Pdf.Optimization.ImageCompressionVersion.Fast;

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "FastShrinkImages_out.pdf");
    }

    // Output the time taken for the operation
    Console.WriteLine("Ticks: {0}", DateTime.Now.Ticks - time);
}
```

### Eliminación de Objetos No Utilizados

Un documento PDF a veces contiene objetos PDF que no están referenciados desde ningún otro objeto en el documento. Esto puede suceder, por ejemplo, cuando se elimina una página del árbol de páginas del documento, pero el objeto de la página en sí no se elimina. Eliminar estos objetos no invalida el documento, sino que lo reduce.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizeDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Set RemoveUsedObject option
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions
        {
            RemoveUnusedObjects = true
        };
        
        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");
    }
}
```

### Eliminación de Flujos No Utilizados

A veces, el documento contiene flujos de recursos no utilizados. Estos flujos no son "objetos no utilizados" porque están referenciados desde un diccionario de recursos de página. Por lo tanto, no se eliminan con el método "eliminar objetos no utilizados". Pero estos flujos nunca se utilizan con el contenido de la página. Esto puede suceder en casos cuando se ha eliminado una imagen de la página pero no de los recursos de la página. Además, esta situación ocurre a menudo cuando se extraen páginas del documento y las páginas del documento tienen recursos "comunes", es decir, el mismo objeto Resources. Se analiza el contenido de la página para determinar si un flujo de recurso se utiliza o no. Se eliminan los flujos no utilizados. A veces, esto disminuye el tamaño del documento. El uso de esta técnica es similar al paso anterior:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizePdfDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Set RemoveUsedStreams option
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions
        {
            RemoveUnusedStreams = true
        };

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");
    }
}
```

### Vinculación de Flujos Duplicados

Algunos documentos pueden contener varios flujos de recursos idénticos (como imágenes, por ejemplo). Esto puede suceder, por ejemplo, cuando un documento se concatena consigo mismo. El documento de salida contiene dos copias independientes del mismo flujo de recurso. Analizamos todos los flujos de recursos y los comparamos. Si los flujos están duplicados, se fusionan, es decir, solo queda una copia. Las referencias se cambian adecuadamente y se eliminan las copias del objeto. En algunos casos, esto ayuda a disminuir el tamaño del documento.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizePdfDocumentWithLinkDuplicateStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Set LinkDuplicateStreams option
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions
        {
            LinkDuplicateStreams = true
        };

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");
    }
}
```

Además, podemos utilizar la configuración [AllowReusePageContent](https://reference.aspose.com/pdf/es/net/aspose.pdf.optimization/optimizationoptions/properties/allowreusepagecontent). Si esta propiedad se establece en verdadero, el contenido de la página se reutilizará al optimizar el documento para páginas idénticas.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizePdfDocumentWithReusePageContent()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Set AllowReusePageContent option
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions
        {
            AllowReusePageContent = true
        };

        Console.WriteLine("Start");

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");
    }

    Console.WriteLine("Finished");

    // Calculate and display file sizes
    var fi1 = new FileInfo(dataDir + "OptimizeDocument.pdf");
    var fi2 = new FileInfo(dataDir + "OptimizeDocument_out.pdf");
    Console.WriteLine("Original file size: {0}. Reduced file size: {1}", fi1.Length, fi2.Length);
}
```

### Desincrustar Fuentes

Si el documento utiliza fuentes incrustadas, significa que todos los datos de la fuente están almacenados en el documento. La ventaja es que el documento es visible independientemente de si la fuente está instalada en la máquina del usuario o no. Pero incrustar fuentes hace que el documento sea más grande. El método de desincrustar fuentes elimina todas las fuentes incrustadas. Así, el tamaño del documento disminuye, pero el documento en sí puede volverse ilegible si la fuente correcta no está instalada.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizePdfDocumentWithUnembedFonts()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Set UnembedFonts option
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions
        {
            UnembedFonts = true
        };

        Console.WriteLine("Start");

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");	
    }
	
    Console.WriteLine("Finished");

    // Calculate and display file sizes
    var fi1 = new FileInfo(dataDir + "OptimizeDocument.pdf");
    var fi2 = new FileInfo(dataDir + "OptimizeDocument_out.pdf");
    Console.WriteLine("Original file size: {0}. Reduced file size: {1}", fi1.Length, fi2.Length);
}
```

Los recursos de optimización aplican estos métodos al documento. Si se aplica alguno de estos métodos, es muy probable que el tamaño del documento disminuya. Si ninguno de estos métodos se aplica, el tamaño del documento no cambiará, lo cual es obvio.

## Formas Adicionales de Reducir el Tamaño del Documento PDF

### Eliminación o Aplanamiento de Anotaciones

Las anotaciones pueden ser eliminadas cuando son innecesarias. Cuando son necesarias pero no requieren edición adicional, pueden ser aplanadas. Ambas técnicas reducirán el tamaño del archivo.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FlattenAnnotationsInPdfDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Flatten annotations
        foreach (var page in document.Pages)
        {
            foreach (var annotation in page.Annotations)
            {
                annotation.Flatten();
            }
        }

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");
    }
}
```

### Eliminación de Campos de Formulario

Si el documento PDF contiene AcroForms, podemos intentar reducir el tamaño del archivo aplanando los campos de formulario.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FlattenPdfForms()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Load source PDF form
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Flatten Forms
        if (document.Form.Fields.Lenght > 0)
        {
            foreach (var item in document.Form.Fields)
            {
                item.Flatten();
            }
        }

        // Save PDF document
        document.Save(dataDir + "FlattenForms_out.pdf");
    }
}
```

### Convertir un PDF del espacio de color RGB a escala de grises

Un archivo PDF comprende Texto, Imagen, Adjunto, Anotaciones, Gráficos y otros objetos. Puedes encontrarte con la necesidad de convertir un PDF del espacio de color RGB a escala de grises para que sea más rápido al imprimir esos archivos PDF. Además, cuando el archivo se convierte a escala de grises, el tamaño del documento también se reduce, pero también puede causar una disminución en la calidad del documento. Esta función es actualmente compatible con la función Pre-Flight de Adobe Acrobat, pero al hablar de automatización de Office, Aspose.PDF es la solución definitiva para proporcionar tales ventajas para manipulaciones de documentos. Para cumplir con este requisito, se puede utilizar el siguiente fragmento de código.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertRgbToGrayScale()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Create RGB to DeviceGray conversion strategy
        var strategy = new Aspose.Pdf.RgbToDeviceGrayConversionStrategy();

        // Iterate through each page
        for (int idxPage = 1; idxPage <= document.Pages.Count; idxPage++)
        {
            // Get instance of particular page inside PDF
            var page = document.Pages[idxPage];

            // Convert the RGB colorspace image to GrayScale colorspace
            strategy.Convert(page);
        }

        // Save PDF document
        document.Save(dataDir + "TestGray_out.pdf");
    }
}
```

### Compresión FlateDecode

{{% alert color="primary" %}}

Esta función es compatible con la versión 18.12 o superior.

{{% /alert %}}

Aspose.PDF for .NET proporciona soporte de compresión FlateDecode para la funcionalidad de Optimización de PDF. El siguiente fragmento de código muestra cómo utilizar la opción en Optimización para almacenar imágenes con compresión **FlateDecode**:

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizeDocumentImagesWithFlateCompression()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddImage.pdf"))
    {
        // Initialize OptimizationOptions
        var optimizationOptions = new Aspose.Pdf.Optimization.OptimizationOptions();

        // To optimize images using FlateDecode compression, set optimization options to Flate
        optimizationOptions.ImageCompressionOptions.Encoding = Aspose.Pdf.Optimization.ImageEncoding.Flate;

        // Set optimization options
        document.OptimizeResources(optimizationOptions);

        // Save PDF document
        document.Save(dataDir + "OptimizeDocumentImagesWithFlateCompression_out.pdf");
    }
}
```

### Almacenar Imagen en XImageCollection

Aspose.PDF for .NET proporciona la capacidad de almacenar nuevas imágenes en **XImageCollection** con compresión FlateDecode. Para habilitar esta opción, puedes usar la bandera **ImageFilterType.Flate**. El siguiente fragmento de código muestra cómo utilizar esta funcionalidad:

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageToPdfWithFlateCompression()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Open the image file stream
        using (var imageStream = new FileStream(dataDir + "aspose-logo.jpg", FileMode.Open))
        {
            // Add the image to the page resources with Flate compression
            page.Resources.Images.Add(imageStream, Aspose.Pdf.ImageFilterType.Flate);
        }

        // Get the added image
        var ximage = page.Resources.Images[page.Resources.Images.Count];

        // Save the current graphics state
        page.Contents.Add(new Aspose.Pdf.Operators.GSave());

        // Set coordinates for the image placement
        int lowerLeftX = 0;
        int lowerLeftY = 0;
        int upperRightX = 600;
        int upperRightY = 600;

        var rectangle = new Aspose.Pdf.Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
        var matrix = new Aspose.Pdf.Matrix(new double[]
        {
            rectangle.URX - rectangle.LLX, 0, 0, rectangle.URY - rectangle.LLY, rectangle.LLX, rectangle.LLY
        });

        // Use ConcatenateMatrix operator to define how the image must be placed
        page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(matrix));
        page.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));

        // Restore the graphics state
        page.Contents.Add(new Aspose.Pdf.Operators.GRestore());

        // Save the document
        document.Save(dataDir + "AddImageToPdfWithFlateCompression_out.pdf");
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