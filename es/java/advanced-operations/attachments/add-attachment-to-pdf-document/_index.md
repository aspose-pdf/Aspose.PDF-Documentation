---
title: Agregar archivos adjuntos a PDF en Java
linktitle: Agregar un archivo adjunto a un documento PDF
type: docs
weight: 10
url: /java/add-attachment-to-pdf-document/
description: Aprenda a agregar archivos adjuntos a documentos PDF en Java usando Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregue archivos incrustados a documentos PDF con Java
Abstract: Este artículo muestra cómo adjuntar un archivo externo a un documento PDF usando Aspose.PDF para Java. El ejemplo abre un PDF existente, crea una especificación de archivo para el archivo adjunto, lo agrega a la colección EmbeddedFiles del documento y guarda el archivo actualizado.
---
Para adjuntar un archivo a un PDF, cargue el documento fuente, cree un `FileSpecification`, agréguelo a la colección de archivos incrustados y guarde el resultado.


## 
Agregar un archivo adjunto a un documento PDF



Utilice este ejemplo cuando deba incrustar un archivo externo en un PDF existente.


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Cree una [Especificación de archivo](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) para el archivo que desea incrustar.
1. Agregue la especificación del archivo a la colección `EmbeddedFiles` y guarde el documento actualizado.

```java
public static void addAttachments(Path inputFile, Path attachmentPath, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        FileSpecification fileSpecification = new FileSpecification(attachmentPath.toString(), "Sample text file");
        document.getEmbeddedFiles().add(attachmentPath.getFileName().toString(), fileSpecification);
        document.save(outputFile.toString());
    }
}
```
