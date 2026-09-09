---
title: Текстовые аннотации с использованием Java
linktitle: Текстовые аннотации
type: docs
weight: 10
url: /ru/java/pdfannotationeditor-class/text-based-annotations/
description: Узнайте, как добавлять, проверять и удалять текстовые, свободные текстовые и помеченные аннотации в PDF‑документах с помощью Java.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Работа с текстовыми PDF‑аннотациями в Java
Abstract: В этой статье объясняется, как создавать, читать и удалять текстовые аннотации в PDF‑документах с помощью Java. Описываются текстовые аннотации, свободные текстовые аннотации и аннотации со штриховкой на основе примеров реализации на Java.
---
## Добавьте текстовую аннотацию

1. Откройте входной PDF и выберите страницу, на которой должна быть размещена текстовая аннотация.
2. Создайте `TextAnnotation`, определите его прямоугольник и задайте его заголовок, тему, флаги и цвет.
3. Добавьте аннотацию на страницу и сохраните обновлённый документ.

```java
public static void textAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextAnnotation textAnnotation = new TextAnnotation(
                document.getPages().get_Item(1), new Rectangle(299.988, 613.664, 428.708, 680.769, true));
        textAnnotation.setTitle("Aspose User");
        textAnnotation.setSubject("Inserted text 1");
        textAnnotation.setFlags(AnnotationFlags.Print);
        textAnnotation.setColor(Color.getBlue());

        document.getPages().get_Item(1).getAnnotations().add(textAnnotation, false);
        document.save(outputFile.toString());
    }
}
```

## Добавьте свободную текстовую аннотацию

1. Загрузите исходный PDF и выбрать целевую страницу и прямоугольник для свободной текстовой заметки.
2. Создайте `FreeTextAnnotation`, инициализировать его стандартный внешний вид, и установить заголовок и цвет.
3. Добавьте аннотацию на страницу и сохранить результат.

```java
public static void freeTextAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        FreeTextAnnotation freeTextAnnotation = new FreeTextAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(299, 713, 308, 720, true),
                new DefaultAppearance());
        freeTextAnnotation.setTitle("Aspose User");
        freeTextAnnotation.setColor(Color.getLightGreen());

        document.getPages().get_Item(1).getAnnotations().add(freeTextAnnotation);
        document.save(outputFile.toString());
    }
}
```


