---
title: Converta outros formatos de arquivo em PDF em Java
linktitle: Converta outros formatos de arquivo para PDF
type: docs
weight: 80
url: /java/convert-other-files-to-pdf/
lastmod: "2026-06-16"
description: Aprenda como converter arquivos EPUB, Markdown, PCL, XPS, PostScript, XML, XSL-FO, OFD e TeX em PDF em Java com Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Como converter outros formatos de arquivo para PDF em Java
Abstract: Este artigo explica como converter vários formatos de arquivo de origem em PDF usando Aspose.PDF para Java. Abrange fluxos de trabalho de conversão EPUB, Markdown, OFD, PCL, PostScript, EPS, TeX, texto, XML, XPS e XSL-FO usando opções de carregamento específicas de formato e etapas de pré-processamento quando necessário.
---
Aspose.PDF para Java suporta conversão de formatos de documento, marcação e descrição de página em PDF.

## Converter OFD em PDF

Use este exemplo quando um documento OFD precisar ser convertido em PDF.

1. Abra a fonte OFD passando o caminho do arquivo e [`OfdLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/ofdloadoptions/) para o construtor [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Deixe o Aspose.PDF analisar o pacote OFD no modelo de documento PDF.
1. Salve o PDF resultante no caminho de saída de destino.

```java
public static void convertOfdToPdf(Path inputFile, Path outputFile) {
       try (Document document = new Document(inputFile.toString(), new OfdLoadOptions())) {
           document.save(outputFile.toString());
       }
       System.out.println(inputFile + " converted into " + outputFile);
   }
```

## Converter TeX em PDF

Use este exemplo quando o conteúdo do TeX precisar ser renderizado diretamente como PDF.

1. Abra o código-fonte TeX passando o caminho do arquivo e [`TeXLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/texloadoptions/) para o construtor [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Deixe o Aspose.PDF interpretar a marcação do TeX e construir o layout do PDF durante o carregamento.
1. Salve o PDF gerado.

```java
public static void convertTexToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new com.aspose.pdf.TeXLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Converter PostScript em PDF

Use este exemplo quando um arquivo PostScript precisar ser convertido em um documento PDF.

1. Abra a fonte PostScript com [`PsLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/psloadoptions/) no construtor [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Deixe o Aspose.PDF traduzir o fluxo de descrição da página PostScript em um modelo de documento PDF.
1. Salve o arquivo PDF convertido.

```java
public static void convertPostScripToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new PsLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Converter EPS para PDF

Use este exemplo quando um arquivo PostScript encapsulado precisar ser convertido em PDF.

1. Abra a fonte EPS com [`PsLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/psloadoptions/) porque o EPS segue o mesmo caminho de carregamento baseado em PostScript.
1. Carregue o arquivo em [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) para que o conteúdo da descrição da página seja convertido durante a importação.
1. Salve o PDF de saída.

