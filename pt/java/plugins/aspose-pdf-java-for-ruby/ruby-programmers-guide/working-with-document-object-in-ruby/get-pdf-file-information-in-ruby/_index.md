---
title: Obtenha informações do arquivo PDF em Ruby
linktitle: Obtenha informações do arquivo PDF em Ruby
type: docs
weight: 50
url: /java/get-pdf-file-information-in-ruby/
description: Extraia metadados e detalhes de arquivos PDF programaticamente usando Aspose.PDF em Ruby.
lastmod: "2026-06-09"
---
## Aspose.PDF - Obtenha informações do arquivo PDF

Para obter informações do arquivo do documento PDF usando **Aspose.PDF Java para Ruby**, basta invocar o módulo **GetPdfFileInfo**.

Código Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open a pdf document.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Get document information

doc_info = doc.getInfo()

# Show document information

puts "Author:-" + doc_info.getAuthor().to_s

puts "Creation Date:-" + doc_info.getCreationDate().to_string

puts "Keywords:-" + doc_info.getKeywords().to_s

puts "Modify Date:-" + doc_info.getModDate().to_string

puts "Subject:-" + doc_info.getSubject().to_s

puts "Title:-" + doc_info.getTitle().to_s
```

## Baixar código em execução

Baixe ** Obtenha informações do arquivo PDF (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/getpdffileinfo.rb)
