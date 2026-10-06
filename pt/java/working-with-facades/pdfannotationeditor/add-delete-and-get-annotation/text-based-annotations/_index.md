---
title: Anotações baseadas em texto usando Java
linktitle: Anotações de texto
type: docs
weight: 10
url: /pt/java/pdfannotationeditor-class/text-based-annotations/
description: Aprenda como adicionar, inspecionar e excluir anotações de texto, texto livre e tachado em documentos PDF usando Java.
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Trabalhar com anotações de texto PDF em Java
Abstract: Este artigo explica como criar, ler e remover anotações baseadas em texto em documentos PDF usando Java. Ele cobre anotações de texto, anotações de texto livre e anotações de tachado com base nas implementações de exemplo em Java.
---
## Adicionar uma anotação de texto

1. Abra o PDF de entrada e selecione a página onde a anotação de texto deve ser inserida.
2. Crie o `TextAnnotation`, defina seu retângulo e defina seu título, assunto, flags e cor.
3. Adicione a anotação à página e salve o documento atualizado.

```java
public static void textAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextAnnotation textAnnotation = new TextAnnotation(
                document.getPages().get_Item(1), new Rectangle(299.988, 613.664, 428.708, 680.769, true));
        textAnnotation.setTitle("Aspose User");
        textAnnotation.setSubject("Inserted text 1");
        textAnnotation.setFlags(AnnotationFlags.Print);
        textAnnotation.setColor(Color.getBlue());

        document.getPages().get_Item(1).getAnnotations().add(textAnnotation, false);
        document.save(outputFile.toString());
    }
}
```

## Adicionar uma anotação de texto livre

1. Carregue o PDF de origem e selecione a página de destino e o retângulo para a anotação de texto livre.
2. Crie o `FreeTextAnnotation`, inicialize sua aparência padrão e defina o título e a cor.
3. Adicione a anotação à página e salve o resultado.

```java
public static void freeTextAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        FreeTextAnnotation freeTextAnnotation = new FreeTextAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(299, 713, 308, 720, true),
                new DefaultAppearance());
        freeTextAnnotation.setTitle("Aspose User");
        freeTextAnnotation.setColor(Color.getLightGreen());

        document.getPages().get_Item(1).getAnnotations().add(freeTextAnnotation);
        document.save(outputFile.toString());
    }
}
```
