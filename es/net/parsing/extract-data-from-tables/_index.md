---
title: Extraer datos de una tabla en PDF con C#
linktitle: Extraer datos de la tabla
type: docs
weight: 40
url: es/net/extract-data-from-table-in-pdf/
description: Aprende cómo extraer datos tabulares de un PDF utilizando Aspose.PDF para .NET en C#
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extraer tablas de PDF programáticamente

Extraer tablas de los PDFs no es una tarea trivial porque las tablas pueden ser creadas de varias maneras.

Aspose.PDF para .NET tiene una herramienta para facilitar la recuperación de tablas. Para extraer datos de una tabla deberías realizar los siguientes pasos:

1. Abrir documento - instanciar un objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document);
1. Crear un objeto [TableAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber).
1. `TableList` es una Lista de [AbsorbedTable](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedtable). Para obtener la fecha, itera a través de `TableList` y maneja [RowList](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedtable/properties/rowlist) y [CellList](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedrow/properties/celllist)
1. Cada [AbsorbedCell](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedcell) contiene una colección de [TextFragments](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedcell/properties/textfragments). Puedes procesarla para tus propios fines.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

El siguiente ejemplo muestra la extracción de tablas de todas las páginas:

```csharp
public static void Extract_Table()
{
    // Cargar el documento PDF fuente
    var filePath="<... ingresa la ruta del archivo pdf aquí ...>";
    Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(filePath);                       
    foreach (var page in pdfDocument.Pages)
    {
        Aspose.Pdf.Text.TableAbsorber absorber = new Aspose.Pdf.Text.TableAbsorber();
        absorber.Visit(page);
        foreach (AbsorbedTable table in absorber.TableList)
        {
            Console.WriteLine("Tabla");
            foreach (AbsorbedRow row in table.RowList)
            {
                foreach (AbsorbedCell cell in row.CellList)
                {                                 
                    foreach (TextFragment fragment in cell.TextFragments)
                    {
                        var sb = new StringBuilder();
                        foreach (TextSegment seg in fragment.Segments)
                            sb.Append(seg.Text);
                        Console.Write($"{sb.ToString()}|");
                    }                           
                }
                Console.WriteLine();
            }
        }
    }
}
```
## Extraer tabla en un área específica de la página PDF

Cada tabla absorbida tiene una propiedad [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedtable/properties/rectangle) que describe la posición de la tabla en la página.

Por lo tanto, si necesitas extraer tablas ubicadas en una región específica, tienes que trabajar con coordenadas específicas.

El siguiente fragmento de código también trabaja con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

El siguiente ejemplo muestra cómo extraer una tabla marcada con una Anotación Cuadrada:

```csharp
public static void Extract_Marked_Table()
{
    // Cargar el documento PDF fuente
    var filePath="<... ingresar ruta al archivo pdf aquí ...>";
    Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(filePath);  
    var page = pdfDocument.Pages[1];
    var squareAnnotation =
        page.Annotations.FirstOrDefault(ann => ann.AnnotationType == Annotations.AnnotationType.Square)
        as Annotations.SquareAnnotation;


    Aspose.Pdf.Text.TableAbsorber absorber = new Aspose.Pdf.Text.TableAbsorber();
    absorber.Visit(page);

    foreach (AbsorbedTable table in absorber.TableList)
    {
        var isInRegion = (squareAnnotation.Rect.LLX < table.Rectangle.LLX) &&
        (squareAnnotation.Rect.LLY < table.Rectangle.LLY) &&
        (squareAnnotation.Rect.URX > table.Rectangle.URX) &&
        (squareAnnotation.Rect.URY > table.Rectangle.URY);

        if (isInRegion)
        {
            foreach (AbsorbedRow row in table.RowList)
            {
                foreach (AbsorbedCell cell in row.CellList)
                {

                    foreach (TextFragment fragment in cell.TextFragments)
                    {
                        var sb = new StringBuilder();
                        foreach (TextSegment seg in fragment.Segments)
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
```
## Extraer datos de tabla de PDF y almacenarlos en archivo CSV

El siguiente ejemplo muestra cómo extraer una tabla y almacenarla como archivo CSV.
Para ver cómo convertir un PDF a una hoja de cálculo de Excel, consulte el artículo [Convertir PDF a Excel](/pdf/net/convert-pdf-to-excel/).

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
public static void Extract_Table_Save_CSV()
{
    // Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET

    // Cargar documento PDF
    Document pdfDocument = new Document(_dataDir + "input.pdf");

    // Instanciar objeto de opción de guardado de Excel
    ExcelSaveOptions excelSave = new ExcelSaveOptions { Format = ExcelSaveOptions.ExcelFormat.CSV };

    // Guardar la salida en formato XLS
    pdfDocument.Save("PDFToXLS_out.xlsx", excelSave);
}
```
