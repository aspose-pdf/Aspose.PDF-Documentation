---
title: Optimize PDF using C++
linktitle: Optimize PDF
type: docs
weight: 30
url: /ru/cpp/optimize-pdf/
description: Оптимизация PDF файла, сжатие всех изображений, уменьшение размера PDF, отключение встроенных шрифтов, включение повторного использования содержимого страницы, удаление или уплощение аннотаций с помощью C++.
lastmod: "2021-11-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Прежде всего, любая оптимизация PDF, которую вы делаете, предназначена для пользователя. В PDF-формате оптимизация для пользователя в основном связана с уменьшением размера ваших PDF-документов, чтобы увеличить скорость их загрузки. Это самая популярная задача.
Мы можем использовать несколько техник для оптимизации PDF, но наиболее важные из них:

- Оптимизация содержимого страницы для онлайн-просмотра
- Уменьшение или сжатие всех изображений
- Включение повторного использования содержимого страницы
- Объединение дублирующихся потоков
- Отключение встроенных шрифтов
- Удаление неиспользуемых объектов
- Удаление полей формы с уплощением
- Удаление или уплощение аннотаций

## Оптимизация PDF-документа для Интернета

Когда вы сталкиваетесь с задачей оптимизации содержимого вашего PDF-документа для лучшего ранжирования в поисковых системах, Aspose.PDF для C++ имеет решение.

