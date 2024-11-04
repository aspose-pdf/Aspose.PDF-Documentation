---
title: Установка свойств элементов структуры
linktitle: Установка свойств элементов структуры
type: docs
weight: 30
url: /net/setting-structure-elements-properties/
description: Вы можете устанавливать различные свойства элементов структуры в документе PDF с помощью Aspose.PDF для .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Установка свойств элементов структуры",
    "alternativeHeadline": "Как установить свойства структурных элементов",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голубь",
        "givenName": "Анастасия",
        "familyName": "Голубь",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация документов PDF",
    "keywords": "pdf, c#, установка текстовой структуры, установка языка, установка заголовка, установка элемента структуры Примечание",
    "wordcount": "302",
    "proficiencyLevel":"Начальный",
    "publisher": {
        "@type": "Organization",
        "name": "Команда документации Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/setting-structure-elements-properties/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/setting-structure-elements-properties/"
    },
    "dateModified": "2022-02-04",
    "description": "Вы можете устанавливать различные свойства элементов структуры в документе PDF с помощью Aspose.PDF для .NET."
}
</script>
Для установки свойств элементов структуры в маркированном PDF документе, Aspose.PDF предлагает методы [CreateSectElement](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent/methods/createsectelement) и [CreateHeaderElement](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent/methods/createheaderelement/index) интерфейса [ITaggedContent](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent).

Следующий фрагмент кода показывает, как установить свойства элементов структуры маркированного PDF документа:

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Создать PDF документ
Document document = new Document();

// Получить содержимое для работы с TaggedPdf
ITaggedContent taggedContent = document.TaggedContent;

// Установить заголовок и язык для документа
taggedContent.SetTitle("Маркированный PDF документ");
taggedContent.SetLanguage("en-US");

// Создать элементы структуры
StructureElement rootElement = taggedContent.RootElement;

SectElement sect = taggedContent.CreateSectElement();
rootElement.AppendChild(sect);

HeaderElement h1 = taggedContent.CreateHeaderElement(1);
sect.AppendChild(h1);
h1.SetText("Заголовок");

h1.Title = "Заголовок";
h1.Language = "en-US";
h1.AlternativeText = "Альтернативный текст";
h1.ExpansionText = "Текст расширения";
h1.ActualText = "Фактический текст";

// Сохранить маркированный PDF документ
document.Save(dataDir + "StructureElementsProperties.pdf");
```
## Установка элементов структуры текста

Для установки элементов структуры текста в тегированный PDF документ, Aspose.PDF предлагает класс [ParagraphElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/paragraphelement). Следующий фрагмент кода показывает, как установить элементы структуры текста в тегированный PDF документ:

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Создать PDF документ
Document document = new Document();

// Получить содержимое для работы с TaggedPdf
ITaggedContent taggedContent = document.TaggedContent;

// Установить название и язык документа
taggedContent.SetTitle("Тегированный PDF документ");
taggedContent.SetLanguage("en-US");

// Получить корневые элементы структуры
StructureElement rootElement = taggedContent.RootElement;

ParagraphElement p = taggedContent.CreateParagraphElement();
// Установить текст в элемент структуры текста
p.SetText("Абзац.");
rootElement.AppendChild(p);

// Сохранить тегированный PDF документ
document.Save(dataDir + "TextStructureElement.pdf");
```
## Установка элементов структуры текстового блока

Для установки элементов структуры текстового блока в тегированном PDF-документе, Aspose.PDF предлагает классы [HeaderElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/headerelement) и [ParagraphElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/paragraphelement). Вы можете добавлять объекты этих классов в качестве дочерних для объекта [StructureElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structureelement).
Следующий фрагмент кода показывает, как установить элементы структуры текстового блока тегированного PDF-документа:

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Создание документа PDF
Document document = new Document();

// Получение содержимого для работы с TaggedPdf
ITaggedContent taggedContent = document.TaggedContent;

// Установка заголовка и языка документа
taggedContent.SetTitle("Tagged Pdf Document");
taggedContent.SetLanguage("en-US");

