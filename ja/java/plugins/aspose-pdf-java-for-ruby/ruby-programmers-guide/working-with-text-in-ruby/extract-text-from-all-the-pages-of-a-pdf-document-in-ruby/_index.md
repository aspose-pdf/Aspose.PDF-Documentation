---
title: "Ruby での PDF ドキュメントのすべてのページからテキストの抽出"
linktitle: "Ruby での PDF ドキュメントのすべてのページからテキストの抽出"
type: docs
weight: 30
url: /ja/java/extract-text-from-all-the-pages-of-a-pdf-document-in-ruby/
description: Ruby と Aspose.PDF を使用して PDF ドキュメントのすべてのページからテキストを抽出する方法を理解し、コンテンツ分析に最適です。
lastmod: "2026-10-06"
---
## Aspose.PDF - すべてのページからテキストの抽出

Ruby 用 **Aspose.PDF Java for Ruby** を使用して PDF ドキュメントのすべてのページからテキストを抽出するには、**ExtractTextFromAllPages** モジュールを呼び出してください。

Ruby コード

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# create TextAbsorber object to extract text

text_absorber = Rjb::import('com.aspose.pdf.TextAbsorber').new

# accept the absorber for all the pages

pdf.getPages().accept(text_absorber)

# In order to extract text from specific page of document, we need to specify the particular page using its index against accept(..) method.

# accept the absorber for particular PDF page

# pdfDocument.getPages().get_Item(1).accept(textAbsorber);

#get the extracted text

extracted_text = text_absorber.getText()

# create a writer and open the file

writer = Rjb::import('java.io.FileWriter').new(Rjb::import('java.io.File').new(data_dir + "extracted_text.out.txt"))

writer.write(extracted_text)

# write a line of text to the file

# tw.WriteLine(extractedText);

# close the stream

writer.close()

puts "Text extracted successfully. Check output file."
```

## 実行コードのダウンロード

**すべてのページからテキストを抽出 (Aspose.PDF)** を、以下に記載されたソーシャルコーディングサイトからダウンロードしてください。

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Text/extracttextfromallpages.rb)
