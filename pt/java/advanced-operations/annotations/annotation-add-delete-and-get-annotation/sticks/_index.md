---
title: Anotações Adesivas em PDF
linktitle: Anotação Adesiva
type: docs
weight: 50
url: /pt/java/sticky-annotations/
description: Este tópico sobre anotações adesivas, como exemplo mostramos a Anotação de Marca d'Água no texto. Ela é usada para representar gráficos na página. Verifique o trecho de código para resolver essa tarefa.
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Adicionar Anotação de Marca d'Água

Uma anotação de marca d'água deve ser usada para representar gráficos que devem ser impressos em um tamanho e posição fixos em uma página, independentemente das dimensões da página impressa.

Você pode adicionar Texto de Marca d'Água usando [WatermarkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/WatermarkAnnotation) em uma posição específica da página PDF. A opacidade da Marca d'Água também pode ser controlada usando a propriedade de opacidade.

Verifique o seguinte trecho de código para adicionar WatermarkAnnotation.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import java.util.*;

public class ExampleWatermarkAnnotation {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddWaterMarkAnnotation()
    {
        // Carregar o arquivo PDF
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        // Criar Anotação
        WatermarkAnnotation wa = new WatermarkAnnotation(page, new Rectangle(100, 500, 400, 600));

        // Adicionar anotação na coleção de Anotações da Página
        page.getAnnotations().add(wa);

        // Criar TextState para configurações de Fonte
        TextState ts = new TextState();

        ts.setForegroundColor(Color.getBlue());
        ts.setFont(FontRepository.findFont("Times New Roman"));
        ts.setFontSize(32);

        // Definir nível de opacidade do Texto da Anotação
        wa.setOpacity(0.5);

        // Adicionar Texto à Anotação
        wa.setTextAndState(new String[] { "Aspose.PDF", "Marca d'Água", "Demo" }, ts);

        // Salvar o Documento
        document.save(_dataDir + "sample_watermark.pdf");
    }
}
```


## Obter Anotação de Marca d'Água

```java
    public static void GetWatermarkAnnotation() {
        // Carregar o arquivo PDF
        Document document = new Document(_dataDir + "sample_watermark.pdf");

        // Filtrar anotações usando AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new WatermarkAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> WatermarkAnnotations = annotationSelector.getSelected();

        // imprimir resultados
        for (Annotation fa : WatermarkAnnotations) {
            System.out.println(fa.getRect());
        }
    }
```

## Excluir Anotação de Marca d'Água

```java
    public static void DeleteWatermarkAnnotation() {
         // Carregar o arquivo PDF
         Document document = new Document(_dataDir + "sample_watermark.pdf");

         // Filtrar anotações usando AnnotationSelector
         Page page = document.getPages().get_Item(1);
         AnnotationSelector annotationSelector = new AnnotationSelector(
                 new WatermarkAnnotation(page, Rectangle.getTrivial()));
         page.accept(annotationSelector);
         List<Annotation> WatermarkAnnotations = annotationSelector.getSelected();

         // excluir anotações
         for (Annotation fa : WatermarkAnnotations) {
            page.getAnnotations().delete(fa);
        }
        document.save(_dataDir + "sample_watermark_del.pdf");
    }
```