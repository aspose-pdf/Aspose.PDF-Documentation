---
title: Оптимизировать, сжать или уменьшить размер PDF в Python
linktitle: Оптимизировать PDF
type: docs
weight: 30
url: /ru/python-net/optimize-pdf/
description: Узнайте, как оптимизировать PDF‑документы в Python для повышения производительности в вебе и уменьшения размера файлов с помощью Aspose.PDF.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Сжать страницы PDF с помощью Python
Abstract: В этой статье представлено всестороннее руководство по оптимизации PDF‑файлов с целью уменьшения их размера и повышения производительности на различных платформах, таких как веб‑страницы, электронная почта и системы хранения. Техники оптимизации включают уменьшение размеров изображений, удаление неиспользуемых ресурсов и удаление встроенных шрифтов. Рассматриваются конкретные методы оптимизации PDF для веба и снижения общего размера файла с использованием методов `Optimize` и `OptimizeResources` в Aspose.PDF для Python. Настройка стратегий оптимизации возможна с помощью `OptimizationOptions`, позволяя выполнять целевые действия, такие как сжатие изображений, удаление неиспользуемых объектов и потоков, объединение дублирующихся потоков и удаление встроенных шрифтов. Дополнительные стратегии охватывают уплощение аннотаций, удаление полей форм и преобразование PDF‑файлов из RGB в градации серого для дальнейшего уменьшения размера. В статье также подчёркнуто использование сжатия FlateDecode для оптимизации изображений, обеспечивая эффективное управление PDF‑файлами при сохранении качества и функциональности.
---

PDF‑документ может иногда содержать дополнительные данные. Сокращение размера PDF‑файла поможет оптимизировать передачу по сети и хранение. Это особенно удобно для публикации на веб‑страницах, обмена в социальных сетях, отправки по электронной почте или архивирования. Мы можем использовать несколько техник для оптимизации PDF:

- Оптимизировать содержимое страниц для онлайн‑просмотра
- Сжать или сжать все изображения
- Включить повторное использование содержимого страниц
- Объединить дублирующие потоки
- Удалить встроенные шрифты
- Удалить неиспользуемые объекты
- Удалить уплощённые поля форм
- Удалить или уплотнить аннотации

{{% alert color="primary" %}}

Подробное объяснение методов оптимизации можно найти на странице обзора методов оптимизации.

{{% /alert %}}

## Оптимизировать PDF‑документ для веба

Оптимизация, или линерация для веба, относится к процессу подготовки PDF‑файла к онлайн‑просмотру в веб‑браузере. Чтобы оптимизировать файл для отображения в вебе:

1. Откройте входной документ в объекте [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) .
1. Используйте метод [Optimize](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) .
1. Сохраните оптимизированный документ, используя метод [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) .

Следующий фрагмент кода демонстрирует, как оптимизировать PDF‑документ для веба.

```python

    import aspose.pdf as ap

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    document = apdf.Document(path_infile)
    document.optimize()
    document.save(path_outfile)
```

## Уменьшить размер PDF

Метод [OptimizeResources()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) позволяет уменьшить размер документа, удаляя ненужную информацию. По умолчанию этот метод работает следующим образом:

- Ресурсы, не используемые на страницах документа, удаляются
- Одинаковые ресурсы объединяются в один объект
- Неиспользуемые объекты удаляются

Приведённый ниже фрагмент – пример. Учтите, однако, что этот метод не может гарантировать уменьшение размера документа.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Optimize PDF document. Note, though, that this method cannot guarantee document shrinking
    document.optimize_resources()
    # Save updated document
    document.save(output_pdf)
```

## Управление стратегией оптимизации

Мы также можем настроить стратегию оптимизации. В настоящее время метод [OptimizeResources()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) использует 5 техник. Эти техники можно применять, используя метод OptimizeResources() с параметром [OptimizationOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/optimizationoptions/) .

### Сжатие или уменьшение всех изображений

У нас есть два способа работы с изображениями: уменьшить качество изображения и/или изменить их разрешение. В любом случае следует применять [ImageCompressionOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/imagecompressionoptions/) . В следующем примере мы сжимаем изображения, уменьшая ImageQuality до 50.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Initialize OptimizationOptions
    optimizeOptions = ap.optimization.OptimizationOptions()
    # Set CompressImages option
    optimizeOptions.image_compression_options.compress_images = True
    # Set ImageQuality option
    optimizeOptions.image_compression_options.image_quality = 50
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(output_pdf)
```

### Удаление неиспользуемых объектов

PDF‑документ иногда содержит PDF‑объекты, которые не связаны ни с одним другим объектом в документе. Это может произойти, например, когда страница удаляется из дерева страниц документа, но сам объект страницы не удаляется. Удаление этих объектов не делает документ недействительным, а наоборот уменьшает его.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Set RemoveUsedObject option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_objects = True

    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(output_pdf)
