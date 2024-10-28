---
title: 将 PDF 文件拆分为单独页面在 Ruby 中
type: docs
weight: 80
url: /java/split-pdf-file-into-individual-pages-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - 拆分页面

要使用 **Aspose.PDF Java for Ruby** 将 PDF 文档拆分为单独的页面，只需调用 **SplitAllPages** 模块。

Ruby 代码

```java

# 文档目录的路径。

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# 打开目标文档

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# 遍历所有页面

pdf_page = 1

#for (int pdfPage = 1; pdfPage<= pdfDocument1.getPages().size(); pdfPage++)

while pdf_page <= pdf.getPages().size()

# 创建一个新的 Document 对象

new_document = Rjb::import('com.aspose.pdf.Document').new

# 在页面集合中获取特定索引的页面

new_document.getPages().add(pdf.getPages().get_Item(pdf_page))

# 保存新生成的 PDF 文件

new_document.save(data_dir + "page_#{pdf_page}.pdf")

pdf_page +=1

end

puts "拆分过程成功完成！"
```


## 下载运行代码

从以下任一社交编程网站下载 **拆分页面 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/splitallpages.rb)