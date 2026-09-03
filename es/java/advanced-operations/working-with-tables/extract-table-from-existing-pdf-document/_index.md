---
title: Extraer tablas de PDF en Java
linktitle: Extraer tabla
type: docs
weight: 20
url: /java/extracting-table/
description: Aprenda a extraer datos de tablas de documentos PDF existentes en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraiga datos de tablas de archivos PDF con Java
Abstract: Este artículo explica cómo extraer tablas de documentos PDF usando Aspose.PDF para Java. Muestra cómo utilizar TableAbsorber para detectar tablas por página, iterar filas y celdas y recopilar texto de celda para su procesamiento posterior.
---
Utilice `TableAbsorber` cuando necesite detectar estructuras de tablas en un PDF existente y leer su contenido.


## 
Extraer texto de tablas detectadas



Utilice este ejemplo cuando necesite ubicar tablas en cada página y recopilar el texto de sus celdas.


1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Visite cada página con [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/).
1. Itere a través de tablas, filas y celdas absorbidas y luego genere el texto extraído.

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
