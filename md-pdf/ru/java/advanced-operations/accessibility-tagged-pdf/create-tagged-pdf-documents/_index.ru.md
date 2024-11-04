---
title: Создание Тегированного PDF
linktitle: Создание Тегированного PDF
type: docs
weight: 10
lastmod: "2021-06-05"
url: /java/create-tagged-pdf-documents/
description: В этой статье объясняется, как программно создать элементы структуры для тегированного PDF-документа, используя Aspose.PDF для Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Создание Элементов Структуры

Чтобы создать элементы структуры в тегированном PDF-документе, Aspose.PDF предлагает методы для создания элемента структуры с использованием интерфейса [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent). Следующий фрагмент кода показывает, как создать элементы структуры тегированного PDF:

```java
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-Java
// Путь к каталогу документов.
String path = "pathTodir";

// Создать PDF документ
Document document = new Document();

// Получить контент для работы с TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Установить заголовок и язык для документа
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// Создать элементы группировки
PartElement partElement = taggedContent.createPartElement();
ArtElement artElement = taggedContent.createArtElement();
SectElement sectElement = taggedContent.createSectElement();
DivElement divElement = taggedContent.createDivElement();
BlockQuoteElement blockQuoteElement = taggedContent.createBlockQuoteElement();
CaptionElement captionElement = taggedContent.createCaptionElement();
TOCElement tocElement = taggedContent.createTOCElement();
TOCIElement tociElement = taggedContent.createTOCIElement();
IndexElement indexElement = taggedContent.createIndexElement();
NonStructElement nonStructElement = taggedContent.createNonStructElement();
PrivateElement privateElement = taggedContent.createPrivateElement();

// Создать текстовые элементы структуры на уровне блока
ParagraphElement paragraphElement = taggedContent.createParagraphElement();
HeaderElement headerElement = taggedContent.createHeaderElement();
HeaderElement h1Element = taggedContent.createHeaderElement(1);

// Создать текстовые элементы структуры на уровне строки
SpanElement spanElement = taggedContent.createSpanElement();
QuoteElement quoteElement = taggedContent.createQuoteElement();
NoteElement noteElement = taggedContent.createNoteElement();

// Создать элементы структуры иллюстраций
FigureElement figureElement = taggedContent.createFigureElement();
FormulaElement formulaElement = taggedContent.createFormulaElement();

// Методы находятся в разработке
ListElement listElement = taggedContent.createListElement();
TableElement tableElement = taggedContent.createTableElement();
ReferenceElement referenceElement = taggedContent.createReferenceElement();
BibEntryElement bibEntryElement = taggedContent.createBibEntryElement();
CodeElement codeElement = taggedContent.createCodeElement();
LinkElement linkElement = taggedContent.createLinkElement();
AnnotElement annotElement = taggedContent.createAnnotElement();
RubyElement rubyElement = taggedContent.createRubyElement();
WarichuElement warichuElement = taggedContent.createWarichuElement();
FormElement formElement = taggedContent.createFormElement();

// Сохранить тегированный PDF-документ
document.save(path + "StructureElements.pdf");
```


## Создание Дерева Элементов Структуры

Для создания дерева элементов структуры в Тегированном PDF документе, Aspose.PDF предлагает методы для создания дерева элементов структуры с использованием интерфейса [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent). Следующий пример кода показывает, как создать дерево элементов структуры Тегированного PDF документа:

```java
// Для полноценных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-Java
// Путь к директории с документами.
String path = "pathTodir";
// Создать PDF документ
Document document = new Document();

// Получить контент для работы с Тегированным PDF
ITaggedContent taggedContent = document.getTaggedContent();

// Установить заголовок и язык для документа
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// Получить корневой элемент структуры (Документ)
StructureElement rootElement = taggedContent.getRootElement();

// Создать логическую структуру
SectElement sect1 = taggedContent.createSectElement();
rootElement.appendChild(sect1);

SectElement sect2 = taggedContent.createSectElement();
rootElement.appendChild(sect2);

DivElement div11 = taggedContent.createDivElement();
sect1.appendChild(div11);

DivElement div12 = taggedContent.createDivElement();
sect1.appendChild(div12);

ArtElement art21 = taggedContent.createArtElement();
sect2.appendChild(art21);

ArtElement art22 = taggedContent.createArtElement();
sect2.appendChild(art22);

DivElement div211 = taggedContent.createDivElement();
art21.appendChild(div211);

DivElement div212 = taggedContent.createDivElement();
art21.appendChild(div212);

DivElement div221 = taggedContent.createDivElement();
art22.appendChild(div221);

DivElement div222 = taggedContent.createDivElement();
art22.appendChild(div222);

SectElement sect3 = taggedContent.createSectElement();
rootElement.appendChild(sect3);

DivElement div31 = taggedContent.createDivElement();
sect3.appendChild(div31);

// Сохранить Тегированный PDF документ
document.save(path + "StructureElementsTree.pdf");
```


