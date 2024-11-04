---
title: 在 Python 中更新页面尺寸
type: docs
weight: 90
url: /java/update-page-dimensions-in-python/
lastmod: "2021-06-05"
---

要使用 **Aspose.PDF Java for Python** 更新页面尺寸，只需调用 **UpdatePageDimensions** 类。

```python
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# 获取页面集合
page_collection = pdf.getPages()

# 获取特定页面
pdf_page = page_collection.get_Item(1)

# 将页面大小设置为 A4 (11.7 x 8.3 英寸)，在 Aspose.PDF 中，1 英寸 = 72 点
# 因此 A4 尺寸以点为单位为 (842.4, 597.6)
pdf_page.setPageSize(597.6,842.4)

# 保存新生成的 PDF 文件
pdf.save(self.dataDir + "output.pdf")

print "Dimensions updated successfully!"

```

**下载运行代码**

从以下任一社交编码网站下载 **Update Page Dimensions (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/UpdatePageDimensions/UpdatePageDimensions.py)