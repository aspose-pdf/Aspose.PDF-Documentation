---
title: Converter PDF para Word em Java
linktitle: Converter PDF para Word
type: docs
weight: 10
url: /pt/java/convert-pdf-to-word/
lastmod: "2026-10-06"
description: Aprenda como converter arquivos PDF para DOC e DOCX em Java com Aspose.PDF para facilitar a edição e reutilização de documentos.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como Converter PDF para Word em Java
Abstract: Este artigo explica como converter arquivos PDF para formatos Microsoft Word usando Aspose.PDF for Java. Ele cobre saída DOC, saída DOCX, conversão DOCX de fluxo aprimorado, preservação de quebras de linha, reconhecimento de marcadores e controle de resolução de imagem através de `DocSaveOptions`.
---
Aspose.PDF for Java pode exportar documentos PDF para formatos Microsoft Word com diferentes opções de reconhecimento e layout. Use [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) para controlar como o texto, listas e imagens do PDF são mapeados para a saída do Word.

## Converter PDF para DOC

Use este exemplo quando um documento PDF deve ser exportado para o formato DOC legado. O código cria `DocSaveOptions`, define o formato como `Doc`, e passa as opções para um método save compartilhado.

1. Abra o PDF de origem em um [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instância.
1. Criar [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) e definir o formato para `Doc`.
1. Chamar `document.save(outputFile.toString(), saveOptions)` portanto, o PDF é exportado para o formato binário de documento do Microsoft Word.
1. Salve o arquivo DOC convertido.

```java
public static void convertPdfToDoc(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.Doc);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Converter PDF para DOCX

Use este exemplo quando um documento PDF deve ser exportado como um arquivo DOCX. DOCX é o formato preferido para a maioria dos novos fluxos de trabalho de processamento de texto porque é amplamente suportado e mais fácil de editar.

1. Abra o PDF de origem em um [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instância.
1. Criar [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) e definir o formato para `DocX`.
1. Chamar `document.save(outputFile.toString(), saveOptions)` portanto, o conteúdo do PDF é exportado como um documento Word do Office Open XML.
1. Salve o arquivo DOCX resultante.

```java
public static void convertPdfToDocx(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Converter PDF para DOCX com reconhecimento de fluxo aprimorado

Use este exemplo quando a exportação para Word deve favorecer conteúdo editável fluido em vez de layout visual fixo.

1. Abra o PDF de origem em um [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instância.
1. Criar [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) para `DocX` saída.
1. Ativar `setMode(DocSaveOptions.RecognitionMode.EnhancedFlow)` assim, o conversor usa o reconhecimento de fluxo aprimorado durante a geração de DOCX.
1. Chamar `document.save(outputFile.toString(), saveOptions)` e salve a saída DOCX convertida.

```java
public static void convertPdfToDocxAdvanced(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        saveOptions.setMode(DocSaveOptions.RecognitionMode.EnhancedFlow);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Converter PDF para DOCX com quebras de linha preservadas

Use este exemplo quando as quebras de linha do PDF de origem devem ser mantidas na saída do Word.

1. Abra o PDF de origem em um [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instância.
1. Criar [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) para `DocX` exportar.
1. Ativar `setAddReturnToLineEnd(true)` para que quebras de linha explícitas sejam preservadas durante a conversão.
1. Chamar `document.save(outputFile.toString(), saveOptions)` e salve o arquivo DOCX.

```java
public static void convertPdfToDocxWithLineBreaks(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        saveOptions.setAddReturnToLineEnd(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Converter PDF para DOCX com reconhecimento de marcadores

Use este exemplo quando marcadores de lista do PDF de origem devem ser reconhecidos e preservados como estruturas de lista no Word.

1. Abra o PDF de origem em um [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instância.
1. Criar [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) para `DocX` exportar.
1. Ativar `setRecognizeBullets(true)` portanto, o conteúdo semelhante a listas em PDF é reconhecido como listas com marcadores durante a conversão.
1. Chamar `document.save(outputFile.toString(), saveOptions)` e salve o arquivo DOCX.

```java
public static void convertPdfToDocxWithBulletRecognition(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        saveOptions.setRecognizeBullets(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Converter PDF para DOCX com resolução de imagem personalizada

Use este exemplo quando a fidelidade da imagem dentro do DOCX gerado deve ser controlada durante a conversão.

1. Abra o PDF de origem em um [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instância.
1. Criar [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) para `DocX` exportar.
1. Conjunto `setImageResolutionX(300)` e `setImageResolutionY(300)` Assim, o conteúdo raster é gerado na resolução solicitada.
1. Chamar `document.save(outputFile.toString(), saveOptions)` e salvar a saída DOCX.

```java
public static void convertPdfToDocxWithImageResolution(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        saveOptions.setImageResolutionX(300);
        saveOptions.setImageResolutionY(300);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
