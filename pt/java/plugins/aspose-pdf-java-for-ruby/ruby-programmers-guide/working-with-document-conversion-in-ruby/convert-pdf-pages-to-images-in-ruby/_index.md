---
title: Converter páginas PDF em Imagens em Ruby
linktitle: Converter páginas PDF em Imagens em Ruby
type: docs
weight: 20
url: /pt/java/convert-pdf-pages-to-images-in-ruby/
description: Descubra como converter páginas PDF em imagens usando Ruby com Aspose.PDF, facilitando a extração de conteúdo visual de PDFs.
lastmod: "2026-10-06"
---
## Aspose.PDF - Converter páginas PDF em Imagens

Para converter todas as páginas em imagens de um documento PDF usando **Aspose.PDF Java for Ruby**, basta invocar o módulo **ConvertPagesToImages**.

Código Ruby

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

## Baixar Código em Execução

DownloadВ **Converter páginas PDF em Imagens (Aspose.PDF)**В deВ qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/convertpagestoimages.rb)
