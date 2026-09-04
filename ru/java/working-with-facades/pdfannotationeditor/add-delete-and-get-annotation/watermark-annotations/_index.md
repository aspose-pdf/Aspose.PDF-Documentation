---
title: Аннотации водяного знака с использованием Java
linktitle: Аннотации водяного знака
type: docs
weight: 70
url: /ru/java/pdfannotationeditor-class/watermark-annotations/
description: Узнайте, как добавлять, просматривать и удалять аннотации водяного знака в PDF‑документах с помощью Java.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Работайте с аннотациями водяного знака в PDF‑файлах с использованием Java
Abstract: Эта статья объясняет, как создавать, просматривать и удалять аннотации водяного знака в PDF‑документах с использованием Java. В ней рассматривается добавление аннотации текстового водяного знака с пользовательским состоянием текста и непрозрачностью, чтение областей существующих аннотаций водяного знака и удаление аннотаций водяного знака.
---
## Добавьте аннотацию водяного знака

1. Откройте входной PDF и определите прямоугольник, в котором будет размещена аннотация водяного знака.
2. Создайте `WatermarkAnnotation`, добавьте его на страницу и настройте состояние текста водяного знака и непрозрачность.
3. Примените строки текста водяного знака и сохраните изменённый PDF.

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


