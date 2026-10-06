---
title: Converter PDF para EPUB, Texto, XPS e Mais em Java
linktitle: Converter PDF para outros formatos
type: docs
weight: 90
url: /pt/java/convert-pdf-to-other-files/
lastmod: "2026-10-06"
description: Aprenda como converter arquivos PDF para EPUB, LaTeX, Markdown, texto, XPS e MobiXML em Java com Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Como converter PDF para outros formatos em Java
Abstract: Este artigo explica como converter arquivos PDF em formatos EPUB, TeX, Markdown, texto, XPS e MobiXML usando Aspose.PDF for Java, com opções de salvamento específicas para cada formato quando necessário.
---
Aspose.PDF for Java pode exportar documentos PDF para formatos de saída de texto, ebook, impressão e formatos orientados a marcação.

## Converter PDF para EPUB

Use este exemplo quando um documento PDF precisar ser exportado para o formato de ebook EPUB.

1. Abra o PDF de origem em um [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instância.
1. Criar [`EpubSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/epubsaveoptions/) e defina o modo de reconhecimento para `Flow`.
1. Chamada `document.save(outputFile.toString(), saveOptions)` então o conteúdo PDF é exportado como marcação EPUB refluível.
1. Salvar o arquivo EPUB convertido.

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

## Converter PDF para TeX

Use este exemplo quando o conteúdo do PDF deve ser exportado para marcação TeX.

1. Abra o PDF de origem em um [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instância.
1. Criar [`TeXSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/texsaveoptions/) para serialização de TeX.
1. Chamada `document.save(outputFile.toString(), saveOptions)` portanto, o conteúdo do PDF é emitido como marcação TeX.
1. Salve o arquivo TeX resultante.

```java
public static void convertPdfToTex(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.save(outputFile.toString(), new TeXSaveOptions());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Converter PDF para texto simples

Use este exemplo quando um documento PDF deve ser exportado como um arquivo de texto.

1. Abra o PDF de origem em um [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instância.
1. Criar um [`TextDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/textdevice/) para extrair conteúdo textual das páginas PDF.
1. Chamada `device.process(document.getPages().get_Item(1), outputFile.toString())` para escrever a primeira página como texto simples.
1. Salvar o arquivo de saída de texto.

```java
public static void convertPdfToTxt(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextDevice device = new TextDevice();
        device.process(document.getPages().get_Item(1), outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Converter PDF para XPS

Use este exemplo quando um documento PDF deve ser convertido para o formato XPS.

1. Abra o PDF de origem em um [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instância.
1. Criar [`XpsSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/xpssaveoptions/) e habilite fontes TrueType incorporadas.
1. Chamada `document.save(outputFile.toString(), saveOptions)` então o PDF é serializado como XPS com recursos de fonte incorporados.
1. Salvar o arquivo XPS convertido.

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

## Converter PDF para Markdown

Use este exemplo quando o conteúdo do PDF deve ser exportado como Markdown.

1. Abra o PDF de origem em um [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instância.
1. Criar [`MarkdownSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/markdownsaveoptions/) e configure o diretório de recursos de imagens mais a saída de tag de imagem HTML.
1. Chamada `document.save(outputFile.toString(), saveOptions)` então o conteúdo do PDF é emitido como Markdown com recursos de imagem externos.
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

## Converter PDF para Mobi XML

Use este exemplo quando o conteúdo do PDF deve ser exportado para XML compatível com Mobi.

1. Abra o PDF de origem em um [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instância.
1. Selecionar [`SaveFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/saveformat/) `MobiXml` como o formato de serialização de destino.
1. Chamada `document.save(outputFile.toString(), SaveFormat.MobiXml)` Portanto, o PDF é exportado como XML compatível com Mobi.
1. Salvar o arquivo convertido.

```java
public static void convertPdfToMobiXml(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.save(outputFile.toString(), SaveFormat.MobiXml);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
