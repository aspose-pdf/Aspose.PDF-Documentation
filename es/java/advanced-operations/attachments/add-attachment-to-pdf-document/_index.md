---
title: Agregar archivos adjuntos a PDF en Java
linktitle: Añadiendo un adjunto a un documento PDF
type: docs
weight: 10
url: /es/java/add-attachment-to-pdf-document/
description: Aprenda cómo agregar archivos adjuntos a documentos PDF en Java usando Aspose.PDF.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar archivos incrustados a documentos PDF con Java
Abstract: Este artículo muestra cómo adjuntar un archivo externo a un documento PDF usando Aspose.PDF for Java. El ejemplo abre un PDF existente, crea un FileSpecification para el adjunto, lo agrega a la colección EmbeddedFiles del documento y guarda el archivo actualizado.
---
Para adjuntar un archivo a un PDF, cargue el documento fuente, cree un `FileSpecification`, añádelo a la colección de archivos incrustados y guarda el resultado.

## Agregar un adjunto a un documento PDF

Utilice este ejemplo cuando un archivo externo deba incrustarse en un PDF existente.

1. Abrir el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crear un [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) para el archivo que deseas incrustar.
1. Agregar la especificación de archivo a la `EmbeddedFiles` colección y guarde el documento actualizado.

```java
public static void addAttachments(Path inputFile, Path attachmentPath, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        FileSpecification fileSpecification = new FileSpecification(attachmentPath.toString(), "Sample text file");
        document.getEmbeddedFiles().add(attachmentPath.getFileName().toString(), fileSpecification);
        document.save(outputFile.toString());
    }
}
```
