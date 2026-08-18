---
title: Работа с формами XFA
linktitle: XFA Forms
type: docs
weight: 20
url: /java/xfa-forms/
description: Узнайте, как конвертировать формы XFA в стандартные AcroForms в документах PDF с помощью Aspose.PDF для Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Преобразование PDF-форм на основе XFA в стандартные AcroForms с помощью Java
Abstract: В этой статье объясняется, как работать с формами на основе XFA с помощью Aspose.PDF для Java. В нем рассматривается преобразование динамической формы XFA в стандартную форму AcroForm и обработка документов XFA, для которых перед преобразованием требуется опция игнорирования необходимости рендеринга.
---
Формы XFA можно преобразовать в стандартные AcroForms, чтобы их можно было обрабатывать с помощью обычных API-интерфейсов форм PDF.

## Преобразование динамической формы XFA в AcroForm

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Откройте документ [Форма](https://reference.aspose.com/pdf/java/com.aspose.pdf/form/) и установите необходимые свойства [FormType](https://reference.aspose.com/pdf/java/com.aspose.pdf/formtype/).
1. Сохраните обновленный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void convertDynamicXfaToAcroform(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getForm().setType(FormType.Standard);
        document.save(outputFile.toString());
    }
}
```

## Преобразуйте форму XFA с помощью `ignoreNeedsRendering`

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Откройте документ [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf/form/) и установите необходимые свойства `ignoreNeedsRendering` и [FormType](https://reference.aspose.com/pdf/java/com.aspose.pdf/formtype/).
1. Сохраните обновленный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void convertXfaFormWithIgnoreNeedsRendering(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        if (!document.getForm().getNeedsRendering() && document.getForm().hasXfa()) {
            document.getForm().setIgnoreNeedsRendering(true);
        }
        document.getForm().setType(FormType.Standard);
        document.save(outputFile.toString());
    }
}
```
