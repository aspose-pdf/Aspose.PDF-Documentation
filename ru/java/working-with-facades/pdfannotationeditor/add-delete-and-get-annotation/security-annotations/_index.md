---
title: Аннотации безопасности с использованием Java
linktitle: Аннотации безопасности
type: docs
weight: 60
url: /java/pdfannotationeditor-class/security-annotations/
description: Узнайте, как помечать текст для редактирования, применять аннотации редактирования и редактировать выбранные области страниц в файлах PDF с помощью Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Редактируйте конфиденциальное содержимое PDF в Java с помощью аннотаций безопасности.
Abstract: В этой статье объясняется, как работать с аннотациями редактирования в документах PDF с помощью Java. Он охватывает маркировку совпадающего текста с помощью примечаний редактирования, постоянное применение исправлений и редактирование выбранных областей на основе обнаруженных прямоугольников размещения изображений.
---
## Отметить текст для редактирования

1. Загрузите PDF-файл и найдите на всех страницах текст, который необходимо отредактировать.
2. Создайте `RedactionAnnotation` для каждого совпавшего фрагмента текста и настройте его внешний вид.
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
