---
title: 在 Python 中更新页面尺寸
type: docs
weight: 90
url: zh/python-java/update-page-dimensions-in-python/
---

<ins>要使用 **Aspose.PDF Java for Python** 更新页面尺寸，只需调用 **UpdatePageDimensions** 类。

**Python 代码**
```s
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# 获取页面集合
page_collection = pdf.getPages()

# 获取特定页面
pdf_page = page_collection.get_Item(1)

# 将页面大小设置为 A4 (11.7 x 8.3 英寸)，在 Aspose.PDF 中，1 英寸 = 72 点
# 因此 A4 的尺寸将是 (842.4, 597.6)
pdf_page.setPageSize(597.6,842.4)

# 保存新生成的 PDF 文件
pdf.save(self.dataDir + "output.pdf")

print "尺寸更新成功！"

```

**下载运行代码**

从以下任意一个社交编码网站下载 **Update Page Dimensions (Aspose.PDF)**：


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/UpdatePageDimensions/UpdatePageDimensions.py)
- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithPages/UpdatePageDimensions/UpdatePageDimensions.py)