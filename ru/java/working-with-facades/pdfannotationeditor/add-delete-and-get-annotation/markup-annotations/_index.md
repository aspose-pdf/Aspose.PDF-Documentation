---
title: Разметка аннотаций с использованием Java
linktitle: Разметка аннотаций
type: docs
weight: 20
url: /java/pdfannotationeditor-class/markup-annotations/
description: Узнайте, как добавлять, проверять и удалять выделения, подчеркивание, волнистую линию и зачеркивание примечаний в документах PDF с помощью Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Работа с аннотациями разметки в файлах PDF с помощью Java
Abstract: В этой статье объясняется, как создавать, проверять и удалять аннотации текстовой разметки в документах PDF с помощью Java. Он охватывает выделение, подчеркивание, волнистую линию и зачеркивание аннотаций на основе примеров Java из репозитория.
---
## Добавление выделенных, подчеркнутых, волнистых или зачеркнутых аннотаций.

1. Откройте входной PDF-файл и выберите область страницы, где должна появиться аннотация разметки.
2. Создайте необходимый тип аннотации и настройте его метаданные или визуальные свойства.
3. Добавьте аннотацию в коллекцию страниц и сохраните документ.

```java
public static void addTextHighlightAnnotation(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HighlightAnnotation highlightAnnotation = new HighlightAnnotation(
                document.getPages().get_Item(1), new Rectangle(300, 750, 320, 770, true));
        document.getPages().get_Item(1).getAnnotations().add(highlightAnnotation);
        document.save(outputFile.toString());
    }
}
```

```java
public static void addTextUnderlineAnnotation(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        UnderlineAnnotation underlineAnnotation = new UnderlineAnnotation(
                document.getPages().get_Item(1), new Rectangle(299.988, 713.664, 308.708, 720.769, true));
        underlineAnnotation.setTitle("Aspose User");
        underlineAnnotation.setSubject("Inserted Underline 1");
        underlineAnnotation.setFlags(AnnotationFlags.Print);
        underlineAnnotation.setColor(Color.getBlue());
        document.getPages().get_Item(1).getAnnotations().add(underlineAnnotation);
        document.save(outputFile.toString());
    }
}
```
