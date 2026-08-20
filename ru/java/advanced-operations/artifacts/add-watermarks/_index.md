---
title: Добавить водяные знаки в PDF на Java
linktitle: Добавление водяного знака
type: docs
weight: 30
url: /ru/java/add-watermarks/
description: Узнайте, как добавлять, извлекать и удалять артефакты водяных знаков в PDF‑файлах с помощью Aspose.PDF for Java.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как добавить водяной знак в PDF с помощью Java
Abstract: В этой статье объясняется, как добавлять, проверять и удалять артефакты водяных знаков в PDF‑документах с использованием Aspose.PDF for Java. Описывается создание текстового водяного знака с настройками выравнивания, вращения, непрозрачности и фона, проверка артефактов водяных знаков на странице и их удаление.
---
Артефакты водяных знаков позволяют размещать постоянные визуальные метки на странице без их смешивания с основным содержимым документа.

## Извлеките артефактов водяных знаков из PDF

Используйте этот пример, когда необходимо проверить существующие артефакты водяных знаков и прочитать их текст или позицию.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Переберите коллекцию артефактов целевой страницы.
1. Отфильтруйте артефакты пагинации водяных знаков и выведите их текст и прямоугольники.

```java
public static void extractWatermarkFromPdf(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Artifact artifact : document.getPages().get_Item(1).getArtifacts()) {
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && artifact.getSubtype() == Artifact.ArtifactSubtype.Watermark) {
                System.out.println(artifact.getText() + " " + artifact.getRectangle());
            }
        }
    }
}
```

## Добавьте артефакт водяного знака

Используйте этот пример, когда страница должна отображать центрированный текстовый водяной знак с пользовательским вращением, непрозрачностью и размещением фона.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [WatermarkArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/watermarkartifact/) и настройте его параметры состояния текста и размещения.
1. Добавьте водяной знак на страницу и сохраните выходной файл.

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

## Удалите артефакты водяных знаков

Используйте этот подход, когда существующие артефакты водяных знаков должны быть удалены со страницы.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Итерируйте коллекцию артефактов страницы в обратном порядке.
1. Удалите артефакты пагинации, чей подтип — водяной знак, затем сохраните документ.

```java
public static void deleteWatermarkArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = document.getPages().get_Item(1).getArtifacts().size(); i >= 1; i--) {
            Artifact artifact = document.getPages().get_Item(1).getArtifacts().get_Item(i);
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && artifact.getSubtype() == Artifact.ArtifactSubtype.Watermark) {
                document.getPages().get_Item(1).getArtifacts().delete(artifact);
            }
        }

        document.save(outputFile.toString());
    }
}
```


