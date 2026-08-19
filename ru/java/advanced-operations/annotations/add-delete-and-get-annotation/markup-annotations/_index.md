---
title: Разметка аннотаций с использованием Java
linktitle: Разметка аннотаций
type: docs
weight: 30
url: /ru/java/markup-annotations/
description: Узнайте, как добавлять, просматривать и удалять аннотации выделения, подчеркивания, волнистого подчёркивания и зачеркивания в PDF‑документах с помощью Aspose.PDF for Java.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Работайте с разметочными аннотациями в PDF‑файлах с использованием Java.
Abstract: В этой статье объясняется, как создавать, проверять и удалять аннотации разметки текста в PDF‑документах с использованием Aspose.PDF for Java. Охватываются аннотации выделения, подчеркивания, волнистой линии и зачеркивания на основе примеров Java из репозитория.
---
Рабочие процессы разметки аннотаций в этом разделе сосредоточены на комментариях в виде заметок, маркерах‑каретах и сценариях групповой замены‑обзора.

## Добавьте текстовую аннотацию

Используйте этот пример, когда вам нужно разместить текстовую аннотацию в стиле стикер-ноты с метаданными всплывающего окна на странице.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [Текстовая аннотация](https://reference.aspose.com/pdf/java/com.aspose.pdf/textannotation/) и настройте его заголовок, содержимое, значок и всплывающее окно.
1. Добавьте аннотацию на страницу и сохраните документ.

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

## Получите текстовые аннотации

Этот пример сканирует страницу и выводит прямоугольник каждой текстовой аннотации.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Итерировать аннотации на странице.
1. Фильтровать аннотации по [ТипАннотации](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Text` и распечатать их прямоугольники.

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

## Удалите текстовые аннотации

Используйте этот подход, когда существующие текстовые аннотации следует удалить из документа.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Собрать аннотации типа [ТипАннотации](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Text`.
1. Удалите собранные аннотации и сохраните файл вывода.

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

## Добавьте кареточную аннотацию

Используйте этот пример, когда необходимо отметить вставленный текст аннотацией обзора в виде каретки.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [Аннотация-каретка](https://reference.aspose.com/pdf/java/com.aspose.pdf/caretannotation/) и настройте его всплывающее окно и внешний вид.
1. Добавьте аннотацию на страницу и сохраните документ.

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

## Получите аннотации caret

Этот пример читает существующие аннотации caret и выводит их расположения.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Итерировать по аннотациям страницы.
1. Фильтровать аннотации по [ТипАннотации](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Caret` и распечатать их прямоугольники.

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

## Удалите аннотации caret

Используйте этот подход, когда нужно удалить каретные аннотации со страницы.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Соберите аннотации, тип которых [ТипАннотации](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Caret`.
1. Удалите собранные аннотации и сохраните выходной документ.

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

## Добавьте сгруппированные аннотации замены

Этот пример сочетает аннотацию caret с аннотацией strikeout, чтобы представить комментарий рецензирования в стиле замены.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте аннотацию caret и связанные с ней [StrikeOutAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/strikeoutannotation/).
1. Связать аннотации через `setInReplyTo` и `setReplyType`, затем сохраните документ.

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

## Получите группированные аннотации замены

Этот пример обнаруживает аннотации зачеркивания, которые участвуют в групповом процессе замены.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Пройдите по аннотациям страницы и выберите аннотации зачёркивания.
1. Проверьте связь ответов и выведите прямоугольник совпадающих аннотаций.

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

## Удалите сгруппированные заменяющие аннотации

Используйте этот подход, когда необходимо удалить с страницы аннотации вычеркивания replace-review.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Соберите аннотации зачеркивания, которые представляют разметку замены.
1. Удалите собранные аннотации и сохраните обновлённый документ.

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

## Связанные темы аннотаций

- [Текстовые аннотации](/pdf/ru/java/text-based-annotations/)
- [Интерактивные аннотации](/pdf/ru/java/interactive-annotations/)
- [Фигурные аннотации](/pdf/ru/java/shape-annotations/)
- [Медиа-аннотации](/pdf/ru/java/media-annotations/)
- [Аннотации безопасности](/pdf/ru/java/security-annotations/)
- [Аннотации водяного знака](/pdf/ru/java/watermark-annotations/)

