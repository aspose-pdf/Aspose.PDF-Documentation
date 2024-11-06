---
title: リストアイテムの操作
type: docs
weight: 30
url: ja/net/working-with-list-item/
description: このセクションでは、FormEditorクラスを使用してAspose.PDF Facadesでリストアイテムを操作する方法について説明します。
lastmod: "2021-06-05"
draft: false
---

## 既存のPDFファイルにリストアイテムを追加

[AddListItem](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addlistitem) メソッドは、[ListBox](https://reference.aspose.com/pdf/net/aspose.pdf.forms/listboxfield) フィールドにアイテムを追加することを可能にします。最初の引数はフィールド名で、2番目の引数はフィールドアイテムです。単一のフィールドアイテムを渡すことも、アイテムのリストを含む文字列の配列を渡すこともできます。このメソッドは [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) クラスによって提供されます。以下のコードスニペットは、PDFファイルにリストアイテムを追加する方法を示しています。

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

## 既存のPDFファイルからリスト項目を削除する

[DelListItem](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/dellistitem) メソッドを使用すると、[ListBox](https://reference.aspose.com/pdf/net/aspose.pdf.forms/listboxfield) から特定の項目を削除できます。最初のパラメータはフィールド名で、2番目のパラメータはリストから削除したい項目です。このメソッドは [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) クラスによって提供されます。以下のコードスニペットは、PDFファイルからリスト項目を削除する方法を示しています。

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