---
title: PDFページサイズをプログラムで変更する
linktitle: PDFページサイズの変更
type: docs
weight: 40
url: /ja/cpp/change-page-size/
description: C++ライブラリを使用してPDFファイルのページサイズを変更します。
lastmod: "2021-12-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDFは静的レイアウトの印刷可能な形式であり、そのためビジネスライフで広く普及しています。

しかし、ページサイズが用紙サイズよりも大きい場合には、PDFドキュメントのサイズを変更する必要があることがあります。でも、どうすればいいのでしょうか？

心配しないでください。このページでは、課題を解決する方法を見つけることができます。

しかしまず、ページサイズシリーズがあることを思い出してみましょう。

世界で広く採用されている2つのページサイズシリーズがあります。
もちろん、多くのフォーマットがありますが、最も一般的に使用されているものがあります。
最初のものはISOペーパーサイズです。 シリーズA4は標準印刷および文房具に使用されます。レターサイズの用紙はポスター、ウォールチャートなどに使用されます。アメリカ合衆国、カナダ、および一部のメキシコは第2のページサイズシリーズを採用し、今日ではISO標準の用紙サイズがまだ広く使用されていない唯一の工業国です。

では、Aspose.PDFがC++ライブラリを使用してページサイズを変更するように促す方法を見てみましょう。

## PDFページサイズを変更する

Aspose.PDF for C++を使用すると、C++アプリケーションで簡単なコード行によってPDFページサイズを変更できます。このトピックでは、既存のPDFファイルのページ寸法（サイズ）を更新/変更する方法を説明します。

[Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page)クラスには、ページサイズを設定できるSetPageSize(...)メソッドが含まれています。以下のコードスニペットは、いくつかの簡単な手順でページ寸法を更新します：

1. ソースPDFファイルをロードします。
1. ページを[PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection)オブジェクトに取得します。
1. 指定されたページを取得します。 SetPageSize(..) メソッドを呼び出して、寸法を更新します。
1. [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) クラスの Save(..) メソッドを呼び出して、ページ寸法が更新された PDF ファイルを生成します。

次のコードスニペットは、PDF ページの寸法を A4 サイズに変更する方法を示しています。

```cpp
void ChangePageSize() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("UpdateDimensions.pdf");
    String outputFileName("UpdateDimensions_out.pdf");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // 特定のページを取得
    auto pdfPage = document->get_Pages()->idx_get(1);

    // ページサイズを A4 (11.7 x 8.3 インチ) に設定し、Aspose.Pdf では 1 インチ = 72 ポイント
    // したがって、ポイントでの A4 寸法は (842.4, 597.6) になります
    pdfPage->SetPageSize(597.6, 842.4);
    // 更新されたドキュメントを保存
    document->Save(_dataDir + outputFileName);
}
```

## PDF ページサイズを取得する

Aspose.PDF for C++ を使用して、既存の PDF ファイルのページサイズを読み取ることができます。 以下のコードサンプルは、C++を使用してPDFページの寸法を読み取る方法を示しています。

```cpp
void GetPDFPageSize() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("UpdateDimensions.pdf");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // 特定のページを取得
    auto page = document->get_Pages()->idx_get(1);

    // ページの高さと幅の情報を取得
    Console::WriteLine(u"{0} {1}", page->GetPageRect(true)->get_Width(), page->GetPageRect(true)->get_Height());
    // ページを90度回転させる
    page->set_Rotate(Rotation::on90);
    // ページの高さと幅の情報を取得
    Console::WriteLine(u"{0} {1}", page->GetPageRect(true)->get_Width(), page->GetPageRect(true)->get_Height());

}
```