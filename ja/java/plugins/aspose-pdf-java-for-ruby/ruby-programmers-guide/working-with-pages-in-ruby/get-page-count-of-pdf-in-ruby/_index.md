---
title: RubyでPDFのページ数を取得
type: docs
weight: 40
url: /ja/java/get-page-count-of-pdf-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - ページ数を取得

**Aspose.PDF Java for Ruby**を使用してPdfドキュメントのページ数を取得するには、**GetNumberOfPages**モジュールを呼び出すだけです。

Rubyコード

```java
data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# PDFドキュメントを作成

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

page_count = pdf.getPages().size()

puts "ページ数:" + page_count.to_s
```

## 実行コードをダウンロード

以下のいずれかのソーシャルコーディングサイトから**Get Page Count (Aspose.PDF)**をダウンロードしてください:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/getnumberofpages.rb)