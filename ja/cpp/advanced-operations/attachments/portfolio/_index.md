---
title: PDFでポートフォリオを作成する
linktitle: ポートフォリオ
type: docs
weight: 40
url: ja/cpp/portfolio/
description: Aspose.PDF for C++でPDFポートフォリオを作成します。Microsoft Excelファイル、Wordドキュメント、および画像ファイルを使用してPDFポートフォリオを作成する必要があります。
lastmod: "2022-02-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDFポートフォリオの作成方法

Aspose.PDFは、[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)クラスを使用してPDFポートフォリオドキュメントを作成することを可能にします。 [FileSpecification](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.file_specification)クラスで取得した後、Document.Collectionオブジェクトにファイルを追加します。ファイルが追加されたら、DocumentクラスのSaveメソッドを使用してポートフォリオドキュメントを保存します。

以下の例では、Microsoft Excelファイル、Wordドキュメント、および画像ファイルを使用してPDFポートフォリオを作成します。

以下のコードは次のポートフォリオを生成します。

### Aspose.PDFで作成されたPDFポートフォリオ

![A PDF Portfolio created with Aspose.PDF for C++](working-with-pdf-portfolio_1.jpg)

```cpp
void WorkingWithAttachments::CreatePortfolio()
{
    String _dataDir("C:\\Samples\\");

    // Documentオブジェクトをインスタンス化する
    auto pdfDocument = MakeObject<Document>();

    // ドキュメントコレクションオブジェクトをインスタンス化する
    pdfDocument->set_Collection(MakeObject<Collection>());

    // ポートフォリオに追加するファイルを取得する
    auto excel = MakeObject<FileSpecification>(_dataDir + u"HelloWorld.xlsx");
    auto word = MakeObject<FileSpecification>(_dataDir + u"HelloWorld.docx");
    auto image = MakeObject<FileSpecification>(_dataDir + u"sample.jpg");

    // ファイルの説明を提供する
    excel->set_Description(u"Excelファイル");
    word->set_Description(u"Wordファイル");
    image->set_Description(u"画像ファイル");

    // ドキュメントコレクションにファイルを追加する
    pdfDocument->get_Collection()->Add(excel);
    pdfDocument->get_Collection()->Add(word);
    pdfDocument->get_Collection()->Add(image);

    // ポートフォリオドキュメントを保存する
    pdfDocument->Save(_dataDir + u"PDFPortfolio.pdf");
}
```


## PDFポートフォリオからファイルを抽出する

PDFポートフォリオを使用すると、さまざまなソース（例：PDF、Word、Excel、JPEGファイル）からのコンテンツを1つの統一されたコンテナにまとめることができます。元のファイルはそれぞれの個別のアイデンティティを保持しますが、PDFポートフォリオファイルに組み立てられます。ユーザーは各コンポーネントファイルを他のコンポーネントファイルとは独立して開く、読む、編集する、およびフォーマットすることができます。

Aspose.PDFは[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)クラスを使用してPDFポートフォリオドキュメントを作成することを可能にします。また、PDFポートフォリオからファイルを抽出する機能も提供します。

次のコードスニペットは、PDFポートフォリオからファイルを抽出する手順を示しています。

```cpp
void WorkingWithAttachments::ExtractPortfolio()
{
    String _dataDir("C:\\Samples\\");
    // ドキュメントを開く
    auto pdfDocument = MakeObject <Document>(_dataDir + u"PDFPortfolio.pdf");
    // 埋め込みファイルのコレクションを取得
    auto embeddedFiles = pdfDocument->get_EmbeddedFiles();

    // ポートフォリオの個々のファイルを反復処理
    for (auto fileSpecification : embeddedFiles) {
    auto initialStream = fileSpecification->get_Contents();
    auto fileContent = MakeArray<uint8_t>(fileSpecification->get_Contents()->get_Length());
    fileSpecification->get_Contents()->Read(fileContent, 0, fileContent->get_Length());
    auto filename = System::IO::Path::GetFileName(fileSpecification->get_Name());
    // 抽出したファイルを任意の場所に保存
    auto fileStream = System::IO::File::OpenWrite(_dataDir + u"_out_" + filename);
    fileStream->Write(fileContent, 0, fileContent->get_Length());
    // ストリームオブジェクトを閉じる
    fileStream->Close();
    }
}
```

![PDFポートフォリオからファイルを抽出する](working-with-pdf-portfolio_2.jpg)

## PDFポートフォリオからファイルを削除する

PDFポートフォリオからファイルを削除するには、次のコード行を試してください。

```cpp
void WorkingWithAttachments::RemoveFilesFromPDFPortfolio()
{
    String _dataDir("C:\\Samples\\");
    // ソースPDFポートフォリオを読み込む
    auto pdfDocument = MakeObject<Document>(_dataDir + u"PDFPortfolio.pdf");
    pdfDocument->get_Collection()->Delete();
    pdfDocument->Save(_dataDir + u"No_PortFolio_out.pdf");
}
```