```

### Удаление неиспользуемых потоков

Иногда документ содержит неиспользуемые ресурсные потоки. Эти потоки не являются «неиспользуемыми объектами», потому что они ссылятся из словаря ресурсов страницы. Поэтому они не удаляются методом «удалить неиспользуемые объекты». Однако эти потоки никогда не используются в содержимом страниц. Это может происходить, когда изображение удалено со страницы, но не из ресурсов страницы. Кроме того, такая ситуация часто возникает, когда страницы извлекаются из документа, а страницы документа имеют «общие» ресурсы, то есть одинаковый объект Resources. Содержимое страниц анализируется, чтобы определить, используется ли ресурсный поток. Неиспользуемые потоки удаляются. Это иногда уменьшает размер документа. Применение этой техники схоже с предыдущим шагом:

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Set RemoveUsedStreams option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_streams = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(output_pdf)
```

### Объединение дублирующих потоков

Некоторые документы могут содержать несколько идентичных ресурсных потоков (например, изображений). Это может произойти, например, когда документ соединяется с самим собой. Выходной документ содержит две независимые копии одного и того же ресурсного потока. Мы анализируем все ресурсные потоки и сравниваем их. Если потоки дублируются, они объединяются, то есть остаётся только одна копия. Соответственно изменяются ссылки, а копии объекта удаляются. В некоторых случаях это помогает уменьшить размер документа.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Set LinkDuplicateStreams option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.link_duplcate_streams = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(output_pdf)
```

### Удаление встроенных шрифтов

Если документ использует встроенные шрифты, это означает, что все данные шрифтов хранятся в документе. Преимущество в том, что документ можно просматривать независимо от того, установлен ли шрифт на компьютере пользователя. Однако встраивание шрифтов увеличивает размер документа. Метод удаления встроенных шрифтов удаляет все встроенные шрифты. Таким образом, размер документа уменьшается, но сам документ может стать нечитаемым, если нужный шрифт не установлен.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Set UnembedFonts  option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.unembed_fonts = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(output_pdf)
    file_stats_1 = os.stat(input_pdf)
    file_stats_2 = os.stat(output_pdf)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

Оптимизационные ресурсы применяют эти методы к документу. Если какой-либо из этих методов применяется, размер документа, скорее всего, уменьшится. Если ни один из методов не применяется, размер документа не изменится, что очевидно.

## Дополнительные способы уменьшения размера PDF‑документа

### Удаление или уплощение аннотаций

Аннотации можно удалить, если они не нужны. Если они нужны, но не требуют дополнительного редактирования, их можно уплощить. Оба этих метода уменьшат размер файла.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Flatten annotations
    for page in document.pages:
        for annotation in page.annotations:
            annotation.flatten()

    # Save updated document
    document.save(output_pdf)
```

### Удаление полей формы

Если PDF‑документ содержит AcroForms, мы можем попытаться уменьшить размер файла, уплощая поля формы.

```python

    import aspose.pdf as ap

    # Load source PDF form
    doc = ap.Document(input_pdf)

    # Flatten Forms
    if len(doc.form.fields) > 0:
        for item in doc.form.fields:
            item.flatten()

    # Save the updated document
    doc.save(output_pdf)
```

### Преобразование PDF из цветового пространства RGB в градации серого

PDF‑файл состоит из текста, изображений, вложений, аннотаций, графиков и других объектов. Вам может понадобиться преобразовать PDF из цветового пространства RGB в градации серого, чтобы ускорить печать этих PDF‑файлов. Кроме того, при преобразовании в градации серого размер документа также уменьшается, хотя это может снизить качество документа. Эта функция в настоящее время поддерживается функцией Pre‑Flight в Adobe Acrobat, но когда речь идет об автоматизации офисных задач, Aspose.PDF является идеальным решением, предоставляющим такие возможности для манипуляций с документами. Чтобы выполнить эту задачу, можно использовать следующий фрагмент кода.

```python

    import aspose.pdf as ap

    # Load source PDF file
    document = ap.Document(input_pdf)
    strategy = ap.RgbToDeviceGrayConversionStrategy()
    for page in document.pages:
        # Convert the RGB colorspace image to GrayScale colorspace
        strategy.convert(page)

    # Save resultant file
    document.save(output_pdf)
```

### Сжатие FlateDecode

Aspose.PDF для Python через .NET предоставляет поддержку сжатия FlateDecode для функции оптимизации PDF. Приведенный ниже фрагмент кода показывает, как использовать параметр в оптимизации для сохранения изображений со сжатием **FlateDecode**:

```python

    import aspose.pdf as ap

    # Open Document
    doc = ap.Document(input_pdf)
    # Initialize OptimizationOptions
    optimizationOptions = ap.optimization.OptimizationOptions()
    # To optimise image using FlateDecode Compression set optimization options to Flate
    optimizationOptions.image_compression_options.encoding = ap.optimization.ImageEncoding.FLATE
    # Set Optimization Options
    doc.optimize_resources(optimizationOptions)
    # Save Document
    doc.save(output_pdf)
```


