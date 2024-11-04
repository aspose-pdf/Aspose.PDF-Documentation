---
title: Advanced operations using JavaScript via C++
linktitle: Advanced operations
type: docs
weight: 60
url: /javascript-cpp/advanced-operations/
description: Aspose.PDF for JavaScript via C++ может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Ознакомьтесь со следующим разделом для продвинутых пользователей и разработчиков.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Advanced Operations** - это раздел о том, как программно работать с существующими PDF-файлами, будь то документы, созданные с помощью Aspose.PDF, как обсуждалось в [Basic Operations](/pdf/javascript-cpp/basic-operations/), или PDF, созданные с помощью Adobe Acrobat, Google Docs, Microsoft Office, Open Office или любого другого PDF-продуцента.

## Использование Web Workers

В версии 23.6 добавлена возможность использования Web Workers:

```js
const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
```

Использование Web Workers из JavaScript через C++ позволяет выполнять операции, не блокируя интерфейс, в отдельном потоке работника.

Web Workers — это простой инструмент для выполнения скриптов в фоновом режиме. Это позволяет выполнять задачи, не мешая пользовательскому интерфейсу, в отдельном потоке рабочего процесса.

Вы узнаете различные способы:

- [Работа с документами](/pdf/javascript-cpp/working-with-documents/) - сжимать, разделять и объединять документы и выполнять другие операции с документом в целом.
- [Работа с страницами](/pdf/javascript-cpp/working-with-pages/) - добавлять, перемещать или удалять, обрезать страницы, штампы.
- [Метаданные в PDF](/pdf/javascript-cpp/pdf-file-metadata/) - получать или устанавливать метаданные в документах.
- [Работа с изображениями](/pdf/javascript-cpp/working-with-images/) - вставлять, удалять, извлекать изображения в документе.
- [Навигация и взаимодействие](/pdf/javascript-cpp/navigation-and-interaction/) - работать с действиями, закладками, навигацией по страницам.
- [Аннотации](/pdf/javascript-cpp/annotations/) - Аннотации позволяют пользователям добавлять пользовательский контент на страницы PDF. Вы можете добавлять, удалять и изменять аннотации в PDF-документах.

- [Защита и подпись](/pdf/javascript-cpp/securing-and-signing/) - защищать и подписывать ваш PDF-документ программно.
- [Attachments](/pdf/javascript-cpp/attachments/) - PDF документы могут содержать вложения. Эти вложения могут быть другими PDF документами или любыми другими файлами, такими как аудиофайлы, документы Microsoft Office и т. д. Вы узнаете, как добавлять вложения в PDF, получать информацию о вложении, сохранять его в файл, удалять вложение из PDF программно с помощью JavaScript.