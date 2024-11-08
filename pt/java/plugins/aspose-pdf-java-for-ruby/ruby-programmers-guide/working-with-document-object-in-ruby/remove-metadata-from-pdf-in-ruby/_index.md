---
title: Remover Metadados de PDF em Ruby
type: docs
weight: 90
url: /pt/java/remove-metadata-from-pdf-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Remover Metadados

Para remover Metadados de um documento Pdf usando **Aspose.PDF Java para Ruby**, basta invocar o módulo **RemoveMetadata**.

Código Ruby

```java
# O caminho para o diretório dos documentos.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Abra um documento pdf.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

if doc.getMetadata().contains("pdfaid:part")

    doc.getMetadata().removeItem("pdfaid:part")

end    

if doc.getMetadata().contains("dc:format")

    doc.getMetadata().removeItem("dc:format")

end

# salve o documento atualizado com a nova informação

doc.save(data_dir + "Remove_Metadata.pdf")

puts "Metadados removidos com sucesso, por favor verifique o arquivo de saída."
```

## Baixar Código em Execução

Baixe **Remover Metadados (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/removemetadata.rb)