---
title: Python を使用して PDF ドキュメントに添付ファイルを追加する
linktitle: PDF ドキュメントに添付ファイルを追加する
type: docs
weight: 10
url: /ja/python-net/add-attachment-to-pdf-document/
description: このページでは、Aspose.PDF for Python via .NET ライブラリを使用して PDF ファイルに添付ファイルを追加する方法について説明します。
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python で PDF に添付ファイルを追加する方法
Abstract: この記事では、Python と Aspose.PDF ライブラリを使用して PDF ファイルに添付ファイルを追加する手順をステップバイステップで紹介します。新しい Python プロジェクトの設定、必要な Aspose.PDF パッケージのインポート、`Document` オブジェクトの作成プロセスを詳しく説明します。記事では、目的のファイルと説明を持つ `FileSpecification` オブジェクトの作成方法、そして `add` メソッドを使用してこのオブジェクトを PDF ドキュメントの `EmbeddedFileCollection` に追加する方法を解説します。`EmbeddedFileCollection` は PDF 内のすべての添付ファイルを保持します。コードスニペットが含まれており、ドキュメントを開き、添付ファイル用のファイルを設定し、ドキュメントの添付コレクションに追加し、更新された PDF を保存する手順を示しています。
---

添付ファイルはさまざまな情報を含めることができ、さまざまなファイルタイプがあります。本記事では、PDF ファイルに添付ファイルを追加する方法を説明します。

1. 新しい Python プロジェクトを作成する。
1. Aspose.PDF パッケージをインポートする
1. [ドキュメント](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) オブジェクトを作成する。
1. 追加するファイルとファイルの説明を持つ [ファイル仕様](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) オブジェクトを作成する。
1. [ファイル仕様](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) オブジェクトを、[ドキュメント](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) オブジェクトの [埋め込みファイルコレクション](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) コレクションに、コレクションの [add](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/#methods) メソッドで追加する。

[埋め込みファイルコレクション](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) コレクションには、PDF ファイル内のすべての添付ファイルが含まれます。以下のコードスニペットは、PDF ドキュメントに添付ファイルを追加する方法を示しています。

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Setup new file to be added as attachment
    fileSpecification = ap.FileSpecification(attachment_file, "Sample text file")

    # Add attachment to document's attachment collection
    document.embedded_files.append(fileSpecification)

    # Save new output
    document.save(output_pdf)
```


