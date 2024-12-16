---
title: Установка Свойств Элементов Структуры в Тегированном PDF
linktitle: Установка Свойств Элементов Структуры
type: docs
weight: 30
url: /ru/java/set-tagged-pdfs-element-properties/
description: С Aspose.PDF для Java вы можете установить различные свойства элементов структуры. Это включает установку элементов структуры текстового блока, установку встроенных элементов структуры, добавление элемента структуры в элементы и т.д.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Установка Свойств Элементов Структуры

Для установки свойств элементов структуры в Тегированном PDF документе, Aspose.PDF предлагает методы **createSectElement()** и **createHeaderElement()** интерфейса [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent). Следующий фрагмент кода показывает, как установить свойства элементов структуры Тегированного PDF документа:

```java
// Для полных примеров и файлов данных, пожалуйста, посетите https://github.com/aspose-pdf/Aspose.PDF-for-Java
// Путь к директории с документами.
String path = "pathTodir";
// Создаем PDF документ
Document document = new Document();

// Получаем контент для работы с TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Устанавливаем заголовок и язык для документа
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// Создаем элементы структуры
StructureElement rootElement = taggedContent.getRootElement();

SectElement sect = taggedContent.createSectElement();
rootElement.appendChild(sect);

HeaderElement h1 = taggedContent.createHeaderElement(1);
sect.appendChild(h1);
h1.setText("Заголовок");

h1.setTitle("Заголовок");
h1.setLanguage("en-US");
h1.setAlternativeText("Альтернативный текст");
h1.setExpansionText("Текст расширения");
h1.setActualText("Фактический текст");

// Сохраняем Тегированный PDF документ
document.save(path + "StructureElementsProperties.pdf");
```


## Установка элементов структуры текста

Для установки элементов структуры текста в документе Tagged PDF, Aspose.PDF предлагает класс [ParagraphElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/class-use/ParagraphElement). Следующий фрагмент кода показывает, как установить элементы структуры текста в документе Tagged PDF:

```java
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-Java
// Путь к каталогу документов.
String path = "pathTodir";

// Создать Pdf документ
Document document = new Document();

// Получить содержимое для работы с TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Установить заголовок и язык для документа
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// Получить корневые элементы структуры
StructureElement rootElement = taggedContent.getRootElement();

ParagraphElement p = taggedContent.createParagraphElement();
// Установить текст для элемента структуры текста
p.setText("Параграф.");
rootElement.appendChild(p);


// Сохранить Tagged Pdf документ
document.save(path + "TextStructureElement.pdf");
```


## Установка элементов структуры текстового блока

Для установки элементов структуры текстового блока в документе Tagged PDF, Aspose.PDF предлагает классы [HeaderElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls.class-use/headerelement) и [ParagraphElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/class-use/ParagraphElement). Вы можете добавлять объекты этих классов как дочерние элементы объекта **StructureElement**. Следующий фрагмент кода показывает, как установить элементы структуры текстового блока в документе Tagged PDF:

```java
// Для получения полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-Java
// Путь к каталогу документов.
String path = "pathTodir";

// Создать Pdf документ
Document document = new Document();

// Получить содержимое для работы с TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Установить заголовок и язык для документа
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// Получить корневой элемент структуры
StructureElement rootElement = taggedContent.getRootElement();

HeaderElement h1 = taggedContent.createHeaderElement(1);
HeaderElement h2 = taggedContent.createHeaderElement(2);
HeaderElement h3 = taggedContent.createHeaderElement(3);
HeaderElement h4 = taggedContent.createHeaderElement(4);
HeaderElement h5 = taggedContent.createHeaderElement(5);
HeaderElement h6 = taggedContent.createHeaderElement(6);
h1.setText("H1. Заголовок уровня 1");
h2.setText("H2. Заголовок уровня 2");
h3.setText("H3. Заголовок уровня 3");
h4.setText("H4. Заголовок уровня 4");
h5.setText("H5. Заголовок уровня 5");
h6.setText("H6. Заголовок уровня 6");
rootElement.appendChild(h1);
rootElement.appendChild(h2);
rootElement.appendChild(h3);
rootElement.appendChild(h4);
rootElement.appendChild(h5);
rootElement.appendChild(h6);

ParagraphElement p = taggedContent.createParagraphElement();
p.setText("P. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean nec lectus ac sem faucibus imperdiet. Sed ut erat ac magna ullamcorper hendrerit. Cras pellentesque libero semper, gravida magna sed, luctus leo. Fusce lectus odio, laoreet nec ullamcorper ut, molestie eu elit. Interdum et malesuada fames ac ante ipsum primis in faucibus. Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat sem tristique eget. Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper pellentesque justo rhoncus accumsan. Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus ac iaculis eget, tempus et magna. Sed non consectetur elit. Sed vulputate, quam sed lacinia luctus, ipsum nibh fringilla purus, vitae posuere risus odio id massa. Cras sed venenatis lacus.");
rootElement.appendChild(p);

// Сохранить документ Tagged Pdf
document.save(path + "TextBlockStructureElements.pdf");
```


