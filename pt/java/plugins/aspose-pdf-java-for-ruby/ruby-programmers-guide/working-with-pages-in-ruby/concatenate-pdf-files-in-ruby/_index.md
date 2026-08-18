---
title: Concatenar arquivos PDF em Ruby
linktitle: Concatenar arquivos PDF em Ruby
type: docs
weight: 10
url: /java/concatenate-pdf-files-in-ruby/
description: Combine vários PDFs em um único documento usando Ruby e Aspose.PDF de forma eficiente.
lastmod: "2026-06-09"
---
## Aspose.PDF - Concatenar arquivos PDF

Para concatenar arquivos PDF usando **Aspose.PDF Java para Ruby**, basta invocar o módulo **ConcatenatePdfFiles**.

Código Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf1 = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# Open the source document

pdf2 = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input2.pdf')

# Add the pages of the source document to the target document

pdf1.getPages().add(pdf2.getPages())

# Save the concatenated output file (the target document)

pdf1.save(data_dir+ "Concatenate_output.pdf")

puts "New document has been saved, please check the output file"
```

## Baixar código em execução

Baixe **Concatenar arquivos PDF (Aspose.PDF)**Â de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/concatenatepdffiles.rb)
