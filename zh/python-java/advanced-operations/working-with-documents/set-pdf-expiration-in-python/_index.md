---
title: 在 Python 中设置 PDF 过期
type: docs
weight: 80
url: /zh/python-java/set-pdf-expiration-in-python/
---

<ins>要使用 **Aspose.PDF Java for Python** 设置 PDF 文档的过期，只需调用 **SetExpiration** 类。

**Python 代码**
```

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

javascript = self.JavascriptAction(

"var year=2014; var month=4;today = new Date();today = new Date(today.getFullYear(), today.getMonth());expiry = new Date(year, month);if (today.getTime() > expiry.getTime())app.alert('The file is expired. You need a new one.');");

doc.setOpenAction(javascript);

# 保存更新后的文档与新信息
doc.save(self.dataDir + "set_expiration.pdf");

print "更新文档信息，请检查输出文件。"
```

**下载运行代码**

从以下任意社交编码网站下载 **Set PDF Expiration (Aspose.PDF)**：


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/SetExpiration/SetExpiration.py)
- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithDocumentObject/SetExpiration/SetExpiration.py)