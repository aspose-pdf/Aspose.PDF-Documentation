---
title: Insira uma página vazia no final do arquivo PDF em Ruby
linktitle: Insira uma página vazia no final do arquivo PDF em Ruby
type: docs
weight: 60
url: /java/insert-an-empty-page-at-end-of-pdf-file-in-ruby/
description: Descubra como inserir uma página vazia no final de um documento PDF usando Ruby com Aspose.PDF, adicionando flexibilidade às suas tarefas de processamento de PDF.
lastmod: "2026-06-09"
---
## Aspose.PDF - Insira uma página vazia no final do arquivo PDF

Para inserir uma página vazia no final do documento PDF usando **Aspose.PDF Java para Ruby**, basta invocar o módulo **InsertEmptyPageAtEndOfFile**.

Código Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# insert a empty page in a PDF

pdf.getPages().add()

# Save the concatenated output file (the target document)

pdf.save(data_dir+ "output.pdf")

puts "Empty page added successfully!"
```

## Baixar código em execução

Baixe **Inserir uma página vazia no final do arquivo PDF (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/insertemptypageatendoffile.rb)
