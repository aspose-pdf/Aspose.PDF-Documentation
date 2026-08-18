---
title: Открыть PDF-документ программно
linktitle: Открыть PDF
type: docs
weight: 20
url: /java/open-pdf-document/
description: Узнайте, как открыть PDF-файл на Java с помощью Aspose.PDF по пути к файлу, потоку или с помощью пароля.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Открытие PDF-документов с помощью библиотеки Aspose.PDF на Java
Abstract: В этой статье показано, как открыть существующие PDF-документы в Java с помощью Aspose.PDF. Он охватывает открытие PDF-файла по пути к файлу, открытие PDF-файла из Входного потока и открытие документа, защищенного паролем, причем в каждом примере считывается количество страниц из загруженного документа.
---
Aspose.PDF для Java поддерживает несколько способов загрузки существующего PDF-документа в зависимости от источника исходных данных.

## Откройте PDF-документ в Java

Вы можете открыть PDF-документ:

1. Откройте [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) непосредственно по пути к файлу.
1. Откройте [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) из `InputStream`.
1. Откройте зашифрованный [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/), указав пароль.

## Откройте документ из файла

```java
public static void openDocumentFromFile(Path inputFile) {
    Document document = new Document(inputFile.toString());
    System.out.println("Pages: " + document.getPages().size());
    document.close();
}
```

## Откройте документ из потока

```java
public static void openDocumentFromStream(Path inputFile) throws Exception {
    try (InputStream stream = Files.newInputStream(inputFile)) {
        Document document = new Document(stream);
        System.out.println("Pages: " + document.getPages().size());
        document.close();
    }
}
```

## Откройте зашифрованный документ

```java
public static void openDocumentEncrypted(Path inputFile) {
    Document document = new Document(inputFile.toString(), "P@ssw0rd");
    System.out.println("Pages: " + document.getPages().size());
    document.close();
}
```
