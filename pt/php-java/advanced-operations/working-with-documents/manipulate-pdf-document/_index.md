---
title: Manipular Documento PDF 
linktitle: Manipular Documento PDF
type: docs
weight: 30
url: pt/php-java/manipulate-pdf-document/
description: Este artigo contém informações sobre como validar Documento PDF para o Padrão PDF A, como trabalhar com TOC, como definir a data de expiração do PDF e como determinar o Progresso da geração do arquivo PDF.
lastmod: "2024-06-05"
---

## Validar Documento PDF para o Padrão PDF A (A 1A e A 1B)

Para validar um documento PDF para compatibilidade com PDF/A-1a ou PDF/A-1b, use o método [validate(...)](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#validate-java.lang.String-com.aspose.pdf.PdfFormat-) da classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Este método permite especificar o nome do arquivo no qual o resultado será salvo e o tipo de validação necessário enumeração [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/PdfFormat): PDF_A_1A ou PDF_A_1B.

O formato XML de saída é um formato personalizado Aspose.
 O XML contém uma coleção de tags com o nome Problem; cada tag contém os detalhes de um problema específico. O atributo ObjectID da tag Problem representa o ID do objeto específico ao qual este problema está relacionado. O atributo Clause representa uma regra correspondente na especificação do PDF.

```php

    // Abrir documento
    $document = new Document($inputFile);
    
    $pdfFormat =  (new PdfFormat())->PDF_A_1A;
    // Validar PDF para PDF/A-1a
    $document->validate($outputFile, $pdfFormat);
    $document->close();
```

## Trabalhando com o TOC

### Adicionar TOC ao PDF Existente

Para adicionar um TOC a um arquivo PDF existente, use a classe [Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) no pacote com.aspose.pdf. O pacote com.aspose.pdf pode tanto criar novos arquivos PDF quanto manipular arquivos PDF existentes. Para adicionar um TOC a um PDF existente, use o pacote com.aspose.pdf.

Este trecho de código PHP usa Aspose.PDF para adicionar um Índice (TOC) a um documento PDF existente:

```php
    // Abrir documento
    $document = new Document($inputFile);

    // Obter acesso à primeira página do arquivo PDF
    $tocPage = $document->getPages()->insert(1);

    // Criar objeto para representar informações do TOC
    $tocInfo = new TocInfo();

    $title = new TextFragment("Índice");
    $title->getTextState()->setFontSize(20);
    $title->getTextState()->setFontStyle(FontStyles::$Bold);

    // Definir o título para o TOC
    $tocInfo->setTitle($title);
    $tocPage->setTocInfo($tocInfo);

    // Criar objetos de string que serão usados como elementos do TOC
    $titles = ["Primeira página", "Segunda página", "Terceira página", "Quarta página"];

    for ($i = 0; $i < 4; $i++) {
        // Criar objeto Heading
        $heading2 = new Heading(1);

        $segment2 = new TextSegment();
        $heading2->setTocPage($tocPage);
        $heading2->getSegments()->add($segment2);

        // Especificar a página de destino para o objeto heading
        $page = $document->getPages()->get_Item($i + 2);
        $heading2->setDestinationPage($page);

        // Página de destino
        $heading2->setTop($page->getRect()->getHeight());

        // Coordenada de destino
        $segment2->setText($titles[$i]);

        // Adicionar heading à página que contém o TOC
        $tocPage->getParagraphs()->add($heading2);
    }
    // Salvar o documento atualizado
    $document->save($outputFile);
    $document->close();
```

### Definir diferentes TabLeaderType para diferentes Níveis de TOC

Aspose.PDF também permite definir diferentes TabLeaderType para diferentes níveis de TOC. Você precisa definir a propriedade LineDash do FormatArray com o valor apropriado do enum TabLeaderType como a seguir.

```php
    // Abrir documento
    $document = new Document($inputFile);
    $tocPage = $document->getPages()->add();

    $tocInfo = new TocInfo();

    // definir LeaderType
    $tocInfo->setLineDash(TabLeaderType->Solid);

    $title = new TextFragment("Índice");
    $title->getTextState()->setFontSize(30);
    $tocInfo->setTitle($title);

    // Adicionar a seção de lista à coleção de seções do documento Pdf
    $tocPage->setTocInfo($tocInfo);

    // Definir o formato da lista de quatro níveis definindo as margens esquerdas e
    // configurações de formato de texto de cada nível
    $fontStyles = new FontStyles();
    $tabLeaderTypes = new TabLeaderType();

    $tocInfo->setFormatArrayLength(4);
    $tocInfo->getFormatArray()[0]->getMargin()->setLeft(0);
    $tocInfo->getFormatArray()[0]->getMargin()->setRight(30);
    $tocInfo->getFormatArray()[0]->setLineDash($tabLeaderTypes->getDot());
    $tocInfo->getFormatArray()[0]->getTextState()->setFontStyle($fontStyles->getBold() | $fontStyles->getItalic());
    $tocInfo->getFormatArray()[1]->getMargin()->setLeft(10);
    $tocInfo->getFormatArray()[1]->getMargin()->setRight(30);
    $tocInfo->getFormatArray()[1]->setLineDash($tabLeaderTypes->getNone());
    $tocInfo->getFormatArray()[1]->getTextState()->setFontSize(10);
    $tocInfo->getFormatArray()[2]->getMargin()->setLeft(20);
    $tocInfo->getFormatArray()[2]->getMargin()->setRight(0);
    $tocInfo->getFormatArray()[2]->getTextState()->setFontStyle($fontStyles->getBold());
    $tocInfo->getFormatArray()[3]->setLineDash($tabLeaderTypes->getSolid());
    $tocInfo->getFormatArray()[3]->getMargin()->setLeft(30);
    $tocInfo->getFormatArray()[3]->getMargin()->setRight(30);
    $tocInfo->getFormatArray()[3]->getTextState()->setFontStyle($fontStyles->getBold());

    // Criar uma seção no documento Pdf
    $page = $document->getPages()->add();

    // Adicionar quatro títulos na seção
    for ($Level = 1; $Level <= 4; $Level++) {
      $heading2 = new Heading($Level);
      $segment2 = new TextSegment();

      $heading2->getSegments()->add($segment2);
      $heading2->setAutoSequence(true);
      $heading2->setTocPage($tocPage);

      $segment2->setText("Título Exemplo" . $Level);
      $fontRepository = new FontRepository();
      $heading2->getTextState()->setFont($fontRepository->findFont("Arial UnicodeMS"));

      // Adicionar o título no Índice.
      $heading2->setInList(true);
      $page->getParagraphs()->add($heading2);
    }

    // Salvar o documento atualizado
    $document->save($outputFile);
    $document->close();
```


### Ocultar Números de Página no TOC

Caso você não queira exibir números de página junto com os títulos no TOC, você pode usar a propriedade [ShowPageNumbers](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/#setShowPageNumbers-boolean-) da Classe [TOCInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo) como false. Por favor, verifique o seguinte trecho de código para ocultar os números de página no índice:

```php
    // Abrir documento
    $document = new Document();
    $tocPage = $document->getPages()->add();
    
    // Criar objeto para representar informações do TOC
    $tocInfo = new TocInfo();

    $title = new TextFragment("Índice");
    $title->getTextState()->setFontSize(20);
    $title->getTextState()->setFontStyle(FontStyles::$Bold);

    // Definir o título para o TOC
    $tocInfo->setTitle($title);

    // Adicionar a seção de lista à coleção de seções do documento Pdf
    $tocPage->setTocInfo($tocInfo);

    // Definir o formato da lista de quatro níveis definindo as margens 
    // à esquerda e as configurações de formato de texto de cada nível

    $tocInfo->setShowPageNumbers(false);
    $tocInfo->setFormatArrayLength(4);
    $tocInfo->getFormatArray()[0]->getMargin()->setRight(0);
    $tocInfo->getFormatArray()[0]->getTextState()->setFontStyle(FontStyles::$Bold | FontStyles::$Italic);

    $tocInfo->getFormatArray()[1]->getMargin()->setLeft(30);
    $tocInfo->getFormatArray()[1]->getTextState()->setUnderline(true);
    $tocInfo->getFormatArray()[1]->getTextState()->setFontSize(10);

    $tocInfo->getFormatArray()[2]->getTextState()->setFontStyle(FontStyles::$Bold);
    $tocInfo->getFormatArray()[3]->getTextState()->setFontStyle(FontStyles::$Bold);

    $page = $document->getPages()->add();

    // Adicionar quatro títulos na seção
    for ($Level = 1; $Level < 5; $Level++) {
      $heading2 = new Heading($Level);
      $segment2 = new TextSegment();
      $heading2->setTocPage($tocPage);
      $heading2->getSegments()->add($segment2);
      $heading2->setAutoSequence(true);
      $segment2->setText("este é o título do nível " + $Level);
      $heading2->setInList(true);
      $page->getParagraphs()->add($heading2);
    }
     
    // Salvar o documento atualizado
    $document->save($outputFile);
    $document->close();
```


### Personalizar Números de Página ao adicionar TOC

É comum personalizar a numeração de páginas no TOC ao adicionar TOC em um documento PDF. Por exemplo, podemos precisar adicionar algum prefixo antes do número da página, como P1, P2, P3 e assim por diante. Nesse caso, Aspose.PDF para PHP via Java fornece a propriedade PageNumbersPrefix da classe TocInfo que pode ser usada para personalizar os números de página, como mostrado no exemplo de código a seguir.

```php

    // Abrir documento
    $document = new Document($inputFile);

    // Obter acesso à primeira página do arquivo PDF
    $tocPage = $document->getPages()->insert(1);

    // Criar objeto para representar as informações do TOC
    $tocInfo = new TocInfo();

    $title = new TextFragment("Índice");
    $title->getTextState()->setFontSize(20);
    $title->getTextState()->setFontStyle(FontStyles::$Bold);

    // Definir o título para o TOC
    $tocInfo->setTitle($title);
    $tocInfo->setPageNumbersPrefix("P");
    $tocPage->setTocInfo($tocInfo);

    // Criar objetos de string que serão usados como elementos do TOC
    $titles = ["Primeira página", "Segunda página", "Terceira página", "Quarta página"];

    for ($i = 0; $i < 4; $i++) {
        // Criar objeto Heading
        $heading2 = new Heading(1);

        $segment2 = new TextSegment();
        $heading2->setTocPage($tocPage);
        $heading2->getSegments()->add($segment2);

        // Especificar a página de destino para o objeto heading
        $page = $document->getPages()->get_Item($i + 2);
        $heading2->setDestinationPage($page);

        // Página de destino
        $heading2->setTop($page->getRect()->getHeight());

        // Coordenada de destino
        $segment2->setText($titles[$i]);

        // Adicionar heading à página contendo TOC
        $tocPage->getParagraphs()->add($heading2);
    }
    // Salvar o documento atualizado
    $document->save($outputFile);
    $document->close();
```


## Adicionar Camadas ao Arquivo PDF

Camadas podem ser usadas em documentos PDF de várias maneiras. Você pode ter um arquivo multilíngue que deseja distribuir e quer que o texto em cada idioma apareça em camadas diferentes, com o design de fundo aparecendo em uma camada separada. Você também pode criar documentos com animação que aparece em uma camada separada. Um exemplo pode ser adicionar um acordo de licença ao seu arquivo, e você não quer que um usuário veja o conteúdo até que concorde com os termos do acordo.

Aspose.PDF para PHP via Java suporta a adição de camadas a arquivos PDF.

Para trabalhar com camadas em arquivos PDF, use os seguintes membros da API.

A classe [Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/Layer) representa uma camada e contém as seguintes propriedades:

- **Name** – o nome da camada.
- **Id** – o ID da camada.
- **Contents** – uma lista de operadores de camada.

Uma vez que os objetos [Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/Layer) tenham sido definidos, adicione-os à coleção Layers do objeto [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).
 O código abaixo mostra como adicionar camadas a um documento PDF.

```php
    // Abrir documento
    $document = new Document($inputFile);
    $page = $document->getPages()->add();
    $arrayList = new java("java.util.ArrayList");
    $page->setLayers($arrayList);

    $layer = new $layer("oc1", "Linha Vermelha");
    $layer->getContents()->add(new operators_SetRGBColorStroke(1, 0, 0));
    $layer->getContents()->add(new operators_MoveTo(500, 700));
    $layer->getContents()->add(new operators_LineTo(400, 700));
    $layer->getContents()->add(new operators_Stroke());    
    $page->getLayers()->add($layer);

    $layer = new $layer("oc2", "Linha Verde");
    $layer->getContents()->add(new operators_SetRGBColorStroke(0, 1, 0));
    $layer->getContents()->add(new operators_MoveTo(500, 750));
    $layer->getContents()->add(new operators_LineTo(400, 750));
    $layer->getContents()->add(new operators_Stroke());
    $page->getLayers()->add($layer);

    $layer = new $layer("oc3", "Linha Azul");
    $layer->getContents()->add(new operators_SetRGBColorStroke(0, 0, 1));
    $layer->getContents()->add(new operators_MoveTo(500, 800));
    $layer->getContents()->add(new operators_LineTo(400, 800));
    $layer->getContents()->add(new operators_Stroke());
    $page->getLayers()->add($layer);
    
    // Salvar o documento atualizado
    $document->save($outputFile);
    $document->close();
```

## Definir Expiração do PDF

O recurso de expiração do PDF define por quanto tempo um arquivo PDF é válido. Em uma data específica, se alguém tentar acessá-lo, um pop-up é exibido, explicando que o arquivo expirou e que eles precisam de um novo.

O Aspose.PDF permite definir a expiração ao criar e editar arquivos PDF.

O trecho de código abaixo mostra como definir a data de expiração para um arquivo PDF. Você precisa usar JavaScript, pois arquivos salvos por componentes de terceiros (por exemplo, OwnerGuard) não podem ser visualizados em outras estações de trabalho sem essa utilidade.

O arquivo PDF pode ser criado usando o PDF OwnerGuard utilizando um arquivo existente com uma data de expiração. Mas o novo arquivo pode ser aberto apenas em uma estação de trabalho que tenha o PDF OwnerGuard instalado. Estações de trabalho sem o PDF OwnerGuard irão gerar um ExpirationFeatureError. Por exemplo, o PDF Reader abre o arquivo se o OwnerGuard estiver instalado, mas o Adobe Acrobat retorna um erro.

```php

    // Abrir documento
    $document = new Document($inputFile);
       
    $javaScript = new JavascriptAction(
      "var year=2020;" + 
      "var month=4;" + 
      "var today = new Date(); today = new Date(today.getFullYear(), today.getMonth());" +
      "var expiry = new Date(year, month);" +
      "if (today.getTime() > expiry.getTime())" + 
      "app.alert('O arquivo está expirado. Você precisa de um novo.');"
      );
    $document->setOpenAction($javaScript);
    $document->save($outputFile);
    $document->close();
```