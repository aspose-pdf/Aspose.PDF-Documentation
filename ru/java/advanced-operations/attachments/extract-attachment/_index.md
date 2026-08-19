---
title: Извлечь вложения из PDF
linktitle: Извлечь вложения
type: docs
weight: 50
url: /ru/java/extract-attachment/
description: Узнайте, как извлечь встроенные файлы и аннотации вложений файлов из PDF‑документов на Java с использованием Aspose.PDF.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Извлечь один или все встроенные файлы из PDF с помощью Java
Abstract: В этой статье объясняется, как извлекать вложения из PDF‑документов с помощью Aspose.PDF for Java. Описывается извлечение одного именованного вложения, сохранение всех встроенных файлов в выходную папку, чтение метаданных файла и экспорт содержимого аннотации FileAttachment на странице.
---
Aspose.PDF for Java поддерживает несколько вариантов извлечения в зависимости от того, как вложения хранятся в документе.

## Извлеките отдельное вложение по имени

Используйте этот пример, когда необходимо сохранить один конкретный встроенный файл из PDF.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Итерируйте по коллекции встроенных файлов, пока не будет найдено требуемое имя вложения.
1. Скопируйте поток вложения в выходной файл и прекратите выполнение после извлечения.

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

## Вывести параметры встроенного файла

Этот вспомогательный метод выводит метаданные, хранящиеся в [FileParams](https://reference.aspose.com/pdf/java/com.aspose.pdf/fileparams/) объекте.

1. Проверьте, существует ли объект параметров файла.
1. Прочитайте доступные значения контрольной суммы, даты создания, даты изменения и размера.
1. Выведите значения в консоль.

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

## Извлеките все вложенные вложения

Используйте этот пример, когда каждый вложенный файл в PDF должен быть записан в выходной каталог.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Пройдите по коллекции вложенных файлов и определите безопасное имя выходного файла для каждого элемента.
1. Выведите метаданные, сохраните каждый поток вложения и продолжайте, пока не будут экспортированы все файлы.

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

## Извлеките аннотацию вложения файла

Используйте этот пример, когда файл прикреплен через аннотацию страницы, а не только через коллекцию вложенных файлов.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Найдите первый [FileAttachmentAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/fileattachmentannotation/) на странице.
1. Прочитайте его спецификацию файла, экспортируйте содержимое и выведите путь назначения.

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

