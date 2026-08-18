---
title: Substitua texto em PDF por Java
linktitle: Substituir texto em PDF
type: docs
weight: 40
url: /java/replace-text-in-pdf/
description: Aprenda como substituir, reorganizar e remover texto em documentos PDF usando Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /python-net/replace-text-in-a-pdf-document/
TechArticle: true
AlternativeHeadline: Substitua, remova e ajuste o conteúdo de texto em PDF usando Java
Abstract: Este artigo explica fluxos de trabalho de substituição de texto em documentos PDF usando Aspose.PDF para Java. Abrange a substituição de texto em todas as páginas, limitando a substituição a uma região selecionada, ajustando o layout de substituição, usando correspondência baseada em regex, substituindo fontes, removendo todo o texto e excluindo texto oculto.
---
Aspose.PDF para Java fornece recursos de substituição simples e de substituição com reconhecimento de layout por meio de `TextFragmentAbsorber` e opções de substituição.

## Substitua o texto em todas as páginas

Use este exemplo quando a mesma frase precisar ser substituída em todo o documento.

1. Abra o documento PDF de origem.
1. Pesquise todas as páginas pela frase alvo com `TextFragmentAbsorber`.
1. Substitua o texto correspondente e salve o PDF atualizado.

```java
public static void replaceTextOnAllPages(Path inputFile, Path outputFile) {
        String searchPhrase = "PDF";
        String replacePhrase = "pdf";

        try (Document document = new Document(inputFile.toString())) {
            TextFragmentAbsorber absorber = new TextFragmentAbsorber(searchPhrase);
            document.getPages().accept(absorber);

            for (TextFragment fragment : absorber.getTextFragments()) {
                fragment.setText(replacePhrase);
            }

            document.save(outputFile.toString());
        }
    }
```

## Substitua o texto em uma região específica da página

Use este exemplo quando a substituição for limitada a um retângulo selecionado em uma página.

1. Abra o documento PDF de origem.
1. Configure `TextSearchOptions` com limites de página e um retângulo de destino.
1. Substitua o texto correspondente dentro dessa região e salve o documento.

```java
public static void replaceTextInParticularPageRegion(Path inputFile, Path outputFile) {
    String searchPhrase = "doc";
    String replacePhrase = "DOC";

    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber(searchPhrase);
        absorber.getTextSearchOptions().setLimitToPageBounds(true);
        absorber.getTextSearchOptions().setRectangle(new Rectangle(300, 442, 500, 742, true));
        document.getPages().get_Item(1).accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            fragment.setText(replacePhrase);
        }

        document.save(outputFile.toString());
    }
}
```

## Substitua o texto e ajuste o espaçamento dentro de um retângulo deslocado

Use este exemplo quando o texto de substituição deve permanecer na página com espaçamento ajustado, mas o tamanho da fonte deve permanecer inalterado.

1. Abra o PDF de origem e colete fragmentos de texto da página de destino.
1. Modifique o retângulo de substituição e escolha o comportamento `AdjustSpaceWidth`.
1. Defina o novo texto e salve o documento.

```java
public static void replaceTextAndResizeAndShiftWithoutChangingFontSize(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        TextFragment fragment = absorber.getTextFragments().get_Item(1);
        String text = fragment.getText();
        Rectangle rectangle = fragment.getRectangle();
        rectangle.setLLX(rectangle.getLLX() + 50);
        rectangle.setURX(rectangle.getURX() - 50);
        fragment.getReplaceOptions().setRectangle(rectangle);
        fragment.getReplaceOptions().setReplaceAdjustmentAction(TextReplaceOptions.ReplaceAdjustment.AdjustSpaceWidth);
        fragment.setText(text + " " + text);

        document.save(outputFile.toString());
    }
}
```

## Substitua o texto dentro de um retângulo de parágrafo maior

Use este exemplo quando o texto de substituição precisar se expandir para uma área de página maior.

1. Abra o PDF de origem e obtenha o primeiro fragmento de texto da página de destino.
1. Construa um retângulo de substituição maior a partir da caixa de mídia da página.
1. Aplique as opções de substituição e salve o PDF.

