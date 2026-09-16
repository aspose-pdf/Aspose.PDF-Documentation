---
title: Текстовые аннотации с использованием Java
linktitle: Текстовые аннотации
type: docs
weight: 10
url: /ru/java/text-based-annotations/
description: Узнайте, как добавлять, просматривать и удалять аннотации типа Text, Free Text и Strikeout в PDF‑документах с помощью Aspose.PDF for Java.
lastmod: "2026-09-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Работайте с текстовыми PDF‑аннотациями в Java.
Abstract: В этой статье объясняется, как создавать, читать и удалять текстовые аннотации в PDF‑документах с использованием Aspose.PDF for Java. Рассматриваются текстовые аннотации, аннотации свободного текста и аннотации зачеркивания на основе примеров реализации на Java.
---
Текстовые сценарии аннотирования в этом разделе охватывают свободный текст, выделение, зачеркивание, волнистое подчеркивание и подчеркивание.

## Добавление, получение и удаление аннотаций свободного текста

Используйте эти примеры, когда вам нужно разместить редактируемые текстовые заметки, просмотреть их или удалить их со страницы.

1. Откройте исходный PDF-документ с помощью [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте, найдите или соберите объекты [FreeTextAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/freetextannotation/) на странице.
1. Сохраните обновлённый документ при добавлении или удалении аннотаций.

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

## Добавление, получение и удаление аннотаций выделения

Эти примеры показывают, как создавать разметку выделения, просматривать существующие аннотации выделения и удалять их.

1. Откройте исходный PDF-документ с помощью [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Работайте с объектами [HighlightAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/highlightannotation/) на странице.
1. Сохраните документ после добавления или удаления аннотации.

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

## Добавление, получение и удаление аннотаций зачёркивания

Используйте эти примеры, когда вам нужен зачёркивание фрагментов текста при рецензировании.

1. Откройте исходный PDF-документ с помощью [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте, проверьте или соберите объекты [StrikeOutAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/strikeoutannotation/).
1. Сохраните документ после применения изменений.

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

## Добавление, получение и удаление аннотаций волнистого подчёркивания

Эти примеры используют волнистую разметку, применяемую для выделения текста при проверке.

1. Откройте исходный PDF-документ с помощью [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте, проверьте или соберите объекты [SquigglyAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/squigglyannotation/).
1. Сохраните документ после добавления или удаления аннотаций.

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

## Добавление, получение и удаление аннотаций подчёркивания

Используйте эти примеры, когда текст должен быть подчеркнут, проверен или удалён с помощью API аннотаций.

1. Откройте исходный PDF-документ с помощью [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Работайте с объектами [UnderlineAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/underlineannotation/) на странице.
1. Сохраните документ после добавления или удаления аннотаций.

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

## Добавление аннотации подчёркивания с заданными вершинами четырёхугольника

В этом примере область подчеркивания определяется явно с помощью координат вершин четырёхугольника, полученных из прямоугольника.

1. Откройте исходный PDF-документ с помощью [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [UnderlineAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/underlineannotation/) и вычислите координаты вершин её четырёхугольника.
1. Добавьте аннотацию на страницу и сохраните документ.

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

## Получение помеченного текста из аннотаций подчёркивания

Эти примеры читают текстовое содержимое, связанное с аннотациями подчеркивания, либо как полную строку, либо как отдельные фрагменты.

1. Откройте исходный PDF-документ с помощью [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Переберите аннотации с подчеркиванием на странице.
1. Получите текст с помощью `getMarkedText()` или `getMarkedTextFragments()` и выведите результаты.

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

## Удаление аннотаций подчёркивания по заголовку

Используйте этот подход, когда подчеркивающие аннотации необходимо удалять выборочно в зависимости от их метаданных.

1. Откройте исходный PDF-документ с помощью [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Отфильтруйте аннотации подчёркивания по заголовку.
1. Удалите совпадающие аннотации и сохраните обновлённый документ.

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

## Добавление аннотации подчёркивания и её преобразование в содержимое страницы

В этом примере добавляется аннотация подчеркивания, которая сразу же преобразуется в статическое содержимое страницы.

1. Откройте исходный PDF-документ с помощью [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Добавьте [UnderlineAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/underlineannotation/) на страницу.
1. Вызовите `flatten()` для аннотации и сохраните выходной файл.

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

## Связанные темы об аннотациях

- [Интерактивные аннотации](/pdf/ru/java/interactive-annotations/)
- [Аннотации разметки](/pdf/ru/java/markup-annotations/)
- [Аннотации безопасности](/pdf/ru/java/security-annotations/)
- [Аннотации фигур](/pdf/ru/java/shape-annotations/)
- [Аннотации водяных знаков](/pdf/ru/java/watermark-annotations/)
- [Импорт и экспорт аннотаций](/pdf/ru/java/import-export-annotations/)
