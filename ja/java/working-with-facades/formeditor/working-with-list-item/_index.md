---
title: リストアイテムの操作
type: docs
weight: 30
url: ja/java/working-with-list-item/
description: このセクションでは、FormEditorクラスを使用してcom.aspose.pdf.facadesでリストアイテムを操作する方法を説明します。
lastmod: "2021-06-05"
draft: false
---

## 既存のPDFファイルにリストアイテムを追加する

[addListItem](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#addListItem-java.lang.String-java.lang.String-) メソッドを使用すると、ListBoxフィールドにアイテムを追加できます。最初の引数はフィールド名で、2番目の引数はフィールドアイテムです。単一のフィールドアイテムを渡すことも、アイテムのリストを含む文字列の配列を渡すこともできます。このメソッドは [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) クラスによって提供されます。以下のコードスニペットは、PDFファイルにリストアイテムを追加する方法を示しています。

```java
public static void AddListItem() {
        FormEditor editor = new FormEditor();
        editor.bindPdf(_dataDir + "Sample-Form-01.pdf");
        editor.addField(FieldType.ListBox, "Country", 1, 232.56f, 476.75f, 352.28f, 514.03f);
        editor.addListItem("Country", "USA");
        editor.addListItem("Country", "Canada");
        editor.addListItem("Country", "France");
        editor.addListItem("Country", "Spain");
        editor.save(_dataDir + "Sample-Form-01-mod.pdf");
    }
```


## 既存のPDFファイルからリストアイテムを削除する

[delListItem](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#delListItem-java.lang.String-java.lang.String-) メソッドを使用すると、ListBoxから特定のアイテムを削除できます。最初のパラメータはフィールド名で、2番目のパラメータはリストから削除したいアイテムです。このメソッドは [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) クラスによって提供されます。次のコードスニペットは、PDFファイルからリストアイテムを削除する方法を示しています。

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