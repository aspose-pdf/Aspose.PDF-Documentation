---
title: Добавление полей формы в PDF
type: docs
weight: 10
url: ru/net/add-form-fields/
description: В этой теме объясняется, как работать с полями формы с помощью Aspose.PDF Facades, используя класс FormEditor.
lastmod: "2021-06-05"
draft: false
---

## Добавление поля формы в существующий PDF файл

Чтобы добавить поле формы в существующий PDF файл, вам нужно использовать метод [AddField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addfield/index) класса [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor). Этот метод требует от вас указать тип поля, которое вы хотите добавить, вместе с именем и местоположением поля. Вам нужно создать объект класса [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor), использовать метод [AddField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addfield/index) для добавления нового поля в PDF. Также вы можете указать ограничение на количество символов в вашем поле с помощью [SetFieldLimit](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/setfieldlimit), и в конце использовать метод [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) для сохранения обновленного PDF файла. Следующий фрагмент кода показывает, как добавить поле формы в существующий PDF файл.

```csharp
   public static void AddField()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir+"Sample-Form-01.pdf");
            editor.AddField(FieldType.Text, "Country", 1, 232.56f, 496.75f, 352.28f, 514.03f);
            editor.SetFieldLimit("Country", 20);
            editor.Save(_dataDir + "Sample-Form-01-mod.pdf");
        }
```
## Добавить URL кнопки отправки в существующий PDF файл

Метод [AddSubmitBtn](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addsubmitbtn) позволяет установить URL кнопки отправки в PDF файле. Это URL, куда данные отправляются при нажатии кнопки отправки. В нашем примере кода мы указываем URL, имя нашего поля, номер страницы, на которую мы хотим добавить, и координаты размещения кнопки. Метод [AddSubmitBtn](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addsubmitbtn) требует имя поля кнопки отправки и URL. Этот метод предоставляется классом [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). Следующий фрагмент кода показывает, как установить URL кнопки отправки.

```csharp
public static void AddSubmitBtn()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");
            editor.AddSubmitBtn("Submit", 1, "Submit", "http://localhost:3000", 232.56f, 466.75f, 352.28f, 484.03f);
            editor.Save(_dataDir + "Sample-Form-01-mod.pdf");
        }
```

## Добавление JavaScript для кнопки

Метод [AddFieldScript](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addfieldscript) позволяет добавить JavaScript к кнопке в PDF файле. Этот метод требует имени кнопки и JavaScript. Этот метод предоставляется классом [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). Следующий фрагмент кода показывает, как установить JavaScript для кнопки.

```csharp
     public static void AddFieldScript()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");
            editor.AddFieldScript("Last Name", "app.alert(\"Only one last name\",3);");
            editor.Save(_dataDir + "Sample-Form-01-mod.pdf");
        }
```