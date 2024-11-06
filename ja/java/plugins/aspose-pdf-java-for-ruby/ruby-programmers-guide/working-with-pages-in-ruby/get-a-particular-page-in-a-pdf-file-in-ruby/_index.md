---
title: PDFファイル内の特定のページをRubyで取得
type: docs
weight: 30
url: ja/java/get-a-particular-page-in-a-pdf-file-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - ページを取得

**Aspose.PDF Java for Ruby**を使用してPDFドキュメント内の特定のページを取得するには、**GetPage**モジュールを呼び出します。

Rubyコード

```java
# ドキュメントディレクトリへのパス。

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# 対象のドキュメントを開く

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# ページコレクションの特定のインデックスのページを取得する

pdf_page = pdf.getPages().get_Item(1)

# 新しいDocumentオブジェクトを作成する

new_document = Rjb::import('com.aspose.pdf.Document').new

# 新しいドキュメントオブジェクトのページコレクションにページを追加する

new_document.getPages().add(pdf_page)

# 新しく生成されたPDFファイルを保存する

new_document.save(data_dir + "output.pdf")

puts "プロセスが正常に完了しました！"
```

## 実行コードをダウンロード

以下に記載されたいずれかのソーシャルコーディングサイトから**Get Page (Aspose.PDF)**をダウンロードしてください。

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/getpage.rb)