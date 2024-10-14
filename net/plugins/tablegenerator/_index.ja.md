---
title: テーブルジェネレータ
type: docs
weight: 130
url: /net/plugins/tablegenerator/
description: 指定されたPDFドキュメントのページ番号にテーブルを追加/挿入することができます。
lastmod: "2024-01-24"
draft: false
---

.NETを使用してPDFドキュメントに動的で視覚的に魅力的なテーブルを作成する必要がありますか？ Aspose.PDF for .NETは、プロセスを簡素化する強力なTableGeneratorクラスを提供しています。この章では、デモドキュメントの作成からTableGeneratorクラスを使用してテーブルを生成するまで、PDFドキュメントでテーブルを生成する手順を説明します。
さあ、テーブル生成の手順を一歩一歩学びましょう。

## 前提条件

以下が必要になります：

* Visual Studio 2019以降
* Aspose.PDF for .NET 24.3以降
* サンプルPDFファイル

## デモドキュメントの作成

テーブル生成に入る前に、テーブルが挿入される空のページでデモドキュメントを作成しましょう。
テーブルの生成に移る前に、テーブルが挿入される空ページを含むデモドキュメントを作成しましょう。

* 新しいPDFドキュメントを作成します。
* ドキュメントに空ページを追加します。
* 指定されたファイルにドキュメントを保存します。

```cs
// <summary>
// 空ページを含むデモドキュメントを作成します。
//
// パラメータ:
// - fileName: 出力ファイルのパスと名前。
// </summary>
internal static void CreateDemoDocument(string fileName)
{
    // 新しいPDFドキュメントを作成します。
    var document = new Aspose.Pdf.Document();

    // ドキュメントに四つの空ページを追加します。
    for (int i = 0; i < 2; i++)
    {
        document.Pages.Add();
    }

    // 指定されたファイルにドキュメントを保存します。
    document.Save(fileName);
}
```

## テーブル生成

デモドキュメントが準備できたら、`TableGenerator` クラスを使用してテーブルを生成することができます。次のスニペットは、さまざまなコンテンツタイプとフォーマットオプションを使用してテーブルを生成する方法を示しています。テーブルの生成方法は次のとおりです:

* `TableGenerator` クラスの新しいインスタンスを作成します。
* `TableGenerator` クラスの新しいインスタンスを作成します。
* テーブルオプションを作成し、入力および出力ファイルのデータソースを指定します。
* オプションにコンテンツとフォーマッティングを指定して、テーブルに行とセルを追加します。
* `Process` メソッドを使用してテーブル生成を処理し、結果のコンテナーを取得します。

### テーブルの作成

Aspose.PDFを使用してテーブルを作成するには、次の手順に従います：

```cs
// TableGenerator クラスの新しいインスタンスを作成します。
var generator = new TableGenerator();

// テーブルオプションを作成し、デモテーブルを追加します。
var options = new TableOptions();

// オプションに入力および出力ファイルのデータソースを追加します。
options.AddInput(new FileDataSource(@"C:\Samples\Results\table-generator-demo.pdf"));
options.AddOutput(new FileDataSource(@"C:\Samples\Results\table-generator-demo.pdf"));

// オプションに最初のテーブルを追加します。
options
    .InsertPageAfter(1)
    .AddTable()
```

上記のコードでは、`TableOptions` のインスタンスを作成し、PDFドキュメントの入力および出力ファイルのデータソースを指定します。
上記のコードでは、`TableOptions`のインスタンスを作成し、PDFドキュメントの入力と出力ファイルデータソースを指定します。

### テーブルへのコンテンツ追加

テーブルが作成されたら、テキスト、HTML、画像など、さまざまなタイプのコンテンツを含む行やセルでそれを埋めることができます。テーブルにコンテンツを追加する方法は以下の通りです：

```csharp
options
    .AddTable()
        .AddRow()
            .AddCell()
                .AddParagraph(new HtmlFragment("<h1>Header 1</h1>")) // セルにHTMLコンテンツを追加します。
            .AddCell()
                .AddParagraph(new HtmlFragment("<h2>Header 2</h2>"))
            .AddCell()
                .AddParagraph(new HtmlFragment("<h3>Header 3</h3>"));
```

この例では、テーブルに行を追加し、ヘッダーを表すHTMLフラグメントを含むセルでそれを埋めます。

役立つメソッド：

* **InsertPageAfter**: 指定されたページ番号の後にページを挿入します。
* **InsertPageBefore**: 指定されたページ番号の後にページを挿入します。
* **AddTable**: ドキュメントにテーブルを追加します。
* **AddTable**: ドキュメントにテーブルを追加します。
* **AddRow**: テーブルに行を追加します。
* **AddCell**: 行にセルを追加します。
* **AddParagraph**: セルに内容を追加します。

段落として以下のタイプの内容を追加できます:

* **HtmlFragment** - HTMLマークアップに基づいた内容
* **TeXFragment** - TeX/LaTeXマークアップに基づいた内容
* **TextFragment** - 単純なテキスト内容
* **Image** - グラフィックス

