---
title: Agregar numeración Bates al PDF en Java
linktitle: Agregando numeración Bates
type: docs
weight: 10
url: /es/java/add-bates-numbering/
description: Aprenda cómo agregar y eliminar numeración Bates en documentos PDF usando Java con Aspose.PDF.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar numeración Bates mediante Java
Abstract: Este artículo explica cómo crear y eliminar artefactos de numeración Bates en documentos PDF usando Aspose.PDF for Java. Cubre la configuración de un `BatesNArtifact`, su aplicación mediante asistentes de numeración Bates o asistentes genéricos de paginación, y la eliminación de la numeración Bates de un documento.
---
Los artefactos de numeración Bates son útiles en flujos de trabajo legales, de archivo y de control de documentos donde cada página necesita un identificador persistente a nivel de página.

## Agregar numeración Bates con el asistente dedicado

Utilice este ejemplo cuando desee aplicar la numeración Bates mediante el asistente dedicado de colección de páginas.

1. Abra el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y añada cualquier página extra requerida por el ejemplo.
1. Cree el [BatesNArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/batesnartifact/) configuración.
1. Aplicar la numeración Bates a la colección de páginas y guardar el archivo de salida.

```java
public static void addBatesNArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = 0; i < 2; i++) {
            document.getPages().add();
        }

        BatesNArtifact batesArtifact = createBatesArtifact();
        PageCollectionExtensions.addBatesNumbering(document.getPages(), batesArtifact);
        document.save(outputFile.toString());
    }
}
```

## Agregar numeración Bates a través de artefactos de paginación

Este ejemplo aplica la numeración Bates pasando el artefacto Bates a través de la API genérica de paginación.

1. Abra el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y agrega las páginas requeridas.
1. Cree el [BatesNArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/batesnartifact/) y agrégalo a una lista de artefactos de paginación.
1. Aplica los artefactos de paginación a la colección de páginas y guarda el documento.

```java
public static void addBatesNArtifactPagination(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = 0; i < 2; i++) {
            document.getPages().add();
        }

        BatesNArtifact batesArtifact = createBatesArtifact();
        List<PaginationArtifact> paginationArtifacts = new ArrayList<>();
        paginationArtifacts.add(batesArtifact);
        PageCollectionExtensions.addPagination(document.getPages(), paginationArtifacts);
        document.save(outputFile.toString());
    }
}
```

## Eliminar la numeración Bates

Utilice este enfoque cuando los artefactos de numeración Bates existentes deban eliminarse del documento.

1. Abra el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
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
