---
title: Extraia anexos de PDF
linktitle: Extrair anexos
type: docs
weight: 50
url: /java/extract-attachment/
description: Aprenda como extrair arquivos incorporados e anotações de anexos de documentos PDF em Java usando Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraia um ou todos os arquivos incorporados de um PDF com Java
Abstract: Este artigo explica como extrair anexos de documentos PDF com Aspose.PDF para Java. Abrange a extração de um único anexo nomeado, salvando cada arquivo incorporado em uma pasta de saída, lendo metadados de arquivo e exportando conteúdo de uma anotação FileAttachment em uma página.
---
Aspose.PDF for Java suporta vários fluxos de extração dependendo de como os anexos são armazenados no documento.

## Extraia um único anexo por nome

Use este exemplo quando precisar salvar um arquivo incorporado específico de um PDF.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Itere pela coleção de arquivos incorporada até que o nome do anexo necessário seja encontrado.
1. Copie o fluxo de anexos para o arquivo de saída e pare após a extração.

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

## Imprimir parâmetros de arquivo incorporados

Este método auxiliar imprime os metadados armazenados em um objeto [FileParams](https://reference.aspose.com/pdf/java/com.aspose.pdf/fileparams/).

1. Verifique se o objeto de parâmetros do arquivo existe.
1. Leia a soma de verificação disponível, data de criação, data de modificação e valores de tamanho.
1. Imprima os valores no console.

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

## Extraia todos os anexos incorporados

Use este exemplo quando cada arquivo incorporado no PDF precisar ser gravado em um diretório de saída.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Itere pela coleção de arquivos incorporada e determine um nome de arquivo de saída seguro para cada item.
1. Imprima os metadados, salve cada fluxo de anexo e continue até que todos os arquivos sejam exportados.

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

## Extraia uma anotação de anexo de arquivo

Use este exemplo quando o arquivo for anexado por meio de uma anotação de página, em vez de apenas por meio da coleção de arquivos incorporados.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Localize o primeiro [FileAttachmentAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/fileattachmentannotation/) na página.
1. Leia a especificação do arquivo, exporte o conteúdo e imprima o caminho de destino.

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
