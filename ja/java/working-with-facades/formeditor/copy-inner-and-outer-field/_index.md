---
title: 内部フィールドと外部フィールドのコピー
type: docs
weight: 40
url: /ja/java/copy-inner-and-outer-field/
description: このセクションでは、FormEditorクラスを使用してcom.aspose.pdf.facadesで内部フィールドと外部フィールドをコピーする方法を説明します。
lastmod: "2021-06-05"
draft: false
---

[copyInnerField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#copyInnerField-java.lang.String-java.lang.String-int-) メソッドは、同じファイル内で、同じ座標、指定したページにフィールドをコピーすることを可能にします。このメソッドには、コピーしたいフィールド名、新しいフィールド名、およびフィールドをコピーするページ番号が必要です。[FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) クラスはこのメソッドを提供します。次のコードスニペットは、同じファイルの同じ場所にフィールドをコピーする方法を示しています。

```java
    public static void CopyInnerField() {
        FormEditor editor = new FormEditor();
        Document document = new Document(_dataDir + "Sample-Form-01.pdf");
        document.getPages().add();
        editor.bindPdf(document);
        editor.copyInnerField("Last Name", "Last Name 2", 2);
        editor.save(_dataDir + "Sample-Form-01-mod.pdf");
    }
```


## 既存のPDFファイルに外部フィールドをコピーする

[copyOuterField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#copyOuterField-java.lang.String-java.lang.String-) メソッドを使用すると、外部PDFファイルからフォームフィールドをコピーし、入力PDFファイルに同じ位置と指定されたページ番号で追加することができます。このメソッドには、フィールドをコピーする元のPDFファイル、フィールド名、およびフィールドをコピーするページ番号が必要です。このメソッドは [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) クラスによって提供されます。次のコードスニペットは、外部PDFファイルからフィールドをコピーする方法を示しています。

```java
  public static void CopyOuterField() {
        FormEditor editor = new FormEditor();
        Document document = new Document();
        document.getPages().add();
        editor.bindPdf(document);
        editor.copyOuterField(_dataDir + "Sample-Form-01.pdf", "First Name", 1);
        editor.copyOuterField(_dataDir + "Sample-Form-01.pdf", "Last Name", 1);
        editor.save(_dataDir + "Sample-Form-02-mod.pdf");
    }
```