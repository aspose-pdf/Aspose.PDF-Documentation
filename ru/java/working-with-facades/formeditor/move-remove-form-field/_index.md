---
title: Перемещение и Удаление Поля Формы
type: docs
weight: 50
url: ru/java/move-remove-form-field/
description: Этот раздел объясняет, как перемещать и удалять поля формы с помощью класса FormEditor.
lastmod: "2021-06-05"
draft: false
---

## Перемещение Поля Формы на Новое Место в Существующем PDF Файле

Если вы хотите переместить поле формы на новое место, вы можете использовать метод [moveField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#moveField-java.lang.String-float-float-float-float-) класса [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor).
 Вы должны предоставить только имя поля и новое местоположение этого поля методу [moveField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#moveField-java.lang.String-float-float-float-float-). Вам также необходимо сохранить обновленный PDF-файл с помощью метода Save класса [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor). Следующий фрагмент кода показывает, как переместить поле формы в новое местоположение в PDF-файле.

```java
 public static void MoveField()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-05.pdf");
            editor.MoveField("Last Name", 262.56f, 496.75f, 382.28f, 514.03f);
            editor.Save(_dataDir + "Sample-Form-05-mod.pdf");
        }
```

## Удаление поля формы из существующего PDF-файла

Чтобы удалить поле формы из существующего PDF-файла, вы можете использовать метод RemoveField класса FormEditor. Этот метод принимает только один аргумент: имя поля. Вам нужно создать объект класса FormEditor, вызвать метод [removeField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#removeField-java.lang.String-), чтобы удалить конкретное поле из PDF, а затем вызвать метод Save для сохранения обновленного PDF файла. В следующем фрагменте кода показано, как удалить поля формы из существующего PDF файла.

```java
 public static void RemoveFields()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");
            editor.RemoveField("First Name");
            editor.RemoveField("Last Name");
            editor.Save(_dataDir + "Sample-Form-01-updated.pdf");
        }
```

## Переименование полей формы в PDF

Также вы можете переименовать ваше поле, используя метод [renameField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#renameField-java.lang.String-java.lang.String-) класса [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor).
```java
    public static void RenameFields()
        {
            var editor = new FormEditor();
            // Привязать PDF
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");
            // Переименовать поле "Фамилия"
            editor.RenameField("Last Name", "LastName");
            // Переименовать поле "Имя"
            editor.RenameField("First Name", "FirstName");
            // Сохранить обновленный PDF
            editor.Save(_dataDir + "Sample-Form-01-updated.pdf");
        }
```