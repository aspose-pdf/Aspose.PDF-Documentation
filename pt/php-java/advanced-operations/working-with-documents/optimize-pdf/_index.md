---
title: Otimizar, Comprimir ou Reduzir Tamanho de PDF em PHP
linktitle: Otimizar Documento PDF
type: docs
weight: 40
url: /pt/php-java/optimize-pdf/
description: Otimizar arquivo PDF, reduzir todas as imagens, diminuir tamanho do PDF, Desincorporar fontes, Remover objetos não utilizados usando PHP.
lastmod: "2024-06-05"
---

Um documento PDF pode, às vezes, conter dados adicionais. Reduzir o tamanho de um arquivo PDF ajudará a otimizar a transferência de rede e o armazenamento. Isso é especialmente útil para publicação em páginas da web, compartilhamento em redes sociais, envio por e-mail ou arquivamento em armazenamento. Podemos usar várias técnicas para otimizar PDF:

- Otimizar o conteúdo da página para navegação online
- Reduzir ou comprimir todas as imagens
- Permitir reutilização do conteúdo da página
- Mesclar fluxos duplicados
- Desincorporar fontes
- Remover objetos não utilizados
- Remover campos de formulário achatados
- Remover ou achatar anotações

## Otimizar Documento PDF para a Web

Otimização ou linearização refere-se ao processo de tornar um arquivo PDF adequado para navegação online usando um navegador da web.
 Aspose.PDF suporta este processo.

Para otimizar um PDF para exibição na web:

