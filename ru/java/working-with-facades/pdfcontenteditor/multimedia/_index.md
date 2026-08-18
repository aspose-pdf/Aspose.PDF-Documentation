---
title: Мультимедиа
linktitle: Мультимедиа
type: docs
weight: 70
url: /java/pdfcontenteditor-multimedia/
description: Узнайте о текущем мультимедийном покрытии, доступном в фасаде Java PdfContentEditor в Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Рабочие процессы мультимедийных аннотаций в Java с помощью PdfContentEditor
Abstract: В этом разделе рассматриваются рабочие процессы, связанные с мультимедиа, которые в настоящее время поддерживаются набором примеров Java PdfContentEditor. Репозиторий включает в себя пример прямой аннотации к фильму, а неподдерживаемые звуковые темы сохраняются как явные примечания к объему.
---
Текущий класс Java `PdfContentEditorExamples` напрямую поддерживает `addMovieAnnotation(...)`.

## Добавьте аннотацию к фильму

1. Привяжите исходный PDF-файл к фасаду `PdfContentEditor`.
2. Вызовите `createMovie(...)`, указав прямоугольник аннотации, путь к файлу фильма и номер страницы.
3. Сохраните обновленный PDF-документ.

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
