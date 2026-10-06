---
title: 在 Python 中设置 PDF 过期
linktitle: 在 Python 中设置 PDF 过期
type: docs
weight: 80
url: /zh/java/set-pdf-expiration-in-python/
description: 了解如何使用 Aspose.PDF 在 Python 中为 PDF 文件设置过期日期，以实现对时间敏感的文档访问。
lastmod: "2026-10-06"
---
要使用 **Aspose.PDF Java for Python** 设置 Pdf 文档的过期，只需调用 **SetExpiration** 类。

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

下载\u0412\u00A0**设置 PDF 过期 (Aspose.PDF)**\u0412\u00A0 来自\u0412\u00A0 以下任意提到的社交编码站点:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/SetExpiration/SetExpiration.py)
