---
title: Atualizar Links em PDF 
linktitle: Atualizar Links
type: docs
weight: 20
url: /pt/java/update-links/
description: Atualizar links em PDF programaticamente. Este guia é sobre como atualizar links em PDF na linguagem Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Atualizar Links no Arquivo PDF

Conforme discutido em Adicionar Hiperlink em um Arquivo PDF, a classe [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation) possibilita adicionar links em um arquivo PDF. Também existe uma classe similar usada para obter links existentes dentro de arquivos PDF. Use isso se você precisar atualizar um link existente. Para atualizar um link existente:

1. Carregue um arquivo PDF.
1. Vá para uma página específica no arquivo PDF.
1. Especifique o destino do link usando a propriedade Destination do objeto [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction).

1. A página de destino é especificada usando o construtor [XYZExplicitDestination](https://reference.aspose.com/pdf/java/com.aspose.pdf/XYZExplicitDestination).

### Definir Destino do Link para uma Página no Mesmo Documento

O trecho de código a seguir mostra como atualizar um link em um arquivo PDF e definir seu destino para a segunda página do documento.

```java
    public static void SetLinkTargetToAPageInTheSameDocument() {
        
        // Carregar o arquivo PDF
        Document document = new Document(_dataDir + "UpdateLinks.pdf");
        Page page = document.getPages().get_Item(1);
        // Obter a primeira anotação de link da primeira página do documento
        LinkAnnotation linkAnnot = (LinkAnnotation)page.getAnnotations().get_Item(1);

        // Modificação do link: alterar destino do link
        GoToAction goToAction = (GoToAction)linkAnnot.getAction();
        // Especificar o destino para objeto de link
        // Representa destino explícito que exibe a página com as coordenadas (esquerda, topo) posicionadas no canto superior esquerdo da
        // janela e o conteúdo da página ampliado pelo fator de zoom.
        // O 1º parâmetro é o número da página de destino.
        // O 2º é a coordenada esquerda
        // O 3º é a coordenada superior
        // O 4º argumento é o fator de zoom ao exibir a respectiva página. Usar 2 significa que a página será exibida com zoom de 200%
        goToAction.setDestination(new XYZExplicitDestination(1, 1, 2, 2 ));
        
        // Salvar o documento com o link atualizado
        document.save(_dataDir + "PDFLINK_Modified_UpdateLinks_out.pdf");        
    }
```


### Definir Destino do Link para um Endereço Web

Para atualizar o hiperlink para que ele aponte para um endereço web, instancie o objeto [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction) e passe-o para a propriedade Action do LinkAnnotation. O trecho de código a seguir mostra como atualizar um link em um arquivo PDF e definir seu alvo para um endereço web.

```java
    public static void SetLinkDestinationToWebAddress() {        
        // Carregar o arquivo PDF
        Document document = new Document(_dataDir + "UpdateLinks.pdf");
        Page page = document.getPages().get_Item(1);
    
        // Obter a primeira anotação de link da primeira página do documento
        LinkAnnotation linkAnnot = (LinkAnnotation)page.getAnnotations().get_Item(1);

        // Modificação do link: alterar ação do link e definir alvo como endereço web
        linkAnnot.setAction(new GoToURIAction("www.aspose.com"));
        
        // Salvar o documento com o link atualizado
        document.save(_dataDir + "PDFLINK_Modified_UpdateLinks_out.pdf");        
    }
```


### Definir o Alvo do Link para Outro Arquivo PDF

O trecho de código a seguir mostra como atualizar um link em um arquivo PDF e definir seu alvo para outro arquivo PDF.

```java
    public static void SetLinkTargetToAnotherPDFFile() {        
        // Carregar o arquivo PDF
        Document document = new Document(_dataDir + "UpdateLinks.pdf");
        Page page = document.getPages().get_Item(1);
    
        LinkAnnotation linkAnnot = (LinkAnnotation)page.getAnnotations().get_Item(1);

        GoToRemoteAction goToR = (GoToRemoteAction)linkAnnot.getAction();
        // A próxima linha atualiza o destino, não atualiza o arquivo
        goToR.setDestination(new XYZExplicitDestination(2, 0, 0, 1.5));
        // A próxima linha atualiza o arquivo
        goToR.setFile (new FileSpecification(_dataDir +  "input.pdf"));

        // Salvar o documento com o link atualizado
        document.save(_dataDir + "PDFLINK_Modified_UpdateLinks_out.pdf");        
    }
```

### Atualizar a Cor do Texto da LinkAnnotation

A anotação de link não contém texto.
 Em vez disso, o texto é colocado no conteúdo da página sob a anotação. Portanto, para alterar a cor do texto, substitua a cor do texto da página em vez de tentar alterar a cor da anotação. O trecho de código a seguir mostra como atualizar a cor da anotação de link em um arquivo PDF.

```java
    public static void UpdateLinkAnnotationTextColor () {        
        // Carregar o arquivo PDF
        Document document = new Document(_dataDir + "UpdateLinks.pdf");
        Page page = document.getPages().get_Item(1);
           
        for (Annotation annotation : page.getAnnotations())
        {
            if (annotation.getAnnotationType() == AnnotationType.Link)
            {
                // Pesquisar o texto sob a anotação
                TextFragmentAbsorber ta = new TextFragmentAbsorber();
                Rectangle rect = annotation.getRect();
                rect.setLLX(rect.getLLX()-10);
                rect.setLLY(rect.getLLY()-10);
                rect.setURX(rect.getURX()+ 10);
                rect.setURY(rect.getURY()+ 10);

                ta.setTextSearchOptions(new TextSearchOptions(rect));
                ta.visit(page);
                // Alterar a cor do texto.
                for (TextFragment tf : ta.getTextFragments())
                {
                    tf.getTextState().setForegroundColor(Color.getRed());
                }
            }
        
        }                       
        // Salvar o documento com link atualizado
        document.save(_dataDir + "UpdateLinkTextColor_out.pdf");        
    }
```