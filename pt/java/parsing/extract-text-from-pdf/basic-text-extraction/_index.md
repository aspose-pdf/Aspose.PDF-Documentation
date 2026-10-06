---
title: Extração Básica de Texto usando Java
linktitle: Extração Básica de Texto
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

- Usar `TextAbsorber` quando você precisar de um resultado em texto simples de um documento ou página.
- Usar `ParagraphAbsorber` quando você precisa preservar o agrupamento de página, seção, parágrafo, linha e fragmento.

As páginas de PDF não armazenam texto como um documento de processamento de texto, portanto a ordem extraída depende do fluxo de conteúdo da página e do layout. Para extração específica de região, detalhes de geometria, layouts de múltiplas colunas, anotações, texto destacado ou detecção de sobrescrito e subscrito, use os artigos de extração relacionados nesta seção.

## Extrair texto de todas as páginas

Usar `TextAbsorber` para coletar um fluxo de texto plano de todo o documento e gravá-lo em um arquivo. Esta é a opção mais simples quando você só precisa do conteúdo de texto legível e não precisa de limites de parágrafo ou coordenadas.

1. Abra o PDF de origem em um [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instância.
1. Criar um [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) para acumular texto em todo o documento.
1. Chamar `document.getPages().accept(textAbsorber)` então cada [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) é visitado pelo absorvedor.
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

Aplique o absorvedor apenas à página que você precisa. Números de página no `Document` a coleção de páginas é indexada a partir de 1, então `get_Item(1)` lê a primeira página.

1. Abra o PDF de origem em um [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instância.
1. Criar um [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) para extração de página única.
1. Chamar `accept(textAbsorber)` no alvo [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) selecionado pelo número da página.
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

Usar `ParagraphAbsorber` quando você precisa de agrupamento estrutural em vez de um único fluxo de texto simples. Ele devolve marcações de página com seções, parágrafos, linhas e `TextFragment` objetos, o que é útil quando a saída deve preservar blocos lógicos de texto.

1. Abra o PDF de origem em um [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instância.
1. Criar um [ParagraphAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/paragraphabsorber/) e visite todo o documento para gerar resultados de marcação de página.
1. Iterar através das marcações de página, seções, parágrafos, linhas e [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) objetos expostos pelo absorvedor.
1. Construir o texto de saída com numeração explícita de página, seção e parágrafo, de modo que o agrupamento estrutural seja preservado.
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
