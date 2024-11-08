---
title: フォームフィールドの移動と削除
type: docs
weight: 50
url: /ja/net/move-remove-form-field/
description: このセクションでは、FormEditor クラスを使用してフォームフィールドを移動および削除する方法について説明します。
lastmod: "2021-06-05"
draft: false
---

## 既存のPDFファイルでフォームフィールドを新しい場所に移動する

フォームフィールドを新しい場所に移動したい場合は、[FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) クラスの [MoveField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/movefield) メソッドを使用できます。 このフィールドの名前と新しい位置を [MoveField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/movefield) メソッドに提供するだけです。また、[FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) クラスの [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) メソッドを使用して更新されたPDFファイルを保存する必要があります。以下のコードスニペットは、PDFファイル内の新しい位置にフォームフィールドを移動する方法を示しています。

```csharp
public static void MoveField()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-05.pdf");
            editor.MoveField("Last Name", 262.56f, 496.75f, 382.28f, 514.03f);
            editor.Save(_dataDir + "Sample-Form-05-mod.pdf");
        }
```

## 既存のPDFファイルからフォームフィールドを削除する

既存のPDFファイルからフォームフィールドを削除するには、FormEditorクラスのRemoveFieldメソッドを使用できます。 このメソッドは1つの引数、フィールド名のみを取ります。FormEditorクラスのオブジェクトを作成し、PDFから特定のフィールドを削除するために[RemoveField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/removefield)メソッドを呼び出し、その後、更新されたPDFファイルを保存するためにSaveメソッドを呼び出す必要があります。次のコードスニペットは、既存のPDFファイルからフォームフィールドを削除する方法を示しています。

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

## PDFのフォームフィールドの名前を変更

また、[FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor)クラスの[RenameField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/renamefield)メソッドを使用してフィールドの名前を変更することもできます。

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