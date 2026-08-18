---
title: Insira uma página vazia em um arquivo PDF em Ruby
linktitle: Insira uma página vazia em um arquivo PDF em Ruby
type: docs
weight: 70
url: /java/insert-an-empty-page-into-a-pdf-file-in-ruby/
description: Aprenda como inserir uma página vazia em um local específico em um documento PDF usando Ruby e Aspose.PDF para gerenciamento preciso de documentos.
lastmod: "2026-06-09"
---
## Aspose.PDF - Insira uma página vazia

Para inserir uma página vazia em um documento PDF usando **Aspose.PDF Java para Ruby**, basta invocar o módulo **InsertEmptyPage**.

Código Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# insert a empty page in a PDF

pdf.getPages().insert(1)

# Save the concatenated output file (the target document)

pdf.save(data_dir+ "output.pdf")

puts "Empty page added successfully!"
```

## Baixar código em execução

Baixe **Insira uma página vazia (Aspose.PDF)**Â de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/insertemptypage.rb)
