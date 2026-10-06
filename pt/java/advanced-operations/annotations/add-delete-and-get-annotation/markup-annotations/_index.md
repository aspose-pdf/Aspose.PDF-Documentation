---
title: Anotações de marcação usando Java
linktitle: Anotações de marcação
type: docs
weight: 30
url: /pt/java/markup-annotations/
description: Aprenda como adicionar, inspecionar e excluir anotações de realce, sublinhado, ondulado e tachado em documentos PDF usando Aspose.PDF for Java.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Trabalhar com anotações de marcação em arquivos PDF usando Java
Abstract: Este artigo explica como criar, inspecionar e remover anotações de marcação de texto em documentos PDF usando Aspose.PDF for Java. Ele abrange anotações de destaque, sublinhado, ondulado e tachado com base nos exemplos Java do repositório.
---
Os fluxos de trabalho de anotações de marcação nesta seção enfocam comentários no estilo de nota, marcadores de cursor e cenários agrupados de substituição-revisão.

## Adicionar uma anotação de texto

Use este exemplo quando precisar colocar uma anotação de texto no estilo de nota adesiva com metadados de pop-up em uma página.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um [TextAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/textannotation/) e configure seu título, conteúdos, ícone e popup.
1. Adicione a anotação à página e salve o documento.

```java
public static void textAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextAnnotation textAnnotation = new TextAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(299.988, 613.664, 428.708, 680.769, true));
        textAnnotation.setTitle("Aspose User");
        textAnnotation.setSubject("Sticky Note");
        textAnnotation.setContents("This is a text annotation added by Aspose.PDF for Java");
        textAnnotation.setFlags(AnnotationFlags.Print);
        textAnnotation.setColor(Color.getBlue());
        textAnnotation.setIcon(TextIcon.Help);

        PopupAnnotation popup = new PopupAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(428.708, 613.664, 528.708, 713.664, true));
        popup.setOpen(true);
        textAnnotation.setPopup(popup);

        document.getPages().get_Item(1).getAnnotations().add(textAnnotation, false);
        document.save(outputFile.toString());
    }
}
```

## Obter anotações de texto

Este exemplo varre a página e imprime o retângulo de cada anotação de texto.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Itere pelas anotações na página.
1. Filtre anotações por [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Text` e imprima seus retângulos.

```java
public static void textAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Text) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

## Excluir anotações de texto

Use esta abordagem quando as anotações de texto existentes devem ser removidas do documento.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Colete anotações do tipo [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Text`.
1. Exclua as anotações coletadas e salve o arquivo de saída.

```java
public static void textAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Text) {
                toDelete.add(annotation);
            }
        }
        for (Annotation annotation : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(annotation);
        }
        document.save(outputFile.toString());
    }
}
```

## Adicionar uma anotação caret

Use este exemplo quando precisar marcar texto inserido com uma anotação de revisão no estilo caret.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um [CaretAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/caretannotation/) e configure seu pop-up e aparência.
1. Adicione a anotação à página e salve o documento.

```java
public static void caretAnnotationsAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        CaretAnnotation caretAnnotation = new CaretAnnotation(
                page,
                new Rectangle(299.988, 713.664, 308.708, 720.769, true));
        caretAnnotation.setTitle("Aspose User");
        caretAnnotation.setSubject("Inserted text 1");
        caretAnnotation.setFlags(AnnotationFlags.Print);
        caretAnnotation.setColor(Color.getBlue());
        caretAnnotation.setPopup(new PopupAnnotation(
                page,
                new Rectangle(310, 713, 410, 730, true)));
        page.getAnnotations().add(caretAnnotation);

        document.save(outputFile.toString());
    }
}
```

## Obter anotações de caret

Este exemplo lê anotações de cursor existentes e imprime suas localizações.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Itere pelas anotações da página.
1. Filtre anotações por [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Caret` e imprima seus retângulos.

```java
public static void caretAnnotationsGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        for (Annotation annot : page.getAnnotations()) {
            if (annot.getAnnotationType() == AnnotationType.Caret) {
                System.out.println(annot.getRect());
            }
        }
    }
}
```

## Excluir anotações de cursor

