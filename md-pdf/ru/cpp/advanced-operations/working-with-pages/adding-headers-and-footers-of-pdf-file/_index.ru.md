---
title: Добавление заголовка и нижнего колонтитула в PDF
linktitle: Добавление заголовка и нижнего колонтитула в PDF
type: docs
weight: 70
url: /cpp/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF для C++ позволяет добавлять заголовки и нижние колонтитулы в ваш PDF-файл, используя класс TextStamp.
lastmod: "2021-12-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF для C++** позволяет добавлять заголовок и нижний колонтитул в ваш существующий PDF-файл. Вы можете добавить изображения или текст в документ PDF. Также попробуйте добавить различные заголовки в один PDF файл с использованием C++.

## Добавление текста в заголовок PDF файла

Вы можете использовать класс [TextStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text_stamp), чтобы добавить текст в заголовок PDF файла. TextStamp класс предоставляет свойства, необходимые для создания штампа на основе текста, такие как размер шрифта, стиль шрифта и цвет шрифта и т. д. Чтобы добавить текст в заголовок, необходимо создать объект Document и объект TextStamp с использованием необходимых свойств. После этого можно вызвать метод AddStamp страницы, чтобы добавить текст в заголовок PDF.

Необходимо установить свойство TopMargin таким образом, чтобы оно корректировало текст в области заголовка вашего PDF. Также необходимо установить HorizontalAlignment в Center и VerticalAlignment в Top.

Следующий фрагмент кода показывает, как добавить текст в заголовок PDF файла с помощью C++.

```cpp
void AddingTextInHeaderOfPdfFile() {
    String _dataDir("C:\\Samples\\");
    String inputFileName("TextinHeader.pdf");
    String outputFileName("TextinHeader_out.pdf");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Создать заголовок
    auto textStamp = MakeObject<TextStamp>(u"Header Text");

    // Установить свойства штампа
    textStamp->set_TopMargin(10);
    textStamp->set_HorizontalAlignment(HorizontalAlignment::Center);
    textStamp->set_VerticalAlignment(VerticalAlignment::Top);

    // Добавить заголовок на все страницы
    for(auto page : document->get_Pages())
    {
        page->AddStamp(textStamp);
    }

    // Сохранить обновленный документ
    document->Save(_dataDir + outputFileName);
}
```
## Добавление текста в нижний колонтитул PDF файла

Вы можете использовать класс TextStamp для добавления текста в нижний колонтитул PDF файла. Класс TextStamp предоставляет свойства, необходимые для создания штампа на основе текста, такие как размер шрифта, стиль шрифта и цвет шрифта и т. д. Для того чтобы добавить текст в нижний колонтитул, вам нужно создать объект Document и объект TextStamp, используя необходимые свойства. После этого вы можете вызвать метод AddStamp страницы, чтобы добавить текст в нижний колонтитул PDF.

{{% alert color="primary" %}}

Вам нужно установить свойство Bottom Margin таким образом, чтобы оно корректировало текст в области нижнего колонтитула вашего PDF. Также необходимо установить HorizontalAlignment в Center и VerticalAlignment в Bottom

{{% /alert %}}

Следующий фрагмент кода показывает, как добавить текст в нижний колонтитул PDF файла с помощью C++.

```cpp
void AddingTextInFooterOfPdfFile() {
    String _dataDir("C:\\Samples\\");
    String inputFileName("TextinFooter.pdf");
    String outputFileName("TextinFooter_out.pdf");

    // Open document
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Create footer
    auto textStamp = MakeObject<TextStamp>(u"Footer Text");

    // Set properties of the stamp
    textStamp->set_BottomMargin(10);
    textStamp->set_HorizontalAlignment(HorizontalAlignment::Center);
    textStamp->set_VerticalAlignment(HorizontalAlignment::Bottom);

    // Add footer on all pages
    for (auto page : document->get_Pages())
    {
        page->AddStamp(textStamp);
    }

    // Save updated document
    document->Save(_dataDir + outputFileName);
}
```

## Добавление изображения в заголовок PDF файла

Вы можете использовать класс [ImageStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_stamp), чтобы добавить изображение в заголовок PDF файла. Класс Image Stamp предоставляет свойства, необходимые для создания штампа на основе изображения, такие как размер шрифта, стиль шрифта и цвет шрифта и т. д. Для того чтобы добавить изображение в заголовок, вам нужно создать объект Document и объект Image Stamp, используя необходимые свойства. После этого вы можете вызвать метод AddStamp страницы, чтобы добавить изображение в заголовок PDF.

Следующий фрагмент кода показывает, как добавить изображение в заголовок PDF файла с помощью C++.

```cpp
void AddingImageInHeaderOfPdfFile() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("ImageinHeader.pdf");
    String outputFileName("ImageinHeader_out.pdf");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Создать заголовок
    auto imageStamp = MakeObject<ImageStamp>(_dataDir + u"aspose-logo.jpg");

    // Установить свойства штампа
    imageStamp->set_TopMargin(10);
    imageStamp->set_HorizontalAlignment(HorizontalAlignment::Center);
    imageStamp->set_VerticalAlignment (VerticalAlignment::Top);

    // Добавить заголовок на все страницы
    for(auto page : document->get_Pages())
    {
        page->AddStamp(imageStamp);
    }

    // Сохранить обновленный документ
    document->Save(_dataDir + outputFileName);
}
```

## Добавление изображения в нижний колонтитул PDF-файла

