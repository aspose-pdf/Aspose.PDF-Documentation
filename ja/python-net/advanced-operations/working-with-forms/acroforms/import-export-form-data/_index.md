---
title: フォームデータのインポートとエクスポート
linktitle: フォームデータのインポートとエクスポート
type: docs
weight: 80
url: /ja/python-net/import-export-form-data/
description: .NET 経由で Aspose.PDF for Python を使用して、AcroForm フィールドデータを XML、FDF、XFDF、JSON 形式でインポートおよびエクスポートします。
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Aspose.PDF for Python を使用して.NET 経由でインポートおよびエクスポートするテクニック。
Abstract: このコンピレーションでは、.NET 経由で Aspose.PDF for Python を使用した、フォームデータのインポートとエクスポートに関する包括的な手法を紹介します。PDF フォームを XML、FDF、XFDF、JSON などの外部データ形式と統合するためのワークフローについて説明しています。ユーザーは、構造化データをインタラクティブフィールドにインポートすることでフォームの一括入力を自動化したり、フィールド値を抽出して分析、バックアップ、または他のシステムとの統合を行うことができます。これらの例は、PDF フォームのバインド、形式間のデータ転送、更新済み文書の保存を行う方法を示しています。これにより、さまざまなアプリケーションでスケーラブルで一貫性のある文書処理が可能になります。
---

このページでは、.NET 経由で Aspose.PDF for Python を使用して AcroForm データをインポートおよびエクスポートする場合の一般的なワークフローを示します。すべての操作では以下を使用します。 [フォーム](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) ファサード。

## XML からフォームフィールドデータをインポートする

この方法を使用して、外部 XML データから PDF フォームに入力します。

1. を作成 `Form` 対象。
1. 入力 PDF をバインドします。
1. XML データファイルを開きます。
1. XML データをフォームにインポートします。
1. 更新した PDF を保存します。

```python
from io import FileIO
import aspose.pdf as ap

def import_data_from_xml(input_file_name, data_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(data_file_name, "r") as f:
        form.import_xml(f)

    form.save(output_file_name)
```

## フォームフィールドデータを XML にエクスポートする

このメソッドは、PDF ドキュメントから XML にフォームフィールド値をエクスポートします。

1. を作成 `Form` 対象。
1. 入力 PDF をバインドします。
1. XML 出力ファイルを開きます。
1. フォームデータを XML にエクスポートします。

```python
from io import FileIO
import aspose.pdf as ap

def export_data_to_xml(input_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)
    with FileIO(output_file_name, "w") as f:
        form.export_xml(f)
```

## FDF からフォームフィールドデータをインポートする

ザの `import_data_from_fdf` メソッドは、フォームフィールドデータを FDF (フォームデータフォーマット) ファイルから PDF フォームにインポートします。

1. を作成 `Form` 対象。
1. 入力 PDF をバインドします。
1. でフォームデータをインポートする `import_fdf()`.
1. 更新した PDF を保存します。

```python
from io import FileIO
import aspose.pdf as ap

def import_data_from_fdf(input_file_name, data_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(data_file_name, "r") as f:
        form.import_fdf(f)
        form.save(output_file_name)
```

## フォームフィールドデータを FDF にエクスポートする

この例では、フォームデータを PDF ドキュメントから FDF ファイルにエクスポートします。

1. を作成 `Form` 対象。
1. PDF ドキュメントをバインドします。
1. でフォームデータをエクスポートする `export_fdf()`.

```python
from io import FileIO
import aspose.pdf as ap

def export_data_to_fdf(input_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(output_file_name, "w") as f:
        form.export_fdf(f)
```

## XFDF からフォームフィールドデータをインポートする

このメソッドを使用して、XFDF (XML フォームデータ形式) ファイルから PDF フォームにフォームフィールドデータをインポートします。

1. を作成 `Form` 対象。
1. 入力 PDF をバインドします。
1. XFDF ファイルからフォームデータをインポートします。
1. 更新した PDF を保存します。

