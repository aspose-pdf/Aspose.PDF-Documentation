---
title: Trabajar con metadatos de archivos PDF en Java
linktitle: Metadatos de archivos PDF
type: docs
weight: 200
url: /es/java/pdf-file-metadata/
description: Aprenda cómo extraer, actualizar y administrar los metadatos de archivos PDF, la información del documento y las propiedades XMP en Java usando Aspose.PDF.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Obtener y establecer la información del documento PDF y los metadatos XMP en Java
Abstract: Este artículo explica cómo trabajar con los metadatos de PDF usando Aspose.PDF for Java. Aprende cómo leer la información del documento como autor, título y palabras clave, actualizar las propiedades del archivo, inspeccionar la versión y los privilegios del PDF, establecer campos de metadatos XMP y guardar los metadatos tanto a través de la API DOM como de la API de fachada.
---
Aspose.PDF for Java ofrece dos formas principales de trabajar con metadatos:

- La API DOM a través `Document`, `DocumentInfo`, y `document.getMetadata()`.
- La API de fachada a través `PdfFileInfo`.

## Obtener información del archivo PDF

Utilice este ejemplo cuando necesite leer los campos de información estándar del documento, como autor, título, asunto o palabras clave.

1. Abrir el PDF fuente [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Acceder al [DocumentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/documentinfo/) objeto.
1. Lea los campos de metadatos requeridos y muestre sus valores.

```java
public static void getPdfFileInformation(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocumentInfo docInfo = document.getInfo();

        System.out.println("Author: " + docInfo.getAuthor());
        System.out.println("Creation Date: " + docInfo.getCreationDate());
        System.out.println("Keywords: " + docInfo.getKeywords());
        System.out.println("Modify Date: " + docInfo.getModDate());
        System.out.println("Subject: " + docInfo.getSubject());
        System.out.println("Title: " + docInfo.getTitle());
    }
}
```

## Establecer metadatos con un prefijo de espacio de nombres

Utilice este ejemplo cuando necesite agregar o actualizar una propiedad XMP usando un prefijo de espacio de nombres registrado.

1. Abrir el PDF fuente [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Registre el espacio de nombres XMP requerido y agregue el elemento de metadatos.
1. Guarde el documento actualizado.

```java
public static void setPrefixMetadata(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getMetadata().registerNamespaceUri("xmp", "http://ns.adobe.com/xap/1.0/");
        document.getMetadata().addItem("xmp:ModifyDate", OffsetDateTime.now().toString());
        document.save(outputFile.toString());
    }
    System.out.println("Prefix metadata saved to " + outputFile);
}
```

## Actualizar campos de información del documento

Utilice este ejemplo cuando desee escribir propiedades estándar de archivo PDF como autor, título, productor o fecha de creación.

1. Abrir el PDF fuente [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Acceso [DocumentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/documentinfo/) y asigne nuevos valores de metadatos.
1. Guarde el documento con la información de archivo actualizada.

```java
public static void setFileInformation(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocumentInfo docInfo = document.getInfo();
        Date now = new Date();

        docInfo.setAuthor("Aspose");
        docInfo.setCreationDate(now);
        docInfo.setKeywords("Aspose.Pdf, DOM, API");
        docInfo.setModDate(now);
        docInfo.setSubject("PDF Information");
        docInfo.setTitle("Setting PDF Document Information");
        docInfo.setProducer("Custom producer");
        docInfo.setCreator("Custom creator");

        document.save(outputFile.toString());
    }
    System.out.println("File information saved to " + outputFile);
}
```

## Establecer propiedades de metadatos XMP

Utilice este ejemplo cuando necesite almacenar entradas XMP adicionales, incluidos valores de metadatos personalizados.

1. Abrir el PDF fuente [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Agregar los elementos de metadatos XMP requeridos a través de `document.getMetadata()`.
1. Guarde el archivo de salida.

```java
public static void setXmpMetadata(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getMetadata().addItem("xmp:CreateDate", OffsetDateTime.now().toString());
        document.getMetadata().addItem("xmp:Nickname", "Nickname");
        document.getMetadata().addItem("xmp:CustomProperty", "Custom Value");
        document.save(outputFile.toString());
    }
    System.out.println("XMP metadata saved to " + outputFile);
}
```
