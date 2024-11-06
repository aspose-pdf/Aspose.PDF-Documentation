---
title: Trabalhando com Ações
linktitle: Ações
type: docs
weight: 20
url: pt/java/actions/
description: Esta seção explica como adicionar ações aos campos de documento e formulário programaticamente com Java. Aprenda como Adicionar, Criar e Obter Hiperlink em um Arquivo PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Um arquivo PDF pode conter anexos de arquivos incorporados e muitas vezes é necessário criar um Hiperlink para esses documentos. Você pode direcionar os leitores do documento PDF principal para um anexo PDF criando um link no documento pai que aponta para o anexo.

## Adicionar Hiperlink em Arquivo PDF

É possível adicionar hiperlinks a arquivos PDF, seja para permitir que os leitores naveguem para outra parte do PDF ou para conteúdo externo.

Para adicionar hiperlinks da web a documentos PDF:

1. Crie um objeto da Classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

1. Obtenha a classe [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) à qual você deseja adicionar o link.
1. Crie um objeto [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) usando os objetos Page e [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle). O objeto rectangle é usado para especificar a localização na página onde o link deve ser adicionado.
1. Defina o método getAction para o objeto [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/GoToURIAction), que especifica a localização do URI remoto.
1. Para exibir um texto de hiperlink, adicione uma string de texto em uma localização semelhante a onde o objeto [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) está colocado.
1. Para adicionar um texto livre:

- Instancie um objeto [FreeTextAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/FreeTextAnnotation).
 Aceita também objetos Page e Rectangle como argumento, então é possível fornecer os mesmos valores conforme especificado no construtor LinkAnnotation.
- Usando a propriedade Contents do objeto [FreeTextAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/FreeTextAnnotation), especifique a string que deve ser exibida no PDF de saída.
- Opcionalmente, defina a largura da borda dos objetos [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) e FreeTextAnnotation para 0, para que não apareçam no documento PDF.
- Uma vez que os objetos [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) e [FreeTextAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/FreeTextAnnotation) tenham sido definidos, adicione esses links à coleção Annotations do objeto [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).

- Finalmente, salve o PDF atualizado usando o método Save do objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
O trecho de código a seguir mostra como adicionar um hyperlink a um arquivo PDF.

```java
package com.aspose.pdf.examples;

import java.util.List;

import com.aspose.pdf.*;

public class ExampleActions {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Actions/";

    private static String GetDataDir() {
        String os = System.getProperty("os.name");
        if (os.startsWith("Windows"))
            _dataDir = "C:\\Samples\\Actions";
        return _dataDir;
    }

    public static void AddHyperlinkInPDFFile() {
        // Abrir documento
        Document document = new Document(GetDataDir() + "AddHyperlink.pdf");
        // Criar link
        Page page = document.getPages().get_Item(1);
        // Criar objeto de anotação de link
        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(100, 100, 300, 300));
        // Criar objeto de borda para LinkAnnotation
        Border border = new Border(link);
        // Definir o valor da largura da borda como 0
        border.setWidth(0);
        // Definir a borda para LinkAnnotation
        link.setBorder(border);
        // Especificar o tipo de link como URI remoto
        link.setAction(new GoToURIAction("www.aspose.com"));
        // Adicionar anotação de link à coleção de anotações da primeira página do arquivo PDF
        page.getAnnotations().add(link);

        // Criar anotação de texto livre
        FreeTextAnnotation textAnnotation = new FreeTextAnnotation(page, new Rectangle(100, 100, 300, 300),
                new DefaultAppearance(FontRepository.findFont("TimesNewRoman"), 10, java.awt.Color.BLUE));

        // String a ser adicionada como texto livre
        textAnnotation.setContents("Link para o site da Aspose");
        // Definir a borda para a anotação de texto livre
        textAnnotation.setBorder(border);
        // Adicionar anotação de texto livre à coleção de anotações da primeira página do documento
        page.getAnnotations().add(textAnnotation);

        // Salvar documento atualizado
        document.save(_dataDir + "AddHyperlink_out.pdf");

    }
```


## Criar Hiperlink para páginas no mesmo PDF