```python
from io import FileIO
import aspose.pdf as ap

def import_data_from_xfdf(input_file_name, data_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(data_file_name, "r") as f:
        form.import_xfdf(f)
        form.save(output_file_name)
```

## フォームフィールドデータを XFDF にエクスポートする

このコードは、フォームフィールドデータを PDF ドキュメントから XFDF ファイルにエクスポートします。

1. を作成 `Form` 対象。
1. 入力 PDF をバインドします。
1. フォームデータを XFDF にエクスポートします。

```python
from io import FileIO
import aspose.pdf as ap

def export_data_to_xfdf(input_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(output_file_name, "w") as f:
        form.export_xfdf(f)
```

## 別の PDF からデータを読み込む

この例では、XFDF をインメモリストリームにエクスポートし、ターゲットフォームにインポートすることで、フォームフィールドデータをソース PDF から宛先 PDF に転送します。

1. 送信元と送信先を作成 `Form` オブジェクト。
1. ソース PDF とターゲットの PDF をバインドします。
1. ソース PDF からフォームデータをエクスポートします。
1. 送信先の PDF にフォームデータをインポートします。
1. 更新した宛先 PDF を保存します。

```python
from io import StringIO
import aspose.pdf as ap

def import_data_from_another_pdf(source_pdf_name, destination_pdf_name, output_file_name):
    form_source = ap.facades.Form()
    form_dest = ap.facades.Form()

    form_source.bind_pdf(source_pdf_name)
    form_dest.bind_pdf(destination_pdf_name)

    with StringIO() as xfdf_stream:
        form_source.export_xfdf(xfdf_stream)
        xfdf_stream.seek(0)
        form_dest.import_xfdf(xfdf_stream)

    form_dest.save(output_file_name)
```

## フォームフィールドを JSON に抽出

このメソッドは、以下を使用してフォームフィールドを JSON ファイルにエクスポートします。 `export_json()`.

1. を作成 `Form` 対象。
1. JSON 出力ファイルを開きます。
1. を使用してフォームフィールドをエクスポートする `export_json()`.

```python
from io import FileIO
import aspose.pdf as ap

def extract_form_fields_to_json(input_file_name, output_file_name):
    form = ap.facades.Form(input_file_name)
    with FileIO(output_file_name, "w") as json_file:
        form.export_json(json_file, True)
```

## フォームフィールドを JSON ドキュメントに抽出

この例では、フォームフィールドの名前と値からカスタム JSON ドキュメントを作成します。

1. 入力ファイルから Form オブジェクトを作成します。
1. 空の辞書を初期化してフォームフィールドデータを保存します。
1. すべてのフォームフィールドを繰り返し処理し、その値を抽出します。
1. フォームデータディクショナリを 4 スペースインデントの JSON 文字列にシリアル化します。
1. JSON 文字列を UTF-8 エンコーディングで出力ファイルに書き込みます。

```python
import json
import aspose.pdf as ap

def extract_form_fields_to_json_doc(input_file_name, output_file_name):
    form = ap.facades.Form(input_file_name)
    form_data = {}
    for field_name in form.field_names:
        form_data[field_name] = form.get_field(field_name)

    json_string = json.dumps(form_data, indent=4)

    with open(output_file_name, "w", encoding="utf-8") as json_file:
        json_file.write(json_string)
```

## 関連トピック (ファサードアプローチ)

- [XML データをインポート](/pdf/ja/python-net/import-xml-data/)
- [FDF データをインポート](/pdf/ja/python-net/import-fdf-data/)
- [XFDF データのインポート](/pdf/ja/python-net/import-xfdf-data/)
- [JSON データをインポートする](/pdf/ja/python-net/import-json-data/)
- [XML にエクスポート](/pdf/ja/python-net/export-to-xml/)
- [FDF にエクスポート](/pdf/ja/python-net/export-to-fdf/)
- [XFDF にエクスポート](/pdf/ja/python-net/export-to-xfdf/)
- [JSON へのエクスポート](/pdf/ja/python-net/export-to-json/)
