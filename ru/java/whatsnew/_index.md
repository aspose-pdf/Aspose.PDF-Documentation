---
title: Что нового
linktitle: Что нового
type: docs
weight: 10
url: ru/java/whatsnew/
description: На этой странице представлены самые популярные новые функции в Aspose.PDF для Java, которые были добавлены в последних выпусках.
sitemap:
    changefreq: "monthly"
    priority: 0.8
lastmod: "2021-06-05"
---

## Что нового в Aspose.PDF 24.8

Начиная с версии 24.8, поддержка формата PDF/A-4:

```java

    Document document = new Document(inputPdf);
    // Только документы PDF-2.x могут быть преобразованы в PDF/A-4
    document.convert(new ByteArrayOutputStream(), PdfFormat.v_2_0, ConvertErrorAction.Delete);
    boolean converted = document.convert(logFile, PdfFormat.PDF_A_4, ConvertErrorAction.Delete);
    document.save(outputFile);
```

Также возможно добавить альтернативный текст для штампа изображения:

Свойство AlternativeText было добавлено в ImageStamp - если ему присвоено значение, то при добавлении ImageStamp в документ он будет иметь альтернативный текст.

```java

    String p1_Alt1 = "*** страница 1, Альтернативный текст 1 ***",
                    p1_Alt2 = "*** страница 1, Альтернативный текст 2 ***",
                    p2_Alt1 = "--- страница 1, Альтернативный текст 1 ---",
                    p2_Alt2 = "--- страница 1, Альтернативный текст 2 ---";

    StructTreeRootElement structTreeRoot = document.getTaggedContent().getStructTreeRootElement();

    ImageStamp imageStamp = new ImageStamp(dataDir + "test.jpg");
    imageStamp.setXIndent(100);
    imageStamp.setYIndent(700);
    imageStamp.setWidth(50);
    imageStamp.setHeight(50);
    imageStamp.setQuality(100);
    imageStamp.setAlternativeText(p1_Alt1);

    // На страницу 1
    document.getPages().get_Item(1).addStamp(imageStamp);

    imageStamp.setYIndent(500);
    imageStamp.setAlternativeText(p1_Alt2);
    document.getPages().get_Item(1).addStamp(imageStamp);

    // На страницу 2
    document.getPages().add();
    imageStamp.setXIndent(400);
    imageStamp.setYIndent(700);
    imageStamp.setWidth(50);
    imageStamp.setHeight(50);
    imageStamp.setAlternativeText(p2_Alt1);
    document.getPages().get_Item(2).addStamp(imageStamp);

    imageStamp.setYIndent(500);
    imageStamp.setAlternativeText(p2_Alt2);
    document.getPages().get_Item(2).addStamp(imageStamp);

    // Сохранить документ
    document.save(outFile);
```


Также следующий код показывает, как добавить альтернативный текст в существующие изображения в FigureElements.

```java

    String inFile = dataDir + "46040.pdf";
    String outFile = dataDir + "46040_1_out.pdf";

    Document document = new Document(inFile);

    ITaggedContent taggedContent = document.getTaggedContent();
    StructureElement rootElement = taggedContent.getRootElement();

    Iterator tmp0 = (rootElement.getChildElements()).iterator();
    while (tmp0.hasNext())
    {
        com.aspose.pdf.tagged.logicalstructure.elements.Element element = (com.aspose.pdf.tagged.logicalstructure.elements.Element)tmp0.next();
        if (element instanceof com.aspose.pdf.tagged.logicalstructure.elements.FigureElement)
                {
            com.aspose.pdf.tagged.logicalstructure.elements.FigureElement figureElement = (com.aspose.pdf.tagged.logicalstructure.elements.FigureElement)element;

            // Установить альтернативный текст
            figureElement.setAlternativeText("Альтернативный текст для изображения (техника 1)");
        }
    }

    // Сохранить документ
    document.save(outFile);
```


## Что нового в Aspose.PDF 24.7

Начиная с версии 24.7, в рамках редактирования тегированных PDF были добавлены методы в **Aspose.Pdf.LogicalStructure.Element**:

- Tag (добавление тегов к определенным операторам, таким как изображения, текст и ссылки)
- InsertChild
- RemoveChild
- ClearChilds

Эти методы позволяют редактировать теги PDF-файлов, например:

