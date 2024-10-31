---
title: Formatação de Documento PDF
linktitle: Formatação de Documento PDF
type: docs
weight: 20
url: /php-java/formatting-pdf-document/
description: Formate o Documento PDF com Aspose.PDF para PHP via Java. Use o próximo trecho de código para resolver suas tarefas.
lastmod: "2024-06-05"
---

## Obter Propriedades da Janela do Documento e Exibição de Página

Este tópico ajuda você a entender como obter as propriedades da janela do documento, do aplicativo visualizador e como as páginas são exibidas.

Para definir estas diferentes propriedades, abra o arquivo PDF usando a classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Agora você pode obter os métodos do objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document), tais como

- [isCenterWindow](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#isCenterWindow--) – Centraliza a janela do documento na tela. Padrão: false.
- [setDirection](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setDirection-int-) – Ordem de leitura.
 Isso determina como as páginas são dispostas quando exibidas lado a lado. Padrão: da esquerda para a direita.  
- [isDisplayDocTitle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#isDisplayDocTitle--) – Exibir o título do documento na barra de título da janela do documento. Padrão: false (o título é exibido).  
- [isHideMenubar](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#isHideMenubar--) – Obtém a flag especificando se a barra de menu deve ser escondida quando o documento está ativo.  
- [isHideToolBar](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#isHideToolBar--) – Obtém a flag especificando se a barra de ferramentas deve ser escondida quando o documento está ativo.  
- [isHideWindowUI](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#isHideWindowUI--) – Obtém a flag especificando se os elementos da interface do usuário devem ser escondidos quando o documento está ativo.

- [getNonFullScreenPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#getNonFullScreenPageMode--) – Obtém o modo de página, especificando como exibir o documento ao sair do modo de tela cheia.- [getPageLayout](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#getPageLayout--) – O layout da página.
- [getPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#getPageMode--) – Obtém o modo da página, especificando como o documento deve ser exibido quando aberto.

O trecho de código a seguir mostra como obter as propriedades usando a classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

```php  

    // Abrir documento
    $document = new Document($inputFile);

    // Obter diferentes propriedades do documento
    // Posição da janela do documento - Padrão: false
    $responseData = "CenterWindow : " . $document->isCenterWindow();

    // Ordem de leitura predominante; determina a posição da página
    // quando exibida lado a lado - Padrão: L2R
    $responseData = $responseData . "Direction : " . $document->getDirection();

    // Se a barra de título da janela deve exibir o título do documento.
    // Se falso, a barra de título exibe o nome do arquivo PDF - Padrão: false
    $responseData = $responseData . "DisplayDocTitle : " . $document->isDisplayDocTitle();

    // Se deve redimensionar a janela do documento para caber no tamanho da
    // primeira página exibida - Padrão: false
    $responseData = $responseData . "FitWindow : " . $document->isFitWindow();

    // Se deve ocultar a barra de menu do aplicativo visualizador - Padrão: false
    $responseData = $responseData . "HideMenuBar :" . $document->isHideMenubar();

    // Se deve ocultar a barra de ferramentas do aplicativo visualizador - Padrão: false
    $responseData = $responseData . "HideToolBar :" . $document->isHideToolBar();

    // Se deve ocultar elementos de IU como barras de rolagem
    // deixando apenas o conteúdo da página exibido - Padrão: false
    $responseData = $responseData . "HideWindowUI :" . $document->isHideWindowUI();

    // O modo de página do documento. Como exibir o documento ao sair
    // do modo de tela cheia.
    $responseData = $responseData . "NonFullScreenPageMode :" . $document->getNonFullScreenPageMode();

    // O layout da página, ou seja, página única, uma coluna
    $responseData = $responseData . "PageLayout :" . $document->getPageLayout();

    // Como o documento deve ser exibido quando aberto.
    $responseData = $responseData . "Page Mode :" . $document->getPageMode();
    $document->close();  
```


## Definir Propriedades da Janela do Documento e Exibição da Página

Este tópico explica como definir as propriedades da janela do documento, do aplicativo visualizador e da exibição da página.

Para definir essas diferentes propriedades:

1. Abra o arquivo PDF usando a classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Defina as propriedades do objeto Document.
1. Salve o arquivo PDF atualizado usando o método Save.

Os métodos disponíveis são:

- [setCenterWindow](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setCenterWindow-boolean-)
- [setDirection](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setDirection-int-)
- [setDisplayDocTitle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setDisplayDocTitle-boolean-)
- [setFitWindow](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setFitWindow-boolean-)
- [setHideMenuBar](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideMenubar-boolean-)

- [setHideToolBar](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideToolBar-boolean-)
- [setHideWindowUI](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideWindowUI-boolean-)
- [setNonFullScreenPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setNonFullScreenPageMode-int-)
- [setPageLayout](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setPageLayout-int-)
- [setPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setPageMode-int-)

O trecho de código a seguir mostra como definir as propriedades usando a classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

```php

    // Abrir documento
    $document = new Document($inputFile);
    // Definir diferentes propriedades do documento
    // especificar para posicionar a janela do documento - Padrão: false
    $document->setCenterWindow(true);
    // Ordem de leitura predominante; determinar a posição da página
    // quando exibida lado a lado - Padrão: L2R
    $document->setDirection(Direction::$R2L);
    // Especificar se a barra de título da janela deve exibir o título do documento
    // se false, a barra de título exibe o nome do arquivo PDF - Padrão: false
    $document->setDisplayDocTitle(true);
    // Especificar se deve redimensionar a janela do documento para caber no tamanho da
    // primeira página exibida - Padrão: false
    $document->setFitWindow(true);
    // Especificar se deve ocultar a barra de menu do aplicativo visualizador - Padrão:
    // false
    $document->setHideMenubar(true);
    // Especificar se deve ocultar a barra de ferramentas do aplicativo visualizador - Padrão:
    // false
    $document->setHideToolBar(true);
    // Especificar se deve ocultar elementos da interface do usuário como barras de rolagem
    // e deixar apenas o conteúdo da página exibido - Padrão: false
    $document->setHideWindowUI(true);
    // Modo de página do documento. especificar como exibir o documento ao sair
    // do modo de tela cheia.
    $document->setNonFullScreenPageMode(PageMode::$UseOC);
    // Especificar o layout da página, ou seja, página única, uma coluna
    $document->setPageLayout(PageLayout::$TwoColumnLeft);
    // Especificar como o documento deve ser exibido quando aberto
    // ou seja, mostrar miniaturas, tela cheia, mostrar painel de anexos
    $document->setPageMode(PageMode::$UseThumbs);
    // Salvar arquivo PDF atualizado
    $document->save($outputFile);
    $document->close();

```


## Incorporando Fontes em um Arquivo PDF Existente

Os leitores de PDF suportam [um núcleo de 14 fontes](http://en.wikipedia.org/wiki/Portable_Document_Format#Fonts) para que os documentos possam ser exibidos da mesma forma, independentemente da plataforma em que o documento é exibido. Quando um PDF contém uma fonte que está fora das fontes principais, incorpore a fonte para evitar a substituição de fonte.

Aspose.PDF para PHP via Java suporta a incorporação de fontes em documentos PDF existentes. Você pode incorporar uma fonte completa ou um subconjunto. Para incorporar a fonte:

1. Abra um arquivo PDF existente usando a classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Use a classe [com.aspose.pdf.Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/Font) para incorporar a fonte.
   1. O método setEmbedded(true) incorpora a fonte completa.
   1. O [método isSubset(true)](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/#isSubset--) incorpora um subconjunto da fonte.

Um subconjunto de fonte incorpora apenas os caracteres que são usados e é útil onde as fontes são usadas para frases curtas ou slogans, por exemplo, onde uma fonte corporativa é usada para um logotipo, mas não para o texto principal.
 Usar um subconjunto reduz o tamanho do arquivo do PDF de saída.

No entanto, se uma fonte personalizada for usada para o texto do corpo, incorpore-a em sua totalidade.

O trecho de código a seguir mostra como incorporar uma fonte em um arquivo PDF.

```php

    // Abrir documento
    $document = new Document($inputFile);
    $pages = $document->getPages();
    for ($i = 1; $i <= $pages->size(); $i++) {
      $page = $pages->get_Item($i);
      $fonts = $page->getResources()->getFonts();
      if (!is_null($fonts)) {
        for ($fontIndex = 1; $fontIndex <= $fonts->size(); $fontIndex++) {
          $pageFont = $fonts->get_Item($fontIndex);
          // Verificar se a fonte já está incorporada
          if (!$pageFont->isEmbedded())
            $pageFont->setEmbedded(true);
        }
      }
      $forms = $page->getResources()->getForms();
      // Verificar objetos de Formulários
      for ($formIndex = 0; $formIndex < -$forms->size(); $formIndex++) {
        $formFonts = $forms->get_Item($formIndex)->getResources()->getFonts();
        if (!is_null($formFonts)) {
          for ($fontIndex = 1; $fontIndex <= $formFonts->size(); $fontIndex++) {
            $pageFont = $formFonts->get_Item($fontIndex);
            // Verificar se a fonte já está incorporada
            if (!$pageFont->isEmbedded())
              $pageFont->setEmbedded(true);
          }
        }
      }
      $responseData = "Ok";
    }

    // Salvar arquivo PDF atualizado
    $document->save($outputFile);
    $document->close();
```

## Incorporando Fontes ao criar PDF

Se você precisar usar qualquer fonte além das 14 fontes principais suportadas pelo Adobe Reader, então você deve incorporar a descrição da fonte ao gerar um arquivo PDF. Se a informação da fonte não estiver incorporada, o Adobe Reader a obterá do Sistema Operacional se estiver instalada no sistema, ou construirá uma fonte substituta de acordo com o descritor da fonte no PDF. Por favor, note que a fonte incorporada deve estar instalada na máquina host, ou seja, no caso do seguinte código, a fonte 'Univers Condensed' está instalada no sistema.

Usamos a propriedade setEmbedded da classe [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/Font) para incorporar a informação da fonte no arquivo PDF. Definir o valor desta propriedade como ‘true' irá incorporar o arquivo completo da fonte no PDF, sabendo que isso aumentará o tamanho do arquivo PDF. Abaixo está o trecho de código que pode ser usado para incorporar a informação da fonte no PDF.

```php

    // Instanciar objeto PDF chamando seu construtor vazio
    $documento = new Document();

    // Criar uma seção no objeto Pdf
    $pagina = $documento->getPages()->add();
    $fragmento = new TextFragment("");
    $segmento = new TextSegment("Este é um texto de exemplo usando fonte personalizada.");

    $repositorioFonte = new FontRepository();

    $estadoTexto = new TextState();
    $estadoTexto->setFont($repositorioFonte->findFont("Univers Condensed"));
    $estadoTexto->getFont()->setEmbedded(true);
    $segmento->setTextState($estadoTexto);
    $fragmento->getSegments()->add($segmento);
    $pagina->getParagraphs()->add($fragmento);

    // Salvar arquivo PDF atualizado
    $documento->save($arquivoSaida);
    $documento->close();
```


## Definir Nome da Fonte Padrão ao Salvar PDF

Quando um documento PDF contém fontes que não estão disponíveis no próprio documento e no dispositivo, a API substitui essas fontes pela fonte padrão. Quando uma fonte está disponível (está instalada no dispositivo ou embutida no documento), o PDF de saída deve ter a mesma fonte (não deve ser substituída pela fonte padrão). O valor da fonte padrão deve conter o nome da fonte (não o caminho para os arquivos de fonte). Implementamos um recurso para definir o nome da fonte padrão ao salvar um documento como PDF. O seguinte trecho de código pode ser usado para definir a fonte padrão:

```php

    // Carregar um documento PDF existente
    $document = new Document($inputFile);
    $newName = "Arial";

    // Inicializar opções de salvamento para o formato PDF
    $ops = new PdfSaveOptions();

    // Definir nome da fonte padrão
    $ops->setDefaultFontName($newName);

    // Salvar arquivo PDF
    $document->save($outputFile, $ops);
    // Salvar arquivo PDF atualizado
    $document->close();
```

## Obter Todas as Fontes de um Documento PDF

Caso você queira obter todas as fontes de um documento PDF, você pode usar o método **Document.getFontUtilities().getAllFonts()** fornecido na classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
 Verifique o seguinte trecho de código para obter todas as fontes de um documento PDF existente:

```php

    // Carregar um documento PDF existente
    $document = new Document($inputFile);

    // Obter todas as fontes do documento
    $fonts = $document->getFontUtilities()->getAllFonts();
    foreach ($fonts as $font) {
      $responseData = $responseData . $f->getFontName() . PHP_EOL;
    }

    // Salvar arquivo PDF atualizado
    $document->close();
```

## Obter-Definir Fator de Zoom do Arquivo PDF

Às vezes, você deseja definir ou obter o fator de zoom de um documento PDF. Você pode facilmente realizar essa tarefa com Aspose.PDF.

O objeto [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/GoToAction) permite que você obtenha o valor de zoom associado a um arquivo PDF. Da mesma forma, ele pode ser usado para definir o fator de Zoom de um arquivo.

```php

    // Carregar um documento PDF existente
    $document = new Document($inputFile);

    // Criar objeto GoToAction
    $action = $document->getOpenAction();

    // Obter o fator de Zoom do arquivo PDF
    $responseData = $action->getDestination()->getZoom();

    // Salvar arquivo PDF atualizado
    $document->close();  
```

O trecho de código a seguir mostra como obter o fator de zoom de um arquivo PDF.

```php

    // Carregar um documento PDF existente
    $document = new Document($inputFile);
    $zoom = 0.5;
    // definindo fator de zoom do documento
    $page = $document->getPages()->get_Item(1);
    $actionzoom = new GoToAction(
      new XYZExplicitDestination($page, $page->getMediaBox()->getWidth(), $page->getMediaBox()->getHeight(), $zoom)
    );

    // definindo ação para ajustar à largura da página no zoom
    $actionFitToWidth = new GoToAction(
      new FitHExplicitDestination($page, $page->getMediaBox()->getWidth())
    );

    // definindo ação para ajustar à altura da página no zoom
    $actionFittoHeight = new GoToAction(
      new FitVExplicitDestination( $page, $page->getMediaBox()->getHeight())
    );

    $document->setOpenAction($actionzoom);
    $document->setOpenAction($actionFittoWidth);
    $document->setOpenAction($actionFittoHeight);

    // Salvar arquivo PDF atualizado
    $document->save($outputFile);
    $document->close();  
```