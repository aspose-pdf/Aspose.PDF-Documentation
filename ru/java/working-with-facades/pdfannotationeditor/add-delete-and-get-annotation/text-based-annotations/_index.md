---
title: Текстовые аннотации с использованием Java
linktitle: Текстовые аннотации
type: docs
weight: 10
url: /java/pdfannotationeditor-class/text-based-annotations/
description: Узнайте, как добавлять, проверять и удалять текст, произвольный текст и зачеркнутые аннотации в документах PDF с помощью Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Работа с текстовыми аннотациями PDF в Java
Abstract: В этой статье объясняется, как создавать, читать и удалять текстовые аннотации в документах PDF с помощью Java. Он охватывает текстовые аннотации, произвольные текстовые аннотации и зачеркнутые аннотации на основе примеров реализации Java.
---
## Добавьте текстовую аннотацию

1. Откройте входной PDF-файл и выберите страницу, на которой должна быть размещена текстовая аннотация.
2. Создайте `TextAnnotation`, определите его прямоугольник и установите заголовок, тему, флаги и цвет.
3. Добавьте аннотацию на страницу и сохраните обновленный документ.

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

## Добавьте произвольную текстовую аннотацию

1. Загрузите исходный PDF-файл и выберите целевую страницу и прямоугольник для произвольной текстовой заметки.
2. Создайте `FreeTextAnnotation`, инициализируйте его внешний вид по умолчанию и установите заголовок и цвет.
3. Добавьте аннотацию на страницу и сохраните результат.

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
