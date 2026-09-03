---
title: Extraer datos de una tabla en PDF con Java
linktitle: Extraer datos de la tabla
type: docs
weight: 40
url: /java/extract-data-from-table-in-pdf/
description: Aprenda a extraer datos de tablas de archivos PDF con Aspose.PDF para Java y exporte tablas detectadas para su posterior procesamiento.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo extraer datos de una tabla en PDF a través de Java
Abstract: Este artículo explica cómo extraer y procesar datos de tablas de documentos PDF con Aspose.PDF para Java. Muestra cómo escanear páginas con `TableAbsorber`, leer filas y celdas de tablas detectadas, limitar la extracción a una región anotada específica y exportar el resultado a Excel.
---
## Extraer tablas de PDF



Utilice `TableAbsorber` para buscar tablas en cada página e iterar a través de filas, celdas, fragmentos de texto y segmentos de texto.


1. Abra el PDF de origen en una instancia de [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Itere a través de los objetos del documento [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) porque las tablas se detectan página por página.

1. Cree un [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/) para cada página y llame a `visit(page)` para completar la lista de tablas detectadas.
1. Itere a través de los objetos detectados [AbsorbedTable](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedtable/), [AbsorbedRow](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedrow/), [AbsorbedCell](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedcell/), [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) y `TextSegment`.

1. Cree el texto de la fila extraído del contenido del fragmento e imprima los datos de la tabla.


```java
public static void extractTablesFromPdf(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Page page : document.getPages()) {
            TableAbsorber absorber = new TableAbsorber();
            absorber.visit(page);

            for (AbsorbedTable table : absorber.getTableList()) {
                System.out.println("Table");
                for (AbsorbedRow row : table.getRowList()) {
                    StringBuilder rowText = new StringBuilder();
                    for (AbsorbedCell cell : row.getCellList()) {
                        if (rowText.length() > 0) {
                            rowText.append("|");
                        }
                        StringBuilder cellText = new StringBuilder();
                        for (TextFragment fragment : cell.getTextFragments()) {
                            StringBuilder fragmentText = new StringBuilder();
                            for (TextSegment segment : fragment.getSegments()) {
                                fragmentText.append(segment.getText());
                            }
                            if (cellText.length() > 0) {
                                cellText.append("|");
                            }
                            cellText.append(fragmentText);
                        }
                        rowText.append(cellText);
                    }
                    System.out.println(rowText);
                }
            }
        }
    }
}
```

## 
Extraer una tabla de un área marcada específica



Este ejemplo busca una anotación cuadrada, compara su rectángulo con cada tabla detectada y genera solo tablas dentro de la región marcada.


1. Abra el PDF de origen en una instancia de [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Obtenga la [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) de destino y ubique el cuadrado [Anotación](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) que marca la región de extracción.

1. Cree un [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/) y llame a `visit(page)` para detectar tablas en esa página.

1. Compare cada [Tabla Absorbida](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedtable/) [Rectángulo](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) detectada con los límites del rectángulo de anotación.

1. Itere a través de los objetos [AbsorbedRow](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedrow/) y [AbsorbedCell](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedcell/) coincidentes y reconstruya el texto de la fila.

1. Imprima los datos de la tabla solo para la región marcada.

```java
public static void extractTableFromSpecificArea(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        Annotation squareAnnotation = null;
        for (Annotation annotation : page.getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Square) {
                squareAnnotation = annotation;
                break;
            }
        }

        if (squareAnnotation == null) {
            System.out.println("No square annotation found.");
            return;
        }

        TableAbsorber absorber = new TableAbsorber();
        absorber.visit(page);

        for (AbsorbedTable table : absorber.getTableList()) {
            Rectangle tableRect = table.getRectangle();
            Rectangle annotationRect = squareAnnotation.getRect();

            boolean isInRegion = annotationRect.getLLX() < tableRect.getLLX()
                    && annotationRect.getLLY() < tableRect.getLLY()
                    && annotationRect.getURX() > tableRect.getURX()
                    && annotationRect.getURY() > tableRect.getURY();

            if (isInRegion) {
                for (AbsorbedRow row : table.getRowList()) {
                    StringBuilder rowText = new StringBuilder();
                    for (AbsorbedCell cell : row.getCellList()) {
                        if (rowText.length() > 0) {
                            rowText.append("|");
                        }
                        StringBuilder cellText = new StringBuilder();
                        for (TextFragment fragment : cell.getTextFragments()) {
                            StringBuilder fragmentText = new StringBuilder();
                            for (TextSegment segment : fragment.getSegments()) {
                                fragmentText.append(segment.getText());
                            }
                            if (cellText.length() > 0) {
                                cellText.append("|");
                            }
                            cellText.append(fragmentText);
                        }
                        rowText.append(cellText);
                    }
                    System.out.println(rowText);
                }
            }
        }
    }
}
```

## Exportar tablas a Excel


1. Abra el PDF de origen en una instancia de [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Cree [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) para la exportación.

1. Establezca el formato de salida de Excel en `XLSX` para que el diseño de la tabla detectada se escriba como un libro de Excel.

1. Llame a `document.save(outputFile.toString(), excelSave)` para exportar el documento en formato Excel.

```java
public static void exportTablesToExcel(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions excelSave = new ExcelSaveOptions();
        excelSave.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);
        document.save(outputFile.toString(), excelSave);
    }
}
```
