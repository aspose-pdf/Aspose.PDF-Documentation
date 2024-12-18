---
title: Obter Informações do Arquivo PDF em Ruby
type: docs
weight: 50
url: /pt/java/get-pdf-file-information-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Obter Informações do Arquivo PDF

Para Obter Informações do Arquivo de um documento PDF usando **Aspose.PDF Java para Ruby**, simplesmente invoque o módulo **GetPdfFileInfo**.

Código Ruby

```java
# O caminho para o diretório dos documentos.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Abrir um documento pdf.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Obter informações do documento

doc_info = doc.getInfo()

# Mostrar informações do documento

puts "Autor:-" + doc_info.getAuthor().to_s

puts "Data de Criação:-" + doc_info.getCreationDate().to_string

puts "Palavras-chave:-" + doc_info.getKeywords().to_s

puts "Data de Modificação:-" + doc_info.getModDate().to_string

puts "Assunto:-" + doc_info.getSubject().to_s

puts "Título:-" + doc_info.getTitle().to_s
```

## Baixar Código Executável

Baixe **Obter Informações do Arquivo PDF (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/getpdffileinfo.rb)