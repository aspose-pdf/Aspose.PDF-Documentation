---
title: Definir Informações do Arquivo PDF em Ruby
type: docs
weight: 120
url: /java/set-pdf-file-information-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Definir Informações do Arquivo PDF

Para atualizar as informações do documento PDF usando **Aspose.PDF Java for Ruby**, simplesmente invoque o módulo **SetPdfFileInfo**.

Código Ruby

```java

# O caminho para o diretório de documentos.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Abrir um documento pdf.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Obter informações do documento

doc_info = doc.getInfo()

doc_info.setAuthor("Aspose.PDF para java")

doc_info.setCreationDate(Rjb::import('java.util.Date').new)

doc_info.setKeywords("Aspose.PDF, DOM, API")

doc_info.setModDate(Rjb::import('java.util.Date').new)

doc_info.setSubject("Informações do PDF")

doc_info.setTitle("Definindo Informações do Documento PDF")

# salvar documento atualizado com novas informações

doc.save(data_dir + "Updated_Information.pdf")

puts "Atualizar informações do documento, por favor verifique o arquivo de saída."
```


## Baixar Código em Execução

Baixe **Definir Informações do Arquivo PDF (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setpdffileinfo.rb)