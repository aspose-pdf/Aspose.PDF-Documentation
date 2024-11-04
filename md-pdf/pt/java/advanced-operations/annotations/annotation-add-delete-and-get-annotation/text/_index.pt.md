---
title: Anotação de Texto em PDF
Texttitle: Anotação de Texto
type: docs
weight: 10
url: /java/text-annotation/
description: Aspose.PDF para Java permite que você Adicione, Obtenha e Exclua Anotações de Texto do seu documento PDF.
lastmod: "2021-11-24"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

Adicionar, Excluir e Obter Anotação são semelhantes para diferentes tipos de anotações. Vamos tomar como exemplo uma Anotação de Texto.

## Como adicionar Anotação de Texto em um arquivo PDF existente

Neste tutorial, você aprenderá como adicionar texto a um documento PDF existente. A ferramenta de texto permite que você adicione texto em qualquer lugar do documento. Uma Anotação de Texto é uma anotação anexada a um local específico em um documento PDF. Quando fechada, a anotação é exibida como um ícone; quando aberta, deve exibir uma janela pop-up contendo o texto da nota na fonte e tamanho escolhidos pelo leitor.

As anotações são contidas pela coleção [Annotations](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/AnnotationCollection) de uma Página específica.
 Esta coleção contém as anotações apenas para aquela página individual; cada página tem sua própria coleção de Anotações.

Para adicionar uma anotação a uma página específica, adicione-a à coleção de Anotações daquela página com o método Add.

1. Primeiro, crie uma anotação que você deseja adicionar ao PDF.
1. Em seguida, abra o PDF de entrada.
1. Adicione a anotação à coleção de Anotações do objeto [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).

O trecho de código a seguir mostra como adicionar uma anotação em uma página PDF.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import java.util.*;

public class ExampleTextAnnotation {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/";

    public static void AddTextAnnotation()
    {
        // Carregar o arquivo PDF
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);
        Rectangle rect = new Rectangle(200, 750, 400, 790);
        TextAnnotation textAnnotation = new TextAnnotation(page, rect);

        textAnnotation.setTitle("Usuário Aspose");
        textAnnotation.setSubject("Assunto de Exemplo");
        textAnnotation.setState (AnnotationState.Accepted);
        textAnnotation.setContents("Conteúdo de exemplo para a anotação");
        textAnnotation.setOpen(true);
        textAnnotation.setIcon(TextIcon.Circle);

        Border border = new Border(textAnnotation);
        border.setWidth(5);
        border.setDash(new Dash(1, 1));
        textAnnotation.setBorder(border);
        textAnnotation.setRect(rect);

        page.getAnnotations().add(textAnnotation);
        document.save(_dataDir + "sample_textannot.pdf");
    }
}
```

## Adicionar Nova (ou Criar) Anotação de Texto Livre

Uma anotação de texto livre exibe texto diretamente na página. O método PdfContentEditor.CreateFreeText permite criar este tipo de anotação. No trecho a seguir, adicionamos uma anotação de texto livre acima da primeira ocorrência da string.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import java.util.*;

public class ExampleFreeTextAnnotation {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/";

    public static void AddFreeTextAnnotation()
    {
        // Carregar o arquivo PDF
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        DefaultAppearance defaultAppearance = new DefaultAppearance();
        defaultAppearance.setFontName("Helvetica");
        defaultAppearance.setFontSize(12);
        defaultAppearance.setTextColor(java.awt.Color.BLUE);

        FreeTextAnnotation freeTextAnnotation = new FreeTextAnnotation(page, new Rectangle(300.0, 770.0, 400.0, 790.0), defaultAppearance);

        freeTextAnnotation.setRichText("Demonstração de Texto Livre");
        page.getAnnotations().add(freeTextAnnotation);
        document.save(_dataDir + "sample_freetext.pdf");
    }
}
```


## Obter Anotação de Texto Livre

Aspose.PDF para Java permite que você obtenha Anotação de Texto Livre do seu documento PDF.

Por favor, verifique o próximo trecho de código para resolver esta tarefa:

```java
public static void GetFreeTextAnnotation() {
        // Carregar o arquivo PDF
        Document document = new Document(_dataDir + "sample_freetext.pdf");

        // Filtrar anotações usando AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new FreeTextAnnotation(page, Rectangle.getTrivial(), new DefaultAppearance()));
        page.accept(annotationSelector);
        List<Annotation> freeTextAnnotations = annotationSelector.getSelected();

        // imprimir resultados
        for (Annotation fa : freeTextAnnotations) {
            System.out.println(fa.getRect());
        }
    }
```

## Excluir Anotação de Texto Livre

Aspose.PDF para Java permite que você exclua Anotação de Texto Livre do seu documento PDF.

Por favor, verifique o próximo trecho de código para resolver esta tarefa:

```java
  public static void DeleteFreeTextAnnotation() {
         // Carregar o arquivo PDF
         Document document = new Document(_dataDir + "sample_freetext.pdf");

         // Filtrar anotações usando AnnotationSelector
         Page page = document.getPages().get_Item(1);
         AnnotationSelector annotationSelector = new AnnotationSelector(
                 new FreeTextAnnotation(page, Rectangle.getTrivial(), new DefaultAppearance()));
         page.accept(annotationSelector);
         List<Annotation> freeTextAnnotations = annotationSelector.getSelected();

         // excluir anotações
         for (Annotation fa : freeTextAnnotations) {
            page.getAnnotations().delete(fa);
        }
        document.save(_dataDir + "sample_freetext_del.pdf");
    }
```

## Excluir Todas as Anotações da Página de um Arquivo PDF

A coleção [AnnotationCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/AnnotationCollection) do objeto [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) contém todas as anotações para essa página específica.
 Para excluir todas as anotações de uma página, chame o método *Delete* da coleção AnnotationCollection.

O trecho de código a seguir mostra como excluir todas as anotações de uma página específica.

```java
    public static void DeleteTextAnnotation() {
         // Carregar o arquivo PDF
         Document document = new Document(_dataDir + "sample_textannot.pdf");

         // Filtrar anotações usando AnnotationSelector
         Page page = document.getPages().get_Item(1);
         AnnotationSelector annotationSelector = new AnnotationSelector(
                 new TextAnnotation(page, Rectangle.getTrivial()));
         page.accept(annotationSelector);
         List<Annotation> TextAnnotations = annotationSelector.getSelected();

         // excluir anotações
         for (Annotation fa : TextAnnotations) {
            page.getAnnotations().delete(fa);
        }
        document.save(_dataDir + "sample_textannot_del.pdf");
    }
```

## Obter Todas as Anotações de uma Página de Documento PDF

Aspose.PDF permite que você obtenha anotações de um documento inteiro ou de uma página específica. Para obter todas as anotações da página em um documento PDF, percorra a coleção [AnnotationCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/AnnotationCollection) dos recursos da página desejada. O trecho de código a seguir mostra como obter todas as anotações de uma página.

```java
  public static void GetTextAnnotation() {
        // Carregar o arquivo PDF
        Document document = new Document(_dataDir + "sample_textannot.pdf");

        // Filtrar anotações usando AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new TextAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> TextAnnotations = annotationSelector.getSelected();

        // imprimir resultados
        for (Annotation fa : TextAnnotations) {
            System.out.println(fa.getRect());
        }
    }
```