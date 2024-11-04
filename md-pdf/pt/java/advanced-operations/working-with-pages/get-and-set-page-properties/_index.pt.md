---
title: Obter e Definir Propriedades da Página
type: docs
weight: 30
url: /java/get-and-set-page-properties/
description: Este tópico explica como obter números em um arquivo PDF, obter propriedades da página e determinar a cor da página usando Aspose.PDF para Java.
lastmod: "2021-06-05"
---

Aspose.PDF para Java permite ler e definir propriedades de páginas em um arquivo PDF em suas aplicações Java. Esta seção mostra como obter o número de páginas em um arquivo PDF, obter informações sobre as propriedades da página PDF, como cor, e definir propriedades da página.

## Obter Número de Páginas em um Arquivo PDF

Ao trabalhar com documentos, muitas vezes você quer saber quantas páginas eles contêm. Com Aspose.PDF isso não leva mais do que duas linhas de código.

Para obter o número de páginas em um arquivo PDF:

1. Abra o arquivo PDF usando a classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

1. Em seguida, use a propriedade Count da coleção [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/PageCollection) (do objeto Document) para obter o número total de páginas no documento.

O trecho de código a seguir mostra como obter o número de páginas de um arquivo PDF.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleGetAndSetPageProperties {
    // O caminho para o diretório dos documentos.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void GetNumberOfPagesInaPDFFile() {

        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "GetNumberofPages.pdf");

        // Obter contagem de páginas
        System.out.println("Contagem de Páginas : " + pdfDocument.getPages().size());
        _dataDir = _dataDir + "ApplyNumberStyle_out.pdf";
        pdfDocument.save(_dataDir);

    }
```

### Obter contagem de páginas sem salvar o documento

A menos que o arquivo PDF seja salvo e todos os elementos sejam realmente colocados dentro do arquivo PDF, não podemos obter a contagem de páginas para um documento específico (porque não podemos ter certeza sobre o número de páginas em que todos os elementos serão acomodados).
 No entanto, a partir do lançamento do Aspose.PDF para Java 10.1.0, introduzimos um método chamado [processParagraphs(...)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#processParagraphs--) que fornece a funcionalidade de obter a contagem de páginas para um documento PDF, sem salvar o arquivo. Assim, podemos obter a informação de contagem de páginas instantaneamente. Por favor, tente usar o seguinte trecho de código para cumprir este requisito.

```java
public static void GetPageCountWithoutSavingTheDocument() {

        // Para exemplos completos e arquivos de dados, por favor acesse
        // https://github.com/aspose-pdf/Aspose.Pdf-for-Java
        // instanciar a instância do Document
        Document doc = new Document();
        // adicionar página à coleção de páginas do arquivo PDF
        Page page = doc.getPages().add();
        // criar um loop para adicionar 300 instâncias de TextFragment
        for (int i = 0; i < 300; i++)
            // adicionar TextFragment à coleção de parágrafos da primeira página do PDF
            page.getParagraphs().add(new TextFragment("Teste de contagem de páginas"));
        // processar parágrafos para obter informações de contagem de páginas
        doc.processParagraphs();
        System.out.println("Número de Páginas no PDF = " + doc.getPages().size());
    }
