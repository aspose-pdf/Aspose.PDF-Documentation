---
title: Concatenate arquivos PDF em Ruby
type: docs
weight: 10
url: /pt/java/concatenate-pdf-files-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Concatenate arquivos PDF

Para concatenar arquivos PDF usando **Aspose.PDF Java para Ruby**, simplesmente invoque o módulo **ConcatenatePdfFiles**.

Código Ruby

```java
# O caminho para o diretório de documentos.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Abra o documento de destino

pdf1 = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# Abra o documento de origem

pdf2 = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input2.pdf')

# Adicione as páginas do documento de origem ao documento de destino

pdf1.getPages().add(pdf2.getPages())

# Salve o arquivo de saída concatenado (o documento de destino)

pdf1.save(data_dir+ "Concatenate_output.pdf")

puts "Novo documento foi salvo, por favor verifique o arquivo de saída"
```

## Baixar Código em Execução

Baixe **Concatenate PDF Files (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/concatenatepdffiles.rb)