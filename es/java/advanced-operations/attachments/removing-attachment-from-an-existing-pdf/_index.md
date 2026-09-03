---
title: Eliminar archivos adjuntos de PDF en Java
linktitle: Eliminar archivos adjuntos de un PDF existente
type: docs
weight: 30
url: /java/removing-attachment-from-an-existing-pdf/
description: Aprenda a eliminar uno o todos los archivos adjuntos incrustados de documentos PDF en Java usando Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Eliminar archivos adjuntos PDF mediante programación con Java
Abstract: Este artículo muestra cómo eliminar archivos adjuntos de archivos PDF usando Aspose.PDF para Java. Los ejemplos demuestran cómo eliminar un archivo incrustado por clave y borrar toda la colección EmbeddedFiles antes de guardar el documento actualizado.
---
Los archivos adjuntos almacenados en un documento PDF se pueden eliminar individualmente o todos a la vez a través de la colección `EmbeddedFiles`.


## 
Eliminar un solo archivo adjunto



Utilice este ejemplo cuando un archivo incrustado con nombre deba eliminarse del PDF.


1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Elimine el archivo adjunto por su clave de la colección de archivos incrustados.
1. Guarde el documento de salida actualizado.


```java
public static void removeAttachment(Path inputFile, String attachmentName, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getEmbeddedFiles().deleteByKey(attachmentName);
        document.save(outputFile.toString());
    }
}
```

## 
Eliminar todos los archivos adjuntos



Utilice este enfoque cuando deba borrar toda la colección de archivos incrustados.


1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Elimine todos los elementos de la colección de archivos incrustados.
1. Guarde el documento de salida limpio.

```java
public static void removeAllAttachments(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getEmbeddedFiles().delete();
        document.save(outputFile.toString());
    }
}
```
