---
title: 将 PDF 转换为 SVG 格式在 Python 中
type: docs
weight: 30
url: /zh/java/convert-pdf-to-svg-format-in-python/
lastmod: "2021-06-05"
---

要使用 **Aspose.PDF Java for Python** 将 PDF 转换为 SVG 格式，只需调用 **PdfToSvg** 模块。

```python

# 打开目标文档
doc=self.Document()
pdf = self.Document()
pdf=self.dataDir +'input1.pdf'

# 实例化 SvgSaveOptions 对象
save_options = self.SvgSaveOptions()

# 不将 SVG 图像压缩到 Zip 存档
save_options.CompressOutputToZipArchive = False;

# 将输出保存为 XLS 格式
doc.save(self.dataDir + "Output1.svg", save_options)

print "文档已成功转换"
```

**下载运行代码**

从以下任何一个社交编码网站下载 **Convert PDF to SVG Format (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentConversion/PdfToSvg/PdfToSvg.py)