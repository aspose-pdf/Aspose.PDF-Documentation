---
title: Adicionar Cabeçalho e Rodapé em PDF
linktitle: Adicionar Cabeçalho e Rodapé em PDF
type: docs
weight: 70
url: pt/php-java/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF para PHP via Java permite adicionar cabeçalhos e rodapés ao seu arquivo PDF usando a classe TextStamp.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Carimbos em PDF são frequentemente usados em contratos, relatórios e materiais restritos, para comprovar que os documentos foram revisados e marcados como "lido", "qualificado" ou "confidencial", etc. Este artigo mostrará como podemos adicionar carimbos de imagem e carimbos de texto a documentos PDF usando o **Aspose.PDF para PHP via Java**.

Se você ler os trechos de código acima linha por linha, deve perceber que a sintaxe e a lógica do código são bastante fáceis de entender.

## Adicionando Texto no Cabeçalho do Arquivo PDF

Você pode usar a classe [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) para adicionar texto no cabeçalho de um arquivo PDF.
 TextStamp class fornece as propriedades necessárias para criar um carimbo baseado em texto, como tamanho da fonte, estilo da fonte e cor da fonte, etc. Para adicionar texto no cabeçalho, você precisa criar um objeto Document e um objeto TextStamp usando as propriedades necessárias. Depois disso, você pode chamar o método AddStamp da Page para adicionar o texto no cabeçalho do PDF.

Você precisa definir a propriedade TopMargin de forma que ajuste o texto na área do cabeçalho do seu PDF. Você também precisa definir HorizontalAlignment para Center e VerticalAlignment para Top.

O snippet de código a seguir mostra como adicionar texto no cabeçalho de um arquivo PDF com PHP.

```php

    // Abrir documento
    $document = new Document($inputFile);

    // Criar cabeçalho
    $textStamp = new TextStamp("Texto do Cabeçalho");
    $horizontalAlignment = new HorizontalAlignment();
    $verticalAlignment = new VerticalAlignment();

    // Definir propriedades do carimbo
    $textStamp->setTopMargin(10);
    $textStamp->setHorizontalAlignment($horizontalAlignment->Center);
    $textStamp->setVerticalAlignment($verticalAlignment->Top);

    $pages = $document->getPages();

    // Adicionar rodapé na 1ª página
    $page = $pages->get_Item(1);
    $page->addStamp($textStamp);
    
    // Salvar documento de saída
    $document->save($outputFile);
    $document->close();
```

## Adicionando Texto no Rodapé do Arquivo PDF

Você pode usar a classe TextStamp para adicionar texto no rodapé de um arquivo PDF. A classe TextStamp fornece as propriedades necessárias para criar um carimbo baseado em texto, como tamanho da fonte, estilo da fonte e cor da fonte, etc. Para adicionar texto no rodapé, você precisa criar um objeto Document e um objeto TextStamp utilizando as propriedades necessárias. Depois disso, você pode chamar o método addStamp da Página para adicionar o texto no rodapé do PDF.

O seguinte trecho de código mostra como adicionar texto no rodapé de um arquivo PDF com PHP.

```php

    // Abrir documento
    $document = new Document($inputFile);

    // Criar cabeçalho
    $textStamp = new TextStamp("Texto do Cabeçalho");
    $horizontalAlignment = new HorizontalAlignment();
    $verticalAlignment = new VerticalAlignment();

    // Definir propriedades do carimbo
    $textStamp->setBottomMargin(10);
    $textStamp->setHorizontalAlignment($horizontalAlignment->Center);
    $textStamp->setVerticalAlignment($verticalAlignment->Bottom);

    $pages = $document->getPages();

    // Adicionar rodapé na primeira página
    $page = $pages->get_Item(1);
    $page->addStamp($textStamp);
    
    // Salvar documento de saída
    $document->save($outputFile);
    $document->close();
```


## Adicionando Imagem no Cabeçalho do Arquivo PDF

Você pode usar a classe [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagestamp) para adicionar uma imagem no cabeçalho de um arquivo PDF. A classe Image Stamp fornece as propriedades necessárias para criar um carimbo baseado em imagem, como tamanho da fonte, estilo da fonte e cor da fonte, etc. Para adicionar uma imagem no cabeçalho, você precisa criar um objeto Document e um objeto Image Stamp usando as propriedades necessárias. Depois disso, você pode chamar o método [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/class-use/Stamp) da página para adicionar a imagem no cabeçalho do PDF.

```php

    // Abrir documento
    $document = new Document($inputFile);
    
    // Criar rodapé
    $imageStamp = new ImageStamp($inputImage);
    $horizontalAlignment = new HorizontalAlignment();
    $verticalAlignment = new VerticalAlignment();

    // Definir propriedades do carimbo
    $imageStamp->setTopMargin(10);
    $imageStamp->setHorizontalAlignment($horizontalAlignment->Center);
    $imageStamp->setVerticalAlignment($verticalAlignment->Top);

    $pages = $document->getPages();

    // Adicionar rodapé à 1ª página
    $page = $pages->get_Item(1);
    $page->addStamp($imageStamp);

    // Salvar documento de saída
    $document->save($outputFile);
    $document->close();
```


O trecho de código a seguir mostra como adicionar uma imagem no cabeçalho de um arquivo PDF com PHP.

## Adicionando Imagem no Rodapé do Arquivo PDF

