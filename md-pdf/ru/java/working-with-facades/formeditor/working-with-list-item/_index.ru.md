---
title: Работа с элементом списка
type: docs
weight: 30
url: /java/working-with-list-item/
description: Этот раздел объясняет, как работать с элементом списка с использованием com.aspose.pdf.facades и класса FormEditor.
lastmod: "2021-06-05"
draft: false
---

## Добавление элемента списка в существующий PDF файл

Метод [addListItem](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#addListItem-java.lang.String-java.lang.String-) позволяет добавить элемент в поле ListBox. Первый аргумент - это имя поля, а второй аргумент - элемент поля. Вы можете передать либо один элемент поля, либо массив строк, содержащий список элементов. Этот метод предоставляется классом [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor). Следующий фрагмент кода показывает, как добавить элементы списка в PDF файл.

```java
public static void AddListItem() {
        FormEditor editor = new FormEditor();
        editor.bindPdf(_dataDir + "Sample-Form-01.pdf");
        editor.addField(FieldType.ListBox, "Country", 1, 232.56f, 476.75f, 352.28f, 514.03f);
        editor.addListItem("Country", "США");
        editor.addListItem("Country", "Канада");
        editor.addListItem("Country", "Франция");
        editor.addListItem("Country", "Испания");
        editor.save(_dataDir + "Sample-Form-01-mod.pdf");
    }
```


## Удаление элемента списка из существующего PDF-файла

Метод [delListItem](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#delListItem-java.lang.String-java.lang.String-) позволяет удалить определённый элемент из ListBox. Первый параметр - это имя поля, а второй параметр - элемент, который вы хотите удалить из списка. Этот метод предоставляется классом [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor). Следующий фрагмент кода показывает, как удалить элемент списка из PDF-файла.

```java
    public static void DelListItem() {
        FormEditor editor = new FormEditor();
        editor.bindPdf(_dataDir + "Sample-Form-04.pdf");
        // -----
        editor.delListItem("Country", "France");
        // -----
        editor.save(_dataDir + "Sample-Form-04-mod.pdf");
    }
```