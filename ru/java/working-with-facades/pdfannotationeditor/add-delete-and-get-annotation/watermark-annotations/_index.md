---
title: Аннотации водяных знаков с использованием Java
linktitle: Аннотации водяных знаков
type: docs
weight: 70
url: /java/pdfannotationeditor-class/watermark-annotations/
description: Узнайте, как добавлять, проверять и удалять аннотации водяных знаков в документах PDF с помощью Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Работа с аннотациями водяных знаков в файлах PDF с помощью Java
Abstract: В этой статье объясняется, как создавать, проверять и удалять аннотации с водяными знаками в документах PDF с помощью Java. В нем рассматривается добавление текстовых аннотаций с водяными знаками с настраиваемым состоянием и непрозрачностью текста, чтение существующих областей аннотаций с водяными знаками и удаление аннотаций с водяными знаками.
---
## Добавьте аннотацию водяного знака

1. Откройте входной PDF-файл и определите прямоугольник, в котором будет размещена аннотация водяного знака.
2. Создайте `WatermarkAnnotation`, добавьте его на страницу и настройте состояние и непрозрачность текста водяного знака.
3. Примените текстовые строки водяных знаков и сохраните измененный PDF-файл.

```java
public static void watermarkAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        WatermarkAnnotation watermarkAnnotation = new WatermarkAnnotation(
                document.getPages().get_Item(1), new Rectangle(100, 0, 400, 100, true));

        document.getPages().get_Item(1).getAnnotations().add(watermarkAnnotation);

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
