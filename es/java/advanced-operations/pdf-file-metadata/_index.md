---
title: Trabajar con metadatos de archivos PDF en Java
linktitle: Metadatos del archivo PDF
type: docs
weight: 200
url: /java/pdf-file-metadata/
description: Aprenda a extraer, actualizar y administrar metadatos de archivos PDF, información de documentos y propiedades XMP en Java usando Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Obtenga y configure información de documentos PDF y metadatos XMP en Java
Abstract: Este artículo explica cómo trabajar con metadatos PDF usando Aspose.PDF para Java. Aprenda a leer información del documento, como autor, título y palabras clave, actualizar las propiedades del archivo, inspeccionar la versión y los privilegios del PDF, configurar campos de metadatos XMP y guardar metadatos a través de las API DOM y de fachada.
---
Aspose.PDF para Java proporciona dos formas principales de trabajar con metadatos:


- La API DOM a través de `Document`, `DocumentInfo` y `document.getMetadata()`.

- La API de fachada a través de `PdfFileInfo`.


## 
Obtener información del archivo PDF



Utilice este ejemplo cuando necesite leer campos de información de documento estándar, como autor, título, asunto o palabras clave.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Acceda al objeto [DocumentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/documentinfo/).

1. Lea los campos de metadatos requeridos y genere sus valores.


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

## 
Establecer metadatos con un prefijo de espacio de nombres



Utilice este ejemplo cuando necesite agregar o actualizar una propiedad XMP mediante un prefijo de espacio de nombres registrado.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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

## 
Actualizar campos de información del documento



Utilice este ejemplo cuando desee escribir propiedades de archivos PDF estándar, como autor, título, productor o fecha de creación.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Acceda a [DocumentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/documentinfo/) y asigne nuevos valores de metadatos.

1. Guarde el documento con la información del archivo actualizada.


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

## 
Establecer propiedades de metadatos XMP



Utilice este ejemplo cuando necesite almacenar entradas XMP adicionales, incluidos valores de metadatos personalizados.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Agregue los elementos de metadatos XMP necesarios a través de `document.getMetadata()`.

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
