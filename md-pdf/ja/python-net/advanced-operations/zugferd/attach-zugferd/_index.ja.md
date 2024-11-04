---
title: PDF/3-A準拠のPDFを作成し、ZUGFeRD請求書をPythonで添付する
linktitle: ZUGFeRDをPDFに添付
type: docs
weight: 10
url: /python-net/attach-zugferd/
description: Aspose.PDF for Python via .NETでZUGFeRDを使用してPDFドキュメントを生成する方法を学ぶ
lastmod: "2024-01-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## ZUGFeRDをPDFに添付

ZUGFeRDをPDFに添付するために次の手順をお勧めします:

1. Aspose.PDFライブラリをインポートし、便利のためにapというエイリアスを付けます。
1. 入力および出力PDFファイルが配置されているディレクトリへのパスを定義します。
1. 処理されるPDFファイルへのパスを定義します。
1. パス変数からPDFファイルを読み込み、Documentオブジェクトを作成します。
1. 請求書メタデータを含むXMLファイルのFileSpecificationオブジェクトを作成します。パス変数と説明文字列を使用してFileSpecificationオブジェクトを作成します。

1. FileSpecificationオブジェクトの`mime_type`プロパティと`af_relationship`プロパティをそれぞれ`text/xml`および`ALTERNATIVE`に設定します。
1. fileSpecificationオブジェクトをドキュメントオブジェクトの埋め込みファイルコレクションに追加します。これにより、XMLファイルがPDFドキュメントに請求書メタデータファイルとして添付されます。
1. PDFドキュメントをPDF/A-3A形式に変換します。ログファイルへのパス、`PdfFormat.PDF_A_3A`列挙型、および`ConvertErrorAction.DELETE`列挙型を使用してドキュメントオブジェクトを変換します。
1. 添付されたZUGFeRDと共にPDFドキュメントを保存します。

```python
import aspose.pdf as ap

# 入力および出力PDFファイルが配置されているディレクトリへのパスを定義します
_dataDir = "./"

# 処理されるPDFファイルを読み込みます
path = _dataDir + "ZUGFeRD/ZUGFeRD-test.pdf"
document = ap.Document(path)

# 請求書メタデータを含むXMLファイルのFileSpecificationオブジェクトを作成します
description = "ZUGFeRD標準に準拠した請求書メタデータ"
path = _dataDir + "ZUGFeRD/factur-x.xml"
fileSpecification = ap.FileSpecification(path, description)

# 埋め込みファイルのMIMEタイプとAFRelationshipプロパティを設定します
fileSpecification.mime_type = "text/xml"
fileSpecification.af_relationship = ap.AFRelationship.ALTERNATIVE

# 埋め込みファイルをPDFドキュメントの埋め込みファイルコレクションに追加します
document.embedded_files.add("factur",fileSpecification)

# PDFドキュメントをPDF/A-3A形式に変換します
path = _dataDir + "ZUGFeRD/log.xml"
document.convert(path, ap.PdfFormat.PDF_A_3A, ap.ConvertErrorAction.DELETE)

# 添付されたZUGFeRDと共にPDFドキュメントを保存します
path = _dataDir + "ZUGFeRD/ZUGFeRD-res.pdf"
document.save(path)
```