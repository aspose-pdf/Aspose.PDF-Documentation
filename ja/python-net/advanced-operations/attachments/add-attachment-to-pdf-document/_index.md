---
title: Python で PDF に添付ファイルを追加する方法
linktitle: PDF ドキュメントへの添付ファイルの追加
type: docs
weight: 10
url: /ja/python-net/add-attachment-to-pdf-document/
description: .NET 経由で Aspose.PDF for Python を使用して Python で PDF ドキュメントに添付ファイルを追加する方法を学びましょう。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF に添付ファイルを追加する方法
Abstract: この記事では、Python と Aspose.PDF ライブラリを使用して PDF ファイルに添付ファイルを追加する方法を段階的に説明します。新しい Python プロジェクトをセットアップし、必要な Aspose.PDF パッケージをインポートし、「Document」オブジェクトを作成するプロセスについて詳しく説明します。この記事では、必要なファイルと説明を含む「FileSpecification」オブジェクトを作成する方法と、このオブジェクトを「add」メソッドを使用して PDF ドキュメントの「EmbeddedFileCollection」に追加する方法について説明します。「EmbeddedFileCollection」には、PDF 内のすべての添付ファイルが格納されます。ドキュメントを開き、添付するファイルを設定し、それをドキュメントの添付コレクションに追加し、更新された PDF を保存するプロセスを示すコードスニペットが含まれています。
---

添付ファイルには、さまざまな情報を含めることができ、さまざまなファイルタイプを使用できます。この記事では、PDF ファイルに添付ファイルを追加する方法について説明します。

関連するソースファイル、スプレッドシート、画像、または関連文書をメインPDFと一緒にパッケージ化する必要がある場合は、埋め込みPDF添付ファイルを使用してください。

1. 新しい Python プロジェクトを作成します。
1. Aspose.PDF パッケージをインポートする
1. を作成 [文書](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 対象。
1. を作成 [ファイル仕様](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) 追加するファイルとファイルの説明を含むオブジェクト。
1. を追加 [ファイル仕様](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) への対象 [文書](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) オブジェクトの [埋め込みファイルコレクション](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) コレクション、コレクションの [追加](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/#methods) 方法。

ザの [埋め込みファイルコレクション](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) コレクションには、PDF ファイル内のすべての添付ファイルが含まれます。次のコードスニペットは、PDF ドキュメントに添付ファイルを追加する方法を示しています。

```python
from os import path
import aspose.pdf as ap

def add_attachments(infile, attachment_path, outfile):
    with ap.Document(infile) as document:
        file_spec = ap.FileSpecification(attachment_path, "Sample text file")
        document.embedded_files.add(path.basename(attachment_path), file_spec)
        document.save(outfile)
```

## 関連する添付トピック

- [Python で PDF の添付ファイルを操作する](/pdf/ja/python-net/attachments/)
- [Python で PDF から添付ファイルを削除する](/pdf/ja/python-net/removing-attachment-from-an-existing-pdf/)
- [Python での PDF ポートフォリオの作成と管理](/pdf/ja/python-net/portfolio/)

