---
title: Eliminar archivos adjuntos de PDF en Java
linktitle: Eliminar un adjunto de un PDF existente
type: docs
weight: 30
url: /es/java/removing-attachment-from-an-existing-pdf/
description: Aprenda cómo eliminar uno o todos los archivos adjuntos incrustados de documentos PDF en Java usando Aspose.PDF.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Eliminar archivos adjuntos de PDF programáticamente con Java
Abstract: Este artículo muestra cómo eliminar archivos adjuntos de archivos PDF usando Aspose.PDF for Java. Los ejemplos demuestran cómo eliminar un archivo incrustado por clave y cómo limpiar toda la colección `EmbeddedFiles` antes de guardar el documento actualizado.
---
Los archivos adjuntos almacenados en un documento PDF pueden eliminarse individualmente o todos a la vez a través del `EmbeddedFiles` colección.

## Eliminar un solo adjunto

Utilice este ejemplo cuando se deba eliminar un archivo incrustado con nombre del PDF.

1. Abrir el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Eliminar el adjunto por su clave de la colección de archivos incrustados.
1. Guardar el documento de salida actualizado.

```java
public static void removeAttachment(Path inputFile, String attachmentName, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getEmbeddedFiles().deleteByKey(attachmentName);
        document.save(outputFile.toString());
    }
}
```

## Eliminar todos los archivos adjuntos

Utilice este enfoque cuando se deba limpiar toda la colección de archivos incrustados.

1. Abrir el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Elimine todos los elementos de la colección de archivos incrustados.
1. Guarde el documento de salida limpiado.

```java
public static void removeAllAttachments(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getEmbeddedFiles().delete();
        document.save(outputFile.toString());
    }
}
```