Вы можете использовать класс Image Stamp для добавления изображения в нижний колонтитул PDF-файла. Класс Image Stamp предоставляет свойства, необходимые для создания штампа на основе изображения, такие как размер шрифта, стиль шрифта и цвет шрифта и т.д. Для того чтобы добавить изображение в нижний колонтитул, вам нужно создать объект Document и объект Image Stamp с использованием необходимых свойств. После этого вы можете вызвать метод AddStamp страницы, чтобы добавить изображение в нижний колонтитул PDF.

Вам необходимо установить свойство [BottomMargin](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.stamp#aeab91949cf3eb473018b31a74fed7173) таким образом, чтобы оно регулировало изображение в области нижнего колонтитула вашего PDF. Вам также нужно установить [HorizontalAlignment](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#aefec9c0bf30ee5e6fb2640e69aed6cd9) в `Center` и [VerticalAlignment](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#ad4956d03096fc515eaa34319a6bf636a) в `Bottom`.

Следующий фрагмент кода показывает, как добавить изображение в нижний колонтитул PDF-файла с использованием C++.

```cpp
void AddingImageInFooterOfPdfFile() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("ImageinFooter.pdf");
    String outputFileName("ImageinFooter_out.pdf");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Создать заголовок
    auto imageStamp = MakeObject<ImageStamp>(_dataDir + u"aspose-logo.jpg");

    // Установить свойства штампа
    imageStamp->set_TopMargin(10);
    imageStamp->set_HorizontalAlignment(HorizontalAlignment::Center);
    imageStamp->set_VerticalAlignment(VerticalAlignment::Top);

    // Добавить заголовок на все страницы
    for (auto page : document->get_Pages())
    {
        page->AddStamp(imageStamp);
    }

    // Сохранить обновленный документ
    document->Save(_dataDir + outputFileName);
}
```

## Добавление различных заголовков в один PDF файл

Мы знаем, что можем добавить TextStamp в раздел Заголовок/Нижний колонтитул документа, используя свойства TopMargin или Bottom Margin, но иногда может возникнуть необходимость добавить несколько заголовков/нижних колонтитулов в один PDF документ. **Aspose.PDF for C++** объясняет, как это сделать.

Для выполнения этого требования мы создадим отдельные объекты TextStamp (количество объектов зависит от количества требуемых заголовков/подвалов) и добавим их в PDF-документ. Мы также можем указать различную информацию о форматировании для каждого объекта штампа. В следующем примере мы создали объект Document и три объекта TextStamp, а затем использовали метод [AddStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#a3b998038dedf5266b4d60586b1b53d02) класса Page для добавления текста в раздел заголовка PDF. Следующий фрагмент кода показывает, как добавить изображение в подвал PDF-файла с помощью Aspose.PDF для C++.

```cpp
void AddingDifferentHeadersInOnePDFFile()
{
    String _dataDir("C:\\Samples\\");
    String inputFileName("multiheader.pdf");
    String outputFileName("multiheader_out.pdf");

    // Открыть исходный документ
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Создать три штампа
    auto stamp1 = MakeObject<TextStamp>("Header 1");
    auto stamp2 = MakeObject<TextStamp>("Header 2");
    auto stamp3 = MakeObject<TextStamp>("Header 3");

    // Установить выравнивание штампа (разместить штамп вверху страницы, центрировано по горизонтали)
    stamp1->set_VerticalAlignment(VerticalAlignment::Top);
    stamp1->set_HorizontalAlignment(HorizontalAlignment::Center);
    // Указать стиль шрифта как Bold
    stamp1->get_TextState()->set_FontStyle(FontStyles::Bold);
    // Установить информацию о цвете текста как красный
    stamp1->get_TextState()->set_ForegroundColor(Color::get_Red());
    // Указать размер шрифта как 14
    stamp1->get_TextState()->set_FontSize(14);

    // Теперь нам нужно установить вертикальное выравнивание второго объекта штампа как Top
    stamp2->set_VerticalAlignment(VerticalAlignment::Top);
    // Установить информацию о горизонтальном выравнивании штампа как центрированную
    stamp2->set_HorizontalAlignment (HorizontalAlignment::Center);
    // Установить коэффициент масштабирования для объекта штампа
    stamp2->set_Zoom(10);

    // Установить форматирование третьего объекта штампа
    // Указать информацию о вертикальном выравнивании объекта штампа как TOP
    stamp3->set_VerticalAlignment(VerticalAlignment::Top);
    // Установить информацию о горизонтальном выравнивании объекта штампа как центрированную
    stamp3->set_HorizontalAlignment(HorizontalAlignment::Center);
    // Установить угол поворота для объекта штампа
    stamp3->set_RotateAngle(35);
    // Установить розовый как цвет фона для штампа
    stamp3->get_TextState()->set_BackgroundColor(Color::get_Pink());
    // Изменить информацию о шрифте штампа на Verdana
    stamp3->get_TextState()->set_Font(FontRepository::FindFont(u"Verdana"));

    // Первый штамп добавляется на первую страницу;
    document->get_Pages()->idx_get(1)->AddStamp(stamp1);
    // Второй штамп добавляется на вторую страницу;
    document->get_Pages()->idx_get(2)->AddStamp(stamp2);
    // Третий штамп добавляется на третью страницу.
    document->get_Pages()->idx_get(3)->AddStamp(stamp3);

    // Сохранить обновленный документ
    document->Save(_dataDir + outputFileName);
}
```