---
title: Aspose.PDF С++ Example
linktitle: Hello World Example
type: docs
weight: 40
url: ja/cpp/hello-world-example/
description: このページは、テキストを含むPDFドキュメントを作成するためのシンプルなプログラミングの使用方法を示しています - Hello World.
lastmod: "2021-11-01"
sitemap:
    changefreq: "monthly"
    priority: 0.6
---

「Hello World」例は、プログラミング言語やソフトウェアの機能をシンプルなユースケースで紹介するために伝統的に使用されます。

Aspose.PDF for C++は、C++アプリケーションにPDFドキュメントの作成、操作、変換機能を組み込むことができる豊富な機能を持つPDF APIです。PDF、XFA、TXT、HTML、PCL、XML、XPS、EPUB、TEXおよび画像ファイル形式を含む多くの一般的なファイル形式での作業をサポートしています。この記事では、「Hello World!」というテキストを含むPDFドキュメントを作成しています。環境にAspose.PDF for C++をインストールした後、以下のコードサンプルを実行して、Aspose.PDF APIの動作を確認できます。

以下のコードスニペットは次の手順に従います：

1. [String クラス](https://reference.aspose.com/pdf/cpp/class/system.string) を作成して、パス名とファイル名を管理します。
1. [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) オブジェクトをインスタンス化します。このステップでは、メタデータはあるがページのない空のPDFドキュメントを作成します。
1. ドキュメントオブジェクトに[Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) を追加します。これで、ドキュメントには1ページが含まれます。
1. 結果のPDFドキュメントを[保存](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/#ac082fe8e67b25685fc51d33e804269fa)します。

以下のコードスニペットは、Aspose.PDF for C++ API の動作を示すHello Worldプログラムです。

```cpp
void ExampleSimple()
{
    // 合成されたパスを保持するバッファー。
    String outputFileName;

    // パス名のための文字列。
    String _dataDir("C:\\Samples\\");

    // ファイル名のための文字列。
    String filename("HelloWorld_out.pdf");

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    // 新しいページにテキストを追加
    auto text = MakeObject<TextFragment>(u"Hello world!");

    auto paragraphs = page->get_Paragraphs();
    paragraphs->Add(text);

    // 更新されたPDFを保存
    outputFileName = _dataDir + filename;

    document->Save(outputFileName);
}
```