```

## Obter Propriedades da Página

Cada página em um arquivo PDF possui várias propriedades, como largura, altura, bleed-, crop- e trimbox. Aspose.PDF permite que você acesse essas propriedades.

### **Compreendendo as Propriedades da Página: a Diferença entre as Propriedades Artbox, BleedBox, CropBox, MediaBox, TrimBox e Rect**

- **Caixa de mídia**: A caixa de mídia é a maior caixa da página. Ela corresponde ao tamanho da página (por exemplo, A4, A5, Carta dos EUA, etc.) selecionado quando o documento foi impresso em PostScript ou PDF. Em outras palavras, a caixa de mídia determina o tamanho físico do meio no qual o documento PDF é exibido ou impresso.
- **Caixa de sangramento**: Se o documento tiver sangramento, o PDF também terá uma caixa de sangramento.
 Bleed é a quantidade de cor (ou arte) que se estende além da borda de uma página. É usado para garantir que, quando o documento for impresso e cortado no tamanho (“refilado”), a tinta irá até a borda da página. Mesmo que a página seja mal refilada - cortada ligeiramente fora das marcas de corte - não aparecerão bordas brancas na página.
- **Caixa de refilo**: A caixa de refilo indica o tamanho final de um documento após a impressão e o corte.
- **Caixa de arte**: A caixa de arte é a caixa desenhada ao redor do conteúdo real das páginas em seus documentos. Esta caixa de página é usada ao importar documentos PDF em outras aplicações.
- **Caixa de corte**: A caixa de corte é o tamanho da “página” em que seu documento PDF é exibido no Adobe Acrobat. Na visualização normal, apenas o conteúdo da caixa de corte é exibido no Adobe Acrobat. Para descrições detalhadas dessas propriedades, leia a especificação Adobe.Pdf, particularmente 10.10.1 Limites de Página.
- **Page.Rect**: a interseção (retângulo comumente visível) do MediaBox e DropBox. A imagem abaixo ilustra essas propriedades.

Para mais detalhes, por favor visite [esta página](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

### Acessando Propriedades da Página

A classe [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) fornece todas as propriedades relacionadas a uma página PDF específica. Todas as páginas dos arquivos PDF estão contidas na coleção [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/PageCollection) do objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

A partir daí, é possível acessar objetos Page individuais usando seu índice, ou percorrer a coleção, usando um loop foreach, para obter todas as páginas. Uma vez que uma página individual é acessada, podemos obter suas propriedades. O seguinte trecho de código mostra como obter propriedades de página.

```java
    public static void AccessingPageProperties() {

        Document pdfDocument = new Document("input.pdf");

        // Obter a coleção de páginas
        PageCollection pageCollection = pdfDocument.getPages();

        // Obter uma página específica
        Page pdfPage = pageCollection.get_Item(1);

        // Obter as propriedades da página
        System.out.printf("\n ArtBox : Altura = " + pdfPage.getArtBox().getHeight() + ", Largura = "
                + pdfPage.getArtBox().getWidth() + ", LLX = " + pdfPage.getArtBox().getLLX() + ", LLY = "
                + pdfPage.getArtBox().getLLY() + ", URX = " + pdfPage.getArtBox().getURX() + ", URY = "
                + pdfPage.getArtBox().getURY());
        System.out.printf("\n BleedBox : Altura = " + pdfPage.getBleedBox().getHeight() + ", Largura = "
                + pdfPage.getBleedBox().getWidth() + ", LLX = " + pdfPage.getBleedBox().getLLX() + ", LLY = "
                + pdfPage.getBleedBox().getLLY() + ", URX = " + pdfPage.getBleedBox().getURX() + ", URY = "
                + pdfPage.getBleedBox().getURY());
        System.out.printf("\n CropBox : Altura = " + pdfPage.getCropBox().getHeight() + ", Largura = "
                + pdfPage.getCropBox().getWidth() + ", LLX = " + pdfPage.getCropBox().getLLX() + ", LLY = "
                + pdfPage.getCropBox().getLLY() + ", URX = " + pdfPage.getCropBox().getURX() + ", URY = "
                + pdfPage.getCropBox().getURY());
        System.out.printf("\n MediaBox : Altura = " + pdfPage.getMediaBox().getHeight() + ", Largura = "
                + pdfPage.getMediaBox().getWidth() + ", LLX = " + pdfPage.getMediaBox().getLLX() + ", LLY = "
                + pdfPage.getMediaBox().getLLY() + ", URX = " + pdfPage.getMediaBox().getURX() + ", URY = "
                + pdfPage.getMediaBox().getURY());
        System.out.printf("\n TrimBox : Altura = " + pdfPage.getTrimBox().getHeight() + ", Largura = "
                + pdfPage.getTrimBox().getWidth() + ", LLX = " + pdfPage.getTrimBox().getLLX() + ", LLY = "
                + pdfPage.getTrimBox().getLLY() + ", URX = " + pdfPage.getTrimBox().getURX() + ", URY = "
                + pdfPage.getTrimBox().getURY());
        System.out.printf(
                "\n Rect : Altura = " + pdfPage.getRect().getHeight() + ", Largura = " + pdfPage.getRect().getWidth()
                        + ", LLX = " + pdfPage.getRect().getLLX() + ", LLY = " + pdfPage.getRect().getLLY() + ", URX = "
                        + pdfPage.getRect().getURX() + ", URY = " + pdfPage.getRect().getURY());
        System.out.printf("\n Número da Página :- " + pdfPage.getNumber());
        System.out.printf("\n Rotacionar :-" + pdfPage.getRotate());
    }
```

## Determinar Cor da Página

A classe [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) fornece as propriedades relacionadas a uma página específica em um documento PDF, incluindo que tipo de cor - RGB, preto e branco, escala de cinza ou indefinido - a página utiliza.

Todas as páginas dos arquivos PDF estão contidas na coleção [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection). A propriedade [ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/ColorType) especifica a cor dos elementos na página. Para obter ou determinar as informações de cor de uma página PDF específica, use a propriedade [ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/ColorType) do objeto da classe [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).

O trecho de código a seguir mostra como iterar através de cada página do arquivo PDF para obter informações de cor.

```java
    public static void DeterminePageColor () {

        Document pdfDocument = new Document("input.pdf");
        // Iterar através de todas as páginas do arquivo PDF
        for (int pageCount = 1; pageCount <= pdfDocument.getPages().size(); pageCount++) {
            // Obter as informações do tipo de cor para uma página PDF específica
            int pageColorType = pdfDocument.getPages().get_Item(pageCount).getColorType();
            switch (pageColorType) {
            case 2:
                System.out.println("Página # -" + pageCount + " é Preto e branco..");
                break;
            case 1:
                System.out.println("Página # -" + pageCount + " é Escala de Cinza...");
                break;
            case 0:
                System.out.println("Página # -" + pageCount + " é RGB..");
                break;
            case 3:
                System.out.println("Página # -" + pageCount + " Cor é indefinida..");
                break;
            }
        }
    }
}
```