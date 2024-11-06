---
title: Optimize, Compress or Reduce PDF Size in PHP
linktitle: Optimize PDF Document
type: docs
weight: 40
url: ru/php-java/optimize-pdf/
description: Оптимизация PDF файла, сжатие всех изображений, уменьшение размера PDF, удаление встроенных шрифтов, удаление неиспользуемых объектов с использованием PHP.
lastmod: "2024-06-05"
---

PDF документ может иногда содержать дополнительные данные. Уменьшение размера PDF файла поможет вам оптимизировать передачу по сети и хранение. Это особенно удобно для публикации на веб-страницах, обмена в социальных сетях, отправки по электронной почте или архивации в хранилище. Мы можем использовать несколько техник для оптимизации PDF:

- Оптимизация содержимого страницы для просмотра в интернете
- Сжатие всех изображений
- Включение повторного использования содержимого страниц
- Объединение дублирующих потоков
- Удаление встроенных шрифтов
- Удаление неиспользуемых объектов
- Удаление или выравнивание полей форм
- Удаление или выравнивание аннотаций

## Оптимизация PDF документа для интернета

Оптимизация или линеаризация относится к процессу создания PDF файла, подходящего для просмотра в интернете с использованием веб-браузера.
 Aspose.PDF поддерживает этот процесс.

Чтобы оптимизировать PDF для отображения в вебе:

