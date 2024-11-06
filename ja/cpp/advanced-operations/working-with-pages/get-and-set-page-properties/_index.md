---
title: ページプロパティの取得と設定
type: docs
weight: 20
url: ja/cpp/get-and-set-page-properties/
description: C++ライブラリを使用してPDFファイルからページプロパティを取得および設定できます。
lastmod: "2021-12-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for C++** を使用すると、C++アプリケーションでPDFファイル内のページのプロパティを読み取り、設定することができます。このセクションでは、PDFファイルのページ数を取得し、色などのPDFページプロパティに関する情報を取得し、ページプロパティを設定し、PDFファイルの特定のページを取得する方法などを示します。

## PDFファイルのページ数を取得する

ドキュメントを扱うとき、多くの場合、それらが何ページ含まれているかを知りたいと思うでしょう。Aspose.PDFを使用すると、これは2行のコードで済みます。

PDFファイルのページ数を取得するには：

1. [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) クラスを使用してPDFファイルを開きます。
1. ドキュメントオブジェクトから[PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection)コレクションのCountプロパティを使用して、ドキュメント内のページの総数を取得します。

次のコードスニペットは、PDFファイルのページ数を取得する方法を示しています。

```cpp
void GetNumberOfPages() {
    // ドキュメントを開く
    String _dataDir("C:\\Samples\\");
    String srcFileName("GetNumberofPages.pdf");

    auto srcDocument = MakeObject<Document>(_dataDir + srcFileName);

    // ページ数を取得
    std::cout << "Page Count : " << srcDocument->get_Pages()->get_Count() << std::endl;
}
```

### ドキュメントを保存せずにページ数を取得する

時々、PDFファイルをフライで生成し、PDFファイルの作成中に、システムやストリーム上でファイルを保存せずにPDFファイルのページ数を取得する必要がある場合があります（目次の作成など）。 この要件に対応するために、Documentクラスに[ProcessParagraphs](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a1773e7b6a887eaddd602073e29939a6f)メソッドが導入されました。ドキュメントを保存せずにページ数を取得する手順を示す以下のコードスニペットをご覧ください。

```cpp
void GetPageCountWithoutSavingTheDocument() {
    // Documentインスタンスをインスタンス化
    auto document = MakeObject<Document>();

    // PDFファイルのページコレクションにページを追加
    auto page = document->get_Pages()->Add();
    // ループインスタンスを作成
    for (int i = 0; i < 300; i++)
        // ページオブジェクトの段落コレクションにTextFragmentを追加
        page->get_Paragraphs()->Add(MakeObject<TextFragment>(u"ページ数テスト"));
    // 正確なページ数を取得するためにPDFファイルの段落を処理
    document->ProcessParagraphs();
    // ドキュメントのページ数を出力
    std::cout << "ドキュメントのページ数 = " << document->get_Pages()->get_Count();
}
```

## ページプロパティを取得する
### ページプロパティへのアクセス

[Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) クラスは、特定のPDFページに関連するすべてのプロパティを提供します。PDFファイルのすべてのページは、[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) オブジェクトの [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) コレクションに含まれています。

そこから、インデックスを使用して個々のPageオブジェクトにアクセスするか、foreachループを使用してコレクションをループしてすべてのページを取得することができます。個々のページにアクセスしたら、そのプロパティを取得できます。次のコードスニペットは、ページプロパティを取得する方法を示しています。

```cpp
void AccessingPageProperties() {

    String _dataDir("C:\\Samples\\");
    String pdfDocument("GetProperties.pdf");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + pdfDocument);

    // 特定のページを取得
    auto pdfPage = document->get_Pages()->idx_get(1);
    // ページプロパティを取得
    Console::WriteLine(u"ArtBox : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_ArtBox()->get_Height(), pdfPage->get_ArtBox()->get_Width(),
        pdfPage->get_ArtBox()->get_LLX(), pdfPage->get_ArtBox()->get_LLY(),
        pdfPage->get_ArtBox()->get_URX(), pdfPage->get_ArtBox()->get_URY());

    Console::WriteLine(u"->get_BleedBox() : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_BleedBox()->get_Height(), pdfPage->get_BleedBox()->get_Width(),
        pdfPage->get_BleedBox()->get_LLX(), pdfPage->get_BleedBox()->get_LLY(),
        pdfPage->get_BleedBox()->get_URX(), pdfPage->get_BleedBox()->get_URY());

    Console::WriteLine(u"get_CropBox() : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_CropBox()->get_Height(), pdfPage->get_CropBox()->get_Width(),
        pdfPage->get_CropBox()->get_LLX(), pdfPage->get_CropBox()->get_LLY(),
        pdfPage->get_CropBox()->get_URX(), pdfPage->get_CropBox()->get_URY());

    Console::WriteLine(u"get_MediaBox() : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_MediaBox()->get_Height(), pdfPage->get_MediaBox()->get_Width(),
        pdfPage->get_MediaBox()->get_LLX(), pdfPage->get_MediaBox()->get_LLY(),
        pdfPage->get_MediaBox()->get_URX(), pdfPage->get_MediaBox()->get_URY());

    Console::WriteLine(u"get_TrimBox() : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_TrimBox()->get_Height(), pdfPage->get_TrimBox()->get_Width(),
        pdfPage->get_TrimBox()->get_LLX(), pdfPage->get_TrimBox()->get_LLY(),
        pdfPage->get_TrimBox()->get_URX(), pdfPage->get_TrimBox()->get_URY());

    Console::WriteLine(u"Rect : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_Rect()->get_Height(), pdfPage->get_Rect()->get_Width(),
        pdfPage->get_Rect()->get_LLX(), pdfPage->get_Rect()->get_LLY(),
        pdfPage->get_Rect()->get_URX(), pdfPage->get_Rect()->get_URY());

    Console::WriteLine(u"Page Number : {0}", pdfPage->get_Number());
    Console::WriteLine(u"Rotate : {0}", pdfPage->get_Rotate());
}
```