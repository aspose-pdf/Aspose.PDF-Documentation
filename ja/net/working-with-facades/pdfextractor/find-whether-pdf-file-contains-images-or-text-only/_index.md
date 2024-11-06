---
title: PDFに画像またはテキストが含まれているかどうかを確認する
linktitle: テキストと画像の存在を確認
type: docs
weight: 40
url: ja/net/find-whether-pdf-file-contains-images-or-text-only/
description: このトピックでは、PdfExtractorクラスを使用してPDFファイルに画像またはテキストのみが含まれているかどうかを確認する方法を説明します。
lastmod: "2021-06-05"
draft: false
---

## 背景

PDFファイルにはテキストと画像の両方を含めることができます。場合によっては、ユーザーがPDFファイルにテキストのみが含まれているか、画像のみが含まれているかを確認する必要があります。また、両方を含むか、いずれも含まないかを見つけることもできます。

{{% alert color="primary" %}}

次のコードスニペットは、この要件を満たす方法を示しています。

{{% /alert %}}

```csharp
 public static void CheckIfPdfContainsTextOrImages()
{
    // メモリストリームオブジェクトをインスタンス化して、ドキュメントから抽出されたテキストを保持する
    MemoryStream ms = new MemoryStream();
    // PdfExtractorオブジェクトをインスタンス化
    PdfExtractor extractor = new PdfExtractor();

    // 入力PDFドキュメントを抽出器にバインド
    extractor.BindPdf(_dataDir + "FilledForm.pdf");
    // 入力PDFドキュメントからテキストを抽出
    extractor.ExtractText();
    // 抽出されたテキストをテキストファイルに保存
    extractor.GetText(ms);
    // MemoryStreamの長さが1以上であるかどうかを確認

    bool containsText = ms.Length >= 1;

    // 入力PDFドキュメントから画像を抽出
    extractor.ExtractImage();

    // whileループ内でHasNextImageメソッドを呼び出し。画像が終了すると、ループが終了
    bool containsImage = extractor.HasNextImage();

    // このPDFがテキストのみか画像のみかを見つける

    if (containsText && !containsImage)
        Console.WriteLine("PDFにはテキストのみが含まれています");
    else if (!containsText && containsImage)
        Console.WriteLine("PDFには画像のみが含まれています");
    else if (containsText && containsImage)
        Console.WriteLine("PDFにはテキストと画像の両方が含まれています");
    else if (!containsText && !containsImage)
        Console.WriteLine("PDFにはテキストも画像も含まれていません");
}
```