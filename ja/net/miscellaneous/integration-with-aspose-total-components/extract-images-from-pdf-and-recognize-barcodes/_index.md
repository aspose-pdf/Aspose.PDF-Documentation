---
title: PDFから画像を抽出し、バーコードを認識する
type: docs
weight: 20
url: /ja/net/extract-images-from-pdf-and-recognize-barcodes/
---

{{% alert color="primary" %}}

PDFドキュメントは通常、テキスト、画像、テーブル、添付ファイル、グラフ、注釈などの関連オブジェクトで構成されています。PDFファイル内にバーコードが埋め込まれている場合があり、一部の顧客はPDFファイル内のバーコードを識別する必要があります。次の記事では、PDFページから画像を抽出し、それらの中のバーキュードを識別する手順について説明します。

{{% /alert %}}

Aspose.PDF for .NETのドキュメントオブジェクトモデルによると、PDFファイルには1ページ以上が含まれており、各ページにはリソースオブジェクトの中に画像、フォーム、フォントのコレクションが含まれています。
Aspose.PDF for .NETのドキュメントオブジェクトモデルによると、PDFファイルには1ページ以上が含まれ、各ページにはリソースオブジェクトのイメージ、フォーム、フォントのコレクションが含まれています。

**C#**

```csharp

//ドキュメントを開く
Aspose.PDF.Document pdfDocument = new Aspose.PDF.Document("source.pdf");

// PDFファイルの個々のページを通して移動する

for (int pageCount = 1; pageCount <= pdfDocument.Pages.Count; pageCount++)
{
    // PDFページから抽出された各イメージを通して移動する
    foreach (XImage xImage in pdfDocument.Pages[pageCount].Resources.Images)
    {
        using (MemoryStream imageStream = new MemoryStream())
        {
            //出力イメージを保存する
            xImage.Save(imageStream, System.Drawing.Imaging.ImageFormat.Jpeg);
   
            // ストリームの位置をストリームの開始位置に設定する
            imageStream.Position = 0;
   
            // BarCodeReaderオブジェクトをインスタンス化する
   
            Aspose.BarCodeRecognition.BarCodeReader barcodeReader = new Aspose.BarCodeRecognition.BarCodeReader(imageStream, Aspose.BarCodeRecognition.BarCodeReadType.Code39Extended);
   
            while (barcodeReader.Read())
            {
                // BarCode画像からBarCodeテキストを取得する
                string code = barcodeReader.GetCodeText();
   
                // BarCodeテキストをコンソール出力に書き込む
                Console.WriteLine("BARCODE : " + code);
            }
   
            // BarCodeReaderオブジェクトを閉じてイメージファイルを解放する
   
            barcodeReader.Close();
        }
    }
}

```

詳細については、次のリンクをご覧ください。

- [PDFファイルから画像を抽出する](/net/extract-images-from-the-pdf-file/)
- [バーコードを読む](https://docs.aspose.com/barcode/net/read-barcodes/)
