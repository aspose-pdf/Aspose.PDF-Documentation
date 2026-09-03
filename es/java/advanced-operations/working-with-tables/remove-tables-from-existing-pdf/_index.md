---
title: Eliminar tablas de documentos PDF existentes
linktitle: Eliminar tablas
description: Aprenda cómo eliminar una o más tablas de documentos PDF existentes en Java.
lastmod: "2026-09-03"
type: docs
weight: 50
url: /es/java/removing-tables/
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Eliminar una o varias tablas de archivos PDF con Java
Abstract: Este artículo explica cómo eliminar tablas de documentos PDF existentes usando Aspose.PDF for Java. Presenta TableAbsorber para localizar tablas y muestra cómo eliminar una tabla individual o eliminar todas las tablas detectadas de una página.
---
Usar `TableAbsorber` cuando necesites eliminar una o más tablas detectadas de un PDF existente.

## Eliminar una tabla detectada

Utilice este ejemplo cuando solo la primera tabla coincidente en una página deba eliminarse.

1. Abrir el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
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

## Eliminar todas las tablas detectadas de una página

Utilice este ejemplo cuando se debe eliminar cada tabla coincidente en la página.

1. Abrir el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Visite la página de destino con [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/) y copie las tablas detectadas a una lista.
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