## Настройка Элементов Встроенной Структуры

Для установки элементов встроенной структуры в Документе Tagged PDF, Aspose.PDF предлагает классы [SpanElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.ils/spanelement) и [ParagraphElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/class-use/ParagraphElement). Вы можете добавлять объекты этих классов как дочерние для объекта **StructureElement**. Следующий фрагмент кода показывает, как установить элементы встроенной структуры в Документе Tagged PDF:

```java
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-Java
// Путь к директории с документами.
String path = "pathTodir";
// Создаем Pdf Документ
Document document = new Document();

// Получаем содержимое для работы с TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Устанавливаем заголовок и язык для документа
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// Получаем корневой элемент структуры
StructureElement rootElement = taggedContent.getRootElement();

HeaderElement h1 = taggedContent.createHeaderElement(1);
HeaderElement h2 = taggedContent.createHeaderElement(2);
HeaderElement h3 = taggedContent.createHeaderElement(3);
HeaderElement h4 = taggedContent.createHeaderElement(4);
HeaderElement h5 = taggedContent.createHeaderElement(5);
HeaderElement h6 = taggedContent.createHeaderElement(6);
rootElement.appendChild(h1);
rootElement.appendChild(h2);
rootElement.appendChild(h3);
rootElement.appendChild(h4);
rootElement.appendChild(h5);
rootElement.appendChild(h6);

SpanElement spanH11 = taggedContent.createSpanElement();
spanH11.setText("H1. ");
h1.appendChild(spanH11);
SpanElement spanH12 = taggedContent.createSpanElement();
spanH12.setText("Заголовок уровня 1");
h1.appendChild(spanH12);

SpanElement spanH21 = taggedContent.createSpanElement();
spanH21.setText("H2. ");
h2.appendChild(spanH21);
SpanElement spanH22 = taggedContent.createSpanElement();
spanH22.setText("Заголовок уровня 2");
h2.appendChild(spanH22);

SpanElement spanH31 = taggedContent.createSpanElement();
spanH31.setText("H3. ");
h3.appendChild(spanH31);
SpanElement spanH32 = taggedContent.createSpanElement();
spanH32.setText("Заголовок уровня 3");
h3.appendChild(spanH32);

SpanElement spanH41 = taggedContent.createSpanElement();
spanH41.setText("H4. ");
h4.appendChild(spanH41);
SpanElement spanH42 = taggedContent.createSpanElement();
spanH42.setText("Заголовок уровня 4");
h4.appendChild(spanH42);

SpanElement spanH51 = taggedContent.createSpanElement();
spanH51.setText("H5. ");
h5.appendChild(spanH51);
SpanElement spanH52 = taggedContent.createSpanElement();
spanH52.setText("Заголовок уровня 5");
h5.appendChild(spanH52);

SpanElement spanH61 = taggedContent.createSpanElement();
spanH61.setText("H6. ");
h6.appendChild(spanH61);
SpanElement spanH62 = taggedContent.createSpanElement();
spanH62.setText("Заголовок уровня 6");
h6.appendChild(spanH62);

ParagraphElement p = taggedContent.createParagraphElement();
p.setText("P. ");
rootElement.appendChild(p);
SpanElement span1 = taggedContent.createSpanElement();
span1.setText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. ");
p.appendChild(span1);
SpanElement span2 = taggedContent.createSpanElement();
span2.setText("Aenean nec lectus ac sem faucibus imperdiet. ");
p.appendChild(span2);
SpanElement span3 = taggedContent.createSpanElement();
span3.setText("Sed ut erat ac magna ullamcorper hendrerit. ");
p.appendChild(span3);
SpanElement span4 = taggedContent.createSpanElement();
span4.setText("Cras pellentesque libero semper, gravida magna sed, luctus leo. ");
p.appendChild(span4);
SpanElement span5 = taggedContent.createSpanElement();
span5.setText("Fusce lectus odio, laoreet nec ullamcorper ut, molestie eu elit. ");
p.appendChild(span5);
SpanElement span6 = taggedContent.createSpanElement();
span6.setText("Interdum et malesuada fames ac ante ipsum primis in faucibus. ");
p.appendChild(span6);
SpanElement span7 = taggedContent.createSpanElement();
span7.setText("Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat sem tristique eget. ");
p.appendChild(span7);
SpanElement span8 = taggedContent.createSpanElement();
span8.setText("Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper pellentesque justo rhoncus accumsan. ");
p.appendChild(span8);
SpanElement span9 = taggedContent.createSpanElement();
span9.setText("Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus ac iaculis eget, tempus et magna. Sed non consectetur elit. ");
p.appendChild(span9);
SpanElement span10 = taggedContent.createSpanElement();
span10.setText("Sed vulputate, quam sed lacinia luctus, ipsum nibh fringilla purus, vitae posuere risus odio id massa. Cras sed venenatis lacus.");
p.appendChild(span10);

// Сохраняем Документ Tagged Pdf
document.save(path + "InlineStructureElements.pdf");
```


