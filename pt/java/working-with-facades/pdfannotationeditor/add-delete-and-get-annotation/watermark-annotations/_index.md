---
title: Anotações de marca d'água usando Java
linktitle: Anotações de marca d’água
type: docs
weight: 70
url: /java/pdfannotationeditor-class/watermark-annotations/
description: Aprenda como adicionar, inspecionar e excluir anotações de marca d'água em documentos PDF usando Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Trabalhe com anotações de marca d’água em arquivos PDF usando Java
Abstract: Este artigo explica como criar, inspecionar e remover anotações de marca d'água em documentos PDF usando Java. Abrange a adição de uma anotação de marca d'água de texto com estado e opacidade de texto personalizados, a leitura de áreas de anotação de marca d'água existentes e a exclusão de anotações de marca d'água.
---
## Adicione uma anotação de marca d’água

1. Abra o PDF de entrada e defina o retângulo onde a anotação da marca d'água será colocada.
2. Crie `WatermarkAnnotation`, adicione-o à página e configure o estado e a opacidade do texto da marca d'água.
3. Aplique as linhas de texto da marca d'água e salve o PDF modificado.

```java
public static void watermarkAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        WatermarkAnnotation watermarkAnnotation = new WatermarkAnnotation(
                document.getPages().get_Item(1), new Rectangle(100, 0, 400, 100, true));

        document.getPages().get_Item(1).getAnnotations().add(watermarkAnnotation);

        TextState textState = new TextState();
        textState.setForegroundColor(Color.getBlue());
        textState.setFontSize(25);
        textState.setFont(FontRepository.findFont("Arial"));

        watermarkAnnotation.setOpacity(0.5);
        watermarkAnnotation.setTextAndState(new String[]{"HELLO", "Line 1", "Line 2"}, textState);

        document.save(outputFile.toString());
    }
}
```
