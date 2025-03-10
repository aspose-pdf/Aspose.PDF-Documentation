---
title: Manipular Tablas en PDF existente
linktitle: Manipular Tablas
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /es/net/manipulate-tables-in-existing-pdf/
description: Aprende a trabajar con tablas en PDFs existentes utilizando Aspose.PDF for .NET, proporcionando flexibilidad en la modificación de documentos.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Manipulate Tables in existing PDF",
    "alternativeHeadline": "Enhance Table Editing in Existing PDF Documents",
    "abstract": "Aspose.PDF for .NET introduce una poderosa característica para manipular tablas PDF existentes, permitiendo a los usuarios buscar, analizar y modificar el contenido de las tablas con facilidad. La nueva clase TableAbsorber permite actualizaciones y reemplazos dinámicos de tablas directamente dentro de documentos PDF, agilizando el proceso de gestión de datos tabulares en PDFs para una funcionalidad mejorada. Explora esta capacidad innovadora para optimizar tus tareas de edición de PDF e integración de datos.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
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
    "url": "/net/manipulate-tables-in-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/manipulate-tables-in-existing-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios avanzados y desarrolladores."
}
</script>

## Manipular tablas en PDF existente

Una de las primeras características soportadas por Aspose.PDF for .NET son sus capacidades de Trabajar con Tablas y proporciona un gran soporte para agregar tablas en archivos PDF generados desde cero o en cualquier archivo PDF existente. También obtienes la capacidad de Integrar Tablas con Base de Datos (DOM) para crear tablas dinámicas basadas en el contenido de la base de datos. En esta nueva versión, hemos implementado una nueva característica de búsqueda y análisis de tablas simples que ya existen en la página del documento PDF. Una nueva clase llamada **Aspose.PDF.Text.TableAbsorber** proporciona estas capacidades. El uso de TableAbsorber es muy similar a la clase existente TextFragmentAbsorber. El siguiente fragmento de código muestra los pasos para actualizar el contenido en una celda de tabla particular.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ManipulateTable()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Create TableAbsorber object to find tables
        var absorber = new Aspose.Pdf.Text.TableAbsorber();

        // Visit first page with absorber
        absorber.Visit(document.Pages[1]);

        // Get access to first table on page, their first cell and text fragments in it
        Aspose.Pdf.Text.TextFragment fragment = absorber.TableList[0].RowList[0].CellList[0].TextFragments[1];

        // Change text of the first text fragment in the cell
        fragment.Text = "hi world";

        // Save PDF document
        document.Save(dataDir + "ManipulateTable_out.pdf");
    }
}
```

## Reemplazar tabla antigua con una nueva en el documento PDF

En caso de que necesites encontrar una tabla particular y reemplazarla con la deseada, puedes usar el método Replace() de la clase [TableAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber) para hacerlo. El siguiente ejemplo demuestra la funcionalidad para reemplazar la tabla dentro del documento PDF:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceTable()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Table_input2.pdf"))
    {
        // Create TableAbsorber object to find tables
        var absorber = new Aspose.Pdf.Text.TableAbsorber();

        // Visit first page with absorber
        absorber.Visit(document.Pages[1]);

        // Get first table on the page
        Aspose.Pdf.Text.AbsorbedTable table = absorber.TableList[0];

        // Create new table
        var newTable = new Aspose.Pdf.Table();
        newTable.ColumnWidths = "100 100 100";
        newTable.DefaultCellBorder = new Aspose.Pdf.BorderInfo(BorderSide.All, 1F);

        Row row = newTable.Rows.Add();
        row.Cells.Add("Col 1");
        row.Cells.Add("Col 2");
        row.Cells.Add("Col 3");

        // Replace the table with new one
        absorber.Replace(document.Pages[1], table, newTable);

        // Save PDF document
        document.Save(dataDir + "ReplaceTable_out.pdf");
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