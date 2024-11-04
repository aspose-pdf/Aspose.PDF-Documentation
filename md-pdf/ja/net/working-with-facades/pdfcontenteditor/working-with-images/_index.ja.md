---
title: 画像を使用したPDFコンテンツエディター
type: docs
weight: 50
url: /net/working-with-images-in-pdf
description: このセクションでは、Aspose.PDF Facadesを使用してPdfContentEditorクラスで画像を追加および削除する方法について説明します。
lastmod: "2021-06-24"
---

## 特定のPDFページから画像を削除する（Facades）

特定のページから画像を削除するには、pageNumberとindexパラメーターを使用して[DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1)メソッドを呼び出す必要があります。 インデックスパラメーターは削除される画像のインデックスを表す整数の配列です。まず、[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) クラスのオブジェクトを作成し、次に [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1) メソッドを呼び出す必要があります。その後、[Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) メソッドを使用して更新されたPDFファイルを保存できます。

次のコードスニペットは、PDFの特定のページから画像を削除する方法を示しています。

```csharp
public static void DeleteImage()
{
    PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
    editor.DeleteImage(2, new[] { 2 });
    editor.Save(_dataDir + "PdfContentEditorDemo10.pdf");
}
```

## PDFファイルからすべての画像を削除する (Facades)

すべての画像は、[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) の [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1) メソッドを使用してPDFファイルから削除できます。 [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1) メソッドを呼び出します – パラメータなしのオーバーロード – すべての画像を削除し、[Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) メソッドを使用して更新されたPDFファイルを保存します。

次のコードスニペットは、PDFファイルからすべての画像を削除する方法を示しています。

```csharp
public static void DeleteImages()
{
    PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
    editor.DeleteImage();
    editor.Save(_dataDir + "PdfContentEditorDemo11.pdf");
}
```

## PDFファイル内の画像を置き換える (Facades)

[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) を使用すると、PDFファイル内の画像を置き換えることができます。このためには [ReplaceImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/replaceimage) メソッドを呼び出し、結果を保存します。

```csharp
public static void ReplaceImage()
{
    PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample_cats_dogs.pdf"));
    editor.ReplaceImage(2, 4, @"C:\Samples\Facades\PdfContentEditor\cat04.jpg");
    editor.Save(_dataDir + "PdfContentEditorDemo12.pdf");
}
```