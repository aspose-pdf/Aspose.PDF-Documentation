---
title: Pesquise e extraia texto PDF em Java
linktitle: Pesquise e obtenha texto
type: docs
weight: 60
url: /java/search-and-get-text-from-pdf/
description: Aprenda como pesquisar, inspecionar e extrair texto de documentos PDF em Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Pesquise texto em PDF e inspecione fragmentos extraídos em Java
Abstract: Este artigo explica como pesquisar e extrair texto de documentos PDF usando Aspose.PDF para Java. Abrange TextAbsorber e TextFragmentAbsorber, incluindo extração baseada em região, pesquisas específicas de página, correspondência de regex e frase, inserção de hiperlink, inspeção de texto estilizado e realce de fragmentos.
---
Aspose.PDF para Java oferece suporte à extração de texto bruto e pesquisa em nível de fragmento com coordenadas, estilos e correspondência de regex.

## Extraia texto de todas as páginas com TextAbsorber

Use este exemplo quando precisar de texto simples extraído de uma região selecionada do documento em todas as páginas.

1. Abra o documento PDF de origem.
1. Crie `TextExtractionOptions` e `TextSearchOptions` baseado na região.
1. Execute `TextAbsorber` em todas as páginas e produza o texto extraído.

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

## Extraia texto de uma página com TextAbsorber

Use este exemplo quando a extração de texto simples deve ser limitada a uma página.

1. Abra o documento PDF de origem.
1. Configure a extração de texto e as opções de pesquisa com a região de destino.
1. Execute `TextAbsorber` na página selecionada e produza o resultado.

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

Use este exemplo quando precisar de conteúdo de texto junto com metadados de fonte, posição e cor.

1. Abra o documento PDF de origem.
1. Execute `TextFragmentAbsorber` em todas as páginas.
1. Itere pelos fragmentos e produza seus metadados.

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

## Pesquise uma frase em uma página específica

Use este exemplo quando uma palavra alvo deve ser encontrada apenas em uma página selecionada.

1. Abra o documento PDF de origem.
1. Crie `TextFragmentAbsorber` com a frase alvo.
1. Visite a página escolhida e produza as posições dos fragmentos correspondentes.

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

## Continue uma pesquisa sequencial nas páginas

Use este exemplo quando quiser reutilizar um absorvedor enquanto passa de uma pesquisa de página para outra.

1. Abra o documento PDF de origem e crie um absorvedor reutilizável.
1. Pesquise a primeira página e inspecione os resultados.
1. Continue pesquisando páginas adicionais e revise as correspondências atualizadas.

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

## Pesquise uma frase dentro de um retângulo selecionado

Use este exemplo quando a correspondência de frase for limitada a uma região de uma página.

1. Abra o documento PDF de origem.
1. Crie `TextFragmentAbsorber` com a frase alvo e `TextSearchOptions` baseado em retângulo.
1. Visite a página e produza as posições dos fragmentos correspondentes.

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

Use este exemplo quando as correspondências precisarem ser encontradas por um padrão regex em vez de uma frase fixa.

1. Abra o documento PDF de origem.
1. Crie um `TextFragmentAbsorber` habilitado para regex.
1. Visite a página de destino e produza os fragmentos correspondentes.

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

## Pesquise uma lista de frases por padrões regex

Use este exemplo quando várias frases-alvo devem ser encontradas em uma passagem.

1. Abra o documento PDF de origem.
1. Crie uma matriz de padrões regex e passe-a para `TextFragmentAbsorber`.
1. Visite o documento e inspecione os resultados de regex agrupados.

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

## Encontre texto e transforme-o em hiperlinks

Use este exemplo quando as palavras correspondentes devem ser destacadas e convertidas em links clicáveis.

1. Abra o documento PDF de origem.
1. Pesquise as palavras-alvo com a pesquisa regex habilitada.
1. Atualize o estilo do texto, anexe hiperlinks e salve o PDF modificado.

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

## Pesquise texto por características de estilo

Use este exemplo quando precisar inspecionar fragmentos com base na formatação, como texto em negrito ou invisível.

1. Abra o documento PDF de origem.
1. Execute `TextFragmentAbsorber` na página de destino.
1. Verifique cada estilo de fragmento e produza as entradas correspondentes.

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

## Destacar os resultados da pesquisa em visualizações de páginas renderizadas

Use este exemplo quando as correspondências de texto precisarem ser correlacionadas com imagens de páginas renderizadas para inspeção visual.

1. Crie um dispositivo PNG com a resolução necessária.
1. Pesquise cada página com `TextFragmentAbsorber` e renderize a página em um fluxo de imagem.
1. Escreva as imagens de visualização da página e as coordenadas do fragmento de saída para inspeção.

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
