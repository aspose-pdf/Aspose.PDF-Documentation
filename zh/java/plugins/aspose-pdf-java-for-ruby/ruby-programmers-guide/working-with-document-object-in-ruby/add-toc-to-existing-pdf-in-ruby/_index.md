---
title: 将目录添加到现有的PDF中使用Ruby
type: docs
weight: 30
url: zh/java/add-toc-to-existing-pdf-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - 添加目录

<ins>要在Pdf文档中添加目录使用 **Aspose.PDF Java for Ruby**，只需调用 **AddToc** 模块。

Ruby 代码

```java
# 文档目录的路径。

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# 打开一个pdf文档。

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# 访问PDF文件的第一页

toc_page = doc.getPages().insert(1)

# 创建对象以表示目录信息

toc_info = Rjb::import('com.aspose.pdf.TocInfo').new

title = Rjb::import('com.aspose.pdf.TextFragment').new("目录")

title.getTextState().setFontSize(20)

#title.getTextState().setFontStyle(Rjb::import('com.aspose.pdf.FontStyles.Bold'))

# 设置目录的标题

toc_info.setTitle(title)

toc_page.setTocInfo(toc_info)

# 创建将用作目录元素的字符串对象

titles = Array["第一页", "第二页"]

i = 0

while i < 2

    # 创建标题对象

    heading2 = Rjb::import('com.aspose.pdf.Heading').new(1)

    segment2 = Rjb::import('com.aspose.pdf.TextSegment').new

    heading2.setTocPage(toc_page)

    heading2.getSegments().add(segment2)

    # 指定标题对象的目标页

    heading2.setDestinationPage(doc.getPages().get_Item(i + 2))

    # 目标页

    heading2.setTop(doc.getPages().get_Item(i + 2).getRect().getHeight())

    # 目标坐标

    segment2.setText(titles[i])

    # 将标题添加到包含目录的页面

    toc_page.getParagraphs().add(heading2)

    i +=1

end

# 保存PDF文档

doc.save(data_dir + "TOC.pdf")

puts "成功添加目录，请检查输出文件。"
```


## <ins> **下载运行代码

从以下任何一个社交编程网站下载 **Add TOC (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/addtoc.rb)