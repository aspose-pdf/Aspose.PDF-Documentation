---
title: Pesquisar e Extrair Texto PDF em Java
linktitle: Pesquisar e Obter Texto
type: docs
weight: 60
url: /pt/java/search-and-get-text-from-pdf/
description: Aprenda como pesquisar, inspecionar e extrair texto de documentos PDF em Java.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Pesquise texto em PDF e inspecione fragmentos extraídos em Java
Abstract: Este artigo explica como pesquisar e extrair texto de documentos PDF usando Aspose.PDF for Java. Ele abrange TextAbsorber e TextFragmentAbsorber, incluindo extração baseada em região, buscas específicas por página, correspondência por regex e frase, inserção de hyperlink, inspeção de texto formatado e realce de fragmentos.
---
Aspose.PDF for Java suporta extração de texto bruto e pesquisa em nível de fragmento com coordenadas, estilos e correspondência por expressões regulares.

## Extrair texto de todas as páginas com TextAbsorber

Use este exemplo quando precisar de texto extraído simples de uma região de documento selecionada em todas as páginas.

1. Abra o documento PDF de origem.
1. Criar `TextExtractionOptions` e baseado em região `TextSearchOptions`.
1. Executar `TextAbsorber` em todas as páginas e exiba o texto extraído.

```java
public static void textAbsorberSearch(Path inputFile) {
        try (Document document = new Document(inputFile.toString())) {
            TextExtractionOptions textExtractionOptions = new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure);
            TextSearchOptions textSearchOptions = new TextSearchOptions(new Rectangle(0, 0, 842, 250, true));
            TextAbsorber absorber = new TextAbsorber(textExtractionOptions, textSearchOptions);

            document.getPages().accept(absorber);
            System.out.println("Text fragments found: " + absorber.getText());
        }
    }
```

## Extrair texto de uma página com TextAbsorber

Use este exemplo quando a extração de texto simples deve ser limitada a uma página.

1. Abra o documento PDF de origem.
1. Configure as opções de extração de texto e pesquisa com a região-alvo.
1. Executar `TextAbsorber` na página selecionada e exiba o resultado.

```java
public static void textAbsorberSearchPage(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextExtractionOptions textExtractionOptions = new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure);
        TextSearchOptions textSearchOptions = new TextSearchOptions(new Rectangle(0, 0, 842, 250, true));
        TextAbsorber absorber = new TextAbsorber(textExtractionOptions, textSearchOptions);

        document.getPages().get_Item(2).accept(absorber);
        System.out.println("Text fragments found: " + absorber.getText());
    }
}
```

## Inspecione todos os fragmentos de texto no documento

Use este exemplo quando precisar de conteúdo de texto juntamente com metadados de fonte, posição e cor.

1. Abra o documento PDF de origem.
1. Executar `TextFragmentAbsorber` em todas as páginas.
1. Itere pelos fragmentos e exiba seus metadados.

```java
public static void textFragmentAbsorberSearch(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        document.getPages().accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            System.out.println("Text: " + fragment.getText());
            System.out.println("Position: " + fragment.getPosition());
            System.out.println("XIndent: " + fragment.getPosition().getXIndent());
            System.out.println("YIndent: " + fragment.getPosition().getYIndent());
            System.out.println("Font - Name: " + fragment.getTextState().getFont().getFontName());
            System.out.println("Font - IsAccessible: " + fragment.getTextState().getFont().isAccessible());
            System.out.println("Font - IsEmbedded: " + fragment.getTextState().getFont().isEmbedded());
            System.out.println("Font - IsSubset: " + fragment.getTextState().getFont().isSubset());
            System.out.println("Font Size: " + fragment.getTextState().getFontSize());
            System.out.println("Foreground Color: " + fragment.getTextState().getForegroundColor());
        }
    }
}
```

## Pesquisar uma frase em uma página específica

Use este exemplo quando uma palavra-alvo deve ser encontrada somente em uma página selecionada.

1. Abra o documento PDF de origem.
1. Criar `TextFragmentAbsorber` com a frase alvo.
1. Visite a página escolhida e retorne as posições dos fragmentos correspondentes.

```java
public static void textFragmentAbsorberSearchPage(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber("whale");
        document.getPages().get_Item(2).accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            System.out.println("Text: " + fragment.getText());
            System.out.println("Position: " + fragment.getPosition());
        }
    }
}
```

## Continue uma busca sequencial entre páginas

Use este exemplo quando quiser reutilizar um absorber ao mover de uma pesquisa de página para a próxima.

1. Abra o documento PDF de origem e crie um absorvedor reutilizável.
1. Pesquise a primeira página e examine os resultados.
1. Continue a procurar páginas adicionais e reveja as correspondências atualizadas.

```java
public static void textFragmentAbsorberSequentialSearch(Path inputFile) {
    Document document = new Document(inputFile.toString());
    TextFragmentAbsorber absorber = new TextFragmentAbsorber();
    absorber.setPhrase("whale");

    document.getPages().get_Item(1).accept(absorber);
    for (TextFragment fragment : absorber.getTextFragments()) {
        System.out.println("Text: " + fragment.getText());
        System.out.println("Page: " + fragment.getPage().getNumber());
        System.out.println("Position: " + fragment.getPosition());
    }

    System.out.println("--");

    document.getPages().get_Item(2).accept(absorber);
    absorber.visit(document);

    for (TextFragment fragment : absorber.getTextFragments()) {
        System.out.println("Text: " + fragment.getText());
        System.out.println("Page: " + fragment.getPage().getNumber());
        System.out.println("Position: " + fragment.getPosition());
    }
}
```

## Pesquisar uma frase dentro de um retângulo selecionado

