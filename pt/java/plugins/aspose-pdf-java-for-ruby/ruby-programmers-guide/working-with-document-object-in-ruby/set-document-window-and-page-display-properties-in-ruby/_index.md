---
title: Definir Propriedades de Janela e Exibição de Página do Documento em Ruby
type: docs
weight: 100
url: /pt/java/set-document-window-and-page-display-properties-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Definir Propriedades de Janela e Exibição de Página do Documento

Para definir as propriedades de janela e exibição de página do documento PDF usando **Aspose.PDF Java para Ruby**, basta invocar o módulo **SetDocumentWindow**.

Código Ruby

```java
# O caminho para o diretório de documentos.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Abra um documento pdf.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Definir diferentes propriedades do documento

# Posição da janela do documento - Padrão: false

doc.setCenterWindow(true)

# Ordem de leitura predominante; determina a posição da página

# quando exibido lado a lado - Padrão: L2R

#doc.setDirection(Rjb::import('com.aspose.pdf.Direction.L2R'))

# Se a barra de título da janela deve exibir o título do documento.

# Se falso, a barra de título exibe o nome do arquivo PDF - Padrão: false

doc.setDisplayDocTitle(true)

# Se deve redimensionar a janela do documento para ajustar o tamanho da

# primeira página exibida - Padrão: false

doc.setFitWindow(true)

# Se deve ocultar a barra de menu do aplicativo visualizador - Padrão: false

doc.setHideMenubar(true)

# Se deve ocultar a barra de ferramentas do aplicativo visualizador - Padrão: false

doc.setHideToolBar(true)

# Se deve ocultar elementos da interface do usuário como barras de rolagem

# deixando apenas o conteúdo da página exibido - Padrão: false

doc.setHideWindowUI(true)

# O modo de página do documento. Como exibir o documento ao sair do modo de tela cheia.

doc.setNonFullScreenPageMode(Rjb::import('com.aspose.pdf.PageMode.UseOC'))

# O layout da página, ou seja, página única, uma coluna

doc.setPageLayout(Rjb::import('com.aspose.pdf.PageLayout.TwoColumnLeft'))

# Como o documento deve ser exibido quando aberto.

doc.setPageMode()

# Salvar arquivo PDF atualizado

doc.save(data_dir + "Set Document Window.pdf")
```


## Download Running Code

Baixar **Definir Propriedades da Janela do Documento e Exibição de Página (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setdocumentwindow.rb)