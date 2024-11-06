---
title: PythonでPDFファイル情報を取得
type: docs
weight: 40
url: ja/python-java/get-pdf-file-information-in-python/
---

<ins>**Aspose.PDF Java for Python**を使用してPDFドキュメントのファイル情報を取得するには、単純に**GetPdfFileInfo**クラスを呼び出します。

**Pythonコード**
```

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# ドキュメント情報を取得
doc_info = doc.getInfo();

# ドキュメント情報を表示
print "Author:-" + str(doc_info.getAuthor())
print "Creation Date:-" + str(doc_info.getCreationDate())
print "Keywords:-" + str(doc_info.getKeywords())
print "Modify Date:-" + str(doc_info.getModDate())
print "Subject:-" + str(doc_info.getSubject())
print "Title:-" + str(doc_info.getTitle())
```

**実行コードのダウンロード**

以下のいずれかのソーシャルコーディングサイトから**Get PDF File Information (Aspose.PDF)**をダウンロードしてください:


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetPdfFileInfo/GetPdfFileInfo.py)
- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithDocumentObject/GetPdfFileInfo/GetPdfFileInfo.py)