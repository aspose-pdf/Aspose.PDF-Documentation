---
title: Извлечь данные AcroForms
linktitle: Извлечь данные AcroForms
type: docs
weight: 30
url: ru/java/extract-form/
description: Этот раздел объясняет, как извлечь формы из вашего PDF-документа с помощью Aspose.PDF для Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Получение значения из отдельного поля PDF-документа

Метод [getValue()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--) позволяет получить значение конкретного поля формы.

Чтобы получить значение, получите поле формы из коллекции Form объекта [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

Этот пример выбирает [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) и извлекает его значение с помощью метода [getValue()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--).

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.Document;
import com.aspose.pdf.Field;
import com.aspose.pdf.TextBoxField;

public class ExamplesExtractFormData {
    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Forms/";

    public static void GetValueFromIndividualFieldPDFDocument() {
        // Открыть документ
        Document pdfDocument = new Document(_dataDir+"GetValueFromField.pdf");

        // Получить поле
        TextBoxField textBoxField = (TextBoxField) pdfDocument.getForm().get("textbox1");

        // Получить имя поля
        System.out.printf("PartialName :-" + textBoxField.getPartialName());

        // Получить значение поля
        System.out.printf("Value :-" + textBoxField.getValue());
    }
```


## Получение значений из всех полей в PDF-документе

Чтобы получить значения из всех полей в PDF-документе, необходимо пройти через все поля формы и затем получить значение, используя метод [getValue()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--). Получите каждое поле из коллекции Form, используя метод [getForm()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--) объекта [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) и получите список полей формы в массив Field, используя getFields(), и пройдитесь по массиву, чтобы получить значение полей.

Следующий фрагмент кода показывает, как получить значения всех полей в PDF-документе.

```java
    public static void GetValuesFromAllFieldsPDFDocument() {
        // Открыть документ
        Document document = new Document(_dataDir + "GetValuesFromAllFields.pdf");

        Field[] fields = document.getForm().getFields();
        for (int i = 0; i < fields.length; i++) {

            System.out.println("Поле формы: " + fields[i].getFullName());
            System.out.println("Поле формы: " + fields[i].getValue());
        }

    }
}
```


## Получение полей формы из определенной области PDF-файла

В некоторых случаях требуется получить данные не из всей формы, а, например, только из верхней левой четверти печатного листа. С Aspose.PDF для Java это не проблема. Вы можете указать область, чтобы отфильтровать поля, находящиеся за пределами заданной области PDF-файла. Чтобы получить поля формы из определенной области PDF-файла:

1. Откройте PDF-файл с помощью объекта Document.
1. Получите форму из коллекции Forms документа.
1. Укажите прямоугольную область и передайте ее методу [getFieldsInRect](https://reference.aspose.com/pdf/java/com.aspose.pdf/Form#getFieldsInRect-com.aspose.pdf.Rectangle-) объекта Form. Возвращается коллекция [Fields](https://reference.aspose.com/pdf/java/com.aspose.pdf/Field).
1. Используйте это для обработки полей.

Следующий фрагмент кода показывает, как получить поля формы в определенной прямоугольной области PDF-файла.

```java
public static void GetValuesFromSpecificRegion() {
    // Открыть PDF-файл
    Document doc = new Document(_dataDir + "GetFieldsFromRegion.pdf");

    // Создать объект прямоугольника для получения полей в этой области
    Rectangle rectangle = new Rectangle(35, 30, 500, 500);

    // Получить форму PDF
    com.aspose.pdf.Form form = doc.getForm();

    // Получить поля в прямоугольной области
    Field[] fields = form.getFieldsInRect(rectangle);

    // Отобразить имена и значения полей
    for (Field field : fields)
    {
        // Отобразить свойства размещения изображения для всех размещений
        System.out.println("Имя поля: " + field.getFullName() + "-" + "Значение поля: " + field.getValue());
    }
}
```