```java
public static void replaceTextAndResizeAndShiftParagraph(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        TextFragment fragment = absorber.getTextFragments().get_Item(1);
        String text = fragment.getText();
        Rectangle rectangle = document.getPages().get_Item(1).getMediaBox();
        rectangle.setLLX(rectangle.getLLX() + 20);
        rectangle.setURX(rectangle.getURX() - 20);
        rectangle.setURY(rectangle.getURY() - 20);
        fragment.getReplaceOptions().setRectangle(rectangle);
        fragment.getReplaceOptions().setReplaceAdjustmentAction(TextReplaceOptions.ReplaceAdjustment.AdjustSpaceWidth);
        fragment.setText(text + " " + text);

        document.save(outputFile.toString());
    }
}
```

## Substitua o texto e dimensione a fonte para preencher o retângulo

Use este exemplo quando o texto de substituição precisar ser ampliado para preencher uma área de destino.

1. Abra o PDF de origem e acesse o fragmento de texto de destino.
1. Defina um retângulo de substituição e habilite o ajuste de fonte `ScaleToFill`.
1. Defina o novo texto e salve o documento atualizado.

```java
public static void replaceTextAndResizeAndExpandFont(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        TextFragment fragment = absorber.getTextFragments().get_Item(1);
        String text = fragment.getText();
        fragment.getReplaceOptions().setRectangle(new Rectangle(100, 300, 512, 692, true));
        fragment.getReplaceOptions().setReplaceAdjustmentAction(TextReplaceOptions.ReplaceAdjustment.AdjustSpaceWidth);
        fragment.getReplaceOptions().setFontSizeAdjustmentAction(TextReplaceOptions.FontSizeAdjustment.ScaleToFill);
        fragment.setText(text + " " + text);

        document.save(outputFile.toString());
    }
}
```

## Substitua o texto e reduza-o para caber

Use este exemplo quando o texto de substituição precisar permanecer dentro do retângulo do texto original.

1. Abra o PDF de origem e selecione o fragmento de destino.
1. Reutilize o retângulo do fragmento atual e ative `ShrinkToFit`.
1. Substitua o texto e salve o documento.

```java
public static void replaceTextAndFitTextIntoRectangle(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        TextFragment fragment = absorber.getTextFragments().get_Item(1);
        String text = fragment.getText();
        fragment.getReplaceOptions().setRectangle(fragment.getRectangle());
        fragment.getReplaceOptions().setFontSizeAdjustmentAction(TextReplaceOptions.FontSizeAdjustment.ShrinkToFit);
        fragment.getReplaceOptions().setReplaceAdjustmentAction(TextReplaceOptions.ReplaceAdjustment.AdjustSpaceWidth);
        fragment.setText(text + " " + text);

        document.save(outputFile.toString());
    }
}
```

## Substitua o texto por expressão regular

Use este exemplo quando o texto correspondente precisar ser encontrado por um padrão regex e reestilizado durante a substituição.

1. Abra o documento PDF de origem.
1. Pesquise a página com um `TextFragmentAbsorber` habilitado para regex.
1. Substitua cada correspondência, atualize seu estilo de texto e salve o resultado.

```java
public static void replaceTextBasedOnRegex(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber(Pattern.compile("\\d{4}-\\d{4}"));
        absorber.setTextSearchOptions(new TextSearchOptions(true));
        document.getPages().get_Item(1).accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            fragment.setText("ABC1-2XZY");
            fragment.getTextState().setFont(FontRepository.findFont("Verdana"));
            fragment.getTextState().setFontSize(12);
            fragment.getTextState().setForegroundColor(Color.getBlue());
            fragment.getTextState().setBackgroundColor(Color.getLightGreen());
        }

        document.save(outputFile.toString());
    }
}
```

## Substitua o texto do espaço reservado e deixe a página reorganizar

Use este exemplo quando um espaço reservado precisar ser substituído por um valor real mais longo, preservando o layout da página.

1. Abra o PDF de origem e procure o texto do espaço reservado.
1. Atribua o texto de substituição e atualize suas configurações de fonte.
1. Salve o documento para que o layout seja recalculado.

