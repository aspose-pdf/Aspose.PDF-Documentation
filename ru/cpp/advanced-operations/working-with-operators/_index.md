---
title: Работа с операторами в C++
linktitle: Работа с операторами
type: docs
weight: 170
url: /ru/cpp/operators/
description: Эта тема объясняет, как использовать операторы с Aspose.PDF в C++. Классы операторов предоставляют отличные возможности для манипуляции с PDF.
lastmod: "2021-12-14"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Введение в операторы PDF и их использование

Оператор — это ключевое слово PDF, указывающее на действие, которое должно быть выполнено, например, рисование графической формы на странице. Ключевое слово оператора отличается от именованного объекта отсутствием начального символа наклонной черты (2Fh). Операторы имеют смысл только внутри потока содержимого.

Поток содержимого — это объект потока PDF, данные которого состоят из инструкций, описывающих графические элементы, которые должны быть нарисованы на странице. Более подробную информацию об операторах PDF можно найти в [спецификации PDF](https://opensource.adobe.com/dc-acrobat-sdk-docs/).

### Подробности реализации

Эта тема объясняет, как использовать операторы с Aspose.PDF. Выбранный пример добавляет изображение в PDF файл для иллюстрации концепции. Чтобы добавить изображение в PDF файл, необходимы различные операторы. В этом примере используются [GSave](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_save), [ConcatenateMatrix](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.concatenate_matrix), [Do](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.do) и [GRestore](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_restore).

- Оператор **GSave** сохраняет текущие графические состояния PDF.
- Оператор **ConcatenateMatrix** (конкатенация матрицы) используется для определения того, как изображение должно быть размещено на странице PDF.
- Оператор **Do** рисует изображение на странице.
- Оператор **GRestore** восстанавливает графическое состояние.

Чтобы добавить изображение в PDF файл:

1. Создайте объект [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) и откройте входной PDF документ.
1. Получите конкретную страницу, на которую будет добавлено изображение.
1. Добавьте изображение в коллекцию ресурсов страницы.
1. Используйте операторы, чтобы разместить изображение на странице:
   - Сначала используйте оператор GSave, чтобы сохранить текущее графическое состояние.
   - Затем используйте оператор ConcatenateMatrix, чтобы указать, где должно быть размещено изображение.
   - Используйте оператор Do, чтобы нарисовать изображение на странице.
1. Наконец, используйте оператор GRestore, чтобы сохранить обновленное графическое состояние.

Следующий фрагмент кода показывает, как использовать операторы PDF.

```cpp
void ExampleUsingOperators()
{
    // Открыть документ
    String _dataDir("C:\\Samples\\");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + u"PDFOperators.pdf");

    // Установить координаты
    int lowerLeftX = 100;
    int lowerLeftY = 100;
    int upperRightX = 200;
    int upperRightY = 200;

    // Получить страницу, на которую нужно добавить изображение
    auto page = document->get_Pages()->idx_get(1);

    // Загрузить изображение в поток
    auto imageStream = System::IO::File::OpenRead(_dataDir + u"PDFOperators.jpg");
    // Добавить изображение в коллекцию изображений ресурсов страницы
    page->get_Resources()->get_Images()->Add(imageStream);

    // Использование оператора GSave: этот оператор сохраняет текущее графическое состояние
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GSave>());
    // Создать объекты Rectangle и Matrix
    auto rectangle = MakeObject<Rectangle>(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
    auto matrix = MakeObject<Matrix>(
        new double[] {
            rectangle->get_URX() - rectangle->get_LLX(), 0, 0,
            rectangle->get_URY() - rectangle->get_LLY(),
            rectangle->get_LLX(),  rectangle->get_LLY() });
    // Использование оператора ConcatenateMatrix (конкатенация матрицы): определяет, как должно быть размещено изображение
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(matrix));
    auto ximage = page->get_Resources()->get_Images()->idx_get(page->get_Resources()->get_Images()->get_Count());
    // Использование оператора Do: этот оператор рисует изображение
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::Do>(ximage->get_Name()));
    // Использование оператора GRestore: этот оператор восстанавливает графическое состояние
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());


    // Сохранить обновленный документ
    document->Save(_dataDir + u"PDFOperators_out.pdf");
}
```
## Нарисовать XForm на странице с использованием операторов

Эта тема демонстрирует, как использовать операторы GSave/GRestore, оператор ContatenateMatrix для позиционирования xForm и оператор Do для рисования xForm на странице.

Код ниже оборачивает существующее содержимое PDF-файла парой операторов GSave/GRestore. Этот подход помогает получить начальное состояние графики в конце существующего содержимого. Без этого подхода нежелательные преобразования могут остаться в конце существующей цепочки операторов.

```cpp
void DrawXFormOnPageUsingOperators() {
    // Открыть документ
    String _dataDir("C:\\Samples\\");

    String imageFile(_dataDir + u"aspose-logo.jpg");
    String inFile(_dataDir + u"DrawXFormOnPage.pdf");
    String outFile(_dataDir + u"blank-sample2_out.pdf");

    auto document = MakeObject<Document>(inFile);
    auto pageContents = document->get_Pages()->idx_get(1)->get_Contents();

    // Пример демонстрирует
    // использование операторов GSave/GRestore
    // использование оператора ContatenateMatrix для позиционирования xForm
    // использование оператора Do для рисования xForm на странице

    // Обернуть существующее содержимое парой операторов GSave/GRestore
    //        это необходимо для получения начального состояния графики в конце существующего содержимого
    //        иначе могут остаться нежелательные преобразования в конце существующей цепочки операторов
    pageContents->Insert(1, MakeObject<Aspose::Pdf::Operators::GSave>());
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

    // Добавить оператор сохранения состояния графики для правильной очистки состояния графики после новых команд
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GSave>());

    // Создать xForm

    auto form = XForm::CreateNewForm(document->get_Pages()->idx_get(1), document);
    document->get_Pages()->idx_get(1)->get_Resources()->get_Forms()->Add(form);
    form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GSave>());
    // Определить ширину и высоту изображения
    form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(200, 0, 0, 200, 0, 0));
    // Загрузить изображение в поток
    auto imageStream = System::IO::File::OpenRead(imageFile);
    // Добавить изображение в коллекцию Images ресурсов XForm
    form->get_Resources()->get_Images()->Add(imageStream);
    auto ximage = form->get_Resources()->get_Images()->idx_get(form->get_Resources()->get_Images()->get_Count());
    // Использование оператора Do: этот оператор рисует изображение
    form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::Do>(ximage->get_Name()));
    form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

    // ----------------------------------------------------

    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GSave>());
    // Разместить форму на координатах x=100 y=500
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(1, 0, 0, 1, 100, 500));
    // Нарисовать форму с помощью оператора Do
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::Do>(form->get_Name()));
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GSave>());
    // Разместить форму на координатах x=100 y=300
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(1, 0, 0, 1, 100, 300));
    // Нарисовать форму с помощью оператора Do
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::Do>(form->get_Name()));
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

    // Восстановить состояние графики с помощью GRestore после GSave
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());
    document->Save(outFile);
}
```

## Удаление графических объектов с использованием классов операторов

Классы операторов предоставляют отличные возможности для манипуляции PDF. Когда файл PDF содержит графику, которую нельзя удалить с помощью метода [DeleteImage](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_content_editor#af7d23ef932737bf606f008ad5ec48380) класса [PdfContentEditor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_content_editor), можно использовать классы операторов для их удаления.

Следующий фрагмент кода показывает, как удалить графику. Обратите внимание, что если в PDF-файле содержатся текстовые метки для графики, они могут остаться в файле PDF при использовании этого подхода. Поэтому найдите графические операторы для альтернативного метода удаления таких изображений.

```cpp
void RemoveGraphicsObjects() {
    // Открыть документ
    String _dataDir("C:\\Samples\\");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + u"RemoveGraphicsObjects.pdf");

    auto page = document->get_Pages()->idx_get(2);
    auto oc = page->get_Contents();

    // Используемые операторы рисования пути
    auto operators = MakeArray<System::SmartPtr<Operator>>({
            MakeObject<Aspose::Pdf::Operators::Stroke>(),
            MakeObject<Aspose::Pdf::Operators::ClosePathStroke>(),
            MakeObject<Aspose::Pdf::Operators::Fill>()
    });

    oc->Delete(operators);
    document->Save(_dataDir + u"No_Graphics_out.pdf");
}
```