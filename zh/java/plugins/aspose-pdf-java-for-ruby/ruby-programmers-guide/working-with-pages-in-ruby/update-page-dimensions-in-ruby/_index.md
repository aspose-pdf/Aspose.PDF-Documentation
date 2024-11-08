---
title: 更新页面尺寸在 Ruby
type: docs
weight: 90
url: /zh/java/update-page-dimensions-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - 更新页面尺寸

要使用 **Aspose.PDF Java for Ruby** 更新页面尺寸，只需调用 **UpdatePageDimensions** 模块。

Ruby 代码

```java

# 文档目录的路径。

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# 打开目标文档

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# 获取页面集合

page_collection = pdf.getPages()

# 获取特定页面

pdf_page = page_collection.get_Item(1)

# 将页面大小设置为 A4 (11.7 x 8.3 英寸)，在 Aspose.PDF 中，1 英寸 = 72 点

# 因此 A4 尺寸以点为单位将是 (842.4, 597.6)

pdf_page.setPageSize(597.6,842.4)

# 保存新生成的 PDF 文件

pdf.save(data_dir + "output.pdf")

puts "尺寸更新成功！"
```

## 下载运行代码

从以下任何一个社交编码网站下载 **更新页面尺寸 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/updatepagedimensions.rb)