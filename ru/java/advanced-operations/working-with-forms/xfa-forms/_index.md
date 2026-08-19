---
title: Работа с XFA-формами
linktitle: XFA-формы
type: docs
weight: 20
url: /ru/java/xfa-forms/
description: Узнайте, как преобразовать XFA-формы в стандартные AcroForm в PDF‑документах с помощью Aspose.PDF for Java.
lastmod: "2026-08-19"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Преобразуйте PDF-формы на основе XFA в стандартные AcroForm с Java
Abstract: В этой статье объясняется, как работать с формами на основе XFA с помощью Aspose.PDF for Java. Описывается преобразование динамической XFA-формы в стандартный AcroForm и обработка XFA-документов, которым перед преобразованием требуется опция ignore-needs-rendering.
---
XFA-формы могут быть преобразованы в стандартные AcroForm, чтобы их можно было обрабатывать с помощью обычных API форм PDF.

## Преобразуйте динамическую форму XFA в AcroForm

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Получите доступ к документу [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf/form/) и установите необходимые [FormType](https://reference.aspose.com/pdf/java/com.aspose.pdf/formtype/) свойства.
1. Сохраните обновлённый PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void convertDynamicXfaToAcroform(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getForm().setType(FormType.Standard);
        document.save(outputFile.toString());
    }
}
```

## Преобразуйте форму XFA с `ignoreNeedsRendering`

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Получите доступ к документу [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf/form/) и установите необходимые `ignoreNeedsRendering` и [FormType](https://reference.aspose.com/pdf/java/com.aspose.pdf/formtype/) свойства.
1. Сохраните обновлённый PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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