```java

    Document document = new Document(dataDir + "test.pdf");

    // Получить первую страницу документа.
    Page page = document.getPages().get_Item(1);

    // Инициализация переменных для хранения элементов BDC (Начало контекста словаря) для разных целей.
    BDC imageBdc = null;
    BDC pBdc = null;
    BDC link1Bdc = null;
    BDC link2Bdc = null;
    BDC helloBdc = null;

    // Перебор содержимого страницы.
    for (int i = 1; i <= page.getContents().size(); i++)
    {
        // Получить текущий оператор из содержимого страницы.
        Operator op = page.getContents().get_Item(i);

        // Проверить, является ли оператор экземпляром BDC.
        if (op instanceof BDC) {
        BDC bdc = (BDC)op; // Приведение оператора к типу BDC.
        if (bdc != null)
        {
            // Проверить, является ли MCID (Идентификатор содержимого метки) BDC равным 0.
            if (bdc.getProperties().getMCID()[0] != null && bdc.getProperties().getMCID()[0] == 0)
            {
                helloBdc = bdc; // Сохранить BDC для дальнейшего использования.
            }
        }
    }

    // Проверить, является ли оператор экземпляром Do (Рисовать объект).
    if (op instanceof Do) {
        Do doXobj = (Do)op; // Приведение оператора к типу Do.
        if (doXobj != null)
        {
            // Создать новый BDC для изображения и вставить его в содержимое страницы.
            imageBdc = new BDC("Figure");
            page.getContents().insert(i - 2, imageBdc); // Вставить перед текущим оператором.
            i++; // Увеличить индекс для учета вставленного BDC.
            page.getContents().insert(i + 1, new EMC()); // Вставить EMC (Конец содержимого метки).
            i++; // Увеличить индекс снова.
        }
    }

    // Проверить, является ли оператор экземпляром TextShowOperator (для отображения текста).
    if (op instanceof TextShowOperator) {
        TextShowOperator tx = (TextShowOperator)op; // Приведение оператора к типу TextShowOperator.
        if (tx != null)
        {
            // Проверка на наличие определенного текстового содержимого и вставка соответствующих BDC.
            if (tx.getText().contains("efter Ukendt forfatter er licenseret under"))
            {
                pBdc = new BDC("P");
                page.getContents().insert(i - 1, pBdc); // Вставить перед текущим оператором.
                i++; // Увеличить индекс.
                page.getContents().insert(i + 1, new EMC()); // Вставить EMC.
                i++; // Увеличить индекс.
            }
            if (tx.getText().contains("CC"))
            {
                link1Bdc = new BDC("Link");
                page.getContents().insert(i - 1, link1Bdc); // Вставить перед текущим оператором.
                i++; // Увеличить индекс.
                page.getContents().insert(i + 1, new EMC()); // Вставить EMC.
                i++; // Увеличить индекс.
            }
            if (tx.getText().contains("Dette billede"))
            {
                link2Bdc = new BDC("Link");
                page.getContents().insert(i - 1, link2Bdc); // Вставить перед текущим оператором.
                i++; // Увеличить индекс.
                page.getContents().insert(i + 1, new EMC()); // Вставить EMC.
                i++; // Увеличить индекс.
            }
        }
    }
}
 
    // Получить тегированное содержимое из документа.
    ITaggedContent tagged = document.getTaggedContent();

    // Обработка тегированного содержимого для изменения атрибутов структуры.
    // Получить первый дочерний элемент корневого элемента в тегированном содержимом.
    com.aspose.pdf.tagged.logicalstructure.elements.Element p = tagged.getRootElement().getChildElements().get_Item(1);
    p.clearChilds(); // Очистить существующие дочерние элементы.

    // Тегировать helloBdc с элементом структуры родителя.
    MCRElement mcr = p.tag(helloBdc);

    // Создать и задать атрибуты структуры для тегированного элемента.
    StructureAttributes attrs = com.aspose.pdf.tagged.logicalstructure.elements.InternalHelper.getParentStructureElement(mcr)
            .getAttributes().createAttributes(AttributeOwnerStandard.Layout);
    StructureAttribute attr = new StructureAttribute(AttributeKey.SpaceAfter);
    attr.setNumberValue(30.625); // Задать атрибут пробела после.
    attrs.setAttribute(attr); // Применить атрибут к структуре.

    // Создать новый FigureElement в тегированном содержимом.
    com.aspose.pdf.tagged.logicalstructure.elements.FigureElement figure = tagged.createFigureElement();
    tagged.getRootElement().insertChild(figure, 2); // Вставить элемент фигуры на вторую позицию.
    figure.setAlternativeText("A fly."); // Установить альтернативный текст для фигуры.

    // Тегировать imageBdc с элементом фигуры.
    MCRElement mcr = figure.tag(imageBdc);

    // Получить родительский элемент структуры для указанного MCR (Ссылка на содержимое метки)
    StructureAttributes attrs = com.aspose.pdf.tagged.logicalstructure.elements.InternalHelper.getParentStructureElement(mcr)
    .getAttributes().createAttributes(AttributeOwnerStandard.Layout);

    // Создать новый StructureAttribute для пробела после элемента
    StructureAttribute spaceAfter = new StructureAttribute(AttributeKey.SpaceAfter);
    spaceAfter.setNumberValue(3.625); // Установить значение пробела после 3.625 единиц
    attrs.setAttribute(spaceAfter); // Назначить атрибут пробела после атрибутам структуры

    // Создать новый StructureAttribute для ограничивающего прямоугольника (BBox)
    StructureAttribute bbox = new StructureAttribute(AttributeKey.BBox);
    bbox.setArrayNumberValue(new Double[][] { new Double[] { (71.9971) }, new Double[] { (375.839) }, new Double[] { (523.299) }, new Double[] { (714.345) } });
    // Установить значения ограничивающего прямоугольника для атрибута структуры
    attrs.setAttribute(bbox); // Назначить атрибут ограничивающего прямоугольника атрибутам структуры

    // Создать новый StructureAttribute для размещения
    StructureAttribute placement = new StructureAttribute(AttributeKey.Placement);
    placement.setNameValue(AttributeName.Placement_Block); // Установить тип размещения в блок
    attrs.setAttribute(placement); // Назначить атрибут размещения атрибутам структуры

    // Получить четвертый дочерний элемент из корневого элемента тегированной структуры
    StructureElement p2 = (StructureElement)tagged.getRootElement().getChildElements().get_Item(3);
    p2.clearChilds(); // Очистить любые существующие дочерние элементы из p2

    // Создать новый SpanElement для добавления в p2
    SpanElement span1 = tagged.createSpanElement();

    // Создать атрибуты структуры для элемента span
    StructureAttributes attrs = span1.getAttributes().createAttributes(AttributeOwnerStandard.Layout);

    // Создать новый StructureAttribute для типа украшения текста
    StructureAttribute textDecorationType = new StructureAttribute(AttributeKey.TextDecorationType);
    textDecorationType.setNameValue(AttributeName.TextDecorationType_Underline); // Установить украшение текста подчеркиванием
    attrs.setAttribute(textDecorationType); // Назначить атрибут типа украшения текста атрибутам структуры

    // Создать новый StructureAttribute для толщины украшения текста
    StructureAttribute textDecorationThickness = new StructureAttribute(AttributeKey.TextDecorationThickness);
    textDecorationThickness.setNumberValue(0); // Установить толщину украшения текста в 0
    attrs.setAttribute(textDecorationThickness); // Назначить атрибут толщины украшения текста атрибутам структуры

    // Создать новый StructureAttribute для цвета украшения текста
    StructureAttribute textDecorationColor = new StructureAttribute(AttributeKey.TextDecorationColor);
    textDecorationColor.setArrayNumberValue(new Double[][] { new Double[] { (0.0196075) }, new Double[] { (0.384308) }, new Double[] { (0.756866) } });
    // Установить значения RGB цвета для украшения текста
    attrs.setAttribute(textDecorationColor); // Назначить атрибут цвета украшения текста атрибутам структуры

    p2.appendChild(span1); // Добавить элемент span1 в p2


    // Создать новый элемент MCR и тегировать его с pBdc
    MCRElement mcr = p2.tag(pBdc);
    // Получить родительский элемент структуры MCR и создать атрибуты компоновки
    StructureAttributes attrs = com.aspose.pdf.tagged.logicalstructure.elements.InternalHelper.getParentStructureElement(mcr)
    .getAttributes().createAttributes(AttributeOwnerStandard.Layout);

    // Создать новый StructureAttribute для выравнивания текста
    StructureAttribute textAlign = new StructureAttribute(AttributeKey.TextAlign);
    textAlign.setNameValue(AttributeName.TextAlign_Center); // Установить выравнивание текста по центру
    attrs.setAttribute(textAlign); // Назначить атрибут выравнивания текста атрибутам структуры

    // Создать новый StructureAttribute для пробела после элемента
    StructureAttribute spaceAfter = new StructureAttribute(AttributeKey.SpaceAfter);
    spaceAfter.setNumberValue(21.75); // Установить значение пробела после 21.75 единиц
    attrs.setAttribute(spaceAfter); // Назначить атрибут пробела после атрибутам структуры


    // Создать новый SpanElement для добавления в p2
    SpanElement span2 = tagged.createSpanElement();

    // Создать атрибуты структуры для элемента span
    StructureAttributes attrs = span2.getAttributes().createAttributes(AttributeOwnerStandard.Layout);

    // Создать новый StructureAttribute для типа украшения текста
    StructureAttribute textDecorationType = new StructureAttribute(AttributeKey.TextDecorationType);
    textDecorationType.setNameValue(AttributeName.TextDecorationType_Underline); // Установить украшение текста подчеркиванием
    attrs.setAttribute(textDecorationType); // Назначить атрибут типа украшения текста атрибутам структуры

    // Создать новый StructureAttribute для цвета украшения текста, используя указанный ключ.
    StructureAttribute textDecorationColor = new StructureAttribute(AttributeKey.TextDecorationColor);

    // Установить значение массива чисел для атрибута цвета украшения текста.
    // Цвет представлен в виде массива значений RGB, где каждое значение является Double.
    textDecorationColor.setArrayNumberValue(new Double[][] {
    new Double[] { (0.0196075) }, // Красная компонента
    new Double[] { (0.384308) },  // Зеленая компонента
    new Double[] { (0.756866) }   // Синяя компонента
    });

    // Установить атрибут цвета украшения текста в объект attrs.
    attrs.setAttribute(textDecorationColor);

    // Добавить дочерний элемент span ко второму элементу.
    p2.appendChild(span2);

    // Создать новый экземпляр LinkElement для второй ссылки.
    LinkElement link2 = tagged.createLinkElement();

    // Присвоить уникальный идентификатор элементу ссылки, используя случайно сгенерированный UUID.
    link2.setId(UUID.randomUUID().toString());

    // Добавить элемент link2 в качестве дочернего элемента span2.
    span2.appendChild(link2);

    // Тегировать элемент link2 с соответствующей аннотацией из аннотаций страницы.
    link2.tag(page.getAnnotations().get_Item(1));

    // Тегировать элемент link2 с дополнительными метаданными или контекстом (link2Bdc).
    link2.tag(link2Bdc);

    // Создать еще один экземпляр LinkElement для первой ссылки.
    LinkElement link1 = tagged.createLinkElement();

    // Присвоить уникальный идентификатор элементу link1, используя случайно сгенерированный UUID.
    link1.setId(UUID.randomUUID().toString());

    // Добавить элемент link1 в качестве дочернего элемента span1.
    span1.appendChild(link1);

    // Тегировать элемент link1 с соответствующей аннотацией из аннотаций страницы.
    link1.tag(page.getAnnotations().get_Item(2));

    // Тегировать элемент link1 с дополнительными метаданными или контекстом (link1Bdc).
    link1.tag(link1Bdc);

    // Удалить первый дочерний элемент из корневого элемента тегированного документа.
    tagged.getRootElement().removeChild(0);

    // Сохранить документ в указанную выходную директорию с именем файла "_out.pdf".
    document.save(dataDir + "_out.pdf");

```


