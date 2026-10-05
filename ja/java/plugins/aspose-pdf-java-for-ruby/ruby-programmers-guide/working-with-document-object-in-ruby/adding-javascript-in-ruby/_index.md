---
title: "Ruby での JavaScriptの追加"
linktitle: "Ruby での JavaScriptの追加"
type: docs
weight: 10
url: /ja/java/adding-javascript-in-ruby/
description: インタラクティブ性と自動化のために、RubyでAspose.PDFを使用してPDFのJavaScript機能を有効にします。
lastmod: "2026-10-05"
---
## Aspose.PDF - JavaScriptの追加

**Aspose.PDF Java for Ruby** を使用してPDFドキュメントにJavaScriptを追加するには、単に **AddJavaScript** モジュールを呼び出します。

Rubyコード

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

## 実行コードをダウンロード

ダウンロード\u0412\u00A0**JavaScript の追加 (Aspose.PDF)**\u0412\u00A0以下に記載されたソーシャルコーディングサイトのいずれかから:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/addjavascript.rb)
