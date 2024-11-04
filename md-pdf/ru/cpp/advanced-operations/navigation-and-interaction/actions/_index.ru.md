---
title: Работа с Действиями в PDF 
linktitle: Действия
type: docs
weight: 20
url: /cpp/actions/
description: Этот раздел объясняет, как программно добавлять действия в документ и поля формы с помощью C++.
lastmod: "2022-01-25"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Добавление Гиперссылки в PDF Файл

PDF документы — отличный способ делиться информацией. Они легки для чтения, редактирования и распространения. Однако создание ссылок в PDF документе может быть сложной задачей. Давайте покажем, как это сделать.

Можно добавлять гиперссылки в PDF файлы, чтобы позволить читателям переходить к другой части PDF или к внешнему контенту.

Например, вы можете захотеть добавить кликабельное оглавление к своим электронным книгам, ссылаться на внешние ресурсы для вашей статьи или быстро перенаправить читателя на другую страницу веб-сайта для получения дополнительной информации по теме.

Чтобы создать гиперссылки в несколько кликов, выполните следующие простые шаги:

1. Создайте объект класса [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Получите класс [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page), к которому вы хотите добавить ссылку.
1. Создайте объект [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) с использованием объектов Page и [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.rectangle/). Объект Rectangle используется для указания места на странице, где должна быть добавлена ссылка.
1. Установите свойство Action в объект [GoToURIAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.go_to_u_r_i_action), который указывает местоположение удаленного URI.
1. Чтобы отобразить текст гиперссылки, добавьте строку текста в место, аналогичное тому, где размещен объект [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation).
1. Чтобы добавить свободный текст:

- Создайте экземпляр объекта [FreeTextAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.free_text_annotation).  Он также принимает объекты Page и Rectangle в качестве аргумента, поэтому можно предоставить те же значения, которые указаны в конструкторе LinkAnnotation.
- Используя свойство Contents объекта [FreeTextAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.free_text_annotation), укажите строку, которая должна отображаться в выходном PDF.
- При желании установите ширину границы объектов [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) и FreeTextAnnotation на 0, чтобы они не отображались в PDF-документе.
- После того, как объекты [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) и [FreeTextAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.free_text_annotation) были определены, добавьте эти ссылки в коллекцию Annotations объекта [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page).

- Наконец, сохраните обновленный PDF, используя метод Save объекта [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
Следующий фрагмент кода показывает, как добавить гиперссылку в PDF файл.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddHyperlinkInPDFFile() {

String _dataDir("C:\\Samples\\");

// Открыть документ

auto document = MakeObject<Document>(_dataDir + u"AddHyperlink.pdf");

// Создать ссылку

auto page = document->get_Pages()->idx_get(1);

// Создать объект аннотации ссылки

auto link = MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, MakeObject<Rectangle>(100, 100, 300, 300));

// Создать объект границы для LinkAnnotation

auto border = MakeObject<Aspose::Pdf::Annotations::Border>(link);

// Установить значение ширины границы как 0

border->set_Width(0);

// Установить границу для LinkAnnotation

link->set_Border(border);

// Указать тип ссылки как удаленный URI

link->set_Action(MakeObject<Aspose::Pdf::Annotations::GoToURIAction>("www.aspose.com"));

// Добавить аннотацию ссылки в коллекцию аннотаций первой страницы PDF файла

page->get_Annotations()->Add(link);


// Создать аннотацию свободного текста

auto textAnnotation = MakeObject<Aspose::Pdf::Annotations::FreeTextAnnotation>(


page,


MakeObject<Rectangle>(100, 100, 300, 300),


MakeObject<Aspose::Pdf::Annotations::DefaultAppearance>(



FontRepository::FindFont(u"TimesNewRoman"), 10, Color::get_Blue()));


// Строка, добавляемая в виде свободного текста

textAnnotation->set_Contents(u"Link to Aspose website");

// Установить границу для аннотации свободного текста

textAnnotation->set_Border(border);

// Добавить аннотацию свободного текста в коллекцию аннотаций первой страницы документа

page->get_Annotations()->Add(textAnnotation);


// Сохранить обновленный документ

document->Save(_dataDir + u"AddHyperlink_out.pdf");

}
```

## Создание гиперссылки на страницы в том же PDF

Aspose.PDF для C++ предоставляет отличную возможность для создания PDF, а также его обработки. Он также предлагает возможность добавлять ссылки на страницы PDF, и ссылка может вести либо на страницы в другом PDF файле, веб-URL, ссылку для запуска приложения или даже ссылку на страницы в том же PDF файле. Для добавления локальных гиперссылок (ссылок на страницы в том же PDF файле) в пространство имен Aspose.PDF добавлен класс с именем [LocalHyperlink](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.local_hyperlink), и этот класс имеет свойство с именем TargetPageNumber, которое используется для указания целевой/назначенной страницы для гиперссылки.

Для добавления локальной гиперссылки нам нужно создать TextFragment, чтобы ссылка могла быть связана с TextFragment. Класс [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.te_x_fragment) имеет свойство с именем Hyperlink, которое используется для связывания экземпляра LocalHyperlink. Следующий фрагмент кода показывает шаги для выполнения этого требования.

```cpp
void CreateHyperlinkToPagesInSamePDF() {

String _dataDir("C:\\Samples\\");


// Создать экземпляр документа

auto document = MakeObject<Document>();


// Добавить страницу в коллекцию страниц PDF файла

auto page = document->get_Pages()->Add();


// Создать экземпляр текстового фрагмента

auto text = MakeObject<TextFragment>(u"link page number test to page 2");


// Создать экземпляр локальной гиперссылки

auto link = MakeObject<LocalHyperlink>();


// Установить целевую страницу для экземпляра ссылки

link->set_TargetPageNumber(2);


// Установить гиперссылку для TextFragment

text->set_Hyperlink(link);


// Добавить текст в коллекцию абзацев страницы

page->get_Paragraphs()->Add(text);


// Создать новый экземпляр TextFragment

text = new TextFragment(u"link page number test to page 1");


// TextFragment должен быть добавлен на новую страницу

text->set_IsInNewPage(true);


// Создать другой экземпляр локальной гиперссылки

link = new LocalHyperlink();


// Установить целевую страницу для второй гиперссылки

link->set_TargetPageNumber(1);


// Установить ссылку для второго TextFragment

text->set_Hyperlink(link);


// Добавить текст в коллекцию абзацев объекта страницы

page->get_Paragraphs()->Add(text);


// Сохранить обновленный документ

document->Save(_dataDir + u"CreateLocalHyperlink_out.pdf");
}
```
## Получить URL назначения гиперссылки в PDF

Ссылки представлены в виде аннотаций в PDF файле, и их можно добавлять, обновлять или удалять. Aspose.PDF для C++ также поддерживает получение назначения (URL) гиперссылки в PDF файле.

Чтобы получить URL ссылки:

1. Создайте объект [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Получите [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page), с которой вы хотите извлечь ссылки.
1. Используйте класс [AnnotationSelector](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/), чтобы извлечь все объекты [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation) с указанной страницы.
1. Передайте объект [AnnotationSelector](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/) методу Accept объекта [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page).
1. Получите все выбранные аннотации ссылок в объект IList с помощью свойства Selected объекта [AnnotationSelector](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/).

1. Наконец, извлеките действие LinkAnnotation как GoToURIAction.

Следующий фрагмент кода показывает, как получить назначения гиперссылок (URL) из PDF-файла.

```cpp
void GetPDFHyperlinkDestination() {

String _dataDir("C:\\Samples\\");


auto document = new Document(_dataDir + u"Aspose-app-list.pdf");

// Извлечение действий

auto page = document->get_Pages()->idx_get(1);


auto selector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(


MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, Rectangle::get_Trivial()));

page->Accept(selector);


auto list = selector->get_Selected();

// Перебор отдельных элементов внутри списка

if (list->get_Count() == 0)


Console::WriteLine(u"Гиперссылки не найдены...");

else {


// Перебор всех закладок


for (auto annot : list) {



auto la = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(annot);



if (la != nullptr) {




auto action = System::DynamicCast<Aspose::Pdf::Annotations::GoToURIAction>(la->get_Action());




// Печать URL назначения




Console::WriteLine(u"Назначение: " + action->get_URI());



}


}

} // конец else
}
```
## Получение текста гиперссылки

Гиперссылка состоит из двух частей: текста, который отображается в документе, и URL назначения. В некоторых случаях нам нужен именно текст, а не URL.

Текст и аннотации/действия в PDF-файле представлены разными сущностями. Текст на странице — это просто набор слов и символов, в то время как аннотации добавляют некоторую интерактивность, такую как та, что присуща гиперссылке.

Чтобы найти URL-содержимое, вам нужно работать как с аннотацией, так и с текстом. Объект [Annotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation) сам по себе не имеет текста, но находится под текстом на странице. Итак, чтобы получить текст, аннотация дает границы URL, а объект Text дает содержимое URL. Пожалуйста, смотрите следующий фрагмент кода.

```cpp
  void GetHyperlinkText() {

String _dataDir("C:\\Samples\\");

auto document = MakeObject<Document>(_dataDir + u"aspose-app-list.pdf");

// Извлечение действий

auto page = document->get_Pages()->idx_get(1);


for (auto annot : page->get_Annotations()) {


auto la = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(annot);


if (la != nullptr) {



// Печать URL каждой аннотации ссылки



auto action = System::DynamicCast<Aspose::Pdf::Annotations::GoToURIAction>(la->get_Action());



Console::WriteLine(u"URI: " + action->get_URI());




auto absorber = MakeObject<TextAbsorber>();



absorber->get_TextSearchOptions()->set_LimitToPageBounds(true);



absorber->get_TextSearchOptions()->set_Rectangle(annot->get_Rect());



page->Accept(absorber);



String extractedText = absorber->get_Text();



// Печать текста, связанного с гиперссылкой



Console::WriteLine(extractedText);


}

}
}
```

## Удаление действия открытия документа из PDF файла

[Как указать страницу PDF при просмотре документа](#how-to-specify-pdf-page-when-viewing-document) объясняет, как сделать так, чтобы документ открывался на другой странице, а не на первой. При объединении нескольких документов, если в одном или нескольких установлено действие GoTo, вероятно, вы захотите их удалить. Например, если вы объединяете два документа, и во втором установлено действие GoTo, которое переводит вас на вторую страницу, итоговый документ откроется на второй странице второго документа, а не на первой странице объединенного документа. Чтобы избежать этого поведения, удалите команду действия открытия.

Чтобы удалить действие открытия:

1. Установите свойство [OpenAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a24b876bb6bee957feac48ac8031dc28e) объекта [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) в null.
1. Сохраните обновленный PDF, используя метод Save объекта Document.

Следующий фрагмент кода показывает, как удалить действие открытия документа из PDF файла.

```cpp
void RemoveDocumentOpenActionFromPDFFile()
{

String _dataDir("C:\\Samples\\");

// Открыть документ

auto document = new Document(_dataDir + u"RemoveOpenAction.pdf");

// Удалить действие открытия документа

document->set_OpenAction(nullptr);


// Сохранить обновленный документ

document->Save(_dataDir + u"RemoveOpenAction_out.pdf");
}
```

## Как указать страницу PDF при просмотре документа {#how-to-specify-pdf-page-when-viewing-document}

При просмотре PDF-файлов в PDF-просмотрщике, таком как Adobe Reader, файлы обычно открываются на первой странице. Однако можно настроить открытие файла на другой странице.

Класс 'XYZExplicitDestination' позволяет указать страницу в PDF-файле, которую вы хотите открыть. При передаче значения объекта GoToAction в свойство OpenAction класса [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document), документ открывается на странице, указанной в объекте XYZExplicitDestination. В следующем примере кода показано, как указать страницу в качестве действия открытия документа.

```cpp
void HowToSpecifyPDFPageWhenViewingDocument()
{

String _dataDir("C:\\Samples\\");

// Загрузить PDF-файл

auto document = new Document(_dataDir + u"SpecifyPageWhenViewing.pdf");

// Получить экземпляр второй страницы документа

auto page2 = document->get_Pages()->idx_get(2);

// Создать переменную для установки коэффициента масштабирования целевой страницы

double zoom = 1;

// Создать экземпляр GoToAction

auto action = MakeObject<Aspose::Pdf::Annotations::GoToAction>(page2);

// Перейти на 2 страницу

action->set_Destination(MakeObject<Aspose::Pdf::Annotations::XYZExplicitDestination>(page2, 0, page2->get_Rect()->get_Height(), zoom));

// Установить действие открытия документа

document->set_OpenAction(action);

// Сохранить обновленный документ

document->Save(_dataDir + u"goto2page_out.pdf");
}
```