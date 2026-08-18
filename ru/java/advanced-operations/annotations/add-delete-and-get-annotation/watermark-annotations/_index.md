---
title: Аннотации водяных знаков с использованием Java
linktitle: Аннотации водяных знаков
type: docs
weight: 70
url: /java/watermark-annotations/
description: Узнайте, как добавлять, проверять и удалять аннотации водяных знаков в документах PDF с помощью Aspose.PDF для Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Работайте с аннотациями водяных знаков в файлах PDF с помощью Java.
Abstract: В этой статье объясняется, как создавать, проверять и удалять аннотации водяных знаков в документах PDF с помощью Aspose.PDF для Java. В нем рассматривается добавление текстовых аннотаций с водяными знаками с настраиваемым состоянием и непрозрачностью текста, чтение существующих областей аннотаций с водяными знаками и удаление аннотаций с водяными знаками.
---
Аннотации с водяными знаками позволяют размещать на странице повторно используемый контент, сохраняя при этом управление им через коллекцию аннотаций.

## Добавьте аннотацию водяного знака

Используйте этот пример, если вам нужна текстовая аннотация водяного знака с пользовательскими настройками шрифта и непрозрачностью.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [WatermarkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/watermarkannotation/) и добавьте его на страницу.
1. Настройте [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstate/), текст водяного знака и непрозрачность, а затем сохраните документ.

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

## Получите аннотации с водяными знаками

В этом примере сканируется коллекция аннотаций и печатается прямоугольник каждой аннотации водяного знака.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Перебирайте аннотации на целевой странице.
1. Отфильтруйте аннотации по [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Watermark` и распечатайте их прямоугольники.

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

## Удаление аннотаций водяных знаков

Используйте этот подход, когда существующие аннотации водяных знаков необходимо удалить из документа.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Собирайте аннотации типа [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Watermark`.
1. Удалите собранные аннотации и сохраните выходной файл.

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

## Связанные темы аннотаций

- [Интерактивные аннотации](/pdf/java/interactive-annotations/)
- [Аннотации разметки](/pdf/java/markup-annotations/)
- [Аннотации безопасности](/pdf/java/security-annotations/)
- [Аннотации к фигурам](/pdf/java/shape-annotations/)
- [Текстовые аннотации](/pdf/java/text-based-annotations/)
- [Импорт и экспорт аннотаций](/pdf/java/import-export-annotations/)