## Что нового в Aspose.PDF 24.6

Начиная с версии 24.6 Aspose.PDF для Java позволяет подписывать PDF с использованием java.security.cert.X509Certificate, java.security.PrivateKey:

Этот код извлекает сертификат и закрытый ключ из хранилища сертификатов, а затем использует их для применения цифровой подписи на первой странице PDF-документа.

```java

    KeyStore trustStore = KeyStore.getInstance("Windows");
    trustStore.load(null, null);
    java.security.cert.X509Certificate certificate = (java.security.cert.X509Certificate) trustStore.getCertificate("ProfMoriarty");
    PrivateKey key = (PrivateKey) trustStore.getKey("ProfMoriarty", null);

    PdfFileSignature pdfSign = new PdfFileSignature(getInputPdf());
    Signature signature = new ExternalSignature(certificate, key);
    pdfSign.sign(1, "reasonTest", "contactTest", "locationTest", true, new java.awt.Rectangle(1, 691, 100, 100), signature);

    pdfSign.save("PDFJAVA.pdf");
    pdfSign.close();
```

## Что нового в Aspose.PDF 24.5

С момента выпуска версии 24.5 были реализованы плагины редактора форм.

**Как редактировать формы в PDF с помощью редактора форм**

- Установите свои лицензионные ключи
- Создайте экземпляр класса FormEditor, который предоставляет методы для манипуляции формами PDF
- Создайте экземпляр класса FormEditorAddOptions, который указывает параметры для добавления полей формы в PDF-документ
- Добавьте источник входного и выходного файла в объект FormEditorAddOptions, используя класс FileDataSource, который представляет путь к файлу или поток
- Вызовите метод Process объекта FormEditor, передав объект FormEditorAddOptions в качестве параметра
- Получите доступ к результату, используя ResultContainer.resultCollection

```java

    // Укажите пути к входному и выходному файлам PDF.
    String inputPath = "sample.pdf";
    String outputPath = "out.pdf";

    // Создайте экземпляр плагина FormEditor.
    FormEditor pdfFormPlugin = new FormEditor();

    // Создайте параметры для добавления полей формы.
    ArrayList<FormFieldCreateOptions> options = new ArrayList<FormFieldCreateOptions>();

    // Создайте текстовое поле формы.
    FormTextBoxFieldCreateOptions tmp1 = new FormTextBoxFieldCreateOptions(1, new Rectangle(10, 600, 90, 610));
    tmp1.setValue("TextBoxField");
    tmp1.setColor(Color.getChocolate());
    tmp1.setPartialName("TexBoxField");
    options.add(tmp1);

    // Создайте поле формы выпадающего списка.
    FormComboBoxFieldCreateOptions tmp2 = new FormComboBoxFieldCreateOptions(1, new Rectangle(310, 800, 350, 815));

    tmp2.setColor(com.aspose.pdf.Color.getRed());
    tmp2.setEditable(new Boolean[]{true});
    tmp2.setDefaultAppearance(new DefaultAppearance("Arial Bold", 12, java.awt.Color.GREEN));
    ArrayList<String> list1 = new ArrayList<String>();
    list1.add("p1");
    list1.add("p2");
    list1.add("p3");
    tmp2.setOptions(list1);
    tmp2.setSelected(new Integer[]{2});
    tmp2.setPartialName("ComboBoxField");
    options.add(tmp2);

    // Создайте поле формы флажка.
    FormCheckBoxFieldCreateOptions tmp3 = new FormCheckBoxFieldCreateOptions(1, new Rectangle(10, 700, 90, 715));
    tmp3.setValue("CheckBoxField 1");
    tmp3.setPartialName("CheckBoxField_1");
    tmp3.setColor(Color.getBlue());
    options.add(tmp3);


    // Создайте поле формы флажка.
    FormCheckBoxFieldCreateOptions tmp4 = new FormCheckBoxFieldCreateOptions(1, new Rectangle(100, 700, 190, 715));
    tmp4.setChecked(new Boolean[]{true});
    tmp4.setValue("CheckBoxField 2");
    tmp4.setDefaultAppearance(new DefaultAppearance("Arial Bold", 12, java.awt.Color.GREEN));
    tmp4.setStyle(new Integer[]{BoxStyle.Cross});
    options.add(tmp4);


    // Создайте поле формы флажка.
    FormCheckBoxFieldCreateOptions tmp5 = new FormCheckBoxFieldCreateOptions(1, new Rectangle(200, 700, 390, 715));
    tmp5.setPartialName("CheckBoxField_3");
    tmp5.setValue("CheckBoxField 3");
    tmp5.setStyle(new Integer[]{BoxStyle.Star});
    tmp5.setChecked(new Boolean[]{true});
    tmp5.setTextHorizontalAlignment(new HorizontalAlignment[]{HorizontalAlignment.Center});
    options.add(tmp5);

    FormEditorAddOptions opt = new FormEditorAddOptions(options);

    // Добавьте входные и выходные файлы в параметры.
    opt.addInput(new FileDataSource(inputPath));
    opt.addOutput(new FileDataSource(outputPath));

    // Обработайте поля формы, используя плагин.
    ResultContainer results = pdfFormPlugin.process(opt);
```


Этот выпуск позволяет нам работать со слоями PDF. Например:

- заблокировать слой PDF
- извлечь элементы слоя PDF
- уплощить многослойный PDF
- объединить все слои внутри PDF в один

**Заблокировать слой PDF**

С версии 24.5 вы можете открыть PDF, заблокировать определенный слой на первой странице и сохранить документ с изменениями. Были добавлены два новых метода и одно свойство:

Layer.Lock(); - Блокирует слой.  
Layer.Unlock(); - Разблокирует слой.  
Layer.Locked; - Свойство, указывающее состояние блокировки слоя.

```java

    Document document = new Document(input);
    Page page = document.getPages().get_Item(1);
    Layer layer = page.getLayers().get(0);

    layer.lock();

    document.save(output);
```

**Извлечение элементов слоя PDF**

Библиотека Aspose.PDF для Java позволяет извлекать каждый слой с первой страницы и сохранять каждый слой в отдельный файл.

Чтобы создать новый PDF из слоя, можно использовать следующий фрагмент кода:

```java

    Document document = new Document(inputPath);
    java.util.List<Layer> layers = document.getPages().get_Item(1).getLayers();

    for (Layer layer : layers)
    {
        layer.save(outputPath);
    }
```


**Уплощение слоистого PDF**

Библиотека Aspose.PDF для Java открывает PDF, проходит через каждый слой на первой странице и уплощает каждый слой, делая его постоянным на странице.

```java

    Document document = new Document(input);
    Page page = document.getPages().get_Item(1);

    for (Layer layer : page.getLayers())
    {
        layer.flatten(true);
    }
    document.save(output);
```

Метод Layer.flatten(boolean cleanupContentStream) принимает булевый параметр, который указывает, следует ли удалять маркеры группы необязательного содержимого из потока содержимого. Установка параметра cleanupContentStream в значение false ускоряет процесс уплощения.

**Объединение всех слоев в PDF в один**

Библиотека Aspose.PDF для Java позволяет объединять все слои PDF или определенный слой на первой странице в новый слой и сохранять обновленный документ.

Были добавлены два метода для объединения всех слоев на странице:

- void mergeLayers(String newLayerName);

- void mergeLayers(String newLayerName, String newOptionalContentGroupId);

