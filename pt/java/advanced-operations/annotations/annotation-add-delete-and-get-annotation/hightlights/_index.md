---
title: PDF Highlights Annotation 
linktitle: Highlights Annotation
type: docs
weight: 20
url: pt/java/highlights-annotation/
description: As anotações de marcação são apresentadas no texto como destaques, sublinhados, tachados ou sublinhados irregulares no texto de um documento.
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

As Anotações de Marcação de Texto devem aparecer como destaques, sublinhados, tachados ou sublinhados irregulares (“ziguezague”) no texto de um documento. Quando abertas, devem exibir uma janela pop-up contendo o texto da nota associada.

As propriedades das anotações de marcação de texto no documento PDF podem ser editadas usando a janela de propriedades fornecida no controle do visualizador de PDF. A cor, opacidade, autor e assunto da anotação de marcação de texto podem ser modificados.

É possível obter ou definir as configurações das anotações de destaque usando a propriedade highlightSettings.
 A propriedade highlightSettings é usada para definir as propriedades de cor, opacidade, autor, assunto, dataModificada e isLocked das anotações de destaque.

Também é possível obter ou definir as configurações das anotações de tachado usando a propriedade strikethroughSettings. A propriedade strikethroughSettings é usada para definir as propriedades de cor, opacidade, autor, assunto, dataModificada e isLocked das anotações de tachado.

O próximo recurso é a capacidade de obter ou definir as configurações das anotações de sublinhado usando a propriedade underlineSettings. A propriedade underlineSettings é usada para definir as propriedades de cor, opacidade, autor, assunto, dataModificada e isLocked das anotações de sublinhado.

## Adicionar Anotação de Marcação de Texto

Para adicionar uma Anotação de Marcação de Texto ao documento PDF, precisamos realizar as seguintes ações:

1. Carregar o arquivo PDF - novo objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Criar anotações:

    - [HighlightAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/HighlightAnnotation) e definir parâmetros (título, cor).- [StrikeOutAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/StrikeOutAnnotation) e definir parâmetros (título, cor).
- [SquigglyAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/SquigglyAnnotation) e definir parâmetros (título, cor).
- [UnderlineAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/UnderlineAnnotation) e definir parâmetros (título, cor).

1. Depois devemos adicionar todas as anotações à página.

```java
package com.aspose.pdf.examples;

import java.util.*;
import com.aspose.pdf.*;

public class ExampleTextMarkupAnnotation {
    // O caminho para o diretório dos documentos.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddTextMarkupAnnotation() {
        try {
            // Carregar o arquivo PDF
            Document document = new Document(_dataDir + "sample.pdf");
            Page page = document.getPages().get_Item(1);
            TextFragmentAbsorber tfa = new TextFragmentAbsorber("PDF");
            tfa.visit(page);

            // Criar anotações
            HighlightAnnotation highlightAnnotation = new HighlightAnnotation(page,
                    tfa.getTextFragments().get_Item(1).getRectangle());
            highlightAnnotation.setTitle("Usuário Aspose");
            highlightAnnotation.setColor(Color.getLightGreen());

            StrikeOutAnnotation strikeOutAnnotation = new StrikeOutAnnotation(page,
                    tfa.getTextFragments().get_Item(2).getRectangle());
            strikeOutAnnotation.setTitle("Usuário Aspose");
            strikeOutAnnotation.setColor(Color.getBlue());

            SquigglyAnnotation squigglyAnnotation = new SquigglyAnnotation(page,
                    tfa.getTextFragments().get_Item(3).getRectangle());
            squigglyAnnotation.setTitle("Usuário Aspose");
            squigglyAnnotation.setColor(Color.getRed());

            UnderlineAnnotation underlineAnnotation = new UnderlineAnnotation(page,
                    tfa.getTextFragments().get_Item(4).getRectangle());
            underlineAnnotation.setTitle("Usuário Aspose");
            underlineAnnotation.setColor(Color.getViolet());

            // Adicionar anotações à página
            page.getAnnotations().add(highlightAnnotation);
            page.getAnnotations().add(squigglyAnnotation);
            page.getAnnotations().add(strikeOutAnnotation);
            page.getAnnotations().add(underlineAnnotation);
            document.save(_dataDir + "sample_mod.pdf");
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }
    }
}
```


Se você quiser destacar um fragmento de várias linhas, você deve usar o exemplo avançado:

