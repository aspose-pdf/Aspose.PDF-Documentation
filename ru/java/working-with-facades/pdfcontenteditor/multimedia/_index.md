---
title: Мультимедиа
linktitle: Мультимедиа
type: docs
weight: 70
url: /ru/java/pdfcontenteditor-multimedia/
description: Узнайте о текущем охвате мультимедиа, доступном в фасаде Java PdfContentEditor в Aspose.PDF.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Рабочие процессы аннотаций мультимедиа в Java с PdfContentEditor
Abstract: Этот раздел охватывает рабочие процессы, связанные с мультимедиа, которые в настоящее время поддерживаются набором примеров Java PdfContentEditor. Репозиторий содержит пример аннотации фильма, а неподдерживаемые темы звука оставлены в виде явных примечаний о области.
---
Текущий Java `PdfContentEditorExamples` класс напрямую поддерживает `addMovieAnnotation(...)`.

## Добавьте аннотацию фильма

1. Привяжите исходный PDF к `PdfContentEditor` фасад.
2. Вызов `createMovie(...)` с прямоугольником аннотации, путем к файлу фильма и номером страницы.
3. Сохраните обновлённый PDF‑документ.

```java
public static void addMovieAnnotation(Path inputFile, Path movieFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.createMovie(new Rectangle(80, 500, 220, 120), movieFile.toString(), 1);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```