1. Откройте входной документ в объекте [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Используйте метод [Optimize](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a04d95824c334f5e543c13f69a19d9cda).
1. Сохраните оптимизированный документ, используя метод Save.

Следующий фрагмент кода показывает, как оптимизировать PDF-документ для веба.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
//Optimize PDF Document for the Web
void OptimizeForWeb() {
    // String for path name
    String _dataDir("C:\\Samples\\");

    // String for input file name
    String outfilename("OptimizeDocument_out.pdf");

    // Open document
    auto document = MakeObject<Document>();

    // Make some operations (add pages, images, etc) 
    // ...

    // Optimize for web
    document->Optimize();

    // Save output document
    document->Save(_dataDir + outfilename);
}
```

## Уменьшение размера PDF

Метод [OptimizeResources()](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#aea33aac69a42423efb82bcdb359f2ec6) позволяет уменьшить размер документа, устраняя ненужную информацию. По умолчанию этот метод работает следующим образом:

- Ресурсы, которые не используются на страницах документа, удаляются
- Одинаковые ресурсы объединяются в один объект
- Неиспользуемые объекты удаляются

Пример приведен ниже. Однако, обратите внимание, что этот метод не может гарантировать уменьшение размера документа.

```cpp
void ReduceSizePDF() {

    // Строка для имени пути
    String _dataDir("C:\\Samples\\");

    // Строка для имени выходного файла
    String outfilename("ShrinkDocument_out.pdf");

    // Открыть документ
    auto document = MakeObject<Document>();
    // Выполнить некоторые операции (добавить страницы, изображения и т.д.)
    // ...

    // Оптимизировать PDF документ. Однако, обратите внимание, что этот метод не может гарантировать уменьшение размера документа
    document->OptimizeResources();

    // Сохранить выходной документ
    document->Save(_dataDir + outfilename);
}
```

## Управление стратегией оптимизации

Мы также можем настроить стратегию оптимизации. В настоящее время метод [OptimizeResources()](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#aea33aac69a42423efb82bcdb359f2ec6) использует 5 техник. Эти техники могут быть применены с помощью метода OptimizeResources() с параметром [OptimizationOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document.optimization_options/).

### Уменьшение или сжатие всех изображений

Чтобы оптимизировать изображения в вашем PDF документе, мы будем использовать [Aspose.Pdf.Optimization](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.optimization).
Чтобы решить проблему с оптимизацией изображений, у нас есть следующие варианты: уменьшить качество изображения и/или изменить их разрешение. В любом случае, следует применять [ImageCompressionOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.image_compression_options/). В следующем примере мы уменьшаем изображения, снижая [ImageQuality](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.image_compression_options#a92ee855b042a6b310984b4966ea7154e) до 50.

```cpp
void CompressImage() {
    // Строка для имени пути
    String _dataDir("C:\\Samples\\");

    // Строка для имени входного файла
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Инициализировать параметры оптимизации
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // Установить параметр CompressImages
    optimizationOptions->get_ImageCompressionOptions()->set_CompressImages(true);
    // Установить параметр ImageQuality
    optimizationOptions->get_ImageCompressionOptions()->set_ImageQuality(50);

    // Оптимизировать PDF-документ, используя параметры оптимизации
    document->OptimizeResources(optimizationOptions); 
    // Сохранить обновленный документ
    document->Save(_dataDir + outfilename);
}
```
Чтобы установить изображение с более низким разрешением, установите [ResizeImages](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.image_compression_options#a0e5aad7e140ee380c09ebbb8a5238ff6) в значение true и [MaxResolution](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.image_compression_options#a05a4d1ace23ef074b3dc203cb213755e) на соответствующее значение.

```cpp
void ResizeImagesWithLowerResolution() {
    // Строка для имени пути
    String _dataDir("C:\\Samples\\");

    // Строка для имени входного файла
    String infilename("ResizeImage.pdf");
    String outfilename("ResizeImages_out.pdf");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Инициализировать OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // Установить опцию CompressImages
    optimizationOptions->get_ImageCompressionOptions()->set_CompressImages(true);
    // Установить опцию ImageQuality
    optimizationOptions->get_ImageCompressionOptions()->set_ImageQuality(75);

    // Установить опцию ResizeImage
    optimizationOptions->get_ImageCompressionOptions()->set_ResizeImages(true);
    // Установить опцию MaxResolution
    optimizationOptions->get_ImageCompressionOptions()->set_MaxResolution(300);

    // Оптимизировать PDF-документ с использованием OptimizationOptions
    document->OptimizeResources(optimizationOptions);
    // Сохранить обновленный документ
    document->Save(_dataDir + outfilename);
}
```

Aspose.PDF for C++ также предлагает вам контроль над настройками времени выполнения. Сегодня мы можем использовать два алгоритма - стандартный и быстрый. Чтобы контролировать время выполнения, мы должны установить свойство [Version](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.image_compression_options#aa2f1d93725ce56f8fabe692152bbf3a4).

Следующий фрагмент демонстрирует быстрый алгоритм:

```cpp
void ResizeImagesWithLowerResolutionFast() {
    auto time = System::DateTime::get_Now().get_Ticks();
    // Строка для имени пути
    String _dataDir("C:\\Samples\\");

    // Строка для имени входного файла
    String infilename("ResizeImage.pdf");
    String outfilename("ResizeImages_out.pdf");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Инициализировать OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // Установить опцию CompressImages
    optimizationOptions->get_ImageCompressionOptions()->set_CompressImages(true);
    // Установить опцию ImageQuality
    optimizationOptions->get_ImageCompressionOptions()->set_ImageQuality(75);

    // Установить опцию ResizeImage
    optimizationOptions->get_ImageCompressionOptions()->set_ResizeImages(true);
    // Установить версию сжатия изображений на быструю
    optimizationOptions->get_ImageCompressionOptions()->set_Version (Aspose::Pdf::Optimization::ImageCompressionVersion::Fast);

    // Оптимизировать PDF-документ с использованием OptimizationOptions
    document->OptimizeResources(optimizationOptions);
    // Сохранить обновленный документ
    document->Save(_dataDir + outfilename);
    std::cout << "Ticks: " << System::DateTime::get_Now().get_Ticks() - time << std::endl;
}
```

### Удаление неиспользуемых объектов

Иногда вам может понадобиться удалить некоторые неиспользуемые объекты из вашего PDF-документа, которые не ссылаются на страницах. Это может произойти, например, когда страница удалена из дерева страниц документа, но сам объект страницы не удален. Удаление этих объектов не делает документ недействительным, а скорее уменьшает его. Проверьте следующий фрагмент кода:

```cpp
void RemovingUnusedObject() { 
    // Строка для имени пути
    String _dataDir("C:\\Samples\\");

    // Строка для имени входного файла
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Инициализировать OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // Установить опцию RemoveUnusedObjects
    optimizationOptions->set_RemoveUnusedObjects(true);

    // Оптимизировать PDF-документ, используя OptimizationOptions
    document->OptimizeResources(optimizationOptions);

    // Сохранить обновленный документ
    document->Save(_dataDir + outfilename); 
}
```

### Удаление неиспользуемых потоков

Иногда документ содержит неиспользуемые потоки ресурсов. Эти потоки не являются «неиспользуемыми объектами», потому что они ссылаются из словаря ресурсов страницы. Таким образом, они не удаляются методом «удаление неиспользуемых объектов». Но эти потоки никогда не используются в содержимом страницы. Это может происходить в случаях, когда изображение было удалено со страницы, но не из ресурсов страницы. Также эта ситуация часто возникает, когда страницы извлекаются из документа, и страницы документа имеют «общие» ресурсы, то есть один и тот же объект ресурсов. Содержимое страницы анализируется для определения, используется ли поток ресурса или нет. Неиспользуемые потоки удаляются. Иногда это уменьшает размер документа. Использование этой техники похоже на предыдущий шаг:

```cpp
void RemovingUnusedStreams() { 
    // Строка для имени пути
    String _dataDir("C:\\Samples\\");

    // Строка для имени входного файла
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // Открыть документ
    auto document = MakeObject<Document>();

    // Инициализировать OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // Установить опцию RemoveUsedStreams
    optimizationOptions->set_RemoveUnusedStreams(true);

    // Оптимизировать PDF документ с использованием OptimizationOptions
    document->OptimizeResources(optimizationOptions);

    // Сохранить обновленный документ
    document->Save(_dataDir + outfilename); 
}
```

### Связывание Дублирующихся Потоков

Некоторые документы могут содержать несколько дублирующихся потоков ресурсов (например, изображения). Это может произойти, например, когда документ соединяется сам с собой. Итоговый документ содержит две независимые копии одного и того же потока ресурсов. Мы анализируем все потоки ресурсов и сравниваем их. Если потоки дублируются, они объединяются, то есть остается только одна копия. Ссылки изменяются соответствующим образом, и копии объекта удаляются. В некоторых случаях это помогает уменьшить размер документа.

```cpp
void LinkingDuplicateStreams() { 
    // Строка для имени пути
    String _dataDir("C:\\Samples\\");

    // Строка для имени входного файла
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Инициализация OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // Установить опцию LinkDuplicateStreams
    optimizationOptions->set_LinkDuplcateStreams(true);

    // Оптимизация PDF документа с использованием OptimizationOptions
    document->OptimizeResources(optimizationOptions);

    // Сохранить обновленный документ
    document->Save(_dataDir + outfilename); 
}
```

Кроме того, мы можем использовать настройки [AllowReusePageContent](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.optimization_options#aedaab36eaf8ed5059a2b1e11275bf6d8). Если это свойство установлено в true, содержимое страницы будет повторно использоваться при оптимизации документа для идентичных страниц.

### Удаление встраивания шрифтов

Когда вы создаете PDF-версию вашего личного файла дизайна, копия всех необходимых шрифтов добавляется в сам PDF-файл. Это и есть встраивание. Независимо от того, где этот PDF будет открыт, будь то на вашем компьютере, компьютере вашего друга или компьютере вашего провайдера печати, все правильные шрифты будут там и будут отображаться правильно.

Но если документ использует встроенные шрифты, это означает, что все данные шрифта хранятся в документе. Преимущество в том, что документ можно просмотреть, независимо от того, установлен ли шрифт на компьютере пользователя или нет. Но встраивание шрифтов делает документ больше. Метод удаления встраивания шрифтов удаляет все встроенные шрифты. Таким образом, размер документа уменьшается, но сам документ может стать нечитаемым, если правильный шрифт не установлен.

```cpp
void UnembedFonts() {
    // Строка для имени пути
    String _dataDir("C:\\Samples\\");

    // Строка для имени входного файла
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir+infilename);

    // Инициализация OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // Установить опцию AllowReusePageContent
    optimizationOptions->set_UnembedFonts(true);

    // Оптимизировать PDF-документ с использованием OptimizationOptions
    document->OptimizeResources(optimizationOptions);

    // Сохранить обновленный документ
    document->Save(_dataDir + outfilename);
}
```

Оптимизационные ресурсы применяют эти методы к документу. Если любой из этих методов применен, размер документа, скорее всего, уменьшится. Если ни один из этих методов не применен, размер документа не изменится, что очевидно.

## Дополнительные способы уменьшить размер PDF-документа

### Удаление или сглаживание аннотаций

Наличие аннотаций в вашем PDF-документе естественным образом увеличивает его размер. Аннотации могут быть удалены, когда они не нужны. Когда они нужны, но не требуют дополнительного редактирования, их можно сгладить. Оба этих метода уменьшат размер файла.

```cpp
void FlatteningAnnotation() {
    // Строка для имени пути
    String _dataDir("C:\\Samples\\");

    // Строка для имени входного файла
    String infilename("OptimizeDocument.pdf");
    // Строка для имени выходного файла
    String outfilename("OptimizeDocument_out.pdf");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Сгладить аннотации
    for(auto page : document->get_Pages())
    {
        for(auto annotation : page->get_Annotations())
        {
        annotation->Flatten();
        }
    }
    // Сохранить обновленный документ
    document->Save(_dataDir + outfilename);
}
```


### Удаление полей формы

Удаление форм из вашего PDF также оптимизирует ваш документ.
Если PDF-документ содержит AcroForms, мы можем попытаться уменьшить размер файла, уплощая поля формы.

```cpp
void FlatteningFormFields() {
    // String for path name
    String _dataDir("C:\\Samples\\");

    // String for input file name
    String infilename("OptimizeFormField.pdf");
    // String for output file name
    String outfilename("OptimizeFormField_out.pdf");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Flatten form fields
    // Flatten Forms
    if (document->get_Form()->get_Fields()->get_Count() > 0)
    {
        for(auto item : document->get_Form()->get_Fields())
        {
            item->Flatten();
        }
    }
    // Save updated document
    document->Save(_dataDir + outfilename);
}
```

### Преобразование PDF из цветового пространства RGB в градации серого

PDF-файл включает текст, изображения, вложения, аннотации, графики и другие объекты.
``` Вы можете столкнуться с требованием конвертировать PDF из цветового пространства RGB в градации серого, чтобы ускорить печать этих PDF-файлов. Также, когда файл конвертируется в градации серого, размер документа также уменьшается, но это может также привести к снижению качества документа. Эта функция в настоящее время поддерживается функцией Pre-Flight в Adobe Acrobat, но когда речь идет об автоматизации Office, Aspose.PDF является идеальным решением для предоставления таких возможностей для манипуляций с документами. Для выполнения этого требования можно использовать следующий фрагмент кода.

