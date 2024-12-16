---
title: Как запустить другие примеры Aspose.PDF для C++
linktitle: Как запустить другие примеры
type: docs
weight: 50
url: /ru/cpp/how-to-run-other-examples/
description: Эта страница демонстрирует рекомендации, которые будут полезны для выполнения следующих требований перед загрузкой и запуском примеров.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Системные требования

Пожалуйста, убедитесь, что вы соответствуете следующим требованиям перед загрузкой и запуском примеров.

1. Microsoft Visual Studio 2017 или более поздней версии.
1. Менеджер пакетов NuGet установлен в Visual Studio. Убедитесь, что в Visual Studio установлена последняя версия API NuGet. Для получения информации о том, как установить менеджер пакетов NuGet, пожалуйста, посетите <http://docs.nuget.org/ndocs/guides/install-nuget>
1. Перейдите в `Инструменты->Параметры->Менеджер пакетов NuGet->Источники пакетов` и убедитесь, что опция **nuget.org** отмечена
1. Пример проекта использует функцию автоматического восстановления пакетов NuGet, поэтому у вас должно быть активное интернет-соединение. Если на компьютере, где будут выполняться примеры, нет активного интернет-соединения, пожалуйста, ознакомьтесь с [Установкой](/pdf/ru/cpp/installation/) и вручную добавьте ссылку на Aspose.PDF.dll в пример проекта.

## Загрузка с GitHub

Все примеры Aspose.PDF для C++ размещены на [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-C).

- Вы можете либо клонировать репозиторий, используя ваш любимый клиент GitHub, либо скачать ZIP-файл [отсюда](https://codeload.github.com/aspose-pdf/Aspose.PDF-for-C/zip/master).
- Извлеките содержимое ZIP-файла в любую папку на вашем компьютере. Все примеры находятся в папке **Examples**.
- Есть два файла решений Visual Studio, один для консольного приложения, другой — для веб-приложения.
- Проекты созданы в Visual Studio 2013, но файлы решений совместимы с Visual Studio 2010 SP1 и выше.

- Откройте файл решения в Visual Studio и соберите проект.- При первом запуске зависимости будут автоматически загружены через NuGet.
- Папка **Data** в корневой папке **Examples** содержит входные файлы, которые используют примеры на CSharp. Обязательно загрузите папку **Data** вместе с проектом примеров.
- Откройте файл *RunExamples.cs*, все примеры вызываются отсюда.
- Раскомментируйте примеры, которые хотите запустить из проекта.

Пожалуйста, не стесняйтесь обращаться на наши форумы, если у вас возникнут проблемы с настройкой или запуском примеров.

## Участие

Если вы хотите добавить или улучшить пример, мы призываем вас внести вклад в проект. Все примеры и демонстрационные проекты в этом репозитории являются открытым исходным кодом и могут свободно использоваться в ваших собственных приложениях.

Чтобы внести вклад, вы можете сделать форк репозитория, изменить исходный код и создать pull request. Мы рассмотрим изменения и включим их в репозиторий, если они будут полезны.