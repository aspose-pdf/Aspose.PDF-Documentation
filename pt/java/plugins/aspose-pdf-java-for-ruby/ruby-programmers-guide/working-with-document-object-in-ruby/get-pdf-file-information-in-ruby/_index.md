---
title: Obter informações de arquivo PDF em Ruby
linktitle: Obter informações de arquivo PDF em Ruby
type: docs
weight: 50
url: /pt/java/get-pdf-file-information-in-ruby/
description: Extrair metadados e detalhes de arquivos PDF programaticamente usando Aspose.PDF em Ruby.
lastmod: "2026-10-06"
---
## Aspose.PDF - obter informações de arquivo PDF

Para obter informações de arquivo de documento Pdf usando **Aspose.PDF Java for Ruby**, basta invocar o módulo **GetPdfFileInfo**.

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

## Baixar o exemplo de código

Download **Obter informações de arquivo PDF (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/getpdffileinfo.rb)
