---
title: 在 Ruby 中设置 PDF 过期
linktitle: 在 Ruby 中设置 PDF 过期
type: docs
weight: 110
url: /zh/java/set-pdf-expiration-in-ruby/
description: 使用 Aspose.PDF for Ruby 在 PDF 中实现过期日期，以处理时间敏感的文档。
lastmod: "2026-10-06"
---
## Aspose.PDF - 设置 PDF 过期

要使用 **Aspose.PDF Java for Ruby** 设置 PDF 文档的过期，只需调用 **SetExpiration** 模块。

Ruby 代码

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open a pdf document.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

javascript = Rjb::import('com.aspose.pdf.JavascriptAction').new(

В В В  "var year=2014;

В В В  var month=4;

В В В  today = new Date();

В В В  today = new Date(today.getFullYear(), today.getMonth());

В В В  expiry = new Date(year, month);

В В В  if (today.getTime() > expiry.getTime())

В В В  app.alert('The file is expired. You need a new one.');")

doc.setOpenAction(javascript)

# save update document with new information

doc.save(data_dir + "set_expiration.pdf")

puts "Update document information, please check output file."
```

## 下载运行代码

下载 **Set PDF Expiration (Aspose.PDF)** 自以下列出的任意社交编码站点：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setexpiration.rb)
