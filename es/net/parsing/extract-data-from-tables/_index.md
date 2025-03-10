---
title: Extraer datos de tablas en PDF con C#
linktitle: Extraer datos de tablas
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /es/net/extract-data-from-table-in-pdf/
description: Aprende cómo extraer datos tabulares de PDF usando Aspose.PDF for .NET en C#
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Data from Table in PDF with C#",
    "alternativeHeadline": "Effortlessly Extract Tables from PDFs Using C#",
    "abstract": "Descubre la poderosa capacidad de extraer datos tabulares de documentos PDF usando Aspose.PDF for .NET en C#. Esta función simplifica el proceso de recuperación y manipulación de tablas al permitir a los usuarios acceder sin problemas a celdas individuales y almacenar los datos extraídos en formatos como CSV y Excel, mejorando la accesibilidad y usabilidad de los datos.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "695",
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
    "url": "/net/extract-data-from-table-in-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-data-from-table-in-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

## Extraer tablas de PDF programáticamente

Extraer tablas de PDFs no es una tarea trivial porque las tablas pueden ser creadas de diversas maneras.

Aspose.PDF for .NET tiene una herramienta para facilitar la recuperación de tablas. Para extraer datos de la tabla, debes realizar los siguientes pasos:

1. Abrir el documento - instanciar un objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Crear un objeto [TableAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber).
1. Decidir qué páginas se van a analizar y aplicar [Visit](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber/methods/visit) a las páginas deseadas. Los datos tabulares serán escaneados y el resultado se almacenará en [TableList](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber/properties/tablelist).
1. `TableList` es una lista de [AbsorbedTable](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedtable). Para obtener los datos, itera a través de `TableList` y maneja [RowList](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedtable/properties/rowlist) y [CellList](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedrow/properties/celllist).
1. Cada [AbsorbedCell](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedcell) contiene una colección de [TextFragments](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedcell/properties/textfragments). Puedes procesarlo para tus propios propósitos.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

El siguiente ejemplo muestra la extracción de tablas de todas las páginas:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTable()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {                    
        foreach (var page in document.Pages)
        {
            Aspose.Pdf.TableAbsorber absorber = new Aspose.Pdf.TableAbsorber();
            absorber.Visit(page);
            foreach (var table in absorber.TableList)
            {
                Console.WriteLine("Table");
                foreach (var row in table.RowList)
                {
                    foreach (var cell in row.CellList)
                    {                                 
                        foreach (var fragment in cell.TextFragments)
                        {
                            var sb = new StringBuilder();
                            foreach (var seg in fragment.Segments)
                            {
                                sb.Append(seg.Text);
                            }
                            Console.Write($"{sb.ToString()}|");
                        }                           
                    }
                    Console.WriteLine();
                }
            }
        }
    }
}
```

## Extraer tabla en un área específica de la página PDF

Cada tabla absorbida tiene una propiedad [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedtable/properties/rectangle) que describe la posición de la tabla en la página.

Si necesitas extraer tablas ubicadas en una región específica, debes trabajar con coordenadas específicas.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

El siguiente ejemplo muestra cómo extraer una tabla marcada con una anotación cuadrada:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractMarkedTable()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    { 
        var page = document.Pages[1];
        var squareAnnotation =
            page.Annotations.FirstOrDefault(ann => ann.AnnotationType == Annotations.AnnotationType.Square)
            as Aspose.Pdf.Annotations.SquareAnnotation;


        var absorber = new Aspose.Pdf.Text.TableAbsorber();
        absorber.Visit(page);

        foreach (var table in absorber.TableList)
        {
            var isInRegion = (squareAnnotation.Rect.LLX < table.Rectangle.LLX) &&
            (squareAnnotation.Rect.LLY < table.Rectangle.LLY) &&
            (squareAnnotation.Rect.URX > table.Rectangle.URX) &&
            (squareAnnotation.Rect.URY > table.Rectangle.URY);

            if (isInRegion)
            {
                foreach (var row in table.RowList)
                {
                    foreach (var cell in row.CellList)
                    {
                        foreach (var fragment in cell.TextFragments)
                        {
                            var sb = new StringBuilder();
                            foreach (var seg in fragment.Segments)
                            {
                                sb.Append(seg.Text);
                            }
                            var text = sb.ToString();
                            Console.Write($"{text}|");
                        }
                    }
                    Console.WriteLine();
                }
            }
        }
    }
}
```

## Extraer datos de la tabla de PDF y almacenarlos en un archivo CSV

El siguiente ejemplo muestra cómo extraer una tabla y almacenarla como un archivo CSV.
Para ver cómo convertir PDF a una hoja de cálculo de Excel, consulta el artículo [Convertir PDF a Excel](/pdf/net/convert-pdf-to-excel/).

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTableSaveExcel()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate ExcelSave Option object
        Aspose.Pdf.ExcelSaveOptions excelSave = new Aspose.Pdf.ExcelSaveOptions { Format = ExcelSaveOptions.ExcelFormat.CSV };

        // Save the output in XLS format
        document.Save(dataDir + "ExtractTableSaveXLS_out.xlsx", excelSave);
    }
}
```