---
title: PDFフォームフィールドを追加
type: docs
weight: 10
url: ja/net/add-form-fields/
description: このトピックでは、FormEditorクラスを使用してAspose.PDF Facadesでフォームフィールドを操作する方法を説明します。
lastmod: "2021-06-05"
draft: false
---

## 既存のPDFファイルにフォームフィールドを追加する

既存のPDFファイルにフォームフィールドを追加するには、[FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor)クラスの[AddField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addfield/index)メソッドを使用する必要があります。 このメソッドでは、追加したいフィールドの種類を名前およびフィールドの位置とともに指定する必要があります。[FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor)クラスのオブジェクトを作成し、[AddField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addfield/index)メソッドを使用してPDFに新しいフィールドを追加します。また、[SetFieldLimit](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/setfieldlimit)を使用してフィールド内の文字数に制限を設けることができ、最後に[Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index)メソッドを使用して更新されたPDFファイルを保存します。次のコードスニペットは、既存のPDFファイルにフォームフィールドを追加する方法を示しています。

```csharp
   public static void AddField()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir+"Sample-Form-01.pdf");
            editor.AddField(FieldType.Text, "Country", 1, 232.56f, 496.75f, 352.28f, 514.03f);
            editor.SetFieldLimit("Country", 20);
            editor.Save(_dataDir + "Sample-Form-01-mod.pdf");
        }
```
## 既存のPDFファイルに送信ボタンのURLを追加する

[AddSubmitBtn](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addsubmitbtn) メソッドは、PDFファイルに送信ボタンのURLを設定することができます。これは、送信ボタンがクリックされたときにデータが送信されるURLです。例のコードでは、URL、フィールド名、追加したいページ番号、ボタンの配置座標を指定します。[AddSubmitBtn](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addsubmitbtn) メソッドには、送信ボタンフィールドの名前とURLが必要です。このメソッドは [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor) クラスによって提供されます。以下のコードスニペットは、送信ボタンのURLを設定する方法を示しています。

```csharp
public static void AddSubmitBtn()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");
            editor.AddSubmitBtn("Submit", 1, "Submit", "http://localhost:3000", 232.56f, 466.75f, 352.28f, 484.03f);
            editor.Save(_dataDir + "Sample-Form-01-mod.pdf");
        }
```

## プッシュボタン用のJavaScriptを追加

[AddFieldScript](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addfieldscript) メソッドを使用すると、PDFファイル内のプッシュボタンにJavaScriptを追加できます。このメソッドには、プッシュボタンの名前とJavaScriptが必要です。このメソッドは [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor) クラスによって提供されます。次のコードスニペットは、プッシュボタンにJavaScriptを設定する方法を示しています。

```csharp
     public static void AddFieldScript()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");
            editor.AddFieldScript("Last Name", "app.alert(\"Only one last name\",3);");
            editor.Save(_dataDir + "Sample-Form-01-mod.pdf");
        }
```