---
title: Операции с изображениями
linktitle: Операции с изображениями
type: docs
weight: 50
url: /ru/java/pdfcontenteditor-image-operations/
description: Узнайте о текущем покрытии операций с изображениями в Java, доступном через фасад PdfContentEditor в Aspose.PDF.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Рабочие процессы редактирования изображений в Java с PdfContentEditor
Abstract: Этот раздел охватывает связанные с изображениями рабочие процессы, которые в настоящее время поддерживаются набором примеров Java PdfContentEditor. Репозиторий включает прямой пример замены изображения, а темы, связанные с удалением изображений, которые не поддерживаются, сохранены в виде явных заметок о рамках.
---
Текущий Java `PdfContentEditorExamples` класс напрямую поддерживает `replaceImage(...)`.

## Замените изображение

1. Привяжите исходный PDF к `PdfContentEditor` фасад.
2. Вызовите `replaceImage(...)` с номером страницы, индексом изображения и путем к заменяемому изображению.
3. Сохраните обновлённый PDF‑документ.

```java
public static void replaceImage(Path inputFile, Path imageFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.replaceImage(1, 1, imageFile.toString());
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```


