---
title: RubyでPDFページを画像に変換する
linktitle: RubyでPDFページを画像に変換する
type: docs
weight: 20
url: /ja/java/convert-pdf-pages-to-images-in-ruby/
description: Aspose.PDF を使用した Ruby で PDF ページを画像に変換する方法を確認し、PDF から視覚コンテンツを簡単に抽出できるようにします。
lastmod: "2026-10-05"
---
## Aspose.PDF - PDFページを画像に変換

PDF ドキュメントのすべてのページを画像に変換するには、**Aspose.PDF Java for Ruby** を使用して、単に **ConvertPagesToImages** モジュールを呼び出すだけです。

Ruby コード

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

converter = Rjb::import('com.aspose.pdf.facades.PdfConverter').new

converter.bindPdf(data_dir + 'input1.pdf')

converter.doConvert()

suffix = ".jpg"

image_count = 1

image_format_internal = Rjb::import('com.aspose.pdf.ImageFormatInternal')

while converter.hasNextImage()

В В В  converter.getNextImage(data_dir + "image#{image_count}#{suffix}", image_format_internal.getJpeg())

В В В  image_count +=1

end

puts "PDF pages are converted to individual images successfully!"
```

## 実行中のコードをダウンロード

以下に記載されたソーシャルコーディングサイトのいずれかから**Convert PDF pages to Images (Aspose.PDF)** をダウンロードしてください：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/convertpagestoimages.rb)
