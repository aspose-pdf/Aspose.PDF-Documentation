---
title: Converta PDF em EPUB, Texto, XPS e muito mais em Java
linktitle: Converta PDF para outros formatos
type: docs
weight: 90
url: /java/convert-pdf-to-other-files/
lastmod: "2026-06-16"
description: Aprenda como converter arquivos PDF para EPUB, LaTeX, Markdown, texto, XPS e MobiXML em Java com Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Como converter PDF para outros formatos em Java
Abstract: Este artigo explica como converter arquivos PDF em formatos EPUB, TeX, Markdown, texto, XPS e MobiXML usando Aspose.PDF para Java, com opções de salvamento específicas do formato quando necessário.
---
Aspose.PDF para Java pode exportar documentos PDF em formatos de texto, e-book, impressão e formatos de saída orientados para marcação.

## Converter PDF em EPUB

Use este exemplo quando um documento PDF precisar ser exportado para o formato de e-book EPUB.

1. Abra o PDF de origem em uma instância [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie [`EpubSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/epubsaveoptions/) e defina o modo de reconhecimento como `Flow`.
1. Chame `document.save(outputFile.toString(), saveOptions)` para que o conteúdo do PDF seja exportado como marcação EPUB refluível.
1. Salve o arquivo EPUB convertido.

```java
public static void convertPdfToEpub(Path inputFile, Path outputFile) {
        try (Document document = new Document(inputFile.toString())) {
            EpubSaveOptions saveOptions = new EpubSaveOptions();
            saveOptions.setContentRecognitionMode(EpubSaveOptions.RecognitionMode.Flow);
            document.save(outputFile.toString(), saveOptions);
        }
        System.out.println(inputFile + " converted into " + outputFile);
    }
```

## Converter PDF em TeX

Use este exemplo quando o conteúdo PDF precisar ser exportado para marcação TeX.

1. Abra o PDF de origem em uma instância [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie [`TeXSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/texsaveoptions/) para serialização TeX.
1. Chame `document.save(outputFile.toString(), saveOptions)` para que o conteúdo do PDF seja emitido como marcação TeX.
1. Salve o arquivo TeX resultante.

```java
public static void convertPdfToTex(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.save(outputFile.toString(), new TeXSaveOptions());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Converter PDF em texto simples

Use este exemplo quando um documento PDF precisar ser exportado como um arquivo de texto.

1. Abra o PDF de origem em uma instância [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um [`TextDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/textdevice/) para extrair conteúdo textual de páginas PDF.
1. Chame `device.process(document.getPages().get_Item(1), outputFile.toString())` para escrever a primeira página como texto simples.
1. Salve o arquivo de saída de texto.

```java
public static void convertPdfToTxt(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextDevice device = new TextDevice();
        device.process(document.getPages().get_Item(1), outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Converter PDF em XPS

Use este exemplo quando um documento PDF precisar ser convertido para o formato XPS.

1. Abra o PDF de origem em uma instância [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie [`XpsSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/xpssaveoptions/) e habilite fontes TrueType incorporadas.
1. Chame `document.save(outputFile.toString(), saveOptions)` para que o PDF seja serializado como XPS com recursos de fonte incorporados.
1. Salve o arquivo XPS convertido.

```java
public static void convertPdfToXps(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        XpsSaveOptions saveOptions = new XpsSaveOptions();
        saveOptions.setUseEmbeddedTrueTypeFonts(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Converter PDF em Markdown

Use este exemplo quando o conteúdo PDF precisar ser exportado como Markdown.

1. Abra o PDF de origem em uma instância [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie [`MarkdownSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/markdownsaveoptions/) e configure o diretório de recursos de imagem mais a saída de tag de imagem HTML.
1. Chame `document.save(outputFile.toString(), saveOptions)` para que o conteúdo do PDF seja emitido como Markdown com recursos de imagem externos.
1. Salve o arquivo Markdown gerado.

```java
public static void convertPdfToMd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        MarkdownSaveOptions saveOptions = new MarkdownSaveOptions();
        saveOptions.setResourcesDirectoryName("images");
        saveOptions.setUseImageHtmlTag(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Converter PDF em Mobi XML

Use este exemplo quando o conteúdo PDF precisar ser exportado para XML compatível com Mobi.

1. Abra o PDF de origem em uma instância [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Selecione [`SaveFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/saveformat/) `MobiXml` como o formato de serialização de destino.
1. Chame `document.save(outputFile.toString(), SaveFormat.MobiXml)` para que o PDF seja exportado como XML compatível com Mobi.
1. Salve o arquivo convertido.

```java
public static void convertPdfToMobiXml(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.save(outputFile.toString(), SaveFormat.MobiXml);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
