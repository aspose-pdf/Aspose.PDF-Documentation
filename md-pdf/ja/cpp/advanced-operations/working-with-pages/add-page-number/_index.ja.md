---
title: PDFにページ番号を追加するC++
linktitle: ページ番号を追加
type: docs
weight: 100
url: /cpp/add-page-number/
description: Aspose.PDF for C++を使用して、PageNumber Stampクラスを使用してPDFファイルにページ番号スタンプを追加できます。
lastmod: "2021-12-03"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 既存のPDFにページ番号を追加する方法

すべてのドキュメントにはページ番号が必要です。ページ番号は、読者がドキュメントのさまざまな部分を見つけやすくします。
**Aspose.PDF for C++**を使用すると、PageNumberStampを使用してページ番号を追加できます。

次のステップとサンプルコードは、[PageNumberStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_number_stamp)ページ要素を使用して既存のPDFドキュメントにページ番号ラベルを追加し、PDFに自動的にページ番号を追加する方法を示しています。

既存のPDFドキュメントにページ番号を追加する手順：

ページ番号スタンプを追加するには、必要なプロパティを使用して[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)オブジェクトと[PageNumberStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_number_stamp)オブジェクトを作成する必要があります。

その後、[Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) の [AddStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#a3b998038dedf5266b4d60586b1b53d02) メソッドを呼び出して、PDF にスタンプを追加できます。

また、ページ番号スタンプのフォント属性を設定することもできます。

次のコードスニペットは、PDF ファイルにページ番号を追加する方法を示しています。

```cpp
void AddPageNumberToPDF() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("PageNumberStamp.pdf");
    String outputFileName("PageNumberStamp_out.pdf");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // ページ番号スタンプを作成
    auto pageNumberStamp = MakeObject<PageNumberStamp>();
    //// スタンプが背景であるかどうか
    //pageNumberStamp.Background = false;
    //pageNumberStamp.Format = "Page # of " + pdfDocument.Pages.Count;
    //pageNumberStamp.BottomMargin = 10;
    //pageNumberStamp.HorizontalAlignment = HorizontalAlignment.Center;
    //pageNumberStamp.StartingNumber = 1;

    //// テキストプロパティを設定
    //pageNumberStamp.TextState.Font = FontRepository.FindFont("Arial");
    //pageNumberStamp.TextState.FontSize = 14.0F;
    //pageNumberStamp.TextState.FontStyle = FontStyles.Bold;
    //pageNumberStamp.TextState.FontStyle = FontStyles.Italic;
    //pageNumberStamp.TextState.ForegroundColor = Color.Aqua;

    // 特定のページにスタンプを追加
    document->get_Pages()->idx_get(1)->AddStamp(pageNumberStamp);

    // 出力ドキュメントを保存
    document->Save(_dataDir+ outputFileName);
}
```

## ライブ例

[PDF ページ番号を追加](https://products.aspose.app/pdf/page-number)は、ページ番号を追加する機能がどのように機能するかを調査するための無料のオンラインウェブアプリケーションです。

[![C++を使用してPDFにページ番号を追加する方法](page_number.png)](https://products.aspose.app/pdf/page-number)

## ベイツ番号の追加/削除

**ベイツ番号**（ベイツスタンプとも呼ばれる）は、法律、医療、ビジネスの分野で、スキャンや処理される画像やドキュメントに識別番号や日付/時刻のマークを付けるために使用されます。例えば、裁判準備の発見段階やビジネス領収書の識別時に使用されます。このプロセスは、画像やドキュメントの識別、保護、および自動連続番号付けを提供します。

Aspose.PDFは、現時点でベイツ番号のサポートが限られています。この機能は、顧客の要求に応じて更新されます。

### ベイツ番号を削除する方法

```cpp
void WorkingWithPages::RemoveBatesNubmering()
{
    String _dataDir("C:\\Samples\\");
    String inputFileName("BatesNumbering.pdf");
    String outputFileName("BatesNumbering_out.pdf");
    String customSubtype("BatesN");
    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + inputFileName);
    for (auto page : document->get_Pages())
    {
        auto coll = page->get_Artifacts();
        for (auto batesNum : coll)
        {
        if (batesNum->get_CustomSubtype() == customSubtype)
            page->get_Artifacts()->Delete(batesNum);
        }
    }

    // 出力ドキュメントを保存
    document->Save(_dataDir + outputFileName);
}
```