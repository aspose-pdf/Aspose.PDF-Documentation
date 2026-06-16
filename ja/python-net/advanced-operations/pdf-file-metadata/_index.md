---
title: Python で PDF ファイルのメタデータを操作する
linktitle: PDF ファイルメタデータ
type: docs
weight: 200
url: /ja/python-net/pdf-file-metadata/
description: Aspose.PDF を使用して Python で PDF ファイルのメタデータと XMP プロパティを抽出、更新、管理する方法を学びましょう。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python で PDF ドキュメント情報と XMP メタデータを取得および設定します
Abstract: この記事では、.NET 経由で Aspose.PDF for Python で PDF メタデータを操作する方法について説明します。Python で PDF ファイルの作成者、タイトル、キーワードなどの文書情報の読み取り、ファイルプロパティの更新、XMP メタデータフィールドの設定、カスタムメタデータプレフィックスの登録を行う方法を学びます。
---

このガイドは、Python でドキュメントのプロパティを調べたり、PDF ファイルの情報を更新して検索やカタログを作成したり、XMP メタデータをプログラム的に管理したりする必要がある場合に使用します。

## PDF ファイル情報を取得

このコードスニペットは、.NET 経由で Aspose.PDF for Python を使用して PDF ドキュメントからメタデータを抽出する方法を示しています。Document オブジェクトの info プロパティにアクセスすることで、作成者、作成日、キーワード、変更日、件名、タイトルなどの重要な情報を取得します。この機能は、文書のカタログ化、検索の最適化、または文書プロパティの検証を必要とするアプリケーションにとって不可欠です。

1. ドキュメントクラスを使用して PDF ファイルを開きます。
1. info プロパティを使用してドキュメントのメタデータを取得する
1. メタデータ情報を表示します。必要なメタデータフィールドを印刷します。

```python
import aspose.pdf as ap
import datetime
import sys
from os import path

def get_pdf_file_information(infile):
    # Open PDF document
    document = ap.Document(infile)

    # Get document information
    doc_info = document.info

    # Display document information
    print(f"Author: {doc_info.author}")
    print(f"Creation Date: {doc_info.creation_date}")
    print(f"Keywords: {doc_info.keywords}")
    print(f"Modify Date: {doc_info.mod_date}")
    print(f"Subject: {doc_info.subject}")
    print(f"Title: {doc_info.title}")
```

## PDF ファイル情報を設定

.NET 経由の Aspose.PDF for Python では、PDF のファイル固有の情報、作成者、作成日、件名、タイトルなどの情報を設定できます。この情報を設定するには:

1. Document クラスを使用して PDF ファイルを開きます。
1. を作成 [ドキュメント情報](https://reference.aspose.com/pdf/python-net/aspose.pdf/documentinfo/) オブジェクトを作成し、必要なメタデータプロパティを設定します。
1. save メソッドを使用して、変更を新しい PDF ファイルに保存します。

次のコードスニペットは、PDF ファイル情報を設定する方法を示しています。

```python
import aspose.pdf as ap
import datetime
import sys
from os import path

def set_file_information(infile, outfile):

    # Open PDF document
    document = ap.Document(infile)

    # Specify document information
    doc_info = ap.DocumentInfo(document)
    doc_info.author = "Aspose"
    doc_info.creation_date = datetime.datetime.now()
    doc_info.keywords = "Aspose.Pdf, DOM, API"
    doc_info.mod_date = datetime.datetime.now()
    doc_info.subject = "PDF Information"
    doc_info.title = "Setting PDF Document Information"
    doc_info.producer = "Custom producer"
    doc_info.creator = "Custom creator"

    # Save PDF document
    document.save(outfile)
```

## PDF ファイルに XMP メタデータを設定

このコードスニペットは、.NET 経由で Aspose.PDF for Python を使用して PDF ドキュメント内の XMP メタデータをプログラム的に設定または更新する方法を示しています。XMP: CreateDate、XMP: NickName、カスタム定義フィールドなどのプロパティを変更することで、標準化されたメタデータを PDF ファイルに埋め込むことができます。この方法は、文書を整理しやすくしたり、検索しやすくしたり、重要な情報をファイルに直接埋め込んだりする場合に特に役立ちます。

Aspose.PDF では、PDF ファイルにメタデータを設定できます。メタデータを設定するには:

1. を使用して PDF ファイルを開きます [文書](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) クラス。
1. 特定のキーに値を割り当てて XMP メタデータを変更します。
1. 更新した PDF ドキュメントを保存します。

次のコードスニペットは、PDF ファイルにメタデータを設定する方法を示しています。

```python
import aspose.pdf as ap
import datetime
import sys
from os import path

def set_xmp_metadata(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Set XMP metadata properties
    document.metadata.add("xmp:CreateDate", datetime.datetime.now().isoformat())
    document.metadata.add("xmp:Nickname", "Nickname")
    document.metadata.add("xmp:CustomProperty", "Custom Value")

    # Save the updated PDF document
    document.save(outfile)
```

## プレフィックス付きのメタデータを挿入

開発者によっては、プレフィックスを付けた新しいメタデータ名前空間を作成する必要があります。次のコードスニペットは、プレフィックス付きのメタデータを挿入する方法を示しています。

```python
import aspose.pdf as ap
import datetime
import sys
from os import path

def set_prefix_metadata(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Register a namespace URI for the 'xmp' prefix
    document.metadata.register_namespace_uri("xmp", "http://ns.adobe.com/xap/1.0/")

    # Set the metadata property using the registered prefix
    document.metadata.add(
        "xmp:ModifyDate", datetime.datetime.now().isoformat()
    )  # ISO 8601 format

    # Save the updated PDF document
    document.save(outfile)
```

## 関連トピック

- [Python での高度な PDF 操作](/pdf/ja/python-net/advanced-operations/)
- [Python で PDF ドキュメントを操作する](/pdf/ja/python-net/working-with-documents/)
- [Python で PDF の添付ファイルを操作する](/pdf/ja/python-net/attachments/)
- [Python で PDF ドキュメントを比較する](/pdf/ja/python-net/compare-pdf-documents/)
