---
title: PDFにテーブルを作成または追加する
linktitle: テーブルを作成または追加する
type: docs
weight: 10
url: /cpp/add-table-in-existing-pdf-document/
description: Aspose.PDF for C++はPDFテーブルを作成、読み取り、編集するためのライブラリです。このライブラリを使用すると、C++を使用してPDFページにテーブルをページングできます。
lastmod: "2021-11-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## C++を使用してテーブルを作成する

PDFドキュメントを扱う際、テーブルは重要です。情報を体系的に表示するための優れた機能を提供します。

PDFドキュメント内のテーブルは、データを行と列に体系的に整理します。Aspose.PDF for C++ APIを使用すると、PDFドキュメントにテーブルを追加し、C++アプリケーションでそれに行と列を追加できます。[Table](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.table/)クラスは、ドキュメントにテーブルを追加するために使用されます。C++を使用してPDFドキュメントにテーブルを追加するには、次の手順を実行します。

### 既存のPDFドキュメントにテーブルを追加する

Aspose.PDF for C++を使用して既存のPDFファイルにテーブルを追加するには、次の手順を実行します。

1. ソースファイルをロードします。
1. テーブルを初期化し、その列と行を設定します。
1. テーブル設定を行います（境界線を設定しました）。
1. テーブルにデータを入力します。
1. テーブルをページに追加します。
1. ファイルを保存します。

以下のコードスニペットは、既存のPDFファイルにテキストを追加する方法を示しています。

>Headers

```cpp
#include <system/date_time.h>
#include <system/io/file.h>
#include <system/console.h>
#include <data/data_table.h>
#include <data/data_column_collection.h>
#include <system/type_info.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Generator/BorderSide.h>
#include <Aspose.PDF.Cpp/Generator/BorderInfo.h>
#include <Aspose.PDF.Cpp/Generator/PageInfo.h>
#include <Aspose.PDF.Cpp/Generator/MarginInfo.h>
#include <Aspose.PDF.Cpp/Generator/GraphInfo.h>
#include <Aspose.PDF.Cpp/Generator/BorderCornerStyle.h>
#include <Aspose.PDF.Cpp/Generator/ColumnAdjustment.h>
#include <Aspose.PDF.Cpp/Generator/ImageFileType.h>
#include <Aspose.PDF.Cpp/Generator/Image.h>
#include <Aspose.PDF.Cpp/Generator/HtmlFragment.h>

#include <Aspose.PDF.Cpp/Text/TextFragment.h>

#include <Aspose.PDF.Cpp/Color.h>

#include <Aspose.PDF.Cpp/Table/Table.h>
#include <Aspose.PDF.Cpp/Table/Row.h>
#include <Aspose.PDF.Cpp/Table/Rows.h>
#include <Aspose.PDF.Cpp/Table/Cell.h>
#include <Aspose.PDF.Cpp/Table/Cells.h>
```

>サンプル

```cpp
using namespace System;
using namespace Aspose::Pdf;

void AddingTableInExistingPDFDocument() {
    
    String _dataDir("C:\\Samples\\");
    
    // ソースPDFドキュメントを読み込む
    auto document = MakeObject<Document>(_dataDir + u"AddTable.pdf");
    
    // Tableの新しいインスタンスを初期化
    auto table = MakeObject<Table>();
    
    // テーブルの境界線の色をLightGrayに設定
    table->set_Border(MakeObject<Aspose::Pdf::BorderInfo>(
        Aspose::Pdf::BorderSide::All, .5f, 
        Aspose::Pdf::Color::get_LightGray()));
    // テーブルセルの境界線を設定
    table->set_DefaultCellBorder (MakeObject<Aspose::Pdf::BorderInfo>(
        Aspose::Pdf::BorderSide::All, .5f, 
        Aspose::Pdf::Color::get_LightGray()));

    // 10行を追加するループを作成
    for (int row_count = 1; row_count < 10; row_count++)
    {
        // テーブルに行を追加
        auto row = table->get_Rows()->Add();
        // テーブルセルを追加
        row->get_Cells()->Add(String::Format(u"Column ({0}, 1)", row_count));
        row->get_Cells()->Add(String::Format(u"Column ({0}, 2)", row_count));
        row->get_Cells()->Add(String::Format(u"Column ({0}, 3)", row_count));
    }

    // テーブルオブジェクトを入力ドキュメントの最初のページに追加
    document->get_Pages()->idx_get(1)->get_Paragraphs()->Add(table);
    
    // テーブルオブジェクトを含む更新されたドキュメントを保存
    document->Save(_dataDir + u"document_with_table_out.pdf");
}
```