## Установка Пользовательского Имени Тега

Для установки пользовательского имени тега элементов Tagged PDF документа, Aspose.PDF предлагает метод **setTag()** для элементов. Следующий фрагмент кода показывает, как установить пользовательское имя тега:

```java
// Для полноценных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-Java
// Путь к директории с документами.
String path = "pathTodir";
// Создание PDF документа
Document document = new Document();

// Получение содержимого для работы с TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Установка названия и языка для документа
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// Создание элементов логической структуры
SectElement sect = taggedContent.createSectElement();
taggedContent.getRootElement().appendChild(sect);

ParagraphElement p1 = taggedContent.createParagraphElement();
ParagraphElement p2 = taggedContent.createParagraphElement();
ParagraphElement p3 = taggedContent.createParagraphElement();
ParagraphElement p4 = taggedContent.createParagraphElement();

p1.setText("P1. ");
p2.setText("P2. ");
p3.setText("P3. ");
p4.setText("P4. ");

p1.setTag("P1");
p2.setTag("Para");
p3.setTag("Para");
p4.setTag("Paragraph");

sect.appendChild(p1);
sect.appendChild(p2);
sect.appendChild(p3);
sect.appendChild(p4);

SpanElement span1 = taggedContent.createSpanElement();
SpanElement span2 = taggedContent.createSpanElement();
SpanElement span3 = taggedContent.createSpanElement();
SpanElement span4 = taggedContent.createSpanElement();

span1.setText("Span 1.");
span2.setText("Span 2.");
span3.setText("Span 3.");
span4.setText("Span 4.");

span1.setTag("SPAN");
span2.setTag("Sp");
span3.setTag("Sp");
span4.setTag("TheSpan");

p1.appendChild(span1);
p2.appendChild(span2);
p3.appendChild(span3);
p4.appendChild(span4);

// Сохранение Tagged Pdf документа
document.save(path + "CustomTag.pdf");
```


## Добавление элемента структуры в элементы

Для установки элементов структуры ссылок в документе PDF с тегами, Aspose.PDF предлагает метод **createLinkElement()** интерфейса [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent). Следующий фрагмент кода показывает, как установить элементы структуры в абзаце с текстом документа PDF с тегами:

