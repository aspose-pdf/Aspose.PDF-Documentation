---
title: Anotações baseadas em texto usando Java
linktitle: Anotações de texto
type: docs
weight: 10
url: /java/pdfannotationeditor-class/text-based-annotations/
description: Aprenda como adicionar, inspecionar e excluir texto, texto livre e anotações tachadas em documentos PDF usando Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Trabalhe com anotações de texto em PDF em Java
Abstract: Este artigo explica como criar, ler e remover anotações baseadas em texto em documentos PDF usando Java. Abrange anotações de texto, anotações de texto livre e anotações riscadas com base nas implementações de exemplo Java.
---
## Adicione uma anotação de texto

1. Abra o PDF de entrada e direcione a página onde a anotação de texto deve ser colocada.
2. Crie o `TextAnnotation`, defina seu retângulo e defina seu título, assunto, bandeiras e cor.
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

## Adicione uma anotação de texto livre

1. Carregue o PDF de origem e selecione a página de destino e o retângulo para a nota de texto livre.
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
