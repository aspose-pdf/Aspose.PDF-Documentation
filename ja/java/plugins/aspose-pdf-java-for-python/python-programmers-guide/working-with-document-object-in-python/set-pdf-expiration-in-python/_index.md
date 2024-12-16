---
title: PythonでPDFの有効期限を設定
type: docs
weight: 80
url: /ja/java/set-pdf-expiration-in-python/
lastmod: "2021-06-05"
---

**Aspose.PDF Java for Python**を使用してPDFドキュメントの有効期限を設定するには、**SetExpiration**クラスを呼び出します。

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

javascript = self.JavascriptAction(

"var year=2021; var month=4;today = new Date();today = new Date(today.getFullYear(), today.getMonth());expiry = new Date(year, month);if (today.getTime() > expiry.getTime())app.alert('ファイルの有効期限が切れています。新しいものが必要です。');");

doc.setOpenAction(javascript);

# 新しい情報で更新されたドキュメントを保存
doc.save(self.dataDir + "set_expiration.pdf");

print "ドキュメント情報を更新しました。出力ファイルを確認してください。"
```

**実行コードをダウンロード**

以下のいずれかのソーシャルコーディングサイトから**Set PDF Expiration (Aspose.PDF)**をダウンロードしてください：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/SetExpiration/SetExpiration.py)