Второй параметр позволяет переименовать маркер группы необязательного содержимого. Значение по умолчанию - "oc1" (/OC /oc1 BDC).

```java

    Document document = new Document(input);
    Page page = document.getPages().get_Item(1);
    page.mergeLayers("NewLayerName");

    // Или page.mergeLayers("NewLayerName", "OC1");

    document.save(output);
```

## Что нового в Aspose.PDF 24.4

Этот выпуск представил Java плагины для PDF:

- Плагин для упрощения формы

```java

    FormFlattener pdfFormPlugin = new FormFlattener();

    FormFlattenAllFieldsOptions opt = new FormFlattenAllFieldsOptions();

    opt.addInput(new FileDataSource("sample.pdf"));
    opt.addOutput(new FileDataSource("sample-flat.pdf"));

    ResultContainer result = pdfFormPlugin.process(opt);

    // Проверка результата.
    java.util.List < IOperationResult > resultCollectionInternal = result.getResultCollection();
```

- Экспортёр форм

```java

    Rectangle rect = new com.aspose.pdf.Rectangle(0, 220, 600, 330);

    // Использование плагина.
    FormExporter pdfFormPlugin = new FormExporter();
    SelectField selectField = new SelectField() {
      public boolean invoke(Field field) {
        return field instanceof TextBoxField && field.getPageIndex() == 2 && rect.isInclude(field.getRect(), 0);
      }
    };
    FormExporterValuesToCsvOptions opt = new FormExporterValuesToCsvOptions(selectField, ';');

    opt.addInput(new FileDataSource(inputFileNameWithFields));
    opt.addInput(new FileDataSource(getInputPath("document-1.pdf")));
    opt.addInput(new FileDataSource(getInputPath("document-2.pdf")));
    opt.addInput(new FileDataSource(getInputPath("document-3.pdf")));
    opt.addOutput(new FileDataSource(getOutputPath("out.csv")));
    ResultContainer result = pdfFormPlugin.process(opt);

    // Проверка результата.
    System.out.println(result.getResultCollectionInternal().size() > 0);
    System.out.println(result.getResultCollectionInternal().get_Item(0).isFile());
    System.out.println(result.getResultCollectionInternal().get_Item(0).getData().toString());
```


- Плагин слияния

```java

    String input1 = "sample.pdf";
    String input2 = "sample.pdf";

    String output = "TestMergeFileAndStream_ResultAsFile.pdf";

    Merger merger = new Merger();

    MergeOptions opt = new MergeOptions();
    opt.addInput(new FileDataSource(input1));
    opt.addInput(new StreamDataSource(new FileInputStream(input2)));

    opt.addOutput(new FileDataSource(output));

    ResultContainer results = merger.process(opt);

    System.out.println(results.getResultCollection().size());
    System.out.println(results.getResultCollection().get(0).isFile());
```

- Плагин оптимизации

Как уменьшить размер PDF документов?

```java

    String input = "Test.pdf";
    String output = "Optimized.pdf";

    Optimizer optimizer = new Optimizer();

    OptimizeOptions opt = new OptimizeOptions();
    opt.addInput(new FileDataSource(input));
    opt.addOutput(new FileDataSource(output));

    optimizer.process(opt);
```

Как изменить размер PDF документов?

```java

    String input = "sample.pdf";
    String output = "ResizeMain.pdf";

    Optimizer organizer = new Optimizer();

    ResizeOptions opt = new ResizeOptions();
    opt.addInput(new FileDataSource(input));
    opt.addOutput(new FileDataSource(output));

    opt.setPageSize(PageSize.getA1());

    organizer.process(opt);
```


Как вращать PDF-документы?

```java

    String input = "sample.pdf";
    String output = "OptimizerRotateMain.pdf";

    Optimizer optimizer = new Optimizer();

    RotateOptions opt = new RotateOptions();
    opt.addInput(new FileDataSource(input));
    opt.addOutput(new FileDataSource(output));
    opt.setRotation(Rotation.on90);

    ResultContainer results = optimizer.process(opt);
```

## Что нового в Aspose.PDF 24.3

Начиная с версии 24.3 реализован поиск через список фраз в TextFragmentAbsorber.

```java

    String[] expressions = new String[] {
      //обнаружение номера телефона
      "\\b\\d{3}-\\d{3}-\\d{4}\\b",
      //обнаружение номера карты
      "\\b(?:\\d[ -]*?){13,16}\\b"
    };
    Document document = new Document(input);

    TextFragmentCollection newTextFragmentCollection = new TextFragmentCollection();

    Pattern[] regexes = new Pattern[6];
    for (int i = 0; i < expressions.length; i++) {
      regexes[i] = Pattern.compile(expressions[i], Pattern.CASE_INSENSITIVE);
    }
    TextFragmentAbsorber newAbsorber = new TextFragmentAbsorber(regexes, new TextSearchOptions(true));
    document.getPages().accept(newAbsorber);
    HashMap < Pattern, TextFragmentCollection > map = newAbsorber.getRegexResults();
```


Следующая функция добавляет возможность конвертации таблиц для конвертера PDF в Markdown

```java

    Document doc = new Document(dataDir + "56201.pdf");
    MarkdownSaveOptions saveOptions = new MarkdownSaveOptions();
    doc.save(dataDir + "56201.md", saveOptions);
```

## Что нового в Aspose.PDF 24.2

С версии 24.2 возможно добавление водяного знака в PDF с AcroForms. TextStamp подходит для использования с файлами AcroForm. Если вы используете TextStamp для файлов XFA, текст отображается на странице как в обычном PDF файле (его можно увидеть в тех просмотрщиках PDF, которые не могут читать файлы XFA, например, в браузере Chrome). Чтобы добавить текст в файл XFA, его необходимо изменить во внутреннем XML файле XFA.

```java

    String sourceName = dataDir + "551.3xfa.pdf";
    String targetName = dataDir + "output_2_" + BuildVersionInfo.AssemblyVersion + ".pdf";

    Document pdfDocument = new Document(sourceName);
    XFA xfa = pdfDocument.getForm().getXFA();

    String watermark =
    "<subform>" +
    "<draw rotate=\"90\" x=\"100px\" y=\"100px\">" +
    "<value>" +
    "<text>Sample Stamp</text>\n" +
    "</value>" +
    "<font typeface=\"Arial\" size=\"14px\" weight=\"bold\" posture=\"italic\">" +
    "<fill>" +
    "<color value=\"0,128,0\"/>" +
    "</fill>" +
    "</font>" +
    "</draw>" +
    "</subform>";

    xfa.appendToTemplate("//tpl:pageArea", watermark);

    pdfDocument.save(targetName);
    pdfDocument.close();
```


Установить StateModel для Аннотации
Мы можем использовать setReviewState и setMarkedState из класса MarkupAnnotation для установки необходимого состояния.
Все аннотации разметки имеют доступную опцию Установить Состояние.

```java

    // Открыть исходный PDF документ
    Document pdfDocument = new Document();
    pdfDocument.getPages().add();
    // Создать аннотацию
    TextAnnotation textAnnotation = new TextAnnotation(pdfDocument.getPages().get_Item(1), new Rectangle(200,
            400, 400, 600));

    //Установить заголовок аннотации
    textAnnotation.setTitle("Пример заголовка аннотации");

    //Установить тему аннотации
    textAnnotation.setSubject("Пример темы");
    //Указать содержимое аннотации
    textAnnotation.setContents("Пример содержимого для аннотации");
    textAnnotation.setOpen(true);
    textAnnotation.setIcon(TextIcon.Key);
    com.aspose.pdf.Border border = new com.aspose.pdf.Border(textAnnotation);
    border.setWidth(5);
    border.setDash(new Dash(1, 1));
    textAnnotation.setBorder(border);
    String userName1 = "Aspose1";
    textAnnotation.setReviewState(AnnotationState.Rejected, userName1);
    textAnnotation.setRect(new Rectangle(200, 400, 400, 600));

    //Добавить аннотацию в коллекцию аннотаций страницы
    pdfDocument.getPages().get_Item(1).getAnnotations().add(textAnnotation);
    pdfDocument.processParagraphs();

    //Сохранить выходной файл
    pdfDocument.save(dataDir + "output_24_2_Rejected.pdf");

    pdfDocument = new Document(dataDir + "output" + version + "3.pdf");
    TextAnnotation textAnnotation2 = (TextAnnotation) pdfDocument.getPages().get_Item(1).getAnnotations().get_Item(1);

    String userName2 = "Aspose2";
    textAnnotation2.setReviewState(AnnotationState.Accepted, userName2);
    pdfDocument.save(dataDir + "output_24_2_Rejected_and_Accepted.pdf");
```


