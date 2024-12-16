---
title: Adicionar Carimbos de Texto em PDF programaticamente
linktitle: Carimbos de Texto em Arquivo PDF
type: docs
weight: 20
url: /pt/php-java/text-stamps-in-the-pdf-file/
description: Adicionar um carimbo de texto a um arquivo PDF usando a classe TextStamp com PHP.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Adicionar Carimbo de Texto com Java

Aspose.PDF para PHP via Java fornece a classe [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) para adicionar um carimbo de texto em um arquivo PDF.
 O [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) class fornece os métodos necessários para especificar o tamanho da fonte, estilo da fonte e cor da fonte etc. para o objeto de carimbo. Para adicionar um carimbo de texto, primeiro você precisa criar um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) e um objeto [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) usando os métodos necessários. Depois disso, você pode chamar o método [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-) da classe [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) para adicionar o carimbo no documento PDF.

O trecho de código a seguir mostra como adicionar um carimbo de texto no arquivo PDF.

```php

    // Abrir documento
    $document = new Document($inputFile);        
    $pages = $document->getPages();
    $colors = new Color();
    // criar carimbo de texto
    $textStamp = new TextStamp("Carimbo de Exemplo");
    // definir se o carimbo é de fundo
    $textStamp->setBackground(true);
    // definir origem
    $textStamp->setXIndent(100);
    $textStamp->setYIndent(100);
    // rotacionar carimbo
    $textStamp->setRotate((new Rotation())->On90);    
    // definir propriedades do texto
    $fontRepository = new FontRepository();
    $fontStyles = new FontStyles();
    $textStamp->getTextState()->setFont($fontRepository->findFont("Arial"));
    $textStamp->getTextState()->setFontSize(14);
    $textStamp->getTextState()->setFontStyle($fontStyles->Bold | $fontStyles->Italic);
    $textStamp->getTextState()->setForegroundColor($colors->getGreen());

    // adicionar carimbo a uma página específica
    $pages->get_Item(1)->addStamp($textStamp);

    // Salvar documento de saída
    $document->save($outputFile);
    $document->close();
```

## Definir alinhamento para o objeto TextStamp

Adicionar marcas d'água a documentos PDF é um dos recursos frequentemente solicitados e o Aspose.PDF para PHP via Java é totalmente capaz de adicionar marcas d'água de imagem, bem como marcas d'água de texto. A classe [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) fornece o recurso para adicionar carimbos de texto sobre o arquivo PDF. Recentemente, houve uma necessidade de suportar o recurso de especificar o alinhamento do texto ao usar o objeto [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp). Portanto, para atender a essa necessidade, introduzimos o método setTextAlignment(..) na classe [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp). Usando este método, você pode especificar o alinhamento horizontal do texto.

Os trechos de código a seguir mostram um exemplo de como carregar um documento PDF existente e adicionar [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) sobre ele.

```php

    // Abrir documento
    $document = new Document($inputFile);        
    $pages = $document->getPages();
    $colors = new Color();

    // instanciar objeto FormattedText com string de exemplo
    $text = new FormattedText("This");

    // adicionar nova linha de texto ao FormattedText
    $text->addNewLineText("é exemplo");
    $text->addNewLineText("Alinhado ao Centro");
    $text->addNewLineText("Carimbo de Texto");
    $text->addNewLineText("Objeto");
    
    // criar carimbo de texto
    $textStamp = new TextStamp($text);

    // especificar o Alinhamento Horizontal do carimbo de texto como Alinhado ao Centro
    $textStamp->setHorizontalAlignment((new HorizontalAlignment)->getCenter());
    // especificar o Alinhamento Vertical do carimbo de texto como Alinhado ao Centro
    $textStamp->setVerticalAlignment((new VerticalAlignment())->getCenter);
    // especificar o Alinhamento Horizontal do Texto do TextStamp como Alinhado ao Centro
    $textStamp->setTextAlignment((new HorizontalAlignment)->getCenter());
    // definir margem superior para o objeto carimbo
    $textStamp->setTopMargin(20);
    
    // adicionar carimbo a uma página específica
    $pages->get_Item(1)->addStamp($textStamp);

    // Salvar documento de saída
    $document->save($outputFile);
    $document->close();  
```


## Preencher Texto de Contorno como Carimbo no Arquivo PDF

Implementamos a configuração do modo de renderização para cenários de adição e edição de texto. Para renderizar texto de contorno, crie um objeto [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextState) e defina RenderingMode para TextRenderingMode.StrokeText e também selecione a cor para a propriedade StrokingColor. Mais tarde, vincule TextState ao carimbo usando o método bindTextState().

O trecho de código a seguir demonstra a adição de Texto de Contorno Preenchido:

```php

   // Crie um objeto TextState para transferir propriedades avançadas
    $ts = new TextState();
        
    // Defina a cor para o contorno
    $ts->setStrokingColor((new Color())->getGray());

    // Defina o modo de renderização do texto
    $ts->setRenderingMode(TextRenderingMode::$StrokeText);

    // Carregue um documento PDF de entrada
    $fileStamp = new PdfFileStamp(new Document($inputFile));

    $stamp = new Stamp();
    $stamp->bindLogo(
        new FormattedText("PAID IN FULL",
            (new Color())->getGray(), "Arial",
            facades_EncodingType::$WinAnsi,
            true, 78));

    // Vincular TextState
    $stamp->bindTextState($ts);
    
    // Defina a origem X,Y
    $stamp->setOrigin(100, 100);
    $stamp->setOpacity (5);
    $stamp->setBlendingSpace(BlendingColorSpace::$DeviceRGB);
    $stamp->setRotation (45.0);
    $stamp->setBackground(false);

    // Adicionar Carimbo
    $fileStamp->addStamp($stamp);
    $fileStamp->save($outputFile);
    $fileStamp->close();
```