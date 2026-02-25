---
title: フォームデータのインポートとエクスポート
type: docs
weight: 80
url: /ja/python-net/import-export-form-data/
description: このセクションでは、フォームデータのインポートとエクスポート方法について説明します。
lastmod: "2025-08-05"
TechArticle: true
AlternativeHeadline: Aspose.PDF for Python via .NET を使用したインポートおよびエクスポート手法
Abstract: このコンパイルでは、Aspose.PDF for Python via .NET を使用したフォームデータのインポートおよびエクスポート手法の包括的なセットを提示します。XML、FDF、XFDF、JSON などの外部データ形式と PDF フォームを統合するワークフローをカバーしています。ユーザーは構造化データをインタラクティブなフィールドにインポートして大量のフォーム入力を自動化したり、フィールド値を抽出して分析、バックアップ、または他システムとの統合に利用できます。サンプルは PDF フォームのバインド、フォーマット間のデータ転送、更新ドキュメントの保存方法を示し、さまざまなアプリケーションでスケーラブルかつ一貫した文書処理を実現します。
---

## XMLファイルからフォームデータをインポート

次の例では、Aspose.PDF for Python を使用して XML ファイルから既存の PDF フォームにフォームデータをインポートする方法を示します。PDF フォームをバインドし、XML データを読み込み、更新されたファイルを保存することで、各ページを手動で編集せずにインタラクティブなフォームフィールドに素早く入力できます。この方法は、大量のフォーム入力の自動化、巨大データセットの処理、複数文書間のデータ一貫性の確保に最適です。

以下の手順を使用してください：

1. Aspose.PDF を使用して Form オブジェクトを作成します。
1. PDF フォームをバインドします。
1. XML データを読み込みます。
1. XML を PDF にインポートします。
1. 更新された PDF を保存します。

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    # Define the working directory path
    workdir_path = "/path/to/working/directory"

    # Construct full file paths using the working directory
    path_infile = path.join(workdir_path, infile)
    path_datafile = path.join(workdir_path, datafile)
    path_outfile = path.join(workdir_path, outfile)

    # Create a Form object from Aspose.PDF
    form = ap.facades.Form()

    # Bind the input PDF form
    form.bind_pdf(path_infile)

    # Import XML data into the form
    with FileIO(path_datafile, "r") as f:
        form.import_xml(f)

    # Save the form with imported data to a new PDF file
    form.save(path_outfile)
```

## PDF ドキュメントから XML ファイルへのフォームフィールドデータのエクスポート

Python ライブラリは、Aspose.PDF for Python を使用して PDF ドキュメントから XML ファイルへフォームフィールドデータをエクスポートする方法を示します。PDF フォームをバインドし、フィールド値を XML 形式で保存することで、フォームデータを他のアプリケーションやワークフローで簡単に保存、処理、再利用できます。このアプローチは、データのバックアップ、分析、外部システムとの統合に最適です。

以下の手順を使用してください：

1. Aspose.PDF を使用して Form オブジェクトを作成します。
1. PDF フォームをバインドします。
1. フォームデータをエクスポートします。
1. フィールド値を XML に保存します。

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    # Combine the working directory path with the input PDF file name
    path_infile = path.join(self.workdir_path, infile)

    # Combine the working directory path with the output XML file name
    path_outfile = path.join(self.workdir_path, datafile)

    # Create a Form object to work with PDF form fields
    form = ap.facades.Form()

    # Bind the PDF document containing the form
    form.bind_pdf(path_infile)

    # Open the XML file in write mode to store exported form data
    with FileIO(path_outfile, "w") as f:
        # Export form field data from the PDF to the XML file
        form.export_xml(f)
```

## FDF からフォームフィールドデータをインポート

'import_data_from_fdf' メソッドは、FDF（Forms Data Format）ファイルから既存の PDF フォームにフォームフィールドデータをインポートし、更新されたドキュメントを保存します。このアプローチは、ドキュメントの構造を変更せずにプログラムで PDF フォームを事前入力または更新する際に便利です。

以下の手順を使用してください：

1. Aspose.PDF を使用して Form オブジェクトを作成します。
1. 入力 PDF をバインドします。
1. import_fdf() を使用してフォームデータをインポートします。
1. インポートされたデータを含む PDF を指定された出力ファイルパスに保存します。

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_datafile = path.join(self.workdir_path, datafile)
    path_outfile = path.join(self.workdir_path, outfile)

    form = ap.facades.Form()
    form.bind_pdf(path_infile)

    with FileIO(path_datafile, "r") as f:
        form.import_fdf(f)
        form.save(path_outfile)
