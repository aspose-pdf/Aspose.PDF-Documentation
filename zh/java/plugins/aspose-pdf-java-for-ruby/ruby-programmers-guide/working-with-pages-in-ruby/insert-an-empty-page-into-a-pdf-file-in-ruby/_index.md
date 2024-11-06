---
title: 在 Ruby 中将空白页插入 PDF 文件
type: docs
weight: 70
url: zh/java/insert-an-empty-page-into-a-pdf-file-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - 插入空白页

要使用 **Aspose.PDF Java for Ruby** 将空白页插入到 PDF 文档中，只需调用 **InsertEmptyPage** 模块。

Ruby 代码

```java

# 文档目录的路径。

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# 打开目标文档

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# 在 PDF 中插入空白页

pdf.getPages().insert(1)

# 保存连接后的输出文件（目标文档）

pdf.save(data_dir+ "output.pdf")

puts "空白页插入成功!"
```

## 下载运行代码

从以下任一社交编码网站下载 **Insert an Empty Page (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/insertemptypage.rb)