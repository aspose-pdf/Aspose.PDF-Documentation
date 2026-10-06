---
title: Anotações de segurança usando Java
linktitle: Anotações de segurança
type: docs
weight: 75
url: /pt/java/security-annotations/
description: Aprenda como marcar texto para remoção, aplicar anotações de remoção e remover áreas selecionadas da página em arquivos PDF usando Aspose.PDF for Java.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Remova conteúdo sensível de PDF em Java com anotações de segurança
Abstract: Este artigo explica como trabalhar com anotações de redação em documentos PDF usando Aspose.PDF for Java. Ele aborda a marcação de texto correspondido com anotações de redação, a aplicação permanente de redações e a redação de áreas selecionadas com base em retângulos de posicionamento de imagens detectados.
---
Os fluxos de trabalho de anotação de segurança nesta seção focam na preparação e aplicação de redações ao conteúdo PDF sensível.

## Marcar texto com anotações de redação

Use este exemplo quando o texto correspondente deve ser coberto por anotações de redação antes que a redação seja aplicada permanentemente.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Pesquise o texto alvo e crie um [RedactionAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/redactionannotation/) para cada correspondência.
1. Configure a aparência da redação e salve o documento.

```java
public static void markTextRedaction(Path inputFile, Path outputFile, String searchTerm) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(searchTerm);
        TextSearchOptions textSearchOptions = new TextSearchOptions(true);
        textFragmentAbsorber.setTextSearchOptions(textSearchOptions);
        document.getPages().accept(textFragmentAbsorber);

        for (var textFragment : textFragmentAbsorber.getTextFragments()) {
            Page page = textFragment.getPage();
            RedactionAnnotation redactionAnnotation = new RedactionAnnotation(page, textFragment.getRectangle());
            redactionAnnotation.setFillColor(Color.getGray());
            redactionAnnotation.setBorderColor(Color.getRed());
            redactionAnnotation.setColor(Color.getWhite());
            redactionAnnotation.setOverlayText("REDACTED");
            redactionAnnotation.setTextAlignment(HorizontalAlignment.Center);
            redactionAnnotation.setRepeat(true);
            page.getAnnotations().add(redactionAnnotation, true);
        }
        document.save(outputFile.toString());
    }
}
```

## Aplicar redações existentes

Este exemplo aplica permanentemente anotações de redação que já existem na página.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Colete anotações do tipo [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Redaction`.
1. Chame `redact()` em cada anotação coletada e salve o arquivo atualizado.

```java
public static void applyRedaction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<RedactionAnnotation> redactionAnnotations = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Redaction) {
                redactionAnnotations.add((RedactionAnnotation) annotation);
            }
        }
        for (RedactionAnnotation redactionAnnotation : redactionAnnotations) {
            redactionAnnotation.redact();
        }
        document.save(outputFile.toString());
    }
}
```

## Redigir uma área de página selecionada

Use esta abordagem quando o conteúdo alvo for identificado por posição em vez de por correspondência de texto.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Detecte o retângulo alvo na página, por exemplo a partir de uma colocação de imagem.
1. Crie um [RedactionAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/redactionannotation/) para essa área e salvar o documento.

```java
public static void redactArea(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber imagePlacementAbsorber = new ImagePlacementAbsorber();
        Page page = document.getPages().get_Item(1);
        page.accept(imagePlacementAbsorber);

        com.aspose.pdf.Rectangle targetRect = imagePlacementAbsorber.getImagePlacements().get_Item(2).getRectangle();
        RedactionAnnotation redactionAnnotation = new RedactionAnnotation(page, targetRect);
        redactionAnnotation.setFillColor(Color.getGray());
        redactionAnnotation.setBorderColor(Color.getRed());
        redactionAnnotation.setColor(Color.getWhite());
        redactionAnnotation.setOverlayText("REDACTED");
        redactionAnnotation.setTextAlignment(HorizontalAlignment.Center);
        redactionAnnotation.setRepeat(true);

        page.getAnnotations().add(redactionAnnotation, true);
        document.save(outputFile.toString());
    }
}
```

## Tópicos de anotação relacionados

- [Anotações interativas](/pdf/pt/java/interactive-annotations/)
- [Anotações de marcação](/pdf/pt/java/markup-annotations/)
- [Anotações de forma](/pdf/pt/java/shape-annotations/)
- [Anotações de Texto](/pdf/pt/java/text-based-annotations/)
- [Anotações de Marca d'água](/pdf/pt/java/watermark-annotations/)
- [Importar e Exportar Anotações](/pdf/pt/java/import-export-annotations/)
