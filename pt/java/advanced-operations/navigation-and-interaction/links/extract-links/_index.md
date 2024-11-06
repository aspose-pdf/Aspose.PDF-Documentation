---
title: Extrair Links do Arquivo PDF
linktitle: Extrair Links
type: docs
weight: 30
url: pt/java/extract-links/
description: Extraia links de PDF com Java. Este tópico explica como extrair links usando a classe AnnotationSelector.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extrair Links do Arquivo PDF

Links são representados como anotações em um arquivo PDF, então para extrair links, extraia todos os objetos [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation).

1. Crie um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Obtenha a [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) da qual você deseja extrair links.
1. Use a classe [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationselector) para extrair todos os objetos [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) da página especificada.

1. Passe o objeto [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationselector) para o método Accept do objeto Page.
1. Obtenha todas as anotações de link selecionadas em um objeto IList usando o método [getSelected](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationSelector#getSelected--) do objeto [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationselector).

O trecho de código a seguir mostra como extrair links de um arquivo PDF.

```java
    public static void ExtractLinksFromThePDFFile() {        
        // Carregar o arquivo PDF
        Document document = new Document(_dataDir + "UpdateLinks.pdf");
        Page page = document.getPages().get_Item(1);
           
        AnnotationSelector selector = new AnnotationSelector(new LinkAnnotation(page, Rectangle.getTrivial()));
        page.accept(selector);
        java.util.List<Annotation> list = selector.getSelected();
        for(Annotation annot : list)
        {
            System.out.println("Anotação localizada: " + annot.getRect());
        }
                
        // Salvar o documento com link atualizado
        //document.save(_dataDir + "ExtractLinks_out.pdf");
    }
```