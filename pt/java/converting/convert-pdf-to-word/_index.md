---
title: Converta PDF para Word em Java
linktitle: Converter PDF em Word
type: docs
weight: 10
url: /java/convert-pdf-to-word/
lastmod: "2026-06-16"
description: Aprenda como converter arquivos PDF em DOC e DOCX em Java com Aspose.PDF para facilitar a edição e reutilização de documentos.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como converter PDF para Word em Java
Abstract: Este artigo explica como converter arquivos PDF para formatos Microsoft Word usando Aspose.PDF para Java. Ele cobre saída DOC, saída DOCX, conversão DOCX de fluxo aprimorado, quebras de linha preservadas, reconhecimento de marcadores e controle de resolução de imagem por meio de `DocSaveOptions`.
---
Aspose.PDF for Java pode exportar documentos PDF para formatos Microsoft Word com diferentes opções de reconhecimento e layout. Use [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) para controlar como o texto, as listas e as imagens do PDF são mapeados na saída do Word.

## Converter PDF em DOC

Use este exemplo quando um documento PDF precisar ser exportado para o formato DOC legado. O código cria `DocSaveOptions`, define o formato como `Doc` e passa as opções para um método de salvamento compartilhado.

1. Abra o PDF de origem em uma instância [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) e defina o formato como `Doc`.
1. Chame `document.save(outputFile.toString(), saveOptions)` para que o PDF seja exportado para o formato de documento binário do Microsoft Word.
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

## Converter PDF em DOCX

Use este exemplo quando um documento PDF precisar ser exportado como um arquivo DOCX. DOCX é o formato preferido para a maioria dos novos fluxos de trabalho de processamento de texto porque é amplamente suportado e mais fácil de editar.

1. Abra o PDF de origem em uma instância [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) e defina o formato como `DocX`.
1. Chame `document.save(outputFile.toString(), saveOptions)` para que o conteúdo PDF seja exportado como um documento Office Open XML Word.
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

## Converta PDF em DOCX com reconhecimento de fluxo aprimorado

Use este exemplo quando a exportação do Word favorecer conteúdo editável fluido em vez de layout visual fixo.

1. Abra o PDF de origem em uma instância [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) para saída `DocX`.
1. Habilite `setMode(DocSaveOptions.RecognitionMode.EnhancedFlow)` para que o conversor use reconhecimento de fluxo aprimorado durante a geração de DOCX.
1. Chame `document.save(outputFile.toString(), saveOptions)` e salve a saída DOCX convertida.

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

## Converta PDF em DOCX com quebras de linha preservadas

Use este exemplo quando os finais de linha do PDF de origem devem ser mantidos na saída do Word.

1. Abra o PDF de origem em uma instância [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) para exportação `DocX`.
1. Habilite `setAddReturnToLineEnd(true)` para que quebras de linha explícitas sejam preservadas durante a conversão.
1. Ligue para `document.save(outputFile.toString(), saveOptions)` e salve o arquivo DOCX.

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

## Converta PDF em DOCX com reconhecimento de marcadores

Use este exemplo quando os marcadores de lista do PDF de origem devem ser reconhecidos e preservados como estruturas de lista no Word.

1. Abra o PDF de origem em uma instância [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) para exportação `DocX`.
1. Habilite `setRecognizeBullets(true)` para que o conteúdo PDF semelhante a uma lista seja reconhecido como listas com marcadores durante a conversão.
1. Ligue para `document.save(outputFile.toString(), saveOptions)` e salve o arquivo DOCX.

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

## Converta PDF em DOCX com resolução de imagem personalizada

Use este exemplo quando a fidelidade da imagem dentro do DOCX gerado precisar ser controlada durante a conversão.

1. Abra o PDF de origem em uma instância [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) para exportação `DocX`.
1. Defina `setImageResolutionX(300)` e `setImageResolutionY(300)` para que o conteúdo raster seja gerado na resolução solicitada.
1. Chame `document.save(outputFile.toString(), saveOptions)` e salve a saída DOCX.

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