### ColSpanとRowSpanを使用した表

Aspose.PDF for C++は、表の列を結合するための[ColSpan](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.cell#ae79c581d2245258699c98617e78c01d1)プロパティと、行を結合するための[RowSpan](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.cell#a4eb7337d118314e6c2180670fb32721a)プロパティを提供しています。

[Cell](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.cell)オブジェクトに[ColSpan](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.cell#ae79c581d2245258699c98617e78c01d1)または[RowSpan](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.cell#a4eb7337d118314e6c2180670fb32721a)プロパティを使用して、表のセルを作成します。必要なプロパティを適用した後、作成されたセルを表に追加することができます。

```cpp
void AddTable_RowColSpan()
{
    String _dataDir("C:\\Samples\\");

    // 元のPDFドキュメントをロード
    auto document = MakeObject<Document>();
    document->get_Pages()->Add();

    // Tableの新しいインスタンスを初期化
    auto table = MakeObject<Table>();
    // 表の境界線の色をLightGrayに設定
    table->set_Border(MakeObject<Aspose::Pdf::BorderInfo>(
        Aspose::Pdf::BorderSide::All, .5f, 
        Color::get_Black()));
    // 表のセルの境界線を設定
    table->set_DefaultCellBorder(
        MakeObject<Aspose::Pdf::BorderInfo>(
            Aspose::Pdf::BorderSide::All, .5f, 
            Color::get_Black()));
    

    // 1行目を表に追加
    auto row1 = table->get_Rows()->Add();
    for (int cellCount = 1; cellCount < 5; cellCount++)
    {
        // 表のセルを追加
        row1->get_Cells()->Add(String::Format(u"Test 1 {0}", cellCount));
    }

    // 2行目を表に追加
    auto row2 = table->get_Rows()->Add();
    row2->get_Cells()->Add(u"Test 2 1");
    auto cell = row2->get_Cells()->Add(u"Test 2 2");
    cell->set_ColSpan(2);
    row2->get_Cells()->Add(u"Test 2 4");

    // 3行目を表に追加
    auto row3 = table->get_Rows()->Add();
    row3->get_Cells()->Add(u"Test 3 1");
    row3->get_Cells()->Add(u"Test 3 2");
    row3->get_Cells()->Add(u"Test 3 3");
    row3->get_Cells()->Add(u"Test 3 4");

    // 4行目を表に追加
    auto row4 = table->get_Rows()->Add();
    row4->get_Cells()->Add(u"Test 4 1");
    cell = row4->get_Cells()->Add(u"Test 4 2");
    cell->set_RowSpan (2);
    row4->get_Cells()->Add(u"Test 4 3");
    row4->get_Cells()->Add(u"Test 4 4");


    // 5行目を表に追加
    auto row5 = table->get_Rows()->Add();
    row5->get_Cells()->Add(u"Test 5 1");
    row5->get_Cells()->Add(u"Test 5 3");
    row5->get_Cells()->Add(u"Test 5 4");

    // 表オブジェクトを入力ドキュメントの最初のページに追加
    document->get_Pages()->idx_get(1)->get_Paragraphs()->Add(table);

    // 表オブジェクトを含む更新されたドキュメントを保存
    document->Save(_dataDir + u"document_with_table_out.pdf");
}
```

コードの実行結果は、次の画像に示されている表です：

![ColSpan and RowSpan demo](colspan_rowspan.png)

## 境界線、余白、パディングの操作

表の境界線、余白、セルのパディングを設定する機能もサポートしていることに注意してください。まず、境界線、余白、パディングの概念を理解しましょう。以下の図に示されています：

![Borders, margins and padding](set-border-style-margins-and-padding-of-table_1.png)

図を詳細に確認してください。表、行、およびセルの境界線が重なっていることを示しています。Aspose.PDF for C++ を使用すると、表には余白があり、セルはインデントすることができます。セルの余白を設定するには、セルのパディングを設定する必要があります。

## 境界線

Table、[Row](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.row) および [Cell](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.cell) オブジェクトの境界線を設定するには、Table.Border、Row.Border および Cell.Border プロパティを使用します。 セル境界線は、[Table](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.table)またはRowクラスのDefaultCellBorderプロパティを使用して設定することもできます。上記で説明したすべての境界線関連プロパティは、コンストラクターを呼び出すことによって作成されたRowクラスのインスタンスに割り当てられます。Rowクラスには、境界線をカスタマイズするために必要なほとんどすべてのパラメーターを受け取る多くのオーバーロードがあります。

## マージンまたはパディング

セルのパディングは、Tableクラスの[DefaultCellPadding](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.table#ac64196de6dfed7550c3278892ed9dbe0)プロパティを使用して管理できます。すべてのパディング関連プロパティは、カスタムマージンを作成するために`Left`、`Right`、`Top`、および`Bottom`パラメーターに関する情報を受け取る[MarginInfo](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.margin_info/)クラスのインスタンスに割り当てられます。

![PDFテーブルのマージンと境界線](margin-border.png)

```cpp
void AddTable_MergingPadding() {

    String _dataDir("C:\\Samples\\");

    // 空のコンストラクタを呼び出してDocumentオブジェクトをインスタンス化
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    // テーブルオブジェクトをインスタンス化
    auto tab1 = MakeObject<Table>();
    // 目的のセクションの段落コレクションにテーブルを追加
    page->get_Paragraphs()->Add(tab1);
    // テーブルの列幅を設定
    tab1->set_ColumnWidths (u"50 50 50");
    // BorderInfoオブジェクトを使用してデフォルトのセル境界線を設定
    tab1->set_DefaultCellBorder (
        MakeObject<Aspose::Pdf::BorderInfo>(
            Aspose::Pdf::BorderSide::All, 0.1F));
    // 別のカスタマイズされたBorderInfoオブジェクトを使用してテーブル境界線を設定
    tab1->set_Border (
        MakeObject<Aspose::Pdf::BorderInfo>(
            Aspose::Pdf::BorderSide::All, 1.0F));

    // MarginInfoオブジェクトを作成し、左、下、右、および上のマージンを設定
    auto margin = MakeObject<MarginInfo>();
    margin->set_Top (5.0f);
    margin->set_Left (5.0f);
    margin->set_Right (5.0f);
    margin->set_Bottom (5.0f);

    // MarginInfoオブジェクトにデフォルトのセルパディングを設定
    tab1->set_DefaultCellPadding (margin);
    // テーブルに行を作成し、その行にセルを作成
    auto row1 = tab1->get_Rows()->Add();
    row1->get_Cells()->Add(u"col1");
    row1->get_Cells()->Add(u"col2");
    row1->get_Cells()->Add();

    auto mytext = MakeObject<Aspose::Pdf::Text::TextFragment>(u"col3 with large text string");
        
    row1->get_Cells()->idx_get(2)->get_Paragraphs()->Add(mytext);
    row1->get_Cells()->idx_get(2)->set_IsWordWrapped(false);
    

    auto row2 = tab1->get_Rows()->Add();
    row2->get_Cells()->Add(u"item1");
    row2->get_Cells()->Add(u"item2");
    row2->get_Cells()->Add(u"item3");
    
    // Pdfを保存
    document->Save(_dataDir + u"MarginsOrPadding_out.pdf");
}
```
テーブルに丸い角を持たせるには、[BorderInfo](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.border_info)クラスの[RoundedBorderRadius](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.border_info#a6a2bed69dd034fba9ce439dcbe1fd3de)値を使用し、テーブルの角のスタイルを丸く設定します。

```cpp
void AddTable_RoundedBorderRadius()
{
    // ドキュメントディレクトリへのパス。
    String _dataDir("C:\\Samples\\");

    auto tab1 = MakeObject<Aspose::Pdf::Table>();

    auto graph = MakeObject<GraphInfo>();
    graph->set_Color(Color::get_Red());
    // 空のBorderInfoオブジェクトを作成
    auto bInfo = MakeObject<BorderInfo>(BorderSide::All, graph);

    // 丸みの半径が15の丸い境界を設定
    bInfo->set_RoundedBorderRadius(15);
    // テーブルの角スタイルを丸く設定
    tab1->set_CornerStyle (Aspose::Pdf::BorderCornerStyle::Round);
    // テーブルの境界情報を設定
    tab1->set_Border(bInfo);
}
```

### ColumnAdjustmentType列挙型のAutoFitToWindowプロパティ

```cpp
void AddTable_AutoFitToWindow() {
    
    // ドキュメントディレクトリへのパス。
    String _dataDir("C:\\Samples\\");

    // 空のコンストラクタを呼び出してPdfオブジェクトをインスタンス化する
    auto document = MakeObject<Document>();

    // Pdfオブジェクトにセクションを作成する
    auto sec1 = document->get_Pages()->Add();

    // テーブルオブジェクトをインスタンス化する
    auto tab1 = MakeObject<Aspose::Pdf::Table>();
    // 目的のセクションの段落コレクションにテーブルを追加する
    sec1->get_Paragraphs()->Add(tab1);

    // テーブルの列幅を設定する
    tab1->set_ColumnWidths (u"50 50 50");
    tab1->set_ColumnAdjustment (ColumnAdjustment::AutoFitToWindow);

    // BorderInfoオブジェクトを使用してデフォルトのセル境界を設定する
    tab1->set_DefaultCellBorder(MakeObject<BorderInfo>(Aspose::Pdf::BorderSide::All, 0.1F));

    // 別のカスタマイズされたBorderInfoオブジェクトを使用してテーブル境界を設定する
    tab1->set_Border (MakeObject<BorderInfo>(Aspose::Pdf::BorderSide::All, 1.0F));

    // MarginInfoオブジェクトを作成し、その左、下、右、上のマージンを設定する
    auto margin = MakeObject<MarginInfo>();
    margin->set_Top(5.0f);
    margin->set_Left(5.0f);
    margin->set_Right(5.0f);
    margin->set_Bottom(5.0f);

    // MarginInfoオブジェクトにデフォルトのセルパディングを設定する
    tab1->set_DefaultCellPadding(margin);

    // テーブル内に行を作成し、その後に行内にセルを作成する
    auto row1 = tab1->get_Rows()->Add();
    row1->get_Cells()->Add(u"col1");
    row1->get_Cells()->Add(u"col2");
    row1->get_Cells()->Add(u"col3");

    auto row2 = tab1->get_Rows()->Add();
    row2->get_Cells()->Add(u"item1");
    row2->get_Cells()->Add(u"item2");
    row2->get_Cells()->Add(u"item3");
    
    // テーブルオブジェクトを含む更新されたドキュメントを保存する
    document->Save(_dataDir + u"AutoFitToWindow_out.pdf");
}
```

### テーブルの幅を取得

テーブルの幅を動的に取得する必要があるタスクがあります。[Aspose.PDF.Table](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.table) クラスにはこの目的のための [GetWidth] メソッドがあります (https://reference.aspose.com/pdf/cpp/class/aspose.pdf.table#a3361cc8d4af87eec2e3da616c474ac1c)。例えば、テーブルの列の幅を明示的に設定しておらず、[ColumnAdjustment] (https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#afc01382935026dd569c96d77d09dc3a4) を AutoFitToContent に設定していない場合、この場合、次のテーブルの幅を取得できます。

```cpp
void GetTableWidth() {
    // 新しいドキュメントを作成
    auto document = MakeObject<Document>();
    
    // ドキュメントにページを追加
    auto page = document->get_Pages()->Add();

    // 新しいテーブルを初期化
    auto table = MakeObject<Table>();
    table->set_ColumnAdjustment(ColumnAdjustment::AutoFitToContent);
    
    // テーブルに行を追加
    auto row = table->get_Rows()->Add();

    // テーブルにセルを追加
    auto cell = row->get_Cells()->Add(u"Cell 1 text");
    cell = row->get_Cells()->Add(u"Cell 2 text");
    // テーブルの幅を取得
    Console::WriteLine(table->GetWidth());
}
```

## テーブルセルにSVG画像を追加

Aspose.PDF for C++は、PDFファイルにテーブルセルを追加することができます。テーブルを作成する際に、セルにテキストや画像を追加できます。さらに、APIはSVGファイルをPDFに変換する機能も提供しています。これらの機能を組み合わせることで、SVG画像を読み込み、テーブルセルに追加することが可能です。

以下のコードスニペットは、テーブルをインスタンス化し、SVG画像をテーブルセルに追加する手順を示しています。

```cpp
void InsertSVGObject() 
{
    String _dataDir("C:\\Samples\\");

    // Documentオブジェクトをインスタンス化
    auto document = MakeObject<Document>();
    // 画像インスタンスを作成
    auto img = MakeObject<Aspose::Pdf::Image>();

    // 画像タイプをSVGに設定
    img->set_FileType(Aspose::Pdf::ImageFileType::Svg);
    // ソースファイルのパス
    img->set_File (_dataDir + u"SVGToPDF.svg");
    // 画像インスタンスの幅を設定
    img->set_FixWidth (50);
    // 画像インスタンスの高さを設定
    img->set_FixHeight(50);
    // テーブルインスタンスを作成
    auto table = MakeObject<Aspose::Pdf::Table>();
    // テーブルセルの幅を設定
    table->set_ColumnWidths (u"100 100");
    // 行オブジェクトを作成し、テーブルインスタンスに追加
    auto row = table->get_Rows()->Add();
    // セルオブジェクトを作成し、行インスタンスに追加
    auto cell = row->get_Cells()->Add();
    // テキストフラグメントをセルオブジェクトの段落コレクションに追加
    cell->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(u"First cell"));
    // 行オブジェクトに別のセルを追加
    cell = row->get_Cells()->Add();
    // 最近追加されたセルインスタンスの段落コレクションにSVG画像を追加
    cell->get_Paragraphs()->Add(img);
    // ページオブジェクトを作成し、ドキュメントインスタンスのページコレクションに追加
    auto page = document->get_Pages()->Add();
    // ページオブジェクトの段落コレクションにテーブルを追加
    page->get_Paragraphs()->Add(table);    
    // PDFファイルを保存
    document->Save(_dataDir + u"AddSVGObject_out.pdf");
}
```

## テーブル内でのHTMLタグの使用

いくつかのタスクでは、データベースの内容をいくつかのHTMLタグと共にインポートし、その内容をTableオブジェクトにインポートする必要があります。内容をインポートする際には、HTMLタグがPDFドキュメント内に表示される必要があります。

以下のコードスニペットでは、テーブルの枠線の色を設定し、テーブルセルの枠線を設定することができます。その後、10行を追加するループを作成します。入力ドキュメントの最初のページにテーブルオブジェクトを追加し、更新されたドキュメントを保存します。

```cpp
void AddHTMLFragmentToTableCell() {
    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>(_dataDir + u"input.pdf");    
    // Initializes a new instance of the Table
    auto table = MakeObject<Table>();
    // Set the table border color as LightGray
    table->set_Border(new BorderInfo(BorderSide::All, .5f, Color::get_LightGray()));
    // set the border for table cells
    table->set_DefaultCellBorder(new BorderInfo(BorderSide::All, .5f, Color::get_LightGray()));
    // create a loop to add 10 rows       
    for (int row_count = 1; row_count < 10; row_count++) {
        SmartPtr<Cell> cell;
        // add row to table
        auto row = table->get_Rows()->Add();
        // add table cells
        cell = row->get_Cells()->Add();
        cell->get_Paragraphs()->Add(new HtmlFragment(String::Format(u"Column <strong>({0}, 1)</strong>", row_count)));

        cell = row->get_Cells()->Add();
        cell->get_Paragraphs()->Add(new HtmlFragment(String::Format(u"Column <span style='color:red'>({0}, 2)</span>",row_count)));

        cell = row->get_Cells()->Add();
        cell->get_Paragraphs()->Add(new HtmlFragment(String::Format(u"Column <span style='text-decoration: underline'>([0}, 3)</span>", row_count)));
    }
    // Add table object to first page of input document
    document->get_Pages()->idx_get(1)->get_Paragraphs()->Add(table);
    // Save updated document containing table object
    document->Save(_dataDir + u"AddHTMLObject_out.pdf");
}
```

## テーブルの行間にページ区切りを挿入する

通常、PDF内でテーブルを作成する際、テーブルがページの下部マージンに達すると次のページに流れます。しかし、特定の行数がテーブルに追加されたときにページ区切りを強制的に挿入する必要がある場合があります。以下のコードスニペットは、テーブルに10行を追加する際にページ区切りを挿入する手順を示しています。

以下のコードスニペットは、テーブルに10行が追加されたときにページ区切りを挿入する手順を示しています。

```cpp
void InsertPageBreak() {
    String _dataDir("C:\\Samples\\");

    // Documentインスタンスを作成
    auto document = MakeObject<Document>();
    
    // PDFファイルのページコレクションにページを追加
    auto page = document->get_Pages()->Add();

    // テーブルインスタンスを作成
    auto tab = MakeObject<Table>();

    // テーブルの境界スタイルを設定
    tab->set_Border(MakeObject<BorderInfo>(BorderSide::All, Color::get_Red()));
    // 境界色を赤にしてテーブルのデフォルト境界スタイルを設定
    tab->set_DefaultCellBorder(MakeObject<BorderInfo>(BorderSide::All, Color::get_Red()));
    // テーブルの列幅を指定
    tab->set_ColumnWidths(u"100 100");

    // テーブルに200行を追加するループを作成
    for (int counter = 0; counter <= 200; counter++) {
        auto row = MakeObject<Row>();
        tab->get_Rows()->Add(row);
        auto cell1 = MakeObject<Cell>();
        cell1->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(String::Format(u"Cell {0}, 0", counter)));
        row->get_Cells()->Add(cell1);

        auto cell2 = new Cell();
        cell2->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(String::Format(u"Cell {0}, 1", counter)));
        row->get_Cells()->Add(cell2);
        // 10行が追加されるたびに、新しいページに新しい行をレンダリング
        if (counter % 10 == 0 && counter != 0)
            row->set_IsInNewPage(true);
    }
    // PDFファイルの段落コレクションにテーブルを追加
    page->get_Paragraphs()->Add(tab);

    // PDFドキュメントを保存
    document->Save(_dataDir + u"InsertPageBreak_out.pdf");
}
```

## 新しいページにテーブルをレンダリングする

デフォルトでは、段落はページオブジェクトのParagraphsコレクションに追加されます。しかし、ページ上の以前に追加された段落レベルオブジェクトの直後ではなく、新しいページにテーブルをレンダリングすることも可能です。

### サンプル: C++を使用して新しいページにテーブルをレンダリングする方法

新しいページにテーブルをレンダリングするには、[BaseParagraph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.base_paragraph)クラスの[IsInNewPage](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.base_paragraph#a614946048d22afb9dce4cd42346c7561)プロパティを使用します。以下のコードスニペットはその方法を示しています。

```cpp
void RenderTableOnNewPage()
{
    auto document = MakeObject<Document>();
    auto pageInfo = document->get_PageInfo();
    auto marginInfo = pageInfo->get_Margin();

    marginInfo->set_Left (37);
    marginInfo->set_Right (37);
    marginInfo->set_Top (37);
    marginInfo->set_Bottom (37);

    pageInfo->set_IsLandscape(true);

    auto table = MakeObject<Aspose::Pdf::Table>();
    table->set_ColumnWidths(u"50 100");
    // ページを追加
    auto curPage = document->get_Pages()->Add();
    for (int i = 1; i <= 120; i++)
    {
        auto row = table->get_Rows()->Add();
        row->set_FixedRowHeight(15);
        auto cell1 = row->get_Cells()->Add();
        cell1->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(u"Content 1"));
        auto cell2 = row->get_Cells()->Add();
        cell2->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(u"HHHHH"));
    }
    auto paragraphs = curPage->get_Paragraphs();
    paragraphs->Add(table);

    //-------------------------------------

    auto document = MakeObject<Document>();
    auto table1 = MakeObject<Aspose::Pdf::Table>();
    table1->set_ColumnWidths(u"100 100");

    String _dataDir("C:\\Samples\\");

    for (int i = 1; i <= 10; i++)
    {
        auto row = table1->get_Rows()->Add();
        auto cell1 = row->get_Cells()->Add();
        cell1->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(u"LAAAAAAA"));
        auto cell2 = row->get_Cells()->Add();
        cell2->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(u"LAAGGGGGG"));
    }
    
    table1->set_IsInNewPage (true);
    // テーブル1を次のページに保持したいです...
    paragraphs->Add(table1);
    
    document->Save(_dataDir + u"IsNewPageProperty_Test_out.pdf");
}
```