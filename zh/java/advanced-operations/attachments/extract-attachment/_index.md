---
title: 从 PDF 中提取附件
linktitle: 提取附件
type: docs
weight: 50
url: /java/extract-attachment/
description: 了解如何使用 Aspose.PDF 从 Java 中的 PDF 文档中提取嵌入文件和文件附件注释。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 从 PDF 中提取一个或所有嵌入文件
Abstract: 本文介绍如何使用 Aspose.PDF for Java 从 PDF 文档中提取附件。它包括提取单个命名附件、将每个嵌入文件保存到输出文件夹、读取文件元数据以及从页面上的 FileAttachment 注释导出内容。
---
Aspose.PDF for Java 支持多种提取流程，具体取决于附件在文档中的存储方式。

## 按名称提取单个附件

当您需要从 PDF 保存一个特定的嵌入文件时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 迭代嵌入的文件集合，直到找到所需的附件名称。
1. 将附件流复制到输出文件并在提取后停止。

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

## 打印嵌入文件参数

此帮助器方法打印存储在 [FileParams](https://reference.aspose.com/pdf/java/com.aspose.pdf/fileparams/) 对象中的元数据。

1. 检查文件参数对象是否存在。
1. 读取可用的校验和、创建日期、修改日期和大小值。
1. 将值打印到控制台。

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

## 提取所有嵌入的附件

当 PDF 中的每个嵌入文件都应写入输出目录时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 迭代嵌入文件集合并确定每个项目的安全输出文件名。
1. 打印元数据，保存每个附件流，然后继续，直到导出所有文件。

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

## 提取文件附件注释

当通过页面注释而不是仅通过嵌入文件集合附加文件时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 找到页面上的第一个 [FileAttachmentAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/fileattachmentannotation/)。
1. 读取其文件规范，导出内容并打印目标路径。

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
