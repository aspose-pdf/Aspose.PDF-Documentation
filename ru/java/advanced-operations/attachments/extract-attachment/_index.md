---
title: Извлечь вложения из PDF
linktitle: Извлечь вложения
type: docs
weight: 50
url: /java/extract-attachment/
description: Узнайте, как извлечь внедренные файлы и аннотации к вложенным файлам из PDF-документов на Java с помощью Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Извлеките один или все встроенные файлы из PDF-файла с помощью Java
Abstract: В этой статье объясняется, как извлекать вложения из PDF-документов с помощью Aspose.PDF для Java. Он охватывает извлечение одного именованного вложения, сохранение каждого внедренного файла в выходную папку, чтение метаданных файла и экспорт содержимого из аннотации FileAttachment на странице.
---
Aspose.PDF для Java поддерживает несколько потоков извлечения в зависимости от того, как вложения хранятся в документе.

## Извлеките одно вложение по имени

Используйте этот пример, когда вам нужно сохранить один конкретный встроенный файл из PDF-файла.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Перебирайте коллекцию внедренных файлов, пока не будет найдено необходимое имя вложения.
1. Скопируйте поток вложений в выходной файл и остановитесь после извлечения.

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

## Распечатать параметры встроенного файла

Этот вспомогательный метод печатает метаданные, хранящиеся в объекте [FileParams](https://reference.aspose.com/pdf/java/com.aspose.pdf/fileparams/).

1. Проверьте, существует ли объект параметров файла.
1. Прочтите доступную контрольную сумму, дату создания, дату модификации и значения размера.
1. Выведите значения на консоль.

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

## Извлеките все встроенные вложения

Используйте этот пример, когда каждый внедренный файл PDF должен быть записан в выходной каталог.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Выполните итерацию по коллекции встроенных файлов и определите безопасное имя выходного файла для каждого элемента.
1. Распечатайте метаданные, сохраните каждый поток вложений и продолжайте, пока все файлы не будут экспортированы.

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

## Извлечение аннотации к вложенному файлу

Используйте этот пример, когда файл прикреплен через аннотацию страницы, а не только через коллекцию внедренных файлов.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Найдите первую [FileAttachmentAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/fileattachmentannotation/) на странице.
1. Прочтите спецификацию файла, экспортируйте содержимое и распечатайте путь назначения.

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