Você pode usar a classe Image Stamp para adicionar uma imagem no rodapé de um arquivo PDF. A classe Image Stamp fornece as propriedades necessárias para criar um carimbo baseado em imagem como tamanho de fonte, estilo de fonte, e cor da fonte, etc. Para adicionar uma imagem no rodapé, você precisa criar um objeto Document e um objeto Image Stamp usando as propriedades necessárias. Depois disso, você pode chamar o método AddStamp da página para adicionar a imagem no rodapé do PDF.

{{% alert color="primary" %}}

Você precisa definir a propriedade BottomMargin de forma que ajuste a imagem na área do rodapé do seu PDF. Você também precisa definir [HorizontalAlignment](https://reference.aspose.com/pdf/java/com.aspose.pdf/HorizontalAlignment) para `Center` e [VerticalAlignment](https://reference.aspose.com/pdf/java/com.aspose.pdf/VerticalAlignment) para `Bottom`.

{{% /alert %}}

O trecho de código a seguir mostra como adicionar uma imagem no rodapé de um arquivo PDF com PHP.

```php

    // Abrir documento
    $document = new Document($inputFile);
    
    // Criar rodapé
    $imageStamp = new ImageStamp($inputImage);
    $horizontalAlignment = new HorizontalAlignment();
    $verticalAlignment = new VerticalAlignment();

    // Definir propriedades do carimbo
    $imageStamp->setBottomMargin(10);
    $imageStamp->setHorizontalAlignment($horizontalAlignment->Center);
    $imageStamp->setVerticalAlignment($verticalAlignment->Bottom);

    $pages = $document->getPages();

    // Adicionar rodapé à 1ª página
    $page = $pages->get_Item(1);
    $page->addStamp($imageStamp);

    // Salvar documento de saída
    $document->save($outputFile);
    $document->close();
```

## Adicionando diferentes Cabeçalhos em um Arquivo PDF

Sabemos que podemos adicionar TextStamp na seção de Cabeçalho/Rodapé do documento usando as propriedades TopMargin ou Bottom Margin, mas às vezes podemos ter a necessidade de adicionar vários cabeçalhos/rodapés em um único documento PDF. **Aspose.PDF para PHP via Java** explica como fazer isso.

Para realizar essa exigência, criaremos objetos individuais [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) (o número de objetos depende do número de Cabeçalhos/Rodapés necessários) e os adicionaremos ao documento PDF.
 Podemos também especificar diferentes informações de formatação para cada objeto de carimbo individual. No exemplo a seguir, criamos um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) e três objetos [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) e, em seguida, usamos o método [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/class-use/Stamp) da Página para adicionar o texto na seção do cabeçalho do PDF. O snippet de código a seguir mostra como adicionar uma imagem no rodapé de um arquivo PDF com Aspose.PDF para PHP via Java.

```php

    // Abrir documento
    $document = new Document($inputFile);

    // Criar três carimbos
    $stamp1 = new TextStamp("Cabeçalho 1");
    $stamp2 = new TextStamp("Cabeçalho 2");
    $stamp3 = new TextStamp("Cabeçalho 3");
    
    $horizontalAlignment = new HorizontalAlignment();
    $verticalAlignment = new VerticalAlignment();
    $fontStyles = new FontStyles();

    // Definir alinhamento do carimbo (colocar carimbo no topo da página, centralizado horizontalmente)
    $stamp1->setVerticalAlignment ($verticalAlignment->Top);
    $stamp1->setHorizontalAlignment($horizontalAlignment->Center);

    // Especificar o estilo da fonte como Negrito
    $stamp1->getTextState()->setFontStyle($fontStyles->Bold);
    // Definir a cor do texto em primeiro plano como vermelho
    $stamp1->getTextState()->setForegroundColor((new Color())->getRed());
    // Especificar o tamanho da fonte como 14
    $stamp1->getTextState()->setFontSize(14);

    // Agora precisamos definir o alinhamento vertical do segundo objeto carimbo como Topo
    $stamp2->setVerticalAlignment($verticalAlignment->Top);
    // Definir informações de alinhamento horizontal para carimbo como Centralizado
    $stamp2->setHorizontalAlignment($horizontalAlignment->Center);
    // Definir o fator de zoom para o objeto carimbo
    $stamp2->setZoom(10);

    // Definir a formatação do terceiro objeto carimbo
    // Especificar informações de alinhamento vertical para o objeto carimbo como TOPO
    $stamp3->setVerticalAlignment($verticalAlignment->Top);
    // Definir informações de alinhamento horizontal para o objeto carimbo como Centralizado
    $stamp3->setHorizontalAlignment ($horizontalAlignment->Center);
    // Definir o ângulo de rotação para o objeto carimbo
    $stamp3->setRotateAngle(35);
    // Definir rosa como cor de fundo para o carimbo
    $stamp3->getTextState()->setBackgroundColor ((new Color())->getPink());  
    // Alterar as informações do tipo de fonte para o carimbo para Verdana
    $stamp3->getTextState()->setFont ((new FontRepository())->findFont("Verdana"));

    // O primeiro carimbo é adicionado na primeira página;
    $document->getPages()->get_Item(1)->addStamp($stamp1);
    // O segundo carimbo é adicionado na segunda página;
    $document->getPages()->get_Item(2)->addStamp($stamp2);
    // O terceiro carimbo é adicionado na terceira página.
    $document->getPages()->get_Item(3)->addStamp($stamp3);
    
    // Salvar documento de saída
    $document->save($outputFile);
    $document->close();
```