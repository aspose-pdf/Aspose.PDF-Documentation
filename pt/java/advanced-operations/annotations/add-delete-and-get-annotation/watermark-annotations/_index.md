---
title: Anotações de marca d'água usando Java
linktitle: Anotações de marca d’água
type: docs
weight: 70
url: /java/watermark-annotations/
description: Aprenda como adicionar, inspecionar e excluir anotações de marca d'água em documentos PDF usando Aspose.PDF para Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Trabalhe com anotações de marca d'água em arquivos PDF usando Java.
Abstract: Este artigo explica como criar, inspecionar e remover anotações de marca d’água em documentos PDF usando Aspose.PDF para Java. Abrange a adição de uma anotação de marca d'água de texto com estado e opacidade de texto personalizados, a leitura de áreas de anotação de marca d'água existentes e a exclusão de anotações de marca d'água.
---
As anotações de marca d'água permitem colocar conteúdo de sobreposição reutilizável em uma página enquanto ainda o gerencia por meio da coleção de anotações.

## Adicione uma anotação de marca d’água

Use este exemplo quando precisar de uma anotação de marca d'água de texto com configurações de fonte e opacidade personalizadas.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie uma [WatermarkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/watermarkannotation/) e adicione-a à página.
1. Configure o [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstate/), o texto da marca d'água e a opacidade e salve o documento.

```java
public static void watermarkAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        WatermarkAnnotation watermarkAnnotation = new WatermarkAnnotation(
                page,
                new Rectangle(100, 100, 400, 200, true));

        page.getAnnotations().add(watermarkAnnotation);

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

## Obtenha anotações de marca d'água

Este exemplo verifica a coleção de anotações e imprime o retângulo de cada anotação de marca d’água.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Itere pelas anotações na página de destino.
1. Filtre as anotações por [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Watermark` e imprima seus retângulos.

```java
public static void watermarkGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation a : document.getPages().get_Item(1).getAnnotations()) {
            if (a.getAnnotationType() == AnnotationType.Watermark) {
                System.out.println(a.getRect());
            }
        }
    }
}
```

## Excluir anotações de marca d'água

Use esta abordagem quando as anotações de marca d’água existentes precisarem ser removidas do documento.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Colete anotações do tipo [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Watermark`.
1. Exclua as anotações coletadas e salve o arquivo de saída.

```java
public static void watermarkDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation a : document.getPages().get_Item(1).getAnnotations()) {
            if (a.getAnnotationType() == AnnotationType.Watermark) {
                toDelete.add(a);
            }
        }
        for (Annotation a : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(a);
        }
        document.save(outputFile.toString());
    }
}
```

## Tópicos de anotação relacionados

- [Anotações interativas](/pdf/java/interactive-annotations/)
- [Anotações de marcação](/pdf/java/markup-annotations/)
- [Anotações de segurança](/pdf/java/security-annotations/)
- [Anotações de forma](/pdf/java/shape-annotations/)
- [Anotações de texto](/pdf/java/text-based-annotations/)
- [Importar e exportar anotações](/pdf/java/import-export-annotations/)
