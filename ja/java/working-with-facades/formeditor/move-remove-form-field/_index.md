---
title: フォームフィールドの移動と削除
type: docs
weight: 50
url: /ja/java/move-remove-form-field/
description: このセクションでは、FormEditorクラスを使用してフォームフィールドを移動および削除する方法を説明します。
lastmod: "2021-06-05"
draft: false
---

## 既存のPDFファイルでフォームフィールドを新しい場所に移動する

フォームフィールドを新しい場所に移動したい場合は、[FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) クラスの [moveField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#moveField-java.lang.String-float-float-float-float-) メソッドを使用できます。
 あなたはこのフィールド名とフィールドの新しい位置だけを[moveField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#moveField-java.lang.String-float-float-float-float-)メソッドに提供する必要があります。また、[FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor)クラスのSaveメソッドを使用して、更新されたPDFファイルを保存する必要があります。以下のコードスニペットは、PDFファイルの新しい位置にフォームフィールドを移動する方法を示しています。

```java
 public static void MoveField()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-05.pdf");
            editor.MoveField("Last Name", 262.56f, 496.75f, 382.28f, 514.03f);
            editor.Save(_dataDir + "Sample-Form-05-mod.pdf");
        }
```

## 既存のPDFファイルからフォームフィールドを削除する

既存のPDFファイルからフォームフィールドを削除するには、FormEditorクラスのRemoveFieldメソッドを使用できます。 このメソッドは1つの引数、つまりフィールド名のみを取ります。FormEditorクラスのオブジェクトを作成し、[removeField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#removeField-java.lang.String-)メソッドを呼び出してPDFから特定のフィールドを削除し、その後、Saveメソッドを呼び出して更新されたPDFファイルを保存します。次のコードスニペットは、既存のPDFファイルからフォームフィールドを削除する方法を示しています。

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

## PDFのフォームフィールドの名前を変更する

また、[FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor)クラスの[renameField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#renameField-java.lang.String-java.lang.String-)メソッドを使用して、フィールドの名前を変更することもできます。
```java
    public static void RenameFields()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");
            editor.RenameField("姓", "LastName");
            editor.RenameField("名", "FirstName");
            editor.Save(_dataDir + "Sample-Form-01-updated.pdf");
        }
```