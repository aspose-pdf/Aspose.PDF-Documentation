---
title: Usando tipos extras de anotações em PDF
linktitle: Anotações Extras
type: docs
weight: 60
url: pt/java/extra-annotations/
description: Esta seção descreve como adicionar, obter e excluir tipos extras de anotações do seu documento PDF.
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Como adicionar Anotação de Marca em um arquivo PDF existente

A Anotação de Marca é um símbolo que indica edição de texto. A Anotação de Marca também é uma anotação de marcação, então a classe Caret deriva da classe Markup e também fornece funções para obter ou definir propriedades da Anotação de Marca e redefinir o fluxo da aparência da Anotação de Marca.

Passos com os quais criamos a anotação de marca:

1. Carregue o arquivo PDF - novo [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

1. Crie uma nova [Caret Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/CaretAnnotation) e defina os parâmetros de Caret (novo Retângulo, título, Assunto, Flags, cor, largura, StartingStyle e EndingStyle). Esta anotação é usada para indicar a inserção de texto.
1. Crie uma nova [StrikeOutAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/StrikeOutAnnotation) e defina os parâmetros (novo Retângulo, título, cor, novos QuadPoints e novos pontos, Assunto, InReplyTo, ReplyType).
1. Depois podemos adicionar anotações à página.

O trecho de código a seguir mostra como adicionar uma Anotação de Caret a um arquivo PDF:

```java
package com.aspose.pdf.examples;

import java.util.*;
import com.aspose.pdf.*;

public class ExampleCaretAnnotation {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddCaretAnnotation() {
        // Carregar o arquivo PDF
        Document document = new Document(_dataDir + "sample.pdf");
        // Esta anotação é usada para indicar a inserção de texto
        CaretAnnotation caretAnnotation1 = new CaretAnnotation(
                document.getPages().get_Item(1), new Rectangle(299.988, 713.664, 308.708, 720.769));
        caretAnnotation1.setTitle("Usuário Aspose");
        caretAnnotation1.setSubject("Texto inserido 1");
        caretAnnotation1.setFlags(AnnotationFlags.Print);
        caretAnnotation1.setColor(Color.getBlue());

        // Esta anotação é usada para indicar a substituição de texto
        CaretAnnotation caretAnnotation2 = new CaretAnnotation(
                document.getPages().get_Item(1), new Rectangle(361.246, 727.908, 370.081, 735.107));

        caretAnnotation2.setTitle("Usuário Aspose");
        caretAnnotation2.setFlags(AnnotationFlags.Print);
        caretAnnotation2.setSubject("Texto inserido 2");
        caretAnnotation2.setColor(Color.getBlue());

        StrikeOutAnnotation strikeOutAnnotation = new StrikeOutAnnotation(
                document.getPages().get_Item(1), new Rectangle(318.407, 727.826, 368.916, 740.098));

        strikeOutAnnotation.setColor(Color.getBlue());
        strikeOutAnnotation.setQuadPoints(new Point[] { new Point(321.66, 739.416),
                new Point(365.664, 739.416), new Point(321.66, 728.508),
                new Point(365.664, 728.508) });

        strikeOutAnnotation.setSubject("Riscar");
        strikeOutAnnotation.setInReplyTo(caretAnnotation2);
        strikeOutAnnotation.setReplyType(ReplyType.Group);

        document.getPages().get_Item(1).getAnnotations().add(caretAnnotation1);
        document.getPages().get_Item(1).getAnnotations().add(caretAnnotation2);
        document.getPages().get_Item(1).getAnnotations().add(strikeOutAnnotation);

        document.save(_dataDir + "sample_caret.pdf");

    }
```


## Obter Anotação de Marca

Por favor, tente usar o seguinte trecho de código para Obter Anotação de Marca em um documento PDF

```java
    public static void GetCaretAnnotation() {
        // Carregar o arquivo PDF
        Document document = new Document(_dataDir + "sample_caret.pdf");

        // Filtrar anotações usando AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new CaretAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> caretAnnotations = annotationSelector.getSelected();

        // imprimir resultados
        for (Annotation ca : caretAnnotations) {
            System.out.println(ca.getRect());
        }
    }
```

## Excluir Anotação de Marca

O trecho de código a seguir mostra como Excluir Anotação de Marca de um arquivo PDF.

```java
public static void DeleteCaretAnnotation() {
        // Carregar o arquivo PDF
        Document document = new Document(_dataDir + "sample_caret.pdf");

        // Filtrar anotações usando AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new CaretAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> caretAnnotations = annotationSelector.getSelected();

        // excluir anotação
        for (Annotation ca : caretAnnotations) {
            document.getPages().get_Item(1).getAnnotations().delete(ca);
        }
        document.save(_dataDir + "sample_caret_del.pdf");
    }
```


A [Link Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) é um hiperlink que leva a um destino em outro lugar no documento ou a uma ação a ser executada.

## Adicionar Anotação de Link

Um Link é uma área retangular que pode ser colocada em qualquer lugar da página. Cada link tem uma ação PDF correspondente associada a ele. Esta ação é executada quando o usuário clica na área deste link.

O seguinte trecho de código mostra como adicionar Anotação de Link a um arquivo PDF usando um exemplo de número de telefone:

```java
package com.aspose.pdf.examples;

import java.util.*;
import com.aspose.pdf.*;

public class ExampleLinkAnnotation {

    // O caminho para o diretório de documentos.

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddLinkAnnotation() {
        try {
            // Carregar o arquivo PDF
            Document document = new Document(_dataDir + "SimpleResume.pdf");
            Page page = document.getPages().get_Item(1);

            // Criar objeto TextFragmentAbsorber para encontrar um número de telefone
            TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("678-555-0103");

            // Aceitar o absorvedor apenas para a 1ª página
            page.accept(textFragmentAbsorber);

            TextFragment phoneNumberFragment = textFragmentAbsorber.getTextFragments().get_Item(1);

            // Criar Anotação de Link e definir a ação para chamar um número de telefone
            LinkAnnotation linkAnnotation = new LinkAnnotation(page, phoneNumberFragment.getRectangle());
            linkAnnotation.setAction(new GoToURIAction("callto:678-555-0103"));

            // Adicionar anotação à página
            page.getAnnotations().add(linkAnnotation);
            document.save(_dataDir + "SimpleResume_mod.pdf");
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }
    }
```


## Obter Anotação de Link

Por favor, tente usar o seguinte trecho de código para Obter Anotação de Link do documento PDF.

```java
    public static void GetLinkAnnotations() {

        // Carregar o arquivo PDF
        Document document = new Document(_dataDir + "SimpleResume_mod.pdf");

        // Filtrar anotações usando AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new LinkAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> linkAnnotations = annotationSelector.getSelected();

        // imprimir resultados
        for (Annotation la : linkAnnotations) {

            LinkAnnotation l = (LinkAnnotation) la;

            // Imprimir a URL de cada Anotação de Link
            System.out.println("URI: " + ((GoToURIAction) l.getAction()).getURI());

            TextAbsorber absorber = new TextAbsorber();
            absorber.getTextSearchOptions().setLimitToPageBounds(true);
            absorber.getTextSearchOptions().setRectangle(l.getRect());
            page.accept(absorber);

            String extractedText = absorber.getText();

            // Imprimir o texto associado ao hyperlink
            System.out.println(extractedText);
        }
    }
```


## Excluir Anotação de Link

O snippet de código a seguir mostra como excluir uma anotação de link de um arquivo PDF. Para isso, precisamos encontrar e remover todas as anotações de link na primeira página. Após isso, salvaremos o documento com a anotação removida.

```java
    public static void DeleteLinkAnnotations() {
        // Carregar o arquivo PDF
        Document document = new Document(_dataDir + "SimpleResume_mod.pdf");

        // Filtrar anotações usando AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new LinkAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> linkAnnotations = annotationSelector.getSelected();

        for (Annotation la : linkAnnotations)
            page.getAnnotations().delete(la);

        // Salvar documento com a anotação removida
        document.save(_dataDir + "SimpleResume_del.pdf");
    }
```

## Redigir determinada região da página com Anotação de Redação usando Aspose.PDF para Java

Aspose.PDF para Java suporta a funcionalidade de adicionar e manipular Anotações em um arquivo PDF existente. Recentemente, alguns de nossos clientes solicitaram a necessidade de redigir (remover texto, imagem, etc. de elementos) uma certa região de página de um documento PDF. Para atender a esse requisito, foi fornecida uma classe chamada RedactionAnnotation, que pode ser usada para redigir certas regiões de página ou pode ser usada para manipular RedactionAnnotations existentes e redigi-las (ou seja, achatar a anotação e remover o texto sob ela).

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import com.aspose.pdf.facades.PdfAnnotationEditor;

public class ExampleRedactAnnotation {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void RedactionAnnotation() {

        // Abrir documento
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        // Criar instância de RedactionAnnotation para região específica da página
        RedactionAnnotation annot = new RedactionAnnotation(page, new Rectangle(200, 500, 300, 600));
        annot.setFillColor(Color.getGreen());
        annot.setBorderColor(Color.getYellow());
        annot.setColor(Color.getBlue());

        // Texto a ser impresso na anotação de redação
        annot.setOverlayText("REDACTED");
        annot.setTextAlignment(HorizontalAlignment.Center);

        // Repetir texto de sobreposição sobre a anotação de redação
        annot.setRepeat(true);

        // Adicionar anotação à coleção de anotações da primeira página
        page.getAnnotations().add(annot);

        // Achatar anotação e redigir o conteúdo da página (ou seja, remover texto e imagem
        // Sob a anotação redigida)
        annot.redact();
        document.save(_dataDir + "RedactPage_out.pdf");
    }
```


## Abordagem de Facades

O namespace Aspose.PDF.Facades também possui uma classe chamada [PdfAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) que fornece o recurso para manipular Anotações existentes dentro do arquivo PDF. Esta classe contém um método chamado [RedactArea(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Redaction#getredactArea-com.aspose.pdf.Page-com.aspose.pdf.Rectangle-java.awt.Color-) que fornece a capacidade de remover certas regiões da página.

```java
    public static void RedactionAnnotationFacades(){
        PdfAnnotationEditor editor = new PdfAnnotationEditor();

        editor.bindPdf(_dataDir + "sample.pdf");

        // Redigir certa região da página
        editor.redactArea(1, new Rectangle(100, 100, 20, 70), java.awt.Color.white);
        editor.bindPdf(_dataDir + "sample.pdf");
        editor.save(_dataDir + "FacadesApproach_out.pdf");
    }
```