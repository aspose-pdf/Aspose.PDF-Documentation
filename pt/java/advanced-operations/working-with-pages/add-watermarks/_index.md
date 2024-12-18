---
title: Adicionar marca d'água ao PDF
linktitle: Adicionar marca d'água
type: docs
weight: 90
url: /pt/java/add-watermarks/
description: Este artigo explica os recursos de trabalhar com artefatos e obter marcas d'água em PDFs usando programaticamente o Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF para Java** permite adicionar marcas d'água ao seu documento PDF usando Artefatos. Por favor, verifique este artigo para resolver sua tarefa.

Uma marca d'água criada com o Adobe Acrobat é chamada de artefato (conforme descrito em 14.8.2.2 Conteúdo Real e Artefatos da especificação PDF). Para trabalhar com artefatos, o Aspose.PDF possui duas classes: [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact) e [ArtifactCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/artifactcollection).

Para obter todos os artefatos em uma página específica, a classe [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/Page) possui a propriedade Artifacts.
 Este tópico explica como trabalhar com artefatos em arquivos PDF.

## Trabalhando com Artefatos

A classe [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact) contém as seguintes propriedades:

**Artifact.Type** – obtém o tipo de artefato (suporta valores da enumeração Artifact.ArtifactType onde os valores incluem Background, Layout, Page, Pagination e Undefined).  
**Artifact.Subtype** – obtém o subtipo de artefato (suporta os valores da enumeração Artifact.ArtifactSubtype onde os valores incluem Background, Footer, Header, Undefined, Watermark).

{{% alert color="primary" %}}

Por favor, note que marcas d'água criadas com Adobe Acrobat têm o tipo Pagination e o subtipo Watermark.

{{% /alert %}}

**Artifact.Contents** – Obtém uma coleção de operadores internos de artefato. Seu tipo suportado é System.Collections.ICollection.  
**Artifact.Form** – Obtém o XForm de um artefato (se XForm for usado). Artefatos de marca d'água, cabeçalho e rodapé contêm XForm que mostram todos os conteúdos do artefato.

**Artifact.Image** – Obtém a imagem de um artefato (se uma imagem estiver presente, caso contrário, null).**Artifact.Text** – Obtém o texto de um artefato.  
**Artifact.Rectangle** – Obtém a posição de um artefato na página.  
**Artifact.Rotation** – Obtém a rotação de um artefato (em graus, valor positivo indica rotação no sentido anti-horário).  
**Artifact.Opacity** – Obtém a opacidade de um artefato. Os valores possíveis estão na faixa de 0…1, onde 1 é completamente opaco.

## Exemplos de Programação: Obtendo Marcas d'água

O trecho de código a seguir mostra como obter cada marca d'água na primeira página de um arquivo PDF com Java.

```java
 package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import com.aspose.pdf.facades.EncodingType;
import com.aspose.pdf.facades.FontStyle;
import com.aspose.pdf.facades.FormattedText;

public class ExampleWatermark {
    // O caminho para o diretório de documentos.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void Split() {

        // Abrir documento
        Document doc = new Document(_dataDir + "text.pdf");      
        FormattedText formattedText = new FormattedText("Watermark", java.awt.Color.BLUE,FontStyle.Courier, EncodingType.Identity_h, true, 72.0F);
        WatermarkArtifact artifact = new WatermarkArtifact();        
        artifact.setText(formattedText);        
        artifact.setArtifactHorizontalAlignment (HorizontalAlignment.Center);
        artifact.setArtifactVerticalAlignment (VerticalAlignment.Center);
        artifact.setRotation (45);
        artifact.setOpacity (0.5);
        artifact.setBackground (true);
        doc.getPages().get_Item(1).getArtifacts().add(artifact);
        doc.save(_dataDir + "watermark.pdf");
    }

}  
```