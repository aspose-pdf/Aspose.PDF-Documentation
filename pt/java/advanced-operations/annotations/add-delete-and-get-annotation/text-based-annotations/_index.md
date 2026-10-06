---
title: Anotações baseadas em texto usando Java
linktitle: Anotações de texto
type: docs
weight: 10
url: /pt/java/text-based-annotations/
description: Aprenda como criar, inspecionar e excluir anotações de PDF baseadas em texto usando Aspose.PDF for Java, incluindo marcações de texto livre, realce, tachado, ondulado e sublinhado.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Trabalhar com anotações de PDF de texto em Java
Abstract: Este artigo demonstra como trabalhar com cinco tipos de anotação baseados em texto no Aspose.PDF for Java, incluindo anotações de texto livre, realce, tachado, ondulado e sublinhado. Aprenda a adicionar, recuperar e excluir anotações, além de técnicas avançadas como marcar texto e achatar marcações interativas.
---
Anotações baseadas em texto permitem que revisores e desenvolvedores adicionem notas interativas, realces e marcações a documentos PDF sem alterar o conteúdo principal. Esta seção aborda cinco tipos práticos de anotações usados em fluxos de trabalho de revisão de documentos, cenários de conformidade e ciclos de feedback colaborativo.

## Guia rápido: tipos de anotação

Este artigo cobre os seguintes tipos de anotação baseados em texto:

- **Free Text**: Caixas de texto editáveis para adicionar notas e comentários
- **Realce**: Ênfase visual em passagens de texto importantes
- **Strikeout**: Marcar texto para exclusão ou revisão durante a revisão
- **Squiggly**: Sublinhado ondulado para indicar erros ou preocupações
- **Sublinhado**: Ênfase tradicional de sublinhado com precisão opcional de quatro pontos

## Adicionar, obter e excluir anotações de texto livre

Anotações de texto livre funcionam como caixas de texto flutuantes que podem ser editadas sem afetar a estrutura do documento. Use estes exemplos para adicionar caixas de comentário, inspecionar suas propriedades ou removê-las.

### Adicionar anotações de texto livre

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um [FreeTextAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/freetextannotation/) com um retângulo e configurações de aparência.
1. Adicione a anotação à página e salve o documento.

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

### Obter anotações de texto livre

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Itere através das anotações na página e filtre por [AnnotationType.FreeText](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).
1. Recupere as propriedades ou limites da anotação.