## テーブル生成を実行する

内容を追加した後、テーブルの作成を開始できます。

```cs
// テーブル生成を処理し、結果のコンテナを取得します。
var resultContainer = generator.Process(options);

// 結果コレクションの結果の数を出力します。
Console.WriteLine(resultContainer.ResultCollection.Count);
```

`Process` メソッドはテーブル生成を実行します。このメソッドは、エラーを処理するために try-catch でラップすることもできます。

以下に完全なコードの例を示します：

```cs
using Aspose.Pdf;
using Aspose.Pdf.Plugins;
using Aspose.Pdf.Text;

namespace AsposePluginsNet8.Documentation
{
    // <summary>
    // Aspose.Pdf でのテーブル生成の使用を示すクラスを表します。
    // </summary>
    internal static class TableDemo
    {
        // <summary>
        // テーブル生成デモを実行します。
        // </summary>
        internal static void Run()
        {
            // デモドキュメントを作成し、テーブルを生成します。
            CreateDemoDocument(@"C:\Samples\Results\table-generator-demo.pdf");
            CreateDemoTable();
        }

        // <summary>
        // 4ページの空のデモドキュメントを作成します。
        //
        // パラメーター:
        // - fileName: 出力ファイルのパスと名前。
        // </summary>
        internal static void CreateDemoDocument(string fileName)
        {
            // 新しいPDFドキュメントを作成します。
            var document = new Aspose.Pdf.Document();

            // ドキュメントに4ページの空ページを追加します。
            for (int i = 0; i < 2; i++)
            {
                document.Pages.Add();
            }

            // 指定したファイルにドキュメントを保存します。
            document.Save(fileName);
        }

        // <summary>
        // TableGenerator クラスを使用してテーブルを生成します。
        // </summary>
        internal static void CreateDemoTable()
        {
            // TableGenerator クラスの新しいインスタンスを作成します。
            var generator = new TableGenerator();

            // テーブルオプションを作成し、デモテーブルを追加します。
            var options = new TableOptions();

            // オプションに入力および出力ファイルデータソースを追加します。
            options.AddInput(new FileDataSource(@"C:\Samples\Results\table-generator-demo.pdf"));
            options.AddOutput(new FileDataSource(@"C:\Samples\Results\table-generator-demo.pdf"));

            // オプションに最初のテーブルを追加します。
            options
                .InsertPageAfter(1)
                .AddTable()
                    .AddRow()
                        .AddCell()
                            .AddParagraph(new HtmlFragment("<h1>ヘッダー 1</h1>"))
                        .AddCell()
                            .AddParagraph(new HtmlFragment("<h2>ヘッダー 2</h2>"))
                        .AddCell()
                            .AddParagraph(new HtmlFragment("<h3>ヘッダー 3</h3>"))
                    .AddRow()
                        .AddCell()
                            .AddParagraph(new TeXFragment("{\\small 方程式 $E=mc^2$、1905年にアルベルト・アインシュタインによって発見されました。}", true))
                        .AddCell()
                            .AddParagraph(new TextFragment("セル 2 2"))
                        .AddCell()
                            .AddParagraph(new TextFragment("セル 2 3"))
                    .AddRow()
                        .AddCell()
                            .AddParagraph(new TextFragment("セル 3 1a"))
                            .AddParagraph(new TextFragment("セル 3 1b"))
                        .AddCell()
                            .AddParagraph(new TextFragment("セル 3 2"))
                        .AddCell()
                            .AddParagraph(new TextFragment("セル 3 3"));

            // オプションに2番目のテーブルを追加します。
            options
                .InsertPageBefore(2)
                .AddTable()
                    .AddRow()
                        .AddCell()
                            .AddParagraph(new TextFragment("ヘッダー 1 1"))
                        .AddCell()
                            .AddParagraph(new TextFragment("ヘッダー 1 2"))
                        .AddCell()
                            .AddParagraph(new TextFragment("ヘッダー 1 3"))
                    .AddRow()
                        .AddCell()
                            .AddParagraph(new Image()
                            {
                                File = @"C:\Samples\logo.png",
                                FixWidth = 75,
                                FixHeight = 75,
                            })
                        .AddCell()
                            .AddParagraph(new Image()
                            {
                                File = @"C:\Samples\sample.svg",
                                FileType = ImageFileType.Svg,
                                FixWidth = 75,
                                FixHeight = 75
                            })
                        .AddCell()
                            .AddParagraph(new Image()
                            {
                                ImageStream = File.OpenRead(@"C:\Samples\Conversion\Demo.dcm"),
                                FileType = ImageFileType.Dicom,
                                FixWidth = 75,
                                FixHeight = 75
                            });

            // テーブル生成を処理し、結果のコンテナを取得します。
            var resultContainer = generator.Process(options);

            // 結果コレクションの結果の数を出力します。
            Console.WriteLine(resultContainer.ResultCollection.Count);
        }
    }
}
```

