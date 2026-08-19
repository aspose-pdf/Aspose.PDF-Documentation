---
title: Поля кнопок и изображения
linktitle: Поля кнопок и изображения
type: docs
weight: 40
url: /ru/java/button-fields-and-images/
description: Узнайте, как добавить изображение в качестве внешнего вида к полю кнопки в PDF-форме с помощью фасада Form в Aspose.PDF for Java.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Добавьте изображение в качестве внешнего вида к полю кнопки PDF в Java
Abstract: В этой статье показано, как использовать фасад Form в Aspose.PDF for Java для привязки PDF-формы, загрузки изображения в виде потока, заполнения поля кнопки изображением и сохранения обновлённого документа.
---
Пример на Java в `FormExamples.addImageAppearanceToButtonField(...)` показывает, как обновить внешний вид поля кнопки с помощью потока изображения.

Процесс работы прост:

- привязать входной PDF к `form.bindPdf(...)`
- открыть файл изображения с помощью `Files.newInputStream(...)`
- звонок `form.fillImageField(...)` для поля кнопки
- сохраните обновлённый PDF

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

