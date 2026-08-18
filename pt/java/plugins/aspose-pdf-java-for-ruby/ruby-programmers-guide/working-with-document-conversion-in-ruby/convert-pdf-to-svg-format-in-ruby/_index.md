---
title: Converter PDF para formato SVG em Ruby
linktitle: Converter PDF para formato SVG em Ruby
type: docs
weight: 50
url: /java/convert-pdf-to-svg-format-in-ruby/
description: Descubra como converter arquivos PDF para o formato SVG usando Ruby e Aspose.PDF, permitindo gráficos vetoriais escaláveis ​​e editáveis.
lastmod: "2026-06-09"
---
## Aspose.PDF - Converter PDF em SVG

Para converter PDF para o formato SVG usando **Aspose.PDF Java for Ruby**, basta invocar o módulo **PdfToSvg**.

Código Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# instantiate an object of SvgSaveOptions

save_options = Rjb::import('com.aspose.pdf.SvgSaveOptions').new

# do not compress SVG image to Zip archive

save_options.CompressOutputToZipArchive = false

# Save the output to XLS format

pdf.save(data_dir + "Output.svg", save_options)

puts "Document has been converted successfully"
```

## Baixar código em execução

Baixe **Converter PDF para formato SVG (Aspose.PDF)**Â de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftosvg.rb)
