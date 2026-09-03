---
title: Extraer datos de tabla en PDF con Java
linktitle: Extraer datos de tabla
type: docs
weight: 40
url: /es/java/extract-data-from-table-in-pdf/
description: Aprenda cómo extraer datos de tabla de archivos PDF con Aspose.PDF for Java y exportar las tablas detectadas para su posterior procesamiento.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo extraer datos de tabla en PDF mediante Java
Abstract: Este artículo explica cómo extraer y procesar datos de tablas de documentos PDF con Aspose.PDF for Java. Muestra cómo escanear páginas con `TableAbsorber`, leer filas y celdas de las tablas detectadas, limitar la extracción a una región anotada específica y exportar el resultado a Excel.
---
## Extraer tablas de PDF

Usar `TableAbsorber` para encontrar tablas en cada página e iterar a través de filas, celdas, fragmentos de texto y segmentos de texto.

1. Abra el PDF de origen en un [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instancia.
1. Iterar a través del documento [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) objetos porque las tablas se detectan página por página.
1. Crear un [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/) para cada página y llame `visit(page)` para rellenar la lista de tablas detectadas.
1. Iterar a través de lo detectado [AbsorbedTable](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedtable/), [AbsorbedRow](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedrow/), [AbsorbedCell](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedcell/), [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/), y `TextSegment` objetos.
1. Construya el texto de la fila extraído del contenido del fragmento e imprima los datos de la tabla.

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

## Extraer una tabla de un área marcada específica

Este ejemplo encuentra una anotación cuadrada, compara su rectángulo con cada tabla detectada y devuelve solo las tablas dentro de la región marcada.

1. Abra el PDF de origen en un [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instancia.
1. Obtenga el objetivo [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) y localice el cuadrado [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) que marca la región de extracción.
1. Crear un [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/) y llamar `visit(page)` para detectar tablas en esa página.
1. Compare cada detectado [AbsorbedTable](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedtable/) [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) con los límites del rectángulo de anotación.
1. Iterar a través de la coincidencia [AbsorbedRow](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedrow/) y [AbsorbedCell](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedcell/) objetos y reconstruir el texto de la fila.
1. Imprimir los datos de la tabla solo para la región marcada.

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

1. Abra el PDF de origen en un [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instancia.
1. Crear [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) para la exportación.
1. Establezca el formato de salida de Excel a `XLSX` por lo tanto, el diseño de tabla detectado se escribe como un libro de Excel.
1. Llamar `document.save(outputFile.toString(), excelSave)` para exportar el documento en formato Excel.

```java
public static void exportTablesToExcel(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions excelSave = new ExcelSaveOptions();
        excelSave.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);
        document.save(outputFile.toString(), excelSave);
    }
}
```
