---
title: Trabajando con Portafolio en PDF
linktitle: Portafolio
type: docs
weight: 40
url: /es/net/portfolio/
description: Cómo crear un portafolio en PDF con C#. Debes usar un archivo de Microsoft Excel, un documento Word y un archivo de imagen para crear un portafolio en PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Trabajando con Portafolio en PDF",
    "alternativeHeadline": "Crear un portafolio en documento PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, c#, portafolio",
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
    "url": "/net/portfolio/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/portfolio/"
    },
    "dateModified": "2022-02-04",
    "description": "Cómo crear un portafolio en PDF con C#. Debes usar un archivo de Microsoft Excel, un documento Word y un archivo de imagen para crear un portafolio en PDF."
}
</script>
## Cómo Crear un Portafolio PDF

Aspose.PDF permite crear documentos de Portafolio PDF utilizando la clase [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Agrega un archivo en un objeto Document.Collection después de obtenerlo con la clase [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification). Cuando los archivos hayan sido añadidos, usa el método Save de la clase Document para guardar el documento del portafolio.

El siguiente ejemplo utiliza un archivo de Microsoft Excel, un documento Word y un archivo de imagen para crear un Portafolio PDF.

El código a continuación resulta en el siguiente portafolio.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

### Un Portafolio PDF creado con Aspose.PDF

![Un Portafolio PDF creado con Aspose.PDF para .NET](working-with-pdf-portfolio_1.jpg)

```csharp
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_TechnicalArticles();

// Instancia el objeto Document
Document doc = new Document();

// Instancia el objeto de colección de documentos
doc.Collection = new Collection();

// Obtiene los archivos para añadir al Portafolio
FileSpecification excel = new FileSpecification( dataDir + "HelloWorld.xlsx");
FileSpecification word = new FileSpecification( dataDir + "HelloWorld.docx");
FileSpecification image = new FileSpecification(dataDir + "aspose-logo.jpg");

// Proporciona descripción de los archivos
excel.Description = "Archivo Excel";
word.Description = "Archivo Word";
image.Description = "Archivo de Imagen";

// Añade archivos a la colección de documentos
doc.Collection.Add(excel);
doc.Collection.Add(word);
doc.Collection.Add(image);

// Guarda el documento del Portafolio
doc.Save(dataDir + "CreatePDFPortfolio_out.pdf");
```
## Extraer archivos de un Portafolio PDF

Los Portafolios PDF permiten reunir contenido de una variedad de fuentes (por ejemplo, archivos PDF, Word, Excel, JPEG) en un contenedor unificado. Los archivos originales conservan sus identidades individuales pero se ensamblan en un archivo de Portafolio PDF. Los usuarios pueden abrir, leer, editar y formatear cada archivo componente de manera independiente de los otros archivos componentes.

Aspose.PDF permite la creación de documentos de Portafolio PDF utilizando la clase [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). También ofrece la capacidad de extraer archivos de un portafolio PDF.

El siguiente fragmento de código te muestra los pasos para extraer archivos de un portafolio PDF.

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_TechnicalArticles();

// Cargar el Portafolio PDF fuente
Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(dataDir + "PDFPortfolio.pdf");
// Obtener colección de archivos incrustados
EmbeddedFileCollection embeddedFiles = pdfDocument.EmbeddedFiles;
// Iterar a través de cada archivo del Portafolio
foreach (FileSpecification fileSpecification in embeddedFiles)
{
    // Obtener el adjunto y escribir en archivo o flujo
    byte[] fileContent = new byte[fileSpecification.Contents.Length];
    fileSpecification.Contents.Read(fileContent, 0, fileContent.Length);
    string filename = Path.GetFileName(fileSpecification.Name);
    // Guardar el archivo extraído en alguna ubicación
    FileStream fileStream = new FileStream(dataDir + "_out" + filename, FileMode.Create);
    fileStream.Write(fileContent, 0, fileContent.Length);
    // Cerrar el objeto de flujo
    fileStream.Close();
}
```
![Extraer archivos de un Portafolio PDF](working-with-pdf-portfolio_2.jpg)

## Eliminar archivos de un Portafolio PDF

Para eliminar archivos de un portafolio PDF, prueba utilizando las siguientes líneas de código.

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_TechnicalArticles();

// Cargar el Portafolio PDF fuente
Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(dataDir + "PDFPortfolio.pdf");
pdfDocument.Collection.Delete();
pdfDocument.Save(dataDir + "No_PortFolio_out.pdf");
```

