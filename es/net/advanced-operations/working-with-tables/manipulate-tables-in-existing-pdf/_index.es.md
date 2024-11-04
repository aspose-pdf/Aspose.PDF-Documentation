---
title: Manipular Tablas en un PDF existente
linktitle: Manipular Tablas
type: docs
weight: 40
url: /net/manipulate-tables-in-existing-pdf/
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Manipular Tablas en un PDF existente",
    "alternativeHeadline": "Cómo actualizar el contenido de Tablas en un PDF existente",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, c#, manipular tablas",
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
    "url": "/net/manipulate-tables-in-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/manipulate-tables-in-existing-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": ""
}
</script>
## Manipular tablas en PDF existentes

Una de las primeras características soportadas por Aspose.PDF para .NET es su capacidad de Trabajar con Tablas y proporciona un gran apoyo para añadir tablas en archivos PDF que se generan desde cero o cualquier archivo PDF existente. También obtienes la capacidad de Integrar Tabla con Base de Datos (DOM) para crear tablas dinámicas basadas en contenidos de la base de datos. En esta nueva versión, hemos implementado una nueva característica de búsqueda y análisis de tablas simples que ya existen en la página del documento PDF. Una nueva clase llamada **Aspose.PDF.Text.TableAbsorber** proporciona estas capacidades. El uso de TableAbsorber es muy similar a la clase TextFragmentAbsorber existente. El siguiente fragmento de código muestra los pasos para actualizar contenidos en una celda de tabla particular.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// El camino al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Cargar archivo PDF existente
Document pdfDocument = new Document(dataDir + "input.pdf");
// Crear objeto TableAbsorber para encontrar tablas
TableAbsorber absorber = new TableAbsorber();

// Visitar la primera página con absorber
absorber.Visit(pdfDocument.Pages[1]);

// Acceder a la primera tabla en la página, su primera celda y los fragmentos de texto en ella
TextFragment fragment = absorber.TableList[0].RowList[0].CellList[0].TextFragments[1];

// Cambiar el texto del primer fragmento de texto en la celda
fragment.Text = "hola mundo";
dataDir = dataDir + "ManipulateTable_out.pdf";
pdfDocument.Save(dataDir);
```
## Reemplazar tabla antigua con una nueva en documento PDF

En caso de que necesite encontrar una tabla particular y reemplazarla con la deseada, puede usar el método Replace() de la clase [TableAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber) para hacerlo. El siguiente ejemplo demuestra la funcionalidad para reemplazar la tabla dentro del documento PDF:

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Cargar el documento PDF existente
Document pdfDocument = new Document(dataDir + @"Table_input2.pdf");

// Crear objeto TableAbsorber para encontrar tablas
TableAbsorber absorber = new TableAbsorber();

// Visitar la primera página con el absorber
absorber.Visit(pdfDocument.Pages[1]);

// Obtener la primera tabla en la página
AbsorbedTable table = absorber.TableList[0];

// Crear nueva tabla
Table newTable = new Table();
newTable.ColumnWidths = "100 100 100";
newTable.DefaultCellBorder = new BorderInfo(BorderSide.All, 1F);

Row row = newTable.Rows.Add();
row.Cells.Add("Col 1");
row.Cells.Add("Col 2");
row.Cells.Add("Col 3");

// Reemplazar la tabla con la nueva
absorber.Replace(pdfDocument.Pages[1], table, newTable);

// Guardar el documento
pdfDocument.Save(dataDir + "TableReplaced_out.pdf");
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF para la biblioteca .NET",
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

