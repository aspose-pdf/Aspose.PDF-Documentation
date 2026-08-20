---
title: Crear carteras PDF en Java
linktitle: Portafolio
type: docs
weight: 20
url: /java/portfolio/
description: Aprenda a crear y administrar carteras de PDF en Java usando Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cree y edite portafolios PDF con archivos incrustados en Java
Abstract: Este artículo explica cómo crear y administrar carteras de PDF utilizando Aspose.PDF para Java. Aprenda cómo habilitar una colección en un documento, agregar varios tipos de archivos al portafolio y eliminar todos los elementos de la colección de un portafolio PDF existente.
---
Un portafolio de PDF puede agrupar varios archivos dentro de un único contenedor de PDF y al mismo tiempo preservar cada archivo en su formato original.


## 
Crear un portafolio en PDF



Utilice este ejemplo cuando necesite empaquetar varios archivos en una colección de portafolios en PDF.


1. 
Cree un nuevo [Documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y habilite su [Colección](https://reference.aspose.com/pdf/java/com.aspose.pdf/collection/).

1. 
Cree objetos [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) para cada archivo de entrada y establezca sus descripciones.
1. Agregue los archivos a la colección de cartera y guarde el documento de salida.


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

## 
Eliminar archivos de un portafolio PDF



Utilice este ejemplo cuando deba borrarse una colección de portafolios en PDF existente.


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Elimine las entradas de la colección de documentos.
1. Guarde el documento de salida limpio.

```java
public static void removeFilesFromPdfPortfolio(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getCollection().delete();
        document.save(outputFile.toString());
    }
}
```
