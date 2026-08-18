---
title: Аннотации безопасности с использованием Java
linktitle: Аннотации безопасности
type: docs
weight: 75
url: /java/security-annotations/
description: Узнайте, как помечать текст для редактирования, применять аннотации редактирования и редактировать выбранные области страниц в файлах PDF с помощью Aspose.PDF для Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Редактируйте конфиденциальное содержимое PDF-файлов на Java с помощью аннотаций безопасности.
Abstract: В этой статье объясняется, как работать с аннотациями редактирования в PDF-документах с помощью Aspose.PDF для Java. Он охватывает маркировку совпадающего текста с помощью примечаний редактирования, постоянное применение исправлений и редактирование выбранных областей на основе обнаруженных прямоугольников размещения изображений.
---
Рабочие процессы аннотаций безопасности в этом разделе сосредоточены на подготовке и применении изменений к конфиденциальному содержимому PDF.

## Пометить текст аннотациями редактирования

Используйте этот пример, когда соответствующий текст должен быть покрыт аннотациями редактирования, прежде чем редактирование будет применено навсегда.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Найдите целевой текст и создайте [RedactionAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/redactionannotation/) для каждого совпадения.
1. Настройте внешний вид редактирования и сохраните документ.

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

## Применить существующие исправления

В этом примере навсегда применяются аннотации редактирования, которые уже существуют на странице.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Собирайте аннотации типа [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Redaction`.
1. Вызовите `redact()` для каждой собранной аннотации и сохраните обновленный файл.

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

## Редактировать выбранную область страницы

Используйте этот подход, когда целевой контент определяется по положению, а не по сопоставлению текста.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Определите целевой прямоугольник на странице, например, по месту размещения изображения.
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

## Связанные темы аннотаций

- [Интерактивные аннотации](/pdf/java/interactive-annotations/)
- [Аннотации разметки](/pdf/java/markup-annotations/)
- [Аннотации к фигурам](/pdf/java/shape-annotations/)
- [Текстовые аннотации](/pdf/java/text-based-annotations/)
- [Аннотации к водяным знакам](/pdf/java/watermark-annotations/)
- [Импорт и экспорт аннотаций](/pdf/java/import-export-annotations/)
