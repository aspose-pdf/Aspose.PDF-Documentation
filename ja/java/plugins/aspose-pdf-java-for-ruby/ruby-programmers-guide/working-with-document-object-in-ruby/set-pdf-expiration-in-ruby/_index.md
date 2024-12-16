---
title: RubyでPDFの有効期限を設定する
type: docs
weight: 110
url: /ja/java/set-pdf-expiration-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - PDFの有効期限を設定する

**Aspose.PDF Java for Ruby**を使用してPDFドキュメントの有効期限を設定するには、**SetExpiration**モジュールを呼び出すだけです。

Rubyコード

```java
# ドキュメントディレクトリへのパス。

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# PDFドキュメントを開く。

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

javascript = Rjb::import('com.aspose.pdf.JavascriptAction').new(

    "var year=2014;

    var month=4;

    today = new Date();

    today = new Date(today.getFullYear(), today.getMonth());

    expiry = new Date(year, month);

    if (today.getTime() > expiry.getTime())

    app.alert('ファイルの有効期限が切れています。新しいファイルが必要です。');")

doc.setOpenAction(javascript)

# 新しい情報で更新されたドキュメントを保存する

doc.save(data_dir + "set_expiration.pdf")

puts "ドキュメント情報を更新しました。出力ファイルを確認してください。"
```


## ダウンロード実行コード

以下のいずれかのソーシャルコーディングサイトから**Set PDF Expiration (Aspose.PDF)**をダウンロードしてください：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setexpiration.rb)