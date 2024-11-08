---
title: Adicionar marca d'água ao PDF 
linktitle: Adicionar marca d'água
type: docs
weight: 90
url: /pt/php-java/add-watermarks/
description: Este artigo explica os recursos de trabalho com artefatos e obtenção de marcas d'água em PDFs usando PHP.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for PHP via Java** permite adicionar marcas d'água ao seu documento PDF usando Artefatos. Por favor, verifique este artigo para resolver sua tarefa.

Uma marca d'água criada com Adobe Acrobat é chamada de artefato (conforme descrito em 14.8.2.2 Conteúdo Real e Artefatos da especificação PDF). Para trabalhar com artefatos, Aspose.PDF possui duas classes: [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact) e [ArtifactCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/artifactcollection).

Para obter todos os artefatos em uma página específica, a classe [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/Page) possui a propriedade Artifacts.
 Este tópico explica como trabalhar com artefatos em arquivos PDF.

## Trabalhando com Artefatos

A classe [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact) contém as seguintes propriedades:

**Artifact.Type** – obtém o tipo de artefato (suporta valores da enumeração Artifact.ArtifactType, onde os valores incluem Background, Layout, Page, Pagination e Undefined).
**Artifact.Subtype** – obtém o subtipo de artefato (suporta os valores da enumeração Artifact.ArtifactSubtype, onde os valores incluem Background, Footer, Header, Undefined, Watermark).

{{% alert color="primary" %}}

Por favor, note que marcas d'água criadas com o Adobe Acrobat têm o tipo Pagination e subtipo Watermark.

{{% /alert %}}

**Artifact.Contents** – Obtém uma coleção de operadores internos de artefato. Seu tipo suportado é System.Collections.ICollection.
**Artifact.Form** – Obtém o XForm de um artefato (se XForm for usado). Artefatos de marcas d'água, cabeçalho e rodapé contêm XForm que mostra todos os conteúdos do artefato.

**Artifact.Image** – Obtém a imagem de um artefato (se uma imagem estiver presente, caso contrário, nulo).**Artifact.Text** – Obtém o texto de um artefato.  
**Artifact.Rectangle** – Obtém a posição de um artefato na página.  
**Artifact.Rotation** – Obtém a rotação de um artefato (em graus, valor positivo indica rotação no sentido anti-horário).  
**Artifact.Opacity** – Obtém a opacidade de um artefato. Os valores possíveis estão na faixa de 0…1, onde 1 é completamente opaco.

## Exemplos de Programação: Obtendo Marcas d'água

O seguinte trecho de código mostra como obter cada marca d'água na primeira página de um arquivo PDF com PHP.

```php

    // Abrir documento
    $document = new Document($inputFile);
            
    $formattedText = new FormattedText("Watermark", 
        (new Color())->getBlue()->getRgb(),
        (new facades_FontStyle())->getCourier(), 
        facades_EncodingType::$Identity_h, 
        true, 72.0);

    $horizontalAlignment = new HorizontalAlignment();
    $verticalAlignment = new VerticalAlignment();

    $artifact = new WatermarkArtifact();        
    $artifact->setText($formattedText);        
    $artifact->setArtifactHorizontalAlignment ($horizontalAlignment->getCenter());
    $artifact->setArtifactVerticalAlignment ($verticalAlignment->getCenter());
    $artifact->setRotation(45);
    $artifact->setOpacity(0.5);
    $artifact->setBackground(true);
    $document->getPages()->get_Item(1)->getArtifacts()->add($artifact);
    
    // Salvar documento de saída
    $document->save($outputFile);
    $document->close();
```