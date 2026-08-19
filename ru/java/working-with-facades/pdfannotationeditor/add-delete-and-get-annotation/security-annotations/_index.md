---
title: Аннотации безопасности с использованием Java
linktitle: Аннотации безопасности
type: docs
weight: 60
url: /ru/java/pdfannotationeditor-class/security-annotations/
description: Узнайте, как помечать текст для редактирования, применять аннотации редактирования и удалять выбранные области страниц в PDF‑файлах с помощью Java.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Удалять конфиденциальное содержимое PDF в Java с помощью аннотаций безопасности
Abstract: В этой статье объясняется, как работать с аннотациями редактирования в PDF‑документах с использованием Java. Рассматривается пометка найденного текста аннотациями редактирования, постоянное применение редактирования и удаление выбранных областей на основе обнаруженных прямоугольников размещения изображения.
---
## Пометить текст для редактирования

1. Загрузите PDF и выполните поиск по всем страницам текста, который должен быть отредактирован.
2. Создайте `RedactionAnnotation` для каждого найденного фрагмента текста и настройте его внешний вид.
3. Добавьте аннотации редактирования на их страницы и сохраните документ.

```java
public static void markTextRedaction(Path inputFile, Path outputFile, String searchTerm) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(searchTerm);
        TextSearchOptions textSearchOptions = new TextSearchOptions(true);
        textFragmentAbsorber.setTextSearchOptions(textSearchOptions);
        document.getPages().accept(textFragmentAbsorber);

        for (TextFragment textFragment : textFragmentAbsorber.getTextFragments()) {
            Page page = textFragment.getPage();
            Rectangle annotationRectangle = textFragment.getRectangle();
            RedactionAnnotation annotation = new RedactionAnnotation(page, annotationRectangle);
            annotation.setFillColor(Color.getGray());
            annotation.setBorderColor(Color.getRed());
            annotation.setColor(Color.getWhite());
            annotation.setOverlayText("REDACTED");
            annotation.setTextAlignment(HorizontalAlignment.Center);
            annotation.setRepeat(true);
            page.getAnnotations().add(annotation, true);
        }

        document.save(outputFile.toString());
    }
}
```