Use esta abordagem quando as anotações de caret devem ser removidas da página.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Colete anotações cujo tipo é [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Caret`.
1. Exclua as anotações coletadas e salve o documento de saída.

```java
public static void caretAnnotationsDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        List<Annotation> caretAnnotations = new ArrayList<>();
        for (Annotation annot : page.getAnnotations()) {
            if (annot.getAnnotationType() == AnnotationType.Caret) {
                caretAnnotations.add(annot);
            }
        }
        for (Annotation annot : caretAnnotations) {
            page.getAnnotations().delete(annot);
        }
        document.save(outputFile.toString());
    }
}
```

## Adicionar anotações de substituição agrupadas

Este exemplo combina uma anotação caret com uma anotação de tachado para representar um comentário de revisão no estilo substituir.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie a anotação de caret e o relacionado [StrikeOutAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/strikeoutannotation/).
1. Vincule as anotações através `setInReplyTo` e `setReplyType`, então salve o documento.

```java
public static void replaceAnnotationsAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        CaretAnnotation caretAnnotation = new CaretAnnotation(
                page,
                new Rectangle(361.246, 727.908, 370.081, 735.107, true));
        caretAnnotation.setFlags(AnnotationFlags.Print);
        caretAnnotation.setSubject("Inserted text 2");
        caretAnnotation.setTitle("Aspose User");
        caretAnnotation.setColor(Color.getBlue());
        caretAnnotation.setPopup(new PopupAnnotation(
                page,
                new Rectangle(310, 713, 410, 730, true)));

        StrikeOutAnnotation strikeoutAnnotation = new StrikeOutAnnotation(
                page,
                new Rectangle(318.407, 727.826, 368.916, 740.098, true));
        strikeoutAnnotation.setColor(Color.getBlue());
        strikeoutAnnotation.setQuadPoints(new Point[]{
                new Point(321.66, 739.416),
                new Point(365.664, 739.416),
                new Point(321.66, 728.508),
                new Point(365.664, 728.508)
        });
        strikeoutAnnotation.setSubject("Cross-out");
        strikeoutAnnotation.setInReplyTo(caretAnnotation);
        strikeoutAnnotation.setReplyType(ReplyType.Group);

        page.getAnnotations().add(caretAnnotation);
        page.getAnnotations().add(strikeoutAnnotation);

        document.save(outputFile.toString());
    }
}
```

## Obter anotações de substituição agrupadas

Este exemplo detecta anotações de tachado que participam de um fluxo de trabalho de substituição agrupada.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Itere pelas anotações da página e selecione as anotações de tachado.
1. Verifique a relação de resposta e imprima o retângulo das anotações correspondentes.

```java
public static void replaceAnnotationsGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        for (Annotation annot : page.getAnnotations()) {
            if (annot.getAnnotationType() == AnnotationType.StrikeOut) {
                StrikeOutAnnotation sa = (StrikeOutAnnotation) annot;
                if (sa.getInReplyTo() != null && sa.getReplyType() == ReplyType.Group) {
                    System.out.println("Replace annotation rect: " + sa.getRect());
                }
            }
        }
    }
}
```

## Excluir anotações de substituição agrupadas

Use esta abordagem quando as anotações de strikeout replace-review devem ser removidas da página.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Colete anotações de tachado que representam a marcação de substituição.
1. Exclua as anotações coletadas e salve o documento atualizado.

```java
public static void replaceAnnotationsDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        List<StrikeOutAnnotation> replaceAnnotations = new ArrayList<>();
        for (Annotation annot : page.getAnnotations()) {
            if (annot.getAnnotationType() == AnnotationType.StrikeOut) {
                replaceAnnotations.add((StrikeOutAnnotation) annot);
            }
        }
        for (StrikeOutAnnotation annot : replaceAnnotations) {
            page.getAnnotations().delete(annot);
        }
        document.save(outputFile.toString());
    }
}
```

## Tópicos relacionados à anotação

- [Anotações de texto](/pdf/pt/java/text-based-annotations/)
- [Anotações Interativas](/pdf/pt/java/interactive-annotations/)
- [Anotações de Formas](/pdf/pt/java/shape-annotations/)
- [Anotações de Mídia](/pdf/pt/java/media-annotations/)
- [Anotações de Segurança](/pdf/pt/java/security-annotations/)
- [Anotações de Marca d'água](/pdf/pt/java/watermark-annotations/)
