---
title: Extraer archivos adjuntos de PDF
linktitle: Extraer archivos adjuntos
type: docs
weight: 50
url: /java/extract-attachment/
description: Aprenda a extraer archivos incrustados y anotaciones de archivos adjuntos de documentos PDF en Java utilizando Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraiga uno o todos los archivos incrustados de un PDF con Java
Abstract: Este artículo explica cómo extraer archivos adjuntos de documentos PDF con Aspose.PDF para Java. Cubre la extracción de un solo archivo adjunto con nombre, el almacenamiento de cada archivo incrustado en una carpeta de salida, la lectura de metadatos del archivo y la exportación de contenido desde una anotación FileAttachment en una página.
---
Aspose.PDF para Java admite varios flujos de extracción dependiendo de cómo se almacenen los archivos adjuntos en el documento.


## 
Extraer un único archivo adjunto por nombre



Utilice este ejemplo cuando necesite guardar un archivo incrustado específico de un PDF.


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Repita la colección de archivos incrustados hasta encontrar el nombre del archivo adjunto requerido.
1. Copie el flujo del archivo adjunto al archivo de salida y deténgalo después de la extracción.


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

## 
Imprimir parámetros de archivos incrustados



Este método auxiliar imprime los metadatos almacenados en un objeto [FileParams](https://reference.aspose.com/pdf/java/com.aspose.pdf/fileparams/).


1. 
Compruebe si el objeto de parámetros del archivo existe.

1. 
Lea la suma de comprobación disponible, la fecha de creación, la fecha de modificación y los valores de tamaño.
1. Imprime los valores en la consola.


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

## 
Extraiga todos los archivos adjuntos incrustados



Utilice este ejemplo cuando cada archivo incrustado en el PDF deba escribirse en un directorio de salida.


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Itere a través de la colección de archivos incrustados y determine un nombre de archivo de salida seguro para cada elemento.
1. Imprima los metadatos, guarde cada secuencia de archivos adjuntos y continúe hasta exportar todos los archivos.


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

## 
Extraer una anotación de archivo adjunto



Utilice este ejemplo cuando el archivo se adjunte a través de una anotación de página en lugar de solo a través de la colección de archivos incrustados.


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Localice la primera [FileAttachmentAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/fileattachmentannotation/) en la página.
1. Lea la especificación del archivo, exporte el contenido e imprima la ruta de destino.

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
