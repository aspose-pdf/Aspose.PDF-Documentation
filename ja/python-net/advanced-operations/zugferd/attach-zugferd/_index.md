---
title: Python で PDF/3-A に準拠した PDF を作成し、ZugFerd 請求書を添付する
linktitle: PDF にツークファードを添付
type: docs
weight: 10
url: /ja/python-net/attach-zugferd/
description: .NET 経由で Python 用 Aspose.PDF で ZugFerd を使って PDF ドキュメントを生成する方法を学びましょう
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDFドキュメントにZugFerdを添付する方法
Abstract: この記事では、Aspose.PDF ライブラリを使用して ZugFerD (電子請求書用のフォーマット) を PDF 文書に添付する方法を段階的に説明します。手順は、必要なライブラリをインポートし、入出力ファイルのディレクトリパスを設定することから始まります。それには、対象の PDF ファイルを Document オブジェクトに読み込み、XML 請求書メタデータファイル用の FileSpecification オブジェクトを作成する必要があります。「mime_type」や「af_relationship」などの主要なプロパティは、メタデータが適切に統合されるように設定されています。その後、XML ファイルが PDF の埋め込みファイルコレクションに追加され、メタデータとして効果的に添付されます。その後、PDF ドキュメントは電子文書のアーカイブに適した PDF/A-3A 形式に変換され、最終的な PDF は ZugFerD が埋め込まれて保存されます。この記事の最後は、これらの手順の実装を示す Python コードスニペットで、文書管理を強化するための ZugFerd と PDF の統合を紹介しています。
---

## PDF にツークファードを添付

ZugFerdをPDFに添付するには、以下の手順をお勧めします。

1. Aspose.PDF ライブラリをインポートし、わかりやすいように ap というエイリアスを付けます。
1. 入出力 PDF ファイルが保存されているディレクトリへのパスを定義します。
1. 処理する PDF ファイルへのパスを定義します。
1. パス変数から PDF ファイルを読み込み、Document オブジェクトを作成します。
1. 請求書メタデータを含む XML ファイルの FileSpecification オブジェクトを作成します。パス変数と説明文字列を使用して FileSpecification オブジェクトを作成します。
1. を設定 `mime_type` と `af_relationship` FileSpecification オブジェクトのプロパティを `text/xml` そして `ALTERNATIVE`それぞれ。
1. FileSpecification オブジェクトをドキュメントオブジェクトの埋め込みファイルコレクションに追加します。これにより、XML ファイルが PDF ドキュメントに請求書メタデータファイルとして添付されます。
1. PDF ドキュメントを PDF/A-3A フォーマットに変換します。ログファイルへのパスを使用して、 `PdfFormat.PDF_A_3A` 列挙、および `ConvertErrorAction.DELETE` 文書オブジェクトを変換するための列挙。
1. ZugFerd が添付された PDF ドキュメントを保存します。

```python
import sys
import os
import aspose.pdf as ap

def attach_invoice_zugferd_format(infile, invoice, outfile):
    document = ap.Document(infile)

    # Create a FileSpecification object for the XML file that contains the invoice metadata
    description = "Invoice metadata conforming to ZUGFeRD standard"
    file_specification = ap.FileSpecification(invoice, description)

    # Set the MIME type and the AFRelationship properties of the embedded file
    file_specification.mime_type = "text/xml"
    file_specification.af_relationship = ap.AFRelationship.ALTERNATIVE

    # Add the embedded file to the PDF document's embedded files collection
    document.embedded_files.add("factur", file_specification)

    # Convert the PDF document to the PDF/A-3A format
    log_path = outfile.replace(".pdf", "_log.xml")
    document.convert(log_path, ap.PdfFormat.PDF_A_3A, ap.ConvertErrorAction.DELETE)
    document.save(outfile)
```
