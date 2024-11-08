---
title: Dividir Arquivo PDF em Páginas Individuais em Ruby
type: docs
weight: 80
url: /pt/java/split-pdf-file-into-individual-pages-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Dividir Páginas

Para dividir um documento PDF em páginas individuais usando **Aspose.PDF Java para Ruby**, basta invocar o módulo **SplitAllPages**.

Código Ruby

```java

# O caminho para o diretório dos documentos.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Abrir o documento de destino

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# loop através de todas as páginas

pdf_page = 1

#for (int pdfPage = 1; pdfPage<= pdfDocument1.getPages().size(); pdfPage++)

while pdf_page <= pdf.getPages().size()

# criar um novo objeto Document

new_document = Rjb::import('com.aspose.pdf.Document').new

# obter a página em um índice particular da Coleção de Páginas

new_document.getPages().add(pdf.getPages().get_Item(pdf_page))

# salvar o arquivo PDF recém-gerado

new_document.save(data_dir + "page_#{pdf_page}.pdf")

pdf_page +=1

end

puts "Processo de divisão concluído com sucesso!"
```


## Download Running Code

Baixe **Páginas Divididas (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/splitallpages.rb)