---
title: PDF Мультимедийная Аннотация с использованием C++
linktitle: Мультимедийная Аннотация
type: docs
weight: 40
url: /cpp/multimedia-annotation/
description: Aspose.PDF для C++ позволяет добавлять, получать и удалять мультимедийные аннотации из вашего PDF документа.
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Добавление видео, аудио и интерактивного контента превращает PDF в многомерные инструменты коммуникации, которые повышают интерес и вовлеченность в ваши документы. Такой контент в формате PDF называется мультимедийными аннотациями.

Аннотации в PDF документе содержатся в коллекции Annotations объекта [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page). Эта коллекция содержит все аннотации только для этой отдельной страницы: каждая страница имеет свою собственную коллекцию Annotations. Чтобы добавить аннотацию на конкретную страницу, добавьте ее в коллекцию Annotations этой страницы, используя метод Add.

Используйте класс [ScreenAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.screen_annotation) в пространстве имен Aspose.PDF.InteractiveFeatures.Annotations, чтобы включить файлы SWF в качестве аннотаций в PDF документ. 
Экранная аннотация указывает область страницы, на которой могут воспроизводиться медиа-клипы.

Когда вам нужно добавить внешнюю видео-ссылку в PDF-документ, вы можете использовать [MovieAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.movie_annotation). Аннотация фильма содержит анимированную графику и звук, которые будут представлены на экране компьютера и через динамики.

[Звуковая аннотация](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.sound_annotation) должна быть аналогичной текстовой аннотации, за исключением того, что вместо текстовой заметки она содержит звук, записанный с микрофона компьютера или импортированный из файла. Когда аннотация активирована, звук должен воспроизводиться. Аннотация должна вести себя как текстовая аннотация в большинстве случаев, с другой иконкой (по умолчанию, динамик), чтобы указать, что она представляет звук.

Однако, когда требуется встроить медиа в PDF-документ, вам нужно использовать [RichMediaAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.rich_media_annotation).
```
## Добавить экранную аннотацию

Следующий фрагмент кода показывает, как добавить экранную аннотацию в PDF файл:

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Annotations;

void MultimediaAnnotations::AddScreenAnnotation()
{
    String _dataDir("C:\\Samples\\");

    // Загрузить PDF файл
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->idx_get(1);

    String mediaFile = _dataDir + u"input.swf";

    // Создать экранную аннотацию
    auto screenAnnotation = MakeObject<ScreenAnnotation>(page, MakeObject<Rectangle>(170, 190, 470, 380), mediaFile);
    page->get_Annotations()->Add(screenAnnotation);

    document->Save(_dataDir + u"sample_swf.pdf");
}
```

## Добавить звуковую аннотацию

Следующий фрагмент кода показывает, как добавить звуковую аннотацию в PDF файл:

```cpp
  void MultimediaAnnotations::AddSoundAnnotation()
{

    String _dataDir("C:\\Samples\\");

    // Загрузить PDF файл
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->idx_get(1);

    String mediaFile = _dataDir + u"file_example_WAV_1MG.wav";

    // Создать звуковую аннотацию
    auto soundAnnotation = MakeObject<SoundAnnotation>(page, new Rectangle(20, 700, 60, 740), mediaFile);
    soundAnnotation->set_Color(Color::get_Blue());
    soundAnnotation->set_Title(u"John Smith");
    soundAnnotation->set_Subject(u"Sound Annotation demo");
    soundAnnotation->set_Popup(MakeObject<PopupAnnotation>(document));

    page->get_Annotations()->Add(soundAnnotation);

    document->Save(_dataDir + u"sample_wav.pdf");
}

```

## Добавить RichMediaAnnotation

Следующий фрагмент кода показывает, как добавить RichMediaAnnotation в PDF файл:

