---
title: Форматирование PDF документа с использованием C++
linktitle: Форматирование PDF документа
type: docs
weight: 20
url: /ru/cpp/formatting-pdf-document/
description: Создание и форматирование PDF документа с помощью Aspose.PDF для C++. Используйте следующий фрагмент кода для решения ваших задач.
lastmod: "2021-11-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Форматирование PDF документа

### Получение свойств окна документа и отображения страниц

Эта тема поможет вам понять, как получить свойства окна документа, приложения просмотра, и как отображаются страницы. Чтобы установить эти свойства, откройте PDF файл с помощью класса [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). Теперь вы можете установить свойства объекта Document, такие как:

- CenterWindow – Центрировать окно документа на экране. По умолчанию: false.
- Direction – Порядок чтения. Определяет, как страницы расположены при отображении рядом друг с другом. По умолчанию: слева направо.
- DisplayDocTitle – Отображать заголовок документа в строке заголовка окна документа. - HideMenuBar – Скрыть или отобразить строку меню окна документа. По умолчанию: false (строка меню отображается).
- HideToolBar – Скрыть или отобразить панель инструментов окна документа. По умолчанию: false (панель инструментов отображается).
- HideWindowUI – Скрыть или отобразить элементы окна документа, такие как полосы прокрутки. По умолчанию: false (элементы пользовательского интерфейса отображаются).
- NonFullScreenPageMode – Как документ отображается, когда он не в полноэкранном режиме.
- PageLayout – Макет страницы.
- PageMode – Как документ отображается при первом открытии. Опции включают показ эскизов, полноэкранный режим, показ панели вложений.

Следующий фрагмент кода показывает, как получить свойства, используя класс [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).

```cpp
void GetDocumentWindowAndPageDisplayProperties()
{
    // Строка для имени пути.
    String _dataDir("C:\\Samples\\");
    // Строка для имени файла.
    String inputFileName("sample.pdf");

    auto document = MakeObject<Document>(inputFileName);

    // Получить различные свойства документа
    // Позиция окна документа - По умолчанию: false
    Console::WriteLine(u"CenterWindow : {0}", document->get_CenterWindow());

    // Преобладающий порядок чтения; определяет позицию страницы
    // При отображении рядом - По умолчанию: L2R
    Console::WriteLine(u"Direction : {0}", document->get_Direction());

    // Должна ли строка заголовка окна отображать заголовок документа
    // Если false, строка заголовка отображает имя PDF файла - По умолчанию: false
    Console::WriteLine(u"DisplayDocTitle : {0}", document->get_DisplayDocTitle());

    // Следует ли изменять размер окна документа, чтобы он соответствовал размеру
    // Первой отображаемой страницы - По умолчанию: false
    Console::WriteLine(u"FitWindow : {0}", document->get_FitWindow());

    // Следует ли скрыть строку меню приложения для просмотра - По умолчанию: false
    Console::WriteLine(u"HideMenuBar : {0}", document->get_HideMenubar());

    // Следует ли скрыть панель инструментов приложения для просмотра - По умолчанию: false
    Console::WriteLine(u"HideToolBar : {0}", document->get_HideToolBar());

    // Следует ли скрыть элементы пользовательского интерфейса, такие как полосы прокрутки
    // И оставить только содержимое страницы отображаемым - По умолчанию: false
    Console::WriteLine(u"HideWindowUI : {0}", document->get_HideWindowUI());

    // Режим страницы документа. Как отображать документ при выходе из полноэкранного режима.
    Console::WriteLine(u"NonFullScreenPageMode : {0}", document->get_NonFullScreenPageMode());

    // Макет страницы, т.е. одна страница, одна колонка
    Console::WriteLine(u"PageLayout : {0}", document->get_PageLayout());

    // Как документ должен отображаться при открытии
    // Т.е. показать эскизы, полноэкранный режим, показать панель вложений
    Console::WriteLine(u"pageMode : {0}", document->get_PageMode());
}
```
### Установить свойства окна документа и отображения страницы

Эта тема объясняет, как установить свойства окна документа, приложения просмотра и отображения страницы. Чтобы установить эти различные свойства:

