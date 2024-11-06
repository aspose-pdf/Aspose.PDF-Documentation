---
title: 画像の操作
type: docs
weight: 30
url: ja/java/working-with-image/
description: このセクションでは、Aspose.PDF Facadesを使用して画像を置き換える方法を説明します。これは、PDFに関する一般的な操作のためのツールセットです。
lastmod: "2021-06-25"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 特定のPDFページから画像を削除する（ファサード）

[PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) クラスは、既存のPDFファイル内の画像を置き換えることを可能にします。
 The [replaceImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#replaceImage-int-int-java.lang.String-) メソッドは、この目標を達成するのに役立ちます。[PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) クラスのオブジェクトを作成し、bindPdf メソッドを使用して入力 PDF ファイルをバインドする必要があります。その後、ページ番号、置き換える画像のインデックス、および置き換える画像のパスの3つのパラメータを使用して [replaceImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#replaceImage-int-int-java.lang.String-) メソッドを呼び出す必要があります。

次のコードスニペットは、既存の PDF ファイル内の画像を置き換える方法を示しています。

```java
public class PdfContentEditorImages {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/facades/PdfContentEditor/";

    public static void DeleteImage()
    {
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
        editor.deleteImage(2, new int [] { 1,3 });
        editor.save(_dataDir + "PdfContentEditorDemo10.pdf");
    }
```

## PDFファイルからすべての画像を削除する (Facades)

すべての画像は、[PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) の [deleteImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#deleteImage--) メソッドを使用してPDFファイルから削除することができます。すべての画像を削除するには、パラメータなしのオーバーロードで [deleteImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#deleteImage--) メソッドを呼び出し、Saveメソッドを使用して更新されたPDFファイルを保存します。

```java
   public static void DeleteImages()
    {
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
        editor.deleteImage();
        editor.save(_dataDir + "PdfContentEditorDemo11.pdf");
    }
```

## PDFファイル内の画像を置き換える (Facades)

[PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) の [replaceImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#replaceImage-int-int-java.lang.String-) メソッドを使用して、PDFファイル内の画像を置き換えることができます。

```java
   public static void ReplaceImage()
    {
        // PdfContentEditorオブジェクトを作成し、指定されたPDFファイルをロードします。
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample_cats_dogs.pdf"));
        // 指定されたページに新しい画像を置き換えます。
        editor.replaceImage(2, 4, _dataDir+"cat04.jpg");
        // 変更を保存して、PDFファイルを指定されたパスに保存します。
        editor.save(_dataDir + "PdfContentEditorDemo12.pdf");
    }
```