---
title: Optimizar, Comprimir o Reducir el Tamaño de PDF en C#
linktitle: Optimizar PDF
type: docs
weight: 30
url: es/net/optimize-pdf/
keywords: "optimize pdf c#"
description: Optimizar archivo PDF, comprimir todas las imágenes, reducir tamaño del PDF, Desincrustar fuentes, Eliminar objetos no utilizados con C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /net/changing-page-sizes-in-a-pdf-file/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Optimizar PDF usando C#",
    "alternativeHeadline": "Cómo optimizar PDF con .NET",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, c#, optimizar pdf",
    "wordcount": "302",
    "proficiencyLevel": "Principiante",
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
    "url": "/net/optimize-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/optimize-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": "Optimizar archivo PDF, comprimir todas las imágenes, reducir tamaño del PDF, Desincrustar fuentes, Eliminar objetos no utilizados con C#."
}
</script>

Un documento PDF a veces puede contener datos adicionales. Reducir el tamaño de un archivo PDF te ayudará a optimizar la transferencia de red y el almacenamiento. Esto es especialmente útil para publicar en páginas web, compartir en redes sociales, enviar por correo electrónico o archivar en almacenamiento. Podemos usar varias técnicas para optimizar PDF:

- Optimizar el contenido de la página para navegación en línea
- Reducir o comprimir todas las imágenes
- Habilitar la reutilización del contenido de la página
- Fusionar flujos duplicados
- Desincrustar fuentes
- Eliminar objetos no utilizados
- Eliminar campos de formulario aplanados
- Eliminar o aplanar anotaciones

{{% alert color="primary" %}}

Se puede encontrar una explicación detallada de los métodos de optimización en la página de Visión General de Métodos de Optimización.

{{% /alert %}}

## Optimizar Documento PDF para la Web

La optimización, o linearización para Web, se refiere al proceso de hacer que un archivo PDF sea adecuado para la navegación en línea usando un navegador web. Para optimizar un archivo para visualización web:

1. Abre el documento de entrada en un objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1.
1. Guarde el documento optimizado utilizando el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save).

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

El siguiente fragmento de código muestra cómo optimizar un documento PDF para la web.

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Abrir documento
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");

// Optimizar para la web
pdfDocument.Optimize();

dataDir = dataDir + "OptimizeDocument_out.pdf";

// Guardar el documento de salida
pdfDocument.Save(dataDir);
```

## Reducir Tamaño PDF

El método [OptimizeResources()](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/optimizeresources) le permite reducir el tamaño del documento eliminando la información innecesaria.
El método [OptimizeResources()](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/optimizeresources) te permite reducir el tamaño del documento eliminando la información innecesaria.

- Se eliminan los recursos que no se utilizan en las páginas del documento
- Los recursos iguales se unen en un solo objeto
- Se eliminan los objetos no utilizados

El fragmento a continuación es un ejemplo. Sin embargo, ten en cuenta que este método no puede garantizar la reducción del tamaño del documento.

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// Abrir documento
Document pdfDocument = new Document(dataDir + "ShrinkDocument.pdf");
// Optimizar el documento PDF. Ten en cuenta, sin embargo, que este método no puede garantizar la reducción del tamaño del documento
pdfDocument.OptimizeResources();
dataDir = dataDir + "ShrinkDocument_out.pdf";
// Guardar el documento actualizado
pdfDocument.Save(dataDir);
```

## Gestión de la Estrategia de Optimización

También podemos personalizar la estrategia de optimización.
También podemos personalizar la estrategia de optimización.

### Reducir o Comprimir Todas las Imágenes

Tenemos dos formas de trabajar con imágenes: reducir la calidad de la imagen y/o cambiar su resolución. En cualquier caso, se deben aplicar [ImageCompressionOptions](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/imagecompressionoptions). En el siguiente ejemplo, reducimos las imágenes disminuyendo [ImageQuality](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/imagecompressionoptions/properties/imagequality) a 50.

