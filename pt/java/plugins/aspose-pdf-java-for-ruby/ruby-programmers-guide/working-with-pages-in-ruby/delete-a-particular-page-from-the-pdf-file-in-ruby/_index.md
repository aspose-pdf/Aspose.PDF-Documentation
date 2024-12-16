---
title: Excluir uma Página Particular do Arquivo PDF em Ruby
type: docs
weight: 20
url: /pt/java/delete-a-particular-page-from-the-pdf-file-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Excluir Página

Para excluir uma Página Particular do documento PDF usando **Aspose.PDF Java para Ruby**, basta invocar o módulo **DeletePage**.

Código Ruby

```java
# O caminho para o diretório de documentos.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Abrir o documento alvo

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# excluir uma página particular

pdf.getPages().delete(2)

# salvar o arquivo PDF recém-gerado

pdf.save(data_dir + "output.pdf")

puts "Página excluída com sucesso!"
```

## Baixar Código em Execução

Baixar **Excluir Página (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/deletepage.rb)