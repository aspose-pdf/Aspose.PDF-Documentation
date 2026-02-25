---
title: PythonでPDF/3-A準拠のPDFを作成し、ZUGFeRD請求書を添付する
linktitle: PDFにZUGFeRDを添付
type: docs
weight: 10
url: /ja/python-net/attach-zugferd/
description: Aspose.PDF for Python via .NETでZUGFeRD付きのPDFドキュメントを生成する方法を学びます
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDFドキュメントにZUGFeRDを添付する方法
Abstract: この記事は、Aspose.PDF ライブラリを使用して、PDF ドキュメントに ZUGFeRD（電子請求書のフォーマット）を添付する手順をステップバイステップで解説しています。手順は、必要なライブラリのインポートと入力・出力ファイル用ディレクトリパスの設定から始まります。対象の PDF ファイルを Document オブジェクトに読み込み、XML 請求書メタデータファイル用に FileSpecification オブジェクトを作成します。`mime_type` や `af_relationship` といった重要なプロパティを設定し、メタデータの適切な統合を行います。その後、XML ファイルを PDF の埋め込みファイルコレクションに追加し、メタデータとして効果的に添付します。続いて、PDF ドキュメントを PDF/A-3A 形式に変換し、電子文書の保存に適した状態にしたうえで、埋め込み ZUGFeRD を含む最終的な PDF を保存します。記事は、これらの手順の実装例を示す Python コードスニペットで締めくくり、PDF と ZUGFeRD の統合による文書管理の向上を紹介しています。
---

## PDFにZUGFeRDを添付

PDFにZUGFeRDを添付するために、以下の手順を推奨します：

1. Aspose.PDF ライブラリをインポートし、便利なようにエイリアス ap を付けます。
1. 入力および出力 PDF ファイルが格納されているディレクトリへのパスを定義します。
1. 処理対象の PDF ファイルへのパスを定義します。
1. パス変数から PDF ファイルを読み込み、Document オブジェクトを作成します。
1. 請求書メタデータを含む XML ファイル用に FileSpecification オブジェクトを作成します。パス変数と説明文字列を使用して FileSpecification オブジェクトを作成します。
1. FileSpecification オブジェクトの `mime_type` と `af_relationship` プロパティをそれぞれ `text/xml` と `ALTERNATIVE` に設定します。
1. fileSpecification オブジェクトを Document オブジェクトの埋め込みファイルコレクションに追加します。これにより XML ファイルが請求書メタデータファイルとして PDF に添付されます。
1. PDF ドキュメントを PDF/A-3A 形式に変換します。ログファイルへのパス、`PdfFormat.PDF_A_3A` 列挙体、および `ConvertErrorAction.DELETE` 列挙体を使用してドキュメントオブジェクトを変換します。
1. 添付された ZUGFeRD を含む PDF ドキュメントを保存します。

```python
import aspose.pdf as ap

# Define the path to the directory where the input and output PDF files are located
_dataDir = "./"

# Load the PDF file that will be processed
path = _dataDir + "ZUGFeRD/ZUGFeRD-test.pdf"
document = ap.Document(path)

# Create a FileSpecification object for the XML file that contains the invoice metadata
description = "Invoice metadata conforming to ZUGFeRD standard"
path = _dataDir + "ZUGFeRD/factur-x.xml"
fileSpecification = ap.FileSpecification(path, description)

# Set the MIME type and the AFRelationship properties of the embedded file
fileSpecification.mime_type = "text/xml"
fileSpecification.af_relationship = ap.AFRelationship.ALTERNATIVE

# Add the embedded file to the PDF document's embedded files collection
document.embedded_files.add("factur",fileSpecification)

# Convert the PDF document to the PDF/A-3A format
path = _dataDir + "ZUGFeRD/log.xml"
document.convert(path, ap.PdfFormat.PDF_A_3A, ap.ConvertErrorAction.DELETE)

# Save the PDF document with the attached ZUGFeRD
path = _dataDir + "ZUGFeRD/ZUGFeRD-res.pdf"
document.save(path)
```

