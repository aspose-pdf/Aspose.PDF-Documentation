---
title: Adicionar carimbos de texto em PDF programaticamente
linktitle: Carimbos de texto no arquivo PDF
type: docs
weight: 20
url: /java/text-stamps-in-the-pdf-file/
description: Adicionar um carimbo de texto a um arquivo PDF usando a classe TextStamp com Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Adicionar Carimbo de Texto com Java

Aspose.PDF para Java fornece a classe [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) para adicionar um carimbo de texto em um arquivo PDF.
 A classe [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) fornece métodos necessários para especificar o tamanho da fonte, estilo da fonte e cor da fonte, etc., para o objeto de carimbo. Para adicionar um carimbo de texto, primeiro você precisa criar um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) e um objeto [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) usando os métodos necessários. Depois disso, você pode chamar o método [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-) da classe [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) para adicionar o carimbo no documento PDF.

O trecho de código a seguir mostra como adicionar um carimbo de texto no arquivo PDF.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import com.aspose.pdf.facades.*;
import com.aspose.pdf.facades.Stamp;

public class ExampleStampingImage {
    // O caminho para o diretório dos documentos.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddTextStamp() {
        // abrir documento
        Document pdfDocument = new Document("input.pdf");
        // criar carimbo de texto
        TextStamp textStamp = new TextStamp("Sample Stamp");
        // definir se o carimbo é plano de fundo
        textStamp.setBackground(true);
        // definir origem
        textStamp.setXIndent(100);
        textStamp.setYIndent(100);
        // girar carimbo
        textStamp.setRotate(Rotation.on90);
        // definir propriedades do texto
        textStamp.getTextState().setFont(FontRepository.findFont("Arial"));
        textStamp.getTextState().setFontSize(14.0F);
        textStamp.getTextState().setFontStyle(FontStyles.Bold);
        textStamp.getTextState().setFontStyle(FontStyles.Italic);
        textStamp.getTextState().setForegroundColor(Color.getGreen());
        // adicionar carimbo a uma página específica
        pdfDocument.getPages().get_Item(1).addStamp(textStamp);
        // salvar documento de saída
        pdfDocument.save("TextStamp_output.pdf");
    }
```

## Definir alinhamento para o objeto TextStamp

Adicionar marcas d'água a documentos PDF é um dos recursos frequentemente exigidos e o Aspose.PDF para Java é totalmente capaz de adicionar marcas d'água de imagem, bem como de texto. A classe [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) fornece o recurso de adicionar carimbos de texto sobre o arquivo PDF. Recentemente, houve uma necessidade de suportar o recurso de especificar o alinhamento do texto ao usar o objeto [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp). Portanto, para atender a essa necessidade, introduzimos o método setTextAlignment(..) na classe [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp). Usando este método, você pode especificar o alinhamento horizontal do texto.

Os trechos de código a seguir mostram um exemplo de como carregar um documento PDF existente e adicionar [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) sobre ele.

```java
    public static void DefineAlignmentTextStamp() {
        // Instanciar objeto Document com arquivo de entrada
        Document pdfDocument = new Document("input.pdf");
        // instanciar objeto FormattedText com string de exemplo
        FormattedText text = new FormattedText("This");
        
        // adicionar nova linha de texto ao FormattedText
        text.addNewLineText("is sample");
        text.addNewLineText("Center Aligned");
        text.addNewLineText("TextStamp");
        text.addNewLineText("Object");
        // criar objeto TextStamp usando FormattedText
        TextStamp stamp = new TextStamp(text);
        // especificar o Alinhamento Horizontal do carimbo de texto como Centralizado
        stamp.setHorizontalAlignment(HorizontalAlignment.Center);
        // especificar o Alinhamento Vertical do carimbo de texto como Centralizado
        stamp.setVerticalAlignment(VerticalAlignment.Center);
        // especificar o Alinhamento Horizontal do Texto do TextStamp como Centralizado
        stamp.setTextAlignment(HorizontalAlignment.Center);
        // definir margem superior para o objeto stamp
        stamp.setTopMargin(20);
        // adicionar carimbo a todas as páginas do arquivo PDF
        pdfDocument.getPages().get_Item(1).addStamp(stamp);
        
        // salvar documento de saída
        pdfDocument.save("TextStamp_output.pdf");
    }
```


## Preencher Texto de Contorno como Carimbo em Arquivo PDF

Implementamos a configuração do modo de renderização para cenários de adição e edição de texto. Para renderizar texto de contorno, por favor crie um objeto [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextState) e defina RenderingMode como TextRenderingMode.StrokeText e também selecione a cor para a propriedade StrokingColor. Posteriormente, vincule o TextState ao carimbo usando o método BindTextState().

O trecho de código a seguir demonstra como adicionar Texto de Preenchimento de Contorno:

```java
   public static void FillStrokeTextAsStampInPDFFile(){
        // Criar objeto TextState para transferir propriedades avançadas
        TextState ts = new TextState();
        
        // Definir cor para o contorno
        ts.setStrokingColor(Color.getGray());
        
        // Definir modo de renderização do texto
        ts.setRenderingMode (TextRenderingMode.StrokeText);
        
        // Carregar um documento PDF de entrada
        PdfFileStamp fileStamp = new PdfFileStamp(new Document(_dataDir + "input.pdf"));

        Stamp stamp = new Stamp();
        stamp.bindLogo(new FormattedText("PAID IN FULL", java.awt.Color.GRAY, "Arial", EncodingType.Winansi, true, 78));

        // Vincular TextState
        stamp.bindTextState(ts);
        // Definir origem X,Y
        stamp.setOrigin(100, 100);
        stamp.setOpacity (5);
        stamp.setBlendingSpace (BlendingColorSpace.DeviceRGB);
        stamp.setRotation (45.0F);
        stamp.setBackground(false);
        // Adicionar Carimbo
        fileStamp.addStamp(stamp);
        fileStamp.save(_dataDir + "ouput_out.pdf");
        fileStamp.close();
    }
```