Use este exemplo quando a correspondência de frases deve ser limitada a uma região em uma página.

1. Abra o documento PDF de origem.
1. Criar `TextFragmentAbsorber` com a frase de destino e baseado em retângulo `TextSearchOptions`.
1. Visite a página e exiba as posições dos fragmentos correspondentes.

```java
public static void textFragmentAbsorberSearchPhrase(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber(
                "elephant", new TextSearchOptions(new Rectangle(0, 0, 842, 250, true)));

        document.getPages().get_Item(2).accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            System.out.println("Text: " + fragment.getText());
            System.out.println("Position: " + fragment.getPosition());
        }
    }
}
```

## Pesquisar texto por expressão regular

Use este exemplo quando as correspondências devem ser encontradas por um padrão regex em vez de uma frase fixa.

1. Abra o documento PDF de origem.
1. Crie um regex habilitado `TextFragmentAbsorber`.
1. Visite a página de destino e exiba os fragmentos correspondentes.

```java
public static void textFragmentAbsorberSearchRegex(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber(
                Pattern.compile("\\d+\\.\\d+"), new TextSearchOptions(true));

        document.getPages().get_Item(2).accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            System.out.println("Text: " + fragment.getText());
            System.out.println("Position: " + fragment.getPosition());
        }
    }
}
```

## Pesquisar uma lista de frases por padrões regex

Use este exemplo quando várias frases-alvo devem ser encontradas em uma única passagem.

1. Abra o documento PDF de origem.
1. Crie um array de padrões regex e passe para `TextFragmentAbsorber`.
1. Visite o documento e inspecione os resultados agrupados da expressão regular.

```java
public static void textFragmentAbsorberSearchListOfPhrases(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Pattern[] patterns = new Pattern[] {
                Pattern.compile("whale"),
                Pattern.compile("elephant")
        };
        TextFragmentAbsorber absorber = new TextFragmentAbsorber(patterns, new TextSearchOptions(true));
        document.getPages().accept(absorber);

        for (TextFragmentCollection fragments : absorber.getRegexResults().values()) {
            for (TextFragment fragment : fragments) {
                System.out.println("Text: " + fragment.getText());
                System.out.println("Position: " + fragment.getPosition());
            }
        }
    }
}
```

## Localizar texto e transformá-lo em hyperlinks

Use este exemplo quando palavras correspondentes devem ser destacadas e convertidas em links clicáveis.

1. Abra o documento PDF de origem.
1. Pesquise as palavras-alvo com a pesquisa regex habilitada.
1. Atualize o estilo do texto, anexe hyperlinks e salve o PDF modificado.

```java
public static void textFragmentAbsorberSearchAndAddHyperlink(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber("whale|elephant");
        absorber.setTextSearchOptions(new TextSearchOptions(true));
        absorber.visit(document.getPages().get_Item(1));

        for (TextFragment fragment : absorber.getTextFragments()) {
            fragment.getTextState().setForegroundColor(Color.getBlue());
            fragment.getTextState().setUnderline(true);
            fragment.setHyperlink(new WebHyperlink("https://en.wikipedia.org/wiki/" + fragment.getText()));
        }

        document.save(inputFile.toString().replace("in.pdf", "out.pdf"));
    }
}
```

## Pesquisar texto por características de estilo

Use este exemplo quando precisar inspecionar fragmentos com base na formatação, como negrito ou texto invisível.

1. Abra o documento PDF de origem.
1. Executar `TextFragmentAbsorber` na página de destino.
1. Verifique cada estilo de fragmento e exiba as entradas correspondentes.

```java
public static void textFragmentAbsorberSearchStyledText(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.setTextSearchOptions(new TextSearchOptions(true));
        absorber.visit(document.getPages().get_Item(1));

        for (TextFragment fragment : absorber.getTextFragments()) {
            if (fragment.getTextState().getFontStyle() == FontStyles.Bold) {
                System.out.println("Bold: " + fragment.getText());
            }
            if (fragment.getTextState().isInvisible()) {
                System.out.println("Invisible: " + fragment.getText());
            }
        }
    }
}
```

## Realçar resultados da pesquisa nas visualizações de página renderizadas

Use este exemplo quando as correspondências de texto devem ser correlacionadas com imagens de página renderizadas para inspeção visual.

1. Crie um dispositivo PNG com a resolução necessária.
1. Pesquisar cada página com `TextFragmentAbsorber` e renderize a página para um fluxo de imagem.
1. Escreva as imagens de pré-visualização da página e forneça as coordenadas dos fragmentos para inspeção.

```java
public static void textFragmentAbsorberSearchAndHighlight(Path inputFile) throws Exception {
    int resolution = 150;
    PngDevice pngDevice = new PngDevice(new Resolution(resolution, resolution));

    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber(Pattern.compile("[\\S]+"));
        absorber.setTextSearchOptions(new TextSearchOptions(true));

        for (int pageNumber = 1; pageNumber <= document.getPages().size(); pageNumber++) {
            Page page = document.getPages().get_Item(pageNumber);
            page.accept(absorber);

            try (ByteArrayOutputStream stream = new ByteArrayOutputStream()) {
                pngDevice.process(page, stream);
                Path output = Path.of(inputFile.toString().replace("_in.pdf", page.getNumber() + "_out.png"));
                Files.write(output, stream.toByteArray());
            }

            for (TextFragment textFragment : absorber.getTextFragments()) {
                Rectangle pageRect = page.getPageRect(true);
                System.out.println("TextFragment = " + textFragment.getText()
                        + " Page URY = " + pageRect.getURY()
                        + " TextFragment URY = " + textFragment.getRectangle().getURY());
            }
        }
    }
}
```
