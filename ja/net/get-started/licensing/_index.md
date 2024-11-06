---
title: Aspose PDF ライセンス
linktitle: ライセンスと制限
type: docs
weight: 90
url: ja/net/licensing/
description: Aspose. PDF for .NET では、クラシックライセンスとメータードライセンスをお客様に提供しています。また、製品をより深く探求するために限定ライセンスを使用することもできます。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 評価版の制限

お客様には購入前にコンポーネントを十分にテストしていただきたいため、評価版では通常どおりに使用できます。

- **評価用透かし付きで作成されたPDF。** Aspose.PDF for .NET の評価版は製品の全機能を提供しますが、生成されたPDFドキュメントの全ページに「Evaluation Only. Created with Aspose.PDF. Copyright 2002-2020 Aspose Pty Ltd」という透かしが上部に入ります。

- **処理できるコレクション項目の数に制限があります。**
評価版では、任意のコレクションから4つの要素のみを処理できます（例えば、4ページ、4つのフォームフィールドなど）。
評価版では、任意のコレクションから4つの要素のみを処理できます（例えば、4ページ、4つのフォームフィールドなど）。

> Aspose.HTML for .NETの評価版制限なしでテストしたい場合は、30日間の一時ライセンスもリクエストできます。[一時ライセンスの取得方法は？](https://purchase.aspose.com/temporary-license)を参照してください。

## クラシックライセンス

ライセンスはファイルまたはストリームオブジェクトからロードできます。ライセンスを設定する最も簡単な方法は、ライセンスファイルをAspose.PDF.dllファイルと同じフォルダに置き、パスなしでファイル名を指定することです。

Aspose.PDF for .NETと一緒に他のAspose for .NETコンポーネントを使用する場合は、[Aspose.Pdf.License](https://reference.aspose.com/pdf/net/aspose.pdf/license)のようにライセンスの名前空間を指定してください。

### ファイルからライセンスをロード

ライセンスを適用する最も簡単な方法は、ライセンスファイルをAspose.PDF.dllファイルと同じフォルダに置き、パスなしでファイル名を指定することです。

[SetLicense](https://reference.aspose.com/pdf/net/aspose.pdf/license/methods/setlicense/index)メソッドを呼び出すときに渡すライセンス名は、ライセンスファイルの名前である必要があります。
[SetLicense](https://reference.aspose.com/pdf/net/aspose.pdf/license/methods/setlicense/index) メソッドを呼び出す際に渡すライセンス名は、ライセンスファイルの名前である必要があります。

```csharp
public static void SetLicenseExample()
{
    // ライセンスオブジェクトを初期化
    Aspose.Pdf.License license = new Aspose.Pdf.License();
    try
    {
        // ライセンスを設定
        license.SetLicense("Aspose.Pdf.lic");
    }
    catch (Exception)
    {
        // 何か問題が発生
        throw;
    }
    Console.WriteLine("ライセンスが正常に設定されました。");
}
```
### ストリームオブジェクトからライセンスをロードする

次の例は、ストリームからライセンスをロードする方法を示しています。

```csharp
public static void SetLicenseFromStream()
{
    // ライセンスオブジェクトを初期化
    Aspose.Pdf.License license = new Aspose.Pdf.License();
    // ファイルストリームからライセンスをロード
    System.IO.FileStream myStream =
        new System.IO.FileStream(
            "Aspose.Pdf.lic",
            System.IO.FileMode.Open);
    // ライセンスを設定
    license.SetLicense(myStream);
    Console.WriteLine("ライセンスが正常に設定されました。");
}
```
## メータードライセンス

Aspose.PDF では、開発者がメータードキーを適用できます。これは新しいライセンスメカニズムです。新しいライセンスメカニズムは、既存のライセンス方法と共に使用されます。API 機能の使用に基づいて課金されたいお客様は、メータードライセンスを使用できます。詳細については、メータードライセンス FAQ セクションを参照してください。

メータードキーを適用するために Metered という新しいクラスが導入されました。以下は、メータード公開キーと秘密キーを設定する方法を示すサンプルコードです。

詳細については、[メータードライセンス FAQ](https://purchase.aspose.com/faqs/licensing/metered) セクションを参照してください。

```csharp
public static void SetMeteredLicense()
{
    // メータード公開キーと秘密キーを設定
    Aspose.Pdf.Metered metered = new Aspose.Pdf.Metered();
    // setMeteredKey プロパティにアクセスし、パラメータとして公開キーと秘密キーを渡す
    metered.SetMeteredKey(
        "<ここに公開キーを入力>",
        "<ここに秘密キーを入力>");

    // ディスクからドキュメントを読み込む。
    Document doc = new Document("input.pdf");
    // ドキュメントのページ数を取得
    Console.WriteLine(doc.Pages.Count);
}
```
COMアプリケーションが **Aspose.PDF for .NET** を使用する場合、License クラスも使用する必要があります。

考慮が必要な点：
組み込みリソースは、追加される方法でアセンブリに含まれています。つまり、テキストファイルをアプリケーションの組み込みリソースとして追加し、結果のEXEをメモ帳で開くと、テキストファイルの正確な内容が表示されます。したがって、ライセンスファイルを組み込みリソースとして使用する場合、誰でも単純なテキストエディタでexeファイルを開き、ライセンスの内容を見たり抽出したりできます。

したがって、アプリケーションにライセンスを埋め込む際に追加のセキュリティ層を追加するために、ライセンスを圧縮/暗号化した後、それをアセンブリに埋め込むことができます。Aspose.PDF.lic ライセンスファイルがあると仮定し、パスワード test で Aspose.PDF.zip を作成し、この zip ファイルをソリューションに埋め込みましょう。以下のコードスニペットを使用してライセンスを初期化できます：

```csharp
using System;
using System.IO;
using System.IO.Compression;
using System.Reflection;

namespace Aspose.Pdf.Examples
{
    class ExampleLicensing
    {
        public static void LicenseDemo()
        {
            License license = new License();
            license.SetLicense(GetSecureLicenseFromStream());
            Document doc = new Document("document.pdf");
            //ドキュメントのページ数を取得する
            Console.WriteLine(doc.Pages.Count);
        }

        private static Stream GetSecureLicenseFromStream()
        {
            var assembly = Assembly.GetExecutingAssembly();
            var memoryStream = new MemoryStream();
            using (var zipToOpen = assembly.GetManifestResourceStream("Aspose.Pdf.Examples.License.Aspose.PDF.zip"))
            {
                using (ZipArchive archive = new ZipArchive(zipToOpen ?? throw new InvalidOperationException(), ZipArchiveMode.Read))
                {
                    var unpackedLicense  = archive.GetEntry("Aspose.PDF.lic");
                    unpackedLicense?.Open().CopyTo(memoryStream);
                }
            }

            memoryStream.Position = 0;
            return memoryStream;
        }
    }
}
```
### 2005/01/22以前に購入したライセンスの適用

Aspose.PDF for .NETは古いスタイルのライセンスをもはやサポートしていません。2005年1月22日以前にライセンスを取得し、Aspose.PDFのより新しいバージョンに更新した場合は、新しいライセンスファイルを取得するために営業チームにご連絡ください。
