---
title: PDF Мультимедийная Аннотация 
linktitle: Мультимедийная Аннотация
type: docs
weight: 40
url: /java/multimedia-annotation/
description: Aspose.PDF for Java позволяет добавлять, получать и удалять мультимедийные аннотации из вашего PDF документа.
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Аннотации в PDF документе содержатся в коллекции Annotations объекта [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page). Эта коллекция содержит все аннотации только для этой отдельной страницы: каждая страница имеет свою собственную коллекцию Annotations. Чтобы добавить аннотацию на конкретную страницу, добавьте ее в коллекцию Annotations этой страницы, используя метод Add.

Используйте класс [ScreenAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/ScreenAnnotation) в пространстве имен Aspose.PDF.InteractiveFeatures.Annotations, чтобы включать файлы SWF в качестве аннотаций в PDF документ.
 Аннотация экрана определяет область страницы, на которой могут воспроизводиться медиа-клипы.

Когда вам нужно добавить внешнюю видеоссылку в PDF-документ, вы можете использовать [MovieAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/MovieAnnotation). Аннотация фильма содержит анимированную графику и звук для отображения на экране компьютера и через динамики.

[Звуковая аннотация](https://reference.aspose.com/pdf/java/com.aspose.pdf/soundannotation) должна быть аналогична текстовой аннотации, за исключением того, что вместо текстовой заметки она содержит звук, записанный с микрофона компьютера или импортированный из файла. Когда аннотация активируется, звук должен воспроизводиться. Аннотация должна вести себя как текстовая аннотация в большинстве случаев, с другой иконкой (по умолчанию, динамик), чтобы указать, что она представляет звук.

Однако, когда требуется встроить медиа в PDF-документ, вам нужно использовать [RichMediaAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/RichMediaAnnotation).
Следующие методы/свойства класса RichMediaAnnotation могут быть использованы.

- Stream CustomPlayer { set; }: Позволяет установить плеер, используемый для воспроизведения видео.
- string CustomFlashVariables { set; }: Позволяет установить переменные, которые передаются в Flash-приложение. Эта строка представляет собой набор пар «ключ=значение», которые разделены символом ‘&’.
- void AddCustomData(string name, Stream data): Добавить дополнительные данные для плеера. Например, source=video.mp4&autoPlay=true&scale=100
- ActivationEvent ActivateOn { get; set}: Событие активирует плеер; возможные значения Click, PageOpen, PageVisible
- void SetContent(Stream stream, string name): Установить видео/аудио данные для воспроизведения.
- void Update(): Создать структуру данных аннотации. Этот метод должен быть вызван последним
- void SetPoster(Stream): Установить постер видео, т.е. изображение, показанное, когда плеер не активен

## Добавить Аннотацию Экрана

Следующий фрагмент кода показывает, как добавить аннотацию экрана в PDF файл:

```java
package com.aspose.pdf.examples;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.*;
import com.aspose.pdf.*;

public class ExampleMultimediaAnnotation {

    // Путь к каталогу документов.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddScreenAnnotation() {
        // Загрузить PDF файл
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        String mediaFile = _dataDir + "input.swf";
        // Создать аннотацию экрана
        ScreenAnnotation screenAnnotation = new ScreenAnnotation(page, new Rectangle(170, 190, 470, 380), mediaFile);
        page.getAnnotations().add(screenAnnotation);

        document.save(_dataDir + "sample_swf.pdf");
    }
}
```


## Добавление звуковой аннотации

Следующий фрагмент кода показывает, как добавить звуковую аннотацию в PDF файл:

```java
          public static void AddSoundAnnotation() {
        // Загрузить PDF файл
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        String mediaFile = _dataDir + "file_example_WAV_1MG.wav";

        // Создать звуковую аннотацию
        SoundAnnotation soundAnnotation = new SoundAnnotation(page, new Rectangle(20, 700, 60, 740), mediaFile);
        soundAnnotation.setColor(Color.getBlue());
        soundAnnotation.setTitle("John Smith");
        soundAnnotation.setSubject("Демонстрация звуковой аннотации");
        soundAnnotation.setPopup(new PopupAnnotation(document));

        page.getAnnotations().add(soundAnnotation);

        document.save(_dataDir + "sample_wav.pdf");
    }
```

## Добавление RichMediaAnnotation

Следующий фрагмент кода показывает, как добавить RichMediaAnnotation в PDF файл:

```java
     public static void AddRichMediaAnnotation() throws FileNotFoundException {
        Document doc = new Document();
        var pathToAdobeApp = "C:\\Program Files (x86)\\Adobe\\Acrobat 2017\\Acrobat\\Multimedia Skins";
        Page page = doc.getPages().add();

        // Назначаем имя видеоданным. Эти данные будут встроены в документ под этим
        // именем и будут ссылаться из flash переменных под этим именем.
        // videoName не должен содержать путь к файлу; это скорее "ключ" для доступа
        // к данным внутри PDF документа

        String videoName = "file_example_MP4_480_1_5MG.mp4";
        String posterName = "file_example_MP4_480_1_5MG_poster.jpg";

        // также мы используем скин для видеоплеера
        String skinName = "SkinOverAllNoFullNoCaption.swf";

        RichMediaAnnotation rma = new RichMediaAnnotation(page, new Rectangle(100, 500, 300, 600));

        // здесь мы указываем поток, содержащий код видеоплеера
        rma.setCustomPlayer(new FileInputStream(pathToAdobeApp + "Players" + "Videoplayer.swf"));

        // составляем строку flash переменных для плеера. обратите внимание, что разные плееры
        // могут иметь разный формат строки flash переменных.
        // Обратитесь к документации для вашего плеера.
        rma.setCustomFlashVariables("source=" + videoName + "&skin=" + skinName);

        // добавляем код скина.
        rma.addCustomData(skinName, new FileInputStream(pathToAdobeApp + "SkinOverAllNoFullNoCaption.swf"));
        // устанавливаем постер для видео
        rma.setPoster(new FileInputStream(_dataDir + posterName));

        // устанавливаем видеоконтент
        rma.setContent(videoName, new FileInputStream(_dataDir + videoName));

        // устанавливаем тип контента (видео)
        rma.setType(RichMediaAnnotation.ContentType.Video);

        // активируем плеер по клику
        rma.setActivateOn(RichMediaAnnotation.ActivationEvent.Click);

        // обновляем данные аннотации. Этот метод должен быть вызван после всех
        // назначений/настроек. Этот метод инициализирует структуру данных аннотации
        // и встраивает необходимые данные.
        rma.update();

        // добавляем аннотацию на страницу.
        page.getAnnotations().add(rma);

        doc.save(_dataDir + "RichMediaAnnotation.pdf");
    }
```


## Получение MultimediaAnnotation

Пожалуйста, попробуйте использовать следующий фрагмент кода, чтобы получить MultimediaAnnotation из PDF документа.

```java
public static void GetMultimediaAnnotation() {
        // Загрузка PDF файла
        Document document = new Document(_dataDir + "RichMediaAnnotation.pdf");

        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new RichMediaAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> mediaAnnotations = annotationSelector.getSelected();

        for (Annotation ma : mediaAnnotations) {
            System.out.println(ma.getAnnotationType() + " " + ma.getRect());
        }
    }
```

## Удаление MultimediaAnnotation

Следующий фрагмент кода показывает, как удалить MultimediaAnnotation из PDF файла.

```java
    public static void DeletePolyAnnotation() {
        // Загрузка PDF файла
        Document document = new Document(_dataDir + "RichMediaAnnotation.pdf");

        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new RichMediaAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> mediaAnnotations = annotationSelector.getSelected();
        for (Annotation ma : mediaAnnotations) {
            page.getAnnotations().delete(ma);
        }
        document.save(_dataDir + "RichMediaAnnotation_del.pdf");
    }
```


## Добавление Аннотаций Виджетов

Интерактивные формы используют [Аннотации Виджетов](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/WidgetAnnotation) для представления внешнего вида полей и управления взаимодействием с пользователем. Мы используем эти элементы формы, которые добавляются в PDF, чтобы облегчить ввод, отправку информации или выполнение некоторых других взаимодействий с пользователем.

Аннотации Виджетов представляют собой графическое изображение поля формы на определенных страницах, поэтому мы не можем создать его напрямую как аннотацию.

Каждая Аннотация Виджета будет иметь соответствующую графику (внешний вид) в зависимости от своего типа. После создания определенные визуальные аспекты могут быть изменены, такие как стиль границы и цвет фона. Другие свойства, такие как цвет текста и шрифт, могут быть изменены через поле, как только они будут прикреплены к нему.

В некоторых случаях вы можете захотеть, чтобы поле отображалось на более чем одной странице, повторяя одно и то же значение.
 В этом случае поля, которые обычно имеют только один виджет, могут иметь несколько виджетов: TextField, ListBox, ComboBox и CheckBox обычно имеют ровно один, в то время как RadioGroup имеет несколько виджетов, по одному на каждую радиокнопку. Кто-то, заполняющий форму, может использовать любой из этих виджетов для обновления значения поля, и это отражается во всех остальных виджетах.

Каждое поле формы для каждого места в документе представляет одну аннотацию виджета. Данные аннотации виджета, специфичные для местоположения, добавляются на конкретную страницу. Каждое поле формы имеет несколько вариаций. Кнопка может быть радиокнопкой, флажком или кнопкой. Виджет выбора может быть списком или комбинированным списком.

В этом примере мы узнаем, как добавить кнопки для навигации в документе.

## Добавить кнопку в документ

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import java.util.*;

public class ExampleWidgetAnnotation {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddButton()
    {
        // Загрузите PDF файл
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        Rectangle rect = new Rectangle(72, 748, 164, 768);
        ButtonField printButton = new ButtonField(page, rect);
        printButton.setAlternateName("Распечатать текущий документ");
        printButton.setColor(Color.getBlack());
        printButton.setPartialName("printBtn1");
        printButton.setNormalCaption("Распечатать документ");

        Border border = new Border(printButton);
        border.setStyle(BorderStyle.Solid);
        border.setWidth(2);

        printButton.setBorder(border);
        printButton.getCharacteristics().setBorder(Color.fromArgb(255, 0, 0, 255));
        printButton.getCharacteristics().setBackground(Color.fromArgb(255, 0, 191, 255));
        document.getForm().add(printButton);

        document.save(_dataDir + "sample_textannot.pdf");
    }
}
```

Эта кнопка имеет границу и установлен фон. Также мы задаем имя кнопки (Name), всплывающую подсказку (AlternateName), метку (NormalCaption) и цвет текста метки (Color).

## Использование действий навигации по документу

Существует более сложный пример использования аннотаций виджетов - навигация по документу в PDF-документе. Это может понадобиться для подготовки презентации PDF-документа.

Этот пример показывает, как создать 4 кнопки:

```java
public static void AddDocumentNavigationActions() {
// Загрузить PDF файл
Document document = new Document(_dataDir + "JSON Fundamenals.pdf");

ButtonField[] buttons = new ButtonField[4];
String[] alternateNames = { "Перейти на первую страницу", "Перейти на предыдущую страницу", "Перейти на следующую страницу", "Перейти на последнюю страницу" };
String[] normalCaptions = { "Первая", "Пред.", "След.", "Последняя" };
int[] actions = { PredefinedAction.FirstPage, PredefinedAction.PrevPage, PredefinedAction.NextPage,
PredefinedAction.LastPage };
Color clrBorder = Color.fromArgb(255, 0, 255, 0);
Color clrBackGround = Color.fromArgb(255, 0, 96, 70);

for (int i = 0; i < 4; i++) {
buttons[i] = new ButtonField(document, new Rectangle(32 + i * 80, 28, 104 + i * 80, 68));
buttons[i].setAlternateName(alternateNames[i]);
buttons[i].setColor(Color.getWhite());
buttons[i].setNormalCaption(normalCaptions[i]);
buttons[i].setOnActivated(new NamedAction(actions[i]));
Border border = new Border(buttons[i]);
border.setStyle(BorderStyle.Solid);
border.setWidth(2);
buttons[i].setBorder(border);
buttons[i].getCharacteristics().setBorder(clrBorder);
buttons[i].getCharacteristics().setBackground(clrBackGround);
}

for (int pageIndex = 1; pageIndex <= 1; pageIndex++)
for (int i = 0; i < 4; i++)
document.getForm().add(buttons[i], "btn" + pageIndex + "_" + (i + 1), pageIndex);

document.getForm().get("btn1_1").setReadOnly(true);
document.getForm().get("btn1_2").setReadOnly(true);

document.getForm().get("btn" + document.getPages().size() + "_3").setReadOnly(true);
document.getForm().get("btn" + document.getPages().size() + "_4").setReadOnly(true);
document.save(_dataDir + "sample_widgetannot_2.pdf");
}
```


## Как удалить аннотацию виджета

Aspose.PDF для Java содержит правила удаления аннотаций из вашего файла:

```java
public static void DeleteWidgetAnnotation() {
        // Загрузить PDF файл
        Document document = new Document(_dataDir + "sample_textannot.pdf");

        // Фильтрация аннотаций с использованием AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(new ButtonField(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> buttonFields = annotationSelector.getSelected();

        // удаление аннотаций
        for (Annotation wa : buttonFields) {
            page.getAnnotations().delete(wa);
        }
        document.save(_dataDir + "sample_widgetannot_del.pdf");
    }
```

В PDF-документах вы можете просматривать и управлять качественным 3D-контентом, созданным с помощью 3D CAD или программного обеспечения для 3D-моделирования и встроенным в PDF-документ.
 Может вращать 3D элементы во всех направлениях, как будто вы держите их в руках.

Зачем вам вообще нужно 3D отображение изображений?

За последние несколько лет технологии совершили огромные прорывы во всех областях благодаря 3D печати. Технологии 3D печати могут быть применены для обучения технологическим навыкам в строительстве, машиностроении, дизайне в качестве основного инструмента. Эти технологии благодаря появлению персональных печатных устройств могут способствовать введению новых форм организации образовательного процесса, увеличению мотивации и формированию необходимых компетенций выпускников и учителей.

Основная задача 3D моделирования — это идея будущего объекта или объекта, потому что для выпуска объекта необходимо понимание его конструктивных особенностей во всех деталях для последовательной регенерации в промышленном дизайне или архитектуре.

## Добавить 3D аннотацию

3D аннотация добавляется с использованием модели, созданной в формате U3D с помощью Aspose.PDF для Java
1. Создайте новый [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document)
1. Загрузите данные нужной 3D модели (в нашем случае "Ring.u3d") для создания [PDF3DContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/PDF3DContent)
1. Создайте объект [3dArtWork](https://reference.aspose.com/pdf/java/com.aspose.pdf/PDF3DArtwork) и свяжите его с документом и 3DContent
1. Настройте объект pdf3dArtWork:

    - 3DLightingScheme - (в примере установим `CAD`)
    - 3DRenderMode - (в примере установим `Solid`)
    - Заполните `ViewArray`, создайте по крайней мере один [3D View](https://reference.aspose.com/pdf/java/com.aspose.pdf/PDF3DView) и добавьте его в массив.

1. Установите 3 основных параметра в аннотации:
    - `page`, на которой будет размещена аннотация,
    - `rectangle`, внутри которого будет аннотация,
    - и объект `3dArtWork`.
1. Для лучшего представления 3D объекта установите рамку границы
1. Установите вид по умолчанию (например - TOP)

1. Добавьте некоторые дополнительные параметры: имя, постер предпросмотра и т. д.
1. Добавьте аннотацию к [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page)
1. Сохраните результат

## Пример

Пожалуйста, ознакомьтесь со следующим фрагментом кода для добавления 3D-аннотации.

```java
    public class Example3DAnnotation
    {
    private static String _dataDir = "/home/aspose/pdf-examples/Samples/";
    public static void Add3dAnnotation()
    {
    // Загрузите PDF файл
    Document document = new Document();
    PDF3DContent pdf3DContent = new PDF3DContent(_dataDir + "Ring.u3d");
    PDF3DArtwork pdf3dArtWork = new PDF3DArtwork(document, pdf3DContent);
    pdf3dArtWork.setLightingScheme(new PDF3DLightingScheme(LightingSchemeType.CAD));
    pdf3dArtWork.setRenderMode(new PDF3DRenderMode(RenderModeType.Solid));

    var topMatrix = new Matrix3D(1,0,0,0,-1,0,0,0,-1,0.10271,0.08184,0.273836);
    var frontMatrix = new Matrix3D(0, -1, 0, 0, 0, 1, -1, 0, 0, 0.332652, 0.08184, 0.085273);
    pdf3dArtWork.getViewArray().add(new PDF3DView(document, topMatrix, 0.188563, "Top")); //1
    pdf3dArtWork.getViewArray().add(new PDF3DView(document, frontMatrix, 0.188563, "Left")); //2

    var page = document.getPages().add();

    var pdf3dAnnotation = new PDF3DAnnotation(page, new Rectangle(100, 500, 300, 700), pdf3dArtWork);
    pdf3dAnnotation.setBorder(new Border(pdf3dAnnotation));
    pdf3dAnnotation.setDefaultViewIndex(1);
    pdf3dAnnotation.setFlags(com.aspose.pdf.AnnotationFlags.NoZoom);
    pdf3dAnnotation.setName("Ring.u3d");
    //установите изображение предпросмотра, если необходимо
    //pdf3dAnnotation.setImagePreview(_dataDir + "sample_3d.png");
    document.getPages().get_Item(1).getAnnotations().add(pdf3dAnnotation);

    document.save(_dataDir+"sample_3d.pdf");
    }
}
```


This code example showed us such a model:

![3D Annotation demo](3d_demo.png)

Этот пример кода показал нам такую модель: