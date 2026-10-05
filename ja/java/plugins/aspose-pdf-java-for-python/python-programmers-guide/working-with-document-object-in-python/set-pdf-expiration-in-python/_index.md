---
title: "Python での PDF の有効期限の設定"
linktitle: "Python での PDF の有効期限の設定"
type: docs
weight: 80
url: /ja/java/set-pdf-expiration-in-python/
description: Aspose.PDF を使用して、時間制限付き文書アクセスのために、Python で PDF ファイルの有効期限を設定する方法を学びます。
lastmod: "2026-10-05"
---
**Aspose.PDF Java for Python** を使用して Pdf ドキュメントの有効期限を設定するには、単に **SetExpiration** クラスを呼び出します。

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

javascript = self.JavascriptAction(

"var year=2021; var month=4;today = new Date();today = new Date(today.getFullYear(), today.getMonth());expiry = new Date(year, month);if (today.getTime() > expiry.getTime())app.alert('The file is expired. You need a new one.');");

doc.setOpenAction(javascript);

# save update document with new information
doc.save(self.dataDir + "set_expiration.pdf");

print "Update document information, please check output file."
```

**実行中のコードをダウンロード**

ダウンロードВ **PDF の有効期限を設定 (Aspose.PDF)**В 以下に記載されたソーシャルコーディングサイトのいずれかから:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/SetExpiration/SetExpiration.py)
