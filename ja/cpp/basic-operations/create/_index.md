---
title: C++を使用してPDFドキュメントを作成する
linktitle: 作成
type: docs
weight: 10
url: /ja/cpp/create-document/
description: PDFファイルを操作する際の最も一般的で基本的なタスクは、最初から文書を作成することです。Aspose.PDF for C++ライブラリを使用します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for C++** APIは、C++のアプリケーション開発者がアプリケーションにPDFドキュメントの処理機能を組み込むことを可能にします。これにより、基盤となるマシンに他のソフトウェアをインストールすることなく、PDFファイルの作成と読み取りが可能になります。Aspose.PDF for C++は、QT、MFC、コンソールアプリなど、さまざまなC++アプリケーションタイプで使用することができます。

## C++を使用してPDFファイルを作成する方法

C++を使用してPDFファイルを作成するには、次の手順を使用します。

1. [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) オブジェクトをインスタンス化する
1. ドキュメントオブジェクトに[Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page/)を追加する
1. [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.te_x_fragment/) オブジェクトを作成する
1. ページの [Paragraph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.paragraphs/) コレクションに [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.te_x_fragment/) を追加する
1. 結果として得られる PDF ドキュメントを保存する

```cpp
void CreatePDF() {
    // パス名の文字列。
    String _dataDir("C:\\Samples\\");

    // ファイル名の文字列。
    String filename("sample-new.pdf");

    // ドキュメントオブジェクトを初期化する
    auto document = MakeObject<Document>();
    // ページを追加する
    auto page = document->get_Pages()->Add();

    // 新しいページにテキストを追加する
    auto textFragment = MakeObject<TextFragment>(u"Hello World!");
    page->get_Paragraphs()->Add(textFragment);

    // 更新された PDF を保存する
    String outputFileName = _dataDir + filename;

    document->Save(outputFileName);
}
```