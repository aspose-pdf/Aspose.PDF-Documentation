---
title: RubyでPDFドキュメントのすべてのページからテキストを抽出する
type: docs
weight: 30
url: /ja/java/extract-text-from-all-the-pages-of-a-pdf-document-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - すべてのページからテキストを抽出する

**Aspose.PDF Java for Ruby**を使用してPDFドキュメントのすべてのページからテキストを抽出するには、単に**ExtractTextFromAllPages**モジュールを呼び出します。

Rubyコード

```java
# ドキュメントディレクトリへのパス。

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# ターゲットドキュメントを開く

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# テキストを抽出するためのTextAbsorberオブジェクトを作成

text_absorber = Rjb::import('com.aspose.pdf.TextAbsorber').new

# すべてのページに対してアブソーバを適用

pdf.getPages().accept(text_absorber)

# ドキュメントの特定のページからテキストを抽出するには、accept(..)メソッドに対して特定のページをそのインデックスを使用して指定する必要があります。

# 特定のPDFページに対してアブソーバを適用

# pdfDocument.getPages().get_Item(1).accept(textAbsorber);

# 抽出されたテキストを取得

extracted_text = text_absorber.getText()

# ライターを作成しファイルを開く

writer = Rjb::import('java.io.FileWriter').new(Rjb::import('java.io.File').new(data_dir + "extracted_text.out.txt"))

writer.write(extracted_text)

# ファイルにテキストの行を書き込む

# tw.WriteLine(extractedText);

# ストリームを閉じる

writer.close()

puts "テキストが正常に抽出されました。出力ファイルを確認してください。"
```


## コードのダウンロード

**すべてのページからテキストを抽出 (Aspose.PDF)** を以下のいずれかのソーシャルコーディングサイトからダウンロードしてください：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Text/extracttextfromallpages.rb)