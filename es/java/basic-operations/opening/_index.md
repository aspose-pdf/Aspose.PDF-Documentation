---
title: Abrir documento PDF programáticamente
linktitle: Abrir PDF
type: docs
weight: 20
url: /es/java/open-pdf-document/
description: Aprende cómo abrir un archivo PDF en Java utilizando Aspose.PDF desde una ruta de archivo, un flujo o con una contraseña.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Abrir documentos PDF usando la biblioteca Aspose.PDF en Java
Abstract: Este artículo muestra cómo abrir documentos PDF existentes en Java usando Aspose.PDF. Cubre la apertura de un PDF por ruta de archivo, la apertura de un PDF desde un InputStream y la apertura de un documento protegido con contraseña, con cada ejemplo leyendo el recuento de páginas del documento cargado.
---
Aspose.PDF for Java admite varias formas de cargar un documento PDF existente según de dónde provengan los datos de origen.

## Abrir un documento PDF en Java

Puedes abrir un documento PDF:

1. Abrir un [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) directamente desde una ruta de archivo.
1. Abrir un [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) de un `InputStream`.
1. Abrir un cifrado [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) proporcionando la contraseña.

## Abrir documento desde archivo

```java
public static void openDocumentFromFile(Path inputFile) {
    Document document = new Document(inputFile.toString());
    System.out.println("Pages: " + document.getPages().size());
    document.close();
}
```

## Abrir documento desde stream

```java
public static void openDocumentFromStream(Path inputFile) throws Exception {
    try (InputStream stream = Files.newInputStream(inputFile)) {
        Document document = new Document(stream);
        System.out.println("Pages: " + document.getPages().size());
        document.close();
    }
}
```

## Abrir un documento cifrado

```java
public static void openDocumentEncrypted(Path inputFile) {
    Document document = new Document(inputFile.toString(), "P@ssw0rd");
    System.out.println("Pages: " + document.getPages().size());
    document.close();
}
```
