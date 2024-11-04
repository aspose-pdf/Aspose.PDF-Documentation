---
title: PythonでPDFファイルを個々のページに分割する
type: docs
weight: 80
url: /python-java/split-pdf-file-into-individual-pages-in-python/
---

<ins>**Aspose.PDF Java for PHP**を使用してPDFドキュメントを個々のページに分割するには、単に**SplitAllPages**クラスを呼び出します。

**Pythonコード**
```

pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# すべてのページをループする
pdf_page = 1
total_size = pdf.getPages().size()
while (pdf_page <= total_size):

# 新しいDocumentオブジェクトを作成する
new_document = self.Document();

# 特定のインデックスでページコレクションのページを取得する
new_document.getPages().add(pdf.getPages().get_Item(pdf_page))

# 新しく生成されたPDFファイルを保存する
new_document.save(self.dataDir + "page_#{$pdf_page}.pdf")

pdf_page+=1

print "分割プロセスが正常に完了しました！";
```


**実行コードのダウンロード**

以下のいずれかのソーシャルコーディングサイトから**Split Pages (Aspose.PDF)**をダウンロードしてください：


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/SplitAllPages/SplitAllPages.py)
- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithPages/SplitAllPages/SplitAllPages.py)