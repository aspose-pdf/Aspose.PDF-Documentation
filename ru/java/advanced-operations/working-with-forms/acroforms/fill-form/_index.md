---
title: Заполнение AcroForms
linktitle: Заполнение AcroForms
type: docs
weight: 20
url: ru/java/fill-form/
description: В этом разделе объясняется, как заполнить поле формы в PDF-документе с помощью Aspose.PDF for Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF-документы великолепны и действительно являются предпочтительным типом файлов для создания форм.

Aspose.PDF for Java позволяет заполнять поле формы, получая поле из коллекции форм объекта Document.

Давайте посмотрим на следующий пример, как решить эту задачу:

```java
public class ExamplesFillForm {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Forms/";

    public static void FillFormFieldPDFDocument() {
        // Открыть документ
        Document pdfDocument = new Document(_dataDir + "TextField.pdf");
        Page page = pdfDocument.getPages().get_Item(1);
        // Создать поле
        TextBoxField textBoxField = new TextBoxField(page, new Rectangle(100, 200, 300, 300));
        textBoxField.setPartialName("textbox1");
        textBoxField.setValue("Text Box");

        // TextBoxField.Border = new Border(
        Border border = new Border(textBoxField);
        border.setWidth(5);
        border.setDash(new Dash(1, 1));
        textBoxField.setBorder(border);

        textBoxField.setColor(Color.getGreen());

        // Добавить поле в документ
        pdfDocument.getForm().add(textBoxField, 1);

        // Сохранить измененный PDF
        pdfDocument.save(_dataDir + "TextBox_out.pdf");

    }

    
}
```