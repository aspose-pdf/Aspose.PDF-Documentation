---
title: Trabalhando com Artefatos 
linktitle: Trabalhando com Artefatos
type: docs
weight: 110
url: pt/java/artifacts/
description: Esta página descreve como trabalhar com a classe Artifact usando Aspose.PDF para Java. Trechos de código mostram como adicionar uma imagem de fundo às páginas do PDF e como obter cada marca d'água na primeira página de um arquivo PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Artefatos são geralmente objetos gráficos ou outras marcas que não fazem parte do conteúdo original. Nos seus exemplos de PDF, artefatos incluem diferentes informações, como cabeçalho ou rodapé de página, linhas ou outros gráficos que separam seções da página, ou imagens decorativas.

A classe [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact) contém:

- [Artifact.Type](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact.ArtifactType) – obtém o tipo de artefato (suporta valores da enumeração Artifact.ArtifactType onde os valores incluem Background, Layout, Page, Pagination e Undefined).
- [Artifact.Subtype](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact.ArtifactSubtype) – obtém o subtipo do artefato (suporta os valores da enumeração Artifact.ArtifactSubtype onde os valores incluem Background, Footer, Header, Undefined, Watermark).

Uma marca d'água criada com o Adobe Acrobat é chamada de artefato (conforme descrito em 14.8.2.2 Conteúdo Real e Artefatos da especificação PDF). Para trabalhar com artefatos, o Aspose.PDF possui duas classes: [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact) e [ArtifactCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/ArtifactCollection).

Para obter todos os artefatos em uma página específica, a classe [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) possui a propriedade Artifacts. Este tópico explica como trabalhar com artefatos em arquivos PDF.

O trecho de código a seguir mostra como definir a marca d'água na primeira página de um arquivo PDF.

```java

 public class ExamplesArtifacts {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Artifacts/";

    public static void SetWatermark(){
        Document doc = new Document(_dataDir + "sample.pdf");
        WatermarkArtifact artifact = new WatermarkArtifact();        
        artifact.setText(new FormattedText("WATERMARK", java.awt.Color.BLUE, 
                            FontStyle.Courier,
                            EncodingType.Identity_h, true, 72));
        artifact.setArtifactHorizontalAlignment (HorizontalAlignment.Center);
        artifact.setArtifactVerticalAlignment (VerticalAlignment.Center);
        artifact.setRotation (45);
        artifact.setOpacity (0.5);
        artifact.setBackground (true);
        doc.getPages().get_Item(1).getArtifacts().add(artifact);
        doc.save(_dataDir + "watermark.pdf");
    }
```


Imagens de fundo podem ser usadas para adicionar uma marca d'água, ou outro design sutil, a documentos. No Aspose.PDF para Java, cada documento PDF é uma coleção de páginas e cada página contém uma coleção de artefatos. A classe [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/BackgroundArtifact) pode ser usada para adicionar uma imagem de fundo a um objeto de página.

O trecho de código a seguir mostra como adicionar uma imagem de fundo às páginas do PDF usando o objeto BackgroundArtifact.

```java

    public static void SetBackground() throws FileNotFoundException {

        // Abrir documento
        Document pdfDocument = new Document();
                
        // Adicionar uma nova página ao objeto documento
        Page page = pdfDocument.getPages().add();

        // Criar objeto Background Artifact
        BackgroundArtifact background = new BackgroundArtifact();

        // Especificar a imagem para o objeto backgroundartifact
        background.setBackgroundImage(new java.io.FileInputStream(new java.io.File(_dataDir + "background.png")));
        
        // Adicionar BackgroundArtifact à coleção de artefatos da página
        page.getArtifacts().add(background);

        // Salvar PDF modificado
        pdfDocument.save(_dataDir + "ImageAsBackground_out.pdf");

    }
```


## Exemplos de Programação: Obtendo Marca d'Água

O trecho de código a seguir mostra como obter cada marca d'água na primeira página de um arquivo PDF.

```java
    public static void GettingWatermarks() {
        // Abrir documento
        Document pdfDocument = new Document(_dataDir +  "watermark_new.pdf");
        // Iterar e obter subtipo, texto e localização do artefato
        for (Artifact artifact : pdfDocument.getPages().get_Item(1).getArtifacts())
        {
            System.out.println(artifact.getSubtype() + " " + artifact.getText() + " " + artifact.getRectangle().toString());
        }
```

## Exemplos de Programação: Contando Artefatos de um Tipo Específico

Para calcular o total de artefatos de um tipo específico (por exemplo, o número total de marcas d'água), use o seguinte código:

```java
    public static void CountingArtifacts() {
        // Abrir documento
        Document pdfDocument = new Document(_dataDir +  "watermark_new.pdf");
        int count = 0;
        for (Artifact artifact : pdfDocument.getPages().get_Item(1).getArtifacts())
        {
            // Se o tipo do artefato é marca d'água, incrementar o contador
            if (artifact.getSubtype() == Artifact.ArtifactSubtype.Watermark) count++;
        }
        System.out.println("A página contém " + count + " marcas d'água");
    }
```