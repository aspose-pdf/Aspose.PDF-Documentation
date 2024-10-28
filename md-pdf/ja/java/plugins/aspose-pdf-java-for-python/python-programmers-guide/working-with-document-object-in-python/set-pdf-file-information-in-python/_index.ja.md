---
title: PythonでPDFファイル情報を設定する
type: docs
weight: 90
url: /java/set-pdf-file-information-in-python/
lastmod: "2021-06-05"
---

**Aspose.PDF Java for Python**を使用してPDFドキュメント情報を更新するには、**SetPdfFileInfo**クラスを呼び出すだけです。

```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# ドキュメント情報を取得
doc_info = doc.getInfo();

doc_info.setAuthor("Aspose.PDF for java");
doc_info.setCreationDate(datetime.today.strftime("%m/%d/%Y"));
doc_info.setKeywords("Aspose.PDF, DOM, API");
doc_info.setModDate(datetime.today.strftime("%m/%d/%Y"));
doc_info.setSubject("PDF情報");
doc_info.setTitle("PDFドキュメント情報の設定");

# 新しい情報で更新されたドキュメントを保存

doc.save(self.dataDir + "Updated_Information.pdf")
print "ドキュメント情報を更新しました。出力ファイルを確認してください。"
```

**実行コードのダウンロード**

次のいずれかのソーシャルコーディングサイトから、**Set PDF File Information (Aspose.PDF)**をダウンロードしてください：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/SetPdfFileInfo/SetPdfFileInfo.py)