```java
    /// <summary>
    /// Exemplo avançado para você que quer destacar um fragmento de várias linhas
    /// </summary>
    public static void AddHighlightAnnotationAdvanced() {
        Document document = new Document(_dataDir + "sample_mod.pdf");
        Page page = document.getPages().get_Item(1);
        TextFragmentAbsorber tfa = new TextFragmentAbsorber("Adobe\\W+Acrobat\\W+Reader", new TextSearchOptions(true));
        tfa.visit(page);
        for (TextFragment textFragment : tfa.getTextFragments()) {
            HighlightAnnotation highlightAnnotation = HighLightTextFragment(page, textFragment, Color.getYellow());
            page.getAnnotations().add(highlightAnnotation);
        }
        document.save(_dataDir + "sample_mod.pdf");
    }

    private static HighlightAnnotation HighLightTextFragment(Page page, TextFragment textFragment, Color color) {
        HighlightAnnotation ha;
        if (textFragment.getSegments().size() == 1) {
            ha = new HighlightAnnotation(page, textFragment.getSegments().get_Item(1).getRectangle());
            ha.setTitle("Aspose User");
            ha.setColor(color);
            ha.setModified(new Date());
            Rectangle rect = textFragment.getSegments().get_Item(1).getRectangle();
            ha.setQuadPoints(
                    new Point[] { new Point(rect.getLLX(), rect.getURY()), new Point(rect.getURX(), rect.getURY()),
                            new Point(rect.getLLX(), rect.getLLY()), new Point(rect.getURX(), rect.getLLY()) });
            return ha;
        }

        int offset = 0;
        Point[] quadPoints = new Point[textFragment.getSegments().size() * 4];
        for (TextSegment segment : textFragment.getSegments()) {
            Rectangle r = segment.getRectangle();
            quadPoints[offset + 0] = new Point(r.getLLX(), r.getURY());
            quadPoints[offset + 1] = new Point(r.getURX(), r.getURY());
            quadPoints[offset + 2] = new Point(r.getLLX(), r.getLLY());
            quadPoints[offset + 3] = new Point(r.getURX(), r.getLLY());
            offset += 4;
        }

        double llx = quadPoints[0].getX();
        double lly = quadPoints[0].getY();
        double urx = quadPoints[0].getX();
        double ury = quadPoints[0].getY();
        for (Point pt : quadPoints) {
            if (llx > pt.getX())
                llx = pt.getX();
            if (lly > pt.getY())
                lly = pt.getY();
            if (urx < pt.getX())
                urx = pt.getX();
            if (ury < pt.getY())
                ury = pt.getY();
        }
        ha = new HighlightAnnotation(page, new Rectangle(llx, lly, urx, ury));
        ha.setTitle("Aspose User");
        ha.setColor(color);
        ha.setModified(new Date());
        ha.setQuadPoints(quadPoints);
        return ha;
    }

    /// <summary>
    /// Como obter um Texto Destacado
    /// </summary>
    public static void GetHighlightedText() {
        // Carregar o arquivo PDF
        Document document = new Document(_dataDir + "sample_mod.pdf");
        Page page = document.getPages().get_Item(1);

        AnnotationSelector annotationSelector1 = new AnnotationSelector(
                new HighlightAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector1);
        List<Annotation> highlightAnnotations = annotationSelector1.getSelected();
        for (Annotation ta : highlightAnnotations) {
            System.out.println("[" + ((HighlightAnnotation) ta).getMarkedText() + "]");
        }
    }
```


## Obter Anotação de Marcação de Texto

Por favor, tente usar o seguinte trecho de código para obter a Anotação de Marcação de Texto do documento PDF.

```java
     public static void GetTextMarkupAnnotation() {
        // Carregar o arquivo PDF
        Document document = new Document(_dataDir + "sample_mod.pdf");
        Page page = document.getPages().get_Item(1);

        AnnotationSelector annotationSelector1 = new AnnotationSelector(
                new HighlightAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector1);
        AnnotationSelector annotationSelector2 = new AnnotationSelector(
                new SquigglyAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector2);

        List<Annotation> textMarkupAnnotations = annotationSelector1.getSelected();
        textMarkupAnnotations.addAll(annotationSelector2.getSelected());

        // imprimir resultados
        for (Annotation ta : textMarkupAnnotations) {
            System.out.printf("[" + ta.getAnnotationType() + ta.getRect() + "]");
        }
    }
```


## Excluir Anotação de Marcação de Texto

O trecho de código a seguir mostra como excluir uma anotação de marcação de texto de um arquivo PDF.

```java
   public static void DeleteTextMarkupAnnotation() {
        // Carregar o arquivo PDF
        Document document = new Document(_dataDir + "sample_mod.pdf");
        Page page = document.getPages().get_Item(1);

        AnnotationSelector annotationSelector1 = new AnnotationSelector(
                new HighlightAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector1);
        AnnotationSelector annotationSelector2 = new AnnotationSelector(
                new SquigglyAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector2);

        List<Annotation> textMarkupAnnotations = annotationSelector1.getSelected();
        textMarkupAnnotations.addAll(annotationSelector2.getSelected());

        // imprimir resultados
        for (Annotation ta : textMarkupAnnotations) {
            page.getAnnotations().delete(ta);
        }
        document.save(_dataDir + "sample_del.pdf");
    }
```