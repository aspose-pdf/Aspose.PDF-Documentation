---
title: 将SVG文件转换为Python中的PDF格式
type: docs
weight: 40
url: zh/java/convert-svg-file-to-pdf-format-in-python/
lastmod: "2021-06-05"
---

## 如何在Python中将SVG文件转换为PDF格式

要使用**Aspose.PDF Java for Python**将SVG文件转换为PDF格式，只需调用**SvgToPdf**模块。

Python代码：

```python
options = self.SvgLoadOptions();
doc=self.Document()
pdf = self.Document()
pdf=self.dataDir +'input1.pdf'
将输出保存为XLS格式
doc.save(self.dataDir + "SVG1.pdf");
print "文档已成功转换"
```

## 下载运行代码

从以下任一社交编码网站下载**Convert SVG to PDF (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentConversion/SvgToPdf/SvgToPdf.py)