// Получение корневого элемента структуры
StructureElement rootElement = taggedContent.RootElement;

HeaderElement h1 = taggedContent.CreateHeaderElement(1);
HeaderElement h2 = taggedContent.CreateHeaderElement(2);
HeaderElement h3 = taggedContent.CreateHeaderElement(3);
HeaderElement h4 = taggedContent.CreateHeaderElement(4);
HeaderElement h5 = taggedContent.CreateHeaderElement(5);
HeaderElement h6 = taggedContent.CreateHeaderElement(6);
h1.SetText("H1. Заголовок первого уровня");
h2.SetText("H2. Заголовок второго уровня");
h3.SetText("H3. Заголовок третьего уровня");
h4.SetText("H4. Заголовок четвертого уровня");
h5.SetText("H5. Заголовок пятого уровня");
h6.SetText("H6. Заголовок шестого уровня");
rootElement.AppendChild(h1);
rootElement.AppendChild(h2);
rootElement.AppendChild(h3);
rootElement.AppendChild(h4);
rootElement.AppendChild(h5);
rootElement.AppendChild(h6);

ParagraphElement p = taggedContent.CreateParagraphElement();
p.SetText("P. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean nec lectus ac sem faucibus imperdiet. Sed ut erat ac magna ullamcorper hendrerit. Cras pellentesque libero semper, gravida magna sed, luctus leo. Fusce lectus odio, laoreet nec ullamcorper ut, molestie eu elit. Interdum et malesuada fames ac ante ipsum primis in faucibus. Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat sem tristique eget. Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper pellentesque justo rhoncus accumsan. Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus ac iaculis eget, tempus et magna. Sed non consectetur elit. Sed vulputate, quam sed luctus lacinia, ipsum nibh fringilla purus, vitae posuere risus odio id massa. Cras sed venenatis lacus.");
rootElement.AppendChild(p);

