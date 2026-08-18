---
title: Trabalhe com metadados de arquivos PDF em Java
linktitle: Metadados de arquivo PDF
type: docs
weight: 200
url: /java/pdf-file-metadata/
description: Aprenda como extrair, atualizar e gerenciar metadados de arquivos PDF, informações de documentos e propriedades XMP em Java usando Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Obtenha e defina informações de documentos PDF e metadados XMP em Java
Abstract: Este artigo explica como trabalhar com metadados PDF usando Aspose.PDF para Java. Aprenda como ler informações de documentos, como autor, título e palavras-chave, atualizar propriedades de arquivos, inspecionar versões e privilégios de PDF, definir campos de metadados XMP e salvar metadados por meio de APIs DOM e de fachada.
---
Aspose.PDF for Java provides two main ways to work with metadata:

- The DOM API through `Document`, `DocumentInfo`, and `document.getMetadata()`.
- A API de fachada por meio de `PdfFileInfo`.

## Obtenha informações do arquivo PDF

Use este exemplo quando precisar ler campos de informações padrão do documento, como autor, título, assunto ou palavras-chave.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Acesse o objeto [DocumentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/documentinfo/).
1. Leia os campos de metadados necessários e gere seus valores.

```java
public static void getPdfFileInformation(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocumentInfo docInfo = document.getInfo();

        System.out.println("Author: " + docInfo.getAuthor());
        System.out.println("Creation Date: " + docInfo.getCreationDate());
        System.out.println("Keywords: " + docInfo.getKeywords());
        System.out.println("Modify Date: " + docInfo.getModDate());
        System.out.println("Subject: " + docInfo.getSubject());
        System.out.println("Title: " + docInfo.getTitle());
    }
}
```

## Definir metadados com um prefixo de namespace

Use este exemplo quando precisar adicionar ou atualizar uma propriedade XMP usando um prefixo de namespace registrado.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Registre o namespace XMP necessário e adicione o item de metadados.
1. Salve o documento atualizado.

```java
public static void setPrefixMetadata(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getMetadata().registerNamespaceUri("xmp", "http://ns.adobe.com/xap/1.0/");
        document.getMetadata().addItem("xmp:ModifyDate", OffsetDateTime.now().toString());
        document.save(outputFile.toString());
    }
    System.out.println("Prefix metadata saved to " + outputFile);
}
```

## Atualizar campos de informações do documento

Use este exemplo quando quiser escrever propriedades padrão de arquivo PDF, como autor, título, produtor ou data de criação.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Acesse [DocumentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/documentinfo/) e atribua novos valores de metadados.
1. Salve o documento com as informações atualizadas do arquivo.

```java
public static void setFileInformation(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocumentInfo docInfo = document.getInfo();
        Date now = new Date();

        docInfo.setAuthor("Aspose");
        docInfo.setCreationDate(now);
        docInfo.setKeywords("Aspose.Pdf, DOM, API");
        docInfo.setModDate(now);
        docInfo.setSubject("PDF Information");
        docInfo.setTitle("Setting PDF Document Information");
        docInfo.setProducer("Custom producer");
        docInfo.setCreator("Custom creator");

        document.save(outputFile.toString());
    }
    System.out.println("File information saved to " + outputFile);
}
```

## Definir propriedades de metadados XMP

Use este exemplo quando precisar armazenar entradas XMP adicionais, incluindo valores de metadados personalizados.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Adicione os itens de metadados XMP necessários por meio de `document.getMetadata()`.
1. Salve o arquivo de saída.

```java
public static void setXmpMetadata(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getMetadata().addItem("xmp:CreateDate", OffsetDateTime.now().toString());
        document.getMetadata().addItem("xmp:Nickname", "Nickname");
        document.getMetadata().addItem("xmp:CustomProperty", "Custom Value");
        document.save(outputFile.toString());
    }
    System.out.println("XMP metadata saved to " + outputFile);
}
```
