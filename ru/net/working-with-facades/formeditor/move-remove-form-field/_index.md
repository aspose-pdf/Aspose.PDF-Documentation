---
title: Перемещение и Удаление Поля Формы
type: docs
weight: 50
url: /ru/net/move-remove-form-field/
description: Этот раздел объясняет, как вы можете перемещать и удалять поля формы с помощью класса FormEditor.
lastmod: "2021-06-05"
draft: false
---


## Перемещение Поля Формы в Новое Местоположение в Существующем PDF Файле

Если вы хотите переместить поле формы в новое местоположение, вы можете использовать метод [MoveField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/movefield) класса [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor). Вам нужно только предоставить имя поля и новое местоположение этого поля методу [MoveField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/movefield). Вам также нужно сохранить обновленный PDF файл, используя метод [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) из класса [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor). Следующий пример кода показывает, как переместить поле формы в новое местоположение в PDF файле.

```csharp
public static void MoveField()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-05.pdf");
            editor.MoveField("Last Name", 262.56f, 496.75f, 382.28f, 514.03f);
            editor.Save(_dataDir + "Sample-Form-05-mod.pdf");
        }
```

## Удаление поля формы из существующего PDF файла

Чтобы удалить поле формы из существующего PDF файла, вы можете использовать метод RemoveField класса FormEditor. Этот метод принимает только один аргумент: имя поля. Вам нужно создать объект класса FormEditor, вызвать метод [RemoveField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/removefield), чтобы удалить определенное поле из PDF, а затем вызвать метод Save, чтобы сохранить обновленный PDF файл. Следующий фрагмент кода показывает, как удалить поля формы из существующего PDF файла.

```csharp
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

Также вы можете переименовать ваше поле, используя метод [RenameField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/renamefield) класса [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor).

```csharp

        public static void RenameFields()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");
            editor.RenameField("Last Name", "LastName");
            editor.RenameField("First Name", "FirstName");
            editor.Save(_dataDir + "Sample-Form-01-updated.pdf");
        }
```