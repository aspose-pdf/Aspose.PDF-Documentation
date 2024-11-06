---
title: PDFページを画像に変換し、バーコードを認識する
type: docs
weight: 10
url: ja/net/convert-pdf-pages-to-images-and-recognize-barcodes/
---

{{% alert color="primary" %}}

PDFドキュメントは通常、テキスト、画像、表、添付ファイル、グラフ、注釈などのオブジェクトを含んでいます。一部のお客様は、ドキュメントにバーコードを埋め込み、そのPDFファイル内のバーコードを識別する必要があります。次の記事では、PDFファイルのページを画像に変換し、Aspose.Barcode for .NETを使用して画像内のバーコードを識別する方法を説明します。

{{% /alert %}}
### **ページを画像に変換し、バーコードを認識する**

{{% alert color="primary" %}}

Aspose.PDF for .NETは、PDFドキュメントを管理するための非常に強力な製品です。これにより、PDFドキュメントのページを画像に簡単に変換できます。Aspose.BarCode for .NETも、バーコードの生成と認識に同じくらい強力な製品です。

Aspose.PDF.Facades名前空間の下のPdfConverterクラスは、PDFページをさまざまな画像形式に変換することをサポートしています。
Aspose.PDF.Facades名前空間の下にあるPdfConverterクラスは、PDFページを様々な画像形式に変換することをサポートしています。

ページが画像形式に変換された後、Aspose.BarCode for .NETを使用して、それらの中のバーコードを識別することができます。以下のコードサンプルは、PdfConverterまたはPngDeviceを使用してページを変換する方法を示しています。

{{% /alert %}}

#### **Aspose.PDF.Facadesの使用**

{{% alert color="primary" %}}

PdfConverterクラスには、現在のPDFページから画像を生成するGetNextImageという名前のメソッドが含まれています。出力画像形式を指定するために、このメソッドはSystem.Drawing.Imaging.ImageFormat列挙型からの引数を受け入れます。

Aspose.Barcodeには、BarCodeRecognitionという名前空間が含まれており、その中にBarCodeReaderクラスがあります。BarCodeReaderクラスでは、画像ファイルからバーコードを読み取り、特定し、識別することができます。

この例の目的では、まずAspose.PDF.Facades.PdfConverterを使用して、PDFファイルのページを画像に変換します。
##### **プログラミングサンプル**
**C#**

{{< highlight csharp >}}

 //PdfConverterオブジェクトを作成する

PdfConverter converter = new PdfConverter();

//入力PDFファイルをバインドする

converter.BindPdf("Source.pdf");

// 処理を開始するページを指定する

converter.StartPage = 1;

// 処理を終了するページを指定する

converter.EndPage = 1;

// 結果の画像の解像度を指定するResolutionオブジェクトを作成する

converter.Resolution = new Aspose.PDF.Devices.Resolution(300);

//変換プロセスを初期化する

converter.DoConvert();

// 結果の画像を保持するためのMemoryStreamオブジェクトを作成する

MemoryStream imageStream = new MemoryStream();

//ページが存在するかを確認し、次々に画像に変換する

while (converter.HasNextImage())

{

    // 指定された画像フォーマットで画像を保存する

    converter.GetNextImage(imageStream, System.Drawing.Imaging.ImageFormat.Png);

    // ストリームの位置をストリームの先頭に設定する

    imageStream.Position = 0;

{{< /highlight >}}
```plaintext
// ストリームの位置をストリームの先頭に設定

imageStream.Position = 0;

// BarCodeReaderオブジェクトをインスタンス化

Aspose.BarCodeRecognition.BarCodeReader barcodeReader = new Aspose.BarCodeRecognition.BarCodeReader(imageStream, Aspose.BarCodeRecognition.BarCodeReadType.Code39Extended);

// String txtResult.Text = "";

while (barcodeReader.Read())

{

    // バーコードイメージからバーコードテキストを取得

    string code = barcodeReader.GetCodeText();

    // バーコードテキストをコンソール出力に書き込み

    Console.WriteLine("BARCODE : " + code);

}

// BarCodeReaderオブジェクトを閉じてイメージファイルを解放

barcodeReader.Close();

}

// PdfConverterインスタンスを閉じてリソースを解放

converter.Close();

// イメージオブジェクトを保持するストリームを閉じる

imageStream.Close();

{{< /highlight >}}

{{% alert color="primary" %}}

上記のコードスニペットでは、出力イメージがMemoryStreamオブジェクトに保存されています。
```
上記のコードスニペットでは、出力画像がMemoryStreamオブジェクトに保存されます。

{anchor:devices]
#### **PngDeviceクラスの使用**
Aspose.PDF.Devicesには、PngDeviceがあります。このクラスを使うと、PDFドキュメントのページをPNG画像に変換できます。

この例では、ソースPDFファイルをDocumentにロードし、ドキュメントのページをPNG画像に変換します。画像が作成されたら、Aspose.BarCodeRecognitionの下にあるBarCodeReaderクラスを使用して、画像内のバーコードを識別し、読み取ります。

このコードサンプルは、PDFドキュメントのページを通過し、各ページ上のバーコードを識別しようとします。

##### **プログラミングサンプル**
**C#**

 //PDFドキュメントを開く

Aspose.PDF.Document pdfDocument = new Aspose.PDF.Document("source.pdf");

// PDFファイルの個々のページをトラバースします

for (int pageCount = 1; pageCount <= pdfDocument.Pages.Count; pageCount++)

{

    using (MemoryStream imageStream = new MemoryStream())
```csharp
using (MemoryStream imageStream = new MemoryStream())
{
    // Resolutionオブジェクトを作成する
    Aspose.PDF.Devices.Resolution resolution = new Aspose.PDF.Devices.Resolution(300);
    
    // Resolutionオブジェクトを引数として渡しながらPngDeviceオブジェクトをインスタンス化する
    Aspose.PDF.Devices.PngDevice pngDevice = new Aspose.PDF.Devices.PngDevice(resolution);
    
    // 特定のページを変換し、画像をストリームに保存する
    pngDevice.Process(pdfDocument.Pages[pageCount], imageStream);
    
    // ストリームの位置をストリームの始まりに設定する
    imageStream.Position = 0;
    
    // BarCodeReaderオブジェクトをインスタンス化する
    Aspose.BarCodeRecognition.BarCodeReader barcodeReader = new Aspose.BarCodeRecognition.BarCodeReader(imageStream, Aspose.BarCodeRecognition.BarCodeReadType.Code39Extended);
    
    // String txtResult.Text = "";
    
    while (barcodeReader.Read())
    {
        // バーコード画像からバーコードテキストを取得する
        string code = barcodeReader.GetCodeText();
    }
}
```
```csharp
string code = barcodeReader.GetCodeText();

// コンソール出力にバーコードテキストを書き込む
Console.WriteLine("BARCODE : " + code);

}

// BarCodeReaderオブジェクトを閉じて、画像ファイルを解放する
barcodeReader.Close();

}

}

{{< /highlight >}}



{{% alert color="primary" %}}

この記事で取り上げられたトピックの詳細については、以下を参照してください:

- PDFページを異なるイメージフォーマットに変換する (Facades)
- すべてのPDFページをPNGイメージに変換する
- [バーコードを読む](https://docs.aspose.com/barcode/net/read-barcodes/)


{{% /alert %}}
```
