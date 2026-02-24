---
title: Python を使用して PDF から添付ファイルを削除する
linktitle: 既存の PDF から添付ファイルを削除する
type: docs
weight: 30
url: /ja/python-net/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF は PDF ドキュメントから添付ファイルを削除できます。Python PDF API を使用して、.NET ライブラリ経由の Aspose.PDF for Python で PDF ファイルの添付ファイルを削除します。
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python で PDF の添付ファイルを削除する方法
Abstract: この記事では、Aspose.PDF for Python を使用して PDF ファイルから添付ファイルを削除する方法について説明します。PDF ドキュメントの添付ファイルは `Document` オブジェクトの `EmbeddedFiles` コレクションに格納されています。PDF からすべての添付ファイルを削除するには、`EmbeddedFiles` コレクションの `delete()` メソッドを呼び出し、`Document` オブジェクトの `save()` メソッドで更新されたドキュメントを保存します。このプロセスを示すコードスニペットが提供されており、ドキュメントのオープン、添付ファイルの削除、変更後のファイルの保存手順を示しています。
---

Aspose.PDF for Python は PDF ファイルから添付ファイルを削除できます。PDF ドキュメントの添付ファイルは Document オブジェクトの [EmbeddedFiles](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) コレクションに格納されています。

PDF ファイルに関連付けられたすべての添付ファイルを削除するには：

1. [EmbeddedFiles](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) コレクションの [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/#methods) メソッドを呼び出します。
1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) オブジェクトの [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) メソッドを使用して更新されたファイルを保存します。

以下のコードスニペットは、PDF ドキュメントから添付ファイルを削除する方法を示しています。

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Delete all attachments
    document.embedded_files.delete()

    # Save updated file
    document.save(output_pdf)
```


