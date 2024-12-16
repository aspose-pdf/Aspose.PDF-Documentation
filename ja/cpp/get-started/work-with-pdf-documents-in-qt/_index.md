---
title: QtでPDFドキュメントを操作する
type: docs
weight: 130
url: /ja/cpp/work-with-pdf-documents-in-qt/
lastmod: "2021-11-01"
---

Qtは、さまざまなデスクトップ、モバイル、Web、組み込みシステムアプリケーションを作成できるクロスプラットフォームアプリケーション開発フレームワークです。この記事では、QtアプリケーションでPDFドキュメントを操作するために、C++ PDFライブラリを統合する方法を紹介します。

## QtでAspose.PDF for C++を使用する

WindowsオペレーティングシステムのQtアプリケーションでAspose.PDF for C++を使用するには、[ダウンロード](https://downloads.aspose.com/pdf/cpp)セクションからAPIの最新バージョンをダウンロードします。APIをダウンロードしたら、次のいずれかのオプションを使用してQtで使用できます。

- Qt Creatorを使用する
- Visual Studioを使用する

ここでは、Qt Creatorを使用してQtコンソールアプリケーション内でAspose.PDF for C++を統合して使用する方法を示します。

### Qtコンソールアプリケーションを作成する

{{% alert color="primary" %}}

この記事では、Qt開発環境とQt Creatorが正しくインストールされていることを前提としています。

{{% /alert %}}

- Qt Creatorを開き、新しい*Qt Console Application*を作成します。

![todo:image_alt_text](https://blog.aspose.com/wp-content/uploads/sites/2/2020/04/Qt-Console-Application.jpg)

- *Build System*のドロップダウンからQMakeオプションを選択します。

![todo:image_alt_text](https://blog.aspose.com/wp-content/uploads/sites/2/2020/04/Qt-Console-Application-QMake.jpg)

- 適切なキットを選択して、ウィザードを終了します。

この時点で、問題なくコンパイルできる実行可能なQt Console Applicationが作成されているはずです。

### Aspose.PDF for C++ APIをQtに統合する

- 以前にダウンロードしたAspose.PDF for C++アーカイブを抽出します
- 抽出されたAspose.PDF for C++パッケージから*Aspose.Pdf.Cpp*と*CodePorting.Native.Cs2Cpp_vc14_20.4*フォルダをプロジェクトのルートにコピーします。プロジェクトは次の画像のようになります。

![todo:image_alt_text](work-with-pdf-documents-in-qt_1.png)

- libフォルダとincludeフォルダへのパスを追加するために、LHSパネルでプロジェクトを右クリックし、*Add Library*を選択します。

![todo:image_alt_text](https://blog.aspose.com/wp-content/uploads/sites/2/2020/04/Add-Word-Library.jpg)

- 外部ライブラリオプションを選択し、パスを参照してlibフォルダーを一つずつ含めます。

![todo:image_alt_text](https://blog.aspose.com/wp-content/uploads/sites/2/2020/04/Add-Word-Library-2.jpg)

- 完了すると、.proプロジェクトファイルに次のエントリが含まれます。

![todo:image_alt_text](work-with-pdf-documents-in-qt_2.png)

- アプリケーションをビルドし、統合が完了します。

### QtでPDFドキュメントを作成する

Aspose.PDF for C++がQtに統合されたので、テキストを含むPDFドキュメントを作成し、ディスクに保存する準備が整いました。これを行うには：

- main.cppに次のヘッダーを含めます

```cpp

    #include "Aspose.PDF.Cpp/Document.h"
    #include "Aspose.PDF.Cpp/Page_.h"
    #include "Aspose.PDF.Cpp/PageCollection.h"
    #include "Aspose.PDF.Cpp/Generator/Paragraphs.h"
    #include "Aspose.PDF.Cpp/Text/TextFragment.h"
```

- PDFドキュメントを生成してディスクに保存するために、main関数に次のコードを挿入します

```cpp

    using namespace System;
    using namespace Aspose::Pdf;
    using namespace Aspose::Pdf::Text;
    
    QString text = "こんにちは世界";
    auto doc = MakeObject<Document>();

    auto pages = doc->get_Pages();

    pages->Add();

    auto page = pages->idx_get(1);

    auto paragraps = page->get_Paragraphs();

    paragraps->Add(MakeObject<TextFragment>(text.toStdU16String().c_str()));

    doc->Save(file_name.toStdU16String().c_str());
```