1. Откройте PDF-файл, используя класс [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Установите различные свойства документа:

- CenterWindow
- Direction
- DisplayDocTitle
- FitWindow
- HideMenuBar
- HideToolBar
- HideWindowUI
- NonFullScreenPageMode
- PageLayout
- PageMode

1. [Сохраните](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/#ac082fe8e67b25685fc51d33e804269fa) обновленный PDF-файл, используя метод Save.

Доступные свойства:

- CenterWindow
- Direction
- DisplayDocTitle
- FitWindow
- HideMenuBar
- HideToolBar
- HideWindowUI
- NonFullScreenPageMode
- PageLayout
- PageMode

Каждое из них используется и описано в коде ниже. Следующий - фрагмент кода показывает, как установить свойства, используя класс [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).

```cpp
void SetDocumentWindowAndPageDisplayProperties()
{
    // Строка для имени пути.
    String _dataDir("C:\\Samples\\");
    // Строка для имени файла.
    String inputFileName("sample.pdf");
    String outputFileName("sample_page_display_properties.pdf");

    auto document = MakeObject<Document>(inputFileName);

    // Установить различные свойства документа
    // Указать позиционирование окна документа - По умолчанию: false
    document->set_CenterWindow(true);

    // Преобладающий порядок чтения; определяет позицию страницы
    // При отображении бок о бок - По умолчанию: L2R
    document->set_Direction(Direction::R2L);

    // Указать, должен ли заголовок окна отображать заголовок документа
    // Если false, заголовок окна отображает имя файла PDF - По умолчанию: false
    document->set_DisplayDocTitle(true);

    // Указать, следует ли изменить размер окна документа, чтобы он соответствовал размеру
    // Первой отображаемой страницы - По умолчанию: false
    document->set_FitWindow(true);

    // Указать, следует ли скрыть строку меню приложения просмотра - По умолчанию: false
    document->set_HideMenubar(true);

    // Указать, следует ли скрыть панель инструментов приложения просмотра - По умолчанию: false
    document->set_HideToolBar(true);

    // Указать, следует ли скрыть элементы интерфейса, такие как полосы прокрутки
    // И оставить только содержимое страницы - По умолчанию: false
    document->set_HideWindowUI(true);

    // Режим страницы документа. укажите, как отображать документ при выходе из полноэкранного режима.
    document->set_NonFullScreenPageMode(PageMode::UseOC);

    // Указать макет страницы, т.е. одна страница, одна колонка
    document->set_PageLayout(PageLayout::TwoColumnLeft);

    // Указать, как документ должен отображаться при открытии
    // Т.е. показывать эскизы, полноэкранный режим, показывать панель вложений
    document->set_PageMode(PageMode::UseThumbs);

    // Сохранить обновленный PDF файл
    document->Save(_dataDir + outputFileName);
}
```
### Встраивание шрифтов в существующий PDF файл

PDF-ридеры поддерживают [основные 14 шрифтов](https://en.wikipedia.org/wiki/PDF#Text), чтобы документы отображались одинаково независимо от платформы, на которой они открываются. Когда PDF содержит шрифт, который не входит в число 14 основных шрифтов, встраивайте шрифт в PDF файл, чтобы избежать замены шрифта.

Aspose.PDF для C++ поддерживает встраивание шрифтов в существующие PDF файлы. Вы можете встроить полный шрифт или подмножество шрифта. Чтобы встроить шрифт, откройте PDF файл, используя класс [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). Затем используйте класс [Aspose.Pdf.Text.Font](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.font), чтобы встроить шрифт в PDF файл. Чтобы встроить полный шрифт, используйте свойство IsEmbeded класса Font; чтобы использовать подмножество шрифта, используйте свойство IsSubset.

{{% alert color="primary" %}}

Подмножество шрифта встраивает только те символы, которые используются, и полезно в случаях, когда шрифты используются для коротких предложений или слоганов, например, когда корпоративный шрифт используется для логотипа, но не для основного текста.  Использование подмножества уменьшает размер выходного PDF-файла. Однако, если для основного текста используется пользовательский шрифт, вложите его полностью.

{{% /alert %}}

Следующий фрагмент кода показывает, как встроить шрифт в PDF-файл.

### Встраивание стандартных шрифтов Type 1

Существуют PDF-документы, использующие шрифты из специального набора, называемые "Стандартными шрифтами Type 1". Этот набор включает 14 шрифтов, и для встраивания этого типа шрифтов необходимо использовать специальные флаги, т.е. [Aspose.Pdf.Document.EmbedStandardFonts](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a8f1a88eef22e05ee9ee22a79db9cb9f6).

Ниже приведен фрагмент кода, который можно использовать для получения документа со всеми встроенными шрифтами, включая стандартные шрифты Type 1:

```cpp
void EmbeddingStandardType1Fonts()
{

    // Строка для имени пути.
    String _dataDir("C:\\Samples\\");
    // Строка для имени файла.
    String inputFileName("sample.pdf");
    String outputFileName("embedded-fonts-updated_out.pdf");

    auto document = MakeObject<Document>(inputFileName);

    // Установить свойство EmbedStandardFonts для документа
    document->set_EmbedStandardFonts(true);
    for (auto page : document->get_Pages())
    {
        auto fonts = page->get_Resources()->get_Fonts();
        if (fonts != nullptr)
        {
            for (auto pageFont : fonts)
            {
                // Проверить, встроен ли шрифт
                if (!pageFont->get_IsEmbedded())
                {
                    pageFont->set_IsEmbedded(true);
                }
            }
        }
    }
    document->Save(_dataDir + outputFileName);
}
```
### Встраивание шрифтов при создании PDF

Если вам нужно использовать любой шрифт, кроме 14 основных шрифтов, поддерживаемых Adobe Reader, вы должны встроить описание шрифта при создании Pdf файла. Если информация о шрифте не встроена, Adobe Reader возьмёт её из операционной системы, если она установлена в системе, или создаст заменяющий шрифт в соответствии с дескриптором шрифта в Pdf.

>Обратите внимание, что встроенный шрифт должен быть установлен на хост-машине, т.е. в случае следующего кода шрифт 'Univers Condensed' установлен в системе.

Мы используем свойство IsEmbedded класса Font для встраивания информации о шрифте в Pdf файл. Установка значения этого свойства в ‘True’ будет встраивать полный файл шрифта в Pdf, зная, что это увеличит размер файла Pdf. Ниже приведён фрагмент кода, который можно использовать для встраивания информации о шрифте в Pdf.

```cpp
void EmbeddingFontsWhileCreatingPDF()
{
    // Строка для имени пути.
    String _dataDir("C:\\Samples\\");
    // Строка для имени файла.
    String inputFileName("sample.pdf");
    String outputFileName("EmbedFontWhileDocCreation_out.pdf");

    auto document = MakeObject<Document>(inputFileName);

    // Создать раздел в объекте Pdf
    auto page = document->get_Pages()->Add();

    auto fragment = MakeObject<TextFragment>("");
    auto segment = MakeObject <TextSegment>(u"This is a sample text using Custom font.");

    auto ts = MakeObject<TextState>();

    ts->set_Font(FontRepository::FindFont(u"Arial"));
    ts->get_Font()->set_IsEmbedded(true);
    segment->set_TextState(ts);
    fragment->get_Segments()->Add(segment);
    page->get_Paragraphs()->Add(fragment);

    // Сохранить PDF документ
    document->Save(_dataDir);
}
```

### Установить имя шрифта по умолчанию при сохранении PDF

Когда в PDF-документе содержатся шрифты, которые недоступны в самом документе и на устройстве, API заменяет эти шрифты на шрифт по умолчанию. Когда шрифт доступен (установлен на устройстве или встроен в документ), выходной PDF должен иметь тот же шрифт (не должен заменяться на шрифт по умолчанию). Значение шрифта по умолчанию должно содержать имя шрифта (а не путь к файлам шрифта). Apose.PDF для C++ реализовал возможность установки имени шрифта по умолчанию при сохранении документа как PDF. Следующий фрагмент кода можно использовать для установки шрифта по умолчанию:

```cpp
void SetDefaultFontNameWhileSavingPDF()
{
    // Строка для пути.
    String _dataDir("C:\\Samples\\");
    // Строка для имени файла.
    String inputFileName("sample.pdf");
    String outputFileName("output_out.pdf");
    String newName("Arial");

    auto document = MakeObject<Document>(inputFileName);

    auto pdfSaveOptions = MakeObject<PdfSaveOptions>();

    // Указать имя шрифта по умолчанию
    pdfSaveOptions->set_DefaultFontName(newName);
    document->Save(_dataDir + outputFileName, pdfSaveOptions);
}
```

### Получить все шрифты из PDF документа

Если вы хотите получить все шрифты из PDF документа, вы можете использовать метод [FontUtilities](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a2e22a508e8baef176dfc34734cf0def9).GetAllFonts(), предоставленный в классе [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).

Пожалуйста, проверьте следующий фрагмент кода, чтобы получить все шрифты из существующего PDF документа:

```cpp
void GetAllFontsFromPDFdocument()
{
    // Строка для имени пути.
    String _dataDir("C:\\Samples\\");
    // Строка для имени файла.
    String inputFileName("sample.pdf");
    String outputFileName("output_out.pdf");
    String newName("Arial");

    auto document = MakeObject<Document>(inputFileName);
    auto fonts = document->get_FontUtilities()->GetAllFonts();
    for (auto font : fonts)
    {
        std::cerr << font->get_FontName() << std::endl;
    }
}
```

### Получить предупреждения о замене шрифтов

Aspose.PDF for C++ предоставляет методы для получения уведомлений о замене шрифтов для обработки случаев замены шрифтов. Фрагменты кода ниже показывают, как использовать соответствующую функциональность.

```cpp
void GetWarningsForFontSubstitution()
{
    // Строка для имени пути.
    String _dataDir("C:\\Samples\\");

    // Строка для имени файла.
    String inputFileName("sample.pdf");
    String outputFileName("output_out.pdf");

    auto document = MakeObject<Document>(inputFileName);

    document->FontSubstitution = Aspose::Pdf::Document::FontSubstitutionHandler(OnFontSubstitution);
}
```

Метод [OnFontSubstitution](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac776d8736d430532bdaa530a36eb51a0) представлен ниже.

```cpp
void OnFontSubstitution(Aspose::Pdf::Text::Font &font, Aspose::Pdf::Text::Font& newFont) {
    std::cout << "Warning: Font " << font.get_FontName() 
            << " was substituted with another font -> " 
            << newFont.get_FontName() << std::endl;
}
```

### Улучшение внедрения шрифтов с помощью FontSubsetStrategy

Функция для внедрения шрифтов в качестве подмножества может быть выполнена с использованием свойства IsSubset, но иногда вы хотите сократить полностью внедренный набор шрифтов только до подмножеств, которые используются в документе. [Aspose.Pdf.Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) имеет свойство [FontUtilities](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document.i_document_font_utilities/), которое включает метод SubsetFonts(FontSubsetStrategy subsetStrategy). В методе SubsetFonts() параметр subsetStrategy помогает настроить стратегию подмножества. FontSubsetStrategy поддерживает два следующих варианта подмножества шрифтов.

- SubsetAllFonts - Это подмножество всех шрифтов, используемых в документе.
- SubsetEmbeddedFontsOnly - Это подмножество только тех шрифтов, которые полностью встроены в документ.

Следующий фрагмент кода показывает, как установить FontSubsetStrategy:

```cpp
void ImproveFontsEmbeddingUsingFontSubsetStrategy()
{
    // Строка для имени пути.
    String _dataDir("C:\\Samples\\");

    // Строка для имени файла.
    String inputFileName("sample.pdf");
    // Строка для имени файла.
    String outputFileName("sample_out.pdf");

    auto document = MakeObject<Document>(inputFileName);
    // Все шрифты будут встроены как подмножество в документ в случае SubsetAllFonts.
    document->get_FontUtilities()->SubsetFonts(FontSubsetStrategy::SubsetAllFonts);
    // Подмножество шрифтов будет встроено для полностью встроенных шрифтов, но шрифты, которые не встроены в документ, не будут затронуты.
    document->get_FontUtilities()->SubsetFonts(FontSubsetStrategy::SubsetEmbeddedFontsOnly);
    document->Save(_dataDir + outputFileName);
}
```
### Установить-Получить Коэффициент Масштабирования PDF Файла

Иногда требуется установить коэффициент масштабирования PDF документа. С помощью Aspose.PDF для C++ вы можете установить значение коэффициента масштабирования с помощью метода [set_OpenAction(…)](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#abb5c84979077034d06a673409b666e21) класса Document.

Свойство Destination класса [GoToAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.go_to_action/) позволяет получить значение масштабирования, связанное с PDF файлом. Аналогично, оно может быть использовано для установки коэффициента масштабирования файла.

#### Установить коэффициент масштабирования

Следующий фрагмент кода показывает, как установить коэффициент масштабирования PDF файла.

```cpp
void SetZoomFactor() {
    // Строка для имени пути.
    String _dataDir("C:\\Samples\\");

    // Строка для имени файла.
    String inputFileName("sample.pdf");
    // Строка для имени файла.
    String outputFileName("Zoomed_pdf_out.pdf");

    auto document = MakeObject<Document>(inputFileName);
    auto action = MakeObject<Aspose::Pdf::Annotations::GoToAction>(MakeObject<Aspose::Pdf::Annotations::XYZExplicitDestination>(1, 0, 0, .5));

    document->set_OpenAction(action);
    // Сохранить документ
    document->Save(_dataDir + outputFileName);
}
```

#### Получить коэффициент увеличения

Получите коэффициент увеличения в вашем PDF-файле, используя Aspose.PDF для C++.

Следующий фрагмент кода показывает, как получить коэффициент увеличения PDF-файла:

```cpp
void GetZoomFactor() 
{
    // Строка для названия пути.
    String _dataDir("C:\\Samples\\");

    // Строка для названия файла.
    String inputFileName("sample.pdf");

    auto document = MakeObject<Document>(inputFileName);

    // Создать объект GoToAction
    auto action = System::DynamicCast<Aspose::Pdf::Annotations::GoToAction>(document->get_OpenAction());

    // Получить коэффициент увеличения PDF-файла
    auto zoom = System::DynamicCast<Aspose::Pdf::Annotations::XYZExplicitDestination>(action->get_Destination());
    Console::WriteLine(zoom->get_Zoom()); // Значение увеличения документа;
}
```

### Установка свойств предварительных настроек диалога печати

Aspose.PDF для C++ позволяет устанавливать свойства предварительных настроек диалога печати PDF-документа. Он позволяет изменить свойство DuplexMode для PDF-документа, которое по умолчанию установлено в simplex. Это можно сделать с помощью двух различных методологий, как показано ниже.

```cpp
void SettingPrintDialogPresetProperties()
{
    // Строка для имени пути.
    String _dataDir("C:\\Samples\\");
    // Строка для имени файла.
    String outputFileName("SettingPrintDialogPresetProperties.pdf");

    auto document = MakeObject<Document>();
    document->get_Pages()->Add();
    document->set_Duplex(PrintDuplex::DuplexFlipLongEdge);
    document->Save(_dataDir + outputFileName);
}
```

### Установка предустановленных свойств диалога печати с использованием PDF Content Editor

```cpp
void SettingPrintDialogPresetPropertiesUsingContentEditor() {
    // Строка для имени пути.
    String _dataDir("C:\\Samples\\");

    // Строка для имени файла.
    String inputFileName("sample.pdf");
    String outputFileName("SetPrintDlgPropertiesUsingPdfContentEditor_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto contentEditor = MakeObject<Aspose::Pdf::Facades::PdfContentEditor>();

    contentEditor->BindPdf(outputFileName);
    if ((contentEditor->GetViewerPreference() & Aspose::Pdf::Facades::ViewerPreference::DuplexFlipShortEdge) > 0)
    {
    std::cout << "Файл имеет дуплекс с переворотом короткого края" << std::endl;
    }

    contentEditor->ChangeViewerPreference(Aspose::Pdf::Facades::ViewerPreference::DuplexFlipShortEdge);
    contentEditor->Save(_dataDir + outputFileName);
}
```