С версии 24.2 реализована конвертация OFD в PDF:

```java

    Document document = new Document(inputPath, new OfdLoadOptions());
    document.save(outputPath);
```

## Что нового в Aspose.PDF 24.1

С релиза 24.1 реализована конвертация PDF в Markdown:

```java

    final Document doc = new Document(inputPdfPath);
    MarkdownSaveOptions saveOptions = new MarkdownSaveOptions();
    saveOptions.setHeadingRecognitionStrategy(HeadingRecognitionStrategy.Outlines);
    doc.save(markdownOutputFilePath, saveOptions);
```

Также в 24.1 реализовано прерывание потока с использованием InterruptMonitor.

```java

    final InterruptMonitor monitor = new InterruptMonitor();

    new Thread(new Runnable() {

      public void run() {

        InterruptMonitor.setThreadLocalInstance(monitor);
        Document document = new Document();

        try {
          Page page = document.getPages().insert(1);
          PageInfo pageInfo = page.getPageInfo();
          pageInfo.setLandscape(true);
          Table topicTable = new Table();
          topicTable.setBorder(new BorderInfo(BorderSide.All, 0.5 f, Color.getBlack()));
          topicTable.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.5 f, Color.getBlack()));
          topicTable.setColumnWidths("5% 10% 5% 60% 10% 10%");
          topicTable.setRepeatingRowsCount(1);

          Row topicRow = topicTable.getRows().add();

          topicRow.getCells().add("текст");
          topicRow.getCells().add("текст");
          topicRow.getCells().add("текст");
          topicRow.getCells().add("текст");
          topicRow.getCells().add("текст");
          topicRow.getCells().add("текст");

          // конвертация foreach в while
          Iterator tmp0 = (topicRow.getCells()).iterator();
          while (tmp0.hasNext()) {
            Cell cell = (Cell) tmp0.next();
            cell.setVerticalAlignment(VerticalAlignment.Center);
            cell.setAlignment(HorizontalAlignment.Center);
          }

          Row row2 = topicTable.getRows().add();
          row2.getCells().add("текст");
          row2.getCells().add("текст");
          row2.getCells().add("текст");
          String LongText = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus.";
          row2.getCells().add(LongText);
          row2.getCells().add("текст");
          row2.getCells().add("текст");
          page.getParagraphs().add(topicTable);
          document.save(dataDir + "out" + version + ".pdf");

        } catch (com.aspose.pdf.exceptions.OperationCanceledException ex) {
          System.out.println("Прерывание сохранения потока в " + System.currentTimeMillis());
        } finally {
          if (document != null) {
            document.close();
          }
        }

      }

    }).start();

    System.out.println("Процесс запущен в потоке в " + System.currentTimeMillis());

    // Тайм-аут должен быть меньше времени, необходимого для полного сохранения документа (без прерывания).
    Thread.sleep(500);

    // Прерывание процесса
    monitor.interrupt();

    System.out.println("Прерывание сохранения потока в " + System.currentTimeMillis());
```


## Что нового в Aspose.PDF 23.12

Форма может быть найдена, и текст может быть заменен, используя следующий фрагмент кода:

```java

    Document document = new Document(input);
    String expectedText = "This is a text added while creating new PDF in Kofx Power PDF Standard.";

    XFormCollection forms = document.getPages().get_Item(1).getResources().getForms();

    Iterator tmp0 = (forms).iterator();
    while (tmp0.hasNext()) {
      XForm form = (XForm) tmp0.next();
      if ("Typewriter".equals(form.getIT()) && "Form".equals(form.getSubtype())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.visit(form);

        Iterator tmp1 = (absorber.getTextFragments()).iterator();
        while (tmp1.hasNext()) {
          TextFragment fragment = (TextFragment) tmp1.next();
          fragment.setText("");
        }
      }
    }

    document.save(output);
```            

Или, форма может быть полностью удалена:

```java

    Document document = new Document(input);
    XFormCollection forms = document.getPages().get_Item(1).getResources().getForms();

    //foreach to while statements conversion
    Iterator tmp0 = (forms).iterator();
    while (tmp0.hasNext()) {
        XForm form = (XForm) tmp0.next();
        if ("Typewriter".equals(form.getIT()) && "Form".equals(form.getSubtype())) {
            String name = forms.getFormName(form);
            forms.delete(name);
        }
    }

    document.save(output);
```


Еще один вариант удаления формы:

```java

    Document document = new Document(input);

    XFormCollection forms = document.getPages().get_Item(1).getResources().getForms();

    for (int i = 1; i <= forms.size(); i++) {
        if ("Typewriter".equals(forms.get_Item(i).getIT()) && "Form".equals(forms.get_Item(i).getSubtype())) {
            forms.delete(forms.get_Item(i).getName());
        }
    }

    document.save(output);
```

- Все формы можно удалить, используя следующий фрагмент кода:

```java

    Document document = new Document(input);

    XFormCollection forms = document.getPages().get_Item(1).getResources().getForms();

    forms.clear();

    document.save(output);
```

## Что нового в Aspose.PDF 23.11

С этого выпуска стала возможна возможность удаления скрытого текста из PDF-файла:

```java

    Document document = new Document(inputFile);

    TextFragmentAbsorber textAbsorber = new TextFragmentAbsorber();
    textAbsorber.setTextReplaceOptions(new TextReplaceOptions(TextReplaceOptions.ReplaceAdjustment.None));
    document.getPages().accept(textAbsorber);

    msStringBuilder result = new msStringBuilder();

    //foreach to while statements conversion
    Iterator tmp0 = (textAbsorber.getTextFragments()).iterator();
        while (tmp0.hasNext()) {
            TextFragment fragment = (TextFragment) tmp0.next();
            if (fragment.getTextState().isInvisible()) {
                result.append(fragment.getText());
                fragment.setText("");
            }
        }

    document.save(outputFile);
```


## Что нового в Aspose.PDF 23.10

Текущее обновление представляет три версии удаления тегов из тегированных PDF-документов.

- Удаление некоторого узлового элемента из documentElement (корневой элемент дерева):

```java
    Document document = new Document(inputPath);
    RootElement structure = document.getLogicalStructure();
    Element documentElement = structure.getChildren().get_Item(0);
    Element structElement = (documentElement.getChildren().getCount() > 1) ?  documentElement.getChildren().get_Item(1) : null;
    documentElement.getChildren().remove(structElement);
    // Вы также можете удалить сам structElement
                //if (structElement != null)
                //{
                //    structElement.remove();
                //}
    document.save(outputPath);
```

- Удалить все теги отмеченных элементов из документа, но сохранить элементы структуры:

```java
    Document document = new Document(inputPath);
    RootElement structure = document.getLogicalStructure();
    Element root= structure.getChildren().get_Item(0);
    Queue<Element> queue = new ArrayDeque<Element>();
    queue.add(root);
    for (Element element : structure.getChildren() ) {
        queue.add(element);
        for (Element child : element.getChildren())
        {
            queue.add(child);
        }
    }
    for (Element element:queue ) {
        if (element instanceof TextElement  || element instanceof FigureElement)
            element.remove();
    }
    document.save(outputPath);
```


