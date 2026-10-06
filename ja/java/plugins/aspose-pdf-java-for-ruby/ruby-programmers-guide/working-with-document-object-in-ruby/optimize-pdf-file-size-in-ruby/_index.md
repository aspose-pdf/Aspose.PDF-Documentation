---
title: "Ruby での PDF ファイルサイズの最適化"
linktitle: "Ruby での PDF ファイルサイズの最適化"
type: docs
weight: 80
url: /ja/java/optimize-pdf-file-size-in-ruby/
description: Aspose.PDF for Ruby を使用して、品質を損なうことなく PDF のファイルサイズを削減する方法を学びます。
lastmod: "2026-10-06"
---
## Aspose.PDF - PDF ファイルサイズの最適化

**Aspose.PDF Java for Ruby** を使用して PDF ドキュメントのファイルサイズを最適化するには、**Optimize** モジュールの **optimize_filesize** メソッドを呼び出してください。

Ruby コード

```java
 def optimize_filesize()

В В В  # The path to the documents directory.

В В В  data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

В В В  # Open a pdf document.

В В В  doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

В В В  # Optimize the file size by removing unused objects

В В В  opt = Rjb::import('aspose.document.OptimizationOptions').new

В В В  opt.setRemoveUnusedObjects(true)

В В В  opt.setRemoveUnusedStreams(true)

В В В  opt.setLinkDuplcateStreams(true)

В В В  doc.optimizeResources(opt)

В В В  # Save output document

В В В  doc.save(data_dir + "Optimized_Filesize.pdf")

В В В  puts "Optimized PDF Filesize, please check output file."

endВ
```

## 実行コードのダウンロード

ダウンロード **PDF ファイルサイズの最適化 (Aspose.PDF)** から、以下に記載されたソーシャルコーディングサイトのいずれか：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/optimize.rb)
