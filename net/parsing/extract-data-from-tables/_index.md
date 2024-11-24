---
title: Extract Data from Table in PDF with C#
linktitle: Extract Data from Table
type: docs
weight: 40
url: /net/extract-data-from-table-in-pdf/
description: Learn how to extract tabular from PDF using Aspose.PDF for .NET in C#
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extract Tables from PDF programmatically

Extracting tables from PDFs is not a trivial task because table can be created in the various way.

Aspose.PDF for .NET has a tool to make it easy to retrieve tables. To extract table data you shoud perform the following steps:

1. Open document - instantiate a [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) object.
1. Create a [TableAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber) object.
1. Decide which pages to be analyzed and apply [Visit](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber/methods/visit) to the desired pages. The tabular data will be scanned and the result will be stored in [TableList](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber/properties/tablelist).
1. `TableList` is a List of [AbsorbedTable](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedtable). To get the date iterate throught `TableList` and handle [RowList](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedtable/properties/rowlist) and [CellList](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedrow/properties/celllist).
1. Each [AbsorbedCell](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedcell) contains [TextFragments](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedcell/properties/textfragments) collection. You can process it for your own purposes.

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

The following example shows table extraction from the all pages:

```csharp
public static void Extract_Table()
{
    // Load source PDF document
    var filePath = "<... enter path to pdf file here ...>";
    Document document = new Document(filePath);                       
    foreach (var page in document.Pages)
    {
        TableAbsorber absorber = new TableAbsorber();
        absorber.Visit(page);
        foreach (AbsorbedTable table in absorber.TableList)
        {
            Console.WriteLine("Table");
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

## Extract table in specific area of PDF page

Each abosorbed table has [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedtable/properties/rectangle) property that describes position of the table on page.

If you need to extract tables located in a specific region, you have to work with specific coordinates.

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

The following example show how to extract table marked with Square Annotation:

```csharp
public static void Extract_Marked_Table()
{
    // Load source PDF document
    var filePath = "<... enter path to pdf file here ...>";
    Document document = new Document(filePath);  
    var page = document.Pages[1];
    var squareAnnotation =
        page.Annotations.FirstOrDefault(ann => ann.AnnotationType == Annotations.AnnotationType.Square)
        as Annotations.SquareAnnotation;


    TableAbsorber absorber = new TableAbsorber();
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

## Extract Table Data from PDF and store it in CSV file

The following example shows how to extract table and store it as CSV file.
To see how to convert PDF to Excel Spreadsheet please refer to [Convert PDF to Excel](/pdf/net/convert-pdf-to-excel/) article.

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

```csharp
public static void Extract_Table_Save_CSV()
{
    // For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET

    // Load PDF document
    Document document = new Document(dataDir + "input.pdf");

    // Instantiate ExcelSave Option object
    ExcelSaveOptions excelSave = new ExcelSaveOptions { Format = ExcelSaveOptions.ExcelFormat.CSV };

    // Save the output in XLS format
    document.Save("PDFToXLS_out.xlsx", excelSave);
}
```