`ImageQuality` funciona de manera similar a la calidad JPEG, donde el valor 0 es el más bajo y el valor 100 es el más alto.

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();
// Abrir documento
Document pdfDocument = new Document(dataDir + "Shrinkimage.pdf");
// Inicializar OptimizationOptions
var optimizeOptions = new Pdf.Optimization.OptimizationOptions();
// Establecer la opción CompressImages
optimizeOptions.ImageCompressionOptions.CompressImages = true;
// Establecer la opción ImageQuality
optimizeOptions.ImageCompressionOptions.ImageQuality = 50;
// Optimizar el documento PDF utilizando OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "Shrinkimage_out.pdf";
// Guardar el documento actualizado
pdfDocument.Save(dataDir);
```
Otra forma es redimensionar las imágenes a una resolución más baja. En este caso, debemos establecer ResizeImages en verdadero y MaxResolution al valor apropiado.

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Inicializar Tiempo
var time = DateTime.Now.Ticks;
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();
// Abrir documento
Document pdfDocument = new Document(dataDir + "ResizeImage.pdf");
// Inicializar OptimizationOptions
var optimizeOptions = new Pdf.Optimization.OptimizationOptions();
// Establecer la opción CompressImages
optimizeOptions.ImageCompressionOptions.CompressImages = true;
// Establecer la opción ImageQuality
optimizeOptions.ImageCompressionOptions.ImageQuality = 75;
// Establecer la opción ResizeImage
optimizeOptions.ImageCompressionOptions.ResizeImages = true;
// Establecer la opción MaxResolution
optimizeOptions.ImageCompressionOptions.MaxResolution = 300;
// Optimizar el documento PDF usando OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "ResizeImages_out.pdf";
// Guardar el documento actualizado
pdfDocument.Save(dataDir);
```
Otro tema importante es el tiempo de ejecución. Pero de nuevo, también podemos gestionar esta configuración. Actualmente, podemos usar dos algoritmos: Estándar y Rápido. Para controlar el tiempo de ejecución debemos establecer una propiedad [Versión](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/imagecompressionoptions/properties/version). El siguiente fragmento demuestra el algoritmo Rápido:

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Inicializar Tiempo
var time = DateTime.Now.Ticks;
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();
// Abrir documento
Document pdfDocument = new Document(dataDir + "Shrinkimage.pdf");
// Inicializar OptimizationOptions
var optimizeOptions = new Pdf.Optimization.OptimizationOptions();
// Establecer la opción CompressImages
optimizeOptions.ImageCompressionOptions.CompressImages = true;
// Establecer la opción ImageQuality
optimizeOptions.ImageCompressionOptions.ImageQuality = 75;
// Establecer la Versión de Compresión de Imagen a rápido
optimizeOptions.ImageCompressionOptions.Version = Pdf.Optimization.ImageCompressionVersion.Fast;
// Optimizar el documento PDF usando OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "FastShrinkImages_out.pdf";
// Guardar el documento actualizado
pdfDocument.Save(dataDir);
Console.WriteLine("Ticks: {0}", DateTime.Now.Ticks - time);
```
### Eliminación de Objetos No Utilizados

Un documento PDF a veces contiene objetos PDF que no están referenciados por ningún otro objeto en el documento. Esto puede suceder, por ejemplo, cuando se elimina una página del árbol de páginas del documento pero el objeto de la página en sí no se elimina. Eliminar estos objetos no hace que el documento sea inválido, sino que lo reduce.

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// Abrir documento
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// Establecer la opción RemoveUsedObject
var optimizeOptions = new Pdf.Optimization.OptimizationOptions
{
    RemoveUnusedObjects = true
};
// Optimizar el documento PDF usando OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "OptimizeDocument_out.pdf";
// Guardar el documento actualizado
pdfDocument.Save(dataDir);
```

### Eliminación de Flujos No Utilizados

A veces el documento contiene flujos de recursos no utilizados.
A veces el documento contiene flujos de recursos no utilizados.

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// Abrir documento
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// Establecer la opción RemoveUsedStreams
var optimizeOptions = new Pdf.Optimization.OptimizationOptions
{
    RemoveUnusedStreams = true
};
// Optimizar el documento PDF utilizando OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "OptimizeDocument_out.pdf";
// Guardar el documento actualizado
pdfDocument.Save(dataDir);
```

### Vinculando flujos duplicados

Algunos documentos pueden contener varios flujos de recursos idénticos (como imágenes, por ejemplo).
Algunos documentos pueden contener varios flujos de recursos idénticos (como imágenes, por ejemplo).

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// Abrir documento
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// Establecer la opción LinkDuplcateStreams
var optimizeOptions = new Pdf.Optimization.OptimizationOptions
{
    LinkDuplcateStreams = true
};
// Optimizar el documento PDF usando OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "OptimizeDocument_out.pdf";
// Guardar el documento actualizado
pdfDocument.Save(dataDir);
```

