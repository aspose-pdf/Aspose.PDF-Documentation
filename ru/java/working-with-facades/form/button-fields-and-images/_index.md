---
title: Поля кнопок и изображения
linktitle: Поля кнопок и изображения
type: docs
weight: 40
url: /java/button-fields-and-images/
description: Узнайте, как добавить внешний вид изображения в поле кнопки в форме PDF с помощью фасада формы в Aspose.PDF для Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Добавление внешнего вида изображения в поле кнопки PDF в Java
Abstract: В этой статье показано, как использовать фасад формы в Aspose.PDF для Java для привязки формы PDF, загрузки изображения в виде потока, заполнения поля кнопки изображения и сохранения обновленного документа.
---
Пример Java в `FormExamples.addImageAppearanceToButtonField(...)` показывает, как обновить внешний вид поля кнопки с помощью потока изображений.

Рабочий процесс прост:

- свяжите входной PDF с помощью `form.bindPdf(...)`
- откройте файл изображения с помощью `Files.newInputStream(...)`
- позвоните `form.fillImageField(...)` для поля кнопки
- сохраните обновленный PDF-файл

```java
public static void addImageAppearanceToButtonField(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream imageStream = Files.newInputStream(imageFile)) {
        form.bindPdf(inputFile.toString());
        form.fillImageField("Image1_af_image", imageStream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
