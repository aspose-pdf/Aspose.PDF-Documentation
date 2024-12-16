---
title: Adicionar TOC ao PDF Existente em Ruby
type: docs
weight: 30
url: /pt/java/add-toc-to-existing-pdf-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Adicionar TOC

<ins>Para adicionar TOC em um documento PDF usando **Aspose.PDF Java para Ruby**, simplesmente invoque o módulo **AddToc**.

Código Ruby

```java
# O caminho para o diretório de documentos.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Abra um documento pdf.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Obtenha acesso à primeira página do arquivo PDF

toc_page = doc.getPages().insert(1)

# Crie um objeto para representar as informações do TOC

toc_info = Rjb::import('com.aspose.pdf.TocInfo').new

title = Rjb::import('com.aspose.pdf.TextFragment').new("Índice")

title.getTextState().setFontSize(20)

#title.getTextState().setFontStyle(Rjb::import('com.aspose.pdf.FontStyles.Bold'))

# Defina o título para o TOC

toc_info.setTitle(title)

toc_page.setTocInfo(toc_info)

# Crie objetos de string que serão usados como elementos do TOC

titles = Array["Primeira página", "Segunda página"]

i = 0

while i < 2

    # Crie objeto de Cabeçalho

    heading2 = Rjb::import('com.aspose.pdf.Heading').new(1)

    segment2 = Rjb::import('com.aspose.pdf.TextSegment').new

    heading2.setTocPage(toc_page)

    heading2.getSegments().add(segment2)

    # Especificar a página de destino para o objeto de cabeçalho

    heading2.setDestinationPage(doc.getPages().get_Item(i + 2))

    # Página de destino

    heading2.setTop(doc.getPages().get_Item(i + 2).getRect().getHeight())

    # Coordenada de destino

    segment2.setText(titles[i])

    # Adicionar cabeçalho à página contendo TOC

    toc_page.getParagraphs().add(heading2)

    i +=1

end

# Salvar Documento PDF

doc.save(data_dir + "TOC.pdf")

puts "TOC adicionado com sucesso, por favor verifique o arquivo de saída."
```


## <ins> **Baixar Código em Execução

Baixe **Adicionar TOC (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/addtoc.rb)