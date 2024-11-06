---
title: PDFから画像を抽出するC#
linktitle: PDFから画像を抽出する
type: docs
weight: 20
url: ja/net/extract-images-from-the-pdf-file/
description: Aspose.PDF for .NETを使用してPDFから画像の一部を抽出する方法
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

各ページの[Resources](https://reference.aspose.com/pdf/net/aspose.pdf/resources)コレクションの[Images](https://reference.aspose.com/pdf/net/aspose.pdf/resources/properties/images)コレクションに画像が保持されています。特定のページを抽出し、Imagesコレクションから特定のインデックスの画像を取得します。

画像のインデックスは[XImage](https://reference.aspose.com/pdf/net/aspose.pdf/ximage)オブジェクトを返します。このオブジェクトには抽出した画像を保存するために使用できるSaveメソッドが提供されています。以下のコードスニペットは、PDFファイルから画像を抽出する方法を示しています。

以下のコードスニペットは[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリでも動作します。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET にアクセスしてください
```
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir+ "ExtractImages.pdf");

// 特定の画像を抽出
XImage xImage = pdfDocument.Pages[1].Resources.Images[1];

FileStream outputImage = new FileStream(dataDir + "output.jpg", FileMode.Create);

// 出力画像を保存
xImage.Save(outputImage, ImageFormat.Jpeg);
outputImage.Close();

dataDir = dataDir + "ExtractImages_out.pdf";

// 更新されたPDFファイルを保存
pdfDocument.Save(dataDir);
```
