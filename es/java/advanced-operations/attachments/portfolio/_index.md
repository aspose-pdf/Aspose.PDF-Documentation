---
title: Crear portafolios PDF en Java
linktitle: Portafolio
type: docs
weight: 20
url: /es/java/portfolio/
description: Aprenda a crear y administrar portafolios PDF en Java usando Aspose.PDF.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Crear y editar portafolios PDF con archivos incrustados en Java
Abstract: Este artículo explica cómo crear y administrar portafolios PDF usando Aspose.PDF for Java. Aprenda cómo habilitar una colección en un documento, agregar varios tipos de archivos al portafolio y eliminar todos los elementos de la colección de un portafolio PDF existente.
---
Un portafolio PDF puede agrupar varios archivos dentro de un único contenedor PDF mientras conserva cada archivo en su formato original.

## Crear un portafolio PDF

Utilice este ejemplo cuando necesite empaquetar varios archivos en una colección de portafolio PDF.

1. Cree un nuevo PDF [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y habilite su [`Collection`](https://reference.aspose.com/pdf/java/com.aspose.pdf/collection/).
1. Cree [`FileSpecification`](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) objetos para cada archivo de entrada y establezca sus descripciones.
1. Añada los archivos a la colección de portafolio y guarde el documento de salida.

```java
public static void createPdfPortfolio(Path[] inputFiles, Path outputFile) {
    try (Document document = new Document()) {
        document.setCollection(new Collection());

        FileSpecification excel = new FileSpecification(inputFiles[0].toString());
        FileSpecification word = new FileSpecification(inputFiles[1].toString());
        FileSpecification image = new FileSpecification(inputFiles[2].toString());

        excel.setDescription("Excel File");
        word.setDescription("Word File");
        image.setDescription("Image File");

        document.getCollection().add(excel);
        document.getCollection().add(word);
        document.getCollection().add(image);

        document.save(outputFile.toString());
    }
}
```

## Eliminar archivos de un portafolio PDF

Utilice este ejemplo cuando se deba limpiar una colección de portafolios PDF existente.

1. Abra el PDF de origen [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Elimine las entradas de la colección de documentos.
1. Guarde el documento de salida limpiado.

```java
public static void removeFilesFromPdfPortfolio(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getCollection().delete();
        document.save(outputFile.toString());
    }
}
```
