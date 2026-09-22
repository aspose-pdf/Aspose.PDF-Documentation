---
title: Аннотации безопасности на Java
linktitle: Аннотации безопасности
type: docs
weight: 75
url: /ru/java/security-annotations/
description: Узнайте, как пометить текст для удаления, применить аннотации удаления и удалить содержимое выбранных областей страниц PDF с помощью Aspose.PDF for Java.
lastmod: "2026-09-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Удаление конфиденциального содержимого PDF в Java с помощью аннотаций безопасности
Abstract: В этой статье объясняется, как работать с аннотациями удаления в PDF-документах с помощью Aspose.PDF for Java. Рассматриваются пометка найденного текста аннотациями удаления, их применение для безвозвратного удаления содержимого и удаление содержимого выбранных областей на основе обнаруженных прямоугольников размещения изображений.
---
В этом разделе рассматриваются подготовка и применение аннотаций для удаления конфиденциального содержимого PDF.

## Пометка текста аннотациями удаления

Используйте этот пример, чтобы пометить найденный текст аннотациями удаления перед его безвозвратным удалением.

1. Откройте исходный PDF-документ с помощью [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Найдите целевой текст и создайте [RedactionAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/redactionannotation/) для каждого совпадения.
1. Настройте внешний вид аннотаций удаления и сохраните документ.

```java
public static void markTextRedaction(Path inputFile, Path outputFile, String searchTerm) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(searchTerm);
        TextSearchOptions textSearchOptions = new TextSearchOptions(true);
        textFragmentAbsorber.setTextSearchOptions(textSearchOptions);
        document.getPages().accept(textFragmentAbsorber);

        for (var textFragment : textFragmentAbsorber.getTextFragments()) {
            Page page = textFragment.getPage();
            RedactionAnnotation redactionAnnotation = new RedactionAnnotation(page, textFragment.getRectangle());
            redactionAnnotation.setFillColor(Color.getGray());
            redactionAnnotation.setBorderColor(Color.getRed());
            redactionAnnotation.setColor(Color.getWhite());
            redactionAnnotation.setOverlayText("REDACTED");
            redactionAnnotation.setTextAlignment(HorizontalAlignment.Center);
            redactionAnnotation.setRepeat(true);
            page.getAnnotations().add(redactionAnnotation, true);
        }
        document.save(outputFile.toString());
    }
}
```

## Применение существующих аннотаций удаления

В этом примере существующие на странице аннотации удаления применяются для безвозвратного удаления содержимого.

1. Откройте исходный PDF-документ с помощью [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Соберите аннотации типа [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Redaction`.
1. Вызовите `redact()` для каждой собранной аннотации и сохраните обновлённый файл.

```java
public static void applyRedaction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<RedactionAnnotation> redactionAnnotations = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Redaction) {
                redactionAnnotations.add((RedactionAnnotation) annotation);
            }
        }
        for (RedactionAnnotation redactionAnnotation : redactionAnnotations) {
            redactionAnnotation.redact();
        }
        document.save(outputFile.toString());
    }
}
```

## Пометка выбранной области страницы для удаления

Используйте этот подход, когда целевой контент определяется по позиции, а не по совпадению текста.

1. Откройте исходный PDF-документ с помощью [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Определите целевой прямоугольник на странице, например по расположению изображения.
1. Создайте [RedactionAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/redactionannotation/) для этой области и сохраните документ.

```java
public static void redactArea(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber imagePlacementAbsorber = new ImagePlacementAbsorber();
        Page page = document.getPages().get_Item(1);
        page.accept(imagePlacementAbsorber);

        com.aspose.pdf.Rectangle targetRect = imagePlacementAbsorber.getImagePlacements().get_Item(2).getRectangle();
        RedactionAnnotation redactionAnnotation = new RedactionAnnotation(page, targetRect);
        redactionAnnotation.setFillColor(Color.getGray());
        redactionAnnotation.setBorderColor(Color.getRed());
        redactionAnnotation.setColor(Color.getWhite());
        redactionAnnotation.setOverlayText("REDACTED");
        redactionAnnotation.setTextAlignment(HorizontalAlignment.Center);
        redactionAnnotation.setRepeat(true);

        page.getAnnotations().add(redactionAnnotation, true);
        document.save(outputFile.toString());
    }
}
```

## Связанные темы об аннотациях

- [Интерактивные аннотации](/pdf/ru/java/interactive-annotations/)
- [Аннотации разметки](/pdf/ru/java/markup-annotations/)
- [Аннотации фигур](/pdf/ru/java/shape-annotations/)
- [Текстовые аннотации](/pdf/ru/java/text-based-annotations/)
- [Аннотации водяных знаков](/pdf/ru/java/watermark-annotations/)
- [Импорт и экспорт аннотаций](/pdf/ru/java/import-export-annotations/)
