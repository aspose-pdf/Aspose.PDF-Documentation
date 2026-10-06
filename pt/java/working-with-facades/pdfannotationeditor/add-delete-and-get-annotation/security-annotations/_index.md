---
title: Anotações de segurança usando Java
linktitle: Anotações de segurança
type: docs
weight: 60
url: /pt/java/pdfannotationeditor-class/security-annotations/
description: Aprenda como marcar texto para redação, aplicar anotações de redação e censurar áreas selecionadas da página em arquivos PDF usando Java.
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Redija conteúdo sensível de PDF em Java com anotações de segurança
Abstract: Este artigo explica como trabalhar com anotações de redação em documentos PDF usando Java. Ele cobre a marcação de texto correspondido com anotações de redação, a aplicação permanente de redações e a censura de áreas selecionadas com base em retângulos de posicionamento de imagem detectados.
---
## Marcar texto para redação

1. Carregue o PDF e procure em todas as páginas o texto que deve ser ocultado.
2. Crie um `RedactionAnnotation` para cada fragmento de texto correspondido e configure sua aparência.
3. Adicione as anotações de ocultação às suas páginas e salve o documento.

```java
public static void markTextRedaction(Path inputFile, Path outputFile, String searchTerm) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(searchTerm);
        TextSearchOptions textSearchOptions = new TextSearchOptions(true);
        textFragmentAbsorber.setTextSearchOptions(textSearchOptions);
        document.getPages().accept(textFragmentAbsorber);

        for (TextFragment textFragment : textFragmentAbsorber.getTextFragments()) {
            Page page = textFragment.getPage();
            Rectangle annotationRectangle = textFragment.getRectangle();
            RedactionAnnotation annotation = new RedactionAnnotation(page, annotationRectangle);
            annotation.setFillColor(Color.getGray());
            annotation.setBorderColor(Color.getRed());
            annotation.setColor(Color.getWhite());
            annotation.setOverlayText("REDACTED");
            annotation.setTextAlignment(HorizontalAlignment.Center);
            annotation.setRepeat(true);
            page.getAnnotations().add(annotation, true);
        }

        document.save(outputFile.toString());
    }
}
```
