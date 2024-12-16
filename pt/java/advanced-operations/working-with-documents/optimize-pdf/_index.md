---
title: Optimize, Compress or Reduce PDF Size in Java
linktitle: Optimize PDF Document
type: docs
weight: 40
url: /pt/java/optimize-pdf/
description: Otimize arquivo PDF, diminuir todas as imagens, reduzir tamanho do PDF, Desincorporar fontes, Remover objetos não utilizados com Java.
lastmod: "2021-06-05"
---

Um documento PDF pode, às vezes, conter dados adicionais. Reduzir o tamanho de um arquivo PDF ajudará a otimizar a transferência de rede e o armazenamento. Isso é especialmente útil para publicação em páginas da web, compartilhamento em redes sociais, envio por e-mail ou arquivamento em armazenamento. Podemos usar várias técnicas para otimizar PDF:

- Otimizar conteúdo da página para navegação online
- Diminuir ou comprimir todas as imagens
- Permitir reutilização do conteúdo da página
- Mesclar fluxos duplicados
- Desincorporar fontes
- Remover objetos não utilizados
- Remover campos de formulário aplainados
- Remover ou aplainar anotações

## Otimizar Documento PDF para a Web

Otimização ou linearização refere-se ao processo de tornar um arquivo PDF adequado para navegação online usando um navegador da web.
 Aspose.PDF suporta este processo.

Para otimizar um PDF para exibição na web:

1. Abra o documento de entrada em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Use o método [optimize()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#optimize--).
1. Salve o documento otimizado usando o método save(..).

O trecho de código a seguir mostra como otimizar um documento PDF para a web.

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.time.Clock;
import java.time.Duration;

import com.aspose.pdf.*;
import com.aspose.pdf.optimization.ImageCompressionVersion;
import com.aspose.pdf.optimization.ImageEncoding;

public class ExampleOptimize {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void OptimizePDFDocumentForTheWeb() {

        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "sample.pdf");

        // Otimizar para web
        pdfDocument.optimize();

        // Salvar documento de saída
        pdfDocument.save(_dataDir + "OptimizeDocument_out.pdf");
    }
```

## Reduzir Tamanho do Arquivo PDF

Este tópico explica as etapas para otimizar/reduzir o tamanho do arquivo PDF. A API Aspose.PDF fornece a classe [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf.optimization/class-use/OptimizationOptions) que oferece flexibilidade para otimizar o PDF de saída removendo objetos desnecessários e comprimindo arquivos PDF com imagens. Ambas as opções são elaboradas nas seções seguintes.

### Remover Objetos Desnecessários
Podemos otimizar o tamanho de documentos PDF removendo objetos duplicados e não utilizados. O trecho de código a seguir mostra como.

```java
public static void ReduceSizePDF() {

        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "sample.pdf");

        // Otimizar documento PDF. Note, porém, que este método não pode garantir
        // a redução do documento
        pdfDocument.optimizeResources();

        // Salvar documento de saída
        pdfDocument.save(_dataDir + "OptimizeDocument_out.pdf");
    }
```

## Reduzindo ou Comprimindo Todas as Imagens

Se o arquivo PDF de origem contiver imagens, considere comprimir as imagens e definir sua qualidade. Para habilitar a compressão de imagens, passe true como argumento para o método setCompressImages(..). Todas as imagens em um documento serão recomprimidas. A compressão é definida pelo método setImageQuality(..), que é o valor da qualidade em porcentagem. 100% é qualidade e tamanho de imagem inalterados. Para diminuir o tamanho da imagem, passe um argumento menor que 100 para o método setImageQuality(..).

```java
public static void ShrinkingCompressing() {
        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "Shrinkimage.pdf");

        // Inicializar OptimizationOptions
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();

        // Definir opção CompressImages
        optimizationOptions.getImageCompressionOptions().setCompressImages(true);

        // Definir opção ImageQuality
        optimizationOptions.getImageCompressionOptions().setImageQuality(50);

        // Otimizar documento PDF usando OptimizationOptions
        pdfDocument.optimizeResources(optimizationOptions);
        _dataDir = _dataDir + "Shrinkimage_out.pdf";
        // Salvar documento atualizado
        pdfDocument.save(_dataDir);
    }
