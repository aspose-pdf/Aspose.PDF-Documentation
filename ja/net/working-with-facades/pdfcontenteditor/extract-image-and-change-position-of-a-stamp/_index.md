---
title: 画像を抽出してスタンプの位置を変更する
type: docs
weight: 30
url: ja/net/extract-image-and-change-position-of-a-stamp/
description: このセクションでは、Aspose.PDF Facadesを使用して画像を抽出し、スタンプの位置を変更する方法を説明します。
lastmod: "2021-06-05"
draft: false
---

## 画像スタンプから画像を抽出する

[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) クラスを使用すると、PDFファイル内のスタンプから画像を抽出できます。 最初に、[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor)クラスのオブジェクトを作成し、[BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3)メソッドを使用して入力PDFファイルをバインドする必要があります。その後、[GetStamps](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/getstamps)メソッドを呼び出して、特定のPDFファイルのページからStampInfoオブジェクトの配列を取得します。その後、StampInfo.Imageプロパティを使用してStampInfoから画像を取得できます。画像を取得したら、その画像を保存したり、画像のさまざまなプロパティを操作したりできます。以下のコードスニペットは、画像スタンプから画像を抽出する方法を示しています。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Stamps-Watermarks-ExtractImageImageStamp-ExtractImageImageStamp.cs" >}}

## PDFファイル内のスタンプの位置を変更する

[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor)クラスを使用すると、PDFファイル内のスタンプの位置を変更できます。 まず、[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) クラスのオブジェクトを作成し、[BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) メソッドを使用して入力 PDF ファイルをバインドする必要があります。その後、スタンプのインデックスと PDF ファイルの特定のページ上の新しい位置を指定して、[MoveStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/movestamp) メソッドを呼び出します。次に、[Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) メソッドを使用して更新されたファイルを保存できます。以下のコードスニペットは、特定のページにスタンプを移動する方法を示しています。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Stamps-Watermarks-ChangeStampPosition-ChangeStampPosition.cs" >}}

また、特定の StampId を使用して特定のスタンプを移動するために、[MoveStampById](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/movestampbyid) メソッドを使用することもできます。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Stamps-Watermarks-ChangeStampPosition-ChangeStampPositionByID.cs" >}}