```

## フォームフィールドデータを FDF にエクスポート

この例では、Aspose.PDF for Python via .NET を使用して PDF ドキュメントから FDF（Forms Data Format）ファイルへフォームデータをエクスポートする方法を示します。

1. Aspose.PDF を使用して Form オブジェクトを作成します。
1. PDF ドキュメントをバインドします。
1. export_fdf() を使用してフォームデータをエクスポートします。

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_outfile = path.join(self.workdir_path, outfile)

    # Create Form object
    form = ap.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export form data to an FDF file
    with FileIO(path_outfile, "w") as f:
        form.export_fdf(f)
```

## XFDF からフォームフィールドデータをインポート

この例では、PDF ドキュメントから XFDF（XML Forms Data Format）ファイルへフォームフィールドデータをエクスポートし、その後 Aspose.PDF for Python via .NET を使用して更新された PDF を保存します。

1. Aspose.PDF を使用して Form オブジェクトを作成します。
1. PDF ドキュメントをフォームにバインドします。
1. フォームデータを XFDF ファイルにエクスポートします。
1. 処理されたフォームを保存します。

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_datafile = path.join(self.workdir_path, datafile)
    path_outfile = path.join(self.workdir_path, outfile)

    # Create Form object
    form = ap.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export form data to an XFDF file
    with FileIO(path_datafile, "w") as f:
        form.export_xfdf(f)
        form.save(path_outfile)
```

## フォームフィールドデータを XFDF にエクスポート

このコードは、PDF ドキュメントからフォームフィールドデータを抽出し、Aspose.PDF for Python を使用して XFDF（XML Forms Data Format）ファイルへエクスポートします。

1. Aspose.PDF を使用して Form オブジェクトを作成します。
1. PDF ドキュメントをフォームにバインドします。
1. フォームデータを FDF ファイルにエクスポートします。

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_outfile = path.join(self.workdir_path, outfile)

    # Create Form object
    form = ap.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export form data to an FDF file
    with FileIO(path_outfile, "w") as f:
        form.export_xfdf(f)
```

## 別の PDF からデータをインポート

このコードスニペットは、ソース PDF からターゲット PDF にフォームフィールドデータを転送する方法を示します。フォームデータはソース PDF から XFDF ストリームとしてエクスポートされ、Aspose.PDF for Python via .NET を使用してターゲット PDF にインポートされます。

1. Aspose.PDF を使用して Form オブジェクトを作成します。
1. PDF ドキュメントをフォームにバインドします。
1. ソース PDF からフォーム データをエクスポートします。
1. 宛先 PDF にフォーム データをインポートします。
1. 更新された宛先 PDF を保存します。

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_outfile = path.join(self.workdir_path, outfile)

    # Create Form object
    form_source = ap.facades.Form()
    form_dest = ap.facades.Form()

    # Bind PDF document
    form_source.bind_pdf(path_infile)
    form_dest.bind_pdf(path_outfile)

    # Export form data to an FDF file
    with StringIO() as f:
        form_source.export_xfdf(f)
        form_dest.import_xfdf(f)
        form_dest.save()
```

## フォーム フィールドを JSON に抽出

このメソッドは入力ファイルからフォーム フィールドを抽出し、JSON ファイルにエクスポートします。

1. Aspose.PDF を使用して Form オブジェクトを作成します。
1. FileIO() を使用して出力ファイルを書き込みモードで開きます。
1. form.export_json() メソッドを使用してフォーム フィールドを JSON ファイルにエクスポートします。

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_outfile = path.join(self.workdir_path, outfile)

    form = ap.facades.Form(path_infile)
    with FileIO(path_outfile, "w") as json_file:
        form.export_json(json_file, True)
```

## フォーム フィールドを JSON ドキュメントに抽出

1. 入力ファイルから Form オブジェクトを作成します。
1. フォーム フィールド データを保存するための空の辞書を初期化します。
1. すべてのフォーム フィールドを反復処理し、その値を抽出します。
1. フォーム データ辞書を 4 スペースインデントの JSON 文字列にシリアライズします。
1. JSON 文字列を UTF-8 エンコーディングで出力ファイルに書き込みます。

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_outfile = path.join(self.workdir_path, outfile)

    form = ap.facades.Form(path_infile)
    form_data = {}
    # Get values from all fields
    for formField in form.field_names:
        # Analyze names and values if needed
        form_data[formField] = form.get_field(formField)

    # Serialize to JSON
    json_string = json.dumps(form_data, indent=4)

    with open(path_outfile, "w", encoding="utf-8") as json_file:
        json_file.write(json_string)
```

