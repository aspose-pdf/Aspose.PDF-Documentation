---
title: Манипулирование PDF Документом
linktitle: Манипулирование PDF Документом
type: docs
weight: 30
url: ru/java/manipulate-pdf-document/
description: Эта статья содержит информацию о том, как проверить PDF документ на соответствие стандарту PDF A, как работать с оглавлением, как установить срок действия PDF и как определить прогресс генерации PDF файла.
lastmod: "2021-06-05"
---

## Проверка PDF Документа на Соответствие Стандарту PDF A (A 1A и A 1B)

Чтобы проверить PDF документ на совместимость с PDF/A-1a или PDF/A-1b, используйте метод [validate(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#validate-java.io.OutputStream-int-) класса [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Этот метод позволяет указать имя файла, в который будет сохранен результат, и требуемый тип проверки из перечисления [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/PdfFormat): PDF_A_1A или PDF_A_1B.

Выходной XML формат является пользовательским форматом Aspose.
 XML содержит набор тегов с именем Problem; каждый тег содержит детали конкретной проблемы. Атрибут ObjectID тега Problem представляет идентификатор объекта, с которым связана эта проблема. Атрибут Clause представляет соответствующее правило в спецификации PDF.

```java
  public static void ValidatePDFDocumentForPDF_A_Standard() {
    // Открыть документ
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // Проверить PDF на соответствие PDF/A-1a
    pdfDocument.validate(_dataDir + "validation-result-A1A.xml", PdfFormat.PDF_A_1A);

    // Сохранить обновленный PDF файл
    // document.save(_dataDir + "UpdatedFile_output.pdf");
  }
```
## Работа с оглавлением

### Добавление оглавления в существующий PDF

Класс ListSection в пакете aspose.pdf позволяет создать оглавление при создании PDF документа с нуля. Чтобы добавить заголовки, которые являются элементами оглавления, используйте класс [aspose.pdf.Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading).

Чтобы добавить оглавление в существующий PDF файл, используйте класс [Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) в пакете com.aspose.pdf. The `com.aspose.pdf` пакет может как создавать новые, так и изменять существующие PDF файлы. Чтобы добавить оглавление в существующий PDF, используйте пакет `com.aspose.pdf`.

Следующий фрагмент кода показывает, как создать оглавление внутри существующего PDF файла.

```java
public static void AddTOCtoExistingPDF() {
    // Загрузить существующие PDF файлы
    Document document = new Document(_dataDir + "sample.pdf");

    // Получить доступ к первой странице PDF файла
    Page tocPage = document.getPages().insert(1);

    // Создать объект для представления информации об оглавлении
    com.aspose.pdf.TocInfo tocInfo = new com.aspose.pdf.TocInfo();
    com.aspose.pdf.TextFragment title = new com.aspose.pdf.TextFragment("Содержание");
    title.getTextState().setFontSize(20);
    title.getTextState().setFontStyle(com.aspose.pdf.FontStyles.Bold);

    // Установить заголовок для оглавления
    tocInfo.setTitle(title);
    tocPage.setTocInfo(tocInfo);

    // Создать строковые объекты, которые будут использоваться в качестве элементов оглавления
    String[] titles = new String[4];
    titles[0] = "Первая страница";
    titles[1] = "Вторая страница";
    titles[2] = "Третья страница";
    titles[3] = "Четвертая страница";
    for (int i = 0; i < 4; i++) {
      // Создать объект заголовка
      com.aspose.pdf.Heading heading2 = new com.aspose.pdf.Heading(1);

      com.aspose.pdf.TextSegment segment2 = new com.aspose.pdf.TextSegment();
      heading2.setTocPage(tocPage);
      heading2.getSegments().add(segment2);

      // Указать целевую страницу для объекта заголовка
      heading2.setDestinationPage(document.getPages().get_Item(i + 2));

      // Целевая страница
      heading2.setTop(document.getPages().get_Item(i + 2).getRect().getHeight());

      // Координата назначения
      segment2.setText(titles[i]);

      // Добавить заголовок на страницу, содержащую оглавление
      tocPage.getParagraphs().add(heading2);
    }
    // Сохранить обновленный документ
    document.save("TOC_Output_Java.pdf");
  }
```
### Установите разные TabLeaderType для разных уровней TOC

Aspose.PDF также позволяет устанавливать различные TabLeaderType для разных уровней TOC. Необходимо установить свойство LineDash FormatArray с соответствующим значением перечисления TabLeaderType следующим образом.

```java
  public static void SetDifferentTabLeaderTypeForTOCLevels() {

    String outFile = "TOC.pdf";

    Document document = new Document();
    Page tocPage = document.getPages().add();

    TocInfo tocInfo = new TocInfo();

    // установить LeaderType

    tocInfo.setLineDash(TabLeaderType.Solid);

    TextFragment title = new TextFragment("Table Of Contents");
    title.getTextState().setFontSize(30);
    tocInfo.setTitle(title);

    // Добавить раздел списка в коллекцию разделов документа Pdf

    tocPage.setTocInfo(tocInfo);

    // Определите формат четырех уровней списка, установив левое поле и
    // настройки формата текста каждого уровня

    tocInfo.setFormatArrayLength(4);
    tocInfo.getFormatArray()[0].getMargin().setLeft(0);
    tocInfo.getFormatArray()[0].getMargin().setRight(30);
    tocInfo.getFormatArray()[0].setLineDash(TabLeaderType.Dot);
    tocInfo.getFormatArray()[0].getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
    tocInfo.getFormatArray()[1].getMargin().setLeft(10);
    tocInfo.getFormatArray()[1].getMargin().setRight(30);
    tocInfo.getFormatArray()[1].setLineDash(TabLeaderType.None);
    tocInfo.getFormatArray()[1].getTextState().setFontSize(10);
    tocInfo.getFormatArray()[2].getMargin().setLeft(20);
    tocInfo.getFormatArray()[2].getMargin().setRight(0);
    tocInfo.getFormatArray()[2].getTextState().setFontStyle(FontStyles.Bold);
    tocInfo.getFormatArray()[3].setLineDash(TabLeaderType.Solid);
    tocInfo.getFormatArray()[3].getMargin().setLeft(30);
    tocInfo.getFormatArray()[3].getMargin().setRight(30);
    tocInfo.getFormatArray()[3].getTextState().setFontStyle(FontStyles.Bold);

    // Создайте раздел в документе Pdf
    Page page = document.getPages().add();

    // Добавьте четыре заголовка в раздел
    for (int Level = 1; Level <= 4; Level++) {
      com.aspose.pdf.Heading heading2 = new com.aspose.pdf.Heading(Level);
      TextSegment segment2 = new TextSegment();

      heading2.getSegments().add(segment2);
      heading2.setAutoSequence(true);
      heading2.setTocPage(tocPage);

      segment2.setText("Sample Heading" + Level);
      heading2.getTextState().setFont(FontRepository.findFont("Arial UnicodeMS"));

      // Добавьте заголовок в Содержание.
      heading2.setInList(true);
      page.getParagraphs().add(heading2);
    }

    // сохранить PDF
    document.save(outFile);
  }
```

### Скрыть номера страниц в оглавлении

Если вы не хотите отображать номера страниц вместе с заголовками в оглавлении, вы можете использовать свойство [IsShowPageNumbers](https://reference.aspose.com/pdf/java/com.aspose.pdf/TocInfo) класса [TOCInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo) как false. Пожалуйста, ознакомьтесь со следующим фрагментом кода, чтобы скрыть номера страниц в оглавлении:

```java
public static void HidePageNumbersInTOC() {
    String outFile = _dataDir + "HiddenPageNumbers_out.pdf";
    Document doc = new Document();
    Page tocPage = doc.getPages().add();
    TocInfo tocInfo = new TocInfo();
    TextFragment title = new TextFragment("Содержание");
    title.getTextState().setFontSize(20);
    title.getTextState().setFontStyle(FontStyles.Bold);
    tocInfo.setTitle(title);

    // Добавить раздел списка в коллекцию разделов документа Pdf
    tocPage.setTocInfo(tocInfo);

    // Определить формат списка из четырех уровней, установив левый отступ и
    // настройки формата текста для каждого уровня

    tocInfo.setShowPageNumbers(false);
    tocInfo.setFormatArrayLength(4);
    tocInfo.getFormatArray()[0].getMargin().setRight(0);
    tocInfo.getFormatArray()[0].getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);

    tocInfo.getFormatArray()[1].getMargin().setLeft(30);
    tocInfo.getFormatArray()[1].getTextState().setUnderline(true);
    tocInfo.getFormatArray()[1].getTextState().setFontSize(10);

    tocInfo.getFormatArray()[2].getTextState().setFontStyle(FontStyles.Bold);
    tocInfo.getFormatArray()[3].getTextState().setFontStyle(FontStyles.Bold);

    Page page = doc.getPages().add();

    // Добавить четыре заголовка в раздел
    for (int Level = 1; Level != 5; Level++) {
      Heading heading2 = new Heading(Level);
      TextSegment segment2 = new TextSegment();
      heading2.setTocPage(tocPage);
      heading2.getSegments().add(segment2);
      heading2.setAutoSequence(true);
      segment2.setText("это заголовок уровня " + Level);
      heading2.setInList(true);
      page.getParagraphs().add(heading2);
    }
    doc.save(_dataDir + outFile);
  }
```


### Настройка номеров страниц при добавлении оглавления

Часто при добавлении оглавления в PDF-документ необходимо настроить нумерацию страниц. Например, может потребоваться добавить префикс перед номером страницы, такой как P1, P2, P3 и так далее. В таком случае, Aspose.PDF для Java предоставляет свойство PageNumbersPrefix класса TocInfo, которое можно использовать для настройки номеров страниц, как показано в следующем примере кода.

```java
  public static void CustomizePageNumbersWhileAddingTOC() {

    String inFile = _dataDir + "sample.pdf";
    String outFile = _dataDir + "42824_out.pdf";

    // Загрузить существующие PDF-файлы
    Document doc = new Document(inFile);
    // Получить доступ к первой странице PDF-файла
    Page tocPage = doc.getPages().insert(1);
    // Создать объект для представления информации об оглавлении
    TocInfo tocInfo = new TocInfo();
    TextFragment title = new TextFragment("Содержание");
    title.getTextState().setFontSize(20);
    title.getTextState().setFontStyle(FontStyles.Bold);

    // Установить заголовок для оглавления
    tocInfo.setTitle(title);
    tocInfo.setPageNumbersPrefix("P");
    tocPage.setTocInfo(tocInfo);

    for (int i = 1; i < doc.getPages().size(); i++) {
      // Создать объект Heading
      Heading heading2 = new Heading(1);
      TextSegment segment2 = new TextSegment();
      heading2.setTocPage(tocPage);
      heading2.getSegments().add(segment2);
      // Указать страницу назначения для объекта заголовка
      heading2.setDestinationPage(doc.getPages().get_Item(i + 1));
      // Страница назначения
      heading2.setTop(doc.getPages().get_Item(i + 1).getRect().getHeight());
      // Координата назначения
      segment2.setText("Страница " + i);
      // Добавить заголовок на страницу с оглавлением
      tocPage.getParagraphs().add(heading2);
    }

    // Сохранить обновленный документ
    doc.save(outFile);
  }
```


## Добавление слоев в PDF файл

Слои могут использоваться в PDF документах различными способами. У вас может быть многоязычный файл, который вы хотите распространять, и текст на каждом языке должен отображаться на разных слоях, а фоновой дизайн - на отдельном слое. Вы также можете создавать документы с анимацией, которая отображается на отдельном слое. Один из примеров может быть добавление лицензионного соглашения к вашему файлу, и вы не хотите, чтобы пользователь просматривал содержимое, пока он не согласится с условиями соглашения.

Aspose.PDF for Java поддерживает добавление слоев в PDF файлы.

Для работы со слоями в PDF файлах используйте следующие члены API.

Класс [Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/Layer) представляет слой и содержит следующие свойства:

- **Name** – имя слоя.
- **Id** – идентификатор слоя.
- **Contents** – список операторов слоя.

После того как объекты [Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/Layer) были определены, добавьте их в коллекцию слоев объекта [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).
 Код ниже показывает, как добавить слои в PDF документ.

```java
public static void AddLayersToPDFFile() {
    Document doc = new Document();
    Page page = doc.getPages().add();
    Layer layer = new Layer("oc1", "Красная линия");
    layer.getContents().add(new com.aspose.pdf.operators.SetRGBColorStroke(1, 0, 0));
    layer.getContents().add(new com.aspose.pdf.operators.MoveTo(500, 700));
    layer.getContents().add(new com.aspose.pdf.operators.LineTo(400, 700));
    layer.getContents().add(new com.aspose.pdf.operators.Stroke());
    page.setLayers(new ArrayList<Layer>());
    page.getLayers().add(layer);
    layer = new Layer("oc2", "Зеленая линия");
    layer.getContents().add(new com.aspose.pdf.operators.SetRGBColorStroke(0, 1, 0));
    layer.getContents().add(new com.aspose.pdf.operators.MoveTo(500, 750));
    layer.getContents().add(new com.aspose.pdf.operators.LineTo(400, 750));
    layer.getContents().add(new com.aspose.pdf.operators.Stroke());
    page.getLayers().add(layer);
    layer = new Layer("oc3", "Синяя линия");
    layer.getContents().add(new com.aspose.pdf.operators.SetRGBColorStroke(0, 0, 1));
    layer.getContents().add(new com.aspose.pdf.operators.MoveTo(500, 800));
    layer.getContents().add(new com.aspose.pdf.operators.LineTo(400, 800));
    layer.getContents().add(new com.aspose.pdf.operators.Stroke());
    page.getLayers().add(layer);
    doc.save("output.pdf");
  
```
## Установить истечение срока действия PDF

Функция истечения срока действия PDF устанавливает, как долго PDF файл действителен. В определенную дату, если кто-то пытается получить к нему доступ, отображается всплывающее окно, объясняющее, что файл устарел и им нужен новый.

Aspose.PDF позволяет установить истечение срока действия при создании и редактировании PDF файлов.

Пример кода ниже показывает, как установить дату истечения срока действия для PDF файла. Вам нужно использовать JavaScript, так как файлы, сохраненные сторонними компонентами (например, OwnerGuard), не могут быть просмотрены на других рабочих станциях без этой утилиты.

PDF файл может быть создан с использованием PDF OwnerGuard с использованием существующего файла с датой истечения срока действия. Но новый файл может быть открыт только на рабочей станции, на которой установлен PDF OwnerGuard. Рабочие станции без PDF OwnerGuard выдадут ошибку ExpirationFeatureError. Например, PDF Reader открывает файл, если OwnerGuard установлен, но Adobe Acrobat возвращает ошибку.

```java
  public static void SetPDFExpiration() {
    Document document = new Document(_dataDir+"sample.pdf");    
    JavascriptAction javaScript = new JavascriptAction(
      "var year=2020;" + 
      "var month=4;" + 
      "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());" + 
      "expiry = new Date(year, month);" + 
      "if (today.getTime() > expiry.getTime())" + 
      "app.alert('The file is expired. You need a new one.');"
      );
    document.setOpenAction(javaScript);
    document.save(_dataDir + "JavaScript-Added.pdf");
  }
```