---
title: Inserir uma Página em Branco em um Arquivo PDF em Ruby
linktitle: Inserir uma Página em Branco em um Arquivo PDF em Ruby
type: docs
weight: 70
url: /pt/java/insert-an-empty-page-into-a-pdf-file-in-ruby/
description: Aprenda como inserir uma página em branco em um local específico dentro de um documento PDF usando Ruby e Aspose.PDF para gerenciamento preciso de documentos.
lastmod: "2026-10-06"
---
## Aspose.PDF - Inserir uma Página em Branco

Para Inserir uma Página em Branco em um documento Pdf usando **Aspose.PDF Java for Ruby**, basta invocar o módulo **InsertEmptyPage**.

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

Baixar\u0412\u00A0**Insert an Empty Page (Aspose.PDF)**\u0412\u00A0de\u0412\u00A0qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/insertemptypage.rb)
