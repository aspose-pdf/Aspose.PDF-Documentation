---
title: 获取文档窗口和页面显示属性在 Ruby 中
type: docs
weight: 40
url: zh/java/get-document-window-and-page-display-properties-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - 获取文档窗口和页面显示属性

要使用 **Aspose.PDF Java for Ruby** 获取 PDF 文档的窗口和页面显示属性，只需调用 **GetDocumentWindow** 模块。

Ruby 代码

```java
# 文档目录的路径。

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# 打开一个 pdf 文档。

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# 获取不同的文档属性

# 文档窗口的位置 - 默认值: false

puts "CenterWindow :- " + doc.getCenterWindow().to_s

# 主要阅读顺序；确定页面的位置

# 当并排显示时 - 默认值: L2R

puts "Direction :- " + doc.getDirection().to_s

# 是否窗口标题栏应显示文档标题。

# 如果为 false，标题栏显示 PDF 文件名 - 默认值: false

puts "DisplayDocTitle :- " + doc.getDisplayDocTitle().to_s

# 是否调整文档窗口的大小以适应

# 首次显示的页面大小 - 默认值: false

puts "FitWindow :- " + doc.getFitWindow().to_s

# 是否隐藏查看器应用程序的菜单栏 - 默认值: false

puts "HideMenuBar :-" + doc.getHideMenubar().to_s

# 是否隐藏查看器应用程序的工具栏 - 默认值: false

puts "HideToolBar :-" + doc.getHideToolBar().to_s

# 是否隐藏 UI 元素如滚动条

# 并仅显示页面内容 - 默认值: false

puts "HideWindowUI :-" + doc.getHideWindowUI().to_s

# 文档的页面模式。在退出全屏模式时如何显示文档。

puts "NonFullScreenPageMode :-" + doc.getNonFullScreenPageMode().to_s

# 页面布局，即单页，一列

puts "PageLayout :-" + doc.getPageLayout().to_s

# 打开文档时应如何显示。

puts "pageMode :-" + doc.getPageMode().to_s
```


## 下载运行代码

从以下任一社交编码网站下载**获取文档窗口和页面显示属性 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/getdocumentwindow.rb)