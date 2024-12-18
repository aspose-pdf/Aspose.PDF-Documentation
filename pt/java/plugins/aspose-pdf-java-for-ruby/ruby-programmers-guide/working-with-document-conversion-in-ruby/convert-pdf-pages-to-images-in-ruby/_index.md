---
title: Converter páginas de PDF em Imagens em Ruby
type: docs
weight: 20
url: /pt/java/convert-pdf-pages-to-images-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Converter páginas de PDF em Imagens

Para converter todas as páginas de um documento PDF em Imagens usando **Aspose.PDF Java para Ruby**, simplesmente invoque o módulo **ConvertPagesToImages**.

Código Ruby

```java

# O caminho para o diretório dos documentos.

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

puts "As páginas do PDF foram convertidas em imagens individuais com sucesso!"
```

## Baixar Código em Execução

Baixe **Converter páginas de PDF em Imagens (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/convertpagestoimages.rb)