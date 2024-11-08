---
title: PDFからテーブルのデータを抽出する 
linktitle: テーブルからデータを抽出する
type: docs
weight: 40
url: /ja/cpp/extract-data-from-table-in-pdf/
description: Aspose.PDF for C++を使用してPDFから表形式のデータを抽出する方法を学びます。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## プログラムでPDFからテーブルを抽出する

PDFは文書交換の最も一般的な形式であるため、分析が必要な複数のデータセットを含む文書を考えてみましょう。この記事では、PDFからテーブルを抽出する方法について説明します。

**Aspose.PDF for C++** は、開発者がPDFドキュメント内のテーブルからデータを抽出するために必要なツールを提供します。

この例は、PDFファイル内のテーブルから表形式のデータを取得するための[TableAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber)クラスの使用を示しています。

次の例は、すべてのページからのテーブル抽出を示しています：

```cpp
void ExtractTable() {
    std::clog << __func__ << ": Start" << std::endl;
    // パス名用の文字列
    String _dataDir("C:\\Samples\\Parsing\\");

    // ファイル名用の文字列
    String infilename("sample-table.pdf");


    auto document = MakeObject<Document>(_dataDir + infilename);
    auto absorber = MakeObject<TableAbsorber>();

    // ページをスキャン
    for (auto page : document->get_Pages()) {
        absorber->Visit(page);
        for (auto table : absorber->get_TableList()) {
        std::cout << "Table" << std::endl;
        // 行のリストを反復処理
        for (auto row : table->get_RowList()) {
            // セルのリストを反復処理
            for (auto cell : row->get_CellList()) {
                String sb;
                for (auto fragment : cell->get_TextFragments()) {
                sb += fragment->get_Text();
                }
                std::cout << sb << "|";
            }
            std::cout << std::endl;
        }
        }
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## PDFページの特定のエリアからテーブルを抽出する

各吸収されたテーブルは、ページ上のテーブルの位置を示す[Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.rectangle/)プロパティを持っています。

したがって、特定の領域にあるテーブルを抽出する必要がある場合は、特定の座標を使用する必要があります。

次の例は、正方形の注釈でマークされたテーブルを抽出する方法を示しています：

```cpp
void ExtractMarkedTable()
{
    std::clog << __func__ << ": Start" << std::endl;
    // パス名のための文字列
    String _dataDir("C:\\Samples\\Parsing\\");

    // ファイル名のための文字列
    String infilename("sample-table.pdf");


    auto document = MakeObject<Document>(_dataDir + infilename);
    auto absorber = MakeObject<TableAbsorber>();

    auto page = document->get_Pages()->idx_get(1);
    auto sqa = MakeObject<Aspose::Pdf::Annotations::SquareAnnotation>(page, Rectangle::get_Trivial());
    auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(sqa);


    auto list = annotationSelector->get_Selected();
    if (list->get_Count() == 0) {
        std::cerr << "Marked tables not found.." << std::endl;
        return;
    }

    auto squareAnnotation = System::DynamicCast<Aspose::Pdf::Annotations::SquareAnnotation>(list->idx_get(1));

    absorber->Visit(page);

    for (auto table : absorber->get_TableList())
    {
        auto isInRegion =
        (squareAnnotation->get_Rect()->get_LLX() < table->get_Rectangle()->get_LLX()) &&
        (squareAnnotation->get_Rect()->get_LLY() < table->get_Rectangle()->get_LLY()) &&
        (squareAnnotation->get_Rect()->get_URX() > table->get_Rectangle()->get_URX()) &&
        (squareAnnotation->get_Rect()->get_URY() > table->get_Rectangle()->get_URY());

        if (isInRegion)
        {
        for (auto row : table->get_RowList()) {
            // セルのリストを反復処理する
            for (auto cell : row->get_CellList()) {
                String sb;
                for (auto fragment : cell->get_TextFragments()) {
                sb += fragment->get_Text();
                }
                std::cout << sb << "|";
            }
            std::cout << std::endl;
        }
        }
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## PDFからテーブルデータを抽出してCSVファイルに保存

以下の例は、テーブルを抽出してCSVファイルとして保存する方法を示しています。
PDFをExcelスプレッドシートに変換する方法については、[PDFをExcelに変換](/pdf/ja/cpp/convert-pdf-to-excel/)の記事を参照してください。

```cpp
void ExtractTableSaveCSV()
{
    std::clog << __func__ << ": Start" << std::endl;
    // パス名のための文字列
    String _dataDir("C:\\Samples\\Parsing\\");

    // ファイル名のための文字列
    String infilename("sample-table.pdf");
    String outfilename("PDFToXLS_out.csv");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + infilename);

    // ExcelSaveオプションオブジェクトをインスタンス化
    auto excelSave = MakeObject<ExcelSaveOptions>();
    excelSave->set_Format(ExcelSaveOptions::ExcelFormat::CSV);

    // 出力をXLS形式で保存
    document->Save(_dataDir + outfilename, excelSave);
    std::clog << __func__ << ": Finish" << std::endl;
}
```