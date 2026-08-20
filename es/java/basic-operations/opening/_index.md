---
title: Abrir documento PDF mediante programación
linktitle: Abrir PDF
type: docs
weight: 20
url: /java/open-pdf-document/
description: Aprenda a abrir un archivo PDF en Java usando Aspose.PDF desde una ruta de archivo, una secuencia o con una contraseña.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Abrir documentos PDF usando la biblioteca Aspose.PDF en Java
Abstract: Este artículo muestra cómo abrir documentos PDF existentes en Java usando Aspose.PDF. Cubre la apertura de un PDF por ruta de archivo, la apertura de un PDF desde un InputStream y la apertura de un documento protegido con contraseña, y cada ejemplo lee el recuento de páginas del documento cargado.
---
Aspose.PDF para Java admite varias formas de cargar un documento PDF existente dependiendo de dónde provienen los datos de origen.


## 
Abrir un documento PDF en Java



Puede abrir un documento PDF:


1. 
Abra un [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) directamente desde una ruta de archivo.

1. 
Abra un [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) de un `InputStream`.
1. Abra un [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) cifrado proporcionando la contraseña.


## 
Abrir documento desde archivo


```java
public static void openDocumentFromFile(Path inputFile) {
    Document document = new Document(inputFile.toString());
    System.out.println("Pages: " + document.getPages().size());
    document.close();
}
```

## 
Abrir documento desde la secuencia


```java
public static void openDocumentFromStream(Path inputFile) throws Exception {
    try (InputStream stream = Files.newInputStream(inputFile)) {
        Document document = new Document(stream);
        System.out.println("Pages: " + document.getPages().size());
        document.close();
    }
}
```

## 
Abrir un documento cifrado

```java
public static void openDocumentEncrypted(Path inputFile) {
    Document document = new Document(inputFile.toString(), "P@ssw0rd");
    System.out.println("Pages: " + document.getPages().size());
    document.close();
}
```
