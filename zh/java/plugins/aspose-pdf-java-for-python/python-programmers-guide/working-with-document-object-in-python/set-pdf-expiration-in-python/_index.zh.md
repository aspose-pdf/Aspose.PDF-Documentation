---
title: 在 Python 中设置 PDF 到期
type: docs
weight: 80
url: /java/set-pdf-expiration-in-python/
lastmod: "2021-06-05"
---

要使用 **Aspose.PDF Java for Python** 设置 PDF 文档的到期，只需调用 **SetExpiration** 类。

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

javascript = self.JavascriptAction(

"var year=2021; var month=4;today = new Date();today = new Date(today.getFullYear(), today.getMonth());expiry = new Date(year, month);if (today.getTime() > expiry.getTime())app.alert('The file is expired. You need a new one.');");

doc.setOpenAction(javascript);

# 保存更新的文档并添加新信息
doc.save(self.dataDir + "set_expiration.pdf");

print "更新文档信息，请检查输出文件。"
```

**下载运行代码**

从以下任一社交编码网站下载 **Set PDF Expiration (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/SetExpiration/SetExpiration.py)