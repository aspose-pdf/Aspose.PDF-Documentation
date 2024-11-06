---
title: Añadir Adjunto a Documento PDF 
linktitle: Añadir Adjunto a Documento PDF 
type: docs
weight: 10
url: es/java/add-attachment-to-pdf-document/
description: Esta página describe cómo añadir un adjunto a un archivo PDF con Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Los adjuntos pueden contener una amplia variedad de información y pueden ser de diversos tipos de archivos. Este artículo explica cómo añadir un adjunto a un archivo PDF.

1. Crear un objeto [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification) que contenga el archivo que deseas adjuntar y la descripción del archivo.

1. Agrega el objeto [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification) a la colección [EmbeddedFiles](https://reference.aspose.com/pdf/java/com.aspose.pdf/EmbeddedFileCollection) de un objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) usando el método [add(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification). La colección [EmbeddedFiles](https://reference.aspose.com/pdf/java/com.aspose.pdf/EmbeddedFileCollection) contiene todos los archivos adjuntos añadidos a un archivo PDF.

El siguiente fragmento de código te muestra cómo agregar un archivo adjunto en un documento PDF.

```java
public class ExampleAttachments {
    
    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Attachments/";

    public static void AddingAttachment() {
        // Abre un documento
        Document pdfDocument = new Document(_dataDir+"input.pdf");
        // Configura un nuevo archivo para ser añadido como adjunto
        FileSpecification fileSpecification = new FileSpecification("sample.txt", "Archivo de texto de muestra");
        // Añade un archivo adjunto a la colección de adjuntos del documento
        pdfDocument.getEmbeddedFiles().add(fileSpecification);
        // Guarda el documento actualizado
        pdfDocument.save("output.pdf");
    }
}
```