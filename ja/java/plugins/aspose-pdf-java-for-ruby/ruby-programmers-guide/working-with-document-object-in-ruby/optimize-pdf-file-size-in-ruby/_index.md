---
title: RubyでPDFファイルサイズを最適化
type: docs
weight: 80
url: /ja/java/optimize-pdf-file-size-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - PDFファイルサイズの最適化

**Aspose.PDF Java for Ruby**を使用してPDFドキュメントのファイルサイズを最適化するには、**Optimize**モジュールの**optimize_filesize**メソッドを呼び出します。

Rubyコード

```java

 def optimize_filesize()

    # ドキュメントディレクトリへのパス。

    data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

    # PDFドキュメントを開く。

    doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

    # 未使用オブジェクトを削除してファイルサイズを最適化

    opt = Rjb::import('aspose.document.OptimizationOptions').new

    opt.setRemoveUnusedObjects(true)

    opt.setRemoveUnusedStreams(true)

    opt.setLinkDuplcateStreams(true)

    doc.optimizeResources(opt)

    # 出力ドキュメントを保存

    doc.save(data_dir + "Optimized_Filesize.pdf")

    puts "最適化されたPDFファイルサイズ、出力ファイルを確認してください。"

end 
```


## 実行コードのダウンロード

Download **PDFファイルサイズの最適化 (Aspose.PDF)** は、以下のいずれかのソーシャルコーディングサイトからダウンロードできます:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/optimize.rb)