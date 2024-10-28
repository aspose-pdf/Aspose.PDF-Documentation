---
title: Изменение AcroForms
linktitle: Изменение AcroForms
type: docs
weight: 40
url: /java/modifing-form/
description: Этот раздел объясняет, как изменять формы в вашем PDF документе с помощью Aspose.PDF для Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Установить Пользовательский Шрифт Поля Формы

Поля формы в файлах Adobe PDF могут быть настроены для использования определенных шрифтов по умолчанию. Aspose.PDF позволяет разработчикам применять любой шрифт в качестве шрифта по умолчанию для поля, будь то один из 14 основных шрифтов или пользовательский шрифт.
Чтобы установить и обновить шрифт по умолчанию, используемый для полей формы, Aspose.PDF имеет класс DefaultAppearance (Font font, double size, Color color). Этот класс может быть доступен с использованием com.aspose.pdf.DefaultAppearance. Для использования этого объекта используйте метод setDefaultAppearance(..) класса Field.

Следующий фрагмент кода показывает, как установить шрифт по умолчанию для поля формы PDF.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.DefaultAppearance;
import com.aspose.pdf.Document;
import com.aspose.pdf.Field;
import com.aspose.pdf.Font;
import com.aspose.pdf.FontRepository;
import com.aspose.pdf.Rectangle;
import com.aspose.pdf.TextBoxField;

public class ExamplesModifying {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Forms/";

    public static void SetFormFieldFontOtherThan14CorePDFFonts() {
        // Открыть документ
        Document pdfDocument = new Document(_dataDir + "FormFieldFont14.pdf");
        // Получить конкретное поле формы из документа
        Field field = (Field) pdfDocument.getForm().get("textbox1");

        // Создать объект шрифта
        Font font = FontRepository.findFont("ComicSansMS");

        // Установить информацию о шрифте для поля формы
        field.setDefaultAppearance (new DefaultAppearance(font, 10, java.awt.Color.BLACK));
        
        // Сохранить обновленный документ
        pdfDocument.save(_dataDir + "FormFieldFont14_out.pdf");
    }
```


## Get/Set FieldLimit

Метод SetFieldLimit класса FormEditor позволяет установить ограничение на количество символов, которое может быть введено в поле.

```java
    public static void GettingMaximumFieldLimit()
    {
        // Получение максимального ограничения на количество символов с использованием DOM
        Document doc = new Document(_dataDir + "FieldLimit.pdf");
        TextBoxField field = (TextBoxField)doc.getForm().get("textbox1");
        System.out.println("Limit: " +field.getMaxLen());
    }
```

Вы также можете получить то же значение, используя пространство имен Aspose.PDF.Facades с помощью следующего фрагмента кода.

```java
    public static void GettingMaximumFieldLimitFacades()
    {
        // Получение максимального ограничения на количество символов с использованием Facades
        com.aspose.pdf.facades.Form form = new com.aspose.pdf.facades.Form();
        form.bindPdf(_dataDir + "FieldLimit.pdf");
        System.out.println("Limit: " + form.getFieldLimit("textbox1"));
    }
```

Аналогично, Aspose.PDF имеет метод, который получает ограничение на количество символов, используя подход DOM.
 Следующий фрагмент кода показывает шаги.

```java
    public static void SettingMaximumFieldLimit()
    {
        // Получение максимального ограничения поля с помощью DOM
        Document doc = new Document(_dataDir + "FieldLimit.pdf");
        TextBoxField field = (TextBoxField)doc.getForm().get("textbox1");
        field.setMaxLen(10);
        System.out.println("Limit: " +field.getMaxLen());       
    }
```

## Удаление конкретного поля формы из PDF-документа

Все поля формы содержатся в коллекции Form объекта [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Эта коллекция предоставляет различные методы управления полями формы, включая метод удаления. Если вы хотите удалить конкретное поле, передайте имя поля в качестве параметра методу удаления, а затем сохраните обновленный PDF-документ.

Следующий фрагмент кода показывает, как удалить поле с указанным именем из PDF-документа.

```java
    public static void DeleteParticularFormField()
    {    
        // Открыть документ
        Document pdfDocument = new Document("input.pdf");

        // Удалить поле по имени
        pdfDocument.getForm().delete("textbox1");

        // Сохранить измененный PDF
        pdfDocument.save("output.pdf");
    }
```

## Изменение поля формы в PDF-документе

Коллекция Form объекта [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) позволяет управлять полями формы в PDF-документе.

Чтобы изменить поле формы, получите это поле из коллекции Form и установите его свойства. Затем сохраните обновленный PDF-документ.

Следующий фрагмент кода показывает, как изменить существующее поле формы в PDF-документе.

```java
    public static void ModifyFormField()
    {
        Document pdfDocument = new Document("input.pdf");
        // Получить поле
        TextBoxField textBoxField = (TextBoxField) pdfDocument.getForm().get("textbox1");

        // Изменить значение поля
        textBoxField.setValue("Обновленное значение");

        // Установить поле как только для чтения
        textBoxField.setReadOnly(true);

        // Сохранить обновленный документ
        pdfDocument.save("output.pdf");
    }
```

### Переместить поле формы на новое место в PDF-файле

Если вы хотите переместить поле формы на новое место на странице PDF, сначала получите объект поля, а затем задайте новое значение для его метода setRect.
 A [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) объект с новыми координатами назначается методу setRect(..). Затем сохраните обновленный PDF, используя метод save объекта [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

Следующий фрагмент кода показывает, как переместить поле формы в новое место.

```java
    public static void ModifyMoveFormFieldNewLocation()
    {    
        // Открыть документ
        Document pdfDocument = new Document(_dataDir+"input.pdf");
        // Получить поле
        TextBoxField textBoxField = (TextBoxField) pdfDocument.getForm().get("textbox1");

        // Изменить местоположение поля
        textBoxField.setRect(new Rectangle(300, 400, 600, 500));

        // Сохранить измененный документ
        pdfDocument.save("output.pdf");
    }
}
```