```

Outro modo é redimensionar as imagens com uma resolução mais baixa. Neste caso, devemos definir ResizeImages como true e MaxResolution para o valor apropriado.

```java
public static void ShrinkingCompressing2() {
        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "ResizeImage.pdf");

        // Inicializar OptimizationOptions
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();

        // Definir opção CompressImages
        optimizationOptions.getImageCompressionOptions().setCompressImages(true);
        // Definir opção ImageQuality
        optimizationOptions.getImageCompressionOptions().setImageQuality(75);

        // Definir opção ResizeImage
        optimizationOptions.getImageCompressionOptions().setResizeImages(true);

        // Definir opção MaxResolution
        optimizationOptions.getImageCompressionOptions().setMaxResolution(300);

        // Otimizar documento PDF usando OptimizationOptions
        pdfDocument.optimizeResources(optimizationOptions);
        _dataDir = _dataDir + "ResizeImages_out.pdf";
        // Salvar documento atualizado
        pdfDocument.save(_dataDir);
    }
```

Another important issue is the execution time. But again, we can manage this setting too. Currently, we can use two algorithms - Standard and Fast. To control the execution time we should set a Version property. The following snippet demonstrates the Fast algorithm:

```java
public static void ShrinkingCompressing3() {

        Clock clock = Clock.systemUTC();

        Duration tickDuration = Duration.ofNanos(250000);
        Clock clock1 = Clock.tick(clock, tickDuration);
        System.out.println("Início : " + clock.instant());

        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "ResizeImage.pdf");

        // Inicializar OptimizationOptions
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();

        // Definir opção CompressImages
        optimizationOptions.getImageCompressionOptions().setCompressImages(true);

        // Definir opção ImageQuality
        optimizationOptions.getImageCompressionOptions().setImageQuality(75);

        // Definir Versão de Compressão de Imagem para rápida
        optimizationOptions.getImageCompressionOptions().setVersion(ImageCompressionVersion.Fast);

        // Otimizar documento PDF usando OptimizationOptions
        pdfDocument.optimizeResources(optimizationOptions);

        _dataDir = _dataDir + "ResizeImages_out.pdf";

        // Salvar documento atualizado
        pdfDocument.save(_dataDir);
        System.out.println("Fim : " + clock1.instant());
    }
```

## Removendo Objetos Não Utilizados

Um documento PDF às vezes contém objetos PDF que não são referenciados por nenhum outro objeto no documento. Isso pode acontecer, por exemplo, quando uma página é removida da árvore de páginas do documento, mas o próprio objeto da página não é removido. Remover esses objetos não torna o documento inválido, mas o reduz.

```java
    public static void RemovingUnusedObjects() {

        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();
        
        optimizationOptions.setRemoveUnusedObjects(true);
        pdfDocument.optimizeResources(optimizationOptions);
        
        _dataDir = _dataDir + "emoveUnusedObjects_out.pdf";

        // Salvar documento atualizado
        pdfDocument.save(_dataDir);

    }
