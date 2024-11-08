---
title: 在 Ruby 中设置 PDF 过期
type: docs
weight: 110
url: /zh/java/set-pdf-expiration-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - 设置 PDF 过期

要使用 **Aspose.PDF Java for Ruby** 设置 PDF 文档的过期，只需调用 **SetExpiration** 模块。

Ruby 代码

```java
# 文档目录的路径。

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# 打开一个 pdf 文档。

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

javascript = Rjb::import('com.aspose.pdf.JavascriptAction').new(

    "var year=2014;

    var month=4;

    today = new Date();

    today = new Date(today.getFullYear(), today.getMonth());

    expiry = new Date(year, month);

    if (today.getTime() > expiry.getTime())

    app.alert('文件已过期。您需要一个新的。');")

doc.setOpenAction(javascript)

# 保存带有新信息的更新文档

doc.save(data_dir + "set_expiration.pdf")

puts "更新文档信息，请检查输出文件。"
```


## 下载运行代码

从以下任一社交编码网站下载**设置PDF到期（Aspose.PDF）**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setexpiration.rb)