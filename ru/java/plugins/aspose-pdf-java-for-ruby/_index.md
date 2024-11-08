---
title: Aspose.PDF Java для Ruby
type: docs
weight: 20
url: /ru/java/aspose-pdf-java-for-ruby/
lastmod: "2021-06-05"
---

## Введение

### Rjb - Ruby Java Bridge

RJB — это программа-мост, которая соединяет Ruby и Java с помощью Java Native Interface. Rake + Rjb — это более мощный и полезный инструмент сборки, чем и Maven, и Ant. Вы можете тестировать свой класс бизнес-логики Java с помощью mock из Rjb. Это помогает мигрировать объект модели Struts в ваше RoR-приложение. Но будьте осторожны при создании приложения Swing, Ruby (и Rjb) не учитывает обработку нативных потоков JVM.

### Aspose.PDF для Java

Aspose.PDF для Java — это компонент для создания PDF-документов, который позволяет вашим Java-приложениям читать, записывать и обрабатывать PDF-документы без использования Adobe Acrobat.

Aspose.PDF для Java — это компонент с доступной ценой, который предлагает невероятное богатство функций, включая: варианты сжатия PDF, создание и обработку таблиц, поддержку графиков, функции работы с изображениями, расширенные функции гиперссылок, расширенные средства управления безопасностью и обработку пользовательских шрифтов.

Aspose.PDF for Java позволяет создавать PDF-файлы непосредственно через предоставленный API и XML-шаблоны. Использование Aspose.PDF for Java также позволит вам добавить возможности PDF в ваши приложения в кратчайшие сроки.

### Aspose.PDF Java для Ruby

Проект Aspose.PDF Java для Ruby показывает, как различные задачи могут быть выполнены с использованием Aspose.PDF Java API в Ruby. Этот проект нацелен на предоставление полезных примеров для разработчиков Ruby, которые хотят использовать Aspose.PDF для Java в своих Ruby проектах с использованием Rjb (Ruby Java Bridge).

## Системные требования и поддерживаемые платформы

### Системные требования

Следующие системные требования для использования Aspose.PDF Java для Ruby:

- Настроен Rjb Gem
- Загружен компонент Aspose.PDF

### Поддерживаемые платформы

Следующие платформы поддерживаются:

- Ruby 2.2.x или выше и соответствующий DevKit.
- Java 1.5 или выше

## Загрузки

### Загрузка необходимых библиотек

Загрузите необходимые библиотеки, упомянутые ниже. Они необходимы для выполнения примеров Aspose.PDF Java для Ruby.

- [Компонент Aspose.PDF для Java](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-pdf)

### Скачать примеры с сайтов социального кодирования

Следующие выпуски работающих примеров доступны для скачивания на указанных ниже сайтах социального кодирования:

GitHub

- [Aspose.PDF Java для Ruby](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_Ruby)

## Установка и использование

### Установка

Установить Aspose.PDF Java для Ruby gem очень просто и легко, пожалуйста, выполните следующие простые шаги:

1. Выполните следующую команду.

{{< highlight java >}}

 $ gem install aspose-pdfjava

{{< /highlight >}}

1. Скачайте необходимый компонент Aspose.PDF для Java по следующей ссылке.
   <https://downloads.aspose.com/pdf/java>
1. Создайте папку "jars" в корне Aspose.PDF Java для Ruby gem и скопируйте в нее скачанный компонент.

### Использование

Подключите необходимые файлы для работы с примером helloworld.

{{< highlight java >}}

 require File.dirname(File.dirname(File.dirname(__FILE__))) + '/lib/aspose-pdfjava'

include Asposepdfjava

include Asposepdfjava::HelloWorld


initialize_aspose_pdf

{{< /highlight >}}

Давайте разберем приведенный выше код.

1. Первая строка обеспечивает загрузку и доступность aspose pdf.
1. Включите файлы, необходимые для доступа к aspose pdf.
1. Инициализируйте библиотеки. Классы aspose JAVA загружаются из пути, указанного в файле aspose.yml.

## Поддержка, расширение и вклад

### Поддержка

С первых дней Aspose мы знали, что просто предоставлять нашим клиентам хорошие продукты будет недостаточно. Нам также нужно было обеспечить хороший сервис. Мы сами разработчики и понимаем, насколько это раздражает, когда техническая проблема или ошибка в программном обеспечении мешает вам делать то, что вам нужно. Мы здесь, чтобы решать проблемы, а не создавать их.

Вот почему мы предлагаем бесплатную поддержку. Любой, кто использует наш продукт, будь то покупатель или пользователь пробной версии, заслуживает нашего полного внимания и уважения.

Вы можете зарегистрировать любые проблемы или предложения, связанные с Aspose.PDF Java для Ruby, используя любую из следующих платформ:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/issues)

### Расширение и Вклад

Aspose.PDF Java для Ruby является открытым исходным кодом, и его исходный код доступен на основных социальных сайтах кодирования, перечисленных ниже. Разработчики призываются загружать исходный код и вносить свой вклад, предлагая или добавляя новые функции или улучшая существующие, чтобы другие также могли извлечь из этого пользу.

### Исходный код

