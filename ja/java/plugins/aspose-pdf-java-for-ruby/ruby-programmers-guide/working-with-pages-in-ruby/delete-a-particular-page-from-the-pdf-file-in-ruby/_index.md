---
title: RubyでPDFファイルから特定のページを削除
type: docs
weight: 20
url: /ja/java/delete-a-particular-page-from-the-pdf-file-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - ページ削除

**Aspose.PDF Java for Ruby**を使用してPDFドキュメントから特定のページを削除するには、**DeletePage**モジュールを呼び出すだけです。

Rubyコード

```java
# ドキュメントディレクトリへのパス。

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# 対象ドキュメントを開く

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# 特定のページを削除

pdf.getPages().delete(2)

# 新しく生成されたPDFファイルを保存

pdf.save(data_dir + "output.pdf")

puts "ページが正常に削除されました！"
```

## 実行コードのダウンロード

以下のいずれかのソーシャルコーディングサイトから**Delete Page (Aspose.PDF)**をダウンロードしてください：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/deletepage.rb)