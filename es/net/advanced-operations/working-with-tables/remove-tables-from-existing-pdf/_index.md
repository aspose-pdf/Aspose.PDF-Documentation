---
title: Eliminar tablas de un PDF existente
linktitle: Eliminar tablas
type: docs
weight: 50
url: es/net/remove-tables-from-existing-pdf/
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Eliminar tablas de un PDF existente",
    "alternativeHeadline": "Cómo eliminar tablas de un PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, c#, eliminar tabla, borrar tablas",
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
    "url": "/net/remove-tables-from-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/remove-tables-from-existing-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": ""
}
</script>
{{% alert color="primary" %}}

Aspose.PDF para .NET ofrece la capacidad de insertar/crear una tabla dentro de un documento PDF mientras se genera desde cero, o también puede agregar el objeto de tabla en cualquier documento PDF existente. Sin embargo, puede tener la necesidad de [Manipular Tablas en un PDF existente](https://docs.aspose.com/pdf/net/manipulate-tables-in-existing-pdf/) donde puede actualizar los contenidos en las celdas de la tabla existente. Sin embargo, puede encontrarse con la necesidad de eliminar objetos de tabla de un documento PDF existente.

{{% /alert %}}

Para eliminar las tablas, necesitamos usar la clase [TableAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber) para tomar control de las tablas en el PDF existente y luego llamar a [Remove](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber/methods/remove).

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Eliminar Tabla de un documento PDF

Hemos agregado una nueva función, es decir,
Hemos añadido una nueva función, es decir:

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Cargar documento PDF existente
Document pdfDocument = new Document(dataDir + "Table_input.pdf");

// Crear objeto TableAbsorber para encontrar tablas
TableAbsorber absorber = new TableAbsorber();

// Visitar la primera página con el absorber
absorber.Visit(pdfDocument.Pages[1]);

// Obtener la primera tabla en la página
AbsorbedTable table = absorber.TableList[0];

// Eliminar la tabla
absorber.Remove(table);

// Guardar PDF
pdfDocument.Save(dataDir + "Table_out.pdf");
```

## Eliminar múltiples tablas de un documento PDF

A veces un documento PDF puede contener más de una tabla y puede surgir la necesidad de eliminar múltiples tablas de él. Para eliminar múltiples tablas de un documento PDF, por favor use el siguiente fragmento de código:

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Cargar documento PDF existente
Document pdfDocument = new Document(dataDir + "Table_input2.pdf");

// Crear objeto TableAbsorber para encontrar tablas
TableAbsorber absorber = new TableAbsorber();

// Visitar la segunda página con el absorber
absorber.Visit(pdfDocument.Pages[1]);

// Obtener copia de la colección de tablas
AbsorbedTable[] tables = new AbsorbedTable[absorber.TableList.Count];
absorber.TableList.CopyTo(tables, 0);

// Recorrer la copia de la colección y eliminar tablas
foreach (AbsorbedTable table in tables)
    absorber.Remove(table);

// Guardar documento
pdfDocument.Save(dataDir + "Table2_out.pdf");
```
{{% alert color="primary" %}}

Tenga en cuenta que eliminar o reemplazar una tabla cambia la colección TableList. Por lo tanto, en caso de eliminar/reemplazar tablas en un bucle, es esencial copiar la colección TableList.

{{% /alert %}}

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


