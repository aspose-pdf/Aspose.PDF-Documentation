---
title: Добавление водяных знаков в PDF на Java
linktitle: Добавление водяных знаков
type: docs
weight: 30
url: /ru/java/add-watermarks/
description: Добавить стилизованные текстовые артефакты водяных знаков на страницы PDF на Java.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавление водяных знаков в PDF на Java
Abstract: Добавить стилизованные текстовые артефакты водяных знаков на страницы PDF на Java.
---
Артефакты водяных знаков позволяют размещать постоянные визуальные метки на странице, не смешивая их с основным содержимым документа.

## Добавление артефакта водяного знака

Используйте этот пример, когда страница должна отображать центрированный текстовый водяной знак с пользовательским вращением, непрозрачностью и размещением фона.

1. Откройте исходный PDF в объекте [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [WatermarkArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/watermarkartifact/).
1. Настройте его параметры текста и размещения.
1. Добавьте водяной знак на страницу.
1. Сохраните выходной файл.

```java
public static void addWatermarkArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextState textState = new TextState();
        textState.setFontSize(72);
        textState.setForegroundColor(Color.getBlueViolet());
        textState.setFontStyle(FontStyles.Bold);
        textState.setFont(FontRepository.findFont("Arial"));

        WatermarkArtifact watermark = new WatermarkArtifact();
        watermark.setTextAndState("WATERMARK", textState);
        watermark.setArtifactHorizontalAlignment(HorizontalAlignment.Center);
        watermark.setArtifactVerticalAlignment(VerticalAlignment.Center);
        watermark.setRotation(60);
        watermark.setOpacity(0.2);
        watermark.setBackground(true);

        document.getPages().get_Item(1).getArtifacts().add(watermark);
        document.save(outputFile.toString());
    }
}
```

## См. также

- [Извлечение текста и границ водяных знаков](/pdf/ru/java/extract-watermarks/)
- [Удаление водяных знаков](/pdf/ru/java/remove-watermarks/)
- [Работа с PDF-артефактами](/pdf/ru/java/artifacts/)
