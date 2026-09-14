---
title: Открытие PDF документа программно
linktitle: Открытие PDF
type: docs
weight: 20
url: /ru/java/open-pdf-document/
description: Узнайте, как открыть файл PDF в Java, используя Aspose.PDF, из пути к файлу, из потока или с паролем.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Открытие PDF документов с использованием библиотеки Aspose.PDF в Java
Abstract: В этой статье показано, как открыть существующие PDF‑документы в Java с помощью Aspose.PDF. Описывается открытие PDF по пути к файлу, открытие PDF из InputStream и открытие защищённого паролем документа, при этом каждый пример считывает количество страниц из загруженного документа.
---
Aspose.PDF for Java поддерживает несколько способов загрузки существующего PDF‑документа в зависимости от того, откуда поступают исходные данные.

## Открытие PDF‑документа в Java

Вы можете открыть PDF‑документ:

1. Откройте [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) непосредственно из пути к файлу.
1. Откройте [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) от an `InputStream`.
1. Откройте зашифрованный [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) указав пароль.

## Открытие документа из файла

```java
public static void openDocumentFromFile(Path inputFile) {
    Document document = new Document(inputFile.toString());
    System.out.println("Pages: " + document.getPages().size());
    document.close();
}
```

## Открытие документа из потока

```java
public static void openDocumentFromStream(Path inputFile) throws Exception {
    try (InputStream stream = Files.newInputStream(inputFile)) {
        Document document = new Document(stream);
        System.out.println("Pages: " + document.getPages().size());
        document.close();
    }
}
```

## Открытие зашифрованного документа

```java
public static void openDocumentEncrypted(Path inputFile) {
    Document document = new Document(inputFile.toString(), "P@ssw0rd");
    System.out.println("Pages: " + document.getPages().size());
    document.close();
}
```