## Стилизация структуры текста

Для стилизации структуры текста в Тегированном PDF-документе Aspose.PDF предлагает свойства **setFont()**, **setFontSize()**, **setFontStyle()** и **setForegroundColor()** класса [StructureTextState](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.class-use/StructureTextState). Следующий фрагмент кода показывает, как стилизовать структуру текста в Тегированном PDF-документе:

```java
// Для получения полных примеров и файлов данных, пожалуйста, посетите https://github.com/aspose-pdf/Aspose.PDF-for-Java
// Путь к директории с документами.
String path = "pathTodir";
// Создать PDF-документ
Document document = new Document();

// Получить контент для работы с TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Установить заголовок и язык для документа
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

ParagraphElement p = taggedContent.createParagraphElement();
taggedContent.getRootElement().appendChild(p);

// В разработке
p.getStructureTextState().setFontSize(18F);
p.getStructureTextState().setForegroundColor(Color.getRed());
p.getStructureTextState().setFontStyle(FontStyles.Italic);

p.setText("Красный курсивный текст.");

// Сохранить Тегированный PDF-документ
document.save(path + "StyleTextStructure.pdf");
```


## Иллюстрация элементов структуры

Для иллюстрации элементов структуры в документе Tagged PDF, Aspose.PDF предлагает класс [IllustrationElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.class-use/IllustrationElement). Следующий фрагмент кода показывает, как иллюстрировать элементы структуры в документе Tagged PDF:

```java
// Для получения полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-Java
// Путь к директории документов.
String path = "pathTodir";
// Создать PDF документ
Document document = new Document();

// Получить содержимое для работы с TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Установить заголовок и язык для документа
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// В разработке
IllustrationElement figure1 = taggedContent.createFigureElement();
taggedContent.getRootElement().appendChild(figure1);
figure1.setActualText("Фигура Один");
figure1.setTitle("Изображение 1");
figure1.setTag("Fig1");
figure1.setImage("image.png");

// Сохранить документ Tagged Pdf
document.save(path + "IllustrationStructureElements.pdf");
```


## **Создание PDF с помеченным изображением**

Для создания PDF с помеченным изображением Aspose.PDF предлагает метод [createFigureElement()](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent#createFigureElement--) интерфейса [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent). Следующий фрагмент кода показывает функциональность.

```java
// Для полных примеров и файлов данных, пожалуйста, посетите https://github.com/aspose-pdf/Aspose.PDF-for-Java
Document document = new Document();
ITaggedContent taggedContent = document.getTaggedContent();

taggedContent.setTitle("CreatePDFwithTaggedImage");
taggedContent.setLanguage("en-US");

IllustrationElement figure1 = taggedContent.createFigureElement();
taggedContent.getRootElement().appendChild(figure1);
figure1.setAlternativeText("Логотип Aspose");
figure1.setTitle("Изображение 1");
figure1.setTag("Fig");
// Добавить изображение с разрешением 300 DPI (по умолчанию)
figure1.setImage("aspose-logo.jpg");
// Сохранить PDF документ
document.save("PDFwithTaggedImage.pdf");
```


## Создание PDF с Тегированным Текстом

Для создания PDF с Тегированным Текстом, Aspose.PDF предлагает интерфейс [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent). Следующий фрагмент кода демонстрирует функциональность.

```java
// Для полноценных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-Java
// Путь к директории с документами.
String dataDir = Utils.getDataDir() + "TaggedPDFs\\";
// Создание Pdf документа
Document document = new Document();

// Получить контент для работы с TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Установить заголовок и язык для документа
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// Создание текстовых элементов блочного уровня
HeaderElement headerElement = taggedContent.createHeaderElement();
headerElement.setActualText("Heading 1");
ParagraphElement paragraphElement1 = taggedContent.createParagraphElement();
paragraphElement1.setActualText("test1");
ParagraphElement paragraphElement2 = taggedContent.createParagraphElement();
paragraphElement2.setActualText("test 2");
ParagraphElement paragraphElement3 = taggedContent.createParagraphElement();
paragraphElement3.setActualText("test 3");
ParagraphElement paragraphElement4 = taggedContent.createParagraphElement();
paragraphElement4.setActualText("test 4");
ParagraphElement paragraphElement5 = taggedContent.createParagraphElement();
paragraphElement5.setActualText("test 5");
ParagraphElement paragraphElement6 = taggedContent.createParagraphElement();
paragraphElement6.setActualText("test 6");
ParagraphElement paragraphElement7 = taggedContent.createParagraphElement();
paragraphElement7.setActualText("test 7");

// Сохранить PDF документ
document.save( dataDir + "PDFwithTaggedText.pdf");
```