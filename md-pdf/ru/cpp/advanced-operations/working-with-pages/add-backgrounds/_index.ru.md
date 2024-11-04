---
title: Добавление фона в PDF с использованием C++
linktitle: Добавление фонов
type: docs
weight: 110
url: /cpp/add-backgrounds/
descriptions: Добавьте фоновое изображение в ваш PDF файл с помощью C++. Используйте объект BackgroundArtifact.
lastmod: "2021-12-03"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Добавление фона в PDF файлы помогает улучшить общую читаемость документа. Содержание PDF становится более привлекательным, и читатели обратят внимание, если у вашего документа хороший внешний вид. Фон также может использоваться для выделения ключевых моментов PDF.

Фоновые изображения могут использоваться для добавления водяных знаков или других тонких элементов дизайна в документы. В Aspose.PDF для C++ каждый PDF документ представляет собой коллекцию страниц, и каждая страница содержит коллекцию артефактов. Класс [BackgroundArtifact](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.background_artifact) может использоваться для добавления фонового изображения к объекту страницы.

Следующий фрагмент кода показывает, как добавить фоновое изображение на страницы PDF, используя объект BackgroundArtifact с C++.

```cpp
void WorkingWithPages::AddBackgrounds()
{
    String _dataDir("C:\\Samples\\");

    // Создать новый объект Document
    auto document = MakeObject<Document>();

    // Добавить новую страницу в объект документа
    auto page = document->get_Pages()->Add();

    // Создать объект Background Artifact
    auto background = MakeObject<BackgroundArtifact>();

    // Указать изображение для объекта backgroundartifact
    background->set_BackgroundImage(System::IO::File::OpenRead(_dataDir + u"background.png"));

    // Добавить backgroundartifact в коллекцию артефактов страницы
    page->get_Artifacts()->Add(background);

    // Сохранить документ
    document->Save(_dataDir + u"ImageAsBackground_out.pdf");
}
```