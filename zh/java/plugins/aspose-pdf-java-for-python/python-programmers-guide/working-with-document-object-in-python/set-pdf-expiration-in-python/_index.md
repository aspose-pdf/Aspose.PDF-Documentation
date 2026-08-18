---
title: 在 Python 中设置 PDF 过期时间
linktitle: 在 Python 中设置 PDF 过期时间
type: docs
weight: 80
url: /java/set-pdf-expiration-in-python/
description: 了解如何使用 Aspose.PDF 在 Python 中设置 PDF 文件的到期日期，以进行时间敏感的文档访问。
lastmod: "2026-06-09"
---
要使用 **Aspose.PDF Java for Python** 设置 Pdf 文档的过期时间，只需调用 **SetExpiration** 类即可。

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

**下载运行代码**

从以下任何一个社交编码网站下载**设置 PDF 过期时间 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/SetExpiration/SetExpiration.py)
