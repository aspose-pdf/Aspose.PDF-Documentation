---
title: PythonでPDFファイル情報を取得する
type: docs
weight: 40
url: /java/get-pdf-file-information-in-python/
lastmod: "2021-06-05"
---

**Aspose.PDF Java for Python**を使用してPdfドキュメントのファイル情報を取得するには、**GetPdfFileInfo**クラスを呼び出すだけです。

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# ドキュメント情報を取得
doc_info = doc.getInfo();

# ドキュメント情報を表示
print "著者:-" + str(doc_info.getAuthor())
print "作成日:-" + str(doc_info.getCreationDate())
print "キーワード:-" + str(doc_info.getKeywords())
print "変更日:-" + str(doc_info.getModDate())
print "件名:-" + str(doc_info.getSubject())
print "タイトル:-" + str(doc_info.getTitle())
```

**実行コードのダウンロード**

以下のいずれかのソーシャルコーディングサイトから**Get PDF File Information (Aspose.PDF)**をダウンロードしてください:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetPdfFileInfo/GetPdfFileInfo.py)