// Сохранение тегированного документа PDF
document.Save(dataDir + "TextBlockStructureElements.pdf");
```
## Установка элементов встроенной структуры

Для установки элементов встроенной структуры тегированного PDF-документа, Aspose.PDF предлагает классы [SpanElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/spanelement) и [ParagraphElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/paragraphelement). Вы можете добавлять объекты этих классов в качестве дочернего элемента объекта [StructureElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structureelement). Следующий фрагмент кода показывает, как установить элементы встроенной структуры тегированного PDF-документа:

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Создать PDF документ
Document document = new Document();

// Получить контент для работы с TaggedPdf
ITaggedContent taggedContent = document.TaggedContent;

// Установить заголовок и язык документа
taggedContent.SetTitle("Tagged Pdf Document");
taggedContent.SetLanguage("en-US");

// Получить корневой структурный элемент
StructureElement rootElement = taggedContent.RootElement;

HeaderElement h1 = taggedContent.CreateHeaderElement(1);
HeaderElement h2 = taggedContent.CreateHeaderElement(2);
HeaderElement h3 = taggedContent.CreateHeaderElement(3);
HeaderElement h4 = taggedContent.CreateHeaderElement(4);
HeaderElement h5 = taggedContent.CreateHeaderElement(5);
HeaderElement h6 = taggedContent.CreateHeaderElement(6);
rootElement.AppendChild(h1);
rootElement.AppendChild(h2);
rootElement.AppendChild(h3);
rootElement.AppendChild(h4);
rootElement.AppendChild(h5);
rootElement.AppendChild(h6);

SpanElement spanH11 = taggedContent.CreateSpanElement();
spanH11.SetText("H1. ");
h1.AppendChild(spanH11);
SpanElement spanH12 = taggedContent.CreateSpanElement();
spanH12.SetText("Заголовок уровня 1");
h1.AppendChild(spanH12);

SpanElement spanH21 = taggedContent.CreateSpanElement();
spanH21.SetText("H2. ");
h2.AppendChild(spanH21);
SpanElement spanH22 = taggedContent.CreateSpanElement();
spanH22.SetText("Заголовок уровня 2");
h2.AppendChild(spanH22);

SpanElement spanH31 = taggedContent.CreateSpanElement();
spanH31.SetText("H3. ");
h3.AppendChild(spanH31);
SpanElement spanH32 = taggedContent.CreateSpanElement();
spanH32.SetText("Заголовок уровня 3");
h3.AppendChild(spanH32);

SpanElement spanH41 = taggedContent.CreateSpanElement();
spanH41.SetText("H4. ");
h4.AppendChild(spanH41);
SpanElement spanH42 = taggedContent.CreateSpanElement();
spanH42.SetText("Заголовок уровня 4");
h4.AppendChild(spanH42);

SpanElement spanH51 = taggedContent.CreateSpanElement();
spanH51.SetText("H5. ");
h5.AppendChild(spanH51);
SpanElement spanH52 = taggedContent.CreateSpanElement();
spanH52.SetText("Заголовок уровня 5");
h5.AppendChild(spanH52);

SpanElement spanH61 = taggedContent.CreateSpanElement();
spanH61.SetText("H6. ");
h6.AppendChild(spanH61);
SpanElement spanH62 = taggedContent.CreateSpanElement();
spanH62.SetText("Заголовок уровня 6");
h6.AppendChild(spanH62);

ParagraphElement p = taggedContent.CreateParagraphElement();
p.SetText("P. ");
rootElement.AppendChild(p);
SpanElement span1 = taggedContent.CreateSpanElement();
span1.SetText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. ");
p.AppendChild(span1);
SpanElement span2 = taggedContent.CreateSpanElement();
span2.SetText("Aenean nec lectus ac sem faucibus imperdiet. ");
p.AppendChild(span2);
SpanElement span3 = taggedContent.CreateSpanElement();
span3.SetText("Sed ut erat ac magna ullamcorper hendrerit. ");
p.AppendChild(span3);
SpanElement span4 = taggedContent.CreateSpanElement();
span4.SetText("Cras pellentesque libero semper, gravida magna sed, luctus leo. ");
p.AppendChild(span4);
SpanElement span5 = taggedContent.CreateSpanElement();
span5.SetText("Fusce lectus odio, laoreet nec ullamcorper ut, molestie eu elit. ");
p.AppendChild(span5);
SpanElement span6 = taggedContent.CreateSpanElement();
span6.SetText("Interdum et malesuada fames ac ante ipsum primis in faucibus. ");
p.AppendChild(span6);
SpanElement span7 = taggedContent.CreateSpanElement();
span7.SetText("Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat sem tristique eget. ");
p.AppendChild(span7);
SpanElement span8 = taggedContent.CreateSpanElement();
span8.SetText("Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper pellentesque justo rhoncus accumsan. ");
p.AppendChild(span8);
SpanElement span9 = taggedContent.CreateSpanElement();
span9.SetText("Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus ac iaculis eget, tempus et magna. Sed non consectetur elit. ");
p.AppendChild(span9);
SpanElement span10 = taggedContent.CreateSpanElement();
span10.SetText("Sed vulputate, quam sed lacinia luctus, ipsum nibh fringilla purus, vitae posuere risus odio id massa. Cras sed venenatis lacus.");
p.AppendChild(span10);

// Сохранить тегированный PDF документ
document.Save(dataDir + "InlineStructureElements.pdf");
```
## Установка пользовательского имени тега

Для установки пользовательского имени тега элементов в Tagged PDF Document, Aspose.PDF предлагает метод [SetTag](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structureelement/methods/settag) класса StructureElement. Следующий фрагмент кода показывает, как установить пользовательское имя тега:

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Создание Pdf документа
Document document = new Document();

// Получение контента для работы с TaggedPdf
ITaggedContent taggedContent = document.TaggedContent;

// Установка заголовка и языка для документа
taggedContent.SetTitle("Tagged Pdf Document");
taggedContent.SetLanguage("en-US");

// Создание элементов логической структуры
SectElement sect = taggedContent.CreateSectElement();
taggedContent.RootElement.AppendChild(sect);

