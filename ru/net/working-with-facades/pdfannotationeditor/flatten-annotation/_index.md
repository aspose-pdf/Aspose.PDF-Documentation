---
title: Flatten Annotation from PDF to XFDF
type: docs
weight: 40
url: ru/net/flatten-annotation/
description: В этом разделе объясняется, как экспортировать аннотации из PDF файла в XFDF с помощью Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Процесс уплощения означает, что когда аннотация удаляется из документа, ее визуальное представление остается неизменным. Уплощенная аннотация все еще видна, но больше не редактируема вашими пользователями или вашим приложением. Это может быть использовано, например, для постоянного применения аннотаций к вашему документу или для того, чтобы сделать аннотации видимыми для зрителей, которые иначе не могут отображать аннотации. Если не указано иное, экспорт сохранит все аннотации как есть.

Когда эта опция выбрана, ваши аннотации будут включены в экспортированный PDF как аннотации стандарта PDF.

Посмотрите, как используется метод [flatteningAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/flatteningannotations) в следующем примере кода.

```csharp
public static void Flattening()
        {
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(_dataDir + "sample_cats_dogs.pdf");
            FlattenSettings flattenSettings = new FlattenSettings
            {
                ApplyRedactions = true,
                CallEvents = false,
                HideButtons = true,
                UpdateAppearances = true
            };
            annotationEditor.FlatteningAnnotations(flattenSettings);
            annotationEditor.Save(_dataDir + "FlattenAnnotation.pdf");
        }
```