Aspose.PDF para Java oferece um ótimo recurso para a criação de PDF, bem como sua manipulação. Ele também oferece a funcionalidade de adicionar links às páginas do PDF, e um link pode direcionar para páginas em outro arquivo PDF, uma URL da web, link para iniciar um aplicativo ou até mesmo link para páginas no mesmo arquivo PDF.

Para adicionar o hiperlink local, precisamos criar um TextFragment para que o link possa ser associado ao TextFragment. A classe [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) possui um método chamado [getHyperlink](https://reference.aspose.com/pdf/java/com.aspose.pdf/BaseParagraph#getHyperlink--) que é usado para associar uma instância de LocalHyperlink. O trecho de código a seguir mostra as etapas para cumprir essa exigência.

```java
public static void CreateHyperlinkToPagesInSamePDF() {
        // Criar instância do Documento
        Document document = new Document();

        // Adicionar página à coleção de páginas do arquivo PDF
        Page page = document.getPages().add();

        // Criar instância do Fragmento de Texto
        TextFragment text = new TextFragment("link page number test to page 2");

        // Criar instância de hiperlink local
        LocalHyperlink link = new LocalHyperlink();

        // Definir página de destino para a instância de link
        link.setTargetPageNumber(2);

        // Definir hiperlink do Fragmento de Texto
        text.setHyperlink(link);

        // Adicionar texto à coleção de parágrafos da Página
        page.getParagraphs().add(text);

        // Criar nova instância do Fragmento de Texto
        text = new TextFragment("link page number test to page 1");

        // O Fragmento de Texto deve ser adicionado em uma nova página
        text.setInNewPage(true);

        // Criar outra instância de hiperlink local
        link = new LocalHyperlink();

        // Definir página de destino para o segundo hiperlink
        link.setTargetPageNumber(1);

        // Definir link para o segundo Fragmento de Texto
        text.setHyperlink(link);

        // Adicionar texto à coleção de parágrafos do objeto página
        page.getParagraphs().add(text);

        // Salvar documento atualizado
        document.save(GetDataDir() + "CreateLocalHyperlink_out.pdf");
    }
```


## Obter Destino do Hiperlink em PDF (URL)

Os links são representados como anotações em um arquivo PDF e podem ser adicionados, atualizados ou deletados. Aspose.PDF para Java também suporta obter o destino (URL) do hiperlink no arquivo PDF.

Para obter o URL de um link:

1. Crie um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Obtenha a [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) da qual você deseja extrair os links.
1. Use a classe [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationSelector) para extrair todos os objetos [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation)) da página especificada.
1. Passe o objeto [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationSelector) para o método Accept do objeto [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).

1. Obtenha todas as anotações de link selecionadas em um objeto IList usando a propriedade Selected do objeto [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationSelector).
1. Finalmente, extraia a Ação LinkAnnotation como GoToURIAction.

O seguinte trecho de código mostra como obter destinos de hiperlink (URL) de um arquivo PDF.

```java
    public static void GetPDFHyperlinkDestination() {
        Document document = new Document(GetDataDir() + "Aspose-app-list.pdf");
        // Extrair ações
        Page page = document.getPages().get_Item(1);
        AnnotationSelector selector = new AnnotationSelector(new LinkAnnotation(page, Rectangle.getTrivial()));
        page.accept(selector);
        List<Annotation> list = selector.getSelected();
        // Iterar através de cada item individual dentro da lista
        if (list.size() == 0)
            System.out.println("Nenhum hiperlink encontrado..");
        else {
            // Percorrer todos os marcadores
            for (Annotation annot : list) {
                LinkAnnotation la = (annot instanceof LinkAnnotation ? (LinkAnnotation) annot : null);
                if (la != null) {
                    // Imprimir o URL de destino
                    System.out.println("Destino: " + ((GoToURIAction) la.getAction()).getURI());
                }
            }
        } // fim do else
    }
```


## Obter Texto do Hiperlink

Um hiperlink possui duas partes: o texto que aparece no documento e a URL de destino. Em alguns casos, é o texto, e não a URL, que precisamos.

Texto e anotações/ações em um arquivo PDF são representados por diferentes entidades. O texto em uma página é apenas um conjunto de palavras e caracteres, enquanto as anotações trazem alguma interatividade, como a inerente a um hiperlink.

