---
title: "Ruby での Web 用に PDF ドキュメントの最適化"
linktitle: "Ruby での Web 用に PDF ドキュメントの最適化"
type: docs
weight: 70
url: /ja/java/optimize-pdf-document-for-the-web-in-ruby/
description: "Ruby で Aspose.PDF を使用して、PDF の配信速度を向上させ、ファイルサイズを削減します。"
lastmod: "2026-10-06"
---
## Aspose.PDF - Web 用に PDF の最適化

Ruby 用 **Aspose.PDF Java for Ruby** を使用して PDF ドキュメントを Web 向けに最適化するには、**Optimize** モジュールの **optimize_web** メソッドを呼び出してください。

Ruby コード

```java

 def optimize_web()

В В В  # The path to the documents directory.

В В В  data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

В В В  # Open a pdf document.

В В В  doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

В В В  # Optimize for web

В В В  doc.optimize()

В В В  #Save output document

В В В  doc.save(data_dir + "Optimized_Web.pdf")

В В В  puts "Optimized PDF for the Web, please check output file."

end
```

## 実行コードのダウンロード

ダウンロード **PDF を Web 用に最適化 (Aspose.PDF)** から、以下に記載されたソーシャルコーディングサイトのいずれか：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/optimize.rb)
