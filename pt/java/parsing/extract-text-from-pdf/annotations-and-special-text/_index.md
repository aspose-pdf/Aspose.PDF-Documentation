---
title: Anotações e texto especial usando Java
linktitle: Anotações e texto especial
type: docs
weight: 40
url: /java/annotation-and-special-text/
description: Aprenda como extrair texto de anotações de carimbo, texto destacado e conteúdo sobrescrito ou subscrito em documentos PDF usando Aspose.PDF para Java.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## Extraia o texto destacado

Itere pelas anotações da página e leia o texto marcado de `HighlightAnnotation`.

1. Abra o PDF de origem em um [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) exemplo.
1. Iterar através do [Anotação](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) objetos no alvo [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Verifique se cada anotação é uma [DestaqueAnotação](https://reference.aspose.com/pdf/java/com.aspose.pdf/highlightannotation/) antes de convertê-lo para a classe de anotação digitada.
1. Leia o texto marcado de cada anotação de destaque e imprima-o no console.

```java
public static void extractHighlightedText(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation instanceof HighlightAnnotation) {
                HighlightAnnotation highlightAnnotation = (HighlightAnnotation) annotation;
                System.out.println(highlightAnnotation.getMarkedText());
            }
        }
    }
}
```

## Extraia texto de anotações de carimbo

Leia o fluxo de aparência normal de uma anotação de carimbo e passe-o `TextAbsorber`.

1. Abra o PDF de origem em um [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) exemplo.
1. Iterar através do [Anotação](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) objetos no alvo [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Filtre as anotações para aquelas cujo tipo é `Stamp`.
1. Crie um [Absorvedor de texto](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) e solicite a entrada de aparência normal do dicionário de aparência de anotação de carimbo.
1. Visite a aparência [Formulário X](https://reference.aspose.com/pdf/java/com.aspose.pdf/xform/) e imprima o texto extraído.

```java
public static void extractStampText(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Stamp) {
                TextAbsorber absorber = new TextAbsorber();
                Object[] xforms = new Object[1];
                if (annotation.getAppearance().tryGetValue("N", xforms) && xforms[0] instanceof XForm) {
                    absorber.visit((XForm) xforms[0]);
                    System.out.println(absorber.getText());
                }
            }
        }
    }
}
```

## Extraia detalhes de texto sobrescrito e subscrito

Usar `TextFragmentAbsorber` quando você precisar do texto extraído e dos sinalizadores sobrescritos ou subscritos em cada fragmento.

1. Abra o PDF de origem em um [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) exemplo.
1. Crie um [TextFragmentAbsorvedor](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragmentabsorber/) para análise de texto em nível de fragmento.
1. Visite o alvo [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) e recolher o seu [Fragmento de Texto](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) objetos.
1. Itere através desses fragmentos e leia o texto junto com os sinalizadores sobrescritos e subscritos de `fragment.getTextState()`.
1. Grave os detalhes extraídos no arquivo de saída.

```java
public static void extractSuperSubDetails(Path inputFile, Path outputFile, int pageNumber) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        document.getPages().get_Item(pageNumber).accept(absorber);
        StringBuilder details = new StringBuilder();
        for (TextFragment fragment : absorber.getTextFragments()) {
            details.append("Text: '").append(fragment.getText())
                    .append("' | Superscript: ").append(fragment.getTextState().isSuperscript())
                    .append(" | Subscript: ").append(fragment.getTextState().isSubscript())
                    .append(System.lineSeparator());
        }
        Files.writeString(outputFile, details.toString());
    }
}
```
