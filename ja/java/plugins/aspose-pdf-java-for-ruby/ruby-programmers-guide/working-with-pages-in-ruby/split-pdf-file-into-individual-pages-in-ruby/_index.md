---
title: Ruby で PDF ファイルを個々のページに分割する
linktitle: Ruby で PDF ファイルを個々のページに分割する
type: docs
weight: 80
url: /ja/java/split-pdf-file-into-individual-pages-in-ruby/
description: Ruby と Aspose.PDF を使用して PDF ファイルを個々のページに分割する方法を理解し、管理やコンテンツ抽出を容易にします。
lastmod: "2026-10-05"
---
## Aspose.PDF - ページ分割

**Aspose.PDF Java for Ruby** を使用して PDF ドキュメントを個々のページに分割するには、単に **SplitAllPages** モジュールを呼び出すだけです。

Ruby コード

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# loop through all the pages

pdf_page = 1

#for (int pdfPage = 1; pdfPage<= pdfDocument1.getPages().size(); pdfPage++)

while pdf_page <= pdf.getPages().size()

# create a new Document object

new_document = Rjb::import('com.aspose.pdf.Document').new

# get the page at particular index of Page Collection

new_document.getPages().add(pdf.getPages().get_Item(pdf_page))

# save the newly generated PDF file

new_document.save(data_dir + "page_#{pdf_page}.pdf")

pdf_page +=1

end

puts "Split process completed successfully!"
```

## 実行中のコードをダウンロード

ダウンロード **Split Pages (Aspose.PDF)**В fromВ 以下に記載されたソーシャルコーディングサイトのいずれかから:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/splitallpages.rb)
