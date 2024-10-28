---
title: Obter Resolução e Dimensões de Imagens Incorporadas
linktitle: Obter Resolução e Dimensões
type: docs
weight: 40
url: /java/get-resolution-and-dimensions-of-embedded-images/
description: Esta seção mostra detalhes sobre como obter resolução e dimensões de Imagens Incorporadas
lastmod: "2021-06-05"
---

Este tópico explica como usar as classes de operadores no namespace Aspose.PDF, que fornecem a capacidade de obter informações de resolução e dimensão sobre imagens sem precisar extraí-las.

Existem diferentes maneiras de conseguir isso. Este artigo explica como usar um `arraylist` e [classes de posicionamento de imagem](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacement).

1. Primeiro, carregue o arquivo PDF de origem (com imagens).
1. Em seguida, crie um objeto ArrayList para armazenar os nomes de quaisquer imagens no documento.
1. Obtenha as imagens usando a propriedade Page.Resources.Images.
1. Crie um objeto stack para armazenar o estado gráfico da imagem e use-o para acompanhar diferentes estados da imagem.

1. Crie um objeto ConcatenateMatrix que define a transformação atual. Ele também suporta escalonamento, rotação e distorção de qualquer conteúdo. Ele concatena a nova matriz com a anterior. Observe que não podemos definir a transformação do zero, mas apenas modificar a transformação existente.
1. Como podemos modificar a matriz com ConcatenateMatrix, também podemos precisar reverter para o estado original da imagem. Use os operadores GSave e GRestore. Esses operadores são emparelhados, então devem ser chamados juntos. Por exemplo, se você fizer algum trabalho gráfico com transformações complexas e finalmente retornar as transformações ao estado inicial, a abordagem será algo assim:

```java
// Desenhar algum texto
GSave

ConcatenateMatrix  // rotacionar conteúdos após o operador

// Algum trabalho gráfico

ConcatenateMatrix // escalar (com rotação anterior) conteúdos após o operador

// Outro trabalho gráfico

GRestore

// Desenhar algum texto
```

Como resultado, o texto é desenhado na forma regular, mas algumas transformações são realizadas entre os operadores de texto.
 Para exibir a imagem ou desenhar objetos de formulário e imagens, precisamos usar o operador Do.

Também temos uma classe chamada XImage que fornece duas propriedades, Largura e Altura, que podem ser usadas para obter as dimensões da imagem.

1. Realize alguns cálculos para computar a resolução da imagem.
2. Exiba as informações em um Prompt de Comando juntamente com o nome da imagem.

O snippet de código a seguir mostra como obter as dimensões e a resolução de uma imagem sem extrair a imagem do documento PDF.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import com.aspose.pdf.operators.*;
import java.util.*;

public class ExampleImagesResolution {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ExampleAddPageNumber() 
    {
        // Carregar o arquivo PDF de origem
        Document doc = new Document(_dataDir+ "ImageInformation.pdf");
        
        // Definir a resolução padrão para imagem
        int defaultResolution = 72;

        Stack<Object> graphicsState = new Stack<Object>();

        // Definir objeto de lista de array que conterá nomes de imagens
        List<String> imageNames = Arrays.asList(doc.getPages().get_Item(1).getResources().getImages().getNames());
        //ArrayList imageNames = new ArrayList<>(Arrays.asList(names));
        // Inserir um objeto na pilha
        graphicsState.push(new Matrix(1, 0, 0, 1, 0, 0));

        // Obter todos os operadores na primeira página do documento
        for (Operator op : doc.getPages().get_Item(1).getContents())
        {
            // Usar operadores GSave/GRestore para reverter as transformações de volta para as anteriormente definidas
            GSave opSaveState = (GSave) op;
            GRestore opRestoreState = (GRestore) op;
            // Instanciar objeto ConcatenateMatrix pois ele define a matriz de transformação atual.
            ConcatenateMatrix opCtm = (ConcatenateMatrix) op;
            // Criar operador Do que desenha objetos dos recursos. Ele desenha objetos de Formulário e objetos de Imagem
            Do opDo = (Do) op;

            if (opSaveState != null)
            {
                // Salvar o estado anterior e empilhar o estado atual no topo da pilha
                Matrix m = new Matrix((Matrix)graphicsState.peek());
                graphicsState.push(m);
            }
            else if (opRestoreState != null)
            {
                // Descartar o estado atual e restaurar o anterior
                graphicsState.pop();
            }
            else if (opCtm != null)
            {
                Matrix cm = new Matrix(
                (float)opCtm.getMatrix().getA(),
                (float)opCtm.getMatrix().getB(),
                (float)opCtm.getMatrix().getC(),
                (float)opCtm.getMatrix().getD(),
                (float)opCtm.getMatrix().getE(),
                (float)opCtm.getMatrix().getF());

                // Multiplicar a matriz atual com a matriz de estado
                ((Matrix)graphicsState.peek()).multiply(cm);

                continue;
            }
            else if (opDo != null)
            {
                // No caso de ser um operador de desenho de imagem
                if (imageNames.contains(opDo.getName()))
                {
                    Matrix lastCTM = (Matrix)graphicsState.peek();
                    // Criar objeto XImage para conter imagens da primeira página do pdf
                    XImage image = doc.getPages().get_Item(1).getResources().getImages().get_Item(opDo.getName());

                    // Obter dimensões da imagem
                    double scaledWidth = Math.sqrt(Math.pow(lastCTM.getElements()[0], 2) + Math.pow(lastCTM.getElements()[1], 2));
                    double scaledHeight = Math.sqrt(Math.pow(lastCTM.getElements()[2], 2) + Math.pow(lastCTM.getElements()[3], 2));
                    // Obter informações de Altura e Largura da imagem
                    double originalWidth = image.getWidth();
                    double originalHeight = image.getHeight();

                    // Calcular a resolução com base nas informações acima
                    double resHorizontal = originalWidth * defaultResolution / scaledWidth;
                    double resVertical = originalHeight * defaultResolution / scaledHeight;

                    // Exibir informações de Dimensão e Resolução de cada imagem
                    System.out.printf(_dataDir + "imagem %s (%.2f:%.2f): res %.2f x %.2f",
                                        opDo.getName(), scaledWidth, scaledHeight, resHorizontal,
                                        resVertical);
                }
                // Salvar documento de saída
                doc.save(_dataDir);
            }
        }
    }
}
```