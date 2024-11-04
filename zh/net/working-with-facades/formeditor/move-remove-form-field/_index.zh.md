---
title: 移动和移除表单字段
type: docs
weight: 50
url: /net/move-remove-form-field/
description: 本节说明如何使用FormEditor类移动和移除表单字段。
lastmod: "2021-06-05"
draft: false
---

## 在现有PDF文件中将表单字段移动到新位置

如果您想将表单字段移动到新位置，可以使用[FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor)类的[MoveField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/movefield)方法。 你只需要为 [MoveField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/movefield) 方法提供字段名称和此字段的新位置。你还需要使用 [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) 类的 [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) 方法保存更新后的 PDF 文件。以下代码片段向你展示了如何在 PDF 文件中移动表单字段到一个新位置。

```csharp
public static void MoveField()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-05.pdf");
            editor.MoveField("Last Name", 262.56f, 496.75f, 382.28f, 514.03f);
            editor.Save(_dataDir + "Sample-Form-05-mod.pdf");
        }
```

## 从现有 PDF 文件中删除表单字段

为了从现有 PDF 文件中删除表单字段，你可以使用 FormEditor 类的 RemoveField 方法。 此方法仅接受一个参数：字段名称。您需要创建一个FormEditor类的对象，调用[RemoveField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/removefield)方法从PDF中移除特定字段，然后调用Save方法保存更新后的PDF文件。以下代码片段向您展示了如何从现有的PDF文件中删除表单字段。

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

## 重命名PDF中的表单字段

您也可以使用[FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor)类的[RenameField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/renamefield)方法重命名您的字段。

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