---
title: Украшение Поля Формы в PDF
type: docs
weight: 20
url: ru/java/decorate-form-field/
description: В этом разделе объясняется, как украсить поле формы в PDF, используя класс FormEditor.
lastmod: "2021-06-05"
draft: false
---

## Украшение Конкретного Поля Формы в Существующем PDF Файле

Метод [decorateField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#decorateField--) присутствующий в классе [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) позволяет украсить конкретное поле формы в PDF файле.
 Если вы хотите украсить конкретное поле, то вам нужно передать имя поля этому методу. Однако, перед вызовом этого метода, вам нужно создать объекты классов [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) и [FormFieldFacade](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormFieldFacade). После этого вы можете установить любые атрибуты, предоставленные объектом [FormFieldFacade](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormFieldFacade). Как только вы установили атрибуты, вы можете вызвать метод [decorateField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#decorateField--) и, наконец, сохранить обновленный PDF, используя метод Save класса [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor).
Следующий фрагмент кода показывает, как украсить конкретное поле формы.

```java
public static void DecorateField() {
        FormEditor editor = new FormEditor();
        editor.bindPdf(_dataDir + "Sample-Form-01.pdf");

        FormFieldFacade cityDecoration = new FormFieldFacade();
        cityDecoration.setFont(FontStyle.Courier);
        cityDecoration.setFontSize(12);
        cityDecoration.setBorderColor(Color.BLACK);
        cityDecoration.setBorderWidth(2);

        editor.setFacade(cityDecoration);
        editor.decorateField("City");
        editor.save(_dataDir + "Sample-Form-02.pdf");
    }
```

## Декорировать Все Поля Определенного Типа в Существующем PDF Файле

Метод [decorateField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#decorateField--) позволяет декорировать все поля формы определенного типа в PDF файле одновременно.
 Если вы хотите украсить все поля определенного типа, то вам нужно передать тип поля этому методу. Однако, прежде чем вызвать этот метод, вам необходимо создать объекты классов [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) и [FormFieldFacade](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormFieldFacade). После этого вы можете установить любые атрибуты, предоставленные объектом [FormFieldFacade](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormFieldFacade). Как только вы установили атрибуты, вы можете вызвать метод [decorateField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#decorateField--) и, наконец, сохранить обновленный PDF, используя метод Save класса [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor). Следующий фрагмент кода показывает, как украсить все поля определенного типа.

```java
   public static void DecorateFields() {
        FormEditor editor = new FormEditor();
        editor.bindPdf(_dataDir + "Sample-Form-01.pdf");

        FormFieldFacade textFieldDecoration = new FormFieldFacade();
        // Устанавливаем выравнивание по центру
        textFieldDecoration.setAlignment(FormFieldFacade.ALIGN_CENTER);

        editor.setFacade(textFieldDecoration);
        editor.decorateField(FieldType.Text);
        editor.save(_dataDir + "Sample-Form-01-align-text.pdf");
    }
```