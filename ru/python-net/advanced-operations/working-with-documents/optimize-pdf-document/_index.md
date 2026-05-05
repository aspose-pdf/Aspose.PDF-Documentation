---
title: Оптимизировать PDF-файлы в Python
linktitle: Оптимизировать PDF
type: docs
weight: 30
url: /ru/python-net/optimize-pdf/
description: Узнайте, как оптимизировать, сжимать и уменьшать размер PDF‑файла в Python с помощью Aspose.PDF.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Сжимайте страницы PDF с помощью Python
Abstract: Эта статья предоставляет всестороннее руководство по оптимизации PDF‑файлов с целью уменьшения их размера и повышения производительности на различных платформах, таких как веб‑страницы, электронная почта и системы хранения. Техники оптимизации включают уменьшение размеров изображений, удаление неиспользуемых ресурсов и разупаковку шрифтов. Рассматриваются конкретные методы оптимизации PDF для веба и снижения общего размера файла, используя методы `Optimize` и `OptimizeResources` в Aspose.PDF for Python. Настройка стратегий оптимизации возможна через `OptimizationOptions`, позволяя выполнять целевые действия, такие как сжатие изображений, удаление неиспользуемых объектов и потоков, связывание дублирующих потоков и разупаковку шрифтов. Дополнительные стратегии охватывают уплощение аннотаций, удаление полей форм и преобразование PDF‑файлов из RGB в градации серого для дальнейшего уменьшения размера. В статье также подчеркивается использование сжатия FlateDecode для оптимизации изображений, обеспечивая эффективное управление PDF‑файлами при сохранении качества и функциональности.
---

PDF‑документ иногда может содержать дополнительные данные. Уменьшение размера PDF‑файла поможет оптимизировать передачу по сети и хранение. Это особенно удобно для публикации на веб‑страницах, обмена в социальных сетях, отправки по электронной почте или архивирования в хранилище. Мы можем использовать несколько техник для оптимизации PDF:

Используйте эту страницу, когда нужно уменьшить размер PDF для веб‑доставки, обмена по электронной почте, экономии места хранения или печати без необходимости воссоздавать документ с нуля.

- Оптимизировать содержимое страницы для онлайн‑просмотра
- Уменьшить или сжать все изображения
- Разрешить повторное использование содержимого страницы
- Объединить дублирующиеся потоки
- Удалить встраивание шрифтов
- Удалить неиспользуемые объекты
- Удалить уплощение полей формы
- Удалить или сплющить аннотации

{{% alert color="primary" %}}

 Подробное объяснение методов оптимизации можно найти на странице Обзор методов оптимизации.

{{% /alert %}}

## Оптимизировать PDF Document для Web

Оптимизация, или линейризация для веба, относится к процессу подготовки PDF‑файла к онлайн‑просмотру с помощью веб‑браузера. Чтобы оптимизировать файл для отображения в вебе:

1. Откройте входной документ в [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) объект.
1. Используйте [optimize()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) метод.
1. Сохранить оптимизированный документ, используя [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) метод.

Следующий фрагмент кода показывает, как оптимизировать PDF‑документ для веба.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def optimize_pdf(infile, outfile):
    document = ap.Document(infile)
    document.optimize()
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

## Уменьшить размер PDF

Эта [OptimizeResources()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) метод позволяет уменьшить размер документа, устраняя лишнюю информацию. По умолчанию этот метод работает следующим образом:

- Ресурсы, не используемые на страницах документа, удаляются
- Равные ресурсы объединяются в один объект
- Неиспользуемые объекты удаляются