```
## Removendo Fluxos Não Utilizados

Às vezes, um documento contém fluxos de recursos não utilizados.
 Esses fluxos não são "objetos não utilizados" porque são referenciados a partir do dicionário de recursos de uma página. Isso pode acontecer em casos onde uma imagem foi removida da página, mas não dos recursos da página. Além disso, essa situação ocorre frequentemente quando páginas são extraídas do documento e as páginas do documento têm recursos "comuns", ou seja, o mesmo objeto de Recursos. O conteúdo das páginas é analisado para determinar se um fluxo de recursos é usado ou não. Fluxos não utilizados são removidos. Às vezes, isso diminui o tamanho do documento.

```java
public static void RemovingUnusedStream() {
        // Abrir documento
        Document pdfDocument = new Document(_dataDir + 
        "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();
        optimizationOptions.setRemoveUnusedStreams(true);
        pdfDocument.optimizeResources(optimizationOptions);
        _dataDir = _dataDir + "removeUnusedObjects_out.pdf";
        
        // Salvar documento atualizado
        pdfDocument.save(_dataDir);
        
    }
```
## Vinculando Fluxos Duplicados

Às vezes, um documento contém vários fluxos de recursos idênticos (por exemplo, imagens). Isso pode acontecer, por exemplo, quando um documento é concatenado consigo mesmo. O documento de saída contém duas cópias independentes do mesmo fluxo de recursos. Analisamos todos os fluxos de recursos e os comparamos. Se os fluxos forem duplicados, eles são mesclados, ou seja, apenas uma cópia é mantida, as referências são alteradas adequadamente e as cópias do objeto são removidas. Às vezes, isso diminui o tamanho do documento.

```java
    public static void LinkingDuplicateStream() {
        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();
        optimizationOptions.setRemoveUnusedStreams(true);
        
        // Otimizar documento PDF usando OptimizationOptions
        pdfDocument.optimizeResources(optimizationOptions);
        _dataDir = _dataDir + "OptimizeDocument_out.pdf";
        
        // Salvar documento atualizado
        pdfDocument.save(_dataDir);
    }
```

Além disso, podemos usar as configurações AllowReusePageContent. Se esta propriedade estiver definida como true, o conteúdo da página será reutilizado ao otimizar o documento para páginas idênticas.

```java
public static void AllowReusePageContent() {
        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();
        optimizationOptions.setAllowReusePageContent(true);
        
        // Otimizar documento PDF usando OptimizationOptions
        pdfDocument.optimizeResources(optimizationOptions);
        _dataDir = _dataDir + "OptimizeDocument_out.pdf";
        
        // Salvar documento atualizado
        pdfDocument.save(_dataDir);
    }
```
## Desincorporando Fontes

Se o documento usa fontes incorporadas, significa que todos os dados da fonte estão presentes no documento.
 A vantagem é que o documento pode ser visualizado independentemente de a fonte estar instalada na máquina do usuário ou não. Mas incorporar fontes torna o documento maior. O método de remoção de fontes incorporadas remove todas as fontes incorporadas. Isso reduz o tamanho do documento, mas o documento pode se tornar ilegível se a fonte correta não estiver instalada.

```java
    public static void UnembedFonts() {
        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();
        optimizationOptions.setUnembedFonts(true);
        
        // Otimizar documento PDF usando OptimizationOptions
        pdfDocument.optimizeResources(optimizationOptions);
        
        _dataDir = _dataDir + "OptimizeDocument_out.pdf";
        // Salvar documento atualizado
        pdfDocument.save(_dataDir);
    }
```

## Removendo ou Achatando Anotações

As anotações podem ser deletadas quando são desnecessárias. Quando eles são necessários, mas não exigem edição adicional, eles podem ser achatados. Ambas as técnicas reduzirão o tamanho do arquivo.

```java
    public static void FlatteningAnnotations() {
        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");

        for (Page page : pdfDocument.getPages()) {
            for (Annotation annotation : page.getAnnotations())
                annotation.flatten();
        }

        _dataDir = _dataDir + "OptimizeDocument_out.pdf";
        // Salvar documento atualizado
        pdfDocument.save(_dataDir);
    }

```
## Removendo Campos de Formulário

Se o documento PDF contiver AcroForms, podemos tentar reduzir o tamanho do arquivo achatando os campos do formulário.

```java
    public static void RemovingFormFields() {
        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");

        // Achatar Formulários
        if (pdfDocument.getForm().getFields().length > 0) {
            for (Field field : pdfDocument.getForm().getFields()) {
                field.flatten();
            }
        }
        _dataDir = _dataDir + "FlattenForms_out.pdf";
        // salvar o documento atualizado
        pdfDocument.save(_dataDir);
    }

```
## Converter um PDF do espaço de cores RGB para escala de cinza

Um arquivo PDF é composto por Texto, Imagem, Anexo, Anotações, Gráficos e outros objetos. Você pode se deparar com a necessidade de converter um PDF do espaço de cores RGB para escala de cinza para que seja mais rápido ao imprimir esses arquivos PDF. Além disso, quando o arquivo é convertido para escala de cinza, o tamanho do documento também é reduzido, mas com essa mudança, a qualidade do documento pode cair. Atualmente, esse recurso é suportado pelo recurso Pre-Flight do Adobe Acrobat, mas quando falamos de automação de escritório, o Aspose.PDF é uma solução definitiva para fornecer tais vantagens para manipulação de documentos.

Para cumprir esse requisito, o snippet de código a seguir pode ser usado.

```java
    public static void ConvertRGBtoGrayscale() {

        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");

        com.aspose.pdf.RgbToDeviceGrayConversionStrategy strategy = new com.aspose.pdf.RgbToDeviceGrayConversionStrategy();
        for (int idxPage = 1; idxPage <= pdfDocument.getPages().size(); idxPage++) {
            Page page = pdfDocument.getPages().get_Item(idxPage);
            strategy.convert(page);
        }
        pdfDocument.save("output.pdf");
    }
```

## Compressão FlateDecode

O Aspose.PDF para Java oferece suporte à compressão FlateDecode para a funcionalidade de Otimização de PDF. O trecho de código abaixo mostra como usar a opção na Otimização para armazenar imagens com compressão FlateDecode:

```java
    public static void FlateDecodeCompression() {

        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();

        optimizationOptions.getImageCompressionOptions().setEncoding(ImageEncoding.Flate);

        // Otimizar documento PDF usando OptimizationOptions
        pdfDocument.optimizeResources(optimizationOptions);

        _dataDir = _dataDir + "OptimizeDocument_out.pdf";
        // Salvar documento atualizado
        pdfDocument.save(_dataDir);
    }
```
## Armazenar Imagem na XImageCollection

O Aspose.PDF para Java fornece a capacidade de armazenar novas imagens na [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/XImageCollection) com compressão FlateDecode.
 Para habilitar esta opção, você pode usar a flag ImageFilterType.Flate. O trecho de código a seguir mostra como usar essa funcionalidade:

```java
    public static void StoreImageInXImageCollection() {
        // Inicializar Documento
        Document document = new Document();
        document.getPages().add();
        Page page = document.getPages().get_Item(1);

        // Carregar imagem em stream
        java.io.FileInputStream imageStream = null;
        try {
            imageStream = new java.io.FileInputStream(new java.io.File("input_image1.jpg"));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
            return;
        }
        page.getResources().getImages().add(imageStream, ImageFilterType.Flate);
        XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());
        page.getContents().add(new com.aspose.pdf.operators.GSave());

        // Definir coordenadas
        int lowerLeftX = 0;
        int lowerLeftY = 0;
        int upperRightX = 600;
        int upperRightY = 600;
        Rectangle rectangle = new Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
        Matrix matrix = new Matrix(new double[] { rectangle.getURX() - rectangle.getLLX(), 0, 0,
                rectangle.getURY() - rectangle.getLLY(), rectangle.getLLX(), rectangle.getLLY() });
        // Usando operador ConcatenateMatrix (concatenar matriz): define como a imagem deve ser colocada
        page.getContents().add(new com.aspose.pdf.operators.ConcatenateMatrix(matrix));
        page.getContents().add(new com.aspose.pdf.operators.Do(ximage.getName()));
        page.getContents().add(new com.aspose.pdf.operators.GRestore());

        document.save(_dataDir + "FlateDecodeCompression.pdf");
    }

}
```