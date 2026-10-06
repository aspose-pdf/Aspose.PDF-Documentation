---
title: Abrir documento PDF programaticamente
linktitle: Abrir PDF
type: docs
weight: 20
url: /pt/java/open-pdf-document/
description: Saiba como abrir um arquivo PDF em Java usando Aspose.PDF a partir de um caminho de arquivo, um fluxo ou com uma senha.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Abrindo documentos PDF usando a biblioteca Aspose.PDF em Java
Abstract: Este artigo mostra como abrir documentos PDF existentes em Java usando Aspose.PDF. Ele cobre a abertura de um PDF por caminho de arquivo, a abertura de um PDF a partir de um InputStream e a abertura de um documento protegido por senha, com cada exemplo lendo a contagem de páginas do documento carregado.
aliases:
    - /pt/java/abrir-documento-pdf/
---
Aspose.PDF for Java suporta várias maneiras de carregar um documento PDF existente, dependendo de onde os dados de origem provêm.

## Abrir um documento PDF em Java

Você pode abrir um documento PDF:

1. Abra um [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) diretamente de um caminho de arquivo.
1. Abra um [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) de um `InputStream`.
1. Abra um criptografado [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) fornecendo a senha.

## Abrir documento a partir do arquivo

```java
public static void openDocumentFromFile(Path inputFile) {
    Document document = new Document(inputFile.toString());
    System.out.println("Pages: " + document.getPages().size());
    document.close();
}
```

## Abrir documento a partir de stream

```java
public static void openDocumentFromStream(Path inputFile) throws Exception {
    try (InputStream stream = Files.newInputStream(inputFile)) {
        Document document = new Document(stream);
        System.out.println("Pages: " + document.getPages().size());
        document.close();
    }
}
```

## Abrir um documento criptografado

```java
public static void openDocumentEncrypted(Path inputFile) {
    Document document = new Document(inputFile.toString(), "P@ssw0rd");
    System.out.println("Pages: " + document.getPages().size());
    document.close();
}
```
