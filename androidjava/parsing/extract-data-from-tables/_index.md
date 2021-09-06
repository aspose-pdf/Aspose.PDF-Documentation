---
title: Extract Table Data from PDF using Java
linktitle: Extract Table Data
type: docs
weight: 40
url: /androidjava/extract-data-from-table-in-pdf/
description: Learn how to extract tabular from PDF using Aspose.PDF for Java
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extract Tables from PDF programmatically

Extracting tables from PDFs is not a trivial task because the table can be created variously.

Aspose.PDF for Java has a tool to make it easy to retrieve tables. To extract table data, you should perform the following steps:

1. Open document - instantiate a [Document](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Document) object;
1. Create a [TableAbsorber](https://apireference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber) object.
1. Decide which pages to be analyzed and apply [visit](https://apireference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#visit-com.aspose.pdf.Page-) to the desired pages. The tabular data will be scanned, and the result will be saved in a list of [AbsorbedTable](https://apireference.aspose.com/pdf/java/aspose.pdf.text/absorbedtable). We can get this list through [getTableList](https://apireference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#getTableList--) method.
1. To get the data iterate throught `TableList` and handle list of [absorbed rows](https://apireference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedRow) and list of absorbed cells. We can access to the first list by calling [getTableList](https://apireference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#getTableList--) method and to the second by calling [getCellList](https://apireference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedRow#getCellList--).
1. Each [AbsorbedCell](https://apireference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedCell) contains [TextFragmentCollections](https://apireference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentCollection). You can process it for your own purposes.

The following example shows table extraction from the all pages:

```java
public static void Extract_Table()
{
        public static void Extract_Table() {
        // Load source PDF document        
        String filePath = "/home/aspose/pdf-examples/Samples/sample_table.pdf";
        com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);
        com.aspose.pdf.TableAbsorber absorber = new com.aspose.pdf.TableAbsorber();

        // Scan pages
        for (com.aspose.pdf.Page page : pdfDocument.getPages()) {
            absorber.visit(page);
            for (com.aspose.pdf.AbsorbedTable table : absorber.getTableList()) {
                System.out.println("Table");
                // Iterate throught list of rows
                for (com.aspose.pdf.AbsorbedRow row : table.getRowList()) {
                    // Iterate throught list of cell
                    for (com.aspose.pdf.AbsorbedCell cell : row.getCellList()) {
                        for (com.aspose.pdf.TextFragment fragment : cell.getTextFragments()) {
                            StringBuilder sb = new StringBuilder();
                            for (com.aspose.pdf.TextSegment seg : fragment.getSegments())
                                sb.append(seg.getText());
                            System.out.print(sb.toString() + "|");
                        }
                    }
                    System.out.println();
                }
            }
        }
    }
}
```

## Extract table in specific area of PDF page

Each abosorbed table has [Rectangle](https://apireference.aspose.com/pdf/java/aspose.pdf.text/absorbedtable/properties/rectangle) property that describes position of the table on page.

So, if you need to extract tables located in a specific region, you have to work with specific coordinates.

The following example show how to extract table marked with Square Annotation:

```java
public static void Extract_Marked_Table() {
    // Load source PDF document
    String filePath = "<... enter path to pdf file here ...>";
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);
    com.aspose.pdf.Page page = pdfDocument.getPages().get_Item(1);

    com.aspose.pdf.AnnotationSelector annotationSelector = new com.aspose.pdf.AnnotationSelector(
            new com.aspose.pdf.SquareAnnotation(page, com.aspose.pdf.Rectangle.getTrivial()));

    java.util.List<com.aspose.pdf.Annotation> list = annotationSelector.getSelected();
    if (list.size() == 0) {
        System.out.println("Marked tables not found..");
        return;
    }

    com.aspose.pdf.SquareAnnotation squareAnnotation = (com.aspose.pdf.SquareAnnotation) list.get(0);

    com.aspose.pdf.TableAbsorber absorber = new com.aspose.pdf.TableAbsorber();
    absorber.visit(page);

    for (com.aspose.pdf.AbsorbedTable table : absorber.getTableList()) {
        {
            boolean isInRegion = (squareAnnotation.getRect().getLLX() < table.getRectangle().getLLX())
                    && (squareAnnotation.getRect().getLLY() < table.getRectangle().getLLY())
                    && (squareAnnotation.getRect().getURX() > table.getRectangle().getURX())
                    && (squareAnnotation.getRect().getURY() > table.getRectangle().getURY());

            if (isInRegion) {
                for (com.aspose.pdf.AbsorbedRow row : table.getRowList()) {
                    {
                        for (com.aspose.pdf.AbsorbedCell cell : row.getCellList()) {
                            for (com.aspose.pdf.TextFragment fragment : cell.getTextFragments()) {
                                StringBuilder sb = new StringBuilder();
                                for (com.aspose.pdf.TextSegment seg : fragment.getSegments())
                                    sb.append(seg.getText());
                                System.out.print(sb.toString() + "|");
                            }
                        }
                        System.out.println();
                    }
                }
            }
        }
    }
}
```

## Extract Table Data from PDF and store it in CSV file

The following example shows how to extract table and store it as CSV file.
To see how to convert PDF to Excel Spreadsheet please refer to [Convert PDF to Excel](/pdf/java/convert-pdf-to-excel/) article.

```java
public static void Extract_Table_Save_CSV()
{
    String filePath = "/home/admin1/pdf-examples/Samples/sample_table.pdf";
    // Load PDF document
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);

    // Instantiate ExcelSave Option object
    com.aspose.pdf.ExcelSaveOptions excelSave = new com.aspose.pdf.ExcelSaveOptions();
    excelSave.setFormat(com.aspose.pdf.ExcelSaveOptions.ExcelFormat.CSV);

    // Save the output in XLS format
    pdfDocument.save("PDFToXLS_out.xlsx", excelSave);
}
```