ParagraphElement p1 = taggedContent.CreateParagraphElement();
ParagraphElement p2 = taggedContent.CreateParagraphElement();
ParagraphElement p3 = taggedContent.CreateParagraphElement();
ParagraphElement p4 = taggedContent.CreateParagraphElement();

p1.SetText("P1. ");
p2.SetText("P2. ");
p3.SetText("P3. ");
p4.SetText("P4. ");

p1.SetTag("P1");
p2.SetTag("Para");
p3.SetTag("Para");
p4.SetTag("Paragraph");

sect.AppendChild(p1);
sect.AppendChild(p2);
sect.AppendChild(p3);
sect.AppendChild(p4);

SpanElement span1 = taggedContent.CreateSpanElement();
SpanElement span2 = taggedContent.CreateSpanElement();
SpanElement span3 = taggedContent.CreateSpanElement();
SpanElement span4 = taggedContent.CreateSpanElement();

span1.SetText("Span 1.");
span2.SetText("Span 2.");
span3.SetText("Span 3.");
span4.SetText("Span 4.");

span1.SetTag("SPAN");
span2.SetTag("Sp");
span3.SetTag("Sp");
span4.SetTag("TheSpan");

p1.AppendChild(span1);
p2.AppendChild(span2);
p3.AppendChild(span3);
p4.AppendChild(span4);

// Сохранение Tagged Pdf документа
document.Save(dataDir + "CustomTag.pdf");
```
## Добавление структурного элемента в элементы

**Эта функция поддерживается версией 19.4 или выше.**

Для установки структурных элементов связи в Тегированный PDF документ, Aspose.PDF предлагает метод [CreateLinkElement](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent/methods/createlinkelement) интерфейса [ITaggedContent](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent). Следующий фрагмент кода показывает, как установить структурные элементы в абзац с текстом Тегированного PDF документа:

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
string outFile = dataDir + "LinkStructureElements_Output.pdf";
string logFile = dataDir + "46035_log.xml";
string imgFile = dataDir + "google-icon-512.png";

// Создание документа и получение Тегированного содержимого PDF
Document document = new Document();
ITaggedContent taggedContent = document.TaggedContent;


// Установка заголовка и языка документа
taggedContent.SetTitle("Пример элементов связи");
taggedContent.SetLanguage("en-US");

// Получение корневого структурного элемента (структурный элемент документа)
StructureElement rootElement = taggedContent.RootElement;


ParagraphElement p1 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p1);
LinkElement link1 = taggedContent.CreateLinkElement();
p1.AppendChild(link1);
link1.Hyperlink = new WebHyperlink("http://google.com");
link1.SetText("Google");
link1.AlternateDescriptions = "Ссылка на Google";


ParagraphElement p2 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p2);
LinkElement link2 = taggedContent.CreateLinkElement();
p2.AppendChild(link2);
link2.Hyperlink = new WebHyperlink("http://google.com");
SpanElement span2 = taggedContent.CreateSpanElement();
span2.SetText("Google");
link2.AppendChild(span2);
link2.AlternateDescriptions = "Ссылка на Google";


ParagraphElement p3 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p3);
LinkElement link3 = taggedContent.CreateLinkElement();
p3.AppendChild(link3);
link3.Hyperlink = new WebHyperlink("http://google.com");
SpanElement span31 = taggedContent.CreateSpanElement();
span31.SetText("G");
SpanElement span32 = taggedContent.CreateSpanElement();
span32.SetText("oogle");
link3.AppendChild(span31);
link3.SetText("-");
link3.AppendChild(span32);
link3.AlternateDescriptions = "Ссылка на Google";


ParagraphElement p4 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p4);
LinkElement link4 = taggedContent.CreateLinkElement();
p4.AppendChild(link4);
link4.Hyperlink = new WebHyperlink("http://google.com");
link4.SetText("Многострочная ссылка: Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google");
link4.AlternateDescriptions = "Ссылка на Google (многострочная)";


ParagraphElement p5 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p5);
LinkElement link5 = taggedContent.CreateLinkElement();
p5.AppendChild(link5);
link5.Hyperlink = new WebHyperlink("http://google.com");
FigureElement figure5 = taggedContent.CreateFigureElement();
figure5.SetImage(imgFile, 1200);
figure5.AlternativeText = "Иконка Google";
StructureAttributes linkLayoutAttributes = link5.Attributes.GetAttributes(AttributeOwnerStandard.Layout);
StructureAttribute placementAttribute = new StructureAttribute(AttributeKey.Placement);
placementAttribute.SetNameValue(AttributeName.Placement_Block);
linkLayoutAttributes.SetAttribute(placementAttribute);
link5.AppendChild(figure5);
link5.AlternateDescriptions = "Ссылка на Google";


// Сохранение Тегированного PDF документа
document.Save(outFile);

// Проверка соответствия PDF/UA
document = new Document(outFile);
bool isPdfUaCompliance = document.Validate(logFile, PdfFormat.PDF_UA_1);
Console.WriteLine(String.Format("Соответствие PDF/UA: {0}", isPdfUaCompliance));
```
## Установка элемента структуры ссылки

