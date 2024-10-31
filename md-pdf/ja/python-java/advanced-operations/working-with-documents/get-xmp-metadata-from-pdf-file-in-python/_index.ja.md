---
title: PythonでPDFファイルからXMPメタデータを取得する
type: docs
weight: 50
url: /python-java/get-xmp-metadata-from-pdf-file-in-python/
---

<ins>**Aspose.PDF Java for Python**を使用してPDFドキュメントからXMPメタデータを取得するには、**GetXMPMetadata**クラスを呼び出します。

**Python コード**
```

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# プロパティを取得
print "xmp:CreateDate: " + str(doc.getMetadata().get_Item("xmp:CreateDate"))
print "xmp:Nickname: " + str(doc.getMetadata().get_Item("xmp:Nickname"))
print "xmp:CustomProperty: " + str(doc.getMetadata().get_Item("xmp:CustomProperty"))
```

**実行コードのダウンロード**

以下のいずれかのソーシャルコーディングサイトから**Get XMP Metadata (Aspose.PDF)**をダウンロードしてください：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetXMPMetadata/GetXMPMetadata.py)

- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithDocumentObject/GetXMPMetadata/GetXMPMetadata.py)