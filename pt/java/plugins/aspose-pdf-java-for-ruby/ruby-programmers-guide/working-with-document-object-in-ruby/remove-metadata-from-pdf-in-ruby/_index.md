---
title: Remover metadados de PDF em Ruby
linktitle: Remover metadados de PDF em Ruby
type: docs
weight: 90
url: /java/remove-metadata-from-pdf-in-ruby/
description: Apague metadados confidenciais ou indesejados de arquivos PDF programaticamente com Aspose.PDF para Ruby.
lastmod: "2026-06-09"
---
## Aspose.PDF - Remover metadados

Para remover metadados de um documento PDF usando **Aspose.PDF Java para Ruby**, basta invocar o módulo **RemoveMetadata**.

Código Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open a pdf document.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

if doc.getMetadata().contains("pdfaid:part")

В В В  doc.getMetadata().removeItem("pdfaid:part")

endВ В  В

if doc.getMetadata().contains("dc:format")

В В В  doc.getMetadata().removeItem("dc:format")

end

# save update document with new information

doc.save(data_dir + "Remove_Metadata.pdf")

puts "Removed metadata successfully, please check output file."
```

## Baixar código em execução

Baixe **Remover metadados (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/removemetadata.rb)
