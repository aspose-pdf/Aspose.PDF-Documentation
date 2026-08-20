---
title: Аннотации безопасности с использованием Java
linktitle: Аннотации безопасности
type: docs
weight: 75
url: /ru/java/security-annotations/
description: Узнайте, как пометить текст для редактирования, применить аннотации редактирования и удалить выбранные области страниц в PDF‑файлах, используя Aspose.PDF for Java.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Замаскируйте конфиденциальное содержимое PDF в Java с помощью аннотаций безопасности.
Abstract: В этой статье объясняется, как работать с redaction annotations в PDF‑документах с использованием Aspose.PDF for Java. Описывается пометка найденного текста с помощью redaction annotations, постоянное применение редактирований и редактирование выбранных областей на основе обнаруженных прямоугольников размещения изображений.
---
Рабочие процессы аннотаций безопасности в этом разделе сосредоточены на подготовке и применении редактирований к конфиденциальному контенту PDF.

## Отметить текст redaction annotations

Используйте этот пример, когда найденный текст должен быть покрыт redaction annotations до того, как редактирование будет применено навсегда.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
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

## Применить существующие редактирования

Этот пример навсегда применяет аннотации редактирования, которые уже существуют на странице.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Собрать аннотации типа [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Redaction`.
1. Вызовите `redact()` для каждой собранной аннотации сохранить обновлённый файл.

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

## Замазать выбранную область страницы

Используйте этот подход, когда целевой контент определяется по позиции, а не по совпадению текста.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Определите целевой прямоугольник на странице, например из размещения изображения.
1. Создайте [RedactionAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/redactionannotation/) для этой области и сохранить документ.

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

- [Интерактивные аннотации](/pdf/ru/java/interactive-annotations/)
- [Аннотации разметки](/pdf/ru/java/markup-annotations/)
- [Фигурные аннотации](/pdf/ru/java/shape-annotations/)
- [Текстовые аннотации](/pdf/ru/java/text-based-annotations/)
- [Аннотации водяных знаков](/pdf/ru/java/watermark-annotations/)
- [Импорт и экспорт аннотаций](/pdf/ru/java/import-export-annotations/)


