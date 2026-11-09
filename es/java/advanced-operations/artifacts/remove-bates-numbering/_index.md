---
title: Eliminar la numeración Bates de PDF en Java
linktitle: Eliminar numeración Bates
type: docs
weight: 100
url: /es/java/remove-bates-numbering/
description: Eliminar la numeración Bates de todas las páginas de un PDF en Java.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Eliminar la numeración Bates en Java
Abstract: Eliminar la numeración Bates de todas las páginas de un PDF en Java.
---
Eliminar la numeración Bates de todas las páginas de un PDF en Java.

## Eliminar numeración Bates

Utilice este enfoque cuando los artefactos de numeración Bates existentes deban eliminarse del documento.

1. Abra el PDF de origen con [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Llame al asistente de colección de páginas que elimina la numeración Bates.
1. Guarde el archivo de salida limpiado.

```java
public static void deleteBatesNumbering(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PageCollectionExtensions.deleteBatesNumbering(document.getPages());
        document.save(outputFile.toString());
    }
}
```

## Temas relacionados

- [Agregar numeración Bates](/pdf/es/java/add-bates-numbering/)
- [Trabajar con artefactos PDF en Java](/pdf/es/java/artifacts/)
