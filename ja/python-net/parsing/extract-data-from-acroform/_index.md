---
title: Python を使用してアクロフォームからデータを抽出する
linktitle: アクロフォームからデータを抽出
type: docs
weight: 50
url: /ja/python-net/extract-data-from-acroform/
description: Aspose.PDF を使用すると、PDF ファイルからフォームフィールドデータを簡単に抽出できます。AcroForms からデータを抽出し、JSON、XML、または FDF 形式で保存する方法を学びましょう。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用してアクロフォームからデータを抽出する方法
Abstract: この記事では、Aspose.PDF for Python を使用して PDF ドキュメント内のフォームフィールドを管理するための包括的なガイドを提供しています。PDF からフォームデータを抽出、操作、およびエクスポートするためのさまざまな方法について詳しく説明します。この記事ではまず、フォームフィールド値を抽出して辞書に保存し、その後に JSON 形式でデータを出力する方法を示します。さらに、フォームデータを JSON ファイルに直接エクスポートして、データのシリアル化機能を強化する方法についても説明します。さらに、この記事では、データ交換や構造化データの保存に役立つ XML、FDF (Forms Data Format)、XFDF など、他の形式へのフォームデータのエクスポートについても説明しています。各セクションには、理解と実装に役立つ Python コードスニペットが含まれています。全体として、この記事は PDF フォーム処理を Python アプリケーションに統合したいと考えている開発者にとって、実用的なリソースとして役立ちます。
---

## PDF ドキュメントからフォームフィールドを抽出

[フォーム](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) から `aspose.pdf.facades` 名前空間を使用すると、ドキュメントオブジェクトモデル全体を開かなくても、AcroForm フィールドデータを簡単に読み取ることができます。繰り返し処理を行います。 `form.field_names` フォームに存在するすべてのフィールド名を取得するには、 `form.get_field(name)` 現在の値を取得します。

1. を構築 `Form` 入力ファイルパスを渡してオブジェクトにします。
1. 反復処理 `form.field_names` すべてのフィールド名を列挙します。
1. コール `form.get_field(name)` 名前ごとに結果を辞書に保存します。

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = self.dataDir + infile
    form = apdf.facades.Form(path_infile)

    form_values = {}
    # Get values from all fields
    for formField in form.field_names:
        # Analyze names and values if needed
        form_values[formField] = form.get_field(formField)

    print(form_values)
```

## タイトル別にフォームフィールド値を取得

PDF フォームで定義されている正確なフィールド名（タイトル）がわかっている場合は、次のコマンドを使用してその値を直接取得できます。 `form.get_field(name)` フィールドコレクション全体を反復処理する必要はありません。これは、特定のフィールドのみが必要な場合に最も速い方法です。

1. を構築 [フォーム](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) 入力ファイルパスを持つオブジェクト。
1. コール `form.get_field("FieldName")` PDF に表示されているとおりのフィールドタイトルを使用します。
1. 返された文字列値をアプリケーションの必要に応じて使用します。

```python

    import aspose.pdf as apdf

    form = apdf.facades.Form(path_infile)

    # Retrieve a single field value by its name
    value = form.get_field("FirstName")
    print(value)
```

## PDF ドキュメントから JSON へのフォームフィールドの抽出

AcroForm データを JSON にエクスポートするには 2 つの方法があります。1 つ目はビルトインのものを使います。 `export_json` メソッドオン [フォーム](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form)は、1 回の呼び出しですべてのフィールドデータをファイルストリームに直接シリアル化します。

1. を構築 `Form` 入力ファイルパスを持つオブジェクト。
1. を使用して出力ファイルをバイナリストリームとして開きます `FileIO`.
1. コール `form.export_json(stream, True)` JSON 出力を書き込むためのものです。

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    form = apdf.facades.Form(path_infile)
    with FileIO(path_outfile, "w") as json_file:
        form.export_json(json_file, True)
```

2 番目の方法では、以下から Python 辞書を作成します。 `field_names` そして `get_field`、次にそれをシリアル化します `json.dumps`。書き込む前にデータを変換またはフィルタリングする必要がある場合に使用します。

1. 反復処理 `form.field_names` そしてディクショナリにフィールド値を入力します。
1. で辞書をシリアル化する `json.dumps(form_data, indent=4)`.
1. 結果の JSON 文字列を出力ファイルに書き込みます。

```python

    import aspose.pdf as apdf
    from os import path
    import json

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    form = apdf.facades.Form(path_infile)
    form_data = {}
    # Get values from all fields
    for formField in form.field_names:
        form_data[formField] = form.get_field(formField)

    # Serialize to JSON
    json_string = json.dumps(form_data, indent=4)
    print(json_string)

    with open(path_outfile, "w", encoding="utf-8") as json_file:
        json_file.write(json_string)
```

## PDF ファイルから XML にデータを抽出

XML エクスポートは、構造化された XML フィードまたはスキーマを使用するシステムと PDF フォームデータを統合するのに役立ちます。は [フォーム](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) クラス提供 `export_xml` 変換をワンステップで処理できます。

1. を作成 `Form` PDF をインスタンス化してバインドする `form.bind_pdf(path)`.
1. 出力ファイルをバイナリストリームとして開きます。
1. コール `form.export_xml(stream)` すべてのフィールドデータを XML として書き込みます。

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Create Form object
    form = apdf.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export data to XML file
    with FileIO(path_outfile, "w") as f:
        form.export_xml(f)
```

## PDF ファイルから FDF へのデータのエクスポート

FDF (Forms Data Format) は、AcroForm データの標準交換形式で、PDF ビューアや処理ツールで広くサポートされています。使用 `export_fdf` 上に [フォーム](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) クラスを指定すると、元のPDFまたは互換性のある別の形式にインポートできるスタンドアロンFDFファイルを生成できます。

1. を作成 `Form` ソース PDF をインスタンス化してバインドする `form.bind_pdf(path)`.
1. 出力ファイルをバイナリストリームとして開きます。
1. コール `form.export_fdf(stream)` FDF データを書き込みます。

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Create Form object
    form = apdf.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export form data to an FDF file
    with FileIO(path_outfile, "w") as f:
        form.export_fdf(f)
```

## PDF ファイルから XFDF へのデータのエクスポート

XFDF (XML フォームデータフォーマット) は FDF の後継の XML ベースのもので、Web サービスや最新のデータパイプラインでの使用に適しています。FDF と同様に、XFDF ファイルは互換性のある PDF フォームにインポートし直すことができます。を使用してください。 `export_xfdf` 上に [フォーム](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) クラスを使って出力を生成します。

1. を作成 `Form` ソース PDF をインスタンス化してバインドする `form.bind_pdf(path)`.
1. 出力ファイルをバイナリストリームとして開きます。
1. コール `form.export_xfdf(stream)` XFDF データを書き込みます。

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Create Form object
    form = apdf.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export form data to an XFDF file
    with FileIO(path_outfile, "w") as f:
        form.export_xfdf(f)
```
