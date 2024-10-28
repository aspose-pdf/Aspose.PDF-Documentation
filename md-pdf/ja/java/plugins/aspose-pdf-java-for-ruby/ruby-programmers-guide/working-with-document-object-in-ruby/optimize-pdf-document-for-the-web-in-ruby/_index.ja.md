---
title: Web用にPDFドキュメントを最適化する方法（Ruby）
type: docs
weight: 70
url: /java/optimize-pdf-document-for-the-web-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - PDFをWeb用に最適化

**Aspose.PDF Java for Ruby**を使用してPDFドキュメントをWeb用に最適化するには、**Optimize**モジュールの**optimize_web**メソッドを呼び出します。

Rubyコード

```java

 def optimize_web()

    # ドキュメントディレクトリへのパス。

    data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

    # PDFドキュメントを開く。

    doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

    # Web用に最適化

    doc.optimize()

    # 出力ドキュメントを保存

    doc.save(data_dir + "Optimized_Web.pdf")

    puts "Web用にPDFを最適化しました。出力ファイルを確認してください。"

end
``` 

## 実行コードのダウンロード

以下のいずれかのソーシャルコーディングサイトから**Optimize PDF for Web (Aspose.PDF)**をダウンロードしてください：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/optimize.rb)