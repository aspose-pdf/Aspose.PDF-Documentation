---
title: 设置 Ruby 中的文档窗口和页面显示属性
type: docs
weight: 100
url: /java/set-document-window-and-page-display-properties-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - 设置文档窗口和页面显示属性

要使用 **Aspose.PDF Java for Ruby** 设置 PDF 文档的窗口和页面显示属性，只需调用 **SetDocumentWindow** 模块。

Ruby 代码

```java
# 文档目录的路径。

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# 打开一个 PDF 文档。

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# 设置不同的文档属性

# 文档窗口的位置 - 默认值: false

doc.setCenterWindow(true)

# 主要阅读顺序；确定页面的位置

# 当并排显示时 - 默认值: L2R

#doc.setDirection(Rjb::import('com.aspose.pdf.Direction.L2R'))

# 窗口的标题栏是否应显示文档标题。

# 如果为 false，标题栏显示 PDF 文件名 - 默认值: false

doc.setDisplayDocTitle(true)

# 是否调整文档窗口的大小以适应

# 首个显示页面的大小 - 默认值: false

doc.setFitWindow(true)

# 是否隐藏查看器应用程序的菜单栏 - 默认值: false

doc.setHideMenubar(true)

# 是否隐藏查看器应用程序的工具栏 - 默认值: false

doc.setHideToolBar(true)

# 是否隐藏 UI 元素如滚动条

# 仅显示页面内容 - 默认值: false

doc.setHideWindowUI(true)

# 文档的页面模式。退出全屏模式时如何显示文档。

doc.setNonFullScreenPageMode(Rjb::import('com.aspose.pdf.PageMode.UseOC'))

# 页面布局，即单页，一栏

doc.setPageLayout(Rjb::import('com.aspose.pdf.PageLayout.TwoColumnLeft'))

# 打开时文档应如何显示。

doc.setPageMode()

# 保存更新的 PDF 文件

doc.save(data_dir + "Set Document Window.pdf")
```


## 下载运行代码

从以下任何一个社交编码网站下载**设置文档窗口和页面显示属性 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setdocumentwindow.rb)