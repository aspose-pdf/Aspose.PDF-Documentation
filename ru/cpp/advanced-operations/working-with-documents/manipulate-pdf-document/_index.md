---
title: Манипулировать PDF-документом 
linktitle: Манипулировать PDF-документом
type: docs
weight: 30
url: ru/cpp/manipulate-pdf-document/
lastmod: "2021-11-11"
description: Этот раздел объясняет проверку PDF-документа на соответствие стандарту PDF A, как работать с Оглавлением, как установить дату истечения срока действия PDF и как определить прогресс генерации PDF-файла.
lastmod: "2021-11-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Проверка PDF-документа на соответствие стандарту PDF A (A 1A и A 1B)

Для проверки совместимости PDF-документа с PDF/A-1a или PDF/A-1b используйте метод [Validate](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#aa1ac4565b320807c718c44eeee7cda8c) класса [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). Этот метод позволяет указать имя файла, в котором будет сохранен результат, и требуемый тип проверки [PdfFormat](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#ac83739fd7c818167c2fdc4dd554de763) перечисления: PDF_A_1A или PDF_A_1B.


{{% alert color="primary" %}}

Формат выходного XML является пользовательским форматом Aspose. XML содержит коллекцию тегов с именем Problem; каждый тег содержит детали конкретной проблемы. Атрибут ObjectID тега Problem представляет ID конкретного объекта, к которому относится эта проблема. Атрибут Clause представляет соответствующее правило в спецификации PDF.

{{% /alert %}}

Следующий фрагмент кода показывает, как проверить PDF-документ на соответствие стандарту PDF/A-1A.

```cpp
void ExampleValidate01() {
    // Строка для имени пути.
    String _dataDir("C:\\Samples\\");

    // Строка для имени файла.
    String inputFileName("ValidatePDFAStandard.pdf");
    String outputFileName("Validation-result-A1A.xml");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + inputFileName);
    // Проверить PDF на соответствие PDF/A-1a
    document->Validate(_dataDir + outputFileName, PdfFormat::PDF_A_1A);
}
```

Следующий фрагмент кода показывает, как проверить PDF-документ на соответствие стандарту PDF/A-1B.

```cpp
void ExampleValidate02() {
    // Строка для имени пути.
    String _dataDir("C:\\Samples\\");

    // Строка для имени файла.
    String inputFileName("ValidatePDFAStandard.pdf");
    String outputFileName("Validation-result-A1B.xml");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + inputFileName);
    // Проверить PDF на соответствие PDF/A-1a
    document->Validate(_dataDir + outputFileName, PdfFormat::PDF_A_1B);
}
```

## Работа с оглавлением

### Добавление оглавления в существующий PDF

Aspose.PDF API позволяет добавить оглавление как при создании PDF, так и в существующий файл.

Чтобы добавить оглавление в существующий PDF файл, используйте класс [Heading](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.heading) из пространства имен Aspose.Pdf. Пространство имен Aspose.Pdf позволяет создавать новые и изменять существующие PDF файлы. Чтобы добавить оглавление в существующий PDF, используйте пространство имен Aspose.Pdf.

Следующий фрагмент кода показывает, как создать оглавление внутри существующего PDF файла.

```cpp
void ExampleToc01() {
    // Строка для путей.
    String _dataDir("C:\\Samples\\");

    // Строка для имен файлов
    String inputFileName("AddTOC.pdf");
    String outputFileName("TOC_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Получить доступ к первой странице PDF файла
    auto tocPage = document->get_Pages()->Insert(1);

    // Создать объект для представления информации об оглавлении
    auto tocInfo = MakeObject<TocInfo>();
    auto title = MakeObject<TextFragment>("Table Of Contents");
    title->get_TextState()->set_FontSize(20);
    title->get_TextState()->set_FontStyle(FontStyles::Bold);

    // Установить заголовок для оглавления
    tocInfo->set_Title(title);
    tocPage->set_TocInfo(tocInfo);

    // Создать строковые объекты, которые будут использоваться как элементы оглавления
    auto titles = MakeArray<String>(4);
    titles->SetValue(u"Первая страница", 0);
    titles->SetValue(u"Вторая страница", 1);
    titles->SetValue(u"Третья страница", 2);
    titles->SetValue(u"Четвертая страница", 3);

    for (int i = 0; i < 2; i++)
    {
        // Создать объект заголовка
        auto heading2 = MakeObject<Heading>(1);
        auto segment2 = MakeObject<TextSegment>();
        heading2->set_TocPage(tocPage);
        heading2->get_Segments()->Add(segment2);

        // Указать страницу назначения для объекта заголовка

        heading2->set_DestinationPage(document->get_Pages()->idx_get(i + 2));

        // Страница назначения
        heading2->set_Top(document->get_Pages()->idx_get(i + 2)->get_Rect()->get_Height());

        // Координата назначения
        segment2->set_Text(titles[i]);

        // Добавить заголовок на страницу, содержащую оглавление
        tocPage->get_Paragraphs()->Add(heading2);
    }

    // Сохранить обновленный документ
    document->Save(_dataDir + outputFileName);
}
```

### Установить различные TabLeaderType для разных уровней TOC

Aspose.PDF для C++ также позволяет устанавливать различные TabLeaderType для разных уровней TOC. Необходимо установить свойство LineDash объекта FormatArray с соответствующим значением TabLeaderType. Затем вы можете добавить секцию списка в коллекцию секций документа Pdf. После этого создайте секцию в документе Pdf и сохраните файл PDF.

```cpp
void ExampleToc02() {
    // Строка для имени пути.
    String _dataDir("C:\\Samples\\");

    // Строка для имени файла.
    String inputFileName("AddTOC.pdf");

    String outputFileName("TOC_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto tocPage = document->get_Pages()->Add();
    auto tocInfo = MakeObject<TocInfo>();

    //установить LeaderType
    tocInfo->set_LineDash(TabLeaderType::Solid);

    // Создать объект для представления информации о TOC
    auto tocInfo = MakeObject<TocInfo>();
    auto title = MakeObject<TextFragment>("Оглавление");
    title->get_TextState()->set_FontSize(20);
    title->get_TextState()->set_FontStyle(FontStyles::Bold);

    // Установить заголовок для TOC
    tocInfo->set_Title(title);

    //Добавить секцию списка в коллекцию секций документа Pdf
    tocPage->set_TocInfo(tocInfo);

    //Определить формат списка четырех уровней, установив левые отступы
    //и
    //настройки формата текста для каждого уровня

    tocInfo->set_FormatArrayLength(4);
    tocInfo->get_FormatArray()->idx_get(0)->get_Margin()->set_Left(0);
    tocInfo->get_FormatArray()->idx_get(0)->get_Margin()->set_Right(30);
    tocInfo->get_FormatArray()->idx_get(0)->set_LineDash(TabLeaderType::Dot);
    tocInfo->get_FormatArray()->idx_get(0)->get_TextState()->set_FontStyle(FontStyles::Bold | FontStyles::Italic);
    tocInfo->get_FormatArray()->idx_get(1)->get_Margin()->set_Left(10);
    tocInfo->get_FormatArray()->idx_get(1)->get_Margin()->set_Right(30);
    tocInfo->get_FormatArray()->idx_get(1)->set_LineDash(TabLeaderType::None);
    tocInfo->get_FormatArray()->idx_get(1)->get_TextState()->set_FontSize(10);
    tocInfo->get_FormatArray()->idx_get(2)->get_Margin()->set_Left(20);
    tocInfo->get_FormatArray()->idx_get(2)->get_Margin()->set_Right(30);
    tocInfo->get_FormatArray()->idx_get(2)->get_TextState()->set_FontStyle(FontStyles::Bold);
    tocInfo->get_FormatArray()->idx_get(3)->set_LineDash(TabLeaderType::Solid);
    tocInfo->get_FormatArray()->idx_get(3)->get_Margin()->set_Left(30);
    tocInfo->get_FormatArray()->idx_get(3)->get_Margin()->set_Right(30);
    tocInfo->get_FormatArray()->idx_get(3)->get_TextState()->set_FontStyle(FontStyles::Bold);

    //Создать секцию в документе Pdf
    auto page = document->get_Pages()->Add();

    //Добавить четыре заголовка в секцию
    for (int Level = 1; Level <= 4; Level++)
    {
    auto heading2 = MakeObject<Heading>(Level);
    auto segment2 = MakeObject<TextSegment>();

    heading2->get_Segments()->Add(segment2);
    heading2->set_IsAutoSequence(true);
    heading2->set_TocPage(tocPage);
    segment2->set_Text(u"Пример Заголовка" + Level);
    heading2->get_TextState()->set_Font(FontRepository::FindFont(u"Arial Unicode MS"));

    //Добавить заголовок в Оглавление.
    heading2->set_IsInList(true);
    page->get_Paragraphs()->Add(heading2);
    }

    // сохранить Pdf
    document->Save(_dataDir + outputFileName);
}
```

### Скрыть номера страниц в Оглавлении

Если вы хотите скрыть номера страниц вместе с заголовками в оглавлении, вы можете использовать свойство [IsShowPageNumbers](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.toc_info#ada10e841699bba062dcd0b440c26b832) класса [TOCInfo](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.toc_info) как false.

Пожалуйста, проверьте следующий фрагмент кода, чтобы скрыть номера страниц в оглавлении:

```cpp
void ExampleToc03() {
    // Строка для имени пути.
    String _dataDir("C:\\Samples\\");

    // Строка для имени файла.
    String inputFileName("AddTOC.pdf");

    String outputFileName("TOC_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);
    auto tocPage = document->get_Pages()->Add();

    // Создать объект для представления информации об оглавлении
    auto tocInfo = MakeObject<TocInfo>();
    auto title = MakeObject<TextFragment>("Table Of Contents");
    title->get_TextState()->set_FontSize(20);
    title->get_TextState()->set_FontStyle(FontStyles::Bold);

    // Установить заголовок для оглавления
    tocInfo->set_Title(title);

    // Добавить раздел списка в коллекцию разделов документа Pdf
    tocPage->set_TocInfo(tocInfo);

    tocInfo->set_IsShowPageNumbers(false);

    // Определить формат списка из четырех уровней, установив отступы слева и
    // настройки формата текста каждого уровня

    tocInfo->set_FormatArrayLength(4);
    tocInfo->get_FormatArray()->idx_get(0)->get_Margin()->set_Right(0);
    tocInfo->get_FormatArray()->idx_get(0)->get_TextState()->set_FontStyle(FontStyles::Bold | FontStyles::Italic);
    tocInfo->get_FormatArray()->idx_get(1)->get_Margin()->set_Left(30);
    tocInfo->get_FormatArray()->idx_get(1)->get_TextState()->set_Underline(true);
    tocInfo->get_FormatArray()->idx_get(1)->get_TextState()->set_FontSize(10);
    tocInfo->get_FormatArray()->idx_get(2)->get_TextState()->set_FontStyle(FontStyles::Bold);
    tocInfo->get_FormatArray()->idx_get(3)->get_TextState()->set_FontStyle(FontStyles::Bold);

    auto page = document->get_Pages()->Add();
    // Добавить четыре заголовка в раздел
    for (int Level = 1; Level != 5; Level++)
    {
        auto heading2 = MakeObject<Heading>(Level);
        auto segment2 = MakeObject<TextSegment>();
        heading2->set_TocPage(tocPage);
        heading2->get_Segments()->Add(segment2);
        heading2->set_IsAutoSequence(true);
        segment2->set_Text(u"this is heading of level " + Level);
        heading2->set_IsInList(true);
        page->get_Paragraphs()->Add(heading2);
    }
    // сохранить Pdf
    document->Save(_dataDir + outputFileName);
}
```

## Как установить дату истечения срока действия PDF

Мы применяем привилегии доступа к PDF-файлам, чтобы определенная группа пользователей могла получать доступ к определенным функциям/объектам PDF-документов. Чтобы ограничить доступ к PDF-файлу, мы обычно применяем шифрование, и у нас может возникнуть необходимость установить срок действия PDF-файла, чтобы пользователь, получающий доступ/просматривающий документ, получал действительное уведомление о сроке действия PDF-файла.

Для выполнения вышеуказанного требования мы можем использовать объект [JavascriptAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.javascript_action/). Пожалуйста, ознакомьтесь со следующим фрагментом кода.

```cpp
void SetPDFexpiryDate() {

    // Строка для имени пути.
    String _dataDir("C:\\Samples\\");

    // Строка для имени файла. 
    String outputFileName("SetExpiryDate_out.pdf");

    // Создать объект Document
    auto document = MakeObject<Document>();

    // Добавить страницу в коллекцию страниц PDF-файла
    document->get_Pages()->Add();

    // Добавить текстовый фрагмент в коллекцию абзацев объекта страницы
    document->get_Pages()->idx_get(1)->get_Paragraphs()->Add(new TextFragment(u"Hello World..."));

    String javascriptCode(u"var year=2017;");
    javascriptCode += u"var month=5;";
    javascriptCode += u"today = new Date(); today = new Date(today.getFullYear(), today.getMonth());";
    javascriptCode += u"expiry = new Date(year, month);";
    javascriptCode += u"if (today.getTime() > expiry.getTime())";
    javascriptCode += u"app.alert('The file is expired. You need a new one.');";

    // Создать объект JavaScript для установки даты истечения срока действия PDF
    auto javaScript = MakeObject<Aspose::Pdf::Annotations::JavascriptAction>(javascriptCode);

    // Установить JavaScript как действие открытия PDF
    document->set_OpenAction(javaScript);

    // Сохранить PDF-документ
    document->Save(_dataDir + outputFileName);
}
```

## Определение прогресса генерации PDF-файла

Клиент попросил нас добавить функцию, которая позволяет разработчикам определять прогресс генерации PDF-файла. Вот ответ на этот запрос.

Поле [CustomerProgressHandler](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.doc_save_options#a712bcc865fa8f75bbdc2a3b55e4581fb) класса [DocSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.doc_save_options) позволяет определить, как проходит генерация PDF.

Примеры кода ниже показывают, как использовать [CustomerProgressHandler](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.doc_save_options#a712bcc865fa8f75bbdc2a3b55e4581fb).

```cpp
using ProgressHandler = System::MulticastDelegate<void(SharedPtr<UnifiedSaveOptions::ProgressEventHandlerInfo>)>;
void ConversionProgressCallback(SharedPtr<UnifiedSaveOptions::ProgressEventHandlerInfo> eventInfo)
{
    String eventType;
    switch (eventInfo->EventType)
    {
    case ProgressEventType::ResultPageCreated:
        eventType = u"ResultPageCreated";
        break;
    case ProgressEventType::ResultPageSaved:
        eventType = u"ResultPageSaved";
        break;
    case ProgressEventType::SourcePageAnalysed:
        eventType = u"SourcePageAnalysed";
        break;
    case ProgressEventType::TotalProgress:
        eventType = u"TotalProgress";
        break;
    }
    Console::WriteLine(String::Format(u"Тип события: {0}, Значение: {1}, Максимальное значение: {2}", 
        eventType, eventInfo->Value, eventInfo->MaxValue));
}
```

```cpp
void DetermineProgressOfPDFfileGeneration() {
    // Строка для имени пути.
    String _dataDir("C:\\Samples\\");

    // Строка для имени файла.
    String inputFileName("AddTOC.pdf");

    String outputFileName("TOC_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);
    // Открыть документ
    auto saveOptions = MakeObject<DocSaveOptions>();

    saveOptions->CustomProgressHandler = ProgressHandler(ConversionProgressCallback);

    document->Save(_dataDir + outputFileName, saveOptions);
}
```

## Преобразование заполняемых PDF в C++

PDF документы часто включают формы с интерактивными заполняемыми виджетами, такими как радио-кнопки, флажки, текстовые поля, списки и т.д. Чтобы сделать их неизменяемыми для различных целей приложений, необходимо преобразовать PDF файл.
Aspose.PDF для C++ предоставляет функцию для преобразования вашего PDF в C++ всего несколькими строками кода:

```cpp
void FlattenFillablePDF() {
    // Строка для имени пути.
    String _dataDir("C:\\Samples\\");
    // Строка для имени файла.
    String inputFileName("sample-form.pdf");
    String outputFileName("FlattenForms_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Преобразование заполняемых PDF 
    if (document->get_Form()->get_Fields()->get_Count() > 0)
    {
        for (auto item : document->get_Form()->get_Fields())
        item->Flatten();
    }

    // Сохранить обновленный документ
    document->Save(_dataDir + outputFileName);
}
```