Приведённый ниже фрагмент является примером. Однако обратите внимание, что этот метод не может гарантировать уменьшение документа.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def reduce_size_pdf(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Optimize PDF document. Note, though, that this method cannot guarantee document shrinking
    document.optimize_resources()
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

## Управление стратегией оптимизации

Мы также можем настроить стратегию оптимизации. В настоящее время, [OptimizeResources()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) метод использует 5 техник. Эти техники можно применить, используя метод OptimizeResources() с [OptimizationOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/optimizationoptions/) параметр.

### Уменьшение или сжатие всех изображений

У нас есть два способа работы с изображениями: уменьшить качество изображения и/или изменить их разрешение. В любом случае, [ImageCompressionOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/imagecompressionoptions/) Это должно быть применено. В следующем примере мы уменьшаем изображения, снижая ImageQuality до 50.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def shrinking_or_compressing_all_images(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Initialize OptimizationOptions
    optimizeOptions = ap.optimization.OptimizationOptions()
    # Set CompressImages option
    optimizeOptions.image_compression_options.compress_images = True
    # Set ImageQuality option
    optimizeOptions.image_compression_options.image_quality = 50
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

### Удаление неиспользуемых объектов

PDF‑документ иногда содержит PDF‑объекты, которые не ссылаются ни из какого другого объекта в документе. Это может произойти, например, когда страница удаляется из дерева страниц документа, но сам объект страницы не удаляется. Удаление этих объектов не делает документ недействительным, а лишь уменьшает его размер.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def removing_unused_objects(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Set RemoveUnusedObjects option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_objects = True

    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

### Удаление неиспользуемых потоков

Иногда документ содержит неиспользуемые потоки ресурсов. Эти потоки не являются “неиспользуемыми объектами”, потому что они находятся в ссылке из словаря ресурсов страницы. Таким образом, они не удаляются методом “remove unused objects”. Но эти потоки никогда не используются в содержимом страницы. Это может происходить в случаях, когда изображение было удалено со страницы, но не из ресурсов страницы. Кроме того, такая ситуация часто возникает, когда из документа извлекаются страницы, а страницы документа имеют “общие” ресурсы, то есть один и тот же объект Resources. Содержимое страниц анализируется, чтобы определить, используется поток ресурса или нет. Неиспользуемые потоки удаляются. Это иногда уменьшает размер документа. Использование этой техники похоже на предыдущий шаг:

```python
import aspose.pdf as ap
from os import path, stat
import sys


def removing_unused_streams(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Set RemoveUnusedStreams option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_streams = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

### Связывание дублирующих потоков

Некоторые документы могут содержать несколько одинаковых потоков ресурсов (например, изображения). Это может произойти, скажем, когда документ конкатенируется сам с собой. Выходной документ содержит две независимые копии одного и того же потока ресурса. Мы анализируем все потоки ресурсов и сравниваем их. Если потоки дублируются, они объединяются, то есть остаётся только одна копия. Ссылки изменяются соответствующим образом, а копии объекта удаляются. В некоторых случаях это помогает уменьшить размер документа.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def linking_duplicate_streams(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Set link_duplicate_streams option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.link_duplicate_streams = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

### Удаление внедренных шрифтов

Если документ использует встроенные шрифты, это означает, что все данные шрифта хранятся в документе. Преимущество заключается в том, что документ можно просматривать независимо от того, установлен ли шрифт на машине пользователя или нет. Но внедрение шрифтов делает документ больше. Метод удаления встроенных шрифтов удаляет все встроенные шрифты. Таким образом, размер документа уменьшается, но сам документ может стать нечитаемым, если нужный шрифт не установлен.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def unembed_fonts(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Set unembed_fonts option
    optimize_options = ap.optimization.OptimizationOptions()
    optimize_options.unembed_fonts = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimize_options)
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

Оптимизационные ресурсы применяют эти методы к документу. Если любой из этих методов будет применён, размер документа, скорее всего, уменьшится. Если ни один из этих методов не будет применён, размер документа не изменится, что очевидно.

## Дополнительные способы уменьшить размер PDF‑документа

### Удаление или уплощение аннотаций

Аннотации можно удалить, когда они не нужны. Когда они нужны, но не требуют дополнительного редактирования, их можно «сплющить». Оба этих метода уменьшат размер файла.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def flatten_annotations(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Flatten annotations
    for page in document.pages:
        for annotation in page.annotations:
            annotation.flatten()

    # Save updated document
    document.save(outfile)
```

### Удаление полей Form

Если PDF-документ содержит AcroForms, мы можем попытаться уменьшить размер файла, уплощением полей формы.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def flatten_forms(infile, outfile):
    # Load source PDF form
    doc = ap.Document(infile)

    # Flatten Forms
    if len(doc.form.fields) > 0:
        for item in doc.form.fields:
            item.flatten()

    # Save the updated document
    doc.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

### Конвертировать PDF из цветового пространства RGB в градации серого

PDF‑файл состоит из текста, изображений, вложений, аннотаций, графиков и других объектов. Вы можете столкнуться с требованием преобразовать PDF из цветового пространства RGB в градации серого, чтобы ускорить печать этих PDF‑файлов. Кроме того, при преобразовании файла в градации серого размер документа также уменьшается, но это может также привести к снижению качества документа. Эта функция в настоящее время поддерживается функцией Pre‑Flight в Adobe Acrobat, но при разговоре об автоматизации Office Aspose.PDF является окончательным решением, предоставляющим такие возможности для манипуляций с документами. Чтобы выполнить это требование, можно использовать следующий фрагмент кода.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def сonvert_PDF_from_RGB_colorspace_to_grayscale(infile, outfile):
    document = ap.Document(infile)
    strategy = ap.RgbToDeviceGrayConversionStrategy()
    for page in document.pages:
        # Convert the RGB colorspace image to GrayScale colorspace
        strategy.convert(page)

    # Save resultant file
    document.save(outfile)
```

### Сжатие FlateDecode

Aspose.PDF for Python via .NET предоставляет поддержку сжатия FlateDecode для функции оптимизации PDF. Ниже приведён фрагмент кода, показывающий, как использовать эту опцию в оптимизации для сохранения изображений с **FlateDecode** сжатием:

```python
import aspose.pdf as ap
from os import path, stat
import sys


def using_flatedecode_compression(infile, outfile):

    # Open Document
    doc = ap.Document(infile)
    # Initialize OptimizationOptions
    optimizationOptions = ap.optimization.OptimizationOptions()
    # To optimise image using FlateDecode Compression set optimization options to Flate
    optimizationOptions.image_compression_options.encoding = (
        ap.optimization.ImageEncoding.FLATE
    )
    # Set Optimization Options
    doc.optimize_resources(optimizationOptions)
    # Save Document
    doc.save(outfile)
```

## Связанные темы Document

- [Работа с PDF документами в Python](/pdf/ru/python-net/working-with-documents/)
- [Объединить PDF файлы в Python](/pdf/ru/python-net/merge-pdf-documents/)
- [Разделить PDF файлы в Python](/pdf/ru/python-net/split-document/)
- [Манипулировать PDF документами в Python](/pdf/ru/python-net/manipulate-pdf-document/)