**Эта функция поддерживается версией 19.4 или выше.**

Aspose.PDF для .NET API также позволяет добавлять элементы структуры ссылок. Следующий фрагмент кода показывает, как добавить элемент структуры ссылки в тегированный PDF документ:

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по адресу https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
string outFile = dataDir + "AddStructureElementIntoElement_Output.pdf";
string logFile = dataDir + "46144_log.xml";

// Создание документа и получение тегированного содержимого PDF
Document document = new Document();
ITaggedContent taggedContent = document.TaggedContent;

// Установка заголовка и языка документа
taggedContent.SetTitle("Пример текстовых элементов");
taggedContent.SetLanguage("en-US");

// Получение корневого структурного элемента (элемент структуры документа)
StructureElement rootElement = taggedContent.RootElement;

ParagraphElement p1 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p1);
SpanElement span11 = taggedContent.CreateSpanElement();
span11.SetText("Span_11");
SpanElement span12 = taggedContent.CreateSpanElement();
span12.SetText(" и Span_12.");
p1.SetText("Параграф с ");
p1.AppendChild(span11);
p1.AppendChild(span12);

ParagraphElement p2 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p2);
SpanElement span21 = taggedContent.CreateSpanElement();
span21.SetText("Span_21");
SpanElement span22 = taggedContent.CreateSpanElement();
span22.SetText("Span_22.");
p2.AppendChild(span21);
p2.SetText(" и ");
p2.AppendChild(span22);

ParagraphElement p3 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p3);
SpanElement span31 = taggedContent.CreateSpanElement();
span31.SetText("Span_31");
SpanElement span32 = taggedContent.CreateSpanElement();
span32.SetText(" и Span_32");
p3.AppendChild(span31);
p3.AppendChild(span32);
p3.SetText(".");

ParagraphElement p4 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p4);
SpanElement span41 = taggedContent.CreateSpanElement();
SpanElement span411 = taggedContent.CreateSpanElement();
span411.SetText("Span_411, ");
span41.SetText("Span_41, ");
span41.AppendChild(span411);
SpanElement span42 = taggedContent.CreateSpanElement();
SpanElement span421 = taggedContent.CreateSpanElement();
span421.SetText("Span 421 и ");
span42.AppendChild(span421);
span42.SetText("Span_42");
p4.AppendChild(span41);
p4.AppendChild(span42);
p4.SetText(".");

// Сохранение тегированного PDF документа
document.Save(outFile);

