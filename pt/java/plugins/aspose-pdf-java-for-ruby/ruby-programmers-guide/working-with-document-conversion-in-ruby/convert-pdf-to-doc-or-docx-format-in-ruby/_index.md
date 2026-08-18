---
title: Converta PDF para formato DOC ou DOCX em Ruby
linktitle: Converta PDF para formato DOC ou DOCX em Ruby
type: docs
weight: 30
url: /java/convert-pdf-to-doc-or-docx-format-in-ruby/
description: Aprenda como converter documentos PDF para formatos DOC ou DOCX em Ruby com Aspose.PDF, facilitando a edição e o processamento.
lastmod: "2026-06-09"
---
## Aspose.PDF - Converta PDF em DOC ou DOCX

Para converter um documento PDF para o formato DOC ou DOCX usando **Aspose.PDF Java para Ruby**, basta invocar o módulo **PdfToDoc**.

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

## Baixar código em execução

Baixe **Converter PDF em DOC ou DOCX (Aspose.PDF)**Â de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftodoc.rb)
