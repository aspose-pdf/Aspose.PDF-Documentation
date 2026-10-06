---
title: "Ruby での DOMを使用したHTML文字列の追加"
linktitle: "Ruby での DOMを使用したHTML文字列の追加"
type: docs
weight: 10
url: /ja/java/add-html-string-using-dom-in-ruby/
description: RubyでDOM APIを使用し、Aspose.PDFで動的コンテンツを生成する際に、HTML文字列をPDFドキュメントに追加する方法を発見してください。
lastmod: "2026-10-06"
---
## Aspose.PDF - HTML の追加

PDFドキュメントにHTML文字列を追加するには、**Aspose.PDF Java for Ruby** を使用し、単に **AddHtml** モジュールを呼び出すだけです。

Ruby コード

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Instantiate Document object

doc = Rjb::import('com.aspose.pdf.Document').new

# Add a page to pages collection of PDF file

page = doc.getPages().add()

# Instantiate HtmlFragment with HTML contents

title = Rjb::import('com.aspose.pdf.HtmlFragment').new("<fontsize=10><b><i>Table</i></b></fontsize>")

# set MarginInfo for margin details

margin = Rjb::import('com.aspose.pdf.MarginInfo').new

margin.setBottom(10)

margin.setTop(200)

# Set margin information

title.setMargin(margin)

# Add HTML Fragment to paragraphs collection of page

page.getParagraphs().add(title)

# Save PDF file

doc.save(data_dir + "html.output.pdf")

puts "HTML added successfully"
```

## 実行中のコードのダウンロード

以下に記載されたソーシャルコーディングサイトから **Add HTML (Aspose.PDF)** をダウンロードしてください。

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Text/addhtml.rb)
