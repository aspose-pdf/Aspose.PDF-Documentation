---
title: Копирование внутреннего и внешнего поля
type: docs
weight: 40
url: /net/copy-inner-and-outer-field/
description: Этот раздел объясняет, как копировать внутреннее и внешнее поле с использованием Aspose.PDF Facades и класса FormEditor.
lastmod: "2021-06-05"
draft: false
---

Метод [CopyInnerField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/copyinnerfield/index) позволяет копировать поле в том же файле, на тех же координатах, на указанной странице. Этот метод требует имя поля, которое вы хотите скопировать, новое имя поля и номер страницы, на которой необходимо скопировать поле. Класс [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor) предоставляет этот метод. Следующий фрагмент кода показывает, как скопировать поле в том же месте в том же файле.

```csharp
  public static void CopyInnerField()
        {
            var editor = new FormEditor();
            var document = new Aspose.Pdf.Document(_dataDir + "Sample-Form-01.pdf");
            document.Pages.Add();
            editor.BindPdf(document);
            editor.CopyInnerField("Last Name", "Last Name 2", 2);
            editor.Save(_dataDir + "Sample-Form-01-mod.pdf");
        }
```

## Копирование внешнего поля в существующий PDF файл

Метод [CopyOuterField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/copyouterfield/index) позволяет скопировать поле формы из внешнего PDF файла и затем добавить его в входной PDF файл на то же место и указанный номер страницы. Этот метод требует PDF файл, из которого необходимо скопировать поле, имя поля и номер страницы, на которую нужно скопировать поле. Этот метод предоставляется классом [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). Следующий фрагмент кода показывает, как скопировать поле из внешнего PDF файла.

```csharp
   public static void CopyOuterField()
        {
            var editor = new FormEditor();
            var document = new Aspose.Pdf.Document();
            document.Pages.Add();
            editor.BindPdf(document);
            editor.CopyOuterField(_dataDir + "Sample-Form-01.pdf", "First Name", 1);
            editor.CopyOuterField(_dataDir + "Sample-Form-01.pdf", "Last Name", 1);
            editor.Save(_dataDir + "Sample-Form-02-mod.pdf");
        }
```