```java
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-Java
// Путь к директории документов.
String dataDir = Utils.getDataDir() + "TaggedPDFs\\";
String outFile = dataDir + "AddStructureElementIntoElement_Output.pdf";
String logFile = dataDir + "46144_log.xml";

// Создание документа и получение содержимого PDF с тегами
Document document = new Document();
ITaggedContent taggedContent = document.getTaggedContent();

// Установка заголовка и языка документа
taggedContent.setTitle("Пример текстовых элементов");
taggedContent.setLanguage("en-US");

// Получение корневого элемента структуры (элемент структуры документа)
StructureElement rootElement = taggedContent.getRootElement();

ParagraphElement p1 = taggedContent.createParagraphElement();
rootElement.appendChild(p1);
SpanElement span11 = taggedContent.createSpanElement();
span11.setText("Span_11");
SpanElement span12 = taggedContent.createSpanElement();
span12.setText(" и Span_12.");
p1.setText("Абзац с ");
p1.appendChild(span11);
p1.appendChild(span12);

ParagraphElement p2 = taggedContent.createParagraphElement();
rootElement.appendChild(p2);
SpanElement span21 = taggedContent.createSpanElement();
span21.setText("Span_21");
SpanElement span22 = taggedContent.createSpanElement();
span22.setText("Span_22.");
p2.appendChild(span21);
p2.setText(" и ");
p2.appendChild(span22);

ParagraphElement p3 = taggedContent.createParagraphElement();
rootElement.appendChild(p3);
SpanElement span31 = taggedContent.createSpanElement();
span31.setText("Span_31");
SpanElement span32 = taggedContent.createSpanElement();
span32.setText(" и Span_32");
p3.appendChild(span31);
p3.appendChild(span32);
p3.setText(".");

ParagraphElement p4 = taggedContent.createParagraphElement();
rootElement.appendChild(p4);
SpanElement span41 = taggedContent.createSpanElement();
SpanElement span411 = taggedContent.createSpanElement();
span411.setText("Span_411, ");
span41.setText("Span_41, ");
span41.appendChild(span411);
SpanElement span42 = taggedContent.createSpanElement();
SpanElement span421 = taggedContent.createSpanElement();
span421.setText("Span 421 и ");
span42.appendChild(span421);
span42.setText("Span_42");
p4.appendChild(span41);
p4.appendChild(span42);
p4.setText(".");

// Сохранение документа PDF с тегами
document.save(outFile);
```


## Настройка элемента структуры заметки

Aspose.PDF для Java API также позволяет добавлять **NoteElement** в тэгированный PDF-документ. Следующий фрагмент кода показывает, как добавить элемент заметки в тэгированный PDF-документ:

```java
// Для полноценных примеров и файлов данных, пожалуйста, посетите https://github.com/aspose-pdf/Aspose.PDF-for-Java
// Путь к директории документов.
String dataDir = Utils.getDataDir() + "TaggedPDFs\\";
String outFile = dataDir + "CreateNoteStructureElement.pdf";
String logFile = dataDir + "45929_log.xml";

// Создать PDF документ
Document document = new Document();
ITaggedContent taggedContent = document.getTaggedContent();

taggedContent.setTitle("Пример элементов заметок");
taggedContent.setLanguage("en-US");

// Добавить элемент параграфа
ParagraphElement paragraph = taggedContent.createParagraphElement();
taggedContent.getRootElement().appendChild(paragraph);

// Добавить NoteElement
NoteElement note1 = taggedContent.createNoteElement();
paragraph.appendChild(note1);
note1.setText("Заметка с автоматически сгенерированным ID. ");

// Добавить NoteElement
NoteElement note2 = taggedContent.createNoteElement();
paragraph.appendChild(note2);
note2.setText("Заметка с ID = 'note_002'. ");
note2.setId("note_002");

// Добавить NoteElement
NoteElement note3 = taggedContent.createNoteElement();
paragraph.appendChild(note3);
note3.setText("Заметка с ID = 'note_003'. ");
note3.setId("note_003");
// Сохранить тэгированный PDF документ
document.save(outFile);
```