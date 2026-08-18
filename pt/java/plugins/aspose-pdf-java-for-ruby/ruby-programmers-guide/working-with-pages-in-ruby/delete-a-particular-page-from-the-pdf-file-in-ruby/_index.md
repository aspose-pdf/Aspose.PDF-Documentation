---
title: Exclua uma página específica do arquivo PDF em Ruby
linktitle: Exclua uma página específica do arquivo PDF em Ruby
type: docs
weight: 20
url: /java/delete-a-particular-page-from-the-pdf-file-in-ruby/
description: Remova páginas específicas de arquivos PDF programaticamente usando Aspose.PDF para Ruby.
lastmod: "2026-06-09"
---
## Aspose.PDF - Excluir página

Para excluir uma página específica do documento PDF usando **Aspose.PDF Java for Ruby**, basta invocar o módulo **DeletePage**.

Código Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# delete a particular page

pdf.getPages().delete(2)

# save the newly generated PDF file

pdf.save(data_dir + "output.pdf")

puts "Page deleted successfully!"
```

## Baixar código em execução

Baixe **Excluir página (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/deletepage.rb)
