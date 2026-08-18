---
title: Anotações de marcação usando Java
linktitle: Anotações de marcação
type: docs
weight: 20
url: /java/pdfannotationeditor-class/markup-annotations/
description: Aprenda como adicionar, inspecionar e excluir anotações de realce, sublinhado, onduladas e riscadas em documentos PDF usando Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Trabalhe com anotações de marcação em arquivos PDF usando Java
Abstract: Este artigo explica como criar, inspecionar e remover anotações de marcação de texto em documentos PDF usando Java. Ele cobre anotações de destaque, sublinhado, onduladas e riscadas com base nos exemplos Java do repositório.
---
## Adicione anotações de destaque, sublinhado, onduladas ou riscadas

1. Abra o PDF de entrada e selecione a área da página onde a anotação de marcação deve aparecer.
2. Crie o tipo de anotação necessário e configure seus metadados ou propriedades visuais.
3. Adicione a anotação à coleção de páginas e salve o documento.

```java
public static void addTextHighlightAnnotation(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HighlightAnnotation highlightAnnotation = new HighlightAnnotation(
                document.getPages().get_Item(1), new Rectangle(300, 750, 320, 770, true));
        document.getPages().get_Item(1).getAnnotations().add(highlightAnnotation);
        document.save(outputFile.toString());
    }
}
```

```java
public static void addTextUnderlineAnnotation(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        UnderlineAnnotation underlineAnnotation = new UnderlineAnnotation(
                document.getPages().get_Item(1), new Rectangle(299.988, 713.664, 308.708, 720.769, true));
        underlineAnnotation.setTitle("Aspose User");
        underlineAnnotation.setSubject("Inserted Underline 1");
        underlineAnnotation.setFlags(AnnotationFlags.Print);
        underlineAnnotation.setColor(Color.getBlue());
        document.getPages().get_Item(1).getAnnotations().add(underlineAnnotation);
        document.save(outputFile.toString());
    }
}
```