1. Откройте входной документ в объекте [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
2. Используйте метод [optimize()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#optimize--).
3. Сохраните оптимизированный документ, используя метод save(..).

Следующий фрагмент кода показывает, как оптимизировать PDF документ для веба.

```php

    // Открыть документ
    $document = new Document($inputFile);

    // Оптимизация для веб
    $document->optimize();

    // Сохранить обновленный документ
    $document->save($outputFile);
    $document->close();
```

## Уменьшение размера PDF файла

Эта тема объясняет шаги по оптимизации/уменьшению размера PDF файла. Aspose.PDF API предоставляет класс [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf.optimization/class-use/OptimizationOptions), который дает возможность оптимизировать выходной PDF, удаляя ненужные объекты и сжимая PDF-файлы, содержащие изображения. Оба этих варианта подробно описаны в следующих разделах.

### Удаление ненужных объектов

Мы можем оптимизировать размер PDF-документов, удаляя дубликаты и неиспользуемые объекты. Следующий фрагмент кода показывает, как это сделать.

```php

    // Открыть документ
    $document = new Document($inputFile);
    
    // Оптимизировать PDF-документ. Тем не менее, обратите внимание, что этот метод не может гарантировать
    // уменьшение размера документа
    $document->optimizeResources();

    // Сохранить обновленный документ
    $document->save($outputFile);
    $document->close();

```

## Сжатие всех изображений

Если исходный PDF-файл содержит изображения, рассмотрите возможность сжатия изображений и установки их качества. Для того чтобы включить сжатие изображений, передайте true в качестве аргумента методу setCompressImages(..). Все изображения в документе будут повторно сжаты. Сжатие определяется методом setImageQuality(..), который принимает значение качества в процентах. 100% означает неизменное качество и размер изображения. Чтобы уменьшить размер изображения, передайте аргумент, меньший 100, в метод setImageQuality(..).

```php

    // Открыть документ
    $document = new Document($inputFile);
    
    // Инициализация параметров оптимизации
    $optimizationOptions = new OptimizationOptions();

    // Установить опцию CompressImages
    $optimizationOptions->getImageCompressionOptions()->setCompressImages(true);

    // Установить опцию ImageQuality
    $optimizationOptions->getImageCompressionOptions()->setImageQuality(50);

    // Оптимизировать PDF документ с использованием параметров оптимизации
    $document->optimizeResources($optimizationOptions);

    // Сохранить обновленный документ
    $document->save($outputFile);
    $document->close();
```

Другой способ — изменить размер изображений с более низким разрешением. В этом случае, мы должны установить ResizeImages в true и MaxResolution на соответствующее значение.

```php

    // Открыть документ
    $document = new Document($inputFile);
    
    // Инициализация OptimizationOptions
    $optimizationOptions = new OptimizationOptions();

    // Установить опцию CompressImages
    $optimizationOptions->getImageCompressionOptions()->setCompressImages(true);
    
    // Установить опцию ImageQuality
    $optimizationOptions->getImageCompressionOptions()->setImageQuality(75);

    // Установить опцию ResizeImage
    $optimizationOptions->getImageCompressionOptions()->setResizeImages(true);

    // Установить опцию MaxResolution
    $optimizationOptions->getImageCompressionOptions()->setMaxResolution(300);

    // Сохранить обновленный документ
    $document->save($outputFile);
    $document->close();
```

Еще одна важная проблема - это время выполнения. Но опять же, мы можем управлять этой настройкой. В настоящее время мы можем использовать два алгоритма - Standard и Fast. Чтобы контролировать время выполнения, мы должны установить свойство Version. Следующий фрагмент демонстрирует алгоритм Fast:

```php
    // Открыть документ
    $document = new Document($inputFile);
    
    // Инициализировать OptimizationOptions
    $optimizationOptions = new optimization_OptimizationOptions();

    // Установить опцию CompressImages
    $optimizationOptions->getImageCompressionOptions()->setCompressImages(true);

    // Установить опцию ImageQuality
    $optimizationOptions->getImageCompressionOptions()->setImageQuality(75);
    $optimization_ImageCompressionVersion = new optimization_ImageCompressionVersion();

    // Установить версию сжатия изображений на fast
    $optimizationOptions->getImageCompressionOptions()->setVersion($optimization_ImageCompressionVersion->Fast);

    // Оптимизировать PDF документ используя OptimizationOptions
    $document->optimizeResources($optimizationOptions);

    // Сохранить обновленный документ
    $document->save($outputFile);
    $document->close();
```

## Удаление неиспользуемых объектов

PDF-документ иногда содержит PDF-объекты, на которые нет ссылок из других объектов в документе. Это может произойти, например, когда страница удаляется из дерева страниц документа, но сам объект страницы не удаляется. Удаление этих объектов не делает документ недействительным, а скорее сокращает его размер.

```php

    // Открыть документ
    $document = new Document($inputFile);
    
    // Инициализация OptimizationOptions
    $optimizationOptions = new OptimizationOptions();

    $optimizationOptions->setRemoveUnusedObjects(true);

    // Оптимизация PDF-документа с использованием OptimizationOptions
    $document->optimizeResources($optimizationOptions);

    // Сохранить обновленный документ
    $document->save($outputFile);
    $document->close();
```

## Удаление неиспользуемых потоков

Иногда документ содержит неиспользуемые потоки ресурсов.
 Эти потоки не являются "неиспользуемыми объектами", потому что они ссылаются из словаря ресурсов страницы. Это может произойти в случаях, когда изображение было удалено со страницы, но не из ресурсов страницы. Также эта ситуация часто возникает, когда страницы извлекаются из документа и страницы документа имеют "общие" ресурсы, то есть один и тот же объект Resources. Содержимое страницы анализируется для определения, используется ли поток ресурсов или нет. Неиспользуемые потоки удаляются. Иногда это уменьшает размер документа.

```php

    // Открыть документ
    $document = new Document($inputFile);
    
    // Инициализация OptimizationOptions
    $optimizationOptions = new OptimizationOptions();

    $optimizationOptions->setRemoveUnusedStreams(true);

    // Оптимизация PDF документа с использованием OptimizationOptions
    $document->optimizeResources($optimizationOptions);

    // Сохранить обновленный документ
    $document->save($outputFile);
    $document->close();
```

## Связывание дублирующихся потоков

Иногда документ содержит несколько идентичных потоков ресурсов (например, изображений). Это может произойти, например, когда документ соединяется с самим собой. Выходной документ содержит две независимые копии одного и того же потока ресурсов. Мы анализируем все потоки ресурсов и сравниваем их. Если потоки дублируются, они объединяются, то есть остается только одна копия, ссылки изменяются соответствующим образом и копии объекта удаляются. Иногда это уменьшает размер документа.

```php
    // Открыть документ
    $document = new Document($inputFile);
    
    // Инициализировать OptimizationOptions
    $optimizationOptions = new OptimizationOptions();
    
    $optimizationOptions->setLinkDuplcateStreams(true);
    
    // Оптимизировать PDF-документ с использованием OptimizationOptions
    $document->optimizeResources($optimizationOptions);

    // Сохранить обновленный документ
    $document->save($outputFile);
    $document->close();
```

Кроме того, мы можем использовать настройки AllowReusePageContent. Если это свойство установлено в значение true, содержимое страницы будет повторно использоваться при оптимизации документа для идентичных страниц.

```php
    // Открыть документ
    $document = new Document($inputFile);
    
    // Инициализировать OptimizationOptions
    $optimizationOptions = new OptimizationOptions();

    $optimizationOptions->setAllowReusePageContent(true);

    // Оптимизировать PDF-документ с использованием OptimizationOptions
    $document->optimizeResources($optimizationOptions);

    // Сохранить обновленный документ
    $document->save($outputFile);
    $document->close();
```

## Удаление встроенных шрифтов

Если документ использует встроенные шрифты, это означает, что все данные шрифта размещены в документе. Преимущество в том, что документ можно просматривать, независимо от того, установлен ли шрифт на компьютере пользователя или нет. Однако встраивание шрифтов делает документ больше. Метод удаления встроенных шрифтов удаляет все встроенные шрифты. Это уменьшает размер документа, но документ может стать нечитаемым, если нужный шрифт не установлен.

```php

    // Открыть документ
    $document = new Document($inputFile);
    
    // Инициализация OptimizationOptions
    $optimizationOptions = new OptimizationOptions();

    $optimizationOptions->setUnembedFonts(true);

    // Оптимизация PDF-документа с использованием OptimizationOptions
    $document->optimizeResources($optimizationOptions);

    // Сохранить обновленный документ
    $document->save($outputFile);
    $document->close();
```

## Удаление или упрощение аннотаций

Аннотации могут быть удалены, если они не нужны.
 Когда они необходимы, но не требуют дополнительного редактирования, их можно упрощать. Оба этих метода уменьшат размер файла.

```php

    // Открыть документ
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
     
    // Сохранить обновленный документ
    $document->save($outputFile);
    $document->close();
```

## Удаление полей формы

Если PDF-документ содержит AcroForms, мы можем попытаться уменьшить размер файла, упрощая поля формы.

```php

    // Открыть документ
    $document = new Document($inputFile);
    
    // Упрощение форм
    $fields = $document->getForm()->getFields();
    foreach ($fields as $field) {
        $field->flatten();
    }            

    // Сохранить обновленный документ
    $document->save($outputFile);
    $document->close();
```

## Преобразование PDF из цветового пространства RGB в градации серого

PDF файл состоит из текста, изображений, вложений, аннотаций, графиков и других объектов. Вы можете столкнуться с требованием преобразовать PDF из цветового пространства RGB в градации серого, чтобы ускорить печать этих PDF файлов. Также, когда файл преобразуется в градации серого, размер документа также уменьшается, но при этом может снизиться качество документа. В настоящее время эта функция поддерживается функцией Pre-Flight Adobe Acrobat, но когда речь идет об автоматизации офисных процессов, Aspose.PDF является идеальным решением для предоставления таких возможностей для манипуляции с документами.

Для выполнения этого требования можно использовать следующий фрагмент кода.

```php

    // Открыть документ
    $document = new Document($inputFile);
    
    $strategy = new RgbToDeviceGrayConversionStrategy();
    for ($idxPage = 1; $idxPage <= $document->getPages()->size(); $idxPage++) {
        $page = $document->getPages()->get_Item($idxPage);
        $strategy->convert($page);
    }          

    // Сохранить обновленный документ
    $document->save($outputFile);
    $document->close();
```


## FlateDecode Сжатие

Aspose.PDF для PHP через Java предоставляет поддержку сжатия FlateDecode для функциональности оптимизации PDF. Следующий фрагмент кода ниже показывает, как использовать опцию в Optimization для хранения изображений с сжатием FlateDecode:

```php

    // Открыть документ
    $document = new Document($inputFile);

    // Инициализация OptimizationOptions
    $optimizationOptions = new OptimizationOptions();

    $optimizationOptions->setUnembedFonts(true);

    // Оптимизация PDF-документа с использованием OptimizationOptions
    $optimizationOptions->getImageCompressionOptions()->setEncoding(optimization_ImageEncoding::$Flate);

    // Сохранить обновленный документ
    $document->save($outputFile);
    $document->close();
```

## Хранение Изображений в XImageCollection

Aspose.PDF для PHP через Java предоставляет возможность хранения новых изображений в [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/XImageCollection) с сжатием FlateDecode.
 Чтобы включить эту опцию, вы можете использовать флаг ImageFilterType.Flate. Следующий фрагмент кода показывает, как использовать эту функциональность:

```php
    // Открыть документ
    $document = new Document($inputFile);

    // Инициализировать документ
    $page = $document->getPages()->get_Item(1);

    // Загрузить изображение в поток
    $imageStream = new java("java.io.FileInputStream",$inputFile);
    $imageFilterType = new ImageFilterType();
    $page->getResources()->getImages()->add($imageStream, $imageFilterType->Flate);
    $idx = $page->getResources()->getImages()->size();
    $ximage = $page->getResources()->getImages()->get_Item($idx);
    $page->getContents()->add(new operators_GSave());

    // Установить координаты
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

    // Использование оператора ConcatenateMatrix (конкатенация матрицы): определяет, как должно быть размещено изображение
    $page->getContents()->add(new operators_ConcatenateMatrix($matrix));
    $page->getContents()->add(new operators_Do($ximage->getName()));
    $page->getContents()->add(new operators_GRestore());

    // Сохранить обновленный документ
    $document->save($outputFile);
    $document->close();
```