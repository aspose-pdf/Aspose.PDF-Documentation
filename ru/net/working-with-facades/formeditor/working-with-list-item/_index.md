---
title: Работа с элементом списка
type: docs
weight: 30
url: ru/net/working-with-list-item/
description: Этот раздел объясняет, как работать с элементом списка с использованием Aspose.PDF Facades и класса FormEditor.
lastmod: "2021-06-05"
draft: false
---

## Добавление элемента списка в существующий PDF файл

Метод [AddListItem](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addlistitem) позволяет добавить элемент в поле [ListBox](https://reference.aspose.com/pdf/net/aspose.pdf.forms/listboxfield). Первый аргумент — это имя поля, а второй — элемент поля. Вы можете передать либо один элемент поля, либо массив строк, содержащий список элементов. Этот метод предоставляется классом [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor). Следующий фрагмент кода показывает, как добавить элементы списка в PDF файл.

```csharp
  public static void AddListItem()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");
            editor.AddField(FieldType.ListBox, "Country", 1, 232.56f, 476.75f, 352.28f, 514.03f);
            editor.AddListItem("Country", "USA");
            editor.AddListItem("Country", "Canada");
            editor.AddListItem("Country", "France");
            editor.AddListItem("Country", "Spain");
            editor.Save(_dataDir + "Sample-Form-01-mod.pdf");
        }
```

## Удалить элемент списка из существующего PDF файла

Метод [DelListItem](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/dellistitem) позволяет удалить определенный элемент из [ListBox](https://reference.aspose.com/pdf/net/aspose.pdf.forms/listboxfield). Первый параметр – это имя поля, а второй параметр – элемент, который вы хотите удалить из списка. Этот метод предоставляется классом [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor). Следующий фрагмент кода показывает, как удалить элемент списка из PDF файла.

```csharp
      public static void DelListItem()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-04.pdf");
            //-----
            editor.DelListItem("Country", "France");
            //-----
            editor.Save(_dataDir + "Sample-Form-04-mod.pdf");
        }
```