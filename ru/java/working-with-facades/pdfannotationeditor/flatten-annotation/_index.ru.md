---
title: Flatten Annotation from PDF File to XFDF (facades)
type: docs
weight: 40
url: /java/flatten-annotation/
description: В этом разделе объясняется, как экспортировать аннотации из PDF-файла в XFDF с помощью Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Процесс упрощения означает, что когда аннотация удаляется из документа, ее визуальное представление остается неизменным. Упрощенная аннотация по-прежнему видна, но больше не может быть отредактирована вашими пользователями или вашим приложением. Это может быть использовано, например, для постоянного применения аннотаций к вашему документу или для того, чтобы сделать аннотации видимыми для зрителей, которые в противном случае не могут отображать аннотации. Если не указано иное, при экспорте все аннотации сохраняются как есть.

Когда эта опция выбрана, ваши аннотации будут включены в ваш экспортированный PDF как стандартные аннотации PDF.

Посмотрите, как используется метод [flatteningAnnotations](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#flatteningAnnotations--) в следующем фрагменте кода.

```java
public static void Flattening() {
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(_dataDir + "sample_cats_dogs.pdf");
        FlattenSettings flattenSettings = new FlattenSettings();
        flattenSettings.setApplyRedactions(true); // Применить редактирование
        flattenSettings.setCallEvents(false); // Отключить вызовы событий
        flattenSettings.setHideButtons(true); // Скрыть кнопки
        flattenSettings.setUpdateAppearances(true); // Обновить внешний вид
        annotationEditor.flatteningAnnotations(flattenSettings);
        annotationEditor.save(_dataDir + "FlattenAnnotation.pdf");
    }
```