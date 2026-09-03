---
title: Agregar numeración Bates a PDF en Java
linktitle: Agregar numeración Bates
type: docs
weight: 10
url: /java/add-bates-numbering/
description: Aprenda cómo agregar y eliminar numeración Bates en documentos PDF usando Java con Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar numeración Bates a través de Java
Abstract: Este artículo explica cómo crear y eliminar artefactos de numeración Bates en documentos PDF utilizando Aspose.PDF para Java. Cubre la configuración de `BatesNArtifact`, su aplicación a través de ayudas de numeración Bates o ayudas de paginación genéricas y la eliminación de la numeración Bates de un documento.
---
Los artefactos de numeración Bates son útiles en flujos de trabajo legales, de archivo y de control de documentos donde cada página necesita un identificador persistente a nivel de página.


## 
Agregue numeración Bates con el ayudante dedicado



Utilice este ejemplo cuando desee aplicar la numeración Bates a través del asistente de colección de páginas dedicado.


1. Abra el [Documento] PDF de origen (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y agregue las páginas adicionales que requiera la muestra.

1. Cree la configuración [BatesNArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/batesnartifact/).
1. Aplique la numeración Bates a la colección de páginas y guarde el archivo de salida.


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

## 
Agregar numeración Bates a través de artefactos de paginación



Este ejemplo aplica la numeración Bates pasando el artefacto Bates a través de la API de paginación genérica.


1. Abra el [Documento] PDF de origen(https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y agregue las páginas requeridas.

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

## 
Eliminar numeración Bates



Utilice este enfoque cuando los artefactos de numeración Bates existentes deban eliminarse del documento.


1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Llame al ayudante de recopilación de páginas que elimina la numeración Bates.
1. Guarde el archivo de salida limpio.

```java
public static void deleteBatesNumbering(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PageCollectionExtensions.deleteBatesNumbering(document.getPages());
        document.save(outputFile.toString());
    }
}
```
