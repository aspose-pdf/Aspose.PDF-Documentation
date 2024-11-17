---
title: Anotações de Figuras em PDF
linktitle: Anotações de Figuras
type: docs
weight: 30
url: /pt/java/figures-annotation/
description: Este artigo descreve como adicionar, obter e excluir anotações de figuras em seu documento PDF com Aspose.PDF para Java
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Adicionar Anotações de Quadrado ou Círculo

As anotações de Quadrado e Círculo devem exibir, respectivamente, um retângulo ou uma elipse na página. Quando abertas, devem exibir uma janela pop-up contendo o texto da nota associada. As anotações de Quadrado são como as anotações de Círculo (instâncias da classe Aspose.Pdf.Annotations.CircleAnnotation) exceto pela forma.

Passos para criar Anotações de Quadrado e Círculo:

1. Carregue o arquivo PDF - novo [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

1. Crie uma nova [Circle Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/circleannotation) e defina os parâmetros do Círculo (novo Retângulo, título, cor, CorInterior, Opacidade).
1. Crie uma nova [PopupAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PopupAnnotation).
1. Em seguida, precisamos criar [Square Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/SquareAnnotation).
1. Defina os mesmos parâmetros do Quadrado (novo Retângulo, título, cor, CorInterior, Opacidade).
1. Depois, precisamos adicionar Anotações de Quadrado e Círculo à página.

O trecho de código a seguir mostra como adicionar Anotações de Círculo em uma página PDF.

```java
package com.aspose.pdf.examples;

import java.util.*;
import com.aspose.pdf.*;

public class ExampleCircleAnnotation {

    // O caminho para o diretório de documentos.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddCircleAnnotation() {
        try {
            // Carregar o arquivo PDF
            Document document = new com.aspose.pdf.Document(_dataDir + "appartments.pdf");
            Page page = document.getPages().get_Item(1);

            // Criar Anotação de Polígono
            CircleAnnotation circleAnnotation = new CircleAnnotation(page, new Rectangle(270, 160, 483, 383));
            circleAnnotation.setTitle("John Smith");
            circleAnnotation.setColor(Color.getRed());
            circleAnnotation.setInteriorColor(Color.getMistyRose());
            circleAnnotation.setOpacity(0.5);
            circleAnnotation.setPopup(new PopupAnnotation(page, new Rectangle(842, 316, 1021, 459)));

            // Criar Anotação de Quadrado
            SquareAnnotation squareAnnotation = new SquareAnnotation(page, new Rectangle(67, 317, 261, 459));
            squareAnnotation.setTitle("John Smith");
            squareAnnotation.setColor(Color.getBlue());
            squareAnnotation.setInteriorColor(Color.getBlueViolet());
            squareAnnotation.setOpacity(0.25);
            squareAnnotation.setPopup(new PopupAnnotation(page, new Rectangle(842, 196, 1021, 338)));

            // Adicionar anotação à página
            page.getAnnotations().add(circleAnnotation);
            page.getAnnotations().add(squareAnnotation);
            document.save(_dataDir + "appartments_mod.pdf");
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }
    }
```


Como exemplo, veremos o seguinte resultado ao adicionar anotações de Quadrado e Círculo a um documento PDF:

![Demonstração de Anotação de Círculo e Quadrado](circle_demo.png)

## Obter Anotação de Círculo

Por favor, tente usar o seguinte trecho de código para Obter Anotação de Círculo do documento PDF.

```java
public static void GetCircleAnnotation() {
        // Carregar o arquivo PDF
        Document document = new Document(_dataDir + "appartments_mod.pdf");

        // Filtrar anotações usando AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new CircleAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> caretAnnotations = annotationSelector.getSelected();

        // imprimir resultados
        for (Annotation ca : caretAnnotations) {
            System.out.println(ca.getRect());
        }
    }
```

## Excluir Anotação de Círculo

O seguinte trecho de código mostra como Excluir Anotação de Círculo de um arquivo PDF.

```java
public static void DeleteCircleAnnotation() {
        // Carregar o arquivo PDF
        Document document = new Document(_dataDir + "appartments_mod.pdf");

        // Filtrar anotações usando AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new CircleAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> circleAnnotations = annotationSelector.getSelected();

        for (Annotation ca : circleAnnotations) {
            page.getAnnotations().delete(ca);
        }
        document.save(_dataDir + "appartments_del.pdf");
    }
```

## Adicionar Anotações de Polígono e Polilinha

A ferramenta Polilinha permite criar formas e contornos com um número arbitrário de lados no documento.

**Anotações de Polígono** representam polígonos em uma página. Eles podem ter qualquer número de vértices conectados por linhas retas.

**Anotações de Polilinha** são também semelhantes aos polígonos, a única diferença é que o primeiro e o último vértice não estão implicitamente conectados.

Passos com os quais criamos anotações de Polígono e Polilinha:

1. Carregar o arquivo PDF - novo [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Criar nova [Polygon Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/PolygonAnnotation) e definir parâmetros do Polígono (novo Rectangle, novos Points, título, cor, InteriorColor e Opacity).
1. Criar uma nova [PopupAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/PopupAnnotation).
1. Em seguida, criar uma [PolyLine Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/PolylineAnnotation) e repetir todas as ações.
1. Depois podemos adicionar anotações à página.

O trecho de código a seguir mostra como adicionar Anotações de Polígono e Polilinha ao arquivo PDF:

```java
 package com.aspose.pdf.examples;

import java.util.*;
import com.aspose.pdf.*;

public class ExamplePolygonAnnotation {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddPolynnotation() {
        try {
            // Carregar o arquivo PDF
            Document document = new Document(_dataDir + "appartments.pdf");
            Page page = document.getPages().get_Item(1);

            // Criar Anotação de Polígono
            PolygonAnnotation polygonAnnotation = new PolygonAnnotation(page, new Rectangle(270, 193, 571, 383),
                    new Point[] { new Point(274, 381), new Point(555, 381), new Point(555, 304), new Point(570, 304),
                            new Point(570, 195), new Point(274, 195) });

            polygonAnnotation.setTitle("John Smith");
            polygonAnnotation.setColor(Color.getBlue());
            polygonAnnotation.setInteriorColor(Color.getBlueViolet());
            polygonAnnotation.setOpacity(0.25);
            polygonAnnotation.setPopup(new PopupAnnotation(page, new Rectangle(842, 196, 1021, 338)));

            // Criar Anotação de Polilinha
            PolylineAnnotation polylineAnnotation = new PolylineAnnotation(page, new Rectangle(270, 193, 571, 383),
                    new Point[] { new Point(545, 150), new Point(545, 190), new Point(667, 190), new Point(667, 110),
                            new Point(626, 111) });

            polygonAnnotation.setTitle("John Smith");
            polygonAnnotation.setColor(Color.getRed());
            polygonAnnotation.setPopup(new PopupAnnotation(page, new Rectangle(842, 196, 1021, 338)));

            // Adicionar anotação à página
            page.getAnnotations().add(polygonAnnotation);
            page.getAnnotations().add(polylineAnnotation);
            document.save(_dataDir + "appartments_mod.pdf");
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }
    }
```


## Obter Anotações de Polígono e Polilinha

Por favor, tente usar o seguinte trecho de código para Obter Anotações de Polígono e Polilinha em um documento PDF.

```java
    public static void GetPolyAnnotation() {
        // Carregar o arquivo PDF
        Document document = new Document(_dataDir + "Appartments_mod.pdf");
        Page page = document.getPages().get_Item(1);

        AnnotationSelector annotationSelector = new AnnotationSelector(
                new PolylineAnnotation(page, Rectangle.getTrivial(), null));
        page.accept(annotationSelector);
        List<Annotation> polyAnnotations = annotationSelector.getSelected();

        for (Annotation pa : polyAnnotations) {
            System.out.printf("[%s]", pa.getRect());
        }
    }
```

## Excluir Anotações de Polígono e Polilinha

O seguinte trecho de código mostra como Excluir Anotações de Polígono e Polilinha de um arquivo PDF.

```java
        public static void DeletePolyAnnotation() {
        // Carregar o arquivo PDF
        Document document = new Document(_dataDir + "Appartments_mod.pdf");
        Page page = document.getPages().get_Item(1);

        AnnotationSelector annotationSelector = new AnnotationSelector(
                new PolylineAnnotation(page, Rectangle.getTrivial(), null));
        page.accept(annotationSelector);
        List<Annotation> polyAnnotations = annotationSelector.getSelected();

        for (Annotation pa : polyAnnotations) {
            page.getAnnotations().delete(pa);
        }

        document.save(_dataDir + "Appartments_del.pdf");
    }
```


## Como adicionar Anotação de Linha em um arquivo PDF existente

O propósito de uma Anotação de Linha é exibir uma única linha reta na página. Quando aberta, deverá exibir uma janela pop-up contendo o texto da nota associada. 
Esta funcionalidade possui entradas adicionais específicas para uma anotação de linha. Estas entradas são criptografadas na forma de letras, por exemplo, LL, BS, IC, e assim por diante.

Além disso, a Anotação de Linha pode incluir uma legenda para uma anotação de linha, que é especificada ao definir Cap para `true`.

A próxima funcionalidade permite o efeito de aplicar uma legenda a uma Anotação de Linha que possui um deslocamento de líder. 
Além disso, este tipo de anotação permite que você defina estilos de término de Linha.

Passos com os quais criamos uma Anotação de Linha:

1. Carregar o arquivo PDF - novo [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
2. Criar nova [Line Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/lineannotation) e definir parâmetros de Linha (novo Rectangle, novo Point, título, cor, largura, StartingStyle e EndingStyle).

1. Crie um novo [PopupAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PopupAnnotation).
1. Depois podemos adicionar anotação à página

O trecho de código a seguir mostra como adicionar uma Anotação de Linha a um arquivo PDF:

```java
package com.aspose.pdf.examples;

import java.util.*;
import com.aspose.pdf.*;

public class ExampleLineAnnotation {

    // O caminho para o diretório de documentos.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddLineAnnotation() {
        try {
            // Carregar o arquivo PDF
            Document document = new Document(_dataDir + "appartments.pdf");
            Page page = document.getPages().get_Item(1);

            // Criar Anotação de Linha
            LineAnnotation lineAnnotation = new LineAnnotation(page, new Rectangle(550, 93, 562, 439),
                    new Point(556, 99), new Point(556, 443));

            lineAnnotation.setTitle("John Smith");
            lineAnnotation.setColor(Color.getRed());
            lineAnnotation.setWidth(3);
            lineAnnotation.setStartingStyle(LineEnding.OpenArrow);
            lineAnnotation.setEndingStyle(LineEnding.OpenArrow);
            lineAnnotation.setPopup(new PopupAnnotation(page, new Rectangle(842, 124, 1021, 266)));

            // Adicionar anotação à página
            page.getAnnotations().add(lineAnnotation);
            document.save(_dataDir + "appartments_mod.pdf");
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }
    }
```


## Obter Anotação de Linha

Por favor, tente usar o trecho de código a seguir para Obter Anotação de Linha em um documento PDF.

```java
    public static void GetLineAnnotation() {
        // Carregar o arquivo PDF
        Document document = new Document(_dataDir + "appartments_mod.pdf");

        // Filtrar anotações usando AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new LineAnnotation(page, Rectangle.getTrivial(), Point.getTrivial(), Point.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> lineAnnotations = annotationSelector.getSelected();

        // imprimir resultados
        for (Annotation la : lineAnnotations) {
            LineAnnotation l = (LineAnnotation) la;
            System.out.println("[" + l.getStarting().getX() + "," + l.getStarting().getY() + "]" + "["
                    + l.getEnding().getX() + "," + l.getEnding().getY() + "]");
        }
    }
```

## Excluir Anotação de Linha

O trecho de código a seguir mostra como excluir uma anotação de linha de um arquivo PDF.

```java
   public static void DeleteLineAnnotation() {
        // Carregar o arquivo PDF
        Document document = new Document(_dataDir + "appartments_mod.pdf");

        // Filtrar anotações usando AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new LineAnnotation(page, Rectangle.getTrivial(), Point.getTrivial(), Point.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> lineAnnotations = annotationSelector.getSelected();

        // imprimir resultados
        for (Annotation la : lineAnnotations) {
            page.getAnnotations().delete(la);
        }
        document.save(_dataDir + "appartments_del.pdf");
    }
}
```

## Como adicionar Anotação de Tinta a um arquivo PDF

Uma Anotação de Tinta representa um "rabisco" feito à mão livre composto por um ou mais caminhos disjuntos.
 Quando aberto, deverá exibir uma janela pop-up contendo o texto da nota associada.

O [InkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/InkAnnotation) representa um rabisco à mão livre composto por um ou mais pontos desconexos. Tente usar o seguinte trecho de código para adicionar InkAnnotation em um documento PDF.

```java
package com.aspose.pdf.examples;

import java.util.*;
import com.aspose.pdf.*;

public class ExampleInkAnnotation {

    // O caminho para o diretório de documentos.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";


    public static void AddInkAnnotation() {
        try {
            // Carregar o arquivo PDF
            Document document = new com.aspose.pdf.Document(_dataDir + "Appartments.pdf");
            Page page = document.getPages().get_Item(1);
            Rectangle arect = new Rectangle(320.086,189.286,384.75,228.927);
            List<Point[]> inkList = new ArrayList<Point[]>();
            //dados em ppts, recebidos de um mouse ou outro dispositivo apontador
            double ppts[] = { 328.002, 222.017, 328.648, 222.017, 329.294, 222.017, 329.617, 222.34, 330.91, 222.663,
                    331.556, 222.663, 332.203, 222.986, 333.495, 223.633, 334.141, 223.956, 334.788, 224.279, 335.434,
                    224.602, 336.08, 224.602, 336.727, 224.925, 337.373, 225.248, 337.696, 225.248, 338.342, 225.572,
                    338.989, 225.895, 341.897, 225.895, 343.513, 226.218, 346.098, 226.218, 348.683, 226.541, 350.622,
                    226.541, 352.238, 226.541, 353.208, 226.541, 353.854, 226.541, 355.146, 226.541, 356.439, 226.541,
                    357.732, 226.541, 358.378, 226.541, 359.024, 226.541, 360.64, 226.541, 361.286, 226.541, 361.933,
                    226.541, 362.256, 226.541, 362.902, 226.541, 363.548, 226.541, 363.872, 226.541, 363.872, 226.218,
                    365.164, 226.218, 365.487, 226.218, 365.811, 226.218, 367.103, 226.218, 367.749, 226.218, 368.719,
                    226.218, 370.012, 226.218, 370.981, 226.218, 371.627, 226.218, 372.597, 225.895, 372.92, 225.895,
                    373.243, 225.895, 373.243, 225.572, 373.566, 225.572, 374.213, 225.248, 374.536, 225.248, 375.182,
                    224.602, 375.182, 224.279, 375.828, 223.956, 376.475, 223.31, 377.121, 222.986, 377.767, 222.986,
                    378.414, 222.017, 379.383, 221.371, 379.706, 220.724, 380.029, 219.432, 380.676, 219.109, 380.676,
                    218.462, 381.645, 217.493, 381.968, 217.17, 381.968, 216.523, 382.291, 215.554, 382.615, 215.231,
                    382.615, 214.261, 382.938, 213.292, 382.938, 212.645, 382.938, 211.999, 382.938, 211.353, 382.938,
                    210.707, 382.938, 209.737, 382.938, 208.768, 382.938, 208.444, 382.615, 207.475, 382.615, 206.829,
                    382.291, 206.505, 382.291, 205.859, 381.968, 204.89, 381.968, 204.243, 381.645, 203.92, 380.999,
                    203.274, 380.999, 202.951, 380.676, 202.305, 380.353, 201.658, 380.029, 201.335, 380.029, 200.689,
                    380.029, 200.366, 379.383, 199.719, 379.06, 199.719, 378.737, 199.073, 377.767, 198.103, 377.121,
                    197.780, 376.475, 197.457, 375.505, 196.488, 374.859, 196.165, 374.536, 195.841, 372.92, 195.195,
                    371.951, 194.549, 370.658, 194.226, 368.719, 193.902, 367.426, 193.256, 366.457, 193.256, 363.872,
                    192.933, 362.902, 192.933, 361.61, 192.61, 359.024, 192.61, 357.409, 192.61, 356.439, 192.61,
                    353.531, 192.61, 352.561, 192.61, 350.945, 192.61, 349.007, 192.933, 348.36, 193.256, 347.391,
                    193.256, 346.098, 193.902, 345.452, 193.902, 344.806, 193.902, 343.513, 193.902, 342.867, 193.902,
                    342.220, 193.902, 341.574, 193.902, 341.251, 194.226, 340.928, 194.226, 340.928, 194.549, 340.605,
                    194.549, 340.605, 194.872, 339.635, 195.195, 339.635, 195.518, 338.989, 195.518, 338.989, 195.841,
                    338.666, 196.165, 338.019, 196.811, 338.019, 197.134, 337.373, 197.457, 336.404, 198.427, 335.757,
                    198.427, 335.434, 198.75, 334.141, 199.719, 333.818, 199.719, 333.818, 200.042, 332.849, 200.366,
                    332.203, 200.366, 331.556, 201.335, 330.91, 201.981, 330.587, 202.305, 330.264, 202.305, 329.294,
                    202.628, 328.971, 202.951, 328.002, 203.274, 328.002, 203.597, 327.355, 204.243, 326.709, 204.567,
                    326.386, 204.89, 326.063, 205.536, 325.416, 205.859, 325.093, 205.859, 324.447, 205.859, 324.124,
                    206.182, 324.124, 206.505, 323.477, 206.829, 323.477, 207.152, 323.477, 207.798, 322.831, 207.798,
                    322.831, 208.121, 322.831, 208.444, 322.508, 208.444, 322.508, 209.091, 322.185, 209.414, 322.185,
                    209.737, 322.185, 210.383, 322.185, 211.03, 322.185, 211.353, 322.185, 211.676, 322.185, 212.322,
                    323.154, 213.292, 323.154, 213.938, 324.447, 214.584, 325.093, 215.877, 325.416, 216.2, 325.416,
                    216.846, 325.739, 217.17, 326.063, 217.493, 326.386, 218.139, 326.709, 218.139, 326.709, 218.462,
                    327.032, 219.109, 327.032, 219.432, 327.032, 219.755, 327.355, 220.078, 327.355, 220.401, 327.678,
                    221.371, 328.002, 221.371, 328.002, 222.017, 328.325, 222.663, 328.648, 222.663, 328.971, 222.986,
                    329.294, 223.31, 329.617, 223.956, 329.617, 224.279 };

            //converter dados para pontos
            Point[] arrpt = new Point[ppts.length/2];
            for (int i = 0, j=0; i < arrpt.length; i++, j+=2) {
                arrpt[i] = new Point(ppts[j],ppts[j+1]);
            }
            inkList.add(arrpt);

            InkAnnotation ia = new InkAnnotation(page, arect, inkList);
            ia.setTitle("Usuário Aspose");
            ia.setColor(Color.getRed());
            ia.setCapStyle(CapStyle.Rounded);

            Border border = new Border(ia);
            border.setWidth(3);
            ia.setOpacity(0.75);

            page.getAnnotations().add(ia);
            document.save(_dataDir + "appartments_mod.pdf");
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }
    }
```

## Obter InkAnnotation do seu PDF

Você pode obter [InkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/InkAnnotation) com o seguinte trecho de código:

```java
public static void GetInkAnnotation() {
        // Carregar o arquivo PDF
        Document document = new Document(_dataDir + "appartments_mod.pdf");

        // Filtrar anotações usando AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new InkAnnotation(page, Rectangle.getTrivial(), null));
        page.accept(annotationSelector);
        List<Annotation> inkAnnotations = annotationSelector.getSelected();

        // imprimir resultados
        for (Annotation ia : inkAnnotations) {
            System.out.println(ia.getRect());
        }
    }
```

## Excluir InkAnnotation

Aspose.PDF para Java permite que você exclua [InkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/InkAnnotation) do seu arquivo PDF.

```java
public static void DeleteInkAnnotation() {
        // Carregar o arquivo PDF
        Document document = new Document(_dataDir + "appartments_mod.pdf");

        // Filtrar anotações usando AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new InkAnnotation(page, Rectangle.getTrivial(), null));
        page.accept(annotationSelector);
        List<Annotation> InkAnnotations = annotationSelector.getSelected();

        for (Annotation ca : InkAnnotations) {
            page.getAnnotations().delete(ca);
        }
        document.save(_dataDir + "appartments_del.pdf");
    }
```