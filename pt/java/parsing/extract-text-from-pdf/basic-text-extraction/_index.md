---
title: Extração básica de texto usando Java
linktitle: Extração básica de texto
type: docs
weight: 10
url: /pt/java/basic-text-extraction/
description: Aprenda como extrair texto de documentos PDF em Java com Aspose.PDF de todas as páginas, de uma página específica ou por estrutura de parágrafo.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
A extração básica de texto é o ponto de partida para ler o conteúdo de PDF em Java. Aspose.PDF oferece duas abordagens comuns:

- Use `TextAbsorber` quando precisar de um resultado em texto simples de um documento ou página.
- Use `ParagraphAbsorber` quando precisar preservar o agrupamento de página, seção, parágrafo, linha e fragmento.

As páginas de PDF não armazenam texto como um documento de processamento de texto, portanto a ordem extraída depende do fluxo de conteúdo da página e do layout. Para extração específica de região, detalhes de geometria, layouts de múltiplas colunas, anotações, texto destacado ou detecção de sobrescrito e subscrito, use os artigos de extração relacionados nesta seção.

## Extrair texto de todas as páginas

Use `TextAbsorber` para coletar um fluxo de texto simples de todo o documento e gravá-lo em um arquivo. Esta é a opção mais simples quando você só precisa do conteúdo de texto legível e não precisa de limites de parágrafo ou coordenadas.

1. Abra o PDF de origem em uma instância de [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) para acumular texto em todo o documento.
1. Chame `document.getPages().accept(textAbsorber)`; assim, cada objeto [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) é visitado pelo absorvedor.
1. Escreva o buffer de texto extraído no arquivo de saída.

```java
public static void extractTextFromAllPages(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextAbsorber textAbsorber = new TextAbsorber();
        document.getPages().accept(textAbsorber);
        Files.writeString(outputFile, textAbsorber.getText());
    }
}
```

## Extrair texto de uma página específica

Aplique o absorvedor apenas à página desejada. A coleção de páginas de `Document` é indexada a partir de 1; portanto, `get_Item(1)` lê a primeira página.

1. Abra o PDF de origem em uma instância de [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) para extração de página única.
1. Chame `accept(textAbsorber)` na página de destino [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) selecionada pelo número da página.
1. Escreva o buffer de texto extraído no arquivo de saída.

```java
public static void extractTextFromPage(Path inputFile, Path outputFile, int pageNumber) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextAbsorber textAbsorber = new TextAbsorber();
        document.getPages().get_Item(pageNumber).accept(textAbsorber);
        Files.writeString(outputFile, textAbsorber.getText());
    }
}
```

## Extrair texto por estrutura de parágrafo

Use `ParagraphAbsorber` quando precisar de agrupamento estrutural em vez de um único fluxo de texto simples. Ele devolve marcações de página com seções, parágrafos, linhas e objetos `TextFragment`, o que é útil quando a saída deve preservar blocos lógicos de texto.

1. Abra o PDF de origem em uma instância de [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um [ParagraphAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/paragraphabsorber/) e visite todo o documento para gerar resultados de marcação de página.
1. Itere através das marcações de página, seções, parágrafos, linhas e objetos [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) expostos pelo absorvedor.
1. Construa o texto de saída com numeração explícita de página, seção e parágrafo, de modo que o agrupamento estrutural seja preservado.
1. Escreva o texto do parágrafo extraído no arquivo de saída.

```java
public static void extractParagraphsFromPdf(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        ParagraphAbsorber absorber = new ParagraphAbsorber();
        absorber.visit(document);

        StringBuilder text = new StringBuilder();
        for (PageMarkup pageMarkup : absorber.getPageMarkups()) {
            int sectionIndex = 1;
            for (MarkupSection section : pageMarkup.getSections()) {
                int paragraphIndex = 1;
                for (MarkupParagraph paragraph : section.getParagraphs()) {
                    StringBuilder paragraphText = new StringBuilder();
                    for (List<TextFragment> line : paragraph.getLines()) {
                        for (TextFragment fragment : line) {
                            paragraphText.append(fragment.getText());
                        }
                        paragraphText.append("\r\n");
                    }
                    text.append("Page ").append(pageMarkup.getNumber())
                            .append(", Section ").append(sectionIndex)
                            .append(", Paragraph ").append(paragraphIndex)
                            .append(":\n");
                    text.append(paragraphText).append("\n");
                    paragraphIndex++;
                }
                sectionIndex++;
            }
        }

        Files.writeString(outputFile, text.toString());
    }
}
```
