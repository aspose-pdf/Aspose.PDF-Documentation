---
title: Obter Propriedades da Janela do Documento e Exibição de Página em Ruby
type: docs
weight: 40
url: /pt/java/get-document-window-and-page-display-properties-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Obter Propriedades da Janela do Documento e Exibição de Página

Para Obter Propriedades da Janela do Documento e Exibição de Página de um documento Pdf usando **Aspose.PDF Java for Ruby**, simplesmente invoque o módulo **GetDocumentWindow**.

Código Ruby

```java
# O caminho para o diretório de documentos.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Abra um documento pdf.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Obter diferentes propriedades do documento

# Posição da janela do documento - Padrão: false

puts "CenterWindow :- " + doc.getCenterWindow().to_s

# Ordem de leitura predominante; determina a posição da página

# quando exibido lado a lado - Padrão: L2R

puts "Direction :- " + doc.getDirection().to_s

# Se a barra de título da janela deve exibir o título do documento.

# Se falso, a barra de título exibe o nome do arquivo PDF - Padrão: false

puts "DisplayDocTitle :- " + doc.getDisplayDocTitle().to_s

# Se deve redimensionar a janela do documento para ajustar o tamanho da

# primeira página exibida - Padrão: false

puts "FitWindow :- " + doc.getFitWindow().to_s

# Se deve ocultar a barra de menu do aplicativo visualizador - Padrão: false

puts "HideMenuBar :-" + doc.getHideMenubar().to_s

# Se deve ocultar a barra de ferramentas do aplicativo visualizador - Padrão: false

puts "HideToolBar :-" + doc.getHideToolBar().to_s

# Se deve ocultar elementos da UI como barras de rolagem

# deixando apenas o conteúdo da página exibido - Padrão: false

puts "HideWindowUI :-" + doc.getHideWindowUI().to_s

# O modo de página do documento. Como exibir o documento ao sair do modo de tela cheia.

puts "NonFullScreenPageMode :-" + doc.getNonFullScreenPageMode().to_s

# O layout da página, ou seja, página única, uma coluna

puts "PageLayout :-" + doc.getPageLayout().to_s

# Como o documento deve ser exibido quando aberto.

puts "pageMode :-" + doc.getPageMode().to_s
```


## Download Running Code

Baixar **Obter Propriedades de Janela de Documento e Exibição de Página (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/getdocumentwindow.rb)