---
title: "Ruby での PDF のページ数の取得"
linktitle: "Ruby での PDF のページ数の取得"
type: docs
weight: 40
url: /ja/java/get-page-count-of-pdf-in-ruby/
description: "Aspose.PDF を使用した Ruby で、プログラム的に PDF ドキュメントの総ページ数を取得します。"
lastmod: "2026-10-06"
---
## Aspose.PDF - ページ数の取得

Pdf ドキュメントのページ数を取得するには、**Aspose.PDF Java for Ruby** を使用して、単に **GetNumberOfPages** モジュールを呼び出すだけです。

Ruby コード

```java
data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Create PDF document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

page_count = pdf.getPages().size()

puts "Page Count:" + page_count.to_s
```

## 実行コードのダウンロード

**Get Page Count (Aspose.PDF)** を、以下に記載されたいずれかのソーシャルコーディングサイトからダウンロードしてください。

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/getnumberofpages.rb)
