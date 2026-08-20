---
title: Размещение форм в PDF с помощью Java
linktitle: Размещение форм
type: docs
weight: 75
url: /ru/java/posting-form/
description: Добавьте кнопки отправки и действия отправки в PDF AcroForms с использованием Aspose.PDF for Java.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавьте кнопки отправки и действия публикации формы в PDF‑файлы с помощью Java
Abstract: В этой статье показано, как добавить возможность отправки в PDF‑формы с использованием Aspose.PDF for Java. Рассматривается создание кнопки отправки с помощью FormEditor и создание пользовательского поля кнопки, которое использует SubmitFormAction для более точного управления URL‑адресом отправки и флагами.
---
Aspose.PDF for Java поддерживает как создание кнопок отправки на основе фасада, так и на основе DOM.

## Добавьте кнопку отправки с FormEditor

1. Создайте [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/formeditor/) фасад для исходного PDF‑документа.
1. Добавьте сконфигурированный объект кнопки отправки через [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/formeditor/) фасад.
1. Сохраните обновлённый PDF‑документ.

```java
public static void addSubmitButton(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    editor.bindPdf(inputFile.toString());
    try {
        editor.addSubmitBtn("submitbutton", 1, "Submit", "http://localhost/testing/show",
                100, 450, 150, 475);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```

## Добавьте действие отправки вручную

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [SubmitFormAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/submitformaction/) и URL [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/).
1. Создайте [ButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/buttonfield/) на целевом [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) и назначьте действие отправки.
1. Сохраните обновлённый PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addSubmitAction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        SubmitFormAction submitAction = new SubmitFormAction();
        submitAction.setUrl(new FileSpecification("http://localhost:3000/submit"));
        submitAction.setFlags(SubmitFormAction.EXPORT_FORMAT | SubmitFormAction.SUBMIT_COORDINATES);

        ButtonField submitButton = new ButtonField(document.getPages().get_Item(1), new Rectangle(10, 10, 100, 40));
        submitButton.setPartialName("SubmitButton");
        submitButton.setValue("Submit");
        submitButton.getPdfActions().add(submitAction);

        document.getForm().add(submitButton, 1);
        document.save(outputFile.toString());
    }
}
```


