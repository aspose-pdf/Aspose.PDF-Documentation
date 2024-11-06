---
title: PDFページを画像に変換する方法（Ruby）
type: docs
weight: 20
url: ja/java/convert-pdf-pages-to-images-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - PDFページを画像に変換

**Aspose.PDF Java for Ruby**を使用してPDFドキュメントのすべてのページを画像に変換するには、単に**ConvertPagesToImages**モジュールを呼び出します。

Rubyコード

```java

# ドキュメントディレクトリへのパス。

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

converter = Rjb::import('com.aspose.pdf.facades.PdfConverter').new

converter.bindPdf(data_dir + 'input1.pdf')

converter.doConvert()

suffix = ".jpg"

image_count = 1

image_format_internal = Rjb::import('com.aspose.pdf.ImageFormatInternal')

while converter.hasNextImage()

    converter.getNextImage(data_dir + "image#{image_count}#{suffix}", image_format_internal.getJpeg())

    image_count +=1

end

puts "PDFページが個別の画像に正常に変換されました！"
```

## 実行可能コードのダウンロード

以下のいずれかのソーシャルコーディングサイトから**Convert PDF pages to Images (Aspose.PDF)**をダウンロードしてください。

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/convertpagestoimages.rb)