- Удалите теги полностью:

```java

    Document document = new Document(inputPath);
    RootElement structure = document.getLogicalStructure();
    Element root = structure.getChildren().get_Item(0);
    root.remove();
    document.save(outputPath);
```

Мы реализовали новую функцию для измерения высоты символов. Используйте следующий код для измерения высоты символа:

```java

    Document doc = new Document("input.pdf");
    TextFragmentAbsorber absorber = new TextFragmentAbsorber();
    absorber.visit(doc.getPages().get_Item(1));
    double height = absorber.getTextFragments().get_Item(1).getTextState().measureHeight('h')
```

Обратите внимание, что измерение основано на шрифте, встроенном в документ. Если какая-либо информация о размере отсутствует, этот метод возвращает 0.

## Что нового в Aspose.PDF 23.9

Начиная с версии 23.9 поддерживается удаление дочерней аннотации из заполняемого поля.

пример 1:

```java

    String input = "55343_1.pdf";
    Document doc = new Document(input);
    final String fieldName = "1 Vehicle Identification Number";
    Field field = (Field) doc.getForm().get_Item(fieldName);
    System.out.println(0 == field.size());
    Rectangle rect = field.getRect();
    doc.getForm().addFieldAppearance(field, 2, rect);
    System.out.println(2 == field.size());

    field = (Field) doc.getForm().get_Item(fieldName);
    System.out.println(2 == field.size());
    doc.getForm().removeFieldAppearance(field, 1);

    System.out.println(0 == field.size());
    field = (Field) doc.getForm().get_Item(fieldName);
    System.out.println(0 == field.size());
```


example 2:

```java

    {
    String option1 = "опция 1";
    String option2 = "опция 2";
    String outputPdf = "output.pdf";

    final Document document = new Document();
    try /*JAVA: использовался*/ {
        Page page = document.getPages().add();

        CheckboxField checkbox = new CheckboxField(page, new Rectangle(50, 50, 70, 70));

        // Установить значение первой опции группы флажков
        checkbox.setExportValue(option1);
        checkbox.addOption(option2);
        document.getForm().add(checkbox);
        java.util.List < String > tmp0 = new ArrayList < String > ();
        tmp0.add("Off");
        tmp0.add(option1);
        tmp0.add(option2);
        System.out.println(collectionAssert_AreEqual(tmp0, checkbox.getAllowedStates()));
        checkbox.setValue(option2);

        WidgetAnnotation f = document.getForm().get_Item(1);
        document.getForm().removeFieldAppearance((Field) f, 2);

        checkbox = (CheckboxField) document.getForm().get_Item(1);
        java.util.List < String > tmp1 = new java.util.ArrayList < String > ();
        tmp1.add("Off");
        tmp1.add(option1);
        System.out.println(collectionAssert_AreEqual(tmp1, checkbox.getAllowedStates()));

        document.save(outputPdf);
    } finally {
        if (document != null)(document).close();
    }
    }
    public static boolean collectionAssert_AreEqual(java.util.List < String > value1,
    java.util.List < String > value2) {
    if (value1.size() == value2.size()) {
        for (int i = 0; i < value1.size(); i++) {
        if (!value1.get(i).equals(value2.get(i)))
            return false;
        }
    } else {
        return false;
    }
    return true;
    }
```


Добавление изображения с использованием ImageFilterType.Flate не сохраняет прозрачность.

```java

    Document document = new Document();
    Page page = document.getPages().add();

    FileInputStream stream = new FileInputStream(("55037_1.png"));

    page.getResources().getImages().addWithImageFilterType(stream, ImageFilterType.Flate);
    page.getContents().add(new GSave());
    Rectangle rectangle = new Rectangle(413, 428, 548, 564);
    Matrix matrix = new Matrix(
      new double[] {
        rectangle.getURX() - rectangle.getLLX(), 0, 0, rectangle.getURY() - rectangle.getLLY(), rectangle.getLLX(), rectangle.getLLY()
      });

    page.getContents().add(new ConcatenateMatrix(matrix));
    XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());
    page.getContents().add(new Do(ximage.getName()));
    page.getContents().add(new GRestore());
    document.save(getOutputPath("55157.pdf"));
    stream.close();
```

## Что нового в Aspose.PDF 23.8

Функция для обнаружения инкрементальных обновлений в PDF-документе была добавлена в версии 23.8. Эта функция возвращает 'true', если документ был сохранен с инкрементальными обновлениями, в противном случае возвращает 'false'.

```java

    Document doc = new Document(dataDir+"PDF_Support_Tech_Note.pdf");
    boolean not_updatedIncrementally = doc.hasIncrementalUpdate();
    System.out.println(not_updatedIncrementally);

    doc.getPages().add();
    doc.saveIncrementally(dataDir+"PDF_updatedIncrementally.pdf");

    doc = new Document(dataDir+"PDF_updatedIncrementally.pdf");
    boolean updatedIncrementally = doc.hasIncrementalUpdate();
    System.out.println(updatedIncrementally);
    doc.close();
```    

Еще одна функция — копирование OutputIntents из входного PDF в целевой PDF.

Мы добавили новое публичное свойство Document.getOutputIntents() для доступа к выходным намерениям в документе. На данный момент поддерживается только использование уже существующих в некоторых документах выходных намерений, пользователь не может создать OutputIntent с нуля.

```java

    Document document1 = new Document(dataDir+"pdfa.pdf");
    Document resultDocument = new Document();
    resultDocument.getPages().add(document1.getPages());

    for (OutputIntent intent : document1.getOutputIntents())
    {
        resultDocument.getOutputIntents().addItem(intent);
    }

    resultDocument.save(dataDir+"resultpath.pdf");
```  


От версии Aspose.PDF 23.8 поддерживается добавление извлечения формы:

```java

{
    String input1 = getInputPdf("46298_1");
    String input2 = getInputPdf("46298_2");

    Document source = new Document(input1);
    Document dest = new Document(input2);

    Page destPage = dest.getPages().get_Item(1);

    TextFragmentAbsorber tfAbsorber = new TextFragmentAbsorber();
    tfAbsorber.visit(source.getPages().get_Item(1));

    // Преобразование foreach в while
    Iterator tmp0 = ( tfAbsorber.getTextFragments()).iterator();
        while (tmp0.hasNext())
        {
            TextFragment textFragment = (TextFragment)tmp0.next();
            System.out.println(textFragment.getText());
            addTextImproved(destPage, textFragment);
        }

    ImagePlacementAbsorber imageAbsorber = new ImagePlacementAbsorber();
    imageAbsorber.visit(source);

    Iterator tmp1 = ( imageAbsorber.getImagePlacements()).iterator();
        while (tmp1.hasNext())
        {
            ImagePlacement image = (ImagePlacement)tmp1.next();
            destPage.addImage(image.getImage().toStream(), image.getRectangle());
        }

    GraphicsAbsorber vectorAbsorber = new GraphicsAbsorber();
    vectorAbsorber.visit(source.getPages().get_Item(1));
    Rectangle area = new Rectangle(90, 250, 300, 400);
    dest.getPages().get_Item(1).addGraphics(vectorAbsorber.getElements(), area);
    dest.save(getOutputPath("46298-out.pdf"));
    }

    private static void addTextImproved(Page page, TextFragment textFragment)
    {
        TextFragment local = new TextFragment();
        local.setPosition(textFragment.getPosition());

        // Пересчитать новую позицию, так как размер страницы отличается от оригинального PDF
        local.getPosition().setXIndent(textFragment.getPosition().getXIndent());//2.5 * 72;
        double newPageHeight = page.getPageRect(true).getHeight();
        double oldPageHeight = textFragment.getPage().getPageRect(true).getHeight();
        local.getPosition().setYIndent(textFragment.getPosition().getYIndent());

        local.setText(textFragment.getText());
        local.getTextState().setFont(textFragment.getTextState().getFont());
        local.getTextState().setFontSize(textFragment.getTextState().getFontSize());

        local.getTextState().setFormattingOptions(textFragment.getTextState().getFormattingOptions());
        local.getTextState().setForegroundColor(textFragment.getTextState().getForegroundColor());

        TextBuilder textBuilder = new TextBuilder(page);
        textBuilder.appendText(local);
    }
```