```cpp
void ConvertPDFfromColorspaceToGrayscale() {
    // Строка для имени пути
    String _dataDir("C:\\Samples\\");

    // Строка для имени входного файла
    String infilename("OptimizeDocument.pdf");
    // Строка для имени выходного файла
    String outfilename("Test-gray_out.pdf");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto strategy = MakeObject<Aspose::Pdf::RgbToDeviceGrayConversionStrategy>();
    for (int idxPage = 1; idxPage <= document->get_Pages()->get_Count(); idxPage++)
    {
        // Получить экземпляр конкретной страницы внутри PDF
        auto page = document->get_Pages()->idx_get(idxPage);
        // Конвертировать изображение из цветового пространства RGB в цветовое пространство градаций серого
        strategy->Convert(page);
    }
    // Сохранить полученный файл
    document->Save(_dataDir + outfilename); 
}
```
### FlateDecode Сжатие

Aspose.PDF для C++ поддерживает сжатие FlateDecode для функциональности оптимизации PDF.
Чтобы оптимизировать изображение с использованием сжатия FlateDecode, установите параметры оптимизации на Flate.
Следующий фрагмент кода показывает, как использовать эту опцию в оптимизации для хранения изображений с использованием сжатия **FlateDecode**:

```cpp
void FlatDecodeCompression() {
 // Строка для имени пути
 String _dataDir("C:\\Samples\\");

 // Строка для имени входного файла
 String infilename("FlateDecodeCompression.pdf");
 // Строка для имени выходного файла
 String outfilename("FlateDecodeCompression_out.pdf");

 // Открыть документ
 auto document = MakeObject<Document>(_dataDir + infilename);

 // Инициализация OptimizationOptions
 auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

 // Чтобы оптимизировать изображение с использованием сжатия FlateDecode, установите параметры оптимизации на Flate
 optimizationOptions->get_ImageCompressionOptions()->set_Encoding(Aspose::Pdf::Optimization::ImageEncoding::Flate);

 // Оптимизировать PDF документ с использованием OptimizationOptions
 document->OptimizeResources(optimizationOptions);

 // Сохранить обновленный документ
 document->Save(_dataDir + outfilename);
}
```

