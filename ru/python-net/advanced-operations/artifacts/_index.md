---
title: Работа с PDF-артефактами на Python
linktitle: Работа с PDF-артефактами
type: docs
weight: 170
url: /ru/python-net/artifacts/
description: Добавляйте, проверяйте и удаляйте PDF-артефакты в Python, включая фоны, водяные знаки, колонтитулы и нумерацию Бейтса.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Работа с PDF-артефактами на Python
Abstract: Найдите руководства по добавлению и удалению PDF-артефактов, проверке деталей водяных знаков и подсчету артефактов пагинации по подтипу с помощью Aspose.PDF for Python via .NET.
---

PDF-артефакты помечают элементы страниц, такие как декоративные фоны, текущие колонтитулы и водяные знаки. В помеченном PDF вспомогательные технологии могут пропускать артефакты и фокусироваться на значимом содержимом документа.

## Выбор руководства

### Добавление артефактов

- [Добавление фона](/pdf/ru/python-net/add-backgrounds/)
- [Добавление водяных знаков](/pdf/ru/python-net/add-watermarks/)
- [Добавление нумерации Бейтса](/pdf/ru/python-net/add-bates-numbering/)
- [Добавление колонтитулов](/pdf/ru/python-net/artifacts-header-footer/)

### Просмотр артефактов

- [Подсчёт артефактов по подтипам](/pdf/ru/python-net/counting-artifacts/)
- [Извлечение текста и границ водяных знаков](/pdf/ru/python-net/extract-watermarks/)

### Удаление артефактов

- [Удаление фона](/pdf/ru/python-net/remove-backgrounds/)
- [Удаление водяных знаков](/pdf/ru/python-net/remove-watermarks/)
- [Удаление нумерации Бейтса](/pdf/ru/python-net/remove-bates-numbering/)
- [Удаление колонтитулов](/pdf/ru/python-net/remove-headers-footers/)

## API артефактов

Свойство `artifacts` возвращает коллекцию [`ArtifactCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/) для страницы. Класс [`Artifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/) предоставляет общие свойства для специализированных классов [`BackgroundArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/backgroundartifact/), [`WatermarkArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/watermarkartifact/), [`HeaderArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerartifact/), [`FooterArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/footerartifact/) и [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/).

| Задача | Свойства |
| --- | --- |
| Определить артефакт | Использовать `type` и `subtype` для стандартных классификаций и `custom_type` и `custom_subtype` для пользовательских имён. |
| Просмотрите его содержимое | Использовать `text`, `image`, и `lines` для текста и изображений, или `contents` и `form` для операторов PDF и связанной XForm. |
| Разместите его на странице | Использовать `rectangle` для проверки его границ. Установить `position` для явного размещения или использования `left_margin`, `right_margin`, `top_margin`, `bottom_margin`, `artifact_horizontal_alignment`, и `artifact_vertical_alignment`. Явная позиция переопределяет отступы и выравнивание. |
| Контролируйте его внешний вид | Использовать `rotation`, `opacity` (от 0 до 1), и `text_state`. Установить `is_background` разместить артефакт за содержимым страницы. |
