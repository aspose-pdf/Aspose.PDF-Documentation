---
title: 既存のPDFファイルにテキストを追加する (Ruby)
type: docs
weight: 20
url: ja/java/add-text-to-an-existing-pdf-file-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - テキストの追加

**Aspose.PDF Java for Ruby**を使用してPdfドキュメントにテキスト文字列を追加するには、単に**AddText**モジュールを呼び出します。

Rubyコード

```java

# ドキュメントディレクトリへのパス。

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Documentオブジェクトをインスタンス化

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# 特定のページを取得

pdf_page = doc.getPages().get_Item(1)

# テキストフラグメントを作成

text_fragment = Rjb::import('com.aspose.pdf.TextFragment').new("main text")

text_fragment.setPosition(Rjb::import('com.aspose.pdf.Position').new(100, 600))

font_repository = Rjb::import('com.aspose.pdf.FontRepository')

color = Rjb::import('com.aspose.pdf.Color')

# テキストプロパティを設定

text_fragment.getTextState().setFont(font_repository.findFont("Verdana"))

text_fragment.getTextState().setFontSize(14)

#text_fragment.getTextState().setForegroundColor(color.BLUE)

#text_fragment.getTextState().setBackgroundColor(color.GRAY)

# TextBuilderオブジェクトを作成

text_builder = Rjb::import('com.aspose.pdf.TextBuilder').new(pdf_page)

# PDFページにテキストフラグメントを追加

text_builder.appendText(text_fragment)

# PDFファイルを保存

doc.save(data_dir + "Text_Added.pdf")

puts "テキストが正常に追加されました"
```


## Download Running Code

以下のいずれかのソーシャルコーディングサイトから **Add Text (Aspose.PDF)** をダウンロードしてください:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Text/addtext.rb)