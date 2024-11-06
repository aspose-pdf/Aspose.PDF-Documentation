---
title: Extraer y Guardar un Adjunto
linktitle: Extraer y Guardar un Adjunto
type: docs
weight: 20
url: es/net/extract-and-save-an-attachment/
description: Aspose.PDF para .NET le permite obtener todos los adjuntos de un documento PDF. Además, puede obtener un adjunto individual de su documento.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extraer y Guardar un Adjunto",
    "alternativeHeadline": "Cómo extraer y guardar un adjunto",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, c#, guardar adjuntos, extraer adjuntos",
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
    "url": "/net/extract-and-save-an-attachment/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-and-save-an-attachment/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF para .NET le permite obtener todos los adjuntos de un documento PDF. Además, puede obtener un adjunto individual de su documento."
}
</script>

## Obtener Todos los Adjuntos

Con Aspose.PDF, es posible obtener todos los adjuntos de un documento PDF. Esto es útil ya sea cuando quieres guardar los documentos por separado del PDF, o si necesitas despojar a un PDF de adjuntos.

Para obtener todos los adjuntos de un archivo PDF:

1. Recorre la colección [EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection) del objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). La colección [EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection) contiene todos los adjuntos. Cada elemento de esta colección representa un objeto [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification). Cada iteración del bucle foreach a través de la colección [EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection) devuelve un objeto [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification).
Los siguientes fragmentos de código muestran cómo obtener todos los archivos adjuntos de un documento PDF.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

// Abrir documento
Document pdfDocument = new Document(dataDir + "GetAlltheAttachments.pdf");

// Obtener la colección de archivos incrustados
EmbeddedFileCollection embeddedFiles = pdfDocument.EmbeddedFiles;

// Obtener el conteo de los archivos incrustados
Console.WriteLine("Total de archivos : {0}", embeddedFiles.Count);

int count = 1;

// Recorrer la colección para obtener todos los archivos adjuntos
foreach (FileSpecification fileSpecification in embeddedFiles)
{
    Console.WriteLine("Nombre: {0}", fileSpecification.Name);
    Console.WriteLine("Descripción: {0}",
    fileSpecification.Description);
    Console.WriteLine("Tipo MIME: {0}", fileSpecification.MIMEType);

    // Verificar si el objeto de parámetros contiene los parámetros
    if (fileSpecification.Params != null)
    {
        Console.WriteLine("Suma de verificación: {0}",
        fileSpecification.Params.CheckSum);
        Console.WriteLine("Fecha de creación: {0}",
        fileSpecification.Params.CreationDate);
        Console.WriteLine("Fecha de modificación: {0}",
        fileSpecification.Params.ModDate);
        Console.WriteLine("Tamaño: {0}", fileSpecification.Params.Size);
    }

    // Obtener el archivo adjunto y escribirlo en un archivo o flujo
    byte[] fileContent = new byte[fileSpecification.Contents.Length];
    fileSpecification.Contents.Read(fileContent, 0,
    fileContent.Length);
    FileStream fileStream = new FileStream(dataDir + count + "_out" + ".txt",
    FileMode.Create);
    fileStream.Write(fileContent, 0, fileContent.Length);
    fileStream.Close();
    count+=1;
}
```
## Obtener Adjunto Individual

Para obtener un adjunto individual, podemos especificar el índice del adjunto en el objeto `EmbeddedFiles` de la instancia del Documento. Por favor, intente usar el siguiente fragmento de código.

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

// Abrir documento
Document pdfDocument = new Document(dataDir + "GetIndividualAttachment.pdf");

// Obtener archivo embebido particular
FileSpecification fileSpecification = pdfDocument.EmbeddedFiles[1];

// Obtener las propiedades del archivo
Console.WriteLine("Nombre: {0}", fileSpecification.Name);
Console.WriteLine("Descripción: {0}", fileSpecification.Description);
Console.WriteLine("Tipo MIME: {0}", fileSpecification.MIMEType);

// Verificar si el objeto de parámetros contiene los parámetros
if (fileSpecification.Params != null)
{
    Console.WriteLine("Suma de verificación: {0}",
    fileSpecification.Params.CheckSum);
    Console.WriteLine("Fecha de creación: {0}",
    fileSpecification.Params.CreationDate);
    Console.WriteLine("Fecha de modificación: {0}",
    fileSpecification.Params.ModDate);
    Console.WriteLine("Tamaño: {0}", fileSpecification.Params.Size);
}

// Obtener el adjunto y escribir a archivo o flujo
byte[] fileContent = new byte[fileSpecification.Contents.Length];
fileSpecification.Contents.Read(fileContent, 0, fileContent.Length);

FileStream fileStream = new FileStream(dataDir + "test_out" + ".txt", FileMode.Create);
fileStream.Write(fileContent, 0, fileContent.Length);
fileStream.Close();
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

