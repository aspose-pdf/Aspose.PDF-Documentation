---
title: Converter PDF para formato DOC ou DOCX em Ruby
linktitle: Converter PDF para formato DOC ou DOCX em Ruby
type: docs
weight: 30
url: /pt/java/convert-pdf-to-doc-or-docx-format-in-ruby/
description: Aprenda como converter documentos PDF para formatos DOC ou DOCX em Ruby com Aspose.PDF, permitindo edição e processamento mais fáceis.
lastmod: "2026-10-06"
---
## Aspose.PDF - converter PDF para DOC ou DOCX

Para converter um documento PDF para o formato DOC ou DOCX usando **Aspose.PDF Java for Ruby**, basta invocar o módulo **PdfToDoc**.

Código Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# Save the concatenated output file (the target document)

pdf.save(data_dir + "output.doc")

puts "Document has been converted successfully"
```

## Baixar o exemplo de código

Baixar **Convert PDF to DOC or DOCX (Aspose.PDF)** de qualquer um dos sites de codificação social abaixo mencionados:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftodoc.rb)
