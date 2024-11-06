---
title: 内部フィールドと外部フィールドのコピー
type: docs
weight: 40
url: ja/net/copy-inner-and-outer-field/
description: このセクションでは、FormEditorクラスを使用してAspose.PDFファサードで内部フィールドと外部フィールドをコピーする方法を説明します。
lastmod: "2021-06-05"
draft: false
---

[CopyInnerField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/copyinnerfield/index) メソッドを使用すると、同じファイル内の指定したページの同じ座標にフィールドをコピーできます。このメソッドには、コピーしたいフィールド名、新しいフィールド名、およびフィールドをコピーするページ番号が必要です。[FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor) クラスはこのメソッドを提供します。以下のコードスニペットは、同じファイルの同じ場所にフィールドをコピーする方法を示しています。

```csharp
  public static void CopyInnerField()
        {
            var editor = new FormEditor();
            var document = new Aspose.Pdf.Document(_dataDir + "Sample-Form-01.pdf");
            document.Pages.Add();
            editor.BindPdf(document);
            editor.CopyInnerField("Last Name", "Last Name 2", 2);
            editor.Save(_dataDir + "Sample-Form-01-mod.pdf");
        }
```

## 既存のPDFファイルで外部フィールドをコピーする

[CopyOuterField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/copyouterfield/index) メソッドを使用すると、外部のPDFファイルからフォームフィールドをコピーし、入力PDFファイルの同じ場所と指定されたページ番号に追加することができます。このメソッドは、フィールドをコピーする必要があるPDFファイル、フィールド名、およびフィールドをコピーする必要があるページ番号を必要とします。このメソッドは [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor) クラスによって提供されます。以下のコードスニペットは、外部のPDFファイルからフィールドをコピーする方法を示しています。

```csharp
   public static void CopyOuterField()
        {
            var editor = new FormEditor();
            var document = new Aspose.Pdf.Document();
            document.Pages.Add();
            editor.BindPdf(document);
            editor.CopyOuterField(_dataDir + "Sample-Form-01.pdf", "First Name", 1);
            editor.CopyOuterField(_dataDir + "Sample-Form-01.pdf", "Last Name", 1);
            editor.Save(_dataDir + "Sample-Form-02-mod.pdf");
        }
```