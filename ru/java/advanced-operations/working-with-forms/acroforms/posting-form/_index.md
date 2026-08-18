---
title: Публикация форм в формате PDF через Java
linktitle: Размещение форм
type: docs
weight: 75
url: /java/posting-form/
description: Добавьте кнопки отправки и действия отправки в PDF AcroForms, используя Aspose.PDF для Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавляйте кнопки отправки и формируйте действия публикации в PDF-файлы с помощью Java.
Abstract: В этой статье показано, как добавить функцию отправки в формы PDF с помощью Aspose.PDF для Java. В нем рассматривается создание кнопки отправки с помощью FormEditor и создание настраиваемого поля кнопки, которое использует SubmitFormAction для большего контроля над URL-адресом отправки и флагами.
---
Aspose.PDF для Java поддерживает создание кнопки отправки как на основе фасада, так и на основе DOM.

## Добавьте кнопку отправки с помощью FormEditor

1. Создайте фасад [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/formeditor/) для исходного PDF-документа.
1. Добавьте настроенный объект кнопки отправки через фасад [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/formeditor/).
1. Сохраните обновленный PDF-документ.

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

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [SubmitFormAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/submitformaction/) и URL-адрес [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/).
1. Создайте [ButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/buttonfield/) на целевой [странице](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) и назначьте действие отправки.
1. Сохраните обновленный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
