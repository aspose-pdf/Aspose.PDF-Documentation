---
title: Formatando Documento PDF 
linktitle: Formatando Documento PDF
type: docs
weight: 20
url: /java/formatting-pdf-document/
description: Formate o Documento PDF com Aspose.PDF para Java. Use o próximo trecho de código para resolver suas tarefas.
lastmod: "2021-06-05"
---

## Obter Propriedades da Janela do Documento e Exibição de Página

Este tópico ajuda você a entender como obter as propriedades da janela do documento, do aplicativo visualizador e como as páginas são exibidas.

Para definir essas diferentes propriedades, abra o arquivo PDF usando a classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Agora você pode obter os métodos do objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document), tais como:

- [IsCenterWindow](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#isCenterWindow--) – Centralizar a janela do documento na tela. Padrão: false.
- [SetDirection](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setDirection-int-) – Ordem de leitura.
  Isso determina como as páginas são dispostas quando exibidas lado a lado. Padrão: da esquerda para a direita.
- [isDisplayDocTitle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#isDisplayDocTitle--) – Exibir o título do documento na barra de título da janela do documento. Padrão: false (o título é exibido).
- [setHideMenuBar](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideMenubar-boolean-) – Ocultar ou exibir a barra de menu da janela do documento. Padrão: false (a barra de menu é exibida).
- [setHideToolBar](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideToolBar-boolean-) – Ocultar ou exibir a barra de ferramentas da janela do documento. Padrão: false (a barra de ferramentas é exibida).
- [setHideWindowUI](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideWindowUI-boolean-) – Ocultar ou exibir elementos da janela do documento, como barras de rolagem. Padrão: false (os elementos da UI são exibidos).

- [setNonFullScreenPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setNonFullScreenPageMode-int-) – Como o documento é exibido quando não está em modo de página inteira.- [setPageLayout](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setPageLayout-int-) – O layout da página.
- [setPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setPageMode-int-) – Como o documento é exibido quando aberto pela primeira vez. As opções são mostrar miniaturas, tela cheia, mostrar painel de anexos.

O trecho de código a seguir mostra como obter as propriedades usando a classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleFormatting {

  private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

  public static void GetDocumentWindowAndPageDisplayProperties() {

    // Abrir documento
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // Obter diferentes propriedades do documento
    // Posição da janela do documento - Padrão: false
    System.out.printf("CenterWindow : " + pdfDocument.isCenterWindow());

    // Ordem de leitura predominante; determinar a posição da página
    // quando exibido lado a lado - Padrão: L2R
    System.out.printf("Direction :- " + pdfDocument.getDirection());

    // Se a barra de título da janela deve exibir o título do documento.
    // Se falso, a barra de título exibe o nome do arquivo PDF - Padrão: false
    System.out.printf("DisplayDocTitle :- " + pdfDocument.isDisplayDocTitle());

    // Se redimensionar a janela do documento para ajustar ao tamanho da
    // primeira página exibida - Padrão: false
    System.out.printf("FitWindow :- " + pdfDocument.isFitWindow());

    // Se ocultar a barra de menu do aplicativo visualizador - Padrão: false
    System.out.printf("HideMenuBar :-" + pdfDocument.isHideMenubar());

    // Se ocultar a barra de ferramentas do aplicativo visualizador - Padrão: false
    System.out.printf("HideToolBar :-" + pdfDocument.isHideToolBar());

    // Se ocultar elementos da interface do usuário como barras de rolagem
    // deixando apenas o conteúdo da página exibido - Padrão: false
    System.out.printf("HideWindowUI :-" + pdfDocument.isHideWindowUI());

    // O modo de página do documento. Como exibir o documento ao sair
    // do modo de tela cheia.
    System.out.printf("NonFullScreenPageMode :-" + pdfDocument.getNonFullScreenPageMode());

    // O layout da página, ou seja, página única, uma coluna
    System.out.printf("PageLayout :-" + pdfDocument.getPageLayout());

    // Como o documento deve ser exibido quando aberto.
    System.out.printf("pageMode :-" + pdfDocument.getPageMode());

  }

```

## Definir Propriedades da Janela do Documento e Exibição da Página

Este tópico explica como definir as propriedades da janela do documento, do aplicativo visualizador e da exibição da página.

Para definir essas diferentes propriedades:

1. Abra o arquivo PDF usando a classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Defina as propriedades do objeto Document.
1. Salve o arquivo PDF atualizado usando o método Save.

As propriedades disponíveis são:

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

O snippet de código a seguir mostra como definir as propriedades usando a classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

```java
  public static void SetDocumentWindowAndPageDisplayProperties() {

    // Abrir documento
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    
    // Definir diferentes propriedades do documento
    // especificar para posicionar a janela do documento - Padrão: false
    pdfDocument.setCenterWindow(true);
    
    // Ordem de leitura predominante; determinar a posição da página
    // quando exibida lado a lado - Padrão: L2R
    pdfDocument.setDirection(com.aspose.pdf.Direction.R2L);
    
    // Especificar se a barra de título da janela deve exibir o título do documento
    // se false, a barra de título exibe o nome do arquivo PDF - Padrão: false
    pdfDocument.setDisplayDocTitle(true);
    
    // Especificar se deve redimensionar a janela do documento para caber no tamanho da
    // primeira página exibida - Padrão: false
    pdfDocument.setFitWindow(true);
    
    // Especificar se deve ocultar a barra de menus do aplicativo visualizador - Padrão:
    // false
    pdfDocument.setHideMenubar(true);
    
    // Especificar se deve ocultar a barra de ferramentas do aplicativo visualizador - Padrão:
    // false
    pdfDocument.setHideToolBar(true);
    
    // Especificar se deve ocultar elementos da UI como barras de rolagem
    // e deixar apenas o conteúdo da página exibido - Padrão: false
    pdfDocument.setHideWindowUI(true);
    
    // Modo de página do documento. especificar como exibir o documento ao sair do
    // modo de tela cheia.
    pdfDocument.setNonFullScreenPageMode(com.aspose.pdf.PageMode.UseOC);
    
    // Especificar o layout da página, ou seja, página única, uma coluna
    pdfDocument.setPageLayout(com.aspose.pdf.PageLayout.TwoColumnLeft);
    
    // Especificar como o documento deve ser exibido ao ser aberto
    // ou seja, mostrar miniaturas, tela cheia, mostrar painel de anexos
    pdfDocument.setPageMode(com.aspose.pdf.PageMode.UseThumbs);
    
    // Salvar arquivo PDF atualizado
    pdfDocument.save(_dataDir + "UpdatedFile_output.pdf");

  }
```

## Incorporando Fontes em um Arquivo PDF Existente

Os leitores de PDF suportam [um núcleo de 14 fontes](http://en.wikipedia.org/wiki/Portable_Document_Format#Fonts) para que os documentos possam ser exibidos da mesma forma, independentemente da plataforma em que o documento é exibido. Quando um PDF contém uma fonte que está fora das fontes principais, incorpore a fonte para evitar a substituição da fonte.

Aspose.PDF para Java suporta a incorporação de fontes em documentos PDF existentes. Você pode incorporar uma fonte completa ou um subconjunto. Para incorporar a fonte:

1. Abra um arquivo PDF existente usando a classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Use a classe [com.aspose.pdf.Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/Font) para incorporar a fonte.
   1. O método setEmbedded(true) incorpora a fonte completa.
   1. O método pageFont.isSubset(true) incorpora um subconjunto da fonte.

Um subconjunto de fonte incorpora apenas os caracteres que são usados e é útil onde as fontes são usadas para frases curtas ou slogans, por exemplo, onde uma fonte corporativa é usada para um logotipo, mas não para o texto principal.
 Usar um subconjunto reduz o tamanho do arquivo do PDF de saída.

No entanto, se uma fonte personalizada for usada para o texto do corpo, incorpore-a na sua totalidade.

O trecho de código a seguir mostra como incorporar uma fonte em um arquivo PDF.
```java
public static void EmbeddingFontsInAnExistingPDFFile() {
    // Abrir documento
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    // Iterar por todas as páginas
    for (com.aspose.pdf.Page page : (Iterable<com.aspose.pdf.Page>) pdfDocument.getPages()) {
      if (page.getResources().getFonts() != null) {
        for (com.aspose.pdf.Font pageFont : (Iterable<com.aspose.pdf.Font>) page.getResources().getFonts()) {
          // Verificar se a fonte já está incorporada
          if (!pageFont.isEmbedded())
            pageFont.setEmbedded(true);
        }
      }

      // Verificar os objetos Form
      for (com.aspose.pdf.XForm form : (Iterable<com.aspose.pdf.XForm>) page.getResources().getForms()) {
        if (form.getResources().getFonts() != null) {
          for (com.aspose.pdf.Font formFont : (Iterable<com.aspose.pdf.Font>) form.getResources().getFonts()) {
            // Verificar se a fonte está incorporada
            if (!formFont.isEmbedded())
              formFont.setEmbedded(true);
          }
        }
      }
    }
    // Salvar arquivo PDF atualizado
    pdfDocument.save(_dataDir + "UpdatedFile_output.pdf");
  }
```

## Incorporando Fontes ao criar PDF

Se você precisar usar qualquer fonte além das 14 fontes principais suportadas pelo Adobe Reader, então você deve incorporar a descrição da fonte ao gerar um arquivo PDF. Se a informação da fonte não for incorporada, o Adobe Reader a obterá do Sistema Operacional se estiver instalada no sistema, ou construirá uma fonte substituta de acordo com o descritor de fonte no PDF. Por favor, note que a fonte incorporada deve estar instalada na máquina host, ou seja, no caso do seguinte código, a fonte 'Univers Condensed' está instalada no sistema.

Usamos a propriedade setEmbedded da classe [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/Font) para incorporar as informações da fonte no arquivo PDF. Definir o valor dessa propriedade como ‘true’ irá incorporar o arquivo completo da fonte no PDF, sabendo que isso aumentará o tamanho do arquivo PDF. A seguir está o trecho de código que pode ser usado para incorporar as informações da fonte no PDF.

```java
public static void EmbeddingFontsWhileCreatingPDF() {

    // Instanciar objeto PDF chamando seu construtor vazio
    com.aspose.pdf.Document document = new com.aspose.pdf.Document();

    // Criar uma seção no objeto Pdf
    com.aspose.pdf.Page page = document.getPages().add();

    com.aspose.pdf.TextFragment fragment = new com.aspose.pdf.TextFragment("");

    com.aspose.pdf.TextSegment segment = new com.aspose.pdf.TextSegment(" Este é um texto de exemplo usando fonte personalizada.");
    com.aspose.pdf.TextState ts = new com.aspose.pdf.TextState();
    ts.setFont(FontRepository.findFont("Univers Condensed"));
    ts.getFont().setEmbedded(true);
    segment.setTextState(ts);
    fragment.getSegments().add(segment);
    page.getParagraphs().add(fragment);

    // Salvar arquivo PDF atualizado
    document.save(_dataDir + "UpdatedFile_output.pdf");
  }
```

## Definir Nome de Fonte Padrão ao Salvar PDF

Quando um documento PDF contém fontes que não estão disponíveis no próprio documento e no dispositivo, a API substitui essas fontes pela fonte padrão. Quando uma fonte está disponível (está instalada no dispositivo ou está incorporada ao documento), o PDF de saída deve ter a mesma fonte (não deve ser substituída pela fonte padrão). O valor da fonte padrão deve conter o nome da fonte (não o caminho para os arquivos de fonte). Implementamos um recurso para definir o nome da fonte padrão ao salvar um documento como PDF. O seguinte trecho de código pode ser usado para definir a fonte padrão:

```java
public static void SetDefaultFontNameWhileSavingPDF() {

    // Carregar um documento PDF existente
    Document document = new Document("input.pdf");

    String newName = "Arial";

    // Inicializar opções de salvamento para formato PDF
    PdfSaveOptions ops = new PdfSaveOptions();

    // Definir nome da fonte padrão
    ops.setDefaultFontName(newName);

    // Salvar arquivo PDF
    document.save(_dataDir + "output_out.pdf", ops);
  }
```


## Obter Todas as Fontes do Documento PDF

Caso você queira obter todas as fontes de um documento PDF, você pode usar o método **Document.getFontUtilities().getAllFonts()** fornecido na classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Por favor, verifique o trecho de código a seguir para obter todas as fontes de um documento PDF existente:

```java
public static void GetAllFontsFromPDFDocument() {

    // Carregar um documento PDF existente
    Document document = new Document(_dataDir + "sample.pdf");

    // Obter todas as fontes do documento
    com.aspose.pdf.Font[] fonts = document.getFontUtilities().getAllFonts();
    for (com.aspose.pdf.Font f : fonts) {
      System.out.println(f.getFontName());
    }
  }
```

## Obter-Definir Fator de Zoom do Arquivo PDF

Às vezes, você deseja definir ou obter o fator de zoom de um documento PDF. Você pode facilmente realizar este requisito com o Aspose.PDF.

O objeto [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/GoToAction) permite que você obtenha o valor de zoom associado a um arquivo PDF.
 Similarly, it can be used to set a file's Zoom factor.

```java
  public static void GetSetZoomFactorOfPDFFile() {
    // Carregar um documento PDF existente
    Document document = new Document(_dataDir + "sample.pdf");
    double zoom = .5;
    // definindo o fator de zoom do documento
    GoToAction actionzoom = new GoToAction(new XYZExplicitDestination(document.getPages().get_Item(1),
        document.getPages().get_Item(1).getMediaBox().getWidth(),
        document.getPages().get_Item(1).getMediaBox().getHeight(), zoom));

    // definindo ação para ajustar à largura da página
    GoToAction actionFittoWidth = new GoToAction(new FitHExplicitDestination(document.getPages().get_Item(1),
        document.getPages().get_Item(1).getMediaBox().getWidth()));

    // definindo ação para ajustar à altura da página
    GoToAction actionFittoHeight = new GoToAction(new FitVExplicitDestination(document.getPages().get_Item(1),
        document.getPages().get_Item(1).getMediaBox().getHeight()));

    document.setOpenAction(actionzoom);
    document.setOpenAction(actionFittoWidth);
    document.setOpenAction(actionFittoHeight);
```

O trecho de código a seguir mostra como obter o fator de Zoom de um arquivo PDF.

```java
    // Instanciar novo objeto Document
    Document doc1 = new Document(_dataDir + "Zoomed_actionzoom.pdf");
    // Criar objeto GoToAction
    GoToAction action = (GoToAction) doc1.getOpenAction();
    // Obter o fator de Zoom do arquivo PDF
    System.out.println(((XYZExplicitDestination) action.getDestination()).getZoom());

    // Salvar arquivo PDF atualizado
    document.save(_dataDir + "UpdatedFile_output.pdf");
  }
}
```