---
title: 既存のPDFにTOCを追加する方法（Ruby）
type: docs
weight: 30
url: ja/java/add-toc-to-existing-pdf-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - TOCを追加

<ins>**Aspose.PDF Java for Ruby**を使用してPDFドキュメントにTOCを追加するには、単に**AddToc**モジュールを呼び出します。

Rubyコード

```java
# ドキュメントディレクトリへのパス。

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# PDFドキュメントを開く。

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# PDFファイルの最初のページにアクセスする

toc_page = doc.getPages().insert(1)

# TOC情報を表すオブジェクトを作成

toc_info = Rjb::import('com.aspose.pdf.TocInfo').new

title = Rjb::import('com.aspose.pdf.TextFragment').new("目次")

title.getTextState().setFontSize(20)

#title.getTextState().setFontStyle(Rjb::import('com.aspose.pdf.FontStyles.Bold'))

# TOCのタイトルを設定

toc_info.setTitle(title)

toc_page.setTocInfo(toc_info)

# TOC要素として使用される文字列オブジェクトを作成

titles = Array["最初のページ", "2ページ目"]

i = 0

while i < 2

    # 見出しオブジェクトを作成

    heading2 = Rjb::import('com.aspose.pdf.Heading').new(1)

    segment2 = Rjb::import('com.aspose.pdf.TextSegment').new

    heading2.setTocPage(toc_page)

    heading2.getSegments().add(segment2)

    # 見出しオブジェクトの宛先ページを指定

    heading2.setDestinationPage(doc.getPages().get_Item(i + 2))

    # 宛先ページ

    heading2.setTop(doc.getPages().get_Item(i + 2).getRect().getHeight())

    # 宛先座標

    segment2.setText(titles[i])

    # TOCを含むページに見出しを追加

    toc_page.getParagraphs().add(heading2)

    i +=1

end

# PDFドキュメントを保存

doc.save(data_dir + "TOC.pdf")

puts "TOCが正常に追加されました。出力ファイルを確認してください。"
```


## <ins> **コードを実行してダウンロード

以下のいずれかのソーシャルコーディングサイトから**Add TOC (Aspose.PDF)**をダウンロードしてください:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/addtoc.rb)