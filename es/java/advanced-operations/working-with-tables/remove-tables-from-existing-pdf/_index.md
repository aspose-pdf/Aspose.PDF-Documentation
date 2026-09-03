---
title: Eliminar tablas de documentos PDF existentes
linktitle: Quitar tablas
description: Aprenda cómo eliminar una o más tablas de documentos PDF existentes en Java.
lastmod: "2026-06-09"
type: docs
weight: 50
url: /java/removing-tables/
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Elimine una o varias tablas de archivos PDF con Java
Abstract: Este artículo explica cómo eliminar tablas de documentos PDF existentes usando Aspose.PDF para Java. Presenta TableAbsorber para localizar tablas y demuestra cómo eliminar una sola tabla o eliminar todas las tablas detectadas de una página.
---
Utilice `TableAbsorber` cuando necesite eliminar una o más tablas detectadas de un PDF existente.


## 
Eliminar una tabla detectada



Utilice este ejemplo cuando solo se deba eliminar la primera tabla coincidente de una página.


1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Visite la página de destino con [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/).
1. Elimine la primera tabla detectada y guarde el documento.


```java
public static void removeOneTable(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TableAbsorber absorber = new TableAbsorber();
        absorber.visit(document.getPages().get_Item(1));
        absorber.remove(absorber.getTableList().get(0));
        document.save(outputFile.toString());
    }
}
```

## 
Eliminar todas las tablas detectadas de una página



Utilice este ejemplo cuando se deban eliminar todas las tablas coincidentes de la página.


1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Visite la página de destino con [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/) y copie las tablas detectadas en una lista.
1. Elimine cada tabla detectada y guarde el PDF actualizado.

```java
public static void removeAllTables(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TableAbsorber absorber = new TableAbsorber();
        absorber.visit(document.getPages().get_Item(1));
        List<AbsorbedTable> tables = new ArrayList<>(absorber.getTableList());
        for (AbsorbedTable table : tables) {
            absorber.remove(table);
        }
        document.save(outputFile.toString());
    }
}
```
