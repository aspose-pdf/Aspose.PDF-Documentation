---
title: Extraer tablas de PDF en Java
linktitle: Extraer tabla
type: docs
weight: 20
url: /es/java/extracting-table/
description: Aprenda cómo extraer datos de tablas de documentos PDF existentes en Java.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraiga datos de tablas de archivos PDF con Java
Abstract: Este artículo explica cómo extraer tablas de documentos PDF usando Aspose.PDF for Java. Muestra cómo usar TableAbsorber para detectar tablas por página, iterar filas y celdas, y recopilar el texto de las celdas para el procesamiento posterior.
---
Usar `TableAbsorber` cuando necesitas detectar estructuras de tabla en un PDF existente y leer su contenido.

## Extraer texto de tablas detectadas

Utilice este ejemplo cuando necesite localizar tablas en cada página y recopilar el texto de sus celdas.

1. Abrir el PDF fuente [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Visitar cada página con [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/).
1. Iterar a través de las tablas absorbidas, filas y celdas, y luego generar el texto extraído.

```java
public static void extract(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Page page : document.getPages()) {
            TableAbsorber absorber = new TableAbsorber();
            absorber.visit(page);
            for (AbsorbedTable table : absorber.getTableList()) {
                System.out.println("Table ----");
                for (AbsorbedRow row : table.getRowList()) {
                    System.out.println("Row:");
                    StringBuilder rowText = new StringBuilder();
                    for (AbsorbedCell cell : row.getCellList()) {
                        StringBuilder cellText = new StringBuilder();
                        for (TextFragment fragment : cell.getTextFragments()) {
                            for (TextSegment segment : fragment.getSegments()) {
                                cellText.append(segment.getText());
                            }
                        }
                        rowText.append(" | ").append(cellText);
                    }
                    System.out.println(rowText);
                }
            }
        }
    }
}
```
