---
title: Open PDF document programmatically
linktitle: Open PDF
type: docs
weight: 20
url: /java/open-pdf-document/
description: Learn how to open a PDF file in Java using Aspose.PDF from a file path, a stream, or with a password.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Abrir documentos PDF usando la biblioteca Aspose.PDF en Java
Abstract: Este artículo muestra cómo abrir documentos PDF existentes en Java usando Aspose.PDF. Cubre la apertura de un PDF por ruta de archivo, la apertura de un PDF desde un InputStream y la apertura de un documento protegido con contraseña, y cada ejemplo lee el recuento de páginas del documento cargado.
---
Aspose.PDF para Java admite varias formas de cargar un documento PDF existente dependiendo de dónde provienen los datos de origen.

## Abrir un documento PDF en Java

You can open a PDF document:

1. Open a [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) directly from a file path.
1. Open a [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) from an `InputStream`.
1. Open an encrypted [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) by supplying the password.

## Open document from file

```java
public static void openDocumentFromFile(Path inputFile) {
    Document document = new Document(inputFile.toString());
    System.out.println("Pages: " + document.getPages().size());
    document.close();
}
```

## Open document from stream

```java
public static void openDocumentFromStream(Path inputFile) throws Exception {
    try (InputStream stream = Files.newInputStream(inputFile)) {
        Document document = new Document(stream);
        System.out.println("Pages: " + document.getPages().size());
        document.close();
    }
}
```

## Open an encrypted document

```java
public static void openDocumentEncrypted(Path inputFile) {
    Document document = new Document(inputFile.toString(), "P@ssw0rd");
    System.out.println("Pages: " + document.getPages().size());
    document.close();
}
```