### **Сохранение изображения в XImageCollection**

Aspose.PDF для C++ предоставляет возможность сохранять новые изображения в [XImageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.x_image_collection) с использованием сжатия FlateDecode. Чтобы включить эту опцию, вы можете использовать флаг **ImageFilterType.Flate**.
Следующий фрагмент кода показывает, как использовать эту функциональность:

```cpp
void StoreImageInXImageCollection() {

 // Строка для имени пути
 String _dataDir("C:\\Samples\\");

 // Строка для имени выходного файла
 String outfilename("FlateDecodeCompression_out.pdf");

 // Открыть документ
 auto document = MakeObject<Document>();
 
 auto page = document->get_Pages()->Add();
 
 auto imageStream = System::IO::File::OpenRead(_dataDir + u"aspose-logo.jpg");
 
 page->get_Resources()->get_Images()->Add(imageStream, Aspose::Pdf::ImageFilterType::Flate);
 
 auto ximage = page->get_Resources()->get_Images()->idx_get(page->get_Resources()->get_Images()->get_Count());

 page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GSave>());

 // Установить координаты
 int lowerLeftX = 0;
 int lowerLeftY = 0;
 int upperRightX = 600;
 int upperRightY = 600;
 
 auto rectangle = MakeObject<Rectangle>(lowerLeftX, lowerLeftY, upperRightX, upperRightY);

 auto matrix = MakeObject<Matrix>(new double[] {rectangle->get_URX() - rectangle->get_LLX(), 0, 0, rectangle->get_URY() - rectangle->get_LLY(), rectangle->get_LLX(), rectangle->get_LLY()});
 // Использование оператора ConcatenateMatrix (конкатенация матрицы): определяет, как изображение должно быть размещено
 page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(matrix));
 page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::Do>(ximage->get_Name()));
 page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

 document->Save(_dataDir + outfilename);
}
```