---
title: フォームエディター
type: docs
weight: 40
url: /net/plugins/formeditor/
description: Aspose.PDFプラグインを使用してPDFファイルのフォームフィールドを追加、更新、および削除する方法
lastmod: "2024-01-24"
draft: false
---

この記事では、PDFファイルのフォームフィールドを追加、更新、および削除することができる[フォームエディタープラグイン](https://products.aspose.org/pdf/net/form-editor/)の使用方法を紹介します。

## 前提条件

以下が必要です：

* Visual Studio 2019以降
* Aspose.PDF for .NET 24.1以降
* フォームフィールドが含まれているサンプルPDFファイル

Aspose.PDF for .NETライブラリは公式ウェブサイトからダウンロードするか、Visual StudioのNuGetパッケージマネージャーを使用してインストールできます。

## 手順

FormEditorプラグインを使用してPDFファイルのフォームフィールドを追加、更新、および削除する基本的な手順は以下の通りです：

1. FormEditorクラスのオブジェクトを作成する
1. FormEditorAddOptions、FormEditorSetOptions、またはFormRemoveSelectedFieldsOptionsクラスのオブジェクトを作成する（実行したい操作に応じて）
1.
1. FormEditorオブジェクトのProcessメソッドを実行する

これらのステップをC#コードで実装する方法を見てみましょう。

### ステップ1: FormEditorクラスのオブジェクトを作成する

FormEditorクラスは、PDFファイル内のフォームフィールドの追加、更新、削除の機能を提供するメインクラスです。これを使用するには、デフォルトコンストラクタを使用してインスタンスを作成する必要があります：

```cs
// FormEditorプラグインのインスタンスを作成する
var plugin = new FormEditor();
```

### ステップ2: 実行したい操作に応じて、FormEditorAddOptions、FormEditorSetOptions、またはFormRemoveSelectedFieldsOptionsクラスのオブジェクトを作成する

`FormEditorAddOptions`, `FormEditorSetOptions`, `FormRemoveSelectedFieldsOptions`クラスは、フォームフィールドのタイプ、値、プロパティ、条件など、フォーム編集操作のさまざまなオプションやパラメーターを指定するためのヘルパークラスです。
`FormEditorAddOptions`、`FormEditorSetOptions`、`FormRemoveSelectedFieldsOptions` クラスは、フォームフィールドのタイプ、値、プロパティ、条件など、フォーム編集操作のさまざまなオプションとパラメータを指定するためのヘルパークラスです。

```cs
    // フォームフィールドを追加するためのオプションを作成します。
    var options = new FormEditorAddOptions(
        [
            // チェックボックスフォームフィールドを作成します。
            new FormCheckBoxFieldCreateOptions(1, new Rectangle(110, 700, 125, 715))
            {
                Value = "CheckBoxField 1",
                PartialName = "CheckBoxField_1",
                Color = Color.Blue,
            },
            // コンボボックスフォームフィールドを作成します。
            new FormComboBoxFieldCreateOptions(1, new Rectangle(310, 600, 350, 615))
            {
                Color = Color.Red,
                Editable = true,
                DefaultAppearance = new DefaultAppearance("Arial Bold", 12, System.Drawing.Color.DarkGreen),
                Options = ["option1", "option2", "option3"],
                Selected = 2
            },
            // テキストボックスフォームフィールドを作成します。
            new FormTextBoxFieldCreateOptions(1, new Rectangle(10, 700, 90, 715))
            {
                MaxLen = 10,
                Value = "Some text",
                Color = Color.Chocolate
            }
        ]);
```
フォームフィールドの値が「a value」または「an another value」である場合、それを「new value」に更新するには、以下のコードを使用できます：

```cs
    var options = new FormEditorSetOptions(
    (field) => { return field.Value == "a value" || field.Value == "an another value"; },
    new FormFieldSetOptions()
    {
        Value = "new value"
    });
```

下左のx座標が300より大きいフォームフィールドを削除するには、以下のコードを使用できます：

```cs
// フォームフィールドを削除するオプションを作成
var options = new FormRemoveSelectedFieldsOptions((field) => field.Rect.LLX > 300);
```

### ステップ 3: オプションオブジェクトに入力および出力データソースを追加する

入力および出力データソースは、編集および保存したいPDFファイルです。
入力データソースと出力データソースは、編集して保存したいPDFファイルです。

```cs
// 入力ファイルと出力ファイルのパスを指定する
string inputPath = $@"C:\Samples\Output\sample_forms.pdf";
string outputPath = $@"C:\Samples\Output\sample_forms2.pdf";

// 入力ファイルと出力ファイルのためのFileDataSourceクラスの新しいインスタンスを作成する
FileDataSource inputData = new(inputPath);
FileDataSource outputData = new(outputPath);

// オプションに入力データソースと出力データソースを追加する
options.AddInput(inputData);
options.AddOutput(outputData);
```

### ステップ 4: FormEditorオブジェクトのProcessメソッドを実行する

最終ステップは、FormEditorオブジェクトのProcessメソッドを実行することです。パラメータとしてoptionsオブジェクトを渡します。
フォームエディターオブジェクトのProcessメソッドを実行し、パラメータとしてオプションオブジェクトを渡すのが最終ステップです。

```cs
// プラグインとオプションを使用してフォーム編集操作を処理します
ResultContainer result = plugin.Process(options);

// 結果コレクションから最初の結果を取得します
var result = resultContainer.ResultCollection[0];

// 結果を印刷します
Console.WriteLine(result);
```

結果には出力ファイルパスなどの情報が含まれます。