```cpp
       void MultimediaAnnotations::AddRichMediaAnnotation()
{
    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>();

    String pathToAdobeApp (u"C:\\Program Files (x86)\\Adobe\\Acrobat 2017\\Acrobat\\Multimedia Skins");
    auto page = document->get_Pages()->Add();

    // дайте имя видеоданным. Эти данные будут внедрены в документ с этим
    // именем и ссылаться на переменные flash с этим именем.
    // videoName не должен содержать путь к файлу; это скорее "ключ" для доступа
    // к данным внутри PDF документа

    String videoName (u"file_example_MP4_480_1_5MG.mp4");
    String posterName (u"file_example_MP4_480_1_5MG_poster.jpg");

    // также мы используем скин для видеоплеера
    String skinName (u"SkinOverAllNoFullNoCaption.swf");

    auto rma = MakeObject<RichMediaAnnotation>(page, MakeObject<Rectangle>(100, 500, 300, 600));

    // здесь мы должны указать поток, содержащий код видеоплеера
    rma->set_CustomPlayer(System::IO::File::OpenRead(pathToAdobeApp + u"Players\\" + u"Videoplayer.swf"));

    // составляем строку flash переменных для плеера. обратите внимание, что у разных плееров
    // может быть разный формат строки flash переменных.
    // Обратитесь к документации вашего плеера.
    rma->set_CustomFlashVariables(u"source=" + videoName + u"&skin=" + skinName);

    // добавляем код скина.
    rma->AddCustomData(skinName, System::IO::File::OpenRead(pathToAdobeApp + u"SkinOverAllNoFullNoCaption.swf"));
    // устанавливаем постер для видео
    rma->SetPoster(System::IO::File::OpenRead(_dataDir + posterName));

    // устанавливаем видеоконтент
    rma->SetContent(videoName, System::IO::File::OpenRead(_dataDir + videoName));

    // устанавливаем тип контента (видео)
    rma->set_Type(RichMediaAnnotation::ContentType::Video);

    // активируем плеер по клику
    rma->set_ActivateOn(RichMediaAnnotation::ActivationEvent::Click);

    // обновляем данные аннотации. Этот метод должен быть вызван после всех
    // назначений/настроек. Этот метод инициализирует структуру данных аннотации
    // и внедряет необходимые данные.
    rma->Update();

    // добавляем аннотацию на страницу.
    page->get_Annotations()->Add(rma);

    document->Save(_dataDir + u"RichMediaAnnotation.pdf");
}
```

### Получение MultimediaAnnotation

Пожалуйста, попробуйте использовать следующий фрагмент кода, чтобы получить MultimediaAnnotation из PDF-документа.

```cpp
void MultimediaAnnotations::GetMultimediaAnnotation() {

    String _dataDir("C:\\Samples\\");
    // Загрузите PDF-файл
    auto document = MakeObject<Document>(_dataDir + u"RichMediaAnnotation.pdf");
    auto page = document->get_Pages()->idx_get(1);

    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<RichMediaAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto mediaAnnotations = annotationSelector->get_Selected();

    for (auto ma : mediaAnnotations) {
        Console::WriteLine(u"{0} {1}", ma->get_AnnotationType(), ma->get_Rect());
    }
}
```

### Удаление MultimediaAnnotation

Следующий фрагмент кода показывает, как удалить MultimediaAnnotation из PDF-файла.

```cpp
void MultimediaAnnotations::DeleteRichMediaAnnotation() {

    String _dataDir("C:\\Samples\\");
    // Загрузите PDF-файл
    auto document = MakeObject<Document>(_dataDir + u"RichMediaAnnotation.pdf");
    auto page = document->get_Pages()->idx_get(1);

    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<RichMediaAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto mediaAnnotations = annotationSelector->get_Selected();

    for (auto ma : mediaAnnotations) {
        page->get_Annotations()->Delete(ma);
    }
    document->Save(_dataDir + u"RichMediaAnnotation_del.pdf");
}
```

## Добавление 3D Аннотации

Сегодня PDF файлы могут содержать разнообразный контент, помимо простого текста и графики, включая логические структуры, интерактивные элементы, такие как аннотации и поля форм, слои, мультимедиа (включая видео контент), и 3D объекты.

Такой 3D контент может быть просмотрен в PDF файле с использованием 3D аннотаций.

Этот раздел показывает основные шаги создания 3D аннотации в PDF документе с использованием библиотеки Aspose.PDF на C++.

3D аннотация добавляется с использованием модели, созданной в формате U3D.

