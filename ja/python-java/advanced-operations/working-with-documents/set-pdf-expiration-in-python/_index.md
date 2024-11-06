---
title: PythonでPDFの有効期限を設定する
type: docs
weight: 80
url: ja/python-java/set-pdf-expiration-in-python/
---

<ins>**Aspose.PDF Java for Python** を使用してPDFドキュメントの有効期限を設定するには、単に **SetExpiration** クラスを呼び出します。

**Pythonコード**
```

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

javascript = self.JavascriptAction(

"var year=2014; var month=4;today = new Date();today = new Date(today.getFullYear(), today.getMonth());expiry = new Date(year, month);if (today.getTime() > expiry.getTime())app.alert('The file is expired. You need a new one.');");

doc.setOpenAction(javascript);

# 新しい情報で更新されたドキュメントを保存します
doc.save(self.dataDir + "set_expiration.pdf");

print "ドキュメント情報を更新しました。出力ファイルを確認してください。"
```

**実行コードをダウンロードする**

以下のいずれかのソーシャルコーディングサイトから **Set PDF Expiration (Aspose.PDF)** をダウンロードしてください:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/SetExpiration/SetExpiration.py)
- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithDocumentObject/SetExpiration/SetExpiration.py)

```python
# このスクリプトは、ドキュメントの有効期限を設定する方法を示します。

import aspose.pdf as ap

# PDF ドキュメントを作成
doc = ap.Document()

# 有効期限を設定
expiration = ap.Expiration(2023, 12, 31)

# ドキュメントに有効期限を設定
doc.set_expiration(expiration)

# PDF を保存
doc.save("output.pdf")
```

- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithDocumentObject/SetExpiration/SetExpiration.md)