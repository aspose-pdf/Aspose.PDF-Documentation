---
title: Работа с PDF-документами в Qt
type: docs
weight: 130
url: ru/cpp/work-with-pdf-documents-in-qt/
lastmod: "2021-11-01"
---

Qt — это кроссплатформенный фреймворк для разработки приложений, который позволяет создавать различные настольные, мобильные, веб- и встроенные системные приложения. В этой статье мы рассмотрим, как вы можете интегрировать нашу библиотеку C++ PDF для работы с PDF-документами в ваших приложениях Qt.

## Использование Aspose.PDF для C++ в Qt

Чтобы использовать Aspose.PDF для C++ в вашем приложении Qt на операционной системе Windows, скачайте последнюю версию API из раздела [загрузки](https://downloads.aspose.com/pdf/cpp). После загрузки API вы можете использовать любой из следующих вариантов для его использования с Qt.

- Используя Qt Creator
- Используя Visual Studio

Здесь мы продемонстрируем, как интегрировать и использовать Aspose.PDF для C++ в консольном приложении Qt с использованием Qt Creator.

### Создание консольного приложения Qt

{{% alert color="primary" %}}

Эта статья предполагает, что у вас правильно установлена среда разработки Qt и Qt Creator.

{{% /alert %}}

- Откройте Qt Creator и создайте новое *Qt Console Application*.

![todo:image_alt_text](https://blog.aspose.com/wp-content/uploads/sites/2/2020/04/Qt-Console-Application.jpg)

- Выберите опцию QMake из выпадающего списка *Build System*.

![todo:image_alt_text](https://blog.aspose.com/wp-content/uploads/sites/2/2020/04/Qt-Console-Application-QMake.jpg)

- Выберите подходящий комплект и завершите мастер.

На этом этапе у вас должно быть работоспособное приложение Qt Console Application, которое должно компилироваться без проблем.

### Интеграция Aspose.PDF для C++ API с Qt

- Извлеките архив Aspose.PDF для C++, который вы скачали ранее
- Скопируйте папки *Aspose.Pdf.Cpp* и *CodePorting.Native.Cs2Cpp_vc14_20.4* из извлеченного пакета Aspose.PDF для C++ в корень проекта. Ваш проект должен выглядеть, как показано на следующем изображении.

![todo:image_alt_text](work-with-pdf-documents-in-qt_1.png)

- Чтобы добавить пути к папкам lib и include, щелкните правой кнопкой мыши на проекте в левой панели и выберите *Add Library*.

![todo:image_alt_text](https://blog.aspose.com/wp-content/uploads/sites/2/2020/04/Add-Word-Library.jpg)

- Выберите опцию Внешняя библиотека и просмотрите пути, чтобы включить и добавить папки lib по очереди.

![todo:image_alt_text](https://blog.aspose.com/wp-content/uploads/sites/2/2020/04/Add-Word-Library-2.jpg)

- После этого ваш .pro файл проекта будет содержать следующие записи:

![todo:image_alt_text](work-with-pdf-documents-in-qt_2.png)

- Соберите приложение, и интеграция будет завершена.

### Создание PDF документа в Qt

Теперь, когда Aspose.PDF для C++ интегрирован с Qt, мы готовы создать PDF документ с некоторым текстом и сохранить его на диск. Для этого:

- Включите следующие заголовки в main.cpp

```cpp

    #include "Aspose.PDF.Cpp/Document.h"
    #include "Aspose.PDF.Cpp/Page_.h"
    #include "Aspose.PDF.Cpp/PageCollection.h"
    #include "Aspose.PDF.Cpp/Generator/Paragraphs.h"
    #include "Aspose.PDF.Cpp/Text/TextFragment.h"
```


- Вставьте следующий код в основную функцию для создания PDF документа и сохранения на диск

```cpp

    using namespace System;
    using namespace Aspose::Pdf;
    using namespace Aspose::Pdf::Text;
    
    QString text = "Привет мир";
    auto doc = MakeObject<Document>();

    auto pages = doc->get_Pages();

    pages->Add();

    auto page = pages->idx_get(1);

    auto paragraps = page->get_Paragraphs();

    paragraps->Add(MakeObject<TextFragment>(text.toStdU16String().c_str()));

    doc->Save(file_name.toStdU16String().c_str());
```