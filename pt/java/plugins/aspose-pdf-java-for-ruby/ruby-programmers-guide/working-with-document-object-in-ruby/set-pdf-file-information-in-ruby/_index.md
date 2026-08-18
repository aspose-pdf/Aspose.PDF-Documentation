---
title: Definir informações do arquivo PDF em Ruby
linktitle: Definir informações do arquivo PDF em Ruby
type: docs
weight: 120
url: /java/set-pdf-file-information-in-ruby/
description: Defina e atualize programaticamente metadados de PDF como título, autor e palavras-chave usando Ruby.
lastmod: "2026-06-09"
---
## Aspose.PDF - Definir informações do arquivo PDF

Para atualizar as informações do documento PDF usando **Aspose.PDF Java para Ruby**, basta invocar o módulo **SetPdfFileInfo**.

Código Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open a pdf document.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Get document information

doc_info = doc.getInfo()

doc_info.setAuthor("Aspose.PDF for java")

doc_info.setCreationDate(Rjb::import('java.util.Date').new)

doc_info.setKeywords("Aspose.PDF, DOM, API")

doc_info.setModDate(Rjb::import('java.util.Date').new)

doc_info.setSubject("PDF Information")

doc_info.setTitle("Setting PDF Document Information")

# save update document with new information

doc.save(data_dir + "Updated_Information.pdf")

puts "Update document information, please check output file."
```

## Baixar código em execução

Baixe **Definir informações do arquivo PDF (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setpdffileinfo.rb)
