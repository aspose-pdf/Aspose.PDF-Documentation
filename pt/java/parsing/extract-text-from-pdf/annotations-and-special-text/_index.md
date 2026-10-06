---
title: Anotações e Texto Especial usando Java
linktitle: Anotações e Texto Especial
type: docs
weight: 40
url: /pt/java/annotation-and-special-text/
description: Aprenda como extrair texto de anotações de selo, texto destacado e conteúdo sobrescrito ou subscrito em documentos PDF usando Aspose.PDF for Java.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## Extrair texto destacado

Iterar pelas anotações da página e ler o texto marcado de `HighlightAnnotation`.

1. Abra o PDF de origem em um [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instância.
1. Iterar através do [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) objetos no destino [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Verifique se cada anotação é um [HighlightAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/highlightannotation/) antes de convertê-la para a classe de anotação tipada.
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

## Extrair texto de anotações de carimbo

Leia o fluxo de aparência normal de uma anotação de carimbo e passe‑o adiante `TextAbsorber`.

1. Abra o PDF de origem em um [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instância.
1. Iterar através do [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) objetos no destino [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Filtre as anotações para aquelas cujo tipo é `Stamp`.
1. Criar um [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) e solicite a entrada de aparência normal do dicionário de aparência da anotação de carimbo.
1. Visite a aparência [XForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/xform/) e imprima o texto extraído.

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

## Extrair detalhes de texto sobrescrito e subscrito

Usar `TextFragmentAbsorber` quando você precisa tanto do texto extraído quanto das marcações de sobrescrito ou subscrito em cada fragmento.

1. Abra o PDF de origem em um [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instância.
1. Criar um [TextFragmentAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragmentabsorber/) para análise de texto em nível de fragmento.
1. Visite o destino [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) e coletar o seu [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) objetos.
1. Itere pelos fragmentos e leia o texto junto com as bandeiras de sobrescrito e subscrito de `fragment.getTextState()`.
1. Escreva os detalhes extraídos no arquivo de saída.

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
