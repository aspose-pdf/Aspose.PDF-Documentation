---
title: Rubyでページ寸法を更新
type: docs
weight: 90
url: /java/update-page-dimensions-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - ページ寸法を更新

**Aspose.PDF Java for Ruby** を使用してページ寸法を更新するには、単に **UpdatePageDimensions** モジュールを呼び出します。

Rubyコード

```java

# ドキュメントディレクトリへのパス。

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# 対象ドキュメントを開く

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# ページコレクションを取得

page_collection = pdf.getPages()

# 特定のページを取得

pdf_page = page_collection.get_Item(1)

# ページサイズをA4（11.7 x 8.3インチ）に設定し、Aspose.PDFでは1インチ = 72ポイント

# したがって、A4の寸法はポイントで (842.4, 597.6) になります

pdf_page.setPageSize(597.6,842.4)

# 新しく生成されたPDFファイルを保存

pdf.save(data_dir + "output.pdf")

puts "寸法が正常に更新されました!"
```

## 実行コードのダウンロード

以下のいずれかのソーシャルコーディングサイトから **Update Page Dimensions (Aspose.PDF)** をダウンロードしてください。

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/updatepagedimensions.rb)

```ruby
# ページの寸法を更新するサンプルコード
require 'java'

# Java ライブラリのインポート
java_import 'com.aspose.pdf.Document'
java_import 'com.aspose.pdf.PageSize'

# PDF ドキュメントをロード
pdf_document = Document.new("input.pdf")

# 最初のページを取得
page = pdf_document.getPages().get_Item(1)

# ページの寸法を設定
page.setPageSize(PageSize.A4.getWidth(), PageSize.A4.getHeight())

# PDF ドキュメントを保存
pdf_document.save("output.pdf")