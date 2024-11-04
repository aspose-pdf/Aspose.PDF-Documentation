---
title: Украшение Поля Формы в PDF
type: docs
weight: 20
url: /net/decorate-form-field/
description: Этот раздел объясняет, как украсить поле формы в PDF, используя класс FormEditor.
lastmod: "2021-06-05"
draft: false
---

## Украшение Конкретного Поля Формы в Существующем PDF Файле

Метод [DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/decoratefield), представленный в классе [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor), позволяет украсить конкретное поле формы в PDF файле. If you want to decorate a particular field then you need to pass the field name to this method.  
Если вы хотите украсить определенное поле, вам нужно передать имя поля этому методу. Однако перед вызовом этого метода вам нужно создать объекты классов [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) и [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade). Вам также необходимо назначить объект [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) свойству [Facade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/properties/index) объекта [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). После этого вы можете установить любые атрибуты, предоставляемые объектом [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade). После установки атрибутов можно вызвать метод [DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/decoratefield) и, наконец, сохранить обновленный PDF, используя метод [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) класса [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor). 

Следующий фрагмент кода показывает, как украсить конкретное поле формы.

```csharp
public static void DecorateField()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");

            var cityDecoration = new FormFieldFacade
            {
                Font = FontStyle.Courier,
                FontSize = 12,
                BorderColor = System.Drawing.Color.Black,
                BorderWidth = 2
            };

            editor.Facade = cityDecoration;
            editor.DecorateField("City");
            editor.Save(_dataDir + "Sample-Form-02.pdf");
        }
```
## Украшение всех полей определенного типа в существующем PDF-файле

Метод [DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades.formeditor/decoratefield/methods/1) позволяет украсить все поля формы определенного типа в PDF-файле одновременно. Если вы хотите декорировать все поля определенного типа, вам нужно передать тип поля этому методу. Однако, перед вызовом этого метода, необходимо создать объекты классов [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) и [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade). Вам также необходимо присвоить объект [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) свойству [Facade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/properties/index) объекта [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). После этого вы можете установить любые атрибуты, предоставляемые объектом [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade). После установки атрибутов вы можете вызвать метод [DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades.formeditor/decoratefield/methods/1) и, наконец, сохранить обновленный PDF с помощью метода [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) класса [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor). Следующий фрагмент кода показывает, как украсить все поля определенного типа.

```csharp
        public static void DecorateField2()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");

            var textFieldDecoration = new FormFieldFacade
            {
                Alignment = FormFieldFacade.AlignCenter,
            };

            editor.Facade = textFieldDecoration;
            editor.DecorateField(FieldType.Text);
            editor.Save(_dataDir + "Sample-Form-01-align-text.pdf");
        }
```