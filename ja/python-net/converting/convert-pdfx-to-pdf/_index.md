---
title: Python で PDF/A と PDF/UA を PDF に変換
linktitle: PDF/A および PDF/UA を PDF に変換
type: docs
weight: 120
url: /ja/python-net/convert-pdf_x-to-pdf/
lastmod: "2026-06-09"
description: .NET 経由の Aspose.PDF for Python を使用して Python の PDF ファイルから PDF/A および PDF/UA コンプライアンスを削除し、それらを標準 PDF ドキュメントとして保存する方法を学びましょう。
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Python で PDF/A と PDF/UA を標準 PDF に変換する方法
Abstract: この記事では、.NET 経由で Aspose.PDF for Python を使用して、標準ベースの PDF ドキュメントから PDF/A および PDF/UA への準拠を削除する方法について説明します。アーカイブファイルやアクセシビリティに制約のあるファイルの代わりに標準 PDF が必要な場合や、コンプライアンスメタデータと制限を削除した後で結果を保存する方法についても説明します。
---

このページは、PDF/A や PDF/UA などの標準ベースの PDF をダウンストリームの編集、処理、または再配布用に通常の PDF ドキュメントに戻す必要がある場合に使用します。

標準に準拠した PDF は、アーカイブ、印刷、アクセシビリティのワークフローに役立ちますが、場合によっては、ファイルを他のシステムやパイプラインに統合する前に、その準拠を解除する必要があります。.NET 経由の Aspose.PDF for Python では、プログラムによってその処理を行い、その結果を標準 PDF ファイルとして保存できます。

## PDF/A を PDF に変換

この例では、文書を通常の PDF ファイルとして再び保存できるように、PDF から PDF/A 準拠のメタデータと制限を削除します。

1. 「AP.ドキュメント」を使用してPDFドキュメントをロードします。
1. 「remove_pdfa_compliance ()」を呼び出して、PDF/A関連のコンプライアンス設定とメタデータをすべて削除します。
1. 結果の PDF を出力パスに保存します。

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDFA_to_PDF(infile, outfile):
    document = ap.Document(infile)
    document.remove_pdfa_compliance()
    document.save(outfile)
```

## PDF/UA コンプライアンスの削除

この例は、アクセシビリティに特化していないワークフローで文書を標準PDFとして保存できるように、PDF/UA関連のコンプライアンスを削除する方法を示しています。

1. 「AP.Document ()」を使用して PDF ドキュメントをロードします。
1. 「document.remove_pdfa_compliance ()」を呼び出して、PDF/Aの制限やコンプライアンス設定をすべて削除してください。
1. 変更した PDF を「パスアウトファイル」に保存します。

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDFUA_to_PDF(infile, outfile):
    document = ap.Document(infile)
    document.remove_pdf_ua_compliance()
    document.save(outfile)
```

## このワークフローを使用するタイミング

- PDF/A または PDF/UA の制限を必要としないツールチェーンにドキュメントを送信する前に、コンプライアンス設定を削除してください。
- アーカイブやアクセシビリティのメタデータが不要になったら、下流の文書処理を簡素化します。
- 入力 PDF を他の形式に書き出す前に正規化します。

## 関連コンバージョン

- [PDF を PDF/A、PDF/E、および PDF/X に変換](/pdf/ja/python-net/convert-pdf-to-pdf_x/) 逆のワークフローが必要で、標準に準拠したPDFを作成したい場合。
- [PDF をワードに変換](/pdf/ja/python-net/convert-pdf-to-word/) コンプライアンス制約を削除した後の編集可能な文書出力用。
- [PDF ファイルを HTML 形式に変換](/pdf/ja/python-net/convert-pdf-to-html/) 標準 PDF ファイルからのブラウザフレンドリーな出力用。
