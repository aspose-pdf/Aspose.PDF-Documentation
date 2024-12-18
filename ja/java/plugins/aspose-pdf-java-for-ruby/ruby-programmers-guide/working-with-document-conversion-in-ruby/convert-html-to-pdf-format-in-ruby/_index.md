---
title: HTMLをPDF形式に変換する方法（Ruby）
type: docs
weight: 10
url: /ja/java/convert-html-to-pdf-format-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - HTMLをPDF形式に変換

**Aspose.PDF Java for Ruby**を使用してHTMLをPDF形式に変換するには、単に**HtmlToPdf**モジュールを呼び出します。

Rubyコード

```java

# ドキュメントディレクトリへのパス。

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

htmloptions = Rjb::import('com.aspose.pdf.HtmlLoadOptions').new(data_dir)

# HTMLファイルを読み込む

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + "index.html", htmloptions)

# 結合された出力ファイルを保存する（ターゲットドキュメント）

pdf.save(data_dir + "html.pdf")

puts "ドキュメントが正常に変換されました"
```

## 実行コードのダウンロード

下記のいずれかのソーシャルコーディングサイトから**Convert HTML to PDF Format (Aspose.PDF)**をダウンロードしてください：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/htmltopdf.rb)