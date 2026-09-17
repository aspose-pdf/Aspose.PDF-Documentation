---
title: Аннотации водяных знаков с использованием Java
linktitle: Аннотации водяных знаков
type: docs
weight: 70
url: /ru/java/watermark-annotations/
description: Узнайте, как добавлять, просматривать и удалять аннотации водяных знаков в PDF‑документах с помощью Aspose.PDF for Java.
lastmod: "2026-09-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Работайте с аннотациями водяных знаков в PDF‑файлах с использованием Java.
Abstract: В этой статье объясняется, как создавать, проверять и удалять аннотации водяных знаков в PDF‑документах с использованием Aspose.PDF for Java. Рассматривается добавление текстовой аннотации водяного знака с пользовательским состоянием текста и непрозрачностью, чтение существующих областей аннотаций водяных знаков и удаление аннотаций водяных знаков.
---
Аннотации водяного знака позволяют размещать повторно используемое наложенное содержимое на странице, управляя им через коллекцию аннотаций.

## Добавление аннотации водяного знака

Используйте этот пример, когда вам нужна текстовая аннотация водяного знака с пользовательскими настройками шрифта и непрозрачностью.

1. Откройте исходный PDF-документ с помощью [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [WatermarkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/watermarkannotation/) и добавьте её на страницу.
1. Настройте [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstate/), текст водяного знака и непрозрачность, затем сохраните документ.

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

## Получение аннотаций водяных знаков

Этот пример сканирует коллекцию аннотаций и выводит прямоугольник каждой аннотации водяного знака.

1. Откройте исходный PDF-документ с помощью [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Переберите аннотации на целевой странице.
1. Отфильтруйте аннотации по [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Watermark` и выведите их прямоугольники.

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

Используйте этот подход, когда существующие аннотации водяных знаков должны быть удалены из документа.

1. Откройте исходный PDF-документ с помощью [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Соберите аннотации типа [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Watermark`.
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

## Связанные темы об аннотациях

- [Интерактивные аннотации](/pdf/ru/java/interactive-annotations/)
- [Аннотации разметки](/pdf/ru/java/markup-annotations/)
- [Аннотации безопасности](/pdf/ru/java/security-annotations/)
- [Аннотации фигур](/pdf/ru/java/shape-annotations/)
- [Текстовые аннотации](/pdf/ru/java/text-based-annotations/)
- [Импорт и экспорт аннотаций](/pdf/ru/java/import-export-annotations/)