Para encontrar o conteúdo da URL, você precisa trabalhar com ambos, anotação e texto. O objeto [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/Annotation) não possui o texto, mas está sob o texto na página. Assim, para obter o texto, a Anotação fornece os limites da URL, enquanto o objeto Texto fornece o conteúdo da URL. Veja o trecho de código a seguir.

```java
    public static void GetHyperlinkText() {
        Document document = new Document(GetDataDir() + "Aspose-app-list.pdf");
        // Extrair ações
        Page page = document.getPages().get_Item(1);

        for (Annotation annot : page.getAnnotations()) {
            LinkAnnotation la = (annot instanceof LinkAnnotation ? (LinkAnnotation) annot : null);
            if (la != null) {
                // Imprimir a URL de cada Anotação de Link
                System.out.println("URI: " + ((GoToURIAction) la.getAction()).getURI());
                TextAbsorber absorber = new TextAbsorber();
                absorber.getTextSearchOptions().setLimitToPageBounds(true);
                absorber.getTextSearchOptions().setRectangle(annot.getRect());
                page.accept(absorber);
                String extractedText = absorber.getText();
                // Imprimir o texto associado ao hiperlink
                System.out.println(extractedText);
            }
        }
    }
```


## Remover Ação de Abertura de Documento de um Arquivo PDF

[Como Especificar a Página do PDF ao Visualizar o Documento](#how-to-specify-pdf-page-when-viewing-document) explicou como instruir um documento para abrir em uma página diferente da primeira. Ao concatenar vários documentos, e um ou mais tem uma ação GoTo definida, você provavelmente desejará removê-los. Por exemplo, se estiver combinando dois documentos e o segundo tiver uma ação GoTo que leva você à segunda página, o documento de saída abrirá na segunda página do segundo documento em vez da primeira página do documento combinado. Para evitar esse comportamento, remova o comando de ação de abertura.

Para remover uma ação de abertura:

1. Defina o método [getOpenAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getOpenAction--) do objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) como nulo.
2. Salve o PDF atualizado usando o método Save do objeto Document.

O trecho de código a seguir mostra como remover uma ação de abertura de documento do arquivo PDF.

```java
    public static void RemoveDocumentOpenActionFromPDFFile()
    {
        // Abrir documento
        Document document = new Document(_dataDir + "RemoveOpenAction.pdf");
        // Remover ação de abertura do documento
        document.setOpenAction(null);
        
        // Salvar documento atualizado
        document.save(GetDataDir()+"RemoveOpenAction_out.pdf");
    }
```


## Como Especificar a Página do PDF ao Visualizar Documento {#how-to-specify-pdf-page-when-viewing-document}

Ao visualizar arquivos PDF em um visualizador de PDF como o Adobe Reader, os arquivos geralmente abrem na primeira página. No entanto, é possível configurar o arquivo para abrir em uma página diferente.

A classe [XYZExplicitDestination](https://reference.aspose.com/pdf/java/com.aspose.pdf/XYZExplicitDestination) permite que você especifique uma página em um arquivo PDF que deseja abrir. Ao passar o valor do objeto GoToAction para o método getOpenAction da classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document), o documento é aberto na página especificada contra o objeto XYZExplicitDestination. O trecho de código a seguir mostra como especificar uma página como a ação de abertura do documento.

```java
    public static void HowToSpecifyPDFPageWhenViewingDocument()
    {
        // Carregar o arquivo PDF
        Document document = new Document(GetDataDir()+ "SpecifyPageWhenViewing.pdf");
        // Obter a instância da segunda página do documento
        Page page2 = document.getPages().get_Item(2);
        // Criar a variável para definir o fator de zoom da página alvo
        double zoom = 1;
        // Criar instância de GoToAction
        GoToAction action = new GoToAction(page2);
        // Ir para a página 2
        action.setDestination (new XYZExplicitDestination(page2, 0, page2.getRect().getHeight(), zoom));
        // Definir a ação de abertura do documento
        document.setOpenAction (action);
        // Salvar documento atualizado
        document.save(_dataDir + "goto2page_out.pdf");
    }
}
```