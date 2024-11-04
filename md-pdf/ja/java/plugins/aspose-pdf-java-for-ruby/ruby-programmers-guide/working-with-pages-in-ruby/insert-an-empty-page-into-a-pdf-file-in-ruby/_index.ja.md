---
title: 空のページをPDFファイルに挿入する方法（Ruby）
type: docs
weight: 70
url: /java/insert-an-empty-page-into-a-pdf-file-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - 空のページを挿入

**Aspose.PDF Java for Ruby**を使用してPDFドキュメントに空のページを挿入するには、**InsertEmptyPage**モジュールを呼び出すだけです。

Ruby コード

```java

# ドキュメントディレクトリへのパス

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# 対象のドキュメントを開く

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# PDFに空のページを挿入する

pdf.getPages().insert(1)

# 結合された出力ファイルを保存する（対象のドキュメント）

pdf.save(data_dir+ "output.pdf")

puts "空のページが正常に追加されました！"
```

## 実行コードのダウンロード

以下のいずれかのソーシャルコーディングサイトから、**Insert an Empty Page (Aspose.PDF)** をダウンロードしてください:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/insertemptypage.rb)