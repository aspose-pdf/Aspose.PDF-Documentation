---
title: RubyでJavaScriptを追加する
type: docs
weight: 10
url: /ja/java/adding-javascript-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - JavaScriptの追加

**Aspose.PDF Java for Ruby**を使用してPdfドキュメントにJavaScriptを追加するには、単に**AddJavaScript**モジュールを呼び出します。

Rubyコード

```java
# ドキュメントディレクトリへのパス。

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# PDFドキュメントを開く。

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# ドキュメントレベルでJavaScriptを追加する

# 希望するJavaScriptステートメントでJavascriptActionをインスタンス化する

javaScript = Rjb::import('com.aspose.pdf.JavascriptAction').new("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

# JavascriptActionオブジェクトをドキュメントの希望するアクションに割り当てる

doc.setOpenAction(javaScript)

# ページレベルでJavaScriptを追加する

doc.getPages().get_Item(2).getActions().setOnOpen(Rjb::import('com.aspose.pdf.JavascriptAction').new("app.alert('page 2 is opened')"))

doc.getPages().get_Item(2).getActions().setOnClose(Rjb::import('com.aspose.pdf.JavascriptAction').new("app.alert('page 2 is closed')"))

# PDFドキュメントを保存する

doc.save(data_dir + "JavaScript-Added.pdf")

puts "JavaScriptが正常に追加されました。出力ファイルを確認してください。"
```


## ダウンロード実行コード

以下のいずれかのソーシャルコーディングサイトから**JavaScriptの追加 (Aspose.PDF)**をダウンロードしてください:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/addjavascript.rb)