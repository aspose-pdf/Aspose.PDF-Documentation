---
title: Операции с изображениями
linktitle: Операции с изображениями
type: docs
weight: 50
url: /java/pdfcontenteditor-image-operations/
description: Изучите текущее покрытие операций с изображениями Java, доступное в фасаде PdfContentEditor в Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Рабочие процессы редактирования изображений в Java с помощью PdfContentEditor
Abstract: В этом разделе рассматриваются рабочие процессы, связанные с изображениями, которые в настоящее время поддерживаются набором примеров Java PdfContentEditor. Репозиторий включает прямой пример замены изображения, а неподдерживаемые темы удаления изображений сохраняются в виде явных примечаний по объему.
---
Текущий класс Java `PdfContentEditorExamples` напрямую поддерживает `replaceImage(...)`.

## Заменить изображение

1. Привяжите исходный PDF-файл к фасаду `PdfContentEditor`.
2. Вызовите `replaceImage(...)` и сообщите номер страницы, индекс изображения и путь к заменяющему изображению.
3. Сохраните обновленный PDF-документ.

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