1. Abra o documento de entrada em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Use o método [optimize()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#optimize--).
1. Salve o documento otimizado usando o método save(..).

O trecho de código a seguir mostra como otimizar um documento PDF para a web.

```php

    // Abrir documento
    $document = new Document($inputFile);

    // Otimizar para a web
    $document->optimize();

    // Salvar o documento atualizado
    $document->save($outputFile);
    $document->close();
```

## Reduzir Tamanho do Arquivo PDF

Este tópico explica as etapas para otimizar/reduzir o tamanho do arquivo PDF. Aspose.PDF API fornece a classe [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf.optimization/class-use/OptimizationOptions) que oferece a flexibilidade de otimizar o PDF de saída removendo objetos desnecessários e comprimindo arquivos PDF que contêm imagens. Ambas as opções são elaboradas nas seções a seguir.

### Remover Objetos Desnecessários

Podemos otimizar o tamanho de documentos PDF removendo objetos duplicados e não utilizados. O trecho de código a seguir mostra como.

```php

    // Abrir documento
    $document = new Document($inputFile);
    
    // Otimizar documento PDF. No entanto, observe que este método não pode garantir
    // a redução do documento
    $document->optimizeResources();

    // Salvar o documento atualizado
    $document->save($outputFile);
    $document->close();

```

## Reduzindo ou Comprimindo Todas as Imagens

Se o arquivo PDF de origem contiver imagens, considere comprimir as imagens e ajustar sua qualidade. Para habilitar a compressão de imagem, passe true como um argumento para o método setCompressImages(..). Todas as imagens em um documento serão recomprimidas. A compressão é definida pelo método setImageQuality(..), que é o valor da qualidade em porcentagem. 100% é qualidade e tamanho de imagem inalterados. Para diminuir o tamanho da imagem, passe um argumento menor que 100 para o método setImageQuality(..).

```php

    // Abrir documento
    $document = new Document($inputFile);
    
    // Inicializar OptimizationOptions
    $optimizationOptions = new OptimizationOptions();

    // Definir opção CompressImages
    $optimizationOptions->getImageCompressionOptions()->setCompressImages(true);

    // Definir opção ImageQuality
    $optimizationOptions->getImageCompressionOptions()->setImageQuality(50);

    // Otimizar documento PDF usando OptimizationOptions
    $document->optimizeResources($optimizationOptions);

    // Salvar o documento atualizado
    $document->save($outputFile);
    $document->close();
```

Outra maneira é redimensionar as imagens com uma resolução menor. Neste caso, devemos definir ResizeImages como verdadeiro e MaxResolution para o valor apropriado.

```php

    // Abrir documento
    $document = new Document($inputFile);
    
    // Inicializar OptimizationOptions
    $optimizationOptions = new OptimizationOptions();

    // Definir opção CompressImages
    $optimizationOptions->getImageCompressionOptions()->setCompressImages(true);
    
    // Definir opção ImageQuality
    $optimizationOptions->getImageCompressionOptions()->setImageQuality(75);

    // Definir opção ResizeImage
    $optimizationOptions->getImageCompressionOptions()->setResizeImages(true);

    // Definir opção MaxResolution
    $optimizationOptions->getImageCompressionOptions()->setMaxResolution(300);

    // Salvar o documento atualizado
    $document->save($outputFile);
    $document->close();
```

Outra questão importante é o tempo de execução. Mas novamente, podemos gerenciar essa configuração também. Atualmente, podemos usar dois algoritmos - Padrão e Rápido. Para controlar o tempo de execução, devemos definir uma propriedade de Versão. O trecho a seguir demonstra o algoritmo Rápido:

```php
    // Abrir documento
    $document = new Document($inputFile);
    
    // Inicializar OptimizationOptions
    $optimizationOptions = new optimization_OptimizationOptions();

    // Definir opção CompressImages
    $optimizationOptions->getImageCompressionOptions()->setCompressImages(true);

    // Definir opção ImageQuality
    $optimizationOptions->getImageCompressionOptions()->setImageQuality(75);
    $optimization_ImageCompressionVersion = new optimization_ImageCompressionVersion();

    // Definir Versão de Compressão de Imagem para rápido
    $optimizationOptions->getImageCompressionOptions()->setVersion($optimization_ImageCompressionVersion->Fast);

    // Otimizar documento PDF usando OptimizationOptions
    $document->optimizeResources($optimizationOptions);

    // Salvar o documento atualizado
    $document->save($outputFile);
    $document->close();
```

## Removendo Objetos Não Utilizados

Um documento PDF às vezes contém objetos PDF que não são referenciados por nenhum outro objeto no documento. Isso pode acontecer, por exemplo, quando uma página é removida da árvore de páginas do documento, mas o próprio objeto da página não é removido. Remover esses objetos não torna o documento inválido, mas sim o reduz.

```php

    // Abrir documento
    $document = new Document($inputFile);
    
    // Inicializar OptimizationOptions
    $optimizationOptions = new OptimizationOptions();

    $optimizationOptions->setRemoveUnusedObjects(true);

    // Otimizar documento PDF usando OptimizationOptions
    $document->optimizeResources($optimizationOptions);

    // Salvar o documento atualizado
    $document->save($outputFile);
    $document->close();
```

## Removendo Streams Não Utilizados

Às vezes, um documento contém streams de recursos não utilizados.
 Esses fluxos não são "objetos não utilizados" porque são referenciados a partir do dicionário de recursos de uma página. Isso pode acontecer em casos onde uma imagem foi removida da página, mas não dos recursos da página. Além disso, essa situação ocorre frequentemente quando páginas são extraídas do documento e as páginas do documento têm recursos "comuns", ou seja, o mesmo objeto Recursos. O conteúdo da página é analisado para determinar se um fluxo de recurso é usado ou não. Fluxos não utilizados são removidos. Às vezes, isso diminui o tamanho do documento.

```php

    // Abrir documento
    $document = new Document($inputFile);
    
    // Inicializar OptimizationOptions
    $optimizationOptions = new OptimizationOptions();

    $optimizationOptions->setRemoveUnusedStreams(true);

    // Otimizar documento PDF usando OptimizationOptions
    $document->optimizeResources($optimizationOptions);

    // Salvar o documento atualizado
    $document->save($outputFile);
    $document->close();
```

## Vinculando Fluxos Duplicados

Às vezes, um documento contém vários fluxos de recursos idênticos (por exemplo, imagens). Isso pode acontecer, por exemplo, quando um documento é concatenado consigo mesmo. O documento de saída contém duas cópias independentes do mesmo fluxo de recursos. Analisamos todos os fluxos de recursos e os comparamos. Se os fluxos forem duplicados, eles são mesclados, ou seja, apenas uma cópia é deixada, as referências são alteradas adequadamente e as cópias do objeto são removidas. Às vezes, isso diminui o tamanho do documento.

```php
    // Abrir documento
    $document = new Document($inputFile);
    
    // Inicializar OptimizationOptions
    $optimizationOptions = new OptimizationOptions();
    
    $optimizationOptions->setLinkDuplcateStreams(true);
    
    // Otimizar documento PDF usando OptimizationOptions
    $document->optimizeResources($optimizationOptions);

    // Salvar o documento atualizado
    $document->save($outputFile);
    $document->close();
```

Além disso, podemos usar as configurações AllowReusePageContent. Se esta propriedade for definida como true, o conteúdo da página será reutilizado ao otimizar o documento para páginas idênticas.

```php
    // Abrir documento
    $document = new Document($inputFile);
    
    // Inicializar OptimizationOptions
    $optimizationOptions = new OptimizationOptions();

    $optimizationOptions->setAllowReusePageContent(true);

    // Otimizar documento PDF usando OptimizationOptions
    $document->optimizeResources($optimizationOptions);

    // Salvar o documento atualizado
    $document->save($outputFile);
    $document->close();
```

## Desincorporando Fontes

Se o documento usa fontes incorporadas, isso significa que todos os dados da fonte são colocados no documento. A vantagem é que o documento pode ser visualizado independentemente de a fonte estar instalada na máquina do usuário ou não. Mas incorporar fontes torna o documento maior. O método de desincorporar fontes remove todas as fontes incorporadas. Isso diminui o tamanho do documento, mas o documento pode se tornar ilegível se a fonte correta não estiver instalada.

```php

    // Abrir documento
    $document = new Document($inputFile);
    
    // Inicializar OptimizationOptions
    $optimizationOptions = new OptimizationOptions();

    $optimizationOptions->setUnembedFonts(true);

    // Otimizar documento PDF usando OptimizationOptions
    $document->optimizeResources($optimizationOptions);

    // Salvar o documento atualizado
    $document->save($outputFile);
    $document->close();
```

## Removendo ou Achatando Anotações

As anotações podem ser deletadas quando são desnecessárias.
 Quando eles são necessários, mas não requerem edição adicional, eles podem ser achatados. Ambas as técnicas reduzirão o tamanho do arquivo.

```php

    // Abrir documento
    $document = new Document($inputFile);
    $pages = $document->getPages();

    for ($i=1; $i < $pages->size() ; $i++) { 
        $page = $pages->get_Item($i);
        $annotations = $page->getAnnotations();
        for ($idx=0; $idx < $annotations->size(); $idx++) { 
            $annotation = $annotations->get_Item($idx);
            $annotation->flatten();
        }
    }
     
    // Salvar o documento atualizado
    $document->save($outputFile);
    $document->close();
```

## Removendo Campos de Formulário

Se o documento PDF contiver AcroForms, podemos tentar reduzir o tamanho do arquivo achatando os campos do formulário.

```php

    // Abrir documento
    $document = new Document($inputFile);
    
    // Achatar Formulários
    $fields = $document->getForm()->getFields();
    foreach ($fields as $field) {
        $field->flatten();
    }            

    // Salvar o documento atualizado
    $document->save($outputFile);
    $document->close();
```

## Converter um PDF do espaço de cores RGB para escala de cinza

Um arquivo PDF é composto por Texto, Imagem, Anexo, Anotações, Gráficos e outros objetos. Você pode se deparar com a necessidade de converter um PDF do espaço de cores RGB para escala de cinza para que seja mais rápido ao imprimir esses arquivos PDF. Além disso, quando o arquivo é convertido para escala de cinza, o tamanho do documento também é reduzido, mas com essa mudança, a qualidade do documento pode cair. Atualmente, esse recurso é suportado pela funcionalidade Pre-Flight do Adobe Acrobat, mas quando se fala em automação de escritório, Aspose.PDF é uma solução definitiva para fornecer tais facilidades para manipulação de documentos.

Para cumprir este requisito, o seguinte trecho de código pode ser usado.

```php

    // Abrir documento
    $document = new Document($inputFile);
    
    $strategy = new RgbToDeviceGrayConversionStrategy();
    for ($idxPage = 1; $idxPage <= $document->getPages()->size(); $idxPage++) {
        $page = $document->getPages()->get_Item($idxPage);
        $strategy->convert($page);
    }          

    // Salvar o documento atualizado
    $document->save($outputFile);
    $document->close();
```


## FlateDecode Compressão

Aspose.PDF para PHP via Java oferece suporte à compressão FlateDecode para a funcionalidade de Otimização de PDF. O trecho de código a seguir mostra como usar a opção em Otimização para armazenar imagens com compressão FlateDecode:

```php

    // Abrir documento
    $document = new Document($inputFile);

    // Inicializar OptimizationOptions
    $optimizationOptions = new OptimizationOptions();

    $optimizationOptions->setUnembedFonts(true);

    // Otimizar o documento PDF usando OptimizationOptions
    $optimizationOptions->getImageCompressionOptions()->setEncoding(optimization_ImageEncoding::$Flate);

    // Salvar o documento atualizado
    $document->save($outputFile);
    $document->close();
```

## Armazenar Imagem em XImageCollection

Aspose.PDF para PHP via Java oferece a capacidade de armazenar novas imagens em [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/XImageCollection) com compressão FlateDecode.
 Para habilitar esta opção, você pode usar a flag ImageFilterType.Flate. O trecho de código a seguir mostra como usar essa funcionalidade:

```php
    // Abrir documento
    $document = new Document($inputFile);

    // Inicializar Documento
    $page = $document->getPages()->get_Item(1);

    // Carregar imagem no stream
    $imageStream = new java("java.io.FileInputStream",$inputFile);
    $imageFilterType = new ImageFilterType();
    $page->getResources()->getImages()->add($imageStream, $imageFilterType->Flate);
    $idx = $page->getResources()->getImages()->size();
    $ximage = $page->getResources()->getImages()->get_Item($idx);
    $page->getContents()->add(new operators_GSave());

    // Definir coordenadas
    $lowerLeftX = 0;
    $lowerLeftY = 0;
    $upperRightX = 600;
    $upperRightY = 600;
    $rectangle = new Rectangle($lowerLeftX, $lowerLeftY, $upperRightX, $upperRightY);
    $matrixData = [
        $rectangle->getURX() - $rectangle->getLLX(), 0, 
        0, $rectangle->getURY() - $rectangle->getLLY(), 
        $rectangle->getLLX(), $rectangle->getLLY()];
    $matrix = new Matrix($matrixData);

    // Usar operador ConcatenateMatrix (concatenar matriz): define como a imagem deve ser posicionada
    $page->getContents()->add(new operators_ConcatenateMatrix($matrix));
    $page->getContents()->add(new operators_Do($ximage->getName()));
    $page->getContents()->add(new operators_GRestore());

    // Salvar o documento atualizado
    $document->save($outputFile);
    $document->close();
```