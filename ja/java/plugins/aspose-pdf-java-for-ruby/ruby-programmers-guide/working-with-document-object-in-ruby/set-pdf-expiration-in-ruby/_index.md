---
title: "Ruby での PDFの有効期限の設定"
linktitle: "Ruby での PDFの有効期限の設定"
type: docs
weight: 110
url: /ja/java/set-pdf-expiration-in-ruby/
description: 時間に敏感な文書のために、Aspose.PDF for Ruby を使用してPDFに有効期限を実装します。
lastmod: "2026-10-05"
---
## Aspose.PDF - PDFの有効期限の設定

**Aspose.PDF Java for Ruby** を使用して В  PDF ドキュメントの有効期限を設定するには、単に **SetExpiration** モジュールを呼び出します。

Rubyコード

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

## 実行コードをダウンロード

ダウンロードВ **Set PDF Expiration (Aspose.PDF)**В 以下に示すいずれかのソーシャルコーディングサイトから:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setexpiration.rb)
