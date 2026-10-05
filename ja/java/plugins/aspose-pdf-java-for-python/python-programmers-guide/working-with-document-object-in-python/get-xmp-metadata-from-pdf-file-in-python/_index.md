---
title: "Python での PDF ファイルから XMP メタデータの取得"
linktitle: "Python での PDF ファイルから XMP メタデータの取得"
type: docs
weight: 50
url: /ja/java/get-xmp-metadata-from-pdf-file-in-python/
description: "Aspose.PDF を使用して Python で PDF ファイルから XMP メタデータを取得し、詳細なコンテンツ分析を可能にする方法をご紹介します。"
lastmod: "2026-10-06"
---
**Aspose.PDF Java for Python** を使用して PDF ドキュメントから XMP メタデータを取得するには、**GetXMPMetadata** クラスを呼び出すだけです。

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Get properties
print "xmp:CreateDate: " + str(doc.getMetadata().get_Item("xmp:CreateDate"))
print "xmp:Nickname: " + str(doc.getMetadata().get_Item("xmp:Nickname"))
print "xmp:CustomProperty: " + str(doc.getMetadata().get_Item("xmp:CustomProperty"))
```

**実行コードをダウンロード**

以下に記載されたソーシャルコーディングサイトのいずれかから、**Get XMP Metadata (Aspose.PDF)** をダウンロードしてください。

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetXMPMetadata/GetXMPMetadata.py)