1. Создайте новый [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/)
1. Загрузите данные желаемой 3D модели (в нашем случае "Ring.u3d") для создания [PDF3DContent](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.p_d_f3_d_content/)
1. Создайте объект [3dArtWork](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.p_d_f3_d_artwork/) и свяжите его с документом и 3DContent
1. Настройте объект pdf3dArtWork:

```cpp
void MultimediaAnnotation::Add3DAnnottaion()
{
    public static void Add3dAnnotation()
    {
        // Загрузите PDF файл
        Document document = new Document();
        PDF3DContent pdf3DContent = new PDF3DContent(_dataDir + "Ring.u3d");
        PDF3DArtwork pdf3dArtWork = new PDF3DArtwork(document, pdf3DContent);
        pdf3dArtWork.setLightingScheme(new PDF3DLightingScheme(LightingSchemeType.CAD));
        pdf3dArtWork.setRenderMode(new PDF3DRenderMode(RenderModeType.Solid));

        var topMatrix = new Matrix3D(1, 0, 0, 0, -1, 0, 0, 0, -1, 0.10271, 0.08184, 0.273836);
        var frontMatrix = new Matrix3D(0, -1, 0, 0, 0, 1, -1, 0, 0, 0.332652, 0.08184, 0.085273);
        pdf3dArtWork.getViewArray().add(new PDF3DView(document, topMatrix, 0.188563, "Top")); //1
        pdf3dArtWork.getViewArray().add(new PDF3DView(document, frontMatrix, 0.188563, "Left")); //2

        var page = document.getPages().add();

        var pdf3dAnnotation = new PDF3DAnnotation(page, new Rectangle(100, 500, 300, 700), pdf3dArtWork);
        pdf3dAnnotation.setBorder(new Border(pdf3dAnnotation));
        pdf3dAnnotation.setDefaultViewIndex(1);
        pdf3dAnnotation.setFlags(com.aspose.pdf.AnnotationFlags.NoZoom);
        pdf3dAnnotation.setName("Ring.u3d");
        //установите превью изображения, если нужно
        //pdf3dAnnotation.setImagePreview(_dataDir + "sample_3d.png");
        document.getPages().get_Item(1).getAnnotations().add(pdf3dAnnotation);

        document.save(_dataDir + "sample_3d.pdf");
    }
}
```

Этот пример кода показал нам такую модель:

![3D Annotation demo](3d_demo.png)


## Добавить Аннотацию Виджета

Аннотация Виджета представляет собой внешний вид полей формы в интерактивной PDF-форме.

С версии PDF 1.2 мы можем использовать Аннотации Виджетов. Это интерактивные элементы формы, которые мы можем добавить в PDF, чтобы упростить ввод, отправку информации или выполнение некоторых других действий с пользователем. Хотя виджеты являются особым типом аннотации, мы не можем создавать их как аннотации напрямую, потому что аннотации виджетов являются графическим представлением поля формы на конкретных страницах.

Каждое поле формы для каждого местоположения в документе представляет одну Аннотацию Виджета. Данные аннотации, специфичные для местоположения виджета, добавляются на конкретную страницу. Каждое поле формы имеет несколько опций. Кнопка может быть переключателем, флажком или кнопкой. Виджет выбора может быть списком или выпадающим списком.


Aspose.PDF для C++ позволяет вам добавить эту аннотацию, используя класс [Widget Annotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.widget_annotation/).

Чтобы добавить кнопку на страницу, нам нужно использовать следующий фрагмент кода:

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;
using namespace Aspose::Pdf::Annotations;

