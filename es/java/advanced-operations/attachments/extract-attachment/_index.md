---
title: Extraer archivos adjuntos del PDF
linktitle: Extraer archivos adjuntos
type: docs
weight: 50
url: /es/java/extract-attachment/
description: Aprenda cómo extraer archivos incrustados y anotaciones de archivo adjunto de documentos PDF en Java usando Aspose.PDF.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraiga uno o todos los archivos incrustados de un PDF con Java
Abstract: Este artículo explica cómo extraer archivos adjuntos de documentos PDF con Aspose.PDF for Java. Cubre la extracción de un único archivo adjunto con nombre, la guardado de todos los archivos incrustados en una carpeta de salida, la lectura de los metadatos del archivo y la exportación del contenido de una anotación FileAttachment en una página.
---
Aspose.PDF for Java admite varios flujos de extracción dependiendo de cómo se almacenen los archivos adjuntos en el documento.

## Extraer un único archivo adjunto por nombre

Utilice este ejemplo cuando necesite guardar un archivo incrustado específico de un PDF.

1. Abrir el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterar a través de la colección de archivos incrustados hasta que se encuentre el nombre del adjunto requerido.
1. Copiar el flujo del adjunto al archivo de salida y detenerse después de la extracción.

```java
public static void extractSingleAttachment(Path inputFile, String attachmentName, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        System.out.println("Extracting attachment: " + attachmentName);

        boolean attachmentFound = false;
        for (FileSpecification fileSpecification : document.getEmbeddedFiles()) {
            if (attachmentName.equals(fileSpecification.getName())) {
                try (InputStream inputStream = fileSpecification.getContents();
                     OutputStream outputStream = Files.newOutputStream(outputFile)) {
                    inputStream.transferTo(outputStream);
                }
                System.out.println("Attachment extracted successfully");
                attachmentFound = true;
                break;
            }
        }

        if (!attachmentFound) {
            throw new IllegalArgumentException("Attachment '" + attachmentName + "' not found in PDF");
        }
    }
}
```

## Imprimir parámetros del archivo incrustado

Este método auxiliar imprime los metadatos almacenados en un [FileParams](https://reference.aspose.com/pdf/java/com.aspose.pdf/fileparams/) objeto.

1. Verifique si el objeto de parámetros de archivo existe.
1. Lea los valores de suma de verificación disponibles, fecha de creación, fecha de modificación y tamaño.
1. Imprima los valores en la consola.

```java
public static void printFileParams(FileParams params) {
    if (params != null) {
        try {
            System.out.println("CheckSum: " + params.getCheckSum());
        } catch (Exception ex) {
            System.out.println("CheckSum: null");
        }
        System.out.println("Creation Date: " + params.getCreationDate());
        System.out.println("Modification Date: " + params.getModDate());
        System.out.println("Size: " + params.getSize());
    }
}
```

## Extraer todos los archivos adjuntos incrustados

Utilice este ejemplo cuando cada archivo incrustado en el PDF deba escribirse en un directorio de salida.

1. Abrir el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Itere a través de la colección de archivos incrustados y determine un nombre de archivo de salida seguro para cada elemento.
1. Imprima los metadatos, guarde cada flujo de adjunto y continúe hasta que se exporten todos los archivos.

```java
public static void extractAttachments(Path inputFile, Path outputDir) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        System.out.println("Total files: " + document.getEmbeddedFiles().size());

        int fileIndex = 1;
        for (FileSpecification fileSpecification : document.getEmbeddedFiles()) {
            String fileName = fileSpecification.getName();
            if (fileName == null || fileName.isBlank()) {
                fileName = fileSpecification.getUnicodeName();
            }
            if (fileName == null || fileName.isBlank()) {
                fileName = "attachment_" + fileIndex + ".bin";
            }

            System.out.println("Name: " + fileName);
            System.out.println("Description: " + fileSpecification.getDescription());
            System.out.println("Mime Type: " + fileSpecification.getMIMEType());
            printFileParams(fileSpecification.getParams());

            Path outputPath = outputDir.resolve(fileName);
            try (InputStream inputStream = fileSpecification.getContents();
                 OutputStream outputStream = Files.newOutputStream(outputPath)) {
                inputStream.transferTo(outputStream);
            }
            fileIndex++;
        }
    }
}
```

## Extraer una anotación de archivo adjunto

Utilice este ejemplo cuando el archivo está adjunto mediante una anotación de página en lugar de solo a través de la colección de archivos incrustados.

1. Abrir el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Localiza el primero [FileAttachmentAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/fileattachmentannotation/) en la página.
1. Lee su especificación de archivo, exporta el contenido e imprime la ruta de destino.

```java
public static void extractFileAttachmentAnnotation(Path inputFile, Path outputDir) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        FileAttachmentAnnotation fileAttachment = null;
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.FileAttachment) {
                fileAttachment = (FileAttachmentAnnotation) annotation;
                break;
            }
        }

        if (fileAttachment == null) {
            System.out.println("File attachment annotation not found.");
            return;
        }

        FileSpecification fileSpecification = fileAttachment.getFile();
        System.out.println("File name: " + fileSpecification.getName());

        Path outputPath = outputDir.resolve("extracted-" + fileSpecification.getName());
        try (InputStream inputStream = fileSpecification.getContents();
             OutputStream outputStream = Files.newOutputStream(outputPath)) {
            inputStream.transferTo(outputStream);
        }

        System.out.println("Extracted to: " + outputPath);
    }
}
```
