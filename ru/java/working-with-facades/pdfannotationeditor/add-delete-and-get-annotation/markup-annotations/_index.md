---
title: Разметка аннотаций с использованием Java
linktitle: Разметка аннотаций
type: docs
weight: 20
url: /ru/java/pdfannotationeditor-class/markup-annotations/
description: Узнайте, как добавлять, просматривать и удалять аннотации выделения, подчеркивания, волнистого подчеркивания и зачеркивания в PDF‑документах с помощью Java.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Работайте с разметкой аннотаций в PDF‑файлах с помощью Java
Abstract: В этой статье объясняется, как создавать, просматривать и удалять текстовые аннотации разметки в PDF‑документах с помощью Java. Рассматриваются аннотации выделения, подчеркивания, волнистого подчеркивания и зачеркивания на основе примеров Java из репозитория.
---
## Добавьте аннотации выделения, подчеркивания, волнистого подчеркивания или зачеркивания

1. Откройте входной PDF и выберите область страницы, где должна появиться разметочная аннотация.
2. Создайте требуемый тип аннотации и настройте её метаданные или визуальные свойства.
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


