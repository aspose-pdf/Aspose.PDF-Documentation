---
title: 在 Ruby 中添加 JavaScript
linktitle: 在 Ruby 中添加 JavaScript
type: docs
weight: 10
url: /java/adding-javascript-in-ruby/
description: 使用 Ruby 中的 Aspose.PDF 在 PDF 中启用 JavaScript 功能，以实现交互性和自动化。
lastmod: "2026-06-09"
---
## Aspose.PDF - 添加 JavaScript

要使用 **Aspose.PDF Java for Ruby** 在 Pdf 文档中添加 JavaScript，只需调用 **AddJavaScript** 模块即可。

红宝石代码

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open a pdf document.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Adding JavaScript at Document Level

# Instantiate JavascriptAction with desried JavaScript statement

javaScript = Rjb::import('com.aspose.pdf.JavascriptAction').new("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

# Assign JavascriptAction object to desired action of Document

doc.setOpenAction(javaScript)

# Adding JavaScript at Page Level

doc.getPages().get_Item(2).getActions().setOnOpen(Rjb::import('com.aspose.pdf.JavascriptAction').new("app.alert('page 2 is opened')"))

doc.getPages().get_Item(2).getActions().setOnClose(Rjb::import('com.aspose.pdf.JavascriptAction').new("app.alert('page 2 is closed')"))

# Save PDF Document

doc.save(data_dir + "JavaScript-Added.pdf")

puts "Added JavaScript Successfully, please check the output file."
```

## 下载运行代码

从以下任何一个社交编码网站下载**添加 JavaScript (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/addjavascript.rb)