```java
public static void convertEpsToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new PsLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Converter EPUB em PDF

Use este exemplo quando um e-book EPUB precisar ser convertido em PDF.

1. Abra a fonte EPUB passando o caminho do arquivo e [`EpubLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/epubloadoptions/) para o construtor [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Deixe o Aspose.PDF carregar a estrutura do e-book e transformá-la em páginas PDF.
1. Salve o PDF convertido.

```java
public static void convertEpubToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new EpubLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Converter Markdown em PDF

Use este exemplo quando o conteúdo do Markdown precisar ser renderizado e salvo como PDF.

1. Abra a fonte Markdown passando o caminho do arquivo e [`MdLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/mdloadoptions/) para o construtor [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Deixe o Aspose.PDF interpretar o conteúdo do Markdown e renderizá-lo no conteúdo da página PDF.
1. Salve o arquivo PDF de saída.

```java
public static void convertMdToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new MdLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Converta texto em PDF com um fluxo de trabalho simples

Use este exemplo quando um arquivo de texto simples precisar ser convertido rapidamente em PDF.

1. Leia a fonte de texto simples com decodificação UTF-8 para que o conteúdo do texto esteja disponível como uma string Java.
1. Crie um [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) vazio e adicione um [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Envolva o texto em [`TextFragment`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) e adicione-o à coleção de parágrafos da página.
1. Salve o PDF gerado.

```java
public static void convertTxtToPdfSimple(Path inputFile, Path outputFile) throws Exception {
    String textContent = Files.readString(inputFile, StandardCharsets.UTF_8);
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getParagraphs().add(new TextFragment(textContent));
        page.close();
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Converta texto em PDF com opções avançadas

Use este exemplo quando o texto simples precisar ser convertido com opções adicionais de layout ou codificação.

1. Leia todas as linhas de texto do arquivo de entrada para que os marcadores de quebra de página possam ser inspecionados durante a conversão.
1. Crie um [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) vazio e configure cada [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) com margens e estado de texto padrão.
1. Resolva a fonte monoespaçada através de [`FontRepository`](https://reference.aspose.com/pdf/java/com.aspose.pdf/fontrepository/) e adicione cada linha como [`TextFragment`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/).
1. Salve o arquivo de saída após a conclusão do loop de construção de página.

```java
public static void convertTxtToPdf(Path inputFile, Path outputFile) throws Exception {
    List<String> lines = Files.readAllLines(inputFile);
    try (Document document = new Document()) {
        com.aspose.pdf.Page page = document.getPages().add();
        page.getPageInfo().getMargin().setLeft(20);
        page.getPageInfo().getMargin().setRight(10);
        page.getPageInfo().getDefaultTextState().setFont(FontRepository.findFont("Courier New"));
        page.getPageInfo().getDefaultTextState().setFontSize(12);

        int pageCount = 1;
        for (String line : lines) {
            if (!line.isEmpty() && line.charAt(0) == '\f') {
                page = document.getPages().add();
                page.getPageInfo().getMargin().setLeft(20);
                page.getPageInfo().getMargin().setRight(10);
                page.getPageInfo().getDefaultTextState().setFont(FontRepository.findFont("Courier New"));
                page.getPageInfo().getDefaultTextState().setFontSize(12);
                pageCount++;
                if (pageCount == 4) {
                    break;
                }
            } else {
                page.getParagraphs().add(new TextFragment(line));
            }
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Converter PCL em PDF

Use este exemplo quando um fluxo de impressão PCL precisar ser convertido em PDF.

1. Crie [`PclLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pclloadoptions/) e habilite erros de análise suprimidos quando um comportamento de importação tolerante for necessário.
1. Abra a fonte PCL passando o caminho do arquivo e as opções de carregamento para o construtor [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Salve o resultado como PDF.

```java
public static void convertPclToPdf(Path inputFile, Path outputFile) {
    PclLoadOptions loadOptions = new PclLoadOptions();
    loadOptions.setSupressErrors(true);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Converta XML para PDF através de XSLT e HTML

Use este exemplo quando os dados XML precisarem ser transformados antes da geração final do PDF.

1. Transforme a fonte XML com o arquivo XSLT em um arquivo HTML temporário chamando o método de transformação dedicado.
1. Passe o arquivo HTML gerado para a função de conversão de HTML para PDF existente para que o PDF final use o fluxo de trabalho padrão [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/).
1. Exclua o arquivo HTML temporário no bloco `finally` após a conclusão da conversão.
1. Salve o arquivo PDF gerado.

```java
public static void convertXmlToPdf(Path xsltFile, Path xmlFile, Path outputFile) throws Exception {
    Path htmlFile = Files.createTempFile("aspose-pdf-xml-", ".html");
    try {
        transformXmlToHtml(xmlFile, xsltFile, htmlFile);
        HtmlToPdfExamples.convertHtmlToPdf(htmlFile, outputFile);
    } finally {
        Files.deleteIfExists(htmlFile);
    }
    System.out.println(xmlFile + " converted into " + outputFile);
}
```

## Converter XPS em PDF

Use este exemplo quando um documento XPS precisar ser convertido em PDF.

1. Abra a fonte XPS passando o caminho do arquivo e [`XpsLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/xpsloadoptions/) para o construtor [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Deixe o Aspose.PDF interpretar a descrição da página XPS durante o carregamento do documento.
1. Salve o PDF convertido.

```java
public static void convertXpsToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new XpsLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Converter XSL-FO em PDF

Use este exemplo quando o conteúdo XSL-FO precisar ser renderizado como PDF.

1. Crie [`XslFoLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/xslfoloadoptions/) com o caminho XSLT para que a origem XML possa ser transformada durante o carregamento.
1. Configure o modo de tratamento de erros de análise para ser lançado imediatamente quando XSL-FO inválido for encontrado.
1. Abra a fonte XML em [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) com essas opções de carregamento.
1. Salve o documento PDF resultante.

```java
public static void convertXslFoToPdf(Path xsltFile, Path xmlFile, Path outputFile) {
    XslFoLoadOptions loadOptions = new XslFoLoadOptions(xsltFile.toString());
    loadOptions.setParsingErrorsHandlingType(XslFoLoadOptions.ParsingErrorsHandlingTypes.ThrowExceptionImmediately);
    try (Document document = new Document(xmlFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(xmlFile + " converted into " + outputFile);
}
```

## Transforme XML em HTML intermediário

Use este método quando os dados XML precisarem ser transformados em HTML antes da etapa final de conversão do PDF.

1. Abra os arquivos de entrada XML e XSLT como fontes de transformação.
1. Crie um `Transformer` a partir da folha de estilo XSLT e execute-o na origem XML.
1. Grave o arquivo HTML transformado em disco para que a função de conversão downstream de PDF possa carregá-lo.

```java
private static void transformXmlToHtml(Path xmlFile, Path xsltFile, Path htmlFile) throws Exception {
    Transformer transformer = TransformerFactory.newInstance()
            .newTransformer(new StreamSource(xsltFile.toFile()));
    transformer.transform(new StreamSource(xmlFile.toFile()), new StreamResult(htmlFile.toFile()));
}
```
