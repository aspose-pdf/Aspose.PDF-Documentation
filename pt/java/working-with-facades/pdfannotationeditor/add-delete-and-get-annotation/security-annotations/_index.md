---
title: Anotações de segurança usando Java
linktitle: Anotações de segurança
type: docs
weight: 60
url: /java/pdfannotationeditor-class/security-annotations/
description: Aprenda como marcar texto para redação, aplicar anotações de redação e redigir áreas de página selecionadas em arquivos PDF usando Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Edite conteúdo confidencial de PDF em Java com anotações de segurança
Abstract: Este artigo explica como trabalhar com anotações de redação em documentos PDF usando Java. Ele cobre a marcação de texto correspondente com anotações de redação, aplicação permanente de redações e redação de áreas selecionadas com base em retângulos de posicionamento de imagem detectados.
---
## Marcar texto para redação

1. Carregue o PDF e pesquise em todas as páginas o texto que deve ser redigido.
2. Crie um `RedactionAnnotation` para cada fragmento de texto correspondente e configure sua aparência.
3. Adicione as anotações de redação às suas páginas e salve o documento.

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
