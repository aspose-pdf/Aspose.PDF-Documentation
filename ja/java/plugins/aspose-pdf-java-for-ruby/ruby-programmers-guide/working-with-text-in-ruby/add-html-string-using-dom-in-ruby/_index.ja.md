---
title: RubyでDOMを使用してHTML文字列を追加
type: docs
weight: 10
url: /java/add-html-string-using-dom-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - HTMLを追加

**Aspose.PDF Java for Ruby**を使用してPdfドキュメントにHTML文字列を追加するには、単に**AddHtml**モジュールを呼び出します。

Rubyコード

```java
# ドキュメントディレクトリへのパス。

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Documentオブジェクトをインスタンス化

doc = Rjb::import('com.aspose.pdf.Document').new

# PDFファイルのページコレクションにページを追加

page = doc.getPages().add()

# HTML内容を持つHtmlFragmentをインスタンス化

title = Rjb::import('com.aspose.pdf.HtmlFragment').new("<fontsize=10><b><i>Table</i></b></fontsize>")

# マージンの詳細のためにMarginInfoを設定

margin = Rjb::import('com.aspose.pdf.MarginInfo').new

margin.setBottom(10)

margin.setTop(200)

# マージン情報を設定

title.setMargin(margin)

# ページの段落コレクションにHTMLフラグメントを追加

page.getParagraphs().add(title)

# PDFファイルを保存

doc.save(data_dir + "html.output.pdf")

puts "HTMLが正常に追加されました"
```


## ダウンロード実行コード

以下のいずれかのソーシャルコーディングサイトから**Add HTML (Aspose.PDF)**をダウンロードしてください：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Text/addhtml.rb)