void ExampleWidgetAnnotation::AddButton() {

    String _dataDir("C:\\Samples\\");

    // Загрузить PDF файл
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->idx_get(1);

    auto rect = MakeObject<Rectangle>(72, 748, 164, 768);

    auto printButton = MakeObject<ButtonField>(page, rect);
    printButton->set_AlternateName(u"Распечатать текущий документ");
    printButton->set_Color(Color::get_Black());
    printButton->set_PartialName(u"printBtn1");
    printButton->set_NormalCaption(u"Распечатать документ");

    auto border = MakeObject<Border>(printButton);
    border->set_Style(BorderStyle::Solid);
    border->set_Width(2);

    printButton->set_Border(border);
    printButton->get_Characteristics()->set_Border(System::Drawing::Color::FromArgb(255, 0, 0, 255));
    printButton->get_Characteristics()->set_Background(System::Drawing::Color::FromArgb(255, 0, 191, 255));
    auto wa = System::DynamicCast<Field>(printButton);
    document->get_Form()->Add(wa);

    document->Save(_dataDir + u"sample_widgetannot.pdf");
}
```

### Использование действий навигации по документу

Этот пример показывает, как создать 4 кнопки:

```cpp
void ExampleWidgetAnnotation::AddDocumentNavigationActions() {

    String _dataDir("C:\\Samples\\");

    // Загрузить PDF файл
    auto document = MakeObject<Document>(_dataDir + u"JSON Fundamenals.pdf");

    auto buttons = MakeArray<System::SmartPtr<ButtonField>>(4);
    auto alternateNames = MakeArray<String>({ u"Перейти на первую страницу", u"Перейти на предыдущую страницу", u"Перейти на следующую страницу", u"Перейти на последнюю страницу" });
    auto normalCaptions = MakeArray<String>({ u"Первая", u"Пред", u"След", u"Последняя" });
    PredefinedAction actions[] = { PredefinedAction::FirstPage, PredefinedAction::PrevPage,
                                    PredefinedAction::NextPage, PredefinedAction::LastPage };
    auto clrBorder = System::Drawing::Color::FromArgb(255, 0, 255, 0);
    auto clrBackGround = System::Drawing::Color::Color::FromArgb(255, 0, 96, 70);

// Мы должны создать кнопки, не прикрепляя их к странице.

    for (int i = 0; i < 4; i++) {
        buttons[i] = MakeObject<ButtonField>(document, MakeObject<Rectangle>(32 + i * 80, 28, 104 + i * 80, 68));
        buttons[i]->set_AlternateName(alternateNames[i]);
        buttons[i]->set_Color(Color::get_White());
        buttons[i]->set_NormalCaption(normalCaptions[i]);
        buttons[i]->set_OnActivated(new NamedAction(actions[i]));
        auto border = MakeObject<Border>(buttons[i]);
        border->set_Style(BorderStyle::Solid);
        border->set_Width(2);
        buttons[i]->set_Border(border);
        buttons[i]->get_Characteristics()->set_Border(clrBorder);
        buttons[i]->get_Characteristics()->set_Background(clrBackGround);
    }

// Мы должны дублировать этот массив кнопок на каждой странице в документе.

    for (int pageIndex = 1; pageIndex <= 4; pageIndex++)
        for (int i = 0; i < 4; i++)
            document->get_Form()->Add(buttons[i], String::Format(u"btn{0}_{1}", pageIndex,(i + 1)), pageIndex);

    document->get_Form()->idx_get(u"btn1_1")->set_ReadOnly(true);
    document->get_Form()->idx_get(u"btn1_2")->set_ReadOnly(true);

    document->get_Form()->idx_get(String::Format(u"btn{0}_3", document->get_Pages()->get_Count()))->set_ReadOnly(true);
    document->get_Form()->idx_get(String::Format(u"btn{0}_4", document->get_Pages()->get_Count()))->set_ReadOnly(true);
    document->Save(_dataDir + u"sample_widgetannot_2.pdf");
}
```

### Удалить аннотацию виджета

```cpp
void ExampleWidgetAnnotation::DeleteWidgetAnnotation() {

    String _dataDir("C:\\Samples\\");

    // Загрузить PDF файл
    auto document = MakeObject<Document>(_dataDir + u"sample_widgetannot.pdf");
    auto page = document->get_Pages()->idx_get(1);
    auto annotationSelector = MakeObject<AnnotationSelector>(MakeObject<ButtonField>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto buttonFields = annotationSelector->get_Selected();

    // удалить аннотации
    for (auto wa : buttonFields) {
        page->get_Annotations()->Delete(wa);
    }
    document->Save(_dataDir + u"sample_widgetannot_del.pdf");
}
```