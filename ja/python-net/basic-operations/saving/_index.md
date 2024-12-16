---
title: プログラムでPDFドキュメントを保存
linktitle: PDFを保存
type: docs
weight: 30
url: /ja/python-net/save-pdf-document/
description: Python Aspose.PDF for Python via .NETライブラリでPDFファイルを保存する方法を学びます。ファイルシステム、ストリーム、およびWebアプリケーションにPDFドキュメントを保存します。
lastmod: "2022-12-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## ファイルシステムにPDFドキュメントを保存

[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) クラスの [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) メソッドを使用して、作成または操作したPDFドキュメントをファイルシステムに保存できます。

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    # いくつかの操作を行う、例：新しい空のページを追加
    document.pages.add()
    document.save(output_pdf)
```

## ストリームにPDFドキュメントを保存

`Save` メソッドのオーバーロードを使用して、作成または操作したPDFドキュメントをストリームに保存することもできます。

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    # いくつかの操作を行う、例：新しい空のページを追加
    document.pages.add()
    document.save(io.FileIO(output_pdf, 'w'))
```


## PDF/A または PDF/X 形式で保存

PDF/A は、電子文書のアーカイブおよび長期保存に使用される ISO 標準化されたポータブル文書形式 (PDF) のバージョンです。 PDF/A は、フォントのリンク（フォントの埋め込みとは対照的）や暗号化など、長期アーカイブに適さない機能を禁止している点で PDF とは異なります。 PDF/A ビューアの ISO 要件には、カラーマネージメントガイドライン、埋め込みフォントのサポート、および埋め込み注釈を読むためのユーザーインターフェイスが含まれます。

PDF/X は PDF ISO 標準のサブセットです。 PDF/X の目的はグラフィックス交換を容易にすることであり、そのため標準の PDF ファイルには適用されない一連の印刷関連要件があります。

どちらの場合も、[save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) メソッドを使用して文書を保存しますが、文書は [convert](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) メソッドを使用して準備する必要があります。

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    document.pages.add()
    document.convert(output_log, ap.PdfFormat.PDF_X_3, ap.ConvertErrorAction.DELETE)
    document.save(output_pdf)
```