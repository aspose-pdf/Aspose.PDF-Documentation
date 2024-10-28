---
title: Obter Propriedades de Janela de Documento e Exibição de Página em PHP
type: docs
weight: 30
url: /java/get-document-window-and-page-display-properties-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Obter Propriedades de Janela de Documento e Exibição de Página

Para obter as propriedades da janela do documento e exibição de página de um documento PDF usando **Aspose.PDF Java para PHP**, simplesmente invoque a classe **GetDocumentWindow**.

Código PHP

```php

# Abrir um documento pdf.
$doc = new Document($dataDir . "input1.pdf");

# Obter diferentes propriedades do documento
# Posição da janela do documento - Padrão: false
print "CenterWindow :- " . $doc->getCenterWindow() . PHP_EOL;

# Ordem de leitura predominante; determinar a posição da página
# quando exibida lado a lado - Padrão: L2R
print "Direction :- " . $doc->getDirection() . PHP_EOL;

# Se a barra de título da janela deve exibir o título do documento.
# Se falso, a barra de título exibe o nome do arquivo PDF - Padrão: false
print "DisplayDocTitle :- " . $doc->getDisplayDocTitle() . PHP_EOL;

# Se deve redimensionar a janela do documento para caber no tamanho da
# primeira página exibida - Padrão: false
print "FitWindow :- " . $doc->getFitWindow() . PHP_EOL;

# Se deve ocultar a barra de menu do aplicativo visualizador - Padrão: false
print "HideMenuBar :-" . $doc->getHideMenubar() . PHP_EOL;

# Se deve ocultar a barra de ferramentas do aplicativo visualizador - Padrão: false
print "HideToolBar :-" . $doc->getHideToolBar() . PHP_EOL;

# Se deve ocultar elementos da interface do usuário como barras de rolagem
# deixando apenas o conteúdo da página exibido - Padrão: false
print "HideWindowUI :-" . $doc->getHideWindowUI() . PHP_EOL;

# O modo de página do documento. Como exibir o documento ao sair do modo de tela cheia.
print "NonFullScreenPageMode :-" . $doc->getNonFullScreenPageMode() . PHP_EOL;

# O layout da página, ou seja, página única, uma coluna
print "PageLayout :-" . $doc->getPageLayout() . PHP_EOL;

# Como o documento deve ser exibido quando aberto.
print "pageMode :-" . $doc->getPageMode() . PHP_EOL;
```


**Baixar Código em Execução**

Baixe **Obter Propriedades da Janela do Documento e Exibição de Página (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetDocumentWindow.php)