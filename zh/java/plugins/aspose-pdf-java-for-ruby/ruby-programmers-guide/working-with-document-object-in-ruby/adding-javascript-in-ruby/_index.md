---
title: 在 Ruby 中添加 JavaScript
type: docs
weight: 10
url: /zh/java/adding-javascript-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - 添加 JavaScript

要在 Pdf 文档中使用 **Aspose.PDF Java for Ruby** 添加 JavaScript，只需调用 **AddJavaScript** 模块。

Ruby 代码

```java
# 文档目录的路径。

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# 打开一个 PDF 文档。

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# 在文档级别添加 JavaScript

# 用所需的 JavaScript 语句实例化 JavascriptAction

javaScript = Rjb::import('com.aspose.pdf.JavascriptAction').new("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

# 将 JavascriptAction 对象分配给文档的所需操作

doc.setOpenAction(javaScript)

# 在页面级别添加 JavaScript

doc.getPages().get_Item(2).getActions().setOnOpen(Rjb::import('com.aspose.pdf.JavascriptAction').new("app.alert('page 2 is opened')"))

doc.getPages().get_Item(2).getActions().setOnClose(Rjb::import('com.aspose.pdf.JavascriptAction').new("app.alert('page 2 is closed')"))

# 保存 PDF 文档

doc.save(data_dir + "JavaScript-Added.pdf")

puts "成功添加 JavaScript，请检查输出文件。"
```


## 下载运行代码

从以下任一社交编码网站下载**添加JavaScript (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/addjavascript.rb)