```java
public static void automaticallyRearrangePageContents(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber("[Long_placeholder_Long_placeholder]");
        document.getPages().accept(absorber);

        for (TextFragment textFragment : absorber.getTextFragments()) {
            textFragment.setText("John Smith, South Development Studio");
            textFragment.getTextState().setFont(FontRepository.findFont("Calibri"));
            textFragment.getTextState().setFontSize(12);
            textFragment.getTextState().setForegroundColor(Color.getNavy());
        }

        document.save(outputFile.toString());
    }
}
```

## Substitua uma fonte por outra

Use este exemplo quando o texto que usa uma fonte incorporada específica precisar ser alterado para outra fonte.

1. Abra o PDF de origem e colete todos os fragmentos de texto.
1. Verifique o nome da fonte de cada fragmento e substitua a fonte de destino.
1. Salve o PDF atualizado.

```java
public static void replaceFonts(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        document.getPages().accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            if ("Arial-BoldMT".equals(fragment.getTextState().getFont().getFontName())) {
                fragment.getTextState().setFont(FontRepository.findFont("Verdana"));
            }
        }

        document.save(outputFile.toString());
    }
}
```

## Substitua fontes e remova recursos de fontes não utilizados

Use este exemplo quando o documento precisar ser limpo após a substituição da fonte.

1. Abra o PDF de origem e configure `TextEditOptions` para remover fontes não utilizadas.
1. Absorva os fragmentos de texto e atribua a fonte substituta.
1. Salve o documento otimizado.

```java
public static void removeUnusedFonts(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextEditOptions options = new TextEditOptions(TextEditOptions.FontReplace.RemoveUnusedFonts);
        TextFragmentAbsorber absorber = new TextFragmentAbsorber(options);
        document.getPages().accept(absorber);

        for (TextFragment textFragment : absorber.getTextFragments()) {
            textFragment.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        }

        document.save(outputFile.toString());
    }
}
```

## Remova todo o texto do documento

Use este exemplo quando todo o conteúdo de texto precisar ser excluído de todas as páginas.

1. Abra o documento PDF de origem.
1. Crie um `TextFragmentAbsorber` e ligue para `removeAllText(document)`.
1. Salve o PDF limpo.

```java
public static void removeAllTextUsingAbsorber1(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.removeAllText(document);
        document.save(outputFile.toString());
    }
}
```

## Remova todo o texto de uma página

Use este exemplo quando todo o texto precisar ser removido apenas de uma página específica.

1. Abra o documento PDF de origem.
1. Crie um `TextFragmentAbsorber` e remova o texto da página de destino.
1. Salve o documento atualizado.

```java
public static void removeAllTextUsingAbsorber2(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.removeAllText(document.getPages().get_Item(1));
        document.save(outputFile.toString());
    }
}
```

## Remover texto de um retângulo selecionado

Use este exemplo quando o texto deve ser excluído somente dentro de uma área de página escolhida.

1. Abra o documento PDF de origem.
1. Crie um `TextFragmentAbsorber` e defina o retângulo a ser limpo.
1. Remova o texto dessa região e salve o documento.

```java
public static void removeAllTextUsingAbsorber3(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.removeAllText(document.getPages().get_Item(1), new Rectangle(10, 200, 120, 600, true));
        document.save(outputFile.toString());
    }
}
```

## Remover texto oculto

Use este exemplo quando fragmentos de texto invisíveis precisarem ser removidos do PDF.

1. Abra o PDF de origem e absorva todos os fragmentos de texto.
1. Verifique cada fragmento quanto ao estado de texto invisível.
1. Limpe o texto oculto e salve o documento.

```java
public static void removeHiddenText(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber textAbsorber = new TextFragmentAbsorber();
        textAbsorber.setTextReplaceOptions(new TextReplaceOptions(TextReplaceOptions.ReplaceAdjustment.None));
        document.getPages().accept(textAbsorber);

        for (TextFragment fragment : textAbsorber.getTextFragments()) {
            if (fragment.getTextState().isInvisible()) {
                fragment.setText("");
            }
        }

        document.save(outputFile.toString());
    }
}
```
