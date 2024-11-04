---
title: RubyでPDFファイル情報を取得
type: docs
weight: 50
url: /java/get-pdf-file-information-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - PDFファイル情報を取得

**Aspose.PDF Java for Ruby**を使用してPDFドキュメントのファイル情報を取得するには、単に**GetPdfFileInfo**モジュールを呼び出します。

Rubyコード

```java
# ドキュメントディレクトリへのパス。

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# PDFドキュメントを開く。

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# ドキュメント情報を取得

doc_info = doc.getInfo()

# ドキュメント情報を表示

puts "Author:-" + doc_info.getAuthor().to_s

puts "Creation Date:-" + doc_info.getCreationDate().to_string

puts "Keywords:-" + doc_info.getKeywords().to_s

puts "Modify Date:-" + doc_info.getModDate().to_string

puts "Subject:-" + doc_info.getSubject().to_s

puts "Title:-" + doc_info.getTitle().to_s
```

## 実行コードのダウンロード

以下のいずれかのソーシャルコーディングサイトから**Get PDF File Information (Aspose.PDF)**をダウンロードしてください。

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/getpdffileinfo.rb)

```ruby
# PDFファイルの情報を取得する
def get_pdf_file_info()
    # PDFファイルを読み込む
    pdf_document = Asposepdfjava::Document.new("example.pdf")
    
    # ページ数を取得する
    number_of_pages = pdf_document.getPages().size()
    puts "ページ数: #{number_of_pages}"
    
    # タイトルを取得する
    title = pdf_document.getInfo().getTitle().to_s
    puts "タイトル: #{title}"
    
    # 作者を取得する
    author = pdf_document.getInfo().getAuthor().to_s
    puts "作者: #{author}"
    
    # 作成日を取得する
    creation_date = pdf_document.getInfo().getCreationDate().to_s
    puts "作成日: #{creation_date}"
end
```

changefreq: "monthly"  
type: docs