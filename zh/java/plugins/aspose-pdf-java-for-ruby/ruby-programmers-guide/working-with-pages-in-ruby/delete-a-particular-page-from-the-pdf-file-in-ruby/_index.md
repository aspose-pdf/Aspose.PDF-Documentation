---
title: 从 PDF 文件中删除特定页面在 Ruby 中
type: docs
weight: 20
url: zh/java/delete-a-particular-page-from-the-pdf-file-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - 删除页面

要使用 **Aspose.PDF Java for Ruby** 从 PDF 文档中删除特定页面，只需调用 **DeletePage** 模块。

Ruby 代码

```java
# 文档目录的路径。

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# 打开目标文档

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# 删除特定页面

pdf.getPages().delete(2)

# 保存新生成的 PDF 文件

pdf.save(data_dir + "output.pdf")

puts "页面删除成功！"
```

## 下载运行代码

从以下任一社交编码网站下载 **Delete Page (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/deletepage.rb)