```java
public static void freeTextAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.FreeText) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

### Excluir anotações de texto livre

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Encontre anotações de texto livre iterando pelas anotações da página e filtrando por tipo.
1. Adicione anotações correspondentes a uma lista de exclusão e removê-las da página.
1. Salve o documento atualizado.

```java
public static void freeTextAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.FreeText) {
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

## Adicionar, obter e excluir anotações de destaque

Anotações de destaque marcam trechos importantes com uma sobreposição semitransparente. Use estes exemplos para criar destaques para revisão de documentos, localizar destaques existentes e limpar a marcação.

### Adicionar anotações de destaque

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um [HighlightAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/highlightannotation/) com um retângulo definindo a área de destaque.
1. Adicione a anotação à página e salve o documento.

```java
public static void textHighlightAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HighlightAnnotation highlightAnnotation = new HighlightAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(300, 750, 320, 770, true));

        document.getPages().get_Item(1).getAnnotations().add(highlightAnnotation);
        document.save(outputFile.toString());
    }
}
```

### Obter anotações de realce

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Itere pelas anotações e filtre por [AnnotationType.Highlight](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).
1. Leia as propriedades da anotação, como limites ou cor.

```java
public static void textHighlightAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Highlight) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

### Excluir anotações de destaque

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Colete anotações de destaque filtrando anotações por tipo.
1. Remova cada anotação da página.
1. Salve o documento atualizado.

```java
public static void textHighlightAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Highlight) {
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

## Adicionar, obter e excluir anotações de tachado

Anotações de tachado riscam o texto para indicar exclusão, rejeição ou revisão. Use estes exemplos para aplicar marcação de tachado durante a revisão de documentos, encontrar texto marcado e remover anotações de tachado.

### Adicionar anotações de tachado

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um [StrikeOutAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/strikeoutannotation/) com um retângulo, título e cor.
1. Adicione a anotação à página e salve o documento.

```java
public static void textStrikeoutAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        StrikeOutAnnotation strikeoutAnnotation = new StrikeOutAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(299.988, 713.664, 308.708, 720.769, true));
        strikeoutAnnotation.setTitle("Aspose User");
        strikeoutAnnotation.setSubject("Inserted text 1");
        strikeoutAnnotation.setFlags(AnnotationFlags.Print);
        strikeoutAnnotation.setColor(Color.getBlue());

        document.getPages().get_Item(1).getAnnotations().add(strikeoutAnnotation);
        document.save(outputFile.toString());
    }
}
```

### Obter anotações de tachado

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Itere pelas anotações e filtre por [AnnotationType.StrikeOut](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).
1. Leia metadados da anotação ou limites.

```java
public static void textStrikeoutAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.StrikeOut) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

### Excluir anotações de tachado

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Colete anotações de tachado filtrando por tipo.
1. Remova cada anotação da página.
1. Salve o documento atualizado.

```java
public static void textStrikeoutAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.StrikeOut) {
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

## Adicionar, obter e excluir anotações onduladas

Anotações onduladas (sublinhados ondulados) destacam erros potenciais, preocupações ou itens que requerem atenção. Use estes exemplos para marcar texto problemático, inspecionar anotações onduladas e removê-las dos documentos.

### Adicionar anotações onduladas

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um [SquigglyAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/squigglyannotation/) com um retângulo e título.
1. Adicione a anotação à página e salve o documento.

```java
public static void textSquigglyAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        SquigglyAnnotation squigglyAnnotation = new SquigglyAnnotation(
                page,
                new Rectangle(67, 317, 261, 459, true));
        squigglyAnnotation.setTitle("John Smith");
        squigglyAnnotation.setColor(Color.getBlue());

        page.getAnnotations().add(squigglyAnnotation);
        document.save(outputFile.toString());
    }
}
```

### Obter anotações onduladas

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Itere pelas anotações e filtre por [AnnotationType.Squiggly](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).
1. Leia limites da anotação ou metadados.

```java
public static void textSquigglyAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Squiggly) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

### Excluir anotações onduladas

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Colete anotações onduladas filtrando por tipo.
1. Remova cada anotação da página.
1. Salve o documento atualizado.

```java
public static void textSquigglyAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Squiggly) {
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

## Adicionar, obter e excluir anotações de sublinhado

Anotações de sublinhado enfatizam trechos importantes com um sublinhado tradicional. Use estes exemplos para criar sublinhados, ler o conteúdo de texto marcado e excluir anotações de sublinhado das páginas.

### Adicionar anotações de sublinhado

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um [UnderlineAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/underlineannotation/) com um retângulo e cor.
1. Adicione a anotação à página e salve o documento.

```java
public static void textUnderlineAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        UnderlineAnnotation underlineAnnotation = new UnderlineAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(299.988, 713.664, 308.708, 720.769, true));
        underlineAnnotation.setTitle("Aspose User");
        underlineAnnotation.setSubject("Inserted Underline 1");
        underlineAnnotation.setFlags(AnnotationFlags.Print);
        underlineAnnotation.setColor(Color.getBlue());

        document.getPages().get_Item(1).getAnnotations().add(underlineAnnotation);
        document.save(outputFile.toString());
    }
}
```

### Obter anotações sublinhadas

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Itere pelas anotações e filtre por [AnnotationType.Underline](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).
1. Leia propriedades da anotação ou limites.

```java
public static void textUnderlineAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Underline) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

### Excluir anotações de sublinhado

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Colete anotações de sublinhado filtrando por tipo.
1. Remova cada anotação da página.
1. Salve o documento atualizado.

```java
public static void textUnderlineAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Underline) {
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

## Adicionar uma anotação de sublinhado com quad points

Este exemplo define a área de sublinhado explicitamente através de pontos quad derivados de um retângulo.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um [UnderlineAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/underlineannotation/) e calcule seus quad points.
1. Adicione a anotação à página e salve o documento.

```java
public static void textUnderlineWithQuadPointsAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Rectangle rect = new Rectangle(299.988, 713.664, 308.708, 720.769, true);
        UnderlineAnnotation underlineAnnotation = new UnderlineAnnotation(
                document.getPages().get_Item(1), rect);
        underlineAnnotation.setTitle("Aspose User");
        underlineAnnotation.setSubject("Inserted Underline with Quad Points");
        underlineAnnotation.setFlags(AnnotationFlags.Print);
        underlineAnnotation.setColor(Color.getBlue());
        underlineAnnotation.setQuadPoints(new com.aspose.pdf.Point[]{
                new com.aspose.pdf.Point(rect.getLLX(), rect.getLLY()),
                new com.aspose.pdf.Point(rect.getURX(), rect.getLLY()),
                new com.aspose.pdf.Point(rect.getURX(), rect.getURY()),
                new com.aspose.pdf.Point(rect.getLLX(), rect.getURY())
        });

        document.getPages().get_Item(1).getAnnotations().add(underlineAnnotation);
        document.save(outputFile.toString());
    }
}
```

## Obter texto marcado a partir de anotações de sublinhado

Recupere o conteúdo de texto real coberto por anotações de sublinhado. Estes exemplos mostram duas abordagens: ler o texto marcado completo como uma única cadeia de caracteres, ou processar fragmentos de texto individualmente para uma análise detalhada.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Itere através das anotações de sublinhado na página.
1. Leia qualquer `getMarkedText()` ou `getMarkedTextFragments()` e imprima os resultados.

```java
public static void textUnderlineMarkedTextGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Underline) {
                UnderlineAnnotation ua = (UnderlineAnnotation) annotation;
                System.out.println("Marked text: " + ua.getMarkedText());
            }
        }
    }
}
```

```java
public static void textUnderlineMarkedFragmentsGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Underline) {
                UnderlineAnnotation ua = (UnderlineAnnotation) annotation;
                for (TextFragment fragment : ua.getMarkedTextFragments()) {
                    System.out.println("Fragment text: " + fragment.getText());
                }
            }
        }
    }
}
```

## Excluir anotações de sublinhado pelo título

Remova anotações seletivamente filtrando por propriedades de metadados como título. Essa abordagem permite a limpeza direcionada de anotações por autor ou finalidade.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Filtre anotações sublinhadas por título.
1. Exclua as anotações correspondentes e salve o documento atualizado.

```java
public static void textUnderlineByTitleDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<UnderlineAnnotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Underline) {
                UnderlineAnnotation ua = (UnderlineAnnotation) annotation;
                if ("Aspose User".equals(ua.getTitle())) {
                    toDelete.add(ua);
                }
            }
        }
        for (UnderlineAnnotation ua : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(ua);
        }
        document.save(outputFile.toString());
    }
}
```

## Adicionar e achatar uma anotação de sublinhado

Converta uma anotação interativa de sublinhado em conteúdo permanente da página, achatando-a. Isso impede edições posteriores enquanto preserva a aparência do sublinhado em qualquer visualizador de PDF.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Adicione um [UnderlineAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/underlineannotation/) para a página.
1. Chame `flatten()` na anotação e salve o arquivo de saída.

```java
public static void textUnderlineFlattenAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        UnderlineAnnotation underlineAnnotation = new UnderlineAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(299.988, 713.664, 308.708, 720.769, true));
        underlineAnnotation.setTitle("Aspose User");
        underlineAnnotation.setSubject("Inserted Underline to Flatten");
        underlineAnnotation.setFlags(AnnotationFlags.Print);
        underlineAnnotation.setColor(Color.getBlue());

        document.getPages().get_Item(1).getAnnotations().add(underlineAnnotation);
        underlineAnnotation.flatten();

        document.save(outputFile.toString());
    }
}
```

## Tópicos relacionados de anotação

- [Anotações Interativas](/pdf/pt/java/interactive-annotations/)
- [Anotações de Marcação](/pdf/pt/java/markup-annotations/)
- [Anotações de Segurança](/pdf/pt/java/security-annotations/)
- [Anotações de Forma](/pdf/pt/java/shape-annotations/)
- [Anotações de Marca d'água](/pdf/pt/java/watermark-annotations/)
- [Importar e Exportar Anotações](/pdf/pt/java/import-export-annotations/)
