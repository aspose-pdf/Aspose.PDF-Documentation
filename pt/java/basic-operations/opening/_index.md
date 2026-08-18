---
title: Abra um documento PDF programaticamente
linktitle: Abrir PDF
type: docs
weight: 20
url: /java/open-pdf-document/
description: Aprenda como abrir um arquivo PDF em Java usando Aspose.PDF a partir de um caminho de arquivo, fluxo ou com uma senha.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Abrindo documentos PDF usando a biblioteca Aspose.PDF em Java
Abstract: Este artigo mostra como abrir documentos PDF existentes em Java usando Aspose.PDF. Abrange a abertura de um PDF por caminho de arquivo, a abertura de um PDF a partir de um InputStream e a abertura de um documento protegido por senha, com cada exemplo lendo a contagem de páginas do documento carregado.
---
Aspose.PDF for Java oferece suporte a várias maneiras de carregar um documento PDF existente, dependendo de onde vêm os dados de origem.

## Abra um documento PDF em Java

Você pode abrir um documento PDF:

1. Abra um [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) diretamente de um caminho de arquivo.
1. Abra um [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) de um `InputStream`.
1. Abra um [Documento] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) criptografado fornecendo a senha.

## Abrir documento do arquivo

```java
public static void openDocumentFromFile(Path inputFile) {
    Document document = new Document(inputFile.toString());
    System.out.println("Pages: " + document.getPages().size());
    document.close();
}
```

## Abrir documento do stream

```java
public static void openDocumentFromStream(Path inputFile) throws Exception {
    try (InputStream stream = Files.newInputStream(inputFile)) {
        Document document = new Document(stream);
        System.out.println("Pages: " + document.getPages().size());
        document.close();
    }
}
```

## Abra um documento criptografado

```java
public static void openDocumentEncrypted(Path inputFile) {
    Document document = new Document(inputFile.toString(), "P@ssw0rd");
    System.out.println("Pages: " + document.getPages().size());
    document.close();
}
```
