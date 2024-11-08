---
title: PythonでPDFからメタデータを削除
type: docs
weight: 70
url: /ja/python-java/remove-metadata-from-pdf-in-python/
---

<ins>**Aspose.PDF Java for Python**を使用してPDFドキュメントからメタデータを削除するには、単に**RemoveMetadata**クラスを呼び出します。

**Pythonコード**
```

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

if (re.findall('/pdfaid:part/',doc.getMetadata())):
doc.getMetadata().removeItem("pdfaid:part")


if (re.findall('/dc:format/',doc.getMetadata())):
doc.getMetadata().removeItem("dc:format")


# 新しい情報を含む更新されたドキュメントを保存
doc.save(self.dataDir + "Remove_Metadata.pdf")

print "メタデータを正常に削除しました。出力ファイルを確認してください。"
```

**実行コードのダウンロード**

以下のいずれかのソーシャルコーディングサイトから**Remove Metadata (Aspose.PDF)**をダウンロードしてください：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/RemoveMetadata/RemoveMetadata.py)

- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithDocumentObject/RemoveMetadata/RemoveMetadata.py)