Также поддерживает возможность обнаружения переполнения при добавлении текста:

```java

    Document doc = new Document();
    String paragraphContent = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras nisl tortor, efficitur sed cursus in, lobortis vitae nulla. Quisque rhoncus, felis sed dictum semper, est tellus finibus augue, ut feugiat enim risus eget tortor. Nulla finibus velit nec ante gravida sollicitudin. Morbi sollicitudin vehicula facilisis. Vestibulum ac convallis erat. Ut eget varius sem. Nam varius pharetra lorem, id ullamcorper justo auctor ac. Integer quis erat vitae lacus mollis volutpat eget et eros. Donec a efficitur dolor. Maecenas non dapibus nisi, ut pellentesque elit. Sed pellentesque rhoncus ante, a consectetur ligula viverra vel. Integer eget bibendum ante. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Curabitur elementum, sem a auctor vulputate, ante libero iaculis dolor, vitae facilisis dolor lorem at orci. Sed laoreet dui id nisi accumsan, id posuere diam accumsan.";
    Rectangle rectangle = new Rectangle(100, 600, 500, 700, false);
    TextParagraph paragraph = new TextParagraph();
    TextFragment fragment = new TextFragment(paragraphContent);
    paragraph.setVerticalAlignment(VerticalAlignment.Top);
    paragraph.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);
    paragraph.setRectangle(rectangle);
    boolean isFitRectangle = fragment.getTextState().isFitRectangle(paragraphContent, rectangle);
    while (!isFitRectangle)
    {
        fragment.getTextState().setFontSize(fragment.getTextState().getFontSize() - 0.5f);
        isFitRectangle = fragment.getTextState().isFitRectangle(paragraphContent, rectangle);
    }
    paragraph.appendLine(fragment);
    TextBuilder builder = new TextBuilder(doc.getPages().add());
    builder.appendParagraph(paragraph);
    doc.save(output);
```


## Что нового в Aspose.PDF 23.7

С версии 23.7 поддержка предустановок диалогового окна печати Масштабирование страницы:

```java

    Document document = new Document();
    document.getPages().add();
    document.setPrintScaling(PrintScaling.None);//PrintScaling.Default
    document.save(outputPdf);

    Document documentOutput = new Document(outputPdf);
    int printScaling = documentOutput.getPrintScaling();
    System.out.println("PrintScaling: " + printScaling);
```

## Что нового в Aspose.PDF 23.6

С версии 23.6 добавлена возможность устанавливать заголовок страницы HTML, Epub.

код для HTML:

```java

    HtmlSaveOptions options = new HtmlSaveOptions();
    options.setFixedLayout(true);
    options.setRasterImagesSavingMode(HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground);
    options.setPartsEmbeddingMode(HtmlSaveOptions.PartsEmbeddingModes.EmbedAllIntoHtml);
    options.setTitle("</title>NEW PAGE & TITILE</head>");

    Document document = new Document(inputPath);
    document.save(outPath, options);
```


код для EPUB:

```java

    EpubSaveOptions epubSaveOptions = new EpubSaveOptions();
    epubSaveOptions.setTitle("</title>НОВАЯ СТРАНИЦА & ЗАГОЛОВОК</head>");
    epubSaveOptions.setContentRecognitionMode(EpubSaveOptions.RecognitionMode.PdfFlow);

    Document document = new Document(inputPath);
    document.save(outPath, epubSaveOptions);
```

С версии 23.6 поддержка предоставления API для позиционирования векторной графики:

```java

    Document document = new Document(input);
    VectorGraphicsAbsorber vectorAbsorber = new VectorGraphicsAbsorber();
    vectorAbsorber.visit(document.getPages().get_Item(1));

    SubPath subPath1 = vectorAbsorber.getSubPaths().get_Item(2);
    SubPath subPath2 = vectorAbsorber.getSubPaths().get_Item(3);
    SubPath subPath3 = vectorAbsorber.getSubPaths().get_Item(4);

    Point point1 = new Point(subPath1.getPosition().getX() + 200, subPath1.getPosition().getY() - 100);
    Point point2 = new Point(subPath2.getPosition().getX() + 200, subPath2.getPosition().getY() - 100);
    Point point3 = new Point(subPath3.getPosition().getX() + 200, subPath3.getPosition().getY() - 100);

    subPath1.setPosition(point1);
    subPath2.setPosition(point2);
    subPath3.setPosition(point3);

    document.save(output);
```

## Что нового в Aspose.PDF 23.1

С версии 23.1 добавлена поддержка создания аннотации PrinterMark. Добавлен один из вариантов аннотации: ColorBarAnnotation.

```java

    Document doc = new Document();
    Page page = doc.getPages().add();
    page.setTrimBox(new com.aspose.pdf.Rectangle(20, 20, 580, 820));
    Rectangle rectBlack = new com.aspose.pdf.Rectangle(100, 300, 300, 320);
    Rectangle rectCyan = new com.aspose.pdf.Rectangle(200, 600, 260, 690);
    Rectangle rectMagenta = new com.aspose.pdf.Rectangle(10, 650, 140, 670);

    ColorBarAnnotation colorBarBlack = new ColorBarAnnotation(page, rectBlack);
    ColorBarAnnotation colorBarCyan = new ColorBarAnnotation(page, rectCyan, ColorsOfCMYK.Cyan);
    ColorBarAnnotation colorBaMagenta = new ColorBarAnnotation(page, rectMagenta);
    colorBaMagenta.setColorOfCMYK(ColorsOfCMYK.Magenta);
    ColorBarAnnotation colorBarYellow = new ColorBarAnnotation(page, new com.aspose.pdf.Rectangle(400, 250, 450, 700), ColorsOfCMYK.Yellow);

    page.getAnnotations().add(colorBarBlack);
    page.getAnnotations().add(colorBarCyan);
    page.getAnnotations().add(colorBaMagenta);
    page.getAnnotations().add(colorBarYellow);
    doc.save("outFile.pdf");
```


## Что нового в Aspose.PDF 22.12

В этом выпуске добавлена поддержка конвертации PDF в DICOM изображение:

```java

    DicomDevice device = new DicomDevice(PageSize.getA4());
    Document doc = new Document("Input.pdf");
    ByteArrayOutputStream stream = new ByteArrayOutputStream();
    device.process(doc.getPages().get_Item(1), stream);
```

## Что нового в Aspose.PDF 22.9

С версии 22.09 поддерживается добавление свойства для изменения порядка рубрик субъекта (E=, CN=, O=, OU=, ) в подписи.

```java

    String inputPdf = getInputPath("input.pdf");
    String inputPfx = getInputPath("input.pfx");
    String outputPdf = getOutputPath("out.pdf");

    final PdfFileSignature fileSign = new PdfFileSignature();
    try 
    {
        fileSign.bindPdf(inputPdf);
        java.awt.Rectangle rect = new java.awt.Rectangle(100, 100, 400, 100);
        PKCS7Detached signature = new PKCS7Detached(inputPfx, "123456789");
        signature.setDate(new Date());
        signature.setCustomAppearance( new SignatureCustomAppearance());
        signature.getCustomAppearance().setUseDigitalSubjectFormat(true);
        signature.getCustomAppearance().setDigitalSubjectFormat(new /*SubjectNameElements*/int[] { SubjectNameElements.CN, SubjectNameElements.O });

        fileSign.sign(1, true, rect, signature);
        fileSign.save(outputPdf);
    }
    finally { 
        if (fileSign != null) 
            fileSign.close(); 
    }
```

## Что нового в Aspose.PDF 22.8

В Aspose.PDF 23.8 добавлена поддержка метода для восстановления таблицы xref:

```java

    PdfFileSanitization sanitizer = new PdfFileSanitization();
    try {
        sanitizer.bindPdf(dataDir + "50528_1.pdf");
        sanitizer.rebuildXrefAndTrailer();
        sanitizer.save(dataDir + "50528_1" + version + ".pdf");
    } finally {
        if (sanitizer != null) ( sanitizer).close();
    }
```

## Что нового в Aspose.PDF 22.6

PDF в PDF_A_1A - реализована опция удаления прозрачного цвета для избежания большого размера выходного файла.

Начиная с версии 22.5, клиент может контролировать качество преобразованной прозрачности и, как результат, размер выходного файла:

```java
    opts.setTransparencyResolution(300);
```

## Что нового в Aspose.PDF 22.5

Во время конверсии в PDF/A прозрачный контент удаляется и заменяется изображением. Мы реализовали новую функцию, и теперь клиент может контролировать качество изображения с помощью параметра TransparencyResolution:

```java

    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document("input.pdf");
    PdfFormatConversionOptions options = new PdfFormatConversionOptions("log.xml", PdfFormat.PDF_A_1A, ConvertErrorAction.Delete);
    options.setTransparencyResolution(300);
    pdfDocument.convert(options);
    pdfDocument.save("finalOutput.pdf");
```


## Что нового в Aspose.PDF 22.4

Этот выпуск включает информацию для Aspose.PDF for Java:

- PDF в ODS: Распознавание текста в нижнем и верхнем индексах;

**пример**

```java

    Document pdfDocument = new Document("Superscript-Subscript.pdf");
    ExcelSaveOptions options = new ExcelSaveOptions();
    options.Format = ExcelSaveOptions.ExcelFormat.ODS;
    pdfDocument.Save("output.ods"), options);
```

- PDF в XMLSpreadSheet2003: Распознавание текста в нижнем и верхнем индексах;

- PDF в Excel: Распознавание текста в нижнем и верхнем индексах;

## Что нового в Aspose.PDF 22.3

PDF в ODS: Поддержка RTL доступна в версии 22.3

```java

    ExcelSaveOptions options = new ExcelSaveOptions();
    options.setFormat(ExcelSaveOptions.ExcelFormat.ODS);
    pdfDocument.save("output.ods", options);
```

## Что нового в Aspose.PDF 22.2

Этот выпуск включает PDF в XSLX: Поддержка RTL (иврит, арабский).

## Что нового в Aspose.PDF 22.1

Aspose.PDF for Java позволяет загружать документы Portable Document Format (PDF) версии 2.0.

## Что нового в Aspose.PDF 21.10

### Как обнаружить скрытый текст?

Пожалуйста, используйте следующий код:

```java

Document pdf = new Document(inFile);
        Page page = pdf.getPages().get_Item(1);
        TextFragmentAbsorber textFragmentAbsorber = new com.aspose.pdf.TextFragmentAbsorber();
        page.accept(textFragmentAbsorber);
        TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

        int fragmentsCount = textFragmentAbsorber.getTextFragments().size();
        int invisibleCount = 0;

        Iterator tmp0 = ( textFragmentCollection).iterator();
            while (tmp0.hasNext())
            {
                com.aspose.pdf.TextFragment fragment = (com.aspose.pdf.TextFragment)tmp0.next();
                System.out.println(fragment.getText());
                System.out.println(fragment.getTextState().isInvisible());
                if (fragment.getTextState().isInvisible())
                    invisibleCount++;
            }
```


## Что нового в Aspose.PDF 21.8

### Как изменить цвет текста в цифровой подписи?

В версии 21.8 метод setForegroundColor позволяет изменить цвет текста в цифровой подписи:

```java
Пожалуйста, используйте следующий код:

                    PdfFileSignature pdfSign = new PdfFileSignature();                
                    pdfSign.bindPdf(inFile);
                    //создаем прямоугольник для расположения подписи
                    java.awt.Rectangle rect = new java.awt.Rectangle(310, 45, 200, 50);
                    PKCS7 pkcs = new PKCS7(inPfxFile, "");

                    pkcs.setCustomAppearance( new SignatureCustomAppearance());
//установить цвет текста
                    pkcs.getCustomAppearance().setForegroundColor(Color.getGreen());

                    // подписать PDF файл
                    pdfSign.sign(1, true, rect, pkcs);
                    //сохранить выходной PDF файл
                    pdfSign.save(outFile);
```

## Что нового в Aspose.PDF 21.6

### Скрытие изображения с помощью ImagePlacementAbsorber из документа

С Aspose.PDF для Java вы можете скрыть изображения, используя ImagePlacementAbsorber из документа:

```java
      Document doc = new Document("input.pdf");

        for (Page page : doc.getPages()) {
            ImagePlacementAbsorber ipa = new ImagePlacementAbsorber();
            ipa.visit(page);
            for (ImagePlacement ip : ipa.getImagePlacements()) {
                ip.hide();
            }
        }

        doc.save("out.pdf");
```

## Что нового в Aspose.PDF 21.5

### Добавить API для объединения изображений

Aspose.PDF 21.4 позволяет объединять изображения. Объединяет список потоков изображений в один поток изображений. Поддерживаются выходные форматы Png/jpg/tiff, в случае использования неподдерживаемого формата выходной поток по умолчанию кодируется как Jpeg. Следуйте следующему примеру кода:

```java
InputStream inputStream;

        ArrayList<InputStream> inputImagesStreams = new ArrayList<InputStream>();
        InputStream inputFile300dpi = new FileInputStream("image1.jpg");
        try  {
            inputImagesStreams.add(inputFile300dpi);
            InputStream inputFile600dpi = new FileInputStream("image2.jpg");
            try {
                inputImagesStreams.add(inputFile600dpi);
                inputStream = PdfConverter.mergeImages(
                        inputImagesStreams,
                        com.aspose.pdf.ImageFormat.Jpeg,
                        ImageMergeMode.Vertical,
                        new Integer(1),
                        new Integer(1)
                );
            } finally {
                if (inputFile600dpi != null) (inputFile600dpi).close();
            }
        } finally {
            if (inputFile300dpi != null) (inputFile300dpi).close();
        }

        Document doc = new Document();
        Page p = doc.getPages().add();
        Image image = new Image();
        image.setImageStream(inputStream);
        p.getParagraphs().add(image);
        doc.save("out.pdf");
        inputStream.close();
```


Также вы можете объединять ваши изображения в формате Tiff:

```java
InputStream inputStream;

        ArrayList<InputStream> inputImagesStreams = new ArrayList<InputStream>();
        InputStream inputFile1 = new FileInputStream("1.tif");
        try  {
            inputImagesStreams.add(inputFile1);
            InputStream inputFile2 = new FileInputStream("2.tif");
            try {
                inputImagesStreams.add(inputFile2);
                inputStream = PdfConverter.mergeImagesAsTiff(inputImagesStreams);
            } finally {
                if (inputFile2 != null) (inputFile2).close();
            }
        } finally {
            if (inputFile1 != null) (inputFile1).close();
        }

        Document doc = new Document();
        Page p = doc.getPages().add();
        Image image = new Image();
        image.setImageStream(inputStream);
        p.getParagraphs().add(image);
        doc.save("out2.pdf");
        inputStream.close();
```

## Что нового в Aspose.PDF 21.02

Aspose.PDF v21.02 Подпись PDF с помощью PAdES LTV Подписей

```java
final Document document = new Document(inputPdf);
    try 
    {
        PdfFileSignature signature = new PdfFileSignature(document);
        PKCS7 pkcs7 = new PKCS7(getInputPath("cert.pfx"), "password");
        //Подписать PDF с помощью PAdES LTV Подписей
        pkcs7.setUseLtv(true);

        signature.sign(1, true, new Rectangle(100, 100, 300, 300), pkcs7);
        signature.save(outputPdf);
    }
    finally { if (document != null) (document).dispose(); }
```