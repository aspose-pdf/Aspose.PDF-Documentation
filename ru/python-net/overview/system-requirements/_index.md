---
title: Системные требования
linktitle: Системные требования
type: docs
weight: 30
url: /ru/python-net/system-requirements/
description: В этом разделе перечислены поддерживаемые операционные системы, необходимые разработчику для успешной работы с Aspose.PDF for Python.
lastmod: "2025-02-22"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Поддерживаемые операционные системы Aspose.PDF for Python через .NET
Abstract: Aspose.PDF for Python через .NET — это API обработки PDF, предназначенное для разработчиков, позволяющее управлять PDF‑документами без необходимости использовать Microsoft Office или автоматизацию Adobe Acrobat. Он поддерживает разработку 32‑ и 64‑разрядных Python‑приложений на различных операционных системах, включая Windows и Linux, где установлен Python 3.5 или более поздней версии. API совместим с несколькими версиями Windows, от Windows XP до Windows 11, а также с основными дистрибутивами Linux, такими как Ubuntu, OpenSUSE и CentOS. Для систем Linux требуются специфические зависимости, включая библиотеки выполнения GCC‑6, зависимости .NET Core Runtime (сам runtime устанавливать не требуется) и сборка Python с pymalloc для версий 3.5‑3.7. Кроме того, необходима общая библиотека libpython, что может потребовать настройки конфигурации для правильного распознавания пути к библиотеке.
---

## Обзор

Aspose.PDF for Python через .NET — API обработки PDF, позволяющий разработчикам работать с PDF‑документами без необходимости использовать Microsoft Office® или автоматизацию Adobe Acrobat. Aspose.PDF for Python можно использовать для разработки 32‑ и 64‑разрядных Python‑приложений для различных операционных систем (например, Windows и Linux), где установлен Python 3.5 или более поздней версии.

## Поддерживаемые операционные системы

### Windows

- Windows 2003 Server
- Windows 2008 Server
- Windows 2012 Server
- Windows 2012 R2 Server
- Windows 2016 Server
- Windows 2019 Server
- Windows XP
- Windows Vista
- Windows 7
- Windows 8, 8.1
- Windows 10
- Windows 11

### Linux

- Ubuntu
- OpenSUSE
- CentOS
- и другие

## Системные требования для целевого Linux

- Библиотеки выполнения GCC‑6 (или новее).

- Зависимости .NET Core Runtime. Установка самого .NET Core Runtime НЕ требуется.

- Для Python 3.5‑3.7: требуется сборка Python с поддержкой pymalloc. Параметр сборки --with-pymalloc включён по умолчанию. Обычно такая сборка Python помечается суффиксом m в имени файла.

- Общая библиотека libpython. Параметр сборки Python --enable-shared отключён по умолчанию, некоторые дистрибутивы Python не включают общую библиотеку libpython. Для некоторых платформ Linux общую библиотеку libpython можно установить через менеджер пакетов, например: sudo apt-get install libpython3.7. Распространённая проблема заключается в том, что библиотека libpython устанавливается в расположение, отличное от стандартного системного пути для общих библиотек. Проблему можно решить, указав альтернативные пути к библиотекам в параметрах сборки Python при компиляции, либо создав символическую ссылку на файл библиотеки libpython в стандартном системном каталоге общих библиотек. Как правило, имя файла общей библиотеки libpython выглядит как libpythonX.Ym.so.1.0 для Python 3.5‑3.7, или libpythonX.Y.so.1.0 для Python 3.8 и новее (например: libpython3.7m.so.1.0, libpython3.9.so.1.0).



