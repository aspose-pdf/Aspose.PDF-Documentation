---
title: Python を使用した AcroForm からのデータ抽出
linktitle: AcroForm からのデータ抽出
type: docs
weight: 50
url: /ja/python-net/extract-data-from-acroform/
description: Aspose.PDF を使用すると、PDF ファイルからフォームフィールド データを簡単に抽出できます。AcroForm からデータを抽出し、JSON、XML、または FDF 形式で保存する方法を学びましょう。
lastmod: "2025-03-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して AcroForm からデータを抽出する方法
Abstract: この記事は、Python 向け Aspose.PDF を使用して PDF 文書内のフォームフィールドを管理するための包括的なガイドを提供します。PDF からフォームデータを抽出、操作、エクスポートするさまざまな方法を詳述しています。記事は、フォームフィールドの値を抽出し、辞書に格納してから JSON 形式でデータを出力する方法のデモから始まります。さらに、フォームデータを直接 JSON ファイルにエクスポートし、データシリアライズ機能を強化する方法も示しています。また、XML、FDF（Forms Data Format）、XFDF などの他の形式へのエクスポートも取り上げており、データ交換や構造化データの保存に役立ちます。各セクションには、理解と実装を支援する Python コードスニペットが含まれています。全体として、この記事は PDF フォーム処理を Python アプリケーションに統合したい開発者にとって実用的なリソースとなります。
---

## PDF ドキュメントからフォームフィールドを抽出

フォームフィールドの生成や入力を可能にするだけでなく、Aspose.PDF for Python は PDF ファイルからフォームフィールド データやフィールドに関する情報を簡単に抽出できるようにします。

このコードスニペットは、PDF フォーム内のすべてのフィールドの値を格納する辞書を作成します。フォームのフィールド名を反復処理し、それらの値を取得して辞書にデータを格納します。最後に、収集したフォーム値を出力します。

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

## タイトルでフォームフィールド値を取得

## PDF ドキュメントからフォームフィールドを JSON に抽出

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    form = apdf.facades.Form(path_infile)
    with FileIO(path_outfile, "w") as json_file:
        form.export_json(json_file, True)
```

提供された Python コードスニペットは、フィールドの値を抽出し、そのデータを JSON 形式にシリアライズします。必要なモジュールをインポートし、入力・出力ファイルパスを構築し、PDF フォームからフィールド名と値を取得し、シリアライズされた JSON 文字列を指定された出力ファイルに書き込みます。

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    form = apdf.facades.Form(path_infile)
    form_data = {}
    # Get values from all fields
    for formField in form.field_names:
        # Analyze names and values if need
        form_data[formField] = form.get_field(formField)

    # Serialize to JSON
    json_string = json.dumps(form_data, indent=4)

    # Output the JSON string
    print(json_string)

    with open(path_outfile, "w", encoding="utf-8") as json_file:
        json_file.write(json_string)
```

## PDF ファイルから XML にデータを抽出

次の Python コードスニペットはフォームオブジェクトを作成し、PDF ドキュメントをそのオブジェクトにバインドして、フォームデータを XML ファイルにエクスポートします。このコードは PDF フォームからデータを自動的に抽出し、構造化された XML 形式で保存します。

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

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

## PDF ファイルから FDF にデータをエクスポート

以下のコードスニペットはフォームオブジェクトを作成し、PDF ドキュメントをそのフォームにバインドした後、フォームデータを FDF（Forms Data Format）ファイルにエクスポートします。FDF ファイルは PDF 文書からのフォームデータを保存するための形式であり、データ交換を容易にします。

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

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

## PDF ファイルから XFDF にデータをエクスポート

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

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

