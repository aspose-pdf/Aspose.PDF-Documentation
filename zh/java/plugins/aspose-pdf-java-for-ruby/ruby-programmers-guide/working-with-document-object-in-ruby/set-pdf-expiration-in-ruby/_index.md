---
title: 在 Ruby 中设置 PDF 过期时间
linktitle: 在 Ruby 中设置 PDF 过期时间
type: docs
weight: 110
url: /java/set-pdf-expiration-in-ruby/
description: 对于时间敏感的文档，​​使用 Aspose.PDF for Ruby 在 PDF 中实现过期日期。
lastmod: "2026-06-09"
---
## Aspose.PDF - 设置 PDF 过期时间

要使用 **Aspose.PDF Java for Ruby** 设置 Pdf 文档的过期时间，只需调用 **SetExpiration** 模块即可。

红宝石代码

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

从以下任何一个社交编码网站下载**设置 PDF 过期时间 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setexpiration.rb)