Вы можете получить последний исходный код из одного из следующих мест:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_Ruby)

## Примеры кода

Этот раздел включает следующие темы:

- [Скачать и настроить Aspose.Pdf в Ruby](/pdf/ru/java/download-and-configure-aspose-pdf-in-ruby/)
- [Руководство для программистов Ruby](/pdf/ru/java/ruby-programmers-guide/)
  - [Работа с объектом документа в Ruby](/pdf/ru/java/working-with-document-object-in-ruby/)
    - [Добавление JavaScript в Ruby](/pdf/ru/java/adding-javascript-in-ruby/)
    - [Добавить слои в PDF файл в Ruby](/pdf/ru/java/add-layers-to-pdf-file-in-ruby/)

    - [Добавить Оглавление в существующий PDF в Ruby](/pdf/ru/java/add-toc-to-existing-pdf-in-ruby/)
- [Получить свойства окна документа и отображения страницы в Ruby](/pdf/ru/java/get-document-window-and-page-display-properties-in-ruby/)
- [Получить информацию о PDF файле в Ruby](/pdf/ru/java/get-pdf-file-information-in-ruby/)
- [Получить XMP метаданные из PDF файла в Ruby](/pdf/ru/java/get-xmp-metadata-from-pdf-file-in-ruby/)
- [Оптимизировать PDF документ для веба в Ruby](/pdf/ru/java/optimize-pdf-document-for-the-web-in-ruby/)
- [Оптимизировать размер PDF файла в Ruby](/pdf/ru/java/optimize-pdf-file-size-in-ruby/)
- [Удалить метаданные из PDF в Ruby](/pdf/ru/java/remove-metadata-from-pdf-in-ruby/)
- [Установить свойства окна документа и отображения страницы в Ruby](/pdf/ru/java/set-document-window-and-page-display-properties-in-ruby/)
- [Установить срок действия PDF в Ruby](/pdf/ru/java/set-pdf-expiration-in-ruby/)
- [Установить информацию о PDF файле в Ruby](/pdf/ru/java/set-pdf-file-information-in-ruby/)
- [Работа с страницами в Ruby](/pdf/ru/java/working-with-pages-in-ruby/)

- [Объединить PDF файлы в Ruby](/pdf/ru/java/concatenate-pdf-files-in-ruby/)
- [Удалить определенную страницу из PDF файла на Ruby](/pdf/ru/java/delete-a-particular-page-from-the-pdf-file-in-ruby/)
- [Получить определенную страницу в PDF файле на Ruby](/pdf/ru/java/get-a-particular-page-in-a-pdf-file-in-ruby/)
- [Получить количество страниц PDF на Ruby](/pdf/ru/java/get-page-count-of-pdf-in-ruby/)
- [Получить свойства страницы на Ruby](/pdf/ru/java/get-page-properties-in-ruby/)
- [Вставить пустую страницу в конец PDF файла на Ruby](/pdf/ru/java/insert-an-empty-page-at-end-of-pdf-file-in-ruby/)
- [Вставить пустую страницу в PDF файл на Ruby](/pdf/ru/java/insert-an-empty-page-into-a-pdf-file-in-ruby/)
- [Разделить PDF файл на отдельные страницы на Ruby](/pdf/ru/java/split-pdf-file-into-individual-pages-in-ruby/)
- [Обновить размеры страницы на Ruby](/pdf/ru/java/update-page-dimensions-in-ruby/)
- [Работа с текстом на Ruby](/pdf/ru/java/working-with-text-in-ruby/)
  - [Добавить HTML строку с использованием DOM на Ruby](/pdf/ru/java/add-html-string-using-dom-in-ruby/)
  - [Добавить текст в существующий PDF файл на Ruby](/pdf/ru/java/add-text-to-an-existing-pdf-file-in-ruby/)
- [Извлечение текста со всех страниц PDF-документа на Ruby](/pdf/ru/java/extract-text-from-all-the-pages-of-a-pdf-document-in-ruby/)
  - [Работа с преобразованием документов на Ruby](/pdf/ru/java/working-with-document-conversion-in-ruby/)
    - [Преобразование HTML в формат PDF на Ruby](/pdf/ru/java/convert-html-to-pdf-format-in-ruby/)
    - [Преобразование страниц PDF в изображения на Ruby](/pdf/ru/java/convert-pdf-pages-to-images-in-ruby/)
    - [Преобразование PDF в формат DOC или DOCX на Ruby](/pdf/ru/java/convert-pdf-to-doc-or-docx-format-in-ruby/)
    - [Преобразование PDF в Excel Workbook на Ruby](/pdf/ru/java/convert-pdf-to-excel-workbook-in-ruby/)
    - [Преобразование PDF в формат SVG на Ruby](/pdf/ru/java/convert-pdf-to-svg-format-in-ruby/)
    - [Преобразование файла SVG в формат PDF на Ruby](/pdf/ru/java/convert-svg-file-to-pdf-format-in-ruby/)
- [Поддержка, расширение и вклад в Aspose.Pdf на Ruby](/pdf/ru/java/support-extend-and-contribute-to-aspose-pdf-in-ruby/)