Adicionalmente, podemos usar la configuración de [AllowReusePageContent](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/optimizationoptions/properties/allowreusepagecontent).
Adicionalmente, podemos usar la configuración de [AllowReusePageContent](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/optimizationoptions/properties/allowreusepagecontent).

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// Abrir documento
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// Configurar la opción AllowReusePageContent
var optimizeOptions = new Pdf.Optimization.OptimizationOptions
{
    AllowReusePageContent = true
};
Console.WriteLine("Inicio");
// Optimizar el documento PDF usando OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
// Guardar el documento actualizado
pdfDocument.Save(dataDir + "OptimizeDocument_out.pdf");
Console.WriteLine("Finalizado");
var fi1 = new System.IO.FileInfo(dataDir + "OptimizeDocument.pdf");
var fi2 = new System.IO.FileInfo(dataDir + "OptimizeDocument_out.pdf");
Console.WriteLine("Tamaño del archivo original: {0}. Tamaño del archivo reducido: {1}", fi1.Length, fi2.Length);
```
### Desincrustar Fuentes

Si el documento utiliza fuentes incrustadas, significa que todos los datos de la fuente se almacenan en el documento. La ventaja es que el documento se puede ver independientemente de si la fuente está instalada en la máquina del usuario o no. Pero incrustar fuentes hace que el documento sea más grande. El método de desincrustar fuentes elimina todas las fuentes incrustadas. Por lo tanto, el tamaño del documento disminuye, pero el documento en sí puede volverse ilegible si no está instalada la fuente correcta.

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// Abrir documento
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// Establecer la opción UnembedFonts
var optimizeOptions = new Pdf.Optimization.OptimizationOptions
{
    UnembedFonts = true
};
Console.WriteLine("Inicio");
// Optimizar el documento PDF usando OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
// Guardar el documento actualizado
pdfDocument.Save(dataDir + "OptimizeDocument_out.pdf");
Console.WriteLine("Finalizado");
var fi1 = new System.IO.FileInfo(dataDir + "OptimizeDocument.pdf");
var fi2 = new System.IO.FileInfo(dataDir + "OptimizeDocument_out.pdf");
Console.WriteLine("Tamaño de archivo original: {0}. Tamaño de archivo reducido: {1}", fi1.Length, fi2.Length);
```
Los recursos de optimización aplican estos métodos al documento. Si se aplican alguno de estos métodos, el tamaño del documento probablemente disminuirá. Si no se aplica ninguno de estos métodos, el tamaño del documento no cambiará, lo cual es obvio.

## Formas adicionales de reducir el tamaño del documento PDF

### Eliminación o aplanamiento de anotaciones

Las anotaciones pueden eliminarse cuando no son necesarias. Cuando son necesarias pero no requieren edición adicional, pueden aplanarse. Ambas técnicas reducirán el tamaño del archivo.

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// Abrir documento
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// Aplanar anotaciones
foreach (var page in pdfDocument.Pages)
{
    foreach (var annotation in page.Annotations)
    {
        annotation.Flatten();
    }

}
// Guardar documento actualizado
pdfDocument.Save(dataDir + "OptimizeDocument_out.pdf");
```
### Eliminación de Campos de Formulario

Si el documento PDF contiene AcroForms, podemos intentar reducir el tamaño del archivo aplanando los campos de formulario.

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Cargar el formulario PDF fuente
Document doc = new Document(dataDir + "input.pdf");

// Aplanar Formularios
if (doc.Form.Fields.Count() > 0)
{
    foreach (var item in doc.Form.Fields)
    {
        item.Flatten();
    }
}

dataDir = dataDir + "FlattenForms_out.pdf";
// Guardar el documento actualizado
doc.Save(dataDir);
```

### Convertir un PDF del espacio de color RGB a escala de grises

Un archivo PDF comprende Texto, Imagen, Adjunto, Anotaciones, Gráficos y otros objetos.
Un archivo PDF comprende Texto, Imagen, Adjunto, Anotaciones, Gráficos y otros objetos.

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Cargar archivo PDF fuente
using (Document document = new Document(dataDir + "input.pdf"))
{
    Aspose.Pdf.RgbToDeviceGrayConversionStrategy strategy = new Aspose.Pdf.RgbToDeviceGrayConversionStrategy();
    for (int idxPage = 1; idxPage <= document.Pages.Count; idxPage++)
    {
        // Obtener instancia de una página particular dentro del PDF
        Page page = document.Pages[idxPage];
        // Convertir la imagen de espacio de color RGB a espacio de color Escala de Grises
        strategy.Convert(page);
    }
    // Guardar el archivo resultante
    document.Save(dataDir + "Test-gray_out.pdf");
}
```

### Compresión FlateDecode

{{% alert color="primary" %}}

Esta característica es compatible con la versión 18.12 o superior.

{{% /alert %}}

Aspose.PDF para .NET proporciona soporte de compresión FlateDecode para la funcionalidad de Optimización de PDF.
Aspose.PDF para .NET proporciona soporte de compresión FlateDecode para la funcionalidad de optimización de PDF.

{{< gist "aspose-com-gists" "63473b1ba28e09e229cfbf4430eabd8a" "Examples-CSharp-AsposePDF-Images-FlateDecodeCompression-1.cs" >}}

### **Almacenar Imagen en XImageCollection**

Aspose.PDF para .NET proporciona la capacidad de almacenar nuevas imágenes en **XImageCollection** con compresión FlateDecode. Para habilitar esta opción puedes usar la bandera **ImageFilterType.Flate**. El siguiente fragmento de código muestra cómo utilizar esta funcionalidad:

{{< gist "aspose-com-gists" "63473b1ba28e09e229cfbf4430eabd8a" "Examples-CSharp-AsposePDF-Images-StoreImageInXImageCollection-1.cs" >}}

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

