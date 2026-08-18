---
title: Converter HTML para formato PDF em Ruby
linktitle: Converter HTML para formato PDF em Ruby
type: docs
weight: 10
url: /java/convert-html-to-pdf-format-in-ruby/
description: Aprenda como converter conteúdo HTML para formato PDF em Ruby usando Aspose.PDF para geração de documentos confiáveis ​​e precisas.
lastmod: "2026-06-09"
---
## Aspose.PDF - Converter HTML para formato PDF

Para converter HTML para formato PDF usando **Aspose.PDF Java para Ruby**, basta invocar o módulo **HtmlToPdf**.

Código Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

htmloptions = Rjb::import('com.aspose.pdf.HtmlLoadOptions').new(data_dir)

# Load HTML file

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + "index.html", htmloptions)

# Save the concatenated output file (the target document)

pdf.save(data_dir + "html.pdf")

puts "Document has been converted successfully"
```

## Baixar código em execução

Baixe **Converter HTML para formato PDF (Aspose.PDF)**Â de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/htmltopdf.rb)