// Проверка соответствия PDF/UA
document = new Document(outFile);
bool isPdfUaCompliance = document.Validate(logFile, PdfFormat.PDF_UA_1);
Console.WriteLine(String.Format("Соответствие PDF/UA: {0}", isPdfUaCompliance));
```
## Установка элемента структуры заметки

Aspose.PDF для .NET API также позволяет добавлять [NoteElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/noteelement) в тегированный PDF-документ. Следующий пример кода показывает, как добавить элемент заметки в тегированный PDF-документ:

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
string outFile = dataDir + "45929_doc.pdf";
string logFile = dataDir + "45929_log.xml";

// Создание документа PDF
Document document = new Document();
ITaggedContent taggedContent = document.TaggedContent;

taggedContent.SetTitle("Пример с элементами заметок");
taggedContent.SetLanguage("en-US");

// Добавление элемента абзаца
ParagraphElement paragraph = taggedContent.CreateParagraphElement();
taggedContent.RootElement.AppendChild(paragraph);

// Добавление NoteElement
NoteElement note1 = taggedContent.CreateNoteElement();
paragraph.AppendChild(note1);
note1.SetText("Заметка с автоматически генерируемым ID. ");

// Добавление NoteElement
NoteElement note2 = taggedContent.CreateNoteElement();
paragraph.AppendChild(note2);
note2.SetText("Заметка с ID = 'note_002'. ");
note2.SetId("note_002");

// Добавление NoteElement
NoteElement note3 = taggedContent.CreateNoteElement();
paragraph.AppendChild(note3);
note3.SetText("Заметка с ID = 'note_003'. ");
note3.SetId("note_003");

// Должно вызвать исключение - Aspose.Pdf.Tagged.TaggedException : Структурный элемент с ID='note_002' уже существует
//note3.SetId("note_002");

// Результирующий документ не соответствует PDF/UA, если использовать ClearId() для элемента структуры заметки
//note3.ClearId();


// Сохранение тегированного документа PDF
document.Save(outFile);

// Проверка соответствия PDF/UA
document = new Document(outFile);
bool isPdfUaCompliance = document.Validate(logFile, PdfFormat.PDF_UA_1);
Console.WriteLine(String.Format("Соответствие PDF/UA: {0}", isPdfUaCompliance));
```
## Установка языка и заголовка

**Эта функция поддерживается начиная с версии 19.6.**

Aspose.PDF для .NET API также позволяет устанавливать язык и заголовок для документа в соответствии со спецификацией PDF/UA. Язык может быть установлен как для всего документа, так и для его отдельных структурных элементов. Следующий код показывает, как установить язык и заголовок в тегированном PDF-документе:

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
Document document = new Document();
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Получить TaggedContent
Tagged.ITaggedContent taggedContent = document.TaggedContent;

// Установить заголовок и язык
taggedContent.SetTitle("Пример тегированного документа");
taggedContent.SetLanguage("en-US");

// Заголовок (en-US, унаследован от документа)
LogicalStructure.HeaderElement h1 = taggedContent.CreateHeaderElement(1);
h1.SetText("Фраза на разных языках");
taggedContent.RootElement.AppendChild(h1);

// Параграф (английский)
LogicalStructure.ParagraphElement pEN = taggedContent.CreateParagraphElement();
pEN.SetText("Привет, мир!");
pEN.Language = "en-US";
taggedContent.RootElement.AppendChild(pEN);

// Параграф (немецкий)
LogicalStructure.ParagraphElement pDE = taggedContent.CreateParagraphElement();
pDE.SetText("Hallo Welt!");
pDE.Language = "de-DE";
taggedContent.RootElement.AppendChild(pDE);

// Параграф (французский)
LogicalStructure.ParagraphElement pFR = taggedContent.CreateParagraphElement();
pFR.SetText("Bonjour le monde!");
pFR.Language = "fr-FR";
taggedContent.RootElement.AppendChild(pFR);

// Параграф (испанский)
LogicalStructure.ParagraphElement pSP = taggedContent.CreateParagraphElement();
pSP.SetText("¡Hola Mundo!");
pSP.Language = "es-ES";
taggedContent.RootElement.AppendChild(pSP);

// Сохранить тегированный PDF-документ
document.Save(dataDir + "SetupLanguageAndTitle.pdf");
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF для библиотеки .NET",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "продажи",
                "areaServed": "США",
                "availableLanguage": "английский"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "продажи",
                "areaServed": "Великобритания",
                "availableLanguage": "английский"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "продажи",
                "areaServed": "Австралия",
                "availableLanguage": "английский"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Библиотека для работы с PDF для .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
```

