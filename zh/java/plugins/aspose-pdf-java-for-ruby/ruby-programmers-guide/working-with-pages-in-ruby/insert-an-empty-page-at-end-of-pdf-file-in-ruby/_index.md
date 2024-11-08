---
title: 在 Ruby 中在 PDF 文件末尾插入空白页
type: docs
weight: 60
url: /zh/java/insert-an-empty-page-at-end-of-pdf-file-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - 在 PDF 文件末尾插入空白页

要在 PDF 文档末尾插入空白页，使用 **Aspose.PDF Java for Ruby**，只需调用 **InsertEmptyPageAtEndOfFile** 模块。

Ruby 代码

```java
# 文档目录的路径。

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# 打开目标文档

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# 在 PDF 中插入一个空白页

pdf.getPages().add()

# 保存合并后的输出文件（目标文档）

pdf.save(data_dir+ "output.pdf")

puts "空白页添加成功！"
```

## 下载运行代码

从以下任何一个社交编码网站下载 **Insert an Empty Page at End of PDF File (Aspose.PDF)**：


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/insertemptypageatendoffile.rb)