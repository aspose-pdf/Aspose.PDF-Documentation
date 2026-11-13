---
title: Agregar numeración Bates a PDF en Java
linktitle: Agregar numeración Bates
type: docs
weight: 10
url: /es/java/add-bates-numbering/
description: Agregar identificadores Bates secuenciales a las páginas PDF en Java con el asistente dedicado de numeración Bates o la API genérica de paginación.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar numeración Bates en Java
Abstract: Agregar identificadores Bates secuenciales a las páginas PDF en Java con el asistente dedicado de numeración Bates o la API genérica de paginación.
---
Los artefactos de numeración Bates son útiles en flujos de trabajo legales, archivísticos y de control de documentos donde cada página necesita un identificador persistente a nivel de página.

## Agregar numeración Bates con el asistente dedicado

Utilice este ejemplo cuando desee aplicar la numeración Bates mediante el asistente dedicado de colección de páginas.

1. Abra el PDF de origen con [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y agregue cualquier página adicional requerida por el ejemplo.
1. Configure un objeto [BatesNArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/batesnartifact/).
1. Aplique numeración Bates a la colección de páginas y guarde el archivo de salida.

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

1. Abra el PDF de origen con [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y agrega las páginas requeridas.
1. Cree el [BatesNArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/batesnartifact/) y agréguelo a una lista de artefactos de paginación.
1. Aplique los artefactos de paginación a la colección de páginas y guarde el documento.

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

## Temas relacionados

- [Eliminar numeración Bates](/pdf/es/java/remove-bates-numbering/)
- [Trabajar con artefactos PDF en Java](/pdf/es/java/artifacts/)
