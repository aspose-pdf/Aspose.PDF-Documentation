---
title: PDFファイルからXMPメタデータを取得する方法（Python）
type: docs
weight: 50
url: /ja/java/get-xmp-metadata-from-pdf-file-in-python/
lastmod: "2021-06-05"
---

**Aspose.PDF Java for Python**を使用してPDFドキュメントからXMPメタデータを取得するには、**GetXMPMetadata**クラスを呼び出すだけです。

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# プロパティを取得
print "xmp:CreateDate: " + str(doc.getMetadata().get_Item("xmp:CreateDate"))
print "xmp:Nickname: " + str(doc.getMetadata().get_Item("xmp:Nickname"))
print "xmp:CustomProperty: " + str(doc.getMetadata().get_Item("xmp:CustomProperty"))
```

**実行可能なコードをダウンロード**

以下のいずれかのソーシャルコーディングサイトから、**Get XMP Metadata (Aspose.PDF)**をダウンロードできます：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetXMPMetadata/GetXMPMetadata.py)