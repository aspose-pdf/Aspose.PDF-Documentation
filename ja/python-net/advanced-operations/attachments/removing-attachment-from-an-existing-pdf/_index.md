---
title: Python で PDF から添付ファイルを削除する方法
linktitle: 既存の PDF からの添付ファイルの削除
type: docs
weight: 30
url: /ja/python-net/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF は PDF ドキュメントから添付ファイルを削除できます。Python PDF API を使用すると、.NET ライブラリ経由で Aspose.PDF for Python を使用して PDF ファイル内の添付ファイルを削除できます。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF から添付ファイルを削除する方法
Abstract: この記事では、Aspose.PDF for Python を使用して PDF ファイルから添付ファイルを削除する方法について説明します。PDF ドキュメント内の添付ファイルは、「Document」オブジェクトの「EmbeddedFiles」コレクションに保存されます。PDF からすべての添付ファイルを削除するには、`EmbeddedFiles` コレクションの `delete () `メソッドを呼び出し、`Document` オブジェクトの `save ()` メソッドを使用して更新されたドキュメントを保存します。このプロセスを説明するコードスニペットが提供されており、文書を開いて添付ファイルを削除し、変更したファイルを保存する手順が紹介されています。
---

Aspose.PDF for Python は PDF ファイルから添付ファイルを削除できます。PDF ドキュメントの添付ファイルは Document オブジェクトに保持されます。 [埋め込みファイル](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) コレクション。

このワークフローは、古くなった埋め込みファイルをクリーンアップしたり、パッケージサイズを小さくしたり、ソース資料を添付せずに再配布するために PDF を準備したりする必要がある場合に役立ちます。

PDF ファイルに関連付けられているすべての添付ファイルを削除するには：

1. に電話してください [埋め込みファイル](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) コレクションの [削除 ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/#methods) 方法。
1. を使用して更新したファイルを保存します。 [文書](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) オブジェクトの [保存 ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法。

次のコードスニペットは、PDF ドキュメントから添付ファイルを削除する方法を示しています。

```python

import aspose.pdf as ap

def remove_attachment(infile, outfile):
    # Open PDF document
    with ap.Document(infile) as document:
        document.embedded_files.delete()
        document.save(outfile)
```

## 特定の添付ファイルを名前で削除する

アタッチメントを 1 つだけ削除して他のアタッチメントを残す必要がある場合は、 [キーで削除 ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/delete_by_key/) メソッドを入力し、添付ファイル名を渡します。

特定の添付ファイルを削除するには:

1. ソース PDF ファイルを開きます。
1. コール `document.embedded_files.delete_by_key(attachment_name)`.
1. 更新した PDF ファイルを保存します。

次のコードスニペットは、名前を指定して添付ファイルを 1 つ削除します。

```python

import aspose.pdf as ap

def remove_attachment(infile, attachment_name, outfile):
    # Open PDF document
    with ap.Document(infile) as document:
        document.embedded_files.delete_by_key(attachment_name)
        document.save(outfile)
```

## 関連する添付トピック

- [Python で PDF の添付ファイルを操作する](/pdf/ja/python-net/attachments/)
- [Python で PDF に添付ファイルを追加する方法](/pdf/ja/python-net/add-attachment-to-pdf-document/)
- [Python での PDF ポートフォリオの作成と管理](/pdf/ja/python-net/portfolio/)

