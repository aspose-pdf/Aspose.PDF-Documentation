---
title: 获取 PDF 文件中特定页面的 Ruby
type: docs
weight: 30
url: /java/get-a-particular-page-in-a-pdf-file-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - 获取页面

要使用 **Aspose.PDF Java for Ruby** 在 PDF 文档中获取特定页面，只需调用 **GetPage** 模块。

Ruby 代码

```java
# 文档目录的路径。

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# 打开目标文档

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# 获取页面集合中特定索引的页面

pdf_page = pdf.getPages().get_Item(1)

# 创建一个新的 Document 对象

new_document = Rjb::import('com.aspose.pdf.Document').new

# 将页面添加到新文档对象的页面集合中

new_document.getPages().add(pdf_page)

# 保存新生成的 PDF 文件

new_document.save(data_dir + "output.pdf")

puts "处理成功完成！"
```

## 下载运行代码

从以下任意一个社交编码网站下载 **Get Page (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/getpage.rb)