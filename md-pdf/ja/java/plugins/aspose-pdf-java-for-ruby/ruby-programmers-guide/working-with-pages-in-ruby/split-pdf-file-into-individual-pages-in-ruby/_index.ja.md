---
title: RubyでPDFファイルを個々のページに分割する
type: docs
weight: 80
url: /java/split-pdf-file-into-individual-pages-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - ページ分割

**Aspose.PDF Java for Ruby**を使用してPDFドキュメントを個別のページに分割するには、**SplitAllPages**モジュールを呼び出します。

Ruby コード

```java

# ドキュメントディレクトリへのパス。

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# ターゲットドキュメントを開く

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# すべてのページをループする

pdf_page = 1

#for (int pdfPage = 1; pdfPage<= pdfDocument1.getPages().size(); pdfPage++)

while pdf_page <= pdf.getPages().size()

# 新しいDocumentオブジェクトを作成

new_document = Rjb::import('com.aspose.pdf.Document').new

# ページコレクションの特定のインデックスのページを取得

new_document.getPages().add(pdf.getPages().get_Item(pdf_page))

# 新しく生成されたPDFファイルを保存

new_document.save(data_dir + "page_#{pdf_page}.pdf")

pdf_page +=1

end

puts "分割プロセスが正常に完了しました！"
```


## Download Running Code

以下のいずれかのソーシャルコーディングサイトから **Split Pages (Aspose.PDF)** をダウンロードしてください：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/splitallpages.rb)