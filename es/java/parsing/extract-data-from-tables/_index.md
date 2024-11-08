---
title: Extraer Datos de Tabla desde PDF 
linktitle: Extraer Datos de Tabla
type: docs
weight: 40
url: /es/java/extract-data-from-table-in-pdf/
description: Aprende cómo extraer datos tabulares de PDF usando Aspose.PDF para Java
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extraer Tablas de PDF programáticamente

Extraer tablas de PDFs no es una tarea trivial porque la tabla puede ser creada de diversas maneras.

Aspose.PDF para Java tiene una herramienta que facilita la recuperación de tablas. Para extraer datos de tablas, debes realizar los siguientes pasos:

1. Abrir documento - instanciar un objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document);
1. Crear un objeto [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber).

1. Decide qué páginas se analizarán y aplica [visit](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#visit-com.aspose.pdf.Page-) a las páginas deseadas. Los datos tabulares serán escaneados y el resultado se guardará en una lista de [AbsorbedTable](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedTable). Podemos obtener esta lista a través del método [getTableList](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#getTableList--).
1. Para obtener los datos, itera a través de `TableList` y maneja la lista de [absorbed rows](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedRow) y la lista de celdas absorbidas. Podemos acceder a la primera lista llamando al método [getTableList](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#getTableList--) y a la segunda llamando al método [getCellList](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedRow#getCellList--).

1. Cada [AbsorbedCell](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedCell) contiene [TextFragmentCollections](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentCollection). Puedes procesarlo para tus propios propósitos.

El siguiente ejemplo muestra la extracción de tablas de todas las páginas:

```java
public static void Extract_Table() {
    // Cargar documento PDF de origen        
    String filePath = "/home/aspose/pdf-examples/Samples/sample_table.pdf";
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);
    com.aspose.pdf.TableAbsorber absorber = new com.aspose.pdf.TableAbsorber();

    // Escanear páginas
    for (com.aspose.pdf.Page page : pdfDocument.getPages()) {
        absorber.visit(page);
        for (com.aspose.pdf.AbsorbedTable table : absorber.getTableList()) {
            System.out.println("Table");
            // Iterar a través de la lista de filas
            for (com.aspose.pdf.AbsorbedRow row : table.getRowList()) {
                // Iterar a través de la lista de celdas
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
```


## Extraer tabla en área específica de la página PDF

Cada tabla absorbida tiene la propiedad [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedTable#getRectangle--) que describe la posición de la tabla en la página.

Por lo tanto, si necesitas extraer tablas ubicadas en una región específica, debes trabajar con coordenadas específicas.

El siguiente ejemplo muestra cómo extraer una tabla marcada con Anotación Cuadrada:

```java
public static void Extract_Marked_Table() {
    // Cargar documento PDF fuente
    String filePath = "<... enter path to pdf file here ...>";
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);
    com.aspose.pdf.Page page = pdfDocument.getPages().get_Item(1);

    com.aspose.pdf.AnnotationSelector annotationSelector = new com.aspose.pdf.AnnotationSelector(
            new com.aspose.pdf.SquareAnnotation(page, com.aspose.pdf.Rectangle.getTrivial()));

    java.util.List<com.aspose.pdf.Annotation> list = annotationSelector.getSelected();
    if (list.size() == 0) {
        System.out.println("Tablas marcadas no encontradas...");
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


## Extraer Datos de Tabla de PDF y almacenarlos en archivo CSV

El siguiente ejemplo muestra cómo extraer una tabla y almacenarla como archivo CSV. Para ver cómo convertir PDF a Hoja de Cálculo de Excel, por favor consulte el artículo [Convertir PDF a Excel](/pdf/es/java/convert-pdf-to-excel/).

```java
public static void Extract_Table_Save_CSV()
{
    String filePath = "/home/admin1/pdf-examples/Samples/sample_table.pdf";
    // Cargar documento PDF
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);

    // Instanciar objeto de opción de guardado en Excel
    com.aspose.pdf.ExcelSaveOptions excelSave = new com.aspose.pdf.ExcelSaveOptions();
    excelSave.setFormat(com.aspose.pdf.ExcelSaveOptions.ExcelFormat.CSV);

    // Guardar salida en formato XLS
    pdfDocument.save("PDFToXLS_out.xlsx", excelSave);
}
```