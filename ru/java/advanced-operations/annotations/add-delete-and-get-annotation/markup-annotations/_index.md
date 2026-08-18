---
title: Разметка аннотаций с использованием Java
linktitle: Разметка аннотаций
type: docs
weight: 30
url: /java/markup-annotations/
description: Узнайте, как добавлять, проверять и удалять выделение, подчеркивание, волнистую линию и зачеркивание аннотаций в PDF-документах с помощью Aspose.PDF для Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Работайте с аннотациями разметки в файлах PDF с помощью Java.
Abstract: В этой статье объясняется, как создавать, проверять и удалять аннотации текстовой разметки в документах PDF с помощью Aspose.PDF для Java. Он охватывает выделение, подчеркивание, волнистую линию и зачеркивание аннотаций на основе примеров Java из репозитория.
---
Рабочие процессы разметки аннотаций в этом разделе сосредоточены на комментариях в стиле примечаний, маркерах курсора и сгруппированных сценариях замены-проверки.

## Добавьте текстовую аннотацию

Используйте этот пример, когда вам нужно разместить на странице текстовую аннотацию в стиле заметки с метаданными всплывающего окна.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [TextAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/textannotation/) и настройте его заголовок, содержимое, значок и всплывающее окно.
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

В этом примере страница сканируется и печатается прямоугольник каждой текстовой аннотации.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Перебирайте аннотации на странице.
1. Отфильтруйте аннотации по [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Text` и распечатайте их прямоугольники.

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

## Удаление текстовых аннотаций

Используйте этот подход, когда существующие текстовые аннотации необходимо удалить из документа.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Собирайте аннотации типа [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Text`.
1. Удалите собранные аннотации и сохраните выходной файл.

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

## Добавьте аннотацию курсора

Используйте этот пример, если вам нужно пометить вставленный текст аннотацией обзора в виде курсора.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [CaretAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/caretannotation/) и настройте его всплывающее окно и внешний вид.
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

## Получите аннотации курсора

В этом примере считываются существующие аннотации курсора и печатается их расположение.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Перебирайте аннотации страниц.
1. Отфильтруйте аннотации по [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Caret` и распечатайте их прямоугольники.

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

## Удаление аннотаций каретки

Используйте этот подход, когда аннотации курсора необходимо удалить со страницы.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Собирайте аннотации типа [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Caret`.
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

В этом примере аннотация курсора сочетается с аннотацией зачеркивания, чтобы представить комментарий к обзору в стиле замены.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте аннотацию курсора и связанную с ней [StrikeOutAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/strikeoutannotation/).
1. Свяжите аннотации через `setInReplyTo` и `setReplyType`, затем сохраните документ.

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

## Получите сгруппированные аннотации замены

В этом примере обнаруживаются зачеркнутые аннотации, которые участвуют в рабочем процессе групповой замены.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Перейдите по аннотациям страницы и выберите зачеркнутые аннотации.
1. Проверьте взаимосвязь ответа и распечатайте прямоугольник совпадающих аннотаций.

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

## Удаление сгруппированных аннотаций замены

Используйте этот подход, когда необходимо удалить со страницы зачеркнутые аннотации замены и проверки.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Соберите зачеркнутые аннотации, которые представляют собой разметку замены.
1. Удалите собранные аннотации и сохраните обновленный документ.

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

- [Текстовые аннотации](/pdf/java/text-based-annotations/)
- [Интерактивные аннотации](/pdf/java/interactive-annotations/)
- [Аннотации к фигурам](/pdf/java/shape-annotations/)
- [Медиа-аннотации](/pdf/java/media-annotations/)
- [Аннотации безопасности](/pdf/java/security-annotations/)
- [Аннотации к водяным знакам](/pdf/java/watermark-annotations/)
